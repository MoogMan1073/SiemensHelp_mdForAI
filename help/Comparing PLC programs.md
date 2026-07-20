---
title: "Comparing PLC programs"
package: ProgPLCCompareenUS
topics: 23
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Comparing PLC programs

This section contains information on the following topics:

- [Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
- [Comparing blocks](#comparing-blocks)
- [Comparing PLC tags](#comparing-plc-tags-1)
- [Comparing PLC data types](#comparing-plc-data-types)

## Basic information on comparing PLC programs

This section contains information on the following topics:

- [Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
- [Comparison of software units](#comparison-of-software-units)
- [Comparing blocks and PLC data types](#comparing-blocks-and-plc-data-types)
- [Comparing PLC tags](#comparing-plc-tags)
- [Comparison of PLC programs based on checksums](#comparison-of-plc-programs-based-on-checksums)

### Introduction to comparing PLC programs

#### Function

You can compare the following objects of a PLC program in order to detect any differences:

- Code blocks with other code blocks
- Data blocks with other data blocks
- PLC tags of a PLC tag table with the PLC tags of another PLC tag table
- PLC data types with other PLC data types

Comparison of tags takes place over tag names.

#### Types and levels of comparison

Two different basic types of comparison can be used:

- Compare offline/online

  The objects in the project are compared with the objects of the corresponding online device. An online connection to the device is necessary for this comparison.
- Offline/offline comparison

  With offline/offline comparison, you can compare the objects of two devices in the project that is currently open. A device from a reference project or from a library can also be dragged onto the right drop area. You can only compare devices within a TIA Portal instance.

Note that you cannot carry out an unlimited number of comparisons at the same time, but only one comparison per comparison type (offline/online or offline/offline).

You can choose between the following levels of comparison depending on how in-depth an object comparison you require:

- Compare editor

  If you start a comparison on a device, the compare editor opens in which the result of the comparison is displayed.
- Detailed comparison

  For some comparison objects, you can then start a detailed comparison in the compare editor in which the objects compared will be opened side-by-side, each in its own program editor instance. Any differences will be highlighted. Note, however, that you can only start a detailed comparison for SCL blocks if the type of block interface is identical for both blocks. In general, you can only compare bocks of the same programming language using the detailed comparison, like a LAD block with another LAD block, for example.

  For blocks, PLC tags and PLC data types, you can also start the detailed comparison directly from the project tree, as well as from the project library or a global library for blocks and PLC data types. Note that this is not possible for versions of types with the "In test" state, but it is possible for their instances.

The table below gives an overview of the types and levels of comparison you can apply for each object:

| Object | Offline/online | Offline/online | Offline/offline | Offline/offline |
| --- | --- | --- | --- | --- |
|  | **Compare editor** | **Detailed comparison** | **Compare editor** | **Detailed comparison** |
| LAD block | X | X | X | X |
| FBD block | X | X | X | X |
| STL block<sup>1</sup> | X | X | X | X |
| SCL block | X | X<sup>3 4 7</sup> | X | X<sup>7</sup> |
| GRAPH block<sup>2</sup> | X | X<sup>4</sup> | X | X<sup>5</sup> |
| CEM block<sup>4</sup> | X | - | X | - |
| Global data block | X | X | X | X |
| Instance data block | X | X | X | X |
| PLC tags | X<sup>6</sup> | X<sup>6</sup> | X | X |
| PLC data type | X<sup>4</sup> | X<sup>4</sup> | X | X |

Legend:

X: Available  
-: Not available

<sup>1</sup>: STL is not available for S7-1200

<sup>2</sup>: GRAPH is not available for S7-1200

<sup>3</sup>: Not for S7-1200 older than version 2.0

<sup>4</sup>: Not for S7-300/400

<sup>5</sup>: Only comparable with a GRAPH block from the same CPU family

<sup>6</sup>: Only for S7-1500 as of version 2.5

<sup>7</sup>: The type of block interface must be identical

> **Note**
>
> **Note the following:**
>
> - You cannot perform a detailed comparison for know-how protected blocks.
> - If the detailed comparison detects differences only with respect to the data types of local tags, with offline being an alarm data type (C_ALARM C_ALARM_S C_ALARM_8 C_ALARM_8P C_ALARM_T C_AR_SEND C_NOTIFY C_NOTIFY_8P) and online a DWORD, this difference is not marked as such.
> - Note the following peculiarities of a detailed comparison for types and master copies from libraries:
>
>   - You cannot compare PLC tag tables and PLC tags.
>   - Online and monitoring functions are not available for detailed comparison of types and master copies.
>   - Navigation to definitions, access and called blocks is not possible.
>   - The display of cross-references and cross-reference information is not possible.
>   - No syntax check is performed during a detailed comparison for types and master copies. Incorrect syntax is therefore not marked.
>   - If when using multilingual comments, the language used to create the type or the master copy deviates from the project language, there might be different comparison results in the compare editor and detailed comparison. In this case, the comparison result in the compare editor displays the correct status.
>   - Inherited comments and the properties of alarms for types and master copies are not displayed.

#### Comparing PLC programs based on checksums

In addition to the comparison options listed above, TIA Portal gives provides you the option of a simple checksum comparison: The system automatically determines a checksum for the entire PLC program. Based on this checksum, you can easily determine whether two PLC programs are identical.

See also: [Comparing PLC programs based on checksums](#comparison-of-plc-programs-based-on-checksums)

#### Access authorizations for the display of the comparison status (S7-1200/1500)

- CPU 1500 &lt; V2.0 (as well as ET200 SP and software controller), CPU 1200 V4.0 and V4.1**:**

  As of TIA Portal V14, the required access rights for displaying the comparison status of blocks have changed for the specified CPUs from the S7-1200/1500 series.

  Previously, you only needed the "HMI access" access level for the listed CPUs to display the comparison status. As of V14, you need the "read access" access level to display the comparison status.

  This change means that you are prompted to enter the password for "read access" when you go online.

  If you only have the password for "HMI access", you can still establish an online connection.

  In this case, click "Cancel" in the password prompt for read access and enter the password for "HMI access" in the subsequent dialog. The online connection is then established with the available "HMI access rights", but no comparison status of the blocks is displayed.

  Only questions marks are displayed in place of the icons for the comparison status.
- CPU 1200 &lt;=V3.x.**:**

  As of TIA Portal V14, there is a password prompt for the above specified CPUs when you go online for displaying the comparison status of blocks, provided that these CPUs are configured with write protection and/or read protection.

  If you do not know the password for access to read-protected blocks on a protected CPU, you can still establish an online connection.

  In this case, leave the displayed password prompt dialog with "Cancel".

  The online connection is still established, but no comparison status of the blocks is displayed.

  Only questions marks are displayed in place of the icons for the comparison status.

---

**See also**

[Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)
  
[Comparing blocks and PLC data types](#comparing-blocks-and-plc-data-types)
  
[Comparing PLC tags](#comparing-plc-tags)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Performing detailed block comparisons](#performing-detailed-block-comparisons)

### Comparison of software units

#### Offline/online and offline/offline comparison of software units

The comparison of software units is basically the same as the comparison of other project data. This means you also get a simple offline/online comparison, for example, when you create an online connection. During this process, comparable objects in the project tree are marked with icons that represent the result of the comparison. The following rules apply here:

- The software units are shown as identical when their properties and all lower-level objects are identical.
- The software units are shown as different when their properties are different.
- An exclamation mark is shown for a software unit when the lower-level objects are different but their properties are identical.

You can also run a more comprehensive offline/online and offline/offline comparison in the compare editor.

When you start an offline/online or offline/offline comparison on a device, the software units are integrated into the comparison. In the compare editor, the software units are shown in both the left and the right comparison table. In the "Property Comparison" section of the comparison editor under "Source Data &gt; Software unit" you can see the checksums of the compared objects.

During the comparison, the software units are assigned to each other based on their name and their objects are compared with each other. Objects with the same name in different software units are not compared with each other. This means, for example, that when the block "Block_1" is contained in the software unit "Unit1" in the offline project and online in the software unit "Unit2" in the device, they are considered as different objects. In an offline/offline comparison, you can also perform a manual comparison. You can select the objects to be compared.

You can perform actions to synchronize objects that are not identical. If several objects with the same name would be created as a result of synchronization, the action is cancelled and a corresponding message is displayed. Overwriting in manual compare mode is also possible with the same name.

---

**See also**

[Introduction to software units (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#introduction-to-software-units-s7-1500)

### Comparing blocks and PLC data types

#### Assignment criteria

The blocks and PLC data blocks to be compared are assigned to each other on the basis of the following criteria:

- Blocks:

  - Compare offline/online: Addresses, e.g. FB100 or DB100
  - Offline/offline comparison: Symbolic names of the blocks
- PLC data types: PLC data types are assigned to each other by name

#### Comparison

When comparing blocks and PLC data types, checksums are formed for specific properties that serve as the basis for comparison. Some of these properties are grouped into categories in the Comparison Editor. No checksums are available with an offline/online comparison for CPUs of the S7-300/400 series; the time stamp is evaluated in this case. Basically, the time stamp is issued as information for an offline/online comparison for all CPUs as a separate category.

After performing the comparison, you can use actions to define what is to be done about the differences. You can also start a detailed comparison for blocks. The versions of a block compared are opened beside each other and the differences are highlighted. For blocks, PLC tags and PLC data types, you can also start the detailed comparison directly from the project tree.

---

**See also**

[Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
  
[Comparing PLC tags](#comparing-plc-tags)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Performing detailed block comparisons](#performing-detailed-block-comparisons)

### Comparing PLC tags

#### Introduction

The device PLC tag tables will also be shown in the comparison editor if you carry out an offline/offline comparison. The PLC tag tables are assigned to each by name and you can see at a glance whether the PLC tag tables are available in both devices. If necessary, you can also perform a detailed comparison for a PLC tag table. For blocks, PLC tag tables and PLC data types, you can also start the detailed comparison directly from the project tree.

With an offline/online comparison, the overall status of all PLC tags is displayed for CPUs of the S7-1200 and S7-1500 series with a firmware version older than V2.5. For S7-1500-CPUs as of firmware version 2.5 and higher, you have the same options as with an offline/online comparison.

---

**See also**

[Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
  
[Comparing blocks and PLC data types](#comparing-blocks-and-plc-data-types)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Performing detailed block comparisons](#performing-detailed-block-comparisons)

### Comparison of PLC programs based on checksums

#### Introduction

PLC programs are automatically identified with unique checksums during compilation. Based on this checksum, you can identify your program and determine whether two PLC programs are identical.

Because the checksum is loaded to the CPU together with the PLC program, it can also serve as important information in case of a service call. You can, for example, easily determine whether the program that is currently running on the CPU is the same program you loaded some time ago or if it has been changed in the meantime. The original program does not need to be installed on your programming device (PG) in this case.

#### Creation of the system diagnostics blocks

PLC programs are automatically given a unique checksum during compilation. If the next compilation run detects that the PLC program has been changed, the program is given a new checksum. If the PLC program has not changed but is still compiled again, the checksum remains the same.

The checksum also remains unchanged when you make changes and undo them.

The check takes place every time the PLC program is compiled, for example, when you select a CPU or a block folder and use the menu command "Compile &gt; Software".

Two checksums are generated:

- Checksum for software: A checksum is generated across all blocks in the block folder.

  - Blocks that are not called in the program but exist in the block folder are also included in the checksum.
  - Safety blocks and safety PLC data types (UDT) are not taken into consideration.
  - Changes to watch tables or force tables do not change the checksum.
  - Data blocks that are created or modified during runtime, for example, by the instructions "WRIT_DBL", "CREAT_DB" and "DELETE_DB", do not influence the formation of the checksum.
- Checksum for text lists: A checksum is generated for all text lists in the project.

#### Loading the checksum

The checksum is loaded to the CPU together with the PLC program and is available in the online program. During download from the CPU, the checksum is not applied to the offline project because it is generated again automatically during the next compilation.

#### Evaluating the checksum

The checksum is displayed in the CPU properties (Properties &gt; General &gt; Checksums). From there, you can apply it manually to your documents. The "GetChecksum" extended instruction is available to read out the checksum while the program is running.

---

**See also**

[GetChecksum: Read out checksum (S7-1200, S7-1500)](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#getchecksum-read-out-checksum-s7-1200-s7-1500)
  
[Overview of the CPU properties (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#overview-of-the-cpu-properties-s7-1500)
  
[What you should know about the access levels (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#what-you-should-know-about-the-access-levels-s7-1500)

## Comparing blocks

This section contains information on the following topics:

- [Comparing blocks in the compare editor](#comparing-blocks-in-the-compare-editor)
- [Performing detailed block comparisons](#performing-detailed-block-comparisons)

### Comparing blocks in the compare editor

You have the following options for comparing blocks in the compare editor:

- Compare offline/online

  The blocks in the project are compared with the blocks of the selected device.
- Automatic offline/offline comparison

  All blocks of the selected devices are compared offline.
- Manual offline/offline comparison

  The selected blocks of the devices are compared offline.

#### Performing an offline/online comparison of blocks

To perform an offline/online comparison, follow these steps:

1. In the project tree, select a device that allows offline/online comparison.
2. Select the "Compare &gt; Offline/online" command in the shortcut menu.
3. If you have not already established an online connection to this device, the "Go online" dialog opens. In this case, set all the necessary parameters for the connection and click "Connect".

   The online connection is established and the compare editor opens.
4. Open the "Program blocks" folder.

   You can identify the status based on the symbols in the status and action area. You can define certain actions depending on the status of the objects. Note, however, that you can only perform actions in one direction in a synchronization action.

#### Performing an automatic offline/offline comparison of blocks

To perform an automatic offline/offline comparison of blocks, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. Open the "Program blocks" folder.

   You can identify the status of the objects based on the symbols in the status and action area. You can define certain actions depending on the status of the objects. When you select an object, the object's properties and the corresponding object of the assigned device are clearly shown in the properties comparison.

You can drag any other device to the drop area at any time to perform further comparisons.

#### Carrying out a manual offline/offline comparison of blocks

To perform a manual offline/offline comparison of blocks, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. In the status and action area, click on the button for switching between automatic and manual comparison.
5. Select the objects that you want to compare.

   The properties comparison is displayed. You can identify the status of the objects based on the symbols. You can define certain actions depending on the status of the objects.

You can drag any other device to the drop area at any time to perform further comparisons.

---

**See also**

[Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)
  
[Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Performing detailed block comparisons](#performing-detailed-block-comparisons)
  
[Comparing PLC tags](#comparing-plc-tags-1)
  
[Comparing PLC data types](#comparing-plc-data-types)

### Performing detailed block comparisons

This section contains information on the following topics:

- [Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
- [Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)](#start-detailed-comparison-for-graph-blocks-s7-300-s7-400-s7-1500)
- [Starting detailed comparison for data blocks](#starting-detailed-comparison-for-data-blocks)
- [Visualization of the comparison result](#visualization-of-the-comparison-result)
- [Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
- [Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
- [Updating comparison results](#updating-comparison-results)

#### Start a detailed comparison for LAD/FBD/STL/SCL blocks

You can start a detailed comparison for blocks. The versions of a block compared are opened beside each other and the differences highlighted. You have the following options for starting a detailed comparison for blocks:

- Starting detailed comparison using the compare editor

  The detailed comparison for blocks is possible with the compare editor, both for offline/online and for offline/offline comparisons.
- Starting detailed comparison in the project tree

  The detailed comparison for blocks is possible with the project tree, both for offline/online and for offline/offline comparisons. An existing online connection is required for the offline/online comparison.
- Starting detailed comparison in a library

  You can also start the detailed comparison for blocks in the project library or a global library. This is possible for both types and master copies.
- Starting detailed comparisons in the program editor

  In this case the opened block is compared with its online version.

> **Note**
>
> Note the following:
>
> - For blocks that are created in the programming language SCL, the detail comparison is not available for S7-1200 series CPUs with a version older than 2.0.
> - You can only start a detailed comparison for two SCL blocks if both blocks use the same interface type, either both in table form or both in text form.
> - S7-1500: It is possible that another user can carry out a loading process on the CPU through joint parallel working on a CPU. If the currently compared block is changed or deleted by this loading process, the detailed comparison is terminated and a message is displayed. In this case, re-start the detailed comparison, if required.
> - Blocks with multiple networks: If you change the order of networks, the corresponding networks may no longer be assigned or compared with other networks. To compare moved networks, adjust the order temporarily.

##### Starting detailed comparison using the compare editor

To start a detailed comparison for a block using the compare editor, follow these steps:

1. First, perform an offline/online or an offline/offline comparison.

   The compare editor opens.
2. In the compare editor, select the block for which you want to perform a detailed comparison.
3. Click "Start detailed comparison" in the toolbar or select the "Start detailed comparison" command from the shortcut menu.

##### Starting detailed comparison in the project tree

To start an offline/offline detailed comparison for a block directly in the project tree, follow these steps:

1. Right-click the block that you want to compare. This can also be a block from a reference project.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the block that you want to compare with the block that you previously selected as left object. This can be a block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

To start an offline/online detailed comparison for a block directly in the project tree, follow these steps:

1. Establish an online connection to the device where the block is located.
2. Right-click the block that you want to compare with its online object.
3. Select the command "Quick compare &gt; Compare with the online object" in the shortcut menu.

##### Starting detailed comparison in a library

To start a detailed comparison for a block directly in a library, follow these steps:

1. In the project library or a global library, right-click the block that you want to compare.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the block that you want to compare with the block that you previously selected as left object. This can be a block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

##### Starting detailed comparisons in the program editor

For the comparison type offline/online, you can start the detailed comparison directly in the program editor. To do this, follow these steps:

1. Open the block for which you wish to carry out a detailed comparison.
2. Establish an online connection.

   See also: [Go online and Go offline](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. Click "Detailed comparison" in the toolbar.
4. Confirm the dialog for closing the block with "Yes".

**Note**

Please note that the block must be available online in order for you to be able to start the detailed comparison for the block within the programming editor.

##### Result

One instance of the program editor will be opened for each version of the block compared and the two instances are displayed side by side.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Visualization of the comparison result for LAD/FBD](#visualization-of-the-comparison-result-for-ladfbd)
  
[Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-stl-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for SCL](#visualization-of-the-comparison-result-for-scl)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

#### Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)

You can start a detailed comparison for GRAPH blocks. The versions of a block compared are opened beside each other and the differences highlighted. You have the following options for starting a detailed comparison for GRAPH blocks:

- Starting detailed comparison using the compare editor

  The detailed comparison for blocks is possible with the compare editor, both for online/offline and for offline/offline comparisons.
- Starting detailed comparison in the project tree

  The detailed comparison for blocks is possible with the project tree, both for online/offline and for offline/offline comparisons. An existing online connection is required for the online/offline comparison.
- Starting detailed comparison in a library

  You can also start the detailed comparison for blocks in the project library or a global library. This is possible for both types and master copies.
- Starting detailed comparisons in the program editor

  In this case the opened block is compared with its online version.

The following comparison methods are available for GRAPH blocks:

- Compare sequence

  Complete sequencers are compared with each other in this mode. A detailed comparison for a GRAPH block always starts in the "Compare sequence" comparison mode. This means the comparison starts at the beginning of the sequencer and the differences between the sequencers are displayed. If there are structural differences between the sequencers, the comparison results are only displayed up to the first structural difference.
- Compare selection

  You can use the "Compare selection" comparison mode to compare any areas with each other. This means you can compare sections of the sequencer which are downstream from a structural difference in the sequence.

You can toggle at random between both comparison modes.

> **Note**
>
> S7-1500: It is possible that another user can carry out a loading process on the CPU through joint parallel working on a CPU. If the currently compared block is changed or deleted by this loading process, the detailed comparison is terminated and a message is displayed. In this case, re-start the detailed comparison, if required.

##### Starting detailed comparison using the compare editor

To start a detailed comparison, follow these steps:

1. First, perform an online/offline or an offline/offline comparison between the two devices.

   The compare editor opens.
2. In the compare editor, select the GRAPH block for which you want to perform a detailed comparison.
3. Click the "Start detailed comparison" button in the toolbar.

   One instance of the program editor is opened for each version of the GRAPH blocks compared and the two instances are displayed side by side. Any differences will be highlighted. The comparison takes place in the "Compare sequence" mode.

**Note**

The manual comparison is also available for an offline/offline comparison. It lets you select any GRAPH block in the comparison editor for the comparison.

##### Starting detailed comparison in the project tree

To start an offline/offline detailed comparison for a GRAPH block directly in the project tree, follow these steps:

1. Right-click the block that you want to compare. This can also be a block from a reference project.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the block that you want to compare with the block that you previously selected as left object. This can be a block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

   One instance of the program editor is opened for each version of the GRAPH blocks compared and the two instances are displayed side by side. Any differences will be highlighted. The comparison takes place in the "Compare sequence" mode.

To start an online/offline detailed comparison for a GRAPH block directly in the project tree, follow these steps:

1. Establish an online connection to the device where the block is located.
2. Right-click the block that you want to compare with its online object.
3. Select the command "Quick compare &gt; Compare with the online object" in the shortcut menu.

   One instance of the program editor is opened for each version of the GRAPH blocks compared and the two instances are displayed side by side. Any differences will be highlighted. The comparison takes place in the "Compare sequence" mode.

##### Starting detailed comparison in a library

To start a detailed comparison for a block directly in a library, follow these steps:

1. In the project library or a global library, right-click the block that you want to compare.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the block that you want to compare with the block that you previously selected as left object. This can be a block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

##### Starting detailed comparisons in the program editor

For the comparison type online/offline, you can start the detailed comparison directly in the program editor. To do this, follow these steps:

1. Open the GRAPH block for which you wish to carry out a detailed comparison.
2. Establish an online connection.

   See also: [Go online and Go offline](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. Click "Detailed comparison" in the toolbar.
4. Confirm the dialog for closing the block with "Yes".

   One instance of the program editor is opened for each version of the GRAPH blocks compared and the two instances are displayed side by side. Any differences will be highlighted. The comparison takes place in the "Compare sequence" mode.

**Note**

Please note that the block must be available online in order for you to be able to start the detailed comparison for the block within the programming editor.

##### Comparing regions​

To compare specific areas within the displayed sequencers, follow these steps:

1. In each sequencer, select the step from which you want to start the comparison.
2. Click "Comparison mode" in the toolbar.

   The comparison mode changes to "Compare selection" and the comparison result is updated. The sequencers are compared as of the selected steps. The compared substrings are highlighted.
3. To compare other areas, select the steps which are to serve as starting point for the comparison.
4. Click "Update the comparison result" in the toolbar.
5. To compare the complete sequencers once again, click "Comparison mode" in the toolbar.

   Each time you click "Comparison mode" you are changing the comparison mode. You can also open the drop-down list with the arrow and select the required mode from the list.

**Note**

When you change the comparison mode, you are also updating the comparison results at the same time. If you stay in "Compare selection" mode, you must manually update the comparison results every time you change the starting point.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-graph-s7-300-s7-400-s7-1500)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

#### Starting detailed comparison for data blocks

You can start a detailed comparison for data blocks. The compared versions of a data block are opened beside each other in two declaration tables and the differences are listed in the "Comparison result" tab in the Inspector window.

You have the following options for starting a detailed comparison for data blocks:

- Starting detailed comparison using the compare editor

  The detailed comparison for data blocks is possible with the compare editor, both for offline/online and for offline/offline comparisons.
- Starting detailed comparison in the project tree

  The detailed comparison for data blocks is possible with the project tree, both for offline/online and for offline/offline comparisons. An existing online connection is required for the offline/online comparison.
- Starting detailed comparison in a library

  For data blocks that you use as master copies, you can also start the detailed comparison in the project library or a global library.

##### Starting detailed comparison using the compare editor

To start a detailed comparison for a data block using the compare editor, follow these steps:

1. First, perform an offline/online or an offline/offline comparison.

   The compare editor opens.
2. In the compare editor, select the data block for which you want to perform a detailed comparison.
3. Click "Start detailed comparison" in the toolbar or select the "Start detailed comparison" command from the shortcut menu.

##### Starting detailed comparison in the project tree

To start an offline/offline detailed comparison for a data block directly in the project tree, follow these steps:

1. Right-click the data block that you want to compare. This can also be a data block from a reference project.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the data block that you want to compare with the data block that you previously selected as left object. This can be a data block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

To start an offline/online detailed comparison for a data block directly in the project tree, follow these steps:

1. Establish an online connection to the device where the data block is located.
2. Right-click the data block that you want to compare with its online object.
3. Select the command "Quick compare &gt; Compare with the online object" in the shortcut menu.

##### Starting detailed comparison in a library

To start a detailed comparison for a data block directly in a library, follow these steps:

1. In the project library or a global library, right-click the data block that you want to compare.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the data block that you want to compare with the data block that you previously selected as left object. This can be a data block from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

#### Visualization of the comparison result

This section contains information on the following topics:

- [Visualization of the comparison result for LAD/FBD](#visualization-of-the-comparison-result-for-ladfbd)
- [Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-stl-s7-300-s7-400-s7-1500)
- [Visualization of the comparison result for SCL](#visualization-of-the-comparison-result-for-scl)
- [Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-graph-s7-300-s7-400-s7-1500)

##### Visualization of the comparison result for LAD/FBD

###### Introduction

The detailed comparison allows you to identify the exact places where versions of a block differ. The following color coding allows you to find these places as quickly as possible:

- The lines where there are differences are highlighted in gray.
- Differing operands and instructions are highlighted in green.
- If the number of networks differs, pseudo-networks are added to allow the display of identical networks to be synchronized. These pseudo-networks are highlighted in gray and contain the text "No corresponding network found" in the title bar of the network. Pseudo-networks cannot be edited.

  > **Note**
  >
  > Note the following:
  >
  > - If there is a difference of more than 50 percent between two networks, these networks are regarded as not belonging together and there is no comparison between these networks. In this case, pseudo networks are also inserted until a suitable network is found.
  > - You obtain a different comparison result depending on which block is your output block and which block is your comparison block.

For the sake of clarity, not all the differences are highlighted but rather the first difference of an operation in each case. For example, if all the inputs in an instruction with multiple inputs are different in the offline and online versions of the block, only the first input is highlighted as a difference. You can resolve this difference and update the comparison list. The next input will then be highlighted as a difference.

The number of differences highlighted within a network therefore depends on the number of instructions.

###### Structure of the detailed comparison

The following figure shows an example of the offline/online detailed comparison for the LAD programming language:

![Structure of the detailed comparison](images/58968013067_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for LAD

② Reference block

③ Compared block

④ Comparison result in the Inspector window

The following figure shows an example of the offline/online detailed comparison for the FBD programming language:

![Structure of the detailed comparison](images/58989308043_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for FBD

② Reference block

③ Compared block

④ Comparison result in the Inspector window

> **Note**
>
> Display of the symbolic names of the online version of the block is only possible for S7-1200 and S7-1500.

###### Toolbar of the detailed comparison

With the toolbar, you can access the following functions:

- General functions

  - Insert network
  - Delete network
  - Insert row
  - Add row
  - Open all networks
  - Close all networks
- Comparison-specific functions

  - Position on first difference
  - Position on previous difference
  - Position on next difference
  - Position on last difference
  - Synchronize scrolling between editors
  - Update comparison results

###### Reference block

The reference block is displayed in the left window. In an offline/online comparison, the reference block is the offline version of the block.

###### Compared block

The compared block is displayed in the right window. In an offline/online comparison, the compared block is the online version of the block.

###### Comparison result in the Inspector window

The differences are displayed in the form of a table in the "Info &gt; Comparison result" tab of the Inspector window. Double-click on a row to navigate to the corresponding difference in the block.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

##### Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)

###### Introduction

The detailed comparison allows you to identify the exact places where versions of a block differ. The following color coding allows you to find these places as quickly as possible:

- The lines where there are differences are highlighted in gray.
- Differing operands and instructions are highlighted in green.
- If the number of networks differs, pseudo-networks are added to allow the display of identical networks to be synchronized. These pseudo-networks are highlighted in gray and contain the text "No corresponding network found" in the title bar of the network. Pseudo-networks cannot be edited.

###### Structure of the detailed comparison

The following figure shows an example of the online/offline detailed comparison for the STL programming language:

![Structure of the detailed comparison](images/58990129419_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for STL

② Reference block

③ Compared block

④ Comparison result in the Inspector window

> **Note**
>
> The display of the symbolic names of the online version of the block is only possible for S7-1500.

###### Toolbar of the detailed comparison

With the toolbar, you can access the following functions:

- General functions

  - Insert network
  - Delete network
  - Insert row
  - Add row
  - Open all networks
  - Close all networks
- Comparison-specific functions

  - Position on first difference
  - Position on previous difference
  - Position on next difference
  - Position on last difference
  - Synchronize scrolling between editors
  - Update comparison results

###### Reference block

The reference block is displayed in the left window. In an online/offline comparison, the reference block is the offline version of the block.

###### Compared block

The compared block is displayed in the right window. In an online/offline comparison, the compared block is the online version of the block.

###### Comparison result in the Inspector window

The differences are displayed in the form of a table in the "Info &gt; Comparison result" tab of the Inspector window. Double-click on a row to navigate to the corresponding difference in the block.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

##### Visualization of the comparison result for SCL

###### Introduction

The detailed comparison allows you to identify the exact places where versions of a block differ. The following color coding allows you to find these places as quickly as possible:

- The lines where there are differences are highlighted in gray.
- Differing operands and instructions are highlighted in green.

> **Note**
>
> The offline/online detailed comparison is not available for the CPU families S7-300/400 and for S7-1200 with a version less than 2.0.

###### Structure of the detailed comparison

The following figure shows an example of the offline/online detailed comparison for the SCL programming language:

![Structure of the detailed comparison](images/59019126795_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for SCL

② Reference block

③ Compared block

④ Comparison result in the Inspector window

> **Note**
>
> The display of the symbolic name of the online version of the block is only possible for S7-1200 and S7-1500.

###### Toolbar of the detailed comparison

With the toolbar, you can access the following functions:

- General functions

  - Insert row
  - Add row
- Comparison-specific functions

  - Position on first difference
  - Position on previous difference
  - Position on next difference
  - Position on last difference
  - Synchronize scrolling between editors
  - Update comparison results

###### Reference block

The reference block is displayed in the left window. In an offline/online comparison, the reference block is the offline version of the block.

###### Compared block

The compared block is displayed in the right window. In an offline/online comparison, the compared block is the online version of the block.

###### Comparison result in the Inspector window

The differences are displayed in the form of a table in the "Info &gt; Comparison result" tab of the Inspector window. Double-click on a row to navigate to the corresponding difference in the block.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

##### Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)

###### Introduction

The detailed comparison allows you to identify the exact places where versions of a block differ. When you start a detailed comparison for a GRAPH block, navigation is opened first. Use the dividers to toggle between the navigation and the currently set view. You can select other views with the toolbar of the detailed comparison.

The result of the comparison is indicated by the comparison symbols.

See also: [Overview of the comparison editor](Editing%20project%20data.md#overview-of-the-compare-editor)

###### Structure of the detailed comparison

The following figure shows an example for the navigation view with an online/offline detailed comparison for the GRAPH programming language:

![Structure of the detailed comparison](images/96117983115_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for GRAPH

② Reference block

③ Compared block

④ Navigation toolbar

⑤ Dividers

⑥ Comparison result in the Inspector window

The following figure shows an example for the sequence view with an online/offline detailed comparison for the GRAPH programming language:

![Structure of the detailed comparison](images/96117987595_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for GRAPH

② Reference block

③ Compared block

④ Dividers

⑤ Comparison result in the Inspector window

> **Note**
>
> If there are structural differences between the blocks, the comparison results are only displayed up to the first structural difference in the sequence view.

The following figure shows an example for the single step view with an online/offline detailed comparison for the GRAPH programming language:

![Structure of the detailed comparison](images/96118081675_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for GRAPH

② Reference block

③ Compared block

④ Dividers

⑤ Comparison result in the Inspector window

> **Note**
>
> The result of the comparison refers to the complete network Differences within the networks are not identified.

The following figure shows an example for the view of permanent instructions with an online/offline detailed comparison for the GRAPH programming language:

![Structure of the detailed comparison](images/96118086155_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for GRAPH

② Reference block

③ Compared block

④ Dividers

⑤ Comparison result in the Inspector window

> **Note**
>
> The result of the comparison refers to the complete network Differences within the networks are not identified.

The following figure shows an example for the alarm view with an online/offline detailed comparison for the GRAPH programming language:

![Structure of the detailed comparison](images/90877313931_DV_resource.Stream@PNG-en-US.png)

① Toolbar of the detailed comparison for GRAPH

② Reference block

③ Compared block

④ Dividers

⑤ Comparison result in the Inspector window

###### Toolbars

With the toolbar of the detailed comparison, you can access the following functions:

- General functions

  - Change to permanent pre-instructions
  - Change to sequence view
  - Change to single step view
  - Change to permanent post-instructions
  - Change to alarm view
  - Add sequence
  - Delete sequence
  - Insert network
  - Delete network
  - Insert row
  - Add row
  - Open all networks
  - Close all networks
- Comparison-specific functions

  - Position on first difference
  - Position on previous difference
  - Position on next difference
  - Position on last difference
  - Synchronize scrolling between editors
  - Update comparison results
  - Select the comparison mode

The navigation has its own toolbar with the following functions:

- Zoom in or zoom out of elements within the navigation
- Synchronize navigation

###### Reference block

The reference block is displayed in the left window. In an online/offline comparison, the reference block is the offline version of the block.

###### Compared block

The compared block is displayed in the right window. In an online/offline comparison, the compared block is the online version of the block.

###### Dividers

You can click the dividers to toggle quickly between the navigation and the current view.

###### Comparison result in the Inspector window

The differences are displayed in the form of a table in the "Info &gt; Comparison result" tab of the Inspector window. Double-click on a row to navigate to the corresponding difference in the block.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)](#start-detailed-comparison-for-graph-blocks-s7-300-s7-400-s7-1500)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

#### Navigating in the detailed comparison

##### Requirement

You have run a detailed comparison.

##### Navigate to the differences

To navigate to a difference between the two blocks, follow these steps:

1. Open the list of results for the detailed comparison under "Info &gt; Comparison result" in the Inspector window.
2. Double-click a difference.

   The difference is selected in both editors.

Or:

1. Click one of the following navigation buttons on the toolbar:

   - Position on first difference

     Navigates to the first difference in the block, and displays the difference in both editors.
   - Position on previous difference

     Navigates to the previous difference starting from the current position, and displays the difference in both editors.
   - Position on next difference

     Navigates to the next difference starting from the current position, and displays the difference in both editors.
   - Position on last difference

     Navigates to the last difference in the block, and displays the difference in both editors.

##### Switching off/on the synchronization of the vertical scrolling between the editors

The scrolling for both editors is synchronized to ensure that the corresponding networks are visible parallel to each other during vertical scrolling. You can switch this mode off and on. To do this, follow these steps:

1. To switch off synchronized scrolling, click the "Synchronize scrolling between editors" button in the toolbar.
2. To switch on synchronized scrolling again, click the "Synchronize scrolling between editors" button one more time in the toolbar.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)](#start-detailed-comparison-for-graph-blocks-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for LAD/FBD](#visualization-of-the-comparison-result-for-ladfbd)
  
[Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-stl-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for SCL](#visualization-of-the-comparison-result-for-scl)
  
[Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-graph-s7-300-s7-400-s7-1500)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

#### Changing blocks during the detailed comparison

While you are carrying out the detailed comparison, you can make changes to the blocks that are being compared. Remember the following:

- Compare offline/online: You can change only the offline block.
- Offline/offline comparison: You can change only the offline block in the left-hand area.

After a block change, it may be necessary to manually update the comparison result in the comparison editor to ensure that the comparison status is displayed correctly. You can then specify actions to synchronize the objects.

> **Note**
>
> You cannot change SCL blocks manually. However, you can apply changes from one block to the other block. In this regard, note the following points:
>
> - You cannot apply any changes in an online block.
> - You can only apply changes in an offline block if this is not write-protected. This is the case, for example, if the blocks of the detailed comparison come from different CPUs. It is then also possible to apply the changes to the block in the right-hand area.

##### Changing LAD, FBD or STL blocks

To change LAD, FBD or STL blocks, follow these steps:

1. Change the block in the left-hand area according to your requirements.
2. If necessary, click on "Update comparison results" in the toolbar.

##### Changing GRAPH blocks

To change a GRAPH block, follow these steps:

1. Switch to sequence view by clicking "Sequence view" between the two blocks.
2. Change the block in the left-hand area according to your requirements.
3. If necessary, click on "Update comparison results" in the toolbar.

##### Changing SCL blocks

To apply a change from one block to another one, follow these steps:

1. In the sidebar of the block from which you want to apply a change to another block, click on the arrow in the corresponding line.

   The line is inserted in the other block and the arrow buttons are removed.
2. If necessary, click on "Update comparison results" in the toolbar.

**Note**

The colors of the arrows mean the following:

- Gray: The changes cannot be applied to the other block, as the other block is either an online block or write-protected.
- Blue: The changes are applied from an offline block to the other block.
- Orange: The changes are applied from an online block to the other block.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)](#start-detailed-comparison-for-graph-blocks-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for LAD/FBD](#visualization-of-the-comparison-result-for-ladfbd)
  
[Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-stl-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for SCL](#visualization-of-the-comparison-result-for-scl)
  
[Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-graph-s7-300-s7-400-s7-1500)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Updating comparison results](#updating-comparison-results)

#### Updating comparison results

As soon as you change an object, the comparison results are no longer valid and must be updated.

##### Requirement

You have run a detailed comparison.

##### Procedure

To update the comparison results, follow these steps:

1. Click "Update the comparison result" in the toolbar.

---

**See also**

[Basic information on comparing PLC programs](#basic-information-on-comparing-plc-programs)
  
[Comparing offline/online](Editing%20project%20data.md#comparing-offlineonline)
  
[Carrying out offline/offline comparisons](Editing%20project%20data.md#carrying-out-offlineoffline-comparisons)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Start a detailed comparison for LAD/FBD/STL/SCL blocks](#start-a-detailed-comparison-for-ladfbdstlscl-blocks)
  
[Start detailed comparison for GRAPH blocks (S7-300, S7-400, S7-1500)](#start-detailed-comparison-for-graph-blocks-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for LAD/FBD](#visualization-of-the-comparison-result-for-ladfbd)
  
[Visualization of the comparison result for STL (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-stl-s7-300-s7-400-s7-1500)
  
[Visualization of the comparison result for SCL](#visualization-of-the-comparison-result-for-scl)
  
[Visualization of the comparison result for GRAPH (S7-300, S7-400, S7-1500)](#visualization-of-the-comparison-result-for-graph-s7-300-s7-400-s7-1500)
  
[Navigating in the detailed comparison](#navigating-in-the-detailed-comparison)
  
[Changing blocks during the detailed comparison](#changing-blocks-during-the-detailed-comparison)

## Comparing PLC tags

You have the following options for comparing PLC tags:

- Automatic offline/offline comparison in the compare editor

  The PLC tag tables of the selected devices are compared offline.
- Manual offline/offline comparison in the compare editor

  The selected PLC tag tables of the devices are compared offline.
- Offline/online comparison (only for S7-1500 version 2.5 and higher)

  The PLC tags in the project are compared with the PLC tags of the selected device.
- Detailed comparison

  Use the detailed comparison to determine differences within the PLC tag tables. You can start the detailed comparison either in the compare editor, in the project tree or in the PLC tag table "PLC tags" (only offline/online). The offline/online detailed comparison is available for all devices; the offline/online detailed comparison for S7-1500 CPUs as of version 2.5.

### Performing automatic offline/offline comparison in the compare editor

To perform an automatic offline/offline comparison of PLC tag tables, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. Open the "PLC tags" folder.

   You can identify the status of the PLC tag tables based on the symbols in the status and action area. You can define certain actions depending on the status.

You can drag any other device to the drop area at any time to perform further comparisons.

### Performing manual offline/offline comparison in the compare editor

To perform a manual offline/offline comparison of PLC tag tables, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. In the status and action area, click on the button for switching between automatic and manual comparison.
5. Select the PLC tag tables that you want to compare.

   The properties comparison is displayed. You can identify the status based on the symbols.

You can drag any other device to the drop area at any time to perform further comparisons.

### Run offline/online comparison (only for S7-1500 version 2.5 and higher)

To perform an offline/offline comparison of PLC tag tables, follow these steps:

1. In the project tree, select a device that allows offline/online comparison.
2. Select the "Compare &gt; Offline/online" command in the shortcut menu.
3. If you have not already established an online connection to this device, the "Go online" dialog opens. In this case, set all the necessary parameters for the connection and click "Connect".

   The online connection is established and the compare editor opens.
4. Open the "PLC tags" folder.

   You can identify the status of the PLC tag tables based on the symbols in the status and action area. You can define certain actions depending on the status of the objects. Note, however, that you can only perform actions in one direction in a synchronization action.

### Starting detailed comparisons using the compare editor

To start a detailed comparison for a PLC tag table using the compare editor, follow these steps:

1. Perform an offline/offline or an offline/online comparison.

   The compare editor opens.
2. For an automatic offline/offline comparison or offline/online comparison in the compare editor, select the PLC tag table for which you want to run a detailed comparison. Note that two PLC tag tables must be selected for comparison for a manual offline/offline comparison.
3. Click the "Start detailed comparison" button in the toolbar.

   A separate compare editor opens. All existing PLC tags and user constants of the selected PLC tag tables are displayed depending on the settings of the compare editor. However, system constants are not shown. You can identify the status of the PLC tags based on the symbols. You can define certain actions for an offline/offline comparison depending on the status of the PLC tags.

### Starting detailed comparison in the project tree

To start an offline/offline detailed comparison for a PLC tag table in the project tree, follow these steps:

1. Right-click the PLC tag table that you want to compare. This can also be a PLC tag table from a reference project.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the PLC tag table that you want to compare with the PLC tag table that you previously selected as left object.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

   A separate compare editor opens. All existing PLC tags and user constants of the selected PLC tag tables are displayed depending on the settings of the compare editor. However, system constants are not shown. You can identify the status of the PLC tags based on the symbols. You can define certain actions depending on the status of the PLC tags.

To start an offline/online detailed comparison for a PLC tag table directly in the project tree, follow these steps:

1. Establish an online connection to the device where the PLC tag table is located.
2. Right-click the PLC tag table that you want to compare with your online object.
3. Select the command "Quick compare &gt; Compare with the online object" in the shortcut menu.

   A separate compare editor opens. All existing PLC tags and user constants of the selected PLC tag tables are displayed depending on the settings of the compare editor. However, system constants are not shown. You can identify the status of the PLC tags based on the symbols.

### Start detailed comparison in the PLC tag table "PLC tags"

To start an offline/online detailed comparison for a PLC tag table in the PLC tag table "Show all tags", follow these steps:

1. Establish an online connection to the device where the PLC tag table is located.
2. Open the "PLC tags" folder under the CPU in the project tree.
3. Double-click the entry "Show all tags".

   The PLC tag table "PLC tags" opens.
4. Click the "Start detailed comparison" button in the toolbar.

   A separate compare editor opens. All existing PLC tags and user constants of the selected PLC tag tables are displayed depending on the settings of the compare editor. However, system constants are not shown. You can identify the status of the PLC tags based on the symbols.

---

**See also**

[Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
  
[Comparing PLC data types](#comparing-plc-data-types)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Comparing blocks](#comparing-blocks)

## Comparing PLC data types

You have the following options for comparing PLC data types:

- Offline/online comparison (S7-1200/1500 only)

  The PLC data types in the project are compared with the PLC data types of the selected device.
- Automatic offline/offline comparison in the compare editor

  The PLC data types of the selected devices are compared offline.
- Manual offline/offline comparison in the compare editor

  The selected PLC data types of the devices are compared offline.
- Detailed comparison

  Use the detailed comparison to determine differences between PLC data types. You can start the detailed comparison either in the compare editor, in the project tree or in a library. This is possible for both types and master copies.

### Performing offline/online comparison of PLC data types in the compare editor

To perform an offline/online comparison, follow these steps:

1. In the project tree, select a device that allows offline/online comparison.
2. Select the "Compare &gt; Offline/online" command in the shortcut menu.

   If you have not already established an online connection to this device, the "Go online" dialog opens. In this case, set all the necessary parameters for the connection and click "Connect".

   The online connection is established and the compare editor opens.
3. Open the "PLC data types" folder.

   You can identify the status of the PLC data types based on the symbols in the status and action area. When you select an object, the properties of the PLC data type and the corresponding PLC data type of the assigned device are displayed in the properties comparison.

### Performing automatic offline/offline comparison in the compare editor

To perform an automatic offline/offline comparison of PLC data types, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. Open the "PLC data types" folder.

   You can identify the status of the PLC data types based on the symbols in the status and action area. You can define certain actions depending on the status. You can drag any other device to the drop area at any time to perform further comparisons.

### Performing manual offline/offline comparison in the compare editor

To perform a manual offline/offline comparison of PLC data types, follow these steps:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Drag-and-drop an additional device to the drop area of the right pane. The device to be compared can originate from the same project, a reference project or the library.
4. In the status and action area, click on the button for switching between automatic and manual comparison.
5. Select the PLC data types that you want to compare.

   The properties comparison is displayed. You can identify the status based on the symbols. You can drag any other device to the drop area at any time to perform further comparisons.

### Starting detailed comparison using the compare editor

To start a detailed comparison for a PLC data type using the compare editor, follow these steps:

1. Perform an offline/offline comparison. You can also perform an offline/online comparison for CPUs of the S7-1200/1500 series.
2. For an automatic offline/offline comparison in the compare editor, select the PLC data type for which you want to run a detailed comparison. Note that two PLC data types must be selected for comparison with a manual offline/offline comparison.
3. Click the "Start detailed comparison" button in the toolbar.

   The "PLC data type comparison" window opens and all tags of the compared PLC data types are displayed. You can view the differences under "Info &gt; Result of comparison" in the inspector window.

### Starting detailed comparison in the project tree

To start a offline/offline detailed comparison for a PLC data type directly in the project tree, follow these steps:

1. Right-click the PLC data type that you want to compare. This can also be a PLC data type from a reference project.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the PLC data type that you want to compare with the PLC data type that you previously selected as left object.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

   The "PLC data type comparison" window opens and all tags of the compared PLC data types are displayed. You can view the differences under "Info &gt; Result of comparison" in the inspector window.

To start an offline/online detailed comparison for a PLC data type for a CPU of the S7-1200/1500 series directly in the project tree, follow these steps:

1. Establish an online connection to the device where the block is located.
2. Right-click the PLC data type that you want to compare with its online object.
3. Select the command "Quick compare &gt; Compare with the online object" in the shortcut menu.

   The "PLC data type comparison" window opens and all tags of the compared PLC data types are displayed. You can view the differences under "Info &gt; Result of comparison" in the inspector window.

### Starting detailed comparison in a library

To start a detailed comparison for a PLC data type directly in a library, follow these steps:

1. In the project library or a global library, right-click the PLC data type that you want to compare.
2. Select the command "Quick compare &gt; Select as left object" in the shortcut menu.
3. Right-click the PLC data type that you want to compare with the block that you previously selected as left object. This can be a PLC data type from the current project, a reference project or a library.
4. Select the command "Quick compare &gt; Compare with &lt;selected object&gt;" in the shortcut menu. "&lt;selected object&gt;" stands for the left comparison object.

---

**See also**

[Introduction to comparing PLC programs](#introduction-to-comparing-plc-programs)
  
[Using the compare editor](Editing%20project%20data.md#using-the-compare-editor)
  
[Comparing blocks](#comparing-blocks)
  
[Comparing PLC tags](#comparing-plc-tags-1)

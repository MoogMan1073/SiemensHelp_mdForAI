---
title: "Configuring CFC charts"
package: CFCFCPenUS
topics: 142
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring CFC charts

This section contains information on the following topics:

- [Cybersecurity information](#cybersecurity-information)
- [Introduction and basics](#introduction-and-basics)
- [Elements and basic settings](#elements-and-basic-settings)
- [Configuring and adapting CFC charts](#configuring-and-adapting-cfc-charts)
- [Configuring and using the trend and dynamic displays](#configuring-and-using-the-trend-and-dynamic-displays)
- [Data types in CFC](#data-types-in-cfc)
- Working with CFC charts for S7
- [Openness: CFC](#openness-cfc)

## Cybersecurity information

Siemens provides products and solutions with industrial cybersecurity functions that support the secure operation of plants, systems, machines and networks.

In order to protect plants, systems, machines and networks against cyber threats, it is necessary to implement – and continuously maintain – a holistic, state-of-the-art industrial cybersecurity concept. Siemens’ products and solutions constitute one element of such a concept.

Customers are responsible for preventing unauthorized access to their plants, systems, machines and networks. Such systems, machines and components should only be connected to an enterprise network or the internet if and to the extent such a connection is necessary and only when appropriate security measures (e.g. firewalls and/or network segmentation) are in place.

For additional information on industrial cybersecurity measures that may be implemented, please visit   
<https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html>.

Siemens’ products and solutions undergo continuous development to make them more secure. Siemens strongly recommends that product updates are applied as soon as they are available and that the latest product versions are used. Use of product versions that are no longer supported, and failure to apply the latest updates may increase customer’s exposure to cyber threats.

To stay informed about product updates, subscribe to the Siemens Industrial Cybersecurity RSS Feed under   
<https://new.siemens.com/global/en/products/services/cert.html>.

## Introduction and basics

This section contains information on the following topics:

- [Basics of CFC](#basics-of-cfc)
- [Configuration options for CFC charts](#configuration-options-for-cfc-charts)
- [Instructions and blocks](#instructions-and-blocks)
- [Type and instance](#type-and-instance)
- [Hierarchical CFC charts](#hierarchical-cfc-charts)
- [Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)
- [Multilingual texts in CFC](#multilingual-texts-in-cfc)
- [Copying objects](#copying-objects)
- [CFC naming conventions](#cfc-naming-conventions)

### Basics of CFC

#### What is CFC?

"CFC" stands for "Continuous Function Chart".

With CFC, you create user programs by simple placement, parameter assignment and interconnection of instructions and blocks in the CFC charts.

You use extensive libraries with premade instructions and blocks. This means that instructions and blocks do not need to be programmed. The likelihood of errors is reduced.

The "CFC" editor supports you with these functions when creating the user program:

- Automatic creation of the user program for all CFC charts
- Transfer of the user program to the device of the target system

#### Using CFC

You use CFC in particular for process engineering or structured automation solutions.

You interconnect, for example, blocks you have created yourself or instructions supplied by CFC with the operands of your target system.

With the help of a CFC chart, even a complex user program remains clearly laid out.

You can monitor process values as well as input and output parameters of the instructions and blocks online for testing.

---

**See also**

[Type and instance](#type-and-instance)
  
[Configuration options for CFC charts](#configuration-options-for-cfc-charts)
  
[Overview for configuration of CFC charts](#overview-for-configuration-of-cfc-charts)
  
["CFC" Editor](#cfc-editor)
  
[Basic settings for CFC charts](#basic-settings-for-cfc-charts)
  
[Icons in CFC](#icons-in-cfc)

### Configuration options for CFC charts

#### Configuring CFC charts

In the "CFC" Editor, you configure the CFC charts either graphically by dragging and dropping with the mouse or textually in the form of a list.

You can change from one configuration method to the other at any time with no restrictions.

When you create user programs with CFC, we recommend that the block programming is complete and that the block types are no longer changed.

#### Graphic configuration of CFC charts in "Data flow" mode

When you configure graphically in "data flow" mode, you insert instructions and blocks in the CFC chart from a library, for example.

You interconnect the input and output parameters with drag-and-drop, via a mouse click or by using a keyboard shortcut and click.

To document the CFC chart, you use text boxes.

The advantages of graphic configuration compared with textual configuration are as follows:

- Simple wiring of input and output parameters using drag-and-drop, a mouse click, or a keyboard shortcut
- Graphic representation of the signal path
- Outline of complex charts in chart partitions

#### Textual configuration of CFC charts in "Control flow" mode

With the textual configuration method in "Control flow" mode, you insert the instructions and blocks in a list.

The input and output parameters are not interconnected graphically, but you will assign values to the parameters.

The advantages of textual configuration compared with graphic configuration are as follows:

- Simple adaptation of the run sequence
- Simple parameter assignment

---

**See also**

[Basics of CFC](#basics-of-cfc)
  
["CFC" Editor](#cfc-editor)

### Instructions and blocks

With CFC, you create user programs by simple placement, parameter assignment and interconnection of instructions and blocks in the CFC charts.

When you create user programs with CFC, we recommend that the block programming is complete and that the block types are no longer changed.

#### Distinction between instructions and blocks

The designation depends on how they are created and the target system, for example.

**Instructions**

Instructions are predefined, basic functions, such as logic operations and arithmetic functions.

Instructions are program components of CFC and are available in the "Instructions" task card.

**Blocks**

You can create blocks yourself or use predefined blocks from the library.

- Function blocks (FB):

  Function blocks are code blocks that store their values permanently in instance data blocks.

  The values are still available after the block has been processed.

  The data are available and accessible during processing across multiple cycles.
- Functions (FC):

  Functions contain program routines for recurring tasks.

  They have no data memory in which values of block parameters can be stored.

  Therefore, when a function is called, all formal parameters must be assigned actual parameters. A data block is not required.

You can also interconnect the parameters of function blocks and functions with elements of global data blocks.

**Blocks for the S7 target system**

There are other block types in the S7 target system.

Additional information: "Working with CFC charts for S7 > Blocks in CFC charts for S7"

#### Properties of instructions and blocks

There are additional terms associated with instructions and blocks:

**Type and instance**

- A type is a reusable, pre-defined block.

  The block can be provided in a library or you can create it yourself.
- An instance is a use of a type, for example, in the CFC chart.

Additional information: "[Type and instance](#type-and-instance)"

**Generic instructions**

The number of inputs is variable in generic instructions and can be changed in the CFC chart, for example, AND logic operation.

Additional information: "[Adding or removing input parameters](#adding-or-removing-input-parameters)"

**Family**

The instructions/blocks are grouped according to their function characteristics, the instruction or block families, e.g. CONVERT.

### Type and instance

#### Type-instance concept

Configuration in CFC is made easier by using types or their instances.

A block type is a reusable, pre-defined function that you yourself create or copy from a library.

You create a block instance by inserting a block type into a CFC chart.

The advantage of this type-instance concept is that you can implement any central change of the type at a later time at all instances.

#### Type

A type can be defined by the following options:

- When inserting a block from the "Program blocks" folder in the project tree into a CFC chart.

  The block in the "Program blocks" folder is imported into CFC and defined as type.

  The "copy" in the CFC chart is an instance of this type.
- A block that you want to define as type is saved in one of the libraries.

  This can be a block from the "Program blocks" folder, for example, or from a CFC chart.

  If this saved block is added to a CFC chart from the library, the block is imported in CFC and defined as type.

  The "copy" in the CFC chart is an instance of this type.

A type can already be defined as supplied block in a library.

**Central type change**

When you change the type, you can update the instances of this type in all CFC charts of a target system.

Additional information: "[Central change of a type](#central-change-of-a-block-type)"

> **Note**
>
> **Delete block type: Check instances**
>
> First delete the instances followed by the block type.
>
> If you delete a type of which an instance still exists, then you will no longer be able to compile the CFC charts of this target system.
>
> You may find the information on the missing block types in the alarms of the Inspector window or in the "Chart sequence & extras" editor.

#### Instance

An instance is the use of a type in the CFC chart.

You can create any number of instances from a type.

Within a CFC chart, each instance has a unique name. The instance name consists of the name of the CFC chart in which the instance is located, the name of the type and the instance number.

The instance normally inherits the defaults of the type, for example, the default values of the parameters.

During configuration, you can enter individual initial values, change the instance name and interconnect the input and output parameters.

---

**See also**

[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)
  
[Creating a block type for CFC](#creating-a-block-type-for-cfc)

### Hierarchical CFC charts

You can create CFC charts in hierarchical structures.

In doing so, you add one or more CFC charts as "subcharts" into a "basic chart".

#### Nesting depth

A subchart can contain additional subcharts so that you are creating a nested hierarchy.

Maximum nesting depth of hierarchical CFC charts:

- 8 hierarchy levels:

  Basic chart + 7 subcharts

#### Managing hierarchical CFC charts

When inserting a CFC chart as subchart, a copy of the inserted chart is created under the basic chart.

**Editing subcharts**

The original, added CFC chart and the newly created subchart are edited independently of one another.

Changes in the subchart do not affect the originally inserted CFC chart and vice versa.

**Copying or moving subcharts**

The hierarchical CFC charts can be handled like blocks.

You can copy or move subcharts within a chart or to another basic chart.

If the selected subchart contains additional subcharts, these are copied or moved as well.

**Deleting hierarchical charts**

When you delete a CFC chart that was inserted as subchart, the subchart is retained.

When you delete a subchart that contains additional subcharts, these charts are deleted as well.

**Replacing subchart**

You can replace a hierarchical CFC chart with a different hierarchical CFC chart.

If possible, the existing interconnections are retained.

The position in the run sequence is not changed.

Additional information: "[Replacing hierarchical CFC charts](#replacing-hierarchical-cfc-charts)"

**Changing layers**

You can elevate a subchart to the root level in the "Charts" folder.

In this case, however, the chart interface may not have an external interconnection.

Additional information: "[Moving subcharts to the root level](#moving-subcharts-to-the-root-level)"

#### Representation in the project tree

Hierarchical charts are displayed in the project tree in the "Charts" folder.

A basic chart is indicated using a folder icon.

The actual basic chart and all subcharts are displayed in this folder. When a subchart contains additional subcharts, this subchart is also displayed as a directory.

To open a basic chart, double-click the "Chart" icon below the chart name: ![Representation in the project tree](images/132539453323_DV_resource.Stream@PNG-de-DE.png)

**Example**

![Representation in the project tree](images/132539144971_DV_resource.Stream@PNG-en-US.png)

The chart "CFC_2" is a basic chart that contains the subcharts "CFC_1", "CFC_2", "CFC_2_1", "CFC_2_2" and "CFC_4".

The subchart "CFC_2_1", in turn, is the basic chart for the contained subcharts "CFC_2_2" and "CFC_4".

The subcharts called "CFC_4" were created as independent copies by inserting the chart "CFC_4". To avoid confusion, assign meaningful names to the subcharts.

#### Visualization of the subcharts in the basic chart

A subchart is visualized in a higher-level chart similar to a block with "subchart header" and "chart interface".

However, a different icon is used in the "subchart header".

The following figure shows a section of the subchart "CFC_2_1" that is included in the basic chart "CFC_2".

The subchart "CFC_2_1" contains the subcharts "CFC_4" and "CFC_2_2":

- Only the standard parameter EN exists at the subchart "CFC_4".
- The parameters that are defined in the chart interface are displayed in the subchart "CFC_2_2".

![Visualization of the subcharts in the basic chart](images/132542456715_DV_resource.Stream@PNG-de-DE.png)

#### Navigation within the hierarchy

The following navigation options are available in the CFC charts:

- Navigation "down":

  - With double-click on the subchart icon.
  - Select the subchart icon and execute the "Open" menu command from the shortcut menu.
- Navigation "up":

  - Execute the "Open parent chart" from the shortcut menu in the opened subchart.
  - Double-click a sheet bar entry that contains an interconnection to the interface of this subchart.

    Use the entry "Back" in the shortcut menu to jump back to the last selected parameter.

#### Interface of the CFC chart

Hierarchical CFC charts and standard CFC charts have an interface structure that is similar to that of blocks. This means that these CFC charts can be configured and interconnected externally similar to blocks.

The chart interface is displayed in the top area of the data flow and control flow section in the "CFC" editor. When the "Interface" area is hidden, enlarge the area with the mouse or click the unhide icon: ![Interface of the CFC chart](images/132651805963_DV_resource.Stream@PNG-de-DE.png)

New parameters can be added, modified or deleted in the Input, Output, InOut sections of the chart interface.

Interconnections of interface parameters with blocks within the CFC chart are displayed in the sheet bar of the chart with connectors.

Additional information:

- "[Adding, editing and sorting parameters of the chart interface](#adding-editing-and-sorting-parameters-of-the-chart-interface)"
- "[Interconnections to parameters of the chart interface](#interconnections-to-parameters-of-the-chart-interface)"

#### Jump to the interconnected parameter

The shortcut menu of a parameter at the subchart icon contains the menu command "Track signal".

The menu command "Track signal" opens the subchart and selects the interconnected parameter of the block.

You use this command to track the signal from the chart interface into the inside of the chart.

If multiple parameters are interconnected, select the required parameter from the shortcut menu.

Use the entry "Back" in the shortcut menu to jump back to the last selected parameter.

#### Interconnections in a hierarchical CFC chart

You configure the interconnections in a hierarchical chart via the chart interface or directly to blocks in the chart.

When you move a block with an interconnection to the chart interface to a different CFC chart, the existing interconnection to the interface is deleted.

The following rules apply to interconnections between the parameters in the block and in the chart interface:

- You can only interconnect parameters from the same section of the chart and block interfaces.

  Example: An Input parameter of the chart interface is interconnected with an Input parameter at the block.

  Alternatively, you can interconnect the Input parameter of a block with an InOut parameter of the chart interface.
- The data types of the interconnected parameters and of the blocks are subject to the same conditions.

  On the S7 target system, it is not possible to interconnect individual elements of a STRUCT parameter type with the chart interface.
- Interface parameters of the Output type cannot be configured directly.

  Enter the value at the interconnected output parameter.

#### Run sequence

- The run sequence of the blocks is bound to the CFC chart.

  Hierarchical CFC charts can be handled like objects within the run sequence.
- Subcharts inherit the task assignment of the basic chart by default.

  If a subchart that has further subcharts has a different task assignment, this different task assignment is inherited by all child subcharts.
- The "Reduction ratio" and "Phase shift" functions are only available for basic charts.

  The subcharts are called in the run sequence in accordance with their associated basic chart.
- The "Enable chart" function is available for subcharts.

  Requirements for processing the lower-level subcharts:

  - The "Enable chart" setting is also set in the basic chart.

---

**See also**

[Creating a subchart for a hierarchical CFC chart](#creating-a-subchart-for-a-hierarchical-cfc-chart)
  
[Overview of textual interconnections](#overview-of-textual-interconnections) 
  
[Managing CFC charts and groups](#managing-cfc-charts-and-groups)

### Protection from unintentional access to CFC charts

#### Overview

To protect a CFC chart or hierarchical CFC chart from unintentional editing, you can protect the chart with a password.

The contents of the CFC chart can only be viewed after the correct password has been entered.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password serves only to protect a CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts |  |

#### Principle

You will be asked for the password when you open the CFC chart.

The password-protected CFC chart can be handled as normal as long as it remains open in the editor.

Once password protection has been set, the current password must be entered to change or remove the password.

**Hierarchical charts**

Setting or removing a password for a basic chart does not affect the passwords of subcharts.

If subcharts are password-protected, you will need to enter the password again when you open these charts.

As soon as a password is assigned to a basic chart, the behavior changes:

- As long as the basic chart is closed, the hierarchical view remains hidden in the project tree
- For subcharts which do not have their own password, the "Access protection" entry in the shortcut menu is hidden.

  The "Protection" button is disabled in the chart properties.

  To protect one of the subcharts from unintentional editing, open the subchart. In the project tree, the "Access protection" entry is displayed in the shortcut menu of the subchart. The "Protection" button is enabled in the chart properties.

#### Properties of a CFC chart with password protection

Without a valid password, you only have limited access to the chart:

- The content of charts and subcharts is not visible.
- References to chart contents via direct object selection with the mouse or text input are not possible.
- Compiling and loading is possible without entering a password.
- During a type update, instances in password-protected charts are also updated.

  Password input is not necessary for this.
- You can copy the chart without entering the password.

  The copied chart has the same password, however.
- The display of the chart properties in the Inspector window is limited.

  Users can only change the name and comment.

  All other properties are either not visible or cannot be changed.
- The chart interface is displayed as read-only.

  The following parameter assignments can be applied:

  - Value
  - "Invisible" property
  - Test settings
  - External interconnections to the chart interface
- The printout comprises only the chart interface and the limited information on the chart properties.

#### More information

- [Activating password for a CFC chart](#activating-password-for-a-cfc-chart)
- [Changing or deactivating password for a CFC chart](#changing-or-deactivating-password-for-a-cfc-chart)
- [Opening a password-protected CFC chart](#opening-a-password-protected-cfc-chart)

### Multilingual texts in CFC

#### Multilingual

The following languages are present in a project:

- Editing language

  Each project has an editing language.

  Any text you enter is always created in the editing language.
- Project language

  Project languages are all languages in which a project will later be used.

  Based on the editing language, all texts can be translated into the various project languages.

Editing language and project languages are configured in the project tree folder "Languages & resources" > "Project languages".

> **Note**
>
> **User interface**
>
> The language of the user interface does not depend on the editing and project language.

#### Multilingual texts in CFC

You can manage the following types of text in CFC in several languages:

- Comments from:

  - CFC chart
  - Instance
  - Parameters
- Text block

You enter these texts in the "CFC" editor when you create the CFC chart in the editing language.

These texts are then translated into the required project languages in the project text editor of the TIA Portal.

#### Translating texts

There are different ways of translating texts:

- Translating texts directly

  You can enter the translations for the individual project languages directly in the "Project texts" table.
- Translating texts using reference texts

  For smaller amounts of text, you can change the editor language.

  All the text cells are filled again with the default values and can be filled in the current language.

More information in the information system of the TIA Portal:

- "Editing project data > [Working with multi-language projects](Editing%20project%20data.md#working-with-multi-language-projects)"

#### User interface language: Installing language packs

You can install additional interface languages using TIA Administrator:

1. Install the TIA Portal language packs for the desired user interface languages.
2. Select the tiles for the "SIMATIC STEP 7 CFC" language pack.
3. Load and install the CFC language pack for the installed TIA Portal user interface languages.

### Copying objects

#### Copy and paste

You can copy within the TIA Portal either by dragging with the mouse or using the "Copy" and "Paste" commands.

If you want to copy an object in the same area by dragging it with the mouse, you can do this by holding down the <Ctrl> key.

All selected objects are copied.

#### Copying objects within a device

If you copy one or more objects within a device, the copies are numbered in ascending order.

If an object with this naming convention already exists, this number is skipped.

**Example:**

The chart folder contains the objects "Tag", "Tag_1" and "Tag_34".

If you copy "Tag", the copy is given the name "Tag_2".

If you copy "Tag_34", the copy is given the name "Tag_3".

#### Copying objects to a different device

If you copy one or more objects to a different device, the object names are not changed.

If there is already an object with the same name at the destination location, you will be prompted to decide what to do.

#### Copying objects to a different project

To copy objects from one project to another, open the second project in a second instance of the TIA Portal.

When you copy, the principles are the same as when copying to a different device.

#### Moving objects

To move objects from one project to another, copy the objects.

Then delete the source object manually.

---

**See also**

[Copying instructions, blocks and charts](#copying-instructions-blocks-and-charts)
  
[Overview of textual interconnections](#overview-of-textual-interconnections)

### CFC naming conventions

#### Permitted characters

Special characters and umlauts are allowed in chart names and in instruction names.

However, to avoid compatibility problems, only use the following characters:

- Characters from "a" to "z"
- Numbers from "0" to "9"
- Underscore "_" for separation

#### Control characters for path and hierarchy information

There are control characters reserved for path and hierarchy information and that are used, for example, in "control flow" or in connectors.

The control characters are relevant only for path and hierarchy information. Outside this context, the control characters are interpreted as permitted parts of a name.

The following table shows the reserved control characters:

| Control character |  | Explanation |
| --- | --- | --- |
| Dot | . | Reserved for path and hierarchy information.  - The dot indicates parameters at instructions/blocks. - The slash represents hierarchical relationships.   Example:  The expression "Chart_1\Block_1.IN_1" addresses the input parameter "IN_1" of the instruction "Block_1" in chart "Chart_1". |
| Slashes | / and \ |  |
| Quotes | " | Reserved for starting and completing a character string. |
| Percent sign | % | Reserved for starting address ranges. |
| Dollar sign | $ | Reserved as the escape character.  The control character following this is interpreted as a permitted character. |

#### Control characters as parts of names

If you edit chart and instruction names with control characters in the path or hierarchy information, use the following syntax:

- Enter the name in quotes.

  Example:

  - "Motor1.Temperature"
- Precede the control character with the escape character $.

  Example:

  - Motor1$.Temperature

**Example**

In the CFC chart "TempControl", the "Motor1.Temperature" instruction is configured for temperature control of a motor.

The naming convention of the plant owner defines the dot as a separator.

To address the output parameter "OUT" of the instruction in "control flow", the following notations are permitted:

- TempControl\"Motor1.Temperature".OUT
- TempControl\Motor1$.Temperature.OUT

## Elements and basic settings

This section contains information on the following topics:

- [Basic settings for CFC charts](#basic-settings-for-cfc-charts)
- ["CFC" Editor](#cfc-editor)
- ["Chart sequence & extras" Editor](#chart-sequence-extras-editor)
- [Keyboard operation in CFC](#keyboard-operation-in-cfc)
- [Icons in CFC](#icons-in-cfc)

### Basic settings for CFC charts

The basic settings of CFC charts refer to all charts that you have configured in a target system.

#### Default settings for new charts

You define the basic settings for new charts in the "Options > Settings > Charts" menu.

You can change the properties of each CFC chart at any time regardless of the basic settings.

**Basic settings**

The following settings are specified when you create new charts:

- Independent of the target system:

  - Color of interconnection lines
- Dependent on the target system:

  - Appearance of the CFC charts, e.g. sheet bar settings and layout
  - If necessary, additional settings, such as the reserved number ranges for user blocks

**Changing basic settings**

Changes to the basic settings only affect newly created CFC charts.

Existing CFC charts remain unchanged.

**Task assignment of CFC charts**

Newly created CFC charts have an assigned main task.

Depending on the target system, you change this task assignment in the "Chart sequence & extras" editor.

Additional information: "[Runtime model](#runtime-model)"

#### Representation of the CFC chart in the editor

If you adapt the zoom factor or the representation of the grid lines in a CFC chart, these changes apply to all CFC charts you open from this point onwards.

This behavior also applies following a program restart.

**Zoom function in the CFC chart**

You zoom in the CFC chart with the <Ctrl> key and the mouse wheel.

The zoom focuses on the position of the mouse pointer.

Alternative zoom options:

- Keyboard shortcuts <Ctrl+"+"> and <Ctrl+"-">
- Zoom scale at the bottom of the editor window
- % entry or selection in the drop-down list

  Position: in the toolbar or next to the zoom scale

---

**See also**

[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Printing a CFC chart](#printing-a-cfc-chart)
  
[CFC views](#cfc-views)
  
[Extending a CFC chart](#extending-a-cfc-chart)
  
["Chart sequence & extras" Editor](#chart-sequence-extras-editor)
  
"Chart sequence & extras" editor for S7
  
[Basics of CFC](#basics-of-cfc)

### "CFC" Editor

In the "CFC" Editor, you configure CFC charts graphically or as a list.

The two configuration methods have the same priority. You can change from one configuration method to the other at any time.

#### Open "CFC" editor

You open the "CFC" editor for the first time by adding a new chart.

1. Open the "Charts" folder in the "Project tree".
2. Double-click "Add new chart".

   A new CFC chart is created and opened in the editor.
3. To open an already-created CFC chart in the editor, double-click the chart.

The "CFC" editor always contains a CFC chart when it is opened.

#### Layout of the "CFC" Editor

![Layout of the "CFC" Editor](images/130578169355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Work area: Display area of the "Data flow" and "Control flow" tabs |
| ② | "Data flow" tab |
| ③ | "Control flow" tab |
| ④ | Task cards |
| ⑤ | Inspector window |
| ⑥ | Detail view |
| ⑦ | "Charts" folder |
| ⑧ | Project tree |

#### Work area with the "Data flow" and "Control flow" tabs

- In the "Data flow" tab, you configure a CFC chart graphically.
- In the "Control flow" tab, you specify the run sequence of the instructions and blocks in the CFC chart.

  You also display the configured instructions and blocks with their input and output parameters in form of a list.

  You also select the input and output parameters for testing.
- Both in "Control flow" and "Data flow" mode, you can insert, interconnect and set parameters for instructions and blocks.

#### Task cards

| Task card | Use |
| --- | --- |
| Instructions | Access to all instructions provided by CFC. |
| Libraries | Access to the project library and global libraries. |
| Testing | Configure test settings. |

> **Note**
>
> **Depending on the target system**
>
> The availability and the content of the task cards depend on the target system for which you are configuring.

#### Inspector window

Additional information on a selected object or executed actions are displayed in the Inspector window.

The Inspector window includes the following elements or functions:

- Different tabs, e.g. "Properties", "Info", "Diagnostics":

  Information on selected objects is displayed and editable properties can be changed.

  In the "General" tab, you can enter additional details on the CFC chart, a comment or version information, for example.
- Additional lower-level tabs in the "Info" and "Diagnostics" tabs

  Alarms and warnings are displayed in the "Info" tab, for example, during compiling or loading.
- Navigation functions within the tabs

You use the Inspector window for the following tasks:

- Set parameters of the instructions/blocks.
- Select parameters of the instructions/blocks for testing.
- Manage interconnections

> **Note**
>
> **Depending on the target system**
>
> The properties or options in the Inspector window depend on the target system for which you are configuring.

---

**See also**

[Basic settings for CFC charts](#basic-settings-for-cfc-charts)
  
[Configuration options for CFC charts](#configuration-options-for-cfc-charts)
  
Overview of CFC instructions
  
Testing CFC charts in the S7 system
  
[Selecting parameters for testing](#selecting-parameters-for-testing)
  
[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
["Chart sequence & extras" Editor](#chart-sequence-extras-editor)
  
[Overview for configuration of CFC charts](#overview-for-configuration-of-cfc-charts)
  
[Keyboard operation in CFC](#keyboard-operation-in-cfc)
  
[Icons in CFC](#icons-in-cfc)

### "Chart sequence & extras" Editor

#### Overview

In the "Chart sequence & extras" editor, you configure the run sequence of charts.

The assignment of the instructions/blocks to the tasks and therefore the run sequence within the target system is also displayed.

> **Note**
>
> **Depending on the target system**
>
> The availability and the content of the tabs depend on the target system for which you are configuring.

#### Tab

You are working in various tabs of the editor.

Depending on the target system, the following tabs are displayed:

- "Chart sequence": Run sequence of the CFC charts
- "Task assignment": Tasks and assigned blocks
- "Tag interconnections": Points of use of interconnected tags and global data blocks
- "Target system settings": Basic settings for chart folder
- "Block instances": Block types with their associated instances

Tabs that are not supported by the target system are not visible.

**Information on S7 target systems**

- "Working with CFC charts for S7 > "Chart sequence & extras" editor for S7"

#### Table layout

In most tabs, you are working in a table.

Depending on the selected tab, you can adapt the representation of the columns in the table.

- Column width:

  - You change the width of the individual columns with the mouse.
  - You optimize the column width automatically via the shortcut menu.
- To change the sequence of the columns, move a column header with a drag-and-drop operation.

---

**See also**

[Basic settings for CFC charts](#basic-settings-for-cfc-charts)
  
["CFC" Editor](#cfc-editor)
  
[Keyboard operation in CFC](#keyboard-operation-in-cfc)
  
[Icons in CFC](#icons-in-cfc)
  
[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)
  
[Adapting the run sequence](#adapting-the-run-sequence)

### Keyboard operation in CFC

In the TIA Portal and in CFC, keyboard shortcuts are also available for many functions.

Alternatively, you can use user-defined keyboard shortcuts.

#### Keyboard shortcuts in CFC

The following shortcuts enable operation without the mouse:

| Function | Keyboard shortcut | Menu command |
| --- | --- | --- |
| Go to the next open CFC chart | <Ctrl+F6> |  |
| Go to the previous open CFC chart | <Ctrl+Shift+F6> |  |
| Go to the next chart partition, if more than one chart partition has been created | <Shift+PgDn> |  |
| Go to the previous chart partition, if more than one chart partition has been created | <Shift+PgUp> |  |
| Project tree:  Go to the next CFC chart | <Ctrl+Arrow up> |  |
| Project tree:  Go to the previous CFC chart | <Ctrl+Arrow down> |  |
| Open/close project tree | <Ctrl+1> | View > Project tree |
| Open/close task card | <Ctrl+3> | View > Task card |
| Open/close detail view | <Ctrl+4> | View > Detail view |
| Open/close Inspector window | <Ctrl+5> | View > Inspector window |
| Display or hide reference projects | <Ctrl+9> |  |
| Download project data to the device | <Ctrl+L> | Online > Download to device |
| Open Help | <F1> | Help > Show help |
| Open help on a block | <Shift+F1> |  |

#### TIA Portal: Operation with the keyboard

You can find an overview of all keyboard shortcuts and the option of assigning user-defined keyboard shortcuts in the settings of the TIA Portal:

1. Select the "Settings" command in the "Options" menu.

   The settings of the TIA Portal are displayed.
2. Open the "Keyboard shortcuts" entry in the area navigation.

   You can see an overview of all default and user-defined keyboard shortcuts that are valid for the currently installed products.

More information in the TIA Portal Information System:

- "User interface and operation > [Keyboard operation in the TIA Portal](Introduction%20to%20the%20TIA%20Portal.md#basic-functions-of-the-tia-portal)"

  You learn how to navigate in the TIA Portal using the keyboard, edit objects and customize the TIA Portal to your needs.

---

**See also**

["CFC" Editor](#cfc-editor)
  
["Chart sequence & extras" Editor](#chart-sequence-extras-editor)

### Icons in CFC

The tables below show the icons that you use when working with CFC and describe their meaning.

- TIA Portal project tree: CFC charts

  - Icons under the "Charts" entry
  - Online/offline comparison status
- Project tree / Trend editor: Trend display/Dynamic display
- Project tree / Toolbars: Other icons
- CFC editor: Toolbar
- CFC editor: Chart view in the "Data flow" tab

  - Icons at the block instances
  - Interconnections
  - Other icons
- "Chart sequence & extras" editor

  - General
  - "Chart sequence" tab
  - "Textual interconnections" tab (S7 target system)
  - "Block types" tab (S7 target system)
- "Update blocks" dialog

#### TIA Portal project tree: CFC charts

**Icons under the "Charts" entry**

| Icon | Meaning |
| --- | --- |
| ![TIA Portal project tree: CFC charts](images/161100152587_DV_resource.Stream@PNG-de-DE.png) | Navigation area for managing CFC charts |
| ![TIA Portal project tree: CFC charts](images/161099698827_DV_resource.Stream@PNG-de-DE.png) | Opens the "Chart sequence & extras" editor |
| ![TIA Portal project tree: CFC charts](images/160947545739_DV_resource.Stream@PNG-de-DE.png) | Creates a new CFC chart. |
| ![TIA Portal project tree: CFC charts](images/161098110603_DV_resource.Stream@PNG-de-DE.png) | CFC chart:  Opens the chart in the CFC editor. |
| ![TIA Portal project tree: CFC charts](images/161099707275_DV_resource.Stream@PNG-de-DE.png) | Hierarchical CFC chart:  Icon for a group of hierarchical charts, consisting of the basic chart and subcharts |
| ![TIA Portal project tree: CFC charts](images/132539453323_DV_resource.Stream@PNG-de-DE.png) | Hierarchical CFC chart:  Opens the basic chart in the CFC editor. |
| ![TIA Portal project tree: CFC charts](images/161098119051_DV_resource.Stream@PNG-de-DE.png) | Password-protected CFC chart  The password serves only to protect a CFC chart from unintentional editing. |
| ![TIA Portal project tree: CFC charts](images/142193806091_DV_resource.Stream@PNG-de-DE.png) | Password-protected hierarchical chart  The password of basic charts does not affect the subcharts contained therein.  To protect the subchart of a protected basic chart from unintentional editing, open the subchart. In the project tree, the "Access protection" entry is displayed in the shortcut menu of the subchart. |

**Online/offline comparison status**

The icons for the status display identify whether changes exist in the project and a download to the device is required.

| Icon | Meaning |
| --- | --- |
| ![TIA Portal project tree: CFC charts](images/133246329739_DV_resource.Stream@PNG-de-DE.png) | The CFC chart exists in the project but not in the device. |
| ![TIA Portal project tree: CFC charts](images/133245771659_DV_resource.Stream@PNG-de-DE.png) | The basic chart exists in the project but not in the device. |
| ![TIA Portal project tree: CFC charts](images/133247165451_DV_resource.Stream@PNG-de-DE.png) | The CFC chart is identical in the project and device. |
| ![TIA Portal project tree: CFC charts](images/133241479947_DV_resource.Stream@PNG-de-DE.png) | The basic chart is identical in the project and device. |
| ![TIA Portal project tree: CFC charts](images/133246326027_DV_resource.Stream@PNG-de-DE.png) | The CFC chart has been changed in the project and exists in the device but is different. |
| ![TIA Portal project tree: CFC charts](images/133245775371_DV_resource.Stream@PNG-de-DE.png) | The basic chart has been changed in the project and exists in the device but is different. |
| ![TIA Portal project tree: CFC charts](images/133241476235_DV_resource.Stream@PNG-de-DE.png) | The basic chart is identical in the project and device, but a subchart has been changed. |

#### Project tree / Trend editor: Trend display/Dynamic display

| Icon | Meaning |
| --- | --- |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/161100130827_DV_resource.Stream@PNG-de-DE.png) | Project tree:  Navigation area for the "Trend display", "Dynamic display", "Force table" components |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/160947545739_DV_resource.Stream@PNG-de-DE.png) | Project tree:  Creates a new trend display or dynamic display |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/161100193035_DV_resource.Stream@PNG-de-DE.png) | Project tree:  Opens the dynamic display in the table editor |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/161100406283_DV_resource.Stream@PNG-de-DE.png) | Project tree:  Opens the trend display in the trend editor |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/161100173835_DV_resource.Stream@PNG-de-DE.png) | Trend editor:  Adds an analog axis in the trend display |
| ![Project tree / Trend editor: Trend display/Dynamic display](images/161100182283_DV_resource.Stream@PNG-de-DE.png) | Trend editor:  Adds a digital axis in the trend display |

#### Project tree / Toolbars: Other icons

| Icon | Meaning |
| --- | --- |
| ![Project tree / Toolbars: Other icons](images/161100122379_DV_resource.Stream@PNG-de-DE.png) | Opens the force table.  You find the entry in the project tree under "Charts - Trend/dynamic display & force table" |
| ![Project tree / Toolbars: Other icons](images/161099921931_DV_resource.Stream@PNG-de-DE.png) | Refreshes the display  The icon is used in multiple editors and views. |
| ![Project tree / Toolbars: Other icons](images/144473179531_DV_resource.Stream@PNG-de-DE.png) | TIA Portal toolbar:  Split editor area horizontally or vertically  Use the split editor areas to drag interconnections between charts or chart partitions. |

#### CFC editor: Toolbar

| Icon | Meaning |
| --- | --- |
| ![CFC editor: Toolbar](images/142197172363_DV_resource.Stream@PNG-de-DE.png) | List of created chart partitions in the open CFC chart  Clicking on an entry changes the view to the selected chart partition. |
| ![CFC editor: Toolbar](images/144137243915_DV_resource.Stream@PNG-de-DE.png) | Create new chart partition |
| ![CFC editor: Toolbar](images/142195683979_DV_resource.Stream@PNG-de-DE.png) | Delete displayed chart partition  Requirement: The CFC chart consists of at least 2 chart partitions. |
| ![CFC editor: Toolbar](images/161097468555_DV_resource.Stream@PNG-de-DE.png) | Zoom in /out on the display of the CFC chart:  - Zoom in - Fit chart to work area - Fit selection to work area - Zoom out |
| ![CFC editor: Toolbar](images/142195687691_DV_resource.Stream@PNG-de-DE.png) | Open displayed CFC chart in a second editor window  This can be used, for example, to simultaneously edit two chart partitions of the same CFC chart. |
| ![CFC editor: Toolbar](images/161096963723_DV_resource.Stream@PNG-de-DE.png) | Select sheet bar view:  - Static sheet bars - No sheet bars - Dynamic sheet bars |
| ![CFC editor: Toolbar](images/161097061771_DV_resource.Stream@PNG-de-DE.png) | Select display of sheet bar entries:  - One-line - Two-line |
| ![CFC editor: Toolbar](images/161097070219_DV_resource.Stream@PNG-de-DE.png) | Show / hide sheet borders  Requirement: The chart or chart partition is divided among at least 2 sheets. |
| ![CFC editor: Toolbar](images/161097091467_DV_resource.Stream@PNG-de-DE.png) | Show / hide sheet numbers |
| ![CFC editor: Toolbar](images/161097099915_DV_resource.Stream@PNG-de-DE.png) | Show / hide grid in chart background |
| ![CFC editor: Toolbar](images/160947553931_DV_resource.Stream@PNG-de-DE.png) | Show / hide position number in the run sequence above the block header. |
| ![CFC editor: Toolbar](images/160950105099_DV_resource.Stream@PNG-de-DE.png) | Show / hide assigned task above the block header. |
| ![CFC editor: Toolbar](images/161097133963_DV_resource.Stream@PNG-de-DE.png) | Show / hide unit of measurement of the parameters  Requirement: A unit of measurement has been configured for the parameter. |
| ![CFC editor: Toolbar](images/132686500363_DV_resource.Stream@PNG-de-DE.png) | Signal flow highlighting: The signal flow is highlighted in color.  Requirement: The instance of a block or subchart has been selected. |
| ![CFC editor: Toolbar](images/130610953099_DV_resource.Stream@PNG-de-DE.png) | Change between the display of parameter names and comments  Requirement: A comment has been entered for the parameter. |
| ![CFC editor: Toolbar](images/132653846667_DV_resource.Stream@PNG-de-DE.png) | Insert new subchart |
| ![CFC editor: Toolbar](images/161097157259_DV_resource.Stream@PNG-de-DE.png) | Insert text box |
| ![CFC editor: Toolbar](images/130610409739_DV_resource.Stream@PNG-de-DE.png) | Optimize run sequence in a CFC chart according to the signal flow |
| ![CFC editor: Toolbar](images/132689015819_DV_resource.Stream@PNG-de-DE.png) | Place blocks in the displayed chart according to the data flow |
| ![CFC editor: Toolbar](images/161095935883_DV_resource.Stream@PNG-de-DE.png) | Show selected object in the control flow |
| ![CFC editor: Toolbar](images/161097460107_DV_resource.Stream@PNG-de-DE.png) | Task assignment of the open CFC chart |
| ![CFC editor: Toolbar](images/144083943435_DV_resource.Stream@PNG-de-DE.png) | Monitoring on/off  Activates the display of the current values during testing.  If you have connected online, all input and output parameters selected for testing are supplied with current values from the device and also highlighted in color. |
| ![CFC editor: Toolbar](images/161080908939_DV_resource.Stream@PNG-de-DE.png) | Control flow:  Collapse display and show only the top elements |
| ![CFC editor: Toolbar](images/161080917387_DV_resource.Stream@PNG-de-DE.png) | Control flow:  Expand display and show all lower-level elements |
| ![CFC editor: Toolbar](images/161095825035_DV_resource.Stream@PNG-de-DE.png) | Control flow:  Show selected object in data flow |

#### CFC editor: Chart view in the "Data flow" tab

**Icons at the block instances**

| Icon | Meaning |
| --- | --- |
| ![CFC editor: Chart view in the "Data flow" tab](images/161099784331_DV_resource.Stream@PNG-de-DE.png) | Identifies the instance of a function block (FB) in the open chart. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161099907979_DV_resource.Stream@PNG-de-DE.png) | Identifies the instance of a function (FC) in the open chart. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161098102155_DV_resource.Stream@PNG-de-DE.png) | Identifies the instance of a subchart in the open chart. |
| Without icon /     ![CFC editor: Chart view in the "Data flow" tab](images/161099784331_DV_resource.Stream@PNG-de-DE.png) / ![CFC editor: Chart view in the "Data flow" tab](images/161099907979_DV_resource.Stream@PNG-de-DE.png) | Instances of instructions can be marked with different icons or only with the instruction name.  Identifying instruction instances: The entry "Go to block type" is missing in the shortcut menu of instruction instances. |
| ![CFC editor: Chart view in the "Data flow" tab](images/173868938379_DV_resource.Stream@PNG-de-DE.png) | Colored border:  The instance has been positioned automatically in the chart. |
| ![CFC editor: Chart view in the "Data flow" tab](images/173868934411_DV_resource.Stream@PNG-de-DE.png) | Instances with a colored background:  Not enough space for a complete display or the objects lie on top of each other.  Move the instance or increase the sheet size. |
| ![CFC editor: Chart view in the "Data flow" tab](images/61425315723_DV_resource.Stream@PNG-de-DE.png) | Block is not processed.  The reason is that the enable input "EN" at the block is "FALSE" or the "Enable chart" option of the chart has been disabled. |
| ![CFC editor: Chart view in the "Data flow" tab](images/61427602955_DV_resource.Stream@PNG-de-DE.png) | Block is processed conditionally.  The reason is that the enable input "EN" at the block or the "Enable chart" option of the chart has been interconnected. |
| ![CFC editor: Chart view in the "Data flow" tab](images/16251709451_DV_resource.Stream@PNG-de-DE.png) | An interconnected parameter is hidden. |
| ![CFC editor: Chart view in the "Data flow" tab](images/16251712651_DV_resource.Stream@PNG-de-DE.png) | A non-interconnected parameter is hidden. |
| ![CFC editor: Chart view in the "Data flow" tab](images/173863540875_DV_resource.Stream@PNG-de-DE.png) | Add additional input parameters at an instruction instance  The icon is hidden in the following cases:  - Addition is not possible. - The maximum number of possible input parameters has been reached. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161097504907_DV_resource.Stream@PNG-de-DE.png) | Connector display for an interconnection that cannot be fully displayed:  - Light beige: The destination connector lies within the sheet or in the sheet bar. - Dark beige: The destination connector lies in the extended sheet bar.   The interconnection is represented by connectors with the same numbers.  To jump between the connectors, double-click the corresponding connector. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161263836171_DV_resource.Stream@PNG-de-DE.png) | Status display for the "Forcing" function  - Brown (online) / light brown (offline):   The "Add forcing" option has been enabled. - Blue (online) / light blue (offline):   The "Add forcing" and "Forcing active" options have been enabled. |

**Interconnections in the data flow**

The color of the interconnection lines depends on the data type of the data source. You select the colors in menu "Options > Settings > Charts > CFC > General".

For interconnections to operands whose data type is not defined, the default value "black" is used.

| Icon | Meaning |
| --- | --- |
| ![CFC editor: Chart view in the "Data flow" tab](images/161279765259_DV_resource.Stream@PNG-de-DE.png) | Create interconnections  When you move the mouse over the input parameters, the interconnectable parameters are displayed with a green background.  The selected parameter is displayed with a light green background. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161271845131_DV_resource.Stream@PNG-de-DE.png) | Colored signal flow marking  Requirement: The "Highlighting for signal flow" option has been enabled in the toolbar. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161256181003_DV_resource.Stream@PNG-de-DE.png) | Interconnections in online mode  For BOOL-type interconnections, the display of interconnection lines in online mode is dependent on the current value.  - Green line: Value = "1" - Dashed blue line: Value = "0" |
| ![CFC editor: Chart view in the "Data flow" tab](images/161359761291_DV_resource.Stream@PNG-de-DE.png) | Identifies textual interconnections in the sheet bar |

**Other icons**

| Icon | Meaning |
| --- | --- |
| ![CFC editor: Chart view in the "Data flow" tab](images/132651805963_DV_resource.Stream@PNG-de-DE.png) | Shows and hides window areas |
| ![CFC editor: Chart view in the "Data flow" tab](images/161097477003_DV_resource.Stream@PNG-de-DE.png) | Footer:  Select zoom factor of work area |
| ![CFC editor: Chart view in the "Data flow" tab](images/161097493899_DV_resource.Stream@PNG-de-DE.png) | Footer:  Slider for zoom factor of the work area |
| ![CFC editor: Chart view in the "Data flow" tab](images/161097485451_DV_resource.Stream@PNG-de-DE.png) | Footer:  Opens a window for navigation in the chart |
| ![CFC editor: Chart view in the "Data flow" tab](images/35945135243_DV_resource.Stream@PNG-de-DE.png) | Inheritance status of attributes of a selected parameter in the Inspector window (tab "Properties > General")  - The value of the attribute is handed down from the type to the instance. |
| ![CFC editor: Chart view in the "Data flow" tab](images/35939430795_DV_resource.Stream@PNG-de-DE.png) | Inheritance status of attributes of a selected parameter in the Inspector window (tab "Properties > General")  - The value is not handed down from the type to the instance because it was changed at the instance.   To restore the inheritance, click on the icon. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161431202443_DV_resource.Stream@PNG-de-DE.png) | Data flow:  Open textual interconnections of interface parameters have the background color "yellow" in the "Operand" column. |
| ![CFC editor: Chart view in the "Data flow" tab](images/161283729163_DV_resource.Stream@PNG-de-DE.png) | Chart interface:  As long as an interface parameter has not been interconnected, the table cell of the "Data type" column has a "light gray" background color.  Upon interconnection, the background color changes to "medium gray". |

#### "Chart sequence & extras" editor

**General**

| Icon | Meaning |
| --- | --- |
| !["Chart sequence & extras" editor](images/161080908939_DV_resource.Stream@PNG-de-DE.png) | Expand display and show only the top elements |
| !["Chart sequence & extras" editor](images/161080917387_DV_resource.Stream@PNG-de-DE.png) | Expand display and show all lower-level elements |
| !["Chart sequence & extras" editor](images/161099921931_DV_resource.Stream@PNG-de-DE.png) | Refreshes the display |

**"Chart sequence" tab**

| Icon | Meaning |
| --- | --- |
| !["Chart sequence & extras" editor](images/130610887435_DV_resource.Stream@PNG-de-DE.png) | Optimize run sequence of CFC charts |
| !["Chart sequence & extras" editor](images/161095825035_DV_resource.Stream@PNG-de-DE.png) | Show selected object in data flow |
| !["Chart sequence & extras" editor](images/161095935883_DV_resource.Stream@PNG-de-DE.png) | Show selected object in the control flow |

**"Textual interconnections" tab (S7 target system)**

| Icon | Meaning |
| --- | --- |
| !["Chart sequence & extras" editor](images/161095944331_DV_resource.Stream@PNG-de-DE.png) | Select all displayed textual interconnections |
| !["Chart sequence & extras" editor](images/161095952779_DV_resource.Stream@PNG-de-DE.png) | Undo selection of textual interconnections and select no interconnection |
| !["Chart sequence & extras" editor](images/161096895627_DV_resource.Stream@PNG-de-DE.png) | Close textual interconnection |
| !["Chart sequence & extras" editor](images/161096904075_DV_resource.Stream@PNG-de-DE.png) | Delete textual interconnection |

**"Block types" tab (S7 target system)**

The "Differences" column displays the status of the block in comparison with the block types.

| Icon | Meaning |
| --- | --- |
| !["Chart sequence & extras" editor](images/25862137611_DV_resource.Stream@PNG-de-DE.png) | There are no differences between the compared blocks.  No action required. |
| !["Chart sequence & extras" editor](images/25903747595_DV_resource.Stream@PNG-de-DE.png) | No instances of this imported block are currently used in the CFC.  Existing differences have no effect in the CFC. |
| !["Chart sequence & extras" editor](images/25862145803_DV_resource.Stream@PNG-de-DE.png) | There are differences between the compared blocks.  The differences are displayed in the Inspector window in the "Properties > Differences" tab. |
| !["Chart sequence & extras" editor](images/160951074187_DV_resource.Stream@PNG-de-DE.png) | The block type of the imported block was not found in the block folder. |
| Other status  Example: !["Chart sequence & extras" editor](images/26522556939_DV_resource.Stream@PNG-de-DE.png) | Status information is displayed in the "Properties" tab of the Inspector window.  Example: The block is not compiled. |

#### "Update blocks" dialog

The icons are displayed in the last column of the "Differences" window.

| Icon | Meaning |
| --- | --- |
| !["Update blocks" dialog](images/130975285899_DV_resource.Stream@PNG-de-DE.png) | No download necessary:  Identifies changed blocks that can be inserted without a download to the CPU.  STEP 7 downloads changed blocks to the PLC where appropriate, irrespective of CFC. |
| !["Update blocks" dialog](images/130975277707_DV_resource.Stream@PNG-de-DE.png) | Download of software necessary |
| !["Update blocks" dialog](images/132531361291_DV_resource.Stream@PNG-de-DE.png) | Download with CPU Stop necessary |

---

**See also**

[Basics of CFC](#basics-of-cfc)
  
["CFC" Editor](#cfc-editor)
  
["Chart sequence & extras" Editor](#chart-sequence-extras-editor)

## Configuring and adapting CFC charts

This section contains information on the following topics:

- [Overview for configuration of CFC charts](#overview-for-configuration-of-cfc-charts)
- ["Undo" and "Redo" functions in CFC](#undo-and-redo-functions-in-cfc)
- [Creating and managing CFC charts](#creating-and-managing-cfc-charts)
- [Adding and managing objects in the CFC chart](#adding-and-managing-objects-in-the-cfc-chart)
- [Configuration and interconnection of input and output parameters](#configuration-and-interconnection-of-input-and-output-parameters)
- [Adapting the run sequence](#adapting-the-run-sequence)
- [Testing the CFC chart](#testing-the-cfc-chart)

### Overview for configuration of CFC charts

#### Preparing the configuration

There is normally a planning phase prior to the configuration of CFC charts.

During this planning phase, you specify, for example, how the open-loop and closed-loop control is structured in the CFC charts.

You can, for example, create a separate CFC chart for each measuring point.

With this strategy, you have greater flexibility when reacting to expansions in the plant.

> **Note**
>
> **Using the functions "Undo" and "Redo"**
>
> Use the "Undo" and "Redo" buttons in the toolbar to undo or redo any basic actions you have executed in CFC.
>
> The options on how you can influence the actions with the two buttons also depend on the target system.
>
> Additional information: "["Undo" and "Redo" functions in CFC](#undo-and-redo-functions-in-cfc)"

#### Basic procedure

1. Create a controller and program block types.
2. Create a CFC chart, or open an existing CFC chart for editing.
3. Add and manage objects in the CFC chart, e.g. blocks, instructions, text boxes.
4. Configure input and output parameters by interconnection or parameter assignment.
5. Adapt the run sequence (*):

   - Sequence of blocks/instructions within a CFC chart
   - Sequence of the CFC charts
6. Compile and download the CFC chart. (*)

   You can find additional information in the documentation for the specific target system.
7. Test the CFC chart or user program. (*)

(*): Whether and to what extent you perform these steps depends on the target system you are using.

Additional information on the S7 target system: "Working with CFC charts for S7"

---

**See also**

["CFC" Editor](#cfc-editor)
  
[Basics of CFC](#basics-of-cfc)
  
[Creating a CFC chart](#creating-a-cfc-chart)
  
[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)
  
[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)
  
[Adapting the run sequence of CFC charts](#adapting-the-run-sequence-of-cfc-charts)

### "Undo" and "Redo" functions in CFC

Use the "Undo" and "Redo" buttons in the toolbar to undo or redo any actions you have performed.

#### Action stack

Every action you perform is saved in an action stack.

When undoing actions, the list is processed from top to bottom.

In other words, if you undo an action that lies further down in the list, all actions located above it in the list will also be undone automatically.

If you perform a new action, then the redo list is emptied.

#### Displaying the undo/redo list

The "Undo" button in the toolbar is enabled as soon as you perform an action that can be undone.

This button is split; you can use the arrow down to open a drop-down list.

It contains all actions of the action stack that you can undo.

If you performed actions in an editor other than the currently displayed editor, then the corresponding editor will also be displayed as a subheading.

This allows you to always identify the point at which the undo operation is applied.

#### Points to note

The listed actions empty the action stack.

You cannot redo or undo actions after such an action.

- Saving the project
- Project management (creating a new project, opening project, closing a project, deleting a project)
- Compile
- Restoring blocks
- Establishing an online connection
- Download

Additional information in the information system of the TIA Portal:

- "Introduction to the TIA Portal > [Undoing and redoing actions](Introduction%20to%20the%20TIA%20Portal.md#undoing-and-redoing-actions)"

### Creating and managing CFC charts

This section contains information on the following topics:

- [CFC views](#cfc-views)
- [Creating a CFC chart](#creating-a-cfc-chart)
- [Extending a CFC chart](#extending-a-cfc-chart)
- [Create CFC chart partitions](#create-cfc-chart-partitions)
- [Managing CFC charts and groups](#managing-cfc-charts-and-groups)
- [Printing a CFC chart](#printing-a-cfc-chart)
- [Limiting editing of CFC with password](#limiting-editing-of-cfc-with-password)
- [Changing the sheet bar view of a CFC chart](#changing-the-sheet-bar-view-of-a-cfc-chart)
- [Creating a subchart for a hierarchical CFC chart](#creating-a-subchart-for-a-hierarchical-cfc-chart)
- [Replacing hierarchical CFC charts](#replacing-hierarchical-cfc-charts)
- [Moving subcharts to the root level](#moving-subcharts-to-the-root-level)
- [Adding, editing and sorting parameters of the chart interface](#adding-editing-and-sorting-parameters-of-the-chart-interface)

#### CFC views

##### Overview

When configuring a CFC chart, you have the following CFC chart views available:

- CFC chart with static sheet bars
- CFC chart with dynamic sheet bars
- CFC chart without sheet bars

You can change the sheet bar view in the toolbar of a CFC chart as required.

More information: "[Changing the sheet bar view of a CFC chart](#changing-the-sheet-bar-view-of-a-cfc-chart)"

##### CFC chart with static sheet bars

A static area is reserved to the right and left in a CFC chart for the sheet bars.

This area is intended solely for sheet bar entries, for example for interconnections between charts.

The following figure shows a CFC chart with sheet bars:

![CFC chart with static sheet bars](images/20777853451_DV_resource.Stream@PNG-de-DE.png)

**Sheet bar width**

The right and left sheet bars of a chart are always the same width.

You can change the width of the sheet bars by dragging with the mouse or in the Inspector window of the CFC chart.

To adapt the sheet bar width to the text length of the interconnections, double-click the boundary line of the sheet bar.

##### CFC chart with dynamic sheet bars

A CFC chart with dynamic sheet bars displays the sheet bar entries only when required and has the following features that differ from a CFC chart with static sheet bars:

- You can place instructions, blocks or text boxes in the sheet bar area.
- The sheet bar area is not highlighted.

The following figure shows a CFC chart with dynamic sheet bars.

The text boxes are placed in the sheet bar area:

![CFC chart with dynamic sheet bars](images/20777915531_DV_resource.Stream@PNG-de-DE.png)

##### CFC chart without sheet bars

The CFC chart is displayed without sheet bars.

Interconnections to other CFC charts or to operands are displayed by connectors. The connectors are placed next the interconnected input or output parameters.

Interconnections between sheets are displayed as if they were on one sheet.

The following figure shows a CFC chart without sheet bars with sheet borders displayed:

![CFC chart without sheet bars](images/20778003211_DV_resource.Stream@PNG-de-DE.png)

**Printing CFCs without sheet bars**

Instructions or blocks in sheet borders are not shown completely when printed.

If you configure without sheet bars, make sure that you do not place these objects in sheet borders.

In this case, show the sheet borders during configuration.

##### Sheet bar extension

If you create more sheet bar entries than there is room for in the sheet bar, then the sheet bar is automatically extended.

If a sheet bar has been extended, you will see an arrow in the sheet bar at the bottom of the sheet.

The following figure shows a sheet bar with the arrow for an extended sheet bar:

![Sheet bar extension](images/161361473675_DV_resource.Stream@PNG-de-DE.png)

**Show the extended sheet bar**

If you click on the arrow, the extended sheet bar is shown.

The extended sheet bar is displayed slightly offset above the sheet bar.

The following figure shows an extended sheet bar.

If you click on the arrow at the top border, you return to the sheet bar.

![Sheet bar extension](images/161361469451_DV_resource.Stream@PNG-de-DE.png)

##### Representation and signal tracking of interconnections

**Interconnections that cannot be displayed**

If the connection line of an interconnection cannot be displayed, the interconnection is displayed with connectors.

The color of the connector indicates the type of interconnection.

The following color coding can be seen in the figure above:

- Connector color "Light beige":

  The associated target connector is displayed in the sheet at a parameter or in the sheet bar.

  These are connectors "1" to "5" as well as "7" in the figure.
- Connector color "Dark beige":

  The selected target connector is displayed in the extended sheet bar.

  These are connectors "6" and "8" in the figure.

**Signal tracking**

If you click on an interconnection or a connector, the interconnection or the associated connector is highlighted in color.

Interconnections to other sheets are also highlighted.

Additional information on the representation and signal tracking of interconnections: "[Representation and properties of interconnections](#representation-and-properties-of-interconnections)"

---

**See also**

[Placing instructions and blocks in the CFC chart](#placing-instructions-and-blocks-in-the-cfc-chart)
  
[Basic settings for CFC charts](#basic-settings-for-cfc-charts)
  
[Representation of instructions and blocks](#representation-of-instructions-and-blocks)

#### Creating a CFC chart

##### Overview

CFC charts always belong to one target system.

A CFC chart is uniquely identified by its name.

The settings, such as sheet number and sheet size, are taken from the basic settings of charts.

Additional information: "[Basic settings for CFC charts](#basic-settings-for-cfc-charts)"

**Display in the overview window**

The created CFC charts are displayed in the overview of the project tree.

The column "Author" contains the user who created the chart. To sort by user, double-click on the column title.

##### Storage of CFC charts

CFC charts are stored in the project tree under the target system in the "Charts" folder.

You cannot rename the "Charts" folder.

**Creating groups**

To structure the storage of CFC charts, create groups within the "Charts" folder.

Storing CFC charts in groups has no effect on interconnections or the run sequence.

Additional information: "[Managing CFC charts and groups](#managing-cfc-charts-and-groups)"

##### Requirement

- The target system has been created.
- The Inspector window is open.

##### Procedure

1. Double-click "Add new chart" in the project tree.

   The CFC chart is added to the "Charts" folder and displayed in the editor window.

   - The configuration data are displayed in the Inspector window in the "Properties" tab.
   - The chart interface is displayed in the top area of the editor window.

     In the "Interface" area you create, delete and interconnect the parameters of the CFC chart.

     You can create interconnections to other CFC charts and block elements.
2. Under "General", enter a meaningful name for the CFC chart in the Inspector window.
3. If necessary, change the sheet number and sheet size under "Sheet bars/layout".

##### S7 target systems: Advanced settings

1. If necessary, change the assigned main task under "S7 specific > Sequence".
2. If necessary, change the settings for the run sequence.

##### Result

The CFC chart has been created and is open in the work area of the CFC editor.

Additional information on the CFC editor: "["CFC" Editor](#cfc-editor)"

---

**See also**

[Create CFC chart partitions](#create-cfc-chart-partitions)
  
[Overview window](Introduction%20to%20the%20TIA%20Portal.md#overview-window-1)
  
[CFC naming conventions](#cfc-naming-conventions)
  
[Changing the sheet bar view of a CFC chart](#changing-the-sheet-bar-view-of-a-cfc-chart)
  
[Runtime model](#runtime-model)
  
[Options for determining the run sequence](#options-for-determining-the-run-sequence)
  
[Extending a CFC chart](#extending-a-cfc-chart)
  
[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)

#### Extending a CFC chart

##### Overview

When it is created, a CFC chart consists of a sheet on which you place and interconnect instructions and blocks.

If there is not enough space for placing or displaying interconnections, extend the CFC chart.

You can extend an existing CFC chart in the following ways:

- Increase the number of sheets, for example in the vertical direction.
- Increase the sheet size, for example from A4 to A3.
- Add chart partitions.

  Additional information: "[Create CFC chart partitions](#create-cfc-chart-partitions)"

##### Requirement

- The CFC chart is open.
- "Data flow" is displayed.
- The Inspector window is open.

##### Procedure

1. Click in a free area of the CFC chart.
2. Select the "General" tab in the Inspector window.
3. Select the "Sheet bar/Layout" entry in the area navigation.
4. To extend the CFC chart, increase the number of sheets or enlarge the sheet size.

   Change the vertical and horizontal outline of the sheets, if necessary.

   The layout settings apply to all chart partitions of a CFC chart.
5. To display all sheets for an overview, select the zoom view "Fit to screen".

   Alternatively, switch to this view with a double-click in the sheet background.

   With a double-click in a sheet, you switch from the overview to the clicked sheet.

##### Alternative procedure

You can also increase the number of sheets by dragging with the mouse.

If you move an instruction or a block beyond the borders of the sheet with drag-and-drop, the number of sheets increases automatically.

##### Reducing the number of sheets or sheet size

When you reduce the sheet size or the number of sheets, some objects may be located outside the new sheet borders.

These objects are automatically positioned in the remaining area.

If the area is not large enough for all objects, the objects are placed at the top left in the CFC chart.

Increase the number of sheets and place the objects manually.

##### Result

The CFC chart is extended.

Use the following keyboard shortcuts to navigate between sheets:

- <Ctrl+Right/Left>
- <Ctrl+Top/Bottom>

---

**See also**

[Placing instructions and blocks in the CFC chart](#placing-instructions-and-blocks-in-the-cfc-chart)
  
[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Managing CFC charts and groups](#managing-cfc-charts-and-groups)
  
[Basic settings for CFC charts](#basic-settings-for-cfc-charts)
  
[Create CFC chart partitions](#create-cfc-chart-partitions)

#### Create CFC chart partitions

##### Overview

When it is created, a CFC chart consists of a sheet on which you place and interconnect instructions and blocks.

If there is not enough space for placing or displaying interconnections, extend the CFC chart.

You can extend an existing CFC chart in the following ways:

- Add chart partitions
- Increase the sheet size or the number of sheets

  More information: "[Extending a CFC chart](#extending-a-cfc-chart)"

##### Working with chart partitions

You work in chart partitions as you do in the sheets of a CFC chart.

You can interconnect and move instructions and blocks between the chart partitions. The placement in chart partitions has no effect on the control flow.

When you add a block to the control flow, the block is placed in the first chart partition.

**Chart partition names**

You can give each chart partition its own name:

- Maximum 15 characters
- The name must be unique in the CFC chart.
- The name is always language-neutral.

**Configuration limits**

A CFC chart contains a maximum of 6 chart partitions with up to 6 sheets each.

When you add additional sheets to a chart partition, this setting also applies to all the other chart partitions of the CFC chart.

**Navigating between chart partitions**

When you open a CFC chart for the first time after starting the TIA Portal, the first chart partition is displayed. The name of the chart partition is displayed grayed out.

As soon as you add a second chart partition, the drop-down list "Changes to another chart partition" is activated. The drop-down list box contains the chart partitions sorted alphabetically by name.

Navigate between the chart partitions using this drop-down list:

![Working with chart partitions](images/142197172363_DV_resource.Stream@PNG-de-DE.png)

Alternatively, change between the chart partitions of the open CFC chart with the following keyboard shortcuts:

- Next chart partition: <Shift+PgDn>
- Previous chart partition: <Shift+PgUp>

##### Requirement

- The CFC chart is open.
- "Data flow" is displayed.

##### Procedure: Creating a chart partition

1. In the toolbar, click on the button "Adds a chart partition in the CFC chart": ![Procedure: Creating a chart partition](images/144137243915_DV_resource.Stream@PNG-de-DE.png)

   The new chart partition is displayed in the editor.

   New chart partitions are always created with the name "Partition_<consecutive number>".
2. To change the name, select the entry "Displayed chart partition" in the "General" tab of the Inspector window.

   Enter a meaningful name and a comment, if necessary.

   You can enter up to 1000 characters in the comment field.
3. To return to the previous view, select the desired chart partition in the drop-down list.
4. To delete a chart partition, display this chart partition and click on the button "Deletes the currently displayed chart partition": ![Procedure: Creating a chart partition](images/142195683979_DV_resource.Stream@PNG-de-DE.png)

   All objects and interconnections of the chart partition are also deleted.

##### Procedure: Configuring interconnections between chart partitions

1. To display both chart partitions, click on the button "Opens the CFC chart in a second window": ![Procedure: Configuring interconnections between chart partitions](images/142195687691_DV_resource.Stream@PNG-de-DE.png)

   The CFC chart is displayed in two editor windows.

   To display both windows, click on one of the buttons for splitting the editor area: ![Procedure: Configuring interconnections between chart partitions](images/144473179531_DV_resource.Stream@PNG-de-DE.png)
2. Select the required chart partition from the drop-down list.
3. Create the interconnection between the two chart partitions, for example, by using drag and drop or copy and paste.

   The connector at the sheet bar contains the name of the chart partition and the sheet number.

**Alternative procedure: Example "Click Clack"**

1. Click on a parameter so that it is displayed in magenta.
2. Use the drop-down list to switch to the required chart partition.
3. Move the mouse pointer to the required parameter.
4. Click on the parameter as soon as it is displayed in green.

##### Result

The CFC chart is divided up into chart partitions.

---

**See also**

[Extending a CFC chart](#extending-a-cfc-chart)
  
[Creating a CFC chart](#creating-a-cfc-chart)
  
[Creating a subchart for a hierarchical CFC chart](#creating-a-subchart-for-a-hierarchical-cfc-chart)

#### Managing CFC charts and groups

The names of a group or CFC must be unique within a target system.

Inside the target system, you can move or copy the CFCs to any other group within the "Charts" folder.

##### Add group

Create groups to structure the CFCs in the "Charts" folder.

You can create additional subgroups to an existing group.

1. Select the "Charts" folder or an existing group in the project tree.
2. Select "Add new group" from the shortcut menu.
3. Enter a meaningful name for the group.
4. Move the CFCs you want to move from the "Charts" folder or another group to the new group using drag-and-drop.

   You can also copy the required CFCs and add them to the new group.

   To create a new CFC in a group, select the item "Add new chart" in the shortcut menu of the group.

##### Copying a group

1. Select the group you want to copy in the project tree.
2. Select "Copy" from the shortcut menu.
3. Highlight the position of the group you want to create in the project tree within the "Charts" folder.
4. Select "Paste" from the shortcut menu.

> **Note**
>
> **Naming conflicts during copying**
>
> If you copy one or more groups, only the group is checked for name conflicts at the destination location.
>
> If the group is replaced, charts with the same name are automatically renamed in the group.

##### Renaming a CFC or group

1. Select the CFC or the group in the project tree.
2. Select the "Rename" command in the shortcut menu.

   Alternatively, press the <F2> key.
3. Enter the new name.

##### Deleting a CFC

> **Note**
>
> **Checking interconnections**
>
> If you delete a CFC, interconnections to other charts are also deleted.
>
> Before deleting a CFC, you should therefore check whether the chart has interconnections to other charts.
>
> The values of the respective input and output parameters are reset to the values preset in the block type.
>
> Correct the reset parameters if necessary.

**Procedure**

1. Select the CFC in the project tree.
2. Select the "Delete" command in the shortcut menu.

   The CFC is deleted.

   Interconnections to other charts are also deleted.

##### Deleting a group

When you delete a group, you also delete all the objects it contains.

**Procedure**

1. Select the group in the project tree.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Copying objects](#copying-objects)
  
[Copying instructions, blocks and charts](#copying-instructions-blocks-and-charts)
  
[Creating a CFC chart](#creating-a-cfc-chart)
  
[Overview of textual interconnections](#overview-of-textual-interconnections) 
  
[Hierarchical CFC charts](#hierarchical-cfc-charts)

#### Printing a CFC chart

##### Overview

You can print CFC charts, for example, to create documentation.

Using multiple selection, you can print several CFC charts at the same time.

In addition to the selected view, the instructions and blocks configured in the CFC chart and their input and output parameters are also printed.

**Settings**

You can select different print settings for printing the CFC charts, e.g. sheet bars, number of sheets, sheet size.

| Symbol | Meaning |
| --- | --- |
| Menu bar:  - "Options > Settings > Charts" | Basic settings for all CFC charts to be newly created |
| Chart properties in the Inspector window  - "General > Sheet bars/Layout" | Print settings for one or more selected CFC charts |

> **Note**
>
> **Taking into account format and sheet borders**
>
> If you use CFC charts without sheet bars, make sure that instructions/blocks are not placed on sheet borders.
>
> If the sheet size used in the CFC chart does not match the sheet size in the printer, the CFC chart is scaled automatically when it is printed.
>
> If you select a smaller sheet size for a CFC chart, the position of the objects in the chart is maintained.
>
> Objects that would be outside the sheet size after the size reduction is positioned automatically.

##### Print settings

| Symbol | Meaning |
| --- | --- |
| Printer | Select the desired printer from the list or via the "Advanced" button. |
| Document information | Select the desired layout from the list.  The frame stored in the document information is used for the printout. |
| Print the cover page | The cover page from the layout selected under "Document information" is used. |
| Print table of contents | The table of contents contains the structure of the CFC charts in the navigation area. |
| Properties | - All: Prints all project data of the selected CFC charts. - Compact: Prints the project data in compact form. |

Additional information in the information system of the TIA Portal:

- "Edit project data > Print project contents > [Print project documentation](Editing%20project%20data.md#printing-project-documentation)"

##### Procedure: Displaying print preview

1. Select the CFC charts you want to print in the project tree.
2. Select the "Print preview" command in the shortcut menu.
3. Select the print settings.
4. Start creating the print preview by pressing the "Preview" button.

   The print preview is opened in the work area.

   You can also print the CFC chart from the print preview.

##### Procedure: Printing a CFC chart

1. Check the chart settings:

   - By using the "Options > Settings > Charts" menu command
   - In the properties of the CFC chart in the Inspector window under "Sheet bars/Layout"
2. Select the CFC charts you want to print in the project tree.
3. Select the "Print" command from the shortcut menu.

   Alternatively, use the keyboard shortcut <Ctrl+P>.
4. Select the print settings.
5. Start the printout with the "Print" button.

##### Alternative procedure: Print a group

Instead of selecting multiple CFC charts, you can also select a group and then the "Print" command from the shortcut menu of the group.

in this case, all the CFC charts in the group are printed.

The order in which they are printed is decided by the order of the CFC charts in the project tree.

##### Result

The CFC chart is output on the printer.

Chart partitions are sorted alphabetically in a CFC chart.

If you have selected several CFC charts, they are printed in the order in which you selected them.

---

**See also**

[Basic settings for CFC charts](#basic-settings-for-cfc-charts)

#### Limiting editing of CFC with password

This section contains information on the following topics:

- [Activating password for a CFC chart](#activating-password-for-a-cfc-chart)
- [Changing or deactivating password for a CFC chart](#changing-or-deactivating-password-for-a-cfc-chart)
- [Opening a password-protected CFC chart](#opening-a-password-protected-cfc-chart)

##### Activating password for a CFC chart

To protect a CFC chart or hierarchical CFC chart from unintentional editing, you can protect the chart with a password.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password serves only to protect a CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts   More information:  - "[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)" |  |

###### Procedure

1. Go to the required CFC chart in the project tree.
2. To open the "Enable protection" dialog, select the menu command "Access protection" from the shortcut menu.

   Alternative procedure:

   - Double-click on the CFC chart to open it.
   - Select the entry "Protection" in the "Properties" tab of the inspector window.
   - Click the "Protection" button.
3. Enter the desired password in both boxes.
4. Click "OK" to close the dialog box.

###### Result

The password is activated for this CFC chart.

This is indicated by a small padlock symbol on the icon of the CFC chart in the project tree.

---

**See also**

[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)
  
[Changing or deactivating password for a CFC chart](#changing-or-deactivating-password-for-a-cfc-chart)
  
[Opening a password-protected CFC chart](#opening-a-password-protected-cfc-chart)

##### Changing or deactivating password for a CFC chart

When a password was assigned for a CFC chart, you can change or deactivate the password.

###### Procedure

1. Go to the required CFC chart in the project tree.
2. To open the "Change protection" dialog, select the menu command "Access protection" from the shortcut menu.

   Alternative procedure:

   - Double-click on the CFC chart to open it and enter the password.
   - Select the entry "Protection" in the "Properties" tab of the inspector window.
   - Click the "Protection" button.
3. Enter the current password in the "Old password" box.
4. Select whether you want to change or deactivate the password:

   - To deactivate the password, click on the "Remove" button.
   - To change the password, enter the new password in the boxes "New password" and "Confirm password".
5. Click "OK" to close the dialog box.

###### Result

The password is activated or changed for this CFC chart.

When you have deactivated the password, the small padlock symbol is no longer shown on the icon for the CFC chart in the project tree.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password serves only to protect a CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts   More information:  - "[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)" |  |

---

**See also**

[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)
  
[Activating password for a CFC chart](#activating-password-for-a-cfc-chart)
  
[Opening a password-protected CFC chart](#opening-a-password-protected-cfc-chart)

##### Opening a password-protected CFC chart

###### Requirement

- The password is activated in the CFC chart.

  Charts with activated password are indicated by a small padlock symbol on the icon of the CFC chart in the project tree.

###### Procedure

1. Go to the required CFC chart in the project tree.
2. Double-click on the CFC chart.

   The "Access protection" dialog opens.
3. Enter the password and click "OK".

   The CFC chart is open in the "CFC" editor.

   The contents of the chart and the interface can be edited.
4. To open the CFC chart write-protected, click the "Cancel" button in the "Access protection" dialog.

   - A message is displayed in the editor window, but the contents of the chart are not displayed.
   - Editing the chart interface is possible to a limited extent.

###### Result

The CFC chart is opened as editable.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Password: No authorization, no know-how protection of the charts**  The password serves only to protect a CFC chart from unintentional editing.  This type of access protection is not intended to increase the access security.  The password does not offer:  - Protection against unauthorized access to know-how in CFC charts - Security-relevant authorization for access to CFC charts   More information:  - "[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)" |  |

---

**See also**

[Protection from unintentional access to CFC charts](#protection-from-unintentional-access-to-cfc-charts)
  
[Activating password for a CFC chart](#activating-password-for-a-cfc-chart)
  
[Changing or deactivating password for a CFC chart](#changing-or-deactivating-password-for-a-cfc-chart)

#### Changing the sheet bar view of a CFC chart

##### Layout of the sheet bars

The following sheet bar views are available:

- Static sheet bars
- No sheet bars
- Dynamic sheet bars

##### Procedure

1. Click in a free area of the CFC chart.
2. Select the required sheet bar view under "Sheet bars/layout" in the Inspector window.

##### Alternative procedure

You can also change the sheet bar view using the icon in the toolbar.

##### Result

The sheet bar view changes.

Connectors in the sheet bars are positioned either in the sheet bar or beside the input or output parameters on the sheet bar view you have set.

To adapt the width of fixed sheet bars to the text length of the interconnections, double-click the boundary line of the sheet bar.

---

**See also**

[CFC views](#cfc-views)

#### Creating a subchart for a hierarchical CFC chart

You can create CFCs in hierarchical structures.

In doing so, you add one or more CFCs as "subcharts" into a "basic chart".

##### Procedure: Create a new subchart

1. Open the CFC in which you want to insert a different chart as subchart.
2. To insert a new CFC as subchart, click the "Insert a new subchart" icon in the toolbar of the "CFC" editor: ![Procedure: Create a new subchart](images/132653846667_DV_resource.Stream@PNG-de-DE.png)

   The mouse pointer transforms into an attached subchart icon.
3. Click the position at which you want to insert the new subchart.

   The new subchart is displayed as an icon in the opened CFC.

   The changes are displayed in the "Charts" folder:

   - If the CFC into which the new subchart was inserted did not contain any subcharts, it is now displayed as a basic chart.
   - The new CFC was created automatically and is now displayed as subchart.
   - The new subchart has the name of the basic chart with the suffix "_1".

     Assign a meaningful name to the subchart.
4. Configure the newly created subchart.

**Alternative procedure: Shortcut menu**

1. In the open chart, right-click the location where you want to insert a subchart.
2. Select the "Insert a new subchart" command from the shortcut menu.

##### Alternative procedure: Insert existing CFC

1. Open the CFC in which you want to insert a different chart as subchart.
2. Drag a CFC from the project tree or a library to the open CFC in the editor.

   The new subchart is displayed as an icon in the opened CFC.

   The changes are displayed in the "Charts" folder:

   - If the CFC into which the new subchart was inserted did not contain any subcharts, it is now displayed as a basic chart.
   - The CFC you inserted is copied and displayed as subchart in the tree structure of the basic chart.

   The new subchart and the CFC inserted as source can be configured independently of one another.

   When you change the original, inserted CFC and want to apply the change to the subchart, you can replace the subchart.

   Additional information: "[Replacing hierarchical CFC charts](#replacing-hierarchical-cfc-charts)"

##### Result

You have inserted a subchart in a CFC that represents a hierarchical chart with basic and subcharts.

In the subchart and basic chart, you can configure new parameters and create interconnections to parameters in the chart interface.

---

**See also**

[Hierarchical CFC charts](#hierarchical-cfc-charts)
  
[Create CFC chart partitions](#create-cfc-chart-partitions)

#### Replacing hierarchical CFC charts

You can replace a hierarchical CFC with a different hierarchical CFC.

If possible, the interconnections of the "old" chart are retained.

##### Use case

Replacement can be used, for example, in situations where subcharts are configured as sub-functions that are intended for use in different applications.

**Example**

You configured a sub-function as hierarchical CFC and interconnected this subchart in a CFC.

This sub-function could be a control for a ventilation system that is available in different variants, depending on the application.

You can always interchange these variants in the overall structure without having to change the interconnections.

##### Requirement

- The CFC that is to replace a specific subchart is available in a library in the "Charts" folder as a basic chart, or in a different CFC.

##### Procedure

1. Open the basic chart that contains the subchart you want to replace.
2. In the project tree or in a library, navigate to the CFC that is to replace the subchart.

   You can also open a different CFC that contains the desired CFC.
3. Drag-and-drop the CFC from the project tree, from the library, or a different CFC into the subchart that is to be replaced.
4. Release the mouse button as soon as the mouse pointer is positioned exactly over the CFC to be replaced.

   Alternatively, copy the CFC and select the "Paste" command in the shortcut menu at the icon of the subchart to be replaced.

   A dialog opens and prompts you to confirm the replacement of the CFC.
5. Confirm the replacement with "Yes".

##### Result

The subchart is replaced by the inserted CFC.

The name of the replaced subchart remains the same.

---

**See also**

[Hierarchical CFC charts](#hierarchical-cfc-charts)
  
[Creating a subchart for a hierarchical CFC chart](#creating-a-subchart-for-a-hierarchical-cfc-chart)

#### Moving subcharts to the root level

##### Requirement

- The CFC to be moved may not contain any external interconnections to the chart interface.

##### Procedure

1. Select the subchart that is to be moved to the root level from the "Charts" folder of the project tree.
2. Drag-and-drop the subchart to the root level of the "Charts" folder.

   You can also copy and paste the subchart to the root level.

##### Result

You have successfully moved or copied the previous subchart to root level in the "Charts" folder.

---

**See also**

[Hierarchical CFC charts](#hierarchical-cfc-charts)

#### Adding, editing and sorting parameters of the chart interface

##### Chart interfaces

Hierarchical CFC charts and standard CFC charts have an interface structure that is similar to that of blocks.

This means that these CFC charts can be configured and interconnected externally similar to blocks.

Interconnections with chart interface parameters are visualized using the chart sheet bar or via connectors.

##### Procedure

1. Open the CFC chart whose interface you want to change.

   The chart interface is displayed in the top area of the "Data flow" or "Control flow" section in the "CFC" editor.

   The properties of the attributes are displayed in the Inspector window.

   When the "Interface" area is hidden, enlarge the area with the mouse or click the unhide icon:

   ![Procedure](images/132651805963_DV_resource.Stream@PNG-de-DE.png)
2. If you want to add a new parameter, click the "<add>" line in the "Name" column in the required Input, Output or InOut section.

   The new parameter is added in the selected line.

   The "Name" field is opened for editing.

   To add a line, select the item "Insert line" or "Add line" from the shortcut menu of the line.
3. Enter the name of the new parameter.
4. Select the desired data type in the "Data type" column.

   All CFC data types are supported in the chart interface except:

   - TIMER
   - COUNTER
   - Hardware data types
5. If necessary, change the other attributes of this parameter, for example, "Value" or "Configurable".
6. If you wish to change a parameter, click the required field in the table line.

   Depending on the type of field, it is opened for editing or a drop-down list is displayed.
7. To change the sequence of parameters in the table, drag the name of the parameter or the line to the new position.

   You can only change the sorting within a section, for example, the parameters in the section "Input".
8. If you wish to delete a parameter, select the name of the required parameter.

   Select the "Delete" command in the shortcut menu.

   The line of this parameter is removed from the table.

##### Result

A parameter was added, edited or deleted in the chart interface.

The sorting of the parameters was changed, if necessary.

---

**See also**

[Hierarchical CFC charts](#hierarchical-cfc-charts)
  
[Interconnections to parameters of the chart interface](#interconnections-to-parameters-of-the-chart-interface)
  
[Data types in CFC](#data-types-in-cfc)

### Adding and managing objects in the CFC chart

This section contains information on the following topics:

- [Representation of instructions and blocks](#representation-of-instructions-and-blocks)
- [Representation options for the block icon in the CFC chart](#representation-options-for-the-block-icon-in-the-cfc-chart)
- [Placing instructions and blocks in the CFC chart](#placing-instructions-and-blocks-in-the-cfc-chart)
- [Copying instructions, blocks and charts](#copying-instructions-blocks-and-charts)
- [Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
- [Adding a text box to a CFC chart](#adding-a-text-box-to-a-cfc-chart)
- [Aligning objects in a CFC chart](#aligning-objects-in-a-cfc-chart)
- [Positioning objects according to the data flow](#positioning-objects-according-to-the-data-flow)
- [Deleting an instruction or block from the CFC chart](#deleting-an-instruction-or-block-from-the-cfc-chart)
- [Central change of a block type](#central-change-of-a-block-type)
- [Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)
- [Creating a block type for CFC](#creating-a-block-type-for-cfc)

#### Representation of instructions and blocks

##### Overview

The following section contains information related to instructions/blocks in the CFC chart:

- Block icon: visualization, layout, editing options
- Block interface: layout, editing options
- Additional information at the block icon: For example, display of run sequence, processing display, display of hidden parameters
- View in the CFC chart: Zoom function, signal flow

> **Note**
>
> **Use of the terms "instruction" and "block"**
>
> The following description applies to both instructions and blocks.
>
> For simplification, however, we only use the term "block", for example, "block header".

##### Representation of the block icon

An instruction or a block is represented as a symbol in the CFC chart.

The following options are available for the representation:

- You cannot change the representation of the block icon in the case of instructions from the "Instructions" task card.
- For blocks, several options are available for the representation of the block icon in the CFC chart.

  More information: "[Representation options for the block icon in the CFC chart](#representation-options-for-the-block-icon-in-the-cfc-chart)"

Additional icons are used for representation of the basic and subcharts.

More information: "[Hierarchical CFC charts](#hierarchical-cfc-charts)"

##### Structure of the block icon

In principle, the block icon in the CFC chart consists of the so-called block header and the block interface.

However, this is not true for the smallest representation option "BuiltIn;SmallBlock" of the block icons.

![Structure of the block icon](images/161016506251_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| (1) | Block header |
| (2) | Block interface |
| (3) | Display for hidden parameters |
| (4) | Processing display |
| (5) | Run sequence: Position number, assigned task (optional display) |

**Change size**

- You can change the width as required.
- The height of the icon depends on the number of input and output parameters.

  To change the height of the icon, show or hide the input and output parameters.

##### Block header (1)

The block header can display the following information:

- Instance name (e.g. "myblock_1_1")
- Type name (e.g. "MyBlock_1")
- Instance comment
- Processing display

The information shown in the block header depends on the instruction or block and the target system you are using.

With some types of instructions and blocks, the block header may be missing altogether or simply contain a small icon, for example, an instruction for an OR logic operation.

![Block header (1)](images/20362174731_DV_resource.Stream@PNG-de-DE.png)

**Editing options in the block header**

In the work area, you have the following options for editing the block header:

- Changing the instance name and instance comment
- Selecting a block/instruction

##### Block interface (2)

The block interface displays the input and output parameters:

- Left: Input parameters
- Right: Output parameters

Normally, the block parameters have the parameter values of the type by default.

The name of the input and output parameter is displayed in full length or truncated depending on the width of the symbol.

**Comments of the block type**

You can show the comments instead of the names of the input and output parameters.

To toggle between names and comments, use the following button in the toolbar: ![Block interface (2)](images/130610953099_DV_resource.Stream@PNG-de-DE.png)

**Parameter: Tooltips**

When you hover your mouse over an input or output parameter, a tooltip with the following information is displayed:

- Name of the parameter
- Data type of the parameter
- Comment of the parameter

When you expand the tooltip, the following information is displayed:

- Value of the parameter
- Parameter section

**Editing options in the block interface**

In the work area, you have the following options for editing the block interface:

- Set the parameters of the input and output parameters.
- Interconnect the input and output parameters using drag-and-drop.
- Select the input and output parameters.
- Selecting a block/instruction

**Navigation with the keyboard**

- To select individual parameters with the keyboard, click on the block and press the <Down> arrow key: ![Block interface (2)](images/144257272971_DV_resource.Stream@PNG-de-DE.png)
- Use the <Right> and <Left> arrow keys to switch between the parameters: ![Block interface (2)](images/144257717259_DV_resource.Stream@PNG-de-DE.png), ![Block interface (2)](images/144257725451_DV_resource.Stream@PNG-de-DE.png)
- Use the <Up> arrow key to return to the block level: ![Block interface (2)](images/144257797643_DV_resource.Stream@PNG-de-DE.png)
- When the entire block is selected, use the <Right> and <Left> arrow keys to switch between the blocks.

##### Display for hidden parameters (3)

The icon indicates that the "Invisible" property of the parameter is activated.

If input or output parameters are set to "invisible" and are therefore hidden in the block icon, this fact is indicated by an additional triangle symbol at the bottom of the icon.

| Icon | Meaning |
| --- | --- |
| ![Display for hidden parameters (3)](images/16251712651_DV_resource.Stream@PNG-de-DE.png) | A non-interconnected parameter is hidden. |
| ![Display for hidden parameters (3)](images/16251709451_DV_resource.Stream@PNG-de-DE.png) | An interconnected parameter is hidden. |

More information: "[Hiding input and output parameters](#hiding-input-and-output-parameters)"

##### Processing display (4)

The processing display at the top left corner of the block header indicates whether the block is processed in the program sequence.

If the block header is missing, for example in the case of instructions, the processing display is shown at the block interface.

The processing of a block depends on the following elements:

- Enable input "EN" at the block
- "Enable chart" option of the CFC chart in which the block is added

The display shows the following states:

| Icon | Meaning |
| --- | --- |
| No symbol | Block is always processed. |
| ![Processing display (4)](images/61427602955_DV_resource.Stream@PNG-de-DE.png) | Block is processed conditionally.  The reason is that the enable input "EN" at the block or the "Enable chart" option of the chart has been interconnected. |
| ![Processing display (4)](images/61425315723_DV_resource.Stream@PNG-de-DE.png) | Block is not processed.  The reason is that the enable input "EN" at the block is "FALSE" or the "Enable chart" option of the chart has been disabled. |

##### Additional information at the block icon

**Mouse pointer**

The change in the mouse pointer over the instruction or block icon indicates the various editing options available, for example, moving or selecting.

**Tooltip**

When you hover your mouse over the block icon, a tooltip with the following information is displayed:

- Instance name
- Type name
- Task
- Comment

  If the instance has no comment, the comment of the type is displayed.

**Display of the run sequence (5)**

Using the toolbar of the data flow, you can show the position of the instruction or block in the run sequence.

| Icon | Meaning |
| --- | --- |
| ![Additional information at the block icon](images/160947553931_DV_resource.Stream@PNG-de-DE.png) | The position number in the run sequence is displayed above the block header. |
| ![Additional information at the block icon](images/160950105099_DV_resource.Stream@PNG-de-DE.png) | The name of the assigned task is displayed above the block header.  For subcharts, information that the task was inherited from the basic chart is added where appropriate. |

![Additional information at the block icon](images/160951069707_DV_resource.Stream@PNG-de-DE.png)

##### Data flow: Zoom function

You can set the zoom ratio and customize the size of the view in the CFC chart using the data flow toolbar functions.

**Zooming in on multiple objects**

If you select multiple objects in the CFC chart and then run the "Zoom in" or "Zoom out" function, the view is zoomed automatically to the center of the selected objects in the work area.

The objects may also extend to other sheets.

**Input boxes: Response to zooming**

When you increase the zoom factor for the view of the CFC chart to over 100%, the input boxes in the chart and in the sheet bar are also zoomed in on. At 200%, input boxes in the sheet bar are enlarged up to the edge of the area.

The text size in the input box is not affected by the zoom factor. The larger input boxes therefore allow convenient editing of even long interconnection paths.

##### Highlighting for signal flow

You can highlight the flow of signals in the CFC chart.

The signal is highlighted starting from the selected block or subchart, ending at the I/O of the signal in the sheet bar of the CFC chart. All relevant interconnections and blocks are marked in color here.

The signal is highlighted only within the CFC chart, but not in other charts.

The signal flow is only displayed when a block or subchart is selected.

The function is enabled using the "Highlight signal flow" toolbar icon: ![Highlighting for signal flow](images/132686500363_DV_resource.Stream@PNG-de-DE.png)

**Example**

The following figure shows an example of the highlighted signal flow for an interconnection of type "BOOL". The example in this figure shows a chart section with three instructions.

The arrow marks the click position for the "AND" instruction.

The highlighting is continued to the left and right of the click position up to the chart boundaries because all three instructions are involved in the signal flow.

![Highlighting for signal flow](images/40978974475_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Placing instructions and blocks in the CFC chart](#placing-instructions-and-blocks-in-the-cfc-chart)
  
[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)
  
[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)
  
[CFC naming conventions](#cfc-naming-conventions)
  
[Options for determining the run sequence](#options-for-determining-the-run-sequence)

#### Representation options for the block icon in the CFC chart

##### Overview

You specify the representation of the block icon in the CFC chart with an attribute at the block type.

There are multiple options for displaying the block instances.

> **Note**
>
> **Block instances**
>
> The configured representation option at the block type cannot be changed for specific instances.
>
> Changing the representation option at the type affects all instances.
>
> **Instructions**
>
> You cannot change the representation option for instructions from the "Instructions" task card.

##### Basic procedure

You specify the size of the block icon in the CFC chart in the properties of the type with the attribute "Block representation":

1. Open the properties via the shortcut menu of the block type.
2. In the "General" tab, select the "Attributes" item.
3. Enter the required representation option in the "Block representation" field in the "User-defined attributes" area.

   Use the following syntax for this:

   | Symbol | Meaning |
   | --- | --- |
   | Large | `BuiltIn;Block` |
   | Medium | `BuiltIn;MediumBlock` |
   | Medium / narrow | `BuiltIn;NarrowMediumBlock` |
   | Small | `BuiltIn;SmallBlock` |
4. Save and compile the changed block.

   If you wish to use the changed block as type in a library, copy the changed block into the respective library.
5. Update the instances of this type in CFC.

   Additional information: "[Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)"

##### Representation options for the block icon

The table shows the various representation options.

The same block is displayed in the "Example" column in the corresponding representation option.

| Representation option/syntax | Example |
| --- | --- |
| "Large" version  Syntax:  - `BuiltIn;Block`   The block icon is displayed in full size in the CFC chart with all details in the block header and block interface. | ![Representation options for the block icon](images/35894948491_DV_resource.Stream@PNG-de-DE.png) |
| "Medium" version  Syntax:  - `BuiltIn;MediumBlock`   The block icon is displayed in medium size in the CFC chart.  The block header is reduced in size and displays only the block name.   The parameter names in the symbol are displayed in abbreviated form in the block interface.  The complete parameter name is displayed as a tooltip. | ![Representation options for the block icon](images/35894952459_DV_resource.Stream@PNG-de-DE.png) |
| "Medium/narrow" version  Syntax:  - `BuiltIn;NarrowMediumBlock`   This version corresponds to the "Medium" version in the representation of block header and interface.  The width of the block icon is also reduced. | ![Representation options for the block icon](images/35913527691_DV_resource.Stream@PNG-de-DE.png) |
| "Small" version  Syntax:  - `BuiltIn;SmallBlock`   The block icon is displayed in the smallest size.  The block header is hidden.  The parameter names in the block interface are only displayed as tooltip. | ![Representation options for the block icon](images/35913531659_DV_resource.Stream@PNG-de-DE.png) |

---

**See also**

[Representation of instructions and blocks](#representation-of-instructions-and-blocks)

#### Placing instructions and blocks in the CFC chart

##### Adding instructions and blocks

The positioning of instructions/blocks on the sheet of a CFC chart depends on whether you are working in "data flow" or "control flow" tab.

- Data flow:

  Position the inserted object by dragging it with the mouse.
- Control flow:

  The inserted object is automatically placed at a free location in the CFC chart.

##### Automatic placing of instructions/blocks

Objects, such as instructions/blocks, are positioned automatically in "data flow" mode under the following conditions:

- You add the object in the control flow.
- You add instructions to the CFC chart by double-clicking in the library.
- You enable automatic positioning in the shortcut menu of the object.

If the location of an automatically placed object is occupied by another object, then this object is moved automatically to a free location.

The property "Position automatically" is set at the properties of an object.

The following figure shows two instructions; automatic positioning is enabled for the instruction on the left.

The automatically positioned instruction has a colored border:

![Automatic placing of instructions/blocks](images/20768374667_DV_resource.Stream@PNG-de-DE.png)

You disable automatic positioning of an object as follows:

- You disable automatic positioning using the shortcut menu.
- You move the object.

##### Positioning objects in the CFC chart according to the data flow

Use the function "Place blocks according to the data flow" to place the objects in the CFC chart, e.g. blocks and instructions, according to the data flow.

This option makes for clearer positioning of objects and data flow as well as easier signal tracking.

The function is executed only manually in the open CFC chart and you cannot enable it permanently.

Additional information: "[Positioning objects according to the data flow](#positioning-objects-according-to-the-data-flow)"

##### Instructions/blocks that cannot be fully displayed

Under the following conditions, objects such as instructions/blocks are displayed without interconnections and in a different color:

- Automatic placing: There is not enough space for all objects on the sheet of a CFC chart.
- Manual placing: You position objects on top of each other, on an interconnection or on a sheet border.

Interconnections to objects that cannot be fully displayed are shown as connectors.

If objects are located on top of each other, the lowest object is shown completely. All objects above it are shown incompletely.

The following figure shows an instruction located on the sheet bar.

The interconnection between the two instructions is displayed as a connector in the sheet bar:

![Instructions/blocks that cannot be fully displayed](images/20768381707_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Deleting an instruction or block from the CFC chart](#deleting-an-instruction-or-block-from-the-cfc-chart)
  
[Aligning objects in a CFC chart](#aligning-objects-in-a-cfc-chart)

#### Copying instructions, blocks and charts

##### Blocks with interconnections to external tags

If you interconnect an input or output parameter with an external tag, a connector is created. The connector has the name of the external tag.

If you copy an instruction or a block with an interconnection to an external tag, the connector is also copied.

The name of the tag will remain the same in the copy of the connector.

Check the interconnection with the external tag in the copy and change the name, if necessary.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Check the user program before using it**  Despite a valid criteria check, the algorithm can be different in the instructions or blocks.  To avoid possible errors in the plant, check the code of the user program in the instruction or block if you are uncertain. |  |

##### Copying CFCs

If you copy a chart, an instruction or a block across devices or projects, then the following conditions will apply:

| Condition | Resulting action |
| --- | --- |
| The block that is to be copied is missing in the target system. | The block is copied completely, including all necessary called blocks, to the "Program blocks" folder.  At the same time, the block is imported as type into the CFC of the target system. |
| The block / type that is to be copied differs only in the block numbering in source and target system. | The CFC is copied to the target system. The type remains the same in the target system. The copied CFCs in the target system is adapted. |
| A type, instruction or block with the same name already exists in the target system. | The two instructions/blocks are compared based on their input and output parameters and the following criteria:  - Quantity - Name - Data type - Section - Order   The copy function will only be performed if all the criteria match. Otherwise, the copy function is canceled. |
| The task of the CFC to be copied does not exist in the target system. | The CFC is not copied to the target system.   **Special considerations for the S7 target system**   The CFC is copied to the target system. The assignment of the CFC to the task is retained. A non-existent task is created during the next compilation of the software, if the target system supports this task. |

---

**See also**

[Copying objects](#copying-objects)
  
[Interconnecting the input and output parameters with an external tag](#interconnecting-the-input-and-output-parameters-with-an-external-tag)
  
[Overview of textual interconnections](#overview-of-textual-interconnections)

#### Adding an instruction or block to the CFC chart

For configuration of a CFC chart insert the instructions or blocks to the chart and configure interconnections and parameters.

##### Requirement

- A CFC chart is open.
- The "Instructions" or "Libraries" task card is open.

##### Procedure

1. Navigate to the storage location of the selected instruction or block.

   Possible storage locations:

   - "Instructions" task card
   - Library
   - "Program blocks" folder in the project tree
2. Drag-and-drop the instruction or block to the CFC chart.
3. Place the instruction or block at the desired location in the CFC chart.

##### Alternative procedure

You can insert one or more existing blocks using copy and paste:

- Keyboard shortcuts <Ctrl+C> and <Ctrl+V>

  Blocks copied in are placed at an offset over the blocks that serve as the copy source.
- Shortcut menu: "Copy" and "Paste" entries

  The position of the mouse pointer when selecting the "Paste" entry determines where the blocks are inserted.

##### Result

The instruction or block is inserted into the CFC chart.

> **Note**
>
> **Inserting a deleted instance again**
>
> Before you insert the deleted instance of a block type again, transfer the change to the controller via a full download or 2x download of changes.
>
> This prevents name conflicts during download.
>
> Additional information: "[Deleting an instruction or block from the CFC chart](#deleting-an-instruction-or-block-from-the-cfc-chart)"

---

**See also**

[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)
  
[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Deleting an instruction or block from the CFC chart](#deleting-an-instruction-or-block-from-the-cfc-chart)
  
[Type and instance](#type-and-instance)
  
[Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)
  
["CFC" Editor](#cfc-editor)

#### Adding a text box to a CFC chart

##### Overview

To document the function of the CFC, add texts and images to the CFC:

- You can use texts, for example, to document the signal path.
- With an image, you can, for example, represent the part of the plant that is processed by the CFC.

Use the text boxes to add texts and images to the CFC.

Text boxes can be located in the foreground or background of the CFC and can contain text as well as a background image.

Text boxes in the background are ignored by blocks, instructions and interconnections.

##### Requirement

- A CFC is open.
- "Data flow" is displayed.

##### Procedure

1. Click "Insert text box" in the toolbar.
2. Keep the mouse button pressed to move the text box to the required position in the CFC and adjust it in size.
3. Select the "Text box in background" option under "General" in the Inspector window.
4. To display a graphic, select the "Use background image" option under "General".

   Select the graphic in the file selection dialog.
5. If necessary, enter the "text" for the text box.
6. If necessary, you can set additional properties of the text box in the Inspector window, such as border, font or font size.

---

**See also**

[Aligning objects in a CFC chart](#aligning-objects-in-a-cfc-chart)

#### Aligning objects in a CFC chart

You can align objects, such as instructions, blocks and text boxes, in the CFC or distribute them evenly.

First, select the required objects.

##### Alignment

The reference object on which the other objects will orient themselves is decided automatically within the selection.

The following criteria apply:

**Align**

The selected objects are aligned with each other.

The object used as the reference is the furthest object in the required alignment direction.

Example: If you want to right align the edges of three objects, the objects are aligned with the object located furthest right.

**Distributing**

The selected objects are distributed evenly.

The reference value used is the average position value of all the objects included in the selection.

##### Requirement

- A CFC is open.
- "Data flow" is displayed.
- Multiple objects have been added.

##### Procedure

1. Select the objects in the chart.
2. Select the command you require under "Align" in the shortcut menu of the selection.

##### Result

The selected objects are aligned or distributed evenly depending on the command you select.

---

**See also**

[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)
  
[Adding a text box to a CFC chart](#adding-a-text-box-to-a-cfc-chart)

#### Positioning objects according to the data flow

##### Overview

When you configure a CFC, objects, such as instructions, blocks and text boxes, are added, positioned and interconnected one after the other.

The representation of the chart can get confusing when you have a large number of objects and interconnections.

Use the function "Place blocks according to the data flow" to place the objects in the CFC, e.g. blocks and instructions, according to the data flow.

This option makes for clearer positioning of objects and data flow as well as easier signal tracking.

##### Response

- The objects in the CFC are sorted automatically in columns one below the other and aligned on a mutual axis in the columns.

  The width of a column is determined by the widest object in the column.
- Independent subnets are listed one after the other and have columns independent of one another.
- Each object is placed automatically in the chart this way so that it does not intersect the sheet bar or other objects.
- For all objects that do not take part in the data flow, e.g. text boxes, the property "Position automatically" is selected.

The function is executed only manually in the open CFC and you cannot enable it permanently.

##### Requirement

- A CFC is open.
- "Data flow" is displayed.
- Multiple objects have been added.

##### Procedure

1. In the toolbar select the symbol "Place blocks according to the data flow": ![Procedure](images/132689015819_DV_resource.Stream@PNG-de-DE.png)

   The selected objects are aligned automatically.
2. Use the "Undo" button in the toolbar to undo this change.

##### Result

The objects in the CFC are sorted according to the data flow.

#### Deleting an instruction or block from the CFC chart

You can delete instances of instructions and block types in a CFC chart.

> **Note**
>
> **Checking interconnections**
>
> If you delete an instruction or a block with interconnections, the interconnections are also deleted.
>
> Before deleting an instruction or block, you should check whether the chart has interconnections.
>
> The values of the respective input and output parameters are reset to the values preset in the block type.
>
> Correct the reset parameters if necessary.

##### Deleting instances in the device

When you insert a new instance of the same block type in the CFC chart after deleting an instance, this instance is given the same name as the deleted instance.

As long as the deleted instance is still in the controller, this leads to a conflict during download.

To restore consistency, perform one of the following actions:

- Full download
- 2x consecutive downloads of changes

  After the first download of changes, the instance in the device may still not have been fully deleted.

##### Requirement

- The CFC chart is open.
- An instruction or block has been created.

##### Procedure

1. Select the instruction or block.
2. Select the "Delete" command in the shortcut menu.
3. Start either a full download or two consecutive downloads of changes.

   This also deletes the instance in the device.

##### Result

The instruction or block is deleted.

All incoming and outgoing interconnections are also deleted.

As default, the affected input and output parameters are assigned the values of the type.

---

**See also**

[Adding an instruction or block to the CFC chart](#adding-an-instruction-or-block-to-the-cfc-chart)

#### Central change of a block type

##### Overview

A block type is a reusable, pre-defined function.

You can create your own block type or use a block type from a library.

You create an instance by inserting a block type into a CFC chart.

The advantage of this type-instance concept is that any change of the block type can be implemented at all instances.

##### Changing the block type

If the interface, the system attributes or the algorithm is changed at a block type, then an update of the instances in the CFC charts becomes necessary.

To this end, the changed block is added to a CFC chart.

All instances of this block are also changed in all CFC charts of this target system so that they match the new block.

**Options for block change**

You can change the following blocks:

- Self-created block type in the "Program blocks" folder in the project tree
- Provided block type in a library

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Interface change can result in full download**  After interface changes at the block type and subsequent update of the block type in the target system, you will often only be able to compile and load the entire software.  An interface change is, for example, the change of the parameter data type.  Loading of the entire software with the S7 target system requires a CPU stop.  **Effects of the block change**  Note the effects on the instances with every change.  **Do not change internal CFC blocks**  CFC creates system blocks that are displayed in a number of views or lists, for example, under "Program information".  You may not change these objects.  Only edit your own blocks and instructions using the STEP 7 editors. |  |

> **Note**
>
> **"Instructions" task card**
>
> You cannot change block types in the "Instructions" task card because they are an integral part of CFC.

##### Updating the instances

To update the instances after a block type change, you will have to import the new version of the block type into the CFC.

You have the following options to do this:

- Blocks from a library:

  Adding the changed block type to a CFC chart
- Blocks from the "Program blocks" folder:

  - Adding the changed block from the "Program blocks" folder
  - Use the "Chart sequence & extras" editor in the "Block types" tab (depending on the target system)

Before the changed block type is imported, the block versions are compared.

The differences are displayed in the "Update blocks" dialog.

An icon in the last column indicates whether or not the change requires a download of the software.

Additional information: "[Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)"

##### Effects on the instances

> **Note**
>
> **Checking the effects**
>
> When you update an instance after a central block type change, all other block instances in the CFC charts of the CPU are changed automatically.
>
> This also applies to instances in password protected CFC charts.
>
> Therefore, check the effects in the instances before you perform the update.

**Block name**

Changing the block name does not affect existing instances.

Only the name of the block type is changed in the "Type data" area of the instance properties.

The instance name in the "Instance data" area is not changed.

**Comments**

Comments are usually overwritten at the instances.

However, comments that were changed for specific instances are not overwritten.

**Parameter**

Examples of typical changes to block type parameters:

| Change to the block type | Effect |
| --- | --- |
| Parameter is added | This change takes effect in the instances.  The system attributes are set to default values.  Check and update the parameter assignment or interconnection of the new parameter at the instances.  The interconnections are hidden when the block instance becomes too large for display in the CFC chart due to an increase in the size of the block type.  If necessary, move the instance so that it is displayed completely in the chart. |
| Parameter was deleted | The parameter is deleted in the instances.  If the parameter is interconnected, the interconnection is also deleted.  After the deletion, check the parameter assignment at the interconnection partner. |
| Changed data type of a parameter | The behavior corresponds to deleting and creating a new parameter. |
| Changed parameter name | The system cannot automatically make a connection to the old name.  This happens when you delete a parameter and create a new one. |
| Changed sequence of parameters | The sequence of parameters is taken into account.  The interconnection, the parameter assignment, and the attributes are retained.  However, moving two subsequent parameters with the same data type only corresponds to renaming the two parameters. It does not include the interconnection of the parameters. |

**Values, comments and system attributes of the parameters**

Effect of attribute changes:

- Changes that cannot be made for a specific instance are made automatically at the instances.
- Instance-specific values, comments, and system attributes are usually overwritten.

  However, values, comments or system attributes that were changed for specific instances are not overwritten.

The table shows examples of deviations from this rule:

| Change to the block type | Effect |
| --- | --- |
| The "Configurable" attribute is deleted. | The "Configurable" attribute cannot be changed for specific instances.  The change has an effect on all instances:  - Existing parameter assignments of the input or output parameter are maintained. |
| The "Interconnectable" attribute is deleted. | The "Interconnectable" attribute cannot be changed for specific instances.  The change has an effect on all instances:  - Existing interconnections are deleted. |
| The "Low limit" and "High limit" attributes are configured. | "Low limit" and "High limit" cannot be changed for specific instances.  The change has an effect on all instances:  - When an existing parameter value exceeds a limit value in the instance, the parameter value is set to the default value of the block. |

---

**See also**

[Type and instance](#type-and-instance)
  
[Creating a block type for CFC](#creating-a-block-type-for-cfc)
  
Blocks in CFC charts for S7
  
[Properties of the tags in data blocks](Programming%20data%20blocks.md#properties-of-the-tags-in-data-blocks)

#### Updating instances of a changed block type

##### Overview

Blocks added in the CFC chart represent an instance of a block type.

The block type exists, for example, in a library or in the "Program blocks" folder of the project tree.

After changing a block type, you can update the instances of this block in all CFC charts of a target system.

Additional information: "[Type and instance](#type-and-instance)"

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Interface change can result in full download**  After interface changes at the block type and subsequent update of the block type in the target system, you will often only be able to compile and load the entire software.  An interface change is, for example, the change of a default value.  Loading of the entire software with the S7 target system requires a CPU stop.  **Effects of the block change**  Note the effects of the change on the updated instances.  Additional information: "[Central change of a block type](#central-change-of-a-block-type)" |  |

##### Requirement

- A CFC chart is open.
- The changed block type exists in a library, for example.

##### Procedure

1. Select the changed block type in a library or in the project tree in the "Program blocks" folder.
2. Drag the symbol in the CFC chart.

   If at least one instance of the block is used in a CFC chart of the CPU, the "Update blocks" dialog is displayed.

   - The changes and their effects are listed.
   - An icon in the last column indicates whether or not the change requires a download of the software:

     ![Procedure](images/130975285899_DV_resource.Stream@PNG-de-DE.png) No download necessary *)

     ![Procedure](images/130975277707_DV_resource.Stream@PNG-de-DE.png) Download of the software required

     ![Procedure](images/132531361291_DV_resource.Stream@PNG-de-DE.png) Download with CPU Stop required

     *) Regardless of CFC, changed blocks may be downloaded by STEP 7 into the controller.
3. To update the instances, click "OK".

   The block instances are updated in all CFC charts of the same target system to the changed version.

   If necessary, change the interconnections at the instances.

##### S7 target systems: Alternative procedure

You can also update block types in the "Program blocks" folder in the "Block types" tab of the "Chart sequence & extras" editor.

The functionality in this tab is specific to the target system.

Additional information: "Working with CFC charts for S7 > Updating block type imported in CFC"

##### Result

The instances of a changed block type are updated in all CFC charts of the target system.

---

**See also**

Blocks in CFC charts for S7

#### Creating a block type for CFC

Complex functions can be combined and reused in a block in the type-instance concept.

You can define a block you have created yourself as a type and save it in the project library or a global library.

##### Requirement

- The "Libraries" task card is displayed.
- You have created a block in the project tree.

##### Procedure

1. Select the pane with the library in the "Libraries" task card in which you want to define a block type:

   - The "Global libraries" pane for the required global library
   - The "Project library" pane
2. Click the "Master copies" folder in the selected library.

   Any existing subfolders are displayed.

   You can create a new subfolder, if necessary, in the shortcut menu with the "Add folder" command.
3. Copy the required block with drag-and-drop to the intended position in the "Master copies" folder.

   The shape of the mouse indicates where you can add the block.

##### Result

A new block type has been defined in the project library or in a global library.

You can create instances of this block type and use them in CFCs.

---

**See also**

[Type and instance](#type-and-instance)
  
[Central change of a block type](#central-change-of-a-block-type)

### Configuration and interconnection of input and output parameters

This section contains information on the following topics:

- [Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)
- [Pre-assignment of attributes for input and output parameters](#pre-assignment-of-attributes-for-input-and-output-parameters)
- [Representation and properties of interconnections](#representation-and-properties-of-interconnections)
- [Interconnections with structures as input and output parameters](#interconnections-with-structures-as-input-and-output-parameters)
- [Changing the color of interconnection lines](#changing-the-color-of-interconnection-lines)
- [Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
- [Working with multiple interconnections](#working-with-multiple-interconnections)
- [Interconnections to parameters of the chart interface](#interconnections-to-parameters-of-the-chart-interface)
- [Interconnecting the input and output parameters with an external tag](#interconnecting-the-input-and-output-parameters-with-an-external-tag)
- [Adding or removing input parameters](#adding-or-removing-input-parameters)
- [Negating input parameters](#negating-input-parameters)
- [Hiding input and output parameters](#hiding-input-and-output-parameters)
- [Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)
- [Changing an interconnection](#changing-an-interconnection)
- [Changing an interconnection to an external tag](#changing-an-interconnection-to-an-external-tag)
- [Deleting an interconnection](#deleting-an-interconnection)
- [Overview of textual interconnections](#overview-of-textual-interconnections)
- [Creating, editing and closing textual interconnections](#creating-editing-and-closing-textual-interconnections)
- [Textual interconnections in the "Chart sequence & extras" editor](#textual-interconnections-in-the-chart-sequence-extras-editor)

#### Setting the parameters of the input and output parameters

##### Overview

If you add an instruction from the "Instructions" task card or a block from a library to a CFC, then the parameters are assigned with the values of this object type by default.

Values that were changed at the type are passed to the instance in the CFC the next time a type import is performed.

If you assign parameter values to the input or output parameters, passing on the parameter value from the type to the instance is interrupted.

You can re-enable the passing on of these values at any time in the Inspector window. The assigned parameter value is then once again replaced by the default value of the type.

When you assign a parameter value, the entered value is checked for plausibility and syntax depending on the data type.

##### Requirement

- A CFC is open.
- "Data flow" is displayed.
- An instruction or block has been added.

##### Procedure

1. Select the required input or output parameter in the CFC.
2. Enter a value for the input or output parameter in the "Value" field of the Inspector window.

   This stops the value from being passed on by the type of this instruction or block.

   If the values for "Low limit" and "High limit" are configured at the type, these limits are taken into consideration when you make an entry in the "Value" field.
3. If necessary, enter a measurement unit in the "Unit" field or select a unit from the list.

   If a unit is assigned at the type, this unit is passed on to the instance.

   You can disable this process by making an entry or selecting from the list.

##### Alternative procedure

As an alternative, you can set the input or output parameters directly in the CFC.

If you need to set many parameters for the input or output parameters, use the "control flow" mode.

##### Result

The input or output parameter has been assigned.

When you download the CFC to the device, the input or output parameter has the assigned value as default.

#### Pre-assignment of attributes for input and output parameters

##### Attributes at the block type

You can configure the attributes of an input or output parameter at each instance of a block.

It is also possible to pre-assign the attributes of an input or output parameter at the block type.

These pre-assigned values are passed on at an instance of this type.

You can either accept this pre-assignment or, if necessary, change it for specific instances.

These attributes include, for example:

- Can be changed for specific instances:

  - Comments
  - Attributes, e.g., "Value", "Unit", "Invisible", "For test"
- Cannot be changed:

  - e.g. the attributes "Configurable", "Interconnectable" "Low limit", High limit"

##### Basic procedure

1. Open the block used as type, for example, in the "Program blocks" folder of the project navigation.
2. Select the required input or output parameter in the interface.

   The "General" tab is displayed in the Inspector window.
3. Under "Attributes", make the required settings to be passed on as pre-assignment to the associated instances.
4. Save and compile the changed block.

   If you wish to use the changed block as type in a library, copy the changed block into the respective library.
5. Update the instances of this type in the CFC.

   Additional information: "[Updating instances of a changed block type](#updating-instances-of-a-changed-block-type)"

##### Display and update at the instance

If the input or output parameter is selected, the pre-assigned values are displayed in the "Type data" column under "General" in the Inspector window.

The pre-assignments for values and functions configured in the type are passed on to the instance.

You can make your own configurations in the instance, e.g., enter start values, select units. This stops the respective value from being passed on by the block type.

The following symbols display the status:

| Icon | Meaning |
| --- | --- |
| ![Display and update at the instance](images/35945135243_DV_resource.Stream@PNG-de-DE.png) | The value is passed on from the type to the instance. |
| ![Display and update at the instance](images/35939430795_DV_resource.Stream@PNG-de-DE.png) | The value is not passed on from the type to the instance because it was changed at the instance.  You can re-enable the passing on by clicking on this symbol. |

**Updating instance**

Instance-specific changes are not automatically overwritten when the type is updated.

##### Notes: "Low limit" and "High limit"

The low limit and high limit values are displayed after the data type as additional information at the parameter of the block instance in the "Type data" column of the "Type" field.

"Low limit" and "High limit" cannot be changed for specific instances.

These two values have an effect on all instances when the type is updated:

If an existing parameter value exceeds a limit value, the parameter value is set to the default value of the type and a log entry is made.

**Example**

- Data type = INT
- Low limit = 10
- High limit = 90

Display in the "Type" field:

- `Int (10..90)`

---

**See also**

Blocks in CFC charts for S7
  
[Properties of the tags in data blocks](Programming%20data%20blocks.md#properties-of-the-tags-in-data-blocks)

#### Representation and properties of interconnections

##### Routing of an interconnection

When configuring interconnections, you only specify which output parameter is interconnected with which input parameter.

The routing of the interconnection is handled by the editor. Other objects in the CFC chart are automatically avoided.

If you move interconnected instructions or blocks in the CFC chart, the routing of the interconnections is adapted automatically.

The following figure shows the routing of an interconnection around a third object:

![Routing of an interconnection](images/20763800587_DV_resource.Stream@PNG-de-DE.png)

If you have marked text boxes as being in the "background", these are ignored by the routing.

##### Interconnection options

The following options are possible for interconnections:

- From one output parameter to one or several input parameters
- From one input or output parameter to one external tag

  An overview of the points of use of interconnected tags and global data blocks can be found in the "Tag interconnections" tab of the "Chart sequence & extras" editor.
- Several options are available for input and output parameters of STRUCT data type.

  More information: "[Interconnections with structures as input and output parameters](#interconnections-with-structures-as-input-and-output-parameters)"

> **Note**
>
> Interconnections to constants are not possible.

**Interconnections from one output parameter to several input parameters**

You can use the value of an output parameter as the value for several input parameters.

You need a multiple interconnection for this purpose.

An interconnection node is inserted for each branch to an input parameter. An interconnection node corresponds to an interconnection at the output parameter.

If you drag an interconnection node to an output parameter, all interconnections leaving the interconnection node is interconnected to this output parameter.

The following figure shows an interconnection from one output parameter to two input parameters with one interconnection node:

![Interconnection options](images/20763766667_DV_resource.Stream@PNG-de-DE.png)

##### Interconnection that cannot be fully displayed

Every object and every interconnection requires space in the CFC chart. If interconnections cannot be displayed fully, the editor automatically uses connectors.

The following figure shows an interconnection between two AND logic operations that cannot be displayed completely:

![Interconnection that cannot be fully displayed](images/20763793547_DV_resource.Stream@PNG-de-DE.png)

The interconnection is represented by connectors with the same numbers.

If there are multiple connectors, the numbers are incremented continuously.

To jump between connectors in the view, double-click the respective connector.

##### Interconnection beyond sheet borders

If you interconnect instructions or blocks beyond sheet borders, the interconnection leads as far as the sheet bar of the sheet.

A connector is inserted in the sheet bar. The connector has the name of the target object and the parameter.

If the destination of an interconnection is located in a different CFC chart, the name of the CFC chart is also displayed. When the CFC chart contains multiple chart partitions, the chart partition name and the sheet number are also displayed.

**Color display**

The color of the connector shows the type of interconnection.

- Connector color "Light beige":

  The selected target connector is displayed in the sheet bar.
- Connector color "Dark beige":

  The selected target connector is displayed in the extended sheet bar.

Connectors 1 to 8 are shown in the following figure at the different output parameters.

- Connectors "1" to "5" as well as "7" are "light beige".

  This means the selected target connector is displayed in the sheet bar.
- Connectors "6" and "8" are "dark beige".

  This means the selected target connector is displayed in the extended sheet bar.

![Interconnection beyond sheet borders](images/161361469451_DV_resource.Stream@PNG-de-DE.png)

**Navigation beyond sheet borders**

When you double-click on a connector or sheet bar entry, the destination of the interconnection is displayed centered in the work area.

To jump back, select the "Back" command in the shortcut menu of the chart.

To continue configuration, use "Back" to switch between the last two positions.

**Display in the sheet bar view**

The following figure shows an interconnection between two instructions on different sheets of a CFC chart with the sheet bars enabled.

![Interconnection beyond sheet borders](images/20763773707_DV_resource.Stream@PNG-de-DE.png)

If the sheet bar view is disabled, the following rules apply to interconnections between sheets or between charts:

- Between sheets:

  The interconnection is displayed normally on one sheet.
- Between charts:

  The connector is placed next to the parameter.

**Placing a connector manually**

In a chart with disabled sheet bar view, you can manually move connectors between sheets and between charts:

- Automatic placing of the moved connector is disabled.

  The connector remains in this position, regardless of the associated instruction position.
- To reenable automatic positioning, select the "Position automatically" option from the shortcut menu of the connector.

##### Signal tracking for interconnections

If you click on an interconnection or a connector, the interconnection is highlighted in color. The mouse pointer changes and is shown as "Interconnection cursor".

If output parameters have several interconnections, which interconnection is highlighted depends on where you click. Depending on the position of the click, either all interconnections or only some of them are highlighted.

You have the following options to track a signal for an interconnection across sheets:

- A single click on the connector at the parameter of the block or instruction displays the associated connector in the sheet bar or the extended sheet bar.
- If you double-click on a connector in the sheet bar, then the destination of the interconnection is displayed in the work area.

  Depending on the position of the interconnection target, the respective sheet of the same CFC chart or chart partition is displayed or the respective CFC chart opened.

  To jump back or to switch between positions, select the "Back" command in the shortcut menu of the chart.

  For navigation between the chart partitions, also use the drop-down list or the keyboard shortcuts <Shift+PgUp> and <Shift+PgDn>.

**Example**

The following figure shows an output parameter with multiple interconnections of a sheet-internal interconnection.

The arrow shows the click position and the resultant color highlighting.

![Signal tracking for interconnections](images/20763815051_DV_resource.Stream@PNG-de-DE.png)

##### Color of connection lines depends on the data type

The interconnection lines in the "Data flow" view of the CFC chart are displayed in different colors depending on the data type.

The assignment of the data type and color can be changed.

The data type of the data source determines the shown color.

For interconnections to operands whose data type is not defined, the default value "black" is used.

More information: "[Changing the color of interconnection lines](#changing-the-color-of-interconnection-lines)"

---

**See also**

[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)
  
[CFC views](#cfc-views)
  
[Placing instructions and blocks in the CFC chart](#placing-instructions-and-blocks-in-the-cfc-chart)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Working with multiple interconnections](#working-with-multiple-interconnections)
  
[Changing an interconnection](#changing-an-interconnection)
  
[Changing the color of interconnection lines](#changing-the-color-of-interconnection-lines)
  
[Deleting an interconnection](#deleting-an-interconnection)
  
[Adding or removing input parameters](#adding-or-removing-input-parameters)
  
[Hiding input and output parameters](#hiding-input-and-output-parameters)
  
[Interconnecting the input and output parameters with an external tag](#interconnecting-the-input-and-output-parameters-with-an-external-tag)
  
[Interconnections with structures as input and output parameters](#interconnections-with-structures-as-input-and-output-parameters)
  
[Negating input parameters](#negating-input-parameters)
  
TERMINAL: Summary of interconnections

#### Interconnections with structures as input and output parameters

##### Interconnecting structures and structure elements

In CFC, it is possible to interconnect the input or output parameters of the STRUCT data type as a complete structure.

However, you can also interconnect individual structure elements of a parameter of the STRUCT data type.

Structure elements can be of an elementary data type or "STRUCT in STRUCT".

> **Note**
>
> **Configuration depending on the target system**
>
> Interconnection of structures and their elements depends on the target system.
>
> **Target system S7: Interconnection with the chart interface**
>
> The individual structure elements cannot be interconnected for a parameter of the STRUCT type in the chart interface.
>
> Only the complete structure can be interconnected.

##### Requirement for interconnection

To interconnect the structure and its elements at the block icon, the "invisible" option must be disabled for the parameter containing the structure or structure element. The corresponding parameter is visible at the block icon.

If you only need to interconnect individual structure elements, the parameter containing the corresponding structure element must be visible, but not necessarily the parameter containing the structure itself.

The "invisible" option is enabled by default and must be disabled at specific instances for each parameter that contains a structure or structure element.

##### Appearance

**Block icon in the CFC**

Parameters of the STRUCT data type and their elements are displayed at the block icon similar to other block parameters. Requirement is that the "invisible" option is disabled in the parameter properties.

The visible parameters of structure elements are displayed with indent, even if the "invisible" option is set for the parameter containing the structure itself.

**Control flow**

Structure elements are displayed in the control flow with right indent.

**Invisible structures and structure elements at the block**

In CFC, the triangular icons below the block icon are normally used to indicate whether this block contains hidden parameters, or hidden interconnected parameters.

For parameters of the STRUCT data type, the triangular icons are only used to indicate the hidden, interconnected structures and structure elements, as structures and structure elements are normally hidden in CFC.

##### Interconnection options

- Input parameter "Input" or "InOut" with the STRUCT data type:

  The parameter can either be interconnected as a complete structure or the individual structure elements of this input parameter can be interconnected individually.
- Output parameter "Output" with the STRUCT data type:

  The complete structure, as well as individual structure elements, can be interconnected.
- Individual structure elements of input or output parameters of the STRUCT data type can be interconnected to a different, compatible input or output parameter.

---

**See also**

[Interconnecting the input and output parameters with an external tag](#interconnecting-the-input-and-output-parameters-with-an-external-tag)

#### Changing the color of interconnection lines

##### Line color and data type

The interconnection lines in the "Data flow" view of the CFC are displayed in different colors depending on the data type.

The assignment of the data type and color can be changed.

The data type of the data source determines the shown color.

For interconnections of operands whose data type is not defined, the default value is "black".

Changing the color assignment has an effect on the display of interconnection lines in an open CFC.

##### Procedure

1. Select the "Settings" command in the "Options" menu.
2. Select the "Charts > CFC > General" group in the area navigation.
3. Select the desired colors for the data types in the "Color of interconnection lines" area.

   You can also use the "Default values" button to reset all settings to the default values.

##### Result

The color setting for the interconnection lines has been changed.

#### Interconnecting input and output parameters

##### Overview

You always interconnect an output parameter with an input parameter.

When you click on an instruction or block while creating an interconnection, the possible destination points are shown in color.

The following rules apply to interconnecting input and output parameters:

- You can only interconnect an input parameter once.
- You can interconnect an output parameter more than once.
- An interconnection is only possible if the data types of the input and output parameters are compatible.

**Possible procedures**

You can create interconnections using the following methods:

- Double-click / Click
- Drag-and-drop
- Click Clack
- <C> key and click
- Copy&Paste
- Manual input of the interconnection target (Textual interconnection)

##### Requirement

- All CFC charts are open whose parameters you want to interconnect.
- "Data flow" is displayed.
- Instructions/blocks have been inserted.

##### Procedure

1. Double-click on the required output parameter.

   An interconnection line is shown between the output parameter and the mouse pointer.
2. If the interconnection destination is in the same chart, click on the input parameter at the target object that you want to interconnect.

   When you move the mouse over the input parameters, the interconnectable parameters are displayed with a green background.

   The selected parameter is displayed with a light green background.

   ![Procedure](images/143633304715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/143633304715_DV_resource.Stream@PNG-de-DE.png)

   The interconnection is inserted and the interconnection line displayed.
3. If the interconnection destination is located in another CFC chart, move the mouse pointer onto the respective CFC chart in the taskbar after step 1.

   The CFC chart is displayed in the work area.
4. In this CFC chart, click on the input parameter at the target object that you want to interconnect.

   The interconnection is inserted and the interconnection line displayed.

   Depending on the space available in the CFC chart, the interconnection is displayed either fully or by connectors.
5. To cancel the interconnection, click on a free location in the CFC chart or press <Esc>.

##### Alternative procedure: Drag-and-drop

1. Select the input or output parameter and keep the mouse button pressed.
2. Drag the interconnection line to the desired parameter and release the mouse button.

**Drag-and-drop between charts**

1. Open the CFC chart and the target chart in the data flow.
2. To display both charts, click one of the buttons for splitting the editor area: ![Alternative procedure: Drag-and-drop](images/144473179531_DV_resource.Stream@PNG-de-DE.png)
3. Drag the cross-chart interconnection with the mouse button.

As an alternative, drag the parameter to the target chart using the taskbar of the open charts.

##### Alternative procedure: Click Clack

1. Select the interconnection line at the input or output parameter.

   The selected parameter turns magenta.
2. Select a parameter that is shown in green when you place the mouse cursor over it.
3. To create multiple interconnections, click on additional parameters displayed in green while pressing the <Ctrl> key.

   The interconnections for the clicked parameters are created.

##### Alternative procedure: <C> and click

1. Select the input or output parameter and press the <C> key.

   The selected parameter turns magenta.
2. Click on a parameter that is displayed in green.
3. To create multiple interconnections, click on additional parameters displayed in green while pressing the <Ctrl> key.

   The interconnections for the clicked parameters are created.

##### Alternative procedure: Copy&Paste

**Keyboard**

1. Select the output parameter and press <Ctrl+C>.
2. Select the output parameter and press <Ctrl+V>.

Use the arrow keys to switch between the parameters of a block or between blocks.

**Mouse operation**

1. Select the "Copy" entry in the shortcut menu of the output parameter.
2. Select the "Paste" entry in the shortcut menu of the input parameter.

##### Alternative procedure: Manual input

**Enter parameter manually**

Interconnection possibilities:

- Direct entry of the parameter in the input field

  You are supported by the auto-complete function in this process.
- Opening a selection dialog with the triangle symbol to the right of the input field

Syntax for manual input:

- Interconnection destination is in the other CFC chart:

  - "\<Chart name>\<Object name>.<Parameter name>"

    Example: \Chart_1\AND_1.OUT2
- Interconnection destination is in the same CFC chart:

  - "<Object name>.<Parameter name>"

    Example: AND_1.OUT2

**Enter operand manually**

Interconnection possibilities:

- Direct entry of the operand in the input field

  You are supported by the auto-complete function in this process.

Syntax for manual input:

- Interconnection destination is an external tag.

  - "<Tag name>"

    Example: "StartMotor"
- Interconnection target is a data block:

  - "<DB name>.<Parameter name>"

    Example: "MotorDB.Start"

**Procedure**

1. Select the parameter to be interconnected at the block in "Data flow" or the corresponding cell in "Control flow".
2. To create an interconnection to an address:

   - Select "Interconnection to operand..." from the shortcut menu.
   - Enter the interconnection destination manually or use the selection dialog box.
3. To create an interconnection to a parameter select the command "Textual interconnection to chart..." from the shortcut menu.

   - Enter the interconnection destination manually or use the selection dialog box.

Additional information: "[Creating, editing and closing textual interconnections](#creating-editing-and-closing-textual-interconnections)"

##### Result

The parameters of the two instructions/blocks are interconnected with each other.

Depending on the space available in the CFC chart, the interconnection is displayed either fully or by connectors.

To display an overview of the points of use of interconnected tags and global data blocks, use the "Tag interconnections" tab of the "Chart sequence & extras" editor.

---

**See also**

[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)
  
[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Working with multiple interconnections](#working-with-multiple-interconnections)
  
[Deleting an interconnection](#deleting-an-interconnection)

#### Working with multiple interconnections

##### Overview

You can interconnect an output parameter with several input parameters.

Place instructions or blocks with multiple interconnections in the CFC chart so that few interconnection nodes are necessary.

The following figure shows the same interconnection, the only difference being the positioning of the objects:

![Overview](images/133401497611_DV_resource.Stream@PNG-de-DE.png)

##### Creating multiple interconnections

You create multiple interconnections by connecting the output parameter to the input parameters of the target objects.

Depending on the positions of the target objects, this step results in one or more interconnection nodes.

You have the following options to interconnect an output parameter with several input parameters:

**Procedure: <C> key and click**

1. Click on the output parameter.
2. Press the <C> key.
3. Press and hold down the <Ctrl> key and click on the input parameters one after the other.

**Alternative procedure: Click Clack**

1. Select the interconnection line at the input or output parameter.

   The selected parameter turns magenta.
2. Select a parameter that is shown in green when you place the mouse cursor over it.
3. Press and hold down the <Ctrl> key and click on other parameters displayed in green.

**Alternative procedure: Copy&Paste**

1. Click on the output parameter.
2. Press the shortcut <Ctrl+C>.
3. Click on the input parameters, one after the other, and press <Ctrl+V>.

Instead of the keyboard shortcuts, you can also use the "Copy" and "Paste" entries in the shortcut menu of the parameters.

**Alternative procedure: Drag-and-drop, double-click**

With this procedure you need to return to the output parameter for each interconnection.

1. Create an interconnection from the output parameter to the input parameter.
2. Select the output parameter again and create the next interconnections, one after the other.

##### Editing multiple interconnections

If you point to an interconnection with the mouse, editing areas are marked.

The following figure shows the editing areas with two multiple interconnections:

![Editing multiple interconnections](images/61424873995_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Interconnection at the input parameter.  Drag-and-drop: Interconnection with another input parameter.  Signal tracking: If you click on an editing area at the input parameter, the interconnection is highlighted in color. |
| ② | Represents the interconnection at the output parameter of the source block.  Drag-and-drop: Interconnection with another output parameter. The interconnection then no longer belongs to the multiple interconnection. |
| ③ | Represents some of the interconnections at the output parameter of the source block.  If several interconnection nodes result, these are arranged hierarchically.  Drag-and-drop: Interconnecting the input parameters with another output parameter. |
| ④ | Represents all interconnections at the output parameter of the source block.  Drag-and-drop: Interconnecting all input parameters with another output parameter. |

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)

#### Interconnections to parameters of the chart interface

##### Overview

Hierarchical CFCs and standard CFCs have an interface.

This means that these CFCs can be configured and interconnected externally similar to blocks.

Interconnections of interface parameters with blocks within the CFC are displayed in the sheet bar of the chart with connectors.

**Parameters and data types**

New parameters can be added, modified or deleted in the Input, Output, InOut sections of the chart interface.

All CFC data types are supported in the chart interface except:

- TIMER
- COUNTER

More information: "[Adding, editing and sorting parameters of the chart interface](#adding-editing-and-sorting-parameters-of-the-chart-interface)"

> **Note**
>
> **S7 target system: Interconnection of structure elements**
>
> The S7 target system does not support interconnections of individual structure elements of parameters of the STRUCT data type in the chart interface.
>
> You can only interconnect the complete structure.
>
> **S7 target system: No hardware data types**
>
> Chart interfaces do not support any hardware data types.

##### Interconnection between interface and block parameters

You create a new interconnection between the input or output parameters of a block and an existing parameter in the chart interface.

Drag the required block parameter with the mouse to the desired location in the chart interface, for example, to the "Output" section for an output parameter of a block.

When you release the mouse button, the new interconnection is created and displayed in the sheet bar of the chart with connectors when the data type matches.

##### Interconnection with the creation of a new interface parameter

You can also create a new interconnection when the interface parameter does not exist yet.

Drag the required block parameter to an empty line of the matching section of the chart interface, for example, to the "Input" section for an input parameter of a block.

When you release the mouse button, the new interface parameter with the matching data type is created. The attributes of the associated block parameter are applied.

##### Rewire interconnection: Blocks

In a rewire you change an existing interconnection between the input and output parameters of blocks in the chart interface.

Drag the required interconnection at the block parameter to an existing parameter in the chart interface using drag-and-drop.

The mouse pointer indicates if this interconnection is possible.

When you release the mouse button, the selected interconnection is rewired to the required parameter in the chart interface.

##### Rewire interconnection: Interface and block parameters

You can also rewire an interconnection between a block parameter and an interface parameter to an existing interface parameter.

Drag the connector of this interconnection in the chart sheet bar, for example, "Input2" to an existing parameter of the chart interface, for example, "Input7".

The mouse pointer indicates if this interconnection is possible.

When you release the mouse button, the selected interconnection is rewired to the required parameter in the chart interface. The associated connector in the sheet bar is renamed, for example, to "Input7".

As long as an interface parameter has not been interconnected, the table cell of the "Data type" column has a "light gray" background color.

Upon interconnection, the background color changes to "medium gray".

---

**See also**

[Hierarchical CFC charts](#hierarchical-cfc-charts)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)

#### Interconnecting the input and output parameters with an external tag

##### Overview

If you need values from the device in the CFC, or want to return values to the PLC, interconnect an input and output parameter with an external tag.

Depending on the target system you are using, an external tag represents signals from modules or the device.

An external tag can also be a structure.

> **Note**
>
> **Interconnection only possible in the target system**
>
> You can only use external tags that belong to the same controller as the CFC.
>
> **Synchronization while compiling the chart**
>
> Only the name of the external tag is stored in the connector.
>
> Whether or not a tag with this name exists in the target system is only checked when the chart is compiled.

##### Interconnecting structures

You can interconnect structures with input and output parameters of the STRUCT data type.

You can interconnect the complete structure, as well as individual structure elements with the compatible block parameters.

Additional information: "[Interconnections with structures as input and output parameters](#interconnections-with-structures-as-input-and-output-parameters)"

##### Requirement

- A CFC is open.
- The detail window is displayed.
- "Data flow" is displayed.
- Instructions/blocks have been inserted.
- The data types of the external tag and the input or output parameters are compatible.

##### Procedure

1. Select the folder in the project tree in which the external tags are stored.

   The position of the folder depends on the target system you are using.
2. Drag the external tag from the detail window to the input or output parameter.

##### Alternative procedure

As an alternative, you can also interconnect the external tag using the shortcut menu of the input or output parameter.

If you have created a tag for a signal, you can drag a signal of a module to an input or output parameter directly from the device configuration.

##### Result

The input or output parameter is interconnected to the external tag.

The connector with the tag name is positioned either in the sheet bar or besides the parameter depending on the sheet bar view you have set.

---

**See also**

[Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)
  
[Copying instructions, blocks and charts](#copying-instructions-blocks-and-charts)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)

#### Adding or removing input parameters

##### Overview

When you insert an instruction to a CFC chart, this object already comes with a certain number of input parameters by default.

You have the option to change the number of input parameters with generic instructions.

There are generic instructions in CFC in the "Instructions" task card in the following instruction families:

- BIT_LGC: Bit logic operations
- MATH_FP, MATH_INT: MathFloat (arithmetic instructions)
- MULTIPLX: Multiplexer
- WRD_LGC: Word logic operations
- Additional instructions: TERMINAL (compilation of interconnections)

When an instruction can be extended, the following symbol is displayed at the bottom of the instruction icon: ![Overview](images/173863540875_DV_resource.Stream@PNG-de-DE.png)

The symbol is hidden once the maximum number of possible input parameters has been reached.

##### Changing the number of parameters

You can change the number of input parameters using the following options:

- Adding or removing input parameters:

  You can make both changes in the properties of the Inspector window.
- Adding input parameters:

  To add an input parameter to the instruction, click on the icon at the instruction symbol: ![Changing the number of parameters](images/173863540875_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Reducing the number**
>
> The value cannot be lower than the number of interconnected input parameters, because only non-interconnected input parameters can be deleted.
>
> If several parameters are not interconnected, the highest index number of the interconnected parameters determines the value. If the 1st and the 5th of 10 parameters are interconnected, the lowest value corresponds to the index of the 5th parameter.

**Example**

![Changing the number of parameters](images/173863544459_DV_resource.Stream@PNG-de-DE.png)

The figure shows an "OR" instruction with two input parameters that are not interconnected.

The following icons are displayed at the bottom of the instruction symbol:

| Icon | Meaning |
| --- | --- |
| ![Changing the number of parameters](images/173863540875_DV_resource.Stream@PNG-de-DE.png) | The number of input parameters can be increased. |
| ![Changing the number of parameters](images/16251712651_DV_resource.Stream@PNG-de-DE.png) | At least one input or output parameter is invisible. |

##### Requirement

- A CFC chart is open.
- An expandable instruction has been added.

##### Procedure

1. Select the required instruction in the CFC chart.
2. In the Inspector window, select the "Properties" tab and then the "General" tab.

   The current number of inputs are displayed in the "Number of input parameters" field.
3. If you want to add an input parameter, simply increase the value in the "Number of input parameters" field.

   You can also add an input parameter by clicking the icon in the CFC chart below the instruction symbol.
4. If you want to delete an input parameter, simply decrease the value in the field "Number of input parameters".

##### Result

One or several input parameters have been added or removed.

You can see an overview and the status of all input and output parameters in the Inspector window in the "Properties" tab under "Parameters".

#### Negating input parameters

##### Requirement

- The input parameter is interconnected.
- The input parameter has the BOOL data type.

##### Procedure

1. Select the interconnection of the input parameter.
2. Select the "Negate" option in the shortcut menu of the interconnection.

   Alternatively, select the option in the properties of the interconnection in the inspector window.

##### Result

The negation symbol is shown at the input parameter.

The value at the input parameter is negated.

If you move or copy the negated interconnection, the negation is retained.

The following figure shows a negated interconnection:

![Result](images/20771447947_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)

#### Hiding input and output parameters

The space available for objects, such as instructions, blocks and interconnections, in a CFC chart is limited by the sheet size.

To gain more space for displaying objects on a sheet, you can hide the input or output parameters. This makes the CFC chart clearer to read.

##### Manage hidden parameters

To display the overview and the status of all parameters, select the instance in the chart and click on "Properties > Interface" in the Inspector window.

If the hidden parameter is interconnected, it is also listed under "Invisible interconnections".

To edit the interconnection of a hidden parameter, make the interconnection listed in "Invisible interconnections" visible again. As a result, the interconnected parameter is visible again.

##### Display at the icon

Hidden parameters of an instruction or block are identified at the associated icon separated by input and output parameters:

| Symbol | Meaning |
| --- | --- |
| ![Display at the icon](images/16251709451_DV_resource.Stream@PNG-de-DE.png) | One or more interconnected parameters are hidden. |
| ![Display at the icon](images/16251712651_DV_resource.Stream@PNG-de-DE.png) | One or more non-interconnected parameters are hidden. |

##### Display at the partner block

The interconnection to a hidden parameter is displayed at the partner block depending on the settings:

| Sheet bar mode | Display |
| --- | --- |
| Static sheet bar | In the sheet bar |
| Dynamic sheet bar | In the sheet bar |
| No sheet bar | As connector |

##### Requirement

- A CFC chart is open.
- An instruction or block has been added.

##### Procedure

1. Select the input or output parameter.
2. Select the "Invisible" option under "General" in the Inspector window.

##### Result

The input or output parameter has been hidden.

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)

#### Displaying points of use of interconnections

##### Overview

In the "Chart sequence & extras" editor, all interconnections are displayed in the "Tag interconnections" tab.

The list of tag interconnections supports you in searching for interconnected tags and interconnected global data blocks in the CFC charts:

- You can filter the list by different criteria.
- You jump from the tag line in the table directly to the reference location in the CFC chart.
- The list is comparable to the cross-reference list.

  However, unlike in the cross-reference list, you cannot add new entries.

##### CFC tag interconnections

The table contains the following information:

| Column | Content |
| --- | --- |
| Tag name | Name of the interconnected tag:  - Tags - Global data blocks |
| Address | Address of the interconnected tag |
| Data type | Data type of the interconnected tag |
| Read/write | Identification of the access:  - Read access:   Interconnection of output parameters ("Output") - Write access:   Interconnection of input parameters ("Input", "InOut") |
| Path | Path of the interconnection:  - Chart name - Block instance name - Parameters   The path is linked with the interconnected parameter.  When clicking on the path, the view jumps to the reference location in the data flow. |
| Comment | Comment for the tag  Comments of the CFC charts, instances and parameters are not included. |
| Block type | Type of the interconnected block |

##### Requirements

Requirement for the full functional scope of the "Tag interconnections" table:

- The CFC charts are not password-protected.

  In CFC charts with configured password, the interconnection paths are not shown in full.

  You have to enter the password to jump to the interconnection point.

  To use the full function scope, open the password-protected CFC charts by entering the password.

##### Procedure

1. Open the "Chart sequence & extras" CFC editor.
2. Select the "Tag interconnections" tab.

   A table with all interconnections in the CFC charts of the control is displayed.
3. To filter the table, enter the desired character string in the field under the column title.

   - Upper and lower cases have no effect.
   - To deactivate the filter in a column, click the filter line "*".
   - To deactivate all filters, click the filter symbol above the line numbers: ![Procedure](images/165126767755_DV_resource.Stream@PNG-de-DE.png)

   If you click a column title, the lines are sorted alphabetically in ascending or descending alphabetical order. A further click deactivates the sorting.

   Depending on the number of lines, the sorting may take some time though. Avoid sorting large tables.
4. To jump to the point of use in the data flow, click on the interconnection path in the "Path" column.

   Alternative procedure:

   - Select the line and in the toolbar of the table click the symbols "Data flow" or "Control flow": ![Procedure](images/161095825035_DV_resource.Stream@PNG-de-DE.png), ![Procedure](images/161095935883_DV_resource.Stream@PNG-de-DE.png)
   - Select the jump to the data flow or control flow in the shortcut menu of the line.

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Working with multiple interconnections](#working-with-multiple-interconnections)
  
[Interconnections to parameters of the chart interface](#interconnections-to-parameters-of-the-chart-interface)
  
[Changing an interconnection](#changing-an-interconnection)

#### Changing an interconnection

You can change the existing interconnection with drag-and-drop.

Additional information: "[Working with multiple interconnections](#working-with-multiple-interconnections)"

##### Requirement

- A CFC is open.
- The parameters are interconnected.

##### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. Select the interconnection. 2. Perform one of the following actions:               ![Procedure](images/20778345483_DV_resource.Stream@PNG-de-DE.png)         ![Procedure](images/20778345483_DV_resource.Stream@PNG-de-DE.png)        | Symbol | Meaning |    | --- | --- |    | ① | Drag-and-drop: Interconnection with another output parameter. |    | ② | Drag-and-drop: Interconnection with another input parameter. | |  |

---

**See also**

[Deleting an interconnection](#deleting-an-interconnection)
  
[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)
  
[Displaying points of use of interconnections](#displaying-points-of-use-of-interconnections)

#### Changing an interconnection to an external tag

##### Requirement

- A CFC is open.
- Instructions/blocks are interconnected.
- "Data flow" is open.

##### Procedure

1. Select the connector with the tag name.
2. Select the external tag from the object list.

##### Result

The interconnection has been changed.

As an alternative, you can also change the interconnections of an instruction or block in the control flow.

---

**See also**

[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)

#### Deleting an interconnection

##### Requirement

- A CFC is open.
- Instructions/blocks are interconnected.
- "Data flow" is open.

##### Procedure

1. Select the interconnection line at the input parameter.
2. Select "Delete" in the shortcut menu of the interconnection line.

##### Result

The interconnection is deleted.

As an alternative, you can also delete the interconnections of an instruction or block in the control flow.

---

**See also**

[Representation and properties of interconnections](#representation-and-properties-of-interconnections)
  
[Changing an interconnection](#changing-an-interconnection)
  
[Hiding input and output parameters](#hiding-input-and-output-parameters)
  
[Interconnecting input and output parameters](#interconnecting-input-and-output-parameters)

#### Overview of textual interconnections

##### Textual interconnections

Textual interconnections are used for interconnections at which the interconnection source, for example a block or chart output, does not yet exist.

A textual interconnection serves as the placeholder for a future interconnection.

Enter a free text with up to 1000 characters as the textual interconnection. The same characters are permitted as for interconnections.

You can create, edit, delete and close textual interconnections in the "Data flow" or "Control flow".

**"Chart sequence & extras" editor**

Depending on the target system, the textual interconnections of a project are displayed in the "Textual interconnections" tab.

You can close or delete the interconnections in the editor.

You can change the path of the interconnection only in the data flow or control flow.

**More information**

- "[Creating, editing and closing textual interconnections](#creating-editing-and-closing-textual-interconnections)"
- "[Textual interconnections in the "Chart sequence & extras" editor](#textual-interconnections-in-the-chart-sequence-extras-editor)"

##### Overview

A textual interconnection can only be created at a block/chart input and always references a block or chart output in the CFC.

**Entering text of the textual interconnection**

- If, after the completion of the entry, the entered text of the textual interconnection can be interpreted as a reference to a valid path "\Chart\Block.Parameter", the textual interconnection is closed immediately and is replaced by a real interconnection.

  This means that each object can be addressed in the same chart, in a different chart or in a lower level chart.
- If the configured text of the textual interconnection cannot be interpreted as a reference to a valid path, this textual interconnection remains "open". The entered text is displayed.

  In the "Data flow", an interconnection is then established to the sheet bar and the "Textual interconnection" symbol is displayed.

  When a referenced interconnection source is created after the textual interconnection has been created, this textual interconnection remains "open" until the user closes it manually.
- Textual interconnections to other sources, such as tags, are not possible.

**Copying a chart object**

When a chart object is copied, a textual interconnection at this object is not copied.

**Moving a chart object**

When a chart object is moved, a textual interconnection at this object is retained.

**Importing block types**

When block types are imported, the textual interconnection behaves like any other interconnection.

**Compiling and loading**

Textual interconnections are not relevant for the automation system and operating system and are therefore ignored during compiling and loading.

##### Effects of actions with the CFC chart

**Copying**

When a chart is copied, the textual interconnections are copied as well.

This is true when the chart is copied within a CPU, between different CPUs and between different projects.

In the copied chart, all existing interconnections to input parameters of the chart or its blocks are replaced by textual interconnections.

**Moving**

Existing textual interconnections are moved with the chart.

If existing interconnections are disconnected by moving a chart, a new textual interconnection is created for each disconnected interconnection.

In this process, the new textual interconnection is created depending on the previous interconnection target, because a textual interconnection can only arise at a block/chart input.

The newly created textual interconnections contain the reference to the path of the interconnection before the move.

- Moving a chart into a different folder of the same CPU:

  Because all the interconnections lie within the same CPU, they can still be reached.

  Interconnections and textual interconnections are retained.
- Moving a subchart to a different folder of the same CPU:

  Interconnections to chart objects and textual interconnections are retained.

  Interconnections to chart interfaces are converted to textual interconnections.
- Moving a chart to a different CPU or a different project:

  To move a chart, copy the chart to the other CPU or project and delete the original chart.

  Interconnections to input parameters are converted to textual interconnections.

  The interconnections of output parameters of the chart or its blocks to other charts are removed in all charts.

**Deleting**

When a CFC chart is deleted, all interconnections of the chart are also deleted.

Interconnections from other CFC charts to the deleted chart are not converted into textual interconnections but are also deleted.

---

**See also**

[Managing CFC charts and groups](#managing-cfc-charts-and-groups)
  
[Hierarchical CFC charts](#hierarchical-cfc-charts)
  
[Copying objects](#copying-objects)
  
[Copying instructions, blocks and charts](#copying-instructions-blocks-and-charts)

#### Creating, editing and closing textual interconnections

You can create, edit or close textual interconnections in the "Data flow" or in the "Control flow".

##### Requirements

- A CFC is open.
- Instructions/blocks have been inserted.
- "Data flow" or "Control flow" is open.

##### Procedure in "Data flow"

**Creating a textual interconnection**

1. Select the input parameter at the desired block or chart at which you want to create the textual interconnection.
2. Select the command "Textual interconnection to chart..." from the shortcut menu.

   An input field is opened at the parameter.
3. Enter a text.

   A maximum of 1000 characters is permitted.

Result:

- If the entered text can be interpreted as a valid path to the interconnection source, a real interconnection is created.
- If the entered text cannot be interpreted as a valid path to the interconnection source, an interconnection to the sheet bar is created.

  The entered text and the "textual interconnection" symbol are displayed in the sheet bar to identify the textual interconnection: ![Procedure in "Data flow"](images/161359761291_DV_resource.Stream@PNG-de-DE.png)

**Edit**

1. Click the desired textual interconnection in the sheet bar.
2. Edit the text.
3. Exit your entry with the <Enter> key.

Result:

- If the entered text can be interpreted as a valid path, the textual interconnection is replaced by a real interconnection.
- If the entered text cannot be interpreted as a valid path to the interconnection source, the textual interconnection remains.

  The changed text is displayed in the sheet bar.

**Delete**

1. Click the desired textual interconnection in the sheet bar.

   Alternatively, click the interconnection line in the chart.
2. Press the <Del> key or select the "Delete" command from the shortcut menu.

**Closing an "open" textual interconnection**

When a referenced interconnection source is created after the textual interconnection has been created, this textual interconnection remains "open" until the user closes it manually.

Depending on the target system, you can also close an "open" textual interconnection in the "Chart sequence & extras" editor.

1. Click the desired textual interconnection in the sheet bar.
2. Select the menu command "Close textual interconnections" from the shortcut menu.

Result:

- If the entered text can be interpreted as a valid path, the textual interconnection is replaced by a real interconnection.
- If the entered text cannot be interpreted as a valid path, the textual interconnection remains and is displayed in the sheet bar.
- A message for the procedure is displayed in the Inspector window in the "Info > General" tab.

##### Procedure in "Control flow"

**Creating a textual interconnection**

1. Navigate in the table to the input parameter of a block at which you want to create the textual interconnection.
2. Click in the row of this input parameter in the table cell of the "Operand" column.
3. Select the command "Textual interconnection to chart..." from the shortcut menu.

   An input field is opened in the table cell.
4. Enter a text.

   A maximum of 1000 characters is permitted.

Result:

- If the entered text can be interpreted as a valid path to the interconnection source, a real interconnection is created.
- If the entered text cannot be interpreted as a valid path to the interconnection source, the textual interconnection is created in the table cell.

  As identification of the textual interconnection, a colored background is assigned to the entered text.

**Edit**

1. Click in the table on the table cell in the "Operand" column that belongs to the desired textual interconnection.
2. Edit the text.
3. Exit your entry with the <Enter> key.

Result:

- If the entered text can be interpreted as a valid path, the textual interconnection is replaced by a real interconnection.
- If the entered text cannot be interpreted as a valid path to the interconnection source, the textual interconnection remains.

  The changed text is displayed in the table cell.

**Delete**

1. Click the desired textual interconnection in the table.
2. Select "Delete interconnection" from the shortcut menu.

**Closing an "open" textual interconnection**

When a referenced interconnection source is created after the textual interconnection has been created, this textual interconnection remains "open" until the user closes it manually.

1. Click the desired textual interconnection in the table.
2. Select the menu command "Close textual interconnections" from the shortcut menu.

Result:

- If the entered text can be interpreted as a valid path, the textual interconnection is replaced by a real interconnection.
- If the entered text cannot be interpreted as a valid path, the textual interconnection remains.
- A message for the procedure is displayed in the Inspector window in the "Info > General" tab.

#### Textual interconnections in the "Chart sequence & extras" editor

All open textual interconnections are displayed in the "Textual interconnections" tab of the "Chart sequence & extras" editor in a table. This display depends on the target system.

Up to 600 interconnections are displayed below the associated CFC chart. If more than 600 textual interconnections were created, the entries for the most recently edited interconnections are displayed.

> **Note**
>
> **Configuration depending on the target system**
>
> You can use the "Chart sequence & extras" editor to check, close or delete open textual interconnections.
>
> The availability and the content of the tabs depend on the target system for which you are configuring.

##### Table columns

**"Chart/Textual interconnection" column**

The associated chart and the text of the textual interconnection are displayed for each textual interconnection.

**"Interconnected with" column**

The column contains the input parameter at which the textual interconnection is configured.

**"Status" column**

The status or a possible action is shown in a comment.

##### Functions

Various functions for textual interconnections are available through the toolbar and the shortcut menu:

**Hierarchy**

In the "Chart/Textual interconnection" column you can completely show or hide the hierarchy.

**List entries**

You can select or deselect all list entries.

**Deleting textual interconnections**

You can select multiple textual interconnections. All selected interconnections are deleted.

When all textual interconnections of a CFC were deleted, the CFC is removed from the table.

**Closing textual interconnections**

You can select textual interconnections as well as CFCs.

A comment is displayed in the "Status" column to help with the selection.

When you select a chart and start the "Close textual interconnections" function, all displayed "open" textual interconnections of this chart are closed. You do not need to select the textual interconnections additionally.

After the process has been completed, a message is displayed for each selected textual interconnection in the "Info > General" tab in the Inspector window.

When all "open" textual interconnections of a CFC are closed, the CFC is removed from the table.

**Jump to "Data flow" or "Control flow"**

When a textual interconnection is selected, you can use the symbols to jump to the "Data flow" or the "Control flow".

When several textual interconnections are selected, the first textual interconnection in the selection is displayed.

---

**See also**

"Chart sequence & extras" editor for S7

### Adapting the run sequence

This section contains information on the following topics:

- [Runtime model](#runtime-model)
- [Options for determining the run sequence](#options-for-determining-the-run-sequence)
- [Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)
- [Adapting the run sequence of CFC charts](#adapting-the-run-sequence-of-cfc-charts)
- [Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)

#### Runtime model

##### Overview

The runtime model describes the following functions:

- If and when CFC charts are to be executed
- When and in which sequence the blocks and instructions in the CFC charts are to be executed in the user program

> **Note**
>
> **Configuration depending on the target system**
>
> You can use the "Chart sequence & extras" editor to check and change the run sequence and task assignment.
>
> The availability and the content of the tabs depend on the target system for which you are configuring.

##### How the runtime model functions

**Task assignment of the CFC charts**

The runtime model is based on the assumption that the target system has one or more tasks.

- In the "Chart sequence & extras" editor you specify the task assignment for the chart folders of the target system.

  When you create a new CFC chart, this task is assigned to the chart as the main task.

  For S7 target systems, you select the main task of a CFC chart in the "Target system settings" tab.
- You can change the task assignment of the chart in the CFC chart properties.

**Run sequence within the CFC chart**

When you insert an instruction or block in the CFC chart, it is assigned to the main task.

However, you can specify the run sequence and the task assignment in the CFC chart individually for each instruction or block.

Additional information: "[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)"

**Run sequence of the CFC charts**

The chart sequence determines the order in which the various CFC charts of the target system is run.

Depending on the target system, you are able to determine the time of the execution of a CFC chart with additional functions, e.g. "Reduction ratio", "Phase offset".

Additional information: "[Options for determining the run sequence](#options-for-determining-the-run-sequence)"

**Optimization of the run sequence**

You can have the run sequence optimized automatically:

- Run sequence of the CFC charts
- Run sequence of the instructions or blocks within the CFC charts

Additional information: "[Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)"

##### Run sequence and task assignment

Instructions and blocks are always assigned to one or more tasks of the target system.

Because of this, the following rules apply:

- If a block or instruction is assigned to several tasks, this object is executed in every task.
- Within a task, the instructions/blocks assigned to it execute in the configured run sequence.

**Example for target system S7**

All blocks of the main task of the chart "task_1" are assigned in a CFC chart.

- An instruction "and_1" in this chart is assigned to another task "task_2".

  The instruction "and_1" is not executed in "task_1" of this CFC chart.
- An instruction "and_2" has been assigned "task_1" and an additional "task_2":

  The instruction "and_2" is executed in both tasks, "task_1" and "task_2".

---

**See also**

[Adapting the run sequence of CFC charts](#adapting-the-run-sequence-of-cfc-charts)
  
CFC tasks for S7
  
[Basic settings for CFC charts](#basic-settings-for-cfc-charts)

#### Options for determining the run sequence

##### Run sequence of instructions and blocks

The run sequence within the CFC chart is determined by the order in which you insert the instructions or blocks in the CFC chart.

You change the run sequence in the control flow.

> **Note**
>
> **Depending on the target system**
>
> The display of the options "Enable chart", "Optimize chart", reduction ratio and phase offset depends on the target system.
>
> This means these options may not always exist and be adjustable in the properties of a chart.

##### "Enable chart" option

CFC charts are enabled or disabled for execution with the "Enable chart" option.

**Configuration**

You set the option at the "EN" parameter:

- 1 = Chart is enabled
- 0 = Chart is not enabled

To interconnect the "EN" parameter, select the output parameter of a block or CFC chart in the "Enable chart" field.

| Editor | Selected object | Configuration | Interconnections |
| --- | --- | --- | --- |
| Chart sequence & extras > "Chart sequence" tab | - | "Enable chart" column | Create  Change  Delete |
| Data flow > Inspector window > "Properties" tab | CFC chart  (No object is selected.) | "S7 specific":  - "Enable chart" field | Create  Change  Delete |
| Subchart in a CFC chart | "Interface":  - "EN" parameter | Interconnected parameters cannot be edited. |  |
| "EN" parameter of a subchart | "General":  - "Value" field | Interconnected parameters cannot be edited. |  |
| Control flow | "EN" parameter of a subchart | "Operand" column | Change  Delete |

**Test mode**

The "Enable chart" option can be changed online.

When the option is interconnected with a parameter, it cannot be edited online.

##### "Optimize chart" option

You enable the setting "Optimize chart" in the chart properties.

When this setting is enabled the following options for optimizing the run sequence of this CFC chart are available:

| Editor | Button | Effect |
| --- | --- | --- |
| Chart sequence & extras:  - Chart sequence | Optimize run sequence according to the signal flow | Chart sequence and / or content of the CFC charts are optimized. |
| CFC chart:  - Data flow - Control flow | Optimize run sequence of the CFC chart according to the signal flow | The content of the CFC chart is optimized. |

When the "Optimize chart" field is disabled, the buttons in the editors have no function.

##### Reduction ratio

The reduction ratio specifies if the CFC chart is executed with each task call or only after a specified number of runs.

The reduction value R is always a power of 2:

- R = 2 <sup>t</sup>

  With 0 ≤ t ≤ 7

This means possible values are:

- 1, 2, 4, 8, 16, 32, 64, 128

Example for SIMATIC S7:

- Basic cycle of a cyclic interrupt:

  500 ms
- Possible cycles due to reduction ratio:

  500 ms, 1 s, 2 s, 8 s, 16 s, 32 s, 64 s

In hierarchical charts you can only use the reduction ratio in basic charts and not in subcharts.

##### Phase offset

Phase offset enables an even load distribution within the target system.

The phase offset always depends on the reduction ratio "R".

The charts are processed as frequently as configured with the reduction ratio "R" and are each shifted by "m" units of the task cycle.

- "m" is an integer

  With 0 ≤ m ≤ (R-1)

##### Example with reduction ratio and phase offset

Settings:

- Basic cycle of a cyclic interrupt: 500 ms
- Reduction ratio = 16

  (The chart is executed every 8 seconds.)
- Phase offset = 3

The chart is executed after 1.5 s; 9.5 s; 17.5 s, etc.

The default setting is "0".

##### Configuring

The configuration of the reduction ratio and the phase offset depends on the target system.

**Configuration for S7 target systems**

You configure the reduction ratio and the phase offset in the chart properties under "General > S7 specific > Sequence".

You check and configure other settings for the run sequence in the "Chart sequence & extras" editor, for example, the task assignment or the run sequence of the charts.

The Editor gives you an overview of the settings of all CFC charts.

---

**See also**

[Runtime model](#runtime-model)
  
[Representation of instructions and blocks](#representation-of-instructions-and-blocks)

#### Adapting the run sequence within the CFC chart

When you insert an instruction or a block in the CFC chart, the instruction or block is assigned to the task of the CFC chart.

The run sequence of the instructions and blocks is decided by the order in which you have inserted them in the CFC chart.

You change the run sequence in the control flow.

##### Optimizing the run sequence

You can also have the run sequence optimized automatically in the CFC chart.

You start this function using the toolbar in the control flow or data flow.

Additional information: "[Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)"

##### Requirement

- The CFC chart is open.
- "Control flow" is displayed.
- Instructions/blocks have been configured.

##### Procedure in the control flow

**Adapting the run sequence manually**

1. Drag the required instruction or block to the new position in the table.

**Adapting the run sequence automatically**

1. Enable the "Optimize chart" property for the chart.
2. In the toolbar, click on "Optimize run sequence of the CFC chart according to the signal flow":![Procedure in the control flow](images/130610409739_DV_resource.Stream@PNG-de-DE.png)

##### Alternative procedure: Data flow

**Adapting the run sequence manually**

You can specify the run sequence in a CFC chart while adding additional instructions/blocks:

1. In the data flow, select an inserted instruction or an added block.
2. In the shortcut menu of the instruction or block, select the entry "Use as predecessor in the run sequence".

The next instruction or block is added in the run sequence after this object.

**Adapting the run sequence automatically**

1. Enable the "Optimize chart" property for the chart.
2. In the toolbar, click on "Optimize run sequence of the CFC chart according to the signal flow":![Alternative procedure: Data flow](images/130610409739_DV_resource.Stream@PNG-de-DE.png)

##### Result

The run sequence is adapted.

---

**See also**

[Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)
  
[Runtime model](#runtime-model)

#### Adapting the run sequence of CFC charts

##### Requirement

- Two or more CFCs have been created for a controller.
- The CFCs have interconnections between charts.
- The "Chart sequence & extras" Editor is open.
- "Chart sequence" is displayed.

##### Procedure

1. Select a CFC.
2. Move the CFC to the new location by dragging it with the mouse.

##### Result

The run sequence is adapted.

---

**See also**

[Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)
  
[Runtime model](#runtime-model)

#### Optimizing the run sequence of CFC charts automatically

##### Overview

To keep the dead times in the user program of a target system low, use the automatic optimization of the run sequence.

The automatic optimization of the run sequence is based on the fact that the objects executed first are those whose output values are used as input values for other objects.

You can, however, also exclude CFC charts explicitly from the automatic optimization.

Additional information: "[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)"

##### Optimization options

You start the automatic optimization in the toolbar of the "Chart sequence & extras" editor.

In the "Optimize run sequence" dialog, you select the scope of the optimization:

| Option | Response |
| --- | --- |
| Chart sequence and contents of all charts | Optimizes the run sequence of the charts as well as the instructions and blocks within the charts. |
| Chart sequence | Optimizes only the run sequence of the charts. |
| Contents of all selected charts | Optimizes only the run sequence of the instructions and blocks within the selected charts. |

**Include/exclude chart content**

To enable the automatic optimization within a chart, enable the "Optimize chart" property for the CFC chart.

If the setting is disabled at a chart, the following applies to this chart:

- The content of this chart is not optimized.
- The chart is taken into account during the optimization of the chart sequence.

##### Requirement

- Cross-chart interconnections or interconnections in the CFC charts are configured.
- The "Chart sequence & extras" editor is open.
- The "Chart sequence" is displayed.

##### Procedure

1. Select the CFC charts whose run sequence you want to optimize automatically.
2. In the toolbar, click on "Optimize run sequence of the CFC chart according to the signal flow": ![Procedure](images/130610887435_DV_resource.Stream@PNG-de-DE.png)

   The "Optimize run sequence" dialog opens.
3. Select the required option in the dialog.
4. Click "OK".

   The selected optimization of the run sequence is started.

##### Result

Depending on your selection, the run sequence of instructions and blocks within the CFC charts and/or the chart sequence are optimized automatically.

---

**See also**

[Adapting the run sequence within the CFC chart](#adapting-the-run-sequence-within-the-cfc-chart)
  
[Adapting the run sequence of CFC charts](#adapting-the-run-sequence-of-cfc-charts)
  
[Runtime model](#runtime-model)

### Testing the CFC chart

This section contains information on the following topics:

- [Selecting parameters for testing](#selecting-parameters-for-testing)
- [Testing a CFC chart](#testing-a-cfc-chart)
- [Effects of test mode on object properties](#effects-of-test-mode-on-object-properties)
- [Testing with the "Forcing" function](#testing-with-the-forcing-function)
- [Setting parameters to defined values for testing ("Forcing" function)](#setting-parameters-to-defined-values-for-testing-forcing-function)
- [Setting several parameters to defined values with the "Forcing" function](#setting-several-parameters-to-defined-values-with-the-forcing-function)

#### Selecting parameters for testing

After configuration of the instructions and blocks in the CFCs, you can test the function of the CFCs.

Values from the device are displayed at the input and output parameters for this.

##### Basic procedure

Configuration takes place in the following steps:

1. Start by selecting the input and output parameters for the test.
2. Then you start the actual test in which values from the device are displayed at the input and output parameters.

Additional information: "[Testing the CFC](#testing-a-cfc-chart)"

> **Note**
>
> **Value display depending on the interconnection**
>
> Input parameters of instructions and, for example, of "FC" functions in S7 can only display values from the device if they are interconnected.
>
> Although they can be selected in the table of parameters for testing, no values are displayed for existing online connections.
>
> **Test settings**
>
> Various test settings are available depending on the target system you are using.
>
> In test mode, you have the option to register or unregister parameters for testing.
>
> Additional information: "[Testing the CFC](#testing-a-cfc-chart)"

##### Deregister input and output parameters from testing

To deregister an input or output parameter from the test, disable the option "For test".

##### Requirement

- The CFC is open.
- Instructions/blocks have been configured.
- "Data flow" is shown in the work area.

##### Procedure

1. Select the required instruction or block.
2. Enable under "Parameters" in the Inspector window for the required input and output parameters the "For test" option.
3. If you want to select all input and output parameters for testing, select the "Activate all" command in the shortcut menu of the header.
4. If you want to test several instructions/blocks of the CFC, repeat steps 1 to 3.
5. If necessary, configure the settings of the update times in the "Testing" task card for the visible area of the CFC and the selected parameter or the interconnection.

##### Result

The required input and output parameters have been selected for testing.

---

**See also**

[Setting the parameters of the input and output parameters](#setting-the-parameters-of-the-input-and-output-parameters)
  
["CFC" Editor](#cfc-editor)

#### Testing a CFC chart

##### Overview

After configuration of the instructions and blocks in the CFC charts, you can test the function of the CFC charts.

Values from the device are displayed at the input and output parameters for this.

> **Note**
>
> **Procedure depending on the target system**
>
> The following section explains the procedure without covering properties of the specific target system.
>
> Additional information is available in the target system documentation e.g. for the S7 target system under:
>
> - "Working with CFC charts for S7"

##### Basic procedure

You always need to perform the following steps to test CFC charts:

1. Start by selecting the input and output parameters for the test.

   Additional information: "[Selecting parameters for testing](#selecting-parameters-for-testing)"
2. Then you start the actual test in which values from the device are displayed at the input and output parameters.

##### Conditions for the test

The following conditions apply to the test:

**Displaying the latest values**

The input and output parameters only receive the latest values for testing at the following conditions:

- The parameters have been selected for the test.
- The parameters are available in the visible part of the CFC chart within the work area.
- Data memory is assigned to the parameters.

  No values are displayed at parameters without data memory.
- The input parameters are connected to a source.

  In the table of parameters, all parameters can be selected for testing, including parameters that are not connected.

**Comparison status of the block parameters**

The values of the input and output parameters are highlighted in color:

![Conditions for the test](images/143859203723_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Yellow | The display of the parameters is uninterrupted.  The CFC charts and blocks are identical in the project and on the device.  The usual editing functions can be performed. For S7 target systems, for example, you can change unconnected input parameters. |
| Red | The status in the project and on the device does not match.  The chart has been changed, for example, but not yet downloaded to the device.  Editing functions are restricted. For example, you cannot change any parameters in the CFC chart for S7 target systems. |

**Testing structures**

If you select a parameter of the STRUCT data type for testing, the value of the first structure element of the configured structure is displayed.

##### Requirement

- The online connection to the device can be established.
- Rules for the device containing the CFC charts to be tested:

  - The corresponding software must be compiled and loaded.
  - To display value changes, the CPU of the device must be in "RUN" mode.
- The required CFC chart is configured and open.
- "Data flow" is shown in the work area.

##### Procedure

1. Click in the CFC chart, or select an instruction, or a block.
2. Click "Go online" in the toolbar.

   Once you are online, all input and output parameters selected for testing are provided with the current values from the device and are highlighted in color.

   To monitor the values, click the "Monitor on/off" icon in the CFC editor: ![Procedure](images/144083943435_DV_resource.Stream@PNG-de-DE.png)
3. If necessary, you can register or deregister a selected input or output parameter in the "Testing" task card for testing.

   You do not have to open the Inspector window for this purpose.
4. If necessary, select additional parameters for testing or remove previously tested parameters in the Inspector window under "Parameters".
5. Depending on the target system, the "Testing" task card may contain additional settings that may be relevant to the test.

   Example S7 system: Update time of the visible area of the CFC chart.

##### Alternative procedure

You can also use the following options in the "Data flow" online mode to show values from the device:

**Value as tooltip**

If you point to the input or output parameter with the mouse pointer, then the latest value from the device is shown as tooltip.

Use the shortcut menu command "For test" to display the value.

**Value with the STRUCT data type**

The structure with all structure elements appears as a tooltip when you move the mouse pointer over a parameter of STRUCT data type.

**Display value permanently**

If you have not selected the input or output parameter for testing, then you can keep the <Ctrl> key pressed and click on an input or output parameter or an interconnection with the mouse pointer.

The parameter is permanently selected for the test and the latest value from the device is displayed.

Repeat this step to revert this function and no longer display the value.

##### Result

All input and output parameters in the visible work area that have been selected for testing are supplied with the latest values from the device.

This enables you to test the function of the instructions and blocks.

#### Effects of test mode on object properties

There are different special considerations in test mode that have an effect on specific functions or editing options.

##### Properties of CFCs

**"Enable chart" option**

The "Enable chart" option can only be changed when online test mode is running.

When the option is interconnected with a parameter, it cannot be edited online.

You set the option at the "EN" parameter.

##### Properties of blocks and instructions

**Interconnection**

You cannot change an interconnection online which means it is blocked from changes in test mode.

Any changes to an interconnection will have to be made offline and transferred by compilation and downloading to the device.

**Changes in parameter assignment**

In test mode, changes to the parameter assignment of input/output parameters of blocks and instructions are transferred directly to the device and into the project.

Such changes do not require a new download.

##### Representing interconnections

The connection lines of interconnections of data type BOOL are visualized in online mode based on their current values.

- Value = "1": Green line
- Value = "0": Dashed blue line

The example in the following figure shows an interconnection of data type BOOL in online mode.

![Representing interconnections](images/40979944075_DV_resource.Stream@PNG-de-DE.png)

##### Additional information

Notes on special considerations in test mode are included in the description of the respective target system.

---

**See also**

[Optimizing the run sequence of CFC charts automatically](#optimizing-the-run-sequence-of-cfc-charts-automatically)
  
[Options for determining the run sequence](#options-for-determining-the-run-sequence)

#### Testing with the "Forcing" function

##### Overview

Individual parameters of a block can be set to a defined value for testing with the "Forcing" function.

The so-called force table includes all parameters for which the "Add forcing" option is selected.

The force table also provides an overview of all these parameters.

The use of the force table makes sense if you want to test several parameters with the "Forcing" function and if these are located in different charts, for example.

**Supported parameters and data types**

- The "Forcing" function only supports parameters of the type "IN" or "INOUT".
- Parameters in the interface of a CFC are not supported.
- The table "Data types" contains the list of the data types that are supported or not supported.

##### Configuration and use

In offline mode, configure the function "Add forcing".

You can enable the function "Forcing active" in online or offline mode and enter the desired values.

However, the effects of the force value in the program are only visible in online mode.

Configuration consists of the following steps:

1. "Add forcing" at the parameter of a block
2. Enable forcing and enter the test value

##### 1. "Add forcing" at the parameter of a block

**Configuration**

- Enable the option at the parameter of a block in "Data flow" or "Control flow" of an open chart.

**Effects**

- The "Forcing active" and "Force value" columns of an interconnected parameter can be edited.

  If the parameter has not been interconnected, the "Forcing active" option and the "Force value" input field remain grayed out.
- The status "Add forcing" is indicated by a corresponding status display at the associated parameter in the "Data flow".
- The parameter registered for forcing is also displayed in the so-called force table.

##### 2. Enable forcing and enter the test value

Enable the "Forcing" function for the desired parameter and enter the respective test value.

**Configuration at the block parameter in "Data flow" or "Control flow"**

- Enable the option "Forcing active" for an interconnected parameter and enter the required force value in the input box.
- For a parameter that is not interconnected, you can enter the required value as a parameter value in the "Value" input box in the "Instance data" area.

Effects:

- The status "Forcing active" is indicated by a corresponding status display at the associated parameter in the "Data flow".
- The "Forcing active" status and the force value appear simultaneously in the row of the force table belonging to the parameter.

**Configuration in the force table**

- Enable the "Forcing active" option in the associated table row of an interconnected parameter.

  Enter the desired force value in the "Force value" column.
- For a parameter that is not interconnected, the table lines associated with the parameter for "Forcing active" and "Force value" are deactivated.

  In this case, select the required parameter in the table.

  The configuration data are displayed in the "Instance data" area in the Inspector window.

  Enter the required value as a parameter value in the "Value" input box in the "Instance data" area.

Effects:

- The entered force value is also displayed at the associated parameter in "Data flow" or "Control flow".
- The status "Forcing active" is indicated by a corresponding status display at the associated parameter.

##### Status displays for "Forcing" function in "Data flow"

The status displays are shown at the associated block parameter in "Data flow":

- The "Add forcing" option has been enabled: the associated parameter is identified by a brown rectangle.
- The "Add forcing" and "Forcing active" options have both been enabled: the associated parameter is identified by a blue rectangle.

**Example**

In this example, the following status displays are shown at a block in "Data flow":

- 1st input parameter:

  The "Add forcing" option has been enabled. The "Forcing active" option has been disabled.
- 2nd input parameter:

  The "Add forcing" and "Forcing active" options have both been enabled.

| Symbol | Meaning |
| --- | --- |
| ![Status displays for "Forcing" function in "Data flow"](images/161263827723_DV_resource.Stream@PNG-de-DE.png) | Offline display |
| ![Status displays for "Forcing" function in "Data flow"](images/161263836171_DV_resource.Stream@PNG-de-DE.png) | Online display |

##### Data types

The following tables show the supported and unsupported data types.

| Data type category | Unsupported data types |
| --- | --- |
| Parameter types | TIMER  COUNTER  BLOCK_DB  BLOCK_FB  BLOCK_FC |
| Pointer | POINTER  ANY  VARIANT |
| Data structures | ARRAY |

| Data type category | Supported data types |
| --- | --- |
| Binary numbers | BOOL  BYTE  WORD  LWORD  DWORD |
| Integers | SINT  USINT  INT  DINT  UDINT  LINT  ULINT |
| Floating-point numbers | REAL  LREAL |
| Times | S5TIME  TIME  LTIME |
| Date and time | DATE  TOD  LTOD  DT  LDT  DTL |
| Strings | CHAR  WCHAR  STRING  STRING[N] |
| Data structures | STRUCT  The data types listed above are supported in each level of the structure for the STRUCT data type. |

---

**See also**

[Setting parameters to defined values for testing ("Forcing" function)](#setting-parameters-to-defined-values-for-testing-forcing-function)
  
[Setting several parameters to defined values with the "Forcing" function](#setting-several-parameters-to-defined-values-with-the-forcing-function)

#### Setting parameters to defined values for testing ("Forcing" function)

##### Overview

Parameters of a block can be set to a defined value for testing with the "Forcing" function.

If you want to test several parameters with the "Forcing" function that are, for example, located in different charts, use of the so-called force table is recommended.

**Additional information**

- Supported data types:

  "[Testing with the "Forcing" function](#testing-with-the-forcing-function)"
- "[Setting several parameters to defined values with the "Forcing" function](#setting-several-parameters-to-defined-values-with-the-forcing-function)"

##### Basic procedure

Configuration basically takes place in two stages in "Data flow" or "Control flow":

1. "Add forcing" at the parameter of a block
2. Select the "Forcing" function for this parameter and enter the required force value of the parameter.

In offline mode, configure the function "Add forcing".

You can enable the function "Forcing active" in online or offline mode and enter the desired values.

However, the effects of the force value in the program are only visible in online mode.

##### Requirements

- The online connection to the device has been established once before.
- Rules for the device containing the CFCs to be tested:

  - The corresponding software must be compiled and loaded.
  - The CPU of this device must be in "RUN" operating mode.
- The required CFC is configured and open.
- "Data flow" or "Control flow" is shown in the work area.

  The following section explains the procedure in "Data flow".

##### Procedure

1. Select the required parameter of an instruction or block.

   The "General" tab is displayed in the Inspector window.
2. Select the "Add forcing" option in the "Instance data" area under "General" in the Inspector window.

   In "Data flow", a green rectangle at the associated parameter indicates that the parameter is registered for "Forcing".

   The parameter is also displayed in the so-called force table under "Charts - Trend/dynamic display & force table".
3. Further configuration depends on whether or not the parameter is interconnected.

   - If the parameter is interconnected, the check box "Forcing active" and the input box "Force value" are shown.

     Select the "Forcing active" check box and enter the required force value in the "Force value" input box.
   - If the parameter is not interconnected, the check box "Forcing active" and the input box "Force value" are not shown.
4. To test the effects of the force value in the CFC, click "Go online" in the toolbar.
5. All force values are transferred to the device once you are connected online.

   All input and output parameters in the visible work area that have been selected for testing are supplied and displayed with the latest values from the device.

   You can change the force values in online mode.

   When you change force values offline, these values will not become effective until after they were downloaded to the PLC.

##### Result

The parameter of an instruction or a block is registered for "Forcing".

The "Forcing" function is selected for this parameter and a force value is configured.

The effect of the force value can be tested in the chart with an existing online connection.

#### Setting several parameters to defined values with the "Forcing" function

##### The "Forcing" function

Parameters of a block can be set to a defined value for testing with the "Forcing" function.

The following section explains how to use the so-called force table with which you use the "Forcing" function for several block parameters.

The use of the force table makes sense if you want to test several parameters with the "Forcing" function and if these are located in different charts, for example.

**Additional information**

- Supported data types:

  "[Testing with the "Forcing" function](#testing-with-the-forcing-function)"
- "[Setting parameters to defined values for testing ("Forcing" function)](#setting-parameters-to-defined-values-for-testing-forcing-function)"

##### Basic procedure

Configuration basically takes place in two stages:

1. "Add forcing" at a block parameter in "Data flow" or "Control flow":
2. Select the "Forcing" function for this interconnected parameter and enter the required force value of the parameter.

   The following paragraph describes the method for working with the force table.

   You can also make this configuration for individual parameters in the "Data flow" or "Control flow" of a chart.

In offline mode, configure the function "Add forcing".

You can enable the function "Forcing active" in online or offline mode and enter the desired values.

However, the effects of the force value in the program are only visible in online mode.

##### Requirements

- The online connection to the device has been established once before.
- Rules for the device containing the CFCs to be tested:

  - The corresponding software must be compiled and loaded.
  - The CPU of this device must be in "RUN" operating mode.

##### Procedure

1. To use the parameters of instructions or blocks in the force table for testing, you first have to select the "Add forcing" option at the required individual parameters.

   If you have already made this configuration, you can continue with step 5.

   Open the CFC of a required parameter in "Data flow" or "Control flow" that is to be available for testing in the force table.
2. Select the required parameter of an instruction or block.

   The "Forcing" function only supports parameters of the type "IN" or "INOUT".

   The "General" tab is displayed in the Inspector window.
3. Select the "Add forcing" option in the "Instance data" area under "General" in the Inspector window.

   In "Data flow", a green rectangle at the associated parameter indicates that the parameter is registered for "Forcing".

   The parameter is also displayed in the so-called force table under "Charts - Trend/dynamic display & force table".
4. Repeat steps 1 - 3 for each parameter that is to be available for testing in the force table.
5. Download the program to the device.
6. Click "Go online" in the toolbar.
7. Open the force table.

   Double-click the "Force table" entry in the "Charts - Trend/dynamic display & force table" folder of the project tree.

   The force table is opened in the work area.

   - You can turn the sorting of the table on/off or change it by clicking the respective table column.
   - You can manipulate the display and width of the table columns with the shortcut menu of a column header.
   - The "Tag" column displays all parameters with the "<Chart>\<Block_name>.<Parameter_name>" path for which the "Add forcing" option is selected.
   - Double-click the path in the "Tag name" column to open the associated CFC and select the configured parameter.
   - When you select a table line, the "General" tab with the configuration data of this parameter is displayed in the Inspector window.
   - If you clear the "Add forcing" option for a parameter, this parameter is removed from the table.
8. Further configuration depends on whether or not the parameter is interconnected.

   - If the parameter is interconnected, the "Forcing active" option and the input box in the "Force value" column can be configured in the table.

     Select the "Forcing active" option for the required parameters and enter the required force value in the table column of the same name.
   - If the parameter is not interconnected, the "Forcing active" option and the "Force value" input box cannot be configured in the table.
9. All force values are transferred to the device because you are already in online mode.
10. To check the effects of the force value of a parameter, open the associated chart with a double-click on the path in the "Tag name" column.

    All input and output parameters in the visible work area that have been selected for testing are supplied and displayed with the latest values from the device.

##### Result

Several parameters of instructions or blocks are registered for "Forcing" and are displayed in the force table.

The "Forcing" function is selected for these parameters and a force value is configured, if necessary.

The effect of the force value can be tested in the chart with an existing online connection.

## Configuring and using the trend and dynamic displays

This section contains information on the following topics:

- [Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)
- [Trend display - Functions and operating options](#trend-display---functions-and-operating-options)
- [Creating a trend display](#creating-a-trend-display)
- [Using the trend display](#using-the-trend-display)
- [Creating a dynamic display](#creating-a-dynamic-display)
- [Using the dynamic display](#using-the-dynamic-display)

### Overview of the trend and dynamic displays

The following options are available for monitoring multiple static and online values:

- Trend display

  This allows you to visualize multiple values in a trend chart.
- Dynamic display

  This allows several values to be displayed in the form of a watch table.

The compilations of selected tags/parameters are stored for reuse.

#### General properties

- The trend and dynamic displays are stored and managed in the project tree, in the "Charts - Trend/dynamic display & force table" folder.

  The objects can be copied to or deleted from this folder.
- You can create several trend and dynamic displays for each target system.

#### Overview of the trend display

The trend display configured in the editor window consists of the following objects:

- Definition table
- Trend window with operator controls and trend chart

**Parameters in the trend display**

The parameters to be monitored can be added to the trend display as follows:

- Using drag-and-drop with trend display opened in the editor window, or using copy/paste to the definition table.

  The parameter you inserted can be assigned directly to an axis.
- If the trend display is not open, you can drag-and-drop the parameter to the trend display in the project tree.

  In this case, the parameter is assigned automatically to an appropriate axis (digital/analog).

  If it does not yet exist, the axis is generated automatically.

The values are assigned to digital and analog axes and displayed.

A trend display can contain several digital and analog axes.

**Exporting values**

The values of the trend chart can be exported or imported in CSV format.

**Printing the trend display**

You start the print in the project navigation via the shortcut menu or from the opened trend display.

Alternatively, you can open the "Print" dialog in the definition table with the key combination <Ctrl+P>.

- Print the axis and curve definition table in the project navigation or in the definition table.
- In the open trend display, print the trend chart using the "Print" button.

**STEP 7 traces**

Alternatively, you can also display the parameters of the CFC blocks in STEP 7 traces.

During trace configuration, the block parameters are listed in the "Signals" table in the selection dialog.

Additional information in the TIA Portal Information System:

- "Using online and diagnostics functions > [Using the trace and logic analyzer function](Using%20the%20trace%20and%20logic%20analyzer%20function.md#recording-of-measured-values-with-the-trace-function)"

**Additional information**

- "[Creating a trend display](#creating-a-trend-display)"
- "[Using the trend display](#using-the-trend-display)"
- "[Trend display - Functions and operating options](#trend-display---functions-and-operating-options)"

#### Overview of the dynamic display

**Parameters in the dynamic display**

The parameters to be monitored can be added to the dynamic display as follows:

Using drag-and-drop with dynamic display opened in the editor window, or using copy/paste to the definition table.

If the dynamic display is not open, you can drag-and-drop the parameter to the corresponding dynamic display in the project tree.

**Printing the dynamic display**

You start printing in the project navigation via the shortcut menu.

Alternatively, you can open the "Print" dialog in the open dynamic display with the <Ctrl+P> key combination.

- In offline mode, the offline values are printed.
- In online mode, the corresponding online values are printed.

**Additional information**

- "[Creating a dynamic display](#creating-a-dynamic-display)"
- "[Using the dynamic display](#using-the-dynamic-display)"

### Trend display - Functions and operating options

#### Layout and operating options

The trend display consists of the following objects:

- Definition table
- Trend window with operator controls and trend chart

The trend window provides various functions for operating and controlling visualization in the trend chart.

The tables below contain the following descriptions:

- Toolbar functions
- Trend window elements and operating options
- User actions for rapid working

#### Overview of the trend view layout

The following figure provides an overview of the elements.

![Overview of the trend view layout](images/45405018763_DV_resource.Stream@PNG-en-US.png)

#### Toolbar functions

The toolbar provides the following functions.

| Element | Function  (icon / selection box) | Description |
| --- | --- | --- |
| (1) | Zoom  (icons) | The zoom icons can be used to zoom the horizontal and vertical axes separately.  The toolbar provide a zoom in and a zoom out icon. |
| (2) | Display mode  (selection box) | The display mode for the x time axis of the trend chart can be set up using the selection box of the toolbar.  The following display modes are available:  - "Static" option (static time range display)   The time interval is not refreshed. You can set any range. This mode can be used to visualize all logged values in detail.   It is recommended to use this display mode for static values. - "Strip" option (dynamic display)   The time axis always displays the current time at the far right. The duration of the time interval can be changed. - "Scope" option (jumping time range display)   The time axis displays a fixed time interval. Once the trend values reach the right edge, the display changes so that the current time is shown at the left edge. - "Sweep" option (sweep mode display)   Similar to "Scope". However, the values of the "last sweep" continue to be displayed until they are overwritten by the current values. |
| (3) | Trend manager  ("Select trend:" selection field) | The trend manager visualizes the trend to axis assignments.   You can hide trends by disabling the corresponding check box. Hidden trends are no longer recorded in the trend chart, but still displayed in the legend in grayed out mode.  Select trends to be edited in the trend manager.  In addition to a color code, the trends in the trend chart are also provided with a marker to enable their quick identification in the legend and trend manager. |
| (4) | Import/export  (icons) | The trends can be exported or imported in CSV format.  The export icon is enabled once you have selected a trend in the trend manager (3).  Imported trends are visualized on separate x and y axes. You can improve the comparison of an imported trend with a trend from active logging by linking the x axis of the imported trend with the existing axis. |
| (5) | Customizing the user interface  ("View" menu) | This menu can be used to show and hide display elements such as the legends, rulers, or markers. |
| (6) | Linking x axes  ("Link axes" selection field) | When a trend is imported, the new x axis (axis "B") can be linked to the existing x axis (axis "A"). In linked mode, axis "B" moves simultaneously with axis "A", but can be adjusted without interfering with axis "A". This mode allows you to compare history trends with the current trend. |
| (7) | Printing   ("Print" icon) | The print dialog can be used to print the currently displayed trends of the trend chart. The printout can include a comment. |

#### Trend view elements and operating options

The following operator controls are provided in the trend view.

| Element | Function  (icon / selection box) | Description |
| --- | --- | --- |
| (8) | Maximum value | Field for displaying the maximum value of an analog axis.   Access for editing depends on the state of the associated write protection (9).  - "Write protection disabled" state (open padlock icon):   You can edit the value in the corresponding column of the definition table, or directly in this field. Changes to the cell in the definition table are transferred to the field of the y axis.   However, changes to the field of the y axis are **not** transferred to the corresponding cell in the definition table! - "Write protection enabled" state (closed padlock icon):   The value cannot be edited in the corresponding column of the definition table or in the y axis field.   You can restore the configured minimum/maximum with double-click on the y axis. |
| (9) | Lock text box | Using this icon, you can enable write protection for the input field next to the icon (closed padlock icon), or disable it (open padlock icon). |
| (10) | Y axis (here: analog axis) | The y axis is labeled with the axis name and the configured physical unit.   In the figure above, axis position "right" was configured for the analog y axis. |
| (11) | Minimum value | Field for displaying the minimum value of an analog axis.   Access for editing depends on the state of the write protection (9).  - "Write protection disabled" state (open padlock icon):   You can edit the value in the corresponding column of the definition table, or directly in this field. Changes to the cell in the definition table are transferred to the field of the y axis.   However, changes to the field of the y axis are **not** transferred to the corresponding cell in the definition table! - "Write protection enabled" state (closed padlock icon):   The value cannot be edited in the corresponding column of the definition table or in the y axis field.   You can restore the configured minimum/maximum with double-click on the y axis. |
| (12) | Time (right edge of the visualized trend range) | The field displays the time for right edge of the x axis.   Write access depends on:   - The state of the associated write protection (9) - The selected display mode (2)   You can use the selection function to open a calendar and select a different day. |
| (13) | Time range of the x-axis | The time range of the x axis is set in the definition table. |
| (14) | Time (left edge of the visualized trend range) | The field displays the time for the left edge of the x axis.   Write access depends on:   - The state of the associated write protection (9) - The selected display mode (2)   You can use the selection function to open a calendar and select a different day. |
| (15) | Digital trend names | The names of the digital trends (25) are displayed outside of the trend chart. The position depends on the configured position of the digital axis (16). |
| (16) | Y axis (here: digital axis) | The y axis is labeled with the axis names.   In the figure above, axis position "left" was configured for the digital y axis. |
| (20) | Legend (analog trends) | The legend displays the markers and names of the visualized analog trends.   The corresponding values are displayed to the right of the trend name:   - If there is no ruler, the last values added to the trend are displayed. - If at least one ruler is displayed, the associated values are displayed to the right of the trend name at the **active** ruler. |
| (21) | Analog trends | Analog trends are visualized in the upper area of the trend window.   The names of the analog trends (F) are displayed in the legend of the trend chart.   A tooltip is displayed for each visualized trend whenever you position the mouse pointer on the trend line. The tooltip first displays the trend name; click this name to display the configured data source. |
| (22) | Markers | Markers help you to distinguish between several trends.   You can enable the display of markers in the "View" menu. |
| (23) | Interpolated trend value | A value **without underscore** on the ruler indicates that this is an interpolated value.   A defined online value is not available for this trend point. |
| (24) | Defined trend value | An **underscored** value on the ruler indicates that this is a defined online value. |
| (25) | Digital trends | Digital trends are visualized in the lower area of the trend window.   The names of the digital trends (15) are displayed outside of the trend chart. The position depends on the configured position of the digital axis (16).   A tooltip is displayed for each visualized trend whenever you position the mouse pointer on the trend line. The tooltip first displays the trend name; click this name to display the configured data source. |
| (26) | Ruler | A ruler displays the value of each trend at the ruler/trend intersections.  Every ruler displays the associated time stamp with data and time.  A trend chart may have several rulers.  The **active** ruler is indicated by a yellow marker at its top end. The values at the active rulers are displayed in the legend (A) to the right of the trend name.  Adding rulers:  - You can drag-and-drop a new ruler from its docking position on the left edge of the trend chart to a specific position in the trend chart.   Copying rulers:  - Press <CTRL> and click the ruler to paste a copy thereof.   Deleting rulers:  - Drag the ruler to the left edge of the trend chart. - Press <ALT> and click the ruler to be deleted. |
| (27) | Ratio display / scroll bar (y axis) | This function depends on the selected display mode (2) and only affects analog trends.  - Scroll bar function + ratio display in "Static" display mode. - Ratio display in all other display modes.    **Ratio display:**   The scroll bar displays the approximate ratio between the configured and currently displayed range of values of the y axis in the trend chart.    **Scroll bar:**    The scroll bar can be used to shift the visible range of a trend in the trend chart if the displayed range of the y axis was modified in **vertical** direction, for example, by means of the zoom icons (1). |
| (28) | Ratio display/scroll bar (x axis) | This function depends on the selected display mode (2) and only affects analog trends.  - Scroll bar function + ratio display in "Static" display mode. - Ratio display in all other display modes.    **Ratio display:**   The scroll bar displays the approximate ratio between the configured and currently displayed range of values of the y axis in the trend chart.   **Scroll bar:**   The scroll bar can be used to shift the visible range of a trend in the trend chart if the displayed time range of the x axis was modified in **horizontal** direction, for example, by means of the zoom icons (1). |

#### User actions for rapid working

Various toolbar functions and mouse actions are available to accelerate your work.

| Action | Function | Description |
| --- | --- | --- |
| Zooming windows with pressed left mouse button | Zoom function with window | You can define the display range of the trend chart by dragging the window while pressing the left mouse button.   All axis value ranges for which write protection is not enabled by means of the lock icon are adapted when you release the mouse button. |
| Double-click on the chart area | Adapting trends | Double-click on the chart area of the trend chart sets the analog range of values of the y axes for analog trends so that the trends are completely visible in the current time range. |
| <Alt> + double-click on the chart area | Arranging trends | <Alt> + double-click in the chart area of the trend chart adapts the range of values of the y axes for analog trends so that the trends are arranged vertically. |
| Dragging the scale with pressed left mouse button | Editing the range of values of the axes | To change the range of values of an axis, click the axis and then drag the scale to the new value while keeping the left mouse button pressed.  - The arrows at the mouse pointer indicate the possible direction of change.   - If the arrows point in both directions you can edit both values.   - You can only edit one value if only one arrow is displayed, for example, in the direction of the minimum value. - Only the axis value ranges for which write protection is not enabled by means of lock icon are adapted.   Example:  If write protection of the minimum and maximum values of the y axis is not enabled, both values change simultaneously when you drag the scale while keeping the left mouse button pressed. The current **difference** between both values **remains unchanged**!  Double-clicking on the axis resets the range of values to the configured values. |
| Double-click on the axis | Resetting the range of values | Double-clicking on the axis resets the range of values to the configured values. |
| Space bar plus drag-and-drop of an axis | Moving axes | The position of the y axes is specified in the definition table of the trend display.  However, you can change the position of the x and y axes in online mode by pressing the space bar and moving the selected axis to the new position using drag-and-drop.  This method can be used, for example, to move the x axis towards the top. |

---

**See also**

[Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)

### Creating a trend display

A trend display allows you to visualize multiple online values in a trend chart.

This section describes how to create and configure a new trend display.

#### Requirements

- The parameters whose online values are to be displayed in the trend display must be configured.
- The CFC charts and blocks must be compiled.

#### Procedure

1. Double-click the "Add new trend display" entry in the "Charts - Trend/dynamic display & force table" folder of the project tree.

   - A new trend display is added to the folder and opened in the editor.
   - In the editor window, the table for the axis definition and the window for the trend chart are displayed.

   Work in the definition table of the trend display to configure parameters whose online values are to be displayed in the trend chart.
2. To change the name of the trend display, select the "Rename" entry in the shortcut menu in the project tree.
3. Open a CFC chart in a second editor window.

   Navigate to the desired parameter in the CFC chart or in the chart interface.
4. Drag-and-drop the parameter from the chart into the "y axis/trend" column.

   Alternatively, use Copy and Paste from the shortcut menu or the <Ctrl+C> and <Ctrl+V> keyboard shortcuts.

   The inserted parameter is displayed in a new row of the table:

   - The name of the "y axis/trend" column is set by default and cannot be changed.
   - The trend name is displayed in the legend in the trend window.
   - Since the trend display is newly created, no axes have been defined yet.

     Depending on the data type of the inserted parameter, an analog or digital axis is automatically inserted in the "y axis/trend" column.
5. Configure the properties for the trend representation in the line of the inserted parameter:

   - Trend name
   - Trend color
   - Emphasis (line thickness)
   - Value representation (line or points)
   - Sampling time

   You can show and hide columns via the shortcut menu in the table header.
6. Add additional parameters if needed.

   A digital or analog axis is inserted automatically if you insert a parameter of a specific data type for which an axis does not yet exist.

   To add a parameter to a specific axis, select the desired axis during insertion. You cannot move the parameters in the table.
7. Configure the properties of the inserted axes in the table:

   - Name of the axis

     The axis name is displayed in the trend view as axis label.
   - Minimum value
   - Maximum value
   - Position (left or right)
   - Unit of the values
   - Axis mode (linear or logarithmic)

   The "Unit" and "Axis mode" properties can only be edited for analog axes.

#### Alternative procedure: Inserting parameters

If the trend display is not open, drag-and-drop a parameter from the chart to the corresponding trend display in the project tree.

The parameter is automatically assigned to an axis.

If it does not yet exist, the axis is generated automatically.

#### Result

You successfully created a new trend display and configured the parameters/tags to be visualized.

---

**See also**

[Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)
  
[Using the trend display](#using-the-trend-display)

### Using the trend display

#### Overview

A trend display allows you to visualize multiple online values in a trend chart.

> **Note**
>
> **Value display depending on the interconnection**
>
> You can only record trends from the values that can also be monitored in online mode.
>
> For this reason, no values of instructions are displayed in the trend chart if the input parameters are not interconnected.

**Additional information**

- "[Creating a trend display](#creating-a-trend-display)"
- "[Trend display - Functions and operating options](#trend-display---functions-and-operating-options)"

#### Trend values: Performance data and storage capacity requirement

**Trend values per trend**

A maximum of 10000 trend values per trend can be stored in the trend display.

**Memory requirements**

Each trend value occupies 16 bytes of memory.

That is, each trend occupies a maximum of 1.6 MB.

**Sampling time and time range**

You increase the sampling time to extend the time range of stored trend values.

- 1 s sampling time: A time range of approx. 2.7 hours can be stored.
- 10 s sampling time: A time range of approx. 27.7 hours can be saved.

For S7 target systems, you have the following options to specify the sampling time:

- In the "Testing" task card in the "Test settings" area you specify the "Sampling time chart" in milliseconds.

  - Minimum value for CFC charts: 500 ms
  - Minimum value for parameters: 200 ms
- You change the sampling time for analog values in the "Sampling time" column of the definition table in the trend display.

  This value can only be equal to or greater than the value of the "Sampling time chart".

#### Requirements

- The CFC charts and blocks have been compiled and downloaded to the device.
- The trend display is configured.
- The online connection to the device has been established once before.
- To display value changes, the CPU of the device must be in "RUN" mode.

#### Procedure

1. Open the trend display by double-clicking its name in the "Charts - Trend/dynamic display & force table" folder.

   The table for the axis definition and the window for the trend chart are displayed in the editor window.
2. Click "Go online" in the toolbar.
3. Click the "Monitoring on/off" toolbar icon in the editor window of the trend display: ![Procedure](images/144083943435_DV_resource.Stream@PNG-de-DE.png)
4. If you hover over the trend line with the mouse, a tooltip with the trend name is displayed for each displayed digital or analog trend.

   When you click on the trend name, the configured data source is displayed.
5. In the toolbar, in the "Time span of x axis" drop-down list, select the time range that the trend chart is to display.

   For analog values, you select the time for each analog trend individually in the "Sampling time" column of the definition table.

   This selection also influences the time range that a trend display can save.
6. In the toolbar, select the functions for controlling the display in the trend view.

   The display of the online values and the trend chart is adjusted.
7. Depending on the target system, the "Testing" task card may contain additional settings for testing and displaying online value.

   Additional information on the S7 target system: "Working with CFC charts for S7"

#### Result

Online values are shown in a trend chart with the trend display.

---

**See also**

[Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)

### Creating a dynamic display

A dynamic display allows you to visualize multiple online values in a table.

This section describes how to create and configure a new dynamic display.

#### Requirements

- The parameters whose online values are to be displayed in the dynamic display must be configured.
- The CFC charts and blocks must be compiled.

#### Procedure

1. Double-click the "Add new dynamic display" entry in the "Charts - Trend/dynamic display & force table" folder of the project tree.

   - A new dynamic display is added in the folder.
   - The table for the dynamic display is opened in the editor window.

   Work in the table of the dynamic display to configure parameters whose online values are to be displayed in the dynamic display.
2. To change the name of the dynamic display, select the "Rename" entry in the shortcut menu in the project tree.
3. Open a CFC chart in a second editor window.

   Navigate to the desired parameter in the CFC chart or in the chart interface.
4. Drag-and-drop the parameter from the chart into the "Tag name" column.

   Alternatively, use Copy and Paste from the shortcut menu or the <Ctrl+C> and <Ctrl+V> keyboard shortcuts.

   The inserted parameter is displayed in a new row of the table.

   The "Tag name" column contains the link to this parameter.
5. Configure the properties in the row containing the inserted parameter.

   You can show and hide columns via the shortcut menu in the table header.

   The "Unit" property can only be edited for analog values.
6. Add additional parameters if needed.
7. You can exclude individual parameters from updating:

   In the Inspector window, disable the "For test" option in the "Properties" tab. Online values are displayed only for the parameters for which the option is enabled.

   This function is particularly useful if you have numerous tags/parameters in the dynamic display and do not need all online values.

#### Alternative procedure: Inserting parameters

If the dynamic display is not open, drag-and-drop a parameter from the chart to the corresponding dynamic display in the project tree.

#### Result

You have successfully created a new dynamic display and configured the parameters/tags to be visualized.

---

**See also**

[Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)
  
[Using the dynamic display](#using-the-dynamic-display)

### Using the dynamic display

A dynamic display allows you to visualize multiple online values in tabular format.

Additional information: "[Creating a dynamic display](#creating-a-dynamic-display)"

#### Requirements

- The CFC charts and blocks have been compiled and downloaded to the device.
- The dynamic display has been configured.
- The online connection to the device has been established once before.
- To display value changes, the CPU of the device must be in "RUN" mode.

#### Procedure

1. Open the dynamic display by double-clicking its name in the "Charts - Trend/dynamic display & force table" folder.

   The editor displays a table.
2. Click "Go online" in the toolbar.
3. Click the "Monitoring on/off" toolbar icon in the editor window of the dynamic display: ![Procedure](images/144083943435_DV_resource.Stream@PNG-de-DE.png)

   The current online values of the configured tags or parameters are displayed in the table.
4. Check the settings in the "For test" column:

   - If the option is enabled, the online values of the configured tags or parameters are displayed.
   - If the option is disabled, no online value is displayed for the corresponding parameter.
5. You can add additional parameters to the table in online mode.

   For example, drag-and-drop a parameter from a CFC chart into the table of the dynamic display.
6. Depending on the target system, the "Testing" task card may contain additional settings for testing and displaying online value.

   Additional information on the S7 target system: "Working with CFC charts for S7"

#### Result

Online values are displayed in a table with the dynamic display.

---

**See also**

[Overview of the trend and dynamic displays](#overview-of-the-trend-and-dynamic-displays)

## Data types in CFC

This section contains information on the following topics:

- [Data types in the TIA Portal](#data-types-in-the-tia-portal)
- [Elementary data types](#elementary-data-types)
- [Compound data types](#compound-data-types)
- [User-defined data types](#user-defined-data-types)
- [Pointer](#pointer)
- [System data types](#system-data-types)
- [Hardware data types](#hardware-data-types)

### Data types in the TIA Portal

CFCs support the standard data types of the TIA Portal.

Additional information on syntax and display of the data types, for example, is available in the TIA Portal information system:

- "Program PLC > [Data types](Data%20types.md#overview-of-the-valid-data-types)"

### Elementary data types

This section contains information on the following topics:

- [Bit strings](#bit-strings)
- [Integers](#integers)
- [Floating-point numbers](#floating-point-numbers)
- [Duration (Times)](#duration-times)
- [Point in time (Date and time)](#point-in-time-date-and-time)
- [Characters](#characters)
- [Parameter types](#parameter-types)

#### Bit strings

This section contains information on the following topics:

- [BOOL (Boolean)](#bool-boolean)
- [BYTE](#byte)
- [WORD](#word)
- [DWORD (Double Word)](#dword-double-word)
- [LWORD (Long Word)](#lword-long-word)

##### BOOL (Boolean)

###### Keyword

BOOL

###### Description

Bit value

###### Value range

0 to 1

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### BYTE

###### Keyword

BYTE

###### Description

Sequence of 8 bits

###### Value range

0 to 255

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### WORD

###### Keyword

WORD

###### Description

Sequence of 16 bits

###### Value range

0 to 65535

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### DWORD (Double Word)

###### Keyword

DWORD

###### Description

Sequence of 32 bits

###### Value range

0 to 4294967295

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### LWORD (Long Word)

###### Keyword

LWORD

###### Description

Sequence of 64 bits

###### Value range

- Signed integers:

  -9_223_372_036_854_775_808 to +9_223_372_036_854_775_807
- Unsigned integers:

  0 to 18_446_744_073_709_551_615

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Integers

This section contains information on the following topics:

- [Signed integers](#signed-integers)
- [Unsigned integers](#unsigned-integers)

##### Signed integers

This section contains information on the following topics:

- [SINT (Short Integer)](#sint-short-integer)
- [INT (Integer)](#int-integer)
- [DINT (Double Integer)](#dint-double-integer)
- [LINT (Long Integer)](#lint-long-integer)

###### SINT (Short Integer)

###### Keyword

SINT

###### Description

Signed integer

###### Value range

-128 to +127

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### INT (Integer)

###### Keyword

INT

###### Description

Signed integer

###### Value range

-32768 to 32767

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### DINT (Double Integer)

###### Keyword

DINT

###### Description

Signed double integer

###### Value range

From -2 147 483 648 to +2 147 483 647

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### LINT (Long Integer)

###### Keyword

LINT

###### Description

Signed integer

###### Value range

-9_223_372_036_854_775_808 to +9_223_372_036_854_775_807

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### Unsigned integers

This section contains information on the following topics:

- [USINT (Unsigned Short Integer)](#usint-unsigned-short-integer)
- [UINT (Unsigned Integer)](#uint-unsigned-integer)
- [UDINT (Unsigned Double Integer)](#udint-unsigned-double-integer)
- [ULINT (Unsigned Long Integer)](#ulint-unsigned-long-integer)

###### USINT (Unsigned Short Integer)

###### Keyword

USINT

###### Description

Unsigned integer

###### Value range

0 to 255

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### UINT (Unsigned Integer)

###### Keyword

UINT

###### Description

Unsigned double integer

Length 16 bits

###### Value range

From 0 to 65_535

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### UDINT (Unsigned Double Integer)

###### Keyword

UDINT

###### Description

Unsigned integer

###### Value range

0 to 4_294_967_295

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

###### ULINT (Unsigned Long Integer)

###### Keyword

ULINT

###### Description

Unsigned integer

###### Value range

0 to 18_446_744_073_709_551_615

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Floating-point numbers

This section contains information on the following topics:

- [REAL (Real Numbers)](#real-real-numbers)
- [LREAL (Long Reals)](#lreal-long-reals)

##### REAL (Real Numbers)

###### Keyword

REAL

###### Description

Signed floating-point number

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### LREAL (Long Reals)

###### Keyword

LREAL

###### Description

Unsigned floating-point number

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Duration (Times)

This section contains information on the following topics:

- [TIME](#time)
- [LTIME (Long Time)](#ltime-long-time)
- [S5TIME](#s5time)

##### TIME

###### Keyword

TIME

###### Description

Duration

###### Value range

-24d_20h_31m_23s_648ms to 24d_20h_31m_23s_647ms

(In milliseconds: -2147483648 ms to 2147483647 ms)

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### LTIME (Long Time)

###### Keyword

LTIME

###### Description

Duration

Days (d), hours (h), minutes (min), seconds (s), milliseconds (ms), microseconds (μs) and nanoseconds (ns).

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### S5TIME

###### Keyword

S5TIME

###### Description

Duration in S5 format

###### Value range

From 0h_0m_0s to 2h_46m_30s

From 0 to 9990 ms in steps of 10 ms

From 100 ms to 99900 ms in steps of 100 ms

From 1 s to 999 s in steps of 1 s

From 10 s to 9990 s in steps of 10 s

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Point in time (Date and time)

This section contains information on the following topics:

- [DATE (Date)](#date-date)
- [TOD (Time of Day)](#tod-time-of-day)
- [LTOD (Long Time of Day)](#ltod-long-time-of-day)
- [DT (Date and Time of Day)](#dt-date-and-time-of-day)
- [LDT (Long Date and Time)](#ldt-long-date-and-time)
- [DTL](#dtl)

##### DATE (Date)

###### Keyword

DATE

###### Description

Point in time

Date (YYYY-MM-DD), e.g. 2020-01-26

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### TOD (Time of Day)

###### Keyword

TOD or TIME_OF_DAY

###### Description

Point in time

Time-of-day in hours:minutes:seconds.milliseconds (HH:MM:SS.MS), e.g. 15:21:00.321

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### LTOD (Long Time of Day)

###### Keyword

LTOD or LTIME_OF_DAY

###### Description

Point in time

Number of nanoseconds since the start of day (0:00 hrs).

Time-of-day in hours:minutes:seconds.nanoseconds (HH:MM:SS.NS)

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### DT (Date and Time of Day)

###### Keyword

DT or DATE_AND_TIME

###### Description

Point in time

Information on date and time of day in BCD format (YYYY-MM-DD-HH:MM.SS.MS)

###### Value range

Min.: DT#1990-01-01-00:00:00.000

Max.: DT#2089-12-31-23:59:59.999

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### LDT (Long Date and Time)

###### Keyword

LDT or LDATE_AND_TIME

###### Description

Point in time

Information on date and time in nanoseconds since 01/01/1970 0:0.

###### DTL and LDT

The data types DTL and DTL provide the same information. The internal data format of these two data types has been optimized for specific operations.

Adding and subtracting, for example, is very easy with LDT.

DTL is suitable for reading the date.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### DTL

###### Keyword

DTL

###### Description

Point in time

###### DTL and LDT

The data types DTL and LDT provide the same information. The internal data format of these two data types has been optimized for specific operations.

Adding and subtracting, for example, is very easy with LDT.

DTL is suitable for reading the date.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Characters

This section contains information on the following topics:

- [CHAR (Single-Byte Character)](#char-single-byte-character)
- [WCHAR (Double-Byte Character)](#wchar-double-byte-character)

##### CHAR (Single-Byte Character)

###### Keyword

CHAR

###### Description

Single character

###### Value range

Depending on the selected Windows character set either "single byte" or "multibyte".

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### WCHAR (Double-Byte Character)

###### Keyword

WCHAR

###### Description

Tag.

Single character.

Sequence of 16 bits.

###### Value range

$0000 - $D7FF

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### Parameter types

This section contains information on the following topics:

- [TIMER](#timer)
- [COUNTER](#counter)

##### TIMER

###### Keyword

TIMER

###### Description

Number of an S7 timer.

###### Value range

0 to 65535 (number depends on the target system).

###### Notes on use in the CFC chart

The data type is not supported in the chart interface.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

##### COUNTER

###### Keyword

COUNTER

###### Description

Number of an S7 counter

###### Value range

0 to 65535 (number depends on the target system).

###### Notes on use in the CFC chart

The data type is not supported in the chart interface.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

### Compound data types

This section contains information on the following topics:

- [STRUCT](#struct)
- [STRING](#string)
- [ARRAY](#array)

#### STRUCT

##### Keyword

STRUCT

##### Description

A structure of data consisting of different elementary and complex data types.

##### Value range

The value ranges of the used data types apply.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### STRING

##### Keyword

STRING

##### Description

String

##### Value range

Without additional information, the data type has a dimension of up to 254 characters.

To explicitly define a specific length, use the syntax STRING[N].

##### STRING[N]

Character string with a length of "N" bytes.

Depending on the selected Windows character set "single byte" or "multibyte" (at least N/2 characters).

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### ARRAY

##### Keyword

ARRAY

##### Description

Data structure consisting of a fixed number of components of the same data type.

All data types except ARRAY and reference data types are permitted for the ARRAY components.

Multidimensional ARRAYs are also supported, e.g.: `"MyDB".MyArray[#i,#j]`. You can find more information on multidimensional ARRAYs as well as an example in the TIA Portal information system under "Programming the PLC > Data types > [Basic information on ARRAY](Data%20types.md#basic-information-on-array)".

Not permitted data types for ARRAY components:

- ARRAY
- Pointer: ANY, POINTER, VARIANT
- Parameter types: COUNTER, TIMER

**Format**

- ARRAY[Low limit..High limit] of <Data type>

##### Restrictions

Supported functions in CFC:

- Import of blocks containing parameters of the data type "ARRAY" with fixed dimension limits
- Import of FBs with the element type "Array of FB":

  ARRAYs of FB types are only allowed in the "Static" section of the block.
- Interconnections between same-type block interfaces of ARRAY tags
- Interconnections of ARRAY module connections with type-same parameters of global DBs

Unsupported functions in CFC:

- Import of blocks containing parameters of data type "ARRAY" with dynamic dimension limits
- Import of FBs with element type "Array of FB" in other sections besides the "Static" section of the block:
- Access to elements within ARRAY tags
- Online display of values in ARRAY tags
- Testing with the "Forcing" function

##### Value range

The specified value ranges are maximum values. The actual number of ARRAY elements that can be used depends on the data type and the CPU used.

**Blocks with standard access**

- [-32 768..32 767] of <DataType>

**S7-1500 blocks with optimized access *)**

- [-2 147 483 648..2 147 483 647] of <DataType>

  Maximum number of ARRAY elements in total:

  - 16 777 216 (= 2 <sup>24</sup>)

<sub>*) The internal storage structure is hidden for S7-1500 blocks with optimized access. The system automatically optimizes and manages the addresses. More information: "Working with CFC charts for S7 > Blocks in CFC charts for S7"</sub>

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)
  
[Basic information on ARRAY](Data%20types.md#basic-information-on-array)
  
Blocks in CFC charts for S7
  
[Example of a multi-dimensional ARRAY](Data%20types.md#example-of-a-multi-dimensional-array)

### User-defined data types

**Overview**

In addition to the elementary and complex data types, you can also use your own data types, so-called "user-defined data types", in a TIA project. These data types are also referred to as "User Defined Datatypes" (UDT).

A user-defined data type is an individually defined version of the STRUCT data type and is stored with its own name (UDT name) in the project.

CFC interprets tags with a UDT name, such as block interfaces, as if these tags were combined directly with a data structure of the STRUCT data type.

---

**See also**

[STRUCT](#struct)
  
[Data types in the TIA Portal](#data-types-in-the-tia-portal)

### Pointer

This section contains information on the following topics:

- [VARIANT](#variant)
- [POINTER](#pointer-1)
- [ANY](#any)

#### VARIANT

##### Keyword

VARIANT

##### Description

A block input of the VARIANT data type can be interconnected with a source of any data type.

The block input can also be interconnected with a data block element of an ARRAY type.

**Exception**

Interconnections with a source of the data type ANY or POINTER are not supported in CFC.

**Notes on use in the CFC**

Blocks with output parameters of the VARIANT data type cannot be imported into CFC.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### POINTER

##### Keyword

POINTER

##### Description

Pointer to a memory area

##### Value range

Only as interconnection

##### Notes on use in the CFC

You can interconnect an input or output parameter of the data type POINTER with all data types except POINTER and ANY.

The destination can also be an external tag.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

#### ANY

##### Keyword

ANY

##### Description

Pointer to a data element

##### Value range

Only as an interconnection with input or output parameter or external tag.

##### Notes on use in the CFC

You can interconnect an input or output parameter of the data type ANY with all data types except POINTER and ANY.

The destination can also be an external tag.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

### System data types

System data types are not supported in CFC.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

### Hardware data types

**Overview**

Hardware data types are made available by the CPU. The number of available hardware data types depends on the CPU.

Some hardware data types are versions of elementary or complex data types.

CFC interprets tags with hardware data types, such as block interfaces, as if these tags were an elementary or complex data type.

---

**See also**

[Data types in the TIA Portal](#data-types-in-the-tia-portal)

## Openness: CFC

This section contains information on the following topics:

- [CFC Charts (Export/Import)](CFC%20Charts%20%28Export-Import%29.md#cfc-charts-exportimport)

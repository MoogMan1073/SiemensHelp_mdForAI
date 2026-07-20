---
title: "Creating FBD programs"
package: ProgBlockFUPenUS
topics: 68
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating FBD programs

This section contains information on the following topics:

- [Basic information on FBD](#basic-information-on-fbd)
- [Settings for FBD](#settings-for-fbd)
- [Working with networks](#working-with-networks)
- [Inserting FBD elements](#inserting-fbd-elements)
- [Editing FBD elements](#editing-fbd-elements)
- [Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
- [Branches in FBD](#branches-in-fbd)
- [Logic paths in FBD](#logic-paths-in-fbd)
- [FBD programming examples](#fbd-programming-examples)

## Basic information on FBD

This section contains information on the following topics:

- [FBD programming language](#fbd-programming-language)
- [Overview of the FBD elements](#overview-of-the-fbd-elements)

### FBD programming language

#### Overview of the Function Block Diagram (FBD) programming language

FBD is a graphical programming language. The representation is based on electronic circuit systems.

The program is mapped in one or more networks. A network contains one or more logic operation paths. The binary signal scans are linked by boxes. The representation of the logic is based on the graphical logic symbols used in Boolean algebra.

#### Example of networks in FBD

The following figure shows an FBD network with AND and OR boxes and an assignment:

![Example of networks in FBD](images/22193133067_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Working with networks](#working-with-networks)

### Overview of the FBD elements

#### FBD elements

An FBD program consists of separate elements that are linked by means of a binary signal flow. Most program elements must be supplied with tags.

A FBD network is programmed from left to right.

For example, the following figure shows elements of an FBD network:

![FBD elements](images/13950837387_DV_resource.Stream@PNG-en-US.png)

1) Binary function

2) Standard box

3) Complex box

#### Binary functions

You can use binary functions to query binary operands and to combine their signal states. The following operations are examples of binary functions: "AND operation", "OR operation" and "EXCLUSIVE OR operation".

#### Standard boxes:

You can use standard boxes to control binary operands, perform RLO edge detection or execute jump functions in the program. Standard boxes generally have only one single input.

#### Complex boxes

Complex boxes represent program elements with complex functions. The empty box is an exception. You can use the empty box as a placeholder in which you can select the required instruction.

The following types of boxes are available to you in an FBD program:

- Complex boxes without EN/ENO mechanism:  
  A box is executed independently of the signal state at the box inputs. The error status of the processing cannot be queried.
- Complex boxes with EN/ENO mechanism:  
  A box is only executed if the enable input "EN" has the signal state "1". If the box is processed correctly, the "ENO" enable output has signal state "1". If an error occurs during processing, the "ENO" output is reset.  
  If the EN enable input is not interconnected, the box is always executed.

Calls of code block are also shown in the network as complex boxes with EN/ENO mechanism.

---

**See also**

[EN/ENO mechanism](Programming%20basics.md#eneno-mechanism)

## Settings for FBD

This section contains information on the following topics:

- [Overview of the settings for FBD](#overview-of-the-settings-for-fbd)
- [Changing the settings](#changing-the-settings)

### Overview of the settings for FBD

#### Overview

The following table shows the settings that you can make:

| Group | Setting | Description |
| --- | --- | --- |
| Font | Font size | Font size in program editor |
| View | Layout | Compact or wide  Changes the vertical spacing between operands and other objects (such as operand and contact). The change becomes visible once the block is reopened. |
| Operand field | Maximum width | Maximum number of characters that can be entered horizontally in the operand field. This setting recalculates the layout of the networks.  Note that, depending on the length of the formal parameter names, the width of the displayed boxes can change as well. |
| Maximum height | Maximum number of characters that can be entered vertically in the operand field. This setting recalculates the layout of the networks. |  |

---

**See also**

[Changing the settings](#changing-the-settings)

### Changing the settings

#### Procedure

To change the settings, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "PLC programming" group.
3. Change the settings.

#### Result

The change will be loaded directly, there is no need to save it explicitly.

---

**See also**

[Overview of the settings for FBD](#overview-of-the-settings-for-fbd)

## Working with networks

This section contains information on the following topics:

- [Using networks](#using-networks)
- [Inserting networks](#inserting-networks)
- [Selecting networks](#selecting-networks)
- [Copying and pasting networks](#copying-and-pasting-networks)
- [Deleting networks](#deleting-networks)
- [Expanding and collapsing networks](#expanding-and-collapsing-networks)
- [Inserting network title](#inserting-network-title)
- [Entering a network comment](#entering-a-network-comment)
- [Navigating networks](#navigating-networks)

### Using networks

#### Function

The user program is created in the block within networks. For a code block to be programmed, it must contain at least one network. To achieve a better overview of the user program, you can also subdivide your program into several networks.

You have the option to insert networks for the textual programming languages SCL and STL in LAD and FBD blocks, and then use instructions in these programming languages. Depending on the CPU you are using, you can insert networks for the following programming languages:

- S7-300/400: STL networks
- S7-1200: SCL networks
- S7-1500: STL and SCL networks

The programming editor always adapts to the network that currently has the focus. This means that you have access to the SCL instructions as well as the SCL functions when programming an SCL network.

> **Note**
>
> You cannot use the instruction "Goto" in SCL networks within LAD or FBD blocks.

#### EN/ENO mechanism in blocks with different network languages

You can also use ​​the EN/ENO mechanism in blocks with different network languages. Each programming language displays the error status differently:

- SCL has an "ENO" tag that stores the error status and can be queried. Direct access to this tag is only possible with SCL.
- LAD/FBD/STL have no special tag for "ENO". However, you can read the error status for STL from the BR bit, and query it via the RET coil for LAD/FBD.

The following rules apply to reading out the error status for the entire block:

- The last network in the block is a LAD/FBD network:

  If you do not use RET coils, the error status is "TRUE" by default.
- The last network in the block is an STL network:

  The BR bit determines the error status. The BR bit can be edited in STL networks using the BR tab.
- The last network in the block is an SCL network:

  The "ENO" tag determines the error status of the block.

---

**See also**

[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Inserting networks

You can either insert a network of the same programming language or a network for a textual programming language in an LAD or FBD block. Keep in mind, however, that not all CPU types support all textual languages.

#### Requirement

An LAD or FBD block is open.

#### Insert LAD or FBD network

To insert a new network, follow these steps:

1. Select the network after which you want to insert a new network.
2. Select the "Insert network" command in the shortcut menu.

#### Insert STL or SCL network

To insert a new network, follow these steps:

1. Select the network after which you want to insert a new network.
2. Select the "Insert STL network" or "Insert SCL network" command in the shortcut menu.

#### Result

A new, empty network is inserted in the block in the corresponding programming language.

---

**See also**

[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Selecting networks

#### Requirements

A network is available.

#### Selecting a network

To select a network, follow these steps:

1. Click the title bar of the network that you want to select.

#### Selecting several networks

Proceed as follows to select several individual networks:

1. Press and hold down the <Ctrl> key.
2. Click all the networks that you want to select.

To select several successive networks, follow these steps:

1. Press and hold down the <Shift> key.
2. Click the first network that you want to select.
3. Click the last network that you want to select.

   The first and last networks and all those in between are selected.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Copying and pasting networks

Copied networks can be pasted within the block or in another block. Networks that were created in LAD or FBD can also be inserted in blocks of the respective other programming language.

#### Requirement

A network is available.

#### Procedure

To copy and paste a network, follow these steps:

1. Select the network or networks to be copied.
2. Select "Copy" in the shortcut menu.
3. Select the network after which you want to paste in the copied network.
4. Select "Paste" in the shortcut menu.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Deleting networks

#### Requirement

A network is available.

#### Procedure

To delete a network, follow these steps:

1. Select the network that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Expanding and collapsing networks

#### Requirements

A network is available.

#### Opening and closing a network

To open a network, follow these steps:

1. Click on the right arrow in the network title bar.

To close a network, follow these steps:

1. Click on the down arrow in the network title bar.

#### Opening and closing all networks

To open and close all networks, follow these steps:

1. In the toolbar, click "Open all networks" or "Close all networks".

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Inserting network title

The network title is the header of a network. The length of the network title is limited to one line. You can enter the title manually or set it automatically. When you set it automatically, you can do this for individual networks or use the settings to specify that the network title is always set automatically.

For automatic insertion of the network title, the comment of the operand in one of the following instructions in the network is evaluated:

- Assignment
- Set output
- Reset output

The instruction that is listed first in the network is used.

The network title is only inserted automatically when the following conditions are fulfilled:

- The network does not have a title yet.
- The operand of the instruction used for the comment has a comment.

> **Note**
>
> Note the following restrictions for automatic insertion of the network title:
>
> - The network title is not adapted if you change the comment of the operand at a later time.
> - The network title is not adapted if you change the operand of the instruction.
> - The network title is only set by the writing instructions listed above.
> - If the operand is of the data type array, the comment of the array is used and not the comments of the array elements.
> - Comments of invalid operands are not taken into consideration.

#### Entering the network title manually

To enter a network title, follow these steps:

1. Click on the title bar of the network.
2. Enter the network title.

#### Setting the network title automatically

To specify that the network titles are always set automatically, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "PLC programming" group.
3. Select the "Set network title automatically" check box in the "Additional settings" group.

   The network titles are set automatically as of this time if the conditions listed above are fulfilled.

To set an individual network title automatically, follow these steps:

1. Right-click "Network <Number of the network>" in the title bar of a network.
2. Select the "Set network title automatically" command in the shortcut menu.

   The title of the selected network is set based on the comment of the operand if the conditions listed above are fulfilled.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Entering a network comment](#entering-a-network-comment)
  
[Navigating networks](#navigating-networks)

### Entering a network comment

You can use network comments to provide comments on the program contents of individual networks. For example, you can indicate the function of the network or draw attention to special characteristics.

#### Requirement

A network is available.

#### Procedure

To enter a network comment, follow these steps:

1. Click on the right arrow before the network title.
2. If the comment area is not visible, click "Network comments on/off" in the toolbar.

   The comment area is displayed.
3. Click "Comment" in the comment area.

   The "Comment" text passage is selected.
4. Enter the network comment.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Navigating networks](#navigating-networks)

### Navigating networks

You can navigate straight to a specific position within a block.

#### Procedure

To navigate to a specific position within a block, follow these steps:

1. Right-click in the code area of the programming window.
2. Select the "Go to > Network/line" command in the shortcut menu.

   The "Go to" dialog will open.
3. Enter the network to which you want to navigate.
4. Enter the line number of the network to which you want to navigate.
5. Confirm your entry with "OK".

#### Result

The relevant line will be displayed if this is possible. If the network or line requested does not exist, the last existing network or the last existing line in the network requested will be displayed.

---

**See also**

[Using networks](#using-networks)
  
[Inserting networks](#inserting-networks)
  
[Selecting networks](#selecting-networks)
  
[Copying and pasting networks](#copying-and-pasting-networks)
  
[Deleting networks](#deleting-networks)
  
[Expanding and collapsing networks](#expanding-and-collapsing-networks)
  
[Inserting network title](#inserting-network-title)
  
[Entering a network comment](#entering-a-network-comment)

## Inserting FBD elements

This section contains information on the following topics:

- [Rules for the use of FBD elements](#rules-for-the-use-of-fbd-elements)
- [Inserting FBD elements using the "Instructions" task card](#inserting-fbd-elements-using-the-instructions-task-card)
- [Inserting FBD elements using an empty box](#inserting-fbd-elements-using-an-empty-box)
- [Selecting the data type of an FBD element](#selecting-the-data-type-of-an-fbd-element)
- [Using favorites in FBD](#using-favorites-in-fbd)
- [Inserting block calls in FBD](#inserting-block-calls-in-fbd)
- [Inserting complex FBD instructions](#inserting-complex-fbd-instructions)
- [Using free-form comments](#using-free-form-comments)

### Rules for the use of FBD elements

#### Rules

Note the following rules when inserting FBD elements:

- An FBD network can consist of several elements. All elements of a logic path must be linked to each other according to IEC 61131-3.
- Standard boxes (flip flops, counters, timers, math operations, etc.) can be added as output to boxes with binary logic operations (for example, AND, OR). Comparison boxes are excluded from this rule.
- Only Boolean inputs in an instruction can be combined with preceding logic operations.
- Only the bottom Boolean output in an instruction can be combined with an additional logic operation.
- Enable input EN or enable output ENO can be connected to boxes, but this is not mandatory.
- Constants (for example, TRUE or FALSE) cannot be assigned to binary logic operations. Instead, use tags of the BOOL data type.
- Only one jump instruction can be inserted in each network.
- Only one jump label can be inserted in each network.
- Instructions for positive or negative RLO edge detection may not be arranged right at the left of the network as this requires a prior logic operation.

#### Placement rules for S7-1200/1500 CPUs

The following table sets out the instructions that can only be positioned at the end of the network:

| Instruction |  | Preceding logic operation required |
| --- | --- | --- |
| Mnemonics | Name |  |
| SET_BF | Set bit field | No |
| RESET_BF | Reset bit field | No |
| JMP | Jump if RLO = 1 | No |
| JMPN | Jump if RLO = 0 | Yes |
| JMP_LIST | Define jump list | No |
| SWITCH | Jump distributor | No |
| RET | Return | No |

#### Placement rules for S7-300/400 CPUs

The following table sets out the instructions that can only be positioned at the end of the network:

| Instruction |  | Preceding logic operation required |
| --- | --- | --- |
| Mnemonics | Name |  |
| S | Set output | Yes |
| R | Reset output | Yes |
| SP | Start pulse timer | Yes |
| SE | Start extended pulse timer | Yes |
| SD | Start on-delay timer | Yes |
| SS | Start retentive on-delay timer | Yes |
| SF | Start off-delay timer | Yes |
| SC | Set counter value | Yes |
| CU | Count up | Yes |
| CD | Count down | Yes |
| JMP | Jump if RLO = 1 | No |
| JMPN | Jump if RLO = 0 | Yes |
| RET | Return | No |
| OPN | Open global data block | No |
| OPNI | Open instance data block | No |
| CALL | Call block | No |
| SAVE | Save RLO in BR bit | No |
| MCRA | Enable MCR range | No |
| MCRD | Disable MCR range | No |
| MCR< | Open MCR ranges | No |
| MCR> | Close MCR ranges | No |

> **Note**
>
> **Calling blocks with binary inputs in S7-300/400 CPUs**
>
> The following FAQ describes the special features when calling blocks with binary inputs:
>
> [FAQ 13988019: What should you watch out for when programming nested FB/FC calls with binary inputs in FBD?](https://support.industry.siemens.com/cs/de/de/view/13988019)

### Inserting FBD elements using the "Instructions" task card

#### Requirement

A network is available.

#### Procedure

To insert FBD elements into a network using the "Instructions" task card, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to the FBD element that you want to insert.
3. Use drag-and-drop to move the element to the desired place in the network.

   If the element is an internal system function block (FB), the "Call options" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks > System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

Or:

1. Select the point in the network at which you want to insert the element.
2. Open the "Instructions" task card.
3. Double-click on the element you want to insert.

   If the element is an internal system function block (FB), the "Call options" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks > System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

#### Result

The selected FBD element is inserted with dummy entries for the parameters.

---

**See also**

[Rules for the use of FBD elements](#rules-for-the-use-of-fbd-elements)
  
[Inserting FBD elements using an empty box](#inserting-fbd-elements-using-an-empty-box)
  
[Inserting FBD elements using favorites](#inserting-fbd-elements-using-favorites)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)
  
[Parameter instances](Programming%20basics.md#parameter-instances)

### Inserting FBD elements using an empty box

#### Requirement

A network is available.

#### Procedure

To insert FBD elements into a network using an empty box, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "General > Empty box" in the "Basic instructions" palette.
3. Use a drag-and-drop operation to move the "Empty box" element to the desired place in the network.
4. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
5. Select the desired FBD element from the drop-down list.

   If the element is an internal system function block (FB), the "Call options" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks > System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

#### Result

The empty box is changed to the respective FBD element. Placeholders are inserted for the parameters.

---

**See also**

[Inserting FBD elements using the "Instructions" task card](#inserting-fbd-elements-using-the-instructions-task-card)
  
[Inserting FBD elements using favorites](#inserting-fbd-elements-using-favorites)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)
  
[Parameter instances](Programming%20basics.md#parameter-instances)

### Selecting the data type of an FBD element

This section contains information on the following topics:

- [Selecting a data type](#selecting-a-data-type)
- [Defining the data type of an instruction](#defining-the-data-type-of-an-instruction)

#### Selecting a data type

##### Introduction

Some instructions can be executed with several different data types. If you use one of these instructions in the program, you have to specify a valid data type for the instruction at the specific point in the program. For some instructions, you have to select the data types for the inputs and outputs separately.

> **Note**
>
> The valid data type (BOOL) for the tags on the enable input EN and the enable output ENO is predefined by the system and cannot be changed.

The valid data types for an instruction are listed in the instruction drop-down list. You specify the data type of the instruction by selecting an entry from the drop-down list. If the data type of an operand differs from the data type of the instruction and cannot be converted implicitly, the operand is displayed in red and a rollout with the corresponding error message appears.

##### Data type selection of mathematical instructions

Some mathematical instructions provide you with the option of having the data type automatically set corresponding to the data types of the operand. In the drop-down list for data type selection, these instructions have the entry "Auto" in addition to the actual data types. If you select this entry and then allocate the first operand, the data type of the operand is selected as data type for the instruction. The entry in the drop-down list changes to "Auto (<Data type>)", e.g. "Auto (Real)". If you allocate additional operands, the automatically set data type of the instruction is adjusted according to the following criteria:

- You supply all other operands with tags of the same data type:

  The data type of the instruction is not changed.
- You supply all other operands with tags whose data type is smaller than the data type of the instruction:

  The data type of the instruction is not changed. For the operand with the smaller data type, an implicit conversion is conducted if necessary.
- You supply an additional operand with a tag whose data type is greater than the data type of the instruction:

  The data type of the instruction is changed to the larger data type. An implicit conversion is performed, if necessary, for operands that deviate from the newly set data type of the instruction.

Each change in the data type of an operand can result in a change of the data type of the instruction. Other operands may possibly be implicitly converted as a result. Operands for which an implicit conversion is performed are marked with a gray square.

> **Note**
>
> Please also observe the information on data type conversion for your device and, in particular, the notes on the IEC check.
>
> See also: [Data type conversion](Data%20types.md#data-type-conversion-for-s7-1200-s7-1200)

---

**See also**

[Defining the data type of an instruction](#defining-the-data-type-of-an-instruction)

#### Defining the data type of an instruction

##### Introduction

Some instructions can be executed with several different data types. When you insert such instructions into your program, you must specify the data type for these instructions at the actual point in the program.

##### Specifying the data type by means of the drop-down list

To define the data type of an instruction using the drop-down list, follow these steps:

1. Insert the instruction at the required point in the program using drag-and-drop.

   The entry "???" (undefined) is displayed in the drop-down list of the inserted instruction.
2. Click the triangle in the upper corner of the drop-down list.

   The drop-down list will open to display the data types valid for the instruction.
3. Select a data type from the drop-down list.

   The selected data type is displayed.
4. If the instruction has two drop-down lists, select the data type for the instruction inputs in the left-hand drop-down list and the data type for the instruction outputs in the right-hand drop-down list.

##### Specifying data type by assigning tags

To define the data type of an instruction by assigning tags, follow these steps:

1. Insert the instruction at the required point in the program using drag-and-drop.

   The entry "???" (undefined) is displayed in the drop-down list of the inserted instruction.
2. At an input or output, specify a valid tag, the data type of which is to be applied as the instruction data type.

   The data type of the tag is displayed in the drop-down list.
3. Enter a valid tag at an input and a valid tag at an output if data types need to be defined for both the inputs and outputs of the instruction. The tag specified at the input determines the data type of the inputs; the tag specified at the output determines the data type of the outputs of the instruction.

##### Automatically specifying the data type of mathematical instructions

To automatically specify the data type for mathematical instructions, follow these steps:

1. Insert the mathematical instruction at the required point in the program using drag-and-drop.

   The entry "???" (undefined) is displayed in the drop-down list of the inserted instruction.
2. Select the "Auto" entry from the drop-down list.
3. Enter a valid tag at an input or output.

   The data type of the tag is applied as data type of the instruction. The entry in the drop-down list changes to "Auto (<Data type>)".

See also: [Selecting a data type](#selecting-a-data-type)

---

**See also**

[Selecting a data type](#selecting-a-data-type)

### Using favorites in FBD

This section contains information on the following topics:

- [Adding FBD elements to Favorites](#adding-fbd-elements-to-favorites)
- [Inserting FBD elements using favorites](#inserting-fbd-elements-using-favorites)
- [Removing FBD elements from Favorites](#removing-fbd-elements-from-favorites)

#### Adding FBD elements to Favorites

##### Requirement

- A block is open.
- The multipane mode is set for the "Instructions" task card or the Favorites are also displayed in the editor.

##### Procedure

To add SCL instructions to the Favorites, follow these steps:

1. Open the "Instructions" task card.
2. Maximize the "Basic instructions" pane.
3. Navigate in the "Basic instructions" pane to the instruction that you want to add to the Favorites.
4. Drag-and-drop the instruction into the "Favorites" pane or into the Favorites area in the program editor.

> **Note**
>
> To additionally display the Favorites in the program editor, click the "Display favorites in the editor" button in the program editor toolbar.

---

**See also**

[Inserting FBD elements using favorites](#inserting-fbd-elements-using-favorites)
  
[Removing FBD elements from Favorites](#removing-fbd-elements-from-favorites)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

#### Inserting FBD elements using favorites

##### Requirement

- A block is open.
- Favorites are available.

##### Procedure

To insert an instruction into a program using Favorites, follow these steps:

1. Drag-and-drop the desired instruction from Favorites to the desired position.

Or:

1. Select the position in the program where you want to insert the instruction.
2. In the Favorites, click on the instruction you want to insert.

> **Note**
>
> To additionally display the Favorites in the program editor, click the "Display favorites in the editor" button in the program editor toolbar.

---

**See also**

[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)
  
[Adding FBD elements to Favorites](#adding-fbd-elements-to-favorites)
  
[Inserting FBD elements using the "Instructions" task card](#inserting-fbd-elements-using-the-instructions-task-card)
  
[Inserting FBD elements using an empty box](#inserting-fbd-elements-using-an-empty-box)
  
[Removing FBD elements from Favorites](#removing-fbd-elements-from-favorites)

#### Removing FBD elements from Favorites

##### Requirement

A code block is open.

##### Procedure

To remove instructions from Favorites, follow these steps:

1. Right-click on the instruction you want to remove.
2. Select the "Remove instruction" command in the shortcut menu.

> **Note**
>
> To additionally display the Favorites in the program editor, click the "Display favorites in the editor" button in the program editor toolbar.

---

**See also**

[Adding FBD elements to Favorites](#adding-fbd-elements-to-favorites)
  
[Inserting FBD elements using favorites](#inserting-fbd-elements-using-favorites)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

### Inserting block calls in FBD

This section contains information on the following topics:

- [Inserting block calls using a drag-and-drop operation](#inserting-block-calls-using-a-drag-and-drop-operation)
- [Updating block calls in FBD](#updating-block-calls-in-fbd)
- [Changing the block call](#changing-the-block-call)
- [Changing the instance type](#changing-the-instance-type)

#### Inserting block calls using a drag-and-drop operation

You can insert calls for existing functions (FC) and function blocks (FB) using a drag-and-drop operation from the project tree. If you call function blocks from other function blocks, you can either call them as a single instance, multi-instance or parameter instance.

See also: [Basics of instances](Programming%20basics.md#basics-of-instances)

##### Requirement

- A network is available.
- The block that is to be called is available.

##### Inserting a call of a function (FC)

To insert a call of a function (FC) into a network using a drag-and-drop operation, follow these steps:

1. Drag the function from the project tree to the required network.

##### Inserting a call for a function block (FB)

To insert a call for a function block (FB), follow these steps:

1. Drag the function block from the project tree to the required network.

   The "Call options" dialog opens.
2. In the dialog, enter whether you want to call the block as a single, multi or parameter instance.

   - If you click on the "Single instance" button, you will have to enter a name in the "Name" text box for the data block that you want to assign to the function block.

     If you call a block that contains monitoring, assign a ProDiag function block to the monitoring functions in the "ProDiag FB" text box.
   - If you click on the "Multi-instance" button, you will have to enter the name of the tag in the "Name in the interface" text box; this is the name that you use to enter the called function block as a static tag in the interface of the calling block.
   - If you click on the "Parameter instance" button, enter the name of the in/out (InOut) parameter to which the instance should be passed during runtime in the "Name in the interface" text box.
3. Confirm your entries with "OK".

##### Result

The function or the function block is inserted with its parameters. You can then assign the parameters.

See also: [Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

> **Note**
>
> If when calling a function block you specify an instance data block that does not exist, it will be created.

---

**See also**

[Updating block calls in FBD](#updating-block-calls-in-fbd)
  
[Changing the instance type](#changing-the-instance-type)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)

#### Updating block calls in FBD

If interface parameters of a called block are changed, the block call can no longer be executed correctly. You can avoid such inconsistent block calls by updating the block calls.

You have the following options for updating the block calls:

- Explicit updating of all inconsistent block calls in the program editor.

  The inconsistent block calls within the open block are updated. The following actions are carried out in the process:

  - New parameters are added.
  - Deleted parameters are removed if they are not connected.
  - Renamed parameters get the new parameter names.
  > **Note**
  >
  > If updating all inconsistent block calls would cause an error in the parameter supply, you cannot use the "Update block calls" command. If this is the case, update each block call individually.
- Explicit updating of a block call in the program editor.

  The "Interface update" dialog is displayed. In this dialog, you have the option of changing the connection of the operands of the new interface. The inconsistent call of this block is then updated. The following actions are carried out in the process:

  - New parameters are added.
  - Deleted parameters are removed if they are not connected.
  - Renamed parameters get the new parameter names.
- Implicit updating during compilation.

  All block calls in the program as well as the used PLC data types will be updated. Note that when you call functions (FCs) before the next compilation process, all new formal parameters must be supplied with actual parameters.

##### Updating all inconsistent block calls in the program editor

To open all block calls in a block, follow these steps:

1. Open the calling block in the program editor.
2. Click "Update inconsistent block calls" in the toolbar.

##### Updating a specific block call in the program editor

To update a specific block call in the program editor, follow these steps:

1. Open the calling block in the program editor.
2. Right-click on the block call that you want to update.
3. Select the "Update" command in the shortcut menu.

   The "Interface update" dialog opens. This dialog shows the differences between the block interface in use and the changed interface of the called block.
4. If necessary, change the connection of the operands. To do this, you have the following options:

   - You can use either a drag-and-drop operation or a cut/copy-and-paste operation to move the operand from the old interface to the new interface.
   - You can delete an operand.
   - You can rename an operand.
   - You can specify a new operand via autocompletion.
5. Click "OK" to update the block call. If you want to cancel the update, click "Cancel".

> **Note**
>
> Note that the "Update block call" command is only available provided you did not previously update all block calls in the editor with the "Update inconsistent block calls" command.

##### Update block calls during compilation

Follow these steps to update all block calls and uses of PLC data types during compilation implicitly:

1. Open the project tree.
2. Select the "Program blocks" folder.
3. Select the command "Compile > Software (rebuild all blocks)" in the shortcut menu.

---

**See also**

[Inserting block calls using a drag-and-drop operation](#inserting-block-calls-using-a-drag-and-drop-operation)
  
[Changing the instance type](#changing-the-instance-type)
  
[Block calls](Programming%20basics.md#block-calls)

#### Changing the block call

You have the option of changing the called block for a block call. But keep in mind that no new instance data blocks are created, for example, when changing from a function (FC) to a function block (FB).

##### Procedure

To change the called block of a block call, follow these steps:

1. Click on the name of the called block within the block call and press the <F2> key. Or double-click the name of the called block.

   A text box opens, and the name of the currently called block is selected.
2. Enter the name of the block you want to call or select a block in the autocompletion.
3. If you want to call an FB, create a new instance data block, if necessary, and specify it as operand.

#### Changing the instance type

##### Instance type

There are two ways of calling function blocks:

- As a single instance
- As a multiple instance
- As parameter instance

See also: [Basics of instances](Programming%20basics.md#basics-of-instances)

You can modify a defined instance type at any time.

##### Requirement

The user program contains a block call.

##### Procedure

To change the instance type of a function block, follow these steps:

1. Open the code block and select the block call.
2. Select the "Change instance" command in the shortcut menu.

   The "Call options" dialog opens.
3. Click on the button "Single instance", "Multi-instance" or "Parameter instance".

   - If you select the "Single instance" instance type, enter a name for the data block that is to be assigned to the function block.
   - If you select "Multiple instance" as the instance type, enter in the "Name in the interface" text field the name of the tag with which the called function block is to be entered as a static tag in the interface of the calling block.
   - If you select "Parameter instance" as the instance type, enter the name of the in/out (InOut) parameter to which the instance should be passed during runtime in the "Name in the interface" text box.
4. Confirm your entries with "OK".

> **Note**
>
> The previous instances are not deleted automatically.

---

**See also**

[Inserting block calls using a drag-and-drop operation](#inserting-block-calls-using-a-drag-and-drop-operation)
  
[Updating block calls in FBD](#updating-block-calls-in-fbd)
  
[Instances](Programming%20basics.md#instances)

### Inserting complex FBD instructions

This section contains information on the following topics:

- [Using the "Calculate" instruction (S7-1200, S7-1500)](#using-the-calculate-instruction-s7-1200-s7-1500)

#### Using the "Calculate" instruction (S7-1200, S7-1500)

##### Requirement

A network is available.

##### Procedure

Proceed as follows to use the "Calculate" instruction:

1. Open the "Instructions" task card.
2. Navigate to "Math functions > CALCULATE" in the "Basic instructions" pane.
3. Use drag-and-drop to move the element to the desired place in the network.

   The instruction "Calculate" will be inserted for the data type with a placeholder expression and question mark.
4. Enter the data type for the calculation.
5. Enter the operands for the calculation.
6. Click on the "Edit 'Calculate' instruction" button to replace the placeholder expression with the correct expression.

   The "Edit 'Calculate' instruction" dialog will open.
7. Enter the required expression in the "OUT:= " text box.
8. Confirm your entry with "OK".

**Note**

The calculation is run with the inputs of the "Calculate" instruction. If you want to use constants you must also insert appropriate inputs for them.

**Note**

In the "Example" area you can find an example of a valid expression and possible instructions that you can use.

To determine a value with the help of Pythagoras' theorem, for example, enter "OUT := SQRT (SQR (IN1) + SQR (IN2))".

---

**See also**

[CALCULATE: Calculate (S7-1200, S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#calculate-calculate-s7-1200-s7-1500)

### Using free-form comments

This section contains information on the following topics:

- [Basic information on using free comments in FBD](#basic-information-on-using-free-comments-in-fbd)
- [Inserting free-form comments](#inserting-free-form-comments)
- [Editing free-form comments](#editing-free-form-comments)
- [Deleting free-form comments](#deleting-free-form-comments)

#### Basic information on using free comments in FBD

##### Introduction

Free-form comments allow you to add comments to the source code for graphic programming languages similar to line comments for textual languages.

Free-form comments can be used for all non-binary boxes.

##### Commenting out program code

To deactivate individual instructions or entire program sections in the LAD and FBD programming languages, you must set a bit parallel to the instruction or in series to an instruction block. Commenting out, as in STL and SCL, is not possible in LAD and FBD.

Examples of commenting out program code in all programming languages are available in the Siemens Industry Online under the following FAQ ID: [109482004](https://support.industry.siemens.com/cs/hu/en/view/109482004)

---

**See also**

[Inserting free-form comments](#inserting-free-form-comments)
  
[Editing free-form comments](#editing-free-form-comments)
  
[Deleting free-form comments](#deleting-free-form-comments)

#### Inserting free-form comments

##### Requirement

A network with instructions is available.

##### Procedure

To insert a free comment on an instruction, proceed as follows:

1. If necessary, activate the "Free-form comments on/off" button in the toolbar.
2. Right-click on the instruction for which you want to insert a free-form comment.
3. Select the "Insert comment" command in the shortcut menu.

   A comment box with a standard comment opens. The comment box is connected by an arrow to the corresponding instruction.
4. Enter the required comment in the comment box.

---

**See also**

[Basic information on using free comments in FBD](#basic-information-on-using-free-comments-in-fbd) 
  
[Editing free-form comments](#editing-free-form-comments)
  
[Deleting free-form comments](#deleting-free-form-comments)

#### Editing free-form comments

##### Introduction

Free-form comments can be edited as follows:

- Changing the comment text
- Changing the position and size of the comment box
- Attaching a comment to another element
- Showing and hiding free comments

##### Changing the comment text

To change the text of free-form comments, follow these steps:

1. Click on the comment box.
2. Enter the desired text.

##### Changing the position of the comment box

To change the positioning of the comment box, follow the steps below:

1. Left-click the comment box and keep the mouse button pressed.
2. Drag the comment box to the desired location.

##### Changing the size of the comment box

To change the size of the comment box, follow the steps below:

1. Click on the comment box.
2. Drag the comment box on the move handle in the lower right corner to the desired size.

##### Attaching a comment to another element

To attach a free-form comment to another element, follow these steps:

1. Left-click the point of the arrow that links the comment box with the instruction and keep the mouse button pressed.
2. Drag the arrow to the element to which you want to attach the comment. Possible insertion points are marked with a green square.
3. Release the mouse button.

##### Showing and hiding free comments

To show or hide a free-form comments, follow these steps:

1. Click the "Free-form comment on/off" button in the toolbar.

---

**See also**

[Basic information on using free comments in FBD](#basic-information-on-using-free-comments-in-fbd) 
  
[Inserting free-form comments](#inserting-free-form-comments)
  
[Deleting free-form comments](#deleting-free-form-comments)

#### Deleting free-form comments

##### Procedure

To delete a free-form comment, proceed as follows:

1. Right-click on the free-form comment that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on using free comments in FBD](#basic-information-on-using-free-comments-in-fbd) 
  
[Inserting free-form comments](#inserting-free-form-comments)
  
[Editing free-form comments](#editing-free-form-comments)

## Editing FBD elements

This section contains information on the following topics:

- [Selecting FBD elements](#selecting-fbd-elements)
- [Copying FBD elements](#copying-fbd-elements)
- [Cutting FBD elements](#cutting-fbd-elements)
- [Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
- [Replacing FBD elements](#replacing-fbd-elements)
- [Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
- [Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
- [Deleting FBD elements](#deleting-fbd-elements)

### Selecting FBD elements

You can select several individual elements or all elements in a network.

#### Requirement

FBD elements are available

#### Selecting several individual FBD elements

To select several individual FBD elements, follow these steps:

1. Press and hold down the <Ctrl> key.
2. Click on all the FBD elements you wish to select.
3. Now release the <Ctrl> key.

#### Selecting all FBD elements in a network

To select all FBD elements in a network, follow these steps:

1. Go to the network whose elements you wish to select.
2. Select the "Select all" command in the "Edit" menu or press <Ctrl+A>.

---

**See also**

[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Copying FBD elements

#### Requirement

An FBD element is available.

#### Procedure

To copy an FBD element, follow these steps:

1. Right-click the FBD element that you want to copy.
2. Select "Copy" in the shortcut menu.

#### Result

The FBD element will be copied and saved to the clipboard.

---

**See also**

[Selecting FBD elements](#selecting-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Cutting FBD elements

#### Requirement

An FBD element is available.

#### Cutting

To cut an FBD element, follow these steps:

1. Right-click the FBD element that you want to cut.
2. Select "Cut" in the shortcut menu.

#### Result

The FBD element will be cut and saved to the clipboard.

---

**See also**

[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Pasting an FBD element from the clipboard

#### Requirement

An FBD element is available.

#### Procedure

To paste an FBD element from the clipboard, follow these steps:

1. Copy an FBD element or cut an FBD element.
2. Right-click the point in the network where you want to paste the element.
3. Select "Paste" in the shortcut menu.

---

**See also**

[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Replacing FBD elements

You can easily exchange FBD elements with other FBD elements of the same type. This has the advantage that the parameters are retained and need not be entered again. For example, you can exchange OR and AND, RS-FlipFlop and SR-FlipFlop, comparison functions or jump instructions.

#### Requirements

A network with at least one FBD element is present.

#### Procedure

To replace an FBD element with another FBD element, follow these steps:

1. Select the FBD element that you want to replace.

   If elements compatible with the selected FBD element are available, a triangle will appear in the upper right-hand corner of the element.
2. Position the cursor above the triangle of the FBD element.

   A drop-down list is displayed.
3. From the drop-down list, select the FBD element that you want to use to replace the existing FBD element.

---

**See also**

[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)

#### Introduction

You can expand several FBD elements with additional inputs that execute arithmetic or binary operations. Such elements are, for example, the instructions "Add" (ADD), "Multiply" (MUL), AND or OR. You can expand the "MOVE value" (MOVE) and "Demultiplex" (DEMUX) instruction boxes by adding additional outputs.

The name of the new inputs and outputs is comprised of the type of inserted element and a consecutive number. The name of a new input is may be "IN2"; the name of a new output may be "OUT2".

#### Requirements

An FBD element is available that permits the insertion of additional inputs and outputs.

#### Inserting an additional input

To add an additional input to the box of an FBD element, follow these steps:

1. Right-click on an existing input of the FBD element.
2. Select "Insert input" in the shortcut menu.

   An additional input is added to the box of the FBD element.

Or:

1. Click on the yellow star symbol beside the last input in the instruction box.

   An additional input is added to the box of the FBD element.

#### Inserting an additional output

To add an additional output to the box of an FBD element, follow these steps:

1. Right-click on an existing output of the FBD element.
2. Select "Insert output" from the shortcut menu.

   An additional output is added to the box of the FBD element.

Or:

1. Click on the yellow star symbol beside the last output of the instruction box.

   An additional output is added to the box of the FBD element.

---

**See also**

[Inserting FBD elements](#inserting-fbd-elements)
  
[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Removing instruction inputs and outputs (S7-1200, S7-1500)

#### Introduction

Inputs and outputs which you have added to an instruction can be removed.

#### Requirement

An FBD element is available, which you have expanded with additional inputs or outputs.

#### Remove input

To remove an input, follow these steps:

1. Select the input that you want to remove.
2. Select the "Delete" command in the shortcut menu.

   The input of the FBD element is removed.

#### Remove output

To remove an output, follow these steps:

1. Select the output that you want to remove.
2. Select the "Delete" command in the shortcut menu.

   The output of the FBD element will be removed.

---

**See also**

[Inserting FBD elements](#inserting-fbd-elements)
  
[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
  
[Deleting FBD elements](#deleting-fbd-elements)

### Deleting FBD elements

#### Requirement

An FBD element is available.

#### Procedure

To delete an FBD element, follow these steps:

1. Right-click the FBD element that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Inserting FBD elements](#inserting-fbd-elements)
  
[Selecting FBD elements](#selecting-fbd-elements)
  
[Copying FBD elements](#copying-fbd-elements)
  
[Cutting FBD elements](#cutting-fbd-elements)
  
[Pasting an FBD element from the clipboard](#pasting-an-fbd-element-from-the-clipboard)
  
[Replacing FBD elements](#replacing-fbd-elements)
  
[Adding additional inputs and outputs to FBD elements (S7-1200, S7-1500)](#adding-additional-inputs-and-outputs-to-fbd-elements-s7-1200-s7-1500)
  
[Removing instruction inputs and outputs (S7-1200, S7-1500)](#removing-instruction-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)

## Inserting operands in FBD instructions

This section contains information on the following topics:

- [Inserting operands](#inserting-operands)
- [Wiring hidden parameters](#wiring-hidden-parameters)
- [Displaying or hiding tag information](#displaying-or-hiding-tag-information)

### Inserting operands

The character strings "<???>", "<??.?>" and "..." are inserted as placeholders for the parameters when a FBD element is inserted:

- The "<???>" and "<??.?>" strings displayed in red indicate parameters that need to be connected.
- The "..." string displayed in black indicates parameters that may be connected.
- "<??.?>" stands for Boolean placeholders.

In addition, FBD elements can have the following different I/Os for the parameters:

- Orange I/Os: Only tags or constants can be interconnected at this I/O.
- Black I/Os: Boolean input or output to which other elements can be connected upstream or downstream.

You can recognize in/out parameters declared in the "InOut" section by the symbol ![Figure](images/153583563915_DV_resource.Stream@PNG-de-DE.png).

> **Note**
>
> To display the available data types in a tooltip, move the cursor over the placeholder.

#### Requirement

An FBD element is available.

#### Procedure

To connect the parameters of an FBD element, follow these steps:

1. Click the placeholder of the parameter.

   An input field is opened.
2. Enter the corresponding parameters, for example a PLC tag, a local tag or a constant.
3. Confirm the parameter with the Enter key.
4. If you have not yet defined the parameter, you can define it directly in the program editor using the shortcut menu.

   See also: "[Declaring PLC tags in the program editor](Declaring%20PLC%20tags.md#declaring-plc-tags-in-the-program-editor)".

**Note**

If you enter the absolute address of a parameter that has already been defined, this absolute address will be changed to the symbolic name of the parameter as soon as the input is confirmed. If you have not yet defined the parameter, a new tag with this absolute address and the default name "Tag_1" will be entered in the PLC tag table. When you confirm your input, the absolute address will be replaced with the symbolic name "Tag_1".

Or drag from it the PLC tag table:

1. In the project tree, select the "PLC tags" folder and open the PLC tag table.
2. If you have opened the PLC tag table, drag the desired tag to the corresponding location in your program. If you have not opened the PLC tag table yet, open the detail view now. Drag the desired tag from the detail view to the appropriate place in your program.

Or drag from it the block interface:

1. Open the block interface.
2. Drag the desired operand from the block interface to the corresponding location in your program.

#### Result

- If the syntax is error-free, the displayed parameter is black.
- If there is an error in the syntax, the cursor stays in the input field and a corresponding error message is displayed in the inspector window in the "Info > Syntax" register.

---

**See also**

[Using and addressing operands](Programming%20basics.md#using-and-addressing-operands)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Wiring hidden parameters

#### Introduction

If an instruction contains hidden parameters, the instruction box has a small arrow on the lower edge. You can recognize hidden parameters by their white font.

You can show and wire the hidden parameters at any time.

#### Showing or hiding hidden parameters

To show or hide hidden parameters, follow these steps:

1. Click on the down arrow at the bottom edge of the instruction box to show hidden parameters.
2. Click on the up arrow at the bottom edge of the instruction box to hide hidden parameters.

#### Wiring hidden parameters

To wire parameters, follow these steps:

1. Wire the hidden parameters like normally visible parameters.

   Its visibility may change due to the interconnection of the parameter:

   - The parameter is visible if you have selected the "Hide, if no parameter is assigned" option in the properties.
   - The parameter remains hidden if you have selected the "Hide" option in the properties.

---

**See also**

[Hiding parameters during the block call](Declaring%20the%20block%20interface.md#hiding-parameters-during-the-block-call)
  
[Library basics](Using%20libraries.md#library-basics)

### Displaying or hiding tag information

#### Introduction

You can display the following information about the tags to be used in the Program editor:

- Name of the tag
- Tag addresses
- Simple or hierarchical comments to document the tags

The information is taken from the block interface for local tags and DB tags and from the PLC tag table for tags that are valid CPU-wide.

You can display the tag information either for all the blocks or for individually opened blocks. If you display the tag information for all the blocks, the tag information for all the blocks currently opened and opened in future is shown. You can hide the tag information at any time again. If you have hidden the tag information for all blocks, you can display it again for individual blocks that are open.

When you select the display of tag information with hierarchical comments, the comments of the higher structure levels are also displayed for structured tags. The comments are shown in brackets after the tag comment; the comments of the individual levels are separated by a dot. If there is no comment for a tag on a structure level, it is not displayed. This is indicated by two successive dots.

You can display the tag information either collectively below a LAD/FBD network or directly at the respective operand. As with showing and hiding tag information, you can set this via the settings for all block or change specifically for an opened block.

#### Displaying or hiding tag information for all the blocks

Proceed as follows to display or hide the tag information for all the blocks:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "PLC programming" group.
3. If you want to display the tag information, select the "Show" option or the "Tag information with hierarchical comments" option in the drop-down list, depending on whether you want to display simple or hierarchical comments.
4. Use the "Position of the tag information (LAD/FBD)" drop-down list to specify whether the tag information is to be displayed below the LAD/FBD network or on the operand.

   For all open blocks, the tag information is shown and displayed at the selected position. If you open additional blocks the tag information for these blocks is also shown.
5. If you want to hide the tag information, select the option "Hide" in the "Tag information" drop-down list.

   The tag information is hidden for all open blocks. If you open additional blocks the tag information for these blocks is also hidden.

#### Displaying or hiding tag information for an opened block

Proceed as follows to display or hide the tag information for an opened block:

1. If you want to display the tag information, select the "Show tag information" option or the "Tag information with hierarchical comments" option in the "Shows the tag information" drop-down list, depending on whether you want to display simple or hierarchical comments.
2. To define the position of the tag information, click the "Position of the tag information (LAD/FBD)" button in the program editor toolbar. The position changes with each click on the button. Alternatively, you can click the small arrow beside the "Position of the tag information (LAD/FBD)" button to open the drop-down list. Than select the position from the drop-down list.

   The tag information is shown and displayed at the selected position.
3. If you want to hide the tag information, select the option "Hide tag information" in the "Shows the tag information" drop-down list.

   The tag information is hidden.

## Branches in FBD

This section contains information on the following topics:

- [Basic information on branches in FBD](#basic-information-on-branches-in-fbd)
- [Rules for branches in FBD](#rules-for-branches-in-fbd)
- [Inserting branches in FBD networks](#inserting-branches-in-fbd-networks)
- [Deleting branches in FBD networks](#deleting-branches-in-fbd-networks)

### Basic information on branches in FBD

#### Definition

You can use the Function Block Diagram (FBD) programming language to program parallel branches. This is done using branches that are inserted between the boxes. You can insert additional boxes within the branch and in this way build up complex function block diagrams.

The figure below shows an example of the use of branches:

![Definition](images/14422831499_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Rules for branches in FBD](#rules-for-branches-in-fbd)
  
[Inserting branches in FBD networks](#inserting-branches-in-fbd-networks)
  
[Deleting branches in FBD networks](#deleting-branches-in-fbd-networks)

### Rules for branches in FBD

#### Rules

The following rules apply to the use of branches in FBD:

- Branches are opened downward.
- Branches can be inserted only between FBD elements.
- To delete a branch, you must delete all FBD elements, including the branch itself.
- If you delete the connection between two branches, the FBD elements of the interrupted branch will be positioned freely in the network.

---

**See also**

[Basic information on branches in FBD](#basic-information-on-branches-in-fbd)
  
[Inserting branches in FBD networks](#inserting-branches-in-fbd-networks)
  
[Deleting branches in FBD networks](#deleting-branches-in-fbd-networks)

### Inserting branches in FBD networks

#### Requirement

A network is available.

#### Procedure

To insert a new branch in a network, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "General > Branch" in the "Basic instructions" palette.
3. Drag the element from the "Elements" pane to the a required location on a connection line between two boxes.

---

**See also**

[Rules for branches in FBD](#rules-for-branches-in-fbd)
  
[Basic information on branches in FBD](#basic-information-on-branches-in-fbd)
  
[Deleting branches in FBD networks](#deleting-branches-in-fbd-networks)

### Deleting branches in FBD networks

#### Requirement

A branch is available.

#### Procedure

To delete a branch, follow these steps:

1. Select the connection line that links the branch to the main branch.
2. Select the "Delete" command in the shortcut menu.

#### Result

The branch is now deleted. Boxes connected to the deleted branch are placed freely within the network.

---

**See also**

[Rules for branches in FBD](#rules-for-branches-in-fbd)
  
[Basic information on branches in FBD](#basic-information-on-branches-in-fbd)
  
[Inserting branches in FBD networks](#inserting-branches-in-fbd-networks)

## Logic paths in FBD

This section contains information on the following topics:

- [Basic information on logic paths in FBD](#basic-information-on-logic-paths-in-fbd)
- [Inserting a logic path](#inserting-a-logic-path)
- [Deleting a logic operation path](#deleting-a-logic-operation-path)

### Basic information on logic paths in FBD

#### Use of logic paths

The user program will be mapped in one or more networks. The networks can contain one or more logic paths on which the binary signals are arranged in the form of boxes.

The following figure shows an example of the use of several logic paths within a network:

![Use of logic paths](images/13490705291_DV_resource.Stream@PNG-en-US.png)

#### Rules

Remember the following rules when using logic paths:

- Connections are not permitted between logic paths.
- Only one jump instruction is permissible per network. The positioning rules for jump instructions remain valid.

#### Executing logic paths

Logic paths are executed from top to bottom and from left to right. This means that the first instruction in the first logic path of the first network is executed first. All instructions of this logic path are then executed. After this come all other logic paths of the first network. The next network is executed only after all logic paths have first been executed.

When jumps are used the regular execution of the logic paths is circumvented and the instruction is executed at the jump destination.

#### Differences between branches and logic paths

The difference between branches and logic paths is that the logic paths are independent branches that can also stand in a different network. Branches, on the other hand, permit the programming of a parallel connection and have a common preceding logic operation.

---

**See also**

[Inserting a logic path](#inserting-a-logic-path)
  
[Deleting a logic operation path](#deleting-a-logic-operation-path)

### Inserting a logic path

#### Requirement

- A block is open.
- A network is available.

#### Procedure

To insert a new logic path in a network, follow these steps:

1. Insert any instruction in a network in such a way that it has no connection to existing instructions.

   A new logic path is inserted.
2. Insert an assignment at the end of the new logic path.
3. Insert additional instructions in the new logic path.

---

**See also**

[Basic information on logic paths in FBD](#basic-information-on-logic-paths-in-fbd)
  
[Deleting a logic operation path](#deleting-a-logic-operation-path)

### Deleting a logic operation path

#### Requirement

A logic path is available.

#### Procedure

To delete a logic path, proceed as follows:

1. Hold down the left mouse button and draw a frame around the logic path. At the same time, make sure that you select all instructions of the logic path. Alternatively, you can hold down the <Shift> key and select the first the last instruction of the logic path.
2. Right-click on one of the instructions in the logic path.
3. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on logic paths in FBD](#basic-information-on-logic-paths-in-fbd)
  
[Inserting a logic path](#inserting-a-logic-path)

## FBD programming examples

This section contains information on the following topics:

- [Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt)
- [Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
- [Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area)
- [Example of calculating an equation](#example-of-calculating-an-equation)
- [Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of controlling a conveyor belt

#### Controlling a conveyor belt

The following figure shows a conveyor belt that can be activated electrically. There are two pushbuttons at the beginning of the conveyor belt: S1 for START and S2 for STOP. There are also two pushbuttons at the end of the conveyor belt: S3 for START and S4 for STOP. It is possible to start and stop the conveyor belt from either end.

![Controlling a conveyor belt](images/70908454283_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Description |
| --- | --- | --- | --- |
| StartPushbutton_Left (S1) | Input | BOOL | Start pushbutton on the left side of the conveyor belt |
| StopPushbutton_Left (S2) | Input | BOOL | Stop pushbutton on the left side of the conveyor belt |
| StartPushbutton_Right (S3) | Input | BOOL | Start pushbutton on the right side of the conveyor belt |
| StopPushbutton_Right (S4) | Input | BOOL | Stop pushbutton on the right side of the conveyor belt |
| MOTOR_ON | Output | BOOL | Turn on the conveyor belt motor |

The following networks show the FBD programming for solving this task:

Network 1:

The conveyor belt motor is switched on when start pushbutton "S1" or "S3" is pressed.

![Implementation](images/70908725643_DV_resource.Stream@PNG-en-US.png)

Network 2:

The conveyor belt motor is switched off when stop pushbutton "S2" or "S4" is pressed.

![Implementation](images/70909217163_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on FBD](#basic-information-on-fbd)
  
[Settings for FBD](#settings-for-fbd)
  
[Working with networks](#working-with-networks)
  
[Inserting FBD elements](#inserting-fbd-elements)
  
[Editing FBD elements](#editing-fbd-elements)
  
[Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
  
[Branches in FBD](#branches-in-fbd)
  
[Logic paths in FBD](#logic-paths-in-fbd)
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area) 
  
[Example of calculating an equation](#example-of-calculating-an-equation)
  
[Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of detecting the direction of a conveyor belt

#### Detecting the direction of a conveyor belt

The detected running direction of the belt is indicated by a RIGHT arrow or a LEFT arrow. If additional conveyed material is approaching PEB1 from the right or PEB2 from the left, the displayed arrow is initially switched off until, after both photoelectric barriers are passed, the running direction can be detected again and the corresponding arrow displayed. For the solution of the task, 2 edge memory bits are needed that detect the signal change from "0" to "1" at the two photoelectric barriers.

![Detecting the direction of a conveyor belt](images/41375220491_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Description |
| --- | --- | --- | --- |
| PEB1 | Input | BOOL | Photoelectric barrier 1 |
| PEB2 | Input | BOOL | Photoelectric barrier 2 |
| RIGHT | Output | BOOL | Display during movement to right |
| LEFT | Output | BOOL | Display during movement to left |
| CM1 | Input | BOOL | Edge bit memory 1 |
| CM2 | Input | BOOL | Edge bit memory 2 |

The following networks show the FBD programming for solving this task:

Network 1:

If the signal state changes from "0" to "1" (positive edge) at photoelectric barrier "PEB1" and, at the same time, the signal state at "PEB2" is "0", the object on the belt is moving to the left.

![Implementation](images/70910992139_DV_resource.Stream@PNG-en-US.png)

Network 2:

If the signal changes from "0" to "1" (positive edge) at photoelectric barrier "PEB2" and, at the same time, the signal state at "PEB1" is "0", the object on the belt is moving to the right.

![Implementation](images/70911162635_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on FBD](#basic-information-on-fbd)
  
[Settings for FBD](#settings-for-fbd)
  
[Working with networks](#working-with-networks)
  
[Inserting FBD elements](#inserting-fbd-elements)
  
[Editing FBD elements](#editing-fbd-elements)
  
[Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
  
[Branches in FBD](#branches-in-fbd)
  
[Logic paths in FBD](#logic-paths-in-fbd)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area) 
  
[Example of calculating an equation](#example-of-calculating-an-equation)
  
[Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of detecting the fill level of a storage area

#### Detecting the fill level of a storage area

The following figure shows a system with two conveyor belts and a temporary storage area between them. Conveyor belt 1 delivers packages to the storage area. A photoelectric barrier at the end of conveyor belt 1 near the storage area detects how many packages are delivered to the storage area. Conveyor belt 2 transports packages from the temporary storage area to a loading dock where they are loaded onto trucks. A photoelectric barrier at the storage area exit detects how many packages leave the storage area to be transported to the loading dock. Five display lamps indicate the capacity of the temporary storage area.

![Detecting the fill level of a storage area](images/41381535883_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Description |
| --- | --- | --- | --- |
| PEB1 | Input | BOOL | Photoelectric barrier 1 |
| PEB2 | Input | BOOL | Photoelectric barrier 2 |
| RESET | Input | BOOL | Reset counter |
| LOAD | Input | BOOL | Adjust the current counter value to the value of the PV parameter​. |
| MAX STORAGE AREA FILL AMOUNT | Input | INT | Maximum possible number of packages in the storage area |
| PACKAGECOUNT | Output | INT | Number of packages in the storage area (current count value) |
| STOCK_PACKAGES | Output | BOOL | Is set when the current count value is greater than or equal to the value of the "MAX STORAGE AREA FILL AMOUNT" tag. |
| STOR_EMPTY | Output | BOOL | Display lamp: Storage area empty |
| STOR_NOT_EMPTY | Output | BOOL | Display lamp: Storage area not empty |
| STOR_50%_FULL | Output | BOOL | Display lamp: Storage area 50 % full |
| STOR_90%_FULL | Output | BOOL | Display lamp: Storage area 90 % full |
| STOR_FULL | Output | BOOL | Display lamp: Storage area full |
| VOLUME_50 | Input | INT | Comparison value: 50 packages |
| VOLUME_90 | Input | INT | Comparison value: 90 packages |
| VOLUME_100 | Input | INT | Comparison value: 100 packages |

The following networks show the FBD programming for activating the lamps:

Network 1:

When a package is delivered to the storage area, the signal state at "PEB1" switches from "0" to "1" (positive signal edge). On a positive signal edge at "PEB1", the "Up" counter is enabled, and the current count value of "PACKAGECOUNT" is increased by one.

When a package is delivered from the storage area to the loading dock, the signal state at "PEB2" switches from "0" to "1" (positive signal edge). On a positive signal edge at "PEB2", the "Down" counter is enabled, and the current count value of "PACKAGECOUNT" is decreased by one.

If there are no packages in the storage area ("PACKAGECOUNT" = "0"), the "STOR_EMPTY" tag is set to signal state "1", and the "Storage area empty" lamp is switched on.

The current count value can be reset to "0" if the "RESET" tag is set to signal state "1".

If the "LOAD" tag is set to signal state "1", the current count value is set to the value of the "MAX STORAGE AREA FILL AMOUNT" tag. As long as the current count value is greater than or equal to the value of the "MAX STORAGE AREA FILL AMOUNT" tag, the "STOCK_PACKAGES" tag supplies the signal state "1".

![Implementation](images/70935833483_DV_resource.Stream@PNG-en-US.png)

Network 2:

As long as there are packages in the storage area, the "STOR_NOT_EMPTY" tag is set to signal state "1", and the "Storage area not empty" lamp is switched on.

![Implementation](images/70913497227_DV_resource.Stream@PNG-en-US.png)

Network 3:

If the number of packages in the storage area is greater than or equal to 50, the "Storage area 50 % full" lamp switches on.

![Implementation](images/70912938635_DV_resource.Stream@PNG-en-US.png)

Network 4:

If the number of packages in the storage area is greater than or equal to 90, the "Storage area 90% full" lamp switches on.

![Implementation](images/70913493131_DV_resource.Stream@PNG-en-US.png)

Network 5:

If the number of packages in the storage area reaches 100, the lamp for the "Storage area full" message switches on.

![Implementation](images/70912934539_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on FBD](#basic-information-on-fbd)
  
[Settings for FBD](#settings-for-fbd)
  
[Working with networks](#working-with-networks)
  
[Inserting FBD elements](#inserting-fbd-elements)
  
[Editing FBD elements](#editing-fbd-elements)
  
[Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
  
[Branches in FBD](#branches-in-fbd)
  
[Logic paths in FBD](#logic-paths-in-fbd)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of calculating an equation](#example-of-calculating-an-equation)
  
[Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of calculating an equation

#### Calculating a complex equation

The following program example shows you how to solve equations of the following type with the FBD programming language:

X= ((A + B) x C) / D

You can always solve this equation with mathematical operations. To do so, you can use the instructions "ADD", "MUL" and "DIV". If you are using a CPU of the S7-1200 or S7-1500 series, you can also use the instruction "CALCULATE". Depending on the data type you choose, different mathematical operations are available for this instruction which can be combined with one another.

#### Implementation with the instructions "ADD", "MUL" and "DIV"

You want to calculate the following equation:

RESULT = ((A + B) x 15) / E

The following table shows the definition of the tags used:

| Name | Data type | Comment |
| --- | --- | --- |
| A | INT | First value for addition |
| B | INT | Second value for addition |
| C | INT | First intermediate result |
| 15 | INT | Multiplier |
| D | INT | Second intermediate result |
| E | INT | Divisor |
| RESULT | INT | End result |

The following network shows the FBD programming for calculating the equation:

![Implementation with the instructions "ADD", "MUL" and "DIV"](images/12898740747_DV_resource.Stream@PNG-en-US.png)

The value of operand "A" is added to the value of operand "B". The sum is stored in operand "C". The value of operand "C" is multiplied by "15". The multiplication result is stored in operand "D". The value stored in operand "D" is then divided by the value of operand "E". The end result is saved in the "RESULT" operand.

#### Implementation with the instruction "CALCULATE" (S7-1200/1500 only)

You want to calculate the following equation:

RESULT = ((5 + 10) x 4) / 6

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Comment | Value |
| --- | --- | --- | --- | --- |
| A | Input | INT | First value for addition | 5 |
| B | Input | INT | Second value for addition | 10 |
| C | Input | INT | Multiplier | 4 |
| D | Input | INT | Divisor | 6 |
| RESULT | Output | INT | End result | 10 |

To program the equation with the instruction "CALCULATE", follow these steps:

1. Drag the instruction "CALCULATE" from the "Instructions" task card to an FBD network.
2. You can select the data type INT for the instruction from the "<???>" drop-down list.
3. Interconnect the tags declared in the block interface with the inputs and outputs of the instruction box.
4. Click the "Calculator" icon on the top right corner of the instruction box to enter the equation to be calculated.

   The dialog "Edit 'Calculate' instruction" opens.
5. Enter the following expression in the "OUT:=" field:

   ((IN1 + IN2) * IN4) / IN3

   The equation is displayed in the instruction box.

   The following network shows the result in the FBD programming language:

   ![Implementation with the instruction "CALCULATE" (S7-1200/1500 only)](images/65854484747_DV_resource.Stream@PNG-de-DE.png)

   ![Implementation with the instruction "CALCULATE" (S7-1200/1500 only)](images/65854484747_DV_resource.Stream@PNG-de-DE.png)

   If the "Tag_Input" has signal state "1", the instruction is executed. The value of operand "A" is added to the value of operand "B". The subtotal is multiplied by "C" and then divided by the value of the "D" operand. The end result is saved in the "RESULT" operand.

---

**See also**

[Basic information on FBD](#basic-information-on-fbd)
  
[Settings for FBD](#settings-for-fbd)
  
[Working with networks](#working-with-networks)
  
[Inserting FBD elements](#inserting-fbd-elements)
  
[Editing FBD elements](#editing-fbd-elements)
  
[Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
  
[Branches in FBD](#branches-in-fbd)
  
[Logic paths in FBD](#logic-paths-in-fbd)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area) 
  
[Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of controlling room temperature

#### Controlling room temperature

In a cold room, the temperature must be maintained below zero degrees Celsius. A sensor is used to check for any temperature fluctuations. If the temperature rises above zero degrees Celsius, the cooling system switches on for a preset time. The "Cooling system on" lamp is lit during this time.

The cooling system and the lamp are turned off if one of the following conditions is met:

- The sensor reports a temperature fall below zero degrees Celsius.
- The preset cooling time has elapsed.
- The "Stop" pushbutton is pressed.

If the preset cooling time has expired and the temperature in the cold room is still too high, the cooling system can be restarted with the "RESET" pushbutton.

![Controlling room temperature](images/70916762891_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Comment |
| --- | --- | --- | --- |
| Sensor | Input | BOOL | Temperature sensor signal |
| RESET | Input | BOOL | Restart |
| STOP | Input | BOOL | The cooling system is switched off. |
| MaxCoolTime | - | TIME | Preset cooling time  This tag is defined in the "DB_Cool" data block. |
| CurrCoolTime | - | TIME | Currently elapsed cooling time  This tag is defined in the "DB_Cool" data block. |
| Cooling system | Output | BOOL | The cooling system is switched on. |
| Lamp | Output | BOOL | The lamp for the "Cooling system on" message is switched on. |
| TempVariable | Temp | BOOL | Temporary tag  This tag stores the signal state of the IEC timer TP. |

The following network shows the FBD programming for controlling room temperature:

Network 1:

![Implementation](images/28098473867_DV_resource.Stream@PNG-en-US.png)

Network 2:

![Implementation](images/70916766987_DV_resource.Stream@PNG-en-US.png)

When the temperature in the cold room rises above zero degrees Celsius, the signal state at the "Sensor" operand switches from "0" to "1" (positive signal edge). In the case of a positive signal edge at the IN input of the timer function, the preset cooling time is started and the "TempVariable" receives the signal state "1". The signal state "1" of the "TempVariable" causes the cooling system as well as the display lamp to be turned on in network 2. The "Sensor", "Cooling system" and "Lamp" outputs must be programmed in network 2, because program only one coil can be programmed at the Q output of the timer function.

If the temperature in the cold room falls below zero degrees Celsius, the signal state of the sensor switches back to "0". This switches the cooling system and lamp off.

If the sensor does not signal a temperature drop, the cooling system and lamp are switched off after the preset cooling time has elapsed, at the latest. In this case, the cooling process can be restarted with the "RESET" pushbutton. Pressing and releasing the pushbutton generates a new positive signal edge at the IN input that restarts the cooling system.

The cooling system and the display lamp can be turned off with the "STOP" pushbutton at any time.

---

**See also**

[Basic information on FBD](#basic-information-on-fbd)
  
[Settings for FBD](#settings-for-fbd)
  
[Working with networks](#working-with-networks)
  
[Inserting FBD elements](#inserting-fbd-elements)
  
[Editing FBD elements](#editing-fbd-elements)
  
[Inserting operands in FBD instructions](#inserting-operands-in-fbd-instructions)
  
[Branches in FBD](#branches-in-fbd)
  
[Logic paths in FBD](#logic-paths-in-fbd)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area) 
  
[Example of calculating an equation](#example-of-calculating-an-equation)

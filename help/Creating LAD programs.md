---
title: "Creating LAD programs"
package: ProgBlockKOPenUS
topics: 75
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating LAD programs

This section contains information on the following topics:

- [Basic information on LAD](#basic-information-on-lad)
- [Settings for LAD](#settings-for-lad)
- [Working with networks](#working-with-networks)
- [Inserting LAD elements](#inserting-lad-elements)
- [Editing LAD elements](#editing-lad-elements)
- [Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
- [Branches in LAD](#branches-in-lad)
- [Crossings in LAD](#crossings-in-lad)
- [Rungs in LAD](#rungs-in-lad)
- [LAD programming examples](#lad-programming-examples)

## Basic information on LAD

This section contains information on the following topics:

- [LAD programming language](#lad-programming-language)
- [Overview of the LAD elements](#overview-of-the-lad-elements)

### LAD programming language

#### Overview of the Ladder Logic (LAD) programming language

LAD is a graphical programming language. The representation is based on circuit diagrams.

The program is mapped in one or more networks. A network contains a power rail on the left where the rungs originate. The binary signal scans are arranged in the form of contacts on the rungs. The serial arrangement of the elements on a rung creates a series connection; arrangement on simultaneous branches creates a parallel connection. Complex functions are represented by boxes.

#### Example of networks in LAD

The following figure shows a LAD network with two normally open contacts, one normally closed contact and one coil:

![Example of networks in LAD](images/63691973899_DV_resource.Stream@PNG-en-US.png)

### Overview of the LAD elements

#### LAD elements

A LAD program consists of separate elements that you can arrange in series or parallel on the power rail of a network. Most program elements must be supplied with tags.

There is at least one rung from the power rail. Network programming starts at the left edge of the rung. You can expand the power rail by several rungs and branches.

For example, the following figure shows elements of a LAD network:

![LAD elements](images/13956468875_DV_resource.Stream@PNG-en-US.png)

1) Power rail

2) Rung

3) Branch

4) Contact

5) Coil

6) Box

#### Power rail

Each LAD network consists of a power rail that contains at least one rung. A network can be extended by adding additional rungs. You can use branches to program parallel connections in the specific rungs.

#### Contacts

You can use contacts to create or interrupt a current-carrying connection between two elements. The current is relayed from left to right. You can use contacts to query the signal state or the value of an operand and control it depending on the result of the current flow.

The following types of contact are available to you in a LAD program:

- Normally open contact:   
  Normally open contacts forward the current if the signal state of a specified binary operand is "1".
- Normally closed contacts:   
  Normally closed contacts forward the current if the signal state of a specified binary operand is "0".
- Contact with additional function:   
  Contacts with additional function forward the current if a specific condition is met. With these contacts you can also execute an additional function, such as an RLO edge detection and a comparison.

#### Coils

You can use coils to control binary operands. Coils can set or reset a binary operand depending on the signal state of the result of logic operation.

The following types of coils are available to you in a LAD program:

- Standard coils:   
  Standard coils set a binary operand if current flows in the coil. The "Assignment" instruction is an example of a standard coil.
- Coils with additional function:  
  These coils have additional functions in addition to the evaluation of the logic operation result. Coils for RLO edge detection and program control are examples of coils with additional function.

#### Boxes

Boxes are LAD elements with complex functions. The empty box is an exception. You can use the empty box as a placeholder in which you can select the required instruction.

The following types of boxes are available to you in a LAD program:

- Boxes without EN/ENO mechanism:  
  A box is executed depending on the signal state at the box inputs. The error status of the processing cannot be queried.
- Boxes with EN/ENO mechanism:  
  A box is only executed if the enable input "EN" carries the signal state "1". If the box is processed correctly, the "ENO" enable output has signal state "1". If an error occurs during the processing, the "ENO" enable output is reset.

Calls of code block are also shown in the network as boxes with EN/ENO mechanism.

---

**See also**

[Rules for the use of LAD elements](#rules-for-the-use-of-lad-elements)
  
[EN/ENO mechanism](Programming%20basics.md#eneno-mechanism)

## Settings for LAD

This section contains information on the following topics:

- [Overview of the settings for LAD](#overview-of-the-settings-for-lad)
- [Changing the settings](#changing-the-settings)

### Overview of the settings for LAD

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

[Overview of the settings for LAD](#overview-of-the-settings-for-lad)

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

[Inserting networks](#inserting-networks)
  
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

[Using networks](#using-networks)
  
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

1. Press and hold down the &lt;Ctrl&gt; key.
2. Click all the networks that you want to select.

To select several successive networks, follow these steps:

1. Press and hold down the &lt;Shift&gt; key.
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

1. Right-click "Network &lt;Number of the network&gt;" in the title bar of a network.
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
2. Select the "Go to &gt; Network/line" command in the shortcut menu.

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

## Inserting LAD elements

This section contains information on the following topics:

- [Rules for the use of LAD elements](#rules-for-the-use-of-lad-elements)
- [Prohibited interconnections in LAD](#prohibited-interconnections-in-lad)
- [Inserting LAD elements using the "Instructions" task card](#inserting-lad-elements-using-the-instructions-task-card)
- [Inserting LAD elements using an empty box](#inserting-lad-elements-using-an-empty-box)
- [Selecting the data type of a LAD element](#selecting-the-data-type-of-a-lad-element)
- [Using favorites in LAD](#using-favorites-in-lad)
- [Insert block calls in LAD](#insert-block-calls-in-lad)
- [Inserting complex LAD instructions](#inserting-complex-lad-instructions)
- [Using free-form comments](#using-free-form-comments)

### Rules for the use of LAD elements

#### Rules

Note the following rules when inserting LAD elements:

- Every LAD network must terminate with a coil or a box. However, the following LAD elements must not be used to terminate a network:

  - Comparator boxes
  - Instructions for positive and negative RLO edge detection
- The starting point of the branch for a box connection must always be the power rail. Logic operations or other boxes can be present in the branch before the box.
- Only contacts can be inserted into simultaneous branches with preceding logic operations. The contact for negating the result of logic operation (-|NOT|-) is an exception here. The contact for negating the result of logic operation, as well as coils and boxes, can be used in simultaneous branches if they originate directly from the power rail.
- Constants (e.g. TRUE or FALSE) cannot be assigned to normally closed or normally open contacts. Instead, use operands of the BOOL data type.
- Only one jump instruction can be inserted in each network.
- Only one jump label can be inserted in each network.
- Instructions with positive or negative edge detection may not be arranged directly at the left margin of the rung as they requires a prior logic operation.

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
| MCR&lt; | Open MCR ranges | No |
| MCR&gt; | Close MCR ranges | No |

> **Note**
>
> **Calling blocks with binary inputs in S7-300/400 CPUs**
>
> The following FAQ describes the special features when calling blocks with binary inputs:
>
> [FAQ 13988019: What should you watch out for when programming nested FB/FC calls with binary inputs in FBD?](#prohibited-interconnections-in-lad)

---

**See also**

[Overview of the LAD elements](#overview-of-the-lad-elements)
  
[FAQ 13988019](https://support.industry.siemens.com/cs/de/de/view/13988019)
  
[EN/ENO mechanism](Programming%20basics.md#eneno-mechanism)

### Prohibited interconnections in LAD

#### Power flow from right to left

No branches can be programmed that could result in a power flow in the reverse direction.

![Power flow from right to left](images/63692584587_DV_resource.Stream@PNG-en-US.png)

#### Short-circuit

No branches may be programmed that would cause a short-circuit.

![Short-circuit](images/63692614283_DV_resource.Stream@PNG-en-US.png)

#### Logic operations

The following rules apply to logic operations:

- Only Boolean inputs can be combined with preceding logic operations.
- Only the first Boolean output can be combined with a further logic operation.
- Only one complete logical path can exist per network. Paths that are not connected can be linked.

---

**See also**

[Rules for the use of LAD elements](#rules-for-the-use-of-lad-elements)

### Inserting LAD elements using the "Instructions" task card

#### Requirement

A network is available.

#### Procedure

To insert a LAD element into a network using the "Instructions" task card, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to the LAD element that you want to insert.
3. Use drag-and-drop to move the element to the desired place in the network.

   If the element is an internal system function block (FB), the "Call options" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks &gt; System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

Or:

1. Select the point in the network at which you want to insert the element.
2. Open the "Instructions" task card.
3. Double-click on the element you want to insert.

   If the element is an internal system function block (FB), the "Call options" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks &gt; System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

#### Result

The selected LAD element is inserted with placeholders for the parameters.

---

**See also**

[Inserting LAD elements using an empty box](#inserting-lad-elements-using-an-empty-box)
  
[Inserting LAD elements using favorites](#inserting-lad-elements-using-favorites)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)
  
[Parameter instances](Programming%20basics.md#parameter-instances)

### Inserting LAD elements using an empty box

#### Requirement

A network is available.

#### Procedure

To insert an LAD element into a network using an empty box, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "General &gt; Empty box" in the "Basic instructions" palette.
3. Use a drag-and-drop operation to move the "Empty box" element to the desired place in the network.
4. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
5. Select the required LAD element from the drop-down list.

   If the element is an internal system function block (FB), the "Call option" dialog opens. In this dialog, you can determine if the data of the inserted element is to be stored in a single, multi or parameter instance. If you select "Single instance", you can find the new instance data block once it is created in the "Program resources" folder of the project tree under "Program blocks &gt; System blocks". You can find multi-instances in the block interface in the "Static" section and parameter instances in the "InOut" section.

#### Result

The empty box is changed to the respective LAD element. Placeholders are inserted for the parameters.

---

**See also**

[Inserting LAD elements using the "Instructions" task card](#inserting-lad-elements-using-the-instructions-task-card)
  
[Inserting LAD elements using favorites](#inserting-lad-elements-using-favorites)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)
  
[Parameter instances](Programming%20basics.md#parameter-instances)

### Selecting the data type of a LAD element

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

Some mathematical instructions provide you with the option of having the data type automatically set corresponding to the data types of the operand. In the drop-down list for data type selection, these instructions have the entry "Auto" in addition to the actual data types. If you select this entry and then allocate the first operand, the data type of the operand is selected as data type for the instruction. The entry in the drop-down list changes to "Auto (&lt;Data type&gt;)", e.g. "Auto (Real)". If you allocate additional operands, the automatically set data type of the instruction is adjusted according to the following criteria:

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

   The data type of the tag is applied as data type of the instruction. The entry in the drop-down list changes to "Auto (&lt;Data type&gt;)".

See also: [Selecting a data type](#selecting-a-data-type)

---

**See also**

[Selecting a data type](#selecting-a-data-type)

### Using favorites in LAD

This section contains information on the following topics:

- [Adding LAD elements to Favorites](#adding-lad-elements-to-favorites)
- [Inserting LAD elements using favorites](#inserting-lad-elements-using-favorites)
- [Removing LAD elements from Favorites](#removing-lad-elements-from-favorites)

#### Adding LAD elements to Favorites

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

[Inserting LAD elements using favorites](#inserting-lad-elements-using-favorites)
  
[Removing LAD elements from Favorites](#removing-lad-elements-from-favorites)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

#### Inserting LAD elements using favorites

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

[Adding LAD elements to Favorites](#adding-lad-elements-to-favorites)
  
[Inserting LAD elements using the "Instructions" task card](#inserting-lad-elements-using-the-instructions-task-card)
  
[Inserting LAD elements using an empty box](#inserting-lad-elements-using-an-empty-box)
  
[Removing LAD elements from Favorites](#removing-lad-elements-from-favorites)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

#### Removing LAD elements from Favorites

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

[Adding LAD elements to Favorites](#adding-lad-elements-to-favorites)
  
[Inserting LAD elements using favorites](#inserting-lad-elements-using-favorites)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

### Insert block calls in LAD

This section contains information on the following topics:

- [Inserting block calls using a drag-and-drop operation](#inserting-block-calls-using-a-drag-and-drop-operation)
- [Updating block calls in LAD](#updating-block-calls-in-lad)
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

[Updating block calls in LAD](#updating-block-calls-in-lad)
  
[Changing the instance type](#changing-the-instance-type)
  
[Single instances](Programming%20basics.md#single-instances)
  
[Multi-instances](Programming%20basics.md#multi-instances)
  
[Block calls](Programming%20basics.md#block-calls)

#### Updating block calls in LAD

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
3. Select the command "Compile &gt; Software (rebuild all blocks)" in the shortcut menu.

---

**See also**

[Inserting block calls using a drag-and-drop operation](#inserting-block-calls-using-a-drag-and-drop-operation)
  
[Changing the instance type](#changing-the-instance-type)
  
[Block calls](Programming%20basics.md#block-calls)

#### Changing the block call

You have the option of changing the called block for a block call. But keep in mind that no new instance data blocks are created, for example, when changing from a function (FC) to a function block (FB).

##### Procedure

To change the called block of a block call, follow these steps:

1. Click on the name of the called block within the block call and press the &lt;F2&gt; key. Or double-click the name of the called block.

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
  
[Updating block calls in LAD](#updating-block-calls-in-lad)
  
[Instances](Programming%20basics.md#instances)
  
[Block calls](Programming%20basics.md#block-calls)

### Inserting complex LAD instructions

This section contains information on the following topics:

- [Using the "Calculate" instruction (S7-1200, S7-1500)](#using-the-calculate-instruction-s7-1200-s7-1500)

#### Using the "Calculate" instruction (S7-1200, S7-1500)

##### Requirement

A network is available.

##### Procedure

Proceed as follows to use the "Calculate" instruction:

1. Open the "Instructions" task card.
2. Navigate to "Math functions &gt; CALCULATE" in the "Basic instructions" pane.
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

[CALCULATE: Calculate (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#calculate-calculate-s7-1200-s7-1500)

### Using free-form comments

This section contains information on the following topics:

- [Basic information on using free-form comments in LAD](#basic-information-on-using-free-form-comments-in-lad)
- [Inserting free-form comments](#inserting-free-form-comments)
- [Editing free-form comments](#editing-free-form-comments)
- [Deleting free-form comments](#deleting-free-form-comments)

#### Basic information on using free-form comments in LAD

##### Introduction

Free-form comments allow you to add comments to the source code for graphic programming languages similar to line comments for textual languages.

Free-form comments can be used for the following elements:

- Boxes
- Coils

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

[Basic information on using free-form comments in LAD](#basic-information-on-using-free-form-comments-in-lad)
  
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

[Basic information on using free-form comments in LAD](#basic-information-on-using-free-form-comments-in-lad)
  
[Inserting free-form comments](#inserting-free-form-comments)
  
[Deleting free-form comments](#deleting-free-form-comments)

#### Deleting free-form comments

##### Procedure

To delete a free-form comment, proceed as follows:

1. Right-click on the free-form comment that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on using free-form comments in LAD](#basic-information-on-using-free-form-comments-in-lad)
  
[Inserting free-form comments](#inserting-free-form-comments)
  
[Editing free-form comments](#editing-free-form-comments)

## Editing LAD elements

This section contains information on the following topics:

- [Selecting LAD elements](#selecting-lad-elements)
- [Copying LAD elements](#copying-lad-elements)
- [Cutting LAD elements](#cutting-lad-elements)
- [Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
- [Replacing LAD elements](#replacing-lad-elements)
- [Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
- [Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
- [Deleting LAD elements](#deleting-lad-elements)

### Selecting LAD elements

You can select several individual elements or all elements in a network.

#### Requirement

LAD elements are available

#### Selecting several individual LAD elements

To select several individual LAD elements, follow these steps:

1. Press and hold down the &lt;Ctrl&gt; key.
2. Click on all the LAD elements you wish to select.
3. Now release the &lt;Ctrl&gt; key.

#### Selecting all LAD elements in a network

To select all LAD elements in a network, follow these steps:

1. Go to the network whose elements you wish to select.
2. Select the "Select all" command in the "Edit" menu or press &lt;Ctrl A&gt;.

---

**See also**

[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Copying LAD elements

#### Requirement

An LAD element is available.

#### Procedure

To copy a LAD element, follow these steps:

1. Right-click the LAD element that you want to copy.
2. Select "Copy" in the shortcut menu.

#### Result

The LAD element will be copied and saved to the clipboard.

---

**See also**

[Selecting LAD elements](#selecting-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Cutting LAD elements

#### Requirement

An LAD element is available.

#### Cutting

To cut a LAD element, follow these steps:

1. Right-click the LAD element that you want to cut.
2. Select "Cut" in the shortcut menu.

#### Result

The LAD element will be cut and saved to the clipboard.

---

**See also**

[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Pasting an LAD element from the clipboard

#### Requirement

An LAD element is available.

#### Procedure

To paste an LAD element from the clipboard, follow these steps:

1. Copy a LAD element or cut a LAD element.
2. Right-click the point in the network where you want to paste the element.
3. Select "Paste" in the shortcut menu.

---

**See also**

[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Replacing LAD elements

You can easily exchange LAD elements with other LAD elements of the same type. This has the advantage that the parameters are retained and need not be entered again. For example, you can exchange normally open contacts and normally closed contacts or RS FlipFlop and SR FlipFlop.

#### Requirements

A network with at least one LAD element is present.

#### Procedure

To replace an LAD element with another LAD element, follow these steps:

1. Select the LAD element that you want to replace.
2. Position the cursor over the triangle in the top right-hand corner of the LAD element.

   A drop-down list is displayed.
3. From the drop-down list, select the LAD element that you want to use to replace the existing LAD element.

---

**See also**

[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)

#### Introduction

You can expand LAD elements which execute commutative arithmetic instructions by adding additional inputs. Such elements are, for example, the instructions "Add" (ADD) and "Multiply" (MUL). You can expand the MOVE and DEMUX instruction boxes by adding additional outputs.

#### Requirement

An LAD element is available that permits the insertion of additional inputs and outputs.

#### Inserting an additional input

To add an additional input to the box of a LAD element, follow these steps:

1. Right-click on an existing input of the LAD element.
2. Select "Insert input" in the shortcut menu.

   An additional input is added to the box of the LAD element.

Or:

1. Click on the yellow star symbol beside the last input in the instruction box.

   An additional input is added to the box of the LAD element.

#### Inserting an additional output

To add an additional output to the box of a LAD element, follow these steps:

1. Right-click on an existing output of the LAD element.
2. Select "Insert output" from the shortcut menu.

   An additional output is added to the box of the LAD element.

Or:

1. Click on the yellow star symbol beside the last input in the instruction box.

   An additional output is added to the box of the LAD element.

---

**See also**

[Inserting LAD elements](#inserting-lad-elements)
  
[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Removing inputs and outputs (S7-1200, S7-1500)

#### Introduction

Inputs and outputs which you have added to an instruction can be removed.

#### Requirement

An LAD element is available to which you have added additional inputs and outputs.

#### Remove input

To remove an input, follow these steps:

1. Select the input that you want to remove.
2. Select the "Delete" command in the shortcut menu.

   The input of the LAD element is removed.

#### Remove output

To remove an output, follow these steps:

1. Select the output that you want to remove.
2. Select the "Delete" command in the shortcut menu.

   The output of the LAD element will be removed.

---

**See also**

[Inserting LAD elements](#inserting-lad-elements)
  
[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
  
[Deleting LAD elements](#deleting-lad-elements)

### Deleting LAD elements

#### Requirement

An LAD element is available.

#### Procedure

To delete a LAD element, follow these steps:

1. Right-click the LAD element that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Inserting LAD elements](#inserting-lad-elements)
  
[Selecting LAD elements](#selecting-lad-elements)
  
[Copying LAD elements](#copying-lad-elements)
  
[Cutting LAD elements](#cutting-lad-elements)
  
[Pasting an LAD element from the clipboard](#pasting-an-lad-element-from-the-clipboard)
  
[Replacing LAD elements](#replacing-lad-elements)
  
[Inserting additional inputs and outputs in LAD elements (S7-1200, S7-1500)](#inserting-additional-inputs-and-outputs-in-lad-elements-s7-1200-s7-1500)
  
[Removing inputs and outputs (S7-1200, S7-1500)](#removing-inputs-and-outputs-s7-1200-s7-1500)
  
[Enabling and disabling the EN/ENO mechanism in LAD and FBD](Programming%20basics.md#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)

## Inserting operands into LAD instructions

This section contains information on the following topics:

- [Inserting operands](#inserting-operands)
- [Wiring hidden parameters](#wiring-hidden-parameters)
- [Displaying or hiding tag information](#displaying-or-hiding-tag-information)

### Inserting operands

The character strings "&lt;???&gt;", "&lt;??.?&gt;" and "..." are inserted as placeholders for the parameters when an LAD element is inserted:

- The "&lt;???&gt;" and "&lt;??.?&gt;" strings displayed in red indicate parameters that need to be connected.
- The "..." string displayed in black indicates parameters that may be connected.
- "&lt;??.?&gt;" stands for Boolean placeholders.

In addition, LAD elements can have the following different I/Os for the parameters:

- Orange I/Os: Only tags or constants can be interconnected at this I/O.
- Black I/Os: Boolean input or output to which other elements can be connected upstream or downstream.

You can recognize in/out parameters declared in the "InOut" section by the symbol ![Figure](images/153583563915_DV_resource.Stream@PNG-de-DE.png).

> **Note**
>
> If you position the cursor over the placeholder, the expected data type will be displayed.

#### Requirement

An LAD element is available.

#### Procedure

To connect the parameters of a LAD element, follow these steps:

1. Double-click the placeholder of the parameter.

   An entry field opens, and the placeholder is selected.
2. Enter the appropriate parameter.
3. Confirm the parameter with the Enter key.
4. If you have not yet defined the parameter, you can define it directly in the program editor using the shortcut menu.

   See also:

   [Declaring PLC tags in the program editor](Declaring%20PLC%20tags.md#declaring-plc-tags-in-the-program-editor)

   [Declaring local tags in the program editor](Declaring%20the%20block%20interface.md#declaring-a-local-tag-in-the-program-editor)

**Note**

If you enter the absolute address of a parameter that has already been defined, this absolute address will be changed to the symbolic name of the parameter as soon as the input is confirmed. If you have not yet defined the parameter, a new tag with this absolute address and the default name "Tag_&lt;n&gt;" will be entered in the PLC tag table. When you confirm your input, the absolute address will be replaced with the symbolic name "Tag_&lt;n&gt;".

Or drag from it the PLC tag table:

1. In the project tree, select the "PLC tags" folder or open the PLC tag table.
2. If you have opened the PLC tag table, drag the symbol from the first column of the desired tag to the appropriate place in your program. If you have not opened the PLC tag table yet, open the detail view now. Drag the desired tag from the detail view to the appropriate place in your program.

Or drag from it the block interface:

1. Open the block interface.
2. Drag the required operand from the block interface to the instruction window.

#### Result

- If the syntax is error-free, the displayed parameter is black. The editor then jumps to the next placeholder.
- If there is an error in the syntax, the cursor stays in the entry field and a corresponding error message is displayed in the status line. If you press the Enter key again, the entry field is closed and the faulty entry is displayed in red italics.

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

## Branches in LAD

This section contains information on the following topics:

- [Basic information on branches in LAD](#basic-information-on-branches-in-lad)
- [Rules for branches in LAD](#rules-for-branches-in-lad)
- [Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)
- [Closing branches in the LAD network](#closing-branches-in-the-lad-network)
- [Deleting branches in LAD networks](#deleting-branches-in-lad-networks)

### Basic information on branches in LAD

#### Definition

You use branches to program parallel circuits with the Ladder Logic (LAD) programming language. Branches are inserted in the main rung. You can insert several contacts into the branch and thus achieve a parallel circuit of series connections. This allows you to program complex ladder logic.

The figure below shows an example of the use of branches:

![Definition](images/6799842699_DV_resource.Stream@PNG-en-US.png)

MOTOR carries signal 1, if one of the following conditions is fulfilled:

- Signal 1 is pending on S2 or S4
- Signal 0 is pending on S5.

---

**See also**

[Rules for branches in LAD](#rules-for-branches-in-lad)
  
[Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)
  
[Closing branches in the LAD network](#closing-branches-in-the-lad-network)
  
[Deleting branches in LAD networks](#deleting-branches-in-lad-networks)

### Rules for branches in LAD

#### Rules

The following rules apply to simultaneous branches:

- A simultaneous branch can only be inserted if the main branch already contains an LAD element.
- Simultaneous branches are opened downwards or are connected directly to the power rail. They are terminated upwards.
- Simultaneous branches are opened after the selected LAD element.
- Simultaneous branches are terminated after the selected LAD element.
- To delete a simultaneous branch, you must delete all LAD elements of this branch. When the last LAD element is removed from the branch, the rest of the branch is also removed.
- You can only insert a coil in a parallel connection when the parallel connection starts directly at the power rail.

---

**See also**

[Basic information on branches in LAD](#basic-information-on-branches-in-lad)
  
[Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)
  
[Deleting branches in LAD networks](#deleting-branches-in-lad-networks)
  
[Closing branches in the LAD network](#closing-branches-in-the-lad-network)

### Inserting branches into the LAD network

You can create several branches in a network.

#### Requirement

- A network is available.
- The network contains elements.

#### Procedure

To insert a new branch in a network, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "General &gt; Open branches" in the "Simple instructions" palette.
3. Use drag-and-drop to move the element to the desired place in the network.

   If you want to connect the new branch directly to the power rail, drag the element to the power rail.

---

**See also**

[Basic information on branches in LAD](#basic-information-on-branches-in-lad)
  
[Rules for branches in LAD](#rules-for-branches-in-lad)
  
[Closing branches in the LAD network](#closing-branches-in-the-lad-network)
  
[Deleting branches in LAD networks](#deleting-branches-in-lad-networks)

### Closing branches in the LAD network

Branches must be closed again at suitable places. If necessary, branches will be arranged so that they do not cross each other.

#### Requirement

A branch is available.

#### Procedure

To close an open branch, follow these steps:

1. Select the open branch.
2. Press and hold down the left mouse button.

   A dashed line will appear as soon as the cursor is moved.
3. Drag the dashed line to a suitable place on the network. Permissible connections are indicated by green lines.
4. Release the left mouse button.

---

**See also**

[Basic information on branches in LAD](#basic-information-on-branches-in-lad)
  
[Rules for branches in LAD](#rules-for-branches-in-lad)
  
[Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)
  
[Deleting branches in LAD networks](#deleting-branches-in-lad-networks)

### Deleting branches in LAD networks

#### Requirement

A branch is available.

#### Procedure

To delete a branch, follow these steps:

1. Select the connection line that links the branch to the main branch.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on branches in LAD](#basic-information-on-branches-in-lad)
  
[Rules for branches in LAD](#rules-for-branches-in-lad)
  
[Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)
  
[Closing branches in the LAD network](#closing-branches-in-the-lad-network)

## Crossings in LAD

This section contains information on the following topics:

- [Basic information on crossings in LAD](#basic-information-on-crossings-in-lad)
- [Inserting crossings](#inserting-crossings)
- [Rearranging crossings](#rearranging-crossings)
- [Deleting crossings](#deleting-crossings)

### Basic information on crossings in LAD

#### Definition

A crossing is a place in a LAD network where one branch is closed and at the same time another branch is opened.

![Definition](images/23589629451_DV_resource.Stream@PNG-en-US.png)

"TagOut" receives signal 1, if the following two conditions are met:

- "TagIn_1" or "TagIn_3" has signal 1
- "TagIn_2" or "TagIn_4" has signal 0

---

**See also**

[Inserting crossings](#inserting-crossings)
  
[Rearranging crossings](#rearranging-crossings)
  
[Deleting crossings](#deleting-crossings)

### Inserting crossings

You can insert crossings in a LAD network by creating connections between the main branch and an additional branch or between different branches.

#### Requirements

A branch is available.

#### Procedure

To insert a new crossing in an LAD network, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "General &gt; Open branches" in the "Simple instructions" palette.
3. Drag the element behind the existing branch.
4. Insert any element into the open branch.
5. Click the arrow of the open branch after the inserted element.
6. Hold down the left mouse button and drag the dashed connecting line to the main branch.
7. Release the left mouse button.

---

**See also**

[Basic information on crossings in LAD](#basic-information-on-crossings-in-lad)
  
[Rearranging crossings](#rearranging-crossings)
  
[Deleting crossings](#deleting-crossings)
  
[Inserting branches into the LAD network](#inserting-branches-into-the-lad-network)

### Rearranging crossings

#### Requirement

A crossing is available.

#### Procedure

To rearrange a connection, follow these steps:

1. Select the connection line that defines the crossings in the respective branches.
2. Select the "Delete" command in the shortcut menu.
3. Open the "Instructions" task card.
4. Navigate to "General &gt; Open branches" in the "Simple instructions" palette.
5. Use a drag-and-drop operation to move the element to the place in the network where you want to insert the new crossing.
6. Click on the arrow for the open branch.
7. Hold down the left mouse button and drag the dashed connecting line to the subsidiary branch in which you wish to insert the new crossing.
8. Release the left mouse button.

---

**See also**

[Basic information on crossings in LAD](#basic-information-on-crossings-in-lad)
  
[Inserting crossings](#inserting-crossings)
  
[Deleting crossings](#deleting-crossings)

### Deleting crossings

#### Requirement

A crossing is available.

#### Procedure

To delete a crossing, follow these steps:

1. Select the connection line that defines the crossings in the respective branches.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on crossings in LAD](#basic-information-on-crossings-in-lad)
  
[Inserting crossings](#inserting-crossings)
  
[Rearranging crossings](#rearranging-crossings)

## Rungs in LAD

This section contains information on the following topics:

- [Basic information on rungs in LAD](#basic-information-on-rungs-in-lad)
- [Insert rung](#insert-rung)
- [Deleting a rung](#deleting-a-rung)

### Basic information on rungs in LAD

#### Using rungs

The program is mapped in one or more networks. A network contains a power rail on the left where one or more rungs originate. The binary signal scans are arranged in the form of contacts on the rungs. The serial arrangement of the elements on a rung creates a series connection; arrangement on simultaneous branches creates a parallel connection. A rung is closed by a coil or a box in which the result of logic operation will be written.

The figure below shows an example of the use of several rungs within a network:

![Using rungs](images/13490027403_DV_resource.Stream@PNG-en-US.png)

#### Rules

Remember the following rules when using several rungs:

- Connections are not permitted between rungs.
- Only one jump instruction is permissible per network. The positioning rules for jump instructions remain valid.

#### Running rungs

Rungs and networks are executed from top to bottom and from left to right. This means that the first instruction in the first rung of the first network is processed first. All instructions of this rung are then processed. After this come all other rungs of the first network. The next network is processed only after all rungs have first been run.

#### Differences between branches and rungs

The difference between branches and rungs is that the rungs are independent branches that can also stand in a different network. Branches, on the other hand, permit the programming of a parallel connection.

---

**See also**

[Insert rung](#insert-rung)
  
[Deleting a rung](#deleting-a-rung)

### Insert rung

#### Requirement

- A block is open.
- A network is available.

#### Procedure

To insert a new rung in a network, proceed as follows:

1. Insert any coil on the power rail.

   A new rung will be inserted and the coil positioned at the end of the rung.
2. Insert additional instructions in the new rung.

---

**See also**

[Basic information on rungs in LAD](#basic-information-on-rungs-in-lad)
  
[Deleting a rung](#deleting-a-rung)

### Deleting a rung

#### Requirement

A rung is available.

#### Procedure

To delete a rung, proceed as follows:

1. Hold down the left mouse button and draw a frame around the rung. At the same time, make sure that you select all instructions. Alternatively, you can hold down the &lt;Shift&gt; key and select the first the last instruction of the rung.
2. Right-click on one of the instructions in the rung.
3. Select the "Delete" command in the shortcut menu.

---

**See also**

[Basic information on rungs in LAD](#basic-information-on-rungs-in-lad)
  
[Insert rung](#insert-rung)

## LAD programming examples

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

The following networks show the LAD programming for solving this task:

Network 1:

The conveyor belt motor is switched on when start pushbutton "S1" or "S3" is pressed.

![Implementation](images/70907806091_DV_resource.Stream@PNG-en-US.png)

Network 2:

The conveyor belt motor is switched off when stop pushbutton "S2" or "S4" is pressed.

![Implementation](images/70908450187_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on LAD](#basic-information-on-lad)
  
[Settings for LAD](#settings-for-lad)
  
[Working with networks](#working-with-networks)
  
[Inserting LAD elements](#inserting-lad-elements)
  
[Editing LAD elements](#editing-lad-elements)
  
[Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
  
[Branches in LAD](#branches-in-lad)
  
[Crossings in LAD](#crossings-in-lad)
  
[Rungs in LAD](#rungs-in-lad)
  
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

The following networks show the LAD programming for solving this task:

Network 1:

If the signal state changes from "0" to "1" (positive edge) at photoelectric barrier "PEB1" and, at the same time, the signal state at "PEB2" is "0", the object on the belt is moving to the left.

![Implementation](images/70910605451_DV_resource.Stream@PNG-en-US.png)

Network 2:

If the signal changes from "0" to "1" (positive edge) at photoelectric barrier "PEB2" and, at the same time, the signal state at "PEB1" is "0", the object on the belt is moving to the right.

![Implementation](images/70910609547_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on LAD](#basic-information-on-lad)
  
[Settings for LAD](#settings-for-lad)
  
[Working with networks](#working-with-networks)
  
[Inserting LAD elements](#inserting-lad-elements)
  
[Editing LAD elements](#editing-lad-elements)
  
[Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
  
[Branches in LAD](#branches-in-lad)
  
[Crossings in LAD](#crossings-in-lad)
  
[Rungs in LAD](#rungs-in-lad)
  
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

The following networks show the LAD programming for activating the lamps:

Network 1:

When a package is delivered to the storage area, the signal state at "PEB1" switches from "0" to "1" (positive signal edge). On a positive signal edge at "PEB1", the "Up" counter is enabled, and the current count value of "PACKAGECOUNT" is increased by one.

When a package is delivered from the storage area to the loading dock, the signal state at "PEB2" switches from "0" to "1" (positive signal edge). On a positive signal edge at "PEB2", the "Down" counter is enabled, and the current count value of "PACKAGECOUNT" is decreased by one.

If there are no packages in the storage area ("PACKAGECOUNT" = "0"), the "STOR_EMPTY" tag is set to signal state "1", and the "Storage area empty" lamp is switched on.

The current count value can be reset to "0" if the "RESET" tag is set to signal state "1".

If the "LOAD" tag is set to signal state "1", the current count value is set to the value of the "MAX STORAGE AREA FILL AMOUNT" tag. As long as the current count value is greater than or equal to the value of the "MAX STORAGE AREA FILL AMOUNT" tag, the "STOCK_PACKAGES" tag supplies the signal state "1".

![Implementation](images/70935451787_DV_resource.Stream@PNG-en-US.png)

Network 2:

As long as there are packages in the storage area, the "STOR_NOT_EMPTY" tag is set to signal state "1", and the "Storage area not empty" lamp is switched on.

![Implementation](images/70912365067_DV_resource.Stream@PNG-en-US.png)

Network 3:

If the number of packages in the storage area is greater than or equal to 50, the "Storage area 50 % full" lamp switches on.

![Implementation](images/70912203275_DV_resource.Stream@PNG-en-US.png)

Network 4:

If the number of packages in the storage area is greater than or equal to 90, the "Storage area 90% full" lamp switches on.

![Implementation](images/70912207371_DV_resource.Stream@PNG-en-US.png)

Network 5:

If the number of packages in the storage area reaches 100, the lamp for the "Storage area full" message switches on.

![Implementation](images/70912199179_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic information on LAD](#basic-information-on-lad)
  
[Settings for LAD](#settings-for-lad)
  
[Working with networks](#working-with-networks)
  
[Inserting LAD elements](#inserting-lad-elements)
  
[Editing LAD elements](#editing-lad-elements)
  
[Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
  
[Branches in LAD](#branches-in-lad)
  
[Crossings in LAD](#crossings-in-lad)
  
[Rungs in LAD](#rungs-in-lad)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of calculating an equation](#example-of-calculating-an-equation)
  
[Example of controlling room temperature](#example-of-controlling-room-temperature)

### Example of calculating an equation

#### Calculating an equation

The following program example shows you how to solve equations of the following type with the LAD programming language:

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

The following network shows the LAD programming for calculating the equation:

![Implementation with the instructions "ADD", "MUL" and "DIV"](images/12894588043_DV_resource.Stream@PNG-en-US.png)

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

1. Drag the instruction "CALCULATE" from the "Instructions" task card to an LAD network.
2. You can select the data type INT for the instruction from the "&lt;???&gt;" drop-down list.
3. Interconnect the tags declared in the block interface with the inputs and outputs of the instruction box.
4. Click the "Calculator" icon on the top right corner of the instruction box to enter the equation to be calculated.

   The dialog "Edit 'Calculate' instruction" opens.
5. Enter the following expression in the "OUT:=" field:

   ((IN1 + IN2) * IN4) / IN3

   The equation is displayed in the instruction box.

The following network shows the result in the LAD programming language:

![Implementation with the instruction "CALCULATE" (S7-1200/1500 only)](images/65853662731_DV_resource.Stream@PNG-de-DE.png)

If the "Tag_Input" has signal state "1", the instruction is executed. The value of operand "A" is added to the value of operand "B". The subtotal is multiplied by "C" and then divided by the value of the "D" operand. The end result is saved in the "RESULT" operand.

---

**See also**

[Basic information on LAD](#basic-information-on-lad)
  
[Settings for LAD](#settings-for-lad)
  
[Working with networks](#working-with-networks)
  
[Inserting LAD elements](#inserting-lad-elements)
  
[Editing LAD elements](#editing-lad-elements)
  
[Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
  
[Branches in LAD](#branches-in-lad)
  
[Crossings in LAD](#crossings-in-lad)
  
[Rungs in LAD](#rungs-in-lad)
  
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
- The "STOP" pushbutton is pressed.

If the preset cooling time has expired and the temperature in the cold room is still too high, the cooling system can be restarted with the "RESET" pushbutton.

![Controlling room temperature](images/70914758667_DV_resource.Stream@PNG-en-US.png)

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

The following network shows the LAD programming for controlling room temperature:

Network 1:

![Implementation](images/40082501131_DV_resource.Stream@PNG-en-US.png)

Network 2:

![Implementation](images/70916294283_DV_resource.Stream@PNG-en-US.png)

When the temperature in the cold room rises above zero degrees Celsius, the signal state at the "Sensor" operand switches from "0" to "1" (positive signal edge). In the case of a positive signal edge at the IN input of the timer function, the preset cooling time is started and the "TempVariable" receives the signal state "1". The signal state "1" of the "TempVariable" causes the cooling system as well as the display lamp to be turned on in network 2. The "Sensor", "Cooling system" and "Lamp" outputs must be programmed in network 2, because program only one coil can be programmed at the Q output of the timer function.

If the temperature in the cold room falls below zero degrees Celsius, the signal state of the sensor switches back to "0". This switches the cooling system and lamp off.

If the sensor does not signal a temperature drop, the cooling system and lamp are switched off after the preset cooling time has elapsed, at the latest. In this case, the cooling process can be restarted with the "RESET" pushbutton. Pressing and releasing the pushbutton generates a new positive signal edge at the IN input that restarts the cooling system.

The cooling system and the display lamp can be turned off with the "STOP" pushbutton at any time.

---

**See also**

[Basic information on LAD](#basic-information-on-lad)
  
[Settings for LAD](#settings-for-lad)
  
[Working with networks](#working-with-networks)
  
[Inserting LAD elements](#inserting-lad-elements)
  
[Editing LAD elements](#editing-lad-elements)
  
[Inserting operands into LAD instructions](#inserting-operands-into-lad-instructions)
  
[Branches in LAD](#branches-in-lad)
  
[Crossings in LAD](#crossings-in-lad)
  
[Rungs in LAD](#rungs-in-lad)
  
[Example of controlling a conveyor belt](#example-of-controlling-a-conveyor-belt) 
  
[Example of detecting the direction of a conveyor belt](#example-of-detecting-the-direction-of-a-conveyor-belt)
  
[Example of detecting the fill level of a storage area](#example-of-detecting-the-fill-level-of-a-storage-area) 
  
[Example of calculating an equation](#example-of-calculating-an-equation)

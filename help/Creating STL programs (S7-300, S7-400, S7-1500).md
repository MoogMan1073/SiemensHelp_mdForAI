---
title: "Creating STL programs (S7-300, S7-400, S7-1500)"
package: ProgBlockAWL34enUS
topics: 53
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating STL programs (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
- [Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
- [Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
- [Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
- [Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
- [STL programming examples (S7-300, S7-400, S7-1500)](#stl-programming-examples-s7-300-s7-400-s7-1500)

## STL Basics (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [STL programming language (S7-300, S7-400, S7-1500)](#stl-programming-language-s7-300-s7-400-s7-1500)
- [Data exchange in STL (S7-300, S7-400, S7-1500)](#data-exchange-in-stl-s7-300-s7-400-s7-1500)
- [Parameter passing via registers (S7-300, S7-400, S7-1500)](#parameter-passing-via-registers-s7-300-s7-400-s7-1500)

### STL programming language (S7-300, S7-400, S7-1500)

#### Overview of the STL (Statement List) programming language

STL is a text-based programming language you can use to program logic blocks.

The STL program is divided into networks. Each network can contain one or more rows. The numbering of the rows begins with 1 in each network and is continued in ascending order with each new row. The individual STL instructions are programmed in the rows of a network, where only one STL instruction can be specified per row. Each statement represents an instruction to the CPU. The CPU executes the instructions from top to bottom.

The following example shows the STL programming of a network:

| STL | Explanation |
| --- | --- |
| A"Tag_Input_1" | // Check whether the signal state of the operand is "1" and AND with current RLO |
| A "Tag_Input_2" | // Check whether the signal state of the operand is "1" and AND with current RLO |
| S "Tag_Output" | // Sets the operand to "1" if the RLO is "1" |
|  |  |

### Data exchange in STL (S7-300, S7-400, S7-1500)

#### S7-300/400 data exchange

For S7-300/400 CPUs, information is exchanged between different memory areas in STL via accumulators. Accumulators are special registers in the process which serve as buffers. All S7-300/400 CPUs have two buffers, namely accumulator 1 (ACCU 1) and accumulator 2 (ACCU 2). The S7-400 CPUs and the S7-318 CPU also have two additional buffers, accumulators 3 (ACCU 3) and 4 (ACCU 4).

#### S7-1500 data exchange

Although S7-1500 CPUs no longer have a register in the processor, they can emulate the address register, ACCU 1, ACCU 2, the status word and the data block registers DB and DI. Data is exchanged primarily via the block interface, global data blocks or via PLC tags. However, using accumulators for data exchange slows downs the program processing.

When programming in STL for S7-1500, note the following basic instructions regarding the register:

- The contents of the registers, accumulators and the status word are only available within STL networks. When an LAD or FBD network follows an STL network, you cannot access the register contents that were previously set in STL from the LAD or FBD network. However, the register contents are available again in a downstream STL network.

  The RLO bit is an exception: It is set to "undefined" at a language change and is no longer available in downstream networks.
- The values from the registers, accumulators and the status word are never transferred to called blocks. The instructions "CC" and "UC" are the only exceptions. If you use "UC" or "CC" and want to pass the parameters to the called block by using registers, the status word or accumulators, you have to select the "Parameter passing via registers" option in the properties of the called block. Note that this option is only available for STL blocks with standard access and the block can have no formal parameters. If the option is enabled, you can transfer register contents between blocks. The RLO bit is an exception here as well: It is set to "undefined" when the block is exited and is no longer available after a block call.
- The data block register DB is set to "0" after each access to the data block with specification of a fully qualified address (for example, %DB10.DBW10). Subsequent partially qualified access leads to an error during compilation.
- To pass an error message to the calling block, you can use the BR bit. You first need to store the error message in the called block in the BR bit with the instruction "SAVE". You can then read the BR bit in the calling block.
- If you symbolically address (e.g. with the instruction L #myIn) a local formal parameter from the block interface in S7-1500, you always access the data block that you specified as an instance in the block call. Although the OPN DI, L AR2, +AR2, CDB, CAR instructions change the contents of the DI or address register, the registers are no longer evaluated when local formal parameters are addressed.

#### Load and transfer

During data exchange, the direction of the information flow is marked. If data is transferred from a memory area to accumulator 1, this is referred to as loading data. Data transfer from accumulator 1 to a memory area is referred to as "transfer". Load and transfer instructions are used for load and transfer in STL.

Load and transfer is necessary above all for editing digital values. If you want to add two values, for example, you have to load them to the buffer and execute the appropriate instruction. First, the first value to be added is loaded to accumulator 1. When the second summand is loaded, the first value, which is located in accumulator 1, is moved to accumulator 2. After execution of the add instruction (e.g. I+), the sum is saved in accumulator 1. The sum can be transferred to any operand using the transfer instruction.

All accumulators are 32 bits long and are organized byte-oriented. Data transfer between the memory areas and accumulator 1 may be byte-oriented, word-oriented or double word-oriented.

#### Data exchange between accumulators

Data can be exchanged between individual accumulators. The accumulator instructions "TAK", "PUSH" and "POP" are used for this purpose. This allows the transfer of data between the available accumulators and the exchange of bytes in Accumulator 1. Please note that the accumulator instructions "ENT" and "LEAVE" are then no longer available for the S7-1500.

---

**See also**

[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
  
[Load (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#load-s7-300-s7-400)
  
[Transfer (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#transfer-s7-300-s7-400)
  
[Accumulators (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#accumulators-s7-300-s7-400)

### Parameter passing via registers (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
- [Activating parameter passing via registers (S7-1500)](#activating-parameter-passing-via-registers-s7-1500)

#### Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)

Block calls can be implemented using the following instructions in STL:

- CALL: Call block
- UC: Unconditional block call
- CC: Conditional block call

In a block call, values are usually transferred between the called and the calling block. The data exchange options are different for the various CPU families.  
See also: [Data exchange in STL](#data-exchange-in-stl-s7-300-s7-400-s7-1500)

##### Values transferred from the calling block to the called block

The following table indicates which registers, accumulators and status bits are directly available after a block call in the called block prior to processing the first network:

|  | S7-300/400 |  | S7-1500 |  |
| --- | --- | --- | --- | --- |
|  | UC / CC | CALL | UC / CC with option "Parameter passing via registers" | CALL |
| Status bit OS | 0 | 0 | 0 | 0 |
| Status bit OV | W | W | W | 0 |
| Status bit CC0 | W | W | W | 0 |
| Status bit CC1 | W | W | W | 0 |
| BR | W | W | W | 1 |
| RLO | W | W | W | A |
| Accu 1 | W | W | W | A |
| Accu 2 | W | W | W | A |
| Address register 1 | W | W | W | 0 |
| Address register 2 | W | Call FC: W Call FB: Instance offset | W | Call FC: 0 Call FB: Instance offset |
| DB register | W | W | W | A |
| DI register | W | Call FC: W Call FB: Instance DB number | W | Call FC: A Call FB: Instance DB number |

Legend:  
0 = Register is set to "0" at block change.  
1 = Register is set to "1" at block change.  
W = Register content can be set in the calling block and read in the called block.  
A = Register content is not transferred to the called block. The contents are undefined, access results in an error during compilation.  
Instance offset = Offset in instance DB  
Instance DB number = Number of the instance DB

##### Values returned from the called block to the calling block

The following table indicates which registers, accumulators and status bits are directly available after processing of the block call in the calling block:

|  | S7-300/400 |  | S7-1500 |  |
| --- | --- | --- | --- | --- |
|  | UC / CC | CALL | UC / CC with option "Parameter passing via registers" | CALL |
| Status bit OS | 0 | 0 | 0 | 0 |
| Status bit OV | W | W | W | - |
| Status bit CC0 | W | W | W | - |
| Status bit CC1 | W | W | W | - |
| BR | W | W | W | W |
| RLO | W | W1 | W | A |
| Accu 1 | W | W1 | W | - |
| Accu 2 | W | W1 | W | - |
| Address register 1 | W | W1 | W | - |
| Address register 2 | W | Call FC: W Call FB: - | W | - |
| DB register | - | X | - | - |
| DI register | - | X | - | - |

Legend:  
0 = Register is set to "0" at block change.  
1 = Register is set to "1" at block change.  
W = Register content can be set in the called block and read in the calling block.  
W1 = The returned value can be changed by the output parameters and in/out parameters of the called block.  
- = Register contents is not returned to the calling block, content is not changed by the block call.  
A = Register content is not transferred to the called block. The content is undefined, access results in an error during compilation.  
X = Register content is not returned to the calling block. The value can be changed implicitly by the parameters of the called block.

---

**See also**

[Passing values using registers or the status word with a block call (S7-1500)](Migrating%20PLC%20programs%20to%20a%20S7-1500%20CPU%20-%20ET%20200SP.md#passing-values-using-registers-or-the-status-word-with-a-block-call-s7-1500)
  
[Passing values using registers with the CC and UC instructions (S7-1500)](Migrating%20PLC%20programs%20to%20a%20S7-1500%20CPU%20-%20ET%20200SP.md#passing-values-using-registers-with-the-cc-and-uc-instructions-s7-1500)
  
[Activating parameter passing via registers (S7-1500)](#activating-parameter-passing-via-registers-s7-1500)

#### Activating parameter passing via registers (S7-1500)

##### Requirement

- The "Optimized block access" option is disabled.
- The block interface does not include any parameters.

##### Procedure

To enable parameter passing via registers, follow these steps:

1. Open the "Program blocks" folder in the project tree.
2. Right-click the block for which you want to set up the parameter passing via registers.
3. Select the "Properties" command in the shortcut menu.
4. The properties dialog box of the block opens.
5. Click "Attributes" in the area navigation.
6. Select the option "Parameter passing via registers".
7. Confirm your entries with "OK".

---

**See also**

[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)
  
[Data exchange in STL (S7-300, S7-400, S7-1500)](#data-exchange-in-stl-s7-300-s7-400-s7-1500)

## Settings for STL (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Overview of the settings for STL (S7-300, S7-400, S7-1500)](#overview-of-the-settings-for-stl-s7-300-s7-400-s7-1500)
- [Changing the settings (S7-300, S7-400, S7-1500)](#changing-the-settings-s7-300-s7-400-s7-1500)

### Overview of the settings for STL (S7-300, S7-400, S7-1500)

#### Overview

The following table shows the settings that you can make for STL:

| Group | Setting | Description |
| --- | --- | --- |
| View | Line break on Enter | Inserts a line break when you press the Enter key. |

---

**See also**

[Changing the settings (S7-300, S7-400, S7-1500)](#changing-the-settings-s7-300-s7-400-s7-1500)

### Changing the settings (S7-300, S7-400, S7-1500)

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

[Overview of the settings for STL (S7-300, S7-400, S7-1500)](#overview-of-the-settings-for-stl-s7-300-s7-400-s7-1500)

## Working with networks (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
- [Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
- [Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
- [Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
- [Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
- [Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
- [Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
- [Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
- [Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Using networks (S7-300, S7-400, S7-1500)

#### Function

The user program is created in the block within networks. For a code block to be programmed, it must contain at least one network. To achieve a better overview of the user program, you can also subdivide your program into several networks.

---

**See also**

[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Inserting networks (S7-300, S7-400, S7-1500)

#### Requirement

A block is open.

#### Procedure

To insert a new network, follow these steps:

1. Select the network after which you want to insert a new network.
2. Select the "Insert network" command in the shortcut menu.

#### Result

A new empty network is inserted into the block.

---

**See also**

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Selecting networks (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Copying and pasting networks (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Deleting networks (S7-300, S7-400, S7-1500)

#### Requirement

A network is available.

#### Procedure

To delete a network, follow these steps:

1. Select the network that you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Expanding and collapsing networks (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Inserting network title (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Entering a network comment (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Navigating networks (S7-300, S7-400, S7-1500)](#navigating-networks-s7-300-s7-400-s7-1500)

### Navigating networks (S7-300, S7-400, S7-1500)

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

[Using networks (S7-300, S7-400, S7-1500)](#using-networks-s7-300-s7-400-s7-1500)
  
[Inserting networks (S7-300, S7-400, S7-1500)](#inserting-networks-s7-300-s7-400-s7-1500)
  
[Selecting networks (S7-300, S7-400, S7-1500)](#selecting-networks-s7-300-s7-400-s7-1500)
  
[Copying and pasting networks (S7-300, S7-400, S7-1500)](#copying-and-pasting-networks-s7-300-s7-400-s7-1500)
  
[Deleting networks (S7-300, S7-400, S7-1500)](#deleting-networks-s7-300-s7-400-s7-1500)
  
[Expanding and collapsing networks (S7-300, S7-400, S7-1500)](#expanding-and-collapsing-networks-s7-300-s7-400-s7-1500)
  
[Inserting network title (S7-300, S7-400, S7-1500)](#inserting-network-title-s7-300-s7-400-s7-1500)
  
[Entering a network comment (S7-300, S7-400, S7-1500)](#entering-a-network-comment-s7-300-s7-400-s7-1500)

## Inserting STL instructions (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Rules for STL (S7-300, S7-400, S7-1500)](#rules-for-stl-s7-300-s7-400-s7-1500)
- [Instructions from the global library "Long Functions" (S7-300, S7-400, S7-1500)](#instructions-from-the-global-library-long-functions-s7-300-s7-400-s7-1500)
- [Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
- [Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
- [Selecting the data type of an STL instruction (S7-300, S7-400, S7-1500)](#selecting-the-data-type-of-an-stl-instruction-s7-300-s7-400-s7-1500)
- [Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)
- [Displaying or hiding tag information (S7-300, S7-400, S7-1500)](#displaying-or-hiding-tag-information-s7-300-s7-400-s7-1500)
- [Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
- [Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)
- [Inserting comments (S7-300, S7-400, S7-1500)](#inserting-comments-s7-300-s7-400-s7-1500)

### Rules for STL (S7-300, S7-400, S7-1500)

#### Rules

The following rules must be observed when entering STL instructions incrementally:

- An instruction consists of the specification of an optional jump label, the operation, the operand, and an optional comment. Example:

  `M001: A I1.0 //comment`
- Each instruction is in its own separate line.
- You can enter a maximum of 999 networks per block.
- The entry of operations or absolute addresses is not case-sensitive.
- If you would like support for block calls, you must program the called block before the calling block.

Impermissible instructions are highlighted in red. A rollout and the inspector window give information for troubleshooting.

#### Jumps

For jump operations, make sure that the jump destination is always at the start of a logic sequence and is within a different nesting level (not applicable to CPU 318-2). The jump designation must not be located within a logic sequence or a nesting level.

---

**See also**

[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Inserting comments (S7-300, S7-400, S7-1500)](#inserting-comments-s7-300-s7-400-s7-1500)
  
[Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)
  
[Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)

### Instructions from the global library "Long Functions" (S7-300, S7-400, S7-1500)

#### Description

The table below shows the instructions included in the global library "Long Functions":

| Instruction | Explanation |
| --- | --- |
| ABS_LINT | Forming absolute value with the LINT data type |
| ABS_LREAL | Forming absolute value with the LREAL data type |
| ACOS_LREAL | Forming arccosine value with the LREAL data type |
| ADD_LINT | Adding with the LINT data type |
| ADD_LREAL | Adding with the LREAL data type |
| ADD_ULINT | Adding with the ULINT data type |
| AND_LWORD | AND logical operation with the LWORD data type |
| ASIN_LREAL | Forming arccosine value with the LREAL data type |
| ATAN_LREAL | Forming arctangent value with the LREAL data type |
| COS_LREAL | Forming cosine value with the LREAL data type |
| DINT_to_LINT | Data type conversion from DINT to LINT |
| DIV_LINT | Dividing with the LINT data type |
| DIV_LREAL | Dividing with the LREAL data type |
| DIV_ULINT | Dividing with the ULINT data type |
| EQ_LINT | Compare for equivalence with the LINT data type |
| EQ_LREAL | Compare for equivalence with the LREAL data type |
| EQ_LWORD | Compare for equivalence with the LWORD data type |
| EQ_ULINT | Compare for equivalence with the ULINT data type |
| EXP_LREAL | Forming exponential value with the LREAL data type |
| GE_LINT | Compare for greater than or equal to with the LINT data type |
| GE_LREAL | Compare for greater than or equal to with the LREAL data type |
| GE_ULINT | Compare for greater than or equal to with the ULINT data type |
| GT_LINT | Compare for greater than with the LINT data type |
| GT_LREAL | Compare for greater than with the LREAL data type |
| GT_ULINT | Compare for greater than with the ULINT data type |
| LE_LINT | Compare for less than or equal to with the LINT data type |
| LE_LREAL | Compare for less than or equal to with the LREAL data type |
| LE_ULINT | Compare for less than or equal to with the ULINT data type |
| LINT_to_DINT | Data type conversion from LINT to DINT |
| LINT_to_LREAL | Data type conversion from LINT to LREAL |
| LINT_to_ULINT | Data type conversion from LINT to ULINT |
| LN_LREAL | Forming natural logarithm with the LREAL data type |
| LREAL_to_LINT | Data type conversion from LREAL to LINT |
| LREAL_to_REAL | Data type conversion from LREAL to REAL |
| LREAL_to_ULINT | Data type conversion from LREAL to ULINT |
| LT_LINT | Compare for less than with the LINT data type |
| LT_LREAL | Compare for less than with the LREAL data type |
| LT_ULINT | Compare for less than with the ULINT data type |
| LWORD_to_ULINT | Data type conversion from LWORD to ULINT |
| LWORD_to_WORD | Data type conversion from LWORD to WORD |
| MOVE_LINT | Move value with the LINT data type |
| MOVE_LREAL | Move value with the LREAL data type |
| MOVE_LWORD | Move value with the LWORD data type |
| MOVE_ULINT | Move value with the ULINT data type |
| MUL_LINT | Multiply by the LINT data type |
| MUL_LREAL | Multiply by the LREAL data type |
| MUL_ULINT | Multiply by the ULINT data type |
| NE_LINT | Compare for non-equivalence with the LINT data type |
| NE_LREAL | Compare for non-equivalence with the LREAL data type |
| NE_LWORD | Compare for non-equivalence with the LWORD data type |
| NE_ULINT | Compare for non-equivalence with the ULINT data type |
| NEG_LINT | Create two's complement with the LINT data type |
| NEG_LREAL | Create two's complement with the LREAL data type |
| OR_LWORD | OR logical operation with the LWORD data type |
| RDN_LREAL | Round number with the LREAL data type |
| REAL_to_LREAL | Data type conversion from REAL to LREAL |
| SIN_LREAL | Form sine value with the LREAL data type |
| SQR_LREAL | Form square with the LREAL data type |
| SQRT_LREAL | Form square root with the LREAL data type |
| SUB_LINT | Subtract with the LINT data type |
| SUB_LREAL | Subtract with the LREAL data type |
| SUB_ULINT | Subtract with the ULINT data type |
| TAN_LREAL | Form tangent value with the LREAL data type |
| TRUNC_LREAL | Create integer with the LREAL data type |
| UDINT_to_ULINT | Data type conversion from UDINT to ULINT |
| ULINT_to_LINT | Data type conversion from ULINT to LINT |
| ULINT_to_LREAL | Data type conversion from ULINT to LREAL |
| ULINT_to_LWORD | Data type conversion from ULINT to LWORD |
| ULINT_to_UDINT | Data type conversion from ULINT to UDINT |
| WORD_to_LWORD | Data type conversion from WORD to LWORD |
| XOR_LWORD | EXCLUSIVE OR logical operation with the LWORD data type |

---

**See also**

[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)

### Entering STL instructions manually (S7-300, S7-400, S7-1500)

When an empty network is created automatically or manually, a two-line entry field is generated within the network. The STL instructions are entered in this entry field.

> **Note**
>
> S7-1500: Instructions from the "Instructions" task card that use emulated registers and accumulators cannot use 64-bit tags, such as LInt, as operands. If you want to use 64-bit tags, use the instructions from the "Long Functions" global library.

#### Requirement

A network is available.

#### Procedure

To enter STL instructions in a network, follow these steps:

1. Click the first empty row of the entry field in a network.
2. Enter an instruction.
3. Enter a space.
4. Enter the operand.
5. Enter a line comment. This step is optional.
6. Confirm the instruction with the Enter key.
7. Repeat steps 2 to 6 until you have entered all the required instructions.

**Note**

You can also use a drag-and-drop operation to insert an already defined operand from the PLC tag table or from the detail view.

#### Result

After the instruction is closed by pressing the Enter key, the program editor performs the following actions:

- Syntax check: After the check, faulty entries are displayed in red italics. In addition, you also receive a detailed error message in the "Syntax" tab of the information window.
- Change of lower and upper case: Instructions are changed to upper case.
- If you have entered absolute addresses in symbolic programming, these will be converted into symbolic names. If no symbolic name is available, "Tag_&lt; number&gt;" is inserted.
- Block call: the necessary parameters are inserted and displayed.
- An additional line is inserted in the entry field.

---

**See also**

[Instructions from the global library "Long Functions" (S7-300, S7-400, S7-1500)](#instructions-from-the-global-library-long-functions-s7-300-s7-400-s7-1500)
  
[Rules for STL (S7-300, S7-400, S7-1500)](#rules-for-stl-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)
  
[Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting comments (S7-300, S7-400, S7-1500)](#inserting-comments-s7-300-s7-400-s7-1500)

### Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)

When an empty network is created automatically or manually, a two-line entry field is generated within the network. The STL instructions are entered in this entry field.

> **Note**
>
> S7-1500: Instructions from the "Instructions" task card that use emulated registers and accumulators cannot use 64-bit tags, such as LInt, as operands. If you want to use 64-bit tags, use the instructions from the "Long Functions" global library.

#### Requirement

A network is available.

#### Procedure

To insert STL instructions into a network using the "Instructions" task card, follow these steps:

1. Open the "Instructions" task card.
2. To insert the instruction, select one of the following steps:

   - Go to the STL element you want to insert and drag it to the required location in the network.
   - Select the location in the network at which you want to insert the element and then double-click on the element you want to insert.
3. Enter the required operands.
4. Enter a line comment. This step is optional.
5. Repeat steps 2 to 4 until you have entered all the required instructions.

**Note**

You can also use a drag-and-drop operation to insert an already defined operand from the PLC tag table, a data block, the detail view or the block interface.

#### Result

After the instruction is closed by pressing the Enter key, the program editor performs the following actions:

- Syntax check: After the check, faulty entries are displayed in red italics. In addition, you also receive a detailed error message in the information window.
- Change of lower and upper case: Instructions are changed to upper case.
- If you have entered absolute addresses in symbolic programming, these will be converted into symbolic names. If no symbolic name is available, "Tag_&lt; number&gt;" is inserted.
- Block call: the necessary parameters are inserted and displayed.
- An additional line is inserted in the entry field.

---

**See also**

[Instructions from the global library "Long Functions" (S7-300, S7-400, S7-1500)](#instructions-from-the-global-library-long-functions-s7-300-s7-400-s7-1500)
  
[Rules for STL (S7-300, S7-400, S7-1500)](#rules-for-stl-s7-300-s7-400-s7-1500)
  
[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)
  
[Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting comments (S7-300, S7-400, S7-1500)](#inserting-comments-s7-300-s7-400-s7-1500)

### Selecting the data type of an STL instruction (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Selecting a data type (S7-300, S7-400, S7-1500)](#selecting-a-data-type-s7-300-s7-400-s7-1500)
- [Defining the data type of an instruction (S7-300, S7-400, S7-1500)](#defining-the-data-type-of-an-instruction-s7-300-s7-400-s7-1500)

#### Selecting a data type (S7-300, S7-400, S7-1500)

##### Introduction

Some instructions can be executed with several different data types. If you use one of these instructions in the program, you have to specify a valid data type for the instruction at the specific point in the program.

The valid data types for an instruction are listed in the instruction drop-down list. You specify the data type of the instruction by selecting an entry from the drop-down list. If the data type of an operand differs from the data type of the instruction and cannot be converted implicitly, the operand is displayed in red and a rollout with the corresponding error message appears.

#### Defining the data type of an instruction (S7-300, S7-400, S7-1500)

##### Introduction

Some instructions can be executed with several different data types. When you insert such instructions into your program, you must specify the data type for these instructions at the actual point in the program.

##### Procedure

To define the data type of an instruction using the drop-down list, follow these steps:

1. Insert the instruction at the required point in the program using drag-and-drop.

   The entry "???" (undefined) is displayed in the drop-down list of the inserted instruction.
2. Click the triangle in the upper corner of the drop-down list.

   The drop-down list opens to display the data types valid for the instruction.
3. Select a data type from the drop-down list.

   The selected data type is displayed.

### Inserting operands (S7-300, S7-400, S7-1500)

You can enter the operands of an STL instruction either manually or by dragging them from the PLC tag table, a data block, the detail view, or the block interface.

> **Note**
>
> S7-1500: Instructions from the "Instructions" task card that use emulated registers and accumulators cannot use 64-bit tags, such as LInt, as operands. If you want to use 64-bit tags, use the instructions from the "Long Functions" global library.

#### Procedure

To enter the operand of an STL instruction manually, follow these steps:

1. Position the cursor to the right of the operation.
2. Enter a space and then the operand.
3. Confirm the parameter with the Enter key.
4. If you have not yet defined the parameter, you can define it directly in the program editor using the shortcut menu.

   See also: "[Declaring tags directly in the program editor](Declaring%20PLC%20tags.md#declaring-plc-tags-in-the-program-editor)"

**Note**

If you enter the absolute address of a parameter that has already been defined in symbolic programming, this absolute address will be changed to the symbolic name of the parameter as you confirm your input. If you have not yet defined the parameter, a new tag with this absolute address and the default name "Tag_1" will be entered in the PLC tag table. When you confirm your input, the absolute address will be replaced with the symbolic name "Tag_1".

Or drag from it the PLC tag table:

1. In the project tree, select the "PLC tags" folder or open the PLC tag table.
2. If you have opened the PLC tag table, drag the symbol from the first column of the desired tag to the appropriate place in your program. If you have not opened the PLC tag table yet, open the detail view now. Drag the desired tag from the detail view to the appropriate place in your program.

Or drag from it the block interface:

1. Open the block interface.
2. Drag the required operand from the block interface to the instruction window.

---

**See also**

[Instructions from the global library "Long Functions" (S7-300, S7-400, S7-1500)](#instructions-from-the-global-library-long-functions-s7-300-s7-400-s7-1500)
  
[Rules for STL (S7-300, S7-400, S7-1500)](#rules-for-stl-s7-300-s7-400-s7-1500)
  
[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting comments (S7-300, S7-400, S7-1500)](#inserting-comments-s7-300-s7-400-s7-1500)
  
[Using and addressing operands](Programming%20basics.md#using-and-addressing-operands)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

### Displaying or hiding tag information (S7-300, S7-400, S7-1500)

#### Introduction

You can hide or show simple or hierarchical comments on the documentation of the tags, regardless of the absolute or symbolic representation of the operands. For local tags and DB tags, this information is obtained from the block interface. For tags that are valid for the entire CPU, the information is obtained from the PLC tag table.

You can display the tag information either for all the blocks or for individually opened blocks. If you display the tag information for all the blocks, the tag information for all blocks currently opened and opened in future is shown.

You can hide the tag information at any time again. If you have hidden the tag information for all blocks, you can display it again for individual ones that you have opened.

If you select the display of tag information with hierarchical comments, the comments of the higher structure levels of structured tags will also be displayed. The display is in brackets after the comment of the tags; the comments of the individual levels are separated by a period. If there is no comment at a structure level for a tag, it is omitted in the display and this is recognizable because there are two periods.

#### Displaying or hiding tag information for all blocks

Follow the steps below to display or hide the tag information for all blocks:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "PLC programming" group.
3. If you want to show the tag information, either select the "Expand" option in the "Tag information" drop-down list or the "Tag information with hierarchy" depending on whether you want to display simple or hierarchical comments.
4. If you want to hide the tag information, select the "Collapse" option in the "Tag information" drop-down list.

   The tag information is displayed or hidden for all blocks. When you open further blocks, the tag information is displayed or hidden depending on the selected setting.

#### Displaying or hiding tag information for an opened block

Follow the steps below to display or hide the tag information for an opened block:

1. If you want to show the tag information, either select the "Show tag information" option in the "Shows the tag information" drop-down list or the "Tag information with hierarchy" depending on whether you want to display simple or hierarchical comments.
2. If you want to hide the tag information, select the "Hide tag information" option in the "Hides tag information" drop-down list.

   The tag information is displayed or hidden.

### Using favorites in STL (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Adding STL elements to Favorites (S7-300, S7-400, S7-1500)](#adding-stl-elements-to-favorites-s7-300-s7-400-s7-1500)
- [Inserting STL instructions using favorites (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-favorites-s7-300-s7-400-s7-1500)
- [Removing STL instructions from Favorites (S7-300, S7-400, S7-1500)](#removing-stl-instructions-from-favorites-s7-300-s7-400-s7-1500)

#### Adding STL elements to Favorites (S7-300, S7-400, S7-1500)

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

[Inserting STL instructions using favorites (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-favorites-s7-300-s7-400-s7-1500)
  
[Removing STL instructions from Favorites (S7-300, S7-400, S7-1500)](#removing-stl-instructions-from-favorites-s7-300-s7-400-s7-1500)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

#### Inserting STL instructions using favorites  (S7-300, S7-400, S7-1500)

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
  
[Adding STL elements to Favorites (S7-300, S7-400, S7-1500)](#adding-stl-elements-to-favorites-s7-300-s7-400-s7-1500)
  
[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Removing STL instructions from Favorites (S7-300, S7-400, S7-1500)](#removing-stl-instructions-from-favorites-s7-300-s7-400-s7-1500)

#### Removing STL instructions from Favorites (S7-300, S7-400, S7-1500)

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

[Adding STL elements to Favorites (S7-300, S7-400, S7-1500)](#adding-stl-elements-to-favorites-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using favorites (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-favorites-s7-300-s7-400-s7-1500)
  
[Overview of the program editor](Program%20editor.md#overview-of-the-program-editor)

### Inserting block calls in STL (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Manually inserting block calls (S7-300, S7-400, S7-1500)](#manually-inserting-block-calls-s7-300-s7-400-s7-1500)
- [Inserting block calls using a drag-and-drop operation (S7-300, S7-400, S7-1500)](#inserting-block-calls-using-a-drag-and-drop-operation-s7-300-s7-400-s7-1500)
- [Updating block calls in STL (S7-300, S7-400, S7-1500)](#updating-block-calls-in-stl-s7-300-s7-400-s7-1500)
- [Changing the instance type (S7-300, S7-400, S7-1500)](#changing-the-instance-type-s7-300-s7-400-s7-1500)

#### Manually inserting block calls (S7-300, S7-400, S7-1500)

You can insert calls for functions (FCs) and function blocks (FBs). Function blocks can be called either as a single, multi or parameter instance.

See also: [Basics of instances](Programming%20basics.md#basics-of-instances)

##### Requirement

A network is available.

##### Inserting a call for a function (FC)

To insert a function call in an STL network, follow these steps:

1. Enter "CALL &lt;Name of the function to be called&gt;".

   Replace "&lt;Name of the function to be called&gt;" with the name of the function that you want to call.
2. Confirm your entry with the Enter key.

   - If the function already exists, all parameters of the function are inserted in the call.
   - If the function does not already exist, you must enter the parameters yourself.

##### Inserting a call for a function block (FB)

To insert the call for a function block (FB), follow these steps:

1. Enter "CALL &lt;Name of the function block to be called&gt;, &lt;Name of the instance data block&gt;".

   Replace "&lt;Name of the function to be called&gt;" with the name of the function block that you want to call. The instance data block entry is optional.
2. Confirm your entry with the Enter key.

   If you have not specified the instance data block or the instance data block you have specified does not exist, the "Call options" dialog is opened. In this case, perform steps 3 and 4.
3. In the dialog, enter whether you want to call the block as a single, multi or parameter instance.

   - If you click the "Single instance" button, enter a name for the data block that will be assigned to the call in the entry field "Name".

     If you call a block that contains monitoring, assign a ProDiag function block to the monitoring functions in the "ProDiag FB" text box.
   - If you click the "Multi instance" button, enter the name of the tag in the "Name in the interface" entry field, with which the called function block will be entered as a static tag in the interface of the calling block.
   - If you click on the "Parameter instance" button, enter the name of the in/out (InOut) parameter to which the instance should be passed during runtime in the "Name in the interface" text box.
4. Confirm your entries with "OK".

##### Result

When you call existing functions or function blocks with an instance data block, the parameters of the function or function block are inserted into the call. You must then assign these parameters.

See also: [Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

If when calling a function block you specify an instance data block that does not exist, it will be created.

---

**See also**

[Inserting block calls using a drag-and-drop operation (S7-300, S7-400, S7-1500)](#inserting-block-calls-using-a-drag-and-drop-operation-s7-300-s7-400-s7-1500)
  
[Updating block calls in STL (S7-300, S7-400, S7-1500)](#updating-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Changing the instance type (S7-300, S7-400, S7-1500)](#changing-the-instance-type-s7-300-s7-400-s7-1500)
  
[Parameter assignment via registers during block call in STL (S7-300, S7-400, S7-1500)](#parameter-assignment-via-registers-during-block-call-in-stl-s7-300-s7-400-s7-1500)

#### Inserting block calls using a drag-and-drop operation (S7-300, S7-400, S7-1500)

You can insert calls for existing functions (FC) and function blocks (FB) using a drag-and-drop operation from the project tree. Function blocks can be called either as a single, multi or parameter instance.

See also: [Basics of instances](Programming%20basics.md#basics-of-instances)

##### Requirement

- A network is available.
- The function to be called (FC) or the function block (FB) to be called is present.

##### Inserting a call for a function (FC)

To insert a function call in an STL network using a drag-and-drop operation, follow these steps:

1. Drag the function from the project tree into the network.

##### Inserting a call for a function block (FB)

To insert the call for a function block (FB), follow these steps:

1. Drag the function block from the project tree into the network.

   The "Call options" dialog opens.
2. In the dialog, enter whether you want to call the block as a single, multi or parameter instance.

   - If you click the "Single instance" button, enter a name for the instance data block to be assigned to the call in the entry field "Name".

     If you call a block that contains monitoring, assign a ProDiag function block to the monitoring functions in the "ProDiag FB" text box.
   - If you click the "Multi-instance" button, in the "Name in the interface" box, enter a name of the tag with which the called function block will be entered as a static tag in the interface of the calling block.
   - If you click on the "Parameter instance" button, enter the name of the in/out (InOut) parameter to which the instance should be passed during runtime in the "Name in the interface" text box.
3. Confirm your entries with "OK".

##### Result

The function or the function block is inserted with its parameters. You must then assign these parameters.

See also: [Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

If when calling a function block you specify an instance data block that does not exist, it will be created.

---

**See also**

[Manually inserting block calls (S7-300, S7-400, S7-1500)](#manually-inserting-block-calls-s7-300-s7-400-s7-1500)
  
[Updating block calls in STL (S7-300, S7-400, S7-1500)](#updating-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Changing the instance type (S7-300, S7-400, S7-1500)](#changing-the-instance-type-s7-300-s7-400-s7-1500)

#### Updating block calls in STL (S7-300, S7-400, S7-1500)

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

[Manually inserting block calls (S7-300, S7-400, S7-1500)](#manually-inserting-block-calls-s7-300-s7-400-s7-1500)
  
[Inserting block calls using a drag-and-drop operation (S7-300, S7-400, S7-1500)](#inserting-block-calls-using-a-drag-and-drop-operation-s7-300-s7-400-s7-1500)
  
[Changing the instance type (S7-300, S7-400, S7-1500)](#changing-the-instance-type-s7-300-s7-400-s7-1500)
  
[Block calls](Programming%20basics.md#block-calls)

#### Changing the instance type (S7-300, S7-400, S7-1500)

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

[Manually inserting block calls (S7-300, S7-400, S7-1500)](#manually-inserting-block-calls-s7-300-s7-400-s7-1500)
  
[Inserting block calls using a drag-and-drop operation (S7-300, S7-400, S7-1500)](#inserting-block-calls-using-a-drag-and-drop-operation-s7-300-s7-400-s7-1500)
  
[Updating block calls in STL (S7-300, S7-400, S7-1500)](#updating-block-calls-in-stl-s7-300-s7-400-s7-1500)
  
[Instances](Programming%20basics.md#instances)

### Inserting comments (S7-300, S7-400, S7-1500)

#### Commenting program code

Various options are available for commenting STL programs:

- Line comment

  A line comment starts with "//" and extends to the end of the line.
- Comment section within a line

  A comment section is started with "(* and completed by "*)". A comment section can be located at any point in the line, but cannot extend over several lines.

#### Requirement

A network is available.

#### Inserting line comments

To insert a line comment into an instruction line, follow these steps:

1. Enter "//" at the end of the instruction line.
2. Enter the comment.

#### Inserting a comment section within a line

Proceed as follows to insert a comment section within an instruction line:

1. Enter a "(*" at any point in the instruction line.
2. Enter the comment after "(*".
3. Enter "*)" after the comment.

#### Disabling one or more lines with comments

To disable program code with with comments, follow these steps:

1. Select the code lines you want to comment out.
2. Click the "Comment selection" button in the editor.
3. "//" is inserted at the beginning of the line in the selected lines. The code that follows is interpreted as a comment. If lines already containing a line comment are disabled, "//" is inserted as well. If the lines are then enabled again, original comments are retained.

#### Enabling comment lines

To enable lines that have been commented out to be enabled as code again, proceed as follows:

1. Select the code lines you want to enable.
2. Click the "Remove comment" button in the editor.
3. The "//" mark for line comments at the beginning of the line is removed.

#### Result

Comments are formatted with highlighting.

---

**See also**

[Rules for STL (S7-300, S7-400, S7-1500)](#rules-for-stl-s7-300-s7-400-s7-1500)
  
[Entering STL instructions manually (S7-300, S7-400, S7-1500)](#entering-stl-instructions-manually-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions using the "Instructions" task card (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-using-the-instructions-task-card-s7-300-s7-400-s7-1500)
  
[Inserting operands (S7-300, S7-400, S7-1500)](#inserting-operands-s7-300-s7-400-s7-1500)
  
[Using favorites in STL (S7-300, S7-400, S7-1500)](#using-favorites-in-stl-s7-300-s7-400-s7-1500)
  
[Inserting block calls in STL (S7-300, S7-400, S7-1500)](#inserting-block-calls-in-stl-s7-300-s7-400-s7-1500)

## Editing STL instructions (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Selecting STL instructions (S7-300, S7-400, S7-1500)](#selecting-stl-instructions-s7-300-s7-400-s7-1500)
- [Copying STL instructions (S7-300, S7-400, S7-1500)](#copying-stl-instructions-s7-300-s7-400-s7-1500)
- [Cutting STL instructions (S7-300, S7-400, S7-1500)](#cutting-stl-instructions-s7-300-s7-400-s7-1500)
- [Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)](#pasting-stl-instructions-from-the-clipboard-s7-300-s7-400-s7-1500)
- [Deleting STL instructions (S7-300, S7-400, S7-1500)](#deleting-stl-instructions-s7-300-s7-400-s7-1500)

### Selecting STL instructions (S7-300, S7-400, S7-1500)

You can select individual instructions or all the instructions of a network.

#### Requirement

STL instructions are available.

#### Selecting individual STL instructions

To select STL instructions, follow these steps:

1. Set the insertion mark before the first character that you want to select.
2. Press and hold down the left mouse button.
3. Move the cursor to a position after the last character that you want to select.
4. Release the left mouse button.

#### Selecting all STL instructions of a network

To select all instructions of a network, follow these steps:

1. Click in the network whose instructions you want to select.
2. Select "Select All" from the "Edit" menu or use the keyboard shortcut &lt;Ctrl+A&gt;.

---

**See also**

[Copying STL instructions (S7-300, S7-400, S7-1500)](#copying-stl-instructions-s7-300-s7-400-s7-1500)
  
[Cutting STL instructions (S7-300, S7-400, S7-1500)](#cutting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)](#pasting-stl-instructions-from-the-clipboard-s7-300-s7-400-s7-1500)
  
[Deleting STL instructions (S7-300, S7-400, S7-1500)](#deleting-stl-instructions-s7-300-s7-400-s7-1500)

### Copying STL instructions (S7-300, S7-400, S7-1500)

#### Requirement

An STL instruction is available.

#### Procedure

To copy an STL instruction, follow these steps:

1. Select the STL instruction you want to copy.
2. Select "Copy" in the shortcut menu.

#### Result

The STL instruction is copied and saved to the clipboard.

---

**See also**

[Selecting STL instructions (S7-300, S7-400, S7-1500)](#selecting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Cutting STL instructions (S7-300, S7-400, S7-1500)](#cutting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)](#pasting-stl-instructions-from-the-clipboard-s7-300-s7-400-s7-1500)
  
[Deleting STL instructions (S7-300, S7-400, S7-1500)](#deleting-stl-instructions-s7-300-s7-400-s7-1500)

### Cutting STL instructions (S7-300, S7-400, S7-1500)

#### Requirement

An STL instruction is available.

#### Procedure

To cut an STL instruction, follow these steps:

1. Select the STL instruction you want to cut.
2. Select "Cut" in the shortcut menu.

#### Result

The STL instruction is cut and saved to the clipboard.

---

**See also**

[Selecting STL instructions (S7-300, S7-400, S7-1500)](#selecting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Copying STL instructions (S7-300, S7-400, S7-1500)](#copying-stl-instructions-s7-300-s7-400-s7-1500)
  
[Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)](#pasting-stl-instructions-from-the-clipboard-s7-300-s7-400-s7-1500)
  
[Deleting STL instructions (S7-300, S7-400, S7-1500)](#deleting-stl-instructions-s7-300-s7-400-s7-1500)

### Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)

#### Requirement

An STL instruction is available.

#### Procedure

To paste an STL instruction from the Clipboard, follow these steps:

1. Copy an STL instruction or cut an STL instruction.
2. Click the place in the network where you want to insert the STL instruction.
3. Select "Paste" in the shortcut menu.

---

**See also**

[Selecting STL instructions (S7-300, S7-400, S7-1500)](#selecting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Copying STL instructions (S7-300, S7-400, S7-1500)](#copying-stl-instructions-s7-300-s7-400-s7-1500)
  
[Cutting STL instructions (S7-300, S7-400, S7-1500)](#cutting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Deleting STL instructions (S7-300, S7-400, S7-1500)](#deleting-stl-instructions-s7-300-s7-400-s7-1500)

### Deleting STL instructions (S7-300, S7-400, S7-1500)

#### Requirement

An STL instruction is available.

#### Procedure

To delete an STL instruction, follow these steps:

1. Select the STL instruction you want to delete.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Selecting STL instructions (S7-300, S7-400, S7-1500)](#selecting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Copying STL instructions (S7-300, S7-400, S7-1500)](#copying-stl-instructions-s7-300-s7-400-s7-1500)
  
[Cutting STL instructions (S7-300, S7-400, S7-1500)](#cutting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Pasting STL instructions from the Clipboard (S7-300, S7-400, S7-1500)](#pasting-stl-instructions-from-the-clipboard-s7-300-s7-400-s7-1500)

## STL programming examples (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
- [Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
- [Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
- [Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
- [Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)
- [Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)

#### Controlling a conveyor belt

The following figure shows a conveyor belt that can be activated electrically. There are two pushbuttons at the beginning of the conveyor belt: S1 for START and S2 for STOP. There are also two pushbuttons at the end of the conveyor belt: S3 for START and S4 for STOP. It is possible to start and stop the conveyor belt from either end.

![Controlling a conveyor belt](images/70908454283_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Operand | Declaration | Data type | Description |
| --- | --- | --- | --- |
| StartPushbutton_Left (S1) | Input | BOOL | Start pushbutton on the left side of the conveyor belt |
| StopPushbutton_Left (S2) | Input | BOOL | Stop pushbutton on the left side of the conveyor belt |
| StartPushbutton_Right (S3) | Input | BOOL | Start pushbutton on the right side of the conveyor belt |
| StopPushbutton_Right (S4) | Input | BOOL | Stop pushbutton on the right side of the conveyor belt |
| MOTOR_ON | Output | BOOL | Turn on the conveyor belt motor |

The following STL program shows how to implement this task:

| STL | Explanation |
| --- | --- |
| O #S1 | // Scan start pushbutton S1 for "1". |
| O #S3 | // Scan start pushbutton S3 for "1". |
| S #MOTOR_ON | // If one of the start pushbuttons (S1 or S3) returns the signal state "1", the conveyor belt motor is switched on. |
| O #S2 | // Scan stop pushbutton S2 for "1". |
| O #S4 | // Scan stop pushbutton S4 for "1". |
| R #MOTOR_ON | // If one of the stop pushbuttons (S2 or S4) returns the signal state "1", the conveyor belt motor is switched off. |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
  
[Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
  
[Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)
  
[Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)

#### Detecting the direction of a conveyor belt

The detected running direction of the belt is indicated by a RIGHT arrow or a LEFT arrow. If additional conveyed material is approaching PEB1 from the right or PEB2 from the left, the displayed arrow is initially switched off until, after both photoelectric barriers are passed, the running direction can be detected again and the corresponding arrow displayed. For the solution of the task, 2 edge memory bits are needed that detect the signal change from "0" to "1" at the two photoelectric barriers.

![Detecting the direction of a conveyor belt](images/41375220491_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Declaration | Data type | Description |
| --- | --- | --- | --- |
| S1 | Input | BOOL | Photoelectric barrier 1 |
| S2 | Input | BOOL | Photoelectric barrier 2 |
| TM1 | Input | BOOL | Edge bit memory 1 |
| TM2 | Input | BOOL | Edge bit memory 2 |
| RIGHT | Output | BOOL | Display for movement to the right |
| LEFT | Output | BOOL | Display for movement to the left |

The following STL program shows how to implement this example:

| STL | Explanation |
| --- | --- |
| A #S1 | // Scan photoelectric barrier "S1" for "1" |
| FP #TM1 | // Query positive edge |
| AN #S2 | // Scan photoelectric barrier "S2" for "0" |
| S #LEFT | //If the signal state changes from "0" to "1" (positive edge) at the photoelectric barrier "S1" and, at the same time, the signal state at the photoelectric barrier "S2" is "0", the object on the belt is moving to the left.  // The display for movement to the left is activated. |
| A #S2 | // Scan photoelectric barrier "S2" for "1" |
| FP #TM2 | // Query positive edge |
| AN #S1 | // Scan photoelectric barrier "S1" for "0" |
| S #RIGHT | //If the signal state changes from "0" to "1" (positive edge) at photoelectric barrier "S2" and, at the same time, the signal state at photoelectric barrier "S1" is "0", the object on the belt is moving to the right.  // The display for movement to the right is activated. |
| AN #S1 | // Scan photoelectric barrier "S1" for "0" |
| AN #S2 | // Scan photoelectric barrier "S2" for "0" |
| R #LEFT | // The display for movement to the left will be turned off when the signal state at both photoelectric barriers is "0". |
| R #RIGHT | // The display for movement to the right will be turned off when the signal state at both photoelectric barriers is "0". |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
  
[Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
  
[Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)
  
[Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example of detecting the fill level of a storage area  (S7-300, S7-400, S7-1500)

#### Detecting the fill level of a storage area

The following figure shows a system with two conveyor belts and a temporary storage area between them. Conveyor belt 1 delivers packages to the storage area. A photoelectric barrier at the end of conveyor belt 1 near the storage area detects how many packages are delivered to the storage area. Conveyor belt 2 transports packages from the temporary storage area to a loading dock where they are loaded onto trucks. A photoelectric barrier at the storage area exit detects how many packages leave the storage area to be transported to the loading dock. Five display lamps indicate the capacity of the temporary storage area.

![Detecting the fill level of a storage area](images/41381535883_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the definition of the tags used:

| Name | Data type | Address | Description |
| --- | --- | --- | --- |
| PACKAGECOUNT | COUNTER | C1 | Number of packages in the storage area (current count value) |

| Name | Section | Data type | Description |
| --- | --- | --- | --- |
| LS1 | Input | BOOL | Photoelectric barrier 1 |
| LS2 | Input | BOOL | Photoelectric barrier 2 |
| STOR_EMPTY | Output | BOOL | Display lamp: Storage area empty |
| STOR_NOT_EMPTY | Output | BOOL | Display lamp: Storage area not empty |
| STOR_50%_FULL | Output | BOOL | Display lamp: Storage area 50% full |
| STOR_90%_FULL | Output | BOOL | Display lamp: Storage area 90% full |
| STOR_FULL | Output | BOOL | Display lamp: Storage area full |

The following STL program shows how to implement this example:

| STL | Explanation |
| --- | --- |
| A #LS1 | // Scan photoelectric barrier "LS1" for "1". |
| CU "PACKAGECOUNT" | // In the event of a positive signal edge at photoelectric barrier "LS1", the count value of counter "PACKAGECOUNT" is increased by one. |
| A #LS2 | // Scan photoelectric barrier "LS2" for "1". |
| CD "PACKAGECOUNT" | // In the event of a positive signal edge at photoelectric barrier "LS2", the count value of counter "PACKAGECOUNT" is decreased by one. |
| AN "PACKAGECOUNT" | // Scan count value for "0". |
| = #STOR_EMPTY | // With a count value of "0" the display lamp "storage area empty" is switched on. |
| A "PACKAGECOUNT" | // Scan count value for "1". |
| = #STOR_NOT_EMPTY | // With a count value greater than "0" the display lamp "Storage area not empty" is switched on. |
| L 50 | // Load the comparison value "50" to accumulator 1. |
| L "PACKAGECOUNT" | // Move the comparison value to accumulator 2.  // Load the current count value to accumulator 1. |
| &lt;=I | // Compare values |
| = #"STOR_50%_FULL" | // With a count value greater than or equal to "50" the display lamp "Storage area 50% full" is switched on. |
| L 90 | // Move the counter value to accumulator 2.  // Load the comparison value "90" to accumulator 1. |
| &gt;=I | // Compare values |
| = #"STOR_90%_FULL" | // With a count value greater than or equal to "90" the display lamp "Storage area 90% full" is switched on. |
| L "PACKAGECOUNT" | // Load the current count value to accumulator 1. |
| L 100 | // Move the counter value to accumulator 2.  // Load the comparison value "100" to accumulator 1. |
| &gt;=I | // Compare values |
| = #STOR_FULL | // At a count value greater than "100" the display lamp "Storage area full" is switched on. |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
  
[Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)
  
[Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example of calculating an equation (S7-300, S7-400, S7-1500)

#### Calculating an equation

The sample program shows you how to use three math instructions to calculate the following equation:

RESULT = ((A + B) x C) /D

#### Implementation

The following table shows the declaration of the operands used in the PLC tag table:

| Name | Data type | Comment |
| --- | --- | --- |
| A | INT | First value for addition |
| B | INT | Second value for addition |
| C | INT | Multiplier |
| D | INT | Divisor |
| RESULT | INT | End result |

The following STL program shows how to implement this example:

| STL | Explanation |
| --- | --- |
| L "A" | // Load value of the operand "A" to accumulator 1 |
| L "B" | // Load value of operand "A" to accumulator 2  // Load value of the operand "B" to accumulator 1 |
| +I | // Add the values of accumulator 1 and 2  // Store sum in accumulator 1 |
| L "C" | // Move the sum to accumulator 2  // Load value of the operand "C" to accumulator 1 |
| *I | // Multiply the values of accumulator 1 and 2  // Store product in accumulator 1 |
| L "D" | // Move the product to accumulator 2  // Load value of the operand "D" to accumulator 1 |
| /I | // Divide the value of accumulator 2 by the value of accumulator 1  // Store result in accumulator 1 |
| T "RESULT" | // Transfer the result to operand "RESULT" |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
  
[Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)
  
[Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example for heating an oven   (S7-300, S7-400, S7-1500)

#### Heating an oven

The following illustration shows an oven that is turned on with a start switch. The heating process is started when the start switch is pressed. The heating period is set with digital thumbwheels. The heating period is set in seconds using the BCD format.

![Heating an oven](images/18747366155_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the declaration of the operands used in the PLC tag table:

| Name | Data type | Address | Comment |
| --- | --- | --- | --- |
| DURATION | WORD | EW0 | Heating period in seconds  - I1.0 to I1.3: Thumbwheels for ones - I1.4 to I1.7: Thumbwheels for tens - I0.0 to I0.3: Thumbwheels for hundreds |
| HEATING | TIMER | T1 | Time that is started with the preset heating period. |

The following table shows the declaration of the operands used in the block interface of the code block:

| Name | Section | Data type | Comment |
| --- | --- | --- | --- |
| START | Input | BOOL | Start switch |
| START_HEATING | Output | BOOL | Start of the heating process |

The following STL program shows how to implement this example:

| STL | Explanation |
| --- | --- |
| A "HEATING" | // Scan to see if time has started |
| = #START_HEATING | // Start the heating process |
| BEC | // For RLO=1 End processing of block   // This prevents the "HEATING" time from being restarted if the button is pressed |
| L "DURATION" | // Load the heating period in accumulator 1 |
| AW W#16#0FFF | // Reset input bits I0.4 to I0.7 to "0" |
| OW W#16#4000 | // Set seconds in bits I1.2 and I1.3 of accumulator 1 |
| A #START | // Scan start switch for "1" |
| SE "HEATING" | // Start heating process as an extended pulse upon a positive signal edge at the start switch |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
  
[Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
  
[Example of a step sequence (S7-300, S7-400, S7-1500)](#example-of-a-step-sequence-s7-300-s7-400-s7-1500)

### Example of a step sequence (S7-300, S7-400, S7-1500)

#### Programming a step sequence

The following figure shows a station for removing glass containers from a pallet. The pallets are transported on a conveyor belt to the station. When a pallet with glass containers reaches the station, the conveyor belt will be stopped and a gripper moves from its basic position (P0) to the position above the pallet (P2). Once the gripper is above the pallet, the gripping clamps will open and the gripper lowered. Sensors detect the actual position of the gripper and the status of the gripping clamps. The sequence of the gripper movement in this example is implemented by a step sequence. You can program the additional steps required for removing the bottles and transporting them on an additional conveyor belt.

![Programming a step sequence](images/18764833931_DV_resource.Stream@PNG-en-US.png)

#### Implementation

The following table shows the declaration of the operands used in the PLC tag table:

| Name | Data type | Comment |
| --- | --- | --- |
| NUMBER | INT | Step number |
| Tag_Error | BOOL | Operand that is set when the step number is greater than 3 or if one of the steps was not executed. |

The following table shows the declaration of the operands used in the block interface of the code block:

| Name | Section | Data type | Comment |
| --- | --- | --- | --- |
| POS_0 | Input | BOOL | Gripper in basic position (P0) |
| POS_1 | Input | BOOL | Gripper in position 1 (P1) |
| POS_2 | Input | BOOL | Gripper in position 2 (P2) |
| GRIPPER_OPEN | Input | BOOL | Gripping clamps open |
| OUT_POS_1 | Output | BOOL | Move gripper to position 1 |
| OUT_POS_2 | Output | BOOL | Move gripper to position 2 |
| OUT_GRIPPER | Output | BOOL | Open gripping clamps |
| OUT_POS_3 | Output | BOOL | Move gripper to position 3 |

The following STL program shows how to implement this example:

| STL | Explanation |
| --- | --- |
| L "NUMBER" | // Load the step number to accumulator 1. |
| JL END | // Start of the jump list |
| JU POSITION_0 | // At a value of "0" in the accumulator 1 jump to jump label "POSITION_0". |
| JU POSITION_1 | // At a value of "1" in the accumulator 1 jump to jump label "POSITION_1". |
| JU POSITION_2 | // At a value of "2" in the accumulator 1 jump to jump label "POSITION_2". |
| JU POSITION_3 | // At a value of "3" in the accumulator 1 jump to jump label "POSITION_3". |
| END: JU ERROR | // End of the jump list  // At a step number greater than 3 jump to jump label "ERROR". |
| POSITION_0: A #POS_0 | // Jump label "POSITION_0"  // Scan to see if gripper is in basic position (P0). |
| = #OUT_POS_1 | // If condition is met, set output "OUT_POS_1" and move gripper to position 1 (P1). |
| JCN ERROR | // With RLO "0" jump to jump label "ERROR". |
| JC NEXT | // With RLO "1" jump to jump label "NEXT". |
| POSITION_1: A #POS_1 | // Jump label "POSITION_1"  // Scan to see if gripper is in position 1 (P1). |
| = #OUT_POS_2 | // If condition is met, set output "OUT_POS_2" and move gripper to position 2 (P2). |
| JCN ERROR | // With RLO "0" jump to jump label "ERROR". |
| JC NEXT | // With RLO "1" jump to jump label "NEXT". |
| POSITION_2: A #POS_2 | // Jump label "POSITION_2"  // Scan to see if gripper is in position 2 (P2). |
| = #OUT_GRIPPER | // If condition is met, set output "OUT_GRIPPER" and open gripping clamps. |
| JCN ERROR | // With RLO "0" jump to jump label "ERROR". |
| JC NEXT | // With RLO "1" jump to jump label "NEXT". |
| POSITION_3: A #POS_2 | // Jump label "POSITION_3"  // Scan to see if gripper is in position 2 (P2). |
| A #GRIPPER_OPEN | // Scan to see if the gripping clamps are open |
| = #OUT_POS_3 | // If condition is met, set output "OUT_POS_3" and move gripper to position 3 (P3). |
| JCN ERROR | // With RLO "0" jump to jump label "ERROR". |
| JC NEXT | // With RLO "1" jump to jump label "NEXT". |
| NEXT: INC 1 | // Jump label "NEXT"  // Increase step number in accumulator 1 by one. |
| T "NUMBER" | // Transfer step number to operand "NUMBER". |
| L 3 | // Move the current step number to accumulator 2.  // Load value 3 to accumulator 1. |
| &gt;I | // Scan to see if current step number is greater than 3. |
| JC RESET_NUMBER | // With a scan result "1" jump to jump label "RESET_NUMBER" and continue with program processing |
| BEU | // End block |
| RESET_NUMBER: L 0 | // Jump label "RESET_NUMBER"  // Load value "0" in accumulator 1. |
| T "NUMBER" | // Assign value "0" to operands "NUMBER" (step number). |
| BEU | // End block |
| ERROR: NOT | // Jump label "ERROR" |
| = "Tag_Error" | // Assign negated RLO to the operand "Tag_Error". |
| BEU | // End block |

---

**See also**

[STL Basics (S7-300, S7-400, S7-1500)](#stl-basics-s7-300-s7-400-s7-1500)
  
[Settings for STL (S7-300, S7-400, S7-1500)](#settings-for-stl-s7-300-s7-400-s7-1500)
  
[Working with networks (S7-300, S7-400, S7-1500)](#working-with-networks-s7-300-s7-400-s7-1500)
  
[Inserting STL instructions (S7-300, S7-400, S7-1500)](#inserting-stl-instructions-s7-300-s7-400-s7-1500)
  
[Editing STL instructions (S7-300, S7-400, S7-1500)](#editing-stl-instructions-s7-300-s7-400-s7-1500)
  
[Example of controlling a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-controlling-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the direction of a conveyor belt (S7-300, S7-400, S7-1500)](#example-of-detecting-the-direction-of-a-conveyor-belt-s7-300-s7-400-s7-1500)
  
[Example of detecting the fill level of a storage area (S7-300, S7-400, S7-1500)](#example-of-detecting-the-fill-level-of-a-storage-area-s7-300-s7-400-s7-1500)
  
[Example of calculating an equation (S7-300, S7-400, S7-1500)](#example-of-calculating-an-equation-s7-300-s7-400-s7-1500)
  
[Example for heating an oven (S7-300, S7-400, S7-1500)](#example-for-heating-an-oven-s7-300-s7-400-s7-1500)

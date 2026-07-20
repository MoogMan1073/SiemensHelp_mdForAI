---
title: "Program editor"
package: ProgPLCProgramEditorenUS
topics: 31
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Program editor

This section contains information on the following topics:

- [Overview of the program editor](#overview-of-the-program-editor)
- [Using the keyboard in the program editor](#using-the-keyboard-in-the-program-editor)
- [Enlarging the programming window](#enlarging-the-programming-window)
- [Setting the mnemonics](#setting-the-mnemonics)
- [Displaying symbolic and absolute addresses](#displaying-symbolic-and-absolute-addresses)
- [Find instructions](#find-instructions)
- [Editing multilingual project texts in blocks](#editing-multilingual-project-texts-in-blocks)
- [Use instruction versions](#use-instruction-versions)
- [Using instruction profiles](#using-instruction-profiles)
- [Using autocompletion](#using-autocompletion)
- [General settings for the PLC programming](#general-settings-for-the-plc-programming)
- [Eliminating syntax errors in the program](#eliminating-syntax-errors-in-the-program)
- [Changing the programming language](#changing-the-programming-language)

## Overview of the program editor

### Function of the program editor

The program editor is the integrated development environment for programming functions, function blocks, and organization blocks. If offers comprehensive support for programming and troubleshooting.

The appearance and functionality of the program editor can vary depending on the CPU, programming language and block type used.

### Structure of the program editor

Using LAD as an example, the following figure shows the components of the program editor:

![Structure of the program editor](images/95951186571_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Block interface |
| ③ | "Favorites" pane in the "Instructions" task card and favorites in the programming window |
| ④ | Programming window |
| ⑤ | "Instructions" task card |
| ⑥ | "Testing" task card |

### Toolbar

The toolbar allows you to access the principal functions of the program editor, such as:

- Show and hide absolute operands
- Showing and hiding favorites
- Skip to syntax errors
- Update block calls
- Show and hide program status

The functions available in the toolbar can vary depending on the programming language used.

### Block interface

The block interface contains the declarations for local tags used solely within the block. The sections available depend on the block type.

### Favorites

You can save frequently used instructions as favorites. These favorites are then displayed in the "Instructions" task card and the "Favorites" pane. You can also display favorites in the programming window using the program editor toolbar. This allows you to access your favorites even when the "Instructions" task card is not visible.

### Programming window

The programming window is the work area of the program editor. You can enter the program code in this window. The appearance and functionality of the program window can vary depending on the programming language used.

### "Instructions" task card

The "Instructions" task card offers you easy access to all instructions available for creating your program. The instructions are broken down by area into a number of different palettes. If an instruction profile is active, the offered instructions may vary. You receive a brief description for each instruction. If several versions of an instruction are available, the versions are listed in a drop-down list and the currently selected version is used in the program. If required, you can select a different instruction version. Read the information in the section "[Basic information on instruction versions](#basic-information-on-instruction-versions)".

With the task card toolbar, you can access the following functions:

- Search up or down for instructions

  You have the option of searching the panes for specific instructions.
- Upgrade project and instructions

  If you are still working with a project which was created with TIA Portal V14, only the instruction versions from V14 will be available. Using the "Upgrade project and instructions" button you can easily upgrade your project to TIA Portal V14 SP1. The "Instructions" task card then receives the new instruction versions of TIA Portal V14 SP1.

  > **Note**
  >
  > Please note the following:
  >
  > - Your program is not changed by the upgrade, i.e. it still contains the old instruction versions from V14. To use the new instruction versions you must update your program.
  > - The "project and operation upgrade" button is only active if you are still working with a TIA Portal V14 project. The button becomes inactive as soon as you upgrade your project to TIA Portal V14 SP1.
- Update program in the current PLC

  Updates the CPU program to the new instruction versions.
- Changing the pane mode

  You can choose between single and multi-pane mode.

  See also: [Change pane mode](Introduction%20to%20the%20TIA%20Portal.md#changing-the-pane-mode)
- Showing/hiding column headers

  You can show or hide column headers in the panes. You can modify the arrangement of columns by clicking a column header and moving the column to the new position by means of drag-and-drop.

### "Testing" task card

You can set settings in the "Testing" task card for troubleshooting using the program status. The functions of the "Testing" task card are only available in online mode. It contains the following panes, which are displayed depending on the selected CPU and the configured programming language of the block:

- CPU operator panel

  The CPU operator panel allows you to switch the CPU operating mode.
- Breakpoints

  You can test blocks you created in the textual programming languages STL and SCL in single step mode. To do this, set breakpoints in the program code.

  In the "Breakpoints" pane, you can find all breakpoints that you have set and you can activate, delete, navigate to, or set the call environment for the individual breakpoints.
- PLC register

  This pane allows you to read off the values for the PLC registers and the accumulators.
- Sequence control

  In this pane you can set the operating mode for testing sequencers for GRAPH blocks.
- Test settings

  This pane allows you to specify the test settings for the GRAPH block.
- Call environment

  This pane allows you to specify the call environment for the block.
- Call hierarchy

  In this pane, you can trace the call hierarchy of the blocks. You only see the call hierarchy during block monitoring.

---

**See also**

[Overview of the block interface](Declaring%20the%20block%20interface.md#overview-of-the-block-interface)
  
[Changing the mode of a CPU](Device%20and%20network%20diagnostics.md#changing-the-mode-of-a-cpu)
  
[Enlarging the programming window](#enlarging-the-programming-window)
  
[Find instructions](#find-instructions)
  
[Using instruction profiles](#using-instruction-profiles)

## Using the keyboard in the program editor

### **Keyboard shortcuts**

The following tables show the keyboard operations that are available to you when programming:

All tables
General keyboard shortcuts: Navigating
General keyboard shortcuts: Enter operands
General keyboard shortcuts: Monitor program
LAD/FBD
STL
CEM
GRAPH
SCL
Editor for named value data types

General keyboard shortcuts: Navigating

| Navigating with the keyboard | Selected object | Keyboard shortcut |
| --- | --- | --- |
| Open "Instructions" task card | Any | <Ctrl+Shift+C> |
| Open "Testing" task card | Any | <Ctrl+Shift+O> |
| Add new block | Any | <Ctrl+N> |
| Open block/PLC data type | Any | <F7> |
| Open a drop-down list  You can open drop-down lists with <ALT+F2> and then navigate with the arrow keys to scroll through the drop-down list. Finally, press the <Enter> key to confirm your selection. | Object that contains a drop-down list | <Alt+F2> |
| Display configuration menu | Object that contains a configuration menu | <F4> |
| Open autocompletion | Any | <Ctrl+I> or <Ctrl+Spacebar> |
| Open "Call options" dialog | Cursor position before or after a block call | <Return> |
| Expand all networks/palettes | Any | <Alt +F11> |
| Reduce all networks/palettes | Any | <Alt+F12> |
| Insert network | Any | <Ctrl+R> |
| Navigate between objects in the network | Object in the network | Arrow keys |
| Navigate to the first element of the network | Object in the network | <Home> |
| Navigate to the last element of the network | Object in the network | <End> |
| Navigate to the next element of the network | Object in the network | <Tab> |
| Navigate to the previous element of the network | Object in the network | <Shift+Tab> |
| To the next network | Network title | <Down arrow> |
| To the previous network | Network title | <Up arrow> |
| Navigate to the next point of use of the selected block or operand | Block or operand | <Ctrl+Shift+G> |
| Navigate to the previous point of use of the selected block or operand | Block or operand | <Ctrl+Shift+F> |
| Navigate to the next read/write access | Block or operand | <Alt+F8> |
| Navigate to the previous read/write access | Block or operand | <Alt+F9> |
| Navigate to the definition of the selected block or operand | Block or operand | <Ctrl+Shift+D> |

General keyboard shortcuts: Enter operands

| Enter operands with the keyboard | Selected object | Keyboard shortcut |
| --- | --- | --- |
| Activate the text box for the first operand of the instruction | Instruction | <Return>  Or  <Any letters/numbers>   An empty text box opens on <Return>, any letters or numbers are entered in the text box. |
| Activate text box for the operand | Operand | <F2> |
| Enter operands | Text box for operands | <Any letters/numbers> |
| Confirm entry of the operand | Text box for operands | <Return> |
| Open autocompletion | Text box for operands | <Ctrl+I> or  <Ctrl+Space> |
| Discard current change | Text box for operands | <Esc>   The text box is disabled and the previous contents restored. |
| Delete operand | Operand | <Del> |
| Define tag | Operand | <Ctrl+Shift+I> |
| Rewire tag | Operand | <Ctrl+Shift+P> |
| Rename tag | Operand | <Ctrl+Shift+T> |

General keyboard shortcuts: Monitor program

| Monitor program with the keyboard | Keyboard shortcut |
| --- | --- |
| Set/delete breakpoint | <Ctrl+Shift+F9> |
| Skip breakpoint | <Ctrl+Shift+F10> |
| Jump to a nested block | <Ctrl+Shift+F11> |
| Jump back to the calling block | <Ctrl+Shift+F12> |
| Run program up to marker (cursor position) | <Ctrl+F3> |
| Display program status | <Ctrl+T> |
| Enable all breakpoints | <Ctrl+Shift+F2> |
| Disable all breakpoints | <Ctrl+Shift+F3> |
| Modify to 0 | <Ctrl+Shift+9> |
| Modify to 1 | <Ctrl+Shift+1> |
| Modify operand | <Ctrl+Shift+2> |

LAD/FBD

| Operate LAD/FBD with the keyboard | Selected object | Keyboard shortcut |
| --- | --- | --- |
| Insert normally open contact | LAD: Rung | <F9> |
| Insert normally closed contact | LAD: Rung | <F10> |
| Insert empty box | LAD: Rung  FBD: Network | <F8> |
| Insert assignment | LAD: Rung  FBD: Network, input or output | <Shift+F7> |
| Open branch | LAD: Rung  FBD: Connecting line between two boxes | <Shift+F8> |
| Close branch | LAD: Rung | <Shift+F9> |
| Insert AND logic operation | FBD: Network, input or output | <F9> |
| Insert OR logic operation | FBD: Network, input or output | <F10> |
| Create a ones complement | FBD: Network, input or output | <Ctrl+Shift+4> |
| Insert input | FBD: Network, input or output | <Ctrl+Shift+3> |

STL

| Operate the STL with the keyboard | Selected object | Keyboard shortcut |
| --- | --- | --- |
| Comment out selection | Line | <Ctrl+Shift+Y> |
| Remove comment | Line | <Ctrl+Shift+U> |

CEM

| Operate CEM with the keyboard | Area | Keyboard shortcut |
| --- | --- | --- |
| Add cause | Any | <Ctrl+R> |
| Add effect | Any | <Ctrl+Shift+R> |
| Add input | Cause | <Ctrl+Shift+3> |
| Add output | Effect | <Ctrl+Shift+3> |
| Create a ones complement | Operand or connection | <Ctrl+Shift+4> |
| Jump to the next programming area (Causes > Intersections > Effects) | Any programming area | <Ctrl+Tab> |
| Jump to the previous programming area (Effects > Intersections > Causes) | Any programming area | <Shift+Tab> |
| Open a drop-down list, e.g. to select an instruction in a box  You can open drop-down lists with <ALT+F2> and then navigate with the arrow keys to scroll through the drop-down list. Finally, press the <Enter> key to confirm your selection. | Instruction box in a cause or effect | <ALT+F2> |
| Navigate to the next element of the action group | Element of an action group | <ALT+F3> |
| Navigate to the previous element of the action group | Element of an action group | <ALT+F6> |
| Expand/collapse causes | Any | <Alt+F11> |
| Expand/collapse effects | Any | <Alt+F12> |
| Display configuration menu, e.g. for programming an intersection | Intersection | <F4> |
| Insert AND logic operation | Cause or effect | <F9> |
| Insert OR logic operation | Cause or effect | <F10> |
| Insert empty box | Cause or effect | <F8> |
| Insert assignment | Cause or effect | <Shift+F7> |
| Add intersection column | Effect | <Shift+F8> |

GRAPH

| Operate GRAPH with the keyboard | Block | Keyboard shortcut |
| --- | --- | --- |
| Page Up/Down | Navigation view, single step view, sequence view, permanent instructions | <Page Up>/  <Page Down> |
| Navigate in the navigation view | Navigation view | <Up arrow>  <Down arrow> |
| Expand/collapse object | Navigation view | <+> or <Right arrow>  <-> or <Left arrow> |
| Switch between single step view and sequence view when a step or a transition is selected | Navigation view | <Return> |
| Switch between navigation view and work area | Navigation view, single step view, sequence view, permanent instructions | <ALT+F6> |
| Go to first element in a network | Single step view | <Home> |
| Go to last element in a network | Single step view | <End> |
| Switch to interlock | Single step view | <Ctrl+Home> |
| Switch to transition | Single step view | <Ctrl+End> |
| Navigate in the structure | Sequence view | Arrow keys |
| Go to first step | Sequence view | <Home> or <Ctrl+Home> |
| Go to last step | Sequence view | <End> or <Ctrl+End> |
| Open branch | Sequence view | <Shift+F8> |
| Close branch | Sequence view | <Shift+F9> |
| Insert sequence end | Sequence view | <Shift+F7> |
| Insert jump | Sequence view | <Shift+F12> |
| Insert step and transition | Sequence view | <F8> |
| Delete element | Sequence view | <Del> |
| Go to first editable element | Permanent instructions | <Home> |
| Go to next editable element | Permanent instructions | <Tab> |
| Go to last editable element | Permanent instructions | <End> |
| Go to previous editable element | Permanent instructions | <Shift+Tab> |
| Jump to the start of the "Action" cell | Actions | <Home> |
| Jump to the end of the "Action" cell | Actions | <End> |
| Insert new action | Actions | <Return> |

SCL

| Operate SCL with the keyboard | Block | Keyboard shortcut |
| --- | --- | --- |
| Navigating in the program code | Line | Arrow keys |
| One word to the right/left | Line | <Ctrl+arrow keys> |
| Cursor to start of line | Line | <Home> |
| Cursor to end of line | Line | <End> |
| Cursor to start of code section | Line | <Ctrl+Home> |
| Cursor to end of code section | Line | <Ctrl+End> |
| Expand/collapse code section | Insertion mark within the code section | <Ctrl+Shift+Num+>  <Ctrl+Shift+Num-> |
| Expand/collapse all code sections | Any | <Ctrl+Shift+Num*>  <Ctrl+Shift+Num/> |
| Expand block | Block overview, block in the programming window | <Ctrl+Shift+Num+> |
| Collapse block | Block overview, block in the programming window | <Ctrl+Shift+Num-> |
| Expand all blocks | Block overview, programming window | <Ctrl+Shift+Num*> |
| Collapse all blocks | Block overview, programming window | <Ctrl+Shift+Num/> |
| Indent line | Line | <Tab> or  <Ctrl+R> |
| Outdent line | Line | <Shift+Tab> or  <Ctrl+Shift+R> |
| Automatically format selected text |  | <Ctrl+Shift+W> |
| Expand/collapse the parameter list | Operand | <Ctrl+Shift+Space> |
| Set/delete bookmarks | Line | <Ctrl+Shift+M> |
| To the next bookmark |  | <Ctrl+Shift+6> |
| To the previous bookmark |  | <Ctrl+Shift+5> |
| Comment out selection | Line | <Ctrl+Shift+Y> |
| Remove comment | Line | <Ctrl+Shift+U> |

Editor for named value data types

| Operate editor for named value data types with the keyboard | Keyboard shortcut |
| --- | --- |
| Copy text | <Ctrl+C> |
| Cut text | <Ctrl+X> |
| Paste copied or cut text | <Ctrl+V> |
| Print named value data type | <Ctrl+P> |
| Go to line | <Ctrl+G> |
| Select all | <Ctrl+A> |
| Find | <Ctrl+F> |
| Replace | <Ctrl+H> |
| Undo last action | <Ctrl+Z> |
| Redo an undone action | <Ctrl+Y> |

---

**See also**

[Keyboard operation in the TIA Portal](Introduction%20to%20the%20TIA%20Portal.md#keyboard-operation-in-the-tia-portal)
  
[Displaying an overview of all keyboard shortcuts](Introduction%20to%20the%20TIA%20Portal.md#displaying-an-overview-of-all-keyboard-shortcuts)
  
[Using user-defined keyboard shortcuts](Introduction%20to%20the%20TIA%20Portal.md#using-user-defined-keyboard-shortcuts)

## Enlarging the programming window

### Introduction

The programming window is relatively small when all components of the application are shown. If the program code is large, you may find you have to rearrange the work area constantly. To avoid this problem, you can hide or minimize the display of the following components of the application and of the program editor:

- Project tree
- Task cards
- Block interface
- Favorites
- Comments
- Networks

> **Note**
>
> You can also use the "Reduce automatically" option for the task cards, project tree, and Inspector window. These windows will then be minimized automatically when you do not need them.
>
> See also: [Maximizing and minimizing the work area](Introduction%20to%20the%20TIA%20Portal.md#maximizing-and-minimizing-the-work-area)

### Hiding and showing the project tree

The project tree allows you to access all areas of the project. You can hide the project tree while you are creating a program so you have more space for the programming window.

To show and hide the project tree, follow these steps:

1. To hide the project tree, deselect the "Project tree" check box in the "View" menu, or click on "Collapse" on the project tree title bar.
2. To show the project tree, select the "Project tree" check box in the "View" menu or click on "Extend" on the project tree title bar.

### Opening and closing task cards

The task cards are located at the right-hand edge of the programming window.

To open or close the task cards, follow these steps:

1. To close the task cards, deselect the "Task card" check box in the "View" menu or click "Collapse" on the task cards title bar.
2. To open the task cards, select the "Task card" check box in the "View" menu or click "Expand" on the task cards title bar.

### Hiding and showing the block interface

The block interface is shown in the upper section of the program editor. During programming you can show and hide it as required.

To show and hide the block interface, follow these steps:

1. In the lower part of the interface within the window splitter, click on the Up arrow or Down arrow.

### Showing and hiding favorites

To hide or show the favorites in the program editor, follow these steps:

1. Click the "Display favorites in the editor" button in the program editor toolbar.

### Showing and hiding comments

Within a block you can enter a comment for the block or for each network. These two types of comments are shown and hidden differently.

To show or hide a block comment, follow these steps:

1. Click the the triangle at the start of the line with the block title.

To show or hide network comments, follow these steps:

1. Click "Network comments on/off" on the program editor toolbar.

> **Note**
>
> The comments available can vary depending on the programming language used.

### Opening and closing networks

Some programming languages use networks. You can open or close these networks as required.

To open or close networks, follow these steps:

1. If you want to open a network, click the right arrow in front of the network title. If you want to close a network, click the down arrow in front of the network title.

To open and close all networks, follow these steps:

1. Click "Open all networks" or "Close all networks" in the program editor toolbar.

> **Note**
>
> Networks are not used in every programming language.

---

**See also**

[Overview of the program editor](#overview-of-the-program-editor)

## Setting the mnemonics

You can program blocks using German or international mnemonics. When you open the TIA Portal for the first time, international mnemonics is set as default. You can change the mnemonics at any time.

### Procedure

To set the mnemonics, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "General" group in the area navigation.
3. In the "General settings" group, select the mnemonics that you want to use.

   The mnemonics is changed in all blocks.

## Displaying symbolic and absolute addresses

You have the following options for displaying operands in the program editor:

- Symbolic representation

  The symbolic operands are displayed in the program. The corresponding absolute addresses are shown in tooltips if you hold the mouse pointer over the operand.
- Absolute representation

  The absolute addresses are displayed in the program. The corresponding symbolic operands are displayed in tooltips.
- Symbolic and absolute representation

  Symbolic operands and absolute addresses are displayed in program. This setting only has an effect on blocks that were programmed with LAD, FBD, CEM, STL, and GRAPH.

  > **Note**
  >
  > Note that absolute operands are not displayed for GRAPH blocks if you have disabled the option "Display absolute operands" in the "Action" column.

You can set the display of operands centrally for all new blocks of the project or for individual blocks.

### Setting operand representation for new blocks

To set the operand representation for all new blocks in the project, follow these steps:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming > General" group in the area navigation.
3. Select the desired representation in the "Operand representation" drop-down list.

   The selected representation is enabled for all new blocks in the program.

### Setting operand representation for an individual block

To change the representation of the operands, follow these steps:

1. Open the block in the program editor.
2. Click the "Absolute/symbolic operands" button in the program editor toolbar.

   Each time you click the button, the representation and the symbol on the button change.

Or:

1. Open the block in the program editor.
2. Click the small arrow next to the "Absolute/symbolic operands" button in the program editor toolbar.

   A drop-down list is displayed.
3. Select the required representation from the drop-down list.

   The symbol on the button changes.

---

**See also**

[Basic information about operands](Programming%20basics.md#basic-information-about-operands)

## Find instructions

You have the option of finding specific instructions in the "Instructions" task card and then inserting them in your program. Note the following rules when entering search terms:

- No distinction is made between upper and lower case text.
- The search function considers parts of a search term.
- You cannot use placeholders, such as "*" and "?".
- If an instruction name includes underscores, the instruction is found even if you do not enter the underscore.
- The text in the columns "Name" and "Description" are taken into consideration in the search.

### Requirement

- A block is open.
- The "Instructions" task card is open.

### Procedure

To search for a specific instruction in the "Instructions" task card, follow these steps:

1. Select a starting point for the search if you want to start the search at a specific point. If you do not select a starting point, the search starts either at the top or bottom in the task card, depending on the type of search you have selected.
2. Enter a search term in the text box of the task card toolbar.
3. Click "Search down" if you want to search the task card from top to bottom.
4. Click "Search up" if you want to search the task card from bottom to top.

   The first match with the search term found is displayed as the result. If you want to continue the search, click the "Search down" or "Search up" button again. If no matches are found, you will receive a corresponding message.

---

**See also**

[Overview of the program editor](#overview-of-the-program-editor)

## Editing multilingual project texts in blocks

### Introduction

A block can contain the following translatable project texts:

- Title of the block and networks
- Comments about the block and the networks
- Comments in the block interface
- Comments on the operands used
- Freely defined comments

To translate these texts into another language, you must activate this language as a project language. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

Note that the texts may not exceed the length of 32767 Unicode characters even after translation.

### Requirement

- Several project languages are activated.
- A block is open and it contains at least one translatable project text.
- The block has no know-how protection.

### Procedure

To edit a text in all project languages, follow these steps:

| 1. Select the desired element in the open block. The following table provides an overview of the selection options:       | Selected element | Displayed project texts |    | --- | --- |    | "Block title" pane | If you select the "Block title" pane, you can edit the following project texts: - Title of the block and networks - Comments about the block and the networks - Freely defined comments anywhere in the block - Comments in the block interface    For multi-instances and parameter instances, only the comments you have changed on an instance-specific basis are displayed. You can recognize these comments from the fact that they are not grayed out. You can only select and edit grayed-out comments in the associated function block. |    | Network pane | If you select one or more network panes, you can edit the following project texts: - Titles and comments of the selected networks - Freely defined comments in the networks |    | Language element | If you select one or more language elements (e.g. boxes in LAD/FBD) or select a part of the program code in STL or SCL, you can edit the following project texts: - Comments on the operands used, including on global PLC tags - For block calls: Comments on the block parameters that are initialized with actual parameters - Freely defined comments for the language element |    | Step or transition | If you select a step or a transition in the GRAPH block, you can edit the following project texts: - Step name - Transition name | 2. Open the "Properties" tab in the Inspector window. 3. Open the "Texts" tab.    The "Texts" tab displays the texts in the active project languages and, if available, their translations. 4. You can edit the translations directly in the table on the "Texts" tab. 5. To edit the translations with an external editor, you can export the displayed texts to OOXML format using the "Export/Import project texts" buttons. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

> **Note**
>
> **Editing all project texts in the global "Project texts" table**
>
> You can also edit the translations for project texts in the global "Project texts" table. You can find the table in the project tree under "Languages & Resources > Project texts". It contains all translatable texts of the entire project.
>
> You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

## Use instruction versions

This section contains information on the following topics:

- [Basic information on instruction versions](#basic-information-on-instruction-versions)
- [Upgrade project and instructions](#upgrade-project-and-instructions)
- [Update program in the current PLC](#update-program-in-the-current-plc)

### Basic information on instruction versions

#### Introduction

The instructions available to you for programming the user program are managed in system libraries. If a new version of a system library is installed by an update, the newer versions of the instructions of this system library may also be installed.

If there are several versions for an instruction, these are listed in a drop down list in the "Instructions" task card after the respective instruction. If the instruction versions are not shown, you can show them again using the shortcut menu of the column header. In the drop-down list, select the version of an instruction which is to be used in the program. If you do not select any versions, the most recent versions are used.

> **Note**
>
> Please note the following:
>
> - You can only ever use the same version of an instruction within a device.
> - If you use an instruction in a know-how-protected block with a version other than the version set in the project, you can compile the know-how-protected block without a password if the interfaces of the instruction versions are identical. The next time you open the know-how-protected block, you will need to update the call for the instruction. The corresponding call is marked in red. The call is updated automatically by the system by compiling the entire program.
> - If you change the version of an instruction that other instructions depend on, the versions of the dependent instructions are also changed.
> - If you select a version for an instruction that can not be run on the CPU used, the instruction is shaded out. This means that you cannot use this instruction in this version with your CPU.
> - Instruction versions that are not supported in the opened block are marked with an asterisk. If necessary, select a different version of the instruction.
> - The system block in the project tree displays the block version number in its properties; it does not have to match the instruction version number of the associated instruction in the task card.
> - If you change the version of an instruction in the task card, you must compile the associated system block in the project tree before you update its block version number.

#### Changes in the versions

New versions can be main versions or secondary versions. New versions, such as 2.0 or 3.0, have more substantial changes to them. New main versions may therefore result in changes to the block interface. New secondary versions, such as 1.3 or 1.4, contain lesser changes or remedies to errors.

#### Using instruction versions

You can decide within a device which version of an instruction you want to use. If you select another version for an instruction, the new version is specified for all locations of use of this instruction within your program. These instructions are identified in the program by a red frame. You must then download your program to the device to use the new instruction version.

If you open your project with a newer TIA Portal version, you can upgrade your project and the instructions to the new TIA Portal version within the "Instructions" task card. Newer versions for some instructions are then available. These do not, however, automatically replace the old versions in your program. To use the new instruction versions in your program, you must explicitly update your program.

---

**See also**

[Upgrade project and instructions](#upgrade-project-and-instructions)
  
[Update program in the current PLC](#update-program-in-the-current-plc)

### Upgrade project and instructions

You can upgrade a project and the instruction versions to a newer TIA Portal version in one step. This will not change your program.

> **Note**
>
> **No backward compatibility**
>
> Projects that are saved with the current version of the TIA Portal are not backward compatible with older versions due to their enhanced functionality. With an upgrade, a new project is saved in the current project version. The original project is not overwritten and can still be edited with a compatible older version of the TIA Portal.

#### Procedure

To upgrade a project and the instructions, follow these steps:

1. Open a code block.
2. Open the "Instructions" task card.
3. Click "Upgrade project and instructions" in the toolbar.

   The "Project compatibility" dialog opens.
4. Click "OK" to continue with the upgrade.

#### Result

The project and instructions are upgraded. The "Upgrade project and instructions" button becomes inactive and the function can no longer be executed.

As the next step, you can update your program so that the new instruction versions can be used.

---

**See also**

[Basic information on instruction versions](#basic-information-on-instruction-versions)
  
[Update program in the current PLC](#update-program-in-the-current-plc)
  
[Upgrading projects](Editing%20projects.md#upgrading-projects)

### Update program in the current PLC

If there are new instruction versions in your project, you can update the program in the PLC so that the new instruction versions are used. This may be the case, for example after upgrading your project to a new TIA Portal version. Please note that you have to compile your program after update.

#### Procedure

Proceed as follows to update the program in the current PLC:

1. Right-click on the PLC for which you would like to update the program in the project tree.
2. Select the "Update program" command in the shortcut menu.

   The "Update program in the current CPU" dialog opens.
3. Click "OK" to perform the update.
4. Compile your program to complete the upgrade.

Or:

1. Open a code block.
2. Open the "Instructions" task card.
3. Click on "Update program in the current PLC" in the toolbar.

   The "Update program in the current CPU" dialog opens.
4. Click "OK" to perform the update.
5. Compile your program to complete the upgrade.

---

**See also**

[Basic information on instruction versions](#basic-information-on-instruction-versions)
  
[Upgrade project and instructions](#upgrade-project-and-instructions)

## Using instruction profiles

This section contains information on the following topics:

- [Basics of instruction profiles](#basics-of-instruction-profiles)
- [Creating new instruction profiles](#creating-new-instruction-profiles)
- [Opening and editing instruction profiles](#opening-and-editing-instruction-profiles)
- [Activating and deactivating instruction profiles](#activating-and-deactivating-instruction-profiles)
- [Deleting instruction profiles](#deleting-instruction-profiles)

### Basics of instruction profiles

#### Introduction

The TIA Portal provides you with numerous instructions that you can use to program the user program. However, you may filter out specific instructions that you do not want to use. To this end you can create instruction profiles in which you can explicitly specify the instructions to be listed in the "Instructions" task card. However, although you may create several instruction profiles in a project, only one of these profiles may be active at any given time. You can exchange instruction profiles with other users by means of shared libraries.

> **Note**
>
> Please note the following:
>
> - The use of instructions that are not allowed in the active profile in a block will trigger the output of a block compilation error. Such a situation may be triggered if you drag-and-drop a block from the library to your program.
> - Instructions of a profile that are not supported by the currently installed products are deleted from the profile the next time it is edited. If you transfer this profile to an engineering system in which these instructions are supported by the installed products, the instructions are again present in the profile but they are disabled. You can enable these instructions as required at any time.
> - If you want to make changes to the active profile, you must recompile the blocks in the project. This is also necessary when you disable or delete the active profile or when you enable a profile.

---

**See also**

[Creating new instruction profiles](#creating-new-instruction-profiles)
  
[Opening and editing instruction profiles](#opening-and-editing-instruction-profiles)
  
[Activating and deactivating instruction profiles](#activating-and-deactivating-instruction-profiles)
  
[Deleting instruction profiles](#deleting-instruction-profiles)

### Creating new instruction profiles

#### Requirement

The "Common data > Instruction profiles" folder is open in the project navigation.

#### Procedure

Proceed as follows to create a new instruction profile:

1. Double-click the "Add new profile" command.

   The Instruction Profile Editor opens and displays the new instruction profile. All instructions are activated for the new instruction profile.
2. Edit the new instruction profile to suit your requirements.

If necessary, you can rename the new instruction profile. To do this, follow these steps:

1. Right-click on the new instruction profile.
2. Select the "Rename" command in the shortcut menu.
3. Enter a name for the new instruction profile.

> **Note**
>
> The first instruction profile that you create will be used as active profile. In this case, compile all blocks in the project. If other instruction profiles are already available you must explicitly activate the new one in order to use it as active profile. You can identify the active profile by its icon in the project navigation.

---

**See also**

[Basics of instruction profiles](#basics-of-instruction-profiles)
  
[Opening and editing instruction profiles](#opening-and-editing-instruction-profiles)
  
[Activating and deactivating instruction profiles](#activating-and-deactivating-instruction-profiles)
  
[Deleting instruction profiles](#deleting-instruction-profiles)

### Opening and editing instruction profiles

Once you have opened an instruction profile, you can edit it as follows:

- Activating and deactivating instructions

  You can explicitly specify the instructions to be allowed in the instruction profile.

  > **Note**
  >
  > Note that dependencies exist between some instructions. As a result, it is possible that several instructions may be activated or deactivated by an action. The check box icon indicates the folders in which instructions are deactivated.
- Activating and deactivating instruction versions

  Certain instructions are available with different versions. You can explicitly specify the instruction versions to be allowed in the instruction profile.
- Renumbering blocks

  An instruction representing an internal function block (FB) or function (FC) in the system is assigned a specific block number by the system. You can replace this block number with your own block number. Within a version, there are several implementations for certain instructions. The block numbers in such instructions can only be changed for the specific implementation.

  > **Note**
  >
  > If an instruction from the instruction profile is used in the program and the specified block number is already in use by a different block, the specified block number of the instruction will be replaced by a free block number.

#### Requirement

The "Common data > Instruction profiles" folder is open in the project navigation.

#### Opening instruction profiles

Proceed as follows to open an instruction profile:

1. Double-click the instruction profile that you want to edit.

   The instruction profile opens in the Instruction Profile Editor.

#### Editing instruction profiles

Proceed as follows to edit an instruction profile in the Instruction Profile Editor:

1. Select the device that you want to edit from the "Device family" drop-down list box.
2. Select the programming language for which you want to edit the instruction profile from the "Language" drop-down list box.
3. Deactivate the instructions or instruction versions that you want to exclude from the instruction profile. You can deactivate a folder to deactivate all subordinate instructions.
4. Activate the instructions or instruction versions that you want to allow in the instruction profile.
5. You may assign your own block numbers.

**Note**

You can assign the number up to 65535 for CPUs of the S7-1200/1500 series. For CPUs of the S7300/400 series you find the restrictions of the number ranges in the respective CPU manual.

> **Note**
>
> A new compilation process is required for all blocks in the project when you change the active profile.

---

**See also**

[Basics of instruction profiles](#basics-of-instruction-profiles)
  
[Creating new instruction profiles](#creating-new-instruction-profiles)
  
[Activating and deactivating instruction profiles](#activating-and-deactivating-instruction-profiles)
  
[Deleting instruction profiles](#deleting-instruction-profiles)
  
[Basic information on instruction versions](#basic-information-on-instruction-versions)

### Activating and deactivating instruction profiles

You first need to activate an instruction profile in order to include filtering of its instructions. You can always deactivate the instruction profile to reset the instructions task card to the default scope of instructions.

> **Note**
>
> A new compilation process is required for all blocks in the project.

#### Requirement

The "Common data > Instruction profiles" folder is open in the project navigation.

#### Activating instruction profiles

Proceed as follows to activate an instruction profile:

1. Right-click on the instruction profile that you want to activate.
2. Select the "Activate profile" command from the shortcut menu.

   The selected instruction profile is now active. Instructions can now only be used in accordance with the settings of this profile.

#### Deactivating instruction profiles

Proceed as follows to deactivate the instruction profile:

1. Right-click on the instruction profile that you want to deactivate.
2. Select the "Deactivate profile" command from the shortcut menu.

   No instruction profile is active and the "Instructions" task card once again shows all instructions that are available for use.

---

**See also**

[Basics of instruction profiles](#basics-of-instruction-profiles)
  
[Creating new instruction profiles](#creating-new-instruction-profiles)
  
[Opening and editing instruction profiles](#opening-and-editing-instruction-profiles)
  
[Deleting instruction profiles](#deleting-instruction-profiles)

### Deleting instruction profiles

#### Requirement

The "Common data > Instruction profiles" folder is open in the project tree.

#### Procedure

Proceed as follows to delete an instruction profile:

1. Right-click on the instruction profile that you want to delete.
2. Select the "Delete" command in the shortcut menu.

> **Note**
>
> A new compilation process is required for all blocks in the project when you delete the active profile.

#### Result

The selected instruction profile is deleted. If you deleted the active instruction profile, no more active profiles are available and the "Instructions" task card once again shows all instructions that are available for use.

---

**See also**

[Basics of instruction profiles](#basics-of-instruction-profiles)
  
[Creating new instruction profiles](#creating-new-instruction-profiles)
  
[Opening and editing instruction profiles](#opening-and-editing-instruction-profiles)
  
[Activating and deactivating instruction profiles](#activating-and-deactivating-instruction-profiles)

## Using autocompletion

This section contains information on the following topics:

- [Basics of autocompletion](#basics-of-autocompletion)
- [Using autocompletion in graphic programming languages](#using-autocompletion-in-graphic-programming-languages)
- [Using autocompletion in textual programming languages](#using-autocompletion-in-textual-programming-languages)

### Basics of autocompletion

#### Function

You can use autocompletion in the program window of the program editor as an easy way to access available tags or instructions during programming. Autocompletion means a context-specific list appears in a dialog from which you can select the tags or instructions you need.

---

**See also**

[Using autocompletion in graphic programming languages](#using-autocompletion-in-graphic-programming-languages)
  
[Using autocompletion in textual programming languages](#using-autocompletion-in-textual-programming-languages)

### Using autocompletion in graphic programming languages

#### Inserting tags using autocompletion

To insert tags in graphic programming languages using autocompletion, follow these steps:

1. Select an operand of the instruction to which you wish to assign a tag.

   The input field for the operand opens. The autocompletion button will appear beside the input field.
2. Either click the autocompletion button or use the shortcut <Ctrl+l>.

   Autocompletion opens. It contains only the local and global tags, data blocks and multiple instances which are admissible for the operand in the given context. You can exit autocompletion at any time by pressing <Esc>.
3. Select the required tag from the list. If necessary, you can also filter the list:

   - For example, enter the first few letters of the name of the tag or instruction you wish to insert. Autocompletion will be filtered further with each letter entered. If there is no tag or instruction starting with the letters entered, autocompletion will remain at the last match.
   - Enter # to access the local tags from the block interface.
   - Global tags:

     - Without namespaces: Enter " to access the global tags.

     - With namespaces: Enter `_.` (<underscore><dot>) to access global tags.

     See also: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)
   - Enter % to access absolute addresses.

   If the tag is a structured tag, a data block or a multiple instance, then an arrow is displayed at the end of the row. Click on the arrow to display the lower-level elements. You can navigate to the very last level in this way. If a structure is allowed as a data type for the operand, you can choose "None" from the list. This assigns the entire structure to the operand as a tag. Use the <Backspace> key to return to the previous level.
4. Press the <Return> key to apply the tag.

---

**See also**

[Basics of autocompletion](#basics-of-autocompletion)
  
[Using autocompletion in textual programming languages](#using-autocompletion-in-textual-programming-languages)

### Using autocompletion in textual programming languages

#### Inserting tags and instructions using autocompletion

To insert tags and instructions in textual programming languages using autocompletion, follow these steps:

1. Enter the first few letters of the name of the tag or instruction you wish to insert. If necessary, you can directly filter the kind of tags:

   - Enter # to access the local tags from the block interface.
   - Enter " to access the global tags.
   - Enter % to access absolute addresses.

   Autocompletion opens. It contains only the local and global tags, data blocks, multiple instances and instructions which are admissible at the current position. You can exit autocompletion at any time by pressing <Esc>.
2. Enter more letters of the name of the tag or instruction you wish to insert. You can use <Enter> or <Tab> to apply the tag or instruction and close autocompletion.

   Autocompletion will be filtered further with each letter entered. If there is no tag or instruction starting with the letters entered, autocompletion only contains the previous matches.
3. Select the tag or instruction required from the list.

   If a tag is a structured tag, a data block or a multiple instance, first select the tag, the data block or multiple instance from the autocompletion and apply the selection with <Enter>. To select the additional components of the structure, data block, or multiple instance, enter a period. Autocompletion then reopens and you can select the next component.
4. Press the <Return> key to apply the tag.

---

**See also**

[Basics of autocompletion](#basics-of-autocompletion)
  
[Using autocompletion in graphic programming languages](#using-autocompletion-in-graphic-programming-languages)

## General settings for the PLC programming

This section contains information on the following topics:

- [Overview of the general settings](#overview-of-the-general-settings)
- [Changing the settings](#changing-the-settings)

### Overview of the general settings

#### Overview

The following table shows the general settings that you can make:

| Group | Setting | Description |
| --- | --- | --- |
| View | Operand representation (LAD/FBD/STL/GRAPH) | Representation of the operand in the program editor. You can select between the following options:  - Symbolic and absolute - Symbolic - Absolute |
| Tag information (LAD/FBD/STL/GRAPH) | Additional information for the tags used is displayed in the program editor. When you select the option "Tag information with hierarchical comments", the comments of the higher structure levels are also displayed for structured tags. |  |
| Location of tag information (LAD/FBD) | Specifies the position at which the tag information is to be displayed. You can display the tag information either collectively below a LAD/FBD network or directly at the respective operand. |  |
| with network comments (LAD/FBD/STL) | Network comments are shown. |  |
| Compilation | Delete actual parameters on interface update | Actual parameters are deleted if the associated formal parameters were deleted in the called block, and you run the "Update block call" function or compile the block. |
| Default settings for new blocks | IEC check for code blocks | The compatibility of operands in comparison operations and arithmetic operations are tested according to IEC rules. You have to explicitly convert non-compatible operands.  See also: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types) |
| Set "DB Accessible from OPC UA" for new data blocks | When the check box is selected, the attribute "DB Accessible from OPC UA" is set for new global data blocks. The data block is thus accessible as complete object from OPC UA. The individual tags of the data block can then be individually released or locked for OPC UA.  See also: [Using OPC UA communication](Configuring%20automation%20systems.md#using-opc-ua-communication-s7-1200-s7-1500-s7-1500t) |  |
| Set "DB Accessible from WebAPI" for new data blocks | If the check box is selected, the "DB accessible from Web API" attribute is set for new global data blocks. This makes the data module as a whole object accessible via the web server. The individual tags of the data block can then be individually released or locked. |  |
| Set instance data block elements with access type "Standard" to retentive. | When this check box is selected, the "Retain" attribute is set for newly created tags. The setting influences the following types of data blocks:  - S7-1200/S7-1500: Instance data blocks without optimized access – the setting influences all data block tags. - S7-1200/S7-1500: Instance data blocks with optimized access – the setting influences all tags with the attribute "Retentivity: set in IDB".      **Note**    With other types of data blocks you cannot specify any default for the retentivity.  - S7-300/S7-400: Tags in instance data blocks and global data blocks are retentive by default. If you change the retentivity setting, the change affects all tags in the block. - S7-1200/S7-1500: Tags in instance data blocks with optimized access are non-retentive by default. You can set the retentivity for each tag individually.   See also:   [Setting retentivity](Programming%20data%20blocks.md#setting-retentivity) |  |
| Additional settings | Set network title automatically | Sets the title of a network based on the comment of the output parameter of the first writing instruction in the network.  See also: [Inserting network title](Creating%20LAD%20programs.md#inserting-network-title) |
| Show autocompletion list | The autocompletion list is displayed. |  |
| Mnemonics | German or international designation of operations and operands |  |
| Download without reinitialization | Memory reserve | Defines the size of reserve in volatile memory that can be used for interface extensions.  See also: [Downloading blocks for S7-1200/1500](Compiling%20and%20downloading%20PLC%20programs.md#downloading-blocks-for-s7-12001500-s7-1200-s7-1500) |
| Block interface / data block elements | Set "Accessible from HMI/OPC UA/Web API" for new elements and ARRAY data block elements. | Enables the option "Accessible from HMI/OPC UA/Web API" for new tags in the block interface and in data blocks. The use of this option makes sense especially when working with large amounts of data in ARRAY data blocks.  See also: [Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks) |
| Set "Writable from HMI/OPC UA/Web API" for new elements and ARRAY data block elements. | When the check box is selected, the attribute "Writable from HMI/OPC UA/Web API" is set for new elements in the block interface and in data blocks. The use of this option makes sense especially when working with large amounts of data in ARRAY data blocks.  See also: [Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks) |  |

---

**See also**

[Overview of the block interface](Declaring%20the%20block%20interface.md#overview-of-the-block-interface)
  
[Changing the settings](#changing-the-settings)
  
[Permissible addresses and data types of PLC tags](Declaring%20PLC%20tags.md#permissible-addresses-and-data-types-of-plc-tags)
  
[Overview of the print settings](Introduction%20to%20the%20TIA%20Portal.md#overview-of-the-print-settings)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Activate or deactivate IEC check (S7-1200)](Data%20types.md#activate-or-deactivate-iec-check-s7-1200)
  
[Using autocompletion](#using-autocompletion)

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

[Overview of the general settings](#overview-of-the-general-settings)

## Eliminating syntax errors in the program

This section contains information on the following topics:

- [Basic information on syntax errors](#basic-information-on-syntax-errors)
- [Finding syntax errors in the program](#finding-syntax-errors-in-the-program)

### Basic information on syntax errors

#### Syntax errors

Below are some examples of syntax errors:

- Missing separators or the use of too many separators
- Incorrect keyword spelling
- Incorrect jump label spelling/notation
- Notation which does not match the set mnemonics (for example, "I2.3" instead of "E2.3")
- The use of key words as operands

#### Identification of syntax errors

Syntax errors are underlined in red or appear in red type.

This identification allows you to recognise incorrect inputs at a glance and jump from error to error to eliminate them. Syntax errors are also listed in the "Info" tab of the inspector window with an error message.

---

**See also**

[Finding syntax errors in the program](#finding-syntax-errors-in-the-program)

### Finding syntax errors in the program

#### Procedure

To find syntax errors in the program, follow these steps:

1. Select the position in the program in which you wish to look for errors.
2. Click "Go to next error" in the toolbar.

   The first error after the position you have selected will be marked.

You can use "Go to next error" and "Go to previous error" in the toolbar to find and correct all errors in the block.

Or:

1. Open the error list in the inspector window with "Info > Syntax".

   All syntax errors are listed in the table with a short description of the error.
2. If there are any errors, click on the blue question mark next to the error text to obtain information on eliminating the problem.
3. Double-click the error you want to correct.

   The corresponding error is highlighted.

---

**See also**

[Basic information on syntax errors](#basic-information-on-syntax-errors)

## Changing the programming language

This section contains information on the following topics:

- [Rules for changing the programming language](#rules-for-changing-the-programming-language)
- [Change the programming language](#change-the-programming-language)

### Rules for changing the programming language

#### Rules

Observe the following rules if you want to change the programming language for a block:

- All CPU series:

  - You can only change the programming language of entire blocks. The programming language cannot be changed for individual networks.
  - You cannot switch blocks programmed in the programming languages SCL or GRAPH. In GRAPH blocks, however, you can change between LAD and FBD as network languages.
- S7-300/400:

  - You can only change between the programming languages LAD, FBD and STL.
  - You can create networks within a block using another programming language and then copy them into the desired block.
  - If the language of individual networks of the block cannot be changed, these networks is displayed in their original language.
- S7-1200/1500:

  - You can change between the programming languages LAD and FBD.
- S7-1500:

  - You can create STL networks within the LAD and FBD blocks. However, you cannot copy between STL and LAD/FBD.

---

**See also**

[Change the programming language](#change-the-programming-language)

### Change the programming language

#### Procedure

To change the programming language, follow these steps:

1. Right-click the block in the project tree.
2. Select the "Properties" command in the shortcut menu.

   The dialog with the properties of the block opens.
3. Select the "General" entry in the area navigation.
4. Select the new programming language in the "Language" drop-down list.
5. Confirm your selection with "OK".

---

**See also**

[Rules for changing the programming language](#rules-for-changing-the-programming-language)

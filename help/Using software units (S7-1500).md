---
title: "Using software units (S7-1500)"
package: ProgUnitsenUS
topics: 31
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using software units (S7-1500)

This section contains information on the following topics:

- [Introduction to software units (S7-1500)](#introduction-to-software-units-s7-1500)
- [Creating a PLC program in software units (S7-1500)](#creating-a-plc-program-in-software-units-s7-1500)
- [Categorizing program elements in namespaces (S7-1500)](#categorizing-program-elements-in-namespaces-s7-1500)
- [Possible program structures with software units (S7-1500)](#possible-program-structures-with-software-units-s7-1500)
- [Creating and managing software units (S7-1500)](#creating-and-managing-software-units-s7-1500)
- [Creating relations (S7-1500)](#creating-relations-s7-1500)
- [Compiling and downloading software units (S7-1500)](#compiling-and-downloading-software-units-s7-1500)
- [Application example: Modularization of PLC programs with software units (S7-1500)](#application-example-modularization-of-plc-programs-with-software-units-s7-1500)

## Introduction to software units (S7-1500)

### Programming with software units

With the help of software units, you can subdivide your user program into individual program units, which you can edit and download independent of each other. For this purpose, the "Software units" folder is available in the project tree in which you can create and program your software units.

The following figure shows the "Software units" folder in the project tree:

![Programming with software units](images/131533388171_DV_resource.Stream@PNG-en-US.png)

Each software unit is enclosed in a visual bracket in the form of a dashed line and contains the following main elements:

- Relations: By means of the relational table, you can set up access from your software unit to the following objects:

  - Published blocks, PLC data types and PLC tag tables of other software units to which a relation exists.
  - Global data blocks outside of the software unit
  - Technology objects
- "Program blocks" folder: You create the program blocks (organization blocks, function blocks, functions, data blocks) in this folder.
- "External sources" folder: You import external SCL sources to this folder to generate blocks or PLC data types from them.
- "PLC tags" folder: You create the PLC tag tables, PLC tags and user constants in this folder.
- "PLC data types" folder: You create the PLC data types in this folder.
- PLC supervisions and alarms: Opens the alarm and supervision editor.
- PLC alarm text lists: Opens the text lists editor.

For published program elements, a small green/white square is displayed on the dashed line.

> **Note**
>
> Note the following information when using software units:
>
> - You can use software units with all versions of the S7-1500 CPU with a firmware version V2.6 and higher.
> - You can use up to 255 software units per CPU.
> - If you have created an online backup for a device that supports software units, you cannot use this backup for a device that does not support software units.
> - The program information contains information about all blocks, regardless as to whether or not they were created in a software unit.
> - In watch and force tables, you can access all PLC data, regardless of its position and publication status.
> - The data blocks and tags from software units are also visible in a device proxy and can therefore be exported and imported. It is irrelevant whether the data blocks are published or not.

### Program structure

Regardless of whether you want to split an existing program into software units or start a new project, you should plan the program structure at the start. A practical division of your user program into software units can be based on the following criteria, for example:

- Functional and technological units

  In software units, you can create functional or technological units that you can edit and load independently of each other. If the blocks of an existing program have already been divided into groups, these groups can result in useful software units.
- Expected frequency of changes

  Another possibility for splitting is the expected change frequency of program sections. To create units that can be loaded as independently of each other as possible, you should create your own software units for program sections with different change intervals. In one software unit, you can create blocks with basic functions that rarely need to be changed and include blocks that need to be changed frequently for commissioning in other software units. This division can also facilitate troubleshooting.
- Editor

  Splitting your program based on editors can significantly reduce the work required for coordination. In order to further optimize the cooperation of the project staff, you can use software units in conjunction with multiuser engineering.
- Widest possible encapsulation of the software units

  To enable you to edit and load the software units independently of one another, there should be no cross-relationships between the software units. Therefore, only use published program elements and relations if this is really necessary. Try to encapsulate the individual software units as far as possible.

You can also mix the individual criteria or create your own criteria for the division. However, you should consider the encapsulation of the software units as a main criterion in order to derive the greatest possible benefit from the software units.

See also:

[Possible program structures with software units](#possible-program-structures-with-software-units-s7-1500)

[Application example: Modularization of PLC programs with software units](#application-example-modularization-of-plc-programs-with-software-units-s7-1500)

### Namespaces in software units

Within software units, you can assign namespaces to program elements, such as blocks. The namespace and the name of the program element together result in a unique designation with which the program element can be identified within the CPU. This makes it possible to use the same name for different program elements as long as they are in different namespaces.

See also: [Categorizing program elements in namespaces](#categorizing-program-elements-in-namespaces-s7-1500)

### Using software units for Team Engineering

Structuring the PLC program with software units simplifies the creation and commissioning of the program by several people. Structuring enables the modular division into different areas of responsibility. Changes to different software units can be loaded onto the PLC independently of each other. TIA Portal ensures that changes made by other users are not overwritten. In most cases, using software units eliminates the need to synchronize the program via the PLC and accelerates the loading process to the PLC. Note the requirements for loading software units.

If blocks of the same software unit are changed by multiple users, you have the option of synchronizing your data when loading.

You can find additional information in the following sections:

- [Overview of working with Team Engineering](Using%20Team%20Engineering.md#overview-of-working-with-team-engineering)
- [Introduction to Multiuser Commissioning](Using%20Multiuser%20Commissioning.md#working-with-asynchronous-commissioning)
- [Downloading software units](#downloading-software-units-s7-1500)

> **Note**
>
> **Synchronization of software units**
>
> The relations and properties associated with the software units (e.g. name, author) cannot be automatically synchronized when working with "Synchronize PLC".
>
> This can result in relations and properties already changed by a user being overwritten by an older version when loading to a device and loading from a device.
>
> Changes to properties and relations of software units should only be carried out in the master project.
>
> See also: [Rules for PLC synchronization](Commissioning%20projects%20with%20PLC%20synchronization.md#rules-for-plc-synchronization)

### Data access

To access the function blocks, functions, global data blocks, PLC tag tables and PLC data types in other software units, these must be published and there must also be a relation to the respective software unit. However, this is not possible for organization blocks. Organization blocks can only be accessed in the software unit in which they are defined.

Program sections that you create outside a software unit have no access to the program sections you create in software units.

Conversely, blocks that you have programmed inside a software unit cannot access blocks outside of software units. However, you can specifically allow a software unit to access data blocks and technology objects outside of software units.

The following figure shows the possible data accesses between programs inside and outside software units:

![Data access](images/155291045387_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Restrictions**
>
> The restrictions for software units are described in the Readme:
>
> See also: [Note on software units](STEP%207.md#note-on-software-units)

---

**See also**

[Creating a PLC program in software units (S7-1500)](#creating-a-plc-program-in-software-units-s7-1500)
  
[Using external source files](Creating%20and%20managing%20blocks.md#using-external-source-files)

## Creating a PLC program in software units (S7-1500)

The general programming concepts remain the same during program creation in software units. You create your user program in the programming editor in the usual manner. You have the same support as outside of software units, e.g. dragging-and-dropping instructions from the "Instructions" task card and auto-complete when entering data types and operand names.

Note the following points when programming inside software units:

### Programming languages

You can use the following programming languages in software units:

- LAD
- FBD
- CEM
- SCL
- GRAPH
- ProDiag

### Symbolic programming

In software units, you can only use symbolic programming. Specifically, this means:

- The "Optimized block access" attribute is selected for all program blocks of a software unit and cannot be disabled. This also means that this attribute must be enabled when moving blocks from outside software units into a software unit. Therefore, do not use instructions with parameters that require absolute addressing, such as "PUT" or "GET".
- With the exception of organization blocks (OBs), all blocks are automatically numbered. The automatically assigned block numbers are not displayed, but you can see them in the properties of a block.
- The parameter types "TIMER", "COUNTER", "BLOCK_FB" and "BLOCK_FC" are not allowed in the block interface.
- Bit memory, the "Timer" function and the "Counter" function are not permitted in the PLC tag table. Using IEC timers and counters instead.
- You cannot use system and clock bit memories. Siemens Industry Online Support provides you with ready-made functions that you can use alternatively.

  See also: <https://support.industry.siemens.com/cs/ww/en/view/109479728>

### Names for software units

The following rules apply for the name of a software unit:

- Permissible characters are all alphanumeric characters and the underscore.
- The maximum number of characters amounts to 125.
- The name of a software unit must be unique for the entire CPU and no block with the same name must exist in the CPU.

### Names for program elements

The program code in software units is part of the overall user program. That is why, for example, block names must be unique CPU-wide when no namespaces are used. However, you can use namespaces to further subdivide your program. This means that names can appear multiple times in a CPU, but they must be unique within a namespace.

See also: [Categorizing program elements in namespaces](#categorizing-program-elements-in-namespaces-s7-1500)

### ProDiag

Each software unit contains its own ProDiag overview editor, which you can open in the project tree via the "PLC supervisions & alarms" entry. You can add supervisions for a software unit in this editor. The supervisions that you create in one software unit are not displayed in other software units. The ProDiag overview editor outside software units, in contrast, displays all PLC supervisions, including supervisions within the software units.

You can export the created supervisions to an Excel spreadsheet and then import them back into TIA Portal. If you export in the ProDiag overview editor of a software unit, only the supervisions of this software unit are exported. To export all supervision data from a PLC, start the export process in the ProDiag overview editor outside the software units. The Excel spreadsheet has an additional column in which the software unit containing the supervision is specified.

Note the following particularities for ProDiag with respect to use within software units:

- User-defined text lists that are referenced in supervision-specific texts can be stored in any software unit but not outside of software units.
- Every software unit has its own ProDiag OB to which a number >= 250 is assigned.
- The global tag supervisions for a ProDiag FB can only supervise operands of the same software unit.
- A ProDiag FB only contains block supervisions that reference parameters from the same software unit.
- You cannot publish a ProDiag FB. Therefore, access from other software units is not possible.
- The initial value acquisition for global supervisions and calls for ProDiag FBs is only supported for write accesses within the software unit in which the ProDiag FB is located.

See also:

- [Displaying ProDiag supervisions](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#displaying-adding-and-editing-prodiag-supervisions-s7-1500)
- [Exporting and importing ProDiag supervisions and properties of a ProDiag FB](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#exporting-and-importing-prodiag-supervisions-and-properties-of-a-prodiag-fb-s7-1500)

### PLC alarm text lists

Each software units has a "PLC alarm text lists" entry in the project tree. This means you can create the corresponding text lists for each software unit. PLC alarm text lists cannot be published. It is not possible to access PLC alarm text lists of other software units.

To create or delete text lists, you must open the text list editor of the corresponding software unit or the CPU. Text list names have to be unique CPU-wide.

### System functions or system function blocks

When instructions that are implemented within the system as functions or function blocks are used, these system functions or system function blocks are created in the "System blocks" folder outside the software units. In contrast, the single instance of the data block of a system function block is created unpublished in the "System blocks" folder of the corresponding software unit. If you want to move the data block and access it, you might need to change the access to "Published" and create a relation to the corresponding software unit.

You cannot move system blocks that are outside software units into a software unit.

### System constants

System constants are global constants, unique throughout the CPU, that are required and automatically created by the system. System constants can, for example, be used to address and identify hardware objects. Depending on the type of system constant, they are stored in different PLC tag tables:

- Some system constants are generated automatically when you create an organization block. These constants are in the standard tag table of the software unit. Other software units can access these constants if there is a relation to the software unit and the standard tag table is published.

  If you change the value of a system constant within a software unit, all dependent software units must be loaded at the next load to ensure the consistency of the online program.
- Some system constants are generated automatically when you insert a module or submodule into the project. These constants are in the standard tag table outside the software units. All software units can access these constants.

  If you change the value of a system constant in a standard tag table outside the software units, the entire CPU must be loaded at the next load to ensure the consistency of the online program.

### Comparing software units

For software units, both the offline/online and the offline/offline comparison are available. The comparison is carried out in the same way as the comparison of PLCs.

See also: [Comparison of software units](Comparing%20PLC%20programs.md#comparison-of-software-units)

### Access via HMI or OPC UA

The use of software units does not change the access options for tags via HMI or OPC UA. You still define these options in the block interface for local tags or in the PLC tag table for global tags.

Configuration data blocks that are generated from OPC UA client interfaces by the system ("<Name of the client interface_Configuration>") are always created outside of the software units. If you want to access them you can create a relation to these client interfaces. To do so, use the "Data block outside of the software unit" option as relation type.

### Fail-safe blocks

You can use fail-safe blocks (F-blocks) within the SafetyUnit. You can find additional information on this in the STEP 7 Safety help under "SafetyUnit".

---

**See also**

[Loading software units to a device (S7-1500)](#loading-software-units-to-a-device-s7-1500)
  
[Introduction to software units (S7-1500)](#introduction-to-software-units-s7-1500)
  
[Possible program structures with software units (S7-1500)](#possible-program-structures-with-software-units-s7-1500)

## Categorizing program elements in namespaces (S7-1500)

### Namespaces in software units

Within software units, you have the option of using namespaces. A namespace declares an area within the PLC program in which program elements can be grouped semantically. You can use namespaces to create more modular and clearly structured user programs.

You can define a namespace for the following program elements:

- Blocks
- PLC data types

Software units themselves are not categorized in namespaces. However, you can define a namespace as a default for a software unit. If you then create program elements in this software unit, they are given the default namespace.

You can change or delete this preset namespace for each program element. You can assign the namespace either immediately when creating these program elements or later in the properties of these objects.

This means that a software unit can contain program elements from different namespaces.

The namespace and the name form the fully qualified name of a program element. This fully qualified name is unique within the entire PLC program. This allows you to use a specific name for several program elements as long as the namespaces differ.

The application example shows the advantages and possible application cases of namespaces in detail:

[Application example: Modularization of PLC programs with software units](#application-example-modularization-of-plc-programs-with-software-units-s7-1500)

### Display of the namespaces in the project tree

To give you an overview of which program elements are categorized in namespaces, the namespaces are displayed in the project tree. With software units, the preset namespace is displayed. The preset is shown in square brackets after the name of a software unit.

The namespaces of program elements are displayed as follows:

- Program element

  The program element has the same namespace that was specified as the preset for the software unit. The namespace is no longer explicitly displayed.
- Program element [specific namespace]

  The program element has a specific namespace that differs from the preset of the software unit. This namespace is displayed in square brackets after the name of the program element.
- Program element []

  No namespace is assigned to the program element. This is shown by square brackets without content after the name of the program element.

The following example shows the representation of namespaces:

![Display of the namespaces in the project tree](images/159307552139_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The software unit has the namespace default setting "Assembly". |
| ② | The block takes over the namespace default setting. |
| ③ | The block has a specific namespace ("storage"). |
| ④ | The block has no namespace. |

### Nesting of namespaces

Namespaces can be structured hierarchically and be subdivided into further sub-namespaces. Use the point to separate the sub-namespaces.

Example

Block [Siemens.SIMATIC]

In this example, " Siemens" is the leading namespace, "SIMATIC" is a sub-namespace and " Block" the program element.

### Naming conventions according to IEC 61131-3

The IEC standard applies for the designation of namespaces and program elements in namespaces here: The following rules apply specifically:

- The name and the namespace of a program element may have a maximum length of 125 characters in total. This also applies to nested namespaces. Dots used as separators are counted as well.

- Permissible characters are "A-z", "0-9" and the underscore.

  Namespaces, sub-namespaces and names must not start with a number or end with an underscore.

  Double underscores are not permitted.
- Dots many not be used within names.
- Do not use keywords as names.

  See also: [Keywords](Programming%20basics.md#keywords-and-reserved-identifiers)
- Do not give names to program elements that you already use as a namespace.

  If you have already defined a namespace `Siemens` in the project, do not use `Siemens` as the name for the program element.

Examples of valid designations

Block [Siemens]

Block1 [Siemens1.SIMATIC1]

Block_1 [Siemens_1.SIMATIC_1]

_Block1 [_Siemens1._SIMATIC1]

### Input and representation of namespaces in program code

The following table shows the representation and input of namespaces in program code:

| Situation | Input | Example of the representation |
| --- | --- | --- |
| Same namespaces:  The calling and called block are in the same namespace. | Specification of the block name is sufficient. Specification of the complete namespace path is optional:   `<BlockName>` | ![Input and representation of namespaces in program code](images/155441103499_DV_resource.Stream@PNG-de-DE.png) |
| Different namespaces:  The calling and the called block are in different namespaces. | Specification of the complete namespace path is necessary.   You have the following options:  - `<Namespace>.<BlockName>`    This input searches relative to the calling block for a block with the specified namespace and block name. - `_.<Namespace>.<BlockName>`    This input searches globally for a block with the specified namespace and block name. | ![Input and representation of namespaces in program code](images/155442463371_DV_resource.Stream@PNG-de-DE.png)   Note that the representation is identical in both cases. |
| Using subnamespaces:  The called block is in a subnamespace of the namespace of the calling block. | Specification of the subnamespace and block name is sufficient. A complete namespace path is optional:   `<Subnamespace>.<BlockName>` | ![Input and representation of namespaces in program code](images/155441107467_DV_resource.Stream@PNG-de-DE.png) |
| Calling a block without namespace:  The called block is not in any namespace. The calling block is in a namespace. | Specification of the block name is sufficient. Specification of the namespace is optional:   `<BlockName>`   However, if there are namespaces containing blocks with the same name, these blocks are also displayed in the autocomplete. Then select the desired block. | ![Input and representation of namespaces in program code](images/155441111435_DV_resource.Stream@PNG-de-DE.png)   However, as the block is searched for globally, a `_.` is prefixed in the representation. |
| Calling block has no  namespace:  The calling block is not in any namespace. The called block is in a namespace. | Specification of the complete namespace path is necessary.   You have the following options:  - `<Namespace>.<BlockName>`    This input searches relative to the calling block for a block with the specified namespace and block name. - `_.<Namespace>.<BlockName>`    This input searches globally for a block with the specified namespace and block name. | ![Input and representation of namespaces in program code](images/155442459403_DV_resource.Stream@PNG-de-DE.png) |

For reasons of compatibility, it is possible to enter quotation marks ("Block") instead of the IEC-conform syntax (_.Block). However, it is preferable to use the IEC-compliant syntax.

> **Note**
>
> **Restrictions**
>
> The restrictions for namespaces are described in the Readme:
>
> See also: [Note on software units](STEP%207.md#note-on-software-units)

---

**See also**

[Introduction to software units (S7-1500)](#introduction-to-software-units-s7-1500)
  
[Creating a PLC program in software units (S7-1500)](#creating-a-plc-program-in-software-units-s7-1500)
  
[Possible program structures with software units (S7-1500)](#possible-program-structures-with-software-units-s7-1500)

## Possible program structures with software units (S7-1500)

The following two simplified examples show how you can structure a user program in software units and thereby reduce cross-references between the individual software units as far as possible.

Both example programs control a production plant consisting of two stations. The stations perform processing steps on workpieces and perform standardized tasks, for example, adding up the produced quantities.

### Program structure - Example 1

![Program structure - Example 1](images/154612689163_DV_resource.Stream@PNG-en-US.png)

In this example, "Unit_1" has the function of a library that provides general functionality. In the example it contains the FB "Global.PartCount" to count quantities. This FB is instantiated once by each station. In practice, such a "standard software unit" may contain a large number of reusable program sections that can be called up whenever needed.

The two stations are mapped in one software unit each. The program sections in the two software units are encapsulated so far that they can be processed by two different persons. However, the two functions "Station1.Control" and "Station2.Control" must be published because they are called from within "Unit_4".

Unit_4 performs central control tasks. The software unit contains an organization block for cyclic program processing and a "LineControl" function block that coordinates the two stations.

### Program structure - Example 2

![Program structure - Example 2](images/155307228427_DV_resource.Stream@PNG-en-US.png)

In the second example, each station is also controlled encapsulated in its own software unit. In the second example, however, each station has its own cyclic organizational block. If a program contains several organizational blocks, the operating system calls them one after the other in the order of their OB numbers. In this example, "Unit_2" and "Unit_3" are even more clearly encapsulated than in the first example.

"Unit_1" serves as a library for repeatedly used program parts. In addition to the "Global.PartCount" FB, it also contains a PLC data type (UDT) that maps the production data of a workpiece. The PLC data type can be used in the interface of each program block and thus enables standardized storage of the workpiece data.

The "Global.DB" block is used for central data storage and processing. This is a global data block in which each software unit can store its workpiece data. The block is also based on the structure of the PLC data type "Global.typeUDT".

---

**See also**

[Introduction to software units (S7-1500)](#introduction-to-software-units-s7-1500)
  
[Creating a PLC program in software units (S7-1500)](#creating-a-plc-program-in-software-units-s7-1500)
  
[Application example: Modularization of PLC programs with software units (S7-1500)](#application-example-modularization-of-plc-programs-with-software-units-s7-1500)

## Creating and managing software units (S7-1500)

This section contains information on the following topics:

- [Creating software units (S7-1500)](#creating-software-units-s7-1500)
- [Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
- [Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
- [Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
- [Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
- [Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
- [Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
- [Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)
- [Managing software units in libraries (S7-1500)](#managing-software-units-in-libraries-s7-1500)

### Creating software units (S7-1500)

#### Requirement

The "Software Units" folder in the project tree is open.

#### Procedure

To create a new software unit, follow these steps:

1. Double-click the "Add new software unit" entry.

   The "Add new software unit" dialog opens.
2. Enter a name for the new software unit.
3. Optionally, enter a preset for the namespace. This preset is then applied as the namespace for all newly created blocks and PLC data types.
4. To enter additional properties for the new software unit, click "Additional information".

   An area with further input fields is displayed.
5. Enter all the properties you require.
6. Confirm your entries with "OK".

> **Note**
>
> **Naming conventions according to IEC 61131-3**
>
> You can find naming conventions for software units here:
>
> [Creating a PLC program in software units](#creating-a-plc-program-in-software-units-s7-1500)
>
> You can find rules for the designation of namespaces and program elements in namespaces here:
>
> [Categorizing program elements in namespaces](#categorizing-program-elements-in-namespaces-s7-1500)

#### Result

The new software unit is created. You can now add additional program elements to the software unit and create the necessary relations.

---

**See also**

[Introduction to software units (S7-1500)](#introduction-to-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)

### Renaming software units (S7-1500)

#### Requirement

The "Software Units" folder in the project tree is open.

#### Procedure

To rename a software unit, follow these steps:

1. Right-click on the software unit you want to rename.
2. Select the "Rename" command in the shortcut menu.

   The name of the software unit in the project tree changes to an entry field.
3. Enter the new, unique name of the software unit.
4. Confirm your entry with the Enter key.

> **Note**
>
> **Naming conventions according to IEC 61131-3**
>
> You can find naming conventions for software units here:
>
> [Creating a PLC program in software units](#creating-a-plc-program-in-software-units-s7-1500)
>
> You can find rules for the designation of namespaces and program elements in namespaces here:
>
> [Categorizing program elements in namespaces](#categorizing-program-elements-in-namespaces-s7-1500)

#### Result

The name of the software unit is changed at all points of use in the program.

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)

### Changing the namespace preset of a software unit (S7-1500)

#### Introduction

You can define a preset for the namespace for software units. If you subsequently create new program elements in a software unit with namespace preset, then these program elements will get the namespace preset as their namespace. You can define, change or remove the namespace preset for a software unit at any time.

#### Applying the namespace preset to the underlying program elements

It is possible to apply the change in the namespace preset to the underlying elements also. The following rules apply here:

- Only those parts of the namespace of the underlying program elements are changed, which are identical with the existing namespace preset. This also applies to removing the namespace preset.
- If the namespace preset is repeated in a sub-namespace of the program element, only the identical part is changed in the leading namespace.
- The new namespace preset is not applied to program elements that have their own namespace.
- For program elements without a namespace only a new namespace preset is applied. When changing the existing namespace preset, such a program element still has no namespace.
- The changed namespace preset is not applied to program elements whose fully qualified name becomes ambiguous as a result of the change.
- The new namespace preset is not applied to program elements with special characters in the name.

Example:

|  |  |  |
| --- | --- | --- |
| ![Applying the namespace preset to the underlying program elements](images/157936149643_DV_resource.Stream@PNG-en-US.png) | ⇒ The namespace preset is changed from "Global" to "General". The change is transmitted to underlying program elements. | ![Applying the namespace preset to the underlying program elements](images/157936166923_DV_resource.Stream@PNG-en-US.png) |

Result:

- The "Main" and "Configuration1" blocks have the namespace preset "Global" as namespace. After the change, the namespace adapts itself for these blocks and becomes "General". Since this namespace is identical to the namespace preset, it is not displayed in the project tree.
- The block "Configuration2" has its own separate namespace. It does not get changed when there is a change in the namespace preset, and remains "Assembly".
- The "Configuration3" block has no namespace. After changing the namespace preset, this block still has no namespace.
- The namespace of the "Configuration4" block is divided into three parts. The leading part "Global" is derived from the namespace preset. By changing the namespace preset, only the leading part is matched. The two sub-namespaces remain unchanged because they are not derived from the preset.

#### Requirement

The "Software Units" folder in the project tree is open.

#### Procedure

To change the namespace preset for a software unit, follow these steps:

1. Right-click on the software unit for which you want to change the namespace preset.
2. Select the "Properties" command from the shortcut menu.

   The properties dialog of the software unit opens.
3. To define the namespace preset, or to change an existing one, in the "Namespace preset" field, enter the new namespace preset.
4. To delete the namespace preset, delete the text in the "Namespace preset" field.
5. Optional: If you wish to apply the change to the underlying program elements, click the "Apply namespace to underlying elements" button. In the "The following namespace will be replaced" field, you can preview which namespace is going to be replaced by the new namespace preset. Note that the change becomes effective immediately.
6. Confirm your entries with "OK".

   The defined namespace preset is used for the software unit.

> **Note**
>
> **Naming conventions according to IEC 61131-3**
>
> You can find naming conventions for software units here:
>
> [Creating a PLC program in software units](#creating-a-plc-program-in-software-units-s7-1500)
>
> You can find rules for the designation of namespaces and program elements in namespaces here:
>
> [Categorizing program elements in namespaces](#categorizing-program-elements-in-namespaces-s7-1500)

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)

### Copying and pasting software units (S7-1500)

You can also create new software units by copying existing software units and pasting the copy. You have the following options for this:

- Copying a software unit and pasting it within the same CPU
- Copying a software unit and pasting it into another CPU within the same project
- Copying a software unit of a reference project and pasting it into the open project
- Copying a software unit from a TIA Portal instance and pasting it into another TIA Portal instance

When software units with names identical to existing software units are pasted, the resulting name conflicts are handled as follows:

- Pasting the copied software unit into the same CPU:

  The copy of the software unit is assigned a name to which a number is added. For example, if "Motor" software unit is copied, a possible name for the copy is "Motor_1". A consecutive number range is not used for the number. Rather the smallest free number is always used. The copy of software unit "Motor" software unit can thus be assigned the name "Motor_25", if a lower number is not free. If a namespace is pre-selected for the copied software unit, it is renamed according to the same rules.
- Pasting the copied software unit into another CPU:

  A dialog box opens in which you can select whether the software unit with the same name is to be replaced or the copied software unit is to be pasted with a new name. If the copied software unit has a namespace that is already used within the CPU, the namespace preset is renamed.

If a namespace preset is used for the copied software unit, the following rules apply to the underlying blocks:

- Blocks without namespace:

  These blocks do not have a namespace even in the copy of the software unit.
- Blocks with the same namespace as the namespace preset of the copied software unit:

  These blocks are given the namespace that is preset in the copy of the software unit.
- Blocks with their own namespace, that is, different from the namespace preset of the copied software unit:

  These blocks keep their namespace. This means that the block has a unique name again, it is renamed. This is done according to the same rules as for the names of the software units.

Additionally, you can use existing master copies from the library. These may also contain software units that you can copy into your project. You can find additional information here:

- [Managing software unit elements in libraries](#managing-software-units-in-libraries-s7-1500)
- [Using master copies](Using%20libraries.md#using-master-copies)

#### Copying software units

To copy a software unit, follow these steps:

1. Right-click on the software unit you want to copy.
2. Select the "Copy" command in the shortcut menu.

   A copy of the software unit is now on the clipboard and can be pasted into either the same CPU or another CPU.

#### Pasting software units

To paste a software unit, follow these steps:

1. In the project tree, open the folder structure for the CPU in which you want to paste the copied software unit.
2. Right-click on the "Software Units" folder.
3. Select the "Paste" command in the shortcut menu.

   - If you are pasting the software unit into the same CPU, the copy is pasted with the name extension "_<smallest free number>". If there is a namespace preset, it will also be renamed.
   - If you are pasting the software unit into another CPU and a software unit with this name already exists, the "Paste" dialog box opens. Select the desired option and confirm your selection with "OK".

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)

### Deleting software units (S7-1500)

#### Requirement

The "Software Units" folder in the project tree is open.

#### Procedure

To delete a software unit, follow these steps:

1. In the "Software Units" folder in the project tree, right-click on the software unit that you want to delete.
2. Select the "Delete" command in the shortcut menu.
3. Confirm the confirmation prompt with "Yes".

   The software unit is deleted from the project.

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)
  
[Managing software units in libraries (S7-1500)](#managing-software-units-in-libraries-s7-1500)

### Rules for program elements in Software Units (S7-1500)

#### Introduction

The following program elements are available in software units:

- Blocks and block calls
- PLC tags and global constants
- PLC data types

Basically, you can create and use these elements in the same way as outside of software units. However, please take into account the special features described below.

#### Using blocks

You can use the following block types inside a software unit:

- Organization blocks (OB)
- Functions (FC)
- Function blocks (FB)
- Data blocks (DB)

You can use the following programming languages to program the blocks: LAD, FBD, CEM, SCL, GRAPH and PRODIAG.

The numbers for FBs, FCs and DBs are always automatically assigned and cannot be changed. On the other hand, you can assign the block numbers for OBs yourself based on the available number range in each case. In a software unit, the block numbers are not displayed in the project tree. However, you can open the properties of a block to display its number.

Note that all restrictions for organization blocks are also retained in software units. This means that you can only use the maximum number of an organization block type, regardless as to whether the organization blocks exist inside or outside of software units.

All MC-OBs used must be contained in one software unit. If you use the MC_Transformation, the associated data block must also be contained in the same software unit.

If you want to access a block of another software unit, the "Published" option must be selected for this block under "Access". Note the following particularities for this:

- Organization blocks:

  The "Access" property is not available for organization blocks. They cannot be accessed from another software unit.
- ProDiag function blocks:

  The "Published" option is always deselected for ProDiag function blocks. This means they also cannot be accessed from another software unit.

#### Call blocks

You can use block calls inside as well as outside of software units. Note the following particularities:

- Within a software unit, you can call up blocks independent of their publishing status. This means that the called block does not have to be published.
- When block calls take place between two software units, there must be a relation between the software units and the called block has to be published. The calling block must have access to the called block and the corresponding instance data block. The instance data block must also have access to its function block. Make sure that there are no circular relations.
- Calls between blocks of software units and blocks outside software units are not possible.
- You cannot publish an instance data block when the associated function block is not published.

#### Using PLC tags and global constants

You can work with PLC tags and global constants inside software units in the same way as outside of software units. Note the following particularities:

- The "Show all tags" tag table is not available inside a software unit.
- The "Show all tags" tag table outside of software units also shows the tags and global constants of the software units. The tags and global constants of the software units can also be edited here.
- You can publish PLC tag tables in software units to access them from other software units. In addition, a relation between these software units is required. Access to tags and global constants of a software unit from outside the software units is not possible. Access via HMI and OPC UA, however, is not restricted.
- S5 timers and S5 counters are not permitted as data types for operands.
- The use of bit memory is not allowed.
- You can also export PLC tag tables to software units for further processing with external applications. You can also import PLC tag tables that have been processed externally into software units. The following formats are supported for import and export:

  - XLSX (Excel)
  - XML
  - SDF

  In "XLSX" format, an additional column is created in which the software unit from which the PLC tag table was exported is specified. The other two formats do not contain any information about the exporting software unit. Note that you can only import PLC tags from an Excel file with the additional column for the software unit into other software units, but not into PLC tag tables outside software units.

#### Using PLC data types

You can also work with PLC data types inside a software unit. If you want to access them from other software units, you can set the "Published" property and set up a relation with the corresponding software unit. You cannot use this PLC data type outside of software units.

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
  
[Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)
  
[Managing software units in libraries (S7-1500)](#managing-software-units-in-libraries-s7-1500)
  
[Creating blocks](Creating%20and%20managing%20blocks.md#creating-blocks)
  
[Block calls](Programming%20basics.md#block-calls)
  
[Creating PLC data types](Declaring%20PLC%20data%20types%20%28UDT%29.md#creating-plc-data-types)
  
[Declaring PLC tags](Declaring%20PLC%20tags.md#declaring-plc-tags-1)

### Basics for copying or moving program elements (S7-1500)

#### Introduction

You can copy or move the following program elements:

- Blocks
- PLC tag tables and tags
- PLC data types
- Text lists

Basically, the system changes the names and the namespaces of the program elements if inserting them would create a conflict. When doing so, the namespace is adjusted on priority and the name is retained if possible. Note that an object is always copied when it is moved to a different CPU by drag-and-drop. The object is not deleted at its original location in this operation.

The table below shows the effects on the copied or moved program element:

| Source |  | Destination |  |  |
| --- | --- | --- | --- | --- |
|  |  | **Software unit with namespace preset** | **Software unit without namespace preset** | **Outside the software units** |
| **Software unit with namespace preset** | Element uses the namespace preset | The element gets the namespace preset of the target software unit. | The namespace is removed. | - The "Access" property is removed for blocks, PLC tag tables and PLC data types. - Automatic numbering and an optimized block access are set for blocks. - An existing namespace is removed. |
| Element has its own separate namespace. | The element retains its namespace. | The element remains without a namespace. |  |  |
| Element does not have a namespace. | The element remains without a namespace. | The element remains without a namespace. |  |  |
| **Software unit without namespace preset** | Element does not have a namespace. | - If the element has a valid name, it is given the namespace of the destination software unit. - If the element name contains invalid characters, it remains without a namespace. | The element remains without a namespace. |  |
| Element has its own separate namespace. | The element retains its namespace. | The element retains its namespace. |  |  |
| **Outside the software units** | Element does not have a namespace. | - Requirement for blocks:   - Automatic numbering   - Optimized block access - For supported blocks, PLC tag tables and PLC data types, the "Access" property is added and the "Published" check box is cleared. - If the element has a valid name, it is given the namespace of the destination software unit. - If the element name contains invalid characters, it remains without a namespace. | - Requirement for blocks:   - Automatic numbering   - Optimized block access - For supported blocks, PLC tag tables and PLC data types, the "Access" property is added and the "Published" check box is cleared. | All set properties of the program element remain unchanged. |

The procedure for copying and moving is identical to the procedure outside the software units:

- [Copying or moving blocks](Creating%20and%20managing%20blocks.md#copying-or-moving-blocks)
- [Copying or moving PLC tag tables](Declaring%20PLC%20tags.md#copying-or-moving-plc-tag-tables)
- [Copying or moving PLC data types](Declaring%20PLC%20data%20types%20%28UDT%29.md#copying-or-moving-plc-data-types)
- [Copying or moving text lists](Editing%20project%20data.md#copying-or-moving-text-lists)

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
  
[Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)
  
[Managing software units in libraries (S7-1500)](#managing-software-units-in-libraries-s7-1500)
  
[Copying entries in the PLC tag table](Declaring%20PLC%20tags.md#copying-entries-in-the-plc-tag-table)

### Displaying and modifying properties of a software unit (S7-1500)

You can display and modify the following properties for software units:

- Name
- Author
- Comment
- Preset of the namespace

#### Requirement

The "Software Units" folder in the project tree is open.

#### Procedure

To display and modify the properties of a software unit, follow these steps:

1. Right-click on the software unit whose properties you want to display or edit.
2. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the block opens and the properties are displayed.
3. Change the desired property as needed.
4. Confirm your entries with "OK".

---

**See also**

[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
  
[Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Managing software units in libraries (S7-1500)](#managing-software-units-in-libraries-s7-1500)

### Managing software units in libraries (S7-1500)

#### Introduction

You can manage software units in libraries to reuse them, if necessary, together with their program elements. You can add software units as master copies to the project library or to a global library.

You can also paste the blocks and PLC data types independently of their software unit into the project library or into a global library. There is no difference when it comes to using blocks and PLC data types that were not programmed within software units. They can also be pasted as master copies or types in the project library or global libraries and then reused in the project. If the block or the PLC data type already exists in the project, you will receive a message informing you about it.

#### Namespaces in libraries

You can also insert blocks and PLC data types into libraries whose names have been extended by a namespace. However, note the following:

- When you insert the blocks or PLC data types as types or master copies into libraries, the namespaces are preserved. You can show the "Namespace" column to display the namespace for each object.
- When you insert a software unit as master copies in libraries, its namespace default is preserved.
- When you insert a type or a master copy with namespace into a software unit, the namespace is preserved.
- If you use a type or a master copy with namespace outside software units, the namespace is lost.
- You cannot change the namespaces within libraries.
- Changes of the namespace of an instance in the project are not passed on to the type in the library. This means that the type retains its original namespace, which is also adopted by further instances. The behavior is equivalent to changing the name of an instance.
- In contrast to the project tree, the names of the objects in a library must be unique, even with namespaces. That is, no two objects with the same name can exist in a library or folder. In this case, you are recommended to create a correspondingly named folder in the library for each namespace. This allows blocks and PLC data types to be retained as types with the same name and structured clearly.

---

**See also**

[Library basics](Using%20libraries.md#library-basics)
  
[Adding master copies](Using%20libraries.md#adding-master-copies)
  
[Using master copies](Using%20libraries.md#using-master-copies)
  
[Creating software units (S7-1500)](#creating-software-units-s7-1500)
  
[Renaming software units (S7-1500)](#renaming-software-units-s7-1500)
  
[Changing the namespace preset of a software unit (S7-1500)](#changing-the-namespace-preset-of-a-software-unit-s7-1500)
  
[Copying and pasting software units (S7-1500)](#copying-and-pasting-software-units-s7-1500)
  
[Deleting software units (S7-1500)](#deleting-software-units-s7-1500)
  
[Rules for program elements in Software Units (S7-1500)](#rules-for-program-elements-in-software-units-s7-1500)
  
[Basics for copying or moving program elements (S7-1500)](#basics-for-copying-or-moving-program-elements-s7-1500)
  
[Displaying and modifying properties of a software unit (S7-1500)](#displaying-and-modifying-properties-of-a-software-unit-s7-1500)

## Creating relations (S7-1500)

This section contains information on the following topics:

- [Basics of relations (S7-1500)](#basics-of-relations-s7-1500)
- [Publishing program elements (S7-1500)](#publishing-program-elements-s7-1500)
- [Setting up relations (S7-1500)](#setting-up-relations-s7-1500)

### Basics of relations (S7-1500)

#### Function of relations

With the help of software units, you can subdivide your user program into individual program units that you can edit, compile and download individually. You can use relations to create connections that allow you access to the following objects outside of the own software unit:

- Function blocks (FB), functions (FC)
- Global data blocks (DB)
- PLC tags
- PLC data types
- Technology objects

Note the following particularities when using relations:

- A software unit cannot create a relation with itself.
- A relation can only be created in one direction at a time. This means that a software unit cannot create a relation to another software unit if a relation back from it already exists.

  Example: Software Unit A has a relation with Software Unit B. Software Unit B cannot establish an additional relation with Software Unit A and can also not access the program elements of Software Unit A.
- Relations that would lead to circular references cannot be created.

You can create, change and delete relations in the relational table.

#### Access to function blocks (FB) and functions (FC)

From a software unit, you can access the function blocks and functions of other software units if these are published and there is a relation to the software units. You can create a new data block as an instance of the function block for this of the other software unit in the accessing software unit. Alternatively, you can also publish the associated instance data block of an FB to access it.

It is not possible to access a function block or a function of a software unit from a block that was not created in a software unit. Likewise, a function block or a function inside a software unit cannot access a block outside of a software unit. Blocks outside of a software unit are the blocks that you have created directly in the "Program blocks" folder below the CPU.

System functions and system blocks are an exception; you can access them as usual.

#### Access to global data blocks (DB)

You have the following options to access global data blocks that are not located in the own software unit.

- You can access global data blocks outside of software units from a software unit if you have created a corresponding relation. The following rules apply to access of global data blocks:

  - Access to a global data block that contains PLC data types is not permitted.
  - Access to an unoptimized data block is not permitted.
  - Access to global ARRAY data blocks is not permitted.
  - Access to a global fail-safe data block (F-DB) is not permitted.
- The global data blocks of a software unit can be accessed from another software unit if the data blocks are published and there is a relation to the software units. However, access to the global data blocks of a software unit from blocks that are not stored in software units is not possible.

#### Access to PLC tags

You can access the PLC tags of another software unit from a software unit if these are contained in a published PLC tag table and there is a relation to this software unit. However, access to the PLC tags of a software unit from blocks that are not stored in software units is not possible.

#### Access to PLC data types

You can access the PLC data types of other software units from a software unit if these are published and there is a relation to this software unit. However, access to the PLC data types of a software unit from blocks that are not stored in software units is not possible.

Blocks and the PLC data types used by them in the block sections "Input", "Output", "InOut" and "Static" must have the same publication status. This means when a "MyMotor" block is published and uses the PLC data type "myUDT1" of the same software unit, the PLC data type "myUDT1" must also be published.

#### Access to technology objects

You can access technology objects from a software unit by creating a relation to the corresponding object in the software unit.

---

**See also**

[Publishing program elements (S7-1500)](#publishing-program-elements-s7-1500)
  
[Setting up relations (S7-1500)](#setting-up-relations-s7-1500)

### Publishing program elements (S7-1500)

These program elements must be published so that other software units can access the function blocks (FBs), functions (FCs), global data blocks (DBs), PLC tag tables and PLC data types of a software unit. If this was not done when these elements were created, you can change the setting at any time. However, you can also cancel the publication again for an element. Access from outside is then no longer possible.

You cannot change the publishing status for the following program elements:

- Organization blocks (OB)
- ProDiag function blocks

These program elements are always unpublished. They cannot be accessed from outside their own software unit.

You can change the publishing status for a program item at the following locations:

- In the properties of the program element
- In the Overview window
- In the portal view

You see the publishing status for each program element in the detail view. Additionally, a small green/white square is displayed in front of the published program elements of the software units in the project navigation.

#### Changing the publishing status in the properties of the program element

To change the publishing status for a program element by its properties, follow these steps:

1. In the project tree, open the "Software Units" folder and navigate to the program element for which you want to change the publishing status.
2. Right-click on the program element.
3. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the program element opens.
4. Click the "General" group in the area navigation if it is not displayed.
5. Select or clear the "Published" check box below "Access".
6. Confirm your entries with "OK".

   The publishing status for the selected program element is changed.

#### Changing the publishing status in the Overview window

To change the publishing status for a program element in the Overview window, follow these steps:

1. In the project tree, open the folder "Software Units" and navigate to the software unit of the program element with the publishing status you want to change.
2. Select either the "Program blocks", "PLC tags" or "PLC data types" folder, depending on the type of program element.
3. Open the Overview window using the "Maximizes/minimizes the overview" button or the "View > Overview" menu.
4. Open the "Details" tab.

   The publishing status is displayed for each element in the "Published" column.
5. In the "Published" column, select or clear the check box of the program element you want to change.
6. Alternatively, you can select several program elements and change the publishing status for all selected elements simultaneously using the shortcut menu command "Publication".

#### Changing the publishing status in the portal view

To change the publishing status for a program element in the portal view, follow these steps:

1. Change to the portal view.
2. Click on "PLC programming".
3. Click on "Show all objects".
4. Open the "Details" tab.

   The publishing status is displayed for each element in the "Published" column.
5. In the "Published" column, select or clear the check box of the program element you want to change.

---

**See also**

[Basics of relations (S7-1500)](#basics-of-relations-s7-1500)
  
[Setting up relations (S7-1500)](#setting-up-relations-s7-1500)

### Setting up relations (S7-1500)

You have the option of setting up relations with other software units, global data blocks and technology objects. Note that you can only access objects of another software unit for which the "Published" property is set. You can change or delete relations at any time.

#### Requirement

The "Software Units" folder in the project tree is open.

#### Creating relations

To create a new relation, follow these steps:

1. In the project tree, open the software unit for which you want to create a relation.
2. Double click on "Relations".

   The relational table opens.
3. Click "<Add new relation>".
4. Select the type of relation in the "Relation type" column.
5. In the "Accessible element" column, select or enter the element you want to access.

   The relation has been created and you can access the element.

#### Changing relations

To change a relation, follow these steps:

1. In the project tree, open the software unit for which you want to change a relation.
2. Double click on "Relations".

   The relational table opens.
3. In the "Accessible element" column, change the element you want to access as required.

#### Deleting relations

To delete a relation, follow these steps:

1. In the project tree, open the software unit for which you want to delete a relation.
2. Double click on "Relations".

   The relational table opens.
3. Select the relations that you want to delete.
4. In the shortcut menu, select the "Delete" command or press the <Del> key.
5. Confirm the confirmation prompt with "Yes".

   The selected relations are deleted.

---

**See also**

[Basics of relations (S7-1500)](#basics-of-relations-s7-1500)
  
[Publishing program elements (S7-1500)](#publishing-program-elements-s7-1500)

## Compiling and downloading software units (S7-1500)

This section contains information on the following topics:

- [Basics for compiling and downloading software units (S7-1500)](#basics-for-compiling-and-downloading-software-units-s7-1500)
- [Compiling software units (S7-1500)](#compiling-software-units-s7-1500)
- [Downloading software units (S7-1500)](#downloading-software-units-s7-1500)

### Basics for compiling and downloading software units (S7-1500)

#### Introduction

Software units are program units that you can compile and download independent of the remaining program code. If there are dependencies between software units, a corresponding message is displayed during compiling. After successful compilation, you can load software units into a device or onto a memory card. Loading can only be performed if the following requirements are met:

- The loading operation does not involve a program element that exists at a different position on the device or the memory card with the same name or the same number.
- If a software unit has relations to objects outside the software unit and these objects have been changed since their last download, these objects have to be included in the loading. This applies to published blocks of other software units, but also to global data blocks, PLC tag tables and technology objects outside of software units.
- The loading does not include a system block that already exists on the device or the memory card with a different number or version.
- The loading does not include any organization blocks with numbers that are used in the device or on the memory card for organization blocks of other types.
- If the loading includes an organization block with a specific start event and further software units with organization blocks with the same start event exist, these further software units also have to be included in the loading. This applies, for example, to the program cycle OB and the startup OB.
- The maximum number of organization blocks of a specific type is not exceeded during the loading to the device or the memory card. If you still want to perform the loading, load the entire CPU into the device or onto the memory card. This restores the consistency between the project and device or memory card.
- Loading all software units via the "Software Units" folder is only possible if all software units that are in the device or on the memory card are also present in the offline project. A software unit that is only available online would otherwise be deleted.

  If you still want to perform the loading, load the entire CPU into the device or onto the memory card. This restores the consistency between the project and device or memory card.

- All the PLC data types on the device or the memory card is also in the offline project with the same version.
- There is already a hardware configuration for the device in the device or on the memory card. If this is not the case, you must load the entire CPU.

If there are no dependencies to other program parts, the only software units included in the loading are those for which you have initiated the loading. This means that the rest of the program might differ between the program elements in the project and on the device or memory card.

> **Note**
>
> **Checksum for individually loaded software units**
>
> In order to check the identity or integrity of PLC programs, a checksum is generated during compiling of a CPU in the project. This is loaded as well into the device or onto the memory card. The "GetChecksum" instruction can be used to read this checksum during runtime in the program. If, by contrast, you load individual software units into a device or onto a memory card, the checksum is reset to "0x0000000000000000". The reason for this is that the checksum in the project no longer matches the checksum of the device. The next time you load the complete PLC program, you again receive a valid checksum. Be aware of this when using "GetChecksum".

#### Loading software units in "RUN" mode:

The same rules apply for the loading of software units in the "RUN" mode as when loading the different program elements outside of the software units. In the process, take into account the descriptions on the pages "Downloading blocks in the "RUN" mode to the device" of the various CPU series in the information system.

#### Software units in connection with OPC UA

If you wish to use OPC UA communication in connection with the software units, note the following special points when compiling your user program:

- When the client interfaces are compiled, the relevant data blocks for OPC UA are created. However, these are stored outside of the software units. Therefore, move them to the desired software units with drag-and-drop.
- New PLC data types are also created in the "System data types" folder outside of the software units when the client interfaces are compiled. Move these also into the "PLC data types" folder of the corresponding software units.
- If you change the name of read, write or method lists, new PLC data types are created. You need to move these into the corresponding software units as well.
- If you create new nodes or change the names of existing nodes in the lists, the corresponding client interface needs to be compiled again for the names to be updated in the data blocks and PLC data types in the software units.

---

**See also**

[Compiling software units (S7-1500)](#compiling-software-units-s7-1500)
  
[Compiling project data](Editing%20project%20data.md#compiling-project-data)
  
[Loading project data](Editing%20project%20data.md#loading-project-data)
  
[Basics for compiling and downloading PLC programs](Compiling%20and%20downloading%20PLC%20programs.md#basics-for-compiling-and-downloading-plc-programs)

### Compiling software units (S7-1500)

The following possibilities are available to compile software units:

- Compiling the program elements of a device. This includes the program elements of the software units.
- Compiling the program elements of all the software units of a device.
- Compiling the program elements of individual software units.
- Compiling the blocks in the "Program blocks" folder of a software unit

Depending on which options you use, you get different options for the compilation process.

- Hardware and software (only changes)
- Hardware (only changes)
- Hardware (rebuild all)
- Software (only changes)
- Software (rebuild all)
- Software (reset memory reserve)

If a software unit accesses program elements of a different software unit, inconsistencies can arise during compiling. In this occurs, compile the dependent software unit as well.

#### Compiling the program elements of a device.

To compile the program elements of a device including the software units, follow these steps:

1. Select the device with the program elements you want to compile in the project tree.
2. Select the desired option in the "Compile" submenu of the shortcut menu.

#### Compiling the program elements of all the software units of a device

To compile the program elements of all the software units of a device, follow these steps:

1. Select the "Software Units" folder in the project tree.
2. Select the desired option in the "Compile" submenu of the shortcut menu.

#### Compiling the program elements of individual software units

To compile the program elements of individual software units, follow these steps:

1. In the "Software Units" folder in the project tree, select the software units whose program elements you want to compile.
2. Select the desired option in the "Compile" submenu of the shortcut menu.

#### Compiling the blocks in the "Program blocks" folder of a software unit

To compile the blocks of a software unit, follow these steps:

1. Select the blocks within a software unit that you want to compile in the "Program blocks" folder of the project tree.
2. Select the desired option in the "Compile" submenu of the shortcut menu.

#### Result

The program elements are compiled. You can check whether or not the compilation was successful in the Inspector window with "Info > Compile".

---

**See also**

[Basics for compiling and downloading software units (S7-1500)](#basics-for-compiling-and-downloading-software-units-s7-1500)

### Downloading software units (S7-1500)

This section contains information on the following topics:

- [Loading software units to a device (S7-1500)](#loading-software-units-to-a-device-s7-1500)
- [Loading software units from a device (S7-1500)](#loading-software-units-from-a-device-s7-1500)
- [Loading software units to a memory card (S7-1500)](#loading-software-units-to-a-memory-card-s7-1500)
- [Loading software units from a memory card (S7-1500)](#loading-software-units-from-a-memory-card-s7-1500)

#### Loading software units to a device (S7-1500)

You can load one, multiple or all Software Units to a device in one load operation. In order to load all the Software Units at one time, the device may not contain any Software Unit that does not exist in the offline project. In this case, you can either load the entire CPU or individual Software Units.

##### Requirement

A hardware configuration exists on the device.

##### Loading one or more software Software Units to a device​

To load one or more Software Units to the device, follow these steps:

1. Open the "Software Units" folder in the project tree.
2. Select the Software Units you want to load.
3. Select one of the following commands in the shortcut menu of the "Download to device" submenu.

   - "Software (only changes)": This option only loads the selected Software Units. However, if changes have been made to other Software Units that result in inconsistencies with the selected units, these Software Units must also be loaded. In this case, the loading process cannot be performed and you must restart the loading with the option "Software (with related Software Units)".
   - "Software (with related Software Units)": This option loads the selected software units together with the software units to which relations are available, if necessary, to ensure the consistency of the online program.

   If an online connection is already defined, the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays messages and recommends actions needed for the loading operation. If you have not already established an online connection, the "Extended download to device" dialog opens. Then perform step 4.
4. Set all parameters required for the connection and click "Load".

   The "Load preview" dialog opens. This dialog displays messages and recommends actions needed for the loading operation.
5. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
6. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the load without synchronization by clicking "Force download to device". If you have performed the suggested actions, you are asked whether you want to continue with the download. Click "Continue download" to download the Software Units. The "Load results" dialog then opens and shows you the status and the actions after the load operation.
7. If the download was not performed in "RUN" mode and you want to start the modules again immediately after the download, select the "Start module" entry in the "Start modules after download" drop-down list.
8. To close the "Load results" dialog box, click "Finish".

##### Loading all Software Units to a device

Proceed as follows to load all Software Units in one loading operation to the device:

1. Select the "Software Units" folder in the project tree.
2. Select the "Download to device > Software (only changes)" command from the shortcut menu.

   If an online connection is already defined, the project data is compiled if necessary and the "Load preview" dialog opens. This dialog displays messages and recommends actions needed for the loading operation. If you have not already established an online connection, the "Extended download to device" dialog opens. Then perform step 3.
3. Set all parameters required for the connection and click "Load".

   The "Load preview" dialog opens. This dialog displays messages and recommends actions needed for the loading operation.
4. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
5. Click "Load".

   If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the load without synchronization by clicking "Force download to device". If you have performed the suggested actions, you are asked whether you want to continue with the download. Click "Continue download" to download the Software Units. The "Load results" dialog then opens and shows you the status and the actions after the load operation.
6. If the download was not performed in "RUN" mode and you want to start the modules again immediately after the download, select the "Start module" entry in the "Start modules after download" drop-down list.
7. To close the "Load results" dialog box, click "Finish".

##### Result

The Software Units are loaded to the device. If the changes affect additional objects, these are compiled and also loaded to the device. Objects that only exist online in the device are deleted. Be aware that loading individual Software Units can result in inconsistencies between the user program in the device and the user program in the offline project.

The messages under "About > General" in the Inspector window show whether the load process was successful.

#### Loading software units from a device (S7-1500)

You can either download software units separately from a device or together with all project data. In order to load the software units together with the project data from a device, read the description on the "[Uploading project data from a device](Editing%20project%20data.md#uploading-project-data-from-a-device)" page in the information system.

##### Procedure

To upload software units from a device, follow these steps:

1. Establish an online connection with the device from which you want to load the software units.

   See also: "[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)"
2. In the project tree, select the software units that you want to load from the device.
3. In the "Online" menu, select the "Upload from device" command.

   The "Upload preview" dialog box opens. This dialog displays messages and recommends actions needed for the loading operation.
4. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Upload from device" button is enabled.
5. Click "Upload from device".

   The loading operation is performed.

##### Result

The software units are loaded from the device to the project. You can edit and recompile them and load them to the device again.

#### Loading software units to a memory card (S7-1500)

You have the following options of loading project data together with software units to a memory card.

- Dragging project data to a memory card
- Writing project data to a memory card

##### Requirement

A memory card is displayed.

##### Procedure

To load software units together with other project data to a memory card, follow these steps:

1. In the project tree, drag the project data you want to load to the memory card. Please note that you cannot use the "Program blocks" folder as destination.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays messages and recommends actions needed for the loading operation.
2. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
3. Click "Load".
4. The loading operation is performed.

Or:

1. In the project navigation, select the project data that you want to load.
2. To do this, right-click the selection and select the "Copy" command from the shortcut menu. You can also use the key combination <Ctrl+C>.
3. Right-click the memory card and select the "Paste" command from the shortcut menu. You can also use the key combination <Ctrl+V>.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays messages and recommends actions needed for the loading operation.
4. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
5. Click "Load".

   The loading operation is performed.

Or:

1. In the project navigation, select the project data that you want to load.
2. Select the "Card Reader/USB memory > Write to memory card" command in the "Project" menu.

   The "Select memory card" dialog opens.
3. Select a memory card that is compatible with the CPU.

   A button with a green check mark is activated at the bottom of the dialog.
4. Click the button with the green check mark.

   If necessary, the project data is compiled. The "Load preview" dialog then opens. This dialog displays messages and recommends actions needed for the loading operation.
5. Check the messages and, where necessary, enable the actions in the "Action" column.

   As soon as loading becomes possible, the "Load" button is enabled.
6. Click "Load".

   The loading operation is performed.

#### Loading software units from a memory card (S7-1500)

To load software units together with other project data to a memory card, follow these steps: You have the following options for this:

- Load project data of the memory card as a new station

  With this option you upload the project data of a memory card to your project as a new station.
- Load project data of the memory card to an existing device

  With this option, you upload project data of a memory card to an existing device in your project.

##### Requirement

- A project is open.
- The memory card is displayed.

##### Loading as new station

To load project data from a memory card to your project, follow these steps:

1. In the project navigation, select the project data you want to upload.
2. Select "Upload device as new station (hardware and software)" in the "Online" menu.

Or:

1. In the project navigation, drag the memory card folder to the project.

Or:

1. Right-click the memory card.
2. Select the "Copy" command in the shortcut menu.
3. Right-click the project.
4. Select the "Paste" command in the shortcut menu.

##### Uploading to an existing device

To upload the project data of a memory card to an existing device, follow these steps:

1. In the project navigation, drag the folder of the memory card to a device in the project or copy the memory card and paste the data into a device.

   The "Upload preview" dialog box opens.
2. Check the messages in the "Upload preview" dialog, and select the necessary actions in the "Action" column.

   As soon as loading becomes possible, the "Upload from device" button is enabled.
3. Click "Upload from device".

   The loading operation is performed.

## Application example: Modularization of PLC programs with software units (S7-1500)

This section contains information on the following topics:

- [Introduction to the application example (S7-1500)](#introduction-to-the-application-example-s7-1500)
- [Modular structure of the application example (S7-1500)](#modular-structure-of-the-application-example-s7-1500)
- [Use of namespaces in the application example (S7-1500)](#use-of-namespaces-in-the-application-example-s7-1500)

### Introduction to the application example (S7-1500)

#### Objective of the application example

This application example serves as an introduction to the use of software units and namespaces in an automation project.

Using a "Pick & Place" application as an example, you will learn how to use software units to modularize your program technologically and administer data access between the individual modules.

A modularized and standardized automation solution offers the following advantages:

- The software will become more transparent, readable and, therefore, easier to use.
- Efficiency in program creation, documentation and commissioning is increased.
- The implementation of programming guidelines and style guide definitions is facilitated.
- Standardized program parts are easily reusable.
- Defined interfaces support the cooperation with other team members or external contractors.
- The jobs can be more easily divided into independent work packages.
- It is easier to automate program creation.
- Flexible management of machine versions is supported.
- Diagnostics and fault correction are simplified.
- Maintenance and servicing of the automation project is supported.

By using software units, you achieve a significant increase in efficiency and promote team collaboration.

#### Technological task

In the example, we want to control a process that places electronic components into workpieces (Pick & Place). In practice, this could be placing buttons into a cell phone.

A conveyor belt system transports a workpiece carrier to a work station. Here, the workpiece positioned on it is fitted by a robot with an electronic component from the storage unit.

![Technological task](images/156212914827_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Robot |
| ② | Electronic component |
| ③ | Workpiece on workpiece holder |
| ④ | Lagereinheit |

### Modular structure of the application example (S7-1500)

#### General program structure

The application example shows you a program that consists mainly of autonomous modules. The data exchange between modules is made easier through standardized interfaces.

The program consists of three levels:

- The "Global Environment" software unit forms the top program level and contains the following components:

  - Global machine data that must also be available outside the technological unit
  - Libraries with type-coded blocks that can be used multiple times
- The middle level contains several software units, each of which controls a plant unit:

  - "TrayStorage" controls the storage and delivery of the electronic components
  - "Placement" separates the parts from the storage system
  - "Assembly" controls the robot arm that places the parts in the workpiece
  - "Transport" coordinates the conveyor belt as well as the parts and workpiece supply
  - "Utility" ensures correct operation of the plant, for example, by checking the supply systems, testing the compressed air system or through power and energy management
- The "Machine Control" software unit forms the bottom program level. Here, the individual modules are centrally coordinated and controlled according to the operating mode.

All software units are encapsulated units. Data exchange is only possible in vertical direction from bottom to top. As a result, no circular relations can arise.

The following figure shows the program structure:

![General program structure](images/149396293899_DV_resource.Stream@PNG-de-DE.png)

#### Structure of the individual software units

All software units have the same standardized structure based on a template. The program elements have standardized names that are identical in all software units. Only the namespaces differ.

Each software unit contains three organization blocks at the top level:

- Main
- ProDiag
- Startup

There are two areas below this:

- Public

  This area contains all published data that must be available outside the software unit. The "Public" area thus represents the interface of the software unit. Other software units can access the data via this interface.  
  For example, the "Machine Control" software unit writes information for the pending operating mode to the "Public" area of the other software units. There, the information is queried and processed by the underlying blocks.
- Private

  This area contains all data and blocks that are only available within the software unit.

The following screen shows the schematic structure of a software unit and its relationships to other program levels.

![Structure of the individual software units](images/149396285707_DV_resource.Stream@PNG-de-DE.png)

#### Advantages of the modular concept

The modular structure offers the following advantages:

- Due to the extensive encapsulation of the program code, you can program, load and test the individual software units independently.
- The modular structure makes it easy to add new software units and adapt or replace existing software units. To add a new software unit, you only need to copy the existing template and change the preset for the namespace. The names of the program elements do not have to be changed.

  If you want to have a contractor program a new software unit for you, for example, you can just provide the "Template" and "GlobalEnvironment" software units. This information is sufficient to create a new software unit that meets your company standard.
- Adding new modules has only a minor impact on the central "Machine Control" software unit. Because the interface structure of the new module is standardized, there is no need to program the data exchange again. Only existing iteration loops must be extended by the new module.

### Use of namespaces in the application example (S7-1500)

The use of namespaces increases the efficiency in programming and the clarity of the program code.

Namespaces support you, for example, in the following areas:

- Deriving software units without renaming the underlying blocks
- Clear representation of elements in the project tree
- Clear representation of operands in the program code

This is shown below using the "GroupAssembly" software unit.

#### Deriving software units

Deriving software units is made easier through namespaces. Because there now may be several program elements with the same name in a CPU, the program elements in a derived software unit must not be renamed.

Only a few steps are necessary, for example, to derive the "GroupAssembly" software unit from a template:

1. Copy the template.
2. Adapt the name and the namespace preset of the software unit.
3. Transfer the namespace to the underlying program elements.

See also: [Changing the namespace preset of a software unit](#changing-the-namespace-preset-of-a-software-unit-s7-1500)

The figure below shows the standardized template and the "GroupAssembly" software unit generated from it. The new software unit only differs in the name and in the namespace preset from the template.

The names of the program elements are identical.

![Deriving software units](images/154801249931_DV_resource.Stream@PNG-en-US.png)

#### Clear representation of elements in the project tree

The representation of the program structure in the project tree is clearly organized: The namespace of an element is only displayed when it differs from the preset.

The "GroupAssembly" software unit has the namespace preset, "Assembly". Most of the underlying program elements adopt this preset. In the project tree, these elements are only displayed with their standardized names, for example, "Main" or "GroupLayer".

The "Robot" function block, for example, comes from a global library and therefore has the different namespace, "LDigi". This makes it easy for the programmer to see that this is a central library element. Libraries of suppliers can, for example, be given the name of the manufacturer as namespace.

![Clear representation of elements in the project tree](images/152274213259_DV_resource.Stream@PNG-de-DE.png)

#### Clear representation of operands in the program code

The display of operands also becomes clearer through the use of namespaces:

- If the operand comes from the same namespace as the block used, only the operand name is displayed.
- If the operand comes from a different namespace, the fully qualified name [namespace].[Operand name] is displayed.

Moreover, the IEC-compliant notation of data blocks without quotation marks also makes for a more clearly structured representation.

The following figure shows the "GroupLayer" FB with interconnected input parameters. In this case, it is easily recognizable which tags are in the "Assembly" namespace together with "GroupLayer" and which tags are in a different namespace.

![Clear representation of operands in the program code](images/153683459595_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Tag in the same namespace as the "Group Layer" block (both are in the "Assembly" namespace).   Only the operand name is displayed. |
| ② | Tag from a different namespace.   The fully qualified name of the operand is displayed: [namespace].[subnamespace].[operand name] |

#### Conclusion

The application example has shown how the use of software units and namespaces makes it easier to break down programs into independent modules and that it also supports standardization tasks.

It also demonstrates a way to efficiently transfer program parts to suppliers and assemble them into one total project once they are completed.

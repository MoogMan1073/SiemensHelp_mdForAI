---
title: "Programming basics"
package: ProgPLCBasicsenUS
topics: 104
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Programming basics

This section contains information on the following topics:

- [Operating system and user program](#operating-system-and-user-program)
- [Blocks in the user program](#blocks-in-the-user-program)
- [Block calls](#block-calls)
- [Using and addressing operands](#using-and-addressing-operands)
- [Serializing structures for data exchange](#serializing-structures-for-data-exchange)
- [Handling program execution errors](#handling-program-execution-errors)
- [Program flow control](Program%20flow%20control.md#program-flow-control)

## Operating system and user program

The following figure shows the interaction of the operating system and the user program:

![Figure](images/108688279691_DV_resource.Stream@PNG-en-US.png)

### Operating system (OS)

The operating system is contained in every CPU and organizes all CPU functions and sequences that are not associated with a specific control task.

The tasks of the operating system, for example, include the following:

- Processing a warm restart
- Updating the process image of the inputs and outputs
- Calling the user program
- Detecting interrupts and calling interrupt OBs
- Detecting and handling errors
- Managing memory areas

The operating system is a component of the CPU and is already installed there upon delivery.

### User program

The user program contains all functions that are necessary for processing your specific automation task.

The tasks of the user program include:

- Checking the requirements for a (warm) restart using startup OBs, for example, limit switch in correct position or safety relay active.
- Processing process data, e.g. linking binary signals, reading in and evaluating analog values, defining binary signals for output, and outputting analog values
- Reaction to interrupts, for example, diagnostic error interrupt if the limit value of an analog expansion module is overshot
- Error handling in normal program execution

You write the user program and load it into the CPU.

## Blocks in the user program

This section contains information on the following topics:

- [Linear and structured programming](#linear-and-structured-programming)
- [Overview of the block types](#overview-of-the-block-types)
- [Organization blocks (OB)](#organization-blocks-ob)
- [Functions (FCs)](#functions-fcs)
- [Function blocks (FB)](#function-blocks-fb)
- [Global data blocks (DB)](#global-data-blocks-db)
- [Global ARRAY data blocks (DB)](#global-array-data-blocks-db)
- [Example of the use of ARRAY data blocks](#example-of-the-use-of-array-data-blocks)
- [Instance data blocks](#instance-data-blocks)
- [CPU data blocks](#cpu-data-blocks)
- [Blocks with optimized access](#blocks-with-optimized-access)

### Linear and structured programming

#### Linear programming

Solutions for small automation tasks can be programmed linearly in a program cycle OB. This is only recommended for simple programs.

The following figure shows a linear program schematically: The "Main" cycle OB contains the complete user program.

![Linear programming](images/108647954699_DV_resource.Stream@PNG-en-US.png)

#### Structured programming

Complex automation tasks can be more easily handled and managed by dividing them into smaller sub-tasks that correspond to the technological functions of the process or that can be reused. These sub-tasks are represented in the user program by blocks. Each block is then an independent section of the user program.

Structuring the program offers the following advantages:

- Extensive programs are easier to program through the structure.
- Individual program sections can be standardized and used repeatedly with changing parameters.
- Program organization is simplified.
- Changes to the program can be made more easily.
- Debugging is simplified since separate sections can be tested.
- Commissioning is simplified.

The following figure shows a structured program schematically: The "Main" cycle OB calls subprograms in succession to execute defined subtasks.

![Structured programming](images/108647950603_DV_resource.Stream@PNG-en-US.png)

#### Nesting depth for blocks

The permissible nesting depth for blocks depends on the CPU that is used.

The following table shows the guide values for the maximum nesting depth. For detailed information on the CPU you are using, refer to the technical specifications in the hardware documentation. To call the hardware documentation on the Internet, click the links in the table.

| CPU family | Nesting depth (guide value) | Link to hardware documentation |
| --- | --- | --- |
| S7-1500 | 24 blocks per priority class | [SIMATIC S7-1500 / ET 200MP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/86140384) |
| S7-1200 | 16 blocks from cycle or startup OB, 6 additional blocks within any interrupt event OB | [SIMATIC S7-1200 Automation System](https://support.industry.siemens.com/cs/ww/en/view/91696622) |
| S7-400 | 24 blocks per priority class, 1-2 additional blocks within an error OB | [SIMATIC S7-400 automation system S7-400 CPU data](https://support.industry.siemens.com/cs/de/en/view/53385241) |
| S7-300 | 16 blocks per priority class, 4 additional blocks within an error OB | [SIMATIC S7-300 CPU 31xC and CPU 31x: Technical specifications](https://support.industry.siemens.com/cs/de/de/view/12996906/en) |
| ET 200SP | 24 blocks | [SIMATIC ET 200SP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/84133942) |

#### Nesting depth for structures

Structures (STRUCT) and PLC data types (UDT) can be nested to a depth of 8. This nesting depth is independent of the CPU used.

### Overview of the block types

#### Block types

Different BLOCK types are available to perform tasks within an automation system. The following table shows the available block types:

| Block type | Brief description |
| --- | --- |
| [Organization blocks](#organization-blocks-ob)  (OB) | Organization blocks define the structure of the user program. |
| [Functions](#functions-fcs)  (FC) | Functions contain program routines for recurring tasks. They have no "memory". |
| [Function blocks](#function-blocks-fb)  (FB) | Function blocks are code blocks that store their values permanently in instance data blocks, so that they remain available even after the block has been executed. |
| [Instance data blocks](#instance-data-blocks) | Instance data blocks are assigned to a function block when it is is called for the purpose of storing program data. |
| [Global data blocks](#global-data-blocks-db) | Global data blocks are data areas for storing data that can be used by any blocks. |

### Organization blocks (OB)

#### Definition

Organization blocks (OBs) form the interface between the operating system and the user program. They are called by the operating system and control, for example, the following operations:

- Startup characteristics of the automation system
- Cyclic program processing
- Interrupt-driven program execution
- Error handling

You can program the organization blocks and at the same time determine the behavior of the CPU. Various organization blocks are available to you depending on the CPU used.

For more information on organization blocks, refer to the descriptions of the modes of operation of CPUs in the "[Create configurations](Configuring%20devices%20and%20networks.md#creating-configurations)" section under "Configuring automation systems".

#### Start information of organization blocks

When certain organization blocks are started, the operating system provides information that can be evaluated in the user program. Refer to the descriptions of the organization blocks to find out which information is provided, if any.

---

**See also**

[Creating organization blocks](Creating%20and%20managing%20blocks.md#creating-organization-blocks)

### Functions (FCs)

#### Definition

[Functions](#)
 (A function (FC) is a code block without memory according to IEC 1131-3. A function gives you the option to transfer parameters in the user program. Functions are therefore particularly suitable for frequently recurring complex constructs, such as calculations. )  (FCs) are code blocks without memory. You have no data memory in which values of block parameters can be stored. Therefore, when a function is called, all formal parameters must be assigned actual parameters.   
Functions can use global [data blocks](#) (A data block is used to store user data. There are global data blocks that can be accessed by all code blocks and instance data blocks that are assigned to a specific FB call.)  to store data permanently.

#### Application

A function contains a program that is executed when the function is called by another code block. Functions can be used, for example, for the following purposes:

- To return function values to the calling block, e.g. for mathematical functions
- To execute technological functions, e.g. individual controls using bit logic operations

A function can also be called several times at different points in a program. As a result, they simplify programming of frequently recurring functions.

> **Note**
>
> **Parameter transfer when calling functions**
>
> To avoid errors when working with functions, observe the information in chapter "[Parameter transfer at block call](#parameter-transfer-at-block-call)".

---

**See also**

[Creating functions and function blocks](Creating%20and%20managing%20blocks.md#creating-functions-and-function-blocks)

### Function blocks (FB)

#### Definition

Function blocks are code blocks that store their input, output and in-out parameters permanently in instance data blocks, so that they remain available even after the block has been executed. Therefore they are also referred to as blocks "with memory".

Function blocks can also operate with temporary tags. Temporary tags are will not be stored in the instance DB, but are available for one cycle only.

#### Application

Function blocks contain subroutines that are always executed when a function block is called by another code block. A function block can also be called several times at different points in a program. As a result, they simplify programming of frequently recurring functions.

#### Instances of function blocks

A call of a function block is referred to as an instance. An instance data block is required for each instance of a function block; it contains instance-specific values for the formal parameters declared in the function block.

The function block can store its instance-specific data in its own instance data block or in the instance data block of the calling block.

#### Access modes

S7-1200 and S7-1500 offer two different access options for the instance data blocks, which can be assigned to a function block when this is called:

- Data blocks with optimized access

  Data blocks with optimized access have no firmly defined memory structure. The data elements contain only a symbolic name in the declaration, no fixed address within the block.
- Data blocks with standard access (compatible with S7-300/400)

  Data blocks with standard access have a fixed memory structure. The declaration elements contain both a symbolic name in the declaration and a fixed address within the block.

> **Note**
>
> To avoid errors when working with function blocks, refer to the section "[Parameter transfer at block call](#parameter-transfer-at-block-call)".

---

**See also**

[Calling a function by another function](#calling-a-function-by-another-function)
  
[Creating functions and function blocks](Creating%20and%20managing%20blocks.md#creating-functions-and-function-blocks)
  
[Multi-instances](#multi-instances)
  
[Instance data blocks](#instance-data-blocks)
  
[Basics of block access](#basics-of-block-access)

### Global data blocks (DB)

#### Definition

Data blocks are used to store program data. Data blocks thus contain variable data that is used by the user program. Global data blocks store data that can be used by all other blocks.

The maximum size of data blocks varies depending on the CPU. You can define the structure of global data blocks anyway you please.

You also have the option of using PLC data types (UDT) as a template for creating global data blocks.

#### Global data blocks in the user program

Every function block, function, or organization block can read the data from a global data block or can itself write data to a global data block. This data remains in the data block even after the data block is exited. A global data block and an instance data block can be open at the same time.

The following figure shows the different accesses to data blocks:

![Global data blocks in the user program](images/108704072459_DV_resource.Stream@PNG-en-US.png)

#### Access modes

S7-1200 and S7-1500 offer two different access options for global data blocks:

- Data blocks with optimized access

  Data blocks with optimized access have no fixed defined structure. In the declaration, the data elements are assigned only a symbolic name and no fixed address within the block.
- Data blocks with standard access (compatible with S7-300/400)

  Data blocks with standard access have a fixed structure. In the declaration, the data elements are assigned both a symbolic name and a fixed address within the block.

---

**See also**

[Creating data blocks](Programming%20data%20blocks.md#creating-data-blocks)
  
[Basics of block access](#basics-of-block-access)

### Global ARRAY data blocks (DB)

#### ARRAY data blocks (S7-1500)

ARRAY data blocks are a particular type of global data block. These consist of an ARRAY of any data type. For example, an ARRAY of a PLC data type (UDT) is possible. The DB contains no other elements besides the ARRAY. Because of their flat structure, ARRAY data blocks facilitate access to the ARRAY elements and their transfer to called blocks.

The "Optimized block access" attribute is always enabled for ARRAY data blocks. ARRAY data blocks with standard access are not possible.

The "Instructions &gt; Basic instructions" task card in the "Move &gt; ARRAY DB" section offers extended options for addressing ARRAY DBs. These instructions give you the option, for example, to address the DB name indirectly:

- ReadFromArrayDB: Read from array data block
- WriteToArrayDB: Write to ARRAY data block
- ReadFromArrayDBL: Read from ARRAY data block in load memory
- WriteToArrayDBL: Write to ARRAY data block in load memory

---

**See also**

[Addressing tags in ARRAY data blocks (S7-1500)](#addressing-tags-in-array-data-blocks-s7-1500)
  
[Creating data blocks](Programming%20data%20blocks.md#creating-data-blocks)
  
[Example of the use of ARRAY data blocks](#example-of-the-use-of-array-data-blocks)

### Example of the use of ARRAY data blocks

#### Using an ARRAY data block (S7-1500)

ARRAY data blocks are global data blocks that consist exclusively of an ARRAY. A data block with a tag of the ARRAY data type is sufficient for most applications because access can be programmed intuitively with a tag of the ARRAY data type (for example, #myArray[#index]) and offer a better runtime performance than ARRAY data blocks. In certain scenarios, however, it is necessary to process ARRAYs with different lengths. The ARRAY data block is particularly suitable for these scenarios.

The following example shows how you can use an ARRAY data block.

#### Programming example

Individual pieces of material are transported on a conveyor belt. These pieces of material pass a scanner which can read out the information that a piece of material carries with it. The information is read out and transmitted to a panel. Because the scanner and the panel have different clock cycles/speeds, the material information must be cached in each case.

In the following programming example, we show you how to program the program code for passing on material information. For this purpose, you use an ARRAY data block.

The example is set up to be flexible, so that you do not have to know at the time the program code is created which ARRAY data block will be read or written or how large it is. You can thus use ARRAYs of different length. Use of data type DB_ANY gives you this flexibility.

The data type VARIANT is used so that you also have flexibility when specifying the value that is to be read or written.

Not until runtime is the ARRAY data block transferred in order to then access the values in the program block. The data type of the ARRAY elements and the data type of the value that is to be read or written are determined.

You can determine the number of objects and the fill level of the ARRAY data block using special instructions.

![Programming example](images/133507894411_DV_resource.Stream@PNG-en-US.png)

#### Procedure

Create the PLC data type "UDT_Queue". This PLC data type is used by both functions ("FC_Enqueue" and "FC_Dequeue"). This is important, for example, for accessing the tag #Queue.Used, as the function "FC_Enqueue" increments the tag by one and the function "FC_Dequeue" decrements the tag by one.

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare the following lines within the PLC data type:

   DB &gt; Data type: DB_ANY

   Size &gt; Data type: DINT

   Used &gt; Data type: DINT

   ReadPos &gt; Data type: DINT

   WritePos &gt; Data type: DINT

   ![Procedure](images/67928633995_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67928633995_DV_resource.Stream@PNG-de-DE.png)

Program the "FC_Enqueue" function, which writes the values of the material information to an ARRAY data block. The specific ARRAY data block and the data type of the value do not have to known at this time, because the interfaces are being programmed with the VARIANT and DB_ANY data types.

1. Create an SCL function and name it "FC_Enqueue".
2. Declare the block interface as follows:

   ![Procedure](images/67929046155_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67929046155_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![Procedure](images/67948895883_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67948895883_DV_resource.Stream@PNG-de-DE.png)

   With this function, you check whether there is still space free in the data block. If so, write the value that is specified at the parameter value into the data block at the parameter db. With each new item of material information that is written, the tag #Queue.Used and the pointer tag #Queue.WritePos are incremented by one. As soon as the cursor reaches the end of the data block, it is reset to 0. If the data block is full, the error code #4711 is returned.

Program the "FC_Dequeue" function, which reads the material information from an ARRAY data block and writes it to the panel. The specific ARRAY data block and the data type of the value do not have to known at this time, because the interfaces are being programmed with the VARIANT and DB_ANY data types. The material information can then be displayed on a panel, for example:

1. Create an SCL function and name it "FC_Dequeue".
2. Declare the block interface as follows:

   ![Procedure](images/67948903563_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67948903563_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![Procedure](images/67954978443_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67954978443_DV_resource.Stream@PNG-de-DE.png)

   With this function, you check whether material information is available in the data block. If so, read the value to which the pointer #Queue.ReadPos points, and write it to the tag #Value. With each item of material information that is read, the tag #Queue.Used is decremented by one and the pointer tag #Queue.ReadPos is incremented by one. As soon as the cursor reaches the end of the data block, it is reset to 0. If the data block is empty, the error code #4712 is returned.

To save the material data, create an ARRAY data block. Use the PLC data type "UDT_Material" as the data type of the ARRAY data block.

First, create the PLC data type "UDT_Material". This PLC data type contains a structure for the material information supplied by the scanner.

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare the following lines within the PLC data type:

   ArticleNumber &gt; Data type: DINT

   ArticleName &gt; Data type: STRING

   Amount &gt; Data type: REAL

   Unit &gt; Data type: STRING

   ![Procedure](images/67954987147_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67954987147_DV_resource.Stream@PNG-de-DE.png)

Create the ARRAY data block "DB_MaterialBuffer". The ARRAY data block is to contain data records with material information of data type "UDT_Material". The material information is written to the ARRAY data block using the "FC_Enqueue" function.

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click "Data block (DB)".
3. Enter the name "DB_MaterialBuffer".
4. Select the type of the data block "ARRAY DB".
5. Select the PLC data type "UDT_Material" as ARRAY data type.
6. Specify "1000" as high ARRAY limit.
7. Click "OK".

   ![Procedure](images/67956941579_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67956941579_DV_resource.Stream@PNG-de-DE.png)

Create the data block "DB_MaterialQueue". The data block is to contain information of data type "UDT_Queue" on the ARRAY data block. The information is written using the OB "OB_MaterialQueue".

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click "Data block (DB)".
3. Enter the name "DB_MaterialQueue".
4. Select the PLC data type "UDT_Queue" as data type.
5. Click "OK".

   ![Procedure](images/133423336587_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/133423336587_DV_resource.Stream@PNG-de-DE.png)

Create the startup organization block (OB) "OB_MaterialQueue". In this organization block, you initialize the tags DB and Size.

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Organization block (OB)" button.
3. Enter the name "OB_MaterialQueue".
4. Select the type "Startup".
5. Select SCL as the language of the organization block.
6. Click "OK".
7. Write the following program code:

   ![Procedure](images/68337179019_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/68337179019_DV_resource.Stream@PNG-de-DE.png)

   Enter the size of the ARRAY data block at the Size parameter. The start value of the Used parameter is "0". The first item of material information is thus written to the ARRAY element "0".

By assigning the data block, you connect the ARRAY data block "DB_MaterialBuffer" with the SCL functions "FC_Enqueue" and "FC_Dequeue".

1. Declare the following tags in the "Default tag table":

   ![Procedure](images/67980494859_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67980494859_DV_resource.Stream@PNG-de-DE.png)
2. Call the SCL function "FC_Enqueue" within the function block in which the scanner reads out the material information.
3. In section "Temp" of the block interface, declare the tags "ConnectionToUDT" (data type "UDT_Material") and "Error" (data type INT):

   ![Procedure](images/133424305163_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/133424305163_DV_resource.Stream@PNG-de-DE.png)
4. Link the function call with the following tags and, at the enable input EN, create the signal edge "P: Scan operand for positive signal edge". Link the signal edge with the global tags from the standard tag table:

   ![Procedure](images/67929053835_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67929053835_DV_resource.Stream@PNG-de-DE.png)
5. Call the SCL function "FC_Dequeue"
6. Link the function call with the following tags and, at the enable input EN, create the signal edge "P: Scan operand for positive signal edge". Link the signal edge with the global tags from the standard tag table:

   ![Procedure](images/67981842827_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67981842827_DV_resource.Stream@PNG-de-DE.png)

#### Result

As soon as a positive signal edge occurs, material information is written to an ARRAY data block with the help of the instruction "WriteToArrayDB" and sent to the panel with the help of the instruction "ReadFromArrayDB".

---

**See also**

[Global ARRAY data blocks (DB)](#global-array-data-blocks-db)
  
[Addressing tags in ARRAY data blocks (S7-1500)](#addressing-tags-in-array-data-blocks-s7-1500)

### Instance data blocks

#### Definition

The call of a function block is referred to as an instance. The data with which the instance works is stored in an instance data block.

The maximum size of instance data blocks varies depending on the CPU. The tags declared in the function block determine the structure of the instance data block.

#### Access modes

S7-1200 and S7-1500 offer two different access options for the instance data blocks, which can be assigned to a function block when this is called:

- Data blocks with optimized access

  Data blocks with optimized access have no firmly defined structure. The declaration elements contain only one symbolic name in the declaration, and no fixed address within the block.
- Data blocks with standard access (compatible with S7-300/400)

  Data blocks with standard access have a fixed structure. The declaration elements contain both a symbolic name in the declaration and a fixed address within the block.

---

**See also**

[Creating data blocks](Creating%20and%20managing%20blocks.md#creating-data-blocks)
  
[Basics of block access](#basics-of-block-access)
  
[Instances](#instances)
  
[Insert block calls in LAD](Creating%20LAD%20programs.md#insert-block-calls-in-lad)
  
[Inserting block calls in FBD](Creating%20FBD%20programs.md#inserting-block-calls-in-fbd)

### CPU data blocks

#### Definition

CPU data blocks are generated by the CPU at runtime. To this purpose, insert the "CREATE_DB" instruction into your user program. You can use the data block that is generated at runtime to save your data.

CPU data blocks are indicated by means of a small CPU icon in the "Program blocks" folder of an available node. You can monitor the values of the variables of a CPU data block in online mode, similar to those of a different data block type.

You cannot create CPU data blocks in your offline project.

#### Loading CPU data blocks

The CPU data block that the user program has generated by means of the "CREATE_DB" instruction is initially only available on the device in online mode. All CPU data blocks will be included with the other blocks the next time you perform a complete download from the device to the project. The CPU data blocks are marked with a small CPU icon in the process. However, you cannot upload these CPU data blocks to your device again.

#### Restrictions on CPU data blocks in the project

Once the CPU data blocks have been loaded into your offline project, you can open and view their content. However, note that the CPU data blocks in the project are write-protected. The CPU data blocks in the project are therefore subject to the following restrictions:

- You cannot edit CPU data blocks, or convert these into a different data block type.
- CPU data blocks cannot be assigned a know-how protection.
- You cannot change the programming language of a CPU data block.
- CPU data blocks cannot be compiled or downloaded to a device.

#### Comparing CPU data blocks

Once the CPU data blocks have been loaded into your offline project, you can run an offline/online comparison for the CPU DBs loaded. The comparison editor provides you with a corresponding overview of the differences. It is possible to synchronize the online and off-line version of CPU data blocks if differences are found, but not by downloading the offline version to the device.

#### Deleting CPU data blocks

You can delete CPU data blocks both from the project and from the CPU.

---

**See also**

[Deleting CPU data blocks](Creating%20and%20managing%20blocks.md#deleting-cpu-data-blocks)

### Blocks with optimized access

This section contains information on the following topics:

- [Basics of block access](#basics-of-block-access)
- [Setting up block access](#setting-up-block-access)

#### Basics of block access

##### Introduction

STEP 7 offers data blocks with different access options:

- Data blocks with optimized access (S7-1200/S7-1500)
- Data blocks with standard access (S7-300 / S7-400 / S7-1200 / S7-1500)

Within one program you can combine the two types of blocks.

##### Data blocks with optimized access

Data blocks with optimized access have no fixed defined structure. In the declaration, the data elements are assigned only a symbolic name and no fixed address within the block. The elements are saved automatically in the available memory area of the block so that there are no gaps in the memory. This makes for optimal use of the memory capacity.

Tags are identified by their symbolic names in these data blocks. To address the tag, enter its symbolic name. For example, you access the "Fill Level" tag in the "Data" DB as follows:

"Data".Fill Level

Blocks with optimized access offers the following advantages:

- You can create data blocks with any structure without paying attention to the physical arrangement of the individual data elements.
- Quick access to the optimized data is always available because the data storage is optimized and managed by the system.
- Access errors, as with indirect addressing or from the HMI, for example, are not possible.
- You can define specific individual tags as retentive.
- Optimized blocks are equipped with a memory reserve by default which lets you expand the interfaces of function blocks or data blocks during operation. You can download the modified blocks without setting the CPU to STOP and without affecting the values of already loaded tags.

> **Note**
>
> The "Optimized block access" attribute is always enabled for the following blocks and cannot be deselected.
>
> - GRAPH blocks
> - CEM blocks
> - ARRAY data blocks

##### Data blocks with standard access

Data blocks with standard access have a fixed structure. In the declaration, the data elements are assigned both a symbolic name and a fixed address within the block. The address is shown in the "Offset" column.

Tags in these data blocks can be addressed in both symbolic and absolute form.

"Data".Fill Level

DB1.DBW2

##### Setting Retentivity for Optimized Access or Standard Access

If you define data as retentive, its values are retained even after a power failure or a network off. A retentive tag is not initialized after the hot restart but retains the value it had prior to the power failure. If a DB tag is defined as retentive, it is stored in the retentive memory area of the data block.

The options for setting the retentivity depend on the access type of the block.

- In data blocks with standard access, you cannot set the retentive behavior of individual tags. The retentivity setting is valid for all tags of the data block.
- In data blocks with optimized access you can define the retentive behavior of individual tags.

  For structured data type tags, the retentivity setting always applies to the entire structure. You cannot make any individual retentivity setting for separate elements within the data type.

##### Setting Addressing Options for Optimized Access or Standard Access

Blocks with optimized access permit only "type-safe" access. Type-safe access addresses tags by their symbolic name only. This means even changes to the block or the block interface will not result in inconsistencies in the program or access errors.

The following table shows the permitted addressing options for optimized data:

| Addressing | Block with standard access | Block with optimized access |
| --- | --- | --- |
| Symbolic addressing | x | x |
| Indexed addressing of ARRAYs | - | x |
| Slice access | x | x |
| Overlapping with AT | x | - |
| Absolute addressing | x | - |
| Indirect addressing via ANY | x | - |
| Indirect addressing via POINTER and VARIANT | x | with symbolic notation only |
| Indirect addressing via references | - | x |

---

**See also**

[Setting up block access](#setting-up-block-access)
  
[Addressing variables in data blocks](#addressing-variables-in-data-blocks)
  
[Retentive memory areas (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#retentive-memory-areas-s7-1200)
  
[Creating blocks](Creating%20and%20managing%20blocks.md#creating-blocks)

#### Setting up block access

##### Introduction

Block access is set up automatically when you create a block:

- Blocks created on CPUs of the S7-1200/1500 product range provide optimized access by means of a default setting.
- New blocks created on CPUs of the S7-300/S7-400 product range provide standard access by means of a default setting.

Access to a block that you copy or migrate to a CPU of a different product range is not converted automatically. However, in certain situations it may be useful to change block access in manual mode, e.g., in order to utilize the full functional scope of the CPU.

In most cases, you will have to recompile and load the program after block access has been converted.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Optimized block access for GRAPH blocks**  The "Optimized block access" attribute is always enabled for GRAPH blocks in S7-1500 and cannot be deselected. |  |

##### Procedure

To set the block access, proceed as follows:

1. Open the "Program blocks" folder in the project tree.
2. Right-click on the block whose block access you want to change.
3. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the block opens.
4. Click "Attributes" in the area navigation.
5. Enable or disable the "Optimized block access" option.
6. Confirm your entries with "OK".

##### Restrictions and special features

As a matter of principle, you can only convert block access on CPUs of the S7-1200/1500 product range, as only these support the "optimized" access mode.

The following restrictions or special features apply in this context:

- Instance data blocks

  The block access of instance data blocks is always determined by the assigned function block and cannot be changed in manual mode. If you change the access mode on a function block, you also need to update the assigned instance data blocks. This update procedure adapts the access mode of the instance data block.
- System blocks and know-how protected blocks

  You cannot manually edit the block access for system blocks and know-how protected blocks.
- Organization blocks

  The start information of an OB with standard access is always stored in the first 20 bytes of the "Temp" section in the block interface. By contrast, the start information of an OB with optimized access is always written to the "Input" section. For this reason, the block interface of OBs will also change whenever you convert block access. Additional information is provided in the following sections.

##### Converting block access from "standard" to "optimized".

A block copied from the CPU of the S7-300/400 product range to a CPU of the S7-1200/1500 product range will initially retain the "standard" access mode. However, you can significantly increase the performance of program execution by using blocks with optimized access, which is why it may be useful to modify the access mode manually.

The blocks are adapted as follows in the course of conversion:

- Function blocks

  All interface parameters are assigned the "Non-retain" retentivity setting.
- Global data blocks

  The retentivity setting that was assigned centrally to the entire data block is transferred to the individual interface parameters. It is now possible to manipulate the retentivity setting of the various parameters.

  However, the following rule will still apply: For structured data type tags, the retentivity setting always applies to the entire structure. You cannot assign separate retentivity settings to the various elements within a structured data type. It therefore follows that you cannot assign individual retentivity settings to the tags of data blocks that are based on PLC data types.
- Organization blocks

  All interface parameters that are stored in the first 20 bytes of the "Temp" section will be deleted. New CPU-specific start information is entered in the "Input" section. Naming conflicts with user-defined interface parameters occurring in the process are resolved by renaming the user-defined interface parameters.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **The conversion of the block access has the following consequences:**  - Absolute addressing of the interface parameters of the block is no longer possible after conversion of block access to the "optimized mode.   Example: `#L0.1` is no longer valid. - Since conversion to the "optimized" block access mode of organization blocks also modifies the OB interface,   you may possibly have to adapt, recompile and load the program again due to these changes. |  |

##### Converting block access from "optimized" to "standard".

If you want to copy or move a block from the CPU of the S7-300/400 product range to a CPU of the S7-1200/1500 product range, you first need to set the "standard" access mode.

The blocks are adapted as follows in the course of conversion:

- Function blocks and global data blocks.

  You can no longer set a retentivity in the function block. The corresponding setting is made in the instance data block.

  All interface parameters in the instance DB or global DB are assigned the same retentivity setting. The conversion is subject to the following rule:

  - If all interface parameters in the original block were retentive, the entire block will be retentive after conversion.
  - If all interface parameters in the original block were non-retentive, the entire block will be non-retentive after conversion.
  - If the interface parameters in the original block had different retentivity settings, the entire block will be non-retentive after conversion.
- Organization blocks

  All interface parameters stored in the "Input" section will be deleted. New CPU-specific start information is entered in the "Temp" section. This data is written to the first 20 bytes. Naming conflicts with user-defined interface parameters occurring in the process are resolved by renaming the user-defined interface parameters.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **The conversion of the block access has the following consequences:**  Since a conversion to "standard" block access mode might change the retentivity settings of the interface parameters, you may possibly have to adapt, recompile and load the program again due to these changes. |  |

---

**See also**

[Basics of block access](#basics-of-block-access)
  
[Specifying block properties](Creating%20and%20managing%20blocks.md#specifying-block-properties)

## Block calls

This section contains information on the following topics:

- [Principles of block calls](#principles-of-block-calls)
- [Call hierarchy](#call-hierarchy)
- [Instances](#instances)
- [Parameter transfer at block call](#parameter-transfer-at-block-call)

### Principles of block calls

#### Function of block calls

For your blocks to be executed in the user program, they need to be called from another block.

When one block calls another block, the instructions of the called block are executed. Only when execution of the called block has been completed does execution of the calling block resume. The execution is continued with the instruction that follows on the block call.

The following figure shows the sequence of a block call within a user program:

![Function of block calls](images/111001110539_DV_resource.Stream@PNG-en-US.png)

#### Parameter transfer

When a block is called, you must assign values to the parameters in the block interface. By providing input parameters you specify the data with which the block is executed. By providing the output parameters you specify where the execution results are saved.

---

**See also**

[Call hierarchy](#call-hierarchy)
  
[Basics of instances](#basics-of-instances)

### Call hierarchy

#### Definition

The order and nesting of block calls is referred to as the call hierarchy.

The following figure shows an example of the order and nesting of block calls within an execution cycle:

![Definition](images/108651744267_DV_resource.Stream@PNG-en-US.png)

#### Nesting depth for blocks

The permissible nesting depth for blocks depends on the CPU that is used.

The following table shows the guide values for the maximum nesting depth. For detailed information on the CPU you are using, refer to the technical specifications in the hardware documentation. To call the hardware documentation on the Internet, click the links in the table.

| CPU family | Nesting depth (guide value) | Link to hardware documentation |
| --- | --- | --- |
| S7-1500 | 24 blocks per priority class | [SIMATIC S7-1500 / ET 200MP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/86140384) |
| S7-1200 | 16 blocks from cycle or startup OB, 6 additional blocks within any interrupt event OB | [SIMATIC S7-1200 Automation System](https://support.industry.siemens.com/cs/ww/en/view/91696622) |
| S7-400 | 24 blocks per priority class, 1-2 additional blocks within an error OB | [SIMATIC S7-400 automation system S7-400 CPU data](https://support.industry.siemens.com/cs/de/en/view/53385241) |
| S7-300 | 16 blocks per priority class, 4 additional blocks within an error OB | [SIMATIC S7-300 CPU 31xC and CPU 31x: Technical specifications](https://support.industry.siemens.com/cs/de/de/view/12996906/en) |
| ET 200SP | 24 blocks | [SIMATIC ET 200SP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/84133942) |

#### Nesting depth for structures

Structures (STRUCT) and PLC data types (UDT) can be nested to a depth of 8. This nesting depth is independent of the CPU used.

---

**See also**

[Basics of instances](#basics-of-instances)
  
[Principles of block calls](#principles-of-block-calls)

### Instances

This section contains information on the following topics:

- [Basics of instances](#basics-of-instances)
- [Single instances](#single-instances)
- [Multi-instances](#multi-instances)
- [Parameter instances](#parameter-instances)
- [Examples of the use of parameter instances](#examples-of-the-use-of-parameter-instances)

#### Basics of instances

##### Definition

After a function block is called, it needs memory for its working data. This data is referred to as an instance.

Instances have the following properties:

- Instances are always assigned to an FB.
- The structure of an instance is derived from the interface of the associated FB and can only be changed there.
- Instances are created automatically when a function block is called.

##### Storage of instances

You have the following options for storing instances:

- Single instance:

  The called function block saves its data in an instance data block of its own.

  See also: [Single instances](#single-instances)
- Multi-instance:

  The called function block does not store its data in an instance data block of its own, but rather in the instance of another function block.

  See also: [Multi-instances](#multi-instances)
- Parameter instance:

  You transfer the instance of a function block to another block as an in-out parameter (InOut). This block can access the data in the transferred instance or call the associated FB.

  See also: [Parameter instances](#parameter-instances)

---

**See also**

[Overview of the block interface](Declaring%20the%20block%20interface.md#overview-of-the-block-interface)
  
[Addressing instance data](#addressing-instance-data)
  
[Addressing variables in data blocks](#addressing-variables-in-data-blocks)
  
[Principles of block calls](#principles-of-block-calls)
  
[Call hierarchy](#call-hierarchy)

#### Single instances

##### Definition

An instance of a function block (FB) that is located in its own instance DB is referred to as a single instance. The instance DB thus contains the working data for an individual block call.

##### Advantages

The use of single instances provides the following advantages:

- Reusability of the function blocks
- Good structuring options for simple programs

##### How single instances work

The following figure shows the FB "Caller" that uses another FB ("Valve"). "Valve" is called as a single instance, i.e. it stores its data in its own instance DB.

![How single instances work](images/121760796043_DV_resource.Stream@PNG-en-US.png)

The structure of the instance data block is defined by the interface of the corresponding FB and can only be changed there. The instance DB contains the following data:

- Block parameters

  The block parameters in the "Input", "Output" and "InOut" sections form the interface of the block for the call in the program.
- Static local data

  Static local data in the "Static" section is used for permanently storing intermediate results beyond the current program cycle, for example for storing the signal state for an edge evaluation.

##### Creating single instances

You have the following options for creating a single instance:

- When you call an FB in the program, the "Call options" dialog appears. Here, you can specify whether you want to call the FB as a single instance, multi-instance or parameter instance.
- When you create a new data block, the "Add new block" dialog opens. Here, you can select a function block that you want to create an instance data block for under "Type".

##### Calling single instances

When a single instance is called, the assigned instance data block is indicated.

The following figure shows the call of the "Block" block as a single instance in LAD. The instance data block "BlockData" is above the call.

![Calling single instances](images/121769154187_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces under: [Introduction to namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

---

**See also**

[Basics of instances](#basics-of-instances)
  
[Multi-instances](#multi-instances)

#### Multi-instances

##### Definition

When a function block (FB) calls another FB, its instance data can also be stored in the instance DB of the calling FB. This type of block call is referred to as a multi-instance.

##### Advantages

The use of multi-instances provides the following advantages:

- Good structuring options for complex blocks
- Lower number of instance DBs
- Easy programming of local subprograms, for example for local timers or edge evaluations.

##### How multi-instances work

The following figure shows an FB that uses another FB ("Valve"). "Valve" is called as a multi-instance, i.e. it stores its data in the instance DB of the calling FB. Multi-instance data is located in the "Static" section of the calling block. In CPUs of the S7-1200/S7-1500 series, the instance can also be located in the instance DB of another function block.

![How multi-instances work](images/121769278603_DV_resource.Stream@PNG-en-US.png)

##### Creating multi-instances

You have the following options for creating a multi-instance:

- When you call an FB in the program, the "Call options" dialog appears. Here, you can specify whether you want to call the FB as a single instance, multi-instance or parameter instance.
- You declare the multi-instance directly in the interface of the calling block.
- You declare the multi-instance in the interface of another function block (S7-1200/S7-1500).

See also: [Declaring multi-instances](Declaring%20the%20block%20interface.md#declaring-multi-instances)

##### ARRAYs of multi-instances

Multi-instances can also be created as an ARRAY. You can address the individual ARRAY elements using a variable index, for example when processing program loops.

![ARRAYs of multi-instances](images/121769308427_DV_resource.Stream@PNG-de-DE.png)

You declare ARRAYs of multi-instances directly in the interface of a function block.

##### Calling multi-instances

When a multi-instance is called, the assigned instance is indicated. The following figures show the call of the "Block" block as a multi-instance in LAD.

In the following example, the instance is located locally in the instance DB of the calling block:

![Calling multi-instances](images/121769312139_DV_resource.Stream@PNG-de-DE.png)

In the following example, the instance is located in the instance DB "MyOtherFB" (S7-1200/S7-1500):

![Calling multi-instances](images/121769315851_DV_resource.Stream@PNG-de-DE.png)

In the following example, the instance is located in an ARRAY of multi-instances in instance DB "MyOtherFB" (S7-1200/S7-1500):

![Calling multi-instances](images/121769357963_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces under: [Introduction to namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

---

**See also**

[Instance data blocks](#instance-data-blocks)
  
[Basics of instances](#basics-of-instances)
  
[Single instances](#single-instances)
  
[Example of using parameter instances in an ARRAY of multi-instances](#example-of-using-parameter-instances-in-an-array-of-multi-instances)

#### Parameter instances

##### Definition

The parameter instance provides a special option for instantiation:

Here, you transfer the block instance to be used to the calling block as an in-out parameter (InOut) during runtime.

##### Advantages

The use of parameter instances provides the following advantages:

- At runtime, you can define which instance is currently being used.
- You can process different instances iteratively in program loops.

> **Note**
>
> **Instance ARRAYs**
>
> To simplify the iterative processing of instances in program loops, define an ARRAY of instances, e.g.
>
> - ARRAY of data type "DB_ANY"
> - ARRAY of multi-instances
>
> You can address the individual ARRAY elements when processing program loops via a variable index.
>
> See also: [Examples of the use of parameter instances](#examples-of-the-use-of-parameter-instances)

##### How parameter instances work

The following figure shows the "Caller", which uses another FB ("Valve"). An instance of "Valve" is transferred as a parameter instance. To do this, define an in-out parameter ("#valveInstance") that will be used to transfer the specific instance at runtime.

![How parameter instances work](images/121770066187_DV_resource.Stream@PNG-en-US.png)

##### Creating parameter instances

Parameter instances are defined when a function block is called: When you call an FB, a dialog appears in which you can specify whether the FB will be called as a single instance, multi-instance or parameter instance. As an alternative, you also have the option of entering parameter instances manually directly in the block interface.

See also: [Declaring parameter instances](Declaring%20the%20block%20interface.md#declaring-parameter-instances)

The following figure shows the call of a parameter instance for the FB "Valve":

![Creating parameter instances](images/121770070411_DV_resource.Stream@PNG-en-US.png)

##### Transferring the instance as a parameter

Each time the higher-level FB is called ("Caller" in the example), transfer an instance for the called FB (in the example "Valve"). You can transfer the following types of instances:

- Single instance

  Transfer an existing instance DB of the called FB.
- Multi-instance

  Transfer an existing multi-instance of the called FB.
- Individual element of an ARRAY of multi-instances

  Transfer an element of an existing ARRAY of multi-instances.
- Tag of the "DB_Any" data type (S7-1200 &gt;= V4.2 / S7-1500 &gt;= V2.0)

  Transfer a tag of the data type "DB_Any" to which you assign a corresponding instance during runtime.  
  Note that this type of parameter transfer is not possible for instances of system blocks from the task card "Instructions".

The following figure shows the call of the FB "Caller". With the "valveInstance" parameter, the instance "#currValve" is transferred. This instance, which is pending at the #currValve parameter during runtime, is used to call "Valve".

![Transferring the instance as a parameter](images/121770202763_DV_resource.Stream@PNG-de-DE.png)

In CPUs of the S7-1200/S7-1500 series, you can also transfer instances as parameters that are located in the instance DB of another block.

In the following example, the transferred instance is located in instance DB "MyOtherIDB" (S7-1200/S7-1500):

![Transferring the instance as a parameter](images/121770206475_DV_resource.Stream@PNG-de-DE.png)

In the following example, the transferred instance is located in an ARRAY of multi-instances in instance DB "MyOtherIDB" (S7-1200/S7-1500):

![Transferring the instance as a parameter](images/121770210187_DV_resource.Stream@PNG-de-DE.png)

In the following example, an instance transferred from an ARRAY of data type "DB_ANY" in the global data block "DB_ValveInstances":

![Transferring the instance as a parameter](images/121770213899_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces under: [Introduction to namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

#### Examples of the use of parameter instances

This section contains information on the following topics:

- [Example of using parameter instances in an ARRAY of multi-instances](#example-of-using-parameter-instances-in-an-array-of-multi-instances)
- [Example of using parameter instances in an ARRAY of DB_ANY (S7-1200, S7-1500)](#example-of-using-parameter-instances-in-an-array-of-db_any-s7-1200-s7-1500)

##### Example of using parameter instances in an ARRAY of multi-instances

###### Task

The use of parameter instances allows you to transfer the instance of a function block to another block (FB or FC) for further processing, for example, a data query or an error analysis, or even have the function block executed with the passed instance.

The ARRAY multi-instances can be used to combine objects of the same type and process their instances indexed in a program loop. Indexed ARRAY elements can also be passed to another block as a parameter instance.

To illustrate this, the object "Valve" (FB_Valve) was selected in the following example. On this basis, you are provided with all required information on valve processing in a program block, "FB_ValveControl" in this case.

The figure below illustrates the features needed and how they can be used:

![Task](images/86190803467_DV_resource.Stream@PNG-en-US.png)

- The two functions "FC_StatusValve" and "FC_MaintainValve" process a parameter instance of the "FB_Valve" program block which they received in the call.
- In the "FB_ValveControl" program block, you use the ARRAY multi-instances on the one hand to declare the number of existing valves and, on the other hand, to manage all of the valves in a loop by means of various functions.

> **Note**
>
> **Completeness**
>
> This solution is only an example to illustrate how this task can be approached. Keep in mind that you need to adjust the program code to your actual task.

The following program blocks are required to implement this example:

| Block | Description | Programming language |
| --- | --- | --- |
| FB_ValveControl | This function block is used as a control block, where you can process all the valves using an ARRAY of multi-instances. | SCL |
| FB_Valve | This function block contains the definition of the valve data and the program code for processing a valve. | SCL  (The three program blocks are used by the "FB_ValveControl" program block.) |
| FC_StatusValve | The function returns the status of the currently processed valve. |  |
| FC_MaintainValve | This function checks if maintenance is required on the valve. If required, the maintenance is performed and the function value TRUE is returned when everything is completed. |  |

###### Procedure: Create "FB_Valve"

To create the SCL function block, follow these steps:

1. Double-click the "Add new block" command.

   The "Add new block" dialog opens.
2. Click on the "Function block (FB)" button.
3. Enter the name "FB_Valve".
4. Select "SCL" as the language.
5. Click "OK".
6. The declaration of the block interface is based on a valve which can open and close, and could look like this, for example:

   ![Procedure: Create "FB_Valve"](images/85963656075_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FB_Valve"](images/85963656075_DV_resource.Stream@PNG-de-DE.png)
7. The program code for controlling the valves could look like this, for example:

   ![Procedure: Create "FB_Valve"](images/85405584779_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FB_Valve"](images/85405584779_DV_resource.Stream@PNG-de-DE.png)

###### Procedure: Create "FC_StatusValve"

To create the SCL function "FC_StatusValve", follow these steps:

1. Double-click on the "Add new block" command.

   The "Add new block" dialog opens.
2. Click on the "Function (FC)" button.
3. Enter the name "FC_StatusValve".
4. Select "SCL" as the language.
5. Click "OK".
6. The declaration of the block interface with integration of the parameter instance "FB_Valve" could look like this, for example:

   ![Procedure: Create "FC_StatusValve"](images/85963663755_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FC_StatusValve"](images/85963663755_DV_resource.Stream@PNG-de-DE.png)
7. Write the following program code, for example:

   ![Procedure: Create "FC_StatusValve"](images/85407049867_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FC_StatusValve"](images/85407049867_DV_resource.Stream@PNG-de-DE.png)

###### Procedure: Create "FC_MaintainValve"

To create the SCL function "FC_MaintainValve", follow these steps:

1. Double-click on the "Add new block" command.

   The "Add new block" dialog opens.
2. Click on the "Function (FC)" button.
3. Enter the name "FC_MaintainValve".
4. Select "SCL" as the language.
5. Click "OK".
6. The declaration of the block interface with integration of the parameter instance "FB_Valve" could look like this, for example:

   ![Procedure: Create "FC_MaintainValve"](images/85965361035_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FC_MaintainValve"](images/85965361035_DV_resource.Stream@PNG-de-DE.png)
7. Write the following program code, for example:

   ![Procedure: Create "FC_MaintainValve"](images/85409397131_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FC_MaintainValve"](images/85409397131_DV_resource.Stream@PNG-de-DE.png)

###### Procedure: Create "FB_ValveControl"

To create the SCL function block, follow these steps:

1. Double-click the "Add new block" command.

   The "Add new block" dialog opens.
2. Click on the "Function block (FB)" button.
3. Enter the name "FB_ValveControl".
4. Select "SCL" as the language.
5. Click "OK".
6. Define the user constant:

   ![Procedure: Create "FB_ValveControl"](images/85965983371_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FB_ValveControl"](images/85965983371_DV_resource.Stream@PNG-de-DE.png)

   The user constant "vmax" is used in this example in order to easily adapt the program to a different number of valves.
7. The declaration of the block interface with integration of the valve instances from "FB_Valve" could look like this, for example:

   ![Procedure: Create "FB_ValveControl"](images/85965991051_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FB_ValveControl"](images/85965991051_DV_resource.Stream@PNG-de-DE.png)
8. Write the following program code, for example:

   ![Procedure: Create "FB_ValveControl"](images/85414112651_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Create "FB_ValveControl"](images/85414112651_DV_resource.Stream@PNG-de-DE.png)

###### Procedure: Call of "FB_ValveControl" in OB 1

To call the "FB_ValveControl" function block in OB 1, follow these steps:

1. Open the "Main [OB1]" block with a double-click.
2. Use a drag-and-drop operation to add the "FB_ValveControl" function block to OB1.

   ![Procedure: Call of "FB_ValveControl" in OB 1](images/85417637515_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure: Call of "FB_ValveControl" in OB 1](images/85417637515_DV_resource.Stream@PNG-de-DE.png)

###### Result

One valve is processed in each program cycle. The respective valve selected by index is processed, its status queried and maintenance is performed, if needed.

In this example, one valve per cycle has been processed. Of course, it is also possible to process all valves in one program loop, but then the cycle time increases accordingly. If you need a short program cycle, we recommend that you avoid working with a program loop.​

---

**See also**

[Parameter instances](#parameter-instances)
  
[Multi-instances](#multi-instances)

##### Example of using parameter instances in an ARRAY of DB_ANY (S7-1200, S7-1500)

###### Task

The following example shows you how to address multiple instances of a function block using a variable index. The instances are to be processed iteratively in a FOR loop.

![Task](images/121008726283_DV_resource.Stream@PNG-de-DE.png)

###### Creating the example program

1. First, create the function block "MyFB" and set the memory reserve to "0 bytes" in the block properties.
2. Generate five instance data blocks for "MyFB".

   ![Creating the example program](images/119270235531_DV_resource.Stream@PNG-de-DE.png)

   ![Creating the example program](images/119270235531_DV_resource.Stream@PNG-de-DE.png)
3. Generate the global data block "DBAnyStorage" and set the memory reserve to "0 bytes" in the properties of the data block.
4. In "DBAnyStorage" , declare an ARRAY of data type "DB_ANY" with five components.

   ![Creating the example program](images/119947574539_DV_resource.Stream@PNG-de-DE.png)

   ![Creating the example program](images/119947574539_DV_resource.Stream@PNG-de-DE.png)
5. For initialization, you assign the symbolic names of the five instance DBs to the individual ARRAY elements in the startup OB.

   ![Creating the example program](images/119266622347_DV_resource.Stream@PNG-de-DE.png)

   ![Creating the example program](images/119266622347_DV_resource.Stream@PNG-de-DE.png)
6. Create the function block "LoopCallDoMyFB" and access individual instances of "MyFB" there iteratively using a FOR loop.

   The instances are transferred to the function "DoMyFB" for execution one after the other.

   The transferred instance is determined during runtime. This means that, at the time of program creation, it cannot be determined whether the instance to be transferred actually matches the parameter declared in the interface of "DoMyFB" . To check this, we recommend using the instruction "TypeOfDB" in the function block "LoopCallDoMyFB".

   ![Creating the example program](images/121009495819_DV_resource.Stream@PNG-de-DE.png)

   ![Creating the example program](images/121009495819_DV_resource.Stream@PNG-de-DE.png)
7. The in/out parameter "currentMyFBInstance" is declared in the interface of "DoMyFB". There, "LoopCallDoMyFB" transfers the instance of "MyFB" to be processed to the function "DoMyFB" during runtime. (Transfer as parameter instance).

   ![Creating the example program](images/119270137739_DV_resource.Stream@PNG-de-DE.png)

   ![Creating the example program](images/119270137739_DV_resource.Stream@PNG-de-DE.png)

###### Result

All instances of "MyFB" are edited in succession by the FB "DoMyFB".

---

**See also**

[Parameter instances](#parameter-instances)

### Parameter transfer at block call

This section contains information on the following topics:

- [Rules for supplying block parameters](#rules-for-supplying-block-parameters)
- [Parameter assignment to functions](#parameter-assignment-to-functions)
- [Parameter assignment to function blocks](#parameter-assignment-to-function-blocks)
- [Transfer parameter as copy or as pointer](#transfer-parameter-as-copy-or-as-pointer)
- [Forwarding of block parameters](#forwarding-of-block-parameters)

#### Rules for supplying block parameters

##### Block parameters

The calling block gives the called block the values with which it is to work. These values are referred to as block parameters. The input parameters provide the called block with the values that it has to process. The block returns the results via the output parameters.

Block parameters therefore form the interface between the calling and the called block.

You use input parameters when you want to only query or read values, and output parameters when you want to set or write these values. If block parameters are read and written you have to create these as in-out parameters.

The following rules apply to the use of block parameters within the block:

- Input parameters may only be read.
- Output parameters may only be written.
- In/out parameters may be read and written.

##### Formal and actual parameters

The block parameters are defined in the interface of the called block. These parameters are referred to as formal parameters. They are placeholders for the parameters that are transferred to the block when it is called. The parameters transferred to the block when it is called are referred to as actual parameters.

The data types of actual and formal parameters must be identical or convertible according to the rules of data type conversion.

> **Note**
>
> **S7-1200/1500: Transferring peripheral inputs or outputs as block parameters**
>
> If you supply an input parameter with a peripheral input or output, it is possible that I/O access errors will occur during runtime when the block is called, e.g. a read error when an input module is accessed directly.
>
> The system response of S7-1500 series CPUs with firmware version V2.1 or higher is as follows:
>
> The block is called and processed with the substitute value of the signal.
>
> The system response of S7-1200 and S7-1500 series CPUs with firmware versions lower than V2.1 is as follows:
>
> The block is not called as a result of the I/O access error. Program execution is continued after the block call. If OB 122 exists or local error handling is enabled, these are executed.
>
> To prevent the situation that the block is not called as a result of an I/O access error, first copy the peripheral input or output to a local tag (Temp) and transfer it as a block parameter to the called block.
>
> The FAQ below provide additional information on this topic:
>
> [FAQ 89377245: Why are blocks in the S7-1200/S7-1500 not processed when they are addressed with unavailable PROFINET components?](https://support.industry.siemens.com/cs/ww/en/view/89377245)

---

**See also**

[Using tags within the program](#using-tags-within-the-program)
  
[Parameter assignment to function blocks](#parameter-assignment-to-function-blocks)
  
[Parameter assignment to functions](#parameter-assignment-to-functions)
  
[Rules for declaring the block interface](Declaring%20the%20block%20interface.md#rules-for-declaring-the-block-interface)
  
[PLC data types (UDT)](Data%20types.md#plc-data-types-udt)
  
[STL Basics (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#stl-basics-s7-300-s7-400-s7-1500)
  
[Fully qualified addresses in STL (S7-1500)](Migrating%20PLC%20programs%20to%20a%20S7-1500%20CPU%20-%20ET%20200SP.md#fully-qualified-addresses-in-stl-s7-1500)
  
[Partially qualified addresses in STL (S7-1500)](Migrating%20PLC%20programs%20to%20a%20S7-1500%20CPU%20-%20ET%20200SP.md#partially-qualified-addresses-in-stl-s7-1500)

#### Parameter assignment to functions

##### Parameters of functions (FC)

Functions have no data memory in which values of block parameters can be stored. Therefore, when a function is called, all formal parameters must be assigned actual parameters.

##### Input parameters (Input)

Input parameters are only read once before each block call. Therefore, the rule is that writing an input parameter within the block does not affect the actual parameter. Only the formal parameter is written.

##### Output parameters (Output)

Output parameters are only read once after each block call. Therefore, the rule is that output parameters should not be read within the block. If you nevertheless read an output parameter, please note that only the value of the formal parameter is read. The value of the actual parameter cannot be read within the block.

If an output parameter of a function is not written in this function, the value that is predefined for the specified data type is used. For example, the value "false" is predefined for BOOL. However, structured output parameters are not pre-assigned with a value.

To prevent unintentional further processing of the predefined value or an undefined value, note the following when programming the block:

- Make sure that the output parameters are written with values for all possible program paths within the block. In doing so, note that jump commands may skip instruction sequences in which outputs are set, for example.
- Note that the set and reset commands are dependent on the result of the logic operation. If the value of an output parameter is determined with these commands and RLO = 0, a value will not be generated.
- If possible, assign a default value for the output parameters of functions.

##### In/out parameters (InOut)

In/out parameters are read before the block call and written after the block call. If you read or write the parameter within the block, you only access its formal parameter.

An exception is in/out parameters with a structured data type. Structured data types consist of several data elements, for example ARRAY or STRUCT. These are transferred to the called block by a pointer. You therefore always access the actual parameter when you read or write a structured in/out parameter within a block.

When an in/out parameter of a function is not written to this function, the old output value or the input value is used as a value. Nevertheless, you should observe the information provided above for output parameters so that old values are not inadvertently processed further.

##### Temporary local data (Temp)

Temporary local data is only available during block processing. It is treated differently depending on the optimization setting of the block:

- Standard access

  The following rule applies to code blocks with standard access as well as to all tags with retentivity setting "Set in IDB":

  If you are using temporary local data, you must ensure that the values are initialized prior to use. Otherwise, the values will be random. Temporary data of the STRING of WSTRING data type is an exception: It is automatically pre-assigned the actual length 0.
- Optimized access

  The following rules apply to code blocks with optimized access:

  - If a temporary tag is not written within a function, the value that is predefined for the specified data type is used.

    The following table shows some examples of pre-defined values:

    | Data type | Pre-defined value |
    | --- | --- |
    | Bool | False |
    | Int | 0 |
    | REAL | 0.0 |
    | Char | ' ' |
    | Wchar | WCHAR#' ' |
    | DTL | DTL#1970-01-01-00:00:00 |
    | DATE_AND_TIME | DT#1990-01-01-00:00:00 |
    | Date | D#1990-01-01 |
  - Elements of the PLC data types are pre-assigned with the default value that is specified in the declaration of the PLC data type (UDT).
  - STRINGs and WSTRINGs are pre-assigned with the actual value "0", even if they are used within a PLC data type.
  - Elements of the data type ARRAY are pre-assigned with the value "0", even if they are used within a PLC data type.

##### Function value (Return)

Functions normally calculate a function value. This function value can be returned to the calling block via the RET_VAL output parameter. For this, the RET_VAL output parameter must be declared in the interface of the function. RET_VAL is always the first output parameter of a function. All data types are permitted for the RET_VAL parameter except ARRAY and STRUCT, as well as parameter types TIMER and COUNTER.

In the SCL programming language functions can be call directly in an expression. The result of the expression is then formed with the calculated function value. Therefore, the data type ANY is not permitted in SCL for the function value.

---

**See also**

[Parameter assignment to function blocks](#parameter-assignment-to-function-blocks)
  
[Rules for supplying block parameters](#rules-for-supplying-block-parameters)
  
[Calling functions](Creating%20SCL%20programs.md#calling-functions)
  
[Examples for calling functions in SCL](Creating%20SCL%20programs.md#examples-for-calling-functions-in-scl)

#### Parameter assignment to function blocks

##### Supplying parameters of function blocks (FB)

In the case of function blocks the parameter values will be stored in the instance data.

If the input, output, or in-out parameters of a function block were not assigned with current values, the stored values are used when the parameter has already been initialized once in a previous cycle. If this is not the case, the CPU goes to STOP with a runtime error.

In some cases, it is mandatory to specify an actual parameter.

The following table shows which parameters of a function block must be assigned actual parameters:

| Parameter | Elementary data type | Structured data type | Parameter type |
| --- | --- | --- | --- |
| Input (Input) | Optional | Optional | Optional |
| Output (Output) | Optional | Optional | Not permitted |
| In-out (InOut) | Optional | - Call of non-optimized block: not absolutely necessary, but the value must be initialized once by a call, otherwise a runtime error is output. - Call of optimized blocks: required | Not permitted |

---

**See also**

[Rules for supplying block parameters](#rules-for-supplying-block-parameters)
  
[Parameter assignment to functions](#parameter-assignment-to-functions)
  
[Parameter types](Data%20types.md#parameter-types)

#### Transfer parameter as copy or as pointer

##### Introduction

When a block is called, you transfer data to the parameters in the block interface. At the input parameters, you transfer the data with which the block is to work. At the output parameters, you specify where the results of the processing are saved. In/out parameters are used to transfer data to the called block as well as to return results.

Internally, STEP 7 recognizes two different methods of parameter transfer: The data is transferred either as pointer or as copy, depending on the transfer range and data type of the parameter.

##### Transfer as copy (Call by value)

During a block call, the value of the operand is copied to the input parameter of the called block. With function blocks, the copy is stored in the instance DB; with functions, it is stored in the block stack. Additional storage space is required for the copy.

This means that the called block always works with the value that the specified operand had at the time of the block call. It cannot access the operand directly. Write access modifies only the copy, but not the actual value of the specified operand. Read access reads only the copy that was created at the time of the block call.

![Transfer as copy (Call by value)](images/71509682955_DV_resource.Stream@PNG-en-US.png)

##### Transfer as pointer (Call by reference)

The parameters are referenced via a pointer during the block call.

This means that the called block can directly access the memory address of the operand that is specified as parameter: Write access directly results in the changing of the specified operand. Read access reads the value of the operand directly at the time of access. As no copy is created, no additional memory is required.

![Transfer as pointer (Call by reference)](images/71510797323_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Declare structured data types in the "InOut" area**
>
> If possible, use the "InOut" area in the block interface for structured tags. Because structured in/out parameters by default are transferred as pointers, the required data memory is not increased unnecessarily.
>
> Structured data types are data types that consist of several elements, for example ARRAY, STRUCT, (W)STRING, Date_And_Time, PLC data types (UDT), system data types (e.g. IEC_Timer or IEC_Counter) and ErrorStruct.

##### Parameter transfer with S7-1200/1500

The following table shows how block parameters with elementary or structured data type are transferred in S7-1200/1500. Elementary data types are, for example, BOOL, INT or BYTE. Structured data types are, for example, ARRAY, STRUCT or STRING.

It also shows how to handle parameter instances and technology objects. A parameter instance is a block call with which the instance of the block being called is transferred as an in-out parameter to the calling block. Technology objects are, for example, objects for controlling axes, PID controllers or high-speed counters.

|  |  | Elementary data types | Structured data types | Parameter instances | Technology objects |
| --- | --- | --- | --- | --- | --- |
| ![Parameter transfer with S7-1200/1500](images/71519938187_DV_resource.Stream@PNG-de-DE.png) | **Input** | Copy | Pointer | Pointer | Pointer |
| **Output** | Copy | Pointer | Pointer | Pointer |  |
| **InOut** | Copy | Pointer | Pointer | Pointer |  |
| ![Parameter transfer with S7-1200/1500](images/71510913931_DV_resource.Stream@PNG-de-DE.png) | **Input** | Copy | Copy | Not possible | Pointer |
| **Output** | Copy | Copy | Not possible | Pointer |  |
| **InOut** | Copy | Pointer | Pointer | Pointer |  |

> **Note**
>
> **Data transfer between memory areas with optimized access and memory areas with standard access**
>
> If structures are transferred to a block as in/out parameters, they are transferred by default as pointers (Call by reference).
>
> However, this does not apply if the memory area of the transferred actual parameter and the called block have different optimization settings: If the actual parameter has the property "Optimized access", for example, and the block has the property "Standard access", the parameter is always transferred as copy (Call by value).
>
> If the called block contains numerous structured parameters, this can quickly lead to the temporary memory area (local data stack) overflowing.
>
> Problems can also occur if the transferred actual parameters are changed by asynchronous processes, such as by HMI access or interrupt OBs. If the values are copied back again to the operands originally transferred as actual parameters after the block processing, the changes made asynchronously to these operands are overwritten.
>
> You can avoid this by setting the same access type for the memory area of the actual parameter and for the called block or by having the asynchronous access written first to a separate memory area and then copying this area synchronously at a suitable time.
>
> See also:
>
> [Blocks with optimized access](#blocks-with-optimized-access)
>
> [FAQ 109478253: How can it happen that data of the HMI system or of the Web server is overwritten in the S7-1500?](https://support.industry.siemens.com/cs/de/en/view/109478253)

##### Parameter transfer with S7-300/400

The following table shows how block parameters with elementary or structured data type are transferred in S7-300/400.

|  |  | Elementary data types | Structured data types |
| --- | --- | --- | --- |
| ![Parameter transfer with S7-300/400](images/71519938187_DV_resource.Stream@PNG-de-DE.png) | **Input** | Copy* | Pointer |
| **Output** | Copy* | Pointer |  |
| **InOut** | Copy* | Pointer |  |
| ![Parameter transfer with S7-300/400](images/71510913931_DV_resource.Stream@PNG-de-DE.png) | **Input** | Copy | Copy |
| **Output** | Copy | Copy |  |
| **InOut** | Copy | Pointer |  |

* Exception: Operands from the memory areas I, Q, M, P, L and partly qualified DB addresses (for example, "DW 2") are transferred as pointer.

> **Note**
>
> **Special aspects of transfer as pointer in S7-300/400**
>
> In cases in which the parameters are transferred via a pointer, it is not possible to forward output parameters or in/out parameters from the calling block to the input parameters of the called block.

#### Forwarding of block parameters

This section contains information on the following topics:

- [Basic information on forwarding block parameters](#basic-information-on-forwarding-block-parameters)
- [Calling a function by another function](#calling-a-function-by-another-function)
- [Call of a function by a function block](#call-of-a-function-by-a-function-block)
- [Call of a function block by a function](#call-of-a-function-block-by-a-function)
- [Call of a function block by another function block](#call-of-a-function-block-by-another-function-block)

##### Basic information on forwarding block parameters

###### Definition

The "Forwarding" of block parameters is a special type of parameter use. In this case the block parameters of the calling block are forwarded to the parameters of the called block. The called block uses the values that are currently present at the block parameters of the calling block as the actual parameters.

The following figure shows how the parameters of the function FC 10 are forwarded to the function FC 12:

![Definition](images/108654797195_DV_resource.Stream@PNG-en-US.png)

###### Rules for LAD/FBD

The following general rules apply in LAD and FBD:

- Input parameters can only be forwarded to input parameters.
- Output parameters can only be forwarded to output parameters.
- In/out parameters can be forwarded to all parameter types.
- In S7-300/400, the two block parameters must have the same data type.
- In S7-1200/1500, the parameters can also be converted according to the rules of implicit conversion.

###### Rules for STL

The following general rules apply in STL:

- Input parameters can only be forwarded to input parameters.
- Output parameters can only be forwarded to output parameters.
- In/out parameters can be forwarded to all parameter types.
- Both block parameters must have the same data type. In STL, this rule applies to all CPU families.

###### Rules for SCL

The rules for SCL are less stringent. So that programs from previous SCL versions can be taken over more easily, additional parameter transfer options are permissible. You can, for example, forward a structured in/out parameter to an input parameter. However, in this case you must ensure that the actual parameter is not located in the temporary local data or in a global data block.

Additional rules are described in detail in the following chapters.

---

**See also**

[Calling a function by another function](#calling-a-function-by-another-function)
  
[Call of a function by a function block](#call-of-a-function-by-a-function-block)
  
[Call of a function block by a function](#call-of-a-function-block-by-a-function)
  
[Call of a function block by another function block](#call-of-a-function-block-by-another-function-block)

##### Calling a function by another function

###### Permissible data types for the call of a function by another function

Specific rules apply to the forwarding of formal parameters. The following table shows the rules according to which parameters can be forwarded in the various CPU families:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **FC calls FC** |  | **Data types** |  |  |  |  |  |  |
| **Actual parameter**     **(calling block)** | **Formal parameter**    **(called block)** | **Standard data types** | **ARRAY, STRUCT, STRING, WSTRING, DT** | **ANY, POINTER** | **VARIANT** | **Parameter types**     **(TIMER, COUNTER, BLOCK_XX)** | **DB_Any** | **REF_TO** |
| **Input** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200 as of V2  S7-1500 | S7-1500 |
| **Output** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - | - |
| **InOut** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - | S7-1500 |
| **InOut** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - | - |
| **InOut** | **InOut** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - | - |

---

**See also**

[Basic information on forwarding block parameters](#basic-information-on-forwarding-block-parameters)

##### Call of a function by a function block

###### Permissible data types for the call of a function by a function block

Specific rules apply to the forwarding of formal parameters. The following table shows the rules according to which parameters can be forwarded in the various CPU families:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **FB calls FC** |  | **Data types** |  |  |  |  |  |  |
| **Actual parameter**     **(calling block)** | **Formal parameter**    **(called block)** | **Standard data types** | **ARRAY, STRUCT, STRING, WSTRING, DT** | **ANY, POINTER** | **VARIANT** | **Parameter types**     **(TIMER, COUNTER, BLOCK_XX)** | **DB_Any** | **REF_TO** |
| **Input** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-300/400  S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200 as of V2  S7-1500 | S7-1500 |
| **Output** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-300/400  S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - | - |
| **InOut** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - | S7-1500 |
| **InOut** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - | - |
| **InOut** | **InOut** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - | - |

---

**See also**

[Basic information on forwarding block parameters](#basic-information-on-forwarding-block-parameters)

##### Call of a function block by a function

###### Permissible data types for the call of a function block by a function

Specific rules apply to the forwarding of formal parameters. The following table shows the rules according to which parameters can be forwarded in the various CPU families:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **FC calls FB** |  | **Data types** |  |  |  |  |  |
| **Actual parameter**     **(calling block)** | **Formal parameters**    **(called block)** | **Standard data types** | **ARRAY, STRUCT, STRING, WSTRING, DT** | **ANY, POINTER** | **VARIANT** | **Parameter types**     **(TIMER, COUNTER, BLOCK_XX)** | **DB_Any** |
| **Input** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | S7-300/400  S7-1500 | S7-1200 as of V2  S7-1500 |
| **Output** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - |
| **InOut** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - |
| **InOut** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - |
| **InOut** | **InOut** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - |

---

**See also**

[Basic information on forwarding block parameters](#basic-information-on-forwarding-block-parameters)

##### Call of a function block by another function block

###### Permissible data types for the call of a function block by another function block

Specific rules apply to the forwarding of formal parameters. The following table shows the rules according to which parameters can be forwarded in the various CPU families:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **FB calls FB** |  | **Data types** |  |  |  |  |  |
| **Actual parameter**    **(calling block)** | **Formal parameters**    **(called block)** | **Standard data types** | **ARRAY, STRUCT, STRING, WSTRING, DT** | **ANY, POINTER** | **VARIANT** | **Parameter types**     **(TIMER, COUNTER, BLOCK_XX)** | **DB_Any** |
| **Input** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-300/400  S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | S7-300/400  S7-1500 | S7-1200 as of V2  S7-1500 |
| **Output** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-300/400  S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - |
| **InOut** | **Input** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - |
| **InOut** | **Output** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | - | S7-1200  S7-1500 | - | - |
| **InOut** | **InOut** | S7-300/400  S7-1200  S7-1500 | S7-1200  S7-1500 | S7-1500 | S7-1200  S7-1500 | - | - |

---

**See also**

[Basic information on forwarding block parameters](#basic-information-on-forwarding-block-parameters)

## Using and addressing operands

This section contains information on the following topics:

- [Basic information about operands](#basic-information-about-operands)
- [Keywords and reserved identifiers](#keywords-and-reserved-identifiers)
- [Using tags within the program](#using-tags-within-the-program)
- [Constants](#constants)
- [Addressing operands](#addressing-operands)

### Basic information about operands

#### Introduction

When you program instructions you must specify which data values the instruction should process. These values are referred to as operands. You can, for example, use the following elements as operands:

- PLC tags
- Constants
- Tags in instance data blocks
- Tags in global data blocks

#### Absolute address and symbolic name

Operands are identified by means of an absolute address and a symbolic name. You define the names and addresses in the PLC tag table or in the tag declaration of the blocks.

> **Note**
>
> **You can find more information on permissible characters in operand names in the following entry in the Siemens Industry Online Support:**
>
> When should identifiers and operands be used in "quotation marks" in STEP 7 (TIA Portal)?
>
> ![Absolute address and symbolic name](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/109477857](https://support.industry.siemens.com/cs/ww/en/view/109477857)
>
> **You can find recommendations for uniform, project-wide tag naming in the programming style guide:**
>
> ![Absolute address and symbolic name](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/81318674](https://support.industry.siemens.com/cs/ww/en/view/81318674)

> **Note**
>
> **Calling and addressing operands in namespaces**
>
> Operands located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The name of the operand is not in quotation marks.
> - The namespace precedes the operand name, separated by a dot.
>
> You can find detailed information on the notation of namespaces at: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

#### Data blocks with optimized access (S7-1200, S7-1500)

Data elements in data blocks with optimized access only receive a symbolic name and no absolute address in the declaration.

---

**See also**

[Displaying symbolic and absolute addresses](Program%20editor.md#displaying-symbolic-and-absolute-addresses)
  
[Basics of block access](#basics-of-block-access)

### Keywords and reserved identifiers

SIMATIC recognizes a range of reserved identifiers that have a specific meaning in the program. Do not use these identifiers as names for program elements, tags or constants.

The following identifiers are reserved:

- Keywords (e.g. "ALTERNATIVE_BRANCH")
- IEC functions (e.g. "ABS")
- Operators (e.g. "SHL")
- Address identifiers (e.g. "A0.0")
- Data types (e.g. "Int")

#### Overview of keywords and reserved identifiers

The following table provides an overview of the keywords and reserved identifiers:

| Alphabetical order | Keywords |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **$** | $ASM |  |  |  |  |
| **A** | A | A0 | A1 | AB | ABS |
| ABSTRACT | ACOS | ACTION | AD | ADD |  |
| ALTERNATIVE_BRANCH | AND | Any_Array | Any_BCD | Any_Bit |  |
| Any_Block | Any_Char | Any_Chars | Any_CodeBlock | Any_DataBlock |  |
| Any_Date | Any_Duration | Any_Elementary | Any_Int | Any_Magnitude |  |
| Any_Num | Any_Ordered | Any_Pointer | Any_Real | Any_Reference |  |
| Any_Signed | Any_String | Any_Struct | Any_StructuredType | Any_TypeBlock |  |
| Any_TypedReference | Any_UnOrdered | Any_UnSigned | Any_UnTypedReference | AR1 |  |
| AR2 | ASIN | AT | ATAN | AUTHOR |  |
| AW |  |  |  |  |  |
| **B** | B | BEGIN | BIE | BR | BROWSERINFO |
| BR | BY |  |  |  |  |
| **C** | C | CALL | CASE | CAUSE | CAUSE_GROUP |
| CC0 | CC1 | CEIL | CLASS | CODE_VERSION1 |  |
| COMM_BLOCK | CONCAT | CONFIGURATION | CONST | CONSTANT |  |
| CONTINUE | COS |  |  |  |  |
| **D** | D | DATA_BLOCK | DATATYPE | DB | DB_SPECIFIC |
| DBB | DBD | DBLG | DBNO | DBW |  |
| DBX | DCHAR | DELETE | DI | DIB |  |
| DID | DILG | DINO | DIV | DIW |  |
| DIX | DO | DT |  |  |  |
| **E** | E | EB | ED | EFFECT | EFFECT_GROUP |
| ELEMENT | ELSE | ELSIF | EN | END_POST_OPERATION |  |
| END_PRE_OPERATION | END_ACTION | END_ALTERNATIVE_BRANCH | END_BROWSERINFO | END_CASE |  |
| END_CAUSE | END_CAUSE_GROUP | END_CLASS | END_CONFIGURATION | END_CONST |  |
| END_DATA_BLOCK | END_EFFECT | END_EFFECT_GROUP | END_ELEMENT | END_FOR |  |
| END_FOREACH | END_FUNCTION | END_FUNCTION_BLOCK | END_IF | END_INTERFACE |  |
| END_INTERLOCK | END_INTERSECTIONS | END_LIBRARY | END_NAMESPACE | END_NETWORK |  |
| END_NAMESPACE | END_NETWORK | END_NODE | END_ORGANIZATION_BLOCK | END_PROGRAM |  |
| END_REGION | END_REPEAT | END_REQUIRE | END_RESOURCE | END_RUNG |  |
| END_SELECTION | END_SEQUENCE | END_SIMULTANEOUS_BRANCH | END_STEP | END_STRUCT |  |
| END_SUPERVISION | END_SYSTEM_FUNCTION | END_SYSTEM_FUNCTION_BLOCK | END_TRANSITION | END_TYPE |  |
| END_VAR | END_WHILE | END_WIRE | ENO | ENTRY |  |
| EQ | EW | EXIT | EXPT | EXTENDS |  |
| **F** | F_EDGE | FALSE | FAMILY | FB | FC |
| FINAL | FIND | FLOOR | FOR | FOREACH |  |
| FUNCTION | FUNCTION_BLOCK |  |  |  |  |
| **G** | GE | GOTO | GT |  |  |
| **I** | I | IB | ID | IF | IMPLEMENTATION |
| IMPLEMENTS | INSERT | INSIDE | INTERFACE | INTERLOCK |  |
| INTERNAL | INTERSECTIONS | INTERVAL | IW |  |  |
| **K** | KNOW_HOW_PROTECT |  |  |  |  |
| **L** | L | LABEL | LB | LD | LDATE |
| LE | LDATE_AND_TIME | LEFT | LEN | LIBRARY |  |
| LIMIT | LN | LOG | LOWER_BOUND | LT |  |
| LTIME_OF_DAY | LW |  |  |  |  |
| **M** | M | MAX | MB | MD | MDD_CHECK |
| METHOD | MID | MIN | MOD | MOVE |  |
| MUL | MUX | MW |  |  |  |
| **N** | NAME | NAME_OF | NAMESPACE | NE | NETWORK |
| NODE | NON_RETAIN | NOP | NOT | NU |  |
| NULL |  |  |  |  |  |
| **O** | OB | OF | ON | OR | ORGANIZATION_BLOCK |
| OS | OV | OVERLAP | OVERRIDE |  |  |
| **P** | P | PA | PAB | PACKED | PAD |
| PAW | PB | PE | PD | PEB |  |
| PED | PEW | PI | PIB | PID |  |
| PIW | POST_OPERATION | PQ | PQB | PQD |  |
| PQW | PRAGMA_BEGIN | PRAGMA_END | PRE_OPERATION | PRIORITY |  |
| PRIVATE | PROGRAM | PROTECTED | PUBLIC | PW |  |
| **Q** | Q | QB | QD | QW |  |
| **R** | R_EDGE | READ_ONLY | READ_WRITE | REF | REF_TO |
| REGION | RELATION | REPEAT | REPLACE | REQUIRE |  |
| RESOURCE | RET_VAL | RETAIN | RETURN | RIGHT |  |
| ROL | ROR | RUNG |  |  |  |
| **S** | S5T | SDB | SEL | SELECTION | SEQUENCE |
| SFB | SFC | SHL | SHR | SIMULTANEOUS_BRANCH |  |
| SIN | SINGLE | SQRT | STANDARD | STEP |  |
| STW | SUB | SUBSET | SUPER | SUPERVISION |  |
| SYSTEM_FUNCTION | SYSTEM_FUNCTION_BLOCK |  |  |  |  |
| **T** | T | TAN | TASK | THEN | THIS |
| TITLE | TO | TO_BOOL | TO_BYTE | TO_CHAR |  |
| TO_DATE | TO_DINT | TO_DT | TO_DWORD | TO_INT |  |
| TO_LDATE | TO_LDT | TO_LINT | TO_LREAL | TO_LTIME |  |
| TO_LTOD | TO_LWORD | TO_REAL | TO_SINT | TO_TIME |  |
| TO_TOD | TO_UDINT | TO_UINT | TO_ULINT | TO_USINT |  |
| TO_WCHAR | TO_WORD | TOD | TRANSITION | TRUE |  |
| TRUNC | TYPE |  |  |  |  |
| **U** | UDT | UNLINKED | UNTIL | UO | UPPER_BOUND |
| USING | USTRING |  |  |  |  |
| **V** | VAR | VAR_ACCESS | VAR_CONFIG | VAR_EXTERNAL | VAR_GLOBAL |
| VAR_IN_OUT | VAR_INPUT | VAR_OUTPUT | VAR_TEMP | VERSION |  |
| **W** | W | WHILE | WIRE | WITH |  |
| **X** | XOR |  |  |  |  |
| **Z** | Z |  |  |  |  |

#### Overview of reserved address identifiers

The following table provides an overview of the reserved identifiers for addresses. The addresses given serve as examples. For example, not only is the identifier "A0.0" reserved but also the identifier of all other possible addresses ("A0.1", "A0.2", etc.).

| Alphabetical order | Identifiers for operands |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **A** | A0.0 | AB0 | AD0 | AW0 |  |
| **C** | C0 |  |  |  |  |
| **D** | DB1 | DBB0 | DBD0 | DBW0 | DBX0.0 |
| DI0 | DIB0 | DID0 | DIW0 | DIX0.0 |  |
| **E** | E0.0 | EB0 | ED0 | EW0 |  |
| **F** | FB1 | FC1 |  |  |  |
| **I** | I0.0 | IB0 | ID0 | IW0 |  |
| **L** | L0.0 | LB0 | LD0 | LW0 |  |
| **M** | M0.0 | MB0 | MD0 | MW0 |  |
| **O** | OB1 |  |  |  |  |
| **P** | P0.0 | PAB0 | PAD0 | PAW0 | PAX0.0 |
| PB0 | PD0 | PEB0 | PED0 | PEW0 |  |
| PEX0.0 | PIB0 | PID0 | PIW0 | PIX0.0 |  |
| PQB0 | PQD0 | PQW0 | PQX0.0 | PW0 |  |
| **Q** | Q0.0 | QB0 | QD0 | QW0 |  |
| **S** | SDB1 | SFB1 | SFC1 |  |  |
| **T** | T0 |  |  |  |  |
| **U** | UDT1 |  |  |  |  |
| **Z** | Z0 |  |  |  |  |

#### Overview of data types

An overview of data types can be found here: [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

### Using tags within the program

#### Definition

A variable is a placeholder for a data value that can be changed in the program. The format of the data value is defined. The use of variables makes your program more flexible. For example, you can assign different values to variables that you have declared in the block interface for each block call. As a result, you can reuse a block you have already programmed for various purposes.

A variable consists of the following elements:

- Name
- Data type
- Absolute address

  - PLC tags and DB variables in blocks with standard access have an absolute address.
  - DB variables in blocks with optimized access have no absolute address.
- Value (optional)

#### Declaring Variables

You can define variables with different scopes for your program:

- PLC tags that apply in all areas of the CPU
- DB variables in global data block that can be used by all blocks throughout the CPU.
- DB variables in instance data blocks that are predominantly used within the block in which they are declared.

The following table shows the difference between the variable types:

|  | PLC tags | Variables in instance DBs | Variables in global DBs |
| --- | --- | --- | --- |
| Range of application | - Are valid throughout the entire CPU. - Can be used by all blocks on the CPU. - The name is unique within the CPU. | - Are predominantly used in the block in which they are defined. - The name is unique within the instance DB. | - Can be used by all blocks on the CPU. - The name is unique within the global DB. |
| Permissible characters | - Letters, numbers, special characters - Quotation marks are not permitted. - Reserved keywords are not permitted. | - Letters, numbers, special characters - Reserved keywords are not permitted. | - Letters, numbers, special characters - Reserved keywords are not permitted. |
| Use | - I/O signals (I, IB, IW, ID, Q, QB, QW, QD) - Bit memory (M, MB, MW, MD) | - Block parameters   (input, output and in-out parameters), - Static data of a block | - Static data |
| Location of definition | PLC tag table | Block interface | Declaration table of the global DB |

> **Note**
>
> **You can find more information on permissible characters in tag names in the Siemens Industry Online Support in the following entries:**
>
> When should identifiers and operands be used in "quotation marks" in STEP 7 (TIA Portal)?
>
> ![Declaring Variables](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/109477857](https://support.industry.siemens.com/cs/ww/en/view/109477857)
>
> **You can find recommendations for uniform, project-wide tag naming in the programming style guide:**
>
> ![Declaring Variables](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/document/109478084](https://support.industry.siemens.com/cs/ww/en/view/81318674)

---

**See also**

[Keywords and reserved identifiers](#keywords-and-reserved-identifiers)
  
[Basic information about operands](#basic-information-about-operands)
  
[Displaying symbolic and absolute addresses](Program%20editor.md#displaying-symbolic-and-absolute-addresses)
  
[Valid names of PLC tags](Declaring%20PLC%20tags.md#valid-names-of-plc-tags)
  
[Permissible addresses and data types of PLC tags](Declaring%20PLC%20tags.md#permissible-addresses-and-data-types-of-plc-tags)

### Constants

This section contains information on the following topics:

- [Basics of constants](#basics-of-constants)
- [Declaration of symbolic names for constants](#declaration-of-symbolic-names-for-constants)
- [Data types of constants](#data-types-of-constants)
- [Examples of using constants](#examples-of-using-constants)

#### Basics of constants

##### Definition

Constants are data with a fixed value that you cannot change during program runtime. Constants can be read by various program elements during the execution of the program but cannot be overwritten. There are defined notations for the value of a constant, depending on the data type and data format. A distinction is made between the typed and non-typed notation.

##### Non-typed constants

In the non-typed notation, you only enter the value of the constant without a data type. Non-typed constants do not receive their data type until the first arithmetic or logical operation in which they are used.

The example below shows the non-typed notation:

| SCL |  |
| --- | --- |
| #My_Int1 := #My_Int2 + 12345; | (*The data type of the constant "12345"  results from the addition with My_Int. 2. "12345" receives the data type INT.*) |
| #My_Real1 := #My_Real2 + 12345; | (*The data type of the constant "12345" results from the addition with My_Real2. "12345" receives the data type REAL.*) |

##### Typed constants

In the typed notation, you specify a data type in addition to the value of the constant.

The example below shows the typed notation:

| SCL |  |
| --- | --- |
| #My_Int1 := INT#12345; | (*The data type of the constant is always INT.*) |

> **Note**
>
> **Constants of BOOL type in LAD/FBD**
>
> The use of constants of type BOOL for inputs of instructions in LAD/FBD is only possible in CPUs of the S7-1200 series FW V4.0 or higher and S7-1500 series FW V1.8 or higher.
>
> In older firmware versions, BOOL-type constants may only be used for instructions that are an internal function block (FB) of the system. These instructions are identified by the fact that the "Call options" dialog opens when you insert the instruction into a network. For all other instructions, Boolean constants must not be used as inputs.
>
> Use of Boolean constants in S7-300/400 is not permitted.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Declaring the block interface](Declaring%20the%20block%20interface.md#declaring-the-block-interface-1)
  
[Declaring global constants](Declaring%20PLC%20tags.md#declaring-global-constants)
  
[Calculating with constants in SCL](Creating%20SCL%20programs.md#calculating-with-constants-in-scl)

#### Declaration of symbolic names for constants

##### Symbolic constants

You have the option of declaring symbolic names for constants and thus making constant values available under a name in the program. This makes a program more readable and easier to maintain when changing constant values.

A symbolic constant consists of the following elements:

- Name
- Data type

  Symbolic constants always have a data type; non-typed notation is not possible for symbolic constants.
- Constant value

  You can select any value from the value range of the specified data type as constant value. For information on the value ranges, refer to the "Data types" chapter.

##### Declaration of constants

You can define constants with different scopes of validity:

- Global constants that apply to all areas of the CPU
- Local constants that only apply within a block

The table below shows the difference between the constant types:

|  | Global constants | Local constants |
| --- | --- | --- |
| Scope of validity | - Are valid throughout the entire CPU - The name is unique within the CPU. | - Are valid only in the block in which they were declared. - The name is unique within the block. |
| Permitted characters | - The permitted characters in constant names are letters, digits and special characters. | - The permitted characters in constant names are letters, digits and special characters. |
| Location of definition | "Constants" tab from the PLC tag table | Block interface |
| Representation | In quotation marks, for example.:   `"Glob_Const"` | Prefixed with a number sign, for example:   `#Loc_Const` |

Name conflicts can occur if you have declared a local and a global constant with the same symbolic name and have used this doubly specified name as the default value of a tag. In this case, the local constant is automatically used.

> **Note**
>
> **Downloading constant declarations (S7-300/400)**
>
> Local and global constant declarations are not downloaded into the CPU. If you download a program from a device, the constant declarations may no longer be available.

> **Note**
>
> **You can find more information on permissible characters in constant names in the Siemens Industry Online Support in the following entries:**
>
> When should identifiers and operands be used in "quotation marks" in STEP 7 (TIA Portal)?
>
> ![Declaration of constants](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/109477857](https://support.industry.siemens.com/cs/ww/en/view/109477857)

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Declaring global constants](Declaring%20PLC%20tags.md#declaring-global-constants)
  
[Declaring the block interface](Declaring%20the%20block%20interface.md#declaring-the-block-interface-1)
  
[Calculating with constants in SCL](Creating%20SCL%20programs.md#calculating-with-constants-in-scl)

#### Data types of constants

##### Permitted data types

For constants, all basic data types as well as all derived data types are permitted:

- Binary numbers
- Bit strings
- Integers
- Floating-point numbers
- Timers
- Date and time
- Character strings

All general rules for explicit and implicit type conversion apply.

##### Data types of non-typed constants

Non-typed constants do not contain an explicit type specification. They do not receive their data type until the first arithmetic or logical operation in which they are used.

The example below shows how non-typed constants are used:

| SCL |  |
| --- | --- |
| #My_Int1 := #My_Int2 + 12345; | (*The data type of the constant "12345"  results from the addition with My_Int. 2. "12345" receives the data type INT.*) |
| #My_Real1 := #My_Real2 + 12345; | (*The data type of the constant "12345" results from the addition with My_Real2. "12345" receives the data type REAL.*) |

> **Note**
>
> **STEP 7 always uses the data type with the highest possible precision**
>
> Unless the data type of a constant can be clearly defined in an expression, the data type with the highest precision available on the current CPU is used.
>
> Example:  
> `#My_Real := #My_Int / 3.5;`
>
> In this expression an integer tag is combined with a non-typed floating point constant. In S7-300/400 the right part of the assignment is calculated in the REAL format. In S7-1200/1500, calculation is performed using the highest possible precision, which in this case means LREAL. As a result, the assignment to a REAL tag is invalid or generates a warning.
>
> To precisely define the data type of a constant, use the typed notation.
>
> Example:
>
> `#My_Real := #My_Int / REAL#3.5;`

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Declaring global constants](Declaring%20PLC%20tags.md#declaring-global-constants)
  
[Declaring the block interface](Declaring%20the%20block%20interface.md#declaring-the-block-interface-1)
  
[Calculating with constants in SCL](Creating%20SCL%20programs.md#calculating-with-constants-in-scl)

#### Examples of using constants

##### Use in instructions, assignments and expressions

Constants can be used in place of tags in instructions or assignments. You can also use constants in expressions in SCL. But because constants cannot be written, they may only be used as inputs.

The example below shows possible uses of constants:

| SCL |  |
| --- | --- |
| #My_Int := 3; |  |
| #My_Real1 := #My_Real2 * 3; |  |
| #My_Real1 := #My_Real2 * #My_local_const; |  |
| #My_Real1 := #My_Real2 * "My_global_const"; |  |

##### Use as a default value

You can use constants as the default value of a tag. To do so, enter either the value or the symbolic name of the constant in the "Default value" column of the block interface. The data type of the constant must match the data type of the tag or be convertible with it according to the implicit conversion with IEC check.

##### Use as maximum STRING length

You can use local or global constants of data type UINT, UDINT, ULINT, SINT, INT, DINT, LINT as maximum STRING length.

The example below shows the use of constants as maximum STRING length:

| SCL |  |
| --- | --- |
| STRING[#My_local_const1]  STRING["My_global_const1"] |  |

##### Use as an ARRAY limit

You can use local or global constants of data type UINT, UDINT, ULINT, SINT, INT, DINT, LINT as ARRAY limits.

The example below shows the use of constants as ARRAY limits:

| SCL |  |
| --- | --- |
| Array[#My_local_const1..#My_local_const2] of REAL  Array["My_global_const1".."My_global_const1"] of REAL |  |

> **Note**
>
> **Constants as ARRAY limits or as maximum STRING length**
>
> - Constants which are used as ARRAY limits or maximum STRING length cannot be changed if the memory reserve of the block is activated. This applies to both local and global constants. To change these constants, you must first disable the memory reserve.
> - Changes to global constants result in inconsistencies in the blocks which use them. The inconsistencies are marked in red in the block used. To remedy these inconsistencies, the data blocks have to be updated.
>
>   See also: [Updating data blocks](Programming%20data%20blocks.md#updating-data-blocks)

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on ARRAY](Data%20types.md#basic-information-on-array)
  
[Declaring global constants](Declaring%20PLC%20tags.md#declaring-global-constants)
  
[Declaring the block interface](Declaring%20the%20block%20interface.md#declaring-the-block-interface-1)
  
[Calculating with constants in SCL](Creating%20SCL%20programs.md#calculating-with-constants-in-scl)

### Addressing operands

This section contains information on the following topics:

- [Addressing PLC tags](#addressing-plc-tags)
- [Addressing variables in data blocks](#addressing-variables-in-data-blocks)
- [Addressing operands indirectly](#addressing-operands-indirectly)

#### Addressing PLC tags

This section contains information on the following topics:

- [Addressing PLC tags](#addressing-plc-tags-1)
- [Accessing I/O devices](#accessing-io-devices)

##### Addressing PLC tags

To address a PLC tag, you can use the absolute address or the symbolic name.

> **Note**
>
> The LWORD, LINT, ULINT, LREAL, LTIME, LTOD and LDT data types can only be addressed by means of their symbolic name.

###### Symbolic addressing of PLC tags

To address PLC tags symbolically, enter the tag name from the PLC tag table.

You can also address structured PLC tags that are based on a PLC data type with the symbolic name of the PLC tag. You can also indicate the names of the individual structure elements separated by a dot.

The notation of the PLC tag depends on whether you use namespaces in your program:

- If the accessing block is in a namespace, the IEC-compliant notation is used. The PLC tag is not with quotation marks.
- If the accessing block is not located in a namespace, PLC tags are notated in quotation marks.

See also: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

###### Absolute addressing of PLC tags

When you use addressing in absolute form, you enter the address of the variables from the PLC tag table. The absolute address uses numerical addresses starting with zero for each operand range. The absolute address of PLC tags is automatically preceded by the address indicator %.

###### Examples

The following examples show applications of symbolic and absolute addressing:

| Addressing | Explanation |
| --- | --- |
| %Q1.0 | Absolute address: Output 1.0 |
| %I16.4 | Absolute address: Input 16.4 |
| %IW4 | Absolute address: Input word 4 |
| _.Motor | Symbolic addressing of the "Motor" PLC tag. The accessing block is in a namespace. |
| "Value" | Symbolic addressing of the "Value" PLC tag. The accessing block is outside namespaces. |
| "Structured_Tag" | Symbolic addressing of a tag that is based on a PLC data type |
| "Structured_Tag".Element | Symbolic addressing of an element of a structured tag. |

---

**See also**

[Displaying symbolic and absolute addresses](Program%20editor.md#displaying-symbolic-and-absolute-addresses)
  
[Permissible addresses and data types of PLC tags](Declaring%20PLC%20tags.md#permissible-addresses-and-data-types-of-plc-tags)
  
[Accessing I/O devices](#accessing-io-devices)
  
[Overview of PLC tag tables](Declaring%20PLC%20tags.md#overview-of-plc-tag-tables)

##### Accessing I/O devices

###### Description

The process image of the CPU is updated once in a cycle. In time-critical applications, however, it can be that the current state of a digital input or output has to be read or transferred more often than once per cycle. For this purpose you can use a suffix for I/O access identifiers on the operand to directly access the I/O.

If you want to read the input directly from the peripherals, use the peripheral inputs memory area (PI) instead of the process image input (I). The peripherals memory area can be read as a bit, byte, word, or double word.

If you want to write directly to the output, use the peripheral output (PQ) memory area instead of the process image output (Q). The peripheral output memory area can be written as a bit, byte, word, or double word.

To read or write a signal directly from a peripheral input, you can add the suffix for I/O access ":P", to the operand.

Components of structured PLC tags can also be addressed with ":P". However, access to the higher-level tag with ":P" is not possible.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Direct writing of the I/O**  Immediate writing to the I/O can lead to hazardous states, for example when writing multiple times to an output in one program cycle. |  |

> **Note**
>
> **S7-1200/1500: Transferring peripheral inputs or outputs as block parameters**
>
> If you supply an input parameter with a peripheral input or output, it is possible that I/O access errors will occur during runtime when the block is called, e.g. a read error when an input module is accessed directly.
>
> The system response of S7-1500 series CPUs with firmware version V2.1 or higher is as follows:
>
> The block is called and processed with the substitute value of the signal.
>
> The system response of S7-1200 and S7-1500 series CPUs with firmware versions lower than V2.1 is as follows:
>
> The block is not called as a result of the I/O access error. Program execution is continued after the block call. If OB 122 exists or local error handling is enabled, these are executed.
>
> To prevent the situation that the block is not called as a result of an I/O access error, first copy the peripheral input or output to a local tag (Temp) and transfer it as a block parameter to the called block.
>
> The FAQ below provide additional information on this topic:
>
> [FAQ 89377245: Why are blocks in the S7-1200/S7-1500 not processed when they are addressed with unavailable PROFINET components?](https://support.industry.siemens.com/cs/ww/en/view/89377245)

###### Syntax

&lt;Operand&gt;:P

###### Example

The following example shows applications of I/O access identifiers:

| Addressing | Description |
| --- | --- |
| "Motor" | Addresses the "Motor" tag in the process image. |
| "Motor":P | Addresses the "Motor" tag in the I/O memory area (PI or PQ). |
| "Structured_Tag".Component | Addresses the component of a structured PLC tag in the process image. |
| "Structured_Tag".Component:P | Addresses the component of a structured PLC tag in the I/O memory area (PI or PQ). |
|  |  |

---

**See also**

[Addressing PLC tags](#addressing-plc-tags-1)

#### Addressing variables in data blocks

This section contains information on the following topics:

- [Addressing tags in global data blocks](#addressing-tags-in-global-data-blocks)
- [Addressing instance data](#addressing-instance-data)
- [Addressing tags in ARRAY data blocks (S7-1500)](#addressing-tags-in-array-data-blocks-s7-1500)
- [Addressing areas of a tag with slice access (S7-1200, S7-1500)](#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
- [Overlaying tags with AT](#overlaying-tags-with-at)

##### Addressing tags in global data blocks

###### Symbolic addressing of tags in global data blocks

For symbolic addressing of tags in global data blocks, use the name of the data block and the name of the tag, separated by a dot.

The notation of the data block name depends on whether you use namespaces in your program:

- If neither the accessing block nor the global data block is located in a namespace, data blocks are notated in quotation marks.
- If one of the two blocks is located in a namespace, the IEC-compliant notation is used. The name of the data block is not in quotation marks.

The following table shows the syntax for symbolic addressing of tags in global data blocks:

| Situation | Syntax | Example |
| --- | --- | --- |
| Neither the accessing block nor the global data block is located in a namespace. | "&lt;BlockName&gt;".&lt;TagName&gt; | "MyDataBlock".MyVariable |
| The accessing block and the global data block are in the same namespace. | &lt;BlockName&gt;.&lt;TagName&gt; | MyDataBlock.MyVariable |
| The accessing block is in a namespace.   The global data block is in one of its subnamespaces. | &lt;Subnamespace&gt;.&lt;BlockName&gt;.&lt;TagName&gt; | MySubnamespace.MyDataBlock.MyVariable |
| The accessing data block is in a namespace.   The global data block has no namespace. | _.&lt;BlockName&gt;.&lt;Tag name&gt; | _.MyDataBlock.MyVariable |
| The accessing block is in a namespace.   The global data block is in a different namespace. | _.&lt;Namespace&gt;.&lt;BlockName&gt;.&lt;Tag name&gt; | _.MyNamespace.MyDataBlock.MyVariable |

###### Absolute addressing of tags in global data blocks

For absolute addressing of tags in global data blocks, use the number of the data block and the absolute address of the tags in the data block, separated by a dot. The address identifier % is set automatically as prefix for the absolute address.

The following table shows the syntax for absolute addressing of tags in global data blocks:

| Data type | Syntax | Example | Description |
| --- | --- | --- | --- |
| BOOL | %&lt;DBn&gt;.DBX&lt;x.y&gt; | %DB1.DBX1.0 | Data bit 1.0 in DB1 |
| BYTE, CHAR, SINT, USINT | %&lt;DBn&gt;.DBB&lt;x&gt; | %DB1.DBB1 | Data bit 1 in DB1 |
| WORD, INT, UINT | %&lt;DBn&gt;.DBW&lt;x&gt; | %DB1.DBW1 | Data word 1 in DB1 |
| DWORD, DINT, UDINT, REAL, TIME | %&lt;DBn&gt;.DBD&lt;x&gt; | %DB1.DBD1 | Data double word 1 in DB1 |

> **Note**
>
> **Absolute addressing of DB tags**
>
> Absolute addressing is not possible for the following tags:
>
> - Tags in blocks with optimized access.
> - Tags of data type LWORD, LINT, ULINT, LREAL, LTIME, LTOD and LDT.
>
> Use the more convenient symbolic addressing for these tags.

---

**See also**

[Addressing individual characters of a STRING or WSTRING (S7-1200, S7-1500)](Data%20types.md#addressing-individual-characters-of-a-string-or-wstring-s7-1200-s7-1500)
  
[Addressing PLC data types (UDT)](Data%20types.md#addressing-plc-data-types-udt)
  
[Addressing STRUCT elements](Data%20types.md#addressing-struct-elements)
  
[Categorizing program elements in namespaces (S7-1500)](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)

##### Addressing instance data

###### Description

You can address data elements from the interface of the current block. These tags are stored in the instance data block.

> **Note**
>
> Tags in blocks with optimized access can only be addressed in symbolic form.

To address a tag from the interface of the current block, enter the character # followed by the symbolic tag name.

You can also access the tags of a multi-instance block. Within the multi-instance block, also use the character # followed by the tag name to address the data. You access the data of the multi-instance block from the calling block using #&lt;Multi-instanceName.TagName&gt;.

###### Syntax

Use the following syntax for addressing tags in instance data blocks:

#&lt;tag name&gt;

#&lt;multi-instance name&gt;.&lt;tag name&gt;

###### Examples

The following examples show the addressing of tags in instance data blocks:

| Addressing | Description |
| --- | --- |
| #Value | Addressing the "Value" tag in the instance data block. |
| #On | Addressing the "On" tag within the multi-instance block |
| #Multi.On | Addressing the "On" tag of the multi-instance block from the calling block |

---

**See also**

[Addressing tags in global data blocks](#addressing-tags-in-global-data-blocks)
  
[Instances](#instances)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)
  
[Addressing areas of a tag with slice access (S7-1200, S7-1500)](#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
  
[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)

##### Addressing tags in ARRAY data blocks (S7-1500)

ARRAY data blocks are a particular type of global data block. They consist of an ARRAY of any data type. The ARRAY can also consist of PLC data types (UDT). ARRAY data blocks always have optimized block access.

###### Addressing ARRAY data blocks

You address elements in ARRAY data blocks with the help of the keyword "THIS". The index is then specified in square brackets. The index can be both a constant and a tag. Integers with a width of up to 32 bits are permitted as tags for the index.

The following table shows the syntax for addressing elements of an ARRAY data block:

| Syntax | Example | Description |
| --- | --- | --- |
| "&lt;ArrayDBName&gt;".THIS[#i].&lt;Component&gt;.&lt;ComponentElement&gt; | "myARRAY_DB".THIS[#myIndex].myComponent.myComponentElement | The ARRAY index is specified with the "myIndex" tag.   The ARRAY element contains two substructures: "MyComponent" and "MyComponentElement".   Neither the accessing block nor the ARRAY data block is located in a namespace. |
|  | "myARRAY_DB".THIS[0] | The ARRAY index is specified with the constant "0".  Neither the accessing block nor the ARRAY data block is located in a namespace. |
| &lt;Namespace&gt;.&lt;ArrayDBName&gt;.THIS[#i].&lt;Component&gt;.&lt;ComponentElement&gt; | myNamespace.myARRAY_DB.THIS[0] | If the accessing block or the ARRAY data block is located in a namespace, the IEC-compliant notation is used. The name of the data block is not in quotation marks. |
| SCL  "&lt;ArrayDBName&gt;"."THIS"[#i].&lt;Component&gt;.&lt;ComponentElement&gt; | "myARRAY_DB"."THIS"[#myIndex].myComponent.myComponentElement | In SCL, the keyword "THIS" is placed in quotation marks. |

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces at: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

###### Instructions for addressing ARRAY data blocks

The "Instructions &gt; Basic instructions" task card in the "Move &gt; ARRAY DB" section offers extended options for addressing ARRAY data blocks. These instructions give you the option, for example, to address the DB name indirectly:

- ReadFromArrayDB: Read from array data block
- WriteToArrayDB: Write to array data block
- ReadFromArrayDBL: Read from array data block in load memory
- WriteToArrayDBL: Write to ARRAY data block in load memory

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Indirect indexing of ARRAY components (S7-1200, S7-1500)](#indirect-indexing-of-array-components-s7-1200-s7-1500)
  
[Global ARRAY data blocks (DB)](#global-array-data-blocks-db)
  
[ARRAY](Data%20types.md#array)
  
[Example of the use of ARRAY data blocks](#example-of-the-use-of-array-data-blocks)

##### Addressing areas of a tag with slice access (S7-1200, S7-1500)

###### Description

You have the option to specifically address areas within declared tags. You can access areas of the 1-bit, 8-bit, 16-bit, or 32-bit width. The division of a memory area (e.g. BYTE or WORD) into a smaller memory area (e.g. BOOL) is also referred to as a "slice".

Structures, constants and tags overlaying AT cannot be addressed with slice access.

###### Syntax

The following syntax is used for addressing:

&lt;Tag&gt;.X&lt;Bit number&gt;

&lt;Tag&gt;.B&lt;BYTE number&gt;

&lt;Tag&gt;.W&lt;WORD number&gt;

&lt;Tag&gt;.D&lt;DWORD number&gt;

The syntax has the following components:

| Part | Description |
| --- | --- |
| &lt;Tag&gt; | Tag that you access. The tag must be of the "Bit string" or "Integer" data type.   With SCL, you can only program slice access to tags of the "Integer" data type when the IEC check is disabled. |
| X  B  W  D | ID for the access width "Bit (1Bit)"  ID for the access width "Byte (8 Bit)"  ID for the access width "Word (16 Bit)"  ID for access width "DWord (32-bit)" |
| &lt;BIT number&gt; | Bit number within &lt;tag&gt; that is accessed. Number 0 accesses the least significant BIT. |
| &lt;BYTE number&gt; | Byte number within &lt;tag&gt; that is accessed.  The number 0 accesses the least significant BYTE. |
| &lt;WORD number&gt; | Word number within &lt;tag&gt; that is accessed.  The number 0 accesses the least significant WORD. |
| &lt;DWORD number&gt; | DWord number within &lt;tag&gt; that is accessed.  The number 0 accesses the least significant DWORD. |

###### Examples of slice access

The following examples show the addressing of slices in bit, byte, word and double word modes:

| Addressing | Description |
| --- | --- |
| "Engine".Motor.X0  "Engine".Motor.X7 | "Motor" is a tag of the BYTE, WORD, DWORD or LWORD data type in the global data block "Engine".  X0 addresses the bit address 0, X7 the bit address 7 within "Motor". |
| "Engine".Speed.B0  "Engine".Speed.B1 | "Speed" is a tag of the WORD, DWORD or LWORD data type in the global data block "Engine".  B0 addresses the byte address 0, B1 the byte address 1 within "Speed". |
| "Engine".Fuel.W0  "Engine".Fuel.W1 | "FUEL" is a tag of the DWORD or LWORD data type in the global data block "Engine".  W0 addresses the word address 0, W1 the word address 1 within "Fuel". |
| "Engine".Data.D0  "Engine".Data.D1 | "Data" is a tag of the LWORD data type in the global data block "Engine".  D0 addresses the double word address 0, D1 the double word address 1 within "Data". |

###### Programming example

You can find a detailed example in the Siemens Industry Online Support:

[https://support.industry.siemens.com/cs/ww/de/view/57374718](https://support.industry.siemens.com/cs/ww/en/view/57374718)

##### Overlaying tags with AT

###### Description

To access data areas within a declared tag, you can overlay the declared tags with an additional declaration. This provides you with the option of addressing an already declared tag with a different data type. You can, for example, address the individual bits of a tag of WORD data type with an ARRAY of BOOL.

Alternatively, you can also use the instructions "SCATTER" and "GATHER" to break down bit sequences into an ARRAY of BOOL or group together individual bits to form a bit sequence. You can find these instructions in the "Basic instructions" task card in the "Move" area.

###### Rules

The following general rules are valid for tag overlaying:

- Overlaying is possible in S7-1200 and S7-1500 in STL, LAD, FBD and GRAPH.
- SCL supports overlaying in all CPU families.
- Overlaying of tags is possible in the following blocks:

  - In code blocks with standard access
  - In code blocks with optimized access for tags with the retain setting "Set in IDB"
- The data width of the overlaying tag must be equal to or less than that of the overlaid tag.
- It is not possible to overlay tags of the VARIANT and INSTANCE data types.
- Multi-instance declarations cannot be overlaid.
- If the overlaid tag is of the data type STRING, ARRAY of BYTE, ARRAY of CHAR, etc., the length should correspond to an even number of bytes.
- Blocks from libraries which are declared as parameters in the interface cannot be overlaid.
- Structured PLC tags that are declared as parameters in the interface cannot be overlaid.
- You cannot address overlaying tags with slice access.

> **Note**
>
> **S7-1200/1500: Using AT in FCs**
>
> The data widths of the overlaying tag and the overlaid tag must be identical for FCs in S7-1200/1500. If this is not possible in your program, check to see if you can use slice access instead of the AT construct, or use the instructions "SCATTER" or "GATHER".
>
> See also: [Addressing areas of a tag with slice access](#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)

The following combination rules are also valid:

|  |  | Overlaying tag | Overlaid tag |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Elementary | Structured * | Any/Pointer | DB_ANY |
| FB | Input | Elementary | x | x ** | - | x |
| Structured * | x | x | x | x |  |  |
| Any/Pointer | - | x | - | - |  |  |
| Temp | Elementary | x | x ** | - | - |  |
| Structured | x | x | x | - |  |  |
| Any/Pointer | - | x | - | - |  |  |
| Static, Output | Elementary | x | x ** | - | x |  |
| Structured | x | x | - | x |  |  |
| Any/Pointer | - | - | - | - |  |  |
| InOut | Elementary | x | - | - | x |  |
| Structured | - | x | - | - |  |  |
| Any/Pointer | - | - | - | - |  |  |
| FC | Temp | Elementary | x | x ** | - | - |
| Structured | x | x | x | - |  |  |
| Any/Pointer | - | x | - | - |  |  |
| Input, Output, InOut | Elementary  (both tags must have the same bit width) | x | - | - | x |  |
| Structured | - | x | - | - |  |  |
| Any/Pointer | - | - | - | - |  |  |
| OB | Temp | Elementary | x | x ** | - | - |
| Structured | x | x | x | - |  |  |
| Any/Pointer | - | x | - | - |  |  |

* Structured data types consist of several data elements, e.g. ARRAY or STRUCT.

** Exception: BOOL, BYTE, SINT, USINT and CHAR must not be overlaid with tags of the data types STRUCT, UDT or ARRAY.

###### Declaration

To overlay a tag, declare an additional tag directly after the tag that is to be overlaid and identify it with the keyword "AT".

###### Example

The following figure shows the declaration of an overlaid tag in the interface of a FB:

![Example](images/126943859723_DV_resource.Stream@PNG-de-DE.png)

When a block is called with the shown tag declaration, the "MyWord" tag will be is assigned. Within the block there are now two options for interpreting the data:

- As WORD
- As one-dimensional ARRAY of BOOL

---

**See also**

[Declaring higher-level tags](Declaring%20the%20block%20interface.md#declaring-higher-level-tags)
  
[Setting retentivity](Programming%20data%20blocks.md#setting-retentivity)

#### Addressing operands indirectly

This section contains information on the following topics:

- [Indirect addressing (S7-1200, S7-1500)](#indirect-addressing-s7-1200-s7-1500)
- [Indirect addressing (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-s7-300-s7-400)

##### Indirect addressing (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
- [Examples of indirect addressing (S7-1200, S7-1500)](#examples-of-indirect-addressing-s7-1200-s7-1500)
- [Indirect addressing using a pointer (S7-1200, S7-1500)](#indirect-addressing-using-a-pointer-s7-1200-s7-1500)
- [Indirect indexing of ARRAY components (S7-1200, S7-1500)](#indirect-indexing-of-array-components-s7-1200-s7-1500)
- [Examples of indirect indexing of ARRAYs (S7-1200, S7-1500)](#examples-of-indirect-indexing-of-arrays-s7-1200-s7-1500)
- [Indirect addressing of a data block via DB_ANY data type (S7-1200, S7-1500)](#indirect-addressing-of-a-data-block-via-db_any-data-type-s7-1200-s7-1500)
- [Indirect addressing of individual characters of a STRING (S7-1200, S7-1500)](#indirect-addressing-of-individual-characters-of-a-string-s7-1200-s7-1500)
- [Indirect addressing in STL (S7-1500)](#indirect-addressing-in-stl-s7-1500)

###### Basics of indirect addressing (S7-1200, S7-1500)

###### Introduction

Indirect addressing offers you the option of addressing operands whose address is not calculated until runtime. With indirect addressing, you can also have program sections run several times and use a different operand during each run. For example, you can use a different index in each run in program loops.

This gives you the following advantages:

- You have more flexibility within your program.
- Indirect addressing is available to you in all STEP 7 programming languages.
- You have a better overview of the program code.
- The existing names of data blocks and tags are used (symbolic addressing). This improves readability of the program code.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Risk of access errors**  Since operands are only calculated at runtime with indirect addressing, there is a risk that access errors may occur and that the program will operate with incorrect values. In addition, memory areas may inadvertently be overwritten with incorrect values. The automation system can then react in an unexpected manner.  Therefore, indirect addressing should be used with caution. |  |

###### General indirect addressing options in S7-1200 and S7-1500

The following indirect addressing options are available in all programming languages:

- Indirect addressing via pointer (e.g. pointer, references or the VARIANT data type)
- Indirect indexing of ARRAY components
- Indirect addressing of a data block via DB_ANY data type.

###### Language-specific options of indirect addressing

The following specific addressing options are also available in the various programming languages:

- In STL, you can address operands indirectly via the address register.
- In SCL, you can read or write a variable memory area with the following instructions:

  - POKE - Write memory address
  - POKE_BOOL - Write memory bit
  - PEEK - Read memory address
  - PEEK_BOOL - Read memory bit
  - POKE_BLK - Write memory area

---

**See also**

[Addressing tags in global data blocks](#addressing-tags-in-global-data-blocks)
  
[POKE: Write memory address (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke-write-memory-address-s7-1200-s7-1500)
  
[POKE_BOOL: Write memory bit (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke_bool-write-memory-bit-s7-1200-s7-1500)
  
[PEEK: Read memory address (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#peek-read-memory-address-s7-1200-s7-1500)
  
[PEEK_BOOL: Read memory bit (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#peek_bool-read-memory-bit-s7-1200-s7-1500)
  
[POKE_BLK: Write memory area (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#poke_blk-write-memory-area-s7-1200-s7-1500)
  
[Indirect addressing using a pointer (S7-1200, S7-1500)](#indirect-addressing-using-a-pointer-s7-1200-s7-1500)
  
[Indirect indexing of ARRAY components (S7-1200, S7-1500)](#indirect-indexing-of-array-components-s7-1200-s7-1500)
  
[Indirect addressing in STL (S7-1500)](#indirect-addressing-in-stl-s7-1500-1)

###### Examples of indirect addressing (S7-1200, S7-1500)

###### 1. Program example

In the example below, you use the index to access three tags from different memory areas.

Overview of the three tags that are assigned to one index each:

| Index | Accessing tag | Memory area |
| --- | --- | --- |
| 1 | Input_WORD_0 | IW 0 |
| 2 | "Processdata".Temperature | DB 1 |
| 3 | Output_WORD_4 | QW 4 |

Declare the following two tags in the "Default tag table":

![1. Program example](images/69382043659_DV_resource.Stream@PNG-de-DE.png)

Create a global data block:

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_Processdata".
4. Select "Global DB" as the type of the data block.
5. Click "OK".
6. Declare the data block element "Temperature":

   ![1. Program example](images/69385713291_DV_resource.Stream@PNG-de-DE.png)

   ![1. Program example](images/69385713291_DV_resource.Stream@PNG-de-DE.png)

Declare indirect access using an index within a function.

1. Create an SCL function and name it "FB_AccessGroupInt".
2. Declare the block interface as follows:

   ![1. Program example](images/69386630923_DV_resource.Stream@PNG-de-DE.png)

   ![1. Program example](images/69386630923_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![1. Program example](images/145725889035_DV_resource.Stream@PNG-de-DE.png)

   ![1. Program example](images/145725889035_DV_resource.Stream@PNG-de-DE.png)
4. Call the "FC_AccessGroupInt" function in OB1:

   ![1. Program example](images/69390642955_DV_resource.Stream@PNG-de-DE.png)

   ![1. Program example](images/69390642955_DV_resource.Stream@PNG-de-DE.png)

   Depending on which number (1, 2 or 3) you specify at the Index parameter, the first, second or third case of the "FC_AccessGroupInt" instruction is executed.

###### 2. Program example

In the example below, you use the index to access three different optimized data blocks.

Since all data blocks should contain the same tags, you can use a PLC data type (UDT) in this case.

1. To create a PLC data type, double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Rename the PLC data type to "UDT_SiloContents".
3. Declare the following lines within the PLC data type:

   MyBool &gt; Data type: BOOL

   MyInt &gt; Data type: INT

   MyWord &gt; Data type: WORD

   ![2. Program example](images/69392328843_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69392328843_DV_resource.Stream@PNG-de-DE.png)

Create three global data blocks.

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the names "DB_SiloWater", "DB_SiloSugar" and "DB_SiloMilk".
4. Select the data blocks "UDT_SiloContents" as the type of the data blocks.
5. Click "OK".

   ![2. Program example](images/69394987275_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69394987275_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69394996107_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69394996107_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69396144139_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69396144139_DV_resource.Stream@PNG-de-DE.png)

Create a function to read the values of the data block tags and to write these to a PLC data type.

1. Create an SCL function and name it "FC_AccessGroupSiloRead".
2. Declare the block interface as follows:

   ![2. Program example](images/69397356171_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69397356171_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![2. Program example](images/69397365003_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69397365003_DV_resource.Stream@PNG-de-DE.png)
4. Call the "FC_AccessGroupSiloRead" function in OB1:

   ![2. Program example](images/69398577035_DV_resource.Stream@PNG-de-DE.png)

   ![2. Program example](images/69398577035_DV_resource.Stream@PNG-de-DE.png)

   Depending on which number (1, 2 or 3) you specify at the

   Index parameter, the first, second or third case of the "FC_AccessGroupSiloRead" instruction is executed.

---

**See also**

[Indirect addressing in STL (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-in-stl-s7-300-s7-400)
  
[Indirect addressing in SCL (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-in-scl-s7-300-s7-400)
  
[Addressing operands indirectly](#addressing-operands-indirectly)

###### Indirect addressing using a pointer (S7-1200, S7-1500)

###### Description

For indirect addressing, a special data format is required that contains the address and possibly also the range and the data type of an operand. This data format is referred to as pointer. The following types of pointers are available to you:

- References (S7-1500)
- VARIANT (S7-1200/1500)
- POINTER (S7-1500)
- ANY (S7-1500, only for blocks with standard access)

For more information on the pointer data types, refer to "See also".

> **Note**
>
> **POINTER in SCL**
>
> In SCL the use of the POINTER is restricted. The only option available is to forward it to the called block.

###### Example

The following example shows an indirect addressing with an area-internal pointer:

| Addressing in STL | Explanation |
| --- | --- |
| L P#10.0 | // Load pointer (P#10.0) in accumulator 1 |
| T MD20 | // Transfer pointer to the operand MD20 |
| L MW [MD20] | // Load MW10 in Accumulator 1 |
| .... | // Any program |
| L MD [MD20] | // Load MD10 in Accumulator 1 |
| .... | // Any program |
| = M [MD20] | // If RLO=1, set the memory bit M10.0 |
|  |  |

The pointer P#10.0 is transferred to the operand MD20. If the operand MD20 in square brackets is programmed, this will be replaced in runtime by the address that is contained in the pointer.

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Pointer](Data%20types.md#pointer)

###### Indirect indexing of ARRAY components (S7-1200, S7-1500)

###### ARRAY access with variable index

For addressing ARRAY elements, you can specify either constants or tags of the integer data type as index. Integers with a length of up to 32 bits are allowed here.

With indirect addressing using a tag, the index is only calculated during program runtime. You can, for example, use a different index for each cycle in program loops.

###### Syntax

The following syntax is used for the indirect indexing of a ARRAY:

"MyDB".MyArray[#i] // One-dimensional ARRAY

"MyDB".MyArray[#i].a // One-dimensional ARRAY of STRUCT

"MyDB".MyArray[#i,#j]// Multi-dimensional ARRAY

"MyDB".MyArray[#i].a // Multi-dimensional ARRAY of STRUCT

The syntax has the following components:

| Part | Description |
| --- | --- |
| MyDB | Name of the data block in which the ARRAY is located |
| MyArray | Tag of the ARRAY data type |
| i, j | PLC tags of the integer data type that are used as pointers |
| a | Additional partial tag of the structure |

> **Note**
>
> When you call a block and transfer an indirectly indexed ARRAY component ("MyDB".MyArray[#i]) to it as in/out parameter (InOut), you cannot change the value of the index tag [i] while the block is being executed. The value is therefore always written back to the same ARRAY component from which it was read.

###### Indexing ARRAY components using the "FieldRead" and "FieldWrite" instructions

You may also use the following instructions for indirect indexing of ARRAY components in LAD and FBD:

- FieldWrite - Write field
- FieldRead - Read field

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)
  
[ARRAY](Data%20types.md#array)
  
[Examples of indirect indexing of ARRAYs (S7-1200, S7-1500)](#examples-of-indirect-indexing-of-arrays-s7-1200-s7-1500)
  
[Indirect addressing of ARRAY components (S7-1200, S7-1500)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#indirect-addressing-of-array-components-s7-1200-s7-1500)

###### Examples of indirect indexing of ARRAYs (S7-1200, S7-1500)

###### Example: ARRAY access with variable index in LAD

The following example shows the indirect indexing of an ARRAY component using LAD as example. "MyArray" is a three-dimensional ARRAY. #Tag_1, #Tag_2 and #Tag_3 are input parameters of the data type "Integer". Depending on their values, one of the MyArray components is copied to the "MyTarget" tag.

![Example: ARRAY access with variable index in LAD](images/83055732107_DV_resource.Stream@PNG-de-DE.png)

###### Example: ARRAY access with variable index in SCL

The following example shows you how to address multiple data blocks using a variable index. Five speed-controlled axes are used in the example. These axes are to be processed with SCL iteratively in a FOR loop.

1. First you create five speed-controlled axes. All five axes must be of the same type.

   A data block is created for each axis in the project navigator:

   ![Example: ARRAY access with variable index in SCL](images/83124582027_DV_resource.Stream@PNG-de-DE.png)

   ![Example: ARRAY access with variable index in SCL](images/83124582027_DV_resource.Stream@PNG-de-DE.png)
2. Next, generate a global data block and declare an ARRAY of the data type ANY with five components.

   ![Example: ARRAY access with variable index in SCL](images/82994766603_DV_resource.Stream@PNG-de-DE.png)

   ![Example: ARRAY access with variable index in SCL](images/82994766603_DV_resource.Stream@PNG-de-DE.png)
3. For initialization, you assign the symbolic names of the five axes to the individual ARRAY elements in the startup OB.

   ![Example: ARRAY access with variable index in SCL](images/82994775435_DV_resource.Stream@PNG-de-DE.png)

   ![Example: ARRAY access with variable index in SCL](images/82994775435_DV_resource.Stream@PNG-de-DE.png)
4. In SCL, access to the individual axes takes place iteratively with the help of a FOR loop. The axes are transferred to the function "MaximumVelocity" for execution one after the other.

   ![Example: ARRAY access with variable index in SCL](images/82995821067_DV_resource.Stream@PNG-de-DE.png)

   ![Example: ARRAY access with variable index in SCL](images/82995821067_DV_resource.Stream@PNG-de-DE.png)

###### Example: ARRAY access with variable index in STL

An application example for ARRAY access with variable index in STL is available under ["Addressing ARRAY elements indirectly".](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#indirect-addressing-of-array-components-s7-1200-s7-1500)

---

**See also**

[Indirect indexing of ARRAY components (S7-1200, S7-1500)](#indirect-indexing-of-array-components-s7-1200-s7-1500)
  
[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)
  
[ARRAY](Data%20types.md#array)

###### Indirect addressing of a data block via DB_ANY data type (S7-1200, S7-1500)

###### Description

The S7-1200/1500 provides you with an option of accessing a data block that is not yet known during programming. For this purpose, create a block parameter of data type DB_ANY in the block interface of the accessing block. The data block name or data block number is transferred to this parameter during runtime.

In order to access the internal tags of the data block, use the name of the block parameter of data type DB_ANY and the absolute address of the tag, separated by a dot.

###### Syntax

The following table shows the syntax for indirect addressing of a data block via the DB_ANY data type:

| Syntax | Example | Description |
| --- | --- | --- |
| #&lt;DB_ANY-BlockParameter&gt;.%&lt;absoluteAddress&gt; | #myDBANY.%DBX30.0 | Absolute addressing of the "DBX30.0" tag in the data block that is transferred during runtime at the "myDBANY" parameter. |

---

**See also**

[Using the DB_ANY data type (S7-1200, S7-1500)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-the-db_any-data-type-s7-1200-s7-1500)

###### Indirect addressing of individual characters of a STRING (S7-1200, S7-1500)

###### Description

For addressing the individual characters of a STRING or WSTRING, you can specify constants and also tags as the index. The tags must be of the Integer data type. When tags are used, the index is calculated during runtime. You can, for example, use a different index for each cycle in program loops.

If you transfer a STRING or WSTRING with variable index to an in/out parameter during a block call, please note that: The index tag [i] is read once at the start of the block call and cannot be changed by the called block while it is being executed.

> **Note**
>
> **Monitoring STRING access in runtime**
>
> When a STRING or WSTRING that exceeds the defined length is written in runtime, unwanted reactions may occur in the program. Violation of the STRING or WSTRING length is monitored in S7-1200/1500. On read access to the STRING, you receive the character '$00' or '$0000'; write access to the STRING is not executed. If the instruction has the enable output ENO, ENO is set to the signal state FALSE. The CPU does not change to STOP.

###### Syntax

The following syntax is used for the indirect indexing of a STRING or WSTRING:

"&lt;Data block&gt;".&lt;STRING&gt;["i"]

"&lt;Data block&gt;".&lt;WSTRING&gt;["i"]

###### Example

The example below shows indirect indexing of a STRING using SCL as an example. "STRING", "WSTRING", "CHAR" and "WCHAR" are tags. "Tag_1" is a PLC tag of the "Integer" data type.

| Addressing in SCL | Description |
| --- | --- |
| STRING["Tag_1"] := CHAR; | (*Indirect addressing: Assignment of "CHAR" to the character of the STRING*) specified by "Tag_1" |
| WSTRING["Tag_1"] := WCHAR; | (*Indirect addressing: Assignment of "WCHAR" to the character of the WSTRING*) specified by "Tag_1" |
| WCHAR := WSTRING["Tag_1"]; | (*Indirect addressing: Assignment of the WSTRING character specified by "Tag_1" to WCHAR*) |

---

**See also**

[STRING](Data%20types.md#string)
  
[WSTRING (S7-1200, S7-1500)](Data%20types.md#wstring-s7-1200-s7-1500)

###### Indirect addressing in STL (S7-1500)

This section contains information on the following topics:

- [Basic information about address registers (S7-1500)](#basic-information-about-address-registers-s7-1500)
- [Indirect addressing in STL (S7-1500)](#indirect-addressing-in-stl-s7-1500-1)

###### Basic information about address registers (S7-1500)

###### Introduction

Two address registers are available for the indirect addressing of operands: address register 1 (AR1), and address register 2 (AR2). The address registers are equal and are 32 bits in length. You can store area-internal and cross-area pointers in the address registers. To define the address of an operand, you can call the stored data in the program.

Data is exchanged between the registers and the other available memory areas with the assistance of load and transfer instructions.

> **Note**
>
> In S7-1500, special rules apply to data exchange via address register and data block register:
>
> - The values in the registers do not remain in existence beyond the block limits.
> - The registers are reset when the language is changed within a block.
> - You can only reference data in blocks with optimized access if these have the retain setting "Set in IDB".
> - It is not possible to reference local data in blocks with optimized access with the help of the address registers (across areas).

---

**See also**

[LAR1: Load AR1 with contents of accumulator 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#lar1-load-ar1-with-contents-of-accumulator-1-s7-300-s7-400)
  
[LAR1 &lt;D&gt;: Load AR1 with double word or area pointer (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#lar1-d-load-ar1-with-double-word-or-area-pointer-s7-300-s7-400)
  
[LAR1 AR2: Load AR1 with contents of AR2 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#lar1-ar2-load-ar1-with-contents-of-ar2-s7-300-s7-400)
  
[LAR2: Load AR2 with contents of accumulator 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#lar2-load-ar2-with-contents-of-accumulator-1-s7-300-s7-400)
  
[CAR: Switch AR1 and AR2 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#car-switch-ar1-and-ar2-s7-300-s7-400)
  
[TAR1: Transfer AR1 to accumulator 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#tar1-transfer-ar1-to-accumulator-1-s7-300-s7-400)
  
[TAR1 &lt;D&gt;: Transfer AR1 to double word (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#tar1-d-transfer-ar1-to-double-word-s7-300-s7-400)
  
[TAR1 AR2: Transfer AR1 to AR2 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#tar1-ar2-transfer-ar1-to-ar2-s7-300-s7-400)
  
[TAR2: Transfer AR2 to accumulator 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#tar2-transfer-ar2-to-accumulator-1-s7-300-s7-400)
  
[+AR1: Add accumulator 1 to AR1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#ar1-add-accumulator-1-to-ar1-s7-300-s7-400)
  
[+AR2: Add accumulator 1 to AR2 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#ar2-add-accumulator-1-to-ar2-s7-300-s7-400)
  
[Indirect addressing in STL (S7-1500)](#indirect-addressing-in-stl-s7-1500-1)
  
[Data exchange in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#data-exchange-in-stl-s7-300-s7-400-s7-1500)
  
[Addressing areas of a tag with slice access (S7-1200, S7-1500)](#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
  
[Load and transfer (S7-1500)](STL%20%28S7-1500%29.md#load-and-transfer-s7-1500)
  
[Setting retentivity](Programming%20data%20blocks.md#setting-retentivity)

###### Indirect addressing in STL (S7-1500)

In STL, the following options are available for indirect addressing:

- Memory-indirect addressing
- Register-indirect area-internal addressing
- Register-indirect cross-area addressing

###### Memory-indirect addressing

In the case of memory-indirect addressing, you store the address in a tag. The tag can be of WORD or DWORD data type. The tag can be located in the memory areas "Data" (DB or DI), "Bit memory" (M) or "Temporary local data" (L). In S7-1500, FB parameters can also be used to store the address. If the tag is located in a data block, it must be a data black with standard access.

The following example shows applications of memory-indirect addressing:

| Addressing in STL | Explanation |
| --- | --- |
| U E [MD 2] | // Execute an AND logic operation with a variable input bit. The address of the input bit is located in the memory double word MD2. |
| = DIX [DBD 2] | // Assign the RLO to a variable data bit. The address of the data bit is located in the data double word DBD2. |
| L EB [DID 4] | // Load a variable input byte to ACCU 1. The address of the input byte is located in the instance double word DID4. |
| AUF DB [LW 2] | // Open a variable data block. The number of the data block is located in the local data word LW2. |
|  |  |

###### Register-indirect area-internal addressing

Register-indirect addressing uses one of the address registers (AR1 or AR2) to pick up the address of the operand.

In the case of register-indirect, area-internal addressing, you index only the bit address and the byte address via the address register (e.g. `P#10.0`). You do not enter the memory area for which the address in the address register is to apply until during programming of the instruction. The address in the address register then moves to the memory area specified in the instruction.

Possible memory areas are "Inputs" (I), "Outputs" (Q), "I/O" (PI or PQ), "Bit memory" (M), "Temporary local data" (L) and "Data" (DB or DI). If the operand is located in a data block, it must be a data black with standard access.

When you enter register-indirect, area-internal addressing, specify an offset after the specification of the address register. This offset is added to the contents of the address register without changing the address register. This offset also has the format of a pointer. The specification of a pointer is mandatory and must be entered as constant (e.g. `P#0.0` or `P#2.0`).

The following example shows an application of register-indirect area-internal addressing:

| STL | Explanation |
| --- | --- |
| LAR1 P#10.0 | // Load pointer (P#10.0) to address register 1 |
| L IW [AR1, P#2.0] | // Increase contents of address register 1 (P#10.0) by offset P#2.0.   // Load contents of input word IW12 into accumulator 1 |
| L IW [AR1, P#0.0] | // Increase contents of address register 1 (P#10.0) by offset P#0.0.   // Load contents of input word IW10 into accumulator 1 |
|  |  |

###### Register-indirect cross-area addressing

In the case of register-indirect, cross-area addressing, use the address register to index the entire address of the operand, in other words, the bit address and byte address, as well as the memory area. Possible memory areas are "Inputs" (I), "Outputs" (Q), "I/O" (P), "Bit memory" (M), "Temporary local data" (L) and "Data" (DB or DI). If the operand is located in a data block, it must be a data black with standard access or the operand must have the retain setting "Set in IDB".

In the instruction, program only the operand width. Possible operand widths are bit, byte, word, and double word.

The following example shows an application of register-indirect cross-area addressing:

|  |  |
| --- | --- |
| LAR1 P#M10.0 | // Load cross-area pointer (P#M10.0) to address register 1 |
| L W [AR1, P#2.0] | // Increase contents of address register 1 (P#M10.0) by offset P#2.0.  // Load contents of memory word "MW12" into accumulator 1 |
| LAR1 P#A10.0 | // Load cross-area pointer (P#A10.0) to address register 1 |
| L W [AR1, P#2.0] | // Add contents of address register 1 (P#A10.0) by offset P#2.0  // Load contents of output word QW12.0 into accumulator 1 |

> **Note**
>
> **Special features in S7-1500**
>
> In S7-1500, special rules apply to data exchange via address register and data block register:
>
> - The values in the registers do not remain in existence beyond the block limits. The registers are also reset when the language is changed within a block.
> - If you access an operand of the BYTE, WORD or DWORD type using register-indirect addressing, the address must begin at a byte limit.
>
>   Examples:
>
>   LAR1 P#0.0   
>   L MW [AR1, P#0.0] // P#0.0 + P#0.0 = P#0.0 - The addressing is allowed, because P#0.0 points to a byte limit.   
>   L MW [AR1, P#2.1] // P#0.0 + P#2.1 = P#2.1 - The addressing is not allowed, because P#2.1 does not point to a byte limit.

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Indirect addressing of data blocks (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-of-data-blocks-s7-300-s7-400)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)
  
[Basic information about address registers (S7-1500)](#basic-information-about-address-registers-s7-1500)
  
[Data exchange in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#data-exchange-in-stl-s7-300-s7-400-s7-1500)

## Serializing structures for data exchange

This section contains information on the following topics:

- [Padding bytes when using structured data types](#padding-bytes-when-using-structured-data-types)

### Padding bytes when using structured data types

#### Padding bytes in non-optimized memory area

Structured data types are aligned in the non-optimized memory area to an even start address (divisible by 2).

If, due to previous data types, the start address of the structured data type falls on an odd address or the end address on an even address, a padding byte is automatically inserted at the relevant position.

If, for example, an array with a length of seven BYTES follows three single BYTES in a data block, a padding byte is inserted automatically both before the array and after the array. The first three BYTES are located, for example, at the addresses "0.0" to "2.0". The subsequent array is then located at the addresses "4.0" to "10.0". A single BYTE that follows would get the address "12.0".

The padding bytes are not visible in the data storage (e.g. in the DB), but have an effect when structures are copied.

If a structured data type of pre-defined form and size is to be transferred between a SIMATIC CPU and an external device, this is done in accordance with the rules for the non-optimized data storage.

#### Padding bytes in an optimized memory area

Depending on the target system, different calculation rules for padding bytes apply to the optimized memory area.

> **Note**
>
> **You can find more information on optimized and non-optimized data storage in the following article at Siemens Industry Online Support:**
>
> Programming Guideline
>
> ![Padding bytes in an optimized memory area](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/90885040](https://support.industry.siemens.com/cs/ww/en/view/90885040)

#### Padding bytes when structured data types are copied

When copying a structured data type composed of elementary data types, a distinction is made whether the same set of rules for the calculation of padding bytes applies to source and target.

- If the same set of rules apply for the source and target, the memory area is copied as a whole, meaning that all the padding bits and padding bytes between the tags are copied as well.
- Otherwise each elementary tag has to be copied individually. In this case, the values of the padding bits and padding bytes remain unchanged in the target. Only the padding bits of Arrays of Bool are also copied.

#### Example scenarios in which padding bytes become visible

The following table shows some scenarios in which padding bytes can become visible:

| Data types | Examples of instructions | Example scenarios |
| --- | --- | --- |
| - Struct - PLC data types - Array | - [Serialize](LAD%20%28S7-1200%2C%20S7-1500%29.md#serialize-serialize-s7-1200-s7-1500), [Deserialize](LAD%20%28S7-1200%2C%20S7-1500%29.md#deserialize-deserialize-s7-1200-s7-1500), - [WRREC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#wrrec-write-data-record-s7-1200-s7-1500-1), [RDREC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rdrec-read-data-record-s7-1200-s7-1500-1), - [TSEND_C](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1), [TRCV_C](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1), [PUT](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#put-write-data-to-a-remote-cpu-s7-1200-s7-1500), [GET](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#get-read-data-from-a-remote-cpu-s7-1200-s7-1500) - [MoveResovledSymbolsToBuffe](SCL%20%28S7-1200%2C%20S7-1500%29.md#moveresolvedsymbolstobuffer-read-values-from-resolved-symbols-and-write-them-into-buffer-s7-1500)r, [MoveResolvedSymbolsFromBuffer](SCL%20%28S7-1200%2C%20S7-1500%29.md#moveresolvedsymbolsfrombuffer-read-values-from-buffer-and-write-them-into-resolved-symbols-s7-1500) | - Structures with structured elements - I/O (manufacturer specific data records) - Structure in the address space of I/O devices - Communication with I/O from other manufacturers - Using hardware under Linux - Driver of a device |

#### Example of a problem case in the standard memory area

You have created the following nested structure as the "typeHARTrequest" PLC data type for sending to an external device as a data record. (See green border.)

![Example of a problem case in the standard memory area](images/128293316619_DV_resource.Stream@PNG-de-DE.png)

Problem: The PLC data type "typeHARTrequest" apparently has a length of 11 bytes. Several odd lengths in bytes also result in padding bytes within the PLC data type. (See red markings.) Including all padding bytes, the PLC data type has a length of 14 bytes for data exchange. The addressed address ranges of the SIMATIC CPU will therefore not match those of the external device for data exchange.

Solution: You change the array marked blue into five single bytes. The new "typeHARTrequest" PLC data type then has a length of 12 bytes (including the padding byte at the end).

---

**See also**

[Basic information on ARRAY](Data%20types.md#basic-information-on-array)
  
[Basic information on STRUCT](Data%20types.md#basic-information-on-struct)

## Handling program execution errors

This section contains information on the following topics:

- [Causes of error](#causes-of-error)
- [Overview of mechanisms for error handling](#overview-of-mechanisms-for-error-handling)
- [EN/ENO mechanism](#eneno-mechanism)
- [Evaluating errors with output parameter RET_VAL](#evaluating-errors-with-output-parameter-ret_val)
- [Use of the instructions GET_ERROR and GET_ERR_ID](#use-of-the-instructions-get_error-and-get_err_id)
- [Example of how to handle program execution errors](#example-of-how-to-handle-program-execution-errors)

### Causes of error

#### Introduction

There are different causes for various error qualities in TIA Portal to which you can respond with different mechanisms.​ These mechanisms with which you can react to an error are independent of the programming languages. Only the display of the individual mechanisms depends on the respective programming language.

The situation determines what counts as an error. The overflow in the case of an addition, for example, can be an error because it does not return the desired result. In some cases, however, the addition overflow is acceptable and defined behavior and therefore not an error.

When creating a program code, you must be aware that certain situations may arise. When you program communication, for example, you must be aware that this connection can be canceled at any time. To be prepared for this situation, you must install a corresponding fault reaction because any connection abort prevents the T_SEND program block from transmitting a message. This is why it is important that the connection abort is signaled to inform the operator that the message can no longer be transmitted. Because the instruction T_SEND cannot prevent the connection abort, the error output is the correct behavior for T_SEND. Ignoring this output can be interpreted as an error made by the programmer.

Below, we will always refer to an error even if it is defined behavior.

#### Different causes for an error

We can distinguish between the following causes for an error:

|  | Faulty parameter values | Faulty programming | Failure of resources |
| --- | --- | --- | --- |
| Description | Errors that are dealt with directly in the instruction. | Programming or access errors that result in the execution of an instruction being aborted. | Errors that are handled by the operating system and for which you can program a reaction in the program code. |
| Error quality | Handled error | Synchronous error | Asynchronous error |
| Example | Overflow of an arithmetic instruction | Faulty programming:  - Querying a non-existent peripheral input - When accessing an ARRAY by means of a variable index, the value of the index is located outside the valid ARRAY limits | Occurrence of a specific event outside the program code. |
| Reaction of the program or operating system | Instructions that are linked with the enable output ENO are not executed. | If you have not programmed an error OB, the operating system response depends on the CPU. | 1. If an organization block (OB) is not assigned to the event, the operating system executes the default system response when the event occurs. 2. If an organization block (OB) is assigned to the event, it is called. |
| Mechanisms for error handling in the program | Depending on the instruction, you have different local error handling options <sup>2)</sup>:  - EN/ENO mechanism - The output parameters:   - RET_VAL   - STATUS   - ERROR | Global error handling <sup>1)</sup>:  - Program execution error OB - Programming error OB - I/O access error OB   Local error handling <sup>2)</sup> with the instructions:  - GET_ERROR - GET_ERR_ID | Error organization blocks (OB):  - Time error (OB 80) - Diagnostic interrupt (OB 82) - Insert/remove module interrupt (OB 83) - Rack error (OB 86)   Possible system responses without assigned error OB:  - The event is ignored by the operating system. - The CPU changes to STOP mode. - If possible, the error handling takes place locally.   If an error OB has been assigned, it will be called in case of a corresponding event.  An application example for diagnostics in the user program [With evaluation of the errors in the error OBs](https://support.industry.siemens.com/cs/document/98210758?lc=en-WW) |
| <sup>1)</sup> You implement global error handling with the help of organization blocks.   <sup>2)</sup> You program local error handling within your program code. |  |  |  |

> **Note**
>
> **Asynchronous error handling**
>
> For a CPU of the S7-1500 series, the error OBs are called asynchronously. This means I/O access errors or programming error OBs may not be processed immediately when the error occurs, but delayed depending on the set priority. If additional errors occur before the I/O access error or the programming error OB was processed completely, no additional I/O access error or programming error OB is called. If you want to prevent I/O access or programming error OBs from being discarded, set the priority correspondingly high.

---

**See also**

[Example of how to handle program execution errors](#example-of-how-to-handle-program-execution-errors)

### Overview of mechanisms for error handling

#### Overview

There are different mechanisms by which you can track parameter, programming or access errors:

| Mechanism | Task | Error handling |
| --- | --- | --- |
| Enable input EN or IF instruction | Prevent execution of a program code | Local |
| Enable output ENO or binary result bit | Indicate an error |  |
| Parameter outputs RET_VAL, STATUS and ERROR |  |  |
| GET_ERROR and GET_ERR_ID instructions | Respond to an error |  |
| Organization blocks | Global |  |

#### Local error handling in the case of faulty parameter values

Not only does local error handling let you react to an error immediately after it has occurred, you can also get a specific reaction within your program code. You program the local error handling directly in a program block (OB, FB or FC). It only handles errors that occur within this individual program block.

Advantages of local error handling:

- You can use the error information to program a reaction to the error that occurred in the program block.
- Programmed error evaluation and error reactions do not interrupt the program cycle.
- System performance is not unnecessarily affected by local error handling. If no errors occur, programmed error analyses and reactions are not executed.

The following local error handling options are available:

| Error handling method | Validity | Explanation |
| --- | --- | --- |
| EN/ENO mechanism <sup>1)</sup> | S7-300 / S7-400 / S7-1200 / S7-1500 | You can detect and handle specific runtime errors with the help of the enable output ENO. Execution of subsequent instructions depends on the signal state of the enable output. You can avoid program crashes by using the EN/ENO mechanism. The block status is passed on in the form of a Boolean tag.  For additional information on the EN/ENO mechanism, refer to: [Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism) |
| Output parameters STATUS and ERROR | S7-300 / S7-400 / S7-1200 / S7-1500 | Using the STATUS and ERROR parameters as return values of system function blocks (SFBs), you can query block-specific error information. The error information is output in a pre-defined structure.  For further information on the output parameters, refer to the descriptions of the individual instructions in the information system. |
| Output parameter RET_VAL | S7-300 / S7-400 / S7-1200 / S7-1500 | You can display general error codes or specific error codes with the help of the output parameter RET_VAL as return value of sequential functions (SFCs). The general error codes refer to any instruction and the specific error codes refer only to a specific instruction. A maximum of one tag of the data type INT or WORD can be output.  Additional information on the output parameter RET_VAL is available here:   [Evaluating errors with output parameter RET_VAL](#evaluating-errors-with-output-parameter-ret_val) |
| <sup>1)</sup> If the parameters of an instruction did not cause any memory access errors, the associated enable output ENO returns the signal state "1" and the outputs return valid values which you can query. |  |  |

#### Global and local error handling in the case of faulty programming

With the global and local error handling, you can react immediately to errors that have occurred without the CPU changing to "STOP" mode. The following options are available for handling programming and access errors:

| Type of global error handling | Validity | Explanation |
| --- | --- | --- |
| Program execution error OB (OB 85) | S7-300 / S7-400 | If you are not using OB 85, the CPU changes from RUN mode to STOP mode in case of a program execution error and generates an entry in the diagnostics buffer.  Additional information on OB 85 ​​can be found here: [Priority class error organization block (OB 85)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#priority-class-error-organization-block-ob-85-s7-300-s7-400) |
| CPU internal error handling in case of programming and access errors | S7-1200 | In the event of an error, the CPU generates an entry in the diagnostics buffer and remains in RUN mode without additional programming effort. |
| Programming error OB (OB 121) | S7-300/ S7-400 / S7-1500 | If you are not using OB 121, the CPU changes from RUN mode to STOP mode in the case of a programming error and generates an entry in the diagnostics buffer.  Additional information on OB 121 ​​can be found here:  S7-300 / S7-400:   [Programming error organization block (OB 121)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#programming-error-organization-block-ob-121-s7-300-s7-400)   S7-1500:   [Programming error OB](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#programming-error-ob-s7-1500)​ |
| I/O access error OB (OB 122) | S7-300/ S7-400 / S7-1500 | S7-300 / S7-400:  If you are not using OB 122, the CPU changes from RUN mode to STOP mode in the case of an access error.   [I/O access error organization block (OB 122)](Organization%20blocks%20%28S7-300%2C%20S7-400%29.md#io-access-error-organization-block-ob-122-s7-300-s7-400)   S7-1500:  In the case of an I/O access error, the CPU always remains in RUN mode and generates an entry in the diagnostics buffer, even if you have not used OB 122.​  Additional information on OB 122 ​​can be found here: [I/O access error OB](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#io-access-error-ob-s7-1500)​ |
| Additional information on reading out the diagnostics buffer ​​can be found here:[Reading out the diagnostics buffer of a CPU](Device%20and%20network%20diagnostics.md#reading-out-the-diagnostics-buffer-of-a-cpu) |  |  |

You can integrate local error handling directly in your program code with the help of the GET_ERROR and GET_ERR_ID instructions. You also have the option of receiving detailed information on the error and evaluating it in your program close to the error location. You program the local error handling directly in a program block (OB, FB or FC). It only handles errors that occur within this individual program block.

| Type of local error handling | Validity | Explanation |
| --- | --- | --- |
| GET_ERROR and GET_ERR_ID instructions | S7-1200/S7-1500 | The instructions give you the opportunity to obtain an error ID or detailed error information and to program a direct response in the program code.  When information about the first error is queried, the memory space of the error in the system memory is enabled again. Then, when additional errors occur, information about the next error is output.   Additional information on the GET_ERROR and GET_ERR_ID instructions and an overview for prioritizing the errors that occur is available here: [Use of the instructions GET_ERROR and GET_ERR_ID](#use-of-the-instructions-get_error-and-get_err_id) |

When using local error handling, query via the GET_ERROR instruction, the following default reactions exist:

- In the case of a write error: The error is ignored and processing of the program continues.
- In the case of a read error: Processing of the program continues with the substitute value "0" for arithmetic instructions.
- In the case of an execution error: Processing of the instruction is canceled and processing of the program continues with the next instruction.

Advantages of local error handling:

- Error information that you can query and evaluate is stored in the system memory (e. g. with the help of the GET_ERROR and GET_ERR_ID instructions).
- You can use the error information to program a reaction to the error that occurred in the program block.
- Programmed error evaluation and error reactions do not interrupt the program cycle.
- Local error handling has a lower effect than global error handling on the system performance. If no errors occur, programmed error analyses and reactions are not executed.
- If local error handling has been set for a program block, no global error handling is conducted in the case of errors.

> **Note**
>
> To prevent the CPU from switching to STOP mode in the case of an error, all programming and I/O access errors must be captured either by global or local error handling.

#### Example

A detailed example of local error handling that contains several of the above described options is available here: [Example of how to handle program execution errors](#example-of-how-to-handle-program-execution-errors)

---

**See also**

[EN/ENO mechanism](#eneno-mechanism)

### EN/ENO mechanism

This section contains information on the following topics:

- [Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)
- [EN/ENO mechanism in LAD](#eneno-mechanism-in-lad)
- [EN-/ENO mechanism in FBD](#en-eno-mechanism-in-fbd)
- [EN/ENO mechanism in STL (S7-1500)](#eneno-mechanism-in-stl-s7-1500)
- [EN/ENO mechanism in SCL](#eneno-mechanism-in-scl)
- [EN/ENO mechanism in GRAPH (S7-1500)](#eneno-mechanism-in-graph-s7-1500)
- [EN/ENO mechanism in blocks with different network languages (S7-1200, S7-1500)](#eneno-mechanism-in-blocks-with-different-network-languages-s7-1200-s7-1500)

#### Basics of the EN/ENO mechanism

##### Introduction

You can detect and handle certain runtime errors using the enable output ENO. Execution of subsequent instructions depends on the signal state of the enable output. You can avoid program crashes by using the EN/ENO mechanism. The block status is passed on in the form of a Boolean tag.

The EN/ENO mechanism can be used at two levels:

- For individual instructions (instruction ENO)

  ![Introduction](images/94667230347_DV_resource.Stream@PNG-de-DE.png)
- For program block calls (block ENO)

  ![Introduction](images/94678080779_DV_resource.Stream@PNG-de-DE.png)

The EN/ENO mechanism is already available in LAD and FBD for calling the simple and advanced instructions in the program code.

With the EN/ENO mechanism you can influence the calling of the following instructions and customize the jumping out from a program block using the instruction "RET: Return". At the same time you can also assign an individual value (0 or 1) to the enable output ENO of the program block. This behavior is generally used for LAD and FBD program blocks. You can also use this procedure for SCL program blocks. You do not necessarily have to use the instruction "RET" to influence the enable output ENO of the SCL program block.

At the network borders the enable output is repeatedly set to the signal state "1". In a LAD program block you can recognize this, for example, by the fact that the left busbar always supplies current, even when the enable output ENO of the last instruction of the previous network returns the signal state "0".

##### Function of the instruction "RET: Return" (LAD/FBD)

When the result of logic operation = 0 the instruction is not executed and the next network is processed.

When the result of logic operation = 1 the instruction is executed and a return to the calling program block takes place.

The signal state of the block ENO can be determined with four options:

- RLO: RLO = 1 is applied, i.e. the block ENO is set to TRUE.
- TRUE: The block ENO is set to TRUE.
- FALSE: The block ENO is set to FALSE.
- Operand: The signal state of the specified operand determines the block ENO.

##### Programming and I/O access errors

You cannot evaluate programming and I/O access errors with the EN/ENO mechanism. To do this, use either the global error handling via OBs or the local error handling using the "GET_ERROR" or "GET_ERR_ID" instructions (S7-1200/1500 only). If none of the errors occurred for an instruction, you can evaluate the associated enable output ENO.

##### Program block calls in all programming languages (S7-300/400)

The following applies to a CPU of the S7-300/400 series: When you call program blocks that do not include any instructions, neither the BR bit nor the ENO enable output are influenced. The signal state of the BR bit remains constant as a result. No statement can be made about the success of the program block call.

#### EN/ENO mechanism in LAD

This section contains information on the following topics:

- [Overview of the EN/ENO mechanism in LAD](#overview-of-the-eneno-mechanism-in-lad)
- [Enabling and disabling the EN/ENO mechanism in LAD and FBD](#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)
- [Influencing the block ENO of an LAD/FBD program block](#influencing-the-block-eno-of-an-ladfbd-program-block)
- [Example of the use of the EN/ENO mechanism in LAD](#example-of-the-use-of-the-eneno-mechanism-in-lad)

##### Overview of the EN/ENO mechanism in LAD

To increase the performance, the EN/ENO mechanism is disabled by default for the instructions. It can be enabled at any time also for individual instructions. For additional information on the enabling and disabling of the EN/ENO mechanism, refer to: [Enabling and disabling the EN/ENO mechanism in LAD and FBD](#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd)

For LAD/FBD program block the EN/ENO mechanism only works with an activated enable output ENO at the respective instructions.

###### EN/ENO mechanism within an instruction.

You can use the enable input EN to make the execution of the instruction dependent on conditions. The instruction is only executed if the signal state at the enable input EN is "1".

You can use the enable output ENO to query runtime errors in an instruction and react to these:

- The enable output ENO has the signal state "1" if no error occurred during the execution.
- Enable output ENO has the signal state "0" if one of the following conditions applies:

  - Enable input EN has the signal state "0".
  - An error occurred during processing.

###### EN/ENO mechanism with program block calls

All program block calls are provided with an enable input EN and an enable output ENO. This applies to all calling program blocks, regardless of the programming language in which they were created. This means that when you call an STL or SCL program block in which there is no default and pre-configured EN/ENO mechanism, the LAD or FBD program block call still has an EN/ENO mechanism.

You can use the enable input EN to call a program block depending on conditions. The program block is only executed if the signal state at the enable input EN is "1".

You can query the error status of the program block using the enable output ENO:

- The enable output ENO returns the signal state "1" when the program block is processed.
- If, in the case of error, you do not explicitly set the enable output ENO within the called program block to the signal state "0", it retains the signal state "1". Using the instruction "RET: Return" you can set the block ENO to the signal state "0".

  Additional information on using the RET instruction is available here: [Influencing the block ENO of an LAD/FBD program block](#influencing-the-block-eno-of-an-ladfbd-program-block)

##### Enabling and disabling the EN/ENO mechanism in LAD and FBD

In LAD and FBD, certain instructions have an enable output ENO and thus use the EN/ENO mechanism. This allows you to query runtime errors in instructions and react to them. In order to increase the performance of the CPU, the EN/ENO mechanism is disabled in the default setting. This means that you are not initially able to react to runtime errors of the instruction using the ENO value. However, you can enable the EN/ENO mechanism again at any time, if required.

You can enable the EN/ENO mechanism individually for each instruction in order to generate the ENO. If you enable the EN/ENO mechanism for an instruction, other instructions that you subsequently add to your program are also inserted with the EN/ENO mechanism enabled. You can disable the EN/ENO mechanism again at any time if you do not want to use the evaluation of ENO for an instruction. Further instructions that you subsequently add to your program will then be inserted without the EN/ENO mechanism.

Runtime errors do not cause the CPU to go to STOP when the enable output ENO is enabled.

###### Activating the EN/ENO mechanism

Proceed as follows to activate the EN/ENO mechanism of an instruction:

1. In your program, right-click the instruction at which you want to activate the EN/ENO mechanism.
2. Select the "Generate ENO" command from the shortcut menu.

   The ENO value is again generated for the instruction. Additional instructions are then also inserted with the activated enable output.

###### Deactivating the EN/ENO mechanism

Proceed as follows to deactivate the EN/ENO mechanism of an instruction:

1. In your program, right-click the instruction at which you want to deactivate the EN/ENO mechanism.
2. Select the "Do not generate ENO" command from the shortcut menu.

   The ENO value is no longer generated for the instruction. Additional instructions are then also inserted without the activated enable output.

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

##### Influencing the block ENO of an LAD/FBD program block

###### Description

Using the instruction "RET: Return" you jump out from a program block and hereby influence the signal state of the ENO block.

###### Procedure

To influence the signal state of the block ENO, follow these steps:

1. Enable the EN/ENO mechanism of an instruction (for example, the addition "ADD").
2. Then use a negation to program the instruction "RET: Return" with signal state FALSE at the enable output ENO.

###### Result

In case of error (for example, an overflow in the result), the signal state "0" is first returned at the enable output ENO. This signal state "0" becomes signal state "1" using the negation and thus forms the RLO = 1 for executing the instruction "RET", which returns the value FALSE. The block ENO of the program block is hereby FALSE and a return takes place from the program block to the next instruction after the previous program block call. This procedure can be programmed in each network (for example, with multiple mathematical functions etc.).

However, it is not compulsory to program a jump out of the program block. Within a network you can also use the signal state "0" of the enable output ENO of a single instruction to determine that the subsequent instruction is not executed. The block ENO is not hereby influenced.

> **Note**
>
> **Influencing of the block ENO**
>
> You can only influence the signal state of the block ENO by jumping out of the program block.
>
> Even if the enable output ENO of the last instruction in the last network within a program block has the signal state "0", the block ENO is not influenced.

##### Example of the use of the EN/ENO mechanism in LAD

###### Example of an instruction with EN/ENO mechanism

The following example shows the "Add" instruction with EN/ENO circuit and a RET coil (Ret False):

![Example of an instruction with EN/ENO mechanism](images/77201443851_DV_resource.Stream@PNG-de-DE.png)

After the NO contact "TagEnable", the enable input EN contains the result of the preceding logic operation:

- If the operand "TagEnable" has the signal state "0", the "Add" instruction is not executed. The enable output ENO is set to signal state "0" and the called program block is exited. The enable output ENO of the calling program block then also has the signal state "0".
- If the operand "TagEnable" has the signal state "1", the enable input "EN has the signal state "1" and the instruction "Add" is executed. The instruction adds two values of the data type INT. If the expected result is outside the value range of INT (16 bits: -32768 to +32767), the instruction still returns a result but it is within the value range of INT. The reason for this is that the 16th bit for INT is the sign bit. This result does not indicate that there was an overflow. Which is why the following applies in case of an addition =&gt; ENO:= NOT(OV). If an error occurs during processing of the program block, the enable output ENO is set to signal state "0" and the called program block is exited. The enable output ENO of the calling program block then also has the signal state "0".
- If the operand "TagEnable" has the signal state "1", the enable input "EN has the signal state "1" and the instruction "Add" is executed. If the instruction is executed without errors, the enable output ENO also has the signal state "1" and the output "TagResult" the result.

A detailed description of the instruction "RET: Return" is available here: [--(RET): Return](LAD%20%28S7-1200%2C%20S7-1500%29.md#ret-return-s7-1200-s7-1500)

###### Example of the effect of the enable output ENO

The following example shows you how to use instructions with the ENO enable output enabled and disabled:

![Example of the effect of the enable output ENO](images/94798723595_DV_resource.Stream@PNG-de-DE.png)

If you have activated the ENO enable output, for example with the SUB instruction, all subsequent instructions are also applied with an activated ENO enable output. If an arithmetic error occurs during the execution of the SUB instruction, the ADD instruction is not executed.

The ENO enable output is disabled for the DIV instruction in the second branch. If a runtime error occurs during execution, the MUL instruction is executed anyway.

###### Example of a program block call with EN/ENO mechanism

The following example shows the call of the program block with EN/ENO circuit:

![Example of a program block call with EN/ENO mechanism](images/77201968395_DV_resource.Stream@PNG-de-DE.png)

The program block is executed only if the operand "TagEnable" has the signal state "1":

- The enable output ENO has a signal state that depends on what was programmed within the program block.
- If the operand "TagEnable" has the signal state "0", the program block call is not executed. The enable input EN and the enable output ENO both have the signal state "0".

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

#### EN-/ENO mechanism in FBD

This section contains information on the following topics:

- [Overview of the EN/ENO mechanism in FBD](#overview-of-the-eneno-mechanism-in-fbd)
- [Enabling and disabling the EN/ENO mechanism in LAD and FBD](#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)
- [Influencing the block ENO of an LAD/FBD program block](#influencing-the-block-eno-of-an-ladfbd-program-block-1)
- [Example of the use of the EN/ENO mechanism in FBD](#example-of-the-use-of-the-eneno-mechanism-in-fbd)

##### Overview of the EN/ENO mechanism in FBD

To increase the performance, the EN/ENO mechanism is disabled by default for the instructions. It can be enabled at any time also for individual instructions. For additional information on the enabling and disabling of the EN/ENO mechanism, refer to: [Enabling and disabling the EN/ENO mechanism in LAD and FBD](#enabling-and-disabling-the-eneno-mechanism-in-lad-and-fbd-1)

For LAD/FBD program block the EN/ENO mechanism only works with an activated enable output ENO at the respective instructions.

###### EN/ENO mechanism within an instruction.

You can use the enable input EN to make the execution of the instruction dependent on conditions. The instruction is only executed if the signal state at the enable input EN is "1".

You can use the enable output ENO to query runtime errors in an instruction and react to these:

- The enable output ENO has the signal state "1" if no error occurred during the execution.
- Enable output ENO has the signal state "0" if one of the following conditions applies:

  - Enable input EN has the signal state "0".
  - An error occurred during processing.

###### EN/ENO mechanism with program block calls

All program block calls are provided with an enable input EN and an enable output ENO. This applies to all calling program blocks, regardless of the programming language in which they were created. This means that when you call an STL or SCL program block in which there is no default and pre-configured EN/ENO mechanism, the LAD or FBD program block call still has an EN/ENO mechanism.

You can use the enable input EN to call a program block depending on conditions. The program block is only executed if the signal state at the enable input EN is "1".

You can query the error status of the program block using the enable output ENO:

- The enable output ENO returns the signal state "1" when the program block is processed.
- If, in the case of error, you do not explicitly set the enable output ENO within the called program block to the signal state "0", it retains the signal state "1". Using the instruction "RET: Return" you can set the block ENO to the signal state "0".

  Additional information on using the RET instruction is available here: [Influencing the block ENO of an LAD/FBD program block](#influencing-the-block-eno-of-an-ladfbd-program-block-1)

##### Enabling and disabling the EN/ENO mechanism in LAD and FBD

In LAD and FBD, certain instructions have an enable output ENO and thus use the EN/ENO mechanism. This allows you to query runtime errors in instructions and react to them. In order to increase the performance of the CPU, the EN/ENO mechanism is disabled in the default setting. This means that you are not initially able to react to runtime errors of the instruction using the ENO value. However, you can enable the EN/ENO mechanism again at any time, if required.

You can enable the EN/ENO mechanism individually for each instruction in order to generate the ENO. If you enable the EN/ENO mechanism for an instruction, other instructions that you subsequently add to your program are also inserted with the EN/ENO mechanism enabled. You can disable the EN/ENO mechanism again at any time if you do not want to use the evaluation of ENO for an instruction. Further instructions that you subsequently add to your program will then be inserted without the EN/ENO mechanism.

Runtime errors do not cause the CPU to go to STOP when the enable output ENO is enabled.

###### Activating the EN/ENO mechanism

Proceed as follows to activate the EN/ENO mechanism of an instruction:

1. In your program, right-click the instruction at which you want to activate the EN/ENO mechanism.
2. Select the "Generate ENO" command from the shortcut menu.

   The ENO value is again generated for the instruction. Additional instructions are then also inserted with the activated enable output.

###### Deactivating the EN/ENO mechanism

Proceed as follows to deactivate the EN/ENO mechanism of an instruction:

1. In your program, right-click the instruction at which you want to deactivate the EN/ENO mechanism.
2. Select the "Do not generate ENO" command from the shortcut menu.

   The ENO value is no longer generated for the instruction. Additional instructions are then also inserted without the activated enable output.

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

##### Influencing the block ENO of an LAD/FBD program block

###### Description

Using the instruction "RET: Return" you jump out from a program block and hereby influence the signal state of the ENO block.

###### Procedure

To influence the signal state of the block ENO, follow these steps:

1. Enable the EN/ENO mechanism of an instruction (for example, the addition "ADD").
2. Then use a negation to program the instruction "RET: Return" with signal state FALSE at the enable output ENO.

###### Result

In case of error (for example, an overflow in the result), the signal state "0" is first returned at the enable output ENO. This signal state "0" becomes signal state "1" using the negation and thus forms the RLO = 1 for executing the instruction "RET", which returns the value FALSE. The block ENO of the program block is hereby FALSE and a return takes place from the program block to the next instruction after the previous program block call. This procedure can be programmed in each network (for example, with multiple mathematical functions etc.).

However, it is not compulsory to program a jump out of the program block. Within a network you can also use the signal state "0" of the enable output ENO of a single instruction to determine that the subsequent instruction is not executed. The block ENO is not hereby influenced.

> **Note**
>
> **Influencing of the block ENO**
>
> You can only influence the signal state of the block ENO by jumping out of the program block.
>
> Even if the enable output ENO of the last instruction in the last network within a program block has the signal state "0", the block ENO is not influenced.

##### Example of the use of the EN/ENO mechanism in FBD

###### Example of an instruction with EN/ENO mechanism

The following example shows the "Add" instruction with EN/ENO circuit and a RET coil (Ret False):

![Example of an instruction with EN/ENO mechanism](images/77203948555_DV_resource.Stream@PNG-de-DE.png)

After the NO contact "TagEnable", the enable input EN contains the result of the preceding logic operation:

- If the operand "TagEnable" has the signal state "0", the "Add" instruction is not executed. The enable output ENO is set to signal state "0" and the called program block is exited. The enable output ENO of the calling program block then also has the signal state "0".
- If the operand "TagEnable" has the signal state "1", the enable input "EN has the signal state "1" and the instruction "Add" is executed. The instruction adds two values of the data type INT. If the expected result is outside the value range of INT (16 bits: -32768 to +32767), the instruction still returns a result but it is within the value range of INT. The reason for this is that the 16th bit for INT is the sign bit. This result does not indicate that there was an overflow. Which is why the following applies in case of an addition =&gt; ENO:= NOT(OV). If an error occurs during processing of the program block, the enable output ENO is set to signal state "0" and the called program block is exited. The enable output ENO of the calling program block then also has the signal state "0".
- If the operand "TagEnable" has the signal state "1", the enable input "EN has the signal state "1" and the instruction "Add" is executed. If the instruction is executed without errors, the enable output ENO also has the signal state "1" and the output "TagResult" the result.

A detailed description of the instruction "RET: Return" is available here: [RET: Return](FBD%20%28S7-1200%2C%20S7-1500%29.md#ret-return-s7-1200-s7-1500)

###### Example of the effect of the enable output ENO

The following example shows you how to use instructions with the ENO enable output enabled and disabled:

![Example of the effect of the enable output ENO](images/94433791755_DV_resource.Stream@PNG-de-DE.png)

If you have activated the ENO enable output, for example with the SUB instruction, all subsequent instructions are also applied with an activated ENO enable output. If an arithmetic error occurs during the execution of the SUB instruction, the ADD instruction is not executed.

The enable output ENO is disabled for the instruction DIV. If a runtime error occurs during execution, the MUL instruction is executed anyway.

###### Example of a program block call with EN/ENO mechanism

The following example shows the call of the program block with EN/ENO circuit:

![Example of a program block call with EN/ENO mechanism](images/77484209291_DV_resource.Stream@PNG-de-DE.png)

The program block is executed only if the operand "TagEnable" has the signal state "1":

- The enable output ENO has a signal state that depends on what was programmed within the program block.
- If the operand "TagEnable" has the signal state "0", the program block call is not executed. The enable input EN and the enable output ENO both have the signal state "0".

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

#### EN/ENO mechanism in STL (S7-1500)

This section contains information on the following topics:

- [Overview of the EN/ENO mechanism in STL (S7-1500)](#overview-of-the-eneno-mechanism-in-stl-s7-1500)
- [Example of the simulation of the EN/ENO mechanism in STL (S7-1500)](#example-of-the-simulation-of-the-eneno-mechanism-in-stl-s7-1500)

##### Overview of the EN/ENO mechanism in STL (S7-1500)

###### EN/ENO mechanism within an instruction.

The EN/ENO mechanism is not available for individual instructions. It is mapped by language-specific instruction sequences and use of the status word (BR bit).

For additional information on the status word, refer to: [Status word for S7-1500](Program%20flow%20control.md#status-word-for-s7-1500-s7-1500)

Additional information is available here: [Example of the simulation of the EN/ENO mechanism in STL](#example-of-the-simulation-of-the-eneno-mechanism-in-stl-s7-1500)

###### EN/ENO mechanism with program block calls

A program block that you call from an STL program block is not provided with the EN and ENO parameters. Regardless of the programming language in which the program block was created, you can get an error statement to the calling STL program block by using the BR bit of the status word.

You can evaluate the error status of the called program block by linking the BR bit of the status word with the result of logic operation (RLO). The RLO has the signal state "1" as soon as the program block execution of the called program block starts. If you do not explicitly reset the RLO to "0" after the execution of the actions, it retains the signal state "1". To signal an error statement back to the calling program block, you have to explicitly reset the RLO to the signal state "0". The error statement is set with the instructions "SAVE: Save RLO in BR bit" and "JNB: Jump if RLO = 0 and save RLO".

An error analysis of the BR bit is available in STL. The BR bit is the basis for generating the enable output ENO in the programming languages LAD, FBD and SCL.

The value "0" in the BR bit of the status word indicates that an error occurred during an STL program block call (calling program block is an STL program block).

| CPU execution of the instruction | BR bit | Return value | Sign of the integer |
| --- | --- | --- | --- |
| With error(s) | 0 | Less than "0" | Negative  (sign bit is "1") |
| Without error | 1 | Greater than or  equal to "0" | Positive  (sign bit is "0") |

For additional information on the BR bit, refer to: [Evaluating errors with output parameter RET_VAL](#evaluating-errors-with-output-parameter-ret_val)

##### Example of the simulation of the EN/ENO mechanism in STL (S7-1500)

###### Example of a program sequence with EN/ENO mechanism

The following example shows a program section for adding values with EN/ENO mechanism:

| STL | Description |
| --- | --- |
| A "TagEnable" | // Query the signal state of the "TagEnable" operand for "1" and AND with the current RLO. |
| JNB MyLABEL | // Evaluation of the enable input EN  // If RLO = "0", jump to jump label "MyLABEL" and save the current RLO in the BR bit. The following actions are not executed.  // If the RLO = "1", execute the following actions. |
| L "Tag_Input_1" | // Load first value for addition. |
| L "Tag_Input_2" | // Load second value for addition. |
| +I | // Add values |
| T "Tag_Result" | // Transfer sum to the operand "Tag_Result".​ |
| AN OV | // Query whether an overflow has occurred. |
| SAVE | // Transfer signal state of the RLO to the BR bit. |
| CLR | /// Reset RLO to "0" and end logic sequence. |
| MyLABEL: A BR | // Jump label "MyLABEL"  // Query BR bit. |
| = "Tag_Output" | // Assign signal state of the RLO to the "Tag_Output" operand. |

The query of the operand "TagEnable" provides the result of the preceding logic operation (RLO). The instruction "JNB: Jump if RLO = 0 and save RLO" saves the RLO in the BR bit. Additionally, the instruction evaluates the RLO and executes the following actions depending on the signal state:

- If the RLO is "0", the processing of the program is continued at the jump label "MyLABEL" with the query of the BR bit. The addition is not executed. The current RLO is assigned with the operand "Tag_Output".
- If the RLO is "1", the addition is executed. A query of the overflow bit (OV) shows whether an error occurred during the addition. The query result is saved in the BR. The instruction "CLR: Reset RLO to 0" resets the RLO to "0" and ends the logic sequence. The BR bit is then queried and assigned to the operand "Tag_Output". The signal state of the BR bit, and the operand "Tag_Output" shows whether the addition was executed without any error.

###### Example of a program block call with EN/ENO mechanism

The following example shows the call of the program block with EN/ENO circuit:

| STL | Description |
| --- | --- |
| A "TagEnable" | // Query the signal state of the "TagEnable" operand for "1" and AND with the current RLO. |
| JNB MyLABEL | // Evaluation of the enable input EN  // If RLO = "0", jump to jump label "MyLABEL" and save the current RLO in the BR bit. The following actions are not executed.  // If the RLO = "1", execute the following actions. |
| CALL "Block name", "Block name_DB" | // The program block is called. |
| MyLABEL: A BR | // Jump label "MyLABEL"  // Query BR bit and link with the RLO after AND. |
| = "Tag_Output" | // Assign signal state of the RLO to the "Tag_Output" operand. |

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

#### EN/ENO mechanism in SCL

This section contains information on the following topics:

- [Overview of the EN/ENO mechanism in SCL](#overview-of-the-eneno-mechanism-in-scl)
- [Enabling and disabling the property "Set ENO automatically" in SCL](#enabling-and-disabling-the-property-set-eno-automatically-in-scl)
- [Using enable output ENO with SCL instructions](#using-enable-output-eno-with-scl-instructions)
- [Influencing "ENO" of an SCL block](#influencing-eno-of-an-scl-block)
- [Influencing ENO within a block](#influencing-eno-within-a-block)
- [Example for using ENO in SCL](#example-for-using-eno-in-scl)

##### Overview of the EN/ENO mechanism in SCL

In SCL networks, you can influence the ENO by assigning a value. To do so, write "ENO:=TRUE" or "ENO:=FALSE" or use a tag of the data type BOOL. When you activate the block property "Set ENO automatically", the compiler adds program code to calculate the ENO like in the programming languages LAD and FBD. This additional program code increases the runtime which is why the property "Set ENO automatically" is disabled by default.

You can find additional information under: "Enabling and disabling the property "Set ENO automatically" in SCL"

In SCL networks, you cannot assign a value to the EN parameter of an FC. This can be remedied by calling the FC conditionally, which means placing it in an "IF" instruction. This means the block call is not executed and does not influence the ENO. This behavior is different than the behavior in the programming languages LAD and FBD.

You can find additional information under: "Influencing ENO of an SCL block"

###### Using ENO

Use of the ENO is optional for instructions.

Additional information is available here: [Using enable output ENO with SCL instructions](#using-enable-output-eno-with-scl-instructions)

---

**See also**

[Enabling and disabling the property "Set ENO automatically" in SCL](#enabling-and-disabling-the-property-set-eno-automatically-in-scl)
  
[Influencing ENO within a block](#influencing-eno-within-a-block)
  
[Influencing "ENO" of an SCL block](#influencing-eno-of-an-scl-block)

##### Enabling and disabling the property "Set ENO automatically" in SCL

###### Description

When the property "Set ENO automatically" is set to "TRUE", the value of the ENO of the called block is forwarded to the ENO of the calling block.

###### Enabling ENO mechanism in the block properties

You enable the property "Set ENO automatically" in the block properties as follows:

1. Open the "Program blocks" folder in the project navigator.
2. Right-click the SCL block whose properties you want to display.
3. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the block opens.
4. Click the "Attributes" group in the area navigation.
5. Activate the property "Set ENO automatically".
6. Confirm your entries with "OK".

Result: The property "Set ENO automatically" is only enabled for the selected block.

###### Setting the property "Set ENO automatically" to "TRUE" for all new program blocks

You enable the property "Set ENO automatically" in the program properties as follows:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the working area.
2. In the area navigation, select the "PLC programming" group.
3. Select the group "SCL (Structured Control Language)".
4. Activate the property "Set ENO automatically".

Result: The property "Set ENO automatically" is enabled for all new program blocks.

##### Using enable output ENO with SCL instructions

###### Description

With each SCL instruction, such as a mathematical function, you must query the enable output ENO in order to be able to work with it.

###### Procedure

To query the enable output ENO, proceed as follows:

1. Activate the EN/ENO mechanism.
2. After the SCL instruction, query the enable output ENO (for example, #MyOutputBool := ENO;)

   If the error case occurs, for example an overflow in the result, returns the enable output ENO returns the signal state "0". With this signal state you can continue to work and, for example, program the instruction "RETURN", a fault display or a substitute value.
3. Reset the signal state of the enable output ENO to "1" (for example, ENO :=1;) before processing the next instruction.

   The signal state for the next error case can hereby be reset to "0". If you do not do this, the signal state of the enable output ENO remains "0".

> **Note**
>
> **Jump to an SCL block.**
>
> With a jump to an SCL block, the signal state of the enable output ENO is automatically set to "1".

##### Influencing "ENO" of an SCL block

###### Description

The last assignment of an ENO within an SCL program block is the ENO of the block. You can also exit the program block and assign the value "TRUE" or "FALSE" to the ENO of the block at the same time by using the "RETURN" instruction.

###### Procedure

You influence the signal state of the ENO of the block as follows:

1. Activate the ENO mechanism.
2. Then program:

   `IF #n := 0 THEN`

   `RETURN FALSE;`

   `END_IF;`

###### Result

When the local tag "#n" is "0", the system returns to the calling block. The ENO of the block has the value "FALSE" in this case.

However, it is not mandatory to program a RETURN. The SCL compiler forwards the value of the current ENO to the ENO of the block. This means the last executed assignment of the ENO will come from the ENO of the block.

##### Influencing ENO within a block

The ENO value can be influenced by the assignment "ENO:=TRUE" or "ENO:=FALSE" or a tag of the data type BOOL. When you activate the block property "Set ENO automatically" (TRUE), the ENO is also influenced when calling a block or an instruction.

##### Example for using ENO in SCL

###### Setting example for ENO

The following example shows an SCL block which checks prior to a division whether the divisor is 0. In this case, ENO is set to the value "FALSE" and the subsequent division is not performed. A calling block can evaluate the ENO of the called block and decide whether the program is to be continued or not.

IF #Divisor = 0 THEN

ENO:=false;

RETURN;

END_IF;

#Quotient:=Dividend/Divisor;

###### Example for calling a program block with ENO mechanism

The following example shows the call of a program block (A) which handles the ENO of a called block (B).

"BlockName_DB"( ENO =&gt; ENO );

IF ENO = false THEN

RETURN;

END_IF;

The program block (A) is called and processed. The called program block (B) reflects the value of its ENO in the process. The value of the ENO of the called block (B) is copied to the ENO of the calling block (A). This ENO is subsequently used in an "IF" instruction.

When the called block (B) returns the signal state "ENO=FALSE", the calling block (A) does not continue with processing and also returns the signal state "ENO=FALSE".

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

#### EN/ENO mechanism in GRAPH (S7-1500)

This section contains information on the following topics:

- [Overview of the EN/ENO mechanism in GRAPH (S7-1500)](#overview-of-the-eneno-mechanism-in-graph-s7-1500)
- [Activating and deactivating EN/ENO mechanism in GRAPH (S7-1500)](#activating-and-deactivating-eneno-mechanism-in-graph-s7-1500)
- [Example of the EN/ENO mechanism in GRAPH (S7-1500)](#example-of-the-eneno-mechanism-in-graph-s7-1500)

##### Overview of the EN/ENO mechanism in GRAPH (S7-1500)

###### EN/ENO mechanism within an instruction.

You have no access to the enable output ENO of the instructions, which means you cannot influence the status of the enable output ENO at the GRAPH function block. However, with conversions, mathematical functions or LAD/FBD instructions, for example, you can have the enable output ENO displayed in the program status.

###### EN/ENO mechanism with program block calls

You can use the enable input EN to call a program block depending on conditions. The program block is only executed if the signal state at the enable input EN is "1".

You can query the error status of the program block using the enable output ENO:

- The enable output ENO has the signal state "1", as soon as the called program block has been executed error-free.
- The enable output ENO has the signal state "0" if an error occurred during the execution of the called program block.
- The enable output ENO cannot be explicitly set or reset.
- The enable output ENO is not influenced by the ENO of the instructions.

##### Activating and deactivating EN/ENO mechanism in GRAPH (S7-1500)

###### Description

The status of the enable output ENO is displayed during testing with program status. This has the value TRUE if the action was successful and FALSE if the action failed.

The display option of the status of the enable output ENO is available at the following positions in the GRAPH program block:

- Permanent pre-instructions
- Sequence view &gt; Actions
- Permanent post-instructions​

###### Enabling EN/ENO mechanism in the block properties

Proceed as follows to activate the EN/ENO mechanism in the block properties:

1. Open the "Program blocks" folder in the project navigator.
2. Right-click the GRAPH block whose properties you want to display.
3. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the block opens.
4. Click the "Attributes" group in the area navigation.
5. Activate the property "Set ENO automatically".
6. Confirm your entries with "OK".

Result: The EN/ENO mechanism is activated only for the selected GRAPH block.

##### Example of the EN/ENO mechanism in GRAPH (S7-1500)

###### Example of a program status with enable output ENO

The following example shows the program status of the enable output ENO in the sequence view under actions:

![Example of a program status with enable output ENO](images/77597472395_DV_resource.Stream@PNG-de-DE.png)

If an error occurs during the execution, the enable output ENO has the signal state FALSE.

###### Example of a program block call

The following example shows the call of the GRAPH program block in a LAD program block with EN/ENO connected:

![Example of a program block call](images/77485843339_DV_resource.Stream@PNG-de-DE.png)

The program block is executed only if the operand "TagEnable" has the signal state "1":

- If the operand "TagEnable" has the signal state "0", the called program block call is not executed. Both the enable input EN and the enable output ENO have the signal state "0".
- If the operand "TagEnable" has the signal state "1", the enable input "EN has the signal state "1" and the called program block is executed. The enable output ENO has a signal state that depends on what was programmed within the program block.

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

#### EN/ENO mechanism in blocks with different network languages (S7-1200, S7-1500)

##### Description

You can also use ​​the EN/ENO mechanism in blocks with different network languages. Each programming language displays the error status differently:

- SCL has an ENO tag that stores the error status and can be queried. Direct access to this tag is only possible with SCL.
- LAD/FBD/STL have no special tag for ENO. However, you can read the error status for STL from the BR bit, and query it via the RET coil for LAD/FBD.

The following rules apply to reading out the error status for the entire block:

- The last network in the block is a LAD/FBD network:

  If you do not use RET coils, the error status is TRUE by default.
- The last network in the block is an STL network:

  The BR bit determines the error status. The BR bit can be edited in STL networks using the BR tab.
- The last network in the block is an SCL network:

  The ENO tag determines the error status of the block.

##### Influencing of the block ENO

For LAD/FBD program blocks with multiple networks that could consist of different programming languages (such as LAD, FBD, STL or SCL), the last processed network determines the signal state of the block ENO.

If the last processed network of such a program block is a LAD or FBD network, the signal state of the block ENO is not necessarily influenced. With an instruction in which the EN/ENO mechanism is activated, it is only influenced if the enable output ENO has the signal state "0" and it is possible to return for the program block using the instruction "RET: Return". If this instruction was not programmed, the block ENO always has the signal state "1". The signal state "0", if any, of an instruction ENO has no influence on the block ENO, as the signal state "1" is always set at the start of a network.

This applies also to a LAD or FBD network that is before another network (LAD, FBD or SCL). The signal state of the block ENO is influenced only using the instruction "RET: Return". Otherwise, the signal state of the block ENO is reset to "1" at the transition to the network.

If the last network of a mixed program block is an SCL network, the block ENO is always influenced by this.

---

**See also**

[Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)

### Evaluating errors with output parameter RET_VAL

#### Basics on error analysis of library blocks (SFB and SFC)

Two additional error evaluation options are available in addition to the output parameter RET_VAL:

- With the EN/ENO mechanism (LAD, FBD, and SCL)

  For more information on the EN/ENO mechanism, refer to: [Basics of the EN/ENO mechanism](#basics-of-the-eneno-mechanism)
- With the BR bit (binary result bit) of the status word (STL)
- With the output parameter RET_VAL (return value)

The enable output ENO only informs you that an error has occurred. If you want to know which error occurred exactly, the output parameter RET_VAL will provide more information. You can use it to determine whether or not the CPU was able to execute the instruction successfully. In the case of an error, you will also learn why the instruction could not be executed successfully.

The section below includes detailed information on the two error evaluation options RET_VAL and BR bit.

#### Recommendation for sequence of error analyses

Before evaluating the instruction-specific output parameters (for example, OUT), you should always follow the steps below:

1. First evaluate the enable output ENO or the BR bit of the status word in STL.
2. Then check the output parameter RET_VAL.

If the enable output ENO or the BR bit indicates that an error has occurred during the execution of the instruction or if output parameter RET_VAL contains a general error code, the instruction-specific output parameters return an invalid value.

If a general error occurs with the output parameter RET_VAL, this is only indicated by the value "0" in the BR bit of the status word. The return value is of the data type integer (INT). The relationship of the return value to the value "0" indicates whether or not an error occurred during execution of the instruction.

#### General and specific error codes (RET_VAL)

The output parameter RET_VAL has two types of error codes:

- A general error code that all instructions can output and
- A specific error code that an instruction can output depending on its specific functions.

The data type of the output parameter RET_VAL is an integer (INT). The error codes of the instruction are grouped according to hexadecimal values. If you want to examine a return value and compare the value with the error codes listed in this documentation, then display the error code in hexadecimal format.

You can write your program so that it reacts to the errors that occur during execution of an instruction. This way you prevent further errors occurring as a result of the first error.

> **Note**
>
> **Error during supply of the input parameters**
>
> When the instruction containing the RET_VAL parameter is executed and errors during supply of the input parameters occur, the RET_VAL parameter outputs an invalid error code and the output parameters of the instruction must not be evaluated.

The figure below shows the structure of a system function error codes in hexadecimal format:

![General and specific error codes (RET_VAL)](images/19487382923_DV_resource.Stream@PNG-en-US.png)

It is easy for you to determine whether an error has occurred because the output parameter RET_VAL is of the type INT:

- If the value is &lt; 0, there is an error.
- If the value is = 0, no error has occurred.
- If the value is &gt; 0, no error has occurred but the instruction was not executed successfully. This is used in asynchronous instructions, for example, to indicate that processing of the instruction was started but is not yet complete. See the return values of T_SEND or WRIT_DBL.

#### General error codes

The general error code indicates errors that can occur in all instructions. A general error code consists of the following two numbers:

- A parameter number from 1 to 111, where 1 indicates the first parameter of the called instruction, 2 the second parameter, and so forth.
- An event number between 0 and 127. The event number indicates an error.

The figure below shows the structure of a general error code:

![General error codes](images/19487837451_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Reaction to a general error code**
>
> If a general error code was entered in the output parameter RET_VAL, the following situations are possible:
>
> - The action associated with the instruction was started or has already been completed.
> - A specific instruction error occurred when the action was performed. As a result of a general error that occurred later, the specific error could, however, no longer be indicated.

The following table explains the general error codes of a return value. The error code is shown in hexadecimal format. The letter x in each code number is simply a placeholder and represents the number of the system function parameter that caused the error:

| Error code  (W#16#...) | Description |
| --- | --- |
| 8x01 | Illegal syntax ID at an VARIANT parameter |
| 8x22 | Range length error when reading a parameter.  This error code indicates that the parameter x is located either entirely or partly outside the range of an address, or that the length of a bit range is not a multiple of 8 with an VARIANT parameter. |
| 8x23 | Range length error when writing a parameter.  This error code indicates that the parameter x is located either entirely or partly outside the range of an address, or that the length of a bit range is not a multiple of 8 with an VARIANT parameter. |
| 8x24 | Range error when reading a parameter.  This error code indicates that the parameter x is located in a range that is illegal for the system function. Refer to the descriptions of the individual functions for information about the illegal ranges. |
| 8x25 | Range error when writing a parameter.  This error code indicates that the parameter x is located in a range that is illegal for the system function. Refer to the descriptions of the individual functions for information about the illegal ranges. |
| 8x26 | The parameter contains a timer cell number that is too high.  This error code indicates that the timer cell specified in parameter x does not exist. |
| 8x27 | The parameter contains a counter cell number that is too high (counter number error).  This error code indicates that the counter cell specified in parameter x does not exist. |
| 8x28 | Alignment error when reading a parameter. |
| 8x29 | Alignment error when writing a parameter.  This error code indicates that the reference to parameter x is an operand with bit address that is not equal to 0. |
| 8x30 | The parameter is located in a read-only global DB. |
| 8x31 | The parameter is located in a read-only instance DB.  This error code indicates that parameter x is located in a read-only data block. If the data block was opened by the system function itself, the system function always returns the value W#16#8x30. |
| 8x32 | The parameter contains a DB number that is too high (DB number error).  This error code indicates that parameter x contains a block number higher than the highest permitted number. |
| 8x34 | The parameter contains an FC number that is too high (FC number error).  This error code indicates that parameter x contains a block number higher than the highest permitted number. |
| 8x35 | The parameter contains an FB number that is too high (FB number error).  This error code indicates that parameter x contains a block number higher than the highest permitted number. |
| 8x3A | The parameter contains the number of a DB that is not loaded. |
| 8x3C | The parameter contains the number of an FC that is not loaded. |
| 8x3E | The parameter contains the number of an FB that is not loaded. |
| 8x42 | An access error occurred while the system was attempting to read a parameter from the peripheral input area. |
| 8x43 | An access error occurred while the system was attempting to write a parameter to the peripheral output area. |
| 8x44 | Error in the nth (n &gt; 1) read access after an error occurred.  This error code indicates that access to the required parameter is denied. |
| 8x45 | Error in the nth (n &gt; 1) write access after an error occurred.  This error code indicates that access to the required parameter is denied. |
| 8x7F | Internal error  This error code indicates an internal error at parameter x. |

#### Specific error codes

Some instructions have a return value that provides an error code specific for the instruction. A specific error code indicates errors that can occur only in specific instructions.

A specific error code consists of the following two numbers:

- An error class from 0 to 7.
- An error number from 0 to 15.

  ![Specific error codes](images/19487882379_DV_resource.Stream@PNG-en-US.png)

For further information on specific error codes, refer to the descriptions of the individual instructions in the information system.

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Use of the instructions GET_ERROR and GET_ERR_ID

#### Introduction

Local error handling makes it possible to query the occurrence of errors within a program block and evaluate the associated error information. You can set local error handling for organization blocks (OBs), function blocks (FBs), and functions (FCs). If local error handling is enabled, the system reaction is ignored.

You can read out the error number from the error information of the instruction GET_ERR_ID. You can find out, for example, which parameter caused an access error from the error information of the instruction GET_ERROR. In order for the instructions to output the required error information, they must be programmed in the user program for each individual program block from which potential errors are to be evaluated. If you work with the instructions, no error OB is called and there is no entry in the diagnostics buffer. With this method of error handling, you actively intervene in the program sequence by programming a reaction to the errors that occurred. Because errors can occur at any location within the program block, we recommend that you integrate the instruction at the end of the program block.

The instructions GET_ERROR and GET_ERR_ID differ in the amount of error information that is output with each one.

As soon as you have integrated one of the two instructions in your program code, the "Handle errors within block" check box is selected in the inspector window under "Properties &gt; Attributes". This setting cannot be edited in the Inspector window. Local error handling can be deactivated by deleting the inserted instructions for local error handling.

> **Note**
>
> **Block property "Handle errors within block"**
>
> This setting is not applied by a calling block, nor is it transferred to called program blocks. The system settings still apply to higher-level and lower-level program blocks, provided dedicated local error handling has not been programmed for these blocks.

#### Error output priorities

In local error handling, information about the first error that occurred is displayed using the instructions GET_ERROR or GET_ERR_ID. If multiple errors occur at the same time while an instruction is being executed, these errors are displayed according to their priority. The following table shows the priority of different types of errors:

| Priority | Error type |
| --- | --- |
| 1 | Error in the program code |
| 2 | Missing reference |
| 3 | Invalid range |
| 4 | DB does not exist |
| 5 | Operands are not compatible |
| 6 | Width of specified area is not sufficient |
| 7 | Timers or counters do not exist |
| 8 | No write access to a DB |
| 9 | I/O error |
| 10 | Instruction does not exist |
| 11 | Block does not exist |
| 12 | Invalid nesting depth |

The highest priority is 1 and the lowest priority is 12.

#### Additional information

For additional information on the instructions, refer to the information system under PLC programming &gt; Instructions &gt; Instructions (S7-1200, S7-1500) &gt; Basic instructions. The instructions are available in the programming languages LAD/FBD/STL/SCL and GRAPH.

---

**See also**

[GET_ERROR: Get error locally (S7-1200, S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#get_error-get-error-locally-s7-1200-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)
  
[GET_ERROR: Get error locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_error-get-error-locally-s7-1200-s7-1500)

### Example of how to handle program execution errors

#### Introduction

The local error handling options can be programmed individually or in combination with one another. To ensure that every error scenario that may occur within your program is recognized, we recommend a combination of local error handling options, as shown in the example below.

For a more precise error analysis, in addition to the RET_VAL output parameter you can also use the "GET_ERROR" or "GET_ERR_ID" instruction. These options provide you with error codes whose detailed explanations are available in the descriptions of the respective instructions.

There are also error scenarios in which the RET_VAL output parameter does not output a valid error code. If an access error occurs while reading an input parameter, for example, the outputs of the instruction are no longer written, because the execution of the instruction is interrupted. In this case, we recommend that you integrate the two instructions "GET_ERROR" and "GET_ERR_ID" in your program because they provide reliable error information even when this type of error occurs.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Access error during reading of an input parameter**  The RET_VAL parameter does not return a valid error code and no detailed error information is output in the diagnostics buffer. |  |

A first indicator for an error can be either the BR bit of the status word or the ENO enable output. If these return signal state "0", there is an error in the execution of the instruction. Signal state "1" indicates that there is no error and no further error analysis is necessary, except when a memory access error is involved. In this case, signal state "1" can also indicate an error.

#### Procedure

The following example shows you how to recognize an access error during reading of an input parameter:

1. Declare the block interface of your program block as follows:

   ![Procedure](images/56935938699_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/56935938699_DV_resource.Stream@PNG-de-DE.png)
2. Write the following program code:

   ![Procedure](images/56935947531_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/56935947531_DV_resource.Stream@PNG-de-DE.png)

In network 1, the instruction "MOVE_BLK_VARIANT": Move block" is called. The "SrcField" source area is accessed using a variable index in the SRC parameter. If no errors occur during execution of the instruction, the ENO enable output returns signal state "1", and program execution jumps to network 4 and continues there.

If an access error occurs during execution of the instruction, for example, due to the variable index, the instruction "GET_ERR_ID: Get error ID locally" in network 2 returns an error ID. The comparison of the error ID for "UNEQUAL" with the value "0" in network 2 returns the result #Test2 = TRUE. The comparison of the error ID for "EQUAL" with the value "0" in network 3 returns the result #Test3 = TRUE.

The #TagRet_Val operand at the RET_VAL output parameter returns no valid error code in this case.

#### Exceptions

There are some instructions, however, for which you cannot program the error handling as described in the example above. These includes the following instructions:

- Instructions that generally have no EN/ENO mechanism
- Instructions in which the ENO was disabled
- S_COMP
- PEEK, PEEK_BOOL, POKE, POKE_BOOL and POKE_BLK

The BR bit or the ENO enable output is set to TRUE in these instructions even if it may result in an access error.

The following example shows how you can program reliable error handling in the STL programming language:

![Exceptions](images/71429933963_DV_resource.Stream@PNG-de-DE.png)

| STL | Explanation |
| --- | --- |
| SET | // The #Tag_ErrorID operand is initialized with "0". |
| L 0 |  |
| T #Tag_ErrorID |  |
|  |  |
| CALL S_COMP | // The instruction is called. |
| src_type := String | // Data type of parameters IN1 and IN2 |
| relation := EQ | // The comparison type of the instruction |
| IN1 := #StringArray.THIS[#index] | // Variable access to the ARRAY component. |
| IN2 := 'STRING' | // The two values are compared with each other. |
| OUT := #TagResult | // If both values are identical, the #TagResult operand receives the signal state "1". |
|  |  |
| A BR | // The BR bit is queried. |
|  |  |
| CALL GET_ERR_ID | // The instruction is called. |
| RET_VAL := #Tag_ErrorID | // The instruction outputs an error code in the case of an access error. |

Even if the BR bit has signal state "1", the access error is detected. You can query the error code by evaluating the #Tag_ErrorID operand of instruction "GET_ERR_ID: Get error ID locally".

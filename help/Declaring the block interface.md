---
title: "Declaring the block interface"
package: ProgPLCInterfaceenUS
topics: 48
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Declaring the block interface

This section contains information on the following topics:

- [Overview of the block interface](#overview-of-the-block-interface)
- [Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
- [Selecting tabular or textual representation of the block interface](#selecting-tabular-or-textual-representation-of-the-block-interface)
- [Declaring the block interface](#declaring-the-block-interface-1)
- [Declare block interface in the textual view](#declare-block-interface-in-the-textual-view)
- [Editing the properties of local tags and constants](#editing-the-properties-of-local-tags-and-constants)
- [Updating the block interface](#updating-the-block-interface)
- [Extending the block interface (S7-1200, S7-1500)](#extending-the-block-interface-s7-1200-s7-1500)

## Overview of the block interface

### Introduction

The interface contains the declarations of local variables and constants that are used within the block. The variables are subdivided into two groups:

- Block parameters that form the block interface when it is called in the program.
- Local data that are used for storage of intermediate results.

You use the variable declaration to define the call interface of a block in the program and the names and data types of variables and constants that you want to use in the block.

The interface of function blocks also defines the structure of the instances that are assigned to the function block.

### Tabular or textual representation of the block interface

The interface is displayed by default in the tabular view. In SCL the interface can also be displayed in a textual view.

See also:

[Selecting tabular or textual representation of the block interface](#selecting-tabular-or-textual-representation-of-the-block-interface)

### Block parameters

The following table shows the types of block parameters:

| Type | Section | Function | Available in |
| --- | --- | --- | --- |
| Input parameters | Input | Parameters whose values are read by the block. | Functions, function blocks and some types of organization blocks |
| Output parameters | Output | Parameters whose values are written by the block. | Functions and function blocks |
| In/out parameters | InOut | Parameters whose values are read by the block when it is called, and whose values are written again by the block after execution. | Functions and function blocks |
| Return value | Return | Value that is returned to the calling block. | Functions |

Depending on the type of block opened, additional sections can be displayed.

### Local data

The following table shows the types of local data:

| Type | Section | Function | Available in |
| --- | --- | --- | --- |
| Temporary local data | Temp | Tags that are used to store temporary intermediate results. Temporary local data is retained for only one cycle. If you use temporary local data, you have to make sure that the values are written within the cycle in which you want to read them.    **Note:**   If you use temporary local data in functions (FC) with standard access, initialize the data before use. Otherwise, the values could be random. | Functions, function blocks and organization blocks   **Note**:  Temporary local data is not shown in instance data blocks. |
| Static local data | Static | Tags that are used for storage of static intermediate results in the instance data block. Static data is retained until overwritten, which can be after several cycles. The names of the blocks, which are called in this code block as multiple instance, will also be stored in the static local data. | Function blocks |
| Constant | Constant | Constants with declared symbolic names that are used within the block. | Functions, function blocks and organization blocks   **Note**:  Local constants are not shown in instance data blocks. |

---

**See also**

[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Valid data types in the block interface (S7-1200, S7-1500)](#valid-data-types-in-the-block-interface-s7-1200-s7-1500)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)
  
[Using setpoints during commissioning](Programming%20data%20blocks.md#using-setpoints-during-commissioning)

## Rules for declaring the block interface

This section contains information on the following topics:

- [General rules for declaring the block interface](#general-rules-for-declaring-the-block-interface)
- [Valid data types in the block interface (S7-300, S7-400)](#valid-data-types-in-the-block-interface-s7-300-s7-400)
- [Valid data types in the block interface (S7-1200, S7-1500)](#valid-data-types-in-the-block-interface-s7-1200-s7-1500)
- [Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)

### General rules for declaring the block interface

#### Using block parameters

The following rules apply to the use of block parameters within the block:

- Input parameters may only be read.
- Output parameters may only be written.
- In/out parameters may be read and written.

> **Note**
>
> **Maximum number of parameters per block**
>
> The maximum permitted number of formal parameters is sufficient for all usual application scenarios. The exact number depends on the selected data types, declaration subsections and other factors.
>
> If the maximum number is exceeded, you receive a message during the compilation process. In this case, you can combine several parameters in a PLC data type (UDT) or in a global data block (DB) and transfer it as a block parameter.
>
> **You can find more information on transferring structures when a block is called in the following FAQ:**
>
> Why should whole structures instead of many single components be transferred for the S7-1500 when a block is called?
>
> ![Using block parameters](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/67585079](https://support.industry.siemens.com/cs/ww/en/view/67585079)

#### Assigning default values to block parameters

You can assign default values to specific parameters in the function block interface. The possibility of the assignment depends on the declaration subsection and data type of the parameter. If you do not specify a default value the pre-defined value for the specified data type is used. For example, the value "false" is predefined for BOOL.

The following table shows which parameters can be assigned a default value:

| Parameter type | Section | Assignment of a default value is possible |  |  |
| --- | --- | --- | --- | --- |
| Elementary data types | Structured data types | Parameter types |  |  |
| Input parameters | Input | X | X | - |
| Output parameters | Output | X | X | - |
| In/out parameters | InOut | X | - <sup>(1)</sup> | - |
| Static local data | Static | X | X | - |
| Temporary local data | Temp | - | - | - |
| Constants | Constant | X | - | - |

<sup>(1)</sup> Exception: In blocks with optimized access, you have the option to use PLC data types as default values under certain conditions.

> **Note**
>
> **You can find more information on permissible characters in tag names in the following entry at Siemens Industry Online Support:**
>
> When should identifiers and operands be used in "quotation marks" in STEP 7 (TIA Portal)?
>
> ![Assigning default values to block parameters](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/109477857](https://support.industry.siemens.com/cs/ww/en/view/109477857)
>
> **You can find recommendations for uniform, project-wide tag naming in the programming style guide:**
>
> ![Assigning default values to block parameters](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/81318674](https://support.industry.siemens.com/cs/ww/en/view/81318674)

> **Note**
>
> **Calling and addressing program elements in namespaces**
>
> Program elements located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The name of the program element is not in quotation marks.
> - The namespace precedes the program element name, separated by a dot.
>
> You can find detailed information on the notation of namespaces at: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

---

**See also**

[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Declaring predefined actual parameters](#declaring-predefined-actual-parameters)

### Valid data types in the block interface (S7-300, S7-400)

#### Valid data types in the block interface in S7-300/400

The following table shows which data types you can assign to the parameters in the individual sections of the interface.

| Section | Standard  Data types | ARRAY  STRUCT  STRING  DT | Parameter types | VOID | POINTER | ANY |
| --- | --- | --- | --- | --- | --- | --- |
| **Organization block** |  |  |  |  |  |  |
| Temp | X | X | - | - | - | X |
| Constant | X | X <sup>(3)</sup> | - | - | - | - |
| **Function block** |  |  |  |  |  |  |
| Input | X | X | X | - | X | X |
| Output | X | X | - | - | - | - |
| InOut | X | X<sup> (1) </sup> | - | - | X | X |
| Static | X | X | - | - | - | - |
| Temp | X | X | - | - | - | X |
| Constant | X | X <sup>(3)</sup> | - | - | - | - |
| **Function** |  |  |  |  |  |  |
| Input | X | X<sup> (1) </sup> | X | - | X | X |
| Output | X | X<sup> (1) </sup> | - | - | X | X |
| InOut | X | X<sup> (1) </sup> | - | - | X | X |
| Temp | X | X | - | - | - | X |
| Return | X | X | - | X | X | X<sup> (2)</sup> |
| Constant | X | X <sup>(3)</sup> | - | - | - | - |
| <sup>(1)</sup> STRING can only be defined in the standard length of 254 characters.   <sup>(2) </sup>In SCL, ANY is not permitted as a function value.   <sup>(3) </sup>Constants with the ARRAY or STRUCT data type are not permitted. |  |  |  |  |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

### Valid data types in the block interface (S7-1200, S7-1500)

#### Valid data types in the block interface in S7-1200

The following table shows which data types you can assign in the parameters in the individual sections of the interface.

| Section | Standard  Data types | ARRAY  STRUCT  STRING / WSTRING  DT | ARRAY [*] | VOID | VARIANT |
| --- | --- | --- | --- | --- | --- |
| **Organization block** |  |  |  |  |  |
| Temp | X | X <sup>(5)</sup> | - | - | X |
| Constant | X | X<sup> (1) (2)</sup> | - | - | - |
| **Function block** |  |  |  |  |  |
| Input | X | X | - | - | X |
| Output | X | X | - | - | - |
| InOut | X | X <sup>(1)</sup> | X <sup>(4)</sup> | - | X |
| Static | X | X | - | - | - |
| Temp | X | X <sup>(5)</sup> | - | - | X |
| Constant | X | X <sup>(1) (2)</sup> | - | - | - |
| **Function** |  |  |  |  |  |
| Input | X | X<sup> (1)</sup> | X <sup>(4)</sup> | - | X |
| Output | X | X <sup>(1)</sup> | X <sup>(4)</sup> | - | X |
| InOut | X | X<sup> (1)</sup> | X <sup>(4)</sup> | - | X |
| Temp | X | X <sup>(5)</sup> | - | - | X |
| Return | X | X <sup>(3)</sup> | - | X | - |
| Constant | X | X <sup>(1) (2)</sup> | - | - | - |
| <sup>(1)</sup> You cannot make length declarations for STRING and WSTRING in these sections. A declaration in the format MyString[3] would not be permitted. WSTRING is only permitted in blocks with optimized access in these sections.   <sup>(2) </sup>Constants with the ARRAY or STRUCT data type are not permitted.   <sup>(3)</sup> Function values of the WSTRING data type must not be longer than 1022 characters.   <sup>(4)</sup> ARRAY[*] is available in blocks with optimized access as of firmware V4.2.   <sup>(5)</sup> Accesses to structured data types (e.g. ARRAY, STRUCT, PLC data type, etc.) which are declared in the "Temp" section can be accelerated by not accessing the entire structure but the individual, elementary structure elements. |  |  |  |  |  |

#### Valid data types in the block interface in S7-1500

The following table shows which data types you can assign in the parameters in the individual sections of the interface.

| Section | Standard  Data types | ARRAY  STRUCT  STRING / WSTRING  DT | ARRAY[*] | Parameter types | VOID | DB_ANY | POINTER | ANY | VARIANT | REF_TO | NVT<sup>(10)</sup> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Organization block** |  |  |  |  |  |  |  |  |  |  |  |
| Temp | X | X<sup>(9)</sup> | - | -<sup> (4)</sup> | - | X | - | X <sup>(3)</sup> | X | X | X |
| Constant | X | X<sup> (1) (5)</sup> | - | - | - | - | - | - | - | - | - |
| **Function block** |  |  |  |  |  |  |  |  |  |  |  |
| Input | X | X | - | X | - | X | X | X | X | - | X |
| Output | X | X | - | - | - | X | - | - | - | - | X |
| InOut | X | X <sup>(1)</sup> | X<sup>(7)(8)</sup> | - <sup>(4)</sup> | - | X | X | X | X | - | X |
| Static | X | X | - | - | - | X | - | - | - | - | X |
| Temp | X | X<sup>(9)</sup> | - | -<sup> (4)</sup> | - | X | - | X <sup>(3)</sup> | X | X | X |
| Constant | X | X <sup>(1)</sup><sup>(5)</sup> | - | - | - | - | - | - | - | - | - |
| **Function** |  |  |  |  |  |  |  |  |  |  |  |
| Input | X | X <sup>(1)</sup> | X <sup>(7)</sup> | X | - | X | X | X | X | X | X |
| Output | X | X <sup>(1)</sup> | X <sup>(7)</sup> | - | - | X | X | X | X | X | X |
| InOut | X | X<sup> (1)</sup> | X <sup>(7)</sup> | -<sup> (4)</sup> | - | X | X | X | X | - | X |
| Temp | X | X<sup>(9)</sup> | - | - <sup>(4)</sup> | - | X | - | X <sup>(3)</sup> | X | X | X |
| Return | X | X <sup>(6)</sup> | - | - | X | X | X | x <sup>(2)</sup> | - | X | X |
| Constant | X | X <sup>(1) (5)</sup> | - | - | - | - | - | - | - | - | - |
| <sup>(1)</sup> You cannot make length declarations for STRING and WSTRING in these sections. A declaration in the format MyString[3] would not be permitted. WSTRING is only permitted in blocks with optimized access in these sections.    <sup>(2) </sup>In SCL, ANY is not permitted as a function value.   <sup>(3)</sup> ANY can only be used in blocks with standard access in the "Temp" section.   <sup>(4)</sup> The "INSTANCE" parameter type is the only exception permissible in the "TEMP" and "InOut" sections.   <sup>(5)</sup> Constants with the ARRAY or STRUCT data type are not permitted.   <sup>(6)</sup> Function values of the WSTRING data type must not be longer than 1022 characters.   <sup>(7)</sup> ARRAY[*] is available in blocks with optimized access as of firmware V2.0.    <sup>(8)</sup> ARRAY[*] is only available when the "Set in IDB" attribute is not set.   <sup>(9)</sup> Accesses to structured data types (e.g. ARRAY, STRUCT, PLC data type, etc.) which are declared in the "Temp" section can be accelerated by not accessing the entire structure but the individual, elementary structure elements.   <sup>(10)</sup> Named value data types (NVT) are only available in software units. |  |  |  |  |  |  |  |  |  |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)

### Setting the retentivity of local tags

#### Introduction

Function blocks store their data in an instance. To prevent data loss in the event of power failure, you can mark the data as retentive. This data is stored in a retentive memory area. The option of setting the retentivity depends on the set access type of the function block.

#### Retentive behavior in blocks with standard access

In blocks with standard access you cannot set the retentive behavior of individual tags. You can only define them as retentive in the assigned instance. All tags contained in the block are then considered as retentive.

#### Retentivity for optimized block access

In data blocks with optimized access you can define the retentive behavior of individual tags.

For structured data type tags, the retentivity setting always applies to the entire structure. You can make no individual retentivity setting for individual elements within the structure.

You cannot create retentive tags of the structured data type in the "InOut" section. In/out parameters with structured data type, for example ARRAY, STRUCT, or STRING, are always non-retentive.

The following settings are available:

- Retentive

  The values of the tags or the structure are available even after a power failure.
- Non-retentive

  The values of the tags or the structure are lost in the event of a power failure.
- Set in IDB

  The retentivity can be set in the instance data block. The setting that is made in the instance data block than applies, however, centrally to all tags that are selected with "Set in IDB".

---

**See also**

[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)

## Selecting tabular or textual representation of the block interface

### Tabular or textual representation of the block interface

By default, the interface is displayed in the table view. The interface may also be displayed in a textual view in SCL.

The representation of the interface of an SCL block can be set centrally. If you select textual representation as the default, the interface of all newly created blocks in the future will be displayed in the textual view.

The following elements can only be used in the text view:

- Comments between sections or at the beginning of a section
- Several sections of a type (e.g. VAR_INPUT)

> **Note**
>
> **Fail-safe blocks and system blocks**
>
> For fail-safe blocks and system blocks, the interface is only displayed in tabular form.

### Setting the display of the interface for new blocks

To configure the representation of the new blocks, proceed as follows:

1. Select the "Settings" command in the "Options" menu.  
    The "Settings" window is displayed in the work area.
2. Select the "PLC programming &gt; SCL" group in the area navigation.
3. Select the desired view of the interface under "Default settings for new blocks &gt; Block interface".

When you create new blocks, their interface is shown in the selected view.

> **Note**
>
> **Display of the interface after importing a block**
>
> After a block is imported, its interface is displayed in the tabular view.

---

**See also**

[Layout of the block interface](#layout-of-the-block-interface)
  
[Structure of the textual block interface](#structure-of-the-textual-block-interface)

## Declaring the block interface

This section contains information on the following topics:

- [Layout of the block interface](#layout-of-the-block-interface)
- [Declaring local tags and constants in the block interface](#declaring-local-tags-and-constants-in-the-block-interface)
- [Declaring a local tag in the program editor](#declaring-a-local-tag-in-the-program-editor)
- [Declaring tags of the ARRAY data type](#declaring-tags-of-the-array-data-type)
- [Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
- [Declare variables of the STRING and WSTRING data types](#declare-variables-of-the-string-and-wstring-data-types)
- [Declaring tags based on a PLC data type](#declaring-tags-based-on-a-plc-data-type)
- [Declaring higher-level tags](#declaring-higher-level-tags)
- [Declaring multi-instances](#declaring-multi-instances)
- [Declaring parameter instances](#declaring-parameter-instances)
- [Hiding parameters during the block call](#hiding-parameters-during-the-block-call)
- [Declaring predefined actual parameters](#declaring-predefined-actual-parameters)
- [Edit table of the block interface](#edit-table-of-the-block-interface)

### Layout of the block interface

#### Layout of the block interface

The following figure shows the structure of the block interface. The number of columns and sections varies depending on the type of block.

![Layout of the block interface](images/83550116363_DV_resource.Stream@PNG-en-US.png)

#### Meaning of the columns

The following table shows the meaning of the individual columns. You can show or hide the columns as required. The number of columns displayed varies depending on the CPU series and the type of the open object.

| Column | Explanation |
| --- | --- |
| ![Meaning of the columns](images/45636405771_DV_resource.Stream@PNG-de-DE.png) | Symbol you can click on to drag-and-drop an element to a program for use as an operand. |
| Name | Name of the element. |
| Data type | Data type of the element. |
| Offset | Relative address of a tag within the block. The column is only visible in blocks with standard access.  Note:  Many instructions from the SIMATIC system libraries have the "optimized block access" property and therefore do not occupy any fixed memory addresses. No offset is displayed for these instructions, even if you use them as multi-instance in a block with standard access. |
| Default value | Value with which you can pre-assign specific tags in the interface of the code block, or the value of a local constant.  Specification of the default value is optional for tags. If you do not specify any value the predefined value for the indicated data type is used. For example, the value "false" is predefined for BOOL.  The default value of a tag is applied as the start value in the corresponding instance data block. You can replace these values with instance-specific start values in the instance data block.  Constants always have the default value declared in the block interface. They are not shown in instance data blocks and cannot be assigned instance-specific values there. |
| Retain | Marks a tag as retentive.   The values of retentive tags are retained even after the power supply is switched off.   This column is only visible in the interface of the function block with optimized access. |
| Visible in HMI engineering | Indicates whether a tag is visible by default in the HMI selection list. |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime. |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |
| Setpoint | Marks a tag as a setpoint. Setpoint are the values that will probably have to be fine tuned during commissioning.   The column is only available in the interface of function blocks. |
| Supervision | Indicates whether monitoring for process diagnostics was created for the tag. |
| Comment | Comments on documentation of the element. |

---

**See also**

[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Valid data types in the block interface (S7-1200, S7-1500)](#valid-data-types-in-the-block-interface-s7-1200-s7-1500)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Selecting tabular or textual representation of the block interface](#selecting-tabular-or-textual-representation-of-the-block-interface)
  
[Parameter transfer at block call](Programming%20basics.md#parameter-transfer-at-block-call)
  
[Using setpoints during commissioning](Programming%20data%20blocks.md#using-setpoints-during-commissioning)

### Declaring local tags and constants in the block interface

#### Requirement

The block interface is open.

#### Procedure

To declare a tag or constant, follow these steps:

1. Select the desired declaration section in the block interface.

   You must declare a constant in the "Constant" section.
2. Enter a name for the element in the "Name" column.
3. Enter the required data type in the "Data type" column. You will be supported by Autocomplete during input.
4. For constants, enter a value in the "Default value" column.
5. Optional: Change the properties that are displayed in the other columns of the block interface.

#### Result

The element is created.

#### Syntax check

A syntax check is performed after each entry, and any errors found are displayed in red. You do not have to correct these errors immediately - you can continue editing and make any corrections later. However, you will not be able to compile the program if the tag declaration contains syntax errors.

> **Note**
>
> If you change the interface of a block, the calls of the block in the program will possibly become inconsistent. The call locations are automatically updated, if possible.
>
> If an automatic updating is not possible, the inconsistent blocks have to be updated manually.
>
> See also:
>
> [Updating block calls in LAD](Creating%20LAD%20programs.md#updating-block-calls-in-lad)
>
> [Updating block calls in FBD](Creating%20FBD%20programs.md#updating-block-calls-in-fbd)

---

**See also**

[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Constants](Programming%20basics.md#constants)
  
[Declaring tags of the ARRAY data type](#declaring-tags-of-the-array-data-type)
  
[Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
  
[Declare variables of the STRING and WSTRING data types](#declare-variables-of-the-string-and-wstring-data-types)
  
[Declaring tags based on a PLC data type](#declaring-tags-based-on-a-plc-data-type)
  
[Declaring higher-level tags](#declaring-higher-level-tags)
  
[Declaring multi-instances](#declaring-multi-instances)
  
[Declaring parameter instances](#declaring-parameter-instances)
  
[Basic information on start values](Programming%20data%20blocks.md#basic-information-on-start-values)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)

### Declaring a local tag in the program editor

#### Requirement

The program editor is open.

#### Procedure

To declare a local tag, follow these steps:

1. Insert an instruction in your program.

   The "&lt;???&gt;", "&lt;??.?&gt;" or "..." strings represent operand placeholders.
2. Replace an operand placeholder with the name of the tag to be created.
3. Select the name of the element.

   If you want to declare multiple elements, select the names of all the elements to be declared.
4. Select the "Define tag" command in the shortcut menu.

   The "Define tag" dialog box opens. It displays a declaration table in which the name of the element is already entered.
5. To declare a local tag, select one of the following sections:

   - Local In
   - Local Out
   - Local InOut
   - Local Static
   - Local Temp
6. In the other columns, enter data type and comments.
7. Click the "Define" button to complete your entry.

#### Result

The declaration is written directly into the block interface and is valid within the entire block.

> **Note**
>
> If you change the interface of a block, the calls of the block in the program will possibly become inconsistent. The call locations are automatically updated, if possible.
>
> If an automatic updating is not possible, the inconsistent blocks have to be updated manually.
>
> See also:
>
> [Updating block calls in LAD](Creating%20LAD%20programs.md#updating-block-calls-in-lad)
>
> [Updating block calls in FBD](Creating%20FBD%20programs.md#updating-block-calls-in-fbd)

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Basic information on start values](Programming%20data%20blocks.md#basic-information-on-start-values)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Edit table of the block interface](#edit-table-of-the-block-interface)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)

### Declaring tags of the ARRAY data type

#### Requirement

The block interface is open.

#### Procedure

To declare a tag of the ARRAY data type, follow these steps:

1. Select the desired declaration section in the block interface.
2. Enter a tag name in the "Name" column.
3. In the "Data type" column, click the button for the data type selection.

   A list of the permissible data types is opened.
4. Select the "Array" data type.

   The "Array" dialog opens.
5. In the "Data type" text box, specify the data type of the ARRAY elements.
6. In the "ARRAY limits" input field, specify the high and low limit for each dimension.

   Example of a one-dimensional ARRAY:

   `Array[0..3] of Bool`

   Example of a three-dimensional ARRAY:

   `Array[0..3, 0..15, 0..33]of Bool`

   Example of a one-dimensional ARRAY with variable limits:

   `Array[*]of Bool`

   Example of a three-dimensional ARRAY with variable limits:

   `Array[*, *, *]of Bool`

   Example of a one-dimensional ARRAY with local constants as ARRAY limits

   `Array[#My_local_const1..#My_local_const2]of Bool`

   Example of a one-dimensional ARRAY with global constants as ARRAY limits

   `Array["My_global_const1".."My_global_const1"]of Bool`
7. Confirm your entry.
8. Optional: Change the properties of the tags that are displayed in the other columns of the block interface.

The tag is created but remains collapsed. To expand the ARRAY, click the triangle in front of the tag. Note that you cannot expand ARRAYs with more than 10,000 elements for reasons of clarity.

> **Note**
>
> **Availability of ARRAY[*]**
>
> ARRAY[*] is available in optimized blocks for a CPU of the S7-1200 series as of firmware version &gt;= 4.2, and for a CPU of the S7-1500 series as of firmware version &gt;= 2.0. In functions (FC) you can use ARRAY[*] in all declaration subsections. In function blocks (FB) you can declare ARRAY[*] only as an in-out parameter in the "InOut" section.

#### Entering default values of ARRAY elements

To pre-assign default values to the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the desired values in the "Default value" column.

#### Adding comments for ARRAYs

To add a comment for the entire ARRAY, enter the comment in the top line of the ARRAY declaration. The comment is used as a preset comment for all lower-level ARRAY elements.

To provide specific comments for the individual elements of an ARRAY, follow these steps:

1. Click the triangle in front of the ARRAY data type tags.

   The ARRAY is expanded and the individual ARRAY elements are shown in separate lines.
2. Enter the desired values in the "Comment" column.

#### Displaying ARRAYs in expanded mode

In "Expanded mode" all ARRAYs are displayed expanded by default.

To enable the expanded mode, follow these steps:

1. Click the "Expanded mode" button in the toolbar.

> **Note**
>
> **Restriction in "Expanded mode" display**
>
> Depending on the amount of RAM available on your computer, the following maximum limits apply to expanded mode:
>
> - RAM &lt; 8 GB: A maximum of 10,000 rows are displayed.
> - RAM &gt;= 8 GB: A maximum of 40,000 rows are displayed.

---

**See also**

[ARRAY](Data%20types.md#array)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)

### Declaring tags of STRUCT data type

#### Requirement

The block interface is open.

#### Procedure

To declare a tag of the STRUCT data type, follow these steps:

1. Select the desired declaration section in the block interface.
2. Enter a tag name in the "Name" column.
3. Enter "Struct" in the "Data type" column. You will be supported by autocompletion during input.

   An empty, indented row is inserted after the new tag.
4. Insert the first structural element in the first empty row.

   An additional empty row is inserted after the element.
5. Select a data type for the structure element.
6. Optional: Change the properties of the structural element that is displayed in the other columns of the block interface.
7. Repeat the step 4 to 6 for all additional structure elements.

   It is not necessary to end the structure explicitly. The structure ends with the last element that is entered.
8. To insert a new tag after the structure, leave a blank row after the end of the structure and then start the new tag in the second empty row.

#### Result

The tag of STRUCT data type is created.

> **Note**
>
> **S7-1200/S7-1500: A maximum of 252 structures (STRUCT) in one data block**
>
> A maximum of 252 structures (STRUCT) are permitted in one block in CPUs of the S7-1200/S7-1500 series. If you need more structures, use PLC data types (UDT) instead of the "STRUCT" data type.

---

**See also**

[Basic information on STRUCT](Data%20types.md#basic-information-on-struct)
  
[Declaration of STRUCT](#declaration-of-struct)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)

### Declare variables of the STRING and WSTRING data types

#### Requirement

The block interface is open.

#### Procedure

To declare a variable the STRING or WSTRING data type, proceed as follows:

1. Select the desired declaration section in the block interface.
2. Enter a variable name in the "Name" column.
3. Enter "STRING" or "WSTRING" in the "Data type" column. You will be supported by autocompletion during input.
4. Optional: Specify the maximum length of the string using square brackets after the keyword STRING or WSTRING. If you do not specify a maximum length, the string has a default length of 254 characters.

   Example of a WSTRING with the maximum length of 4:

   `WSTRING[4]`

   Example of a string whose maximum length is defined by a local constant:

   `STRING[#My_local_const1]`

   Example of a string whose maximum length is defined by a global constant:

   `STRING["My_global_const1"]`

#### Result

The variable of the STRING or WSTRING data type is applied.

---

**See also**

[Declaration of STRING and WSTRING](#declaration-of-string-and-wstring)

### Declaring tags based on a PLC data type

#### Requirement

A PLC data type is declared in the current CPU.

#### Procedure

To declare a tag based on a PLC data type, follow these steps:

1. Select the desired declaration section in the block interface.
2. Enter the PLC data type in the "Data type" column. You will be supported by Autocomplete during input.

   The tag is created.
3. If you have already defined default values or comments for the tags within a PLC data type during declaration of the PLC data type, these are shown in gray. You can change these values in the block interface.

   The changed values are displayed in black and apply only to the specific point of use.

> **Note**
>
> If you change or delete PLC data types that are used in the block interface, the interface becomes inconsistent. To eliminate this inconsistency, you must recompile the program.
>
> See also: [Updating the block interface](#updating-the-block-interface)

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Declaring higher-level tags

#### Introduction

To access data areas within a declared tag, you can overlay the declared tags with an additional declaration. This provides you with the option of addressing an already declared tag with a different data type. You can, for example, address the individual bits of a tag of WORD data type with an ARRAY of BOOL.

#### Overlaying tags

To overlay a tag with a new data type, follow these steps:

1. Open the block interface.
2. In the interface, select the tag that you want to overlay with a new data type.
3. Click "Add row" in the toolbar.

   A row is inserted after the tag to be overlaid. The overlaying tag must be declared in the row directly after the tag that is to be overlaid.
4. Enter a tag name in the "Name" column.
5. Enter the "AT" entry in the "Data type" column. You will be supported by Autocomplete in this step.

   The following is added to the entry in the "Name" column.

   `"AT<Name of the higher-level tag>"`
6. Click the data type selection button again and select the data type for the new tag.

   The tag is created. It points to the same data as the higher-level tag, however interprets this data with the new data type.

#### Removing overlay

To remove the overlay of a tag, follow these steps:

1. Select the higher-level tag in the block interface.
2. Select the "Delete" command in the shortcut menu.

The overlay is removed.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Overlaying tags with AT](Programming%20basics.md#overlaying-tags-with-at)

### Declaring multi-instances

#### Requirement

The function block to be called exists in project tree and is multi-instance capable.

#### Declaring a multi-instance

To declare a function block to be called as a multi-instance, follow these steps:

1. Open the block interface of the calling function block.
2. In the "Name" column of the "Static" section, enter a designation for the block call.
3. In the "Data type" column, enter the symbolic name for the function block to be called.

> **Note**
>
> The program editor will declare the multi-instance automatically if you program a block call in a network and then specify in the "Call options" dialog that you want to call the block as a multiple instance.

#### Declaring multi-instances as ARRAY

To declare an ARRAY of multi-instances, follow these steps:

1. Open the block interface of the calling function block.
2. In the "Name" column of the "Static" section, enter a designation for the ARRAY.
3. Select the ARRAY data type in the "Data type" column.

   The "Array" dialog opens.
4. In the "Data type" input field, enter the name of the function block for which an instance should be defined. The block name must be in quotation marks.
5. In the "ARRAY limits" input field, specify the high and low limit for each dimension.

   Example of a one-dimensional ARRAY:[0..3]

   Example of a three-dimensional ARRAY:[0..3, 0..15, 0..33]
6. Confirm your entry.

---

**See also**

[Multi-instances](Programming%20basics.md#multi-instances)
  
[Updating the block interface](#updating-the-block-interface)
  
[Declaration of instances](#declaration-of-instances)

### Declaring parameter instances

#### Introduction

The following table shows the options for declaring and using parameter instances in the block interface:

| Declaration | Block type | Application |
| --- | --- | --- |
| InOut | FB   FC | You can then call the instance that you transfer as actual parameter within the function block. |
| Input | FC | You have read access to the data of the instance that you transfer as actual parameter. However, you cannot call the instance from within the block. |
| Output | FC | You have write access to the data of the instance that you transfer as actual parameter. However, you cannot call the instance from within the block. |

#### Requirement

The block interface is open.

#### Procedure

To declare a parameter instance, follow these steps:

1. Open the required section of the block interface (see table).
2. In the "Name" column, enter a designation for the in/out parameter to which the instance is transferred.
3. In the "Data type" column, enter the name of the function block for which an instance should be defined. The block name must be in quotation marks.

> **Note**
>
> **Declaring parameter instances automatically**
>
> The program editor will declare the parameter instance automatically if you program a block call in a network and then specify in the "Call options" dialog that you want to call the block as a parameter instance.

---

**See also**

[Parameter instances](Programming%20basics.md#parameter-instances)
  
[Declaration of instances](#declaration-of-instances)

### Hiding parameters during the block call

#### Introduction

You can hide the block parameters when calling the block in LAD or FBD. Hidden parameters are not visible initially, but can be displayed via a small arrow at the bottom edge of the call box.

Two options are available for hiding a parameter:

- Hide

  The parameter is always hidden.
- Hide, if no parameter is assigned

  The parameter is hidden as long as it has not yet been interconnected. If you assign an actual parameter, the parameter is displayed at the call box.

#### Procedure

Proceed as follows to define whether a block parameter is to be displayed or hidden during the call:

1. Open the block interface.
2. Select a parameter in the block interface.
3. Open the "Properties" tab in the Inspector window.
4. Select the "Attributes" group in the area navigation.
5. Select one of the following options under "Visibility at block calls in LAD / FBD":

   - "Show"
   - "Hide"
   - "Hide, if no parameter is assigned"

#### Result

The parameter is displayed or hidden at the block call in LAD or FBD depending on the setting.

If a syntax error is found during the block call, the parameter cannot be hidden.

---

**See also**

[Wiring hidden parameters](Creating%20LAD%20programs.md#wiring-hidden-parameters)
  
[Declaring predefined actual parameters](#declaring-predefined-actual-parameters)

### Declaring predefined actual parameters

#### Introduction

You can specify during the declaration of a block parameter which actual parameter is to be used during the block call.

This can be useful if you are using program blocks as library elements and want to store information about the actual parameters to be used along with the library element.

In addition you have the option in LAD and FBD to hide parameters that have a valid predefined actual parameter during the block call. Hidden parameters are not visible initially, but can be displayed via a small arrow at the bottom edge of the call box.

Two options are available for hiding a predefined parameter:

- The parameter is always hidden.
- The parameter is hidden as long as the predefined actual parameter is assigned. However, when a different parameter is assigned, the parameter becomes visible.

#### Requirement

The parameter is located in the section "Input", "Output" or "InOut".

#### Procedure

Proceed as follows to predefine an actual parameter:

1. Open the block interface.
2. Select a parameter in the block interface.
3. Open the "Properties" tab in the Inspector window.
4. Select the "Attributes" group in the area navigation.
5. Enter the required actual parameter in the "Predefined actual parameter" input box.
6. Select the "Hide" option under "Visibility at block calls in LAD / FBD".
7. As an additional option, select "Show if parameter assigned on block call is not identical to the predefined actual parameter". This option is only available if the "Hide" option was activated beforehand.

#### Result

- An actual parameter is predefined. If you save the program block as a library element, it thus also contains information about the actual parameter to be used.
- If the library element is used in the program, a check is made to determine whether the actual parameter you have predefined can be addressed. If so, it is automatically used as the actual parameter.
- If the actual parameter If the actual parameter is not found in the program, a syntax error is signaled and you have to carry out the parameter assignment manually. Parameters with an invalid assignment are not hidden.

---

**See also**

[Hiding parameters during the block call](#hiding-parameters-during-the-block-call)

### Edit table of the block interface

This section contains information on the following topics:

- [Inserting table rows](#inserting-table-rows)
- [Inserting table rows](#inserting-table-rows-1)
- [Deleting tags](#deleting-tags)
- [Automatically filling in successive cells](#automatically-filling-in-successive-cells)
- [Show and hide table columns](#show-and-hide-table-columns)
- [Editing tags with external editors](#editing-tags-with-external-editors)

#### Inserting table rows

##### Procedure

Proceed as follows to insert a row above the selected row:

1. Select the row in front of which you want to insert a new row.
2. Click the "Insert row" button on the toolbar of the table.

##### Result

A new row is inserted above the selected row.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Inserting table rows

##### Procedure

Proceed as follows to insert a row below the selected row:

1. Select the row below which you want to insert a new row.
2. Click the "Add row" button on the table toolbar.

##### Result

A new empty row will be inserted below the selected row.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Deleting tags

##### Procedure

To delete a tag, follow these steps:

1. Select the row with the tag to be deleted. You can also select several rows by clicking on them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking on the first and last row.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Automatically filling in successive cells

You can load the contents of one or several table cells into the cells below, automatically filling in the successive cells.

If you automatically fill in cells in the "Name" column, a consecutive number will be appended to each name. For example, "Motor" will become "Motor_1".

You can define individual or more cells as well as entire rows as source area.

If less rows exist in the open table than you want to fill, then you will first have to insert additional empty rows.

##### Requirement

- The table is open.
- Sufficient declaration rows are available.

##### Procedure

To automatically fill in successive cells, follow these steps:

1. Select the cells to be loaded.
2. Click the "Fill" symbol in the bottom right corner of the cell.

   The mouse pointer is transformed into a crosshair.
3. Keep the mouse button pressed and drag the mouse pointer downwards over the cells that you want to fill in automatically.
4. Release the mouse button.

   The cells are filled in automatically.
5. If entries are already present in the cells that are to be automatically filled in, a dialog appears. In this dialog you can indicate whether you want to overwrite the existing entries or insert new rows for the new tags.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Show and hide table columns

You can show or hide the columns in a table as needed.

##### Procedure

To show or hide table columns, follow these steps:

1. Click a column header.
2. Select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
3. To show a column, select the column's check box.
4. To hide a column, clear the column's check box.
5. To hide or show several columns, click "More" and activate or deactivate the check box of the corresponding columns in the "Show/Hide" dialog.

#### Editing tags with external editors

To edit individual tags in external table editors, such as Excel, you can export or import these tags using copy and paste.

> **Note**
>
> **Restriction when displaying and copying ARRAY elements**
>
> Depending on the amount of work memory available on your computer, the following maximum limits apply when displaying and copying ARRAYs from the block interface in an Excel table:
>
> - RAM &lt; 8 GB: A maximum of 10,000 elements are displayed and copied.
> - RAM &gt;= 8 GB: A maximum of 40,000 elements are displayed and copied.

##### Requirements

The block interface and an external editor are opened.

##### Procedure

To export individual tags to an external editor and import them again, follow these steps:

1. Click the "Expanded mode" button to show all elements of structured data types.
2. Select one or more tags.
3. Select "Copy" in the shortcut menu.
4. Switch to the external editor and paste the copied tags.
5. Edit the tags as required.
6. Copy the tags in the external editor.
7. Select the tags in the external editor.
8. Switch back to the block interface.
9. Select "Paste" in the shortcut menu.

## Declare block interface in the textual view

This section contains information on the following topics:

- [Structure of the textual block interface](#structure-of-the-textual-block-interface)
- [Block declaration and return value](#block-declaration-and-return-value)
- [Declaration sections](#declaration-sections)
- [Variable declaration and initialization](#variable-declaration-and-initialization)
- [Declaration of STRUCT](#declaration-of-struct)
- [Declaration of ARRAY](#declaration-of-array)
- [Declaration of STRING and WSTRING](#declaration-of-string-and-wstring)
- [Declaration of instances](#declaration-of-instances)
- [Attributes for variables](#attributes-for-variables)
- [Comments](#comments)
- [Edit textual block interface](#edit-textual-block-interface)
- [Restore default interface of an organization block](#restore-default-interface-of-an-organization-block)
- [Example of a textual block interface](#example-of-a-textual-block-interface)

### Structure of the textual block interface

#### Structure of the textual block interface

The following figure shows the structure of the textual block interface, as it is appears after a new function block is created:

![Structure of the textual block interface](images/110941098379_DV_resource.Stream@PNG-de-DE.png)

The textual block interface consists of the following areas:

| Area | Meaning |
| --- | --- |
| ① Block declaration | The block declaration defines the name and type of block. |
| ② Declaration sections | Declare the parameters and local data of the block in the declaration sections. The declaration sections are already entered in the empty block interface. However, you can move, copy or delete the sections any way you wish. |
| ③ Sidebar | You can set bookmarks in the sidebar. |
| ④ Line numbers | The line numbers are displayed to the left of the declaration sections. |

---

**See also**

[Selecting tabular or textual representation of the block interface](#selecting-tabular-or-textual-representation-of-the-block-interface)

### Block declaration and return value

#### Block declaration

The textual block interface begins with the block declaration. You do not have to enter the block declaration yourself. It is already included in the template of the interface.

#### Return value

For functions (FC), you specify the return value of the function block after the declaration. The return value is the value that is returned to the calling block. If you specify a "VOID" value, the function does not return a value.

#### Syntax

The following syntax is used for the block declaration and the return value:

| Block type | Syntax | Example |
| --- | --- | --- |
| Function (FC) | FUNCTION &lt;Name&gt; [:Data type return value&gt;]  &lt;Declaration&gt; | `FUNCTION "My_Function" : Int`     `FUNCTION "My_Function" : Void` |
| Function block (FB) | FUNCTION_BLOCK &lt;Name&gt;  &lt;Declaration&gt; | `FUNCTION_BLOCK "My_FunctionBlock"` |
| Organization block (OB) | ORGANIZATION_BLOCK &lt;Name&gt;  &lt;Declaration&gt; | `ORGANIZATION_BLOCK "My_OrganizationBlock"` |

---

**See also**

[Example of a textual block interface](#example-of-a-textual-block-interface)

### Declaration sections

#### Declaration sections

The textual block interface is divided into different declaration sections, which are characterized by keyword pairs. Different sections are allowed depending on the type of block.

The order of declaration sections is not of importance. A section can occur several times in the block interface.

The following syntax is used for the declaration section:

| Declaration section | Syntax |
| --- | --- |
| Input parameters | VAR_INPUT [&lt;ATTRIBUTE&gt;]    &lt;Declaration&gt;   END_VAR |
| Output parameters | VAR_OUTPUT [&lt;ATTRIBUTE&gt;]    &lt;Declaration&gt;   END_VAR |
| In/out parameters | VAR_IN_OUT [&lt;ATTRIBUTE&gt;]    &lt;Declaration&gt;   END_VAR |
| Temporary local data | VAR_TEMP   &lt;Declaration&gt;   END_VAR |
| Static local data | VAR [&lt;ATTRIBUTE&gt;]    &lt;Declaration&gt;   END_VAR |
| Constant | VAR CONSTANT   &lt;Declaration&gt;   END_VAR |

You can find information on the individual declaration sections at:

[Overview of the block interface](#overview-of-the-block-interface)

#### Attributes for declaration section

Optionally, you can assign attributes to sections. The attributes apply to all variables that are declared in this section. If a section appears more than once, you can use other attributes for each occurrence.

The following attributes are available:

| Attribute | Meaning |
| --- | --- |
| RETAIN | The tags in this section are retentive, i.e. their values are still available after a power failure. |
| DB_SPECIFIC | Retentivity can be set in the instance data block |

If you do not specify an attribute, the data of the declaration section is non-retentive.

---

**See also**

[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Variable declaration and initialization

#### Declaration and initialization of variables or constants

You declare the local variables and constants that are used within the block in the individual declaration sections.

A variable declaration consists of a symbolic name and a data type. Optionally, you can specify a default value for initializing the variable.

A constant declaration always contains a value besides the symbolic name and the data type. Constant declarations are only permitted in the "VAR CONSTANT" section.

#### Overlaying variables with AT

To access data areas within a declared variable, you can overlay the declared variables with an additional declaration. This provides you with the option of addressing an already declared variable with a different data type. You can, for example, address the individual bits of a variable of WORD data type with an ARRAY of BOOL.

While an AT declaration must always be directly after the referenced tag in the table view, it can be at any position in the text view.

AT declarations cannot be initialized. Note that AT declarations can only be used in non-optimized blocks.

#### Syntax

The following syntax is used to declare a variables and constants:

| Declaration | Syntax | Examples |
| --- | --- | --- |
| Tag | &lt;Name&gt; : &lt;Data type&gt; [:= &lt;Value&gt;]; | `myBit : BOOL;`     `myBit : BOOL := true;` |
| Constant | &lt;Name&gt; : &lt;Data type&gt; := &lt;Value&gt;; | `PI : REAL := 3.141592;`     `myInt: INT := INT#16#7FFF;`     `myString: STRING := 'hello';` |
| AT declaration | &lt;Name&gt; AT &lt;Name of the referenced variable&gt; : &lt;Data type&gt;; | `myReferenceToVar2 AT Var_2 : Int;` |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[General rules for declaring the block interface](#general-rules-for-declaring-the-block-interface)
  
[Overlaying tags with AT](Programming%20basics.md#overlaying-tags-with-at)
  
[Declaring higher-level tags](#declaring-higher-level-tags)
  
[Constants](Programming%20basics.md#constants)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Declaration of STRUCT

#### Declaration of STRUCT

The STRUCT data type represents a data structure that consists of a fixed number of components of different data types.

A structure can also be created based on a PLC data type (UDT). To do this, assign the PLC data type as a data type of the structure. A tooltip shows you the individual elements of the PLC data type.

#### Syntax

The following syntax is used to declare a STRUCT:

| Declaration | Syntax | Examples |
| --- | --- | --- |
| STRUCT | &lt;Name&gt; : Struct   &lt;Element name&gt; : &lt;Data type&gt; [:= &lt;Value&gt;];   &lt;Element name&gt; : &lt;Data type&gt; [:= &lt;Value&gt;];   ...   END_Struct := (&lt;Initialization list&gt;); | `myStruct : Struct`     `mem_1 : Int;`     `mem_2 : Int;`      `mem_3 : BOOL;`     `END_Struct := (6,0, TRUE) ;` |
| STRUCT based on a PLC data type (UDT) | &lt;Name&gt; : "&lt;UDT name&gt;" := (&lt;initialization list&gt;); | `myStruct : "myType" := (6,0, TRUE);` |

> **Note**
>
> **S7-1500: A maximum of 252 structures in one data block**
>
> A maximum of 252 structures is permitted in one data block in CPUs of the S7-1500 series. If you need additional structures, you must restructure your program. You can, for example, create the structures in several global data blocks.

#### Initialization of STRUCT

The initialization of STRUCT is optional. For initialization, enter a value directly after the tag declaration or use an initialization list.

An initialization list is placed after the keyword END_STRUCT in parentheses and := introduces it. If the structure contains lower-level structures, use nested brackets for initialization. If you unintentionally use both options for the initialization, the value from the initialization list is used.

The following syntax is used for the initialization list:

| Declaration | Syntax | Examples | Comment |
| --- | --- | --- | --- |
| Initialization of STRUCT | &lt;Name&gt; : Struct    &lt;Element name&gt; : &lt;Data type&gt; [:= &lt;Value&gt;];   ...   END_Struct | `myStruct : Struct`     `mem_1 : Int := 1;`     `mem_2 : Int := 2;`      `mem_3 : BOOL := FALSE`    `End_Struct` | The structure elements are initialized as follows:  // mem_1 := 1  // mem_2 := 2  // mem_3 := FALSE |
| Initialization list for STRUC | := (&lt;Value&gt;,&lt;Value&gt;,&lt;Value&gt;... ) | `myStruct : Struct`      `mem_1 : Int;`     `mem_2 : Int;`      `mem_3 : BOOL`    `End_Struct:=(2,0,TRUE);` | The structure elements are initialized as follows:  // mem_1 := 2  // mem_2 := 0  // mem_3 := TRUE |
| Initialization list for nested STRUC | := (&lt;Value&gt;,(&lt;Value&gt;,&lt;Value&gt;... )) | `myStruct : Struct`     `mem_1 : Int;`     `mem_2 : Int;`     `mem_3 : Struct`    `mem_4 : BOOL;`    `mem_5 : BOOL;`    `End_Struct;`    `End_Struct:=(2,0, (TRUE,TRUE));` | The structure elements are initialized as follows:  // mem_1 := 2  // mem_2 := 0  // mem_4 := TRUE  // mem_5 := TRUE |
| Initialization list for STRUCT with element name specification | := (&lt;Element name&gt; := &lt;Value&gt;), (&lt;Element name&gt; := &lt;Value&gt;)... | `myStruct : Struct`     `mem_1 : Int;`     `mem_2 : Int;`    `End_Struct:=(mem_2:=55);` | The structure elements are initialized as follows:  // mem_2 := 55 |
| Initialization list for PLC data type (UDT) | := (&lt;Value&gt;,&lt;Value&gt;,&lt;Value&gt;... ) | `myStruct : "myType" := (2,0,TRUE);` | The structure elements are initialized as follows:  // mem_1 := 2  // mem_2 := 0  // mem_3 := TRUE |
| Initialization list for nested PLC data type (UDT) | := (&lt;Value&gt;,(&lt;Value&gt;,&lt;Value&gt;... )) | `myStruct : "myType" := (2,0,(TRUE,TRUE);` | The structure elements are initialized as follows:  // mem_1 := 2  // mem_2 := 0  // mem_3 := TRUE  // mem_4 := TRUE |
| Initialization list for PLC data type (UDT) with element name specification | := (&lt;Element name&gt; := &lt;Value&gt;), (&lt;Element name&gt; := &lt;Value&gt;)... | `myStruct : "myType" := (mem_1:=22,mem_2:=55);` | The structure elements are initialized as follows:  // mem_1 := 22  // mem_2 := 55 |

---

**See also**

[Declaring tags of STRUCT data type](#declaring-tags-of-struct-data-type)
  
[STRUCT data structure (anonymous structures)](Data%20types.md#struct-data-structure-anonymous-structures)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Declaration of ARRAY

#### Declaration of ARRAY

The ARRAY data type represents a data structure that consists of a fixed number of elements of the same data type.

The following syntax is used to declare an ARRAY:

| Declaration | Syntax | Examples |
| --- | --- | --- |
| ARRAY | &lt;Name&gt; : ARRAY [Low limit..High limit] OF &lt;Data type&gt; := [&lt;Initialization list&gt;]; | `MyARRAY_1 : ARRAY[0..7] OF BOOL;`    `MyARRAY_1 : ARRAY[0..7] OF BOOL := [1,1,0,0,0,1,0,0];` |
| ARRAY with variable limits | &lt;Name&gt; : ARRAY [*] OF &lt;Data type&gt;; | `MyARRAY_1 : ARRAY[*] OF INT;`    `MyARRAY_2 : ARRAY[*, *, *] OF INT;` |
| ARRAY with local constants as limits | &lt;Name&gt; : ARRAY [#&lt;Constant name&gt;..#&lt;Constant name&gt;] OF &lt;Data type&gt; := [&lt;Initialization list&gt;]; | `MyARRAY_1 : ARRAY[#LocConst1..#LocConst2] OF INT;`    `MyARRAY_2 : ARRAY[1..#LocConst] OF INT;`    `MyARRAY_3 : ARRAY[1..#LocConst] OF INT := [1,1,0,0];` |
| ARRAY with global constants as limits | &lt;Name&gt; : ARRAY ["&lt;Constant name&gt;".."&lt;Constant name&gt;"] OF &lt;Data type&gt; := [&lt;Initialization list&gt;]; | `MyARRAY_1 : ARRAY["GlobConst1".."GlobConst2"] OF INT;`    `MyARRAY_2 : ARRAY[1.."GlobConst", 2..5,#l..#u] OF INT;`    `MyARRAY_3 : ARRAY[1.."GlobConst"] OF INT:= [1,1,0,0];` |
| ARRAY OF STRUCT | &lt;Name&gt; : ARRAY[Low limit..high limit] OF Struct   &lt;Element name&gt; : &lt;Data type&gt;;   &lt;Element name&gt; : &lt;Data type&gt;;  ...  END_Struct := [&lt;Initialization list&gt;]; | `MyARRAY_1 : Array[0..1] OF Struct`     `mem_1 : Int;`     `mem_2 : Int;`    `END_STRUCT := [ (2,4),(22,44) ];` |
| ARRAY OF UDT | &lt;Name&gt; : ARRAY[Low limit..High limit] OF "&lt;UDT_ Name&gt;" := [&lt;Initialization list&gt;]; | MyARRAY_1 : Array[0..1] OF MyType := [ (2,4),(22,44) ]; |

#### Initialization of ARRAY

The initialization of an ARRAY is optional. You use an initialization list for this. It is enclosed in square brackets after the declaration and starts with :=. The list contains comma-separated values for all elements of the ARRAY. You can initialize a maximum of 10000 elements.

Optionally, you can use repetition factors in parentheses to initialize several successive elements with the same value. The repetition factor must be a positive integer.

With an ARRAY OF STRUCT, you optionally also the opportunity to initialize element by element. You have centrally assign all structural elements of a type a value.

The following syntax is used for the initialization list:

| Declaration | Syntax | Examples | Comment |
| --- | --- | --- | --- |
| Initialization list | := [&lt;Value&gt;,&lt;Value&gt;,&lt;Value&gt;... ] | myArray : ARRAY[0..2] OF BOOL := [1,1,0]; | The ARRAY elements are initialized as follows:  // myArray[0] := 1  // myArray[1] := 1  // myArray[2] := 0 |
| Initialization list with repetition factor | := [&lt;Value&gt;,&lt;Repetition factor&gt;(Value),&lt;Value&gt;... ] | myArray : ARRAY[1..2, 1..3] OF INT := [9,8,3(10),6]; | The ARRAY elements are initialized as follows:  // myArray[1,1] := 9  // myArray[1,2] := 8  // myArray[1,3] := 10  // myArray[2,1] := 10  // myArray[2,2] := 10  // myArray[2,3] := 6 |
| Initialization list for ARRAY of STRUCT | := [(&lt; Value list element 1&gt;), (&lt; Value list element 2&gt;)...] | myArray : Array[0..1] OF Struct    Element1 : Int;    Element2 : Int;   END_Struct := [ (2,4),(22,44) ]; | The ARRAY elements are initialized as follows:  // myArray[0].Element1 := 2  // myArray[0].Element2 := 4  // myArray[1].Element1 := 22  // myArray[1].Element2 := 44 |
| Initialization list for ARRAY of STRUCT with element name specification | := [(&lt;Element name&gt; := &lt;Value&gt;), (&lt;Element name&gt; := &lt;Value&gt;)...] | myArray : Array[0..1] OF Struct   Element1 : Int;    Element2 : Int;   END_Struct := [ (Element1 := 2 , Element2:=4), (Element1 := 22, Element2:=44) ]; | The ARRAY elements are initialized as follows:  // myArray[0].Element1 := 2  // myArray[0].Element2 := 4  // myArray[1].Element1 := 22  // myArray[1].Element2 := 44 |
| Initialization list for ARRAY of STRUCT with repetition factor | := [&lt;Repetition factor&gt;(Value list element 1),&lt;Repetition factor&gt;(Value list element 2),... ] | myArray : Array[0..1, 0..1] OF Struct   Element_x : Int;    Element_y : Int;   End_Struct:=[2((1, 11)), 2((2, 22))]; | The ARRAY elements are initialized as follows:  // myArray[0,0].Element_x:= 1  // myArray[0,0].Element_y:= 11  // myArray[0,1].Element_x:= 1  // myArray[0,1].Element_y:= 11  // myArray[1,0].Element_x:= 2  // myArray[1,0].Element_y:= 22  // myArray[1,1].Element_x:= 2  // myArray[1,1].Element_y:= 22 |
| Initialization list for ARRAY of UDT | := [(Value list element 1&gt;), (&lt;Value list element 2&gt;)...] | myArray : Array[0..1] OF MyType := [ (2,4),(22,44) ]; | The ARRAY elements are initialized as follows:  // myArray[0].UDT-Element1 := 2  // myArray[0].UDT-Element2 := 4  // myArray[1].UDT-Element1 := 22  // myArray[1].UDT-Element2 := 44 |
| Initialization list for ARRAY of UDT with element name specification | := [(&lt;Element name&gt; := &lt;Value&gt;), (&lt;Element name&gt; := &lt;Value&gt;)...] | myArray : Array[0..1] OF MyType := [ (UDT-Element1 := 2,UDT-Element2:=4),(UDT-Element1 := 22,UDT-Element2:=44) ]; | The ARRAY elements are initialized as follows:  // myArray[0].UDT-Element1 := 2  // myArray[0].UDT-Element2 := 4  // myArray[1].UDT-Element1 := 22  // myArray[1].UDT-Element2 := 44 |
| Initialization list for ARRAY of UDT with repetition factor | := [&lt;Repetition factor&gt;(Value list element 1),&lt;Repetition factor&gt;(Value list element 2),... ] | myArray : Array[0..1] OF myType :=[2(((),1))]; | The ARRAY elements are initialized as follows:  // myArray[0].UDT-Element1 := 0  // myArray[0].UDT-Element2 := 1  // myArray[1].UDT-Element1 := 0  // myArray[1].UDT-Element2 := 1 |

---

**See also**

[ARRAY](Data%20types.md#array)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Declaration of STRING and WSTRING

#### Declaration of STRING and WSTRING

The STRING and WSTRING data types store multiple characters in a string. Any character of the ASCII code is permitted in the string. The characters are given in single quotes.

Optionally, you can specify a default value for initializing the string.

The maximum length of the character string can be specified during the declaration of an operand using square brackets after the keyword STRING or WSTRING (for example, STRING[4]). To declare the maximum length, you can enter an absolute value or use local or global constants.

If the specification of the maximum length is omitted, the standard length of 254 characters is set for the respective operand.

#### Syntax

The following syntax is used to declare a STRING and WSTRING:

| Declaration | Syntax | Examples |
| --- | --- | --- |
| STRING | `<` `Name` `> : STRING [:= <` `Value` `>];` | `myString: STRING;`    `myString: STRING := 'hello';` |
| WSTRING | `<` `Name` `> : WSTRING [:= <` `Value` `>];` | `myWstring: WSTRING;`    `myWstring_var: WSTRING := 'helloWorld';` |
| STRING with defined maximum length | `<` `Name` `> : STRING[[` `Constant` `]];` | `myString: STRING[10];`    `myString: STRING["globConst"];`    `myString: STRING[#locConst];` |

---

**See also**

[STRING](Data%20types.md#string)
  
[WSTRING (S7-1200, S7-1500)](Data%20types.md#wstring-s7-1200-s7-1500)
  
[Declare variables of the STRING and WSTRING data types](#declare-variables-of-the-string-and-wstring-data-types)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Declaration of instances

#### Declaration of multi-instances

You declare multi-instances in the "VAR ...END_VAR" section of the textual block interface. Simply enter the name of the called block as the data type.

Multi-instances can also be created as an ARRAY.

It is not possible to initialize the parameters of the called block in the textual interface.

See also:

[Multi-instances](Programming%20basics.md#multi-instances)

[Declaring multi-instances](#declaring-multi-instances)

#### Declaration of parameter instances

It is best to declare parameter instances as in/out parameters in "VAR_IN_OUT...END_VAR" of the textual block interface. However, they are also possible as input or output parameters in functions (FC). Simply enter the name of the called block as the data type.

It is not possible to initialize the parameters of the called block in the textual interface.

See also:

[Parameter instances](Programming%20basics.md#parameter-instances)

[Declaring parameter instances](#declaring-parameter-instances)

| Instance | Syntax | Examples | Meaning |
| --- | --- | --- | --- |
| Multi-instance | VAR   &lt;Multi-instance name&gt;:"&lt;Block name&gt;";  END_VAR | `VAR`      `instFB : "MyFB";`    `END_VAR` | "instFB" is a multi-instance of the "MyFB" block. |
| ARRAY of multi-instances | VAR   &lt;Multi-instance name&gt;: ARRAY [n...m] of "&lt;Block name&gt;";  END_VAR | `VAR`     `instArray : ARRAY [0…4] of "MyFB";`    `END_VAR` | "instArray" is an array of multi-instances of the "MyFB" block. |
| Parameter instance | VAR    &lt;Parameter instance name&gt;:"&lt;Block name&gt;";   END_VAR | `VAR_IN_OUT`     `instParam:"MyFB";`    `END_VAR` | "instParam" is a parameter instance of the "MyFB" block. |

---

**See also**

[Example of a textual block interface](#example-of-a-textual-block-interface)

### Attributes for variables

#### Attributes for variables

Optionally, you can assign attributes to each variable. If you do not explicitly assign an attribute to a variable, it has the preassigned attribute values. You can change the default settings of some attributes in the general settings for PLC programming.

The following attributes are available:

| Attribute | Meaning | Default |
| --- | --- | --- |
| Visible in HMI engineering | Indicates whether a tag is visible by default in the HMI selection list. | TRUE |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime. | TRUE |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. | FALSE |
| Setpoint | Marks a tag as a setpoint. Setpoint are the values that will probably have to be fine tuned during commissioning. The column is only available in the interface of function blocks. | FALSE |

#### Syntax

The following syntax is used for attributes:

| Attribute | Syntax | Examples |
| --- | --- | --- |
| Visible in HMI engineering | &lt;Name&gt; {EXTERNALVISIBLE:=&lt;value&gt;}: &lt;Data type&gt;; | `myInt {EXTERNALVISIBLE:= 'False'} : INT;` |
| Accessible from HMI/OPC UA/Web API | &lt;Name&gt; {EXTERNALACCESSIBLE:=&lt;value&gt;}: &lt;Data type&gt;; | `myInt {EXTERNALACCESSIBLE:= 'False'} : INT;` |
| Writable from HMI/OPC UA/Web API | &lt;Name&gt; {EXTERNALWRITABLE:=&lt;value&gt;}: &lt;Data type&gt;; | `myInt {EXTERNALWRITABLE:= 'False'} : INT;` |
| Setpoint | &lt;Name&gt; {S7_SETPOINT:=&lt;value&gt;}: &lt;Data type&gt;; | `myInt {S7_SETPOINT:= 'False'} : INT;` |

---

**See also**

[General settings for the PLC programming](Program%20editor.md#general-settings-for-the-plc-programming)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Comments

#### Comments

There are several ways to comment a variable in the textual block interface:

- Line comment

  A line comment starts with "//" and extends to the end of the line.
- Comment section

  A comment section is started with "(*" and ended with "*)". It can span several lines.

The following rules apply to comments:

- Comments cannot be nested.
- Multilingual comments are not possible in the textual block interface.
- Comments are not permitted between the block declaration and the first declaration section.

  Exception: A single-line comment is permissible in functions (FC) at this point.

#### Syntax

The following syntax is used for comments:

| Attribute | Syntax | Examples |
| --- | --- | --- |
| Line comment | &lt;Declaration&gt;; //&lt;Comment&gt; | `MyInt : INT; //`  `this is my comment` |
| Comment section | &lt;Declaration&gt;; (*&lt;Comment&gt;*) | `MyInt : INT;`  `(* these are my comments:`     `1st comment`     `2nd comment*)` |

---

**See also**

[Editing multilingual comments in the block interface (S7-1500)](#editing-multilingual-comments-in-the-block-interface-s7-1500)
  
[Example of a textual block interface](#example-of-a-textual-block-interface)

### Edit textual block interface

When editing the textual block interface, you can use the same editing functions as those for editing the program code.

#### Use autocomplete

1. Enter the syntax of the declaration on the keyboard.

   The autocomplete opens during the entry. It offers all the syntax elements that are allowed at the current location.
2. Select the desired element from the autocomplete.

See also: [Entering SCL instructions manually](Creating%20SCL%20programs.md#entering-scl-instructions-manually)

#### Automatically format lines

1. Select the text that you want to format or place the insertion point in the appropriate line.
2. Select the "Format selected text automatically" button into the toolbar of the programming editor.

   All selected lines are formatted as long as they are syntactically correct.

See also: [Formatting SCL code](Creating%20SCL%20programs.md#formatting-scl-code)

#### Indenting or outdenting lines

1. Click in the line that you want to indent or outdent.
2. Press the "Indent text", "Outdent text" button into the toolbar of the programming editor.

   You can set the width of the indent in "Options &gt; Settings".

See also: [Formatting SCL code](Creating%20SCL%20programs.md#formatting-scl-code)

#### Expanding and collapsing sections of code

1. Click the minus sign in the outline view.

   The code section closes.
2. Click the plus sign in the outline view.

   The code section opens.

See also: [Expanding and collapsing sections of code](Creating%20SCL%20programs.md#expanding-and-collapsing-sections-of-code)

#### Using bookmarks

1. Click on the line in which you want to place the bookmark.
2. Click the "Set/delete bookmark" button in the toolbar.

> **Note**
>
> **Navigation view between interface and program code**
>
> If you have set bookmarks both in the interface and in the program code, you cannot use the commands "Go to next/previous bookmark" to navigate between the two windows.

See also: [Using bookmarks](Creating%20SCL%20programs.md#using-bookmarks)

#### Copying or moving tags between textual and tabular interfaces

You can copy or move tags between a textual interface and a tabular interface.

1. Select one or more tags in a declaration section.
2. In the shortcut menu, select the "Copy" or "Cut" command.
3. Place the mouse pointer at the position where you want to insert the tag.
4. Select "Paste" in the shortcut menu.

> **Note**
>
> **Copying or moving structured data types with initializations**
>
> When nested structured data types (for example, ARRAY of STRUCT) are copied from a textual interface to a tabular interface, the default values of the lower-level structures are not copied or moved.

### Restore default interface of an organization block

#### Introduction

Organization blocks have defined interface parameters that include the start information of the OB. If you change or delete these predefined parameters in the textual block interface, you have the option to restore the defined standard interface with optimized organization blocks.

#### Procedure

To restore the default interface of an organization block, proceed as follows:

1. Select the "Restore default interface" command in the shortcut menu.

#### Result

- Deleted or changed OB parameters are restored.
- Parameters which you have added manually are not deleted but are retained.

### Example of a textual block interface

#### Example

The following figure shows an example of a textual block interface:

![Example](images/110954048779_DV_resource.Stream@PNG-de-DE.png)

## Editing the properties of local tags and constants

This section contains information on the following topics:

- [Properties of local tags and constants](#properties-of-local-tags-and-constants)
- [Changing properties of local tags and constants](#changing-properties-of-local-tags-and-constants)
- [Editing multilingual comments in the block interface (S7-1500)](#editing-multilingual-comments-in-the-block-interface-s7-1500)

### Properties of local tags and constants

#### Properties

The table below provides an overview of the properties of local tags and constants:

| Group | Property | Description |
| --- | --- | --- |
| General | Name | Name of the element |
| Data type | Data type of the element |  |
| Default value | Value with which you can pre-assign specific tags in the interface of the code block, or the value of a local constant.   Specification of the default value is optional for tags. If you do not specify any value the predefined value for the indicated data type is used. For example, the value "false" is predefined for BOOL.  The default value of a tag is applied as the start value in the corresponding instance. You can then replace these adopted values with instance-specific start values. |  |
| Comment | Comment for the element |  |
| Attributes | Retain | Marks the tag as retentive.   The values of retentive tags are retained even after the power supply is switched off.   This attribute is only available in the interface of the function block with optimized access. |
| Visible in HMI engineering | Shows whether the tag is visible by default in the HMI selection list. |  |
| Writable from HMI/OPC UA/Web API | Indicates whether or not the tag can be written from HMI/OPC UA/Web API during runtime. |  |
| Accessible from HMI/OPC UA/Web API | Indicates whether HMI/OPC UA/Web API can access this variable during runtime.  Note, however, that you cannot implement general access protection for the tag with the "Accessible from HMI/OPC UA/Web API" attribute. Read or write access from other applications is possible even if the attribute is not enabled. |  |
| Visibility in block calls in LAD/FBD | Show:  The parameter is always visible at block calls in LAD or FBD. |  |
| Hide:  The parameter is always hidden at block calls in LAD or FBD.   The instruction box then has a small arrow on the lower edge. You can have the parameters displayed and interconnect them by clicking this arrow. |  |  |
| Hide if no parameter is assigned:  The parameter is always hidden at block calls in LAD or FBD as long as it has not yet been interconnected. If you assign an actual parameter, the parameter is displayed at the call box. |  |  |
| Predefined actual parameter | Defines a parameter that is to be used as actual parameter during the block call. |  |
| Show if parameter assigned on block call is not identical to the predefined actual parameter | The parameter is hidden at block calls in LAD or FBD as long as the predefined actual parameter has not yet been assigned. However, when a different parameter is assigned, the parameter becomes visible.     This option is only active if you have selected the "Hide" parameter and have defined a predefined actual parameter. |  |
| User-defined attributes | CFC_Configurable | Configurable  Indicates whether a parameter is configurable in CFC. |
| CFC_ForTest | For test  Indicates whether a parameter is registered for the CFC test mode. |  |
| CFC_Visible | Visible  Indicates whether a parameter is visible in CFC. |  |
| CFC_Interconnectable | Interconnectable  Indicates whether a parameter is interconnectable in CFC. |  |
| CFC_EnableTagReadback | Enable tag readback  Indicates whether a parameter is relevant for the "Read back chart" function in CFC. |  |
| CFC_EnumerationTexts | Enumeration texts  The attribute is only used internally. |  |
| CFC_EngineeringUnit | Engineering unit  Assigns a parameter to a unit in CFC. |  |
| CFC_LowLimit | Low limit  Defines the low limit for the parameter in CFC. |  |
| CFC_HighLimit | High limit  Defines the high limit for the parameter in CFC. |  |

---

**See also**

[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Changing properties of local tags and constants](#changing-properties-of-local-tags-and-constants)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Hiding parameters during the block call](#hiding-parameters-during-the-block-call)
  
[Declaring predefined actual parameters](#declaring-predefined-actual-parameters)

### Changing properties of local tags and constants

#### Editing properties of an element in the tabular block interface

To edit the properties of an element in the block interface, follow these steps:

1. Open the block interface.
2. Select the required element in the table.
3. Change the entries in the columns.

#### Editing properties of multiple elements in the tabular block interface

You can also simultaneously set or reset some properties for multiple selected elements.

To change one of these properties for several elements, follow these steps:

1. Open the block interface.
2. Hold down the &lt;Ctrl&gt; key.
3. In the required column, select each of the table cells whose value you want to change.
4. Select the "Set &lt;property&gt;" or "Reset &lt;property&gt;" command in the shortcut menu.

#### Editing properties in the properties window

To edit the properties of an individual tag or constant, follow these steps:

1. Select the tag or constant.

   The properties of the element are shown in the Inspector window.
2. Change the entries in the inspector window.

#### Renaming tags directly in the program editor

To rename one or more elements, follow these steps:

1. Select one or more elements in the program.
2. Select the "Rename tag" command in the shortcut menu.

   The "Rename tag" dialog opens. It displays a declaration table with the selected elements.
3. Change the entries in the "Name" column.
4. Confirm the input by clicking the "Change" button.

#### Editing the data type or comment in the program editor

Proceed as follows to edit the data type or tag comment in the program editor:

1. Select the name of the tag.
2. Select the "Rewire tag" command in the shortcut menu.

   The "Rewire tag" dialog will open. The dialog shows a declaration table.
3. Change the entry in the "Data type" or "Comment" columns.
4. Click the "Change" button to confirm the input.

#### Effect in the program

In case of a change of the name, data type or address of a tag or constant, each location of use of the tag is automatically updated in the program.

> **Note**
>
> If you change the interface of a block, the program may become inconsistent. The inconsistencies are automatically updated, if possible.
>
> If an automatic updating is not possible, the inconsistent calls are marked in red. You than have to manually updated the inconsistencies.
>
> See also:
>
> [Updating block calls in LAD](Creating%20LAD%20programs.md#updating-block-calls-in-lad)
>
> [Updating block calls in FBD](Creating%20FBD%20programs.md#updating-block-calls-in-fbd)

---

**See also**

[Overview of the block interface](#overview-of-the-block-interface)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Basic information on start values](Programming%20data%20blocks.md#basic-information-on-start-values)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Updating the block interface](#updating-the-block-interface)
  
[Edit table of the block interface](#edit-table-of-the-block-interface)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)

### Editing multilingual comments in the block interface (S7-1500)

You can edit the comments from the block interface in all project languages that you have activated in the project language settings. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

Note that the texts must not exceed a length of 32767 Unicode characters even after translation.

Multilingual comments are not possible in the textual block interface.

#### Requirement

- You have activated multiple project languages.
- The block interface is open and it contains at least one comment.
- The block does not have know-how protection.

#### Procedure

To edit a comment in all project languages, follow these steps:

1. Click on the comment whose translation you want to edit.

   If you want to edit the translations of several comments at the same time, select all the desired comments.
2. Open the "Properties" tab in the Inspector window.
3. Open the "Texts" tab.

   The "Texts" tab displays the selected comments in the active project languages and, if available, the translations of the comments.
4. You can edit the translations directly in the table in the "Texts" tab.
5. To edit the translations with an external editor, you can export the displayed texts to OOXML format using the "Export/Import project texts" buttons.

> **Note**
>
> **Editing all project texts in the global "Project texts" table**
>
> You can also edit the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts". It contains all translatable texts of the entire project.
>
> You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

## Updating the block interface

### Introduction

If you change or delete PLC data types or multiple instances that are used in the block interface, the interface will become inconsistent. To remedy this inconsistency, the interface has to be updated.

You have two options for updating the block interface:

- Explicit updating of the block interface.  
  The used PLC data types and multiple instances will be updated. The instance data blocks that belong to the block are not implicitly updated during this process.
- Implicit updating during compilation.  
  All used PLC data types and multiple instances as well as the related instance data blocks will be updated.

### Explicit updating of the block interface

To explicitly update the block interface, follows these steps:

1. Open the block interface.
2. Select the "Update" command in the shortcut menu.

### Implicit Updating during Compilation

Proceed as follows to implicitly update all uses of PLC data types and multiple instances as well as the instance data blocks during compilation:

1. Open the project tree.
2. Select the "Program blocks" folder.
3. Select the command "Compile &gt; Software (rebuild all blocks)" in the shortcut menu.

---

**See also**

[Declaring tags based on a PLC data type](#declaring-tags-based-on-a-plc-data-type)
  
[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)
  
[Basic information on start values](Programming%20data%20blocks.md#basic-information-on-start-values)
  
[Using tags within the program](Programming%20basics.md#using-tags-within-the-program)
  
[Keywords and reserved identifiers](Programming%20basics.md#keywords-and-reserved-identifiers)
  
[Properties of local tags and constants](#properties-of-local-tags-and-constants)
  
[Setting the retentivity of local tags](#setting-the-retentivity-of-local-tags)
  
[Updating block calls in LAD](Creating%20LAD%20programs.md#updating-block-calls-in-lad)
  
[Declaring multi-instances](#declaring-multi-instances)
  
[Edit table of the block interface](#edit-table-of-the-block-interface)
  
[Rules for declaring the block interface](#rules-for-declaring-the-block-interface)

## Extending the block interface (S7-1200, S7-1500)

### Description

In order to enable the editing of PLC programs that have already been commissioned and that are running without error on a system, CPUs of the S7-1500 series and most CPUs of the S7-1200 V4 and higher series support the option of extending the interfaces of function blocks during runtime.

You can download the modified blocks without setting the CPU to STOP and without affecting the values of already loaded tags.

This is a simple means of implementing program changes. This load process (download without reinitialization) will not have a negative impact on the controlled process.

### Principle of operation

Each function block is always assigned a default memory reserve. The memory reserve is not used initially. Activate the memory reserve if you have compiled and loaded the block and then decide that you want to load interface changes later. All tags that you subsequently declare will be saved to the memory reserve. The subsequent download does not influence any tags that are already loaded or therefore have a negative impact on the ongoing operation.

If you decide to review your program at a later time while the plant is not in operation, you are also provided an option of reworking the memory layout of individual or several blocks in a single pass. With this action, you move all tags from the reserve area to the regular area. The memory reserve is now cleared and made available for further interface extensions.

### Requirements

This "Download without reinitialization" function is available if the following requirements are met:

- The project is in the "TIA Portal V12" format or a higher version.
- You are working with a CPU that supports "Download without reinitialization".
- The blocks were created in LAD, FBD, STL, or SCL.
- The blocks were created by the user, i.e. they are not included with the blocks delivered in your package.
- These blocks are assigned the optimized access attribute.

### Basic steps

To extend the interface of a function block and then load the block without re-initialization, follows these steps:

1. All blocks have a default memory reserve of 100 bytes. You can adapt this memory reserve to suit your requirements.
2. Activate the memory reserve.
3. Extend the block interface.
4. Compile the block.
5. Download the block to the CPU as usual.

For more information on the various steps, refer to chapter "Loading blocks (S7-1200/1500) ".

> **Note**
>
> The full scope of the "Download without reinitialization" function is only available on CPUs of the S7-1500 and S7-1200 V4 series.
>
> However, all CPU families support the option of extending the interface of function blocks and downloading newly declared tags without repercussion:
>
> - You may add new tags in the "Temp" section and download these without influencing the process.
> - You may create new tags of a structured data type in the "InOut" section and download these without influencing the process.

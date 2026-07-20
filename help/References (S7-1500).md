---
title: "References (S7-1500)"
package: ProgDatatypeRefenUS
topics: 11
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# References (S7-1500)

This section contains information on the following topics:

- [Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)
- [Declaring references (S7-1500)](#declaring-references-s7-1500)
- [Referencing (S7-1500)](#referencing-s7-1500)
- [Dereferencing (S7-1500)](#dereferencing-s7-1500)
- [Standard instructions with references (S7-1500)](#standard-instructions-with-references-s7-1500)
- [Assignment attempt to a reference (S7-1500)](#assignment-attempt-to-a-reference-s7-1500)
- [Transferring references as block parameters (S7-1500)](#transferring-references-as-block-parameters-s7-1500)
- [Example: Transferring tags of different data types using references (S7-1500)](#example-transferring-tags-of-different-data-types-using-references-s7-1500)
- [Example: Return data to the calling block via reference (S7-1500)](#example-return-data-to-the-calling-block-via-reference-s7-1500)
- [Example: Editing different axis types iteratively in a program loop (S7-1500)](#example-editing-different-axis-types-iteratively-in-a-program-loop-s7-1500)

## Basic information about references (S7-1500)

### Description

A reference is a tag that itself contains no value but rather points to the memory location of another tag.

References enable the forwarding of tags beyond block boundaries and thus the direct manipulation of tag values without having to create a copy of the tags.

When you declare the reference you specify from which data type the referenced tag must be. References are type-safe. This is a key aspect in particular for control system on which runtime errors need to be avoided. The restriction, made in IEC, that references must point to temporary data elements further increases the reliability. In this way runtime errors are avoidable.

It is ensured that references either refer to a valid memory space of the correct data type or are assigned the value NULL.

### Using references in the program

Requirement for using references is a CPU of the S7-1500 series with the firmware version V2.5 or higher.

The following graphic provides an overview of options for using references.

![Using references in the program](images/155570783371_DV_resource.Stream@PNG-en-US.png)

### Differences between references and VARIANT

A tag of VARIANT data type is like a pointer that can point to other tags of any data type. For this reason, the data type that the VARIANT tag will point to does not have to be defined yet when the program is created. The data type is not defined until runtime. A VARIANT tag can even have different data types in different program cycles. The data type VARIANT is suitable for creating generic programs and for indirect addressing. If you want to further process a VARIANT tag in the program code, however, you need to use special instructions to determine which data type is currently present. You also cannot directly read and write VARIANT tags. Rather, special instructions, e.g. VariantGet and VariantPut must likewise be used for this.

If you use references, you define the data type when creating the program. Because the data type does not have to be determined at runtime, the program will perform better and be more clearly structured. Through dereferencing you can have direct write or read access to the referenced tag without having to integrate additional instructions in your program.

Unlike VARIANT, however, references may only point to data that are located in an optimized memory area.

### Examples

The example below shows various possible applications for references.

The block interface contains the "myRefInt" tag that was declared as a reference:

![Examples](images/99650362379_DV_resource.Stream@PNG-de-DE.png)

The figure below shows how this tag is used in SCL:

![Examples](images/101225494795_DV_resource.Stream@PNG-de-DE.png)

## Declaring references (S7-1500)

### Description

References can be declared in the block interface of functions and function blocks. The following declaration areas are permitted for this purpose:

- FC: Input, Output, Temp, Return
- FB: Temp
- OB: Temp

Reference declarations in structures are not possible.

To declare references, use keyword "REF_TO" and specify the required data type of the referenced tag. However, do not yet specify which specific tag the reference points to:

![Description](images/153263854475_DV_resource.Stream@PNG-de-DE.png)

References can point to the following elements:

| Referenced element | Comments |
| --- | --- |
| Bit strings | References to BYTE, WORD, DWORD and LWORD are possible.  References to BOOL are not possible. |
| Integers | References to integers are possible. |
| Floating-point numbers | References to floating-point numbers are possible. |
| Character strings | References to character strings are possible.  Length declarations for character strings are not possible. |
| IEC timers | References to IEC_TIMER and IEC_LTIMER are possible.   References to derived data types, such as TON, are not possible. |
| IEC counters | References to IEC_COUNTER / IEC_UCOUNTER, IEC_SCOUNTER / IEC_USCOUNTER, IEC_DCOUNTER / IEC_UDCOUNTER are possible.  References to derived data types, such as CTU, are not possible. |
| PLC data types (UDT) | References to PLC data types are possible. |
| System data types (SDT) | References to system data types are possible. |
| ARRAY | References to ARRAYs of the data types listed above are possible.  References to ARRAY[*] are not possible.  ARRAYs from references are not possible.  The following declaration would therefore not be permitted: `ARRAY of REF_TO` `<data type>` |
| Technology objects | References to technology objects of the "Motion" and "SIMATIC Ident" categories are possible as of firmware V3.0.  References to ARRAYs of technology objects are not possible. The following declaration would therefore not be permitted: `REF_TO ARRAY of` `<technology object>` |
| Data block | References to an entire data block are only possible if the data block was originally derived from a PLC data type (UDT) or system data type (SDT). |

### Initialization

When a reference tag is created, the system initializes it with the value NULL. This means that although the reference itself exists, it still does not refer to any valid memory. If a ZERO reference is accessed during runtime, a programming error is output. You cannot yourself enter an initialization in the block interface.

Use the instruction "REF ()" to initialize a reference.

See also: [Referencing](#referencing-s7-1500)

### Retentivity

References cannot be retentive. However, they can point to retentive data.

> **Note**
>
> **Maximum number of reference parameters per block**
>
> The permissible maximum amount of parameters of data type "REF_TO" in a block depends on various factors, such as the block type and the number of other declared parameters with structured data type (ARRAYs, PLC data types, etc.) as well as the number of declared instances.
>
> If the maximum number is exceeded, you receive a message during the compilation process. In this case, you can combine several parameters in a PLC data type (UDT) or in a global data block (DB) and transfer it as a block parameter.

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)
  
[Valid data types in the block interface (S7-1200, S7-1500)](Declaring%20the%20block%20interface.md#valid-data-types-in-the-block-interface-s7-1200-s7-1500)

## Referencing (S7-1500)

### Description

The keyword "REF()" is used to specify the tag to which a previously declared reference is to point. As parameter, specify the tag to be referenced. The data type of the tag must correspond exactly to the data type of the declared reference. This means that a reference with data type "REF_TO Int" can only point to a tag of data type "Int". No data type conversion is made.

> **Note**
>
> **Transferring "**REF()**" as an actual parameter during the block call**
>
> You can also transfer "REF()" as an actual parameter to a called block in whose interface references are declared.
>
> See also: [Transferring references as block parameters](#transferring-references-as-block-parameters-s7-1500)

### Rules

The following rules apply to referencing:

- The data to which a reference points must be located in an optimized memory space.
- The reference must only point to data in a global DB or static tags.
- The reference must not refer to the following data:

  - Temporary local data
  - Global tags from the PLC tag table
  - Block parameters
  - Constants
  - Write-protected tags
- The following applies to references to arrays:

  - The array limits and dimensions of the reference and the referenced tag must be identical.
  - References to arrays with dynamic limits (Array[*]) cannot be created.
  - References to ARRAY DBs that are based on a PLC data type must be created as follows:

    `REF("my_ArrayDB_UDT"."THIS")`

    `REF("my_ArrayDB_UDT"."THIS"[i])`
- Technology objects cannot be referenced with REF().

### Examples

The example below shows the interface of a block: The interface contains several parameters that were declared with data type "REF_TO". When declaring the reference, you define only the data type of the referenced tag. You do not yet specify the tag to which the reference points.

![Examples](images/102962168203_DV_resource.Stream@PNG-de-DE.png)

In the program code you specify to which specific tag the declared reference parameters should point.

Examples in SCL:

![Examples](images/102917709067_DV_resource.Stream@PNG-de-DE.png)

Examples in LAD:

![Examples](images/102962177931_DV_resource.Stream@PNG-de-DE.png)

Examples in STL:

![Examples](images/102964708363_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)
  
[Declaring references (S7-1500)](#declaring-references-s7-1500)

## Dereferencing (S7-1500)

### Description

To have read or write access to the value of a referenced tag, you use the caret character "^". This type of access is called "dereferencing".

### Examples

The example below shows the interface of a block: The interface contains the "myRefInt" parameter that was declared as a reference and a few static parameters that have already been initialized with a value:

![Examples](images/99650372491_DV_resource.Stream@PNG-de-DE.png)

The figure below shows how the "REF()" instruction is used to specify that "myRefInt" points to "#a" and how "#a" is used in calculations in SCL.

![Examples](images/99652173323_DV_resource.Stream@PNG-de-DE.png)

The following example shows how to read or write the elements of a referenced technology object using the caret character. The interface contains the two reference declarations "myReferenceSpeedAxis" and "myReferencePositioningAxis":

![Examples](images/159546792075_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the write and read access:

![Examples](images/159546800651_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)

## Standard instructions with references (S7-1500)

You can use references as input or output parameters of assignments or comparison instructions.

You can use dereferenced values as parameters of any instruction, provided they have the correct data type.

### Assignment

References can be assigned to each other like any other tag. In this case, the address of the reference, not its value, is assigned to the second reference. References can only be assigned to each other if they refer to the same data type. No implicit data type conversion is made.

References to PLC data types, too, must be of the same data type. It is not enough for both PLC data types to have the same structure.

You can also assign a reference to a VARIANT. In this case the VARIANT must be declared as temporary tag (Temp).

The following rules apply to references to technology objects:

- Two technology objects of the same type can be assigned to each other.
- A derived type can be assigned to its basic type.
- A basic type cannot be assigned to its derived type.
- Assignment to a pointer, e.g. a VARIANT, is not possible.

### Comparison

References can be used in compare instructions. You can use a comparison with NULL to determine whether a tag has already been assigned to a reference. This is always advisable when the program flow does not explicitly ensure that a reference has been initialized.

Other comparisons are not possible.

### Examples

The following example shows the use of references in assignments and comparison instructions in SCL:

![Examples](images/159547567371_DV_resource.Stream@PNG-de-DE.png)

The following example shows the use in LAD:

![Examples](images/159547571339_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)

## Assignment attempt to a reference (S7-1500)

With the "?=" assignment attempt, you attempt to make an assignment to a reference tag.

The following assignment attempts are possible:

- Assignment attempt of a VARIANT to a reference
- Assignment attempt of a DB_ANY to the reference of a technology object

### Assignment attempt of a VARIANT to a reference

The data type of a reference tag is determined at the time of declaration. However, the data type of a VARIANT tag is determined at runtime. An implicit data type conversion is not permitted with reference tags. Therefore, to assign the two data types to each other, use the assignment attempt. With the assignment attempt, a check is made at runtime to find out whether the assigned tag is of the correct data type. If this is the case, the assignment is performed. If the instruction is executed successfully, there is a valid reference in the target tag, otherwise a NULL.

After the assignment attempt, you can check if the attempt was successful and, depending on the result, continue processing the program. In LAD and FBD, you can use the enable output ENO for the check. ENO returns the signal state "1" if the assignment attempt was successful. Only then are the subsequent instructions executed in the network.

In STL and SCL you can use the instructions "IS_NULL" or "NOT_NULL", for example, to check the success of an assignment attempt. See the examples below.

The following rules apply to the assignment attempt of VARIANT. VARIANT tags that do not match these rules return the value "NULL" at runtime.

- The VARIANT must point to an address in an optimized memory area.
- The VARIANT must not point to an address in a temporary memory area.
- If you want to assign a VARIANT to a reference to an ARRAY, the following rules apply:

  - The VARIANT tag must point to an ARRAY whose limits exactly match with those of the declared reference. A VARIANT tag which points to an ARRAY [0..9], does not match a tag REF_TO ARRAY[1..10].
  - Moreover, you should compile the blocks that form the value of the VARIANT tag once in a CPU of the S7-1500 series, firmware version V2.5.
- The assignment attempt of a VARIANT to the reference of a technology object is not possible.
- In SCL, assignment attempts cannot be used in multiple assignments (a := b := c;).

### Example

The following example shows how you can use references to symbolically read or write the value of a VARIANT tag directly. It is not necessary to copy the value with the "VariantGet" and "VariantPut" instructions.

![Example](images/99723640075_DV_resource.Stream@PNG-de-DE.png)

The VARIANT tag "variantTelegramData" can transfer data of type "Telegram1" and data of type "Telegram2".

An assignment attempt is used to test whether the data is of the type "Telegram1". If this is the case, the values "T" and "W" are assigned to the parameters "Info1" and "Info2".

Example in SCL:

![Example](images/101234058251_DV_resource.Stream@PNG-de-DE.png)

Example in LAD:

![Example](images/102973127691_DV_resource.Stream@PNG-de-DE.png)

### Assignment attempt of a DB_ANY to the reference of a technology object

A reference to a technology object always points to a specific technology object, e.g. REF_TO TO_SpeedAxis. If you want to assign a technology object via a tag of the type DB_ANY during runtime, you need to check whether the technology object matches the declared reference. To do this, use the assignment attempt. With the assignment attempt, a check is made during runtime to find out whether the technology object has the declared type. If this is the case, the assignment is performed. If this is executed successfully, there is a valid reference in the target tag, otherwise a NULL.

The following rules apply to the assignment attempt of a DB_ANY to the reference of a technology object:

- The DB_ANY must point to a technology object in an optimized memory area.
- Two technology objects of the same type can be assigned to each other.
- A derived type can be assigned to its basic type.
- A basic type cannot be assigned to its derived type.

You can find an example of using the assignment attempt for a technology object here:

[Example: Editing different axis types iteratively in a program loop](#example-editing-different-axis-types-iteratively-in-a-program-loop-s7-1500)

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)

## Transferring references as block parameters (S7-1500)

### Description

References can also be transferred as block parameters when calling functions or function blocks.

When you call a block in whose interface a reference is declared as a formal parameter, you can transfer a reference in the form of "REF()" or "#MyRef" as an actual parameter.

### Rules

The following rules apply to the transfer of references as block parameters:

- "REF()" can only be transferred as an actual parameter for an input parameter (Input) of a function.
- "REF()" cannot be transferred as an actual parameter to a block parameter of data type "VARIANT".
- The data type of the transferred tag must correspond exactly to the data type of the declared reference. No data type conversion is made.
- A reference to a derived technology object can be passed to a reference of the basic type.
- A reference to the basic type cannot be passed to a reference to a derived technology object.

### Example 1

The example below shows the interface of the "Callee" function. The interface contains several parameters that were declared as reference:

![Example 1](images/158005863563_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the call of this block in SCL and the parameter assignment for the declared references.

![Example 1](images/158005859595_DV_resource.Stream@PNG-de-DE.png)

### Example 2

The following example shows additional options for transferring references during a block call:

![Example 2](images/102664608267_DV_resource.Stream@PNG-de-DE.png)

The example shows two possibilities for the transfer:

- Transfer from the FB to the called FC:

  The input parameter "refStationData" is declared in the "FC StationData".

  "FB LineData" transfers `REF("ReceiveData1")` as an actual parameter (line 2 in the program code of the "FB LineData") during the call. "ReceiveData1" is a data block that is based on the PLC data type "typeStationData".
- Return from the FC to the calling FB:

  References with the same data type are declared in the interface of both blocks (in the example: `"refPoductionData"`).

  During the block call, the two references are assigned to each other (line 3 in the program code of the "FB LineData").

  The reference is initialized in the called "FC StationData" (line 2) and is written to the temporary data of the calling FB via the output parameter.

The example shows a section from the programming example "Return data to the calling block via reference". You can find the detailed program code under "See also".

---

**See also**

[Basic information about references (S7-1500)](#basic-information-about-references-s7-1500)
  
[Dereferencing (S7-1500)](#dereferencing-s7-1500)
  
[Example: Return data to the calling block via reference (S7-1500)](#example-return-data-to-the-calling-block-via-reference-s7-1500)

## Example: Transferring tags of different data types using references (S7-1500)

### Task

In the following application example, a production plant requests data. Different data is transferred to the plant depending on the type of data structure requested.

The data structures are mapped in two different PLC data types. The PLC data type "typeTelegram1" contains general information of the data type "CHAR", the PLC data type "typeTelegram2" contains the part ID of the data type "STRING". A data block is generated from each of the two PLC data types:

![Task](images/102060293259_DV_resource.Stream@PNG-de-DE.png)

### Example programs

The following figure shows the implementation of the task with and without the use of references in SCL:

![Example programs](images/102801379723_DV_resource.Stream@PNG-de-DE.png)

Because both blocks should be able to process different telegram formats, they have an in-out parameter (InOut) of data type "VARIANT" at which the telegrams are transferred as structured tags. Since the data type of a VARIANT parameter is not yet known at the time the program is created, it is not possible to directly access the parameter. Therefore, in both examples, "TypeOf" is used to determine which data type is currently available at the time of the call.

In the left block, the tag pending during runtime is now copied into a temporary tag of the corresponding data type using the "VariantGet" instruction, where it is described with the appropriate values. Then the structure is copied back to the "telegram" parameter using the "VariantPut" instruction. Copying has a detrimental effect on the program runtime and costs memory space.

In the right block, references are used to solve the task: The interface contains one reference parameter each for the two possible data structures. Depending on the currently pending tag, the matching reference is initialized using "AssignmentAttempt" and now points to the memory location of the tag in the data block. The values are now written directly to the data block.

The program code is clearer and easier to maintain. Because the structured tags do not have to be copied, the program runtime and memory requirements are not affected.

## Example: Return data to the calling block via reference (S7-1500)

### Task

In the following application example, we are configuring a production plant that consists of multiple stations. The stations are controlled by two CPUs which send data to a control CPU. This CPU must analyze for which station new data exists and execute the higher-level control tasks, for example, adding up the number of produced pieces.

The following figure shows the structure of the production plant:

![Task](images/102751672459_DV_resource.Stream@PNG-de-DE.png)

### Blocks in the example program

The program on the control CPU is structured as follows:

- PLC data type "typeStationData"

  The data of a station is mapped in the PLC data type "typeStationData". The PLC data type contains two lower-level PLC data types:

  - "typeGeneralInfo"

    The data type contains the station number.
  - "typeProductionData"

    The data type contains the number of pieces of the station.
- DB "ReceiveData"

  For communication between the CPUs, a "ReceiveData" data block of the type "typeStationData" is available for each CPU. The communication data is written to this block.
- "FB LineData"

  The FB runs a complete analysis of the production line. This includes, for example, adding up all unit counters of the individual stations. It also calls the "FC StationData" which, among other things, copies the received data from the "ReceiveData" DB to the global DB "Station".
- "FC StationData"

  The FC checks from which station new data was received and copies it to the corresponding ARRAY element in the global DB "Station". The ARRAY element is then returned as reference to the calling "FB LineData" for further processing.
- Global DB "Station"

  This DB contains the station information of the five stations. It is stored in an ARRAY of the type "typeStationData" from five components.

### Example program

The following figure shows the implementation of the task in SCL:

![Example program](images/102751676811_DV_resource.Stream@PNG-de-DE.png)

The "FB LineData" calls the "FC StationData" and transfers the reference to the receive data block when being called by `REF("ReceiveData")`.

By dereferencing to the transferred receive data block, the FC reads out the station number and writes it to the temporary tag "stationNo".

The production data from the receive data block is then copied to the corresponding ARRAY element in the global DB "Station".

This ARRAY element is returned as reference to the calling "FB LineData" via the "refProductionData" output.

It can subsequently access the transferred ARRAY element directly by dereferencing and thus update the unit counter for the entire production line.

---

**See also**

[Transferring references as block parameters (S7-1500)](#transferring-references-as-block-parameters-s7-1500)

## Example: Editing different axis types iteratively in a program loop (S7-1500)

### Example

The following example shows how you can iteratively edit different axis types in a FOR loop. In addition to the "SpeedAxis" type, derived axis types can also be processed in the loop, e.g. the "PositioningAxis" or "SynchronousAxis" axis types.

1. Create a global data block and declare an ARRAY of the "DB_ANY" data type. Any technology object can be passed to a DB_ANY in runtime. You can, for example, initialize the global data block in a startup OB by assigning specific technology objects to the ARRAY elements.

   ![Example](images/159829569931_DV_resource.Stream@PNG-de-DE.png)

   ![Example](images/159829569931_DV_resource.Stream@PNG-de-DE.png)
2. In the SCL block, declare a reference of the "REF_TO TO_SpeedAxis" data type. Axes of the "SpeedAxis" type as well as derived axes can be passed to the reference in runtime.
3. In the FOR loop, first there is a check for each technology object from the "DB_Axis" to determine whether it matches the declared reference. An assignment attempt is used for this.  
   If the assignment attempt is successful, the axis parameters are read and written.

   ![Example](images/169283093515_DV_resource.Stream@PNG-de-DE.png)

   ![Example](images/169283093515_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Assignment attempt to a reference (S7-1500)](#assignment-attempt-to-a-reference-s7-1500)

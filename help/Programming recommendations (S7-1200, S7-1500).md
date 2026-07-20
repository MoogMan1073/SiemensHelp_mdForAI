---
title: "Programming recommendations (S7-1200, S7-1500)"
package: ProgTIATIPPS1215enUS
topics: 8
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Programming recommendations (S7-1200, S7-1500)

This section contains information on the following topics:

- [The new S7-1200/1500 CPU functions and programming recommendations at a glance (S7-1200, S7-1500)](#the-new-s7-12001500-cpu-functions-and-programming-recommendations-at-a-glance-s7-1200-s7-1500)
- [Symbolic addressing (S7-1200, S7-1500)](#symbolic-addressing-s7-1200-s7-1500)
- [Indirect addressing of ARRAY components (S7-1200, S7-1500)](#indirect-addressing-of-array-components-s7-1200-s7-1500)
- [Using the DB_ANY data type (S7-1200, S7-1500)](#using-the-db_any-data-type-s7-1200-s7-1500)
- [Using PLC data types (UDT) (S7-1200, S7-1500)](#using-plc-data-types-udt-s7-1200-s7-1500)
- [Using MOVE instructions in STL (S7-1500)](#using-move-instructions-in-stl-s7-1500)
- [Using IEC timers and counters (S7-1200, S7-1500)](#using-iec-timers-and-counters-s7-1200-s7-1500)

## The new S7-1200/1500 CPU functions and programming recommendations at a glance (S7-1200, S7-1500)

### Higher performance

The S7-1200/1500 CPUs offer much higher performance than the S7-300/400 CPUs. When programming with STEP 7 V5.x, you were probably used to methods such as absolute addressing to achieve higher performance from the CPU and leaner program code. Due to the high performance provided by CPUs of the S7-1200/1500 series, this is now no longer necessary. If you wish to reuse the programming code created on an S7-300/400CPU on an S7-1200/1500 CPU, it will probably be necessary to modify the program code here and there in order to fully exploit the high performance.

In the paragraphs below, we would like to introduce some new programming options of the S7-1200/1500 CPUs.

You can find more tips on improving the performance here: [Increasing performance in STEP 7 (TIA Portal)](https://support.industry.siemens.com/cs/ww/en/view/37571372)

### Universal symbolism

The S7-1500 allows you to use the symbolism throughout the entire project. Using the auto-complete function, you are given context-dependent support for programming with symbols within the programming editors. The data elements, for example those in a data block, are assigned only a symbolic name in the declaration but no fixed address within the data block. This allows you to fully exploit the high performance of the S7-1500 when accessing these data elements. The absolute addresses of operands need not be known and access errors are avoided.

Your program code will be clearer due to the symbolism and you have to comment less. All points of use are automatically updated when a correction is made to the symbolism.

> **Note**
>
> **You can find additional information on the use of universal symbols at:**
>
> How can I address symbolically?
>
> [Symbolic addressing](#symbolic-addressing-s7-1200-s7-1500)

### Optimized block access

With optimized block access, the declared data elements are arranged automatically in the available memory area of the block in a way that makes optimal use of its capacity. The data is structured and saved in way that is optimal for the CPU used. The storage is left to the system. The data elements are assigned only a symbolic name in the declaration by which the tag within the block can be addressed. This allows you to increase the performance of the CPU. Access errors, from the HMI, for example, are not possible.

![Optimized block access](images/53556881291_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **You can find additional information on blocks with optimized access here:**
>
> [Blocks with optimized access](Programming%20basics.md#blocks-with-optimized-access)

### New data types

The new data types LWORD, LINT, ULINT, LTIME, LTOD, LDT and ARRAY (32-bit limit) offer much higher calculation accuracy when using mathematical functions. In the area of implicit and explicit data type conversion, you have more options in comparison to the CPUs of the S7-300/400 series.

> **Note**
>
> **You can find additional information on the new data types here:**
>
> [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

### PLC data types

PLC data types (UDT) are data structures that you define and that can be used multiple times within the program. The structure of a PLC data type is made up of several components, each of which can contain different data types. You define the type of components in the declaration of the PLC data type.

You can use the PLC data type as a base data type for defining tags and as a template for creating global data blocks. If you later make changes to the PLC data type, the changes are automatically updated at all points of use.

You can also symbolically access individual elements of an ARRAY within a PLC data type.

> **Note**
>
> **You can find additional information on the PLC data types here:**
>
> What does a PLC data type look like and how can I declare it in my program?
>
> - [PLC data types (UDT)](Data%20types.md#plc-data-types-udt)
>
> You can find programming recommendations for the PLC data type here:
>
> - [Using PLC data types (UDT)](#using-plc-data-types-udt-s7-1200-s7-1500)
> - [Using the DB_ANY data type](#using-the-db_any-data-type-s7-1200-s7-1500)

### Uniform instructions in all programming languages

You are provided with a uniform set of instructions in all programming languages (LAD, FBD, STL, SCL, and GRAPH).

### Slice access

Slice access gives you the option of specifically addressing areas within declared tags. You can implement symbolic access to a single bit up to the level of the tag. The single bit is then addressed absolutely.

> **Note**
>
> **You can find additional information on slice access here:**
>
> How can I address with slice access?
>
> - [Addressing areas of a tag with slice access](Programming%20basics.md#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
> - [Basics of block access](Programming%20basics.md#basics-of-block-access)

### Indirect addressing

Indirect addressing offers you the option of addressing operands whose address is not calculated until runtime. All programming languages provide general methods for indirect addressing, for example, via POINTER. In the STL and SCL programming languages, you can also use PEEK and POKE instructions.

> **Note**
>
> **You can find additional information on indirect addressing here:**
>
> [Indirect addressing](Programming%20basics.md#indirect-addressing-s7-1200-s7-1500)

### "Sample Library for Instructions"

You can use the "Sample Library for Instructions" to assist in programming. You will find practical and easy-to-understand programming examples for SIMATIC S7-1500 and S7-1200 in the LAD language here. You can simply insert the examples into your program and reuse them there.

> **Note**
>
> **You can find additional information on the program examples here:**
>
> [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500)

### Additional programming recommendations

You can find additional information about programming recommendations and a programming guide in the Siemens Industry online support under:

- FAQs: [Programming recommendations](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=0&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&Datakey=47071380&extranet=standard&groupid=4000002&viewreg=WW&nodeid0=29156492&objaction=csopen)
- Background and system descriptions in the [Programming Guideline and Programming Styleguide](https://support.industry.siemens.com/cs/document/81318674/programming-guideline-and-programming-styleguide-for-s7-1200-and-s7-1500?dti=0&lc=en-WW)

## Symbolic addressing (S7-1200, S7-1500)

### Advantages of symbolic addressing

The use of universally applied and meaningful symbols in the overall project makes the program code easier to read and understand.

This gives you the following advantages:

- You do not have to write detailed comments.
- Data access is faster.
- No errors occur when accessing data.
- You no longer have to work with absolute addresses.
- The assignment of the symbol to the memory address is monitored by STEP 7, which means all points of use are automatically updated when the name or the address of a tag changes.

### Programming in STEP 7 V5.x

STEP 7 V5.x already gave you the option to write a program that is easier to read by using descriptive names for operands and blocks. You did this by assigning the symbolic operands to memory addresses and blocks in the symbol table. In order for a change in the symbolism to also have an affect on the program code in the program editor, you had to use the "Operand priority" property to specify whether the symbol or the absolute value had priority.

The use of symbolic addressing allowed you to create a program with greater clarity. However, in some cases, such as when programming with user-defined data types (UDT), this could impair performance.

You could increase the performance by ignoring the symbolism in the UDT and using absolute addressing. This made it necessary, however, to know the data storage. Changes to the UDT were not automatically updated. Using absolute addressing, you could also access parts of a tag and edit these. The disadvantage of exclusively absolute addressing, however, was that the program code became cluttered after a certain level and you had to insert additional comments for better orientation.

### Procedure in STEP 7 TIA Portal

The S7-1500 CPU offers much higher performance than the S7-300/400 CPUs. To make full use of this high performance, we recommend that you enable optimized block access for all blocks and use symbolic addressing in the program code.

The program editor helps you work with symbols through context-sensitive input help, for example, auto-completion. Using it, you can easily access existing tags or instructions during programming.

### Programming example

The following example shows you how to symbolically access individual elements:

![Programming example](images/53320051723_DV_resource.Stream@PNG-de-DE.png)

You can use the tag names that you have defined in the block interface directly at the parameters of the TON instruction without knowing the absolute address of the tags.

---

**See also**

[Setting up block access](Programming%20basics.md#setting-up-block-access)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Addressing areas of a tag with slice access (S7-1200, S7-1500)](Programming%20basics.md#addressing-areas-of-a-tag-with-slice-access-s7-1200-s7-1500)
  
[Addressing PLC tags](Programming%20basics.md#addressing-plc-tags-1)
  
[Addressing tags in global data blocks](Programming%20basics.md#addressing-tags-in-global-data-blocks)
  
[Using autocompletion](Program%20editor.md#using-autocompletion)

## Indirect addressing of ARRAY components (S7-1200, S7-1500)

### Implementing ARRAY access in TIA Portal with a variable index

It is advisable to use an ARRAY when you want to process assembled data of the same data type. For addressing ARRAY elements, you can specify either constants or tags of the integer data type as index. Integers with lengths of up to 32 bits are allowed here.

With indirect addressing using a tag, the index is only calculated during program runtime. You can, for example, use a different index for each cycle in program loops. You can also access an ARRAY within a PLC data type (UDT).

This gives you the following advantages:

- No addressing is necessary with address registers or with self-assembled pointers, for example, an ANY pointer.
- More flexibility within your program.
- The variable index is available in all STEP 7 programming languages.
- It uses the existing names of data blocks and ARRAY tags (symbolic addressing). This improves readability of the program code.
- The start address of the ARRAY does not have to be known.
- The program code is easier to create and the compiler generates optimized program code.

### Procedure in STEP 7 V5.x

In STEP 7 V5.x, you had to use an address register with the help of a self-configured POINTER for indirect addressing of ARRAY elements. The following aspects had to be taken into consideration for this:

- The name of the ARRAY was not used. This reduced the readability of the program code and make additional comments necessary.
- The start address of the ARRAY had to be known to perform the addressing.

The SCL programming language already supported indirect addressing with variable index.

### Programming example in STEP 7 V5.x

The "Data_classic" data block is required for the following STL example. To address an element of the "Quantities" ARRAY, the following commands must be used:

| STL | Explanation |
| --- | --- |
| OPN "Data_classic" | // The "Data_classic" data block is called. |
| L #index | // The value of the local tag #index is loaded into accumulator 1. |
| SLD 3 | // Move bits 0 to 31 of accumulator 1 by 3 positions to the left.  // Fill the now empty bit places with zeros. |
| LAR1 | // Load address register 1 with contents of accumulator 1. |
| L DBW [AR1, P#10.0] | // Load the ARRAY element addressed with #index into accumulator 1.  // P#10.0 = Start address of the array |

### Programming example in STEP 7 TIA Portal

In the example below, you see the indirect addressing of an ARRAY element in STL in the TIA Portal.

Create a global data block for this purpose:

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_Quantities".
4. Select the type of the data block "ARRAY DB".
5. Select the "DINT" data type as ARRAY data type.
6. Specify "10" as high ARRAY limit.
7. Click "OK".​

   ![Programming example in STEP 7 TIA Portal](images/69365438987_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/69365438987_DV_resource.Stream@PNG-de-DE.png)

1. Create a function block and name it "FB_Quantities".
2. Declare the block interface as follows:

   ![Programming example in STEP 7 TIA Portal](images/69370503819_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/69370503819_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![Programming example in STEP 7 TIA Portal](images/69377962763_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/69377962763_DV_resource.Stream@PNG-de-DE.png)

   You need just one more program line for addressing an ARRAY element in the TIA Portal. The value of the ARRAY element #index is loaded directly from the data block into accumulator 1.
4. Call the "FB_Quantities" function block in OB1 and assign it an index between 0 - 10:

   ![Programming example in STEP 7 TIA Portal](images/69377971851_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/69377971851_DV_resource.Stream@PNG-de-DE.png)

Note the following to get the best performance:

- Declare tags that are used as an ARRAY index as an integer of less than or equal to 32 bits.
- Store intermediate results and ARRAY indexes in the temporary local data area.

---

**See also**

[Indirect addressing of ARRAY components (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-of-array-components-s7-300-s7-400)
  
[Basic information on ARRAY](Data%20types.md#basic-information-on-array)
  
[ARRAY](Data%20types.md#array)
  
[Indirect addressing in STL (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-in-stl-s7-300-s7-400)
  
[Indirect addressing in SCL (S7-300, S7-400)](Indirect%20addressing%20%28S7-300%2C%20S7-400%29.md#indirect-addressing-in-scl-s7-300-s7-400)

## Using the DB_ANY data type (S7-1200, S7-1500)

### Using the DB_ANY data type (S7-1200/1500)

The DB_ANY data type is used to identify any data block. For CPUs of the S7-1200/1500 series, you have the option of accessing a data block that is not yet available during programming. For this purpose, create a block parameter of the DB_ANY data type in the block interface of the accessing block. The data block name or a tag of data type DB_ANY which was previously assigned to the data block name is transferred to this parameter during runtime. You can symbolically process the content of a data block by means of the following instructions:

- VARIANT_TO_DB_ANY: Convert VARIANT to DB_ANY
- DB_ANY_TO_VARIANT: Convert DB_ANY to VARIANT

For more information about the instructions, refer to "Basic instructions > STL/SCL > Conversion operations > VARIANT".

The advantage of this procedure: You can create the program code before you know which data block will be processed.

The following objects are required for this example:

![Using the DB_ANY data type (S7-1200/1500)](images/103649833227_DV_resource.Stream@PNG-de-DE.png)

### Programming example

The following example shows you how to use the DB_ANY data type:

A punching machine can punch out a variety of geometric shapes. The punching jobs are transferred to the machine and there are specific job data for each individual job. The job data differ in their job type as well as in their values.

### Procedure - Creating the PLC data types

In the first job, a round hole is to be punched out of a piece of sheet metal. For the punching machine to be able to execute this job, it needs the center point coordinates and the radius of the hole. You can transfer these job data to the punching machine collectively in a PLC data type (UDT).

![Procedure - Creating the PLC data types](images/68792234123_DV_resource.Stream@PNG-de-DE.png)

Create the PLC data type "UDT_Hole" to transfer the job data:

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare the following lines within the PLC data type:

   X-coordinate > REAL

   Y-coordinate > REAL

   Diameter > REAL

   ![Procedure - Creating the PLC data types](images/103463506059_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the PLC data types](images/103463506059_DV_resource.Stream@PNG-de-DE.png)

A rectangle is to be punched out of a piece of sheet metal in the second job. For this job, you need two coordinates which define the upper left-hand point and the bottom right-hand point of the rectangle. You can transfer these job data to the punching machine collectively in the PLC data type "UDT_RectangleWindowStatic".

![Procedure - Creating the PLC data types](images/68792400779_DV_resource.Stream@PNG-de-DE.png)

Create the PLC data type "UDT_RectangleWindowStatic":

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare the following lines within the PLC data type:

   X1-coordinate > REAL

   Y1-coordinate > REAL

   X2-coordinate > REAL

   Y2-coordinate > REAL

   ![Procedure - Creating the PLC data types](images/68758734603_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the PLC data types](images/68758734603_DV_resource.Stream@PNG-de-DE.png)

The job data of the "UDT_RectangleWindowStatic" can only be used to punch out rectangles whose edges are aligned parallel to the x and y axis.

If you want to punch out a rectangle with different alignment, i.e., not parallel to the x and y axis, you need an additional PLC data type. In it, you can specify the height and width, for example, as well as the alignment of the rectangle to the x axis by means of an angle.

![Procedure - Creating the PLC data types](images/68792477835_DV_resource.Stream@PNG-de-DE.png)

Create the PLC data type "UDT_RectangleWindowFlexible":

1. Double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Declare the following lines within the PLC data type:

   X-coordinate > REAL

   Y-coordinate > REAL

   Height > REAL

   Width > REAL

   Angle > REAL

   ![Procedure - Creating the PLC data types](images/68761686283_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the PLC data types](images/68761686283_DV_resource.Stream@PNG-de-DE.png)

The x and y coordinates specify the center of the rectangle.

### Procedure - Creating the data blocks

In the next section, you will learn how to transfer simple geometric shapes whose job data you have defined in the PLC data types to the punching machine. The punch jobs are broken down into individual punches in the program code; these punches are then executed consecutively by the punching machine. The punching machine has a cross table on which a sheet metal has been firmly clamped. You can move a cross table along the x and/or y axis just as in a coordinate system. The cross table is moved by two motors. The tool has different dies to punch out shapes from the sheet metal, such as circles and rectangles of different sizes. The tool can also be rotated by up to 90 degrees to cut out rectangles at different alignments.

You now use the PLC data types to create several instance data blocks. The instance data block then includes the specific values, for example, for a hole.

Create the instance data block "DB_OrderHole":

1. Double-click on the "Add new block" command under the "Program blocks" folder.

   The "Add new block" dialog box opens.

1. Click the "Data block (DB)" button.
2. Specify the name "DB_OrderHole".
3. Select the data block "UDT_Hole" as the type.
4. Click "OK".

Enter the appropriate start values:

![Procedure - Creating the data blocks](images/103463502091_DV_resource.Stream@PNG-de-DE.png)

To manufacture a specific sheet metal part such as the side panel of a control cabinet, for example, the necessary geometric shapes are loaded to the punching machine. For this purpose, you need to create another data block which includes a list of data blocks.

Create the data block "DB_OrderList":

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_OrderList".
4. Select "Global DB" as the type of the data block.
5. Click "OK".

Create the following job list in the data block:

![Procedure - Creating the data blocks](images/103495270667_DV_resource.Stream@PNG-de-DE.png)

### Procedure - Creating the program code

A separate function is created for each job type. The punch jobs are broken down into individual punches here and collected in an ARRAY.

1. Create the PLC data type "UDT_Punch".
2. Double-click the "Add new data type" command under "PLC data types".

   A new PLC data type with the name "UserDataType_x" is created.
3. Rename the PLC data type "UDT_Punch".
4. Declare the following lines within the PLC data type:

   Tool > DINT

   x > REAL

   y > REAL

   w > REAL

   ![Procedure - Creating the program code](images/103794671883_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103794671883_DV_resource.Stream@PNG-de-DE.png)
5. Create the ARRAY data block "DB_PunchList".

   ![Procedure - Creating the program code](images/103469572363_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103469572363_DV_resource.Stream@PNG-de-DE.png)

To prepare the punch job for a hole and break it down into individual punches, create an SCL function and name it "FC_PrepareHole".

1. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/68762223883_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/68762223883_DV_resource.Stream@PNG-de-DE.png)
2. Write the following program code:

   ![Procedure - Creating the program code](images/103485616907_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103485616907_DV_resource.Stream@PNG-de-DE.png)

To prepare the punch job for a window, you need a function which combines four punch sequences into the punch job. Create an SCL function and name it "FC_PrepareWindowStatic".

1. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/103798156683_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103798156683_DV_resource.Stream@PNG-de-DE.png)
2. Write the following program code:

   ![Procedure - Creating the program code](images/103798164363_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103798164363_DV_resource.Stream@PNG-de-DE.png)

To prepare the punch job for a variable rectangle, you need a function which combines four punch sequences into the punch job. Create an SCL function and name it "FC_PrepareWindowFlexible".

1. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/103810916491_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103810916491_DV_resource.Stream@PNG-de-DE.png)
2. Write the following program code:

   ![Procedure - Creating the program code](images/103810925323_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103810925323_DV_resource.Stream@PNG-de-DE.png)

The punching machine should now start processing the jobs. If it is already processing the jobs, it should get the next job from the job list and prepare it.

1. Create an SCL function block.
2. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
3. Click the "Function block (FB)" button.
4. Specify the name "FB_PrepareNextOrder".
5. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/103626938507_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103626938507_DV_resource.Stream@PNG-de-DE.png)
6. Declare the global tag "AllOrdersDone":

   ![Procedure - Creating the program code](images/103809897611_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103809897611_DV_resource.Stream@PNG-de-DE.png)
7. Write the following program code:

   ![Procedure - Creating the program code](images/103628776587_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103628776587_DV_resource.Stream@PNG-de-DE.png)

The next job on the list is prepared by breaking down the current punch job into individual punches. The punching machine must be able to recognize which punch job it is processing.

1. Create an SCL function.
2. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
3. Click the "Function (FC)" button.
4. Specify the name "FC_PrepareOrder".
5. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/103495278347_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103495278347_DV_resource.Stream@PNG-de-DE.png)
6. Write the following program code:

SCL

#a : DB_ANY_TO_VARIANT(in := #Order, err => #Error);

CASE TypeOf(#a) OF

"UDT_Hole":

VariantGet(SRC := #a,

DST => #Hole);

"FC_PrepareHole"(#Hole);

"UDT_RectangleWindowStatic":

VariantGet(SRC := #a,

DST => #WindowStatic);

"FC_PrepareWindowStatic"(#WindowStatic);

"UDT_RectangleWindowFlexible":

VariantGet(SRC := #a,

DST => #WindowFlexible);

"FC_PrepareWindowFlexible"(#WindowFlexible);

ELSE;

END_CASE;

Call the SCL function "FC_PrepareOrder" in the SCL function block "FB_PrepareNextOrder"

![Procedure - Creating the program code](images/103628776587_DV_resource.Stream@PNG-de-DE.png)

Then, call the "FB_PrepareNextOrder" in OB1:

![Procedure - Creating the program code](images/103629957003_DV_resource.Stream@PNG-de-DE.png)

In addition to the option as described above, of loading the jobs with the help of the data block "DB_OrderList" to the punching machine in a pre-defined job, the job list could also be dynamically generated, for example. Or there is a selection of different job lists, for example. Then you have the option of loading a new job list to the punching machine after an job list has been processed. You need the following additional code for this.

Create an instance data block of the "FB_PrepareNextOrder" function block.

1. Double-click on the "Add new block" command under the "Program blocks" folder.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_FB_PrepareNextOrder".
4. Select the data block "FB_PrepareNextOrder" as the type.
5. Click "OK".

![Procedure - Creating the program code](images/103811980299_DV_resource.Stream@PNG-de-DE.png)

In order to be able to swap the job list, create an additional SCL function:

1. Create the STL function "FC_SwapOrderList".
2. Declare the block interface as follows:

   ![Procedure - Creating the program code](images/103649815563_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103649815563_DV_resource.Stream@PNG-de-DE.png)
3. Declare the global tag "NewModelNr":

   ![Procedure - Creating the program code](images/103811664267_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103811664267_DV_resource.Stream@PNG-de-DE.png)
4. Write the following program code:

   ![Procedure - Creating the program code](images/103649824395_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Creating the program code](images/103649824395_DV_resource.Stream@PNG-de-DE.png)

Create the data block "DB_OrderRepository":

1. Double-click on the "Add new block" command under the "Program blocks" folder.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_OrderRepository".
4. Select "Global DB" as the type of the data block.
5. Click "OK".

![Procedure - Creating the program code](images/103811989131_DV_resource.Stream@PNG-de-DE.png)

Then, call the "FC_SwapOrderList" in OB1:

![Procedure - Creating the program code](images/103813098763_DV_resource.Stream@PNG-de-DE.png)

### Result

This example shows you how to use the instruction "DB_ANY_TO_VARIANT: Convert DB_ANY to VARIANT" to determine the PLC data type of a data block and how to select and execute a suitable function based on this.

---

**See also**

[Addressing tags in global data blocks](Programming%20basics.md#addressing-tags-in-global-data-blocks)

## Using PLC data types (UDT) (S7-1200, S7-1500)

### Using a PLC data type

PLC data types (UDT) are data structures that you define yourself and that can be used multiple times in the program. The structure can be composed of multiple elements of different data types. You define the data types of the individual elements during the declaration of a PLC data type.

PLC data types are frequently used if an assembled data record with various data types is required and these are to be processed from different points in the program. For example, these could be:

- Data records for material tracking
- Parameter sets for a motor setting
- Recipes

The use of PLC data types provides you with the following benefits:

- The elements of a PLC data type can also be addressed indirectly, which means the address is variable and is not calculated until during runtime.
- Tags based on a PLC data type inherit all properties of the PLC data type. When there is a change to the PLC data type, all tags based on this PLC data type are therefore adapted automatically.
- Using universal symbolism makes the program easier to read, because the names of the individual elements of a PLC data type are displayed in the program.
- Optimum utilization of the high performance of an S7-1500 CPU.
- The PLC data type can be passed as a complete structure for a block call.
- A simplified call interface due to a lower number of parameters to be supplied.

### Procedure in STEP 7 V5.x

STEP 7 V5.x already gave you the option to create a data record as a structured tag using the STRUCT data type or a PLC data type (UDT). However, the performance was adversely affected by the use of symbolic addressing.

The declaration in the data blocks was mostly implemented as an anonymous structure. The blocks themselves were then programmed to pass the values of the structure as actual parameters and the calculated values were copied back into the structure. This enabled you to also pass the data block number and use absolute addressing in the block. The number of parameters that you had to supply was often very large. The actual data was stored in the data blocks and the calculated values were passed to other blocks. However, no symbolism was available when passing the data block tags.

### Programming example in STEP 7 TIA Portal

You can assign both a formula parameter and an actual parameter to a PLC data type. This means that you no longer have to declare individual parameters. If a block has an input parameter that is based on a PLC data type, you must transfer a tag of the same PLC data type as actual parameter.

The following example shows the call and the parameter assignment of a function block (FB) with two formal parameters:

1. To create a PLC data type, double-click the "Add new data type" command in the "PLC data types" folder in the project tree.

   A new declaration table for creating a PLC data type will be created and opened.
2. Rename the PLC data type to "UDT_Material".
3. Declare the following lines within the PLC data type:

   ArticleNumber > Data type: DINT

   ArticleName > Data type: STRING

   Amount > Data type: REAL

   Unit > Data type: STRING

   ![Programming example in STEP 7 TIA Portal](images/67954987147_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/67954987147_DV_resource.Stream@PNG-de-DE.png)

Use the PLC data type within a global data block. You can specify the PLC data type either directly as data type of the data block or within the data block as data type of a tag.

Create a global data block for this purpose:

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click the "Data block (DB)" button.
3. Specify the name "DB_MaterialBuffer".
4. Select the type of the data block "ARRAY DB".
5. Select the PLC data type "UDT_Material" as ARRAY data type.
6. Specify "1000" as high ARRAY limit.
7. Click "OK".

   ![Programming example in STEP 7 TIA Portal](images/67956941579_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/67956941579_DV_resource.Stream@PNG-de-DE.png)

At the function block call, interconnect the formal parameters with tags from the global data block "DB_MaterialBuffer".

1. Create an SCL function block and name it "FB_Material".
2. Declare the block interface as follows:

   ![Programming example in STEP 7 TIA Portal](images/68850678923_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/68850678923_DV_resource.Stream@PNG-de-DE.png)
3. Write the following program code:

   ![Programming example in STEP 7 TIA Portal](images/68850687755_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/68850687755_DV_resource.Stream@PNG-de-DE.png)
4. Call the "FB_Material" function block in OB1 and interconnect the formal parameters with tags of the global data block "DB_MaterialBuffer":

   ![Programming example in STEP 7 TIA Portal](images/68850811787_DV_resource.Stream@PNG-de-DE.png)

   ![Programming example in STEP 7 TIA Portal](images/68850811787_DV_resource.Stream@PNG-de-DE.png)

The material data are moved within the global data block "DB_MaterialBuffer".

---

**See also**

[Other useful information regarding structured PLC tags](Declaring%20PLC%20tags.md#other-useful-information-regarding-structured-plc-tags)
  
[Creating structured PLC tags](Declaring%20PLC%20tags.md#creating-structured-plc-tags)
  
[Rules for supplying block parameters](Programming%20basics.md#rules-for-supplying-block-parameters)
  
[Inspector window: Displaying UDTs](Configuring%20devices%20and%20networks.md#inspector-window-displaying-udts)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)
  
[PLC data types (UDT)](Data%20types.md#plc-data-types-udt)

## Using MOVE instructions in STL (S7-1500)

### Possible applications

You can now program with MOVE instructions in STL on an S7-1500 CPU.

This gives you the following advantages:

- The program structure is easier to create.
- The performance of the CPU increases.

### Programming in STEP 7 V5.x

In STEP 7 V5.x, you used the "BLKMOV: Move block" and "UBLKMOV: Move block uninterruptible" system functions to implement the MOVE functionality.

### Procedure in STEP 7 TIA Portal

The following new MOVE instructions are available in STEP 7 TIA Portal:

- MOVE: Move value
- MOVE_BLK: Move block
- MOVE_BLK_VARIANT: Move block
- UMOVE_BLK: Move block uninterruptible

### Programming example

The following example shows you how the "MOVE_BLK instruction works: Move block". An ARRAY block is copied into another ARRAY block:

![Programming example](images/53169995403_DV_resource.Stream@PNG-de-DE.png)

![Programming example](images/53175201035_DV_resource.Stream@PNG-de-DE.png)

Using the MOVE_BLK instruction, ten elements from "Array_1" of the "Data_DB" data block are copied into "Array_2" of the same data block.

---

**See also**

[MOVE: Move value (S7-1500)](STL%20%28S7-1500%29.md#move-move-value-s7-1500)
  
[MOVE_BLK: Move block (S7-1500)](STL%20%28S7-1500%29.md#move_blk-move-block-s7-1500)
  
[MOVE_BLK_VARIANT: Move block (S7-1500)](STL%20%28S7-1500%29.md#move_blk_variant-move-block-s7-1500)
  
[UMOVE_BLK: Move block uninterruptible (S7-1500)](STL%20%28S7-1500%29.md#umove_blk-move-block-uninterruptible-s7-1500)

## Using IEC timers and counters (S7-1200, S7-1500)

### Advantages of IEC timers and counters

The universal use of IEC timers and counters makes your program code more efficient.

This gives you the following advantages:

- The blocks can be called multiple times with newly generated instance data blocks.
- The IEC counters have a large counting range.
- Compared to S5 timers, IEC timers have better performance and greater time accuracy.

### Programming in STEP 7 V5.x

The S5 timers and counters in STEP 7 V5.x were addressed absolutely via a number. Due to this dependency on numbers, program blocks were not reusable with S5 timers and counters.

The value range of a timer was limited to 9990 seconds and that of a counter limited to a maximum of 999.

### Procedure in STEP 7 TIA Portal

You declare IEC timers and counters in the program block where they are called or needed. The IEC timer is a structure of data type IEC_TIMER, IEC_LTIMER, or TON_TIME and TON_LTIME, for example, which you can also declare as a local tag in a block. The IEC counter is a structure of data type IEC_SCOUNTER, IEC_USCOUNTER, etc.

### Programming examples in the TIA Portal

The following example shows you how to declare an IEC timer and IEC counter as a local tag:

![Programming examples in the TIA Portal](images/53004562443_DV_resource.Stream@PNG-de-DE.png)

The data of the TON IEC timer and the CTU IEC counter is stored as a local tag (multi-instance) in the block interface.​

You also have the option to create IEC timers and IEC counters within structures as multiple instances and to use them in your program code.

1. To do this, for example, create a global data block with an ARRAY of TON. The data type TON does not appear in the drop-down list, but can be entered manually:

   ![Programming examples in the TIA Portal](images/67988903179_DV_resource.Stream@PNG-de-DE.png)

   ![Programming examples in the TIA Portal](images/67988903179_DV_resource.Stream@PNG-de-DE.png)
2. Create a function block and drag the instruction "TON: Generate on-delay" to a network. Call the instance of IEC timer TON as follows:

   ![Programming examples in the TIA Portal](images/67994352011_DV_resource.Stream@PNG-de-DE.png)

   ![Programming examples in the TIA Portal](images/67994352011_DV_resource.Stream@PNG-de-DE.png)

### Call of a timer as multi-instance

If you want to use the IN parameter to start a timer as multi-instance, you must not initialize it beforehand in your program code. In this case, the timer called at the IN parameter no longer recognizes a positive signal edge and the timer is not started:

1. Create the timer "Time_1" as a multi-instance of the data type "TP_TIME" in the "Static" section of the block interface.

2. Write the following program code:

| STL | Explanation |
| --- | --- |
| A "Tag_Output" | // When the "Tag_Output" output receives the signal state 1, |
| = #​Time_1.IN | // the IN parameter of the multi-instance timer #Timer_1 is initialized with a positive signal edge. |
|  |  |
| CALL #Time_1 | // When the multi-instance timer is now called and the IN parameter queried again, the timer is not started because there is no new positive signal edge.    // Enter TIME as data type of the instruction. |
| time_type := Time |  |
| IN := "Tag_Output" |  |
| PT := T#30s |  |
| Q := "Tag_4" |  |
| ET := "Tag_ElapsedTime" |  |

This is why you must program the initialization of the multi-instance timer within the call.

| STL | Explanation |
| --- | --- |
| CALL #Time_1 | // The timer is called and started.    // Enter TIME as data type of the instruction. |
| time_type := Time |  |
| IN := "Tag_Output" |  |
| PT := T#30s |  |
| Q := "Tag_4" |  |
| ET := "Tag_ElapsedTime" |  |

---

**See also**

[Calling IEC timers (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#calling-iec-timers-s7-1200-s7-1500)
  
[Calling IEC counters (S7-1200, S7-1500)](SCL%20%28S7-1200%2C%20S7-1500%29.md#calling-iec-counters-s7-1200-s7-1500)
  
[Timers](Data%20types.md#timers)

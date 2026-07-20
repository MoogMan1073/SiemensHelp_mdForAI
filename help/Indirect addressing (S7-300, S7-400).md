---
title: "Indirect addressing (S7-300, S7-400)"
package: ProgIndiad34enUS
topics: 9
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Indirect addressing (S7-300, S7-400)

This section contains information on the following topics:

- [Indirect addressing via pointer (S7-300, S7-400)](#indirect-addressing-via-pointer-s7-300-s7-400)
- [Indirect addressing in SCL (S7-300, S7-400)](#indirect-addressing-in-scl-s7-300-s7-400)
- [Indirect addressing in STL (S7-300, S7-400)](#indirect-addressing-in-stl-s7-300-s7-400)

## Indirect addressing via pointer (S7-300, S7-400)

### Description

For indirect addressing, a special data format is required that contains the address and possibly also the range and the data type of an operand. This data format is referred to as pointer. The following types of pointer are available to you:

- POINTER (S7-300/400)
- ANY (S7-300/400)
- VARIANT (S7-1200/1500)

For more information on the pointer data type, refer to "See also".

> **Note**
>
> In SCL the use of the pointer data type is restricted. The only option available is to forward it to the called block.

### Example

The following example shows an indirect addressing with an area-internal pointer:

| Addressing in STL | Description |
| --- | --- |
| L P#10.0 | // Load pointer (P#10.0) in accumulator 1 |
| T MD20 | // Transfer pointer to the operand MD20 |
| L MW [MD20] | // Load MW10 in accumulator 1 |
| .... | // Any program |
| L MD [MD20] | // Load MD10 in accumulator 1 |
| .... | // Any program |
| = M [MD20] | // If RLO=1, set the memory bit M10.0 |
|  |  |

The pointer P#10.0 is transferred to the operand MD20. If the operand MD20 in square brackets is programmed, this will be replaced in runtime by the address that is contained in the pointer.

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Pointer](Data%20types.md#pointer)

## Indirect addressing in SCL (S7-300, S7-400)

This section contains information on the following topics:

- [Indirect addressing of data blocks (S7-300, S7-400)](#indirect-addressing-of-data-blocks-s7-300-s7-400)
- [Indirect addressing of tags (S7-300, S7-400)](#indirect-addressing-of-tags-s7-300-s7-400)
- [Indirect addressing of ARRAY components (S7-300, S7-400)](#indirect-addressing-of-array-components-s7-300-s7-400)

### Indirect addressing of data blocks (S7-300, S7-400)

#### Indirect addressing of data blocks in SCL

You can use the conversion function WORD_TO_BLOCK_DB to address data blocks indirectly. The DB number is therefore specified as the tag or expression with WORD data type.

#### Syntax

The following syntax is used for the indirect addressing of a data block:

WORD_TO_BLOCK_DB(Index).Operand ID (Address)

#### Examples

Example 1: The global tag "Address index" of WORD data type is used as the number of the DB.

Addressing in SCL

%M0.0:=WORD_TO_BLOCK_DB("Addressindex").DX(0,0);

%MW0:=WORD_TO_BLOCK_DB("Addressindex").DW(4);

Example 2: The global tag "Address index" of WORD data type is used as the number of the DB. The data element within the DB is also specified by means of an index:

Addressing in SCL

%M0.0:=WORD_TO_BLOCK_DB("Addressindex").DX(#i,#y);

%MW0:=WORD_TO_BLOCK_DB("Addressindex").DW(#y);

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Indirect addressing in STL (S7-1500)](Programming%20basics.md#indirect-addressing-in-stl-s7-1500-1)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)

### Indirect addressing of tags (S7-300, S7-400)

#### Indirect addressing of tags in SCL

Indirect addressing is performed similarly to absolute addressing. An offset in round brackets is specified instead of the address. The offset consists of one byte tag or, in the case of Boolean operands, one byte tag and one bit tag. Byte and bit tags must be of data type INT.

Timers and counters from the PLC tag table cannot be addressed indirectly in this way.

#### Syntax

The following syntax is used for the indirect addressing of a global tag:

Operand ID (Byte tag)

Operand ID (Byte tag.Bit tag)

The following syntax is used for the indirect addressing of a DB tag:

MyDB.OperandID(ByteTag)

MyDB.OperandID(ByteTag.BitTag)

#### Examples

Example 1: One of the input words 2 to 8 is set to 0, depending on the value of run tag i.

| Addressing in SCL |  |
| --- | --- |
| #i:=2;  FOR #i := 2 TO 8 DO   %IW(#i) := 0 ;  END_FOR; |  |

Example 2: One of the words 2 to 8 in DB10 is set to 0, depending on the value of run tag i.

| Addressing in SCL |  |
| --- | --- |
| #i:=2;  FOR #i := 2 TO 8 DO   %DB10.DW(#i) := 0 ;  END_FOR; |  |

### Indirect addressing of ARRAY components (S7-300, S7-400)

#### Description

For addressing the components of an ARRAY, you can enter tags of the integer data type as well as constants as the index. When using tags, the index will be calculated during runtime. You can, for example, use a different index for each cycle in program loops.

> **Note**
>
> The index tag [i] is read once at the start of the block call and cannot be changed by the called block while it is being processed.
>
> When you call a block and transfer an indirectly indexed ARRAY component ("&lt;DataBlock&gt;".&lt;ARRAY&gt;["i"]) to it as in/out parameter (InOut), you cannot change the value of the index tag while the block is being processed. The value is therefore always written back to the same ARRAY component from which it was read.

#### Syntax

The following syntax is used for the indirect indexing of a ARRAY:

"&lt;Data block&gt;".&lt;ARRAY&gt;["i"] // one-dimensional ARRAY

"&lt;Data block&gt;".&lt;ARRAY&gt;["i"] // one-dimensional ARRAY of STRUCT

"&lt;Data block&gt;".&lt;ARRAY&gt;["i"] // multidimensional ARRAY

"&lt;Data block&gt;".&lt;ARRAY&gt;["i"] // multidimensional ARRAY of STRUCT

The syntax has the following components:

| Part | Description |
| --- | --- |
| Data block | Name of the data block in which the ARRAY is located |
| ARRAY | Tag of the ARRAY data type |
| i, j | PLC tags of the integer data type that are used as pointers |
| a | Additional partial tag of the structure |

#### Examples

The following examples are based on SCL and demonstrate indirect indexing of an ARRAY component. MOTOR is a one-dimensional ARRAY_of_INT with three rows. VALUES is a PLC tag of data type "Integer".

| Addressing in SCL | Explanation |
| --- | --- |
| MOTOR[2] := VALUES; | (*Direct addressing: Assignment of VALUES to the second row of the ARRAY MOTOR*) |
| MOTOR["Tag_1"] := VALUES; | (*Indirect addressing: Assignment of VALUES to the rows of ARRAY MOTOR*) specified by "Tag_1" |
| #MOTOR["Tag_2"+"Tag_3"] := #Values; | (*Indirect addressing: Assignment of VALUES to the row of the MOTOR*) ARRAY specified by the expression "Tag_2"+"Tag_3" |

---

**See also**

[Addressing ARRAY components](Data%20types.md#addressing-array-components)

## Indirect addressing in STL (S7-300, S7-400)

This section contains information on the following topics:

- [Basic information about address registers (S7-300, S7-400)](#basic-information-about-address-registers-s7-300-s7-400)
- [Indirect addressing in STL (S7-300, S7-400)](#indirect-addressing-in-stl-s7-300-s7-400-1)

### Basic information about address registers (S7-300, S7-400)

#### Introduction

Two address registers are available for the indirect addressing of operands: address register 1 (AR1), and address register 2 (AR2). The address registers are equal and are 32 bits in length. You can store area-internal and cross-area pointers in the address registers. To define the address of an operand, you can call the stored data in the program.

Data is exchanged between the registers and the other available memory areas with the assistance of load and transfer instructions.

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
  
[Indirect addressing in STL (S7-300, S7-400)](#indirect-addressing-in-stl-s7-300-s7-400-1)
  
[Data exchange in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#data-exchange-in-stl-s7-300-s7-400-s7-1500)
  
[Load and transfer (S7-1500)](STL%20%28S7-1500%29.md#load-and-transfer-s7-1500)

### Indirect addressing in STL (S7-300, S7-400)

In STL, the following options are available for indirect addressing:

- Memory-indirect addressing
- Register-indirect area-internal addressing
- Register-indirect cross-area addressing

#### Memory-indirect addressing

In the case of memory-indirect addressing, you store the address in a tag. The tag can be of WORD or DWORD data type. The tag can be located in the memory areas "Data" (DB or DI), "Bit memory" (M) or "Temporary local data" (L).

The following example shows applications of memory-indirect addressing:

| Addressing in STL | Description |
| --- | --- |
| U E [MD 2] | // Execute an AND logic operation with a variable input bit. The address of the input bit is located in the memory double word MD2. |
| = DIX [DBD 2] | // Assign the RLO to a variable data bit. The address of the data bit is located in the data double word DBD2. |
| L EB [DID 4] | // Load a variable input byte to ACCU 1. The address of the input byte is located in the instance double word DID4. |
| AUF DB [LW 2] | // Open a variable data block. The number of the data block is located in the local data word LW2. |
|  |  |

#### Register-indirect area-internal addressing

Register-indirect addressing uses one of the address registers (AR1 or AR2) to pick up the address of the operand.

In the case of register-indirect, area-internal addressing, you index only the bit address and the byte address via the address register (e.g. `P#10.0`). You do not enter the memory area for which the address in the address register is to apply until during programming of the instruction. The address in the address register then moves to the memory area specified in the instruction.

Possible memory areas are "Inputs" (I), "Outputs" (Q), "I/O" (PI or PQ), "Bit memory" (M), "Temporary local data" (L) and "Data" (DB or DI).

When you enter register-indirect, area-internal addressing, specify an offset after the specification of the address register. This offset is added to the contents of the address register without changing the address register. This offset also has the format of a pointer. The specification of a pointer is mandatory and must be entered as constant (e.g. `P#0.0` or `P#2.0`).

The following example shows an application of register-indirect area-internal addressing:

| STL | Description |
| --- | --- |
| LAR1 P#10.0 | // Load pointer (P#10.0) to address register 1 |
| L IW [AR1, P#2.0] | // Increase content of address register 1 (P#10.0) by offset P#2.0.   // Load content of input word IW12 into accumulator 1 |
| L IW [AR1, P#0.0] | // Increase content of address register 1 (P#10.0) by offset P#0.0.   // Load content of input word IW10 into accumulator 1 |
|  |  |

#### Register-indirect cross-area addressing

In the case of register-indirect, cross-area addressing, use the address register to index the entire address of the operand, i.e., the bit address and byte address, as well as the memory area. Possible memory areas are "Inputs" (I), "Outputs" (Q), "I/O" (P), "Bit memory" (M), "Temporary local data" (L) and "Data" (DB or DI). In the instruction, program only the operand width. Possible operand widths are bit, byte, word, and double word.

The following example shows an application of register-indirect cross-area addressing:

|  |  |
| --- | --- |
| LAR1 P#M10.0 | // Load cross-area pointer (P#M10.0) to address register 1 |
| L W [AR1, P#2.0] | // Increase content of address register 1 (P#M10.0) by offset P#2.0.  // Load content of memory word "MW12" into accumulator 1 |
| LAR1 P#A10.0 | // Load cross-area pointer (P#A10.0) to address register 1 |
| L W [AR1, P#2.0] | // Add content of address register 1 (P#A10.0) by offset P#2.0  // Load content of output word QW12.0 into accumulator 1 |

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Indirect addressing of data blocks (S7-300, S7-400)](#indirect-addressing-of-data-blocks-s7-300-s7-400)
  
[Addressing ARRAY components](Data%20types.md#addressing-array-components)
  
[Basic information about address registers (S7-300, S7-400)](#basic-information-about-address-registers-s7-300-s7-400)
  
[Data exchange in STL (S7-300, S7-400, S7-1500)](Creating%20STL%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#data-exchange-in-stl-s7-300-s7-400-s7-1500)

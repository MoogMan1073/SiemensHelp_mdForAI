---
title: "Data types"
package: ProgDatentypenenUS
topics: 142
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Data types

This section contains information on the following topics:

- [Overview of the valid data types](#overview-of-the-valid-data-types)
- [Binary numbers](#binary-numbers)
- [Integers](#integers)
- [Floating-point numbers](#floating-point-numbers)
- [Timers](#timers)
- [Date and time](#date-and-time)
- [Character strings](#character-strings)
- [PLC data types (UDT)](#plc-data-types-udt)
- [Named value data types (S7-1500)](#named-value-data-types-s7-1500)
- [STRUCT data structure (anonymous structures)](#struct-data-structure-anonymous-structures)
- [ARRAY](#array)
- [Pointer](#pointer)
- [Parameter types](#parameter-types)
- [System data types](#system-data-types)
- [Hardware data types](#hardware-data-types)
- [Data type conversion for S7-1500: (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#data-type-conversion-for-s7-1500-s7-1500)
- [Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)
- [Data type conversion for S7-300, S7-400 (S7-300, S7-400)](Data%20type%20conversion%20for%20S7-300%2C%20S7-400%20%28S7-300%2C%20S7-400%29.md#data-type-conversion-for-s7-300-s7-400-s7-300-s7-400)

## Overview of the valid data types

### Validity of data type groups

The data type groups define the properties of the data, for example, the representation of the contents and the valid memory areas.

In the user program, you have the option of using pre-defined data types, which you add to the data types you have defined yourself. The following type categories are available for this:

- Elementary data types (binary numbers, integers, floating-point numbers, timers, DATE, TOD, LTOD CHAR, WCHAR)
- Complex data types (DT, LDT, DTL, STRING, WSTRING, ARRAY, STRUCT)
- User-defined data types (PLC data type (UDT))
- Pointer
- Parameter types
- System data types
- Hardware data types

The following tables show the availability of data types in the various S7-CPUs:

All tables
Binary numbers
Integers
Floating-point numbers
Timers
Date and time
Character strings
PLC data types (UDT)
Named value data types (NVT)
Anonymous structures
ARRAY
Pointer
Parameter types
System data types
Hardware data types

Binary numbers

| Binary numbers | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [BOOL](#bool-bit) | X | X | X |
| **Bit strings** |  |  |  |
| [BYTE](#byte) | X | X | X |
| [WORD](#word) | X | X | X |
| [DWORD](#dword) | X | X | X |
| [LWORD](#lword-s7-1500) | - | - | X |

Integers

| Integers | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [SINT](#sint-8-bit-integers-s7-1200-s7-1500) | - | X | X |
| [INT](#int-16-bit-integers) | X | X | X |
| [DINT](#dint-32-bit-integers) | X | X | X |
| [USINT](#usint-8-bit-integers-s7-1200-s7-1500) | - | X | X |
| [UINT](#uint-16-bit-integers-s7-1200-s7-1500) | - | X | X |
| [UDINT](#udint-32-bit-integers-s7-1200-s7-1500) | - | X | X |
| [LINT](#lint-64-bit-integers-s7-1500) | - | - | X |
| [ULINT](#ulint-64-bit-integers-s7-1500) | - | - | X |

Floating-point numbers

| Floating-point numbers | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [REAL](#real) | X | X | X |
| [LREAL](#lreal-s7-1200-s7-1500) | - | X | X |

Timers

| Timers | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [S5TIME](#s5time-duration-s7-300-s7-400) | X | - | X |
| [TIME](#time-iec-time) | X | X | X |
| [LTIME](#ltime-iec-time-s7-1500) | - | - | X |

Date and time

| Date and time | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [DATE](#date) | X | X | X |
| [TIME_OF_DAY (TOD)](#time_of_day-tod) | X | X | X |
| [LTOD (LTIME_OF_DAY)](#ltod-ltime_of_day-s7-1500) | - | - | X |
| [DT (DATE_AND_TIME)](#date_and_time-date-and-time-of-day) | X | - | X |
| [LDT](#ldt-date_and_ltime-s7-1500) | - | - | X |
| [DTL](#dtl-s7-1200-s7-1500) | - | X | X |

Character strings

| Character strings | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [CHAR](#char) | X | X | X |
| [WCHAR](#wchar-s7-1200-s7-1500) | - | X | X |
| [STRING](#string) | X | X | X |
| [WSTRING](#wstring-s7-1200-s7-1500) | - | X | X |

PLC data types (UDT)

| PLC data types (UDT) | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [PLC data type](#basics-of-plc-data-types-udt) (UDT) | X | X | X |

Named value data types (NVT)

| Named value data types (NVT) | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [Named value data types (NVT)](#basics-of-named-value-data-types-s7-1500) |  |  | X |

Anonymous structures

| Anonymous structures | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [STRUCT](#basic-information-on-struct) | X | X | X |

ARRAY

| ARRAY | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [ARRAY [....] of &lt;data type&gt;](#basic-information-on-array) | X | X | X |

Pointer

| Pointer | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [References](References%20%28S7-1500%29.md#basic-information-about-references-s7-1500) | - | - | X |
| [VARIANT](#basic-information-on-variant-s7-1200-s7-1500) | - | X | X |
| [POINTER](#pointer-s7-300-s7-400-s7-1500) | X | - | X |
| [ANY](#any-s7-300-s7-400-s7-1500) | X | - | X |

Parameter types

| Parameter types | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [TIMER](#parameter-types-1) | X | - | X |
| [COUNTER](#parameter-types-1) | X | - | X |
| [BLOCK_FC](#parameter-types-1) | X | - | X |
| [BLOCK_FB](#parameter-types-1) | X | - | X |
| [BLOCK_DB](#parameter-types-1) | X | - | - |
| [BLOCK_SDB](#parameter-types-1) | X | - | - |
| [VOID](#parameter-types-1) | X | X | X |
| [PARAMETER](#parameter-types-1) | - | X | X |

System data types

| System data types | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [IEC_TIMER](#system-data-types-1) | X<sup>1)</sup> | X | X |
| [IEC_LTIMER](#system-data-types-1) | - | - | X |
| [IEC_SCOUNTER](#system-data-types-1) | - | X | X |
| [IEC_USCOUNTER](#system-data-types-1) | - | X | X |
| [IEC_COUNTER](#system-data-types-1) | X<sup>2)</sup> | X | X |
| [IEC_UCOUNTER](#system-data-types-1) | - | X | X |
| [IEC_DCOUNTER](#system-data-types-1) | - | X | X |
| [IEC_UDCOUNTER](#system-data-types-1) | - | X | X |
| [IEC_LCOUNTER](#system-data-types-1) | - | - | X |
| [IEC_ULCOUNTER](#system-data-types-1) | - | - | X |
| [ERROR_STRUCT](#system-data-types-1) | - | X | X |
| [NREF](#system-data-types-1) | - | X | X |
| [CREF](#system-data-types-1) | - | X | X |
| [VREF](#system-data-types-1) | - | X | X |
| [SSL_HEADER](#system-data-types-1) | X | - | - |
| [CONDITIONS](#system-data-types-1) | - | X | - |
| [TADDR_Param](#system-data-types-1) | - | X | X |
| [TCON_Param](#system-data-types-1) | - | X | X |
| [HSC_Period](#system-data-types-1) | - | X | - |
| [AssocValues](#system-data-types-1) | - | X | X |
| <sup>1)</sup> For S7-300/400 CPUs, the data type is represented by TP, TON and TOF.   <sup>2)</sup> For S7-300/400 CPUs, the data type is represented by CTU, CTD and CTUD. |  |  |  |

Hardware data types

| Hardware data types | S7-300/400 | S7-1200 | S7-1500 |
| --- | --- | --- | --- |
| [REMOTE](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_ANY](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_DEVICE](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_DPMASTER](#hardware-data-types-derived-data-types) | - | - | X |
| [HW_DPSLAVE](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_IO](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_IOSYSTEM](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_SUBMODULE](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_MODULE](#hardware-data-types-derived-data-types) | - | - | X |
| [HW_INTERFACE](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_IEPORT](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_HSC](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_PWM](#hardware-data-types-derived-data-types) | - | X | X |
| [HW_PTO](#hardware-data-types-derived-data-types) | - | X | X |
| [EVENT_ANY](#hardware-data-types-derived-data-types) | - | X | X |
| [EVENT_ATT](#hardware-data-types-derived-data-types) | - | X | X |
| [EVENT_HWINT](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_ANY](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_DELAY](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_TOD](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_CYCLIC](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_ATT](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_PCYCLE](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_HWINT](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_DIAG](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_TIMEERROR](#hardware-data-types-derived-data-types) | - | X | X |
| [OB_STARTUP](#hardware-data-types-derived-data-types) | - | X | X |
| [PORT](#hardware-data-types-derived-data-types) | - | X | X |
| [RTM](#hardware-data-types-derived-data-types) | - | X | X |
| [PIP](#hardware-data-types-derived-data-types) | - | - | X |
| [CONN_ANY](#hardware-data-types-derived-data-types) | - | X | X |
| [CONN_PRG](#hardware-data-types-derived-data-types) | - | X | X |
| [CONN_OUC](#hardware-data-types-derived-data-types) | - | X | X |
| [CONN_R_ID](#hardware-data-types-derived-data-types) | - | - | X |
| [DB_ANY](#hardware-data-types-derived-data-types) | - | X | X |
| [DB_WWW](#hardware-data-types-derived-data-types) | - | X | X |
| [DB_DYN](#hardware-data-types-derived-data-types) | - | X | X |

> **Note**
>
> Depending on the CPU version, the actually valid data types can deviate slightly from the table.

## Binary numbers

This section contains information on the following topics:

- [BOOL (bit)](#bool-bit)
- [Bit strings](#bit-strings)

### BOOL (bit)

#### Description

An operand of data type BOOL represents a bit value and contains one of the following values:

- TRUE
- FALSE

The following table shows the properties of data type BOOL:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 1 | Boolean | FALSE or TRUE  BOOL#0 or BOOL#1  BOOL#FALSE or BOOL#TRUE | TRUE  BOOL#1  BOOL#TRUE |
| Unsigned integers (decimal system) | 0 or 1 | 1 |  |
| Binary numbers | 2#0 or 2#1 | 2#0 |  |
| Octal numbers | 8#0 or 8#1 | 8#1 |  |
| Hexadecimal numbers | 16#0 or 16#1 | 16#1 |  |

> **Note**
>
> **Applies to CPUs of the S7-1500 series**
>
> For a block with the block property "Optimized block access", the bit has a length of 1 byte.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### Bit strings

This section contains information on the following topics:

- [BYTE](#byte)
- [WORD](#word)
- [DWORD](#dword)
- [LWORD (S7-1500)](#lword-s7-1500)

#### BYTE

##### Description

An operand of data type BYTE is a bit string of 8 bits.

The following table shows the properties of data type BYTE:

| Length (bits) | Format | Value range | Examples of value input |  |
| --- | --- | --- | --- | --- |
| Constants | Absolute and symbolic addresses |  |  |  |
| 8 | Integers<sup>1)</sup> (decimal system) | Signed integers: -128 to +127  Unsigned integers: 0 to 255 | - 15 - BYTE#15 - BYTE#10#15 - B#15 | - IB2 - MB10 - DB1.DBB4 - Tag_Name |
| Binary numbers | 2#0 to 2#1111_1111 | - 2#0000_1111 - BYTE#2#0000_1111 - B#2#0000_1111 |  |  |
| Octal numbers | 8#0 to 8#377 | - 8#17 - BYTE#8#17 - B#8#17 |  |  |
| Hexadecimal numbers | 16#0 to 16#FF | - 16#0F - BYTE#16#0F - B#16#0F |  |  |
| <sup>1)</sup> The value range depends on the relevant interpretation or conversion. |  |  |  |  |

> **Note**
>
> The BYTE data type cannot be compared for more than or less than. It can only be supplied with the same decimal data that can be processed by the SINT and USINT data types.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

#### WORD

##### Description

An operand of data type WORD is a bit string of 16 bits.

The following table shows the properties of data type WORD:

| Length (bits) | Format | Value range | Examples of value input |  |
| --- | --- | --- | --- | --- |
| Constants | Absolute and symbolic addresses |  |  |  |
| 16 | Integers (decimal system) | Signed integers: -32_768 to +32_767  Unsigned integers: 0 to 65_535 | - 61_680 - WORD#61_680 - WORD#10#61_680 - W#61_680 | - MW10 - DB1.DBW2 - Tag_Name |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111 | - 2#1111_0000_1111_0000 - WORD#2#1111_0000_1111_0000 - W#2#1111_0000_1111_0000 |  |  |
| Octal numbers | 8#0 to 8#177_777 | - 8#170_360 - WORD#8#170_360 - W#8#170_360 |  |  |
| Hexadecimal numbers | 16#0 to 16#FFFF | - 16#F0F0 - WORD#16#F0F0 - W#16#F0F0 |  |  |
| BCD | C#0 to C#999 | C#55 |  |  |
| Decimal sequence | B#(0, 0) to B#(255, 255) | B#(127, 200) |  |  |

> **Note**
>
> The WORD data type cannot be compared for more than or less than. It can only be supplied with the same decimal data that can be processed by the INT and UINT data types.
>
> The "BCD" format is not possible in SCL.
>
> The "Decimal sequence" is not possible in SCL and GRAPH.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

#### DWORD

##### Description

An operand of data type DWORD is a bit string of 32 bits.

The following table shows the properties of data type DWORD:

| Length (bits) | Format | Value range | Examples of value input |  |
| --- | --- | --- | --- | --- |
| Constants | Absolute and symbolic addresses |  |  |  |
| 32 | Integers (decimal system) | Signed integers: -2_147_483_647 to +2_147_483_647  Unsigned integers: 0 to 4_294_967_295 | - +15_793_935 - DWORD#+15_793_935 - DWORD#10#+15_793_935 - DW#+15_793_935 | - MD10 - DB1.DBD8 - Tag_Name |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111_1111_1111_1111_1111 | - 2#0000_0000_1111_0000_1111_1111_0000_1111 - DWORD#2#0000_0000_1111_0000_1111_1111_0000_1111 - DW#2#0000_0000_1111_0000_1111_1111_0000_1111 |  |  |
| Octal numbers | 8#0 to 8#37_777_777_777 | - 8#74_177_417 - DWORD#8#74_177_417 - DW#8#74_177_417 |  |  |
| Hexadecimal numbers | 16#0000_0000 to 16#FFFF_FFFF | - 16#00F0_FF0F - DWORD#16#00F0_FF0F - DW#16#00F0_FF0F |  |  |
| Decimal sequence | B#(0, 0, 0, 0) to B#(255, 255, 255, 255) | B#(127, 200, 127, 200) |  |  |

> **Note**
>
> The DWORD​ data type cannot be compared for more than or less than. It can only be supplied with the same decimal data that can be processed by the DINT and UDINT data types.
>
> The "Decimal sequence" is not possible in SCL and GRAPH.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

#### LWORD (S7-1500)

##### Description

An operand of data type LWORD is a bit string of 64 bits.

The following table shows the properties of data type LWORD:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 64 | Integers (decimal system) | Signed integers: -9_223_372_036_854_775_808 to +9_223_372_036_854_775_807  Unsigned integers: 0 to 18_446_744_073_709_551_615 | - +26_123_590_360_715 - LWORD#+26_123_590_360_715 - LWORD#10#+26_123_590_360_715 - LW#+26_123_590_360_715 |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111 | - 2#0000_0000_0000_0000_0000_1011_1110_0001_0010_1111_0101_0010_1101_1110_1000_1011 - LWORD#2#0000_0000_0000_0000_0000_1011_1110_0001_0010_1111_0101_0010_1101_1110_1000_1011 - LW#2#0000_0000_0000_0000_0000_1011_1110_0001_0010_1111_0101_0010_1101_1110_1000_1011 |  |
| Octal numbers | 8#0 to 8#1_777_777_777_777_777_777_777 | - 8#13_724_557_213 - LWORD#8#13_724_557_213 - LW#8#13_724_557_213 |  |
| Hexadecimal numbers | 16#0000_0000 to 16#FFFF_FFFF_FFFF_FFFF | - 16#0000_0000_5F52_DE8B - LWORD#16#0000_0000_5F52_DE8B - LW#16#0000_0000_5F52_DE8B |  |
| Decimal sequence | B#(0, 0, 0, 0, 0, 0, 0, 0) to B#(255, 255, 255, 255, 255, 255, 255, 255) | B#(127, 200, 127, 200, 127, 200, 127, 200) |  |

> **Note**
>
> The LWORD data type cannot be compared for more than or less than. It can only be supplied with the same decimal data that can be processed by the LINT and ULINT data types.
>
> The "Decimal sequence" is not possible in SCL and GRAPH.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

## Integers

This section contains information on the following topics:

- [SINT (8-bit integers) (S7-1200, S7-1500)](#sint-8-bit-integers-s7-1200-s7-1500)
- [USINT (8-bit integers) (S7-1200, S7-1500)](#usint-8-bit-integers-s7-1200-s7-1500)
- [INT (16-bit integers)](#int-16-bit-integers)
- [UINT (16-bit integers) (S7-1200, S7-1500)](#uint-16-bit-integers-s7-1200-s7-1500)
- [DINT (32-bit integers)](#dint-32-bit-integers)
- [UDINT (32-bit integers) (S7-1200, S7-1500)](#udint-32-bit-integers-s7-1200-s7-1500)
- [LINT (64-bit integers) (S7-1500)](#lint-64-bit-integers-s7-1500)
- [ULINT (64-bit integers) (S7-1500)](#ulint-64-bit-integers-s7-1500)

### SINT (8-bit integers) (S7-1200, S7-1500)

#### Description

An operand of data type SINT (Short INT) has a length of 8 bits and consists of two components: a sign and a numerical value in the two's complement. The signal states of bits 0 to 6 represent the number value. The signal state of bit 7 represents the sign. The sign may assume "0" for the positive, or "1" for the negative signal state.

An operand of data type SINT occupies one BYTE in the memory.

The following table shows the properties of data type SINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 8 | Signed integers (decimal system) | -128 to +127 | - +44 - SINT#+44 - SINT#10#+44  The value range extends to a maximum of SINT#255 when using the type SINT#. This value is interpreted as an integer with -1. |
| Binary numbers (only positive) | 2#0 to 2#0111_1111 | - 2#0010_1100 - SINT#2#0010_1100 - SINT#2#10 |  |
| Octal numbers (only positive) | 8#0 to 8#177 | - 8#54 - SINT#8#54 |  |
| Hexadecimal numbers (only positive) | 16#0 to 16#7F | - 16#2C - SINT#16#2C  The value range extends to a maximum of SINT#16#FF when using the type SINT#. This value is interpreted as an integer with -1. |  |

#### Example

The following figure shows the integer +44 as a binary number:

![Example](images/37854793483_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### USINT (8-bit integers) (S7-1200, S7-1500)

#### Description

An operand of data type USINT (Unsigned Short INT) has a length of 8 bits and contains unsigned numerical values:

An operand of data type USINT occupies one BYTE in the memory.

The following table shows the properties of data type USINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 8 | Unsigned integers (decimal system) | 0 to 255 | - 78 - USINT#78 - USINT#10#78 |
| Binary numbers | 2#0 to 2#1111_1111 | - 2#0100_1110 - USINT#2#0100_1110 - USINT#2#10 |  |
| Octal numbers | 8#0 to 8#377 | - 8#116 - USINT#8#116 |  |
| Hexadecimal numbers | 16#0 to 16#FF | - 16#4E - USINT#16#4E |  |

#### Example

The following figure shows the integer 78 as a binary number:

![Example](images/37883287435_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### INT (16-bit integers)

#### Description

An operand of data type INT has a length of 16 bits and consists of two components: a sign and a numerical value in the two's complement. The signal states of bits 0 to 14 represent the number value. The signal state of bit 15 represents the sign. The sign may assume "0" for the positive, or "1" for the negative signal state.

An operand of data type INT occupies two BYTE in the memory.

The following table shows the properties of data type INT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 16 | Signed integers (decimal system) | -32_768 to +32_767 | - +3_785 - INT#+3_785 - INT#10#+3_785 |
| Binary numbers (only positive) | 2#0 to 2#0111_1111_1111_1111 | - 2#0000_1110_1100_1001 - INT#2#0000_1110_1100_1001 - INT#2#10 |  |
| Octal numbers (only positive) | 8#0 to 8#7_7777 | - 8#7311 - INT#8#7311 |  |
| Hexadecimal numbers (only positive) | 16#0 to 16#7FFF | - 16#0EC9 - INT#16#0EC9 |  |

#### Example

The following figure shows the integer +3785 as a binary number:

![Example](images/63680045451_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### UINT (16-bit integers) (S7-1200, S7-1500)

#### Description

An operand of data type UINT (Unsigned INT) has a length of 16 bits and contains unsigned numerical values.

An operand of data type UINT occupies two BYTE in the memory.

The following table shows the properties of data type UINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 16 | Unsigned integers (decimal system) | 0 to 65_535 | - 65_295 - UINT#65_295 - UINT#10#65_295 |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111 | - 2#1111_1111_0000_1111 - UINT#2#1111_1111_0000_1111 - UINT#2#10 |  |
| Octal numbers | 8#0 to 8#17_7777 | - 8#17_7417 - UINT#8#17_7417 |  |
| Hexadecimal numbers | 16#0 to 16#FFFF | - 16#FF0F - UINT#16#FF0F |  |

#### Example

The following figure shows the integer 65295 as a binary number:

![Example](images/37884116875_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### DINT (32-bit integers)

#### Description

An operand of data type DINT (Double INT) has a length of 32 bits and consists of two components: a sign and a numerical value in the two's complement. The signal states of bits 0 to 30 represent the number value. The signal state of bit 31 represents the sign. The sign may assume "0" for the positive, or "1" for the negative signal state.

An operand of data type DINT occupies four BYTE in the memory.

The following table shows the properties of data type DINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 32 | Signed integers (decimal system) | -2_147_483_648 to +2_147_483_647 | - +125_790 - DINT#+125_790 - DINT#10#+125_790 - L#275 |
| Binary numbers (only positive) | 2#0 to 2#0111_1111_1111_1111_1111_1111_1111_1111 | - 2#0000_0000_0000_0001_1110_1011_0101_1110 - DINT#2#0000_0000_0000_0001_1110_1011_0101_1110 - DINT#2#10 |  |
| Octal numbers (only positive) | 8#0 to 8#177_7777_7777 | - 8#36_5536 - DINT#8#36_5536 |  |
| Hexadecimal numbers | 16#0 to 16#7FFF_FFFF | - 16#0001_EB5E - DINT#16#0001_EB5E |  |

#### Example

The following figure shows the integer +125790 as a binary number:

![Example](images/37855362827_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### UDINT (32-bit integers) (S7-1200, S7-1500)

#### Description

An operand of data type UDINT (Unsigned Double INT) has a length of 32 bits and contains unsigned numerical values.

An operand of data type UDINT occupies four BYTE in the memory.

The following table shows the properties of data type UDINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 32 | Unsigned integers (decimal system) | 0 to 4_294_967_295 | - 4_042_322_160 - UDINT#4_042_322_160 - UDINT#10#4_042_322_160 |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111_1111_1111_1111_1111 | - 2#1111_0000_1111_0000_1111_0000_1111_0000 - UDINT#2#1111_0000_1111_0000_1111_0000_1111_0000 - UDINT#2#10 |  |
| Octal numbers | 8#0 to 8#377_7777_7777 | - 8#360_7417_0360 - UDINT#8#360_7417_0360 |  |
| Hexadecimal numbers | 16#0 to 16#FFFF_FFFF | - 16#F0F0_F0F0 - UDINT#16#F0F0_F0F0 |  |

#### Example

The following figure shows the integer 4042322160 as a binary number:

![Example](images/37885138571_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### LINT (64-bit integers) (S7-1500)

#### Description

An operand of data type LINT (Long INT) has a length of 64 bits and consists of two components: a sign and a numerical value in the two's complement. The signal states of bits 0 to 62 represent the number value. The signal state of bit 63 represents the sign. The sign may assume "0" for the positive, or "1" for the negative signal state.

An operand of data type LINT occupies eight BYTE in the memory.

The following table shows the properties of data type LINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 64 | Signed integers (decimal system) | -9_223_372_036_854_775_808 to +9_223_372_036_854_775_807 | - +154_325_790_816_159 - LINT#+154_325_790_816_159 - LINT#10#+154_325_790_816_159 |
| Binary numbers (only positive) | 2#0 to 2#0111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111 | - 2#0000_0000_0000_0000_1000_1100_0101_1011_1100_0101_1111_0000_1111_0111_1001_1111 - LINT#2#0000_0000_0000_0000_1000_1100_0101_1011_1100_0101_1111_0000_1111_0111_1001_1111 - LINT#2#10 |  |
| Octal numbers (only positive) | 8#0 to 8#7_7777_7777_7777_7777_7777 | - 8#4305_5705_7417_3637 - LINT#8#4305_5705_7417_3637 |  |
| Hexadecimal numbers (only positive) | 16#0 to 16#7FFF_FFFF_FFFF_FFFF | - 16#0000_8C5B_C5F0_F79F - LINT#16#0000_8C5B_C5F0_F79F |  |

#### Example

The following figure shows the integer +154325790816159 as a binary number:

![Example](images/66825611915_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### ULINT (64-bit integers) (S7-1500)

#### Description

An operand of data type ULINT (Unsigned Long INT) has a length of 64 bits and contains unsigned numerical values.

An operand of data type ULINT occupies eight BYTE in the memory.

The following table shows the properties of data type ULINT:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 64 | Unsigned integers (decimal system) | 0 to 18_446_744_073_709_551_615 | - 154_325_790_816_159 - ULINT#154_325_790_816_159 - ULINT#10#154_325_790_816_159 |
| Binary numbers | 2#0 to 2#1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111_1111 | - 2#0000_0000_0000_0000_1000_1100_0101_1011_1100_0101_1111_0000_1111_0111_1001_1111 - ULINT#2#0000_0000_0000_0000_1000_1100_0101_1011_1100_0101_1111_0000_1111_0111_1001_1111 - ULINT#2#10 |  |
| Octal numbers | 8#0 to 8#17_7777_7777_7777_7777_7777 | - 8#4305_5705_7417_3637 - ULINT#8#4305_5705_7417_3637 |  |
| Hexadecimal numbers | 16#0 to 16#FFFF_FFFF_FFFF_FFFF | - 16#0000_8C5B_C5F0_F79F - ULINT#16#0000_8C5B_C5F0_F79F |  |

#### Example

The following figure shows the integer 154325790816159 as a binary number:

![Example](images/46682480907_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

## Floating-point numbers

This section contains information on the following topics:

- [REAL](#real)
- [LREAL (S7-1200, S7-1500)](#lreal-s7-1200-s7-1500)
- [Invalid floating-point numbers](#invalid-floating-point-numbers)

### REAL

#### Description

Operands of the data type REAL have a length of 32 bits and are used to represent floating-point numbers. An operand of the REAL data type consists of the following three components:

- Sign: The sign is determined by the signal state of bit 31. The bit 31 assume the value "0" (positive) or "1" (negative).
- 8-bit exponents to basis 2: The exponent is increased by a constant (base, +127), so that it has a value range of 0 to 255.
- 23-bit mantissa: Only the fraction part of the mantissa is shown. The integer part of the mantissa is always 1 with normalized floating-point numbers and is not stored.

The REAL data type is processed with a precision of 6 digits.

The following figure shows the structure of the REAL data type:

![Description](images/63681883915_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> With floating-point numbers, only the precision defined by the IEEE754 standard is stored. Additionally specified decimals are rounded off according to IEEE754.
>
> The number of decimal places may decrease for frequently nested arithmetic calculations.
>
> If more decimal places are specified than can be stored by the data type, the number is rounded to the value corresponding to the precision allowed by this value range.

The following table shows the properties of data type REAL:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 32 | Floating-point numbers according to IEEE754 | -3.402823e+38 to -1.175495e-38  ±0.0  +1.175495e-38 to +3.402823e+38 | 1.0e-5; REAL#1.0e-5 |
| Floating-point numbers | 1.0; REAL#1.0 |  |  |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)
  
[Calculating with floating-point numbers (REAL and LREAL) in SCL](Creating%20SCL%20programs.md#calculating-with-floating-point-numbers-real-and-lreal-in-scl)

### LREAL (S7-1200, S7-1500)

#### Description

Operands of the data type LREAL have a length of 64 bits and are used to represent floating-point numbers. An operand of the LREAL data type consists of the following three components:

- Sign: The sign is determined by the signal state of bit 63. The bit 63 assumes the value "0" (positive) or "1" (negative).
- 11-bit exponents to base 2: The exponent is increased by a constant (base, +1023), so that it has a value range of 0 to 2047.
- 52-bit mantissa: Only the fraction part of the mantissa is shown. The integer part of the mantissa is always 1 with normalized floating-point numbers and is not stored.

The LREAL data type is processed with a precision of 15 digits.

The following figure shows the structure of the LREAL data type:

![Description](images/15078002187_DV_resource.Stream@PNG-en-US.png)

The following table shows the properties of data type LREAL:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 64 | Floating-point numbers according to IEEE754 | -1.7976931348623157e+308 to -2.2250738585072014e-308  ±0.0  +2.2250738585072014e-308 to +1.7976931348623157e+308 | 1.0e-5; LREAL#1.0e-5 |
| Floating-point numbers | 1.0; LREAL#1.0 |  |  |

> **Note**
>
> With floating-point numbers, only the precision defined by the IEEE754 standard is stored. Additionally specified decimals are rounded off according to IEEE754.
>
> The number of decimal places may decrease for frequently nested arithmetic calculations.
>
> If more decimal places are specified than can be stored by the data type, the number is rounded to the corresponding value of the precision allowed by this value range .

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)
  
[Calculating with floating-point numbers (REAL and LREAL) in SCL](Creating%20SCL%20programs.md#calculating-with-floating-point-numbers-real-and-lreal-in-scl)

### Invalid floating-point numbers

#### Description

We distinguish between four number ranges for data types REAL and LREAL:

- normalized numbers stored with full accuracy
- denormalized numbers not stored with full accuracy
- Infinite numbers: +Inf/-Inf (infinity)
- Invalid numbers: NaN (Not a Number)

> **Note**
>
> Floating-point numbers are stored as specified by the IEEE754 standard. Results of conversion or arithmetic functions with a denormalized, infinite or NaN (Not a Number) floating point depend on the CPU.

If you are not working with normalized floating-point numbers in mathematical functions, the result will show significant differences depending on the series of the CPU which you are using.

A CPU cannot calculate with denormalized floating-point numbers, with the exception of older CPU versions of the S7-300 and S7-400 series. The bit pattern of a denormalized number is interpreted as a zero. If the result of calculation falls into this range, it is continued with zero; the status bits OV and OS are set (number range undershoot).

Even though the values of invalid floating-point numbers can only be displayed with limited accuracy for mathematical functions, numbers with an exponent of -39 (e.g. 2.4408e-039) can be monitored in the TIA Portal and therefore do not necessarily represent a faulty result. This means that floating-point values may be located outside the range of valid numerical values.

> **Note**
>
> **The following applies to CPUs of the series S7-1200 V1, V2 and V3:**
>
> The comparison operation "Equal" uses the bit pattern of the invalid floating-point number. If two "NaN numbers" with the same bit pattern are compared, the output of the "Equal" comparison operation returns the result TRUE.

> **Note**
>
> **The following applies to CPUs of the S7-1200 V4 and S7-1500 series:**
>
> If two invalid numbers (NaN) are compared with each other, the result is always FALSE, regardless of the bit pattern of the invalid number or the relation (&gt;, &gt;, ...).

> **Note**
>
> **Comparison of denormalized floating-point numbers**
>
> For the comparison operation "Equal" with two denormalized floating-point numbers, the output for CPUs of the S7-300/400 series is set to the signal state "0" and for CPUs of the S7-1200/1500 series to the signal state "1".

If the input variables of a mathematical function represent an invalid floating-point number, an invalid floating-point number will also be output as result.

You have the following options to evaluate possible errors caused by invalid floating-point numbers:

- In LAD/FBD and SCL, you can query the enable output ENO for FALSE
- In STL, you can evaluate the status bit OV

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)
  
[Calculating with floating-point numbers (REAL and LREAL) in SCL](Creating%20SCL%20programs.md#calculating-with-floating-point-numbers-real-and-lreal-in-scl)

## Timers

This section contains information on the following topics:

- [S5TIME (duration) (S7-300, S7-400)](#s5time-duration-s7-300-s7-400)
- [TIME (IEC time)](#time-iec-time)
- [LTIME (IEC time) (S7-1500)](#ltime-iec-time-s7-1500)

### S5TIME (duration) (S7-300, S7-400)

#### Format

Data type S5TIME stores the duration in BCD format. The duration is the product from a time in the range 0 to 999 and a time basis. The time basis indicates the interval at which a timer decrements the time value by one unit until it reaches "0". The resolution of the times can be controlled via the time basis.

The following table shows the range of values for data type S5TIME:

| Length (bits) | Format | Range of values | Examples of value input |
| --- | --- | --- | --- |
| 16 | S7 time in increments of 10 ms (default value) | S5T#0MS to S5T#2H_46M_30S_0MS | S5T#10s, S5TIME#10s |

The following table shows the time base coding for S5TIME:

| Time basis | Binary code for time basis |
| --- | --- |
| 10 ms | 00 |
| 100 ms | 01 |
| 1 s | 10 |
| 10 s | 11 |

Always observe range limits and the resolution of time values when using data type S5TIME with timers. The table below specifies the range associated with each resolution:

| Resolution | Range |
| --- | --- |
| 0.01 s | 10 ms to 9 s 990 ms |
| 0.1 s | 100 ms to 1 min 39 s 900 ms |
| 1 s | 1 s to 16 min 39 s |
| 10 s | 10 s to 2 h 46 min 30 s |

Values that exceed 2h46m30s are not accepted.

#### Example

The following figure shows the content of the time operand for a time value of 127 and a time base of 1 s:

![Example](images/63689698571_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### TIME (IEC time)

#### Description

The contents of an operand of the data type TIME is interpreted as milliseconds. The representation contains information for days (d), hours (h), minutes (m), seconds (s) and milliseconds (ms).

The following table shows the properties of data type TIME:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 32 | Signed duration | T#-24d_20h_31m_23s_648ms to T#+24d_20h_31m_23s_647ms | T#10d_20h_30m_20s_630ms, TIME#10d_20h_30m_20s_630ms |

It is not necessary to specify all time units. T#5h10s is a valid entry, for example. If only one unit is specified, the absolute value of days, hours, and minutes must not exceed the high or low limits. When more than one time unit is specified, the value must not exceed 24 days, 23 hours, 59 minutes, 59 seconds or 999 milliseconds.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### LTIME (IEC time) (S7-1500)

#### Description

The contents of an operand of data type LTIME is interpreted as nanoseconds. The representation contains information for days (d), hours (h), minutes (m), seconds (s) and milliseconds (ms), microseconds (us) and nanoseconds (ns).

The following table shows the properties of data type LTIME:

| Length (bits) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 64 | Signed duration | LT#-106751d_23h_47m_16s_854ms_775us_808ns to LT#+106751d_23h_47m_16s_854ms_775us_807ns | LT#11350d_20h_25m_14s_830ms_652us_315ns, LTIME#11350d_20h_25m_14s_830ms_652us_315ns |

It is not necessary to specify all time units. LT#5h10s is therefore a valid entry, for example. If only one unit is specified, the absolute value of days, hours, and minutes must not exceed the high or low limits. When more than one time unit is specified, the value must not exceed 106751 days, 23 hours, 59 minutes, 59 seconds, 999 milliseconds, 999 microseconds or 999 nanoseconds.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

## Date and time

This section contains information on the following topics:

- [DATE](#date)
- [TIME_OF_DAY (TOD)](#time_of_day-tod)
- [LTOD (LTIME_OF_DAY) (S7-1500)](#ltod-ltime_of_day-s7-1500)
- [DATE_AND_TIME (date and time of day)](#date_and_time-date-and-time-of-day)
- [LDT (DATE_AND_LTIME) (S7-1500)](#ldt-date_and_ltime-s7-1500)
- [DTL (S7-1200, S7-1500)](#dtl-s7-1200-s7-1500)

### DATE

#### Format

The DATE data type saves the date as an unsigned integer. The representation contains the year, the month, and the day.

The contents of an operand of DATE data type correspond in hexadecimal format to the number of days since 01-01-1990 (16#0000).

The following table shows the properties of data type DATE:

| Length (bytes) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 2 | IEC date  (Year-Month-Day) | D#1990-01-01 to D#2169-06-06 | D#2009-12-31, DATE#2009-12-31 |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### TIME_OF_DAY (TOD)

#### Format

Data type TOD (TIME_OF_DAY) occupies a double word and stores the number of milliseconds since the beginning of the day (0:00 h) as unsigned integer.

The following table shows the properties of data type TOD:

| Length (bytes) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 4 | Time-of-day (hours:minutes:seconds.milliseconds) | TOD#00:00:00.000 to TOD#23:59:59.999 | TOD#10:20:30.400, TIME_OF_DAY#10:20:30.400 |

You always need to specify the hours, minutes and seconds. The specification of milliseconds is optional.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### LTOD (LTIME_OF_DAY) (S7-1500)

#### Format

Data type LTOD (LTIME_OF_DAY) occupies two double words and stores the number of nanoseconds since the beginning of the day (0:00 h) as unsigned integer.

The following table shows the properties of data type LTOD:

| Length (bytes) | Format | Value range | Examples of value input |
| --- | --- | --- | --- |
| 8 | Time-of-day (hours:minutes:seconds.nanoseconds) | LTOD#00:00:00.000000000 to LTOD#23:59:59.999999999 | LTOD#10:20:30.400_365_215, LTIME_OF_DAY#10:20:30.400_365_215 |

You always need to specify the hours, minutes and seconds. The specification of nanoseconds is optional.

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### DATE_AND_TIME (date and time of day)

#### Format

The DT (DATE_AND_TIME) data type saves the information on date and time of day in BCD format.

The following table shows the properties of data type DT:

| Length (bytes) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| 8 | Date and time  (year-month-day-hour:minute:second:millisecond <sup>3)</sup>) | Min.: DT#1990-01-01-00:00:00.000  Max.: DT#2089-12-31-23:59:59.999 | DT#2008-10-25-08:12:34.567, DATE_AND_TIME#2008-10-25-08:12:34.567 |

The following table shows the structure of the DT data type:

| Byte | Contents | Value range |
| --- | --- | --- |
| 0 | Year | 0 to 99  (Years 1990 to 2089)  BCD#90 = 1990  ...  BCD#0 = 2000  ...  BCD#89 = 2089 |
| 1 | Month | BCD#1 to BCD#12 |
| 2 | Day | BCD#1 to BCD# 31 |
| 3 | Hour | BCD#0 to BCD#23 |
| 4 | Minute | BCD#0 to BCD#59 |
| 5 | Second | BCD#0 to BCD#59 |
| 6 | The two most significant digits of MSEC | BCD#0 to BCD#99 |
| 7 (4MSB) <sup>1)</sup> | The least significant digit of MSEC | BCD#0 to BCD#9 |
| 7 (4LSB) <sup>2)</sup> | Weekday | BCD#1 to BCD#7  BCD#1 = Sunday  ...  BCD#7 = Saturday |
| <sup>1) </sup>MSB: Most significant bit   <sup>2) </sup>LSB: Least significant bit   <sup>3)</sup> Fixed point number |  |  |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### LDT (DATE_AND_LTIME)  (S7-1500)

#### Format

Data type LDT (DATE_AND_LTIME) stores the date and time-of-day information in nanoseconds since 01/01/1970 0:0.

The following table shows the properties of data type LDT:

| Length (bytes) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| 8 | Date and time  (Year-Month-Day-Hour:Minute:Second.Nanoseconds) | Min.: LDT#1970-01-01-00:00:00.000000000  Max.: LDT#2262-04-11-23:47:16.854775807 | LDT#2008-10-25-08:12:34.567 |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Overview of data type conversion (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#overview-of-data-type-conversion-s7-1500)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Implicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#implicit-conversions-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

### DTL (S7-1200, S7-1500)

#### Description

An operand of data type DTL has a length of 12 bytes and stores date and time information in a predefined structure.

The following table shows the properties of data type DTL:

| Length (bytes) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| 12 | Date and time  (Year-Month-Day-Hour:Minute:Second.Nanoseconds) | Min.: DTL#1970-01-01-00:00:00.0  Max.: DTL#2262-04-11-23:47:16.854775807 | DTL#2008-12-16-20:30:20.250 |

The structure of data type DTL consists of several components each of which can contain a different data type and range of values. The data type of a specified value must match the data type of the corresponding components.

> **Note**
>
> **Invalid monitor value of DTL tags in hexadecimal format**
>
> If the monitor value of the DTL tags is represented in hexadecimal format, this can be because one of the values (YEAR, MONTH, DAY, etc.) is invalid. For example, this is the case if a value &gt; 24 was specified at the HOUR tag.

The following table shows the structure components of data type DTL and their properties:

| Byte | Component | Data type | Value range |
| --- | --- | --- | --- |
| 0 | Year | UINT | 1970 to 2262 |
| 1 |  |  |  |
| 2 | Month | USINT | 1 to 12 |
| 3 | Day | USINT | 1 to 31 |
| 4 | Weekday | USINT | 1(Sunday) to 7(Saturday)  The weekday is not considered in the value entry. |
| 5 | Hour | USINT | 0 to 23 |
| 6 | Minute | USINT | 0 to 59 |
| 7 | Second | USINT | 0 to 59 |
| 8 | Nanosecond | UDINT | 0 to 999999999 |
| 9 |  |  |  |
| 10 |  |  |  |
| 11 |  |  |  |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

## Character strings

This section contains information on the following topics:

- [Character](#character)
- [Character strings](#character-strings-1)

### Character

This section contains information on the following topics:

- [CHAR](#char)
- [WCHAR (S7-1200, S7-1500)](#wchar-s7-1200-s7-1500)

#### CHAR

##### Description

A tag of the CHAR (Character) data type has a length of 8 bits and occupies one BYTE of memory.

The CHAR data type stores a single character in ASCII coding. You can find information on the encoding of special characters under "See also &gt; STRING".

The following table shows the value range of the CHAR data type:

| Length (bits) | Format | Value range | Example of value inputs |
| --- | --- | --- | --- |
| 8 | ASCII characters | ASCII character set | 'A', CHAR#'A' |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[STRING](#string)

#### WCHAR (S7-1200, S7-1500)

##### Description

A tag of the data type WCHAR (Wide Characters) has a length of 16 bits and occupies two BYTE of memory.

The data type WCHAR saves a single character of an expanded character set in UTF-16 coding. However, only a subset of the entire Unicode range is covered. Characters that cannot be displayed are made displayable using an escape character.

The following table shows the value range of the WCHAR data type:

| Length (bits) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| 16 | Unicode | $0000 - $D7FF | WCHAR#'a' |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)

### Character strings

This section contains information on the following topics:

- [STRING](#string)
- [Structure of a STRING tag](#structure-of-a-string-tag)
- [WSTRING (S7-1200, S7-1500)](#wstring-s7-1200-s7-1500)
- [Addressing individual characters of a STRING or WSTRING (S7-1200, S7-1500)](#addressing-individual-characters-of-a-string-or-wstring-s7-1200-s7-1500)
- [Transferring a tag of the STRING or WSTRING data type](#transferring-a-tag-of-the-string-or-wstring-data-type)

#### STRING

##### Description

An operand of the STRING data type saves several characters in a character string that can consist of up to 254 characters. In a character string, all characters of the codepage created on the system are permitted. The characters are specified in single quotation marks.

A character string can also contain special characters. The escape character $ is used to identify control characters, dollar signs and single quotation marks.

> **Note**
>
> **Different code pages**
>
> Please note that the special characters are coded using the code page currently set in Windows. This means that a string that contains special characters can be displayed differently on a different operating system with a different code page.
>
> The dependency of the codepage on the created system makes an international use of the user program more difficult. Only the characters from the 7-bit ASCII coding are internationally valid.

The following table shows the properties of a STRING tag:

| Length (bytes) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| n + 2 <sup>1)</sup> | ASCII character string incl. special characters | 0 to 254 characters | - 'Name' - STRING#'NAME' - STRING#'Na... (The actual length of the string is longer than the space available on the screen.) - STRING#'' (The string is empty.) |
| <sup>1)</sup> An operand of the STRING data type occupies two bytes more than the specified maximum length in the memory. |  |  |  |

The table below shows examples for the notation of special characters:

| Character | Hex | Meaning | Example |
| --- | --- | --- | --- |
| $L or $l | 0A | Line feed | '$LText', '$0AText' |
| $N | 0A and 0D | Line break  The line break occupies 2 characters in the character string and is converted to $R$L in the display in the editor. | '$NText', '$0A$0DText' |
| $P or $p | 0C | Page feed | '$PText', '$0CText' |
| $R or $r | 0D | Carriage return (CR) | '$RText','$0DText' |
| $T or $t | 09 | Tab | '$TText', '$09Text' |
| $$ | 24 | Dollar sign | '100$$', '100$24' |
| $' | 27 | Single quotation mark | '$'Text$'','$27Text$27' |

If the escape character $ is followed by a letter from the table, the character indicated in the table is entered in the string. If the escape character $ is followed by a letter that is not in the table, this letter is entered in the string. If the escape character $ is followed by two hexadecimal digits or only one digit, this code is entered in the string.

##### Use in the watch table

The following applies to a CPU of the S7-300/400 series: If a tag of the STRING data type is being monitored, only the first 30 characters will be displayed. If the actual length is greater than 30 characters, an ellipsis (…) is displayed instead of the final apostrophe ('). STRING values with more than 30 characters cannot be used for modifying.

##### Maximum length of a character string

The maximum length of the character string can be specified during the declaration of an operand using square brackets after the keyword STRING (for example, STRING[4]). You can also use local or global constants to declare the maximum length (for example, STRING[#loc_const] or STRING["glob_const"]). If the specification of the maximum length is omitted, the standard length of 254 characters is set for the respective operand.

You can find additional information about using local or global constants to declare the maximum length here:

- Declaring the block interface: [Declare variables of the STRING and WSTRING data types](Declaring%20the%20block%20interface.md#declare-variables-of-the-string-and-wstring-data-types)
- Programming data blocks: [Declaring tags of the STRING data type](Programming%20data%20blocks.md#declaring-tags-of-the-string-data-type)
- [Examples of using constants](Programming%20basics.md#examples-of-using-constants)

If the actual length of a specified character string is shorter than the declared maximum length, the characters are written to the character string left-justified and the remaining character spaces remain undefined. Only occupied character spaces that define the actual length of the string are considered for the value processing and all displays.

> **Note**
>
> For S7-300/400 CPUs, please note: If a temporary tag of the STRING data type was defined, you must describe the BYTE "Max. length of string" with the defined length before you use the tags in the user program.

##### Transferring a STRING for parameter supply

You can transfer the STRING data type as a parameter. You can find additional information on parameter supply with STRING here:

- [Transferring a tag of the STRING or WSTRING data type](#transferring-a-tag-of-the-string-or-wstring-data-type)
- For S7-1200/1500: [Valid data types in the block interface](Declaring%20the%20block%20interface.md#valid-data-types-in-the-block-interface-s7-1200-s7-1500)
- For S7-300/400: [Valid data types in the block interface](Declaring%20the%20block%20interface.md#valid-data-types-in-the-block-interface-s7-300-s7-400)

##### Example

The example below shows the byte sequence if the STRING[4] data type is specified with output value 'QB':

![Example](images/63689945355_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

#### Structure of a STRING tag

##### Introduction

A tag with STRING data type (character string) is maximum 256 characters long with 254 bytes user data. It starts in a non-optimized block at a word limit (at a byte with even address). In an optimized block it can start at any byte limit.

When tags are created their maximum length is specified. In the case of the preassignment or editing of the character string, the current length (the actually used length of the character string = number of valid characters) is entered. The maximum length is located in the first byte of the character string. The current length is in the second byte. This is followed by the characters, coded according to the codepage set in Windows.

Structure of a STRING tag

![Introduction](images/93444824075_DV_resource.Stream@PNG-en-US.png)

#### WSTRING (S7-1200, S7-1500)

##### Description

An operand of data type WSTRING (Wide Character String) stores several Unicode characters of data type WCHAR in one character string. If you do not specify a length, the character string has a preset length of 254 characters. In a character string, all characters that are supported by the operating system are permitted. This means you can also use Chinese characters in a character string. Windows supports only some (but sufficient number) of the characters defined in Unicode.

> **Note**
>
> **Coding**
>
> STEP 7 prohibits all coding of $D000 to $FFFF.

When declaring an operand of data type WSTRING you can define its length using square brackets (for example WSTRING[10]). If you do not specify a length, the length of the WSTRING is set to 254 characters by default. You can declare a length of up to 16382 characters (WSTRING[16382]).

The specification of the characters occurs in single quotes and always with the qualifier WSTRING#.

The following table shows the properties of a WSTRING tag:

| Length (WORD) | Format | Value range | Example of value input |
| --- | --- | --- | --- |
| n + 2 <sup>1)</sup> | Unicode character string;  n specifies the length of the character string. | Preset value: 0 to 254 characters  Max. possible value: 0 to 16382 | - WSTRING#'Hello World' - WSTRING#'Hello Wo... (The actual length of the string is longer than the space available on the screen.) - WSTRING#'' (The string is empty.) |
| <sup>1)</sup> An operand of the WSTRING data type occupies two WORDs more in the memory than the specified maximum length. |  |  |  |

A character string can also contain special characters. The escape character $ is used to identify control characters, dollar signs and single quotation marks.

The table below shows examples for the notation of special characters:

| Character | Hex | Meaning | Example |
| --- | --- | --- | --- |
| $L or $l | 000A | Line feed | '$LText', '$000AText' |
| $N | 000A and 000D | Line break  The line break occupies 2 characters in the character string and is converted to $R$L in the display in the editor. | '$NText', '$000A$000DText' |
| $P or $p | 000C | Page feed | '$PText', '$000CText' |
| $R or $r | 000D | Carriage return (CR) | '$RText','$000DText' |
| $T or $t | 0009 | Tab | '$TText', '$0009Text' |
| $$ | 0024 | Dollar sign | '100$$', '100$0024' |
| $' | 0027 | Single quotation mark | '$'Text$'','$0027Text$0027' |

If the escape character $ is followed by a letter from the table, the character indicated in the table is entered in the string. If the escape character $ is followed by a letter that is not in the table, this letter is entered in the string. If the escape character $ is followed by four hexadecimal digits, this code is entered in the string.

> **Note**
>
> **Conversion of WSTRING tags**
>
> Implicit conversion of the WSTRING data type is not possible. Explicit conversion of the WSTRING data type to STRING is generally possible. However, as standard, it is only possible to convert characters in the code range from 0 - 127 in all Windows code pages. For all characters outside this range, the code page character and the lower byte of the Unicode character must be in exactly the same position for the conversion to work without errors.

##### Use in the watch table

If a tag of the WSTRING data type is being monitored, only the first 254 characters are displayed. If the actual length is greater than 254 characters, an ellipsis (…) is displayed instead of the closing apostrophe ('). WSTRING values with more than 254 characters cannot be used for modifying.

##### Use in SCL

In rare cases, the WSTRING results are truncated when you create very large WSTRINGs using WSTRING-generating functions (e.g. CONCAT, INSERT, JOIN, SPLIT, LEFT, MID, RIGHT) in SCL.

Therefore, check the ENO of these functions for FALSE to see if the WSTRING has been truncated.

##### Maximum length of a character string

The maximum length of the character string can be specified during the declaration of an operand using square brackets after the keyword WSTRING (for example, WSTRING[4]). You can also use local or global constants to declare the maximum length (for example, WSTRING[#loc_const] or WSTRING["glob_const"]). If the specification of the maximum length is omitted, the standard length of 254 characters is set for the respective operand.

You can find additional information about using local or global constants to declare the maximum length here:

- Declaring the block interface: [Declare variables of the STRING and WSTRING data types](Declaring%20the%20block%20interface.md#declare-variables-of-the-string-and-wstring-data-types)
- Programming data blocks: [Declaring tags of the STRING data type](Programming%20data%20blocks.md#declaring-tags-of-the-string-data-type)
- [Examples of using constants](Programming%20basics.md#examples-of-using-constants)

If the actual length of a specified character string is shorter than the declared maximum length, the characters are written to the character string left-justified and the remaining character spaces remain undefined. Only occupied character spaces are considered in the value processing.

##### Transferring a WSTRING for parameter supply

Operands of the data type WSTRING can be transferred as parameters up to the maximum length for blocks with "optimized" access.

For function blocks (FB) with "standard" access, operands of the data type WSTRING can be declared as parameters in all sections of the block interface except in the section "InOut". For a function (FC) with "standard" access, only operands of the WSTRING data type can be transferred as parameters.

The function value of an FC in the "Return" section and expressions in the SCL programming language are another exception to this rule. In these cases, the WSTRING tag must not be longer than 1022 characters.

The declared lengths of formal and actual parameters may be different. You can find additional information on parameter supply with WSTRING here:

- [Transferring a tag of the STRING or WSTRING data type](#transferring-a-tag-of-the-string-or-wstring-data-type)
- [Valid data types in the block interface](Declaring%20the%20block%20interface.md#valid-data-types-in-the-block-interface-s7-1200-s7-1500)

##### Example

The example below shows the byte sequence if the WSTRING[4] data type is specified with output value 'QB':

![Example](images/58395011723_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Constants](Programming%20basics.md#constants)

#### Addressing individual characters of a STRING or WSTRING (S7-1200, S7-1500)

##### Addressing individual characters of a STRING or WSTRING

Use the syntax `StringName[i]` to access an individual character of a STRING or WSTRING tag. The counting index "i" begins with "1". Thus, you access the first character of the string with StringName[1].

You cannot access individual characters of a STRING or WSTRING constant.

##### Examples

The following examples show the addressing of (W)STRINGs:

| Addressing | Explanation |
| --- | --- |
| #myWSTRING[3] | Addresses the third character of the WSTRING. |
| "myDB".mySTRING[3] | Addresses the third character of the STRING in the data block. |
| myNamespace.myDB.mySTRING[3] | Addresses the third character of the STRING in the data block in the "myNamespace" namespace. |

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

##### Troubleshooting W(STRING) access

Access errors result during runtime when you access a character that is located outside the STRING length. On read access to the character string, you receive the character '$00' or '$0000'; write access to the character string is not executed. If the instruction has the enable output ENO, ENO is set to the signal state FALSE. The CPU does not change to STOP.

The only exception is when the character is written directly after the actual length of the character string.

The following example shows the string 'Hello' with the actual length of 5. The 27th character of the STRING lies outside the actual length and cannot therefore be written. The STRING remains unchanged; the result of the assignment is 'hello'.

SCL

MyDB.mystring := 'hello';

MyDB.mystring[27] := CHAR_TO_BYTE('!');

The following example shows the specified exception: The character is written directly behind the STRING to the 6th character. The result of the assignment is 'hello!'.

SCL

MyDB.mystring := 'hello';

MyDB.mystring[6] := CHAR_TO_BYTE('!');

Where possible, use instructions from the "Extended instructions &gt; String + Char" pane to handle STRINGs.

CONCAT(IN1 := 'hello', IN2 := '!');

#### Transferring a tag of the STRING or WSTRING data type

##### Description

You can transfer tags of the STRING or WSTRING data type as parameters. The following table shows the rules that apply to the (W)STRING transfer in the various CPU families:

| CPU family | Data type | Rules for transfer at the block call |
| --- | --- | --- |
| S7-300/400 | STRING | The declared lengths of formal and actual parameters must be identical. |
| S7-1200/1500 | STRING  WSTRING | The declared lengths of formal and actual parameters may be different. If the declared length of the target parameter during runtime is insufficient to accept the (W)STRING, the (W)STRING is truncated and the enable output ENO is set to FALSE.  In the programming editor, a gray rectangle at the parameter indicates that (W)STRING might be truncated during runtime.  Exception:   When calling STL blocks, the declared lengths of formal and actual parameters must always be identical. |

The following figure shows a block call in which the lengths of the declared formal and actual parameters differ. Due to the different declared lengths, both "Input_String_20" and "Output_String_10" could be truncated during runtime.

![Description](images/78498390795_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Rules for supplying block parameters](Programming%20basics.md#rules-for-supplying-block-parameters)

## PLC data types (UDT)

This section contains information on the following topics:

- [Basics of PLC data types (UDT)](#basics-of-plc-data-types-udt)
- [Transferring a tag of the PLC data type (UDT)](#transferring-a-tag-of-the-plc-data-type-udt)
- [Addressing PLC data types (UDT)](#addressing-plc-data-types-udt)

### Basics of PLC data types (UDT)

#### Description

A PLC data type (UDT) is a complex, user-defined data type that is used for the declaration of a tag. It represents a data structure made up of several components of different data types. The components can also be derived from another PLC data type, from an ARRAY or directly using the STRUCT keyword as a structure. The nesting depth is hereby limited to 8 levels.

You can change a PLC data type (UDT) centrally and use it repeatedly in the program code. All locations of use are updated automatically.

Advantages of the PLC data types:

- Simple data exchange via block interfaces among several blocks
- Group data according to the process control
- Transferring a parameter as a data unit

#### Using a PLC data type

You can declare PLC data types as a type when creating data blocks. Based on this type, you can create a number of data blocks, all of which have the same data structure. These data blocks can be adapted by entering different actual values for the corresponding task.

For instance, create a PLC data type for a recipe for blending paints. You can then assign this data type to several data blocks, each of which contains different quantity information.

The following figure shows this application:

![Using a PLC data type](images/87923405707_DV_resource.Stream@PNG-en-US.png)

PLC data types can be used for the following applications:

- PLC data types can be used as data types for tags in the tag declaration of logic blocks or in data blocks.
- PLC data types can be used as templates for the creation of global data blocks with identical data structures.
- PLC data types can be used in S7-1200 and S7-1500 as a template for the creation of structured PLC tags.

#### Nesting depth of PLC data types

PLC data types (UDT) can be nested to a depth of 8 hierarchy levels.

#### Disadvantages of anonymous structures

The components of the structured tags can be identically addressed. This is regardless of whether the declaration has been made using a PLC data type or an anonymous structure.

The following disadvantages apply when using anonymous structures:

- Reusability of the same structure by copying. This makes it difficult to change the structure
- Anonymous structures are not compatible with PLC data types (UDT) of the same structure
- Performance, since the matching types for structural components are checked during runtime
- The high limit is more easily reached when using anonymous structures, since all components must be evaluated individually.

#### Example

The following example shows the data type definition of the "MyUDT" PLC data type:

![Example](images/87681598219_DV_resource.Stream@PNG-de-DE.png)

#### PLC data types generated by the system

Some instructions generate their own PLC data types during instancing which are saved in the "PLC data types" project folder. Do not use these PLC data types created by the system in a library, because this may result in undesirable system behavior. If necessary, these PLC data types are created by the system, which means they must not be stored in a library.

#### Generating external sources from blocks

When generating external sources from blocks, the changes made directly in the block interface to the default values of PLC data types are not exported to the sources. This means that these values are not available when the sources are imported once again. The default values are applied instead. To prevent this loss of data for the modified default values, the changes must be made directly in the PLC data type and not in the block interface. In this case, the changes are also exported when external sources are generated.

#### Additional information on the PLC data types (UDTs)

> **Note**
>
> Declaring PLC data types (UDTs):
>
> [Structure of the declaration table for PLC data types](Declaring%20PLC%20data%20types%20%28UDT%29.md#structure-of-the-declaration-table-for-plc-data-types)
>
> Programming recommendations for PLC data types:
>
> [Using PLC data types (UDT)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-plc-data-types-udt-s7-1200-s7-1500)
>
> [Using the DB_ANY data type](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-the-db_any-data-type-s7-1200-s7-1500)
>
> Comparison of PLC data types (UDTs) in the program:
>
> [Comparing PLC data types](Comparing%20PLC%20programs.md#comparing-plc-data-types)

> **Note**
>
> **You can find more information on the PLC data types in the Siemens Industry Online Support in the following contributions:**
>
> How can you initialize structures in optimized memory areas at the S7-1500 in STEP 7 (TIA Portal)?
>
> [https://support.industry.siemens.com/cs/ww/de/view/78678760](https://support.industry.siemens.com/cs/ww/en/view/78678760)
>
> How do you create a PLC data type (UDT) at an S7-1500 control system?
>
> [https://support.industry.siemens.com/cs/ww/de/view/67599090](https://support.industry.siemens.com/cs/ww/en/view/67599090)
>
> How is the specific application of own PLC data types (UDT) effected in STEP 7 (TIA Portal)?
>
> [https://support.industry.siemens.com/cs/de/de/view/67582844](https://support.industry.siemens.com/cs/de/en/view/67582844)
>
> Why should complete structures be transferred at a block call for S7-1500 instead of many individual components?
>
> [https://support.industry.siemens.com/cs/ww/de/view/67585079](https://support.industry.siemens.com/cs/ww/en/view/67585079)

---

**See also**

[Addressing PLC data types (UDT)](#addressing-plc-data-types-udt)
  
[Declaring tags based on a PLC data type](Declaring%20the%20block%20interface.md#declaring-tags-based-on-a-plc-data-type)
  
[Declaring tags based on a PLC data type](Programming%20data%20blocks.md#declaring-tags-based-on-a-plc-data-type)
  
[Comparing PLC tags](Comparing%20PLC%20programs.md#comparing-plc-tags)
  
[Creating structured PLC tags](Declaring%20PLC%20tags.md#creating-structured-plc-tags)
  
[Permissible addresses and data types of PLC tags](Declaring%20PLC%20tags.md#permissible-addresses-and-data-types-of-plc-tags)
  
[CMP ==: Equal (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-equal-s7-1200-s7-1500)
  
[Transferring a tag of the PLC data type (UDT)](#transferring-a-tag-of-the-plc-data-type-udt)

### Transferring a tag of the PLC data type (UDT)

#### Description

You can also transfer tags that are declared as PLC data type (UDT) as actual parameters. If the formal parameter is declared as a PLC data type (UDT) in the tag declaration, you must transfer a tag that has the same PLC data type (UDT) as an actual parameter.

An element of a tag declared using the PLC data type (UDT) can also be transferred as an actual parameter for the block call, provided the data type of the element of the tag matches the data type of the formal parameter.

Structures and user-defined PLC data types can be assigned to one another if they have identical structures. This means that the data types and the order of all structure components must be identical. In nested structures, the data types and the order of the lower-level structures and their components must also match.

Two different PLC data types can also be assigned to one another if the data types and the order of all structure components including the lower-level structures are identical. The names of the PLC data types do not have to match.

User-defined PLC data types and structures cannot be assigned to system data types.

---

**See also**

[Rules for supplying block parameters](Programming%20basics.md#rules-for-supplying-block-parameters)

### Addressing PLC data types (UDT)

#### Addressing data elements of an PLC data type

PLC data types are types that you can use as a template to create program elements. For example, you can derive PLC tags or data blocks from PLC data types. Direct access to a PLC data type is therefore not possible. However, you can access the program elements that you have created based on a PLC data type.

Use the following syntax for this:

`<ProgramelementName>.<ElementName>`

#### Examples

The following examples show the addressing of structured data type tags:

| Addressing | Explanation |
| --- | --- |
| #Values.Temperature | Addressing of the "Temperature" element in the "Values" tag, which is based on a PLC data type. |
| "Global_DB".Valves | Addressing of the "Valves" element in the global data block "Global_DB". Neither the accessing block nor the called block is located in a namespace. |
| MyNamespace.Global_DB.Valves | Addressing of the "Valves" element in the global data block "Global_DB".  The "Global_DB" block is in the "MyNamespace" namespace. |

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces under: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

---

**See also**

[Addressing tags in global data blocks](Programming%20basics.md#addressing-tags-in-global-data-blocks)

## Named value data types (S7-1500)

This section contains information on the following topics:

- [Basics of named value data types (S7-1500)](#basics-of-named-value-data-types-s7-1500)
- [Application example: Named value data types (S7-1500)](#application-example-named-value-data-types-s7-1500)
- [Application example: Creating state machines with named value data types (S7-1500)](#application-example-creating-state-machines-with-named-value-data-types-s7-1500)

### Basics of named value data types (S7-1500)

#### Introduction

"Named values" are values that have a unique name assigned to them. Named values are easily referenced throughout the program and increase the readability and maintainability of the program.

In TIA Portal, you declare named values within "named value data types". They contain a set of values that are associated with a unique set of names.

Named value data types are based on a base data type that is valid for all elements within the named value data type. Tags based on Named value data types can assume all values that lie within the value range of the base data type, thus including values not explicitly specified in the declaration.

Named value data types are available only within software units and are supported by the following SIMATIC programming languages:

- LAD
- FBD
- STL
- SCL
- GRAPH

An application example for named value data types is available here:

[Application example: Named value data types](#application-example-named-value-data-types-s7-1500)

> **Note**
>
> **Creating named value data types**
>
> Named value data types are created in the project tree in the "PLC data types" folder.
>
> See also: [Creating named value data types](Declaring%20named%20value%20data%20types%20%28S7-1500%29.md#creating-named-value-data-types-s7-1500)
>
> **Document-based programming**
>
> You declare named value data types in text documents. The documents have the file name extension *.nvt.
>
> See also: [Document-based programming](Declaring%20named%20value%20data%20types%20%28S7-1500%29.md#document-based-programming-s7-1500)

#### Declaration

The following syntax is used to declare named value data types:

Syntax

NAMESPACE &lt;name&gt;

{ PUBLISHED := 'TRUE|FALSE' }

    TYPE

        &lt;namedValueType&gt; : &lt;BaseType&gt;

        (

                &lt;NAME_1&gt; := &lt;Value_1&gt;,

                &lt;NAME_2&gt; := &lt;Value_2&gt;,

                &lt;NAME_3&gt; := &lt;Value_3&gt;

        ) := &lt;Default&gt;;

    END_TYPE

END_NAMESPACE

The following table describes the individual syntax elements:

| Syntax element | Description |
| --- | --- |
| NAMESPACE  END_NAMESPACE | Optional  Specifies the namespace of one or more named value data types. You can define a namespace for each named value data type, or you can place several data types in a namespace.  If you do not define a namespace, the data type is not in a namespace. |
| {PUBLISHED : = 'TRUE|FALSE'} | Optional  Specifies whether the named value data type is published. Program elements from other software units can access published data types.   The pragma can assume the values "TRUE" or "FALSE". If you do not specify the "PUBLISHED" pragma, the data type is not published by default. |
| TYPE  END_TYPE | Surrounds the declaration of one or more named value data types. |
| &lt;namedValueType&gt; : &lt;BaseType&gt; | Name and base data type of the named value data type.   Naming conventions according to IEC 61131-3 apply.  The following base data types are possible:  - Integers: SINT, USINT, INT, UINT, DINT, UDINT, LINT and ULINT - Bit strings: BYTE, WORD, DWORD, LWORD |
| &lt;NAME_1&gt; := &lt;Value_1&gt;,   &lt;NAME_2&gt; := &lt;Value_2&gt;,  &lt;NAME_3&gt; := &lt;Value_3&gt; | List of individual named values  The named value data type can be one of the declared values. However, it can take a different value that corresponds to the base data type.  Naming conventions according to IEC 61131-3 apply. The maximum name length amounts to 128 characters.  The names of the individual named values are not multilingual. |
| := &lt;Default&gt; | Optional  Specifies the default value of the named value data type.  You can specify one of the values from the declaration list or any other value that matches the base data type. If you do not enter an explicit default value, the first value in the declaration list is used as default value. In this example, the value of "NAMED_VALUE_1" would be the default value. |
| //comment | Optional  A line comment extends to the end of the line. |
| (* comment section *)  /* comment section */ | Optional  A comment section can span several lines. |

#### Using named value data types

Named value data types are types that you use as templates to create program elements. They can be replaced as follows:

- You can declare parameters based on a named value data type in the block interface.
- You can declare elements based on a named value data type in global data blocks.
- You can declare elements based on a named value data type in PLC data types (UDT).

> **Note**
>
> **No automatic updating of reference locations**
>
> Since named value data types are programmed document-based, reference locations are not updated automatically. If you, for example, rename a named value data type, the reference locations in the PLC program are not modified automatically. Instead, a syntax error is reported during compilation. Then update the reference locations manually.

#### Uniquely addressing named values

You can use named values in operations in the same way as other constants of the base data type. They can also be used to declare ARRAY boundaries or STRING lengths.

For unique identification, specify the named value data type followed by the name of the named value in the following form:

&lt;namedValueType&gt;#&lt;NAMED_VALUE&gt;

#### Examples

The following examples show some addressing options for named values.

The examples are based on the declaration of the named value data types "nvtTrafficLight" and "nvtPaintingColor":

![Examples](images/171701232523_DV_resource.Stream@PNG-de-DE.png)

The following example shows how named values are used to declare ARRAY boundaries and STRING lengths:

![Examples](images/171701236619_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Using the keyboard in the program editor](Program%20editor.md#using-the-keyboard-in-the-program-editor)

### Application example: Named value data types (S7-1500)

#### Objective of the application example

This application example provides an introduction to using named value data types in an automation project.

A positioning axis is controlled in the project. Named value data types are used to assign unique names across the program to specific axis parameters. This way they can be easily referred in the program. This increases the readability and maintainability of the program.

#### Example program

The figure below shows the named value data type "nvtMoveAbsoluteDirection". It contains definitions for the possible movement directions of the axis:

![Example program](images/170614000651_DV_resource.Stream@PNG-de-DE.png)

The figure below shows the named value data type "nvtPositionerStatus". It contains definitions for the possible states which the axis can assume:

![Example program](images/170613544203_DV_resource.Stream@PNG-de-DE.png)

The following figure shows the call of the technology object "TO_PositioningAxis".

- The axis has the input parameter "Direction" which controls the direction of movement of the axis. When the axis is called, the actual value of the parameter is transferred by "nvtMoveAbsoluteDirection".
- The axis has different output parameters, which return the status information of the axis to the calling block. The status values are transferred by means of an IF instruction to "nvtPositionerStatus".

![Example program](images/170613539979_DV_resource.Stream@PNG-de-DE.png)

### Application example: Creating state machines with named value data types (S7-1500)

#### Objective of the application example

This application example shows the use of named value data types for the implementation of a state machine.

In the project, different states are defined which the controlled process can assume. A named value data type is used to assign unique names to the states across the program. This way the states can be referenced easily in the entire program.

#### Example program

The figure below shows the named value data type "nvtOperationStates". It contains definitions for the states of the process:

![Example program](images/171724732299_DV_resource.Stream@PNG-de-DE.png)

The following figure shows a block which changes the values of "nvtOperationStates" by using a CASE statement. This way the current state of the process can be set centrally for all reference locations of "nvtOperationStates".

![Example program](images/170614004875_DV_resource.Stream@PNG-de-DE.png)

## STRUCT data structure (anonymous structures)

This section contains information on the following topics:

- [Basic information on STRUCT](#basic-information-on-struct)
- [Structure of a STRUCT tag](#structure-of-a-struct-tag)
- [Addressing STRUCT elements](#addressing-struct-elements)
- [Transferring tags of the STRUCT data type](#transferring-tags-of-the-struct-data-type)

### Basic information on STRUCT

#### Description

The STRUCT data type represents a data structure that consists of a fixed number of components of different data types. Structures can also be nested and contain components of data type STRUCT or ARRAY. Structures can be used to group data according to the process control system and to transfer parameters as one data unit.

Structure declarations that are used directly at the tag are called anonymous structures. An anonymous structure can have the following form:

![Description](images/96073460491_DV_resource.Stream@PNG-de-DE.png)

All of the subsequent explanations refer to this structure image.

#### Nesting depth and potential number of structures

Structures (STRUCT) can be nested to a depth of 8 hierarchy levels.

A maximum of 252 structures (STRUCT) are permitted in one data block in CPUs of the S7-1200/S7-1500 series. If you require other structures, use PLC data types (UDT) instead of the "STRUCT" data type.

[Using PLC data types (UDT)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-plc-data-types-udt-s7-1200-s7-1500)

#### Transferring a STRUCT for parameter supply

You can transfer the STRUCT data type as a parameter. You can find additional information on parameter supply with STRUCT here:

[Transferring tags of the STRUCT data type](#transferring-tags-of-the-struct-data-type)

#### Disadvantages of anonymous structures

The components of the structured tag can be identically addressed. This is regardless of whether the declaration has been made using a PLC data type or an anonymous structure.

The following disadvantages apply when using anonymous structures:

- Increased maintenance costs: If an anonymous structure was copied multiple times, then it must also have been changed multiple times during a change.
- Anonymous structures are not compatible with PLC data types (UDT) of the same structure
- Performance, since the matching types of all structural components are checked
- Increased memory requirement: Each anonymous structure is a separate object, whose description is loaded to the AS.

#### Example

If you declare the tag of the data type STRUCT in a PLC data type (UDT), more usage options are available to you (see figure on left). However, you can also declare the tag directly with the data type STRUCT (see figure on right).

Declaration of the structured tag "Motor" with or without PLC data type (UDT):

| Structured tag with PLC data type (UDT) | Structured tag without PLC data type (UDT) |
| --- | --- |
| ![Example](images/96074581131_DV_resource.Stream@PNG-de-DE.png) | ![Example](images/96073460491_DV_resource.Stream@PNG-de-DE.png) |

#### Processing of complex structures

A series of instructions (e.g. "Serialize: Serialization", "Deserialize: Deserialization", "CMP" (comparator) and "MOVE: Move value") can process very large, complex structured tags. In doing so, the CPU analyzes the form of the tag structure and executes the corresponding instruction for each substructure contained in the total structure or for all contained elementary components.

With a very complex structure, this structure analysis may lead to an unexpected increase in the run time of the corresponding instruction. In addition to the complexity of structured tags specified in the operation, the total number of anonymous structures declared in the program also has an effect on the run time. A very large number of different anonymous structure definitions can also increase the run time.

Solution:

- Avoid anonymous structures Use PLC data types instead.
- Avoid multiple declaration of data structures that are structured very similarly. Try to assemble these into a structure declaration.
- Avoid the declaration of numerous individual tags in structures and data blocks, if they have the same data type. Use the ARRAY data type in this case, if possible.

---

**See also**

[Declaring tags of STRUCT data type](Declaring%20the%20block%20interface.md#declaring-tags-of-struct-data-type)
  
[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

### Structure of a STRUCT tag

#### Introduction

A STRUCT tag always starts in a non-optimized block at a word limit, i.e. at a byte with even address. The individual components are then located in the order of their declaration in the memory. STRUCT tags occupy the memory up to the next word limit.

Components with BOOL data type start in the least significant bit. Components with BYTE and CHAR data type start in the next byte. Components with different data type start at a word limit. In optimized blocks the structures are stored so that all components are aligned according to their size. The order in the memory does not correspond to the display in the editor.

A nested structure is a structure that is a component of another structure. A nesting depth of maximum 8 structures is possible. A nesting depth of maximum 9 structures is possible in the "InOut" section. The nesting depth is calculated including the highest structure element (example: "Anna.Berta.Carla" corresponds to a nesting depth of 3).

All components can be separately addressed. The individual names of components are separated by a dot.

Structure of a STRUCT tag with elementary and complex data types in the non-optimized memory area:

- Declaration of the "Motor" STRUCT tag

  ![Introduction](images/96073460491_DV_resource.Stream@PNG-de-DE.png)
- Required memory of the "Motor" STRUCT tag

  ![Introduction](images/96071542283_DV_resource.Stream@PNG-en-US.png)

### Addressing STRUCT elements

#### Addressing elements in structures

You can access individual elements in a structure using the following syntax:

`"<Blockname>".Structure.Element`

`<Namespace>.<Blockname>.Structure.Element`

#### Examples

The following examples show the addressing of structured data type tags:

| Addressing | Explanation |
| --- | --- |
| "Global_DB".Motor.Valves | Addressing of the "Valves" element in the "Motor" structure of the global data block "Global_DB".   Neither the accessing block nor the called block is located in a namespace. |
| myNamespace.Global_DB.Motor.Valves | Addressing of the "Valves" element in the "Motor" structure of the global data block "Global_DB".   The "Global_DB" block is in the "myNamespace" namespace. |

> **Note**
>
> **Calling and addressing blocks in namespaces**
>
> Blocks located in namespaces are represented in the program code in IEC-compliant notation:
>
> - The block name is not in quotation marks.
> - The namespace precedes the block name, separated by a dot.
>
> You can find detailed information on the notation of namespaces under: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

### Transferring tags of the STRUCT data type

#### Description

You can also transfer individual components of a STRUCT tag as actual parameters if the components correspond to the data type of the formal parameter.

You can also transfer complete structures as parameters. If a block has an input parameter of the STRUCT data type, you must transfer a STRUCT with identical structure as the actual parameter. This means that the names and data types of all structure components have to be identical.

Structures and user-defined PLC data types can be assigned to one another if they have identical structures. This means that the data types and the order of all structure components must be identical. In nested structures, the data types and the order of the lower-level structures and their components must also match.

Two different PLC data types can also be assigned to one another if the data types and the order of all structure components including the lower-level structures are identical. The names of the PLC data types do not have to match.

User-defined PLC data types and structures cannot be assigned to system data types.

> **Note**
>
> We recommend that you program structures as PLC data types (UDT). PLC data types (UDT) make programming easier, since they can be used repeatedly and changed centrally.

---

**See also**

[Rules for supplying block parameters](Programming%20basics.md#rules-for-supplying-block-parameters)

## ARRAY

This section contains information on the following topics:

- [Basic information on ARRAY](#basic-information-on-array)
- [Structure of an ARRAY tag](#structure-of-an-array-tag)
- [Addressing ARRAY components](#addressing-array-components)
- [Transferring tags of the ARRAY / ARRAY[*] data type](#transferring-tags-of-the-array-array-data-type)
- [Examples of how to use ARRAYs](#examples-of-how-to-use-arrays)

### Basic information on ARRAY

#### Description

A tag of the ARRAY data type represents a data structure that consists of a fixed number of components of the same data type. All data types except ARRAY are permitted for the components.

When you create an ARRAY tag the index limits are defined in square brackets and the data type is defined after the keyword "of". The ARRAY limits can be either defined fixed using integers or global and local constants or as formal parameters of a block, or defined variably using ARRAY[*]. The low limit must be smaller than or equal to the high limit. An ARRAY may contain up to six dimensions, the limits of which can be specified separated by a comma.

The structure of a one-dimensional tag of the ARRAY data type has, for example, the following form:

![Description](images/82013678603_DV_resource.Stream@PNG-de-DE.png)

The maximum ARRAY limits depend on the following factors:

- Data type of the ARRAY component
- Memory reserve (only in blocks with optimized access)

  You can find additional information under: [Basic information on loading block extensions without reinitialization](Loading%20block%20extensions%20without%20reinitialization%20%28S7-1200%2C%20S7-1500%29.md#basic-information-on-loading-block-extensions-without-reinitialization-s7-1200-s7-1500).
- Maximum size of the data block
- Maximum memory capacity of the CPU (you can find more information in the manual for the device)

The following table shows the properties of the ARRAY data type:

| Block property | Format | ARRAY limits | Data type |
| --- | --- | --- | --- |
| Standard | ARRAY[low limit..high limit] of &lt;DataType&gt; | [-32 768..32 767] of &lt;DataType&gt; | All data types except ARRAY  Multi-instances |
| Optimized | [-2 147 483 648..2 147 483 647] of &lt;DataType&gt; |  |  |

Various options are available for defining the ARRAY limits depending on the ARRAY that you declared.

| ARRAY limits | Global data block / tag table | Block interface |
| --- | --- | --- |
| Using integers as fixed ARRAY limits | x | x |
| Using global constants as fixed ARRAY limits | x | x |
| Using local constants as fixed ARRAY limits | - | x |
| Using variable ARRAY limits ARRAY[*] | - | x |
| ARRAY of multi-instances | - | x |

For more information on the section of the block interface in which you can define an ARRAY or an ARRAY[*], refer to: [Valid data types in the block interface](Declaring%20the%20block%20interface.md#valid-data-types-in-the-block-interface-s7-1200-s7-1500)

> **Note**
>
> **Applies to CPUs of the S7-1500 series**
>
> For a block with the "Optimized block access" block property, an element of the BOOL data type requires 1 byte of memory. This is also true when you use an ARRAY of &lt;data type&gt;. An ARRAY[0..1] of BOOL, for example, thus requires 2 bytes in an optimized program block.

#### Using integers as fixed ARRAY limits

You can use integers as fixed ARRAY limits:

- Example of a one-dimensional ARRAY

  ![Using integers as fixed ARRAY limits](images/93675555979_DV_resource.Stream@PNG-de-DE.png)
- Example of a three-dimensional ARRAY:

  ![Using integers as fixed ARRAY limits](images/93675564811_DV_resource.Stream@PNG-de-DE.png)

#### Using constants as fixed ARRAY limits

You can use local or global constants as fixed ARRAY limits:

- Fixed ARRAY limits for a one-dimensional ARRAY, consisting of two global user constants

  ![Using constants as fixed ARRAY limits](images/93681035147_DV_resource.Stream@PNG-de-DE.png)
- Fixed ARRAY limits for a one-dimensional ARRAY, consisting of two global user constants

  ![Using constants as fixed ARRAY limits](images/93707835147_DV_resource.Stream@PNG-de-DE.png)
- Fixed ARRAY limits for a two-dimensional ARRAY, consisting of global and local user constants

  ![Using constants as fixed ARRAY limits](images/93707843979_DV_resource.Stream@PNG-de-DE.png)

For more information on creating and using constants as ARRAY limits, refer to:

- [Declaring local tags and constants in the block interface](Declaring%20the%20block%20interface.md#declaring-local-tags-and-constants-in-the-block-interface)
- [Examples of using constants](Programming%20basics.md#examples-of-using-constants)

#### Using integers and global and local constants as fixed ARRAY limits

You can also combine all three above-named options with each other and also used integers and global and local constants mixed within an ARRAY as ARRAY limits.

![Using integers and global and local constants as fixed ARRAY limits](images/93711809035_DV_resource.Stream@PNG-de-DE.png)

#### Using variable ARRAY limits ARRAY[*] (only in blocks with optimized access)

You can use an ARRAY[*] to program blocks that can process an ARRAY with flexible length. To do this, you declare variable ARRAY limits for the parameters of a function or function block. ARRAY[*] is available in all programming languages.

Using the "LOWER_BOUND" and "UPPER_BOUND" instructions, you can read the low and high limits of an ARRAY with variable limits during runtime.

> **Note**
>
> **Availability of ARRAY[*]**
>
> ARRAY[*] is available in optimized blocks for a CPU of the S7-1200 series as of firmware version &gt;= 4.2, and for a CPU of the S7-1500 series as of firmware version &gt;= 2.0. In functions (FC) you can use ARRAY[*] in all declaration subsections. In function blocks (FB) you can declare ARRAY[*] only as an in-out parameter in the "InOut" section.

- Variable ARRAY limits for a one-dimensional ARRAY:

  ![Using variable ARRAY limits ARRAY[*] (only in blocks with optimized access)](images/93731585931_DV_resource.Stream@PNG-de-DE.png)
- Variable ARRAY limits for a one-dimensional ARRAY:

  ![Using variable ARRAY limits ARRAY[*] (only in blocks with optimized access)](images/93731594763_DV_resource.Stream@PNG-de-DE.png)

You can find additional information on the use of ARRAY[*] here:

- [Transferring tags of the ARRAY / ARRAY[*] data type](#transferring-tags-of-the-array-array-data-type)
- [Declaring tags of the ARRAY data type](Declaring%20the%20block%20interface.md#declaring-tags-of-the-array-data-type) in the block interface

#### Using multiple instances (only in blocks with optimized access)

You can also create multi-instances as ARRAY, in order to be able, for example, to use a variable index to address the individual multi-instances during the processing of program loops:

![Using multiple instances (only in blocks with optimized access)](images/93712624267_DV_resource.Stream@PNG-de-DE.png)

For more information on creating and using multi-instances, refer to:

- [Multi-instances](Programming%20basics.md#multi-instances)
- [Declaring multi-instances](Declaring%20the%20block%20interface.md#declaring-multi-instances)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)
  
[Indirect addressing of ARRAY components (S7-1200, S7-1500)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#indirect-addressing-of-array-components-s7-1200-s7-1500)

### Structure of an ARRAY tag

#### Introduction

With non-optimized blocks, an ARRAY tag never starts at a word limit, i.e. at a byte with even address. ARRAY tags occupy the memory up to the next word limit.

In optimized block the ARRAY requires as much space as the widest element of the structure. This means, for example, that an ARRAY of BYTE is located at a Byte limit and an ARRAY of LREAL is located at an 8-byte limit.

Structure of an ARRAY tag in the one-dimensional array:

![Introduction](images/93418101003_DV_resource.Stream@PNG-en-US.png)

Components with BOOL data type start in the least significant bit. Components with BYTE and CHAR data type start in the right byte. The individual components are listed in order.

Structure of an ARRAY tag in the multidimensional array:

![Introduction](images/93441377803_DV_resource.Stream@PNG-en-US.png)

In multidimensional arrays, the components are stored line-by-line (dimension-by-dimension), starting with the first dimension. In bit and byte components a new dimension always starts at the next byte. In components of other data types a new dimension always starts in the next word (in the next even byte) in non-optimized blocks.

In optimized blocks each dimension requires as much space as the first dimension.

### Addressing ARRAY components

#### Introduction

ARRAY components are addressed using fixed of variable index. The components of an ARRAY tag can be treated like tags of the same data type.

The index of the component is specified in square brackets. The index includes an integer value (fixed index) or a tag (variable index) for each ARRAY dimension.

#### Addressing of ARRAY components using fixed index

The addressing of an ARRAY component using fixed index has the following form:

![Addressing of ARRAY components using fixed index](images/93732693643_DV_resource.Stream@PNG-de-DE.png)

#### Addressing ARRAY components using variable index

An ARRAY component can also be addressed with a tag the value of which is only calculated during runtime. The tag can be an absolute or symbolic addressed global or local tag of integer data type. This addressing is also possible with multidimensional ARRAYs and with the addressing of sub-arrays. (&lt;ArrayName&gt;[i,j,k...])

A change of the tags in the called block has no effect on an ARRAY component that is created as actual parameter at an in/out parameter and addressed using a variable index. The value is written back to the same ARRAY component, transferred during the call, from which it was read.

The addressing of an ARRAY component using an index tag has the following form:

![Addressing ARRAY components using variable index](images/93739716875_DV_resource.Stream@PNG-de-DE.png)

For more information on the indirect addressing of ARRAY components, refer to:

- [Indirect indexing of ARRAY components](Programming%20basics.md#indirect-indexing-of-array-components-s7-1200-s7-1500)
- Programming recommendations:[Indirect addressing of ARRAY components](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#indirect-addressing-of-array-components-s7-1200-s7-1500)

#### Error handling for ARRAY access

Access errors result when you access an element during runtime which is located outside the declared ARRAY limits. The various CPU families react differently to violations of the ARRAY limits:

- S7-300/400

  - The CPU changes to "STOP" mode.
  - You can program the program execution error OB (OB 85) to prevent this.
  - In SCL, you also have the option of enabling the attribute "Check ARRAY limits" in the block properties. This causes the enable output ENO to be set to FALSE in the case of ARRAY access errors.
- S7-1200

  - The CPU generates a diagnostic buffer entry and remains in "RUN" mode.
- S7-1500

  - The CPU changes to "STOP" mode.
  - You can program the programming error OB (OB 121) to prevent this.
  - You also have the option of programming the local error handling with the instructions "GET_ERROR: Get error locally" or "GET_ERROR_ID: Get error ID locally".

> **Note**
>
> **Monitoring ARRAY access errors with ENO**
>
> The enable output ENO is not set to the signal state FALSE if the ARRAY limits are violated during execution of an instruction. The only exception is SCL blocks on CPUs of the S7-300/400 series for which the block property "Check ARRAY limits" is set.

### Transferring tags of the ARRAY / ARRAY[*] data type

#### Transferring tags of the ARRAY data type

You can also transfer individual elements of an ARRAY as actual parameter if the element corresponds to the data type of the formal parameter.

You can transfer tags of the ARRAY data type as parameters. If a block has an input parameter of ARRAY data type, you must pass an ARRAY with identical structure as the actual parameter. This means that the data type, the number of dimensions and the number of field components must be identical.

ARRAYs can be assigned to one another if they have an identical structure. This means that the data type, the number of dimensions and the number of array components must be identical. The names of the ARRAYs do not have to match.

#### Transferring tags of the ARRAY data type[*]

You can use ARRAY[*] to declare ARRAYs with variable limits at the parameters of a function or function block. When you create the block you can define the limits of the ARRAY that will be transferred later during runtime after the call during runtime.

The following figure shows two calls of a block with an input parameter of the ARRAY[*] data type. ARRAYs of different length are transferred with each call.

![Transferring tags of the ARRAY data type[*]](images/86477189259_DV_resource.Stream@PNG-de-DE.png)

#### Applicable rules when transferring ARRAYs with flexible limits

Create the function "BlockWithArrayStarIn_FC" for the example so that it can be called later:

![Applicable rules when transferring ARRAYs with flexible limits](images/96000264075_DV_resource.Stream@PNG-de-DE.png)

The assignment of ARRAY[*] to ARRAY[*] is permitted if the number of dimensions and the data type match. However, you cannot transfer individual ARRAY components in this process:

1. Declare the function block "BlockCaller_FB" and call the function "BlockWithArrayStarIn_FC":

   ![Applicable rules when transferring ARRAYs with flexible limits](images/96011620747_DV_resource.Stream@PNG-de-DE.png)

The assignment of an ARRAY with known limits to an ARRAY[*] is permitted if the number of dimensions and the data type match. Here, you can also assign individual ARRAY components.

1. Declare the function block "BlockCallerFixLimits_FB" and call the function "BlockWithArrayStarIn_FC" twice:

   ![Applicable rules when transferring ARRAYs with flexible limits](images/96011629579_DV_resource.Stream@PNG-de-DE.png)

The assignment of ARRAY[*] to VARIANT is permitted. Here, you can also assign individual ARRAY components.

1. Create the function "BlockWithVariantIn_FC" so that it can be called:

   ![Applicable rules when transferring ARRAYs with flexible limits](images/96012240011_DV_resource.Stream@PNG-de-DE.png)
2. Declare the function "BlockWithArrayStarInVariant_FC" and call the function "BlockWithVariantIn_FC":​

   ![Applicable rules when transferring ARRAYs with flexible limits](images/96013976843_DV_resource.Stream@PNG-de-DE.png)

The assignment of ARRAY[*] to ARRAYs with fixed limits is not permitted.

> **Note**
>
> Block parameters of the ARRAY[*] type must be supplied with an actual parameter.

---

**See also**

[Rules for supplying block parameters](Programming%20basics.md#rules-for-supplying-block-parameters)

### Examples of how to use ARRAYs

This section contains information on the following topics:

- [Example of a multi-dimensional ARRAY](#example-of-a-multi-dimensional-array)
- [Example for calculating the scalar product of two vectors with ARRAY[*]](#example-for-calculating-the-scalar-product-of-two-vectors-with-array)

#### Example of a multi-dimensional ARRAY

##### Description

Tags of the ARRAY data type can contain up to 6 dimensions. The same rules apply as for one-dimensional ARRAYs. The dimension areas are written in the declaration in square brackets, each separated by a comma. In multidimensional arrays, the components are stored starting with the first dimension.

The following table shows the declaration of a two-dimensional tag of the ARRAY data type:

| Name | Data type | Value | Comment |
| --- | --- | --- | --- |
| Betr_Temp | ARRAY[1..2, 1..3] of INT | 1,1,4(0) | Two-dimensional tag of the ARRAY data type with 6 components The first two components are assigned the value "1". The remaining four components are assigned the value "0". |

The following figure shows the structure of the declared tag of the ARRAY data type:

![Description](images/82014336523_DV_resource.Stream@PNG-de-DE.png)

##### Access to the components

The values of the individual components are accessed via an index. You can use a constant or a tag for the index. The index of the first component is, for example, [1,1] and the index of the fourth array component is [2,1]. For example, you need to declare "Station[2,1]" in the program to enable access to the value of the fourth component.

#### Example for calculating the scalar product of two vectors with ARRAY[*]

##### Description

The scalar product is a mathematical link that assigns a number to two vectors (scalar).

The scalar product of two vectors results in a scalar variable and is defined by:

![Description](images/96310193547_DV_resource.Stream@PNG-de-DE.png)

Here ∝ is the angle between the two vectors ![Description](images/96307428235_DV_resource.Stream@PNG-de-DE.png) and ![Description](images/96309988491_DV_resource.Stream@PNG-de-DE.png) .

An example for calculating the scalar product is:

![Description](images/96310970379_DV_resource.Stream@PNG-de-DE.png)

In this case, the result is the number 22.

In the following programming example, you see how you can calculate the scalar product of two vectors with flexible ARRAY bounds using ARRAY[*]. Here, the function "ScalarProduct_FC" serves as a template for calculating the individual scalar products.

You need the following objects for the programming example:

- Two data blocks and a PLC data type (UDT) for managing the vector data.
- Function that contains the program code for calculating the scalar product.
- The two instructions "LOWER_BOUND" and "UPPER_BOUND" to read out the ARRAY bounds.
- Organization block for calculating the scalar products

##### Procedure

In this example vectors, that is to say ARRAYs with 1 dimension, are used. Other calculations, such as matrix multiplications, can of course work with multi-dimensional ARRAYs.

To calculate the scalar products, follow these steps:

1. Create the PLC data type (UDT) "VectorArrays_UDT":

   ![Procedure](images/96310979211_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96310979211_DV_resource.Stream@PNG-de-DE.png)

   The two ARRAYs "VectorD5Coordinates" and "VectorE13Coordinates" provide a data basis with which you can then calculate scalar products.
2. Create the "VectorArrays1_DB" data block on the basis of the "VectorArrays_UDT" PLC data type:

   ![Procedure](images/96318783243_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96318783243_DV_resource.Stream@PNG-de-DE.png)
3. Create the second "VectorArrays2_DB" data block. Besides the vectors from the "VectorArrays_UDT" PLC data type, it also contains two other vectors:

   ![Procedure](images/96319188875_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96319188875_DV_resource.Stream@PNG-de-DE.png)

   You have now created the data basis for calculating the scalar products.
4. Create the "ScalarProduct_FC" function as a template for creating the calculation procedure for calculating the scalar product:

   The block interface:

   ![Procedure](images/96319927307_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96319927307_DV_resource.Stream@PNG-de-DE.png)

   Program code:

   ![Procedure](images/96319936139_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96319936139_DV_resource.Stream@PNG-de-DE.png)

   The upper and lower ARRAY bounds of vector 1 and vector 2 are queried in rows 1–4. It is then known how many coordinates the two ARRAYs of the vectors have. As the scalar product cannot be established until the number of coordinates of the two vectors that you wish to multiply is equal, rows 6 to 9 are required

   If the two lower or upper bounds of the ARRAYs are not the same, the "ScalarProduct_FC" function produces the function value "-1" and the program block is exited (RETURN).

   If the two lower or upper bounds of the ARRAY are the same, the #Sum tag in initialized (row 10) with the value "0" and the calculation of the scalar product is executed (rows 11 - 13).
5. Create the "Main_OB" organization block with the event class "Program cycle". The "ScalarProduct_FC" function created in step 4 now serves as a template for calculating scalar products in "Main_OB":

   The block interface:

   ![Procedure](images/96321877771_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96321877771_DV_resource.Stream@PNG-de-DE.png)

   Program code:

   ![Procedure](images/96327813003_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96327813003_DV_resource.Stream@PNG-de-DE.png)

##### Result

The results of the individual scalar product calculations are written in the tags #Result1 -5.

## Pointer

This section contains information on the following topics:

- [References (S7-1500)](References%20%28S7-1500%29.md#references-s7-1500)
- [VARIANT (S7-1200, S7-1500)](#variant-s7-1200-s7-1500)
- [POINTER (S7-300, S7-400, S7-1500)](#pointer-s7-300-s7-400-s7-1500)
- [ANY (S7-300, S7-400, S7-1500)](#any-s7-300-s7-400-s7-1500)

### VARIANT (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on VARIANT (S7-1200, S7-1500)](#basic-information-on-variant-s7-1200-s7-1500)
- [Applications for pointers in the comparison (S7-1200, S7-1500)](#applications-for-pointers-in-the-comparison-s7-1200-s7-1500)
- [VARIANT instructions (S7-1200, S7-1500)](#variant-instructions-s7-1200-s7-1500)
- [Application options for VARIANT instructions (S7-1200, S7-1500)](#application-options-for-variant-instructions-s7-1200-s7-1500)
- [Initializing VARIANT (S7-1200, S7-1500)](#initializing-variant-s7-1200-s7-1500)
- [Transferring and reading out various data types with VARIANT (S7-1200, S7-1500)](#transferring-and-reading-out-various-data-types-with-variant-s7-1200-s7-1500)
- [Examples of using the VARIANT data type (S7-1200, S7-1500)](#examples-of-using-the-variant-data-type-s7-1200-s7-1500)

#### Basic information on VARIANT (S7-1200, S7-1500)

##### Description

A parameter of VARIANT data type is a pointer or a reference It can point to tags of various data types. The VARIANT pointer cannot point to an instance and therefore cannot point to a multiple instance or ARRAY of multiple instances. The VARIANT pointer can be an object of an elementary data type, such as INT or REAL. It can also be a STRING, DTL, ARRAY of STRUCT, UDT, or ARRAY of UDT. The VARIANT pointer can recognize structures and point to individual structure components. An operand of data type VARIANT occupies no space in the instance data block or work memory. However, it will occupy memory space on the CPU.

A tag of the VARIANT type is not an object but rather a reference to another object. Individual elements of the VARIANT type can only be declared on formal parameters within the block interface of a function in the VAR_IN, VAR_IN_OUT and VAR_TEMP sections. For this reason, it cannot be declared in a data block or in the static section of the block interface of a function block, for example, because its size is unknown. The size of the referenced objects can change.

Using the VARIANT data type, you can in particular create generic, standardized function blocks (FB) or functions (FC) for various data types. Various instructions in all programming languages are available to you for this purpose. During the creation of the program, you can specify which data types the block should be able to process. The VARIANT data type supports you here by allowing the interconnection of any tags. You can then react accordingly to their data types in the block. When a block is called, you can connect the parameters of the block to tags of any data type. When a block is called, the type information of the tag is transferred in addition to a pointer to the tag. The code of the block can then be executed according to its type in line with the tag transferred during runtime.

If, for example, a block parameter of a function has the VARIANT data type, then a tag of the integer data type can be transferred at one point in the program, and a tag of the PLC data type can be transferred at another point in the program. With the help of the VARIANT instructions, the function is then in a position to react to the situation without errors.

> **Note**
>
> You can only point to a complete data block if it was originally derived from a user-defined data type (UDT).

> **Note**
>
> **Address I/O**
>
> Direct reading or writing of a signal from an I/O input or output is only possible on a CPU of an S7-1500 module. (&lt;Operand&gt;: P)

The following table shows the properties of the VARIANT pointer:

| Length (bytes) | Representation | Format | Example of value input |
| --- | --- | --- | --- |
| 0 | Symbolic | Operand | "TagResult" |
| NameDataBlock.NameOperand.Component | "Data_TIA_Portal".StructVariable.FirstComponent |  |  |
| Absolute | Operand | %MW10 |  |
| DataBlockNumber.Operand Type Length | P#DB10.DBX10.0 INT 12 <sup>1)</sup> |  |  |
| NULL pointer | NULL |  |  |
| <sup>1)</sup> If you use the prefix P#, you can only point to memory areas with "standard" access mode. |  |  |  |

##### Coding of data types

If you use absolute addressing with P#, the following data types are permitted:

- BOOL
- BYTE
- CHAR
- WORD
- INT
- DWORD
- DINT
- REAL
- TIME
- S5TIME
- DATE
- TOD
- DT

##### Example

The following example shows how VARIANT works using the "MOVE: Move value" instruction of STL:

| STL | Explanation |
| --- | --- |
| CALL MOVE | // The instruction is called. |
| value_type := VARIANT | // Data type of the parameters IN and OUT |
| IN := "Data_TIA_Portal".StructVariable.FirstComponent | // The contents of the "FirstComponent" operand are moved from the "Data_TIA_Portal" DB. |
| OUT := "MotorDB".StructResult.TagResult | // And transferred to the "TagResult" operand from the "MotorDB" DB. |

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Basics of block access](Programming%20basics.md#basics-of-block-access)
  
[Principles of block calls](Programming%20basics.md#principles-of-block-calls)
  
[VARIANT instructions (S7-1200, S7-1500)](#variant-instructions-s7-1200-s7-1500)
  
[Accessing I/O devices](Programming%20basics.md#accessing-io-devices)
  
[Data type conversion for S7-1200 (S7-1200)](#data-type-conversion-for-s7-1200-s7-1200)

#### Applications for pointers in the comparison (S7-1200, S7-1500)

##### Application cases for pointers with an S7-1200/1500 CPU as compared to S7-300/400

The following table provides you with an overview of the various applications for pointers on a CPU of the S7-300/400 series (ANY pointer) and their solution with a CPU of the S7-1200/1500 series.

In most applications, the use of a pointer is no longer required on a CPU of the S7-1200/1500 series. Instead, much simpler language resources are available.

It is only advisable to use the VARIANT data type for indirect addressing, when the data types are only determined during the program runtime.

| What is the purpose of the ANY pointer? | Recommendations in the TIA Portal (S7-1200/S7-1500) |
| --- | --- |
| Moving data of any source and destination data type in the program using the instruction "BLKMOV: Move block". | Definition of tags within a PLC data type. You can use the instructions "Serialize" and "Deserialize" to move the tags. |
| Initializing an ARRAY structure | Using the instruction "FILL_BLK: Fill block", you initialize or fill an ARRAY structure. |
| Moving ARRAY elements | Using the instruction "MOVE_BLK: Move block". you move the content of multiple elements of an ARRAY structure to another ARRAY structure. |
| Memory and performance optimization using structured data | Use the InOut section in the block interface to optimize memory and performance.  You can find additional information in the "Programming Guideline for S7-1200/1500" under the following link [Programming Guideline for S7-1200/1500](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=4&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&groupid=4000002&extranet=standard&viewreg=WW&nodeid4=20229695&objaction=csopen) |
| Access to individual bits/bytes of a WORD | Use the "slice access"  You can find additional information here: [Example of a slice access](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=0&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&groupid=4000002&extranet=standard&viewreg=WW&nodeid0=29156492&objaction=csopen) |
| Determination of the length of structures or data blocks | Use an ARRAY and read its length using the instruction "CountofElements: Get number of ARRAY elements". The instruction only works in conjunction with the data type VARIANT. |
| Indirect addressing | You can use the VARIANT pointer for the indirect addressing of data types that will only be known during runtime. You can use the data type DB_ANY for indirect access to a data block. |

#### VARIANT instructions (S7-1200, S7-1500)

##### VARIANT instructions

The following instructions for working with VARIANT are available to you in the TIA Portal:

| Basic instructions |  |  |
| --- | --- | --- |
| Category | Instruction | Description |
| Comparator operations | EQ_Type | Compare data type for EQUAL with the data type of a tag |
| NE_Type | Compare data type for UNEQUAL with the data type of a tag |  |
| EQ_ElemType | Compare data type of an ARRAY element for EQUAL with the data type of a tag |  |
| NE_ElemType | Compare data type of an ARRAY element for UNEQUAL with the data type of a tag |  |
| IS_NULL | Query for EQUALS ZERO pointer |  |
| NOT_NULL | Query for UNEQUALS ZERO pointer |  |
| IS_ARRAY | Check for ARRAY |  |
| TypeOf | Check data type of a VARIANT tag |  |
| TypeOfElements | Check element data type of a VARIANT tag |  |
| Move operations | MOVE_BLK_VARIANT | Move block |
| VariantGet | Read out VARIANT tag value |  |
| VariantPut | Write VARIANT tag value |  |
| CountOfElements | Get number of ARRAY elements |  |
| Conversion operations | VARIANT_TO_DB_ANY | Convert VARIANT to DB_ANY |
| DB_ANY_TO_VARIANT | Convert DB_ANY to VARIANT |  |

> **Note**
>
> **Differences between MOVE, MOVE_BLK and MOVE_BLK_VARIANT**
>
> - You can use the "MOVE" instruction to copy complete structures.
> - You can use the "MOVE_BLK" instruction to move parts of ARRAYs with known data type.
> - The MOVE_BLK_VARIANT instruction is only required if you want to move parts of ARRAYs with a data type that is only known during program runtime.

You can find additional information on the individual instructions in the information system under "Basic instructions &gt; Respective programming language".

You can also find additional instructions which also work with the VARIANT data type under the "Extended instructions".

---

**See also**

[Basic information on VARIANT (S7-1200, S7-1500)](#basic-information-on-variant-s7-1200-s7-1500)
  
[Indirect addressing with the VARIANT data type](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=0&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&groupid=4000002&extranet=standard&viewreg=WW&nodeid0=29156492&objaction=csopen)

#### Application options for VARIANT instructions (S7-1200, S7-1500)

##### Introduction

In the following chapter, you will learn which application options you have with VARIANT instructions.

##### Evaluating data types of tags to which a VARIANT points

In the table below, you see which instructions are available to you to evaluate data types of tags to which a VARIANT points:

| Function | Instruction | Description |
| --- | --- | --- |
| To determine the data type | TypeOf(): Check data type of a VARIANT tag  (This instruction is available only in SCL and only in conjunction with an IF or CASE instruction.) | You use this instruction to compare the data type to which a VARIANT tag points with the data type of any other tag. You can also make the comparison with a PLC data type. |
| TypeOfElements(): Scan data type of an ARRAY element of a VARIANT tag  (This instruction is available only in SCL and only in conjunction with an IF or CASE instruction.) | You use this instruction to compare the data type to which a VARIANT tag points with the data type of any other tag. You can also make the comparison with a PLC data type. If the data type of the VARIANT tag is an ARRAY, the data type of the ARRAY elements is compared. |  |
| EQ_Type: Compare data type for EQUAL with the data type of a tag  NE_Type: Compare data type for UNEQUAL with the data type of a tag | You use this instruction to compare the data type to which a VARIANT tag points with the data type of any other tag. You can also make the comparison with a PLC data type. |  |
| EQ_ElemType: Compare data type of an ARRAY element for EQUAL with the data type of a tag  NE_ElemType: Compare data type of an ARRAY element for UNEQUAL with the data type of a tag | You use this instruction to compare the data type to which a VARIANT tag points with the data type of any other tag. You can also make the comparison with a PLC data type. If the data type of the VARIANT tag is an ARRAY, the data type of the ARRAY elements is compared. |  |
| To evaluate ARRAY elements | IS_ARRAY: Check for ARRAY | You use this instruction to check whether the data type to which a VARIANT tag points is an ARRAY. |
| CountOfElements: Get number of ARRAY elements | You use this instruction to read out how many ARRAY elements the tag has to which the VARIANT tag points. |  |

You can find additional information on the individual instructions in the information system under "Basic instructions &gt; Respective programming language".

##### Reading data to which a VARIANT points

To be able to use the data you must move this data to a tag as an intermediate step, as it cannot be processed directly.

| Instruction | Description | Example |  | Result |
| --- | --- | --- | --- | --- |
| VARIANT points to | Destination data type |  |  |  |
| VariantGet: Read out VARIANT tag value | You use this instruction to move the value of a single tag to another tag. The data types of both tags must match. | UDT_1 | UDT_1 | The instruction is executed |
| REAL | REAL |  |  |  |
| DINT | DWORD | The instruction is not executed. |  |  |

##### Assigning data to a VARIANT tag

You cannot use the instruction to initialize VARIANT tags. The VARIANT tags must therefore already be initialized when the data is returned to the tag. Do not use uninitialized temporary VARIANT tags.

| Instruction | Description | Example |  | Result |
| --- | --- | --- | --- | --- |
| Source data type | VARIANT points to: |  |  |  |
| VariantPut: Write VARIANT tag value | You use this instruction to move the value of a single tag to another tag. The data types of both tags must match. | UDT_1 | UDT_1 | The instruction is executed |
| REAL | REAL |  |  |  |
| DINT | DWORD | The instruction will not be executed, as the data types are different. |  |  |

##### Processing dynamic ARRAY structures

|  |  |  |
| --- | --- | --- |
| To evaluate ARRAY elements | TypeOfElements(): Scan data type of an ARRAY element of a VARIANT tag  (This instruction is available only in SCL and only in conjunction with an IF or CASE instruction.) | You use this instruction to compare the data type to which a VARIANT tag points with the data type of any other tag. You can also make the comparison with a PLC data type. If the data type of the VARIANT tag is an ARRAY, the data type of the ARRAY elements is compared. |
| IS_ARRAY: Check for ARRAY | You use this instruction to check whether the data type to which a VARIANT tag points is an ARRAY. |  |
| CountOfElements: Get number of ARRAY elements | You use this instruction to read out how many ARRAY elements the tag has to which the VARIANT tag points. |  |
| MOVE_BLK_VARIANT: Move block | This instruction is used to move dynamic and type-safe (integrated type test) ARRAYs. You can freely select the limit values for the source and destination ARRAYs. The data types of ARRAY elements must match. |  |

> **Note**
>
> **Differences between MOVE, MOVE_BLK and MOVE_BLK_VARIANT**
>
> - You can use the "MOVE" instruction to copy complete structures.
> - You can use the "MOVE_BLK" instruction to move parts of ARRAYs with known data type.
> - The MOVE_BLK_VARIANT instruction is only required if you want to move parts of ARRAYs with a data type that is only known during program runtime.

Additional information on the use of the MOVE_BLK_VARIANT instruction can be found in the "Moving data" programming example.

---

**See also**

[Basic information on VARIANT (S7-1200, S7-1500)](#basic-information-on-variant-s7-1200-s7-1500)
  
[Example of moving data (S7-1200, S7-1500)](#example-of-moving-data-s7-1200-s7-1500)

#### Initializing VARIANT (S7-1200, S7-1500)

##### Description

Initialize the VARIANT data type by assigning a specific tag to the VARIANT block parameter at the block call. This forms a reference to the address of the passed tag. To do this, create a block parameter of the VARIANT data type in the block interface. In the following example, these are the two block parameters SourceArray and DestinationArray in the section InOut.

![Description](images/67642737291_DV_resource.Stream@PNG-de-DE.png)

The example shows a section from the programming example "Example of moving data". You can find the detailed program code under "See also".

> **Note**
>
> Direct passing of a tag to a VARIANT tag is not possible, such as myVARIANT := #Variable

---

**See also**

[Example of moving data (S7-1200, S7-1500)](#example-of-moving-data-s7-1200-s7-1500)

#### Transferring and reading out various data types with VARIANT (S7-1200, S7-1500)

The example shows a section from the programming example "Example of moving data". You can find the detailed program code under "See also".

> **Note**
>
> **VARIANT as formal parameter**
>
> If the VARIANT is declared as a formal parameter, no write-protected data may be transferred as actual parameters.

##### Passing various data types

In the following example, you see how the VARIANT block parameter can be initialized with different tags when a generic, standardized function is called multiple times:

The "FC_PartialArrayCopy" function is called twice. The VARIANT parameter SourceArray is interconnected with an ARRAY of "my_struct" with the left call. The VARIANT parameter SourceArray is interconnected with an ARRAY of REAL with the right call.

![Passing various data types](images/67637339019_DV_resource.Stream@PNG-de-DE.png)

##### Reading out and checking data types

Various comparison instructions are available to you to read out the data type of a tag or an element and compare it with data types of other tags or elements.

In the figure below, you see the usage of multiple comparison instructions to check whether the elements of the ARRAYs have the same data type:

![Reading out and checking data types](images/67651462923_DV_resource.Stream@PNG-de-DE.png)

The MOVE_BLK_VARIANT instruction is only executed if the data types of the ARRAY elements are the same.

---

**See also**

[Example of moving data (S7-1200, S7-1500)](#example-of-moving-data-s7-1200-s7-1500)

#### Examples of using the VARIANT data type (S7-1200, S7-1500)

This section contains information on the following topics:

- [Example of moving data (S7-1200, S7-1500)](#example-of-moving-data-s7-1200-s7-1500)
- [Example of programming a queue (FIFO) (S7-1200, S7-1500)](#example-of-programming-a-queue-fifo-s7-1200-s7-1500)

##### Example of moving data (S7-1200, S7-1500)

###### Programming example

In this programming example, data values, which are collected for example during a production shift, are moved for further processing. The data is collected in an ARRAY. Using the "MOVE_BLK_VARIANT instruction: Move block", you can move either the entire ARRAY or only individual ARRAY elements dynamically and type-safe. You can freely select the ARRAY limits for the respective source and destination ARRAYs and these do not have to match. However, the data type of the data values that are to be moved must match. This instruction is available in all programming languages.

By using the VARIANT data type, you can use the created program code to move data for other production shifts as well, by specifying a different source and destination area at the block call.​

###### Procedure

1. Create a function using the SCL programming language and give it the name "FC_PartialArrayCopy".
2. Declare the block interface as follows:

   ![Procedure](images/67702161291_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67702161291_DV_resource.Stream@PNG-de-DE.png)
3. Create the SCL program code as follows:

   You can find the program code below as template.

   ![Procedure](images/67704242571_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67704242571_DV_resource.Stream@PNG-de-DE.png)
4. Create the PLC data type "UDT_MyStruct":

   ![Procedure](images/67704673931_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67704673931_DV_resource.Stream@PNG-de-DE.png)
5. Create the global data block "DB_WithArrays":

   ![Procedure](images/67704682507_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67704682507_DV_resource.Stream@PNG-de-DE.png)
6. Call the "FC_PartialArrayCopy" function in an organization block, for example OB1, and initialize the parameters with the DB_WithArrays data block. Enter the named constants:

   ![Procedure](images/67705880587_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67705880587_DV_resource.Stream@PNG-de-DE.png)
7. Instead of using the first two ARRAYs, which have the data type UDT_MyStruct, you can also use the third and fourth ARRAY, which have the data type REAL:

   ![Procedure](images/67807724299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/67807724299_DV_resource.Stream@PNG-de-DE.png)

###### Result

As soon as the "FC_PartialArrayCopy" block is called in the program cycle, two data values, starting with the fourth element, are copied from the first ARRAY of the "DB_WithArrays" global data block to the second ARRAY of the data block. The copied data values are inserted in the second ARRAY, starting from the fourth element.

SCL program code for copying:

SCL

IF IS_ARRAY(#SourceArray) AND TypeOfElements(#SourceArray) = TypeOfElements(#DestinationArray) THEN

#Error := MOVE_BLK_VARIANT(COUNT := #Count, SRC := #SourceArray, SRC_INDEX := #SourceIndex,

DEST =&gt; #DestinationArray, DEST_INDEX := #DestinationIndex);

END_IF;

#FC_PartialArrayCopy := #Error;

---

**See also**

[Basic information on VARIANT (S7-1200, S7-1500)](#basic-information-on-variant-s7-1200-s7-1500)

##### Example of programming a queue (FIFO) (S7-1200, S7-1500)

###### Programming example

In the following example, you program a ring buffer which consists of an ARRAY and is written and read according to the FIFO principle. The program code has a read-VARIANT pointer and a write-VARIANT pointer. Using the VARIANT instructions, you can program the program code robustly and ensure reliable copying or deleting.

Using the VARIANT data type, program sections can be influenced during runtime. The VARIANT pointer is a type-safe pointer, i.e. a type test is performed during runtime. For blocks that have been created with the block property "optimized", sub-functions that were previously programmed with an ANY pointer can now be resolved with a VARIANT pointer. The VARIANT data type is used to transfer structures to system function blocks.

###### Procedure

| 1. Create an SCL function block and name it "FIFOQueue". 2. Declare the block interface as follows:       | Declaration | Parameters | Data type | Comment |    | --- | --- | --- | --- |    | Input | request | BOOL | The instruction is executed when a positive signal edge is detected at the "request" parameter. |    | mode | BOOL | 0 = The first entry in the ring buffer is returned. 1 = An entry is written at the last position in the ring buffer. |  |    | initialValue | VARIANT | Value with which the ARRAY of the ring buffer is initialized. |  |    | Output | error | INT | Error information |    | InOut | item | VARIANT | The entry that is either returned from the ring buffer or written to the ring buffer. |    | buffer | VARIANT | An ARRAY that is used as a ring buffer. |  |    | Static | edgeupm | BOOL | Edge memory bit in which the RLO of the previous query is saved. |    | firstItemIndex | INT | Index of the oldest entry in the ring buffer |  |    | nextEmptyItemIndex | INT | Index of the next free entry in the ring buffer |  |    | Temp | edgeup | BOOL | Result of edge evaluation |    | internalError | INT | Error information |  |    | newFirstItemIndex | INT | Variable index |  |    | newNextEmptyItemIndex | INT | Variable index |  |    | bufferSize | UDINT | Number of ARRAY elements in the ring buffer |  | 3. Create the following program code in the "FIFOQueue" function block: |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

(* This program code section is only executed once after a positive signal edge. If there is no change in the signal state of the result of logic operation, the program processing of the "FIFOQueue" FB is terminated. *)

#edgeup := #request &amp; NOT #edgeupm;

#edgeupm := #request;

IF NOT (#edgeup) THEN

RETURN;

END_IF;

  

// ------Validation of whether all parameter inputs are valid.----

(* This program code section checks whether the ring buffer is an ARRAY. If so, the number of the ARRAY elements is read out. If it is not an ARRAY, the program execution is terminated at this point and the error code "-10" is output. *)

IF NOT (IS_ARRAY(#buffer)) THEN

#error := -10;

RETURN;

ELSE

#bufferSize := CountofElements(#buffer);

END_IF;

 

(* This program code section checks whether the data type of the ARRAY elements matches the data type of the entry (tag #item). If the data types do not match, the program execution is terminated at this point and the error code "-11" is output. *)

IF NOT (TypeOf(#item) = TypeOfElements(#buffer)) THEN

#error := -11;

RETURN;

END_IF;

 

(* This program code section checks whether the initial value of the ring buffer matches the entry (tag #item). If the data types do not match, the program execution is terminated at this point and the error code "-12" is output. *)

IF NOT (TypeOf(#item) = TypeOf(#initialValue)) THEN

#error := -12;

RETURN;

END_IF;

 

(* This program code section checks whether the variable indices are within the ARRAY limits. If this is not the case, the program execution is terminated at this point and either error code "-20" or "-21" is output depending on the index. *)

IF (#nextEmptyItemIndex &gt;= #bufferSize) THEN

#error := -20;

RETURN;

END_IF;

IF (#firstItemIndex &gt;= #bufferSize) THEN

#error := -21;

RETURN;

END_IF;

  

//-----------Program code execution, depending on the Mode parameter-------------

// The execution of the instructions depends on the signal state of the Mode parameter.

IF #mode = 0 THEN

 

// If the Mode parameter has the signal state "0", the first entry from the passed ring buffer is returned.

(* This program code section checks whether the ring buffer is empty. If this is the case, program execution is terminated at this point and the error code "-40" is output. *)

IF (#firstItemIndex = -1) THEN

#error := -40;

RETURN;

END_IF;

 

// This program code section returns the first entry of the ring buffer.

#internalError := MOVE_BLK_VARIANT(SRC := #buffer,

COUNT := 1,

SRC_INDEX := #firstItemIndex,

DEST_INDEX := 0,

DEST =&gt; #item);

 

IF (#internalError = 0) THEN

(* This program code section checks whether the ring buffer contains ARRAY elements. If it does, the first entry is passed on and the index is incremented by 1. *)

#internalError := MOVE_BLK_VARIANT(SRC := #initialValue,

COUNT := 1,

SRC_INDEX := 0,

DEST_INDEX := #firstItemIndex,

DEST =&gt; #buffer);

 

// This program code section calculates the new index of the first entry.

#newFirstItemIndex := #firstItemIndex +1;

#newFirstItemIndex := #newFirstItemIndex MOD UDINT_TO_INT(#bufferSize);

 

// This program section checks whether the ring buffer is empty.

IF (#nextEmptyItemIndex = #newFirstItemIndex) THEN

// If the ring buffer is empty, the index is set to 0.

#firstItemIndex := -1;

#nextEmptyItemIndex := 0;

ELSE

// The index of the first entry is changed.

#firstItemIndex := #newFirstItemIndex;

END_IF;

END_IF;

ELSE

  

// If the Mode parameter has the signal state "1", the entry is written to the passed ring buffer.

(* This program code section checks whether the ring buffer is full. If this is the case, program execution is terminated at this point and the error code "-50" is output. *)

IF (#nextEmptyItemIndex = #firstItemIndex) THEN

#error := -50;

RETURN;

END_IF;

 

// This program code section writes the entry to the ring buffer.

#internalError := MOVE_BLK_VARIANT(SRC := #item,

COUNT := 1,

SRC_INDEX := 0,

DEST_INDEX := #nextEmptyItemIndex,

DEST =&gt; #buffer);

 

IF (#internalError = 0) THEN

// This program code section increments the index by 1 and calculates the new empty entry index.

#newNextEmptyItemIndex := #nextEmptyItemIndex +1;

#newNextEmptyItemIndex := #newNextEmptyItemIndex MOD #bufferSize;

#nextEmptyItemIndex := #newNextEmptyItemIndex;

 

(* This program code section checks which index the "#firstItemIndex" tag has. If the number = -1, the ring buffer is initialized and the entry is written to the ring buffer. This is why the tag value "0" must be assigned. *)

IF (#firstItemIndex = -1) THEN

#firstItemIndex := 0;

END_IF;

END_IF;

END_IF;

 

//-------------------------Local error handling----------------------------

(* This program code section checks whether a local error has occurred. If this is the case, program execution is terminated at this point and the error code "-100" is output. *)

IF (#internalError &gt; 0) THEN

#error := -100;

RETURN;

END_IF;

 

// If no error occurred during program execution, the error code "0" is output.

#error := 0;

###### Result

Call the SCL function block at the position in your program at which the FIFO queue is to run.

### POINTER (S7-300, S7-400, S7-1500)

#### Description

A parameter of the type POINTER is a pointer that can point to a specific tag. It occupies 6 bytes (48 bits) in memory and may contain the following tag information:

- DB number, or 0 if the data is not stored in a DB
- Memory area in the CPU
- Tag address

The following figure shows the structure of parameter type POINTER:

![Description](images/40118211851_DV_resource.Stream@PNG-en-US.png)

#### Types of pointer

Depending on the information, you can use parameter type POINTER to declare the following four types of pointer:

- Area-internal pointer:

  An area-internal pointer contains information on the address of a tag.
- Cross-area pointer:

  A cross-area pointer contains information on the memory area and the address of a tag.
- DB pointer:

  You can use a DB pointer to point to a data block tag. A DB pointer also contains a data block number in addition to the memory area and the address of a tag.
- Zero pointer:

  Use the zero pointer to indicate a missing value. A missing value may indicate that no value exists, or that the value is not yet known. A zero value represents the absence of a value, but is also a value.

The following table shows the formats for the declaration of various pointer types:

| P#ByteRepresentation | Format | Example of value input | Description |
| --- | --- | --- | --- |
| Symbolic | P#Byte.Bit | "MyTag" | Area-internal pointer |
| P#OperandAreaByte.Bit | "MyTag" | Cross-area pointer |  |
| P#Data_block.Data_operand | "MyDB"."MyTag" | DB pointer |  |
| P#Zero value | - | Zero pointer |  |
| Absolute | P#Byte.Bit | P#20.0 | Area-internal pointer |
| P#OperandAreaByte.Bit | P#M20.0 | Cross-area pointer |  |
| P#Data_block.Data_operand | P#DB10.DBX20.0 | DB pointer |  |
| P#Zero value | P#0.0, ZERO | Zero pointer |  |

#### The prefix P#

Enter the actual value without prefix P# in the block call to supply a formal parameter of the POINTER data type. The entry is then automatically converted to the POINTER format.

If you use the prefix P#, you can only point to memory areas with "Standard" access mode. You can find additional information and a direct comparison of the two access options here:

- [Basics of block access](Programming%20basics.md#basics-of-block-access)
- [The new S7-1200/1500 CPU functions and programming recommendations at a glance](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#the-new-s7-12001500-cpu-functions-and-programming-recommendations-at-a-glance-s7-1200-s7-1500)

The following should be noted when using the prefix P# in the STL programming language:

| Block type | "Optimized" access mode | "Standard" access mode |
| --- | --- | --- |
| Function (FC) | A tag cannot be used in the program code with the prefix P#. | The following tags can be used in the program code with the prefix P#.  - Structured tags that are declared in the InOut section of the block interface.   Tags with elementary data types cannot be used with the prefix P#. |
| Function block (FB) | A tag cannot be used in the program code with the prefix P#. | The following tags can be used in the program code with the prefix P#.  - Tags that have been declared in the sections Static, Input and Output of the block interface. - Tags with the PLC data type (UDT) that are declared in the InOut section of the block interface. |

You can find additional information about structured and elementary data types here: [Transfer parameter as copy or as pointer](Programming%20basics.md#transfer-parameter-as-copy-or-as-pointer)

#### Memory areas

The following table shows the hexadecimal codes of the memory areas for parameter type POINTER:

| Hexadecimal code | Memory area | Description |
| --- | --- | --- |
| B#16#80<sup>1)</sup> | P | Peripherals on a CPU S7-300/400 |
| 16#1 | P | Peripheral inputs on a CPU S7-1500 |
| 16#2 | P | Peripheral outputs on a CPU S7-1500 |
| B#16#81 | I | Memory area of inputs |
| B#16#82 | Q | Memory area of outputs |
| B#16#83 | M | Memory area of bit memory |
| B#16#84 | DBX | Data block |
| B#16#85 | DIX | Instance data block |
| B#16#86 | L | Local data |
| B#16#87 | V | Previous local data (local data of the calling module) |
| B#16#C0  B#16#C1  etc. | V | Previous local data (local data of calling modules from higher levels of the call hierarchy) |
| <sup>1)</sup> These data types can only be used for the POINTER pointer on a CPU S7-300/400. |  |  |

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)

### ANY (S7-300, S7-400, S7-1500)

#### Description

An ANY type parameter points to the start of a data area and specifies its length. An ANY pointer occupies 10 bytes of memory and may contain the following information:

- Data type:

  Data type of the elements of the data area
- Repetition factor:

  Number of elements of the data area
- DB number:

  Data block that contains the declaration of data area elements.
- Memory area:

  Memory area of the CPU that stores the data area elements.
- Start address of the data in the format "byte.bit":

  Data area start identified by the ANY pointer.
- Zero pointer:

  Use the zero pointer to indicate a missing value. A missing value may indicate that no value exists, or that the value is not yet known. A zero value represents the absence of a value, but is also a value.

> **Note**
>
> **ANY pointer to a STRING**
>
> If an ANY pointer is generated in an LAD/FBD/STL or SCL network through the assignment of a string, an ANY pointer of the data type BYTE and the repetition factor maxstringlen is created.
>
> If an ANY pointer is generated in an SCL block through the assignment of a string, an ANY pointer to a STRING is created.
>
> A pointer of this type can, for instance, be created by transferring it from an SCL block to an LAD network or by superimposing it with an AT construct and manually setting the data type to STRING.

> **Note**
>
> **Access options**
>
> For a CPU of the S7-1500 series, the ANY pointer can also only point to memory areas with "Standard" access mode. You can find additional information and a direct comparison of the two access options here:
>
> - [Basics of block access](Programming%20basics.md#basics-of-block-access)
> - [The new S7-1200/1500 CPU functions and programming recommendations at a glance](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#the-new-s7-12001500-cpu-functions-and-programming-recommendations-at-a-glance-s7-1200-s7-1500)

In the programming languages SCL and STL, memory of any kind can be transferred upon a block call if an ANY pointer has been programmed at a block parameter.

The ANY pointer cannot, however, store any information on the structure of the memory. For example, the ANY pointer does not save the information that it points to a tag of the PLC data type. The ANY pointer sees this as an ARRAY of BYTE.

Parameters of the ANY data type can be passed to system function blocks (SFBs) or system functions (SFCs).

The following figure shows the structure of the ANY pointer:

![Description](images/40118940171_DV_resource.Stream@PNG-en-US.png)

An ANY pointer cannot identify structures. It can only be assigned to local tags.

The following table shows the formats for the declaration of an ANY pointer:

| Representation | Format | Example of value input | Description |
| --- | --- | --- | --- |
| Symbolic | P#DataBlock.MemoryArea DataAddress Type Number | "MyDB".StructTag.InitialComponents | Area with 10 words in global DB11 starting with DBB20.0 |
| P#MemoryArea DataAddress Type Number | "MyMarkerTag" | Area with 4 bytes starting with MB 20.0 |  |
| "MyTag" | Input I1.0 |  |  |
| P#Zero value | - | Zero value |  |
| Absolute | P#DataBlock.MemoryArea DataAddress Type Number | P#DB11.DBX20.0 INT 10 | Area with 10 words in global DB11 starting with DBB20.0 |
| P#MemoryArea DataAddress Type Number | P#M20.0 BYTE 10 | Area with 10 bytes starting with MB 20.0 |  |
| P#I1.0 BOOL 8 | Range with 8 bits from input I1.0 (the range length specified must be divisible by 8.) |  |  |
| P#Zero value | P#P0.0 VOID 0, NULL <sup>1)</sup> | Zero value |  |
| <sup>1)</sup> In the programming languages LAD and FBD, only NULL is a value entry for the zero value. |  |  |  |

#### Coding of data types

The following table lists the coding of data types for the ANY pointer:

| Hexadecimal code | Data type | Description |
| --- | --- | --- |
| B#16#00 | NIL | Null pointer |
| B#16#01<sup>1)</sup> | BOOL | Bits |
| B#16#02 | BYTE | bytes, 8 bits |
| B#16#03 | CHAR | 8-bit characters |
| B#16#04 | WORD | 16-bit words |
| B#16#05 | INT | 16-bit integers |
| B#16#06 | DWORD | 32-bit words |
| B#16#07 | DINT | 32-bit integers |
| B#16#08 | REAL | 32-bit floating-point numbers |
| B#16#0B | TIME | Time duration |
| B#16#0C | S5TIME | Time duration |
| B#16#09 | DATE | Date |
| B#16#0A | TOD | Date and time |
| B#16#0E | DT | Date and time |
| B#16#13 | STRING | Character string |
| B#16#17<sup>1)</sup> | BLOCK_FB | Function block |
| B#16#18<sup>1)</sup> | BLOCK_FC | Function |
| B#16#19<sup>1)</sup> | BLOCK_DB | Data block |
| B#16#1A<sup>1)</sup> | BLOCK_SDB | System data block |
| B#16#1C<sup>1)</sup> | COUNTER | Counter |
| B#16#1D<sup>1)</sup> | TIMER | Timer |
| <sup>1)</sup> These data types can only be used for the ANY pointer on a CPU S7-300/400. |  |  |

#### Coding of the memory area

The following table lists the coding of the memory areas for the ANY pointer:

| Hexadecimal code | Area | Description |
| --- | --- | --- |
| B#16#80<sup>1)</sup> | P | I/O |
| B#16#81 | I | Memory area of inputs |
| B#16#82 | Q | Memory area of outputs |
| B#16#83 | M | Memory area of bit memory |
| B#16#84 | DBX | Data block |
| B#16#85<sup>1)</sup> | DIX | Instance data block |
| B#16#86 | L | Local data |
| B#16#87 | V | Previous local data |
| <sup>1)</sup> These memory areas can only be used for the ANY pointer on an S7-300/400 CPU. |  |  |

---

**See also**

[Basics of indirect addressing (S7-1200, S7-1500)](Programming%20basics.md#basics-of-indirect-addressing-s7-1200-s7-1500)
  
[Overview of the valid data types](#overview-of-the-valid-data-types)
  
[Basics of constants](Programming%20basics.md#basics-of-constants)
  
[Transfer parameter as copy or as pointer](Programming%20basics.md#transfer-parameter-as-copy-or-as-pointer)

## Parameter types

This section contains information on the following topics:

- [Parameter types](#parameter-types-1)

### Parameter types

#### Description

The parameter types are data types for formal parameters that are transferred to called blocks. A parameter type can also be a PLC data type.

The following table shows the available parameter data types and their purpose:

| Parameter type | Length (bits) | Description |
| --- | --- | --- |
| TIMER | 16 | Is used to specify a timer that is used in the called code block. If you supply a formal parameter of the TIMER parameter type, the associated actual parameter must be a timer.  Example: T1 |
| COUNTER | 16 | Is used to specify a counter that is used in the called code block. If you supply a formal parameter of the COUNTER parameter type, the associated actual parameter must be a counter.  Example: C10 |
| BLOCK_FC | 16 | Is used to specify a block that is used as input in the called code block.  The declaration of the parameter determines the block type (for example FB, FC, DB) that is to be used.  If you supply a formal parameter of the BLOCK parameter type, specify a block address as the actual parameter.  Example: DB3 |
| BLOCK_FB | 16 |  |
| BLOCK_DB | 16 |  |
| BLOCK_SDB | 16 |  |

> **Note**
>
> **Parameter type "Block_DB" to transfer an instance DB**
>
> In LAD and FBD, you cannot enter the instance DB of a function block using an input of the data type "BLOCK_DB". Use a parameter instance instead.
>
> See also: [Parameter instances](Programming%20basics.md#parameter-instances)

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)

## System data types

This section contains information on the following topics:

- [System data types](#system-data-types-1)

### System data types

#### Description

The system data types (SDT) are made available by the system and have a predefined structure. The structure of a system data type consists of a fixed number of components that can have various data types. It is not possible to change the structure of a system data type.

System data types can only be assigned to one another if they are of the same type and their name matches. This also applies to PLC data types generated by the system, such as IEC_Timer, etc.

The system data types can only be used for specific instructions. The following table shows the available system data types and their purpose:

| System data type | Length (bytes) | Description |
| --- | --- | --- |
| IEC_TIMER | 16 | Structure of a timer in which the PT, ET, IN and Q parameters are declared. The time values are of TIME data type.  This data type is used for the "TP", "TOF", "TON", "TONR", "RT" and "PT" instructions, for example. |
| IEC_LTIMER | 32 | Structure of a timer in which the PT, ET, IN and Q parameters are declared. The time values are of LTIME data type.  This data type is used for the "TP", "TOF", "TON", "TONR", "RT" and "PT" instructions, for example. |
| IEC_SCOUNTER | 3 | Structure of a counter whose count values are of SINT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_USCOUNTER | 3 | Structure of a counter whose count values are of USINT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_COUNTER | 6 | Structure of a counter whose count values are of INT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_UCOUNTER | 6 | Structure of a counter whose count values are of UINT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_DCOUNTER | 12 | Structure of a counter whose count values are of DINT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_UDCOUNTER | 12 | Structure of a counter whose count values are of UDINT data type.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_LCOUNTER | 24 | Structure of a counter with count values of data type UDINT.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| IEC_ULCOUNTER | 24 | Structure of a counter with count values of data type UINT.  This data type is used for the "CTU", "CTD" and "CTUD" instructions, for example. |
| ERROR_STRUCT | 28 | Structure of an error information to a programming or I/O access error.  This data type is used, for example, for the "GET_ERROR" instruction. |
| CREF | 8 | Components of the ERROR_STRUCT data type, in which information about the address of a block is saved. |
| NREF | 8 | Components of the ERROR_STRUCT data type, in which information about the address of an operand is saved. |
| VREF | 12 | Is used for storage of a VARIANT pointer.  This data type is, for example, used for instructions from S7-1200/1500 Motion Control. |
| SSL_HEADER | 4 | Specifies the data structure in which information about the data records are saved during the reading of the system status lists. This data type is used, for example, for the "RDSYSST" instruction. |
| CONDITIONS | 52 | User-defined data structure defining the conditions for start and end of a data reception.  This data type is used, for example, for the "RCV_CFG" instruction. |
| TADDR_Param | 8 | Specifies the structure of a data block which stores descriptions of connections for Open User Communication via UDP.  This data type is used for the "TUSEND" and "TURSV" instructions, for example. |
| TCON_Param | 64 | Specifies the structure of a data block which stores descriptions of connections for Open User Communication via Industrial Ethernet (PROFINET).  This data type is used for the "TSEND" and "TRSV" instructions, for example. |
| HSC_Period | 12 | Specifies the structure of the data block for the time period measurement with the extended high-speed counter.  This data type is used, for example, for the "CTRL_HSC_EXT" instruction. |
| AssocValues | 16 | Defined data structure This defines which associated values are sent with a message.  This data type is used, for example, for the "Gen_UsrMsg" instruction. |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)

## Hardware data types

This section contains information on the following topics:

- [Hardware data types (derived data types)](#hardware-data-types-derived-data-types)

### Hardware data types (derived data types)

#### Description

The hardware data types are made available by the CPU. The number of available hardware data types depends on the CPU.

Constants of a specific hardware data type are stored based on the modules set in the hardware configuration. When an instruction for controlling or activating a configured module is inserted in the user program, the available constants can be used for the parameters.

The following table shows the available hardware data types and their purpose:

| Data type | Basic data type | Description |
| --- | --- | --- |
| REMOTE | ANY | Serves to specify the address of a remote CPU.  This data type is used, for example, for the "PUT" and "GET" instructions. |
| HW_ANY | UINT | Identification of any hardware component, e.g. a module. |
| HW_DEVICE | HW_ANY | Identification of a DP slave/PROFINET IO device |
| HW_DPMASTER | HW_INTERFACE | Identification of a DP master |
| HW_DPSLAVE | HW_DEVICE | Identification of a DP slave |
| HW_IO | HW_ANY | Identification number of the CPU or the interface  The number is automatically allocated and is stored in the properties of the CPU or of the interface in the hardware configuration. |
| HW_IOSYSTEM | HW_ANY | Identification of a PN/IO system or DP master system |
| HW_SUBMODULE | HW_IO | Identification of a central hardware component |
| HW_MODULE | HW_IO | Identification of a module |
| HW_INTERFACE | HW_SUBMODULE | Identification of an interface component |
| HW_IEPORT | HW_SUBMODULE | Identification of a port (PN/IO) |
| HW_HSC | HW_SUBMODULE | Identification of a high-speed counter  This data type is used, for example, for the "CTRL_HSC" and "CTRL_HSC_EXT" instructions. |
| HW_PWM | HW_SUBMODULE | Identification of a pulse width modulation  This data type is used, for example, for the "CTRL_PWM" instruction. |
| HW_PTO | HW_SUBMODULE | Identification of a pulse encoder  This data type is used for Motion Control. |
| EVENT_ANY | AOM_IDENT | Used to identify any event |
| EVENT_ATT | EVENT_ANY | Is used to specify an event that can be assigned dynamically to an OB  This data type is used, for example, for the "ATTACH" and "DETACH" instructions. |
| EVENT_HWINT | EVENT_ATT | Is used to specify a hardware interrupt event |
| OB_ANY | INT | Serves to specify any organization block. |
| OB_DELAY | OB_ANY | Used to specify an organization block that is called when a time-delay interrupt occurs.  This data type is used, for example, for the "SRT_DINT" and "CAN_DINT" instructions. |
| OB_TOD | OB_ANY | Specifies the number of a time-of-day interrupt OB.  This data type is used, for example, for the "SET_TINT", "CAN_TINT", "ACT_TINT" and "QRY_TINT" instructions. |
| OB_CYCLIC | OB_ANY | Is used to specify an organization block that is called when a watchdog interrupt occurs. |
| OB_ATT | OB_ANY | Is used to specify an organization block that can be assigned dynamically to an event.  This data type is used, for example, for the "ATTACH" and "DETACH" instructions. |
| OB_PCYCLE | OB_ANY | Is used to specify an organization block that can be assigned to an event of the "Cyclic program" event class. |
| OB_HWINT | OB_ATT | Is used to specify an organization block that is called when a hardware interrupt occurs. |
| OB_DIAG | OB_ANY | Is used to specify an organization block that is called when a diagnostic interrupt occurs. |
| OB_TIMEERROR | OB_ANY | Is used to specify an organization block that is called when a time error occurs. |
| OB_STARTUP | OB_ANY | Is used to specify an organization block that is called when a startup event occurs. |
| PORT | HW_SUBMODULE | Serves to specify a communication port.  This data type is used for point-to-point communication. |
| RTM | UINT | Serves to specify the number of an operating hours counter.  This data type is used, for example, for the "RTM" instruction. |
| PIP | UINT | Is used to create and connect a "Synchronous Cycle" OB. This data type is used for the SFCs 26, 27, 126 and 127. |
| CONN_ANY | WORD | Serves to specify any connection. |
| CONN_PRG | CONN_ANY | Serves to specify a connection for open communication over UDP. |
| CONN_OUC | CONN_ANY | Used to specify a connection for open communication over Industrial Ethernet (PROFINET). |
| CONN_R_ID | DWORD | Data type for the R_ID parameter on the S7 communication blocks. |
| DB_ANY | UINT | Identification (name or number) of a DB  The data type "DB_ANY" has the length 0 in the section "Temp". |
| DB_WWW | DB_ANY | Number of a DB generated via the Web application (for example, "WWW" instruction)  The data type "DB_WWW" has the length 0 in the section "Temp". |
| DB_DYN | DB_ANY | Number of a DB generated by the user program |
| C_ALARM | C_ALARM | CPU S7-400: 1 channel, with acknowledgment, up to 10 associated values  This data type is not supported for the ALARM alarm block. |
| C_ALARM_S | DWORD | CPU S7-300/400: 1 channel, with and without acknowledgment, up to 1 associated value  This data type is used for the ALARM_S, ALARM_SQ, ALARM_DQ and ALARM_D alarm blocks. |
| C_ALARM_8 | C_ALARM | CPU S7-400: 8 channels, with acknowledgment, no associated values  This data type is not supported for the ALARM_8 alarm block. |
| C_ALARM_8P | C_ALARM | CPU S7-400: 8 channels, with acknowledgment, up to 10 associated values per channel  This data type is not supported for the ALARM_8P alarm block. |
| C_AR_SEND | C_ALARM | CPU S7-400: Used to send an archive  This data type is not supported for the AR_SEND alarm block. |
| C_NOTIFY | C_ALARM | CPU S7-400: 1 channel, no acknowledgment, up to 10 associated values  This data type is not supported for the NOTIFY alarm block. |
| C_NOTIFY_8P | C_ALARM | CPU S7-400: 8 channels, no acknowledgment, up to 10 associated values  This data type is not supported for the NOTIFY_8P alarm block. |
| C_ALARM_SD | DWORD | Is used for recording the message number. This data type can only be used with the CPU S7-410H. |

---

**See also**

[Overview of the valid data types](#overview-of-the-valid-data-types)

## Data type conversion for S7-1200 (S7-1200)

This section contains information on the following topics:

- [Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
- [Implicit conversions (S7-1200)](#implicit-conversions-s7-1200)
- [Explicit conversions (S7-1200)](#explicit-conversions-s7-1200)

### Overview of data type conversion (S7-1200)

#### Introduction

If you link several operands in an instruction, you must make sure that the data types are compatible. This applies also for assignments or for supplying block parameters. If the operands are not the same data type, a conversion has to be carried out.

There are two options for the conversion:

- Implicit conversion

  The conversion take place automatically when the instruction is executed.
- Explicit conversion

  You use an explicit conversion instruction before the actual instruction is executed.

> **Note**
>
> The data type conversion options described always refer to the latest version of the CPU (V.4) Conversions marked as possible may not be available in CPU versions 1 - 3.

> **Note**
>
> **Converting bit strings in SCL**
>
> All bit strings (BYTE, WORD, and DWORD) are handled like the corresponding unsigned integers (USINT, UINT, and UDINT) in expressions. Therefore, implicit conversion from DWORD to REAL is carried out like a conversion from UDINT to REAL, for example.

#### Implicit conversion

An implicit conversion is executed automatically if the data types of the operands are compatible. This compatibility test can be carried out according to criteria that are more or less strict:

- With IEC check (default)

  If IEC check is set, the following rules are applied:

  - Implicit conversion of BOOL to other data types is not possible.
  - Only the REAL, BYTE, WORD, DINT, INT, SINT, UDINT, UINT, USINT, TIME, DT, STRING, CHAR and WCHAR data types can be converted implicitly.
  - The bit length of the source data type must not exceed the bit length of the target data type. An operand of data type WORD, for example, cannot be declared at a parameter at which data type BYTE is expected.
- Without IEC check

  If IEC check is not set, the following rules are applied:

  - Implicit conversion of BOOL to other data types is not possible.
  - Only the REAL, LREAL, BYTE, WORD, DWORD, SINT, INT, DINT, USINT, UINT, UDINT, TIME, DTL, TOD, DATE, STRING, CHAR and WCHAR data types can be converted implicitly.
  - The bit length of the source data type must not exceed the bit length of the target data type. An operand of data type DWORD, for example, cannot be declared at a parameter at which data type WORD is expected.
  - The bit length of an operand entered in-out parameters InOut) must be the same as the programmed bit length for the parameter in question.

> **Note**
>
> **Implicit conversion without IEC check**
>
> The programming editor uses a gray rectangle to mark operands that are implicitly converted. The dark gray rectangle signals that an implicit conversion is possible without any accuracy loss, for example, if you convert the data type SINT to INT. A light gray rectangle signals that implicit conversion is possible, but errors could occur during runtime. If, for example, you are converting the data type DINT to INT and an overflow occurs, the enable output ENO is set to "0".

For more information about the setting of the IEC check and the implicit conversion, refer to "See also".

#### Explicit conversion

If the operands are not compatible and an implicit conversion is therefore not possible, you can use an explicit conversion instruction. You can find the conversion instructions in the "Instructions" task card.

A possible overflow is displayed at the ENO enable output. An overflow is created, for example, if the value of the source data type is greater than the value of the target data type.

> **Note**
>
> **Shifting of bit patterns​**
>
> If the explicit conversion involves shifting a bit pattern, the enable output ENO is not set.

For more information about explicit conversion, refer to "See also".

The following figure shows an example in which an explicit data type conversion must be carried out:

![Explicit conversion](images/13105019147_DV_resource.Stream@PNG-en-US.png)

The "Block" function block expects a tag of the INT data type at the "IN_INT" input parameter. Therefore, the value of the "IN_DINT" tag must first be converted from DINT to INT. If the value of the "IN_DINT" tag is within the permitted value range of the INT data type, the conversion takes place. Otherwise, an overflow is signaled. A conversion still takes place even in case of an overflow, but the values are cut off and the enable output ENO is set to "0".

---

**See also**

[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Implicit conversions (S7-1200)](#implicit-conversions-s7-1200)
  
[Explicit conversions (S7-1200)](#explicit-conversions-s7-1200)

### Implicit conversions (S7-1200)

This section contains information on the following topics:

- [Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
- [Binary numbers (S7-1200)](#binary-numbers-s7-1200)
- [Integers (S7-1200)](#integers-s7-1200)
- [Floating-point numbers (S7-1200)](#floating-point-numbers-s7-1200)
- [Timers (S7-1200)](#timers-s7-1200)
- [Date and time (S7-1200)](#date-and-time-s7-1200)
- [Character strings (S7-1200)](#character-strings-s7-1200)

#### Activate or deactivate IEC check (S7-1200)

The data types of the operands used are check for compatibility. This compatibility test can be carried out according to criteria that are more or less strict. If "IEC check for code blocks" is activated, stricter criteria are applied.

You can set the IEC check centrally for all new blocks of the project or for individual blocks.

##### Setting IEC check for new blocks

To set the IEC check for all new blocks in the project, proceed as follows:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming &gt; General" group in the area navigation.
3. Select or clear the "IEC check for code blocks" check box in the "Default settings for new blocks" group.

   The IEC check is enabled or disabled for all new blocks in the program.

##### Setting IEC check for a block

To set the IEC check for a block, proceed as follows:

1. Open the block.
2. Open the "Properties" tab in the Inspector window.
3. Select the "Attributes" group in the area navigation.
4. Select or clear the "IEC check" check box.

   The IEC check is enabled or disabled for this block. The setting is stored together with the project.

#### Binary numbers (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of BOOL (S7-1200)](#implicit-conversion-of-bool-s7-1200)
- [Bit strings (S7-1200)](#bit-strings-s7-1200)

##### Implicit conversion of BOOL (S7-1200)

###### Options for implicit conversion

The implicit conversion of the BOOL data type is not possible.

---

**See also**

[BOOL (bit)](#bool-bit)

##### Bit strings (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of BYTE (S7-1200)](#implicit-conversion-of-byte-s7-1200)
- [Implicit conversion of WORD (S7-1200)](#implicit-conversion-of-word-s7-1200)
- [Implicit conversion of DWORD (S7-1200)](#implicit-conversion-of-dword-s7-1200)

###### Implicit conversion of BYTE (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the BYTE data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| BYTE | BOOL | - | - | No implicit conversion |
| WORD | x | x | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DWORD | x | x |  |  |
| SINT | - | x |  |  |
| USINT | - | x |  |  |
| INT | - | x |  |  |
| UINT | - | x |  |  |
| DINT | - | x |  |  |
| UDINT | - | x |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | x | The bit pattern of the source value is transferred unchanged to the target data type. |  |
| WCHAR | - | x |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[BYTE](#byte)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of BYTE (S7-1200)](#explicit-conversion-of-byte-s7-1200)

###### Implicit conversion of WORD (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the WORD data type:

| Source | Target | With  IEC check | Without  IEC check | Description |
| --- | --- | --- | --- | --- |
| WORD | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The least significant byte is transferred to the target data type, while the most significant byte is ignored. |  |
| DWORD | X | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| SINT | - | X | The least significant byte is transferred to the target data type, while the most significant byte is ignored. |  |
| USINT | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | X | The bit pattern of the source value is transferred unchanged to the target data type. |  |
| STRING | - | - | No implicit conversion |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[WORD](#word)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of WORD (S7-1200)](#explicit-conversion-of-word-s7-1200)

###### Implicit conversion of DWORD (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the DWORD data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DWORD | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The right bytes are transferred to the target data type; the left bytes are ignored. |  |
| WORD | - | X |  |  |
| SINT | - | X |  |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| UDINT | - | X |  |  |
| REAL | - | X | The value is converted to the format of the target data type. (The value "-1", for example, is converted to the value "-1.0".) |  |
| LREAL | - | - | No implicit conversion |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DTL | - | - | No implicit conversion |  |
| TOD | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DATE | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DWORD](#dword)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of DWORD (S7-1200)](#explicit-conversion-of-dword-s7-1200)

#### Integers (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of SINT (S7-1200)](#implicit-conversion-of-sint-s7-1200)
- [Implicit conversion of USINT (S7-1200)](#implicit-conversion-of-usint-s7-1200)
- [Implicit conversion of INT (S7-1200)](#implicit-conversion-of-int-s7-1200)
- [Implicit conversion of UINT (S7-1200)](#implicit-conversion-of-uint-s7-1200)
- [Implicit conversion of DINT (S7-1200)](#implicit-conversion-of-dint-s7-1200)
- [Implicit conversion of UDINT (S7-1200)](#implicit-conversion-of-udint-s7-1200)

##### Implicit conversion of SINT (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the SINT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| SINT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The remaining bits are filled with "0". |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| USINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value transfer from SINT #-1 -&gt; INT #-1, not filled with "0".) |  |
| INT | X | X |  |  |
| UINT | - | X |  |  |
| DINT | X | X |  |  |
| UDINT | - | X |  |  |
| REAL | X | X | The value is converted to the format of the target data type. (The value "-1", for example, is converted to the value "-1.0".) |  |
| LREAL | X | X |  |  |
| TIME | - | - | No implicit conversion |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[SINT (8-bit integers) (S7-1200, S7-1500)](#sint-8-bit-integers-s7-1200-s7-1500)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of SINT (S7-1200)](#explicit-conversion-of-sint-s7-1200)

##### Implicit conversion of USINT (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the USINT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| USINT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The remaining bits are filled with "0". |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from USINT #10 -&gt; DINT #10 or USINT #128 -&gt; SINT #-128) |  |
| INT | X | X |  |  |
| UINT | X | X |  |  |
| DINT | X | X |  |  |
| UDINT | X | X |  |  |
| REAL | X | X | The value is converted to the format of the target data type. (The value "1", for example, is converted to the value "1.0".) |  |
| LREAL | X | X |  |  |
| TIME | - | - | No implicit conversion |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[USINT (8-bit integers) (S7-1200, S7-1500)](#usint-8-bit-integers-s7-1200-s7-1500)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of USINT (S7-1200)](#explicit-conversion-of-usint-s7-1200)

##### Implicit conversion of INT (S7-1200)

###### Options for implicit conversion

The following table shows the options for the implicit conversion of the INT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| INT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from INT #-1 -&gt; SINT #-1, or INT #-32 767 -&gt; UINT #32 769) |  |
| USINT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | X | X |  |  |
| UDINT | - | X |  |  |
| REAL | X | X | The value is converted to the format of the target data type. (The value "-1", for example, is converted to the value "-1.0".) |  |
| LREAL | X | X |  |  |
| TIME | - | - | No implicit conversion |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| STRING | - | - | No implicit conversion |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[INT (16-bit integers)](#int-16-bit-integers)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of INT (S7-1200)](#explicit-conversion-of-int-s7-1200)

##### Implicit conversion of UINT (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the UINT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| UINT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from UINT #100 -&gt; DINT #100 or UINT #60 000 -&gt; INT #-5536) |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| DINT | X | X |  |  |
| UDINT | X | X |  |  |
| REAL | X | X | The value is converted to the format of the target data type. (The value "1", for example, is converted to the value "1.0".) |  |
| LREAL | X | X |  |  |
| TIME | - | - | No implicit conversion |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| STRING | - | - | No implicit conversion |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[UINT (16-bit integers) (S7-1200, S7-1500)](#uint-16-bit-integers-s7-1200-s7-1500)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of UINT (S7-1200)](#explicit-conversion-of-uint-s7-1200)

##### Implicit conversion of DINT (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the DINT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DINT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from DINT #-1 -&gt; SINT #-1 or DINT #-1 -&gt; USINT #255) |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| UDINT | - | X |  |  |
| REAL | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from DINT #-1 -&gt; REAL #-1.0, but there is a loss in accuracy for numbers with an absolute value greater than 8 388 608) |  |
| LREAL | X | X | The value is converted to the format of the target data type. (The value "-1", for example, is converted to the value "-1.0".) |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DTL | - | - | No implicit conversion |  |
| TOD | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DATE | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DINT (32-bit integers)](#dint-32-bit-integers)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of DINT (S7-1200)](#explicit-conversion-of-dint-s7-1200)

##### Implicit conversion of UDINT (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the UDINT data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| UDINT | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from DINT #-1 -&gt; SINT #-1 or DINT #-1 -&gt; USINT #255) |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| REAL | - | X | The bit pattern of the source value is converted and transferred to the target data type. (for example, value conversion from DINT #-1 -&gt; REAL #-1.0, but there is a loss in accuracy for numbers with an absolute value greater than 8 388 608) |  |
| LREAL | X | X | The value is converted to the format of the target data type. (The value "1", for example, is converted to the value "1.0".) |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DTL | - | - | No implicit conversion |  |
| TOD | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| DATE | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| WCHAR | - | X |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[UDINT (32-bit integers) (S7-1200, S7-1500)](#udint-32-bit-integers-s7-1200-s7-1500)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of UDINT (S7-1200)](#explicit-conversion-of-udint-s7-1200)

#### Floating-point numbers (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of REAL (S7-1200)](#implicit-conversion-of-real-s7-1200)
- [Implicit conversion of LREAL (S7-1200)](#implicit-conversion-of-lreal-s7-1200)

##### Implicit conversion of REAL (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the REAL data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| REAL | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |
| SINT | - | X | The bit pattern of the source value is rounded off and converted and transferred to the target data type. (for example, rounding off and value conversion of REAL #2.5 -&gt; INT #2 or negative number REAL #-2.5 -&gt; INT #-2 -&gt; USINT #254. With an overflow, the remainder is determined REAL #305.5 -&gt; INT #306 -&gt; USINT #50) |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| UDINT | - | X |  |  |
| LREAL | X | X | The value is transferred to the target data type. |  |
| TIME | - | - | No implicit conversion |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[REAL](#real)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of REAL (S7-1200)](#explicit-conversion-of-real-s7-1200)

##### Implicit conversion of LREAL (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the LREAL data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| LREAL | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | - | X | The bit pattern of the source value is rounded off and converted and transferred to the target data type. (for example, rounding off and value conversion of REAL #2.5 -&gt; INT #2 or negative number REAL #-2.5 -&gt; INT #-2 -&gt; USINT #254. With an overflow, the remainder is determined REAL #305.5 -&gt; INT #306 -&gt; USINT #50) |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[Explicit conversion of LREAL (S7-1200)](#explicit-conversion-of-lreal-s7-1200)

#### Timers (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of TIME (S7-1200)](#implicit-conversion-of-time-s7-1200)

##### Implicit conversion of TIME (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the TIME data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| TIME | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion shows the duration in milliseconds. |  |
| SINT | - | - | No implicit conversion |  |
| USINT | - | - |  |  |
| INT | - | - |  |  |
| UINT | - | - |  |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion shows the duration in milliseconds. |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | X | The bit pattern of a source value that is less than 24 h (86 400 00 ms) is transferred without changes to the target data type. No further changes are made to the target value. The result of the conversion shows the time that has passed since midnight. |  |
| DATE | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[TIME (IEC time)](#time-iec-time)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of TIME (S7-1200)](#explicit-conversion-of-time-s7-1200)

#### Date and time (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of DATE (S7-1200)](#implicit-conversion-of-date-s7-1200)
- [Implicit conversion of TOD (S7-1200)](#implicit-conversion-of-tod-s7-1200)
- [Implicit conversion of DTL (S7-1200)](#implicit-conversion-of-dtl-s7-1200)

##### Implicit conversion of DATE (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the DATE data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DATE | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of days since 01-01-1990. |  |
| DWORD | - | - | No implicit conversion |  |
| SINT | - | - |  |  |
| USINT | - | - |  |  |
| INT | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of days since 01-01-1990. |  |
| UINT | - | X |  |  |
| DINT | - | - | No implicit conversion |  |
| UDINT | - | - |  |  |
| REAL | - | - |  |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of days since 01-01-1990. |  |
| TOD | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DATE](#date)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of DATE (S7-1200)](#explicit-conversion-of-date-s7-1200)

##### Implicit conversion of TOD (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the TOD data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| TOD | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of milliseconds since the start of day (0:00 hrs). |  |
| SINT | - | - | No implicit conversion |  |
| USINT | - | - |  |  |
| INT | - | - |  |  |
| UINT | - | - |  |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of milliseconds since the start of day (0:00 hrs). |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion corresponds to the number of milliseconds since the start of day (0:00 hrs). |  |
| DTL | - | - | No implicit conversion |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[TIME_OF_DAY (TOD)](#time_of_day-tod)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of TOD (S7-1200)](#explicit-conversion-of-tod-s7-1200)

##### Implicit conversion of DTL (S7-1200)

###### Options for implicit conversion

The DTL data type cannot be implicitly converted.

---

**See also**

[Explicit conversion of DTL (S7-1200)](#explicit-conversion-of-dtl-s7-1200)

#### Character strings (S7-1200)

This section contains information on the following topics:

- [Implicit conversion of CHAR (S7-1200)](#implicit-conversion-of-char-s7-1200)
- [Implicit conversion of WCHAR (S7-1200)](#implicit-conversion-of-wchar-s7-1200)
- [Implicit conversion of STRING (S7-1200)](#implicit-conversion-of-string-s7-1200)
- [Implicit conversion of WSTRING (S7-1200)](#implicit-conversion-of-wstring-s7-1200)

##### Implicit conversion of CHAR (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the CHAR data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| CHAR | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The remaining bits are filled from the left with "0". |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X |  |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| WCHAR | - | - |  |  |
| STRING | X | X | The STRING is shortened to length 1 and includes the character. |  |
| WSTRING | - | - | No implicit conversion |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[CHAR](#char)
  
[Activate or deactivate IEC check (S7-1200)](#activate-or-deactivate-iec-check-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)
  
[Explicit conversion of CHAR (S7-1200)](#explicit-conversion-of-char-s7-1200)

##### Implicit conversion of WCHAR (S7-1200)

###### Options for implicit conversion

The following table shows the options for the implicit conversion of the WCHAR data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| WCHAR | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The remaining bits are filled from the left with "0". |  |
| WORD | - | X |  |  |
| DWORD | - | X |  |  |
| SINT | - | X |  |  |
| USINT | - | X |  |  |
| INT | - | X |  |  |
| UINT | - | X |  |  |
| DINT | - | X |  |  |
| UDINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| CHAR | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | X | X | The WSTRING is shortened to length 1 and includes the character. |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

##### Implicit conversion of STRING (S7-1200)

###### Options for implicit conversion

The following table shows the options for implicit conversion of the STRING data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| STRING | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | - | - |  |  |
| USINT | - | - |  |  |
| INT | - | - |  |  |
| UINT | - | - |  |  |
| DINT | - | - |  |  |
| UDINT | - | - |  |  |
| REAL | - | - |  |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| DATE | - | - |  |  |
| TOD | - | - |  |  |
| CHAR | - | X | The first character of the STRING is returned if the STRING includes one or more characters. Otherwise, the character is output with coding $00. |  |
| WCHAR | - | - | No implicit conversion |  |
| WSTRING | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[Explicit conversion of STRING (S7-1200)](#explicit-conversion-of-string-s7-1200)

##### Implicit conversion of WSTRING (S7-1200)

###### Options for implicit conversion

The following table shows the options for the implicit conversion of the WSTRING data type:

| Source | Target | With  IEC check | Without  IEC check | Explanation |
| --- | --- | --- | --- | --- |
| WSTRING | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | - | - |  |  |
| USINT | - | - |  |  |
| INT | - | - |  |  |
| UINT | - | - |  |  |
| DINT | - | - |  |  |
| UDINT | - | - |  |  |
| REAL | - | - |  |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| DATE | - | - |  |  |
| TOD | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | X | The first character of the WSTRING is returned if the WSTRING includes one or more characters. Otherwise, the character is output with coding $0000. |  |
| STRING | - | - | No implicit conversion |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

### Explicit conversions (S7-1200)

This section contains information on the following topics:

- [Binary numbers (S7-1200)](#binary-numbers-s7-1200-1)
- [Integers (S7-1200)](#integers-s7-1200-1)
- [Floating-point numbers (S7-1200)](#floating-point-numbers-s7-1200-1)
- [Timers (S7-1200)](#timers-s7-1200-1)
- [Clock and calendar (S7-1200)](#clock-and-calendar-s7-1200)
- [Character strings (S7-1200)](#character-strings-s7-1200-1)

#### Binary numbers (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of BOOL (S7-1200)](#explicit-conversion-of-bool-s7-1200)
- [Bit strings (S7-1200)](#bit-strings-s7-1200-1)

##### Explicit conversion of BOOL (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the BOOL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| BOOL | BYTE | X | Only the LSB (Least Significant Bit) is set in the target data type. The enable output ENO is always "1". | BOOL_TO_BYTE |
| WORD | X | BOOL_TO_WORD |  |  |
| DWORD | X | BOOL_TO_DWORD |  |  |
| SINT | X | BOOL_TO_SINT |  |  |
| USINT | X | BOOL_TO_USINT |  |  |
| INT | X | BOOL_TO_INT |  |  |
| UINT | X | BOOL_TO_UINT |  |  |
| DINT | X | BOOL_TO_DINT |  |  |
| UDINT | X | BOOL_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[BOOL (bit)](#bool-bit)
  
[Implicit conversion of BYTE (S7-1200)](#implicit-conversion-of-byte-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Bit strings (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of BYTE (S7-1200)](#explicit-conversion-of-byte-s7-1200)
- [Explicit conversion of WORD (S7-1200)](#explicit-conversion-of-word-s7-1200)
- [Explicit conversion of DWORD (S7-1200)](#explicit-conversion-of-dword-s7-1200)

###### Explicit conversion of BYTE (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the BYTE data type:

| Source | Target | Conversion | Explanation | Mnemonics of   Instruction |
| --- | --- | --- | --- | --- |
| BYTE<sup>1)</sup> | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bits are not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | BYTE_TO_BOOL |
| WORD<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | BYTE_TO_WORD |  |
| DWORD<sup>1)</sup> | X | BYTE_TO_DWORD |  |  |
| SINT | X | BYTE_TO_SINT |  |  |
| USINT | X | BYTE_TO_USINT |  |  |
| INT | X | BYTE_TO_INT |  |  |
| UINT | X | BYTE_TO_UINT |  |  |
| DINT | X | BYTE_TO_DINT |  |  |
| UDINT | X | BYTE_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | BYTE_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | BYTE_TO_TOD |  |
| DATE | X | BYTE_TO_DATE |  |  |
| STRING | - | No explicit conversion | - |  |
| WSTRING | - | - |  |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | BYTE_TO_CHAR |  |
| WCHAR | X | BYTE_TO_WCHAR |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) are interpreted as an unsigned integer with the same bit length.. Data type BYTE is interpreted as USINT, WORD as UINT and DWORD as UDINT. |  |  |  |  |

---

**See also**

[BYTE](#byte)
  
[Implicit conversion of BYTE (S7-1200)](#implicit-conversion-of-byte-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

###### Explicit conversion of WORD (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the WORD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| WORD<sup>1)</sup> | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | WORD_TO_BOOL |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_BYTE |  |
| DWORD<sup>1)</sup> | X | WORD_TO_DWORD |  |  |
| SINT | X | ENO = TRUE  #sint1 := WORD_TO_SINT(16#FFFF); // -1 to #sint1 := WORD_TO_SINT(16#FF80); // -128 #sint1 := WORD_TO_SINT(16#0); // 0 to #sint1 := WORD_TO_SINT(16#007F); // 127    ENO = FALSE  #sint1 := WORD_TO_SINT(16#FF7F); // -129 to #sint1 := WORD_TO_SINT(16#8000); // -32768 #sint1 := WORD_TO_SINT(16#0080); // 128 to #sint1 := WORD_TO_SINT(16#7FFF); // 32767 | WORD_TO_SINT |  |
| USINT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_USINT |  |
| INT | X | WORD_TO_INT |  |  |
| UINT | X | WORD_TO_UINT |  |  |
| DINT | X | WORD_TO_DINT |  |  |
| UDINT | X | WORD_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_TOD |  |
| DATE | X | WORD_TO_DATE |  |  |
| STRING | - | No explicit conversion | - |  |
| WSTRING | - | - |  |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_CHAR |  |
| WCHAR | X | WORD_TO_WCHAR |  |  |
| WORD_BCD16 | INT | X | The value to be converted has data type WORD and is accepted as a BCD-coded value between -999 and +999. The result is available after conversion as an integer (in binary notation) of the type INT. A real conversion takes place. If the bit pattern includes an invalid tetrad, a synchronous error is not triggered but only the status bit OV is set instead. | WORD_BCD16_TO_INT |
| BCD16 | INT | X | BCD16_TO_INT |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) are interpreted as an unsigned integer with the same bit length.. Data type BYTE is interpreted as USINT, WORD as UINT and DWORD as UDINT. |  |  |  |  |

---

**See also**

[WORD](#word)
  
[Implicit conversion of WORD (S7-1200)](#implicit-conversion-of-word-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

###### Explicit conversion of DWORD (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the DWORD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DWORD<sup>1)</sup> | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and the enable output ENO is "1". - If bit is not equal to LSB in the source value, the destination data type is set according to LSB and the enable output ENO is "0". | DWORD_TO_BOOL |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_BYTE |  |
| WORD<sup>1)</sup> | X | DWORD_TO_WORD |  |  |
| SINT | X | ENO = TRUE  #sint1 := DWORD_TO_SINT(16#FFFF_FFFF); // -1 to #sint1 := DWORD_TO_SINT(16#FFFF_FF80); // -128 #sint1 := DWORD_TO_SINT(16#0); // 0 to #sint1 := DWORD_TO_SINT(16#0000_007F); // 127    ENO = FALSE  #sint1 := DWORD_TO_SINT(16#FFFF_FF7F); // -129 #sint1 := DWORD_TO_SINT(16#8000_0000); // -2147483648 #sint1 := DWORD_TO_SINT(16#0000_0080); // 128 to #sint1 := DWORD_TO_SINT(16#7FFF_FFFF); // 2147483647 | DWORD_TO_SINT |  |
| USINT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_USINT |  |
| INT | X | ENO = TRUE  #int1 := DWORD_TO_INT(16#FFFF_FFFF); // -1 to #int1 := DWORD_TO_INT(16#FFFF_8000); // -32768 #int1 := DWORD_TO_INT(16#0); // 0 to #int1 := DWORD_TO_INT(16#0000_7FFF); // 32767    ENO = FALSE  #int1 := DWORD_TO_INT(16#FFFF_7FFF); // -32769 #int1 := DWORD_TO_INT(16#8000_0000); // -2147483648 #int1 := DWORD_TO_INT(16#8000); // 32768 to #int1 := DWORD_TO_INT(16#7FFF_FFFF); // 2147483647 | DWORD_TO_INT |  |
| UINT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_UINT |  |
| DINT | X | DWORD_TO_DINT |  |  |
| UDINT | X | DWORD_TO_UDINT |  |  |
| REAL | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If no errors occur during the conversion, the signal state of ENO = 1; if an error occurs during processing, the signal state of ENO = 0. | DWORD_TO_REAL |  |
| LREAL | - | No explicit conversion | - |  |
| TIME | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_TOD |  |
| DATE | X | DWORD_TO_DATE |  |  |
| STRING | - | No explicit conversion | - |  |
| WSTRING | - | - |  |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DWORD_TO_CHAR |  |
| WCHAR | X | DWORD_TO_WCHAR |  |  |
| DWORD_BCD32 | DINT | X | The value to be converted has data type DWORD and is accepted as a BCD-coded value between -9999999 and +9999999. The result is available after conversion as an integer (in binary notation) of the type DINT. A real conversion takes place. If the bit pattern includes an invalid tetrad, a synchronous error is not triggered but only the status bit OV is set instead. | DWORD_BCD32_TO_DINT |
| BCD32 | DINT | X | BCD32_TO_DINT |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) are interpreted as an unsigned integer with the same bit length.. Data type BYTE is interpreted as USINT, WORD as UINT and DWORD as UDINT. |  |  |  |  |

---

**See also**

[DWORD](#dword)
  
[Implicit conversion of DWORD (S7-1200)](#implicit-conversion-of-dword-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

#### Integers (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of SINT (S7-1200)](#explicit-conversion-of-sint-s7-1200)
- [Explicit conversion of USINT (S7-1200)](#explicit-conversion-of-usint-s7-1200)
- [Explicit conversion of INT (S7-1200)](#explicit-conversion-of-int-s7-1200)
- [Explicit conversion of UINT (S7-1200)](#explicit-conversion-of-uint-s7-1200)
- [Explicit conversion of DINT (S7-1200)](#explicit-conversion-of-dint-s7-1200)
- [Explicit conversion of UDINT (S7-1200)](#explicit-conversion-of-udint-s7-1200)

##### Explicit conversion of SINT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the SINT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| SINT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | SINT_TO_BOOL |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | SINT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | SINT_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | SINT_TO_DWORD |  |  |
| USINT | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. | SINT_TO_USINT |  |
| INT | X | SINT_TO_INT |  |  |
| UINT | X | SINT_TO_UINT |  |  |
| DINT | X | SINT_TO_DINT |  |  |
| UDINT | X | SINT_TO_UDINT |  |  |
| REAL | X | The value is converted into the format of the target data type (the value "-1" will be converted into the value "-1.0" with the "Convert value" (CONVERT) instruction. | SINT_TO_REAL, NORM_X |  |
| LREAL | X | SINT_TO_LREAL, NORM_X |  |  |
| TIME | X | The value is transferred to the target data type and interpreted as milliseconds. | SINT_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in milliseconds since 0:0) | SINT_TO_TOD |  |
| DATE | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in days since 1990-1-1) | SINT_TO_DATE |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | SINT_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | SINT_TO_WSTRING |  |  |
| CHAR<sup>1)</sup> | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. | SINT_TO_CHAR |  |
| WCHAR<sup>1)</sup> | X | SINT_TO_WCHAR |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width including sign, and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[SINT (8-bit integers) (S7-1200, S7-1500)](#sint-8-bit-integers-s7-1200-s7-1500)
  
[Implicit conversion of SINT (S7-1200)](#implicit-conversion-of-sint-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of USINT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the USINT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| USINT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | USINT_TO_BOOL |
| BYTE <sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | USINT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | USINT_TO_WORD |  |  |
| DWORD <sup>1)</sup> | X | USINT_TO_DWORD |  |  |
| SINT | X | The bit pattern of the source value is transferred unchanged to the target data type. If the sign is changed during the conversion, the enable output ENO is set to "0". | USINT_TO_SINT |  |
| INT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | USINT_TO_INT |  |
| UINT | X | USINT_TO_UINT |  |  |
| DINT | X | USINT_TO_DINT |  |  |
| UDINT | X | USINT_TO_UDINT |  |  |
| REAL | X | The value is converted into the format of the target data type (the value "1" will be converted into the value "1.0" with the "Convert value" (CONVERT) instruction. | USINT_TO_REAL, NORM_X |  |
| LREAL | X | USINT_TO_LREAL, NORM_X |  |  |
| TIME | X | The value is transferred to the target data type and interpreted as milliseconds. | USINT_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | USINT_TO_TOD |  |
| DATE | X | USINT_TO_DATE |  |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | USINT_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | USINT_TO_WSTRING |  |  |
| CHAR <sup>1)</sup> | X | The bit pattern of the source value is converted and transferred to the target data type. | USINT_TO_CHAR |  |
| WCHAR <sup>1)</sup> | X | USINT_TO_WCHAR |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width (the non-existing sign is replaced with zeros) and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[USINT (8-bit integers) (S7-1200, S7-1500)](#usint-8-bit-integers-s7-1200-s7-1500)
  
[Implicit conversion of USINT (S7-1200)](#implicit-conversion-of-usint-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of INT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the INT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| INT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | INT_TO_BOOL |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | INT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | INT_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | INT_TO_DWORD |  |  |
| SINT | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | INT_TO_SINT |  |
| USINT | X | INT_TO_USINT |  |  |
| UINT | X | INT_TO_UINT |  |  |
| DINT | X | INT_TO_DINT |  |  |
| UDINT | X | INT_TO_UDINT |  |  |
| REAL | X | The value is converted to the format of the target data type (the value "-1", for example, is converted with the instruction "Convert value" (CONVERT) to the value "-1.0"). | INT_TO_REAL, NORM_X |  |
| LREAL | X | INT_TO_LREAL, NORM_X |  |  |
| TIME | X | The value is transferred to the target data type and interpreted as milliseconds. | INT_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". (interpretation in milliseconds since 0:0; check for 24h limit) | INT_TO_TOD |  |
| DATE | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". (interpretation in days since 1990-1-1; check for negative value) | INT_TO_DATE |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | INT_TO_STRING, S_CONV, VAL_STRG<sup>)</sup> |  |
| WSTRING | X | INT_TO_WSTRING |  |  |
| CHAR<sup>1)</sup> | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | INT_TO_CHAR |  |
| WCHAR<sup>1)</sup> | X | INT_TO_WCHAR |  |  |
| BCD16 | X | The value to be converted has type INT and is accepted as an integer with a value between -999 and +999. The result is available after conversion as a BCD-coded number of the type WORD. A real conversion takes place. If the value is outside the target area, a synchronous error is not triggered, but rather only the status bit OV is set. | INT_TO_BCD16 |  |
| BCD16_WORD | X | INT_TO_BCD16_WORD |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width including sign, and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[INT (16-bit integers)](#int-16-bit-integers)
  
[Implicit conversion of INT (S7-1200)](#implicit-conversion-of-int-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of UINT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the UINT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| UINT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | UINT_TO_BOOL |
| BYTE <sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If bits are lost in the process, the enable output ENO is set to "0". | UINT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | UINT_TO_WORD |  |  |
| DWORD <sup>1)</sup> | X | UINT_TO_DWORD |  |  |
| SINT | X | UINT_TO_SINT |  |  |
| USINT | X | UINT_TO_USINT |  |  |
| INT | X | The bit pattern of the source value is transferred unchanged to the target data type. If the sign bit is changed during the conversion, the enable output ENO is set to "0". | UINT_TO_INT |  |
| DINT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | UINT_TO_DINT |  |
| UDINT | X | UINT_TO_UDINT |  |  |
| REAL | X | The value is converted to the format of the target data type (the value "1", for example, is converted with the instruction "Convert value" (CONVERT) to the value "1.0"). | UINT_TO_REAL, NORM_X |  |
| LREAL | X | UINT_TO_LREAL, NORM_X |  |  |
| TIME | X | The value is transferred to the target data type and interpreted as milliseconds. | UINT_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in milliseconds since 0:0; check for 24h limit) | UINT_TO_TOD |  |
| DATE | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in days since 1990-1-1; check for negative value) | UINT_TO_DATE, T_CONV |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | UINT_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | UINT_TO_WSTRING |  |  |
| CHAR <sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged to the target data type. The enable output ENO is set to "0" in the event of overflow. | UINT_TO_CHAR |  |
| WCHAR <sup>1)</sup> | X | UINT_TO_WCHAR |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD, LWORD) and the data type CHAR are first extended to the necessary width (the non-existing sign is replaced with zeros) and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[UINT (16-bit integers) (S7-1200, S7-1500)](#uint-16-bit-integers-s7-1200-s7-1500)
  
[Implicit conversion of UINT (S7-1200)](#implicit-conversion-of-uint-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of DINT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the DINT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DINT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | DINT_TO_BOOL |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | DINT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | DINT_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | DINT_TO_DWORD |  |  |
| SINT | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | DINT_TO_SINT |  |
| USINT | X | DINT_TO_USINT |  |  |
| INT | X | DINT_TO_INT |  |  |
| UINT | X | DINT_TO_UINT |  |  |
| UDINT | X | DINT_TO_UDINT |  |  |
| REAL | X | The value is converted to the format of the target data type (the value "-1", for example, is converted with the instruction "Convert value" (CONVERT) to the value "-1.0"). | DINT_TO_REAL, NORM_X |  |
| LREAL | X | DINT_TO_LREAL, NORM_X |  |  |
| TIME | X | The value is transferred to the target data type and interpreted as milliseconds. | DINT_TO_TIME, T_CONV |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". (interpretation in milliseconds since 0:0) | DINT_TO_TOD |  |
| DATE | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". (interpretation in days since 1990-1-1) | DINT_TO_DATE |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | DINT_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | DINT_TO_WSTRING |  |  |
| CHAR<sup>1)</sup> | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF)). If a negative value is converted to an unsigned target data type, the enable output ENO is set to "0". | DINT_TO_CHAR |  |
| WCHAR<sup>1)</sup> | X | DINT_TO_WCHAR |  |  |
| BCD32 | X | The value to be converted has type DINT and is accepted as an integer with a value between –999999 and +9999999. The result is available after conversion as a BCD-coded number of the type DWORD. The enable output is set to "0" in the event of overflow. A real conversion takes place. If the value is outside the target area, a synchronous error is not triggered, but rather only the status bit OV is set. | DINT_TO_BCD32 |  |
| BCD32_DWORD | X | DINT_TO_BCD32_DWORD |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width including sign, and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[DINT (32-bit integers)](#dint-32-bit-integers)
  
[Implicit conversion of DINT (S7-1200)](#implicit-conversion-of-dint-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of UDINT (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the UDINT data type:

| Source | Destination | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| UDINT | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and enable output ENO is "1". - If bit is not equal to LSB in the source value, the target data type is set according to LSB and enable output ENO is "0". | UDINT_TO_BOOL |
| BYTE <sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged to the target data type. If bits are lost in the process, the enable output ENO is set to "0". | UDINT_TO_BYTE |  |
| WORD<sup>1)</sup> | X | UDINT_TO_WORD |  |  |
| DWORD <sup>1)</sup> | X | UDINT_TO_DWORD |  |  |
| SINT | X | UDINT_TO_SINT |  |  |
| USINT | X | UDINT_TO_USINT |  |  |
| INT | X | UDINT_TO_INT |  |  |
| UINT | X | UDINT_TO_UINT |  |  |
| DINT | X | The bit pattern of the source value is transferred unchanged to the target data type. If the sign bit is changed during the conversion, the enable output ENO is set to "0". | UDINT_TO_DINT |  |
| REAL | X | The value is converted to the format of the target data type (the value "1", for example, is converted with the instruction "Convert value" (CONVERT) to the value "1.0"). | UDINT_TO_REAL, NORM_X |  |
| LREAL | X | UDINT_TO_LREAL, NORM_X |  |  |
| TIME | X | The bit pattern of the source value is transferred unchanged right-justified and interpreted as milliseconds to the target data type. | UDINT_TO_TIME |  |
| DTL | - | No explicit conversion | - |  |
| TOD | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in milliseconds since 0:0; check for 24h limit) | UDINT_TO_TOD, T_CONV |  |
| DATE | X | The bit pattern of the source value is converted and transferred to the target data type. (The value "-1" (16#FF) becomes the value "-1" (16#FFFFFFFF). Enable output ENO is set to "0" if a negative value is converted to an unsigned target data type. (interpretation in days since 1990-1-1; check for negative value) | UDINT_TO_DATE |  |
| STRING | X | The value is converted into a character string.  The first characters of the string are padded with spaces. The number of spaces depends on the length of the numerical value.  Positive numeric values are output without a sign.   If the permitted length of the character string is violated, the enable output ENO is set to "0".  The following special features apply to SCL:  - No spaces are inserted. - The character string is shown preceded by a sign. | UDINT_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | UDINT_TO_WCHAR |  |  |
| CHAR <sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged to the target data type. The enable output ENO is set to "0" in the event of overflow. | UDINT_TO_CHAR |  |
| WCHAR <sup>1)</sup> | X | UDINT_TO_WCHAR |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD, LWORD) and the data type CHAR are first extended to the necessary width (the non-existent sign is replaced with zeros) and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[UDINT (32-bit integers) (S7-1200, S7-1500)](#udint-32-bit-integers-s7-1200-s7-1500)
  
[Implicit conversion of UDINT (S7-1200)](#implicit-conversion-of-udint-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

#### Floating-point numbers (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of REAL (S7-1200)](#explicit-conversion-of-real-s7-1200)
- [Explicit conversion of LREAL (S7-1200)](#explicit-conversion-of-lreal-s7-1200)

##### Explicit conversion of REAL (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the REAL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| REAL | BOOL | - | No explicit conversion | - |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | X | The bit pattern of the source value is transferred unchanged to the target data type. | REAL_TO_DWORD |  |
| SINT | X | The value is converted to the target data type. The result of the conversion depends on the instruction used. Enable output ENO is set to "0" if the valid range of values of the target data type is exceeded during conversion, or if the value to be converted is an invalid floating-point number. | REAL_TO_SINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |
| USINT | X | REAL_TO_USINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| INT | X | REAL_TO_INT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| UINT | X | REAL_TO_UINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| DINT | X | REAL_TO_DINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| UDINT | X | REAL_TO_UDINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| LREAL | X | The value is converted to the target data type. The result of the conversion depends on the instruction used, e.g. TRUNC(2.5) = 2.0; CEIL(2.5) = 3.0 | REAL_TO_LREAL, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |
| TIME | - | No explicit conversion | - |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | X | The value is converted to a character string. Enable output ENO is set to "0" if the character string length is exceeded, or if the value to be converted is an invalid floating-point number. The string has a minimum length of 14 characters. | REAL_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | REAL_TO_WSTRING |  |  |
| CHAR | - | No explicit conversion | - |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[REAL](#real)
  
[Implicit conversion of REAL (S7-1200)](#implicit-conversion-of-real-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of LREAL (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the LREAL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| LREAL | BOOL | - | No explicit conversion | - |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | X | The value is converted to the target data type. The result of the conversion depends on the instruction used. Enable output ENO is set to "0" if the valid range of values of the target data type is exceeded during conversion, or if the value to be converted is an invalid floating-point number. | LREAL_TO_SINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |
| USINT | X | LREAL_TO_USINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| INT | X | LREAL_TO_INT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| UINT | X | LREAL_TO_UINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| DINT | X | LREAL_TO_DINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| UDINT | X | LREAL_TO_UDINT, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |  |
| REAL | X | The value is converted to the target data type. Enable output ENO is set to "0" if the valid range of values of the target data type is exceeded during conversion, or if the value to be converted is an invalid floating-point number. A loss in accuracy is tolerated. | LREAL_TO_LREAL, ROUND, CEIL, FLOOR, TRUNC, NORM_X, SCALE_X |  |
| TIME | - | No explicit conversion | - |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | X | The value is converted to a character string. Enable output ENO is set to "0" if the character string length is exceeded, or if the value to be converted is an invalid floating-point number. The string has a minimum length of 21 characters. | LREAL_TO_STRING, S_CONV, VAL_STRG |  |
| WSTRING | X | LREAL_TO_WSTRING |  |  |
| CHAR | - | No explicit conversion | - |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[LREAL (S7-1200, S7-1500)](#lreal-s7-1200-s7-1500)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

#### Timers (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of TIME (S7-1200)](#explicit-conversion-of-time-s7-1200)

##### Explicit conversion of TIME (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the TIME data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| TIME | BOOL | - | No explicit conversion | - |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged to the target data type. | TIME_TO_BYTE |  |
| WORD<sup>1)</sup> | X | TIME_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | TIME_TO_DWORD |  |  |
| SINT | X | The bit pattern of the source value is transferred unchanged right-justified and interpreted as milliseconds to the target data type. | TIME_TO_SINT |  |
| USINT | X | TIME_TO_USINT |  |  |
| INT | X | TIME_TO_INT |  |  |
| UINT | X | TIME_TO_UINT |  |  |
| DINT | X | The bit pattern of the source value is transferred unchanged to the target data type. The result of the conversion shows the duration in milliseconds. | TIME_TO_DINT, T_CONV |  |
| UDINT | X | The bit pattern of the source value is transferred unchanged right-justified and interpreted as milliseconds to the target data type. Enable output ENO is set to "0" if the sign changes. | TIME_TO_UDINT |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| DTL | - | - |  |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If the source value exceeds the range of values of TOD, the target data type remains unchanged. | TIME_TO_TOD |  |
| DATE | - | No explicit conversion | - |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[TIME (IEC time)](#time-iec-time)
  
[Implicit conversion of TIME (S7-1200)](#implicit-conversion-of-time-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

#### Clock and calendar (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of DATE (S7-1200)](#explicit-conversion-of-date-s7-1200)
- [Explicit conversion of TOD (S7-1200)](#explicit-conversion-of-tod-s7-1200)
- [Explicit conversion of DTL (S7-1200)](#explicit-conversion-of-dtl-s7-1200)

##### Explicit conversion of DATE (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the DATE data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DATE | BOOL | - | No explicit conversion | - |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DATE_TO_BYTE |  |
| WORD<sup>1)</sup> | X | DATE_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | DATE_TO_DWORD |  |  |
| SINT | X | The number of days since 1/1/1990 is returned as result. | DATE_TO_SINT |  |
| USINT | X | DATE_TO_USINT |  |  |
| INT | X | DATE_TO_INT |  |  |
| UINT | X | DATE_TO_UINT |  |  |
| DINT | X | DATE_TO_DINT |  |  |
| UDINT | X | DATE_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL<sup> 2)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | DATE_TO_DTL |  |
| TOD | - | No explicit conversion | - |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width and then the bits are copied. The source type determines the interpretation.   <sup>2)</sup> The data type DTL is initialized as follows: 1970-1-1-0:0:0. Conversion from DATE_TO_DTL only sets the corresponding part of the DTL. The rest of the DTL remains as it was initialized. This results in the following differences for the instructions "T_COMBINE" and "T_CONV":  - T_COMBINE(D#2015-24-12, LTOD#12:13:14) returns DTL#2015-24-12-12:13:14 - myDTL := T_CONV(D#2015-24-12); myDTL := T_CONV(LTOD#12:13:14) results in myDTL = DTL#1970-1-1-12:13:14 |  |  |  |  |

---

**See also**

[DATE](#date)
  
[Implicit conversion of DATE (S7-1200)](#implicit-conversion-of-date-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of TOD (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the TOD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| TOD | BOOL | - | No explicit conversion | - |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged to the target data type. | TOD_TO_BYTE |  |
| WORD<sup>1)</sup> | X | TOD_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | TOD_TO_DWORD |  |  |
| SINT | X | The number of milliseconds since midnight is returned as result. | TOD_TO_SINT |  |
| USINT | X | TOD_TO_USINT |  |  |
| INT | X | TOD_TO_INT |  |  |
| UINT | X | TOD_TO_UINT |  |  |
| DINT | X | TOD_TO_DINT |  |  |
| UDINT | X | The result of the conversion corresponds to the number of milliseconds since the start of day (0:00 hrs). | TOD_TO_UDINT, T_CONV |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | X | The duration since midnight is returned as result. | TOD_TO_TIME |  |
| DTL | X | The date is set to 1.1.1970 as a result. | TOD_TO_DTL |  |
| DATE | - | No explicit conversion | - |  |
| STRING | - | - |  |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width including sign, and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[TIME_OF_DAY (TOD)](#time_of_day-tod)
  
[Implicit conversion of TOD (S7-1200)](#implicit-conversion-of-tod-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of DTL (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the DTL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DTL | BYTE | - | No explicit conversion | - |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | - | - |  |  |
| USINT | - | - |  |  |
| INT | - | - |  |  |
| UINT | - | - |  |  |
| DINT | - | - |  |  |
| UDINT | - | - |  |  |
| REAL | - | - |  |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| TOD | X | During the conversion, the time-of-day is extracted from the DTL format and written to the target data type. | DTL_TO_TOD, T_CONV |  |
| DATE | X | During the conversion, the date is extracted from the DTL format and written to the target data type. The enable output ENO is set to "0" in the event of overflow. | DTL_TO_DATE, T_CONV |  |
| STRING | - | No explicit conversion | - |  |
| WSTRING | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DTL (S7-1200, S7-1500)](#dtl-s7-1200-s7-1500)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

#### Character strings (S7-1200)

This section contains information on the following topics:

- [Explicit conversion of CHAR (S7-1200)](#explicit-conversion-of-char-s7-1200)
- [Explicit conversion of WCHAR (S7-1200)](#explicit-conversion-of-wchar-s7-1200)
- [Explicit conversion of STRING (S7-1200)](#explicit-conversion-of-string-s7-1200)
- [Explicit conversion of WSTRING (S7-1200)](#explicit-conversion-of-wstring-s7-1200)

##### Explicit conversion of CHAR (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the CHAR data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| CHAR | BOOL | - | No explicit conversion | - |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | CHAR_TO_BYTE |  |
| WORD<sup>1)</sup> | X | CHAR_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | CHAR_TO_DWORD |  |  |
| SINT | X | CHAR_TO_SINT |  |  |
| USINT | X | CHAR_TO_USINT |  |  |
| INT | X | CHAR_TO_INT |  |  |
| UINT | X | CHAR_TO_UINT |  |  |
| DINT | X | CHAR_TO_DINT |  |  |
| UDINT | X | CHAR_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | X | The value is converted to the first character in the character string (STRING). If the length of the character string is not defined, the length "1" is set after the conversion. If the length of the character string is defined, it remains unchanged after the conversion. | CHAR_TO_STRING |  |
| WSTRING | - | No explicit conversion | - |  |
| WCHAR | X |  | CHAR_TO_WCHAR |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

---

**See also**

[CHAR](#char)
  
[Implicit conversion of CHAR (S7-1200)](#implicit-conversion-of-char-s7-1200)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of WCHAR (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the WCHAR data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| WCHAR | BOOL | - | No explicit conversion | - |
| BYTE<sup>1)</sup> | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WCHAR_TO_BYTE |  |
| WORD<sup>1)</sup> | X | WCHAR_TO_WORD |  |  |
| DWORD<sup>1)</sup> | X | WCHAR_TO_DWORD |  |  |
| SINT | X | WCHAR_TO_SINT |  |  |
| USINT | X | WCHAR_TO_USINT |  |  |
| INT | X | WCHAR_TO_INT |  |  |
| UINT | X | WCHAR_TO_UINT |  |  |
| DINT | X | WCHAR_TO_DINT |  |  |
| UDINT | X | WCHAR_TO_UDINT |  |  |
| REAL | - | No explicit conversion | - |  |
| LREAL | - | - |  |  |
| TIME | - | - |  |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| WSTRING | X | The value is converted to the first character in the character string (WSTRING). If the length of the character string is not defined, the length "1" is set after conversion. If the length of the character string is defined, it remains unchanged after conversion. | WCHAR_TO_WSTRING |  |
| CHAR | X |  | WCHAR_TO_CHAR |  |
| x: Conversion possible  - : Conversion not possible   <sup>1)</sup> Bit strings (BYTE, WORD, DWORD) and data type CHAR are first extended to the necessary width and then the bits are copied. The source type determines the interpretation. |  |  |  |  |

##### Explicit conversion of STRING (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the STRING data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| STRING | BOOL | - | No explicit conversion | - |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | X | Conversion begins with the first character in the character string (STRING) and stops at the end of the string or at the first inadmissible character. The following characters are permitted for conversion:  - Digit - Sign - Dot   The first character of the string may be a sign (+, -) or a number. Leading spaces are ignored. The dot is used as separation for the conversion of floating-point numbers. The exponential notation "e" or "E" is not permitted. The comma as thousands separator is permitted to the left of the decimal point but will be ignored. If the layout of the character string is invalid for the conversion or an overflow occurs, then the enable output ENO will be set to "0". | STRING_TO_SINT, S_CONV, STRG_VAL |  |
| USINT | X | STRING_TO_USINT, S_CONV, STRG_VAL |  |  |
| INT | X | STRING_TO_INT, S_CONV, STRG_VAL |  |  |
| UINT | X | STRING_TO_UINT, S_CONV, STRG_VAL |  |  |
| DINT | X | STRING_TO_DINT, S_CONV, STRG_VAL |  |  |
| UDINT | X | STRING_TO_UDINT, S_CONV, STRG_VAL |  |  |
| REAL | X | STRING_TO_REAL, S_CONV, STRG_VAL |  |  |
| LREAL | X | STRING_TO_LREAL, S_CONV, STRG_VAL |  |  |
| TIME | - | No explicit conversion | - |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| CHAR | X | The first character in the character string (STRING) is transferred to the destination data type. If the string is empty, then the value "0" will be written in the destination data type. | STRING_TO_CHAR, S_CONV |  |
| WCHAR | - | No explicit conversion | - |  |
| WSTRING | X |  | STRING_TO_WSTRING |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[STRING](#string)
  
[Overview of data type conversion (S7-1200)](#overview-of-data-type-conversion-s7-1200)

##### Explicit conversion of WSTRING (S7-1200)

###### Options for explicit conversion

The following table shows the options and instructions for explicit conversion of the WSTRING data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| WSTRING | BOOL | - | No explicit conversion | - |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | - |  |  |
| SINT | X | Conversion begins with the first character in the character string (STRING) and stops at the end of the string or at the first inadmissible character. The following characters are permitted for conversion:  - Digit - Sign - Dot   The first character of the string may be a sign (+, -) or a number. Leading spaces are ignored. The dot is used as separation for the conversion of floating-point numbers. The exponential notation "e" or "E" is not permitted. The comma as thousands separator is permitted to the left of the decimal point but will be ignored. If the layout of the character string is invalid for the conversion, or an overflow occurs, the enable output ENO will be set to "0". | WSTRING_TO_SINT, S_CONV, STRG_VAL |  |
| USINT | X | WSTRING_TO_USINT, S_CONV, STRG_VAL |  |  |
| INT | X | WSTRING_TO_INT, S_CONV, STRG_VAL |  |  |
| UINT | X | WSTRING_TO_UINT, S_CONV, STRG_VAL |  |  |
| DINT | X | WSTRING_TO_DINT, S_CONV, STRG_VAL |  |  |
| UDINT | X | WSTRING_TO_UDINT, S_CONV, STRG_VAL |  |  |
| REAL | X | WSTRING_TO_REAL, S_CONV, STRG_VAL |  |  |
| LREAL | X | WSTRING_TO_LREAL, S_CONV, STRG_VAL |  |  |
| TIME | - | No explicit conversion | - |  |
| DTL | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| CHAR | - | - |  |  |
| WCHAR | X | The first character in the character string (WSTRING) is transferred to the target data type. If the string is empty, the value "0" will be written in the target data type. | WSTRING_TO_WCHAR |  |
| STRING | X |  | WSTRING_TO_STRING |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

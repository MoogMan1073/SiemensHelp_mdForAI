---
title: "Data type conversion for S7-300, S7-400 (S7-300, S7-400)"
package: ProgConvert34enUS
topics: 49
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Data type conversion for S7-300, S7-400 (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
- [Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)
- [Explicit conversions (S7-300, S7-400)](#explicit-conversions-s7-300-s7-400)

## Overview of data type conversions (S7-300, S7-400)

### Introduction

If you combine several operands in an instruction, you must make sure that the data types are compatible. This also applies when you assign or supply block parameters. If the operands are not of the same data type, a conversion has to be carried out.

There are two options for conversion:

- Implicit conversion

  Implicit conversion is supported by the programming languages LAD, FBD, SCL and GRAPH. Implicit conversion is not possible in the STL programming language.
- Explicit conversion

> **Note**
>
> **Converting bit strings to SCL**
>
> All bit strings (BYTE, WORD, and DWORD) are handled like the corresponding unsigned integers (USINT, UINT, and UDINT) in expressions. Therefore, implicit conversion from DWORD to REAL is carried out like a conversion from UDINT to REAL, for example.

### Implicit conversion

Implicit conversion is executed automatically if the data types of the operands are compatible. This compatibility test can be carried out according to strict or less strict criteria:

- With IEC check

  The following rules apply in the LAD, FBD and GRAPH programming languages when the IEC check has been set:

  - The only data types for which implicit conversion is possible are BYTE and WORD.
  - The bit length of the source data type may not exceed the bit length of the target data type. A WORD data type operand, for example, cannot be specified at a parameter at which the BYTE data type is expected.

  The following rules apply in the SCL programming language when the IEC check has been set:

  - Implicit conversion of bit strings into other data types is not possible. A WORD data type operand, for example, cannot be specified at a parameter at which the INT data type is expected.
  - The bit length of the source data type may not exceed the bit length of the target data type. A WORD data type operand, for example, cannot be specified at a parameter at which the BYTE data type is expected.
- Without IEC check (default setting)

  The following rules apply in the LAD, FBD and GRAPH programming languages when the IEC check has not been set:

  - Implicit conversion of data types BYTE, WORD, DWORD, INT, DINT, TIME, S5TIME, TOD, DATE and CHAR is possible.
  - The bit length of the source data type may not exceed the bit length of the target data type. A DWORD data type operand, for example, cannot be specified at a parameter at which the WORD data type is expected.

  The following rules apply in the SCL programming language when the IEC check has not been set:

  - Bit strings can be implicitly converted into other data types. A WORD data type operand can, for example, be given at a parameter at which the WORD data type is expected.
  - Bit strings cannot be implicitly converted into floating-point numbers. A WORD data type operand, for example, cannot be specified at a parameter at which the REAL data type is expected.
  - Bit strings can only be implicitly converted into the data types TIME, TOD, DATE and CHAR if these have the same bit length. A DWORD data type operand, for example, cannot be specified at a parameter at which the DATE data type is expected.
  - The bit length of the source data type may not exceed the bit length of the target data type. A DINT data type operand, for example, cannot be specified at a parameter at which the INT data type is expected.
  - The bit length of an operand entered at in-out parameters must be the same as the programmed bit length for the parameter in question.

### Explicit conversion

If the operands are not compatible and implicit conversion is therefore not possible, you can use an explicit conversion instruction. You can find the conversion instructions in the "Instructions" task card.

Any overflow will be displayed on the ENO enable output. An overflow occurs, for example, if the value of the source data type is greater than the value of the target data type.

> **Note**
>
> **Shifting of bit patterns​**
>
> If the explicit conversion involves shifting a bit pattern, the enable output ENO is not set.

You can find additional information on explicit conversion under "See also".

The following figure shows an example in which explicit data type conversion must be carried out:

![Explicit conversion](images/22121470731_DV_resource.Stream@PNG-en-US.png)

The "Block" function block expects a tag of the INT data type at the "IN_INT" input parameter. The value of the "IN_DINT" tag has therefore to the converted first from DINT to INT. Conversion is performed if the value of the "IN_DINT" tag is within the admissible value range for the INT data type. Otherwise an overflow is reported. However, a conversion takes place even in the event of an overflow, but the values are truncated and the ENO enable output is set to "0".

---

**See also**

[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)
  
[Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)
  
[Explicit conversions (S7-300, S7-400)](#explicit-conversions-s7-300-s7-400)

## Implicit conversions (S7-300, S7-400)

This section contains information on the following topics:

- [Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)
- [Binary numbers (S7-300, S7-400)](#binary-numbers-s7-300-s7-400)
- [Integers (S7-300, S7-400)](#integers-s7-300-s7-400)
- [Floating-point numbers (S7-300, S7-400)](#floating-point-numbers-s7-300-s7-400)
- [Timers (S7-300, S7-400)](#timers-s7-300-s7-400)
- [Date and time (S7-300, S7-400)](#date-and-time-s7-300-s7-400)
- [Character strings (S7-300, S7-400)](#character-strings-s7-300-s7-400)

### Activate or deactivate IEC check (S7-300, S7-400)

The data types of the tags used are checked for compatibility. This compatibility test can be carried out according to criteria that are more or less strict. If "IEC check for code blocks" is activated, stricter criteria are applied.

You can set the IEC check centrally for all new blocks of the project or for individual blocks.

#### Setting IEC check for new blocks

To set the IEC check for all new blocks in the project, proceed as follows:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. Select the "PLC programming > General" group in the area navigation.
3. Select or clear the "IEC check for code blocks" check box in the "Default settings for new blocks" group.

   The IEC check is enabled or disabled for all new blocks in the program.

#### Setting IEC check for a block

To set the IEC check for a block, proceed as follows:

1. Open the block.
2. Open the "Properties" tab in the inspector window.
3. Select the "Attributes" group in the area navigation.
4. Select or clear the "IEC check" check box.

   The IEC check is enabled or disabled for this block. The setting is stored together with the project.

---

**See also**

[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)

### Binary numbers (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of BOOL (S7-300, S7-400)](#implicit-conversion-of-bool-s7-300-s7-400)
- [Bit strings (S7-300, S7-400)](#bit-strings-s7-300-s7-400)

#### Implicit conversion of BOOL (S7-300, S7-400)

##### Implicit conversion options

The BOOL data type cannot be implicitly converted.

---

**See also**

[BOOL (bit)](Data%20types.md#bool-bit)

#### Bit strings (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of BYTE (S7-300, S7-400)](#implicit-conversion-of-byte-s7-300-s7-400)
- [Implicit conversion of WORD (S7-300, S7-400)](#implicit-conversion-of-word-s7-300-s7-400)
- [Implicit conversion of DWORD (S7-300, S7-400)](#implicit-conversion-of-dword-s7-300-s7-400)

##### Implicit conversion of BYTE (S7-300, S7-400)

###### Implicit conversion options

The following table shows the options for the implicit conversion of BYTE data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| BYTE | BOOL | - | - | No implicit conversion |
| WORD | X | X | The bit pattern of the source value is transferred unchanged right-justified to the target data type. |  |
| DWORD | X | X |  |  |
| INT | - | - | No implicit conversion |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged right-justified to the target data type. |  |
| REAL | - | - | No implicit conversion |  |
| TIME | - | - |  |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | X | The bit pattern of the source value is transferred unchanged to the target data type. |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[BYTE](Data%20types.md#byte)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of BYTE (S7-300, S7-400)](#explicit-conversion-of-byte-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

##### Implicit conversion of WORD (S7-300, S7-400)

###### Implicit conversion options

The following table shows the options for the implicit conversion of WORD data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| WORD | BOOL | - | - | No implicit conversion |
| BYTE | - | X | Only the low byte is transferred to the destination data type. |  |
| DWORD | X | X | The bit pattern of the source value is transferred unchanged right-justified to the destination data type. |  |
| INT | - | X |  |  |
| DINT | - | X |  |  |
| REAL | - | - | No implicit conversion |  |
| TIME | - | - |  |  |
| S5TIME | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| DT | - | - | No implicit conversion |  |
| TOD | - | - |  |  |
| DATE | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| STRING | - | - | No implicit conversion |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[WORD](Data%20types.md#word)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of WORD (S7-300, S7-400)](#explicit-conversion-of-word-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

##### Implicit conversion of DWORD (S7-300, S7-400)

###### Implicit conversion options

The following table shows the options for the implicit conversion of DWORD data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DWORD | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| WORD | - | X |  |  |
| INT | - | - | No implicit conversion |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| REAL | - | - | No implicit conversion |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| S5TIME | - | - | No implicit conversion |  |
| DT | - | - |  |  |
| TOD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| DATE | - | - | No implicit conversion |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DWORD](Data%20types.md#dword)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of DWORD (S7-300, S7-400)](#explicit-conversion-of-dword-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

### Integers (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of INT (S7-300, S7-400)](#implicit-conversion-of-int-s7-300-s7-400)
- [Implicit conversion of DINT (S7-300, S7-400)](#implicit-conversion-of-dint-s7-300-s7-400)

#### Implicit conversion of INT (S7-300, S7-400)

##### Options for implicit conversion

The following table shows the options for the implicit conversion of INT data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| INT | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| DWORD | - | - | No implicit conversion |  |
| DINT <sup>1)</sup> | X | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| REAL | X | X |  |  |
| TIME | - | - | No implicit conversion |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible   <sup>1)</sup>: Only possible in SCL |  |  |  |  |

---

**See also**

[INT (16-bit integers)](Data%20types.md#int-16-bit-integers)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of INT (S7-300, S7-400)](#explicit-conversion-of-int-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

#### Implicit conversion of DINT (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of DINT data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DINT | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| INT | - | - | No implicit conversion |  |
| REAL | - | - |  |  |
| TIME | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| S5TIME | - | - | No implicit conversion |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DINT (32-bit integers)](Data%20types.md#dint-32-bit-integers)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of STRING (S7-300, S7-400)](#explicit-conversion-of-string-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

### Floating-point numbers (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of REAL (S7-300, S7-400)](#implicit-conversion-of-real-s7-300-s7-400)

#### Implicit conversion of REAL (S7-300, S7-400)

##### Implicit conversion options

The REAL data type cannot be implicitly converted.

---

**See also**

[REAL](Data%20types.md#real)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of CHAR (S7-300, S7-400)](#explicit-conversion-of-char-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

### Timers (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of TIME (S7-300, S7-400)](#implicit-conversion-of-time-s7-300-s7-400)
- [Implicit conversion of S5TIME (S7-300, S7-400)](#implicit-conversion-of-s5time-s7-300-s7-400)

#### Implicit conversion of TIME (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of TIME data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| TIME | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of conversion shows the duration in milliseconds. |  |
| INT | - | - | No implicit conversion |  |
| DINT | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of conversion shows the duration in milliseconds. |  |
| REAL | - | - | No implicit conversion |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[TIME (IEC time)](Data%20types.md#time-iec-time)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of TIME (S7-300, S7-400)](#explicit-conversion-of-time-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

#### Implicit conversion of S5TIME (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of S5TIME data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| S5TIME | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of conversion shows the duration in milliseconds. |  |
| DWORD | - | - | No implicit conversion |  |
| INT | - | - |  |  |
| DINT | - | - |  |  |
| REAL | - | - |  |  |
| TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[S5TIME (duration) (S7-300, S7-400)](Data%20types.md#s5time-duration-s7-300-s7-400)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of S5TIME (S7-300, S7-400)](#explicit-conversion-of-s5time-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

### Date and time (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of DATE (S7-300, S7-400)](#implicit-conversion-of-date-s7-300-s7-400)
- [Implicit conversion of TOD (S7-300, S7-400)](#implicit-conversion-of-tod-s7-300-s7-400)
- [Implicit conversion of DT (S7-300, S7-400)](#implicit-conversion-of-dt-s7-300-s7-400)

#### Implicit conversion of DATE (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of DATE data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| DATE | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of the conversion corresponds to the number of days since 01/01/1990. |  |
| DWORD | - | - | No implicit conversion |  |
| INT | - | - |  |  |
| DINT | - | - |  |  |
| REAL | - | - |  |  |
| TIME | - | - |  |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[DATE](Data%20types.md#date)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

#### Implicit conversion of TOD (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of TOD data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| TOD | BOOL | - | - | No implicit conversion |
| BYTE | - | - |  |  |
| WORD | - | - |  |  |
| DWORD | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of the conversion corresponds to the number of milliseconds since the start of day (0:00). |  |
| INT | - | - | No implicit conversion |  |
| DINT | - | - |  |  |
| REAL | - | - |  |  |
| TIME | - | - |  |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| DATE | - | - |  |  |
| STRING | - | - |  |  |
| CHAR | - | - |  |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[TIME_OF_DAY (TOD)](Data%20types.md#time_of_day-tod)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

#### Implicit conversion of DT (S7-300, S7-400)

##### Implicit conversion options

The DT data type cannot be implicitly converted.

---

**See also**

[DATE_AND_TIME (date and time of day)](Data%20types.md#date_and_time-date-and-time-of-day) 
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of DT (S7-300, S7-400)](#explicit-conversion-of-dt-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

### Character strings (S7-300, S7-400)

This section contains information on the following topics:

- [Implicit conversion of CHAR (S7-300, S7-400)](#implicit-conversion-of-char-s7-300-s7-400)
- [Implicit conversion of STRING (S7-300, S7-400)](#implicit-conversion-of-string-s7-300-s7-400)

#### Implicit conversion of CHAR (S7-300, S7-400)

##### Implicit conversion options

The following table shows the options for the implicit conversion of CHAR data type:

| Source | Target | With IEC check | Without IEC check | Explanation |
| --- | --- | --- | --- | --- |
| CHAR | BOOL | - | - | No implicit conversion |
| BYTE | - | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| WORD | - | - | No implicit conversion |  |
| DWORD | - | - |  |  |
| INT | - | - |  |  |
| DINT | - | - |  |  |
| REAL | - | - |  |  |
| TIME | - | - |  |  |
| S5TIME | - | - |  |  |
| DT | - | - |  |  |
| TOD | - | - |  |  |
| DATE | - | - |  |  |
| STRING | X | X | The bit pattern of the source value is transferred unchanged to the destination data type. |  |
| x: Conversion possible  -: Conversion not possible |  |  |  |  |

---

**See also**

[CHAR](Data%20types.md#char)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of CHAR (S7-300, S7-400)](#explicit-conversion-of-char-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

#### Implicit conversion of STRING (S7-300, S7-400)

##### Implicit conversion options

The STRING data type cannot be implicitly converted.

---

**See also**

[STRING](Data%20types.md#string)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Explicit conversion of STRING (S7-300, S7-400)](#explicit-conversion-of-string-s7-300-s7-400)
  
[Activate or deactivate IEC check (S7-300, S7-400)](#activate-or-deactivate-iec-check-s7-300-s7-400)

## Explicit conversions (S7-300, S7-400)

This section contains information on the following topics:

- [Binary numbers (S7-300, S7-400)](#binary-numbers-s7-300-s7-400-1)
- [Integers (S7-300, S7-400)](#integers-s7-300-s7-400-1)
- [Floating-point numbers (S7-300, S7-400)](#floating-point-numbers-s7-300-s7-400-1)
- [Timer operations (S7-300, S7-400)](#timer-operations-s7-300-s7-400)
- [Date and time (S7-300, S7-400)](#date-and-time-s7-300-s7-400-1)
- [String (S7-300, S7-400)](#string-s7-300-s7-400)
- [Additional conversion functions (S7-300, S7-400)](#additional-conversion-functions-s7-300-s7-400)

### Binary numbers (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of BOOL (S7-300, S7-400)](#explicit-conversion-of-bool-s7-300-s7-400)
- [Bit strings (S7-300, S7-400)](#bit-strings-s7-300-s7-400-1)

#### Explicit conversion of BOOL (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the BOOL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| BOOL | BYTE | X | Only the LSB (Least Significant Bit) is set in the destination data type. The enable output ENO is always "1". | CONVERT |
| WORD | X |  |  |  |
| DWORD | X |  |  |  |
| INT | X | BOOL_TO_INT |  |  |
| DINT | X | BOOL_TO_DINT |  |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[BOOL (bit)](Data%20types.md#bool-bit)
  
[Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)

#### Bit strings (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of BYTE (S7-300, S7-400)](#explicit-conversion-of-byte-s7-300-s7-400)
- [Explicit conversion of WORD (S7-300, S7-400)](#explicit-conversion-of-word-s7-300-s7-400)
- [Explicit conversion of DWORD (S7-300, S7-400)](#explicit-conversion-of-dword-s7-300-s7-400)

##### Explicit conversion of BYTE (S7-300, S7-400)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the BYTE data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| BYTE | BOOL | X | The following possibilities can occur:  - If the source is "0", the target data type is also "0" and the enable output ENO "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and the enable output ENO "1". - If bits are not equal to LSB in the source value, the target data type is set according to LSB and the enable output ENO is "0". | CONVERT |
| WORD | X | The bit pattern of the source value is transferred unchanged right-justified to the target data type. The remaining bits are set to "0". | CONVERT |  |
| DWORD | X |  |  |  |
| INT | X |  |  |  |
| DINT | X |  |  |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged right-justified to the target data type. The remaining bits are set to "0". | CONVERT |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[BYTE](Data%20types.md#byte)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of BYTE (S7-300, S7-400)](#implicit-conversion-of-byte-s7-300-s7-400)

##### Explicit conversion of WORD (S7-300, S7-400)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the WORD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| WORD | BOOL | X | The following possibilities can occur:  - If the source is "0", the destination data type is also "0" and the enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the destination data type is also "1" and the enable output ENO is "1". - If bit is not equal to LSB in the source value, the destination data type is set according to LSB and the enable output ENO is "0". | CONVERT |
| BYTE | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. If the permitted value range of the destination data type is violated, the enable output ENO is set to "0". The result of the conversion is invalid in such a case. |  |  |
| DWORD | X |  |  |  |
| INT | X |  |  |  |
| DINT | X |  |  |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | MOVE |  |
| DT | - | No explicit conversion | - |  |
| TOD | - |  |  |  |
| DATE | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | MOVE |  |
| STRING | - | No explicit conversion | - |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | WORD_TO_CHAR |  |
| BLOCK_DB | X | The bit pattern of WORD is interpreted as a data block number. | WORD_TO_BLOCK_DB |  |
| WORD_BCD<sup>1) 2)</sup> | INT | X | If the permitted value range of the destination data type is violated or if there is an invalid tetrad in the A - F range, the enable output ENO is set to "0". The result of the conversion is invalid in such a case. | WORD_BCD_TO_INT |
| BCD<sup>1) 2)</sup> | INT | X | BCD_TO_INT |  |
| x: Conversion possible  - : Conversion not possible   <sup>1) </sup>The value to be converted has data type WORD and is accepted as a BCD-coded value between -999 and +999. The result is available after conversion as an integer (in binary notation) of the type INT.   <sup>2)</sup> Valid for SCL: If the BCD code contains a pseudo tetrad, the CPU reports a programming error and opens the organization block "OB121". If the organization block OB121 is not present, the CPU changes to STOP mode. |  |  |  |  |

---

**See also**

[WORD](Data%20types.md#word)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of WORD (S7-300, S7-400)](#implicit-conversion-of-word-s7-300-s7-400)

##### Explicit conversion of DWORD (S7-300, S7-400)

###### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the DWORD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DWORD | BOOL | X | The following scenarios are possible:  - If the source is "0", the target data type is also "0" and enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the target data type is also "1" and the enable output ENO is "1". - If bit is not equal to LSB in the source value, the destination data type is set according to LSB and the enable output ENO is "0". | CONVERT |
| BYTE | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. |  |  |
| WORD | X |  |  |  |
| INT | X | ENO = TRUE  #int1 := DWORD_TO_INT(16#FFFF_FFFF); // -1 to #int1 := DWORD_TO_INT(16#FFFF_8000); // -32768 #int1 := DWORD_TO_INT(16#0); // 0 to #int1 := DWORD_TO_INT(16#0000_7FFF); // 32767    ENO = FALSE  #int1 := DWORD_TO_INT(16#FFFF_7FFF); // -32769 #int1 := DWORD_TO_INT(16#8000_0000); // -2147483648 #int1 := DWORD_TO_INT(16#8000); // 32768 to #int1 := DWORD_TO_INT(16#7FFF_FFFF); // 2147483647 |  |  |
| DINT | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | MOVE |  |
| REAL | X |  |  |  |
| TIME | X |  |  |  |
| S5TIME | - | No explicit conversion | - |  |
| DT | - |  |  |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | MOVE |  |
| DATE | - | No explicit conversion | - |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| DWORD_BCD<sup>1) 2)</sup> | DINT | X | If the permitted value range of the destination data type is violated or if there is an invalid tetrad in the A - F range, the enable output ENO is set to "0". The result of the conversion is invalid in such a case. | DWORD_BCD_TO_DINT |
| BCD<sup>1) 2)</sup> | DINT | X | BCD_TO_DINT |  |
| x: Conversion possible  - : Conversion not possible   <sup>1) </sup>The value to be converted has data type DWORD and is accepted as a BCD-coded value between -9999999 and +9999999. The result is available after conversion as an integer (in binary notation) of the type DINT.   <sup>2)</sup> Valid for SCL: If the BCD code contains a pseudo tetrad, the CPU reports a programming error and opens the organization block "OB121". If the organization block OB121 is not present, the CPU changes to STOP mode. |  |  |  |  |

---

**See also**

[DWORD](Data%20types.md#dword)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of DWORD (S7-300, S7-400)](#implicit-conversion-of-dword-s7-300-s7-400)

### Integers (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of INT (S7-300, S7-400)](#explicit-conversion-of-int-s7-300-s7-400)
- [Explicit conversion of DINT (S7-300, S7-400)](#explicit-conversion-of-dint-s7-300-s7-400)

#### Explicit conversion of INT (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the INT data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| INT | BOOL | X | The value is first converted to WORD and then to BOOL.  The following possibilities can occur:  - If the source is "0", the destination data type is also "0" and the enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the destination data type is also "1" and the enable output ENO is "1". - If bit is not equal to LSB in the source value, the destination data type is set according to LSB and the enable output ENO is "0". | INT_TO_BOOL |
| BYTE | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The enable output ENO is set to "0" if a negative value is converted to an unsigned destination data type or if overflow occurs. | CONVERT |  |
| WORD | X | MOVE |  |  |
| DWORD | X |  |  |  |
| DINT | X | CONVERT, ITD |  |  |
| REAL | X | The value is converted into the format of the destination data type (the value "1", for example, is converted with the instruction "Convert value" (CONVERT) into the value "1.0"). | CONVERT, SCALE, ITR |  |
| TIME | - | No explicit conversion | - |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | X | The value is converted into a character string. The character string is shown preceded by a sign. If the permitted length of the character string is violated, the enable output ENO is set to "0". | S_CONV, CONVERT |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged to the destination data type. With the conversion of negative values or with an overflow, the enable output ENO will be set to "0". | CONVERT |  |
| BCD<sup>1) 2)</sup> | X | If the permitted value range of the destination data type is violated or if there is an invalid tetrad in the A - F range, the enable output ENO is set to "0". The result of the conversion is invalid in such a case. | INT_TO_BCD |  |
| BCD_WORD<sup>1) 2)</sup> | X | INT_TO_BCD_WORD |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1) </sup>The value to be converted has type INT and is accepted as an integer with a value between -999 and +999. The result is available after conversion as a BCD-coded number of the type WORD.   <sup>2)</sup> Valid for SCL: If the BCD code contains a pseudo tetrad, the CPU reports a programming error and opens the organization block "OB121". If the organization block OB121 is not present, the CPU changes to STOP mode. |  |  |  |  |

---

**See also**

[INT (16-bit integers)](Data%20types.md#int-16-bit-integers)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of INT (S7-300, S7-400)](#implicit-conversion-of-int-s7-300-s7-400)

#### Explicit conversion of DINT (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the DINT data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DINT | BOOL | X | The value is first converted to DWORD and then to BOOL.  The following possibilities can occur:  - If the source is "0", the destination data type is also "0" and the enable output ENO is "1". - If only the LSB (Least Significant Bit) "1" is set in the source value, the destination data type is also "1" and the enable output ENO is "1". - If bit is not equal to LSB in the source value, the destination data type is set according to LSB and the enable output ENO is "0". | DINT_TO_BOOL |
| BYTE | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. The enable output ENO is set to "0" if a negative value is converted to an unsigned destination data type or if overflow occurs. | CONVERT |  |
| WORD | X |  |  |  |
| DWORD | X | MOVE |  |  |
| INT | X | CONVERT |  |  |
| REAL | X | The value is converted into the format of the destination data type (the value "1", for example, is converted with the instruction "Convert value" (CONVERT) into the value "1.0"). | CONVERT, DTR, SCALE |  |
| TIME | X | The bit pattern of the source value is transferred unchanged to the destination data type. | T_CONV, MOVE |  |
| S5TIME | - | No explicit conversion | - |  |
| DT | - |  |  |  |
| TOD | X | The bit pattern of the source value is transferred unchanged, right-justified, to the target data type. | CONVERT |  |
| DATE | X |  |  |  |
| STRING | X | The value is converted into a character string. The character string is shown preceded by a sign. If the permitted length of the character string is violated, the enable output ENO is set to "0". | S_CONV, CONVERT |  |
| CHAR | X | The bit pattern of the source value is transferred unchanged to the destination data type. With the conversion of negative values or with an overflow, the enable output ENO will be set to "0". | DINT_TO_CHAR |  |
| BCD<sup>1) 2)</sup> | X | If the permitted value range of the destination data type is violated or if there is an invalid tetrad in the A - F range, the enable output ENO is set to "0". The result of the conversion is invalid in such a case. | DINT_TO_BCD |  |
| BCD_DWORD<sup>1) 2)</sup> | X | DINT_TO_BCD_DWORD |  |  |
| x: Conversion possible  - : Conversion not possible   <sup>1) </sup>The value to be converted has data type DWORD and is accepted as a BCD-coded value between -9999999 and +9999999. The result is available after conversion as an integer (in binary notation) of the type DINT.   <sup>2)</sup> Valid for SCL: If the BCD code contains a pseudo tetrad, the CPU reports a programming error and opens the organization block "OB121". If the organization block OB121 is not present, the CPU changes to STOP mode. |  |  |  |  |

---

**See also**

[DINT (32-bit integers)](Data%20types.md#dint-32-bit-integers)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)

### Floating-point numbers (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of REAL (S7-300, S7-400)](#explicit-conversion-of-real-s7-300-s7-400)

#### Explicit conversion of REAL (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the REAL data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| REAL | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | - |  |  |  |
| DWORD | X | The bit pattern of the source value is transferred unchanged to the destination data type. | CONVERT, MOVE |  |
| INT | X | The value is converted into the destination data type. The result of conversion depends on the instruction employed. The enable output ENO is set to "0" if the admissible range of values of the destination data type is exceeded during conversion or the value to be converted has an invalid floating-point number. | CONVERT, ROUND, RND, CEIL, RND+, FLOOR, RND-, TRUNC, UNSCALE |  |
| DINT | X |  |  |  |
| TIME | - | No explicit conversion | - |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | X | The value is converted into a character string. The enable output ENO is set to "0" if the character string length is exceeded or the value to be converted has an invalid floating-point number. | S_CONV, CONVERT |  |
| CHAR | - | No explicit conversion | - |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[REAL](Data%20types.md#real)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)

### Timer operations (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of TIME (S7-300, S7-400)](#explicit-conversion-of-time-s7-300-s7-400)
- [Explicit conversion of S5TIME (S7-300, S7-400)](#explicit-conversion-of-s5time-s7-300-s7-400)

#### Explicit conversion of TIME (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the TIME data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| TIME | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | - |  |  |  |
| DWORD | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of conversion shows the duration in milliseconds. | CONVERT |  |
| INT | - | No explicit conversion | - |  |
| DINT | X | The bit pattern of the source value is transferred unchanged to the destination data type. The result of conversion shows the duration in milliseconds. | T_CONV, CONVERT |  |
| REAL | - | No explicit conversion | - |  |
| S5TIME | X | The value is converted to the destination data type format. The enable output ENO is set to "0" in the event of overflow. | T_CONV, CONVERT |  |
| DT | - | No explicit conversion | - |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[TIME (IEC time)](Data%20types.md#time-iec-time)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of TIME (S7-300, S7-400)](#implicit-conversion-of-time-s7-300-s7-400)

#### Explicit conversion of S5TIME (S7-300, S7-400)

##### Options for explicit conversion in LAD, FBD, STL and GRAPH

The following table shows the options and instructions for the explicit conversion of the S5TIME data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| S5TIME | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | X | The value is converted to the destination data type format. | S5TIME_TO_WORD |  |
| DWORD | - | No explicit conversion | - |  |
| INT | - |  |  |  |
| DINT | - |  |  |  |
| REAL | - |  |  |  |
| TIME | X | The value is converted to the destination data type format. | T_CONV, CONVERT |  |
| DT | - | No explicit conversion | - |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[S5TIME (duration) (S7-300, S7-400)](Data%20types.md#s5time-duration-s7-300-s7-400)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of S5TIME (S7-300, S7-400)](#implicit-conversion-of-s5time-s7-300-s7-400)

### Date and time (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of DATE (S7-300, S7-400)](#explicit-conversion-of-date-s7-300-s7-400)
- [Explicit conversion of TOD (S7-300, S7-400)](#explicit-conversion-of-tod-s7-300-s7-400)
- [Explicit conversion of DT (S7-300, S7-400)](#explicit-conversion-of-dt-s7-300-s7-400)

#### Explicit conversion of DATE (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the DATE data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DATE | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | X | The value is converted to the destination data type format. | DATE_TO_WORD |  |
| DWORD | - | No explicit conversion | - |  |
| INT | X | The value is converted to the destination data type format. | DATE_TO_INT |  |
| DINT | X | DATE_TO_DINT |  |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[DATE](Data%20types.md#date)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of DATE (S7-300, S7-400)](#implicit-conversion-of-date-s7-300-s7-400)

#### Explicit conversion of TOD (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the TOD data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| TOD | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | - |  |  |  |
| DWORD | X | The value is converted to the destination data type format. | TOD_TO_DWORD |  |
| INT | - | No explicit conversion | - |  |
| DINT | X | The bit pattern of the source value is transferred unchanged right-justified to the destination data type. | TOD_TO_DINT |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| DATE | - |  |  |  |
| STRING | - |  |  |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[TIME_OF_DAY (TOD)](Data%20types.md#time_of_day-tod)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of TOD (S7-300, S7-400)](#implicit-conversion-of-tod-s7-300-s7-400)

#### Explicit conversion of DT (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the DT data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| DT | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | - |  |  |  |
| DWORD | - |  |  |  |
| INT | - |  |  |  |
| DINT | - |  |  |  |
| REAL | - |  |  |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| TOD | X | During conversion, times are extracted from the DTL format and transferred to the destination data type. | T_CONV, CONVERT |  |
| DATE | X | During the conversion, the date information is extracted from the DTL format and transferred to the destination data type. |  |  |
| STRING | - | No explicit conversion | - |  |
| CHAR | - |  |  |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[DATE_AND_TIME (date and time of day)](Data%20types.md#date_and_time-date-and-time-of-day) 
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)

### String (S7-300, S7-400)

This section contains information on the following topics:

- [Explicit conversion of CHAR (S7-300, S7-400)](#explicit-conversion-of-char-s7-300-s7-400)
- [Explicit conversion of STRING (S7-300, S7-400)](#explicit-conversion-of-string-s7-300-s7-400)

#### Explicit conversion of CHAR (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the CHAR data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| CHAR | BOOL | - | No explicit conversion | - |
| BYTE | X | The bit pattern of the source value is transferred unchanged right-justified to the destination data type. | CONVERT |  |
| WORD | X |  |  |  |
| DWORD | X |  |  |  |
| INT | X |  |  |  |
| DINT | X |  |  |  |
| REAL | - | No explicit conversion | - |  |
| TIME | - |  |  |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| STRING | X | The value is converted into the first character in the character string (STRING). The length "1" is set after conversion if the character string length is not defined. If the character string length is defined, it remains unchanged following conversion. | S_CONV, CONVERT |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[CHAR](Data%20types.md#char)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversion of CHAR (S7-300, S7-400)](#implicit-conversion-of-char-s7-300-s7-400)

#### Explicit conversion of STRING (S7-300, S7-400)

##### Options for explicit conversion

The following table shows the options and instructions for the explicit conversion of the STRING data type:

| Source | Target | Conversion | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- | --- |
| STRING | BOOL | - | No explicit conversion | - |
| BYTE | - |  |  |  |
| WORD | - |  |  |  |
| DWORD | - |  |  |  |
| INT | X | Conversion begins with the first character in the character string (STRING) and stops at the end of the string or at the first inadmissible character. The following characters are admissible for conversion:  - Digit - Sign - Dot   The first character in the character string may be a sign (+, -) or a digit. Leading spaces are ignored. The dot is used as separation for the conversion of floating-point numbers. The exponential notation "e" or "E" is not permitted. The comma as thousand separator to the left of the decimal point is permitted but is ignored. If the layout of the character string is invalid for the conversion or an overflow occurs, then the enable output ENO will be set to "0". | S_CONV, CONVERT |  |
| DINT | X |  |  |  |
| REAL | X |  |  |  |
| TIME | - | No explicit conversion | - |  |
| S5TIME | - |  |  |  |
| DT | - |  |  |  |
| TOD | - |  |  |  |
| DATE | - |  |  |  |
| CHAR | X | The first character in the character string (STRING) is transferred to the target data type. The value "0" is written to the target data type if the character string is empty. | S_CONV, CONVERT |  |
| x: Conversion possible  - : Conversion not possible |  |  |  |  |

---

**See also**

[STRING](Data%20types.md#string)
  
[Overview of data type conversions (S7-300, S7-400)](#overview-of-data-type-conversions-s7-300-s7-400)
  
[Implicit conversions (S7-300, S7-400)](#implicit-conversions-s7-300-s7-400)

### Additional conversion functions (S7-300, S7-400)

This section contains information on the following topics:

- [Additional explicit conversion functions in SCL (S7-300, S7-400)](#additional-explicit-conversion-functions-in-scl-s7-300-s7-400)

#### Additional explicit conversion functions in SCL (S7-300, S7-400)

##### Additional options for explicit conversion in SCL

The following table shows the additional options and operations for explicit conversion in SCL:

| Source | Target | Explanation | Mnemonics of the instruction |
| --- | --- | --- | --- |
| WORD | BLOCK_DB | The bit pattern of WORD is interpreted as a data block number. | WORD_TO_BLOCK_DB |
| BLOCK_DB | WORD | The data block number is interpreted as a bit pattern of WORD. | BLOCK_DB_TO_WORD |

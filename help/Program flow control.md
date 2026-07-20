---
title: "Program flow control"
package: ProgFlowControlenUS
topics: 24
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Program flow control

This section contains information on the following topics:

- [Status word for S7-300, S7-400 (S7-300, S7-400)](#status-word-for-s7-300-s7-400-s7-300-s7-400)
- [Status word for S7-1500 (S7-1500)](#status-word-for-s7-1500-s7-1500)
- [Master Control Relay (S7-300, S7-400)](#master-control-relay-s7-300-s7-400)

## Status word for S7-300, S7-400 (S7-300, S7-400)

This section contains information on the following topics:

- [Basic information on the status word (S7-300, S7-400)](#basic-information-on-the-status-word-s7-300-s7-400)
- [Setting status bits (S7-300, S7-400)](#setting-status-bits-s7-300-s7-400)
- [Querying status bits in STL (S7-300, S7-400)](#querying-status-bits-in-stl-s7-300-s7-400)

### Basic information on the status word (S7-300, S7-400)

#### Description

The status word combines status bits that the CPU uses to control the binary logic operations and sets for digital processing. You can query the status bits and influence them individually.

The following table shows the arrangement of the status bits in the status word:

|  | Status word |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit number | 15-9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Content | 0 | BR | CC 1 | CC 0 | OV | OS | OR | STA | RLO | /FC |

The status bits /FC, RLO, STA, OR and BR are binary codes which the CPU uses for binary instructions. The status bits OS, OV, CC 0 and CC 1 are digital codes which generally express math function results.

#### /FC (first check)

The /FC bit signal state controls a logic operation string.

A logic operation string begins with an /FC bit signal state of "0" and a binary scan instruction (first scan). The first scan is the first binary bit logic operation or scan in a network. This sets the /FC bit to "1". The logic operation string ends with a binary value assignment (e.g. the "Set" instruction), a conditional jump or a change of block. This sets the /FC bit to "0".

#### RLO (result of logic operation)

The status bit RLO is the buffer in binary logic operations.

The CPU transfers the scan results of the first scan to the RLO. The scan results for each subsequent scan are combined with the RLO saved and the result obtained is then saved in the RLO.

You can set, reset or negate the RLO or save it in the binary result (BR) using the corresponding instructions.

The RLO is used to control the memory, timer and counter instructions and execute certain jump instructions.

#### STA (status)

The STA status bit is equal to the signal state of the binary operand queried.

The status of a logic operation that reads memory is always the same as the value of the addressed bit. The status of a logic operation that writes to memory (e.g. the "Set" or "Reset" instructions) always has the same value as the bit written by the instruction. If the instruction does not write to memory, the status has the same value as the addressed bit. The status bit has no significance for logic operation instructions that do not access the memory. These instructions set the status bit to "1". The status bit is not queried by instructions. It is only evaluated when displaying the online status of program variables.

#### OR (OR bit)

The OR status bit is used when an AND logic operation is executed before an OR logic operation.

The OR bit is set if the RLO of the AND logic operation is "1". This anticipates the result of the OR logic operation. Every other binary instruction resets the OR bit.

#### OS (Overflow, stored)

The OS status bit saves the set OV status bit.

When the CPU sets the OV status bit, it also sets the OS status bit. However, while the next properly executed instruction resets the OV bit, the OS status bit remains set. You are therefore able to query a number range overflow or, for example, the use of invalid floating-point numbers at a later stage in the current CPU cycle.

#### OV (Overflow)

The OV status bit shows a number range overflow or the use of invalid floating-point numbers.

The OV status bit can be influenced by math functions, conversion instructions, and floating-point number comparisons.

#### CC 0 and CC 1 (condition code bits)

The CC 0 and CC 1 status bits provide information on the results of the following instructions:

- Comparison instructions
- Math functions
- Word logic operations
- Shift and rotate instructions

#### BR (binary result)

The BR status bit is used to execute the EN/ENO mechanism for boxes or as a condition in certain jump instructions (STL). You can influence the BR status bit using certain instructions (e.g. SAVE).

### Setting status bits (S7-300, S7-400)

This section contains information on the following topics:

- [Setting the status bit for bit logic operations (S7-300, S7-400)](#setting-the-status-bit-for-bit-logic-operations-s7-300-s7-400)
- [Setting status bits in timer and counter instructions (S7-300, S7-400)](#setting-status-bits-in-timer-and-counter-instructions-s7-300-s7-400)
- [Setting the status bits in instructions with integers (S7-300, S7-400)](#setting-the-status-bits-in-instructions-with-integers-s7-300-s7-400)
- [Setting the status bits in instructions with floating-point numbers (S7-300, S7-400)](#setting-the-status-bits-in-instructions-with-floating-point-numbers-s7-300-s7-400)
- [Setting the status bit for comparison instructions (S7-300, S7-400)](#setting-the-status-bit-for-comparison-instructions-s7-300-s7-400)
- [Setting status bits in program control operation instructions (S7-300, S7-400)](#setting-status-bits-in-program-control-operation-instructions-s7-300-s7-400)
- [Setting the status bit for word logic operations (S7-300, S7-400)](#setting-the-status-bit-for-word-logic-operations-s7-300-s7-400)
- [Setting the status bits for shift and rotate instructions (S7-300, S7-400)](#setting-the-status-bits-for-shift-and-rotate-instructions-s7-300-s7-400)

#### Setting the status bit for bit logic operations (S7-300, S7-400)

##### Description

Binary instructions affect the OR, STA, RLO and /FC status bits.

##### Setting the status bits in LAD

The following table shows how the status bits are set in the LAD programming language:

| Instruction |  | Status bit |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OR | STA | RLO | /FC |
| -| |- | Normally open contact | x | x | x | 1 |
| -| / |- | Normally closed contact | x | x | x | 1 |
| -|NOT|- | Invert RLO | - | 1 | x | - |
| -( )- | Assignment | 0 | x | - | 0 |
| -(R)- | Reset output | 0 | x | - | 0 |
| -(S)- | Set output | 0 | x | - | 0 |
| SR | Set/reset flip-flop | x | x | x | 1 |
| RS | Reset/set flip-flop | x | x | x | 1 |
| -|P|- | Scan operand for positive signal edge | 0 | 1 | x | 1 |
| -|N|- | Scan operand for negative signal edge | 0 | 1 | x | 1 |
| P_TRIG | Scan RLO for positive signal edge | 0 | x | x | 1 |
| N_TRIG | Scan RLO for negative signal edge | 0 | x | x | 1 |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |

##### Setting the status bits in FBD

The following table shows how the status bits are set in the FBD programming language:

| Instruction |  | Status bit |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OR | STA | RLO | /FC |
| &amp; | AND logic operation | x | x | x | 1 |
| &lt;=1 | OR logic operation | x | x | x | 1 |
| X | EXCLUSIVE OR logic operation | x | x | x | 1 |
| -| | Insert binary input | - | 1 | x | - |
| -o| | Invert RLO | - | 1 | x | - |
| -( )- | Assignment | 0 | x | - | 0 |
| R | Reset output | 0 | x | - | 0 |
| S | Set output | 0 | x | - | 0 |
| SR | Set/reset flip-flop | x | x | x | 1 |
| RS | Reset/set flip-flop | x | x | x | 1 |
| P | Scan operand for positive signal edge | 0 | 1 | x | 1 |
| N | Scan operand for negative signal edge | 0 | 1 | x | 1 |
| P_TRIG | Scan RLO for positive signal edge | 0 | x | x | 1 |
| N_TRIG | Scan RLO for negative signal edge | 0 | x | x | 1 |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |

##### Setting the status bits in STL

The following table shows how the status bits are set in the STL programming language:

| Instruction |  | Status bit |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OR | STA | RLO | /FC |
| A | AND logic operation | 0 | x | x | 1 |
| AN | Negated AND logic operation | 0 | x | x | 1 |
| O | OR logic operation | 0 | x | x | 1 |
| ON | Negated OR logic operation | 0 | x | x | 1 |
| X | EXCLUSIVE OR logic operation | 0 | x | x | 1 |
| XN | Negated EXCLUSIVE OR logic operation | 0 | x | x | 1 |
| O | OR logic operation from AND functions | 0 | 1 | - | 0 |
| A( | AND logic operation with branch | 0 | 1 | - | 0 |
| AN( | Negated AND logic operation with branch | 0 | 1 | - | 0 |
| O( | OR logic operation with branch | 0 | 1 | - | 0 |
| ON( | Negated OR logic operation with branch | 0 | 1 | - | 0 |
| X( | EXCLUSIVE OR logic operation with branch | 0 | 1 | - | 0 |
| XN( | Negated EXCLUSIVE OR logic operation with branch | 0 | 1 | - | 0 |
| = | Assignment | 0 | x | - | 0 |
| R | Reset output | 0 | x | - | 0 |
| S | Set output | 0 | x | - | 0 |
| NOT | Invert RLO | - | 1 | x | - |
| SET | Set RLO to 1 | 0 | 1 | 1 | 0 |
| CLR | Reset RLO to 0 | 0 | 0 | 0 | 0 |
| SAVE | Save RLO in BR bit | - | - | - | - |
| FN | Scan RLO for negative signal edge | 0 | x | x | 1 |
| FP | Scan RLO for positive signal edge | 0 | x | x | 1 |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |

#### Setting status bits in timer and counter instructions (S7-300, S7-400)

##### Description

The timer and counter instructions affect the OR, STA, RLO and /ER status bits.

##### Setting the status bits in LAD and FBD

The following table shows how the status bits are set in the LAD and FDB programming languages:

| Instruction |  | Status bit |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OS | OR | STA | RLO | /FC |
| S_PULSE | Assign pulse timer parameters and start | - | x | x | x | 1 |
| S_PEXT | Assign extended pulse timer parameters and start | - | x | x | x | 1 |
| S_ODT | Assign on-delay timer parameters and start | - | x | x | x | 1 |
| S_ODTS | Assign retentive on-delay timer parameters and start | - | x | x | x | 1 |
| S_OFFDT | Assign off-delay timer parameters and start | - | x | x | x | 1 |
| SP | Start pulse timer | - | 0 | - | - | 0 |
| SE | Start extended pulse timer | - | 0 | - | - | 0 |
| SD | Start on-delay timer | - | 0 | - | - | 0 |
| SS | Start retentive on-delay timer | - | 0 | - | - | 0 |
| SF | Start off-delay timer | - | 0 | - | - | 0 |
| S_CUD | Assign parameters and count up / down | - | x | x | x | 1 |
| S_CU | Assign parameters and count up | - | x | x | x | 1 |
| S_CD | Assign parameters and count down | - | x | x | x | 1 |
| SC | Set counter value | - | 0 | x | - | 0 |
| CU | Count up | - | 0 | x | - | 0 |
| CD | Count down | - | 0 | - | - | 0 |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |  |

##### Setting the status bits in STL

The following table shows how the status bits are set in the STL programming language:

| Instruction |  | Status bit |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OS | OR | STA | RLO | /FC |
| FR | Enable timer | - | 0 | - | - | 0 |
| R | Reset timer | - | 0 | - | - | 0 |
| SP | Start pulse timer | - | 0 | - | - | 0 |
| SE | Start extended pulse timer | - | 0 | - | - | 0 |
| SD | Start on-delay timer | - | 0 | - | - | 0 |
| SS | Start retentive on-delay timer | - | 0 | - | - | 0 |
| SF | Start off-delay timer | - | 0 | - | - | 0 |
| FR | Enable counters | - | 0 | - | - | 0 |
| R | Reset counter | - | 0 | - | - | 0 |
| S | Set counter | - | 0 | - | - | 0 |
| CU | Count up | - | 0 | - | - | 0 |
| CD | Count down | - | 0 | - | - | 0 |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |  |

#### Setting the status bits in instructions with integers (S7-300, S7-400)

##### Description

Instructions with integers affect status bits CC 1, CC 0, OV and OS in the status word.

With a negative result, status bits CC 1 and CC 0 are set to "0". A positive result sets status bit CC 1 to "1" and status bit CC 0 to "0". Status bit CC 1 is set to "0" and status bit CC 0 is set to "1" if the result is negative.

In the case of a number range overflow, status bits OV and OS are set to "1". A divide by zero is indicated by status bits CC 1, CC 0, OV and OS having signal status "0".

The following tables show how the status bits are set when using integers:

| Valid range | CC 1 | CC 0 | OV | OS |
| --- | --- | --- | --- | --- |
| 0 (zero) | 0 | 0 | 0 | * |
| 16 bits: -32768 &lt;=result &lt; 0 (negative number)  32 bits: -2147483648 &lt;=result &lt; 0 (negative number) | 0 | 1 | 0 | * |
| 16 bits: 32767 &gt;= result &gt; 0 (positive number)  32 bits: 2147483647 &gt;= result &gt; 0 (positive number) | 1 | 0 | 0 | * |
| * The OS bit is not influenced by the result of the operation. |  |  |  |  |

| Invalid range | CC 1 | CC 0 | OV | OS |
| --- | --- | --- | --- | --- |
| Underflow at addition  16 bits: Result = -65536  32 bits: Result = -4294967296 | 0 | 0 | 1 | 1 |
| Underflow at multiplication  16 bits: Result &lt; -32768 (negative number)  32 bits: Result &lt; -2147483648 (negative number) | 0 | 1 | 1 | 1 |
| Overflow at addition, subtraction  16 bits: Result &gt; 32767 (positive number)  32 bits: Result &gt; 2147483647 (positive number) | 0 | 1 | 1 | 1 |
| Overflow at multiplication, division  16 bits: Result &gt; 32767 (positive number)  32 bits: Result &gt; 2147483647 (positive number) | 1 | 0 | 1 | 1 |
| Underflow at addition, subtraction  16 bits: Result &lt; -32768 (negative number)  32 bits: Result &lt; -2147483648 (negative number) | 1 | 0 | 1 | 1 |
| Division by 0 | 1 | 1 | 1 | 1 |

#### Setting the status bits in instructions with floating-point numbers (S7-300, S7-400)

##### Description

Instructions with floating point numbers affect status bits CC 1, CC 0, OV and OS in the status word.

With a negative result, status bits CC 1 and CC 0 are set to "0". A positive result sets status bit CC 1 to "1" and status bit CC 0 to "0". Status bit CC 1 is set to "0" and status bit CC 0 is set to "1" if the result is negative.

In the case of a number range overflow, status bits OV and OS are set to "1". An invalid floating point number is indicated by status bits CC 1, CC 0, OV and OS having signal status "0".

The following tables show how the status bits are set when using floating point numbers:

| Valid range | CC 1 | CC 0 | OV | OS |
| --- | --- | --- | --- | --- |
| +0, -0 (zero) | 0 | 0 | 0 | * |
| -3.402823E+38 &lt; result &lt; -1.175494E-38 (negative number) | 0 | 1 | 0 | * |
| +1.175494E-38 &lt; result &lt; 3.402824E+38 (positive number) | 1 | 0 | 0 | * |
| * The OS bit is not influenced by the result of the operation. |  |  |  |  |

| Invalid range | CC 1 | CC 0 | OV | OS |
| --- | --- | --- | --- | --- |
| Underflow  -1.175494E-38 &lt; result &lt; -1.401298E-45 (negative number) | 0 | 0 | 1 | 1 |
| Underflow  +1.401298E-45 &lt; result &lt; +1.175494E-38 (positive number) | 0 | 0 | 1 | 1 |
| Overflow  Result &lt; -3.402823E+38 (negative number) | 0 | 1 | 1 | 1 |
| Overflow  Result &gt; 3.402823E+38 (positive number) | 1 | 0 | 1 | 1 |
| Not a valid floating-point number or invalid operation (input value outside of the valid value range) | 1 | 1 | 1 | 1 |

#### Setting the status bit for comparison instructions (S7-300, S7-400)

##### Description

Comparison statements affect status bits CC 1, CC 0, OV, OS in the status word.

Comparison statements set status bits CC 1 and CC 0 regardless of the comparison relationship.

When invalid floating point numbers are used, status bits CC 1, CC 0, OV and OS are set to "1".

The following table shows how the status bits are set with comparison statements:

| Result | CC 1 | CC 0 | OV | OS |
| --- | --- | --- | --- | --- |
| Equal to (ACCU2 = ACCU1) | 0 | 0 | 0 | * |
| Greater than (ACCU2 &gt; ACCU1) | 1 | 0 | 0 | * |
| Smaller than (ACCU2 &lt; ACCU1) | 0 | 1 | 0 | * |
| Invalid floating-point number | 1 | 1 | 1 | 1 |
| * The OS bit is not influenced by the result of the operation. |  |  |  |  |

#### Setting status bits in program control operation instructions (S7-300, S7-400)

##### Description

The instructions for program control affect the OS, OR, STA, RLO and /FC status bits.

##### Setting the status bits in LAD and FBD

The following table shows how the status bits are set in the LAD and FDB programming languages:

| Instruction |  | Status bit |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OS | OR | STA | RLO | /FC |
| JMP | Jump if RLO = 1 | - | 0 | 1 | 1 | 0 |
| JMPN | Jump if RLO = 0 | - | 0 | 1 | 1 | 0 |
| RET | Return | 0 | 0 | 1 | 1 | 0 |
| CALL | Call block | 0 | 0 | 1 | - | 0 |
| OPN | Open global data block | - | - | - | - | - |
| OPNI | Open instance data block | - | - | - | - | - |
| MCR&lt; | Open MCR ranges | - | 0 | 1 | - | 0 |
| MCR&gt; | Close MCR ranges | - | 0 | 1 | - | 0 |
| MCRA | Enable MCR range | - | - | - | - | - |
| MCRD | Disable MCR range | - | - | - | - | - |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |  |

##### Setting the status bits in STL

The following table shows how the status bits are set in the STL programming language:

| Instruction |  | Status bit |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Mnemonics | Title | OS | OR | STA | RLO | /FC |
| JU | Unconditional jump | - | - | - | - | - |
| JC | Jump if RLO = 1 | - | 0 | 1 | 1 | 0 |
| JCN | Jump if RLO = 0 | - | 0 | 1 | 1 | 0 |
| JCB | Jump if RLO = 1 and save RLO | - | 0 | 1 | 1 | 0 |
| JNB | Jump if RLO = 0 and save RLO | - | 0 | 1 | 1 | 0 |
| JBI | Jump if BR = 1 | - | 0 | 1 | - | 0 |
| JNBI | Jump if BR = 1 | - | 0 | 1 | - | 0 |
| JO | Jump if OV = 1 | - | - | - | - | - |
| JOS | Jump if OS = 1 | 0 | - | - | - | - |
| JZ | Jump if the result is zero | - | - | - | - | - |
| JN | Jump if the result is not zero | - | - | - | - | - |
| JP | Jump if the result is greater than zero | - | - | - | - | - |
| JM | Jump if the result is less than zero | - | - | - | - | - |
| JPZ | Jump if the result is greater than or equal to zero | - | - | - | - | - |
| JMZ | Jump if the result is less than or equal to zero | - | - | - | - | - |
| JUO | Jump if the result is invalid | - | - | - | - | - |
| JL | Defining the jump list | - | - | - | - | - |
| LOOP | Loop | - | - | - | - | - |
| OPN | Open global data block | - | - | - | - | - |
| OPN_DI | Open instance data block | - | - | - | - | - |
| CALL | Call block | 0 | 0 | 1 | - | 0 |
| CC | Conditional block call | 0 | 0 | 1 | 1 | 0 |
| UC | Unconditional block call | 0 | 0 | 1 | - | 0 |
| BE | Block end | 0 | 0 | 1 | - | 0 |
| BEC | Conditional block end | x | 0 | 1 | 1 | 0 |
| BEU | Conditional block end | 0 | 0 | 1 | - | 0 |
| MCR( | Open MCR ranges | - | 0 | 1 | - | 0 |
| )MCR | Close MCR ranges | - | 0 | 1 | - | 0 |
| MCRA | Enable MCR range | - | - | - | - | - |
| MCRD | Disable MCR range | - | - | - | - | - |
| x: The instruction can write "1" or "0"  1: The instruction sets the status bit to "1".  0: The instruction resets the status bit to "0".  -: The status bit is not influenced. |  |  |  |  |  |  |

#### Setting the status bit for word logic operations (S7-300, S7-400)

##### Description

Word logic instructions affect status bits CC 1, CC 0, and OV in the status word.

If all the bits in the result of a word logic instruction are "0", status bit CC 1 is reset to "0". If at least one bit in the result is "1", status bit CC 1 is set to "1".

The following table shows how the status bits are set with word logic instructions:

| Result | CC 1 | CC 0 | OV |
| --- | --- | --- | --- |
| Zero | 0 | 0 | 0 |
| Not zero | 1 | 0 | 0 |

#### Setting the status bits for shift and rotate instructions (S7-300, S7-400)

##### Description

Shift and rotate instructions affect status bits CC 1, CC 0, and OV in the status word.

In the case of shift and rotate instructions, the signal status of the last shifted or rotated bit is transferred to status bit CC 1. Status bits CC 0 and OV are reset.

The following table shows the setting of the status bit for shift and rotate instructions:

| Displaced/rotated bit | CC 1 | CC 0 | OV |
| --- | --- | --- | --- |
| "0" | 0 | 0 | 0 |
| "1" | 1 | 0 | 0 |
| For shift or rotate number 0 | * | * | * |
| * The bit is not influenced by the result of the operation. |  |  |  |

### Querying status bits in STL (S7-300, S7-400)

This section contains information on the following topics:

- [Querying status bits with bit logic operation instructions (S7-300, S7-400)](#querying-status-bits-with-bit-logic-operation-instructions-s7-300-s7-400)
- [Querying status bits with jump instructions (S7-300, S7-400)](#querying-status-bits-with-jump-instructions-s7-300-s7-400)

#### Querying status bits with bit logic operation instructions (S7-300, S7-400)

##### Description

You can use the following bit logic instructions to query the signal state of bits in the status word:

- A: AND logic operation
- AN: Negated AND logic operation
- O: OR logic operation
- ON: Negated OR logic operation
- X: EXCLUSIVE OR logic operation
- XN: Negated EXCLUSIVE OR logic operation

The following table shows the operands which can be used to scan the signal state of the bits in the status word:

| Operand | Querying the status word |
| --- | --- |
| == 0 | Scan for ((CC 0 = 0) AND (CC 1 = 0)) |
| &lt;&gt; 0 | Scan for CC 0 &lt;&gt;CC 1 |
| &gt; 0 | Scan for ((CC 0 = 0) AND (CC 1 = 1)) |
| &lt; 0 | Scan for ((CC 0 = 1) AND (CC 1 = 0)) |
| &gt;= 0 | Scan for CC 0 = 0 |
| &lt;= 0 | Scan for CC 1 = 0 |
| UO | Scan for ((CC 1 = 1) AND (CC 0 = 1)) |
| OV | Scan for OV = 1 |
| OS | Scan for OS = 1 |
| BR | Scan for BR = 1 |

---

**See also**

[A: AND logic operation" (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#a-and-logic-operation-s7-300-s7-400)
  
[AN: Negated AND logic operation (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#an-negated-and-logic-operation-s7-300-s7-400)
  
[O: OR logic operation (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#o-or-logic-operation-s7-300-s7-400)
  
[ON: Negated OR logic operation (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#on-negated-or-logic-operation-s7-300-s7-400)
  
[X: EXCLUSIVE OR logic operation (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#x-exclusive-or-logic-operation-s7-300-s7-400)
  
[XN: Negated EXCLUSIVE OR logic operation (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#xn-negated-exclusive-or-logic-operation-s7-300-s7-400)
  
[O: OR logic operation of AND functions (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#o-or-logic-operation-of-and-functions-s7-300-s7-400)
  
[A(: AND logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#a-and-logic-operation-with-branch-s7-300-s7-400)
  
[AN(: Negated AND logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#an-negated-and-logic-operation-with-branch-s7-300-s7-400)
  
[O(: OR logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#o-or-logic-operation-with-branch-s7-300-s7-400)
  
[ON(: Negated OR logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#on-negated-or-logic-operation-with-branch-s7-300-s7-400)
  
[X(: EXCLUSIVE OR logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#x-exclusive-or-logic-operation-with-branch-s7-300-s7-400)
  
[XN(: Negated EXCLUSIVE OR logic operation with branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#xn-negated-exclusive-or-logic-operation-with-branch-s7-300-s7-400)
  
[): Close branch (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#close-branch-s7-300-s7-400)
  
[=: Assignment (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#assignment-s7-300-s7-400)
  
[R: Reset (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#r-reset-s7-300-s7-400)
  
[S: Set (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#s-set-s7-300-s7-400)
  
[NOT: Invert RLO (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#not-invert-rlo-s7-300-s7-400)
  
[SET: Set RLO to 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#set-set-rlo-to-1-s7-300-s7-400)
  
[CLR: Reset RLO to 0 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#clr-reset-rlo-to-0-s7-300-s7-400)
  
[SAVE: Save RLO in BR bit (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#save-save-rlo-in-br-bit-s7-300-s7-400)
  
[FN: Scan RLO for negative signal edge (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#fn-scan-rlo-for-negative-signal-edge-s7-300-s7-400)
  
[FP: Scan RLO for positive signal edge (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#fp-scan-rlo-for-positive-signal-edge-s7-300-s7-400)

#### Querying status bits with jump instructions (S7-300, S7-400)

##### Description

The following table shows the jump instruction evaluation of the status bits:

| RLO | BR | CC 1 | CC 0 | OV | OS | Executed instruction mnemonics |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - | JC, JCB |
| 0 | - | - | - | - | - | JCN, JNB |
| - | 1 | - | - | - | - | JBI |
| - | 0 | - | - | - | - | JNBI |
| - | - | 0 | 0 | - | - | JZ, JMZ, JPZ |
| - | - | 1 | 0 | - | - | JN, JP, JPZ |
| - | - | 0 | 1 | - | - | JN, JM, JMZ |
| - | - | 1 | 1 | - | - | JUO |
| - | - | - | - | 1 | - | JO |
| - | - | - | - | - | 1 | JOS |

The following table shows the dependency between status bits CC1 and CC0 and the conditional jump instructions:

| CC 1 | CC 0 | Result | Executed instruction mnemonics |
| --- | --- | --- | --- |
| 0 | 0 | = 0 | JZ |
| 1 or 0 | 0 or 1 | &lt;&gt; 0 | JN |
| 1 | 0 | &gt; 0 | JP |
| 0 | 1 | &lt; 0 | JM |
| 0 or 1 | 0 | &gt;= 0 | JPZ |
| 0 | 0 or 1 | &lt;= 0 | JMZ |
| 1 | 1 | UO (invalid) | JUO |

---

**See also**

[JU: Unconditional jump (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#ju-unconditional-jump-s7-300-s7-400)
  
[JC: Jump if RLO = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jc-jump-if-rlo-1-s7-300-s7-400)
  
[JCN: Jump if RLO = 0 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jcn-jump-if-rlo-0-s7-300-s7-400)
  
[JCB: Jump if RLO = 1 and save RLO (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jcb-jump-if-rlo-1-and-save-rlo-s7-300-s7-400)
  
[JNB:: Jump if RLO = 0 and save RLO (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jnb-jump-if-rlo-0-and-save-rlo-s7-300-s7-400)
  
[JBI: Jump if BR = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jbi-jump-if-br-1-s7-300-s7-400)
  
[JNBI: Jump if BR = 0 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jnbi-jump-if-br-0-s7-300-s7-400)
  
[JO: Jump if OV = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jo-jump-if-ov-1-s7-300-s7-400)
  
[JOS: Jump if OS = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jos-jump-if-os-1-s7-300-s7-400)
  
[JZ: Jump if the result is zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jz-jump-if-the-result-is-zero-s7-300-s7-400)
  
[JN: Jump if the result is not zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jn-jump-if-the-result-is-not-zero-s7-300-s7-400)
  
[JP: Jump if the result is greater than zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jp-jump-if-the-result-is-greater-than-zero-s7-300-s7-400)
  
[JM: Jump if the result is less than zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jm-jump-if-the-result-is-less-than-zero-s7-300-s7-400)
  
[JPZ: Jump if the result is greater than or equal to zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jpz-jump-if-the-result-is-greater-than-or-equal-to-zero-s7-300-s7-400)
  
[JMZ: Jump if the result is less than or equal to zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jmz-jump-if-the-result-is-less-than-or-equal-to-zero-s7-300-s7-400)
  
[JUO: Jump if the result is invalid (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#juo-jump-if-the-result-is-invalid-s7-300-s7-400)
  
[JL: Define jump list (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jl-define-jump-list-s7-300-s7-400)
  
[LOOP: Loop (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#loop-loop-s7-300-s7-400)

## Status word for S7-1500 (S7-1500)

This section contains information on the following topics:

- [Basic information on the status word (S7-1500)](#basic-information-on-the-status-word-s7-1500)
- [Querying and setting status bits in STL (S7-1500)](#querying-and-setting-status-bits-in-stl-s7-1500)

### Basic information on the status word (S7-1500)

#### Description

The status word combines status bits that the CPU uses to control the binary logic operations and sets for digital processing. You can query the status bits and influence them individually.

The following table shows the arrangement of the status bits in the status word:

|  | Status word |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit number | 15-9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Content | 0 | BR | CC 1 | CC 0 | OV | OS | 0 | 0 | 0 | 0 |

The status bits OS, OV, CC 0 and CC 1 are digital codes which generally express math function results.

#### OS (Overflow, stored)

The OS status bit saves the set OV status bit.

When the CPU sets the OV status bit, it also sets the OS status bit. However, while the next properly executed instruction resets the OV bit, the OS status bit remains set. You are therefore able to query a number range overflow or, for example, the use of invalid floating-point numbers at a later stage in the current CPU block.

#### OV (Overflow)

The OV status bit shows a number range overflow or the use of invalid floating-point numbers.

The OV status bit can be influenced by math functions, conversion instructions, and floating-point number comparisons.

#### CC 0 and CC 1 (condition code bits)

The CC 0 and CC 1 status bits provide information on the results of the following instructions:

- Comparison instructions
- Math functions
- Word logic operations
- Shift and rotate instructions

#### BR (binary result)

The BR status bit is used to execute the EN/ENO mechanism for boxes or as a condition in certain jump instructions (STL). You can influence the BR status bit using certain instructions (e.g. SAVE).

#### RLO (result of logic operation)

Status bit RLO is the buffer for binary logic operations and is not a component of the status word.

The CPU transfers the scan results of the first scan to the RLO. The scan results for each subsequent scan are combined with the RLO saved and the result obtained is then saved in the RLO.

You can set or reset the RLO using the corresponding instructions.

The RLO is used to control the memory, timer and counter instructions and execute certain jump instructions.

> **Note**
>
> Since the status bits are only partly needed for internal processing, they are only displayed if they are available for further program execution.

### Querying and setting status bits in STL (S7-1500)

This section contains information on the following topics:

- [Querying status bits with bit logic operation instructions (S7-1500)](#querying-status-bits-with-bit-logic-operation-instructions-s7-1500)
- [Querying status bits with jump instructions (S7-1500)](#querying-status-bits-with-jump-instructions-s7-1500)
- [Setting the status bit for word logic operations (S7-1500)](#setting-the-status-bit-for-word-logic-operations-s7-1500)

#### Querying status bits with bit logic operation instructions (S7-1500)

##### Description

You can use the following bit logic instructions to query the signal state of bits in the status word:

- A: AND logic operation
- AN: Negated AND logic operation
- O: OR logic operation
- ON: Negated OR logic operation
- X: EXCLUSIVE OR logic operation
- XN: Negated EXCLUSIVE OR logic operation

The following table shows the operands which can be used to scan the signal state of the bits in the status word:

| Operand | Querying the status word |
| --- | --- |
| == 0 | Scan for ((CC 0 = 0) AND (CC 1 = 0)) |
| &lt;&gt; 0 | Scan for CC 0 &lt;&gt;CC 1 |
| &gt; 0 | Scan for ((CC 0 = 0) AND (CC 1 = 1)) |
| &lt; 0 | Scan for ((CC 0 = 1) AND (CC 1 = 0)) |
| &gt;= 0 | Scan for CC 0 = 0 |
| &lt;= 0 | Scan for CC 1 = 0 |
| UO | Scan for ((CC 1 = 1) AND (CC 0 = 1)) |
| OV | Scan for OV = 1 |
| OS | Scan for OS = 1 |
| BR | Scan for BR = 1 |

---

**See also**

[A: AND logic operation (S7-1500)](STL%20%28S7-1500%29.md#a-and-logic-operation-s7-1500)
  
[AN: Negated AND logic operation (S7-1500)](STL%20%28S7-1500%29.md#an-negated-and-logic-operation-s7-1500)
  
[O: OR logic operation (S7-1500)](STL%20%28S7-1500%29.md#o-or-logic-operation-s7-1500)
  
[ON: Negated OR logic operation (S7-1500)](STL%20%28S7-1500%29.md#on-negated-or-logic-operation-s7-1500)
  
[X: EXCLUSIVE OR logic operation (S7-1500)](STL%20%28S7-1500%29.md#x-exclusive-or-logic-operation-s7-1500)
  
[XN: Negated EXCLUSIVE OR logic operation (S7-1500)](STL%20%28S7-1500%29.md#xn-negated-exclusive-or-logic-operation-s7-1500)
  
[O: OR logic operation of AND functions (S7-1500)](STL%20%28S7-1500%29.md#o-or-logic-operation-of-and-functions-s7-1500)
  
[A(: AND logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#a-and-logic-operation-with-branch-s7-1500)
  
[AN(: Negated AND logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#an-negated-and-logic-operation-with-branch-s7-1500)
  
[O(: OR logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#o-or-logic-operation-with-branch-s7-1500)
  
[ON(: Negated OR logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#on-negated-or-logic-operation-with-branch-s7-1500)
  
[X(: EXCLUSIVE OR logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#x-exclusive-or-logic-operation-with-branch-s7-1500)
  
[XN(: Negated EXCLUSIVE OR logic operation with branch (S7-1500)](STL%20%28S7-1500%29.md#xn-negated-exclusive-or-logic-operation-with-branch-s7-1500)
  
[): Close branch (S7-1500)](STL%20%28S7-1500%29.md#close-branch-s7-1500)
  
[=: Assignment (S7-1500)](STL%20%28S7-1500%29.md#assignment-s7-1500)
  
[R: Reset (S7-1500)](STL%20%28S7-1500%29.md#r-reset-s7-1500)
  
[S: Set (S7-1500)](STL%20%28S7-1500%29.md#s-set-s7-1500)
  
[NOT: Invert RLO (S7-1500)](STL%20%28S7-1500%29.md#not-invert-rlo-s7-1500)
  
[SET: Set RLO to 1 (S7-1500)](STL%20%28S7-1500%29.md#set-set-rlo-to-1-s7-1500)
  
[CLR: Reset RLO to 0 (S7-1500)](STL%20%28S7-1500%29.md#clr-reset-rlo-to-0-s7-1500)
  
[SAVE: Save RLO in BR bit (S7-1500)](STL%20%28S7-1500%29.md#save-save-rlo-in-br-bit-s7-1500)
  
[FN: Scan RLO for negative signal edge (S7-1500)](STL%20%28S7-1500%29.md#fn-scan-rlo-for-negative-signal-edge-s7-1500)
  
[FP: Scan RLO for positive signal edge (S7-1500)](STL%20%28S7-1500%29.md#fp-scan-rlo-for-positive-signal-edge-s7-1500)

#### Querying status bits with jump instructions (S7-1500)

##### Description

The following table shows the jump instruction evaluation of the status bits:

| RLO | BR | CC 1 | CC 0 | OV | OS | Executed instruction mnemonics |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | - | - | - | - | - | JC, JCB |
| 0 | - | - | - | - | - | JCN, JNB |
| - | 1 | - | - | - | - | JBI |
| - | 0 | - | - | - | - | JNBI |
| - | - | 0 | 0 | - | - | JZ, JMZ, JPZ |
| - | - | 1 | 0 | - | - | JN, JP, JPZ |
| - | - | 0 | 1 | - | - | JN, JM, JMZ |
| - | - | 1 | 1 | - | - | JUO |
| - | - | - | - | 1 | - | JO |
| - | - | - | - | - | 1 | JOS |

The following table shows the dependency between status bits CC 0 and CC 1 and the conditional jump instructions:

| CC 1 | CC 0 | Result | Executed instruction mnemonics |
| --- | --- | --- | --- |
| 0 | 0 | = 0 | JZ |
| 1 or 0 | 0 or 1 | &lt;&gt; 0 | JN |
| 1 | 0 | &gt; 0 | JP |
| 0 | 1 | &lt; 0 | JM |
| 0 or 1 | 0 | &gt;= 0 | JPZ |
| 0 | 0 or 1 | &lt;= 0 | JMZ |
| 1 | 1 | UO (invalid) | JUO |

---

**See also**

[JU: Unconditional jump (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#ju-unconditional-jump-s7-300-s7-400)
  
[JC: Jump if RLO = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jc-jump-if-rlo-1-s7-300-s7-400)
  
[JCN: Jump if RLO = 0 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jcn-jump-if-rlo-0-s7-300-s7-400)
  
[JCB: Jump if RLO = 1 and save RLO (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jcb-jump-if-rlo-1-and-save-rlo-s7-300-s7-400)
  
[JNB:: Jump if RLO = 0 and save RLO (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jnb-jump-if-rlo-0-and-save-rlo-s7-300-s7-400)
  
[JBI: Jump if BR = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jbi-jump-if-br-1-s7-300-s7-400)
  
[JNBI: Jump if BR = 0 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jnbi-jump-if-br-0-s7-300-s7-400)
  
[JO: Jump if OV = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jo-jump-if-ov-1-s7-300-s7-400)
  
[JOS: Jump if OS = 1 (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jos-jump-if-os-1-s7-300-s7-400)
  
[JZ: Jump if the result is zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jz-jump-if-the-result-is-zero-s7-300-s7-400)
  
[JN: Jump if the result is not zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jn-jump-if-the-result-is-not-zero-s7-300-s7-400)
  
[JP: Jump if the result is greater than zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jp-jump-if-the-result-is-greater-than-zero-s7-300-s7-400)
  
[JM: Jump if the result is less than zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jm-jump-if-the-result-is-less-than-zero-s7-300-s7-400)
  
[JPZ: Jump if the result is greater than or equal to zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jpz-jump-if-the-result-is-greater-than-or-equal-to-zero-s7-300-s7-400)
  
[JMZ: Jump if the result is less than or equal to zero (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jmz-jump-if-the-result-is-less-than-or-equal-to-zero-s7-300-s7-400)
  
[JUO: Jump if the result is invalid (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#juo-jump-if-the-result-is-invalid-s7-300-s7-400)
  
[JL: Define jump list (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#jl-define-jump-list-s7-300-s7-400)
  
[LOOP: Loop (S7-300, S7-400)](STL%20%28S7-300%2C%20S7-400%29.md#loop-loop-s7-300-s7-400)
  
[Jump label (S7-1500)](STL%20%28S7-1500%29.md#jump-label-s7-1500)
  
[JU: Unconditional jump (S7-1500)](STL%20%28S7-1500%29.md#ju-unconditional-jump-s7-1500)
  
[JC: Jump if RLO = 1 (S7-1500)](STL%20%28S7-1500%29.md#jc-jump-if-rlo-1-s7-1500)
  
[JCN: Jump if RLO = 0 (S7-1500)](STL%20%28S7-1500%29.md#jcn-jump-if-rlo-0-s7-1500)
  
[JCB: Jump if RLO = 1 and save RLO (S7-1500)](STL%20%28S7-1500%29.md#jcb-jump-if-rlo-1-and-save-rlo-s7-1500)
  
[JNB: Jump if RLO = 0 and save RLO (S7-1500)](STL%20%28S7-1500%29.md#jnb-jump-if-rlo-0-and-save-rlo-s7-1500)
  
[JBI: Jump if BR = 1 (S7-1500)](STL%20%28S7-1500%29.md#jbi-jump-if-br-1-s7-1500)
  
[JNBI: Jump if BR = 0 (S7-1500)](STL%20%28S7-1500%29.md#jnbi-jump-if-br-0-s7-1500)
  
[JO: Jump if OV = 1 (S7-1500)](STL%20%28S7-1500%29.md#jo-jump-if-ov-1-s7-1500)
  
[JOS: Jump if OS = 1 (S7-1500)](STL%20%28S7-1500%29.md#jos-jump-if-os-1-s7-1500)
  
[JZ: Jump if the result is zero (S7-1500)](STL%20%28S7-1500%29.md#jz-jump-if-the-result-is-zero-s7-1500)
  
[JN: Jump if the result is not zero (S7-1500)](STL%20%28S7-1500%29.md#jn-jump-if-the-result-is-not-zero-s7-1500)
  
[JP: Jump if the result is greater than zero (S7-1500)](STL%20%28S7-1500%29.md#jp-jump-if-the-result-is-greater-than-zero-s7-1500)
  
[JM: Jump if the result is less than zero (S7-1500)](STL%20%28S7-1500%29.md#jm-jump-if-the-result-is-less-than-zero-s7-1500)
  
[JPZ: Jump if the result is greater than or equal to zero (S7-1500)](STL%20%28S7-1500%29.md#jpz-jump-if-the-result-is-greater-than-or-equal-to-zero-s7-1500)
  
[JMZ: Jump if the result is less than or equal to zero (S7-1500)](STL%20%28S7-1500%29.md#jmz-jump-if-the-result-is-less-than-or-equal-to-zero-s7-1500)
  
[JUO: Jump if the result is invalid (S7-1500)](STL%20%28S7-1500%29.md#juo-jump-if-the-result-is-invalid-s7-1500)
  
[JL: Define jump list (S7-1500)](STL%20%28S7-1500%29.md#jl-define-jump-list-s7-1500)
  
[LOOP: Loop (S7-1500)](STL%20%28S7-1500%29.md#loop-loop-s7-1500)

#### Setting the status bit for word logic operations (S7-1500)

##### Description

Word logic instructions affect status bits CC 0 , CC 1, and OV in the status word. The status bits are only set if they are used in the program sequence.

If all the bits in the result of a word logic instruction are "0", status bit CC 1 is reset to "0". If at least one bit in the result is "1", status bit CC 1 is set to "1".

The following table shows how the status bits are set with word logic instructions:

| Result | CC 1 | CC 0 | OV |
| --- | --- | --- | --- |
| Zero | 0 | 0 | 0 |
| Not zero | 1 | 0 | 0 |

---

**See also**

[AW: AND logic operation word by word (S7-1500)](STL%20%28S7-1500%29.md#aw-and-logic-operation-word-by-word-s7-1500)
  
[OW: OR logic operation word by word (S7-1500)](STL%20%28S7-1500%29.md#ow-or-logic-operation-word-by-word-s7-1500)
  
[XOW: EXCLUSIVE OR logic operation word by word (S7-1500)](STL%20%28S7-1500%29.md#xow-exclusive-or-logic-operation-word-by-word-s7-1500)
  
[AD: AND logic operation double word by double word (S7-1500)](STL%20%28S7-1500%29.md#ad-and-logic-operation-double-word-by-double-word-s7-1500)
  
[OD: OR logic operation double word by double word (S7-1500)](STL%20%28S7-1500%29.md#od-or-logic-operation-double-word-by-double-word-s7-1500)
  
[XOD: EXCLUSIVE OR logic operation double word by double word (S7-1500)](STL%20%28S7-1500%29.md#xod-exclusive-or-logic-operation-double-word-by-double-word-s7-1500)

## Master Control Relay (S7-300, S7-400)

This section contains information on the following topics:

- [Master control relay (S7-300, S7-400)](#master-control-relay-s7-300-s7-400-1)
- [Important notes on using MCR functions (S7-300, S7-400)](#important-notes-on-using-mcr-functions-s7-300-s7-400)

### Master control relay (S7-300, S7-400)

#### Description of the MCR functionality

With conventional programmable controllers, the Master Control Relay (MCR) enables or disables the signal flow in one part of the controller.

> **Note**
>
> Refer to the information in the "[Important notes on using MCR functions](#important-notes-on-using-mcr-functions-s7-300-s7-400)" section

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| To prevent personal injury or property damage, never use the MCR to replace a hard-wired mechanical master control relay that is being used as an emergency stop or safety switching device. |  |

The MCR affects all instructions that write a value back to the memory. When MCR dependency is enabled these instructions respond regardless of any previous binary or digital logic operation.

The following instructions are available for the implementation of the MCR:

- MCRA: Enable MCR area
- MCR: Open MCR ranges
- MCR: Close MCR ranges
- MCRD: Disable MCR area

The MCR dependency for this area is enabled when the result of logic operation is "1" directly before the opening of an MCR area. If the RLO of the area is "0" when it is opened, the processing in this area is without MCR dependency.

### Important notes on using MCR functions (S7-300, S7-400)

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| Note the following for blocks in which the master control relay was enabled with the instruction "Enable MCR range" (MCRA):   - When the MCR is switched off, the value "0" is written by all assignments in program sections between the instructions "Open MCR range" (MCR( ) and "Close MCR range". - The MCR is then switched off exactly at the point when the result of logic operation (RLO) was "0" before an "Open MCR range" (MCR( ) instruction. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| CPU in STOP or undefined runtime characteristics!  For address calculations and also writes to local data, the compiler accesses the temporary variables defined after VAR_TEMP. The following command sequences therefore change the AS to STOP or lead to undefined runtime characteristics (refer to following explanations).    **Formal parameter access**   - Access to components of complex FC parameters of the type STRUCT, PLC data type (UDT), ARRAY, STRING - Access to components of complex FB parameters of the type STRUCT, PLC data type (UDT), ARRAY, STRING from the InOut area in a block with multiple instance capability. - Access to parameters of a function block with multiple instance capability if its address is greater than 8180.0. - Access in a function block with multiple instance capability to a parameter of the type BLOCK_DB opens DB0. Any subsequent data access changes the CPU to STOP. T 0, C 0, FC0, or FB0 are also always used for TIMER, COUNTER, BLOCK_FC, and BLOCK_FB.    **Parameter transfer**   In block calls in which parameters are transferred.   **Remedy**   Free the above commands from their dependence on the MCR:   1. Use the instruction "Disable MCR range" (MCRD) to disable the master control relay before the assignment or network in question. 2. Use the instruction "Enable MCR range" (MCRA) to enable the master control relay before the assignment or network in question. |  |

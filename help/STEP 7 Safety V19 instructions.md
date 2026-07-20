---
title: "STEP 7 Safety V19 instructions"
package: InstrFAILenUS
topics: 111
source: Siemens TIA Portal Information System (offline help, en-US)
---


# STEP 7 Safety V19 instructions

This section contains information on the following topics:

- [Overview of instructions](#overview-of-instructions)
- [General](#general)
- [Bit logic operations](#bit-logic-operations)
- [Safety functions](#safety-functions)
- [Timer operations](#timer-operations)
- [Counter operations](#counter-operations)
- [Comparator operations](#comparator-operations)
- [Math functions](#math-functions)
- [Move operations](#move-operations)
- [Conversion operations](#conversion-operations)
- [Program control operations](#program-control-operations)
- [Word logic operations](#word-logic-operations)
- [Shift and rotate](#shift-and-rotate)
- [Operating](#operating)
- [Additional instructions](#additional-instructions)
- [Communication](#communication)

## Overview of instructions

### Overview of instructions for the safety program

When programming an F-block, you can find all instructions available for programming an F-block in LAD or FBD with the configured F-CPU in the "Instructions" task card.

In addition to the instructions that are familiar to you from programming a standard block, there are also special safety functions, e.g., for two-hand monitoring, discrepancy analysis, muting, emergency STOP/emergency OFF, safety door monitoring, and feedback monitoring and instructions for safety-related CPU-CPU communication.

### Note the following

> **Note**
>
> Enable input EN and enable output ENO cannot be connected.
>
> Exception:
>
> (S7-1200, S7-1500) With the following instructions you can program overflow detection by connecting the enable output ENO:
>
> - [ADD: Add (STEP 7 Safety V19)](#add-add-step-7-safety-v19)
> - [SUB: Subtract (STEP 7 Safety V19)](#sub-subtract-step-7-safety-v19)
> - [MUL: Multiply (STEP 7 Safety V19)](#mul-multiply-step-7-safety-v19)
> - [DIV: Divide (STEP 7 Safety V19)](#div-divide-step-7-safety-v19)
> - [NEG: Create two's complement (STEP 7 Safety V19)](#neg-create-twos-complement-step-7-safety-v19)
> - [ABS: Form absolute value (STEP 7 Safety V19) (S7-1200, S7-1500)](#abs-form-absolute-value-step-7-safety-v19-s7-1200-s7-1500)
> - [CONVERT: Convert value (STEP 7 Safety V19)](#convert-convert-value-step-7-safety-v19)

## General

This section contains information on the following topics:

- [LAD](#lad)
- [FBD](#fbd)

### LAD

This section contains information on the following topics:

- [New network (STEP 7 Safety V19)](#new-network-step-7-safety-v19)
- [Empty box (STEP 7 Safety V19)](#empty-box-step-7-safety-v19)
- [Open branch (STEP 7 Safety V19)](#open-branch-step-7-safety-v19)
- [Close branch (STEP 7 Safety V19)](#close-branch-step-7-safety-v19)

#### New network (STEP 7 Safety V19)

##### Requirement

An F-block is open.

##### Procedure

To insert a new network, follow these steps:

1. Select the network after which you want to insert a new network.
2. Select the "Insert network" command in the shortcut menu.

> **Note**
>
> If you insert an element into the last empty network of the F-block in an LAD program, a new empty network is automatically inserted below it.

##### Result

A new empty network is inserted into the F-block.

#### Empty box (STEP 7 Safety V19)

##### Requirement

A network is available.

##### Procedure

To insert an LAD instruction into a network using an empty box, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "Basic instructions > General > Empty box".
3. Use a drag-and-drop operation to move the "Empty box" element to the desired place in the network.
4. Hover the cursor over the yellow triangle in the top right corner of the empty box.

   A drop-down list is displayed.
5. Select the required instruction from the drop-down list.

If the instruction acts as a function block (FB) within the system, the "Call options" dialog opens. In this dialog, you can create an instance data block for the function block, either as a single instance or, if necessary, multi-instance, in which data of the inserted instruction are stored. Once it is created, the new instance data block can be found in the "Program resources" folder in the project tree under "Program blocks > System blocks". If you have selected "multi-instance", you can find it in the block interface in the "Static" section.

##### Result

The empty box is changed to the appropriate instruction. Placeholders are inserted for the parameters.

#### Open branch (STEP 7 Safety V19)

##### Description

Use branches to program parallel connections with the Ladder Logic (LAD) programming language. Branches are inserted into the main current path. You can insert several contacts into the branch, thereby creating a parallel connection from series connections. You can program complex ladder diagrams in this way.

##### Requirement

- A network is available.
- The network contains elements.

##### Procedure

To insert a new branch in a network, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "Basic instructions > General > Open branch".
3. Use a drag-and-drop operation to move the element to the desired place in the network.
4. If you want to connect the new branch directly to the power rail, drag the element to the power rail.

##### Example

The following figure provides an example of how to use branches:

![Example](images/93487932683_DV_resource.Stream@PNG-de-DE.png)

#### Close branch (STEP 7 Safety V19)

##### Description

Branches must be closed again at suitable places. If necessary, branches will be arranged so that they do not cross each other.

##### Requirement

A branch is available.

##### Procedure

To close an open branch, follow these steps:

1. Select the open branch.
2. Press and hold down the left mouse button.

   A dashed line will appear as soon as the cursor is moved.
3. Drag the dashed line to a suitable place on the network. Permissible connections are indicated by green lines.
4. Release the left mouse button.

##### Example

The figure below provides an example of how to use branches:

![Example](images/93487932683_DV_resource.Stream@PNG-de-DE.png)

### FBD

This section contains information on the following topics:

- [New network (STEP 7 Safety V19)](#new-network-step-7-safety-v19-1)
- [Empty box (STEP 7 Safety V19)](#empty-box-step-7-safety-v19-1)
- [Open branch (STEP 7 Safety V19)](#open-branch-step-7-safety-v19-1)
- [Insert binary input (STEP 7 Safety V19)](#insert-binary-input-step-7-safety-v19)
- [Invert RLO (STEP 7 Safety V19)](#invert-rlo-step-7-safety-v19)

#### New network (STEP 7 Safety V19)

##### Requirement

An F-block is open.

##### Procedure

To insert a new network, follow these steps:

1. Select the network after which you want to insert a new network.
2. Select the "Insert network" command in the shortcut menu.

> **Note**
>
> If you insert an element into the last empty network of the F-block in an FBD program, a new empty network is automatically inserted below it.

##### Result

A new empty network is inserted into the F-block.

#### Empty box (STEP 7 Safety V19)

##### Requirement

A network is available.

##### Procedure

To insert FBD elements into a network using an empty box, follow these steps:

1. Open the "Instructions" task card.
2. Navigate to "Basic instructions > General > Empty box".
3. Use a drag-and-drop operation to move the "Empty box" element to the desired place in the network.
4. Hover the cursor over the yellow triangle in the top right corner of the empty box.

   A drop-down list is displayed.
5. Select the desired FBD element from the drop-down list.

If the instruction acts as a function block (FB) within the system, the "Call options" dialog opens. In this dialog, you can create an instance data block for the function block, either as a single instance or, if necessary, multi-instance, in which data of the inserted instruction are stored. Once it is created, the new instance data block can be found in the "Program resources" folder in the project tree under "Program blocks > System blocks". If you have selected "multi-instance", you can find it in the block interface in the "Static" section.

##### Result

The empty box is changed to the appropriate instruction. Placeholders are inserted for the parameters.

#### Open branch (STEP 7 Safety V19)

##### Description

You use branches, which you insert between the boxes, to program parallel connections with the Function Block Diagram (FBD) programming language You can insert additional boxes in the branch, thereby programming complex function block diagrams.

##### Requirement

A network is available.

##### Procedure

To insert a new branch in a network, follow these steps:

1. Open the "Instructions" task card.
2. Navigate in the pane to "Basic instructions > General > Branch".
3. Use a drag-and-drop operation to move the element to the desired place to a connecting line between two boxes.

##### Example

The following figure provides an example of how to use branches:

![Example](images/96274698635_DV_resource.Stream@PNG-de-DE.png)

#### Insert binary input (STEP 7 Safety V19)

##### Description

Use the "Insert binary input" instruction to expand the box of one of the following instructions by a binary input:

- "AND logic operation"
- "OR logic operation"
- "EXCLUSIVE OR logic operation"

You can query the signal state of several operands by expanding the instruction box.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | The operand indicates the bit whose signal state will be queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93490222219_DV_resource.Stream@PNG-de-DE.png)

The box of instruction "AND logic operation" has been expanded by an additional binary input at which the signal state of operand "TagIn_3" is queried. Output "TagOut" is set when the signal state of operands "TagIn_1", "TagIn_2", and "TagIn_3" is "1".

---

**See also**

[AND logic operation (STEP 7 Safety V19)](#and-logic-operation-step-7-safety-v19)
  
[OR logic operation (STEP 7 Safety V19)](#or-logic-operation-step-7-safety-v19)
  
[X: EXCLUSIVE OR logic operation (STEP 7 Safety V19)](#x-exclusive-or-logic-operation-step-7-safety-v19)

#### Invert RLO (STEP 7 Safety V19)

##### Description

You can use the "Invert RLO" instruction to invert the result of logic operation (RLO).

##### Example

The following example shows how the instruction works:

![Example](images/93490622731_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- The "TagIn_1" and/or "TagIn_2" input has the signal state "0".
- The "TagIn_3" or "TagIn_4" input has the signal state "0" or the "TagIn_5" input has the signal state "1".

## Bit logic operations

This section contains information on the following topics:

- [LAD](#lad-1)
- [FBD](#fbd-1)

### LAD

This section contains information on the following topics:

- [---| |---: NO contact (STEP 7 Safety V19)](#no-contact-step-7-safety-v19)
- [---| / |---: NC contact (STEP 7 Safety V19)](#nc-contact-step-7-safety-v19)
- [--|NOT|--: Invert RLO (STEP 7 Safety V19)](#not---invert-rlo-step-7-safety-v19)
- [---( )---: Assignment (STEP 7 Safety V19)](#assignment-step-7-safety-v19)
- [---( R )---: Reset output (STEP 7 Safety V19)](#r-----reset-output-step-7-safety-v19)
- [---( S )---: Set output (STEP 7 Safety V19)](#s-----set-output-step-7-safety-v19)
- [SR: Set/reset flip-flop (STEP 7 Safety V19)](#sr-setreset-flip-flop-step-7-safety-v19)
- [RS: Reset/set flip-flop (STEP 7 Safety V19)](#rs-resetset-flip-flop-step-7-safety-v19)
- [--|P|--: Scan operand for positive signal edge (STEP 7 Safety V19)](#p---scan-operand-for-positive-signal-edge-step-7-safety-v19)
- [--|N|--: Scan operand for negative signal edge (STEP 7 Safety V19)](#n---scan-operand-for-negative-signal-edge-step-7-safety-v19)
- [P_TRIG: Scan RLO for positive signal edge (STEP 7 Safety V19)](#p_trig-scan-rlo-for-positive-signal-edge-step-7-safety-v19)
- [N_TRIG: Scan RLO for negative signal edge (STEP 7 Safety V19)](#n_trig-scan-rlo-for-negative-signal-edge-step-7-safety-v19)

#### ---|   |---: NO contact (STEP 7 Safety V19)

##### Description

The activation of the normally open contact depends on the signal state of the associated operand. If the operand has signal state "1," the normally open contact is closed. Power flows from the left power rail through the normally open contact into the right power rail and the signal state at the output of the instruction is set to "1".

If the operand has signal state "0," the normally open contact is not activated. The power flow to the right power rail is interrupted and the signal state at the output of the instruction is reset to "0".

Two or more normally open contacts are linked bit-by-bit by AND when connected in series. With a series connection, power flows when all contacts are closed.

The normally open contacts are linked by OR when connected in parallel. With a parallel connection, power flows when one of the contacts is closed.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | Operand whose signal state is queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93487932683_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state at operand "TagIn_3" is "1".

#### ---| / |---: NC contact (STEP 7 Safety V19)

##### Description

The activation of the normally closed contact depends on the signal state of the associated operand. If the operand has signal state "1", the normally closed contact is opened and the signal state at the output of the instruction is reset to "0".

If the operand has signal state "0", the normally closed contact is not activated and the signal state at the output of the instruction is set to "1".

Two or more normally closed contacts are linked bit-by-bit by AND when connected in series. With a series connection, power flows when all contacts are closed.

The normally closed contacts are linked by OR when connected in parallel. With a parallel connection, power flows when one of the contacts is closed.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | Operand whose signal state is queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93490867723_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state at operand "TagIn_3" is "0".

#### --|NOT|--: Invert RLO (STEP 7 Safety V19)

##### Description

You can use the "Invert RLO" instruction to invert the signal state of the result of logic operation (RLO). When the signal state is "1" at the input of the instruction, the output of the instruction has the signal state "0". When the signal state is "0" at the input of the instruction, the output has the signal state "1".

##### Example

The following example shows how the instruction works:

![Example](images/93492330763_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is reset when one of the following conditions is fulfilled:

- Operand "TagIn_1" has signal state "1".
- Operands "TagIn_2" and "TagIn_3" have signal state "1".

#### ---(   )---: Assignment (STEP 7 Safety V19)

##### Description

You can use the "Assignment" instruction to set the bit of a specified operand. When the result of logic operation (RLO) at the input of the coil is "1," the specified operand is set to signal state "1". When the signal state is "0" at the input of the coil, the bit of the specified operand is reset to "0".

The instruction does not influence the RLO. The RLO at the input of the coil is sent immediately to the output.

The "Assignment" instruction can be placed at any position in the network.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand to which the RLO is assigned. |

##### Example

The following example shows how the instruction works:

![Example](images/93492412683_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state at operand "TagIn_3" is "0".

#### ---( R )---: Reset output (STEP 7 Safety V19)

##### Description

You can use the "Reset output" instruction to reset the signal state of a specified operand to "0".

If power flows to the coil (RLO is "1"), the specified operand is set to "0". If the result of logic operation at the input of the coil is "0" (no signal flow to the coil), the signal state of the specified operand remains unchanged.

The instruction does not influence the RLO. The RLO at the input of the coil is sent directly to the output of the coil.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

> **Note**
>
> You cannot use the "process image of the inputs", "process image of the outputs" from standard I/O and "standard DB" and "bit memory" operand areas for the operands of the instruction.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand that is reset when RLO = "1". |

##### Example

The following example shows how the instruction works:

![Example](images/93493663371_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is reset when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state of operand "TagIn_3" is "0".

#### ---( S )---: Set output (STEP 7 Safety V19)

##### Description

You can use the "Set output" instruction to set the signal state of a specified operand to "1".

If power flows to the coil (RLO is "1"), the specified operand is set to "1". If the result of logic operation at the input of the coil is "0" (no signal flow to the coil), the signal state of the specified operand remains unchanged.

The instruction does not influence the RLO. The RLO at the input of the coil is sent directly to the output of the coil.

> **Note**
>
> The instruction is not executed if it is applied to an output of an F‑I/O that is passivated (e.g., during startup of the F‑system). Therefore, it is preferable to access outputs of the F-I/O using only the "Assignment" instruction.
>
> An F-I/O output is passivated if QBAD or QBAD_O_xx = 1 or value status = 0 is set in the corresponding F-I/O DB.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

> **Note**
>
> You cannot use the "process image of the inputs", "process image of the outputs" from standard I/O and "standard DB" and "bit memory" operand areas for the operands of the instruction.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand that is set when RLO = "1". |

##### Example

The following example shows how the instruction works:

![Example](images/93493813515_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state of operand "TagIn_3" is "0".

#### SR: Set/reset flip-flop (STEP 7 Safety V19)

##### Description

You can use the "Set/reset flip-flop" instruction to set or reset the bit of the specified operand based on the signal state of inputs S and R1. If the signal state at input S is "1" and the signal state at input R1 is "0", the specified operand is set to "1". If the signal state at input S is "0" and the signal state at input R1 is "1", the specified operand is reset to "0".

Input R1 takes priority over input S. If the signal state is "1" at the two inputs S and R1, the signal state of the specified operand is reset to "0".

The instruction is not executed if the signal state at the two inputs S and R1 is "0". The signal state of the operand then remains unchanged.

The current signal state of the operand is transferred to output Q and can be queried there.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the operands of the instruction.
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| S | Input | BOOL | Enable set |
| R1 | Input | BOOL | Enable reset |
| <Operand> | Output | BOOL | Operand that is set or reset. |
| Q | Output | BOOL | Signal state of the operand |

##### Example

The following example shows how the instruction works:

![Example](images/102644408075_DV_resource.Stream@PNG-de-DE.png)

Operands ""F_DB_1".TagSR" and "TagOut" are set when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "1".
- Operand "TagIn_2" has signal state "0".

Operands ""F_DB_1".TagSR" and "TagOut" are reset when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "0" and operand "TagIn_2" has signal state "1".
- Both operands "TagIn_1" and "TagIn_2" have signal state "1".

#### RS: Reset/set flip-flop (STEP 7 Safety V19)

##### Description

You can use the "Reset/set flip-flop" instruction to reset or set the bit of the specified operand based on the signal state of inputs R and S1. When the signal state is "1" at input R and "0" at input S1, the specified operand is reset to "0". When the signal state is "0" at input R and "1" at input S1, the specified operand is set to "1".

Input S1 takes priority over input R. If the signal state is "1" at the two inputs R and S1, the signal state of the specified operand is set to "1".

The instruction is not executed if the signal state at the two inputs R and S1 is "0". The signal state of the operand then remains unchanged.

The current signal state of the operand is transferred to output Q and can be queried there.

> **Note**
>
> If you want to use a formal parameter of an F-FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the operands of the instruction.
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| R | Input | BOOL | Enable reset |
| S1 | Input | BOOL | Enable set |
| <Operand> | Output | BOOL | Operand that is reset or set. |
| Q | Output | BOOL | Signal state of the operand |

##### Example

The following example shows how the instruction works:

![Example](images/102644424715_DV_resource.Stream@PNG-de-DE.png)

Operands ""F_DB_1".TagRS" and "TagOut" are reset when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "1".
- Operand "TagIn_2" has signal state "0".

Operands ""F_DB_1".TagRS" and "TagOut" are set when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "0" and operand "TagIn_2" has signal state "1".
- Operands "TagIn_1" and "TagIn_2" have signal state "1".

#### --|P|--: Scan operand for positive signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan operand for positive signal edge" instruction to determine if there is a change from "0" to "1" in the signal state of a specified operand (<Operand1>). The instruction compares the current signal state of <Operand1> with the signal state of the previous query saved in <Operand2>. If the instruction detects a change in the result of logic operation from "0" to "1", there is a positive, rising edge.

If a rising edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

Enter the operand to be queried (<Operand1>) in the operand placeholder above the instruction. Enter the edge memory bit (<Operand2>) in the operand placeholder below the instruction.

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand2> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand2> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand2> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand1> | Input | BOOL | Signal to be queried |
| <Operand2> | InOut | BOOL | Edge memory bit in which the signal state of the previous query is saved. |

##### Example

The following example shows how the instruction works:

![Example](images/93494415883_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when the following conditions are fulfilled:

- There is a rising edge at input "TagIn_1". The signal state of the previous query is saved at edge memory bit ""F_DB_1".Tag_M".
- The signal state of operand "TagIn_2" is "1".

#### --|N|--: Scan operand for negative signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan operand for negative signal edge" instruction to determine if there is a change form "1" to "0" in the signal state of a specified operand. The instruction compares the current signal state of <Operand1> with the signal state of the previous query saved in <Operand2>. If the instruction detects a change in the result of logic operation from "1" to "0", there is a negative, falling edge.

If a falling edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

Enter the operand to be queried (<Operand1>) in the operand placeholder above the instruction. Enter the edge memory bit (<Operand2>) in the operand placeholder below the instruction.

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand2> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand2> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand2> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand1> | Input | BOOL | Signal to be queried |
| <Operand2> | InOut | BOOL | Edge memory bit in which the signal state of the previous query is saved. |

##### Example

The following example shows how the instruction works:

![Example](images/93494419851_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when the following conditions are fulfilled:

- There is a falling edge at operand "TagIn_1". The signal state of the previous query is saved at edge memory bit ""F_DB_1".Tag_M".
- The signal state of operand "TagIn_2" is "1".

#### P_TRIG: Scan RLO for positive signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan RLO for positive signal edge" instruction to query a change in the signal state of the result of logic operation from "0" to "1". The instruction compares the current signal state of the result of logic operation (RLO) with the signal state of the previous query, which is saved in the edge bit memory (<Operand>). If the instruction detects a change in the RLO from "0" to "1", there is a positive, rising edge.

If a rising edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CLK | Input | BOOL | Current RLO |
| <Operand> | InOut | BOOL | Edge memory bit in which the RLO of the previous query is saved. |
| Q | Output | BOOL | Result of edge evaluation |

##### Example

The following example shows how the instruction works:

![Example](images/93494436619_DV_resource.Stream@PNG-de-DE.png)

The RLO from the previous bit logic operation is saved in edge memory bit ""F_DB_1".Tag_M". If a change in the RLO signal state from "0" to "1" is detected, the program jumps to jump label CAS1.

#### N_TRIG: Scan RLO for negative signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan RLO for negative signal edge" instruction to query a change in the signal state of the result of logic operation from "1" to "0". The instruction compares the current signal state of the result of logic operation with the signal state from the previous query, which is saved in the edge memory bit (<Operand>). If the instruction detects a change in the RLO from "1" to "0", there is a negative, falling edge.

If a falling edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CLK | Input | BOOL | Current RLO |
| <Operand> | InOut | BOOL | Edge memory bit in which the RLO of the previous query is saved. |
| Q | Output | BOOL | Result of edge evaluation |

##### Example

The following example shows how the instruction works:

![Example](images/93494440587_DV_resource.Stream@PNG-de-DE.png)

The RLO of the previous bit logic operation is saved in edge bit memory ""F_DB_1".Tag_M". If a change in the RLO signal state from "1" to "0" is detected, the program jumps to jump label CAS1.

### FBD

This section contains information on the following topics:

- [AND logic operation (STEP 7 Safety V19)](#and-logic-operation-step-7-safety-v19)
- [OR logic operation (STEP 7 Safety V19)](#or-logic-operation-step-7-safety-v19)
- [X: EXCLUSIVE OR logic operation (STEP 7 Safety V19)](#x-exclusive-or-logic-operation-step-7-safety-v19)
- [=: Assignment (STEP 7 Safety V19)](#assignment-step-7-safety-v19-1)
- [R: Reset output (STEP 7 Safety V19)](#r-reset-output-step-7-safety-v19)
- [S: Set output (STEP 7 Safety V19)](#s-set-output-step-7-safety-v19)
- [SR: Set/reset flip-flop (STEP 7 Safety V19)](#sr-setreset-flip-flop-step-7-safety-v19-1)
- [RS: Reset/set flip-flop (STEP 7 Safety V19)](#rs-resetset-flip-flop-step-7-safety-v19-1)
- [P: Scan operand for positive signal edge (STEP 7 Safety V19)](#p-scan-operand-for-positive-signal-edge-step-7-safety-v19)
- [N: Scan operand for negative signal edge (STEP 7 Safety V19)](#n-scan-operand-for-negative-signal-edge-step-7-safety-v19)
- [P_TRIG: Scan RLO for positive signal edge (STEP 7 Safety V19)](#p_trig-scan-rlo-for-positive-signal-edge-step-7-safety-v19-1)
- [N_TRIG: Scan RLO for negative signal edge (STEP 7 Safety V19)](#n_trig-scan-rlo-for-negative-signal-edge-step-7-safety-v19-1)

#### AND logic operation (STEP 7 Safety V19)

##### Description

You can use the "AND logic operation" instruction to query the signal states of two or more specified operands and evaluate them according to the AND truth table.

If the signal state of all the operands is "1", then the conditions are fulfilled and the instruction returns the result "1". If the signal state of one of the operands is "0", then the conditions are not fulfilled and the instruction generates the result "0".

If the "AND logic operation" instruction is the first instruction in a logic string, it saves the result of its signal state query in the RLO bit.

Each "AND logic operation" instruction that is not the first instruction in the logic string logically combines the result of its signal state query with the value saved in the RLO bit. This logical combination is performed according to the AND truth table.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | The operand indicates the bit whose signal state will be queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93495298315_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the signal state of operands "TagIn_1" and "TagIn_2" is "1".

##### AND truth table

The following table shows the results when linking two operands by an AND logic operation:

| Signal state of the first operand | Signal state of the second operand | Result of logic operation |
| --- | --- | --- |
| 1 | 1 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 0 | 0 | 0 |

---

**See also**

[Insert binary input (STEP 7 Safety V19)](#insert-binary-input-step-7-safety-v19)

#### OR logic operation (STEP 7 Safety V19)

##### Description

You can use the "OR logic operation" instruction to get the signal states of two or more specified operands and evaluate them according to the OR truth table.

If the signal state of at least one of the operands is "1", then the conditions are fulfilled and the instruction returns the result "1". If the signal state of all of the operands is "0", then the conditions are not fulfilled and the instruction generates the result "0".

If the "OR logic operation" instruction is the first instruction in a logic string, it saves the result of its signal state query in the RLO bit.

Each "OR logic operation" instruction that is not the first instruction in the logic string, logically combines the result of its signal state query with the value saved in the RLO bit. This logical combination is performed according to the OR truth table.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | The operand indicates the bit whose signal state will be queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93495302283_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the signal state of operand "TagIn_1" or "TagIn_2" is "1".

##### OR truth table

The following table shows the results when linking two operands by an OR logic operation:

| Signal state of the first operand | Signal state of the second operand | Result of logic operation |
| --- | --- | --- |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 0 | 0 | 0 |

---

**See also**

[Insert binary input (STEP 7 Safety V19)](#insert-binary-input-step-7-safety-v19)

#### X: EXCLUSIVE OR logic operation (STEP 7 Safety V19)

##### Description

You can use the "EXCLUSIVE OR logic operation" instruction to get the result of a signal state query according to the the EXCLUSIVE OR truth table.

With an "EXCLUSIVE OR logic operation" instruction, the signal state is "1" when the signal state of one of the two specified operands is "1". When more than two operands are queried, the overall result of logic operation is "1" if an odd-numbered quantity of queried operands returns the result "1".

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Input | BOOL | The operand indicates the bit whose signal state will be queried. |

##### Example

The following example shows how the instruction works:

![Example](images/93495499531_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the signal state of one of the two operands "TagIn_1" and "TagIn_2" is "1". When both operands have signal state "1" or "0" then output "TagOut" is reset.

##### EXCLUSIVE OR truth table

The following table shows the results when two operands are linked by an EXCLUSIVE OR:

| Signal state of the first operand | Signal state of the second operand | Result of logic operation |
| --- | --- | --- |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |
| 0 | 0 | 0 |

The following table shows the results when three operands are linked by an EXCLUSIVE OR:

| Signal state of the first operand | Signal state of the second operand | Signal state of the third operand | Result of logic operation |
| --- | --- | --- | --- |
| 1 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 0 | 0 | 0 | 0 |

---

**See also**

[Insert binary input (STEP 7 Safety V19)](#insert-binary-input-step-7-safety-v19)

#### =: Assignment (STEP 7 Safety V19)

##### Description

You can use the "Assignment" instruction to set the bit of a specified operand. If the result of logic operation (RLO) at the box input has signal state "1" or the box input for S7-1200/1500 F-CPUs is not connected, the specified operand is set to signal state "1". If the signal state at the box input is "0", the bit of the specified operand is reset to "0".

The instruction does not influence the RLO. The RLO at the box input is assigned directly to the operand located above the Assign box.

The "Assignment" instruction can be placed at any position in the logic operation sequence.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand to which the RLO is assigned. |

##### Example

The following example shows how the instruction works:

![Example](images/93495507467_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" at the output of the "Assignment" instruction is set when one of the following conditions is fulfilled:

- Inputs "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state at input "TagIn_3" is "0".

#### R: Reset output (STEP 7 Safety V19)

##### Description

You can use the "Reset output" instruction to reset the signal state of a specified operand to "0".

If the box input has signal state "1" or the box input for S7-1200/1500 F-CPUs is not connected, the specified operand is reset to "0". If there is a result of logic operation of "0" at the box input, the signal state of the specified operand remains unchanged.

The instruction does not influence the RLO. The RLO at the box input is transferred directly to the box output.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

> **Note**
>
> You cannot use the "process image of the inputs", "process image of the outputs" from standard I/O and "standard DB" and "bit memory" operand areas for the operands of the instruction.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand that is reset with RLO = "1". |

##### Example

The following example shows how the instruction works:

![Example](images/93497698059_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is reset when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state of operand "TagIn_3" is "0".

#### S: Set output (STEP 7 Safety V19)

##### Description

You can use the "Set output" instruction to set the signal state of a specified operand to "1".

If the box input has signal state "1" or the box input for S7-1200/1500 F-CPUs is not connected, the specified operand is set to "1". If there is a result of logic operation of "0" at the box input, the signal state of the specified operand remains unchanged.

The instruction does not influence the RLO. The RLO at the box input is transferred directly to the box output.

> **Note**
>
> The instruction is not executed if it is applied to an output of an F‑I/O that is passivated (e.g., during startup of the F‑system). Therefore, it is preferable to access outputs of the F-I/O using only the "Assignment" instruction.
>
> An F-I/O output is passivated if QBAD or QBAD_O_xx = 1 or value status = 0 is set in the corresponding F-I/O DB.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> If the operand area "local data (temp)" is used for the operands of the instruction, the local data bit used must be initialized beforehand.

> **Note**
>
> You cannot use the "process image of the inputs", "process image of the outputs" from standard I/O and "standard DB" and "bit memory" operand areas for the operands of the instruction.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand> | Output | BOOL | Operand that is set when RLO = "1". |

##### Example

The following example shows how the instruction works:

![Example](images/93497702027_DV_resource.Stream@PNG-de-DE.png)

Operand "TagOut" is set when one of the following conditions is fulfilled:

- Operands "TagIn_1" and "TagIn_2" have signal state "1".
- The signal state of operand "TagIn_3" is "0".

#### SR: Set/reset flip-flop (STEP 7 Safety V19)

##### Description

You can use the "Set/reset flip-flop" instruction to set or reset the bit of the specified operand based on the signal state of inputs S and R1. If the signal state at input S is "1" and the signal state at input R1 is "0", the specified operand is set to "1". If the signal state at input S is "0" and the signal state at input R1 is "1", the specified operand is reset to "0".

Input R1 takes priority over input S. If the signal state is "1" at the two inputs S and R1, the signal state of the specified operand is reset to "0".

The instruction is not executed if the signal state at the two inputs S and R1 is "0". The signal state of the operand then remains unchanged.

The current signal state of the operand is transferred to output Q and can be queried there.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the operands of the instruction.
>
> If the operand area "local data (temp)" is used for the edge bit memory of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| S | Input | BOOL | Enable set |
| R1 | Input | BOOL | Enable reset |
| <Operand> | Output | BOOL | Operand that is set or reset. |
| Q | Output | BOOL | Signal state of the operand |

##### Example

The following example shows how the instruction works:

![Example](images/102645389835_DV_resource.Stream@PNG-de-DE.png)

Operands ""F_DB_1".TagSR" and "TagOut" are set when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "1".
- Operand "TagIn_2" has signal state "0".

Operands ""F_DB_1".TagSR" and "TagOut" are reset when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "0" and operand "TagIn_2" has signal state "1".
- Both operands "TagIn_1" and "TagIn_2" have signal state "1".

#### RS: Reset/set flip-flop (STEP 7 Safety V19)

##### Description

You can use the "Reset/set flip-flop" instruction to reset or set the bit of the specified operand based on the signal state of inputs R and S1. When the signal state is "1" at input R and "0" at input S1, the specified operand is reset to "0". When the signal state is "0" at input R and "1" at input S1, the specified operand is set to "1".

Input S1 takes priority over input R. If the signal state is "1" at the two inputs R and S1, the signal state of the specified operand is set to "1".

The instruction is not executed if the signal state at the two inputs R and S1 is "0". The signal state of the operand then remains unchanged.

The current signal state of the operand is transferred to output Q and can be queried there.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the operand of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the operands of the instruction.
>
> If the operand area "local data (temp)" is used for the edge bit memory of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| R | Input | BOOL | Enable reset |
| S1 | Input | BOOL | Enable set |
| <Operand> | Output | BOOL | Operand that is reset or set. |
| Q | Output | BOOL | Signal state of the operand |

##### Example

The following example shows how the instruction works:

![Example](images/102645393675_DV_resource.Stream@PNG-de-DE.png)

Operands ""F_DB_1".TagRS" and "TagOut" are reset when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "1".
- Operand "TagIn_2" has signal state "0".

Operands ""F_DB_1".TagRS" and "TagOut" are set when the following conditions are fulfilled:

- Operand "TagIn_1" has signal state "0" and operand "TagIn_2" has signal state "1".
- Operands "TagIn_1" and "TagIn_2" have signal state "1".

#### P: Scan operand for positive signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan operand for positive signal edge" instruction to determine if there is a change from "0" to "1" in the signal state of a specified operand (<Operand1>). The instruction compares the current signal state of <Operand1> with the signal state of the previous query saved in <Operand2>. If the instruction detects a change in the result of logic operation from "0" to "1", there is a positive, rising edge.

If a rising edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

Enter the operand to be queried (<Operand1>) in the operand placeholder above the instruction. Enter the edge memory bit (<Operand2>) in the operand placeholder below the instruction.

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand2> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand2> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand2> of the instruction, the local data bit used must be initialized beforehand.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand1> | Input | BOOL | Signal to be queried |
| <Operand2> | InOut | BOOL | Edge memory bit in which the signal state of the previous query is saved. |

##### Example

The following example shows how the instruction works:

![Example](images/93498717963_DV_resource.Stream@PNG-de-DE.png)

"TagOut" is set when the following conditions are fulfilled:

- There is a rising edge at input "TagIn_1".
- The signal state of operand "TagIn_2" is "1".

#### N: Scan operand for negative signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan operand for negative signal edge" instruction to determine if there is a change form "1" to "0" in the signal state of a specified operand. The instruction compares the current signal state of <Operand1> with the signal state of the previous query saved in <Operand2>. If the instruction detects a change in the result of logic operation from "1" to "0", there is a negative, falling edge.

If a falling edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

Enter the operand to be queried (<Operand1>) in the operand placeholder above the instruction. Enter the edge memory bit (<Operand2>) in the operand placeholder below the instruction.

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand2> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand2> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand2> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Operand1> | Input | BOOL | Signal to be queried |
| <Operand2> | InOut | BOOL | Edge memory bit in which the signal state of the previous query is saved. |

##### Example

The following example shows how the instruction works:

![Example](images/93498734731_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- There is a falling edge at input "TagIn_1".
- The signal state of operand "TagIn_2" is "1".

#### P_TRIG: Scan RLO for positive signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan RLO for positive signal edge" instruction to query a change in the signal state of the result of logic operation from "0" to "1". The instruction compares the current signal state of the result of logic operation with the signal state from the previous query, which is saved in the edge memory bit (<Operand>). If the instruction detects a change in the RLO from "0" to "1", there is a positive, rising edge.

If a rising edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CLK | Input | BOOL | Current RLO |
| <Operand> | InOut | BOOL | Edge memory bit in which the RLO of the previous query is saved. |
| Q | Output | BOOL | Result of edge evaluation |

##### Example

The following example shows how the instruction works:

![Example](images/93498746635_DV_resource.Stream@PNG-de-DE.png)

The RLO from the previous bit logic operation is saved in edge memory bit ""F_DB_1".Tag_M". If a change in the RLO signal state from "0" to "1" is detected, the program jumps to jump label CAS1.

#### N_TRIG: Scan RLO for negative signal edge (STEP 7 Safety V19)

##### Description

You can use the "Scan RLO for negative signal edge" instruction to query a change in the signal state of the result of logic operation from "1" to "0". The instruction compares the current signal state of the result of logic operation with the signal state from the previous query, which is saved in the edge memory bit (<Operand>). If the instruction detects a change in the RLO from "1" to "0", there is a negative, falling edge.

If a falling edge is detected, the output of the instruction has signal state "1". In all other cases, the signal state at the output of the instruction is "0".

> **Note**
>
> The address of the edge memory bit must not be used more than once in the program, otherwise the edge memory bit would be overwritten. This would influence edge evaluation and the result would no longer be unequivocal.

> **Note**
>
> If you want to use a formal parameter of an F‑FC for the edge memory bit <Operand> of the instruction, it must be declared as an input/output parameter.

> **Note**
>
> You cannot use the "process image", "standard DB" and "bit memory" operand areas for the edge memory bit <Operand> of the instruction.
>
> If operand area "local data (temp)" is used for the edge memory bit <Operand> of the instruction, the local data bit used must be initialized beforehand.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CLK | Input | BOOL | Current RLO |
| <Operand> | InOut | BOOL | Edge memory bit in which the RLO of the previous query is saved. |
| Q | Output | BOOL | Result of edge evaluation |

##### Example

The following example shows how the instruction works:

![Example](images/93498865803_DV_resource.Stream@PNG-de-DE.png)

The RLO of the previous bit logic operation is saved in edge bit memory ""F_DB_1".Tag_M". If a change in the RLO signal state from "1" to "0" is detected, the program jumps to jump label CAS1.

## Safety functions

This section contains information on the following topics:

- [ESTOP1: Emergency STOP/OFF up to stop category 1 (STEP 7 Safety V19)](#estop1-emergency-stopoff-up-to-stop-category-1-step-7-safety-v19)
- [TWO_HAND: Two-hand monitoring (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#two_hand-two-hand-monitoring-step-7-safety-advanced-v19-s7-300-s7-400)
- [TWO_H_EN: Two-hand monitoring with enable (STEP 7 Safety V19)](#two_h_en-two-hand-monitoring-with-enable-step-7-safety-v19)
- [MUTING: Muting (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#muting-muting-step-7-safety-advanced-v19-s7-300-s7-400)
- [MUT_P: Parallel muting (STEP 7 Safety V19)](#mut_p-parallel-muting-step-7-safety-v19)
- [EV1oo2DI: 1oo2 evaluation with discrepancy analysis (STEP 7 Safety V19)](#ev1oo2di-1oo2-evaluation-with-discrepancy-analysis-step-7-safety-v19)
- [FDBACK: Feedback circuit monitoring (STEP 7 Safety V19)](#fdback-feedback-circuit-monitoring-step-7-safety-v19)
- [SFDOOR: Protective door monitoring (STEP 7 Safety V19)](#sfdoor-protective-door-monitoring-step-7-safety-v19)
- [ACK_GL: Global acknowledgment of all F-I/O in an F-runtime group (STEP 7 Safety V19)](#ack_gl-global-acknowledgment-of-all-f-io-in-an-f-runtime-group-step-7-safety-v19)

### ESTOP1: Emergency STOP/OFF up to stop category 1 (STEP 7 Safety V19)

#### Description

This instruction supports the implementation of an EMERGENCY STOP/EMERGENCY OFF shutdown with acknowledgment for STOP categories 0 and 1 for the purpose of complying with requirements of IEC 60204 or IEC 61800-5-2. However, additional measures described in the respective standard may have to be taken in order to fully comply with the requirements of the respective standard.

Enable signal Q is reset to 0, as soon as input E_STOP takes a signal state of 0 (Stop category 0). Enable signal Q_DELAY is reset to 0 after the time delay set at input TIME_DEL (Stop Category 1).

Enable signal Q is reset to 1 not before input E_STOP takes a signal state of 1 and an acknowledgment occurs. The acknowledgment for the enable takes place according to the parameter assignment at input ACK_NEC:

- If ACK_NEC = 0, the acknowledgment is automatic.
- If ACK_NEC = 1, you must use a rising edge at input ACK for acknowledging the enable.

Output ACK_REQ is used to signal that a user acknowledgment is required at input ACK for the acknowledgment. The instruction sets output ACK_REQ to 1, as soon as input E_STOP = 1.

Following an acknowledgment, the instruction resets ACK_REQ to 0.

Every call of the "Emergency STOP/Emergency OFF up to Stop Category 1" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., ESTOP1_DB_1) or a multi-instance (e.g., ESTOP1_Instance_1) for the "Emergency STOP/Emergency OFF up to Stop Category 1" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The ACK_NEC tag must not be assigned a value of "0" unless an automatic restart of the affected process is otherwise excluded. (S033) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

**Note:** In case of two channels according to category 3.4 of ISO 13849-1:2015 or EN ISO 13849-1:2015, the discrepancy monitoring of the two NC contacts of the EMERGENCY STOP/EMERGENCY OFF must already take place in the F-I/O. The F-I/O has to be configured accordingly (sensor evaluation: two-channel, equivalent), and the result of the evaluation interconnected with the E_STOP input. In order to keep the discrepancy time from influencing the response time, you must assign "Supply value 0" for the behavior of discrepancy during configuration.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| E_STOP | Input | BOOL | EMERGENCY STOP/EMERGENCY OFF |
| ACK_NEC | Input | BOOL | 1=Acknowledgment necessary |
| ACK | Input | BOOL | 1=Acknowledgment |
| TIME_DEL | Input | TIME | Time delay |
| Q | Output | BOOL | 1=Enable |
| Q_DELAY | Output | BOOL | Enable is OFF delayed |
| ACK_REQ | Output | BOOL | 1=Acknowledgment necessary |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | Version 1.0 requires that the F_TOF block with the number FB 186 is available in the project tree in the "Program blocks/System blocks/STEP 7 Safety" folder.   When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically. If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. You will then avoid number conflicts. |
| 1.1 | x | — | -— | These versions have identical functions to version 1.0, but do not require the F_TOF block to have a particular number. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | o | o |  |
| 1.5 | x | x | x |  |
| 1.6 | x | x | x | The reaction of the delay time TIME_DEL for F-CPUs S7-1200/1500 was adapted to the reaction of F-CPUs S7-300/400: If the input ESTOP (0 -> 1 (including acknowledgment) -> 0) is changed while the delay time is running, the delay time is restarted. |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Startup behavior

After an F-system startup, when ACK_NEC = 1, you must acknowledge the instruction using a rising edge at input ACK.

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits 4 and 5 are saved until you acknowledge at the ACK input.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Incorrect TIM_DEL setting | Time delay setting < 0 | Set time delay > 0 |
| Bit 1 | Reserved | — | — |
| Bit 2 | Reserved | — | — |
| Bit 3 | Reserved | — | — |
| Bit 4 | Acknowledgment not possible because emergency STOP/emergency OFF is still active | Emergency STOP/Emergency OFF pushbutton is locked | Release Emergency STOP/Emergency OFF pushbutton |
| F‑I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F‑I/O of emergency STOP/emergency OFF pushbutton | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Emergency STOP/Emergency OFF pushbutton is defective | Check emergency STOP/emergency OFF pushbutton |  |  |
| Wiring fault | Check wiring of the emergency STOP/emergency OFF pushbutton |  |  |
| Bit 5 | If enable is missing: input ACK has a permanent signal state of 1 | Acknowledgment button defective | Check acknowledgment button |
| Wiring fault | Check wiring of acknowledgment button |  |  |
| Bit 6 | Acknowledgment required (= state of ACK_REQ) | — | — |
| Bit 7 | State of output Q | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95099509515_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95099530123_DV_resource.Stream@PNG-de-DE.png)

### TWO_HAND: Two-hand monitoring (STEP 7 Safety Advanced V19) (S7-300, S7-400)

#### Description

This instruction supports the implementation of two-hand monitoring for the purpose of complying with requirements of ISO 13851. However, additional measures described in the standard may have to be taken in order to fully comply with the requirements of the standard.

> **Note**
>
> This instruction is only available for S7-300 and S7-400 F-CPUs. For S7-1200/1500 F-CPUs, you use the instruction "Two-hand monitoring with enable". The application "Two-hand monitoring with enable" replaces the instruction "Two-hand monitoring" with compatible functions.

If pushbuttons IN1 and IN2 are activated within the permitted discrepancy time DISCTIME ≤ 500 ms (IN1/IN2 = 1) (synchronous activation), output signal Q is set to 1. If the time difference between activation of pushbutton IN1 and pushbutton IN2 is greater than DISCTIME, then the pushbuttons must be released and reactivated.

Q is reset to 0 as soon as one of the pushbuttons is released (IN1/IN2 = 0). Enable signal Q can be reset to 1 only if the other pushbutton has been released, and if both pushbuttons are then reactivated within the discrepancy time. Enable signal Q can never be set to 1 if the discrepancy time is set to values less than 0 or greater than 500 ms.

Every call of the "Two-hand monitoring" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., TWO_HAND_DB_1) or a multi-instance (e.g., TWO_HAND_Instance_1) for the "Two-hand monitoring" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

**Note:** Only one signal per pushbutton can be evaluated in the instruction. Discrepancy monitoring of the NC and NO contacts of pushbuttons IN1 and IN2 is performed directly during suitable configuration (sensor evaluation: 1oo2 evaluation, non-equivalent) directly through the F‑I/O with inputs. The normally open contact must be wired in such a way that it supplies the useful signal (see manual for the F-I/O you are using). In order to keep the discrepancy time from influencing the response time, you must assign "Supply value 0" for the behavior of discrepancy during configuration. If a discrepancy is detected, a fail-safe value of 0 is entered in the process image of the inputs (PII) for the pushbutton and QBAD or QBAD_I_xx = 1 is set in the relevant F-I/O DB. (See also [F-I/O access](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#f-io-access))

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | BOOL | Pushbutton 1 |
| IN2 | Input | BOOL | Pushbutton 2 |
| DISCTIME | Input | TIME | Discrepancy time (0 to 500 ms) |
| Q | Output | BOOL | 1=Enable |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95099563787_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95099840395_DV_resource.Stream@PNG-de-DE.png)

### TWO_H_EN: Two-hand monitoring with enable (STEP 7 Safety V19)

#### Description

This instruction supports the implementation of two-hand monitoring with enable for the purpose of complying with requirements of ISO 13851. However, additional measures described in the standard may have to be taken in order to fully comply with the requirements of the standard.

If pushbuttons IN1 and IN2 are activated within the permitted discrepancy time DISCTIME ≤ 500 ms (IN1/IN2 = 1) (synchronous activation), output signal Q is set to 1 when existing ENABLE = 1. If the time difference between activation of pushbutton IN1 and pushbutton IN2 is greater than DISCTIME, then the pushbuttons must be released and reactivated.

Q is reset to 0 as soon as one of the pushbuttons is released (IN1/IN 2 = 0) or ENABLE = 0. Enable signal Q can be reset to 1 only if the other pushbutton has been released, and if both pushbuttons are then reactivated within the discrepancy time when existing ENABLE = 1.

Every call of the "Two-hand monitoring with enable" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., TWO_H_EN_DB_1) or a multi-instance (e.g., TWO_H_EN_Instance_1) for the "Two-hand monitoring with enable" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

**Note:** Only one signal per pushbutton can be evaluated in the instruction. Discrepancy monitoring of the NC and NO contacts of pushbuttons IN1 and IN2 is performed directly during suitable configuration (sensor evaluation: 1oo2 evaluation, non-equivalent) directly through the F‑I/O with inputs. The normally open contact must be wired in such a way that it supplies the useful signal (see manual for the F-I/O you are using). In order to keep the discrepancy time from influencing the response time, during the configuration of discrepancy behavior, you must configure "Supply value 0".

If a discrepancy is detected, a fail-safe value of 0 is entered in the process image of the inputs (PII) for the pushbutton and QBAD or QBAD_I_xx = 1 or respectively value status = 0 is set in the relevant F-I/O DB.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | BOOL | Pushbutton 1 |
| IN2 | Input | BOOL | Pushbutton 2 |
| ENABLE | Input | BOOL | Enable input |
| DISCTIME | Input | TIME | Discrepancy time (0 to 500 ms)  For productive use, select a discrepancy time > 0 ms. |
| Q | Output | BOOL | 1=Enable |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits 0 to 5 are saved until the cause of the error has been eliminated.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Incorrect discrepancy time DISCTIME setting | Discrepancy time setting is <0 or > 500 ms | Set discrepancy time in range of 0 to 500 ms |
| Bit 1 | Discrepancy time elapsed | Discrepancy time setting is too low | If necessary, set a higher discrepancy time |
| Pushbuttons were not activated within the discrepancy time | Release pushbuttons and activate them within the discrepancy time |  |  |
| Wiring fault | Check wiring of pushbuttons |  |  |
| Pushbuttons defective | Check pushbuttons |  |  |
| Pushbuttons are wired to different F-I/O, and F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON on an F-I/O | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Bit 2 | Reserved | — | — |
| Bit 3 | Reserved | — | — |
| Bit 4 | Incorrect activation sequence | One pushbutton was not released | Release pushbuttons and activate them within the discrepancy time |
| Pushbuttons defective | Check pushbuttons |  |  |
| Bit 5 | ENABLE does not exist | ENABLE = 0 | Set ENABLE = 1, release pushbutton and activate it within the discrepancy time |
| Bit 6 | Reserved | — | — |
| Bit 7 | State of output Q | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95100148875_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95100195339_DV_resource.Stream@PNG-de-DE.png)

### MUTING: Muting (STEP 7 Safety Advanced V19) (S7-300, S7-400)

#### Description

This instruction performs parallel muting with two or four muting sensors.

> **Note**
>
> This instruction is only available for S7-300 and S7-400 F-CPUs. For S7-1200/1500 F-CPUs, you use the instruction "[Parallel muting](#mut_p-parallel-muting-step-7-safety-v19)". The instruction "Parallel muting" replaces the instruction "Muting" with compatible functions.

Muting is a defined suppression of the protective function of light curtains. Light curtain muting can be used to introduce goods or objects into the danger area monitored by the light curtain without causing the machine to stop.

To utilize the muting function, at least two independently wired muting sensors must be present. The use of two or four muting sensors and correct integration into the production sequence must ensure that no persons enter the danger area while the light curtain is muted.

Every call of the "Muting" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., MUTING_DB_1) or a multi-instance (e.g., MUTING_Instance_1) for the "Muting" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| MS_11 | Input | BOOL | Muting sensor 1 of sensor pair 1 |
| MS_12 | Input | BOOL | Muting sensor 2 of sensor pair 1 |
| MS_21 | Input | BOOL | Muting sensor 1 of sensor pair 2 |
| MS_22 | Input | BOOL | Muting sensor 2 of sensor pair 2 |
| STOP | Input | BOOL | 1=Conveyor system stopped |
| FREE | Input | BOOL | 1=Light curtain uninterrupted |
| QBAD_MUT | Input | BOOL | QBAD signal of the F-I/O or QBAD_O_xx signal of the muting lamp channel |
| DISCTIM1 | Input | TIME | Discrepancy time of sensor pair 1 (0 to 3 s) |
| DISCTIM2 | Input | TIME | Discrepancy time of sensor pair 2 (0 to 3 s) |
| TIME_MAX | Input | TIME | Maximum muting time (0 to 10 min) |
| ACK | Input | BOOL | Acknowledgment of restart inhibit |
| Q | Output | BOOL | 1= Enable, not off |
| MUTING | Output | BOOL | Display of muting is active |
| ACK_REQ | Output | BOOL | Acknowledgment necessary |
| FAULT | Output | BOOL | Group error |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)

![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657067915_DV_resource.Stream@PNG-en-US.png)

- If both muting sensors MS_11 and MS_12 are activated by the product within DISCTIM1 (apply signal state = 1), the instruction starts the MUTING function. Enable signal Q remains 1, even when input FREE = 0 (light curtain interrupted by product). The MUTING output for setting the muting lamp switches to 1.

  > **Note**
  >
  > The muting lamp can be monitored using the QBAD_MUT input. To do this, you must wire the muting lamp to an output with wire break monitoring of an F-I/O and supply the QBAD_MUT input with the QBAD signal of the associated F-I/O or the QBAD_O_xx signal of the associated channel. If QBAD_MUT = 1, muting is terminated by the instruction. If monitoring of the muting lamp is not necessary, you do not have to supply input QBAD_MUT.
  >
  > F‑I/O that can promptly detect a wire break after activation of the muting operation must be used (see manual for specific F‑I/O).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657200651_DV_resource.Stream@PNG-en-US.png)
- As long as both muting sensors MS_11 and MS_12 continue to be activated, the MUTING function of the instruction causes Q to remain 1 and MUTING to remain 1 (so that the product can pass through the light curtain without causing the machine to stop).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657451403_DV_resource.Stream@PNG-en-US.png)
- The two muting sensors MS_21 and MS_22 must be activated (within DISCTIM2) before muting sensors MS_11 and MS_12 are switched to inactive (apply signal state 0). In this way, the instruction retains the MUTING function. (Q = 1, MUTING = 1).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166659404555_DV_resource.Stream@PNG-en-US.png)
- Only if one of the two muting sensors MS_21 and MS_22 is switched to inactive (product enables sensors) is the MUTING function terminated (Q = 1, MUTING = 0). The maximum activation time for the MUTING function is the time set at input TIME_MAX.

  > **Note**
  >
  > The MUTING function is also started if the product passes the light curtain in the reverse direction and the muting sensors are thus activated by the product in reverse order.

#### Timing diagrams for error-free muting procedure with 4 muting sensors

![Timing diagrams for error-free muting procedure with 4 muting sensors](images/166667233931_DV_resource.Stream@PNG-de-DE.png)

#### Schematic sequence of muting procedure with reflection light barriers

If reflection light barriers are used as muting sensors, they are generally arranged diagonally.

In general, this arrangement of reflection light barriers as muting sensors requires only two light barriers, and only MS_11 and MS_12 are interconnected.

The sequence is similar to that of the muting procedure with 4 muting sensors. Step 3 is omitted. In step 4, replace MS_21 and MS_22 with MS_11 and MS_12, respectively.

![Schematic sequence of muting procedure with reflection light barriers](images/166656509963_DV_resource.Stream@PNG-en-US.png)

#### Restart inhibit upon interruption of light curtain (if MUTING is not active), when errors occur, and during F-system startup

Enable signal Q cannot be set to 1 or becomes 0, if:

- Light curtain is interrupted (e.g., by a person or material transport) while the MUTING function is not active
- The muting lamp monitoring function responds at input QBAD_MUT
- Sensor pair 1 (MS_11 and MS_12) or sensor pair 2 (MS_21 and MS_22) is not activated or deactivated during discrepancy time DISCTIM1 or DISCTIM2, respectively
- The MUTING function is active longer than the maximum muting time TIME_MAX
- Discrepancy times DISCTIM1 and DISCTIM2 have been set to values < 0 or > 3 s
- Maximum muting time TIME_MAX has been set to a value< 0 or > 10 min

In the identified cases, output FAULT (group error) is set to 1 (restart inhibit). If the MUTING function is started, it will be terminated and the Muting output becomes 0.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When a valid combination of signal states of muting sensors is immediately detected at startup of the F‑system (for example, because the muting sensors are interconnected to inputs of a standard I/O that immediately provide process values during the F‑system startup), the MUTING function is immediately started and the MUTING output and enable signal Q are set to 1. The FAULT output (group error) is not set to 1 (no restart inhibit!). (S035) |  |

#### Acknowledgment of restart inhibit

Enable signal Q becomes 1 again, when:

- The light curtain is no longer interrupted
- If present, errors are eliminated (see output DIAG)

  and
- A user acknowledgment with positive edge occurs at input ACK (see also [Implementation of user acknowledgment](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementation-of-user-acknowledgment)).

The FAULT output is set to 0. Output ACK_REQ = 1 signals that user acknowledgment at input ACK is required to eliminate the restart inhibit. The instruction sets ACK-REQ = 1 as soon as the light curtain is no longer interrupted or errors have been eliminated. Once acknowledgment has occurred, the instruction resets ACK_REQ to 0.

> **Note**
>
> Following discrepancy errors and once the maximum muting time has been exceeded, ACK_REQ is immediately set to 1. As soon as a user acknowledgment has taken place at input ACK, discrepancy times DISCTIM1 and DISCTIM2 and maximum muting time TIME_MAX are reset.

#### Timing diagrams for discrepancy errors at sensor pair 1 or interruption of the light curtain (if MUTING is not active)

![Timing diagrams for discrepancy errors at sensor pair 1 or interruption of the light curtain (if MUTING is not active)](images/166667166603_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Sensor pair 1 (MS_11 and MS_12) is not activated within discrepancy time DISCTIM1. |
| ② | The light curtain is interrupted even though the MUTING function is not active. |
| ③ | Acknowledgment |

#### Behavior with stopped conveyor equipment

If, while the conveyor equipment has stopped, the monitoring for one of the following reasons is to be deactivated:

- To comply with discrepancy time DISCTIM1 or DISCTIM2
- To comply with maximum muting time TIME_MAX

You must supply input STOP with a "1" signal for as long as the conveyor equipment is stopped. As soon as the conveyor equipment is running again (STOP = 0), discrepancy times DISCTIM1 and DISCTIM2 and maximum muting time TIME_MAX are reset.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When STOP = 1, the discrepancy monitoring is shut down. During this time, if inputs MSx1/MSx2 of a sensor pair both take a signal state of 1 due to an undetected error, for example, because both muting sensors have adopted signal state 1 in the event of an error, the fault is not detected and the MUTING function can be started unintentionally. (S036) |  |

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits are saved until acknowledgment at input ACK.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Discrepancy error or incorrect discrepancy time DISCTIM 1 setting for sensor pair 1 | Malfunction in production sequence | Malfunction in production sequence eliminated |
| Sensor defective | Check sensors |  |  |
| Wiring fault | Check wiring of sensors |  |  |
| Sensors are wired to different F-I/O, and F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON on an F-I/O | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Discrepancy time setting is too low | If necessary, set a higher discrepancy time |  |  |
| Discrepancy time setting is < 0 s or > 3 s | Set discrepancy time in range between 0 s and 3 s |  |  |
| Bit 1 | Discrepancy error or incorrect discrepancy time DISCTIM 2 setting for sensor pair 2 | Same as Bit 0 | Same as Bit 0 |
| Bit 2 | Maximum muting time exceeded or incorrect muting time TIME_MAX setting | Malfunction in production sequence | Malfunction in production sequence eliminated |
| Maximum muting time setting is too low | If necessary, set a higher maximum muting time |  |  |
| Muting time setting is < 0 s or > 10 min | Set muting time in range from 0 s to 10 min |  |  |
| Bit 3 | Light curtain interrupted and muting not active | Light curtain is defective | Check light curtain |
| Wiring fault | Check wiring of light curtain (FREE input) |  |  |
| F‑I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F‑I/O of light curtain (FREE input) | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| See other DIAG bits |  |  |  |
| Bit 4 | Muting lamp is defective or cannot be set | Muting lamp is defective | Replace muting lamp |
| Wiring fault | Check wiring of muting lamp |  |  |
| F‑I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F‑I/O of muting lamp | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Bit 5 | Reserved | — | — |
| Bit 6 | Reserved | — | — |
| Bit 7 | Reserved | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95100451083_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95100458891_DV_resource.Stream@PNG-de-DE.png)

### MUT_P: Parallel muting (STEP 7 Safety V19)

#### Description

This instruction performs parallel muting with two or four muting sensors.

Muting is a defined suppression of the protective function of light curtains. Light curtain muting can be used to introduce goods or objects into the danger area monitored by the light curtain without causing the machine to stop.

To utilize the muting function, at least two independently wired muting sensors must be present. The use of two or four muting sensors and correct integration into the production sequence must ensure that no persons enter the danger area while the light curtain is muted.

Every call of the "Parallel muting" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., MUT_P_DB_1) or a multi-instance (e.g., MUT_P_Instance_1) for the "Parallel muting" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| MS_11 | Input | BOOL | Muting sensor 11 |
| MS_12 | Input | BOOL | Muting sensor 12 |
| MS_21 | Input | BOOL | Muting sensor 21 |
| MS_22 | Input | BOOL | Muting sensor 22 |
| STOP | Input | BOOL | 1=Conveyor system stopped |
| FREE | Input | BOOL | 1=Light curtain uninterrupted |
| ENABLE | Input | BOOL | 1=Enable MUTING |
| QBAD_MUT | Input | BOOL | QBAD signal of the F-I/O or QBAD_O_xx signal / inverted value status of the muting lamp channel |
| ACK | Input | BOOL | Acknowledgment of restart inhibit |
| DISCTIM1 | Input | TIME | Discrepancy time of sensor pair 1 (0 to 3 s) |
| DISCTIM2 | Input | TIME | Discrepancy time of sensor pair 2 (0 to 3 s) |
| TIME_MAX | Input | TIME | Maximum muting time (0 to 10 min) |
| Q | Output | BOOL | 1= Enable, not off |
| MUTING | Output | BOOL | Display of muting is active |
| ACK_REQ | Output | BOOL | Acknowledgment necessary |
| FAULT | Output | BOOL | Group error |
| DIAG | Output | WORD | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x* | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x* | — | — | These versions have identical functions to version 1.0.   The output DIAG can now be correctly interconnected with the operand of data type WORD. |
| 1.2 | x* | — | o |  |
| 1.3 | x* | o | o |  |
| 1.4 | x | x | x |  |
| o This version is no longer supported.  * S7-300/400: When a restart inhibit (output FAULT = 1) and ENABLE = 1 is present, output ACK_REQ is set to 1 even if not at least one muting sensor is activated. Use the DIAG bits 5 and 6 for more information. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)

![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657067915_DV_resource.Stream@PNG-en-US.png)

- If muting sensors MS_11 and MS_12 are both activated by the product within DISCTIM1 (apply signal state = 1) and MUTING is enabled by setting the ENABLE input to 1, the instruction starts the MUTING function. Enable signal Q remains 1, even when input FREE = 0 (light curtain interrupted by product). The MUTING output for setting the muting lamp switches to 1.

  > **Note**
  >
  > The muting lamp can be monitored using the QBAD_MUT input. To do this, you must wire the muting lamp to an output with wire break monitoring of an F-I/O and supply the QBAD_MUT input with the QBAD signal of the associated F-I/O or the QBAD_O_xx signal / with inverted value statues of the associated channel. If QBAD_MUT = 1, muting is terminated by the instruction. If monitoring of the muting lamp is not necessary, you do not have to supply input QBAD_MUT.
  >
  > F‑I/O that can promptly detect a wire break after activation of the muting operation must be used (see manual for specific F‑I/O).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657200651_DV_resource.Stream@PNG-en-US.png)
- As long as both muting sensors MS_11 and MS_12 continue to be activated, the MUTING function of the instruction causes Q to remain 1 and MUTING to remain 1 (so that the product can pass through the light curtain without causing the machine to stop). Each of the two muting sensors MS_11 and MS_12 may be switched to inactive (t < DISCTIM1) for a short time (apply signal state 0).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166657451403_DV_resource.Stream@PNG-en-US.png)
- Muting sensors MS_21 and MS_22 must both be activated (within DISCTIM2) before muting sensors MS_11 and MS_12 are switched to inactive (apply signal state 0). In this way, the instruction retains the MUTING function. (Q = 1, MUTING = 1).

  ![Schematic sequence of error-free muting procedure with 4 muting sensors (MS_11, MS_12, MS_21, MS_22)](images/166659404555_DV_resource.Stream@PNG-en-US.png)

Only if muting sensors MS_21 and MS_22 are both switched to inactive (product enables sensors) is the MUTING function terminated (Q = 1, MUTING = 0). The maximum activation time for the MUTING function is the time set at input TIME_MAX.

> **Note**
>
> The MUTING function is also started if the product passes the light curtain in the reverse direction and the muting sensors are thus activated by the product in reverse order.

#### Timing diagrams for error-free muting procedure with 4 muting sensors

![Timing diagrams for error-free muting procedure with 4 muting sensors](images/166667670411_DV_resource.Stream@PNG-de-DE.png)

#### Schematic sequence of muting procedure with reflection light barriers

If reflection light barriers are used as muting sensors, they are generally arranged diagonally.

In general, this arrangement of reflection light barriers as muting sensors requires only two light barriers, and only MS_11 and MS_12 are interconnected.

The sequence is similar to that of the muting procedure with 4 muting sensors. Step 3 is omitted. In step 4, replace MS_21 and MS_22 with MS_11 and MS_12, respectively.

![Schematic sequence of muting procedure with reflection light barriers](images/166656509963_DV_resource.Stream@PNG-en-US.png)

#### Restart inhibit upon interruption of light curtain (MUTING is not active), as well as when errors occur and during F-system startup

Enable signal Q cannot be set to 1 or becomes 0, if:

- Light curtain is interrupted (e.g., by a person or material transport) while the MUTING function is not active
- Light curtain is (being) interrupted and the muting lamp monitoring at input QBAD_MUT is set to 1
- Light curtain is (being) interrupted and the MUTING function is not enabled by setting input ENABLE to 1
- Sensor pair 1 (MS_11 and MS_12) or sensor pair 2 (MS_21 and MS_22) is not activated or deactivated during discrepancy time DISCTIM1 or DISCTIM2, respectively
- The MUTING function is active longer than the maximum muting time TIME_MAX
- Discrepancy times DISCTIM1 and DISCTIM2 have been set to values < 0 or > 3 s
- Maximum muting time TIME_MAX has been set to a value< 0 or > 10 min
- The F-system starts up (regardless of whether or not the light curtain is interrupted, because the F-I/O is passivated after F-system startup and, thus, the FREE input is initially supplied with 0)

In the identified cases, output FAULT (group error) is set to 1 (restart inhibit). If the MUTING function is started, it will be terminated and the Muting output becomes 0.

#### User acknowledgment of restart inhibit (no muting sensor is activated or ENABLE = 0)

Enable signal Q becomes 1 again, when:

- The light curtain is no longer interrupted
- If present, errors are eliminated (see output DIAG)

  and
- A user acknowledgment with positive edge occurs at input ACK (see also [Implementation of user acknowledgment](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementation-of-user-acknowledgment)).

The FAULT output is set to 0. Output ACK_REQ = 1 (and DIAG bit 6) signals that user acknowledgment at input ACK is required to eliminate the restart inhibit. The instruction sets ACK_REQ = 1 as soon as the light curtain is no longer interrupted or the errors have been eliminated. Once acknowledgment has occurred, the instruction resets ACK_REQ to 0.

#### User Acknowledgment of restart inhibit (at least one muting sensor is activated and ENABLE = 1)

Enable signal Q becomes 1 again, when:

- If present, errors are eliminated (see output DIAG)
- FREE function occurs until a valid combination of muting sensors is detected

The FAULT output is set to 0. The MUTING function is restarted, if necessary, and the MUTING output becomes 1 if a valid combination of muting sensors is detected. When ENABLE = 1, output ACK_REQ = 1 (and DIAG-Bit 5) signals that FREE function is necessary for error elimination and for removal of the restart inhibit. Once FREE function has occurred successfully, the instruction resets ACK_REQ to 0.

> **Note**
>
> Once the maximum muting time is exceeded, TIME_MAX is reset as soon as the MUTING function is restarted.

#### FREE function

If an error cannot be corrected immediately, the FREE function can be used to free the muting range. Enable signal Q and output MUTING =1 temporarily. The FREE function can be used if:

- ENABLE = 1
- At least one muting sensor is activated
- A user acknowledgment with rising edge at input ACK occurs twice within 4 s, and the second user acknowledgment at input ACK remains at a signal state of 1 (acknowledgment button remains activated)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using the FREE function, the action must be observed. A dangerous situation must be able to be interrupted at any time by releasing the acknowledgment button. The acknowledgment button must be mounted in such a way that the entire danger area can be observed by the operator. (S037) |  |

#### Timing diagrams for discrepancy errors at sensor pair 1 or interruption of the light curtain (MUTING is not active)

![Timing diagrams for discrepancy errors at sensor pair 1 or interruption of the light curtain (MUTING is not active)](images/166668176267_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Sensor pair 1 (MS_11 and MS_22) is not activated within discrepancy time DISCTIM1. |
| ② | The light curtain is interrupted even though there is no enable (ENABLE=0) |
| ③ | FREE function |
| ④ | Acknowledgment |

#### Behavior with stopped conveyor equipment

If, while the conveyor equipment has stopped, the monitoring for one of the following reasons is to be deactivated:

- To comply with discrepancy time DISCTIM1 or DISCTIM2
- To comply with maximum muting time TIME_MAX

You must supply input STOP with a "1" signal for as long as the conveyor equipment is stopped. As soon as the conveyor equipment is running again (STOP = 0), discrepancy times DISCTIM1 and DISCTIM2 and maximum muting time TIME_MAX are reset.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When STOP = 1 or ENABLE = 0, discrepancy monitoring is shut down. During this time, if inputs MSx1/MSx2 of a sensor pair both take a signal state of 1 due to an undetected error, for example, because both muting sensors have adopted signal state 1 in the event of an error, the fault is not detected and the MUTING function can be started unintentionally (when ENABLE =1). (S038) |  |

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits 0 to 6 are saved until acknowledgment at input ACK.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Discrepancy error or incorrect discrepancy time DISCTIM 1 setting for sensor pair 1 | Malfunction in production sequence | Malfunction in production sequence eliminated |
| Sensor defective | Check sensors |  |  |
| Wiring fault | Check wiring of sensors |  |  |
| Sensors are wired to different F-I/O, and F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON on an F-I/O | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Discrepancy time setting is too low | If necessary, set a higher discrepancy time |  |  |
| Discrepancy time setting is < 0 s or > 3 s | Set discrepancy time in range between 0 s and 3 s |  |  |
| Bit 1 | Discrepancy error or incorrect discrepancy time DISCTIM 2 setting for sensor pair 2 | Same as Bit 0 | Same as Bit 0 |
| Bit 2 | Maximum muting time exceeded or incorrect muting time TIME_MAX setting | Malfunction in production sequence | Malfunction in production sequence eliminated |
| Maximum muting time setting is too low | If necessary, set a higher maximum muting time |  |  |
| Muting time setting is < 0 s or > 10 min | Set muting time in range from 0 s to 10 min |  |  |
| Bit 3 | Light curtain interrupted and muting not active | ENABLE = 0 | Set ENABLE = 1 |
| Light curtain is defective | Check light curtain |  |  |
| Wiring fault | Check wiring of light curtain (FREE input) |  |  |
| F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F-I/O of light curtain  (FREE input) | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Startup of F-system | For FREE function, see DIAG Bit 5 |  |  |
| See other DIAG bits |  |  |  |
| Bit 4 | Muting lamp is defective or cannot be set | Muting lamp is defective | Replace muting lamp |
| Wiring fault | Check wiring of muting lamp |  |  |
| F‑I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F‑I/O of muting lamp | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Bit 5 | FREE function is necessary | See other DIAG bits | Two rising edges at ACK within 4 s, and activate acknowledgment button until ACK_REQ = 0 |
| Bit 6 | Acknowledgment necessary | — | — |
| Bit 7 | State of output Q | — | — |
| Bit 8 | State of output MUTING | — | — |
| Bit 9 | FREE function active | — | — |
| Bit 10 | Reserved | — | — |
| ... |  |  |  |
| Bit 15 | Reserved | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95100817035_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95100850443_DV_resource.Stream@PNG-de-DE.png)

### EV1oo2DI: 1oo2 evaluation with discrepancy analysis (STEP 7 Safety V19)

#### Description

This instruction implements a 1oo2 evaluation of two single‑channel sensors combined with a discrepancy analysis.

Output Q is set to 1, if the signal states of inputs IN1 and IN2 both equal 1 and no discrepancy error DISC_FLT is stored. if the signal state of one or both inputs is 0, output Q is set to 0.

As soon as the signal states of inputs IN1 and IN2 are different, the discrepancy time DISCTIME is started. If the signal states of the two inputs are still different once the discrepancy time expires, a discrepancy error is detected and DISC_FLT is set to 1 (restart inhibit).

If the discrepancy between inputs IN1 and IN2 is no longer detected, the discrepancy error is acknowledged according to the parameter assignment of ACK_NEC:

- If ACK_NEC = 0, the acknowledgment is automatic.
- If ACK_NEC = 1, you must use a rising edge at input ACK to acknowledge the discrepancy error.

The output ACK_REQ = 1 signals that a user acknowledgment at input ACK is necessary to acknowledge the discrepancy error (cancel the restart inhibit). The instruction sets ACK_REQ = 1 as soon as discrepancy is no longer detected. After acknowledgment or if, prior to acknowledgment, there is once again a discrepancy between inputs IN1 and IN2, the instruction resets ACK_REQ to 0.

Output Q can never be set to 1 if the discrepancy time setting is < 0 or > 60 s. In this case, output DISC_FLT is also set to 1 (restart inhibit). The call interval of the safety program (e.g., OB 35) must be less than the discrepancy time setting.

Every call of the "1oo2 evaluation with discrepancy analysis" instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., EV1oo2DI_DB_1) or a multi-instance (e.g., EV1oo2DI_Instance_1) for the "1oo2 evaluation with discrepancy analysis" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The ACK_NEC tag must not be assigned a value of "0" unless an automatic restart of the affected process is otherwise excluded. (S033) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | BOOL | Sensor 1 |
| IN2 | Input | BOOL | Sensor 2 |
| DISCTIME | Input | TIME | Discrepancy time (0 to 60 s) |
| ACK_NEC | Input | BOOL | 1 = acknowledgment necessary for discrepancy error |
| ACK | Input | BOOL | Acknowledgment of discrepancy error |
| Q | Output | BOOL | Output |
| ACK_REQ | Output | BOOL | 1 = acknowledgment required |
| DISC_FLT | Output | BOOL | 1 = discrepancy error |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Activating inputs IN1 and IN2

Inputs IN1 and IN2 must both be activated in such a way that their safe state is 0.

#### Example with QBAD or QBAD_I_xx signal

For non-equivalent signals you need to OR the input (IN1 and IN2) with which you assign the encoder signal to the safe state 1, with the QBAD signal of the associated F‑I/O or the QBAD_I_xx signal of the associated channel (with S7-300/400 F-CPUs) and negate the result. Signal state 0 is then at input IN1 or IN2 when fail-safe values are output.

![Example with QBAD or QBAD_I_xx signal](images/95140161547_DV_resource.Stream@PNG-en-US.png)

![Example with QBAD or QBAD_I_xx signal](images/95146176651_DV_resource.Stream@PNG-en-US.png)

#### Example with value status

For non-equivalent signals, you have to negate the input (IN1 or IN2) with which you have assigned the encoder signal to a safe state of 1 and AND it with the value status of the associated channel. Signal state 0 is then at input IN1 or IN2 when fail-safe values are output.

![Example with value status](images/95139097995_DV_resource.Stream@PNG-en-US.png)

![Example with value status](images/95139467787_DV_resource.Stream@PNG-en-US.png)

#### Timing diagrams EV1oo2DI

If ACK_NEC = 1:

![Timing diagrams EV1oo2DI](images/166668019339_DV_resource.Stream@PNG-de-DE.png)

#### Startup behavior

> **Note**
>
> If the sensors at inputs IN1 and IN2 are assigned to different F‑I/O, it is possible that the fail‑safe values are output for different lengths of time following startup of the F-system due to different startup behavior of the F‑I/O. If the signal states of inputs IN1 and IN2 remain different after the discrepancy time DISCTIME has expired, a discrepancy error is detected after the F‑system starts up.
>
> If ACK_NEC = 1 you must acknowledge the discrepancy error with a rising edge at input ACK.

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits are saved until acknowledgment at input ACK.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Discrepancy error or incorrect discrepancy time setting  (= status of DISC_FLT) | Sensor defective | Check sensors |
| Wiring fault | Check wiring of sensors |  |  |
| Sensors are wired to different F‑I/O, and F‑I/O fault, channel fault, or communication error, or passivation by means of PASS_ON on an F‑I/O | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Discrepancy time setting is too low | If necessary, set a higher discrepancy time |  |  |
| Discrepancy time setting is < 0 s or > 60 s | Set discrepancy time in range between 0 s and 60 s |  |  |
| Bit 1 | For discrepancy errors: last signal state change was at input IN1 | — | — |
| Bit 2 | For discrepancy errors: last signal state change was at input IN2 | — | — |
| Bit 3 | Reserved | — | — |
| Bit 4 | Reserved | — | — |
| Bit 5 | For discrepancy errors: input ACK has a permanent signal state of 1 | Acknowledgment button defective | Replace acknowledgment button |
| Wiring fault | Check wiring of acknowledgment button |  |  |
| Bit 6 | Acknowledgment necessary | — | — |
| Bit 7 | State of output Q | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/95121995019_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95122079627_DV_resource.Stream@PNG-de-DE.png)

### FDBACK: Feedback circuit monitoring (STEP 7 Safety V19)

#### Description

This instruction implements feedback monitoring.

The signal state of output Q is checked to see whether it corresponds to the inverse signal state of the feedback input FEEDBACK.

Output Q is set to 1 as soon as input ON = 1. Requirement for this is that the feedback input FEEDBACK = 1 and no feedback error is saved.

Output Q is reset to 0, as soon as input ON = 0 or if a feedback error is detected.

A feedback error ERROR = 1 is detected if the inverse signal state of the feedback input FEEDBACK (to input Q) does not follow the signal state of output Q within the maximum tolerable feedback time. The feedback error is saved.

If a discrepancy is detected between the feedback input FEEDBACK and the output Q after a feedback error, the feedback error is acknowledged in accordance with the parameter assignment of ACK_NEC:

- If ACK_NEC = 0, the acknowledgment is automatic.
- If ACK_NEC = 1, you must acknowledge the feedback error with a rising edge at input ACK.

The ACK_REQ = 1 output then signals that a user acknowledgment is necessary at input ACK to acknowledge the feedback error. Following an acknowledgment, the instruction resets ACK_REQ to 0.

To avoid a feedback errors from being detected and acknowledgment from being required when the F-I/O controlled by the Q output are passivated, you need to supply input QBAD_FIO with the QBAD signal of the associated F-I/O or the QBAD_O_xx signal / inverted value status of the associated channel.

Every call of the "Feedback monitoring" instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., FDBACK_DB_1) or a multi-instance (e.g., FDBACK_Instance_1) for the "Feedback monitoring" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The ACK_NEC tag must not be assigned a value of "0" unless an automatic restart of the affected process is otherwise excluded. (S033) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ON | Input | BOOL | 1= Enable output |
| FEEDBACK | Input | BOOL | Feedback input |
| QBAD_FIO | Input | BOOL | QBAD signal of the F-I/O or QBAD_O_xx signal / inverted value status of the Q output |
| ACK_NEC | Input | BOOL | 1=Acknowledgment necessary |
| ACK | Input | BOOL | Acknowledgment |
| FDB_TIME | Input | TIME | Feedback time |
| Q | Output | BOOL | Output |
| ERROR | Output | BOOL | Feedback error |
| ACK_REQ | Output | BOOL | Acknowledgment request |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | Version 1.0 requires that the F_TOF block with the number FB 186 is available in the project tree in the "Program blocks/System blocks/STEP 7 Safety" folder.   When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically. If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. You will then avoid number conflicts. |
| 1.1 | x | — | — | These versions have identical functions to version 1.0, but do not require the F_TOF block to have a particular number. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | o | o |  |
| 1.5 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Interconnection example

![Interconnection example](images/171644128139_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Sent to the FEEDBACK input of the instruction |
| ② | from output Q of the instruction |

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits 0, 2, and 5 are saved until acknowledgment at input ACK.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Feedback error or incorrect feedback time setting (= state of ERROR) | Feedback time setting < 0 | Set feedback time > 0 |
| Feedback time setting is too low | If necessary, set a higher feedback time |  |  |
| Wiring fault | Check wiring of actuator and feedback contact |  |  |
| Actuator or feedback contact is defective | Check actuator and feedback contact |  |  |
| I/O fault or channel fault of feedback input | Check I/O |  |  |
| Bit 1 | Passivation of F-I/O/channel controlled by output Q (= state of QBAD_FIO) | F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F-I/O | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |
| Bit 2 | After feedback error: feedback input has permanent signal state of 0 | F-I/O fault or channel fault of feedback input | Check I/O |
| Feedback contact is defective | Check feedback contact |  |  |
| F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F-I/O of feedback input | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |  |  |
| Bit 3 | Reserved | — | — |
| Bit 4 | Reserved | — | — |
| Bit 5 | For feedback error: input ACK has a permanent signal state of 1 | Acknowledgment button defective | Check acknowledgment button |
| Wiring fault | Check wiring of acknowledgment button |  |  |
| Bit 6 | Acknowledgment required (= state of ACK_REQ) | — | — |
| Bit 7 | State of output Q | — | — |

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction for S7-300/400 F-CPUs works:

![Example](images/95122677771_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95122698379_DV_resource.Stream@PNG-de-DE.png)

The following example shows how the instruction for S7-1200/1500 F-CPUs works:

![Example](images/115866487051_DV_resource.Stream@PNG-de-DE.png)

![Example](images/115866494475_DV_resource.Stream@PNG-de-DE.png)

### SFDOOR: Protective door monitoring (STEP 7 Safety V19)

#### Description

This instruction implements safety door monitoring.

Enable signal Q is reset to 0 as soon as one of the inputs IN1 or IN2 take a signal state of 0 (safety door is opened). The enable signal can be reset to 1, only if:

- Inputs IN1 and IN2 both take a signal state of 0 prior to opening the door (safety door has been completely opened)
- Inputs IN1 and IN2 then both take a signal state of 1 (safety door is closed)
- An acknowledgment occurs

The acknowledgment for the enable takes place according to the parameter assignment at input ACK_NEC:

- If ACK_NEC = 0, the acknowledgment is automatic.
- If ACK_NEC = 1, you must use a rising edge at input ACK for acknowledging the enable.

Output ACK_REQ = 1 is used to signal that a user acknowledgment is required at input ACK for the acknowledgment. The instruction sets ACK_REQ = 1 as soon as the door is closed. Following an acknowledgment, the instruction resets ACK_REQ to 0.

In order for the instruction to recognize whether inputs IN1 and IN2 are 0 merely due to passivation of the associated F-I/O, you need to supply inputs QBAD_IN1 or QBAD_IN2 with the QBAD signal of the associated F-I/O or QBAD_I_xx signal / inverted value status of the associated channel. Among other things, this will prevent you from having to open the safety door completely prior to an acknowledgment in the event the F-I/O are passivated.

Every call of the "Safety door monitoring" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., SFDOOR_DB_1) or a multi-instance (e.g., SFDOOR_Instance_1) for the "Safety door monitoring" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The ACK_NEC tag must not be assigned a value of "0" unless an automatic restart of the affected process is otherwise excluded. (S033) |  |

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | BOOL | Input 1 |
| IN2 | Input | BOOL | Input 2 |
| QBAD_IN1 | Input | BOOL | QBAD signal of the F-I/O or QBAD_O_xx signal / inverted value status of the channel of input IN1 |
| QBAD_IN2 | Input | BOOL | QBAD signal of the F-I/O or QBAD_O_xx signal / inverted value status of the channel of input IN2 |
| OPEN_NEC | Input | BOOL | 1= Open necessary at startup |
| ACK_NEC | Input | BOOL | 1=Acknowledgment necessary |
| ACK | Input | BOOL | Acknowledgment |
| Q | Output | BOOL | 1= Enable, safety door closed |
| ACK_REQ | Output | BOOL | Acknowledgment request |
| DIAG | Output | BYTE | Non-fail safe service information |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Interconnection example

You must interconnect the NC contact of position switch 1 of the safety door at input IN1 and the NO contact of position switch 2 at input IN2. Position switch 1 must be mounted in such a way that it is positively operated when the safety door is open. Position switch 2 must be mounted in such a way that it is operated when the safety door is closed.

![Interconnection example](images/166663939083_DV_resource.Stream@PNG-en-US.png)

#### Startup behavior

After an F-system startup, enable signal Q is reset to 0. The acknowledgment for the enable takes place according to the parameter assignment at inputs OPEN_NEC and ACK_NEC:

- When OPEN_NEC = 0, an automatic acknowledgment occurs **independently** of ACK_NEC, as soon as the two inputs IN1 and IN2 take signal state 1 for the first time following reintegration of the associated F-I/O (safety door is closed).
- When OPEN_NEC = 1 **or** if at least one of the IN1 and IN2 inputs still has a signal state of 0 after reintegration of the associated F-I/O, an automatic acknowledgment occurs **according** to ACK_NEC or you have to use a rising edge at input ACK for the enable. Prior to acknowledgment, inputs IN1 and IN2 both have to take a signal state of 0 (safety door has been completely opened) followed by a signal state of 1 (safety door is closed).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The OPEN_NEC tag must not be assigned a value of "0" unless an automatic restart of the affected process is otherwise excluded. (S039) |  |

#### Output DIAG

The DIAG output provides non-fail-safe information on errors for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program.

#### Structure of DIAG

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Reserved | — | — |
| Bit 1 | Signal state 0 is missing at both IN1 and IN2 inputs | Safety door was not completely opened when OPEN_NEC = 1 after F-system startup | Open safety door completely |
| Open safety door was not completely opened | Open safety door completely |  |  |
| Wiring fault | Check wiring of position switch |  |  |
| Position switch is defective | Check position switch |  |  |
| Position switch is incorrectly adjusted | Adjust position switch properly |  |  |
| Bit 2 | Signal state 1 is missing at both IN1 and IN2 inputs | Safety door was not closed | Close safety door |
| Wiring fault | Check wiring of position switch |  |  |
| Position switch is defective | Check position switch |  |  |
| Position switch is incorrectly adjusted | Adjust position switch properly |  |  |
| Bit 3 | QBAD_IN1 and/or QBAD_IN2 = 1 | F-I/O fault, channel fault, or communication error, or passivation by means of PASS_ON of F-I/O or channel of IN1 and/or IN2 | For a solution, see the section "Structure of DIAG", bits 0 to 6 in [DIAG](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#diag) |
| Bit 4 | Reserved | — | — |
| Bit 5 | If enable is missing: input ACK has a permanent signal state of 1 | Acknowledgment button defective | Check acknowledgment button |
| Wiring fault | Check wiring of acknowledgment button |  |  |
| Bit 6 | Acknowledgment required (= state of ACK_REQ) | — | — |
| Bit 7 | State of output Q | — | — |

#### Example

The following example shows how the instruction for S7-300/400 F-CPUs works:

![Example](images/95123297035_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95123304843_DV_resource.Stream@PNG-de-DE.png)

The following example shows how the instruction for S7-1200/1500 F-CPUs works:

![Example](images/95138578699_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95138586507_DV_resource.Stream@PNG-de-DE.png)

### ACK_GL: Global acknowledgment of all F-I/O in an F-runtime group (STEP 7 Safety V19)

#### Description

This instruction creates an acknowledgment for the simultaneous reintegration of all F-I/O or channels of the F-I/O of an F-runtime group after communication errors, F-I/O errors, or channel faults.

A [user acknowledgment](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementation-of-user-acknowledgment) with a positive edge at input ACK_GLOB is required for reintegration. The acknowledgment occurs analogously to the user acknowledgment via the ACK_REI tag of the [F-I/O DB](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#ack_rei), but it acts simultaneously on all F-I/O of the F‑runtime group in which the instruction is called.

If you use the instruction ACK_GL, you do not have to provide a user acknowledgment for each F‑I/O of the F-runtime group via the ACK_REI tag of the F‑I/O DB.

Every call of the "Global acknowledgment of all F-I/O of a runtime group" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., ACK_GL_DB_1) or a multi-instance (e.g., ACK_GL_Instance_1) for the "Global acknowledgment of all F-I/O of a runtime group" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

> **Note**
>
> An acknowledgment via the ACK_GL instruction is only possible if the tag ACK_REI of the F-I/O DB = 0. Accordingly, an acknowledgment via the tag ACK_REI of the F-I/O DB is only possible if the input ACK_GLOB of the instruction = 0.
>
> The instruction is only allowed to be called once per F-runtime group.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ACK_GLOB | Input | BOOL | 1=acknowledgment for reintegration |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/95119915403_DV_resource.Stream@PNG-de-DE.png)

![Example](images/95121728011_DV_resource.Stream@PNG-de-DE.png)

## Timer operations

This section contains information on the following topics:

- [TP: Generate pulse (STEP 7 Safety V19)](#tp-generate-pulse-step-7-safety-v19)
- [TON: Generate on-delay (STEP 7 Safety V19)](#ton-generate-on-delay-step-7-safety-v19)
- [TOF: Generate off-delay (STEP 7 Safety V19)](#tof-generate-off-delay-step-7-safety-v19)

### TP: Generate pulse (STEP 7 Safety V19)

#### Description

You can use the "Generate pulse" instruction to set output Q for a programmed period. The instruction is started if the result of logic operation (RLO) changes from "0" to "1" (positive edge) at input IN. The programmed period PT starts running when the instruction starts. Output Q is set for period PT, regardless of the subsequent sequence of the input signal. Also the detection of a new positive signal edge does not influence the signal state at output Q as long as period PT runs.

You can query the current time value at the output ET. The time value begins at T#0s and ends when the value of period PT is reached. If period PT is reached and the signal state at input IN is "0", output ET is reset.

Every call of the "Generate pulse" instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Timer_DB_1) or a multi-instance (e.g., F_IEC_Timer_Instance_1) for the "Generate pulse" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

The operating system resets the instances of the "Generate pulse" instruction on a startup of the F-system.

> **Note**
>
> The functionality of this instruction differs from the corresponding standard TP instruction in the following points:
>
> - If the instruction is called while the time is running with PT = 0 ms, the outputs Q and ET are reset.
> - If the instruction is called with PT < 0 ms, the outputs Q and ET are reset.
>
> To restart the pulse, a new rising signal edge at input IN is required once PT is greater than 0 again.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | BOOL | Start input |
| PT | Input | TIME | Duration of pulse; must be positive. |
| Q | Output | BOOL | Pulse output |
| ET | Output | TIME | Current time value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Pulse diagram

The following figure shows the pulse diagram of the instruction "Generate pulse":

![Pulse diagram](images/166649537291_DV_resource.Stream@PNG-de-DE.png)

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/93520121355_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93520117771_DV_resource.Stream@PNG-de-DE.png)

If the signal state of operand "TagIn_1" changes from "0" to "1", the "Generate pulse" instruction is started and the period assigned at input PT (100 ms) runs, regardless of the further course of operand "TagIn_1".

Operand "TagOut" at output Q has signal state "1" as long as the period is running. Operand ""F_DB_1".Tag_ET" contains the current time value.

### TON: Generate on-delay (STEP 7 Safety V19)

#### Description

You use the "Generate on-delay" instruction to delay the setting of output Q by the assigned period PT. The instruction is started if the result of logic operation (RLO) changes from "0" to "1" (positive edge) at input IN. The programmed period PT starts running when the instruction starts. When period PT has expired, output Q is set to signal state "1". Output Q remains set as long as the start input is set to "1". When the signal state at the start input changes from "1" to "0", output Q is reset. The time function is restarted when a new positive signal edge is detected at the start input.

You can query the current time value at the output ET. The time value begins at T#0s and ends when the value of period PT is reached. Output ET is reset, as soon as the signal state at input IN changes to "0".

Every call of the "Generate on-delay" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Timer_DB_1) or a multi-instance (e.g., F_IEC_Timer_Instance_1) for the "Generate on-delay" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

The operating system resets the instances of the "Generate on-delay" instruction on a startup of the F-system.

> **Note**
>
> The functionality of this instruction differs from the corresponding standard TON instruction in the following points:
>
> - If the instruction is called while the time is running with PT = 0 ms, the output ET is reset.
> - If the instruction is called with PT < 0 ms, the outputs Q and ET are reset.
>
> To restart the on-delay, a new rising signal edge at input IN is required once PT is greater than 0 again.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | BOOL | Start input |
| PT | Input | TIME | Duration of on-delay; must be positive. |
| Q | Output | BOOL | Output that is set after expiration of time PT. |
| ET | Output | TIME | Current time value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Pulse diagram

The following figure shows the pulse diagram of the instruction "Generate on-delay":

![Pulse diagram](images/166649482763_DV_resource.Stream@PNG-de-DE.png)

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/93520366859_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93520145675_DV_resource.Stream@PNG-de-DE.png)

When the signal state of operand "TagIn_1" changes from "0" to "1", the "Generate on-delay" instruction is started and the period assigned at input PT (1 s) runs.

Operand "TagOut" at output Q feeds signal state "1" when the period has elapsed and remains set as long as operand "TagIn_1" still feeds signal state "1". Operand ""F_DB_1".Tag_ET" contains the current time value.

### TOF: Generate off-delay (STEP 7 Safety V19)

#### Description

You use the "Generate off-delay" instruction to delay the resetting of output Q by the assigned period PT. Output Q is set if the result of logic operation (RLO) changes from "0" to "1" (positive edge) at input IN. When the signal state at input IN changes back to "0", the programmed period PT starts. Output Q remains set as long as period PT runs. After period PT expires, output Q is reset. If the signal state at input IN changes to "1" before period PT has expired, then the time is reset. The signal state at output Q remains at "1".

You can query the current time value at the output ET. The time value begins at T#0s and ends when the value of period PT is reached. After time PT has elapsed, output ET remains at its current value until input IN changes back to "1". If input IN changes to "1" before time PT has expired, the output ET is reset to value T#0.

Every call of the "Generate off-delay" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is in inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Timer_DB_1) or a multi-instance (e.g., F_IEC_Timer_Instance_1) for the "Generate off-delay" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

The operating system resets the instances of the "Generate off-delay" instruction on a startup of the F-system.

> **Note**
>
> The functionality of this instruction differs from the corresponding standard TOF instruction in the following points:
>
> - If the instruction is called while the time is running with PT = 0 ms, the outputs Q and ET are reset.
> - If the instruction is called with PT < 0 ms, the outputs Q and ET are reset.
>
> To restart the off-delay, another falling signal edge at input IN is required once PT is greater than 0 again.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | BOOL | Start input |
| PT | Input | TIME | Duration of off delay; must be positive. |
| Q | Output | BOOL | Output that is reset after expiration of time PT. |
| ET | Output | TIME | Current time value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Pulse diagram

The following figure shows the pulse diagram of the instruction "Generate off-delay":

![Pulse diagram](images/166649249035_DV_resource.Stream@PNG-de-DE.png)

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

The following example shows how the instruction works:

![Example](images/93520599819_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93520378635_DV_resource.Stream@PNG-de-DE.png)

If the signal state of operand "TagIn_1" changes from "0" to "1", the signal state of operand"TagOut" at output Q is set to "1".

If the signal state of operand "TagIn_1" changes back to "0", the period assigned at input PT (200 ms) runs.

The "TagOut" operand at output Q is set back to "0" when the period expires. Operand ""F_DB_1".Tag_ET" contains the current time value.

## Counter operations

This section contains information on the following topics:

- [CTU: Count up (STEP 7 Safety V19)](#ctu-count-up-step-7-safety-v19)
- [CTD: Count down (STEP 7 Safety V19)](#ctd-count-down-step-7-safety-v19)
- [CTUD: Count up and down (STEP 7 Safety V19)](#ctud-count-up-and-down-step-7-safety-v19)

### CTU: Count up (STEP 7 Safety V19)

#### Description

You can use the "Count up" instruction to increment the value at output CV. When the signal state at the CU input changes from "0" to "1" (positive signal edge), the instruction is executed and the current count at the CV output increases by one. The count value is increased on each detection of a positive signal edge until it reaches the high limit of the data type specified at the CV output. When the high limit is reached, the signal state at the CU input no longer affects the instruction.

The counter status can be queried at output Q. The signal state at output Q is determined by parameter PV. When the current count value is greater than or equal to the value of parameter PV, output Q is set to signal state "1". In all other cases, the signal state at output Q is "0".

The value at output CV is reset to zero when the signal state at input R changes to "1". As long as signal state "1" exists at input R, the signal state at input CU has no effect on the instruction.

Every call of the "Count up" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Counter_DB_1) or a multi-instance (e.g., F_IEC_Counter_Instance_1) for the "Count up" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

The operating system resets the instances of the "Count up" instruction on a startup of the F-system.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CU | Input | BOOL | Counter input |
| R | Input | BOOL | Reset input |
| PV | Input | INT | Value for which output Q is set |
| Q | Output | BOOL | Counter status |
| CV | Output | INT | Current count value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/96275838603_DV_resource.Stream@PNG-de-DE.png)

![Example](images/96275835147_DV_resource.Stream@PNG-de-DE.png)

When the signal state of the "CU" input changes from "0" to "1", the "Count up" instruction is executed and the current count of the "CV" output increases by one. The count value is increased on every additional positive signal edge until the high limit of the specified data type (32767) is reached.

The value at the PV parameter is applied as the limit for determining the "TagOut" operands at the Q output. Output "Q" returns the signal state "1" as long as the current count is greater than or equal to the value of operand "PV". In all other cases, the "Q" output has the signal state "0".

### CTD: Count down (STEP 7 Safety V19)

#### Description

You can use the "Count down" instruction to decrement the value at output CV. When the signal state at input CD changes from "0" to "1" (positive signal edge), the instruction is executed and the current count value at output CV is decreased by one. The count value is decreased on each detection of a positive signal edge until it reaches the low limit of the specified data type. When the low limit is reached, the signal state at input CD no longer affects the instruction.

The counter status can be queried at output Q. When the current count value is less than or equal to zero, output Q is set to signal state "1". In all other cases, the signal state at output Q is "0".

The value at output CV is set to the value of parameter "PV" when the signal state at input LD changes to "1". As long as signal state "1" exists at input LD, the signal state at input CD has no effect on the instruction.

Every call of the "Count down" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Counter_DB_1) or a multi-instance (e.g., F_IEC_Counter_Instance_1) for the "Count down" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

The operating system resets the instances of the "Count down" instruction on a startup of the F-system.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CD | Input | BOOL | Counter input |
| LD | Input | BOOL | Load input |
| PV | Input | INT | Value at the output CV when LD = 1 is set |
| Q | Output | BOOL | Counter status |
| CV | Output | INT | Current count value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93521247627_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93521244043_DV_resource.Stream@PNG-de-DE.png)

When the signal state of the "CD" input changes from "0" to "1", the "Count down" instruction is executed and the current count at "CV" output decreases by one. The count value is decreased on each additional positive signal edge until the low limit of the specified data type (-32768) is reached.

Output "Q" returns the signal state "1" as long as the current count is less than or equal to zero. In all other cases, output "Q" has signal state "0".

### CTUD: Count up and down (STEP 7 Safety V19)

#### Description

You can use the "Count up and down" instruction to increment and decrement the count value at output CV. If the signal state at the CU input changes from "0" to "1" (positive signal edge), the current count at the CV output increases by one. If the signal state at input CD changes from "0" to "1" (positive signal edge), the count value at output CV is decreased by one. If a positive signal edge is present at inputs CU and CD in one program cycle, the current count value at output CV remains unchanged.

The count value can be increased until it reaches the high limit of the data type specified at output CV. When the high limit is reached, the count value is no longer incremented on a positive signal edge. When the low limit of the specified data type is reached, the count value is no longer decreased.

When the signal state at input LD changes to "1", the count value at output CV is set to the value of parameter PV. As long as signal state "1" exists at input LD, the signal state at inputs CU and CD has no effect on the instruction.

The count value is set to zero, when the signal state at input R changes to "1". As long as signal state "1" exists at input R, the signal state at inputs CU, CD, and LD has no effect on the "Count up and down" instruction.

The status of the up counter can be queried at output QU. When the current count value is greater than or equal to the value of parameter PV, output QU delivers signal state "1". In all other cases, the signal state at output QU is "0".

The status of the down counter can be queried at output QD. When the current count value is lesser than or equal to zero, output QD delivers signal state "1". In all other cases, the signal state at output QD is "0".

Every call of the "Count up and down" instruction must be assigned a data area in which the instruction data are stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., F_IEC_Counter_DB_1) or a multi-instance (e.g., F_IEC_Counter_Instance_1) for the "Count up and down" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

The operating system resets the instances of the "Count up and down" instruction when the F-system is started up.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| CU | Input | BOOL | Count up input |
| CD | Input | BOOL | Count down input |
| R | Input | BOOL | Reset input |
| LD | Input | BOOL | Load input |
| PV | Input | INT | Value set at the output QU/ at which the output CV is set at LD = 1. |
| QU | Output | BOOL | Status of up counter |
| QD | Output | BOOL | Status of down counter |
| CV | Output | INT | Current count value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93521569931_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93521425547_DV_resource.Stream@PNG-de-DE.png)

When the signal state at the "CU" input or at the "CD" input changes from "0" to "1" (positive signal edge), the "Count up and down" instruction is executed. When a positive signal edge is present at the "CU" input, the current count of the "CV" output increases by one. When a positive signal edge is present at the "CD" input, the current count at the "CV" output decreases by one. The count value is increased on each positive signal edge at the CU input until it reaches the high limit of 32767. The count value is decreased on each positive signal edge at the CD input until it reaches the low limit of -32768.

Output "QU" returns the signal state "1" as long as the current count is greater than or equal to the value at the "PV" input. In all other cases, output "QU" has signal state "0".

Output "QD" returns the signal state "1" as long as the current count is less than or equal to zero. In all other cases, output "QD" has signal state "0".

## Comparator operations

This section contains information on the following topics:

- [CMP ==: Equal (STEP 7 Safety V19)](#cmp-equal-step-7-safety-v19)
- [CMP <>: Not equal (STEP 7 Safety V19)](#cmp-not-equal-step-7-safety-v19)
- [CMP >=: Greater or equal (STEP 7 Safety V19)](#cmp-greater-or-equal-step-7-safety-v19)
- [CMP <=: Less or equal (STEP 7 Safety V19)](#cmp-less-or-equal-step-7-safety-v19)
- [CMP >: Greater than (STEP 7 Safety V19)](#cmp-greater-than-step-7-safety-v19)
- [CMP <: Less than (STEP 7 Safety V19)](#cmp-less-than-step-7-safety-v19)

### CMP ==: Equal (STEP 7 Safety V19)

#### Description

You can use the "Equal" instruction to determine if the first comparison value (IN1 or <Operand1>) is equal to the second comparison value (IN2 or <Operand2>).

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME, WORD, (S7-300, S7-400) DWORD | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME, WORD, (S7-300, S7-400) DWORD | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93521690635_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93521686667_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" = "Tag_Value2").

### CMP <>: Not equal (STEP 7 Safety V19)

#### Description

You can use the "Not equal" instruction to determine if the first comparison value (IN1 or <Operand1>) is not equal to the second comparison value (IN2 or <Operand2>).

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME, WORD, (S7-300, S7-400) DWORD | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME, WORD, (S7-300, S7-400) DWORD | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93521796107_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93521792139_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" <> "Tag_Value2").

### CMP >=: Greater or equal (STEP 7 Safety V19)

#### Description

You can use the "Greater or equal" instruction to determine if the first comparison value (IN1 or <Operand1>) is greater than or equal to the second comparison value (IN2 or <Operand2>). Both comparison values must be of the same data type.

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93522311691_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93521987723_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" >= "Tag_Value2").

### CMP <=: Less or equal (STEP 7 Safety V19)

#### Description

You can use the "Less or equal" instruction to determine if the first comparison value (IN1 or <Operand1>) is less than or equal to the second comparison value (IN2 or <Operand2>). Both comparison values must be of the same data type.

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93528521867_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93527596299_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" <= "Tag_Value2").

### CMP >: Greater than (STEP 7 Safety V19)

#### Description

You can use the "Greater than" instruction to determine if the first comparison value (IN1 or <Operand1>) is greater than the second comparison value (IN2 or <Operand2>). Both comparison values must be of the same data type.

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93531315723_DV_resource.Stream@PNG-de-DE.png)

![Example](images/96165253003_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" > "Tag_Value2").

### CMP <: Less than (STEP 7 Safety V19)

#### Description

You can use the "Less than" instruction to determine if the first comparison value (IN1 or <Operand1>) is less than the second comparison value (IN2 or <Operand2>). Both comparison values must be of the same data type.

If the condition of the comparison is satisfied, the instruction returns result of logic operation (RLO) "1". If the condition of the comparison is not satisfied, the instruction returns RLO "0".

For LAD:

The RLO of the instruction is linked to the RLO of the entire current path as follows:

- By AND, when the comparison instruction is connected in series.
- By OR, when the comparison instruction is connected in parallel.

Enter the first comparison value (<Operand1>) in the operand placeholder above the instruction. Enter the second comparison value (<Operand2>) in the operand placeholder below the instruction.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| FBD: IN1  LAD: <Operand1> | Input | INT, DINT, TIME | First value to compare |
| FBD: IN2  LAD: <Operand2> | Input | INT, DINT, TIME | Second value to compare |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93531511051_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93531507083_DV_resource.Stream@PNG-de-DE.png)

Output "TagOut" is set when the following conditions are fulfilled:

- "Tag_In1" has signal state "1".
- The condition of the comparison instruction is fulfilled ("Tag_Value1" < "Tag_Value2").

## Math functions

This section contains information on the following topics:

- [ADD: Add (STEP 7 Safety V19)](#add-add-step-7-safety-v19)
- [SUB: Subtract (STEP 7 Safety V19)](#sub-subtract-step-7-safety-v19)
- [MUL: Multiply (STEP 7 Safety V19)](#mul-multiply-step-7-safety-v19)
- [DIV: Divide (STEP 7 Safety V19)](#div-divide-step-7-safety-v19)
- [NEG: Create two's complement (STEP 7 Safety V19)](#neg-create-twos-complement-step-7-safety-v19)
- [ABS: Form absolute value (STEP 7 Safety V19) (S7-1200, S7-1500)](#abs-form-absolute-value-step-7-safety-v19-s7-1200-s7-1500)

### ADD: Add (STEP 7 Safety V19)

#### Description

You can use the "Add" instruction to add the value at input IN1 and the value at input IN2 and query the sum at the OUT output (OUT = IN1 + IN2).

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> (S7-1200, S7-1500) You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.
>
> (S7-300, S7-400) You can avoid a STOP of the F-CPU by inserting a "Get status bit OV" instruction in the next network, thereby programming overflow detection.
>
> Note the following:
>
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The network with the "Get status bit OV" instruction must not contain any jump labels.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - A warning is issued if you do not insert a "Get status bit OV" instruction.
> - Work memory requirement of safety program is increased.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN1 | Input | INT, DINT | First addend |
| IN2 | Input | INT, DINT | Second addend |
| OUT | Output | INT, DINT | Total |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example for S7-300/400 F-CPUs

The following example shows how the instruction works:

![Example for S7-300/400 F-CPUs](images/102770770059_DV_resource.Stream@PNG-en-US.png)

![Example for S7-300/400 F-CPUs](images/102770228363_DV_resource.Stream@PNG-en-US.png)

The "Add" instruction is always executed regardless of the signal state at enable input EN.

The value of the "Tag_Value1" operand is added to value of the "Tag_Value2" operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

If needed, you can also store the signal status of the ENO enable output in an (F-)DB, and centrally evaluate whether overflows have occurred for all or one group of instructions with overflow detection.

When an overflow occurs during execution of the "Add" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### Example for S7-1200/1500 F-CPUs

The following example shows how the instruction works:

![Example for S7-1200/1500 F-CPUs](images/102771021835_DV_resource.Stream@PNG-de-DE.png)

![Example for S7-1200/1500 F-CPUs](images/102771017483_DV_resource.Stream@PNG-de-DE.png)

The "Add" instruction is always executed regardless of the signal state at enable input EN.

The value of the "#Tag_Value1" operand is added to value of the "#Tag_Value2" operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

When no overflow occurs during execution of the "Add" instruction, the ENO enable output has the signal state "1" and the "#TagOut" operand is set.

If needed, you can also store the signal status of the ENO enable output in an (F-)DB, and centrally evaluate whether overflows have occurred for all or one group of instructions with overflow detection.

---

**See also**

[---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
  
[---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

### SUB: Subtract (STEP 7 Safety V19)

#### Description

You can use the "Subtract" instruction to subtract the value at input IN2 from the value at input IN1 and query the difference at the OUT output (OUT = IN1 – IN2).

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> (S7-1200, S7-1500) You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.
>
> (S7-300, S7-400) You can avoid a STOP of the F-CPU by inserting a "Get status bit OV" instruction in the next network, thereby programming overflow detection.
>
> Note the following:
>
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The network with the "Get status bit OV" instruction must not contain any jump labels.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - A warning is issued if you do not insert a "Get status bit OV" instruction.
> - Work memory requirement of safety program is increased.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN1 | Input | INT, DINT | Minuend |
| IN2 | Input | INT, DINT | Subtrahend |
| OUT | Output | INT, DINT | Difference |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example for S7-300/400 F-CPUs

The following example shows how the instruction works:

![Example for S7-300/400 F-CPUs](images/102773944715_DV_resource.Stream@PNG-en-US.png)

![Example for S7-300/400 F-CPUs](images/102771521419_DV_resource.Stream@PNG-en-US.png)

The "Subtract" instruction is always executed regardless of the signal state at enable input EN.

The value of the "Tag_Value2" operand is subtracted from the value of the "Tag_Value1" operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

When an overflow occurs during execution of the "Subtract" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### Example for S7-1200/1500 F-CPUs

The following example shows how the instruction works:

![Example for S7-1200/1500 F-CPUs](images/102775638795_DV_resource.Stream@PNG-de-DE.png)

![Example for S7-1200/1500 F-CPUs](images/102775643403_DV_resource.Stream@PNG-de-DE.png)

The "Subtract" instruction is always executed regardless of the signal state at enable input EN.

The value of the "#Tag_Value2" operand is subtracted from the value of the "#Tag_Value1" operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

When no overflow occurs during execution of the "Subtract" instruction, the ENO enable output has the signal state "1" and the "#TagOut" operand is set.

---

**See also**

[---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
  
[---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

### MUL: Multiply (STEP 7 Safety V19)

#### Description

You can use the "Multiply" instruction to multiply the value at input IN1 by the value at input IN2 and query the product at output OUT (OUT = IN1 × IN2).

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> (S7-1200, S7-1500) You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.
>
> (S7-300, S7-400) You can avoid a STOP of the F-CPU by inserting a "Get status bit OV" instruction in the next network, thereby programming overflow detection.
>
> Note the following:
>
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The network with the "Get status bit OV" instruction must not contain any jump labels.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - A warning is issued if you do not insert a "Get status bit OV" instruction.
> - Work memory requirement of safety program is increased.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN1 | Input | INT, DINT | Multiplier |
| IN2 | Input | INT, DINT | Multiplicand |
| OUT | Output | INT, DINT | Product |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example for S7-300/400 F-CPUs

The following example shows how the instruction works:

![Example for S7-300/400 F-CPUs](images/102776441227_DV_resource.Stream@PNG-en-US.png)

![Example for S7-300/400 F-CPUs](images/102775848587_DV_resource.Stream@PNG-en-US.png)

The "Multiply" instruction is always executed regardless of the signal state at enable input EN.

The value of the "Tag_Value1" operand is multiplied by the value of the "Tag_Value2" operand. The result of the multiplication is stored in the ""F_DB_1".Tag_Result" operand.

When an overflow occurs during execution of the "Multiply" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### Example for S7-1200/1500 F-CPUs

The following example shows how the instruction works:

![Example for S7-1200/1500 F-CPUs](images/102777646987_DV_resource.Stream@PNG-de-DE.png)

![Example for S7-1200/1500 F-CPUs](images/102776451979_DV_resource.Stream@PNG-de-DE.png)

The "Multiply" instruction is always executed regardless of the signal state at enable input EN.

The value of the "#Tag_Value1" operand is multiplied by the value of the "#Tag_Value2" operand. The result of the multiplication is stored in the ""F_DB_1".Tag_Result" operand.

When no overflow occurs during execution of the "Multiply" instruction, the ENO enable output has the signal state "1" and the "#TagOut" operand is set.

---

**See also**

[---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
  
[---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

### DIV: Divide (STEP 7 Safety V19)

#### Description

You can use the "Divide" instruction to divide the value at input IN1 by the value at input IN2 and query the quotient at the OUT output (OUT = IN1 / IN2).

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> (S7-1200, S7-1500) You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.
>
> (S7-300, S7-400) You can avoid a STOP of the F-CPU by inserting a "Get status bit OV" instruction in the next network, thereby programming overflow detection.
>
> Note the following:
>
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The network with the "Get status bit OV" instruction must not contain any jump labels.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - A warning is issued if you do not insert a "Get status bit OV" instruction.
> - Work memory requirement of safety program is increased.

> **Note**
>
> S7-300/400, S7-1200/1500 (enable output ENO connected):
>
> If the divisor (input IN2) of a DIV instruction = 0, the quotient of the division (result of division at output OUT) = 0. The result reacts like the corresponding instruction in a standard block. The F-CPU does not go to STOP mode.
>
> S7-1200/1500 (enable output ENO not connected):
>
> If the divisor (input IN2) of a DIV instruction = 0, the F-CPU goes to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU. We recommend that you rule out a divisor (input IN2) = 0 when creating the program.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN1 | Input | INT, DINT | Dividend |
| IN2 | Input | INT, DINT | Divisor |
| OUT | Output | INT, DINT | Quotient |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example for S7-300/400 F-CPUs

The following example shows how the instruction works:

![Example for S7-300/400 F-CPUs](images/102778112267_DV_resource.Stream@PNG-en-US.png)

![Example for S7-300/400 F-CPUs](images/102778108171_DV_resource.Stream@PNG-en-US.png)

The "Divide" instruction is always execute regardless of the signal state at enable input EN.

The value of the "Tag_Value1" operand is divided by the value of the "Tag_Value2" operand. The result of the division is stored in the ""F_DB_1".Tag_Result" operand.

When an overflow occurs during execution of the "Divide" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### Example for S7-1200/1500 F-CPUs

The following example shows how the instruction works:

![Example for S7-1200/1500 F-CPUs](images/102779311755_DV_resource.Stream@PNG-de-DE.png)

![Example for S7-1200/1500 F-CPUs](images/102778999947_DV_resource.Stream@PNG-de-DE.png)

The "Divide" instruction is always execute regardless of the signal state at enable input EN.

The value of the "#Tag_Value1" operand is divided by the value of the "#Tag_Value2" operand. The result of the division is stored in the ""F_DB_1".Tag_Result" operand.

When no overflow occurs during execution of the "Divide" instruction, the ENO enable output has the signal state "1" and the "#TagOut" operand is set.

---

**See also**

[---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
  
[---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

### NEG: Create two's complement (STEP 7 Safety V19)

#### Description

You can use the "Create twos complement" instruction to change the sign of the value at input IN input and query the result at output OUT. If there is a positive value at input IN, for example, the negative equivalent of this value is sent to output OUT.

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> (S7-1200, S7-1500) You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.
>
> (S7-300, S7-400) You can avoid a STOP of the F-CPU by inserting a "Get status bit OV" instruction in the next network, thereby programming overflow detection.
>
> Note the following:
>
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The network with the "Get status bit OV" instruction must not contain any jump labels.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - A warning is issued if you do not insert a "Get status bit OV" instruction.
> - Work memory requirement of safety program is increased.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN | Input | INT, DINT | Input value |
| OUT | Output | INT, DINT | Twos complement of the input value |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example for S7-300/400 F-CPUs

The following example shows how the instruction works:

![Example for S7-300/400 F-CPUs](images/102779419403_DV_resource.Stream@PNG-en-US.png)

![Example for S7-300/400 F-CPUs](images/102779415307_DV_resource.Stream@PNG-en-US.png)

The "Create two's complement" instruction is always executed regardless of the signal state at enable input EN.

The sign of the "TagIn_Value" operand is changed and the result is stored in the ""F_DB_1".TagOut_Value" operand.

When an overflow occurs during execution of the "Create two's complement" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### Example for S7-1200/1500 F-CPUs

The following example shows how the instruction works:

![Example for S7-1200/1500 F-CPUs](images/102790154635_DV_resource.Stream@PNG-de-DE.png)

![Example for S7-1200/1500 F-CPUs](images/102790982923_DV_resource.Stream@PNG-de-DE.png)

The "Create two's complement" instruction is always executed regardless of the signal state at enable input EN.

The sign of the "#TagIn_Value" operand is changed and the result is stored in the ""F_DB_1".TagOut_Value" operand.

When no overflow occurs during execution of the "Create two's complement" instruction, the ENO enable output has the signal state "1" and the "TagOut" operand is set.

---

**See also**

[---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
  
[---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

### ABS: Form absolute value (STEP 7 Safety V19) (S7-1200, S7-1500)

#### Description

You use the "Form absolute value" instruction to calculate the absolute amount of the value which is specified at the input "IN". The result of the instruction is output at the OUT output and can be queried there.

Enable input "EN" or (S7-300, S7-400) enable output "ENO" cannot be connected. The instruction is therefore always executed regardless of the signal state at enable input "EN".

> **Note**
>
> When the result of the instruction is located outside the permitted range for this data type, the F-CPU may switch to STOP. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.
>
> You must therefore ensure that the permitted range for the data type is observed when creating the program!
>
> You can avoid a STOP of the F-CPU by connecting the ENO enable output, thereby programming overflow detection.
>
> Note the following:
>
> - If the result of the instruction is located outside the permitted range for this data type, the enable output ENO returns the signal state "0".
> - The result of the instruction reacts like the analogous instruction in a standard block.
> - The execution time of the instruction is extended (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).
> - Work memory requirement of safety program is increased.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | (S7-1200, S7-1500)  Enable output |
| IN | Input | INT, DINT | Input value |
| OUT | Output | INT, DINT | Absolute value of the input value |

You select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/102782217995_DV_resource.Stream@PNG-de-DE.png)

![Example](images/102782214283_DV_resource.Stream@PNG-de-DE.png)

The instruction "Form absolute value"is always executed regardless of the signal state at enable input "EN".

The absolute amount of the value at the "TagIn_Value" operand is calculated and the result is stored in the ""F_DB_1".TagOut_Value" operand.

When no overflow occurs during execution of the "Form absolute value" instruction, the enable output ENO has the signal state "1" and the "#TagOut" operand is set.

## Move operations

This section contains information on the following topics:

- [MOVE: Move value (STEP 7 Safety V19)](#move-move-value-step-7-safety-v19)
- [RD_ARRAY_I: Read value from INT F-array (STEP 7 Safety V19) (S7-1500)](#rd_array_i-read-value-from-int-f-array-step-7-safety-v19-s7-1500)
- [RD_ARRAY_DI: Read value from DINT F-array (STEP 7 Safety V19) (S7-1500)](#rd_array_di-read-value-from-dint-f-array-step-7-safety-v19-s7-1500)
- [WR_FDB: Write value indirectly to an F-DB (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#wr_fdb-write-value-indirectly-to-an-f-db-step-7-safety-advanced-v19-s7-300-s7-400)
- [RD_FDB: Read value indirectly from an F-DB (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#rd_fdb-read-value-indirectly-from-an-f-db-step-7-safety-advanced-v19-s7-300-s7-400)

### MOVE: Move value (STEP 7 Safety V19)

#### Description

You can use the "Move value" instruction to transfer the content of the operand at input IN to the operand at output OUT1.

Only operands with identical operand width and identical data structure can be specified for input IN and output OUT1.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

(S7-1200, S7-1500) In the basic state, the instruction box contains an output (OUT1). The number of outputs can be expanded. The inserted outputs are numbered in ascending order on the box. During execution, the content of the operand at the IN input is transferred to all available outputs. The instruction box cannot be expanded if operands with F-compliant PLC data types (UDT) are transferred.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | INT, DINT, WORD, (S7-300, S7-400) DWORD, TIME, F-compliant PLC data type (UDT) | Source value |
| OUT1 | Output | INT, DINT, WORD, (S7-300, S7-400) DWORD, TIME, F-compliant PLC data type (UDT) | Destination address |

#### Example

The following example shows how the instruction works:

![Example](images/96739258379_DV_resource.Stream@PNG-de-DE.png)

![Example](images/96736259339_DV_resource.Stream@PNG-de-DE.png)

The instruction is always executed regardless of the signal state at enable input "EN". The instruction copies the content of operand "TagIn_Value" to operand ""F_DB_1".TagOut_Value".

### RD_ARRAY_I: Read value from INT F-array (STEP 7 Safety V19) (S7-1500)

#### Description

You use the "Read value from INT F-array" instruction to read an element from the array at the ARRAY input, which refers to the index at the INDEX input, and write its value at the OUT output. If an error occurs while accessing the array during runtime, this is displayed at the output ERROR.

The array must be created in an F-global DB and can contain only one dimension. The elements of the ARRAY must be data type INT. The following applies for the array limits in contrast:

- The low limit must be 0.
- The high limit can be 10000 maximum.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at the "EN" enable input).

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ARRAY | Input | VARIANT | Array from which is read |
| INDEX | Input | DINT | Element in the array which is read. The specification may be a constant or a tag. |
| OUT | Output | INT | Value which is read and output. |
| ERROR | Output | BOOL | Error information  The parameter ERROR is set if an error occurs during the processing of the instruction. |

#### ARRAY parameter

In addition to the direct connection with an array within a fail-safe global DB, this input can also be interconnected with an INOUT of data type ARRAY[*] of INT. This enables the decoupling of data and program logic in order, for example, to create a library function without any connection existing to a dedicated data block.

#### ERROR parameter

The table below shows the meaning of the value of the ERROR parameter:

| Symbol | Meaning |
| --- | --- |
| **Value** | **Description** |
| FALSE | No error |
| TRUE | Value at the INDEX parameter is outside the limit value of the ARRAY. |

#### Instruction versions

One version is available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | — | — | x<sup>1</sup> |  |
| <sup>1 </sup>supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Reaction to errors

If the value at the INDEX input is outside the array limits, the output ERROR = 1 is set, and the array value of the element with index = 0 is output at OUT output, regardless of the value passed at the INDEX input.

Therefore, set the value of the element with index = 0 as a fail-safe substitute value.

#### Example

The following example shows how the instruction works:

![Example](images/101419802635_DV_resource.Stream@PNG-de-DE.png)

![Example](images/101419794187_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Operand** | **Value** |
| ARRAY | "Global_DB".Array | The "Global_DB".Array operand is an ARRAY of data type Array[0..10] of INT |
| INDEX | #Tag_Index | 2 |
| OUT | #TagOut_Value | Value of the element at the location array[2] |
| ERROR | #TagError_Value | False |

The instruction "Read value from INT F-array" is always executed regardless of the signal state at enable input "EN".

The content of the 2nd element of the operand "Global_DB.Array" is output at the "#TagOut_Value" output.

### RD_ARRAY_DI: Read value from DINT F-array (STEP 7 Safety V19) (S7-1500)

#### Description

You use the "Read value from DINT F-array" instruction to read an element from the array at the ARRAY input, which refers to the index at the INDEX input, and write its value at the OUT output. If an error occurs while accessing the array during runtime, this is displayed at the output ERROR.

The array must be created in an F-global DB and can contain only one dimension. The elements of the array must be of the DINT data type. The following applies for the array limits in contrast:

- The low limit must be 0.
- The high limit can be 10000 maximum.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at the "EN" enable input).

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ARRAY | Input | VARIANT | Array from which is read |
| INDEX | Input | DINT | Element in the array which is read. The specification may be a constant or a tag. |
| OUT | Output | DINT | Value which is read and output. |
| ERROR | Output | BOOL | Error information  The parameter ERROR is set if an error occurs during the processing of the instruction. |

#### ARRAY parameter

In addition to the direct connection with an array within a fail-safe global DB, this input can also be interconnected with an INOUT of data type ARRAY[*] of DINT. This enables the decoupling of data and program logic in order, for example, to create a library function without any connection existing to a dedicated data block.

#### ERROR parameter

The table below shows the meaning of the value of the ERROR parameter:

| Symbol | Meaning |
| --- | --- |
| **Value** | **Description** |
| FALSE | No error |
| TRUE | Value at the INDEX parameter is outside the limit value of the ARRAY. |

#### Instruction versions

One version is available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | — | — | x<sup>1</sup> |  |
| <sup>1 </sup>supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Reaction to errors

If the value at the INDEX input is outside the array limits, the output ERROR = 1 is set, and the array value of the element with index = 0 is output at OUT output, regardless of the value passed at the INDEX input.

Therefore, set the value of the element with index = 0 as a fail-safe substitute value.

#### Example

The following example shows how the instruction works:

![Example](images/101255798155_DV_resource.Stream@PNG-de-DE.png)

![Example](images/101255794443_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Operand** | **Value** |
| ARRAY | "Global_DB".Array | The operand "Global_DB".Array is an ARRAY of data type Array[0..10] of DINT |
| INDEX | #Tag_Index | 2 |
| OUT | #TagOut_Value | Value of the element at the location array[2] |
| ERROR | #TagError_Value | False |

The instruction "Read value from DINT F-array" is always executed regardless of the signal state at enable input "EN".

The content of the 2nd element of the operand "Global_DB.Array" is output at the "#TagOut_Value" output.

### WR_FDB: Write value indirectly to an F-DB (STEP 7 Safety Advanced V19) (S7-300, S7-400)

#### Description

This instruction writes the value specified in input IN to the tag addressed by INI_ADDR and OFFSET in an F‑DB.

The address of the tags addressed using INI_ADDR and OFFSET must be within the address range defined by addresses INI_ADDR and END_ADDR.

If the F-CPU has gone to STOP mode with diagnostics event ID 75E2, check to determine if this condition is satisfied.

The start address of the area in an F-DB to which the value at input IN is to be written is transferred using input INI_ADDR. The associated offset in this area is transferred using input OFFSET.

The addresses transferred in input INI_ADDR or END_ADDR must point to a tag of the selected data type in an F-DB. Only tags of the selected data type are permitted between the INI_ADDR and END_ADDR addresses. The INI_ADDR address must be smaller than the END_ADDR address.

As shown in the following example, the INI_ADDR and END_ADDR addresses must be transferred fully-qualified as "DBx".DBWy or in the corresponding symbolic representation. Transfers in other forms are not permitted.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | INT, DINT | Value to be written to the F-DB |
| INI_ADDR | Input | POINTER | Start address of the area in an F-DB |
| END_ADDR | Input | POINTER | End address of the area in an F-DB |
| OFFSET | Input | INT | Offset |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Examples of parameter assignment of INI_ADDR, END_ADDR, and OFFS

| Name | Data type | Initial value | Comment |
| --- | --- | --- | --- |
| `Static` |  |  |  |
| `VAR_BOOL10` | `BOOL` | `false` |  |
| `VAR_BOOL11` | `BOOL` | `false` |  |
| `VAR_BOOL12` | `BOOL` | `false` |  |
| `VAR_BOOL13` | `BOOL` | `false` |  |
| `VAR_TIME10` | `TIME` | `T#0MS` |  |
| `VAR_TIME11` | `TIME` | `T#0MS` |  |
| `VAR_INT10` | `INT` | `0` | `<- INI_ADDR = "F-DB_1".VAR_INT10` `Example 1` |
| `VAR_INT11` | `INT` | `0` |  |
| `VAR_INT12` | `INT` | `0` |  |
| `VAR_INT13` | `INT` | `0` | `<- OFFSET = 3` |
| `VAR_INT14` | `INT` | `0` |  |
| `VAR_INT15` | `INT` | `0` | `<- END_ADDR = "F-DB_1".VAR_INT15` |
| `VAR_BOOL20` | `BOOL` | `false` |  |
| `VAR_BOOL21` | `BOOL` | `false` |  |
| `VAR_BOOL22` | `BOOL` | `false` |  |
| `VAR_BOOL23` | `BOOL` | `false` |  |
| `VAR_INT20` | `INT` | `0` | `<- INI_ADDR = "F-DB_1".VAR_INT20` `Example 2` |
| `VAR_INT21` | `INT` | `0` |  |
| `VAR_INT22` | `INT` | `0` |  |
| `VAR_INT23` | `INT` | `0` | `<- END_ADDR = "F-DB_1".VAR_INT23` |
| `VAR_INT30` | `INT` | `0` | `<- INI_ADDR = "F-DB_1".VAR_INT30` `Example 3` |
| `VAR_INT31` | `INT` | `0` | `<- OFFSET = 1` |
| `VAR_INT32` | `INT` | `0` |  |
| `VAR_INT33` | `INT` | `0` |  |
| `VAR_INT34` | `INT` | `0` | `<- END_ADDR = "F-DB".VAR_INT34` |
| `VAR_TIME20` | `TIME` | `T#0MS` |  |
| `VAR_DINT10` | `DINT` | `0` | `<- INI_ADDR = "F-DB_1".VAR_DINT10` `Example 4` |
| `VAR_DINT11` | `DINT` | `0` |  |
| `VAR_DINT12` | `DINT` | `0` | `<- OFFSET = 2` |
| `VAR_DINT13` | `DINT` | `0` | `<- END_ADDR = "F-DB_1".VAR_DINT13` |

#### Example

The following example shows how the instruction works:

![Example](images/93567266827_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93567270411_DV_resource.Stream@PNG-de-DE.png)

### RD_FDB: Read value indirectly from an F-DB (STEP 7 Safety Advanced V19) (S7-300, S7-400)

#### Description

This instruction reads the tag addressed via INI_ADDR and OFFSET in an F-DB and provides it at output OUT.

The address of the tags addressed using INI_ADDR and OFFSET must be within the address range defined by addresses INI_ADDR and END_ADDR.

If the F-CPU has gone to STOP mode with diagnostics event ID 75E2, check to determine if this condition is satisfied.

The start address of the area in an F-DB from which the tag is to be read is transferred using input INI_ADDR. The associated offset in this area is transferred using input OFFSET.

The addresses transferred in input INI_ADDR or END_ADDR must point to a tag of the selected data type in an F-DB. Only tags of the selected data type are permitted between the INI_ADDR and END_ADDR addresses. The INI_ADDR address must be smaller than the END_ADDR address.

The INI_ADDR and END_ADDR addresses must be transferred fully-qualified as "DBx".DBWy or in the corresponding symbolic representation. Transfers in other forms are not permitted. Examples of parameter assignment of INI_ADDR, END_ADDR, and OFFSET are contained in [WR_FDB: Write value indirectly to an F-DB (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#wr_fdb-write-value-indirectly-to-an-f-db-step-7-safety-advanced-v19-s7-300-s7-400).

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| INI_ADDR | Input | POINTER | Start address of the area in an F-DB |
| END_ADDR | Input | POINTER | End address of the area in an F-DB |
| OFFSET | Input | INT | Offset |
| OUT | Output | INT, DINT | Value to be read from the F-DB |

You can select the data type of the instruction in the "<???>" drop-down list in the instruction box.

#### Example

The following example shows how the instruction works:

![Example](images/93567433099_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93567436683_DV_resource.Stream@PNG-de-DE.png)

## Conversion operations

This section contains information on the following topics:

- [CONVERT: Convert value (STEP 7 Safety V19)](#convert-convert-value-step-7-safety-v19)
- [BO_W: Convert 16 data elements of data type BOOL to a data element of data type WORD (STEP 7 Safety V19)](#bo_w-convert-16-data-elements-of-data-type-bool-to-a-data-element-of-data-type-word-step-7-safety-v19)
- [W_BO: Convert a data element of data type WORD to 16 data elements of data type BOOL (STEP 7 Safety V19)](#w_bo-convert-a-data-element-of-data-type-word-to-16-data-elements-of-data-type-bool-step-7-safety-v19)
- [SCALE: Scale value (STEP 7 Safety V19)](#scale-scale-value-step-7-safety-v19)
- [SCALE_D: Scale to data type DINT (STEP 7 Safety V19) (S7-1200, S7-1500)](#scale_d-scale-to-data-type-dint-step-7-safety-v19-s7-1200-s7-1500)

### CONVERT: Convert value (STEP 7 Safety V19)

#### Description

The "Convert value" instruction reads the content of parameter IN and converts it according to the data types selected in the instruction box. The converted value is output at the OUT output .

Enable input "EN" cannot be connected. The instruction is therefore always executed (regardless of the signal state at the "EN" enable input). The connection of the "ENO" enable output is only possible and required when converting from the "DINT" to the "INT" data type.

> **Note**
>
> When converting from "DINT" to the "INT" data type, you need to connect the ENO enable output and thereby programming overflow detection.
>
> Note the following:
>
> - If the value at the input is outside the INT range, ENO returns 0.
> - The result of the instruction reacts like the analogous instruction in a standard block.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ENO | Output | BOOL | Enable output |
| IN | Input | INT, DINT | Value to be converted. |
| OUT | Output | INT, DINT | Result of the conversion |

You can select the data types of the instruction in the "<???>" drop-down lists of the instruction box. The supported conversions are from "INT to DINT" and "DINT to INT".

#### Example

The following example shows how the "Convert value "DINT to INT"" instruction for S7-1200/1500 F-CPUs works:

![Example](images/102789763851_DV_resource.Stream@PNG-de-DE.png)

![Example](images/102789759755_DV_resource.Stream@PNG-de-DE.png)

The instruction is always executed regardless of the signal state at enable input EN.

The value of the "TagIn_Value" operand is converted to an integer (16-bit) and the result is stored in the ""F_DB_1".TagOut_Value" operand.

When no overflow occurs during execution of the "Convert value "DINT to INT"" instruction, the ENO enable output has the signal state "1" and the "TagOut" operand is set.

You can also store the signal status of the ENO enable output in an (F-)DB, and centrally evaluate whether overflows have occurred for all or one group of instructions with overflow detection.

### BO_W: Convert 16 data elements of data type BOOL to a data element of data type WORD (STEP 7 Safety V19)

#### Description

This instruction converts the 16 values of data type BOOL at inputs IN0 to IN15 to a value of data type WORD, which is made available at output OUT. The conversion takes place as follows: The i-th bit of the WORD value is set to 0 (or 1), if the value at input INi = 0 (or 1).

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN0 | Input | BOOL | Bit 0 of WORD value |
| IN1 | Input | BOOL | Bit 1 of WORD value |
| ... |  |  | ... |
| IN15 | Input | BOOL | Bit 15 of WORD value |
| OUT | Output | WORD | WORD value consisting of IN0 to IN15 |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | o | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| o This version is no longer supported.   <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93605819787_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93604536203_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN0 | TagValue_0 | FALSE |
| IN1 | TagValue_1 | FALSE |
| ... |  | ... |
| IN13 | TagValue_13 | FALSE |
| IN14 | TagValue_14 | TRUE |
| IN15 | TagValue_15 | TRUE |
| OUT | "F_DB_1".Result | W#16#C000 |

The values of operands "TagValue_0" to "TagValue_15" are combined into a value of the data type WORD and assigned to operand ""F_DB_1".TagResult".

### W_BO: Convert a data element of data type WORD to 16 data elements of data type BOOL (STEP 7 Safety V19)

#### Description

This instruction converts the value of data type WORD at input IN to 16 values of data type BOOL, which are provided at outputs OUT0 to OUT15. The conversion takes place as follows: Output OUTi is set to 0 (or 1), if the i-th bit of the WORD value is 0 (or 1).

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | WORD | WORD value |
| OUT0 | Output | BOOL | Bit 0 of WORD value |
| OUT1 | Output | BOOL | Bit 1 of WORD value |
| ... |  |  | ... |
| OUT15 | Output | BOOL | Bit 15 of WORD value |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | o | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| o This version is no longer supported.   <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93606393867_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93606390283_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | "F_DB_1".TagValue | W#16#C000 |
| OUT0 | TagOUT_0 | FALSE |
| OUT1 | TagOUT_1 | FALSE |
| ... |  | ... |
| OUT13 | TagOUT_13 | FALSE |
| OUT14 | TagOUT_14 | TRUE |
| OUT15 | TagOUT_15 | TRUE |

The value of operand ""F_DB_1".TagValue" of data type WORD is converted to the 16 values "TagOUT_0" to "TagOUT_15" of data type BOOL.

### SCALE: Scale value (STEP 7 Safety V19)

#### Description

This instruction scales the value at input IN in physical units between the low limit value at input LO_LIM and the high limit value at input HI_LIM. It is assumed that the value at input IN is between 0 and 27648. The scaling result is provided at output OUT.

The instruction uses the following equation:

OUT = [ IN × (HI_LIM – LO_LIM) ] / 27648 + LO_LIM

As long as the value at input IN is greater than 27648, output OUT is linked to HI_LIM and OUT_HI is set to 1.

As long as the value at input IN is less than 0, output OUT is linked to LO_LIM and OUT_LO is set to 1.

For inverse scaling, you must assign LO_LIM > HI_LIM. With inverse scaling, the output value at output OUT decreases while the input value at input IN increases.

Every call of the "Scale value" instruction must be assigned a data area in which the instruction data is stored. In addition, when the instruction is inserted in the program, the "Call options" dialog is automatically opened, where you can create a data block (single instance) (e.g., SCALE_DB_1) or a multi-instance (e.g., SCALE_Instance_1) for the "Scale value" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | INT | Input value to be scaled in physical units |
| HI_LIM | Input | INT | High limit value of value range of OUT |
| LO_LIM | Input | INT | Low limit value of value range of OUT |
| OUT | Output | INT | Result of scaling |
| OUT_HI | Output | BOOL | 1 = Input value > 27648: OUT = HI_LIM |
| OUT_LO | Output | BOOL | 1 = Input value < 0: OUT = LO_LIM |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Behavior in the event of overflow or underflow of analog values and fail‑safe value output

> **Note**
>
> If inputs from the PII of an SM 336; AI 6 x 13Bit or SM 336; F-AI 6 x 0/4 ... 20 mA HART are used as input values, note that the F‑system detects an overflow or underflow of a channel of this F‑SM as an F‑I/O fault or channel fault. The fail-safe value 0 is provided in place of 7FFF<sub>H</sub> (for overflow) or 8000<sub>H</sub> (for underflow) in the PII for the safety program.
>
> If other fail-safe values should be output in this case, you need to evaluate the QBAD signal of the associated F-I/O or QBAD_I_xx signal / value status of the corresponding channel.
>
> If the value in the PII of the F‑SM is within the overrange or underrange, but is > 27648 or < 0, you can likewise branch to the output of an individual fail‑safe value by evaluating outputs OUT_HI and OUT_LO, respectively.

#### Example

The following example shows how the instruction works:

![Example](images/93597077259_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93597073675_DV_resource.Stream@PNG-de-DE.png)

When operand "TagIn_Value" = 20000, the result for ""F_DB_1".TagOut_Value" is 361.

### SCALE_D: Scale to data type DINT (STEP 7 Safety V19) (S7-1200, S7-1500)

#### Description

This instruction scales the value at input IN in physical units between the low limit value at input LO_LIM and the high limit value at input HI_LIM. It is assumed that the value at input IN is between 0 and 27648. The scaling result is provided at output OUT.

The instruction uses the following equation:

OUT = [ IN × (HI_LIM – LO_LIM) ] / 27648 + LO_LIM

As long as the value at input IN is greater than 27648, output OUT is linked to HI_LIM and OUT_HI is set to 1.

As long as the value at input IN is less than 0, output OUT is linked to LO_LIM and OUT_LO is set to 1.

For inverse scaling, you must assign LO_LIM > HI_LIM. With inverse scaling, the output value at output OUT decreases while the input value at input IN increases.

Every call of the "Scale value to data type DINT" instruction must be assigned a data area in which the instruction data is stored. In addition, when the instruction is inserted in the program, the "Call options" dialog is automatically opened, where you can create a data block (single instance) (e.g., SCALE_D_DB_1) or a multi-instance (e.g., SCALE_D_Instance_1) for the "Scale value to data type DINT" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | INT | Input value to be scaled in physical units |
| HI_LIM | Input | DINT | High limit value of value range of OUT |
| LO_LIM | Input | DINT | Low limit value of value range of OUT |
| OUT | Output | DINT | Result of scaling |
| OUT_HI | Output | BOOL | 1 = Input value > 27648: OUT = HI_LIM |
| OUT_LO | Output | BOOL | 1 = Input value < 0: OUT = LO_LIM |

#### Instruction versions

One version is available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 2.0 | — | x<sup>1</sup> | x<sup>2</sup> |  |
| <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Behavior in the event of overflow or underflow of analog values and fail‑safe value output

> **Note**
>
> If inputs from the PII of an SM 336; AI 6 x 13Bit or SM 336; F-AI 6 x 0/4 ... 20 mA HART are used as input values, note that the F‑system detects an overflow or underflow of a channel of this F‑SM as an F‑I/O fault or channel fault. The fail-safe value 0 is provided in place of 7FFF<sub>H</sub> (for overflow) or 8000<sub>H</sub> (for underflow) in the PII for the safety program.
>
> If other fail-safe values should be output in this case, you need to evaluate the QBAD signal of the associated F-I/O or QBAD_I_xx signal / value status of the corresponding channel.
>
> If the value in the PII of the F‑SM is within the overrange or underrange, but is > 27648 or < 0, you can likewise branch to the output of an individual fail‑safe value by evaluating outputs OUT_HI and OUT_LO, respectively.

#### Example

The following example shows how the instruction works:

![Example](images/128289019147_DV_resource.Stream@PNG-de-DE.png)

![Example](images/128289026571_DV_resource.Stream@PNG-de-DE.png)

When the operand "TagIn_Value" = 20000, the result for ""F_DB_1".TagOut_Value" is 72337.

## Program control operations

This section contains information on the following topics:

- [JMP: Jump if RLO = 1 (STEP 7 Safety V19)](#jmp-jump-if-rlo-1-step-7-safety-v19)
- [JMPN: Jump if RLO = 0 (STEP 7 Safety V19)](#jmpn-jump-if-rlo-0-step-7-safety-v19)
- [LABEL: Jump label (STEP 7 Safety V19)](#label-jump-label-step-7-safety-v19)
- [RET: Return (STEP 7 Safety V19)](#ret-return-step-7-safety-v19)
- [OPN: Open global data block (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#opn-open-global-data-block-step-7-safety-advanced-v19-s7-300-s7-400)

### JMP: Jump if RLO = 1 (STEP 7 Safety V19)

#### Description

You can use the "Jump if RLO = 1" instruction to interrupt the linear execution of the program and resume it in another network. The destination network must be identified by a [jump label](#label-jump-label-step-7-safety-v19) (LABEL). The description of the jump label is specified in the placeholder above the instruction.

The specified jump label must be in the same block in which the instruction is executed. The name you specify can only occur once in the block.

If the result of logic operation (RLO) at the input of the instruction is "1" or the input is not connected, the jump to the network identified by the jump label is executed. The jump direction can be towards higher or lower network numbers.

If the result of logic operation (RLO) at the input of the instruction is "0", the program continues executing in the next network.

> **Note**
>
> (S7-1200, S7-1500)  
> If the jump destination (jump label) for an instruction "JMP" or "JMPN" is above the associated instruction "JMP" or "JMPN" (backwards jump), you cannot insert any other instructions for program control (JMP, JMPN, RET, jump label) between them.   
> **Exception:** You can insert an instruction "JMP" or "JMPN" between them if you also insert the associated jump destination in between as well as below the associated instruction "JMP" or "JMPN" (forward jump).  
> Non-compliance can lead to compilation errors or to the F-CPU going to STOP.

> **Note**
>
> You are not permitted to insert any SENDDP or SENDS7 instructions between an instruction JMP or JMPN and the associated jump destination (jump label).

#### Example

The following example shows how the instruction works:

![Example](images/96279160971_DV_resource.Stream@PNG-en-US.png)

![Example](images/96279131275_DV_resource.Stream@PNG-en-US.png)

When operand "TagIn_1" has signal state "1", the "Jump if RLO = 1" instruction is executed. The linear execution of the program is interrupted and continues in Network 3, which is identified by the jump label CAS1. When input "TagIn_3" has signal state "1", output "TagOut_3" is reset.

### JMPN: Jump if RLO = 0 (STEP 7 Safety V19)

#### Description

You can use the "Jump if RLO = 0" instruction to interrupt the linear execution of the program and resume it in another network, when the result of logic operation at the input of the instruction is "0". The destination network must be identified by a [jump label](#label-jump-label-step-7-safety-v19) (LABEL). The description of the jump label is specified in the placeholder above the instruction.

The specified jump label must be in the same block in which the instruction is executed. The name you specify can only occur once in the block.

If the result of logic operation (RLO) at the input of the instruction is "0", the jump to the network identified by the jump label is executed. The jump direction can be towards higher or lower network numbers.

If the result of logic operation (RLO) at the input of the instruction is "1", the program continues executing in the next network.

> **Note**
>
> (S7-1200, S7-1500)  
> If the jump destination (jump label) for an instruction "JMP" or "JMPN" is above the associated instruction "JMP" or "JMPN" (backwards jump), you cannot insert any other instructions for program control (JMP, JMPN, RET, jump label) between them.   
> **Exception:** You can insert an instruction "JMP" or "JMPN" between them if you also insert the associated jump destination in between as well as below the associated instruction "JMP" or "JMPN" (forward jump).  
> Non-compliance can lead to compilation errors or to the F-CPU going to STOP.

> **Note**
>
> You are not permitted to insert any SENDDP or SENDS7 instructions between an instruction JMP or JMPN and the associated jump destination (jump label).

#### Example

The following example shows how the instruction works:

![Example](images/96279849867_DV_resource.Stream@PNG-en-US.png)

![Example](images/96279845771_DV_resource.Stream@PNG-en-US.png)

When operand "TagIn_1" has signal state "0", the "Jump if RLO = 0" instruction is executed. The linear execution of the program is interrupted and continues in Network 3, which is identified by the jump label CAS1. When input "TagIn_3" has signal state "1", output "TagOut_3" is reset.

### LABEL: Jump label (STEP 7 Safety V19)

#### Description

You can use a jump label to specify a destination network, in which the program execution should resume after a jump.

The jump label and the instruction in which the jump label is specified must be located in the same block. The name of a jump label can only be assigned once in a block.

Only one jump label can be placed in a network. To each jump label can be jumped from several locations.

#### Example

The following example shows how the instruction works:

![Example](images/93597458315_DV_resource.Stream@PNG-en-US.png)

![Example](images/93597454091_DV_resource.Stream@PNG-en-US.png)

When operand "TagIn_1" has signal state "1", the "Jump if RLO = 1" instruction is executed. The linear execution of the program is interrupted and continues in Network 3, which is identified by the jump label CAS1. When input "TagIn_3" has signal state "1", output "TagOut_3" is reset.

---

**See also**

[JMP: Jump if RLO = 1 (STEP 7 Safety V19)](#jmp-jump-if-rlo-1-step-7-safety-v19)
  
[JMPN: Jump if RLO = 0 (STEP 7 Safety V19)](#jmpn-jump-if-rlo-0-step-7-safety-v19)
  
[RET: Return (STEP 7 Safety V19)](#ret-return-step-7-safety-v19)

### RET: Return (STEP 7 Safety V19)

#### Description

You can use the "Return" instruction to stop the processing of a block.

If the result of logic operation (RLO) at the input of the "Return" instruction is "1" or the box input of the S7-1200/1500 F-CPUs is not connected in FBD, program execution is terminated in the currently called block and continued in the calling block (for example, in the main safety block) after the call function. If the RLO at the input of the "Return" instruction is "0", the instruction is not executed. Program execution continues in the next network of the called block.

Influencing the status of the call function (ENO) is irrelevant, because the enable output "ENO" cannot be connected.

> **Note**
>
> (S7-300, S7-400) You may not program a RET instruction in the main safety block.

#### Example

The following example shows how the instruction works:

![Example](images/93597745035_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93597677067_DV_resource.Stream@PNG-de-DE.png)

When the "TagIn" operand delivers signal state "1", the "Return" instruction is executed. Program execution is terminated in the called block and continues in the calling block.

---

**See also**

[JMP: Jump if RLO = 1 (STEP 7 Safety V19)](#jmp-jump-if-rlo-1-step-7-safety-v19)
  
[JMPN: Jump if RLO = 0 (STEP 7 Safety V19)](#jmpn-jump-if-rlo-0-step-7-safety-v19)
  
[LABEL: Jump label (STEP 7 Safety V19)](#label-jump-label-step-7-safety-v19)

### OPN: Open global data block (STEP 7 Safety Advanced V19) (S7-300, S7-400)

#### Description

You can use the "Open global data block" instruction to open a data block. The number of the data block is transferred to the DB register. Subsequent DB commands access the relevant blocks depending on the register contents.

> **Note**
>
> Note when using the "Open global data block" instruction that the content of the DB register can be changed after calls of F‑FB/F‑FC and "fully qualified DB accesses", such that there is no guarantee that the last data block you opened with "Open global data block" is still open.
>
> You should therefore use the following method for addressing data to avoid errors when accessing data of the DB register:
>
> - Use symbolic addressing.
> - Use only fully qualified DB accesses.
>
> If you still want to use the "Open global data block" operation, you must ensure that the DB register is restored by repeating the "Open global data block" instruction following calls of F-FB/F-FC and "fully qualified DB accesses." Otherwise, a malfunction could result.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| <Data block> | Input | BLOCK_DB | Data block that is opened |

#### "Fully qualified DB access"

The initial access to data of a data block in an F-FB/F-FC must always be a "fully qualified DB access," or it must be preceded by the "Open global data block" instruction. This also applies to the initial access to data of a data block after a jump label.

An example of "fully qualified DB access" and "non-fully qualified DB access" is provided in [Restrictions in the programming languages FBD/LAD](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#restrictions-in-the-programming-languages-fbdlad).

#### Access to instance DBs

You can also access instance DBs of F‑FBs with fully qualified access, e.g., for transfer of block parameters. It is not possible to access static local data in single/multi-instances of other F-FBs.

Note that accessing instance DBs of F‑FBs that are not called in the safety program can cause the F-CPU to go to STOP mode.

#### Example

The following example shows how the instruction works:

![Example](images/96302845963_DV_resource.Stream@PNG-en-US.png)

![Example](images/96302850059_DV_resource.Stream@PNG-en-US.png)

The "Motor_DB" data block is called in network 1. The number of the data block is transferred to the DB register. The "DBX0.0" operand is queried in network 2. The signal state of the "DBX0.0" operand is assigned to the "Tag_Output" operand.

## Word logic operations

This section contains information on the following topics:

- [AND: AND logic operation (STEP 7 Safety V19)](#and-and-logic-operation-step-7-safety-v19)
- [OR: OR logic operation (STEP 7 Safety V19)](#or-or-logic-operation-step-7-safety-v19)
- [XOR: EXCLUSIVE OR logic operation (STEP 7 Safety V19)](#xor-exclusive-or-logic-operation-step-7-safety-v19)

### AND: AND logic operation (STEP 7 Safety V19)

#### Description

You can use the "AND logic operation" instruction to combine the value at input IN1 to the value at input IN2 bit-by-bit by AND logic and query the result at output OUT.

When the instruction is executed, bit 0 of the value at input IN1 and bit 0 of the value at input IN2 are ANDed. The result is stored in bit 0 of output OUT. The same logic operation is executed for all other bits of the specified values.

The result bit has signal state "1" only when both of the bits in the logic operation also have signal state "1". If one of the two bits of the logic operation has signal state "0", the corresponding result bit is reset.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | WORD | First value of logic operation |
| IN2 | Input | WORD | Second value of logic operation |
| OUT | Output | WORD | Result of the instruction |

#### Example

The following example shows how the instruction works:

![Example](images/93598213515_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93598319755_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| IN1 | `"Tag_Value1" = 01010101 01010101` |
| IN2 | `"Tag_Value2" = 00000000 00001111` |
| OUT | `"F_DB_1"."Tag_Result" = 00000000 00000101` |

The instruction is always executed regardless of the signal state at enable input "EN". The value of the "Tag_Value1" operand and the value of the "Tag_Value2" operand are ANDed. The result is mapped bit-by-bit and output in the ""F_DB_1".Tag_Result" operand.

### OR: OR logic operation (STEP 7 Safety V19)

#### Description

You can use the "OR logic operation" instruction to connect the value at input IN1 input to the value at input IN2 bit-by-bit by OR logic and query the result at output OR.

When the instruction is executed, bit 0 of the value at input IN1 and bit 0 of the value at input IN2 are ORed. The result is stored in bit 0 of output OUT. The same logic operation is executed for all bits of the specified tags.

The result bit has signal state "1" when at least one of the two bits in the logic operation has signal state "1". If both of the bits of the logic operation have signal state "0", the corresponding result bit is reset.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | WORD | First value of logic operation |
| IN2 | Input | WORD | Second value of logic operation |
| OUT | Output | WORD | Result of the instruction |

#### Example

The following example shows how the instruction works:

![Example](images/93598355851_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93598590091_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| IN1 | `"Tag_Value1" = 01010101 01010101` |
| IN2 | `"Tag_Value2" = 00000000 00001111` |
| OUT | `"F_DB_1"."Tag_Result" = 01010101 01011111` |

The instruction is always executed regardless of the signal state at enable input "EN". The value of the "Tag_Value1" operand and the value of the "Tag_Value2" operand are ORed. The result is mapped bit-by-bit and output in the ""F_DB_1".Tag_Result" operand.

### XOR: EXCLUSIVE OR logic operation (STEP 7 Safety V19)

#### Description

You can use the "EXCLUSIVE OR logic operation" instruction to combine the value at input IN1 and the value at input IN2 bit-by-bit by EXCLUSIVE OR logic and query the result at output OUT.

When the instruction is executed, bit 0 of the value at input IN1 input and bit 0 of the value at input IN2 are logically combined by EXCLUSIVE OR. The result is stored in bit 0 of output OUT. The same logic operation is executed for all other bits of the specified value.

The result bit has signal state "1" when one of the two bits in the logic operation has signal state "1". If both of the bits of the logic operation have signal state "1" or "0", the corresponding result bit is reset.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN1 | Input | WORD | First value of logic operation |
| IN2 | Input | WORD | Second value of logic operation |
| OUT | Output | WORD | Result of the instruction |

#### Example

The following example shows how the instruction works:

![Example](images/93598624395_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93598641035_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| IN1 | `"Tag_Value1" = 01010101 01010101` |
| IN2 | `"Tag_Value2" = 00000000 00001111` |
| OUT | `"F_DB_1"."Tag_Result" = 01010101 01011010` |

The instruction is always executed regardless of the signal state at enable input "EN". The value of the "Tag_Value1" operand and the value of the "Tag_Value2" operand are logically combined by EXCLUSIVE OR. The result is mapped bit-by-bit and output in the ""F_DB_1".Tag_Result" operand.

## Shift and rotate

This section contains information on the following topics:

- [SHR: Shift right (STEP 7 Safety V19)](#shr-shift-right-step-7-safety-v19)
- [SHL: Shift left (STEP 7 Safety V19)](#shl-shift-left-step-7-safety-v19)

### SHR: Shift right (STEP 7 Safety V19)

#### Description

Use the "Shift right" instruction to shift the content of the operand at input IN bit-by-bit to the right and query the result at output OUT. Use input N to specify the number of bit positions by which the specified value is to be moved.

If the value at input N is "0", the value at input IN is copied to the operand at output OUT.

If the value at input N is greater than the number of available bit positions, the operand value at input IN is shifted to the right by the available number of bit positions.

The bit locations that are freed up in the left area of the operand during the shift operation are filled with zeros.

The following figure shows how the content of an operand of data type WORD is moved by 6 bit positions to the right:

![Description](images/22780120843_DV_resource.Stream@PNG-en-US.png)

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

> **Note**
>
> S7-300/400:
>
> Only the low-byte is evaluated from input N.
>
> S7-1200/1500:
>
> If the value at input N < 0, the output OUT is set to 0.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | WORD | Value that is shifted |
| N | Input | INT | Number of bit positions by which the value is shifted |
| OUT | Output | WORD | Result of the instruction |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | o | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| o This version is no longer supported.   <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93599076363_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93598714379_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | "F_DB_1".TagIn_Value | `0011 1111 1010 1111` |
| N | Tag_Number | 3 |
| OUT | "F_DB_1".TagOut_Value | `0000 0111 1111 0101` |

The instruction is always executed regardless of the signal state at enable input "EN". The content of the operand ""F_DB_1".TagIn_Value" is moved three bit positions to the right. The result is output at output ""F_DB_1".TagOut_Value".

### SHL: Shift left (STEP 7 Safety V19)

#### Description

Use the "Shift left" instruction to shift the content of the operand at input IN bit-by-bit to the left and query the result at output OUT. Use input N to specify the number of bit positions by which the specified value is to be moved.

If the value at input N is "0", the value at input IN is copied to the operand at output OUT.

If the value at input N is greater than the number of available bit positions, the operand value at input IN is shifted to the left by the available number of bit positions.

The bit positions that are freed up in the right area of the operand during the shift operation are filled with zeros.

The following figure shows how the content of an operand of data type WORD is moved by 6 bit positions to the left:

![Description](images/18386585995_DV_resource.Stream@PNG-en-US.png)

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

> **Note**
>
> S7-300/400:
>
> Only the low-byte is evaluated from input N.
>
> S7-1200/1500:
>
> If the value at input N < 0, the output OUT is set to 0.

#### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | Input | WORD | Value that is shifted |
| N | Input | INT | Number of bit positions by which the value is shifted |
| OUT | Output | WORD | Result of the instruction |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | o | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | — | o |  |
| 1.3 | x | o | o |  |
| 1.4 | x | x | x |  |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| o This version is no longer supported.   <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Example

The following example shows how the instruction works:

![Example](images/93604247307_DV_resource.Stream@PNG-de-DE.png)

![Example](images/93604192523_DV_resource.Stream@PNG-de-DE.png)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | "F_DB_1".TagIn_Value | `0011 1111 1010 1111` |
| N | Tag_Number | 4 |
| OUT | "F_DB_1".TagOut_Value | `1111 1010 1111 0000` |

The instruction is always executed regardless of the signal state at enable input "EN". The content of the operand ""F_DB_1".TagIn_Value" is moved four bit positions to the left. The result is output at output ""F_DB_1".TagOut_Value".

## Operating

This section contains information on the following topics:

- [ACK_OP: Fail-safe acknowledgment (STEP 7 Safety V19)](#ack_op-fail-safe-acknowledgment-step-7-safety-v19)

### ACK_OP: Fail-safe acknowledgment (STEP 7 Safety V19)

#### Description (S7-300, S7-400)

This instruction enables fail‑safe acknowledgment from an operator control and monitoring system. It allows, for example, reintegration of F‑I/O to be controlled from the operator control and monitoring system. Acknowledgment takes place in two steps:

- Input/output parameter IN changes to a value of 6 for exactly one cycle.
- Input/output parameter IN changes to a value of 9 within a minute for exactly one cycle

Once the in/out parameter IN has changed to a value of 6, the instruction evaluates whether this parameter has changed to a value of 9 after 1 second, at the earliest, or one minute, at the latest. Output OUT (output for acknowledgment) is then set to 1 for one cycle.

If an invalid value is input or if in/out parameter IN has not changed to the value 9 within one minute or the change occurred before one second has elapsed, then in/out parameter IN is reset to 0, and both steps listed above must be repeated.

During the time in which in/out parameter IN must change from 6 to the value 9, output Q is set to 1. Otherwise, Q has a value of 0.

Every call of the "Fail-safe acknowledgment" instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., ACK_OP_DB_1) or a multi-instance (e.g., ACK_OP_Instance_1) for the "Fail-safe acknowledgment" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

> **Note**
>
> A separate data area must be used for each call of ACK_OP. Each call can be processed only once in an F-runtime group cycle.
>
> If this is not observed, the behavior described under "Description" is no longer ensured.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The two acknowledgment steps must **not** be triggered by one single operation, for example, by programming them including the time conditions and using one function key to trigger them.  The two separate acknowledgment steps also prevent an erroneous triggering of an acknowledgment, for example, by your non-fail-safe operator control and monitoring system. (S013) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you have operator control and monitoring systems and F‑CPUs that are interconnected and use the ACK_OP instruction for fail-safe acknowledgment, you need to ensure that the intended F‑CPU will be addressed **before** you perform the two acknowledgment steps.  - To do this, store a network-wide* unique name for the F-CPU in a DB of your standard user program in each F-CPU. - In your operator control and monitoring system, set up a text box from which you can read out the F‑CPU name from the DB online before executing the two acknowledgment steps. - Optional:    In your operator control and monitoring system, set up a text box to permanently store the F‑CPU name. Then, you can determine whether the intended F‑CPU is being addressed by simply comparing the F‑CPU name read out online with the permanently stored designation. (S014) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet.

> **Note**
>
> You can read out output Q by means of operator control and monitoring systems or, if applicable, evaluate it in your standard user program.
>
> You can provide the in/out parameter IN with a separate memory word or DBW of a DB of the standard user program supply for each call of the ACK_OP instruction.

> **Note**
>
> The configuration of your operator control and monitoring system does not have any effect on the Collective F-Signature.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Description (S7-1200, S7-1500)

This instruction enables fail‑safe acknowledgment from an operator control and monitoring system. It allows, for example, reintegration of F‑I/O to be controlled from the operator control and monitoring system. Acknowledgment takes place in two steps:

- Input/output parameter IN changes to a value of 6 for exactly one cycle.
- Input/output parameter IN changes to the value at the ACK_ID input within a minute for exactly one cycle

Once the in/out parameter IN has changed to a value of 6, the instruction evaluates whether this parameter has changed to a value at the ACK_ID input after 1 second, at the earliest, or one minute, at the latest. Output OUT (output for acknowledgment) is then set to 1 for one cycle.

If an invalid value is input or if in/out parameter IN has not changed to the value at the ACK_ID input within one minute or the change occurred before one second has elapsed, then in/out parameter IN is reset to 0, and both steps listed above must be repeated.

During the time in which in/out parameter IN must change from 6 to the value at the ACK_ID input, output Q is set to 1. Otherwise, Q has a value of 0.

Every call of the "Fail-safe acknowledgment" instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., ACK_OP_DB_1) or a multi-instance (e.g., ACK_OP_Instance_1) for the "Fail-safe acknowledgment" instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

> **Note**
>
> A separate data area must be used for each call of ACK_OP. Each call can be processed only once in an F-runtime group cycle.
>
> If this is not observed, the behavior described under "Description" is no longer ensured.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The two acknowledgment steps must **not** be triggered by one single operation, for example, by programming them including the time conditions and using one function key to trigger them.  The two separate acknowledgment steps also prevent an erroneous triggering of an acknowledgment, for example, by your non-fail-safe operator control and monitoring system. (S013) |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| If you have operator control and monitoring systems and F‑CPUs that are interconnected and use the ACK_OP instruction for fail-safe acknowledgment, you need to ensure that the intended F‑CPU will be addressed **before** you perform the two acknowledgment steps.  Alternative 1:  - The value for each identifier of the acknowledgment (ACK_ID input; data type: INT) can be freely selected in the range from 9 to 30000, but must be unique network-wide* for all instances of the ACK_OP instruction. You must supply the ACK_ID input with constant values when calling the instruction. Direct read or write access to the ACK_ID tag in the associated instance DB is not permitted!   Alternative 2:  - Store a network-wide* unique name for the F-CPU in a DB of your standard user program in each F-CPU. - In your operator control and monitoring system, set up a text box from which you can read out the F‑CPU name from the DB online before executing the two acknowledgment steps. - Optional:    In your operator control and monitoring system, set up a text box to permanently store the F‑CPU name. Then, you can determine whether the intended F‑CPU is being addressed by simply comparing the F‑CPU name read out online with the permanently stored designation. (S047) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet.

> **Note**
>
> You can read out output Q by means of operator control and monitoring systems or, if applicable, evaluate it in your standard user program.
>
> You need to provide the in/out parameter IN with a separate memory word or DBW of a DB of the standard user program for each call of the ACK_OP instruction.

> **Note**
>
> The supply of the IN input/output of the ACK_OP instruction as well as the configuration of your operator control and monitoring system do not have any effect on the Collective F-Signature, the Collective F-SW-Signature or the signature of the block that calls the ACK_OP instruction.
>
> Changes to the supply of the IN input/output or to the configuration of your operator control and monitoring system therefore do not result in a changed Collective F-Signature/Collective F-SW-Signature/signature of the calling block.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| When using an instruction with time processing, take the following timing imprecision sources into account when determining your response times:  - The temporal blurring known from the standard user program, which is caused by the cyclic processing - Timing imprecision resulting from the update time of the time base used in the instruction (see figure in section "Timing imprecision resulting from the update time of the time base used in the instruction") - Tolerance of internal time monitoring in the F‑CPU   - For time values up to 200 ms, a maximum of 4 ms   - For time values greater than or equal to 200 ms, a maximum of 2% of the (assigned) time value - Tolerance of internal time monitoring in the S7-1500 HF‑CPU   - For time values up to 500 ms, a maximum of 10 ms   - For time values greater than or equal to 500 ms, a maximum of 2% of the (assigned) time value   You must choose the interval between two calls of an instruction with time processing in such a way that the required response times are achieved, taking into account the possible timing imprecision. (S034) |  |

#### Parameters (S7-300, S7-400)

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| IN | InOut | INT | Input variable from operator control and monitoring system |
| OUT | Output | BOOL | Output for acknowledgment |
| Q | Output | BOOL | Time status |

#### Parameters (S7-1200, S7-1500)

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ACK_ID | Input | INT | Identifier of the acknowledgment (9 to 30000) |
| IN | InOut | INT | Input variable from operator control and monitoring system |
| OUT | Output | BOOL | Output for acknowledgment |
| Q | Output | BOOL | Time status |

#### Instruction versions

A number of versions are available for this instruction:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | x | — | o | These versions have identical functions to version 1.0 for S7-300/400 F-CPUs.  The input ACK_ID must also be taken into consideration for S7-1200/1500 F-CPUs. |
| 1.2 | x | o | o |  |
| 1.3 | x | x | x |  |
| o This version is no longer supported. |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

#### Timing imprecision resulting from the update time of the time base used in the instruction:

![Timing imprecision resulting from the update time of the time base used in the instruction:](images/169854665355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | For the first call in cycle n+1, the call time of the instruction relative to the start of the F‑runtime group is earlier than that in cycle n by the amount of Δ<sub>1</sub>, e.g. because parts of the safety program of the F‑runtime group before the call time of the instruction in cycle n+1 are skipped. For the time update, the instruction takes account of time T<sub>Base_1</sub> instead of the time T<sub>1</sub> that has actually elapsed in cycle n since the call. |
| ② | The instruction is called a second time in cycle n+1. This does not involve another time update (by Δ<sub>2</sub>). |
| ③ | For the call in cycle n+2, the call time of the instruction relative to the start of the F‑runtime group is later than that in cycle n by the amount of Δ<sub>3</sub>, e.g. because the F‑runtime group was interrupted by a higher priority interrupt before the call time of the instruction in cycle n+2. The instruction took into account time T<sub>Base_1</sub> + T<sub>Base_2 </sub> instead of the time T<sub>3</sub> that has actually elapsed in cycle n since the call. This would also be the case if no call occurred in cycle n+1. |

#### Example

An example how the instruction is used is available under [Implementing User Acknowledgment in the Safety Program of the F-CPU of a DP Master or IO controller](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-dp-master-or-io-controller).

---

**See also**

[Implementing user acknowledgment in the safety program of the F-CPU of a I-slave or I-device](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementing-user-acknowledgment-in-the-safety-program-of-the-f-cpu-of-a-i-slave-or-i-device)

## Additional instructions

This section contains information on the following topics:

- [LAD](#lad-2)
- [FBD](#fbd-2)

### LAD

This section contains information on the following topics:

- [---| |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)
- [---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-negated-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400)

#### ---|   |--- OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)

##### Description

You can use the "Get status bit OV" instruction to detect whether a number range overflow occurred in the last arithmetic instruction processed.

The "Get status bit OV" instruction functions like a normally open contact. If the query is fulfilled, the instruction has signal state "1". If the query is not fulfilled, the instruction has signal state "0".

The "Get status bit OV" evaluation must be inserted in the network that follows the instruction that influences the OV. This network must not contain any jump labels.

> **Note**
>
> The execution time of the OV-affecting instruction is extended when the "Get status bit OV " instruction is used (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).

##### Example

The following example shows how the instruction works:

![Example](images/102770228363_DV_resource.Stream@PNG-en-US.png)

The "Add" instruction is always executed (regardless of the signal state at enable input EN).

The value of the "Tag_Value1" operand is added to value of the Tag_Value2 operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

If an overflow occurs during execution of the "Add" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

#### ---| / |--- OV: Get negated status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)

##### Description

You can use the "Get negated status bit OV" instruction to detect whether a number range overflow occurred in the last arithmetic instruction processed. This instruction is only available in LAD.

The "Get negated status bit OV" instruction functions like a normally closed contact. If the query is satisfied, the instruction has signal state "0". If the query is not satisfied, the instruction has signal state "1".

The "Get negated status bit OV" evaluation must be inserted in the network following the instruction that influences the OV. This network must not contain any jump labels.

> **Note**
>
> The execution time of the OV-affecting instruction is extended when the "Get negated status bit OV " instruction is used (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).

##### Example

The following example shows how the instruction works:

![Example](images/93501419275_DV_resource.Stream@PNG-en-US.png)

The "Add" instruction is always executed (regardless of the signal state at enable input EN).

The value of the "Tag_Value1" operand is added to value of the Tag_Value2 operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

If an overflow does not occur during execution of the "Add" instruction, the status bit OV is reset to "0". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

### FBD

This section contains information on the following topics:

- [OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#ov-get-status-bit-ov-step-7-safety-advanced-v19-s7-300-s7-400-1)

#### OV: Get status bit OV (STEP 7 Safety Advanced V19) (S7-300, S7-400)

##### Description

You can use the "Get status bit OV" instruction to detect whether a number range overflow occurred in the last arithmetic instruction processed.

The "Get status bit OV" evaluation must be inserted in the network that follows the instruction that influences the OV. This network must not contain any jump labels.

If the query is fulfilled, the instruction has signal state "1". If the query is not fulfilled, the instruction has signal state "0".

You can program a query of status bit OV for "0" with the "Invert RLO" instruction.

> **Note**
>
> The execution time of the OV-affecting instruction is extended when the "Get status bit OV " instruction is used (see also [Excel file for response time calculation](https://support.industry.siemens.com/cs/ww/en/view/109783831)).

##### Example

The following example shows how the instruction works:

![Example](images/102770770059_DV_resource.Stream@PNG-en-US.png)

The value of the "Tag_Value1" operand is added to value of the Tag_Value2 operand. The result of the addition is stored in the ""F_DB_1".Tag_Result" operand.

If an overflow occurs during execution of the "Add" instruction, the status bit OV is set to "1". In network 2, following the query of the status bit OV, the "Set output" (S) instruction is executed and the "TagOut" operand is set.

## Communication

This section contains information on the following topics:

- [PROFIBUS/PROFINET](#profibusprofinet)
- [S7 communication](#s7-communication)

### PROFIBUS/PROFINET

This section contains information on the following topics:

- [SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)](#senddp-and-rcvdp-send-and-receive-data-via-profibus-dpprofinet-io-step-7-safety-v19)

#### SENDDP and RCVDP: Send and receive data via PROFIBUS DP/PROFINET IO (STEP 7 Safety V19)

##### Introduction

You use the SENDDP and RCVDP instructions for fail-safe sending and receiving of data using:

- Safety-related master-master communication
- Safety-related master-master communication for S7 Distributed Safety
- Safety-related master-I-slave communication
- Safety-related I-slave-I-slave communication
- Safety-related IO controller-IO controller communication
- Safety-related IO controller-IO controller communication for S7 Distributed Safety
- Safety-related IO controller-I-device communication
- Safety-related IO controller-I-slave communication

##### Description

The SENDDP instruction sends 16 data elements of data type BOOL and 2 data elements of data type INT or one data element of the data type DINT (S7-1200, S7-1500) in a fail-safe manner to another F‑CPU via PROFIBUS DP/PROFINET IO. The data can be received there by the related RCVDP instruction.

Every call of this instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g. RCVDP_DB_1) for these instructions. Once it is created, the new data block can be found in the "STEP 7 Safety" folder in the project tree under "Program blocks > System blocks". For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

With the SENDDP instruction, the data to be sent (for example, outputs of other F-blocks/instructions) are available at input SD_BO_xx or SD_I_xx or SD_DI_00 as alternative.

With the RCVDP instruction, the data received are available at outputs RD_BO_xx and RD_I_xx or RD_DI_00 as alternative for additional processing by other F‑blocks/instructions.

(S7-1200, S7-1500) At the DINTMODE input of the SENDDP instruction you specify if the data at the inputs SD_I_00 and SD_I_01 or the data at the input SD_DI_00 is sent.

The operating mode of the F-CPU with the SENDDP instruction is provided at output SENDMODE. If the F-CPU with the SENDDP instruction is in disabled safety mode, output SENDMODE = 1.

Communication between F-CPUs takes place in the background by means of a special safety protocol. You must define the communication relationship between a SENDDP instruction in one F-CPU and a RCVDP instruction in the other F-CPU by specifying an F-communication ID at the DP_DP_ID inputs of the SENDDP and RCVDP instructions. Associated SENDDP and RCVDP instructions are assigned the same value for DP_DP_ID.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value for the respective F-communication ID (input DP_DP_ID; data type: INT) can be freely selected**; however, it must be unique network-wide* and CPU-wide**** at all times for all safety-related communication connections. You must check the uniqueness in the safety summary during acceptance of the safety program.  You must supply constant values*** to the DP_DP_ID and LADDR inputs when calling the instruction. Direct write access to DP_DP_ID and LADDR in the associated instance DB is not permitted in the safety program! (S016) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, no connection is established at the DP_DP_ID input for a F-communication ID "0".

*** S7-1200/1500: As of version V3.0 of the SENDDP and RCVDP instructions, the DP_DP_ID input can also be supplied with variable values from a global F-DB. In this case also, you have to check during acceptance of the safety program that uniqueness is ensured at all times. You need to check the algorithm for forming the variable value accordingly. If you cannot ensure a unique F-communication ID during startup of the safety program, because it is only specified after startup of the safety program, you must make sure that the value at the DP_DP_ID input is "0" during this phase.

**** With a redundant S7-1500HF system, both F-CPUs of the redundant S7-1500HF system are to be regarded as one single F-CPU with regard to the DP_DP_ID.

> **Note**
>
> Within a safety program, you must assign a different start address (S7-300, S7-400) or HW identifier (S7-1200, S7-1500) for every call of the SENDDP and RCVDP instructions at input LADDR.
>
> A separate instance DB must be used for each call of the SENDDP and RCVDP instructions. You must not declare and call these instructions as multi-instances.
>
> (S7-300, S7-400) The inputs of the RCVDP and RCVS7 instructions may not have preceding logic operations (for example "AND logic operation").
>
> The inputs of the RCVDP instruction cannot be initialized using fully qualified DB accesses with outputs of a RCVDP or RCVS7 instruction called in an upstream network.
>
> (S7-1200, S7-1500) The RD_D_00 output must not be evaluated for DINTMODE = 0; the RD_I_xx outputs of the RCVDP instruction must not be evaluated for DINTMODE = 1.
>
> (S7-1200, S7-1500) The outputs of the SENDDP and RCVDP instructions must not be supplied with tags from the standard user program. Exception: RET_DPRD, RET_DPWR and DIAG outputs.
>
> Fully qualified access to DP_DP_ID and LADDR is not possible in the safety program.
>
> You cannot use an actual parameter for an output of an RCVDP instruction, if it is already being used for an input of the same or another RCVDP or RCVS7 instruction.
>
> The F-CPU can go to STOP if this is not observed. The cause of the diagnostics event is entered in the diagnostics buffer of the F-CPU.

> **Note**
>
> You are not permitted to insert any SENDDP/RCVDP instructions between a JMP or JMPN instruction and the associated jump destination (jump label).
>
> You cannot insert a RET instruction prior to a SENDDP instruction.

##### SENDDP parameter

The following table shows the parameters of the SENDDP instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| SD_BO_00 | Input | BOOL | Send data BOOL 00 |
| ... |  |  | ... |
| SD_BO_15 | Input | BOOL | Send data BOOL 15 |
| SD_I_00 | Input | INT | Send data INT 00 |
| SD_I_01 | Input | INT | Send data INT 01 |
| SD_DI_00 | Input | DINT | (S7-1200, S7-1500)  (hidden)  Send data DINT 00 |
| DINTMODE | Input | DINT | (S7-1200, S7-1500)  (hidden)  0=SD_I_00 u. SD_I_01 are sent   1=SD_DI_00 is sent |
| DP_DP_ID | Input | INT | F-communication ID between SENDDP and RCVDP |
| TIMEOUT | Input | TIME | Monitoring time in ms for safety-related communication (see also [Monitoring and response times](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#monitoring-and-response-times)) |
| LADDR | Input | INT (S7-300, S7-400)  HW_SUBMODULE (S7-1200, S7-1500) | The start address (S7-300, S7-400) or HW identifier (S7-1200, S7-1500) of the address area/transfer area:   - Of DP/DP coupler for safety-related master-master communication - For safety-related master-I-slave communication - For safety-related I-slave-I-slave communication - Of PN/PN coupler for safety-related IO controller-IO controller communication - For safety-related IO controller-I-device communication - For safety-related IO controller-I-slave communication |
| ERROR | Output | BOOL | 1=Communication error |
| SUBS_ON | Output | BOOL | 1=RCVDP outputs fail-safe values |
| RET_DPRD | Output | WORD | Non-fail-safe error code RET_VAL of the DPRD_DAT instruction (for a description of error codes, refer to the help for the DPRD_DAT instruction ("Extended instructions > Distributed I/O > Other")). |
| RET_DPWR | Output | WORD | Non-fail-safe error code RET_VAL of the DPWR_DAT instruction (for a description of error codes, refer to the help for the DPWR_DAT instruction ("Extended instructions > Distributed I/O > Other")). |
| DIAG | Output | BYTE | Non-fail safe service information |

##### RCVDP parameter:

The following table shows the parameters of the RCVDP instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ACK_REI | Input | BOOL | 1=Acknowledgment for reintegration of send data following communication error |
| SUBBO_00 | Input | BOOL | Fail-safe value for receive data BOOL 00 |
| ... |  |  | ... |
| SUBBO_15 | Input | BOOL | Fail-safe value for receive data BOOL 15 |
| SUBI_00 | Input | INT | Fail-safe value for receive data INT 00 |
| SUBI_01 | Input | INT | Fail-safe value for receive data INT 01 |
| SUBDI_00 | Input | DINT | (S7-1200, S7-1500)  (hidden)  Fail-safe value for receive data DINT 00 |
| DP_DP_ID | Input | INT | F-communication ID between SENDDP and RCVDP |
| TIMEOUT | Input | TIME | Monitoring time in ms for safety-related communication (see also [Monitoring and response times](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#monitoring-and-response-times)) |
| LADDR | Input | INT (S7-300, S7-400)  HW_SUBMODULE (S7-1200, S7-1500) | The start address (S7-300, S7-400) or HW identifier (S7-1200, S7-1500) of the address area/transfer area:   - Of DP/DP coupler for safety-related master-master communication - For safety-related master-I-slave communication - For safety-related I-slave-I-slave communication - Of PN/PN coupler for safety-related IO controller-IO controller communication - For safety-related IO controller-I-device communication - For safety-related IO controller-I-slave communication |
| ERROR | Output | BOOL | 1=Communication error |
| SUBS_ON | Output | BOOL | 1=Fail-safe values are output |
| ACK_REQ | Output | BOOL | 1=Acknowledgment for reintegration of send data required |
| SENDMODE | Output | BOOL | 1=F-CPU with SENDDP instruction in disabled safety mode |
| RD_BO_00 | Output | BOOL | Receive data BOOL 00 |
| ... |  |  | ... |
| RD_BO_15 | Output | BOOL | Receive data BOOL 15 |
| RD_I_00 | Output | INT | Receive data INT 00 |
| RD_I_01 | Output | INT | Receive data INT 01 |
| RD_DI_00 | Output | DINT | (S7-1200, S7-1500)  (hidden)  Receive data DINT 00 |
| RET_DPRD | Output | WORD | Non-fail-safe error code RET_VAL of the DPRD_DAT instruction (for a description of error codes, refer to the help for the DPRD_DAT instruction ("Extended instructions > Distributed I/O > Other")). |
| RET_DPWR | Output | WORD | Non-fail-safe error code RET_VAL of the DPWR_DAT instruction (for a description of error codes, refer to the help for the DPWR_DAT instruction ("Extended instructions > Distributed I/O > Other")). |
| DIAG | Output | BYTE | Non-fail safe service information |

##### Instruction versions

A number of versions are available for these instructions:

| Version | S7-300/400 | S7-1200 | S7-1500 | Function |
| --- | --- | --- | --- | --- |
| 1.0 | x | — | — | When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.0 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.1 | o | — | o | These versions have identical functions to version 1.0. |
| 1.2 | x | — | o |  |
| 1.4 | x | — | x |  |
| 1.3 | x | — | o | S7-300/400: These versions have identical functions to version 1.0.  S7-1200/1500: Instead of 2 data of data type INT, one data of data type DINT can be sent/received as alternative. Otherwise functionally identical to version 1.0. |
| 1.5 | x | x | x |  |
| 2.0 | x | x<sup>1</sup> | x<sup>2</sup> |  |
| 3.0 | x | x<sup>1</sup> | x<sup>2</sup> | S7-300/400: This version has identical functions to version 2.0.   S7-1200/1500:   - The DP_DP_ID input can also be supplied with tags of a global F-DB. In case of DP_DP_ID = 0 no connection is established. - Supports the data status byte of the PN/PN coupler as of firmware V4.0 - Supports the simulation of the communication in S7-PLCISM operation   Otherwise functionally identical to version 2.0 |
| o This version is no longer supported.   <sup>1</sup> supported as of firmware V4.2   <sup>2</sup> supported as of firmware V2.0 |  |  |  |  |

When a new F-CPU is created with STEP 7 Safety, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

##### Placement

You need to insert the RCVDP instruction either at the start of the main safety block or (with S7-1200/1500 F-CPUs) in an F-FB/F-FC called directly at the start of the main safety block. No other instructions can be located before in the main safety block and no other instructions can be located before or afterwards in the F-FB/F-FC.

You need to insert the SENDDP instruction either at the end of the main safety block or (with S7-1200/1500 F-CPUs) in an F-FB/F-FC called directly at the end of the main safety block. No other instructions can be located afterwards in the main safety block and no other instructions can be located before or afterwards in the F-FB/F-FC.

##### Startup behavior

After the sending and receiving F-systems are started up, communication must be established between the connection partners for the fist time (SENDDP and RCVDP instructions). During this time, the receiver (RCVDP instruction) outputs the fail-safe values present at its inputs SUBBO_xx and SUBI_xx or alternatively SUBDI_00.

The SENDDP and RCVDP instructions signal this with 1 at output SUBS_ON. The SENDMODE output has default setting "0" and is not updated as long as output SUBS_ON = 1.

As of version V3.0 of the SENDDP and RCVDP instructions, communication is only established when DP_DP_ID <> 0.

##### Behavior in the event of communication errors

If a communication error occurs, for example, due to a signature error (CRC) or when monitoring time TIMEOUT expires or for F-CPUs S7-1200/1500 as of V3.0 due to a change of the DP_DP_ID to 0 after establishment of communication, the outputs ERROR and SUBS_ON = 1 are set. The receiver (RCVDP instruction) then outputs the fail-safe values assigned at its inputs SUBBO_xx and SUBI_xx or alternatively SUBDI_00 inputs. Output SENDMODE is not updated while output SUBS_ON = 1.

The send data of the SENDDP instruction present at inputs SD_BO_xx and SD_I_xx, SD_DI_00 as alternative, are only output again when communication errors are no longer detected (ACK_REQ = 1) and you [acknowledge](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementation-of-user-acknowledgment) the RCVDP instruction with a positive edge at input ACK_REI.

Communication errors also occur if the values of the DP_DP_IDs between associated SENDDP and RCVDP are temporarily different on a change of the values of variable DP_DP_IDs after communication establishment.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For the user acknowledgment, you must interconnect input ACK_REI with a signal generated by the operator input.  An interconnection with an automatically generated signal is not permitted.* (S040) |  |

* If variable F-communication IDs are used, the communication partner of the SENDDP or RCVDP instructions can be changed during running operation. The resultant communication errors may only be acknowledged with an automatically generated signal at the ACK_REI input under the following conditions:

- The safety program reliably forms a signal "Communication partner change is in progress" with the RCVDP instruction on the basis of the process state.
- The signal "Communication partner change is in progress" is only formed if there is no communication error.
- While the signal "Communication partner change is in progress" is active, no evaluation of the received process values is carried out at the RCVDP instruction.
- The automatic acknowledgement is only carried out if the "Communication partner change is in progress" signal is available.
- From a safety standpoint automatic reintegration is permitted for the relevant process.

Note that output ERROR (1=communication error) for a communication error will not be set unless communication between the connection partners (SENDDP and RCVDP instructions) has been previously established. If communication cannot be established after startup of the sending and receiving F-Systems, check the configuration of the safety-related CPU-CPU communication, the parameter assignment of the SENDDP and the RCVDP instructions, and the bus connection. You also obtain information on possible error causes by evaluating outputs DIAG, RET_DPRD and RETDP_WR.

In general, always evaluate RET_DPRD and RETDP_WR, since it is possible that only one of the two outputs will contain error information.

##### Timing diagrams SENDDP/RCVDP

![Timing diagrams SENDDP/RCVDP](images/166667419787_DV_resource.Stream@PNG-en-US.png)

##### Output DIAG

In addition, non-fail-safe information about the type of communication errors that occurred is provided at output DIAG of the SENDDP and RCVDP instructions for service purposes.

You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits are saved until you acknowledge the errors at input ACK_REI of the RCVDP instruction.

##### Structure of DIAG of the SENDDP/RCVDP instruction

| Bit no. | Assignment | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Reserved | — | — |
| Bit 1 | Reserved | — | — |
| Bit 2 | Reserved | — | — |
| Bit 3 | Invalid DP_DP_ID | The DP_DP_ID is 0. | Check the DP_DP_ID of SENDDP or RCVDP. |
| Bit 4 | Timeout of SENDDP/RCVDP detected | The standard user program overwrites transfer areas of SENDDP and RCVDP. | Check the standard user program for write access to the transfer areas of SENDDP and RCVDP. Also take indirect accesses into account. |
| DP_DP_ID of SENDDP and RCVDP different. | Check the DP_DP_ID of SENDDP and RCVDP. |  |  |
| For variable F-communication IDs the values are changed at the DP_DP_ID input. | When the DP_DP_ID of SENDDP and RCVD is consistent again, perform an acknowledgment at the ACK_REI input. |  |  |
| Interference in bus connection to partner F-CPU. | Check the bus connection and ensure that there are no external sources of interference. |  |  |
| Monitoring time setting for F-CPU and partner F-CPU is too low. | Check the parameterized monitoring time TIMEOUT at SENDDP and RCVDP of both CPUs. Set a higher value if necessary. Recompile the safety program. |  |  |
| Configuration of the DP/DP coupler or PN/PN coupler is invalid. | Check the configuration of the DP/DP coupler or of the PN/PN coupler. |  |  |
| Data validity indicator "DIA" of the DP/DP coupler is "ON". | Set the data validity indicator "DIA" at the DIL switch of the DP/DP coupler to "OFF". |  |  |
| Parameter "Data validity indicator DIA" of the PN/PN coupler is activated. | Deactivate the "Data validity display DIA" parameter in the properties for the PN/PN coupler. |  |  |
| Parameter "Activate data status" of the PN/PN coupler (as of V4.0) is activated. | Deactivate the "Activate data status" parameter in the properties for the PN/PN coupler (as of V4.0)   or   S7-1200/1500: Use Version V3.0 of the SENDDP and RCVDP instructions. |  |  |
| Internal fault of DP/DP coupler or PN/PN coupler | Replace the DP/DP coupler or PN/PN coupler |  |  |
| CP in STOP mode, or internal fault in CP | Switch the CP to RUN. Check the diagnostics buffer of the CP.   If necessary, replace the CP. |  |  |
| F-CPU/partner F-CPU in STOP mode, or internal fault in F-CPU/partner F-CPU | Switch the F-CPUs to RUN. Check the diagnostics buffer of the F-CPUs.   If necessary, replace the F-CPUs. |  |  |
| Bit 5 | Sequence number error of SENDDP/RCVDP detected | See description for bit 4 | See description for bit 4 |
| Bit 6 | CRC-error of SENDDP/RCVDP detected | See description for bit 4 | See description for bit 4 |
| DP_DP_ID of SENDDP and RCVDP different | Check DP_DP_ID of SENDDP and RCVDP |  |  |
| Bit 7 | Reserved | — | — |

---

**See also**

[Communication with S7 Distributed Safety via PN/PN coupler (IO controller-IO controller communication)](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#communication-with-s7-distributed-safety-via-pnpn-coupler-io-controller-io-controller-communication)
  
[Communication with S7 Distributed Safety via DP/DP coupler (master-master communication)](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#communication-with-s7-distributed-safety-via-dpdp-coupler-master-master-communication)
  
[Configuring and programming communication (S7-300, S7-400)](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#configuring-and-programming-communication-s7-300-s7-400)
  
[Safety-related IO controller-IO controller communication](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-io-controller-io-controller-communication)
  
[Safety-related master-master communication](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-master-master-communication)
  
[Safety-related IO controller-I-device communication](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-io-controller-i-device-communication)
  
[Safety-related master-I-slave communication](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-master-i-slave-communication)
  
[Safety-related IO controller-I-slave communication](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-io-controller-i-slave-communication)

### S7 communication

This section contains information on the following topics:

- [SENDS7 and RCVS7: Communication via S7 connections (STEP 7 Safety Advanced V19) (S7-300, S7-400)](#sends7-and-rcvs7-communication-via-s7-connections-step-7-safety-advanced-v19-s7-300-s7-400)

#### SENDS7 and RCVS7: Communication via S7 connections (STEP 7 Safety Advanced V19) (S7-300, S7-400)

##### Introduction

You use the SENDS7 and RCVS7 instructions for fail-safe sending and receiving of data using S7 connections.

> **Note**
>
> In STEP 7 Safety Advanced, S7 connections are generally permitted over Industrial Ethernet only.
>
> Safety-related communication via S7 connections is possible from and to F-CPUs with PROFINET interface or S7-400 F-CPUs with PROFINET-capable CPs. See also [Safety-related communication via S7 connections](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#safety-related-communication-via-s7-connections).

##### Description

The SENDS7 instruction sends the send data contained in an F-communication DB to the F-communication DB of the associated RCVS7 instruction of another F-CPU in a fail-safe manner using an S7 connection.

Every call of this instruction must be assigned a data area in which the instruction data is stored. The "Call options" dialog is automatically opened when the instruction is inserted in the program for this reason. There you can create a data block (single instance) (e.g., SENDS7_DB_1) or a multi-instance (e.g., SENDS7_Instance_1) for this instruction. Once it is created, you can find the new data block in the project tree in the "STEP 7 Safety" folder under "Program blocks > System blocks" or the multi-instance as a local tag in the "Static" section of the block interface. For more information, refer to the help on STEP 7.

Enable input "EN" and enable output "ENO" cannot be connected. The instruction is therefore always executed (regardless of the signal state at enable input "EN").

Information on the F-communication DB is contained in "[Programming safety-related communication via S7 connections](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#programming-safety-related-communication-via-s7-connections)".

An F-communication DB is an F-DB for safety-related CPU-CPU communication with special properties. You must specify the numbers of the F-communication DBs at inputs SEND_DB and RCV_DB of instructions SENDS7 and RCVS7.

The operating mode of the F-CPU with the SENDS7 instruction is provided at output SENDMODE of the RCVS7 instruction. If the F-CPU with the SENDS7 instruction is in disabled safety mode, then output SENDMODE = 1.

To reduce the bus load, you can temporarily shut down communication between the F-CPUs at input EN_SEND of the SENDS7 instruction. To do so, supply input EN_SEND with "0" (default = "1"). In this case, send data is no longer sent to the F-communication DB of the associated RCVS7 instruction, and the receiver provides fail-safe values for this period of time (initial values in its F-communication DB). If communication was already established between the partners, a communication error is detected.

You must specify the local ID - from the perspective of the F-CPU - of the S7 connection (from the connection table in the network view) at input ID of the SENDS7 instruction (see also [Configuring](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#configuring)).

Communication between F-CPUs takes place in the background by means of a special safety protocol. You must define a communication relationship between an SENDS7 instruction in one F-CPU and a communication relationship between an RCVS7 instruction and the other F-CPU by assigning an odd number at input R_ID (of the SENDS7 and RCVS7 instructions). Associated SENDS7 and RCVS7 instructions receive the same value for R_ID.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| The value of the respective F-communication ID (input R_ID; data type: DWORD) can be freely selected; however, it must be odd and unique for all safety-related communication connections network-wide* and CPU-wide. The value R_ID + 1 is internally assigned and must not be used.  You must supply inputs ID and R_ID with constant values when calling the instruction. Direct read or write access to ID and R_ID in the associated instance DB is not permitted in the safety program. (S020) |  |

* A network consists of one or more subnets. "Network-wide" means beyond the boundaries of the subnet. In PROFIBUS, a network includes all the nodes accessible via PROFIBUS DP. In PROFINET IO, a network includes all the nodes accessible via RT_Class_1/2/3 (Ethernet/WLAN/Bluetooth, Layer 2) and, if applicable, RT_Class_UDP (IP, Layer 3).

> **Note**
>
> A separate instance DB must be used for each call of the SENDS7 and RCVS7 instructions within a safety program. You must not declare and call these instructions as multi-instances.
>
> The inputs of the RCVS7 instruction cannot be initialized with outputs (using fully qualified DB accesses) of a RCVS7 or RCVDP instruction called in an upstream network.
>
> You cannot use an actual parameter for an output of an RCVS7 instruction, if it is already being used for an input of the same or another RCVS7 or RCVDP instruction.
>
> The F-CPU can go to STOP if this is not observed. A diagnostics event is entered in the diagnostics buffer of the F-CPU.

> **Note**
>
> You must not program any SENDS7/RCVS7 instruction between a JMP or JMPN instruction and the associated destination network of the JMP or JMPN instruction.
>
> You cannot program a RET instruction prior to a SENDS7 instruction.

##### SENDS7 parameter

The following table shows the parameters of the SENDS7 instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| SEND_DB | Input | BLOCK_DB | Number of F‑communication DB |
| TIMEOUT | Input | TIME | Monitoring time in ms for safety-related communication (see also [Monitoring and response times](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#monitoring-and-response-times)) |
| EN_SEND | Input | BOOL | 1= Send enable |
| ID | Input | WORD | Local ID of the S7 connection |
| R_ID | Input | DWORD | Network-wide unique value for a F-communication ID between a SENDS7 instruction and a RCVS7 instruction |
| ERROR | Output | BOOL | 1=Communication error |
| SUBS_ON | Output | BOOL | 1=Receiving block outputs fail-safe values |
| STAT_RCV | Output | WORD | Non-fail-safe status parameter STATUS of the URCV instruction (You can find a description of error codes in the help for the URCV instruction ("Communication > S7 Communication")) |
| STAT_SND | Output | WORD | Non-fail-safe status parameter STATUS of the USEND instruction (You can find a description of error codes in the help for the USEND instruction ("Communication > S7 Communication")) |
| DIAG | Output | BYTE | Non-fail safe service information |

##### RCVS7 parameter

The following table shows the parameters of the RCVS7 instruction.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ACK_REI | Input | BOOL | Acknowledgment for reintegration of send data after communication error |
| RCV_DB | Input | BLOCK_DB | Number of F‑communication DB |
| TIMEOUT | Input | TIME | Monitoring time in ms for safety-related communication (see also [Monitoring and response times](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#monitoring-and-response-times)) |
| ID | Input | WORD | Local ID of the S7 connection |
| R_ID | Input | DWORD | Network-wide unique value for a F-communication ID between a SENDS7 instruction and a RCVS7 instruction |
| ERROR | Output | BOOL | 1=Communication error |
| SUBS_ON | Output | BOOL | 1=Fail-safe values are output |
| ACK_REQ | Output | BOOL | 1=Acknowledgment for reintegration of send data required |
| SENDMODE | Output | BOOL | 1=F-CPU with the SENDS7 instruction in disabled safety mode |
| STAT_RCV | Output | WORD | Non-fail-safe status parameter STATUS of the URCV instruction (You can find a description of error codes in the help for the URCV instruction ("Communication > S7 Communication")) |
| STAT_SND | Output | WORD | Non-fail-safe status parameter STATUS of the USEND instruction (You can find a description of error codes in the help for the USEND instruction ("Communication > S7 Communication")) |
| DIAG | Output | BYTE | Non-fail safe service information |

##### Instruction versions

A number of versions are available for these instructions:

| Version | S7-300/400 | S7-1500 | Function |
| --- | --- | --- | --- |
| 1.0 | x | — |  |
| 1.1 | x | — | This version has identical functions to version 1.0.  It also supports later versions of internally called instructions.  When projects that were created with S7 Distributed Safety V5.4 SP5 are migrated, version 1.1 of the instruction is used automatically.   If you want to compile a migrated safety program with STEP 7 Safety Advanced for the first time, we recommend that you first update to the latest available version of the instruction. |
| 1.2 | x | — | This version has identical functions to version 1.0/1.1.  It also supports later versions of internally called instructions. |

When a new F-CPU is created with STEP 7 Safety Advanced, the latest available version for the F-CPU created is automatically preset.

For more information on the use of instruction versions, refer to the help on STEP 7 under "Using instruction versions".

##### Placement

You must insert the RCVS7 instruction at the start of the main safety block. No other instructions may be located before it in the main safety block.

You must insert the SENDS7 instruction at the end of the main safety block. No other instructions may be located after it in the main safety block.

##### Startup behavior

After the sending and receiving F-systems are started up, communication must be established between the connection partners for the fist time (SENDS7 and RCVS7 instructions). The receiver (RCVS7 instruction) provides fail-safe values for this time period (initial values in its F-communication DB).

The SENDS7 and RCVS7 instructions signal this with 1 at output SUBS_ON. The SENDMODE output (RCVS7 instruction) has default setting "0" and is not updated as long as output SUBS_ON = 1.

##### Behavior in the event of communication errors

If a communication error occurs, for example, due to a signature error (CRC) or when monitoring time TIMEOUT expires, outputs ERROR and SUBS_ON = 1 are set. The receiver (RCVS7 instruction) then provides fail-safe values (initial values in its F-communication DB). Output SENDMODE is not updated while output SUBS_ON = 1.

The send data present in the F-communication DB (SENDS7 instruction) are not output before the communication error is no longer detected (ACK_REQ = 1) and you [acknowledge](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#implementation-of-user-acknowledgment) with a positive edge at input ACK_REI of the RCVS7 instruction.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| For the user acknowledgment, you must interconnect input ACK_REI with a signal generated by the operator input.  An interconnection with an automatically generated signal is not permitted. (S040) |  |

Note that output ERROR (1=communication error) will be set for the first time on a communication error if communication has already been established between the connection partners (SENDS7 and RCVS7 instructions). If communication cannot be established after startup of the sending and receiving F-Systems, check the configuration of the safety-related CPU-CPU communication, the parameter assignment of the SENDS7 and the RCVS7 instructions, and the bus connection. You can also receive information on possible error causes by evaluating the STAT_RCV and STAT_SND outputs.

In general, always evaluate STAT_RCV and STAT_SND, since it is possible that only one of the two outputs will contain error information.

If one of the DIAG bits is set at output DIAG, also check whether the length and structure of the associated F-communication DB on both the sending and receiving ends match.

##### Timing diagrams SENDS7 and RCVS7

![Timing diagrams SENDS7 and RCVS7](images/166668230795_DV_resource.Stream@PNG-en-US.png)

##### Output DIAG

Non-fail-safe information on the type of communication errors that have occurred is made available at output DIAG for service purposes. You can read out this information by means of operator control and monitoring systems or, if applicable, you can evaluate it in your standard user program. DIAG bits are saved until you acknowledge them at input ACK_REI of the associated RCVS7 instruction.

##### Structure of DIAG

| Bit no. | Assignment of SENDS7 and RCVS7 | Possible error causes | Remedies |
| --- | --- | --- | --- |
| Bit 0 | Reserved | — | — |
| Bit 1 | Reserved | — | — |
| Bit 2 | Reserved | — | — |
| Bit 3 | Reserved | — | — |
| Bit 4 | Timeout detected by SENDS7 and RCVS7 | Fault in bus connection to partner F-CPU | Check bus connection and ensure that no external fault sources are present. |
| Monitoring time setting for F-CPU and partner F-CPU is too low | Check assigned monitoring time TIMEOUT for SENDS7 and RCVS7 of both F‑CPUs. If possible, set a higher value. Recompile safety program |  |  |
| CPs in STOP mode, or internal fault in CPs | - Switch CPs to RUN mode - Check diagnostic buffer of CPs - Replace CPs, if necessary |  |  |
| F-CPU/partner F-CPU in STOP mode, or internal fault in F-CPU/partner F-CPU | - Switch F-CPUs to RUN mode - Check diagnostic buffer of F-CPUs - Replace F-CPUs, if necessary |  |  |
| Communication was shut down with EN_SEND = 0. | Enable communication again at the associated SENDS7 with EN_SEND = 1 |  |  |
| S7 connection has changed, the IP address of the CP has changed, for example | Recompile the safety programs and download them to the F-CPUs |  |  |
| Bit 5 | Sequence number error detected by SENDS7 and RCVS7 | See description for bit 4 | See description for bit 4 |
| Bit 6 | CRC-error detected by SENDS7 and RCVS7 | See description for bit 4 | See description for bit 4 |
| Bit 7 | RCVS7:  Communication cannot be established | Configuration of the safety-related CPU-CPU communication is incorrect, parameter assignment of the SENDS7 and RCVS7 instructions is incorrect  See also description for Bit 4 | Check configuration of the safety-related CPU-CPU communication, the parameter assignment of the SENDS7 and the RCVS7 instructions is incorrect  See also description for Bit 4 |
| SENDS7:   Reserved | — | — |  |

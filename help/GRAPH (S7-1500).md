---
title: "GRAPH (S7-1500)"
package: ProgGRAPH15enUS
topics: 119
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# GRAPH (S7-1500)

This section contains information on the following topics:

- [GRAPH sequencer (S7-1500)](#graph-sequencer-s7-1500)
- [GRAPH actions (S7-1500)](#graph-actions-s7-1500)
- [GRAPH LAD instructions (S7-1500)](#graph-lad-instructions-s7-1500)
- [GRAPH FBD instructions (S7-1500)](#graph-fbd-instructions-s7-1500)

## GRAPH sequencer (S7-1500)

This section contains information on the following topics:

- [Step and transition (S7-1500)](#step-and-transition-s7-1500)
- [Step (S7-1500)](#step-s7-1500)
- [Transition (S7-1500)](#transition-s7-1500)
- [Sequence end (S7-1500)](#sequence-end-s7-1500)
- [Jump to step (S7-1500)](#jump-to-step-s7-1500)
- [Alternative branch (S7-1500)](#alternative-branch-s7-1500)
- [Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
- [Close branch (S7-1500)](#close-branch-s7-1500)

### Step and transition (S7-1500)

#### Description

You can use the "Step and transition" structure element to insert a step and transition simultaneously in your sequencer.

See also:

[Step](#step-s7-1500)

[Transition](#transition-s7-1500)

---

**See also**

[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)
  
[Steps and transitions (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#steps-and-transitions-s7-300-s7-400-s7-1500)

### Step (S7-1500)

#### Description

Steps are used to subdivide complex automation tasks into straightforward subtasks that can then be accomplished using actions. The individual steps are organized in sequencers so that every step can be executed in the specified order in the program execution. Each step must be assigned a unique name and number.

For the execution to actually be performed, the step must be activated by one of the following conditions:

- The step has been defined as an initial step.
- The transition of the previous step has been fulfilled.
- The step has been called by an event-dependent action.

Once all actions have been executed, the step becomes inactive again.

Steps in which no actions are programmed are called empty steps. Such an empty step reacts like an active step and the subsequent transition is always fulfilled.

---

**See also**

[Basics on steps (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-on-steps-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Transition (S7-1500)

#### Description

Transitions are located between the steps and contain the conditions for advancing from one step to the next (step-enabling). When the step-enabling conditions of a transition are fulfilled, the next step becomes active and its actions are executed. You can program the conditions of a transition either in LAD or FBD.

---

**See also**

[Basics on transitions (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-on-transitions-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Sequence end (S7-1500)

#### Description

You can use the "Sequence end" structure element to stop a sequencer or a branch. In a simultaneous branch, a transition must precede the sequence end.

> **Note**
>
> If all branches of a sequencer are completed with a sequence end, the sequencer can be restarted by the "INIT_SQ" parameter or using the "Initialize" button in the "Sequence control" pane of the "Testing" task card.

---

**See also**

[Elements of a sequencer (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#elements-of-a-sequencer-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Jump to step (S7-1500)

#### Description

You can use a jump to continue the program execution at any step within the GRAPH function block. Jumps can be inserted at the end of the main branch or an alternative branch to enable cyclic processing of the sequencer. The jump and jump destination are represented in the sequencer as arrows, in which case the return transition is specified for the jump destination.

---

**See also**

[Elements of a sequencer (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#elements-of-a-sequencer-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Alternative branch (S7-1500)

#### Description

You can use alternative branches to program OR branches. This means that you insert branches that start with a transition after a step. The corresponding branch is executed depending on which transition is satisfied first. If several transitions are satisfied at the same time, the transition farthest to the left has the highest priority and the corresponding branch is executed. Alternative branches end once again with a transition.

You can program up to 125 alternative branches in a sequencer.

---

**See also**

[Elements of a sequencer (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#elements-of-a-sequencer-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Simultaneous branch (S7-1500)

#### Description

You can use simultaneous branches to program AND branches. This means that you use one transition to activate multiple steps, the actions of which are then executed. Simultaneous branches always start with a step.

The subsequent transitions of the simultaneous branches are located on the main branch, in which case the various simultaneous branches can be connected to various points of the main branch. Note that branches that you join together in a transition only advance to the next step when all branches are completely executed.

You can program up to 249 simultaneous branches in a sequencer.

---

**See also**

[Elements of a sequencer (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#elements-of-a-sequencer-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Close branch (S7-1500)](#close-branch-s7-1500)

### Close branch (S7-1500)

#### Description

You can use the "Close branch" element to close simultaneous and alternative branches to their parent branch. This is necessary if you do not want to complete the branch with a jump or a sequence end. In a simultaneous branch, you can insert "Close branch" only after a step.

---

**See also**

[Elements of a sequencer (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#elements-of-a-sequencer-s7-300-s7-400-s7-1500)
  
[Step and transition (S7-1500)](#step-and-transition-s7-1500)
  
[Step (S7-1500)](#step-s7-1500)
  
[Transition (S7-1500)](#transition-s7-1500)
  
[Sequence end (S7-1500)](#sequence-end-s7-1500)
  
[Jump to step (S7-1500)](#jump-to-step-s7-1500)
  
[Alternative branch (S7-1500)](#alternative-branch-s7-1500)
  
[Simultaneous branch (S7-1500)](#simultaneous-branch-s7-1500)

## GRAPH actions (S7-1500)

This section contains information on the following topics:

- [Timer operations (S7-1500)](#timer-operations-s7-1500)
- [Counter operations (S7-1500)](#counter-operations-s7-1500)
- [Math functions (S7-1500)](#math-functions-s7-1500)
- [Move operations (S7-1500)](#move-operations-s7-1500)
- [Conversion operations (S7-1500)](#conversion-operations-s7-1500)
- [Program control operations (S7-1500)](#program-control-operations-s7-1500)
- [Word logic operations (S7-1500)](#word-logic-operations-s7-1500)
- [Shift and Rotate (S7-1500)](#shift-and-rotate-s7-1500)
- [Legacy (S7-1500)](#legacy-s7-1500-2)

### Timer operations (S7-1500)

This section contains information on the following topics:

- [TP: Generate pulse (S7-1500)](#tp-generate-pulse-s7-1500)
- [TON: Generate on-delay (S7-1500)](#ton-generate-on-delay-s7-1500)
- [TOF: Generate off-delay (S7-1500)](#tof-generate-off-delay-s7-1500)
- [TONR: Time accumulator (S7-1500)](#tonr-time-accumulator-s7-1500)

#### TP: Generate pulse (S7-1500)

##### Description

You use the "Generate pulse" instruction to set the Q output for a programmed duration. The instruction is started when the result of logic operation (RLO) of the IN parameter changes from "0" to "1" (positive signal edge). The programmed time PT begins when the instruction starts. The Q parameter is set for the time PT, regardless of the subsequent changes in the input signal. While the time PT is running, the detection of a new positive signal edge at the IN input has no influence on the signal state at the Q output.

You can query the current time value set in the ET parameter. The timer value starts at T#0s and ends when the value of time PT is reached. When time PT is reached and the signal state of the IN parameter is "0", the ET parameter is reset. If the instruction is not called in the program because it is skipped, for example, the ET output returns a constant value as soon as the time has expired.

The "Generate pulse" instruction can be placed within or at the end of the network. It requires a preceding logic operation.

Each call of the "Generate pulse" instruction must be assigned to an IEC timer in which the instance data is stored. An IEC timer is a structure of the data type IEC_TIMER, IEC_LTIMER, TP_TIME or TP_LTIME that you can declare as follows:

- Declaration of a data block of system data type IEC_TIMER or IEC_LTIMER (for example, "MyIEC_TIMER")
- Declaration as a local tag of the type TP_TIME, TP_LTIME, IEC_TIMER or IEC_LTIMER in the "Static" section of a block (for example, #MyIEC_TIMER)

##### Updating the actual values in the instance data

The instance data from "Generate pulse" is updated according to the following rules:

- IN input

  The "Generate pulse" instruction compares the current RLO with the RLO from the previous query, which is saved in the IN parameter in the instance data. If the instruction detects a change in the RLO from "0" to "1", there is a positive signal edge and the time measurement is started. After the "Generate pulse" instruction has been processed, the value of the IN parameter is updated in the instance data and is used as edge memory bit for the next query.

  Note that the edge evaluation is disrupted when the actual values of the IN parameter are written or initialized by other functions.
- PT input

  The value at the PT input is written to the PT parameter in the instance data when the edge changes at the IN input.
- Q and ET outputs

  The actual values of the Q and ET outputs are updated in the following cases:

  - When the instruction is called if the ET or Q outputs are interconnected.

    Or
  - At an access to Q or ET.

  If the outputs are not interconnected and also not queried, the current time value at the Q and ET outputs is not updated. The outputs are not updated, even if the instruction is skipped in the program.

  The internal parameters of the "Generate pulse" instruction are used to calculate the time values for Q and ET. Note that the time measurement is disrupted when the actual values of the instruction are written or initialized by other functions.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when reinitializing the actual values**  Reinitializing the actual values of an IEC timer while the time measurement is running disrupts the function of the IEC timer. Changing the actual values can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.   The following functions can cause the actual values to be reinitialized:  - Loading the block with reinitialization - Loading snapshots as actual values - Controlling or forcing the actual values - The "WRIT_DBL" instruction   Before you execute these functions, take the following precautions:  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the IEC timer has expired before initializing its actual values. - If you overwrite the actual values with a snapshot, make sure that the snapshot was taken at a time when the system was in a safe state. - Make sure that the program does not read or write the affected data during transmission. |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | BOOL | I, Q, M, D, L, P or constant | Start input |
| PT | Input | TIME, LTIME | I, Q, M, D, L, P or constant | Duration of the pulse.  The value of the PT parameter must be positive. |
| Q | Output | BOOL | I, Q, M, D, L, P | Pulse output |
| ET | Output | TIME, LTIME | I, Q, M, D, L, P | Current timer value |

You can select the data type of the instruction from the "???" drop-down list.

##### Pulse timing diagram

The following figure shows the pulse diagram of the "Generate pulse" instruction after the start:

![Pulse timing diagram](images/16634461963_DV_resource.Stream@PNG-de-DE.png)

##### Example

The following example shows how the instruction works:

GRAPH

CALL TP TIME, "IEC_TP_DB"

(IN := "Tag_Start"

PT := "Tag_PresetTIME"

Q =&gt; "Tag_Status"

ET =&gt; "Tag_ElapsedTIME"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the time programmed for the PT parameter is started and the "Tag_Status" operand is set to "1". The current time value is stored in the "Tag_ElapsedTIME" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### TON: Generate on-delay (S7-1500)

##### Description

You use the "Generate on-delay" instruction to delay setting of the Q output by the programmed time PT. The instruction is started when the result of logic operation (RLO) of the IN parameter changes from "0" to "1" (positive signal edge). The programmed time PT begins when the instruction starts. When the time PT has elapsed, the Q parameter has the signal state "1". The Q parameter remains set as long as the start input IN is still "1". When the signal state at the start input changes from "1" to "0", the Q parameter is reset. The timer function is started again when a new positive signal edge is detected at the start input.

You can query the current time value at the ET output. The timer value starts at T#0s and ends when the value of time PT is reached. The ET parameter is reset as soon as the signal state of the IN parameter changes to "0". If the instruction is not called in the program because it is skipped, for example, the ET output returns a constant value as soon as the time PT has expired.

The "Generate on-delay" instruction can be placed within or at the end of the network. It requires a preceding logic operation.

Each call of the "Generate on-delay" instruction must be assigned to an IEC timer in which the instance data is stored. An IEC timer is a structure of the data type IEC_TIMER, IEC_LTIMER, TON_TIME or TON_LTIME that you can declare as follows:

- Declaration of a data block of system data type IEC_TIMER or IEC_LTIMER (for example, "MyIEC_TIMER")
- Declaration as a local tag of the type TON_TIME, TON_LTIME, IEC_TIMER or IEC_LTIMER in the "Static" section of a block (for example, #MyIEC_TIMER)

##### Updating the actual values in the instance data

The instance data from "Generate on-delay" is updated according to the following rules:

- IN input

  The "Generate on-delay" instruction compares the current RLO with the RLO from the previous query, which is saved in the IN parameter in the instance data. If the instruction detects a change in the RLO from "0" to "1", there is a positive signal edge and the time measurement is started. After the "Generate on-delay" instruction has been processed, the value of the IN parameter is updated in the instance data and is used as edge memory bit for the next query.

  Note that the edge evaluation is disrupted when the actual values of the IN parameter are written or initialized by other functions.
- PT input

  The value at the PT input is written to the PT parameter in the instance data when the edge changes at the IN input.
- Q and ET outputs

  The actual values of the Q and ET outputs are updated in the following cases:

  - When the instruction is called if the ET or Q outputs are interconnected.

    Or
  - At an access to Q or ET.

  If the outputs are not interconnected and also not queried, the current time value at the Q and ET outputs is not updated. The outputs are not updated, even if the instruction is skipped in the program.

  The internal parameters of the "Generate on-delay" instruction are used to calculate the time values for Q and ET. Note that the time measurement is disrupted when the actual values of the instruction are written or initialized by other functions.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when reinitializing the actual values**  Reinitializing the actual values of an IEC timer while the time measurement is running disrupts the function of the IEC timer. Changing the actual values can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.   The following functions can cause the actual values to be reinitialized:  - Loading the block with reinitialization - Loading snapshots as actual values - Controlling or forcing the actual values - The "WRIT_DBL" instruction   Before you execute these functions, take the following precautions:  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the IEC timer has expired before initializing its actual values. - If you overwrite the actual values with a snapshot, make sure that the snapshot was taken at a time when the system was in a safe state. - Make sure that the program does not read or write the affected data during transmission. |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | BOOL | I, Q, M, D, L, P or constant | Start input |
| PT | Input | TIME, LTIME | I, Q, M, D, L, P or constant | Duration of the on-delay  The value of the PT parameter must be positive. |
| Q | Output | BOOL | I, Q, M, D, L, P | Signal state that is delayed by the time PT. |
| ET | Output | TIME, LTIME | I, Q, M, D, L, P | Current timer value |

You can select the data type of the instruction from the "???" drop-down list.

##### Pulse timing diagram

The following figure shows the behavior of the "Generate on-delay" instruction after the start:

![Pulse timing diagram](images/40088237707_DV_resource.Stream@PNG-de-DE.png)

##### Example

The following example shows how the instruction works:

GRAPH

CALL TON TIME, "IEC_TON_DB"

(IN := "Tag_Start"

PT := "Tag_PresetTIME"

Q =&gt; "Tag_Status"

ET =&gt; "Tag_ElapsedTIME"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the time programmed for the PT parameter is started. When the time expires, the "Tag_Status" operand is set to the signal state "1". The "Tag_Status" operand remains set to "1" as long as the "Tag_Start" operand has signal state "1". The current time value is stored in the "Tag_ElapsedTime" operand. When the signal state of the "Tag_Start" operand changes from "1" to "0", the "Tag_Status" operand is reset.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### TOF: Generate off-delay (S7-1500)

##### Description

You can use the "Generate off-delay" instruction to reset the Q output by the programmed time PT. The Q output is set when the result of logic operation (RLO) at input IN changes from "0" to "1" (positive signal edge). When the signal state at input IN changes back to "0" (negative signal edge), the programmed time PT starts. Output Q remains set as long as the time duration PT is running. When the PT time duration expires, the Q output is reset. If the signal state at input IN changes to "1" before the PT time duration expires, the timer is reset. The signal state at the output Q continues to be "1".

The "Generate off-delay" instruction can be placed within or at the end of the network. It requires a preceding logic operation.

The current time value can be queried in the ET parameter. The timer value starts at T#0s and ends when the value of time PT is reached. When the time PT expires, the ET parameter remains set to the current value until the IN parameter changes back to "1". If the IN input changes to "1" before time PT has expired, the ET output is reset to the value T#0s. If the instruction is not called in the program because it is skipped, for example, the ET output returns a constant value as soon as the time has expired.

Each call of the "Generate off-delay" instruction must be assigned to an IEC timer in which the instance data is stored. An IEC timer is a structure of the data type IEC_TIMER, IEC_LTIMER, TOF_TIME or TOF_LTIME that you can declare as follows:

- Declaration of a data block of system data type IEC_TIMER or IEC_LTIMER (for example, "MyIEC_TIMER")
- Declaration as a local tag of the type TOF_TIME, TOF_LTIME, IEC_TIMER or IEC_LTIMER in the "Static" section of a block (for example, #MyIEC_TIMER)

##### Updating the actual values in the instance data

The instance data from "Generate off-delay" is updated according to the following rules:

- IN input

  The "Generate off-delay" instruction compares the current RLO with the RLO from the previous query, which is saved in the IN parameter in the instance data. If the instruction detects a change in the RLO from "1" to "0", there is a negative signal edge and the time measurement is started. After the "Generate off-delay" instruction has been processed, the value of the IN parameter is updated in the instance data and is used as edge memory bit for the next query.

  Note that the edge evaluation is disrupted when the actual values of the IN parameter are written or initialized by other functions.
- PT input

  The value at the PT input is written to the PT parameter in the instance data when the edge changes at the IN input.
- Q and ET outputs

  The actual values of the Q and ET outputs are updated in the following cases:

  - When the instruction is called, if the ET or Q outputs are interconnected.

    Or
  - At an access to Q or ET.

  If the outputs are not interconnected and also not queried, the current time value at the Q and ET outputs is not updated. The outputs are not updated, even if the instruction is skipped in the program.

  The internal parameters of the "Generate off-delay" instruction are used to calculate the time values for Q and ET. Note that the time measurement is disrupted when the actual values of the instruction are written or initialized by other functions.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when reinitializing the actual values**  Reinitializing the actual values of an IEC timer while the time measurement is running disrupts the function of the IEC timer. Changing the actual values can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.   The following functions can cause the actual values to be reinitialized:  - Loading the block with reinitialization - Loading snapshots as actual values - Controlling or forcing the actual values - The "WRIT_DBL" instruction   Before you execute these functions, take the following precautions:  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the IEC timer has expired before initializing its actual values. - If you overwrite the actual values with a snapshot, make sure that the snapshot was taken at a time when the system was in a safe state. - Make sure that the program does not read or write the affected data during transmission. |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | BOOL | I, Q, M, D, L, P or constant | Start input |
| PT | Input | TIME, LTIME | I, Q, M, D, L, P or constant | Duration of the off delay  The value of the PT parameter must be positive. |
| Q | Output | BOOL | I, Q, M, D, L, P | Signal state that is delayed by the time PT. |
| ET | Output | TIME, LTIME | I, Q, M, D, L, P | Current timer value |

You can select the data type of the instruction from the "???" drop-down list.

##### Pulse timing diagram

The following figure shows the behavior of the "Generate off-delay" instruction after the start:

![Pulse timing diagram](images/10383011595_DV_resource.Stream@PNG-en-US.png)

##### Example

The following example shows how the instruction works:

GRAPH

CALL TOF TIME, "IEC_TOF_DB"

(IN := "Tag_Start"

PT := "Tag_PresetTIME"

Q =&gt; "Tag_Status"

ET =&gt; "Tag_ElapsedTIME"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the "Tag_Status" operand is set. When the signal state of the "Tag_Start" operand changes from "1" to "0", the time programmed for the PT parameter is started. As long as the time is running, the "Tag_Status" operand remains set. When the time has expired, the "Tag_Status" operand is reset. The current time value is stored in the "Tag_ElapsedTIME" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### TONR: Time accumulator (S7-1500)

##### Description

The instruction "Time accumulator" is used to accumulate time values within a period set by the parameter PT. When the signal state at the IN input changes from "0" to "1" (positive signal edge), the time measurement and the time duration PT are started. While the time PT is running, the time values are accumulated that are recorded when the IN input has signal state "1". The accumulated time is written to the ET output and can be queried there. When the duration PT expires, the output Q has signal state "1". The Q parameter remains set to "1", even when the signal state at the IN parameter changes from "1" to "0" (negative signal edge).

The "Time accumulator" instruction can be placed within or at the end of the network. It requires a preceding logic operation.

The R input resets the ET and Q outputs regardless of the signal state of the start input.

Each call of the "Time accumulator" instruction must be assigned an IEC timer in which the instance data is stored. An IEC timer is a structure of the data type IEC_TIMER, IEC_LTIMER, TONR_TIME or TONR_LTIME that you can declare as follows:

- Declaration of a data block of system data type IEC_TIMER or IEC_LTIMER (for example, "MyIEC_TIMER")
- Declaration as a local tag of the type TONR_TIME, TONR_LTIME, IEC_TIMER or IEC_LTIMER in the "Static" section of a block (for example, #MyIEC_TIMER)

##### Updating the actual values in the instance data

The instance data from "Time accumulator" is updated according to the following rules:

- IN input

  The "Time accumulator" instruction compares the current RLO with the RLO from the previous query, which is saved in the IN parameter in the instance data. If the instruction detects a change in the RLO from "0" to "1", there is a positive signal edge and the time measurement is continued. If the instruction in the RLO detects a change from "1" to "0", there is a negative signal edge and the time measurement is interrupted. After the "Time accumulator" instruction has been processed, the value of the IN parameter is updated in the instance data and is used as edge memory bit for the next query.

  Note that the edge evaluation is disrupted when the actual values of the IN parameter are written or initialized by other functions.
- PT input

  The value at the PT input is written to the PT parameter in the instance data when the edge changes at the IN input.
- R input

  The signal "1" at input R resets the time measurement and blocks it. Edges at the IN input are ignored. The signal "0" at input R enables time measurement again.
- Q and ET outputs

  The actual values of the Q and ET outputs are updated in the following cases:

  - When the instruction is called if the ET or Q outputs are interconnected.

    Or
  - At an access to Q or ET.

  If the outputs are not interconnected and also not queried, the current time value at the Q and ET outputs is not updated. The outputs are not updated, even if the instruction is skipped in the program.

  The internal parameters of the "Time accumulator" instruction are used to calculate the time values for Q and ET. Note that the time measurement is disrupted when the actual values of the instruction are written or initialized by other functions.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Danger when reinitializing the actual values**  Reinitializing the actual values of an IEC timer while the time measurement is running disrupts the function of the IEC timer. Changing the actual values can result in inconsistencies between the program and the actual process. This can cause serious damage to property and personal injury.   The following functions can cause the actual values to be reinitialized:  - Loading the block with reinitialization - Loading snapshots as actual values - Controlling or forcing the actual values - The "WRIT_DBL" instruction   Before you execute these functions, take the following precautions:  - Make sure that the plant is in a safe state before you overwrite the actual values. - Make sure that the IEC timer has expired before initializing its actual values. - If you overwrite the actual values with a snapshot, make sure that the snapshot was taken at a time when the system was in a safe state. - Make sure that the program does not read or write the affected data during transmission. |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | BOOL | I, Q, M, D, L, P or constant | Start input |
| R | Input | BOOL | I, Q, M, D, L, P or constant | Reset input |
| PT | Input | TIME, LTIME | I, Q, M, D, L, P or constant | Maximum duration of time recording  The value of the PT parameter must be positive. |
| Q | Output | BOOL | I, Q, M, D, L, P | Output that is set when time PT expires. |
| ET | Output | TIME, LTIME | I, Q, M, D, L, P | Accumulated time |

You can select the data type of the instruction from the "???" drop-down list.

##### Pulse timing diagram

The following figure shows the pulse timing diagram of the "Time accumulator" instruction:

![Pulse timing diagram](images/136610072843_DV_resource.Stream@PNG-de-DE.png)

##### Example

The following example shows how the instruction works:

GRAPH

CALL TONR TIME, "IEC_TONR_DB"

(IN := "Tag_Start"

R := "Tag_Reset"

PT := "Tag_PresetTIME"

Q =&gt; "Tag_Status"

ET =&gt; "Tag_ElapsedTIME"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the time programmed for the PT parameter is started. While the time is running, the time values are accumulated that are recorded when the "Tag_Start" operand has signal state "1". The accumulated time is stored in the "Tag_ElapsedTIME" operand. When the time value specified for the PT parameter is reached, the "Tag_Status" operand is set to the signal state "1". The current time value is stored in the "Tag_ElapsedTIME" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Counter operations (S7-1500)

This section contains information on the following topics:

- [CTU: Count up (S7-1500)](#ctu-count-up-s7-1500)
- [CTD: Count down (S7-1500)](#ctd-count-down-s7-1500)
- [CTUD: Count up and down (S7-1500)](#ctud-count-up-and-down-s7-1500)

#### CTU: Count up (S7-1500)

##### Description

You can use the "Count up" instruction to increment the value at the CV parameter. When the signal state of the parameter CU changes from "0" to "1" (positive signal edge), the instruction is executed and the current counter value of the parameter CV is incremented by one. The counter value is incremented each time a positive signal edge is detected, until it reaches the high limit for the data type specified at the CV output. When the high limit is reached, the signal state of the CU parameter no longer has an effect on the instruction.

You can query the count status of the Q parameter. The signal state of the Q parameter is determined by the PV parameter. When the current counter value is greater than or equal to the value of the PV parameter, the Q parameter is set to signal state "1". In all other cases, the signal state of the Q parameter is "0".

The value of the CV parameter is reset to zero when the signal state at the R parameter changes to "1". As long as the signal state of the R parameter is "1", the signal state of the CU parameter has no effect on the instruction.

> **Note**
>
> Only use a counter at a single point in the program to avoid the risk of counting errors.

Each call of the "Count up" instruction must be assigned an IEC counter in which the instruction data is stored. An IEC counter is a structure with one of the following data types:

##### Data block of system data type IEC_&lt;Counter&gt; (Shared DB)

- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

##### Local tag

- CTU_SINT / CTU_USINT
- CTU_INT / CTU_UINT
- CTU_DINT / CTU_UDINT
- CTU_LINT / CTU_ULINT
- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

You can declare an IEC counter as follows:

- Declaration of a data block of system data type IEC_&lt;Counter&gt; (for example, "MyIEC_COUNTER")
- Declaration as a local tag of the type CTU_&lt;Data_type&gt; or IEC_&lt;Counter&gt; in the "Static" section of a block (for example #MyCTU_COUNTER)

When you set up the IEC counter in a separate data block (single instance), the instance data block is created by default with "optimized block access" and the individual tags are defined as retentive. For additional information on setting retentivity in an instance data block, refer to "See also".

When you set up the IEC counter as local tag (multi-instance) in a function block with "optimized block access", it is defined as retentive in the block interface.

The execution of the "Count up" instruction requires a preceding logic operation. It can be placed within or at the end of the network.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CU | Input | BOOL | I, Q, M, D, L or constant | Count input |
| R | Input | BOOL | I, Q, M, D, L, P or constant | Reset input |
| PV | Input | Integers | I, Q, M, D, L, P or constant | Value at which the Q output is set. |
| Q | Output | BOOL | I, Q, M, D, L | Counter status |
| CV | Output | Integers, CHAR, WCHAR, DATE | I, Q, M, D, L, P | Current counter value |

You can select the data type of the instruction from the "???" drop-down list.

##### Example

The following example shows how the instruction works:

GRAPH

CALL CTU INT, "IEC_CTU_DB"

(CU := "Tag_Start"

R := "Tag_ResetCOUNTER"

PV := "Tag_PresetValue"

Q =&gt; "Tag_Status"

CV =&gt; "Tag_CounterValue"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the "Count up" instruction is executed and the current counter value of the "Tag_CounterValue" operand is incremented by one. With each additional positive signal edge, the counter value is incremented until it reaches the high limit of the (INT =32767) data type.

The value of the PV parameter is adopted as the limit for determining the "Tag_Status" output. The "Tag_Status" output has signal state "1" as long as the current counter value is greater than or equal to the value of the "Tag_PresetValue" operand. In all other cases, the "Tag_Status" output has signal state "0".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Setting retentivity in an instance data block](Programming%20data%20blocks.md#setting-retentivity-in-an-instance-data-block)
  
[Setting the retentivity of local tags](Declaring%20the%20block%20interface.md#setting-the-retentivity-of-local-tags)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### CTD: Count down (S7-1500)

##### Description

The "Count down" instruction is used to decrement the value at the parameter CV. When the signal state of the CD parameter changes from "0" to "1" (positive signal edge), the instruction is executed and the current counter value of the CV parameter is decremented by one. Each time a positive signal edge is detected, the counter value is decremented until it reaches the low limit of the specified data type. When the low limit is reached, the signal state of the CD parameter no longer has an effect on the instruction.

You can query the count status of the Q parameter. If the current counter value is less than or equal to zero, the Q parameter is set to signal state "1". In all other cases, the signal state of the Q parameter is "0".

The value of the CV parameter is set to the value of the PV parameter when the signal state of the LD parameter changes to "1". As long as the signal state of the LD parameter is "1", the signal state of the CD parameter has no effect on the instruction.

> **Note**
>
> Only use a counter at a single point in the program to avoid the risk of counting errors.

Each call of the "Count down" instruction must be assigned an IEC counter in which the instruction data is stored. An IEC counter is a structure with one of the following data types:

##### Data block of system data type IEC_&lt;Counter&gt; (Shared DB)

- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

##### Local tag

- CTD_SINT / CTD_USINT
- CTD_INT / CTD_UINT
- CTD_DINT / CTD_UDINT
- CTD_LINT / CTD_ULINT
- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

You can declare an IEC counter as follows:

- Declaration of a data block of system data type IEC_&lt;Counter&gt; (for example, "MyIEC_COUNTER")
- Declaration as a local tag of the type CTD_&lt;Data_type&gt; or IEC_&lt;Counter&gt; in the "Static" section of a block (for example #MyCTD_COUNTER)

When you set up the IEC counter in a separate data block (single instance), the instance data block is created by default with "optimized block access" and the individual tags are defined as retentive. For additional information on setting retentivity in an instance data block, refer to "See also".

When you set up the IEC counter as local tag (multi-instance) in a function block with "optimized block access", it is defined as retentive in the block interface.

The execution of the "Count down" instruction requires a preceding logic operation. It can be placed within or at the end of the network.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CD | Input | BOOL | I, Q, M, D, L or constant | Count input |
| LD | Input | BOOL | I, Q, M, D, L, P or constant | Load input |
| PV | Input | Integers | I, Q, M, D, L, P or constant | Value to which the CV output is set with LD = 1. |
| Q | Output | BOOL | I, Q, M, D, L | Counter status |
| CV | Output | Integers, CHAR, WCHAR, DATE | I, Q, M, D, L, P | Current counter value |

You can select the data type of the instruction from the "???" drop-down list.

##### Example

The following example shows how the instruction works:

GRAPH

CALL CTD INT, "IEC_CTD_DB"

(CD := "Tag_Start"

LD := "Tag_LoadPV"

PV := "Tag_PresetValue"

Q =&gt; "Tag_Status"

CV =&gt; "Tag_CounterValue"

)

When the signal state of the "Tag_Start" operand changes from "0" to "1", the "Count down" instruction is executed and the value of the "Tag_CounterValue" output is decremented by one. With each additional positive signal edge, the counter value is decremented until the low limit of the specified data type (INT = -32768) is reached.

The "Tag_Status" output has signal state "1" as long as the current counter value is less than or equal to zero. In all other cases, the "Tag_Status" output has signal state "0".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Setting retentivity in an instance data block](Programming%20data%20blocks.md#setting-retentivity-in-an-instance-data-block)
  
[Setting the retentivity of local tags](Declaring%20the%20block%20interface.md#setting-the-retentivity-of-local-tags)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### CTUD: Count up and down (S7-1500)

##### Description

You can use the "Count up and down" instruction to increment and decrement the value of the CV parameter. When the signal state of the CU parameter changes from "0" to "1" (positive signal edge), the current counter value of the CV parameter is incremented by one. When the signal state of the CD parameter changes from "0" to "1" (positive signal edge), the current counter value of the CV parameter is decremented by one. If there is a positive signal edge at the CU and CD inputs in a program cycle, the current counter value of the CV parameter remains unchanged.

The counter value can be incremented until it reaches the high limit of the data type specified at the CV parameter. When the high limit is reached, the counter value is no longer incremented on a positive signal edge. The counter value is no longer decremented once the low limit of the specified data type has been reached.

When the signal state of the LD parameter changes to "1", the counter value of the CV parameter is set to the value of the PV parameter. As long as the LD parameter has signal state "1", the signal state of the CU and CD inputs has no effect on the instruction.

The counter value is set to zero when the signal state of the R parameter changes to "1". As long as the R parameter has signal state "1", a change in the signal state of the CU, CD and LD parameters has no effect on the "Count up and down" instruction.

You can query the status of the up counter at the QU parameter. When the current counter value is greater than or equal to the value of the PV parameter, the QU parameter is set to signal state "1". In all other cases, the signal state of the QU parameter is "0".

You can query the status of the down counter at the QD parameter. If the current counter value is less than or equal to zero, the QD parameter is set to signal state "1". In all other cases, the signal state of the QD parameter is "0".

> **Note**
>
> Only use a counter at a single point in the program to avoid the risk of counting errors.

Each call of the "Count up and down" instruction must be assigned an IEC counter in which the instruction data is stored. An IEC counter is a structure with one of the following data types:

##### Data block of system data type IEC_&lt;Counter&gt; (Shared DB)

- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

##### Local tag

- CTUD_SINT / CTUD_USINT
- CTUD_INT / CTUD_UINT
- CTUD_DINT / CTUD_UDINT
- CTUD_LINT / CTUD_ULINT
- IEC_SCOUNTER / IEC_USCOUNTER
- IEC_COUNTER / IEC_UCOUNTER
- IEC_DCOUNTER / IEC_UDCOUNTER
- IEC_LCOUNTER / IEC_ULCOUNTER

You can declare an IEC counter as follows:

- Declaration of a data block of system data type IEC_&lt;Counter&gt; (for example, "MyIEC_COUNTER")
- Declaration as a local tag of the type CTUD_&lt;Data_type&gt; or IEC_&lt;Counter&gt; in the "Static" section of a block (for example #MyCTUD_COUNTER)

When you set up the IEC counter in a separate data block (single instance), the instance data block is created by default with "optimized block access" and the individual tags are defined as retentive. For additional information on setting retentivity in an instance data block, refer to "See also".

When you set up the IEC counter as local tag (multi-instance) in a function block with "optimized block access", it is defined as retentive in the block interface.

The execution of the "Count up and down" instruction requires a preceding logic operation. It can be placed within or at the end of the network.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CU | Input | BOOL | I, Q, M, D, L or constant | Count up input |
| CD | Input | BOOL | I, Q, M, D, L or constant | Count down input |
| R | Input | BOOL | I, Q, M, D, L, P or constant | Reset input |
| LD | Input | BOOL | I, Q, M, D, L, P or constant | Load input |
| PV | Input | Integers | I, Q, M, D, L, P or constant | Value at which the QU output is set / value to which the CV output is set when LD = 1. |
| QU | Output | BOOL | I, Q, M, D, L | Status of the up counter |
| QD | Output | BOOL | I, Q, M, D, L | Status of the down counter |
| CV | Output | Integers, CHAR, WCHAR, DATE | I, Q, M, D, L, P | Current counter value |

You can select the data type of the instruction from the "???" drop-down list.

##### Example

The following example shows how the instruction works:

GRAPH

CALL CTUD INT, "IEC_CTUD_DB"

(CU := "Tag_StartCTU"

CD := "Tag_StartCTD"

R := "Tag_ResetCOUNTER"

LD := "Tag_LoadPV"

PV := "Tag_PresetValue"

​ QU =&gt; "Tag_CounterStatusUP"

QD =&gt; "Tag_CounterStatusDOWN"

CV =&gt; "Tag_CounterValue"

)

When the signal state of the "Tag_StartCTU" or "Tag_StartCTD" input changes from "0" to "1" (positive signal edge), the "Count up and down" instruction is executed. When there is a positive signal edge at the "Tag_StartCTU" input, the current counter value is incremented by one and stored in the "Tag_CounterValue" output. When there is a positive signal edge at the "Tag_StartCTD" input, the counter value is decremented by one and stored in the "Tag_CounterValue" output. When there is a positive signal edge at the CU input, the counter value is incremented until it reaches the high limit of 32767. When there is a positive signal edge at the CD input, the counter value is decremented until it reaches the low limit of INT = -32768.

The "Tag_CounterStatusUP" output has signal state "1" as long as the current counter value is greater than or equal to the value of the "Tag_PresetValue" input. In all other cases, the "Tag_CounterStatusUP" output has signal state "0".

The "Tag_CounterStatusDOWN" output has signal state "1" as long as the current counter value is less than or equal to zero. In all other cases, the "Tag_CounterStatusDOWN" output has signal state "0".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Setting retentivity in an instance data block](Programming%20data%20blocks.md#setting-retentivity-in-an-instance-data-block)
  
[Setting the retentivity of local tags](Declaring%20the%20block%20interface.md#setting-the-retentivity-of-local-tags)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Math functions (S7-1500)

This section contains information on the following topics:

- [NEG: Create twos complement (S7-1500)](#neg-create-twos-complement-s7-1500)
- [ABS: Form absolute value (S7-1500)](#abs-form-absolute-value-s7-1500)
- [MIN: Get minimum (S7-1500)](#min-get-minimum-s7-1500)
- [MAX: Get maximum (S7-1500)](#max-get-maximum-s7-1500)
- [LIMIT: Set limit value (S7-1500)](#limit-set-limit-value-s7-1500)
- [SQR: Form square (S7-1500)](#sqr-form-square-s7-1500)
- [SQRT: Form square root (S7-1500)](#sqrt-form-square-root-s7-1500)
- [LN: Form natural logarithm (S7-1500)](#ln-form-natural-logarithm-s7-1500)
- [EXP: Form exponential value (S7-1500)](#exp-form-exponential-value-s7-1500)
- [SIN: Form sine value (S7-1500)](#sin-form-sine-value-s7-1500)
- [COS: Form cosine value (S7-1500)](#cos-form-cosine-value-s7-1500)
- [TAN: Form tangent value (S7-1500)](#tan-form-tangent-value-s7-1500)
- [ASIN: Form arcsine value (S7-1500)](#asin-form-arcsine-value-s7-1500)
- [ACOS: Form arccosine value (S7-1500)](#acos-form-arccosine-value-s7-1500)
- [ATAN: Form arctangent value (S7-1500)](#atan-form-arctangent-value-s7-1500)
- [FRAC: Return fraction (S7-1500)](#frac-return-fraction-s7-1500)

#### NEG: Create twos complement (S7-1500)

##### Description

You use the "Create twos complement" instruction to change the sign of the operand value. For example, if the value is positive, the negative equivalent of this value is output.

The value of the OUT output is invalid if the result of the instruction is outside the range permitted for the data type specified at the OUT output (only valid for integers).

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | SINT, INT, DINT, LINT, floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | SINT, INT, DINT, LINT, floating-point numbers | I, Q, M, D, L, P | Twos complement of the input value |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := NEG_REAL("Tag_InValue")

The instruction changes the sign of the value of the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ABS: Form absolute value (S7-1500)

##### Description

You use the "Form absolute value" instruction to calculate the absolute value of the operand value.

The value of the result is invalid if a floating-point number has an invalid value.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | SINT, INT, DINT, LINT, floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | SINT, INT, DINT, LINT, floating-point numbers | I, Q, M, D, L, P | Absolute value of the input value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ABS("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | -6.234 |
| Tag_OutValue | 6.234 |

The instruction calculates the absolute value of the value of the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MIN: Get minimum (S7-1500)

##### Description

You use the "Get minimum" instruction to compare the values of the available IN1 and IN2 inputs and write the lowest value in the OUT output.

The value of the OUT output is invalid if one of the following conditions is met:

- The implicit conversion of the data types fails during execution of the instruction.
- A floating-point number has an invalid value.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | First input value |
| IN2 | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | Second input value |
| OUT | Output | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P | Result |
| The data types TOD, LTOD, DATE, and LDT can only be used if the IEC test is not enabled. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL MIN INT

(IN1 := "TagIn_Value1"

IN2 := "TagIn_Value2"

​OUT =&gt; "Tag_Minimum"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN1 | TagIn_Value1 | 12222 |
| IN2 | TagIn_Value2 | 14444 |
| OUT | Tag_Minimum | 12222 |

The instruction compares the values of the specified operands and copies the lowest value ("TagIn_Value1") to the "Tag_Minimum" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MAX: Get maximum (S7-1500)

##### Description

You use the "Get maximum" instruction to compare the values of the IN1 and IN2 inputs and write the highest value to the OUT output.

The value of the OUT output is invalid if one of the following conditions is met:

- The implicit conversion of the data types fails during execution of the instruction.
- A floating-point number has an invalid value.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | First input value |
| IN2 | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | Second input value |
| OUT | Output | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P | Result |
| The data types TOD, LTOD, DATE, and LDT can only be used if the IEC test is not enabled. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL MAX INT

(IN1 := "TagIn_Value1"

IN2 := "TagIn_Value2"

​OUT =&gt; "Tag_Maximum"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN1 | TagIn_Value1 | 12222 |
| IN2 | TagIn_Value2 | 14444 |
| OUT | Tag_Maximum | 14444 |

The instruction compares the values of the specified operands and copies the highest value ("TagIn_Value2") to the "Tag_Maximum" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### LIMIT: Set limit value (S7-1500)

##### Description

You use the "Set limit value" instruction to limit the value of the IN input to the values of the MN and MX inputs. If the value of the IN input meets the condition MN &lt;= IN &lt;= MX, it is copied to the OUT output. If the condition is not met and the IN input value is below the low limit MN, the OUT output is set to the value of the MN input. If the high limit MX is exceeded, the OUT output is set to the value of the MX input.

If the value at the MN input is greater than at the MX input, the result is the value specified at the IN parameter. The instruction is only executed if the tags of all inputs are of the same data type.

The value of the OUT output is invalid if one of the following conditions is met:

- The specified tags are not of the same data type.
- An operand has an invalid value.
- The value of the MN parameter is greater than the value of the MX parameter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MN | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | Low limit |
| IN | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | Input value |
| MX | Input | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | High limit |
| OUT | Output | Integers, floating-point numbers, TIME, LTIME, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P | Result |
| The data types TOD, LTOD, DATE, and LDT can only be used if the IEC test is not enabled. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL LIMIT INT

(MN := "Tag_LowLimit"

IN := "Tag_InputValue"

MX := "Tag_HighLimit"

​OUT =&gt; "Tag_Result"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| MN | Tag_LowLimit | 12000 |
| IN | Tag_InputValue | 8000 |
| MX | Tag_HighLimit | 16000 |
| OUT | Tag_Result | 12000 |

The value of the "Tag_InputValue" operand is compared with the values of the "Tag_LowLimit" and "Tag_HighLimit" operands. Since the value of the "Tag_InputValue" operand is less than the low limit, the value of the "Tag_LowLimit" operand is copied to the "Tag_Result" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SQR: Form square (S7-1500)

##### Description

The "Form square" instruction is used to square the value of the floating-point number of the operand and write the result to the output.

If the operand contains an invalid floating-point number, the value of the result is invalid.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Square of the input value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SQR("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 5.0 |
| Tag_OutValue | 25.0 |

The instruction squares the value of the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SQRT: Form square root (S7-1500)

##### Description

Use the "Form square root" instruction to calculate the square root of the input value and save the result in the specified operand. The instruction has a positive result if the input value is greater than zero. If input values are less than zero, the instruction returns an invalid floating-point number. If the value of the operand is "0", then the result is also "0".

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L | Square root of the input value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SQRT("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 25.0 |
| Tag_OutValue | 5.0 |

The instruction calculates the square root of the value of the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Invalid floating-point numbers](Data%20types.md#invalid-floating-point-numbers)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### LN: Form natural logarithm (S7-1500)

##### Description

You use the "Form natural logarithm" instruction to calculate the natural logarithm to base e (e=2.718282) from the input value. The instruction has a positive result if the input value is greater than zero. If input values are less than zero, the instruction returns an invalid floating-point number.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Natural logarithm of the input value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := LN("Tag_InValue")

The instruction calculates the natural logarithm of the value in the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Invalid floating-point numbers](Data%20types.md#invalid-floating-point-numbers)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### EXP: Form exponential value (S7-1500)

##### Description

You use the "Form exponential value" instruction to calculate the exponent from the base e (e = 2,718282) and the value of the operand.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Exponential value of the input value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := EXP("Tag_InValue")

The instruction calculates the exponent from base e and the value of the "Tag_InValue" operand and outputs the result (e<sup>IN</sup>) in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Invalid floating-point numbers](Data%20types.md#invalid-floating-point-numbers)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SIN: Form sine value (S7-1500)

##### Description

You use the "Form sine value" instruction to calculate the sine of an angle. The size of the angle is specified in radians in the operand.

The value of the result is invalid if the value of the operand is not a valid floating-point number.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Size of angle in radians |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Sine of the specified angle |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SIN("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | +1.570796 (π/2) |
| Tag_OutValue | 1.0 |

The instruction calculates the sine of the angle specified in the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### COS: Form cosine value (S7-1500)

##### Description

You use the "Form cosine value" instruction to calculate the cosine of an angle. The size of the angle is specified in radians in the operand.

The value of the result is invalid if the value of the operand is not a valid floating-point number.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Size of angle in radians |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Cosine of the specified angle |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := COS("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | +1.570796 (π/2) |
| Tag_OutValue | 0 |

The instruction calculates the cosine of the angle specified in the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### TAN: Form tangent value (S7-1500)

##### Description

You use the "Form tangent value" instruction to calculate the tangent of an angle. The size of the angle is specified in radians in the operand.

The value of the result is invalid if the value of the operand is not a valid floating-point number.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Size of angle in radians |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Tangent of the specified angle |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := TAN("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | +3.141593 (π) |
| Tag_OutValue | 0 |

The instruction calculates the tangent of the angle specified in the "Tag_InValue" operand and outputs the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ASIN: Form arcsine value (S7-1500)

##### Description

You use the "Form arcsine value" instruction to calculate the size of the angle that corresponds to the sine value specified in the operand. Only valid floating-point numbers within the range -1 to +1 can be specified for the operand. The calculated angle size can range in value from -π/2 to +π/2.

The value of the result is invalid if any of the following conditions are met:

- The value of the operand is not a valid floating-point number.
- The value of the operand is outside the permitted value range (-1 to +1).

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Sine value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Size of angle in radians |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ASIN("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 1.0 |
| Tag_OutValue | +1.570796 (π/2) |

The instruction calculates the size of the angle corresponding to the sine value in the "Tag_InValue" operand. The result of the instruction is stored in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ACOS: Form arccosine value (S7-1500)

##### Description

You use the "Form arccosine value" instruction to calculate the size of the angle that corresponds to the cosine value specified in the operand. Only valid floating-point numbers within the range -1 to +1 can be specified for the operand. The calculated angle size can range in value from 0 to +π.

The value of the result is invalid if any of the following conditions are met:

- The value of the operand is not a valid floating-point number.
- The value of the operand is outside the permitted value range (-1 to +1).

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Cosine value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Size of angle in radians |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ACOS("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 0 |
| Tag_OutValue | +1.570796 (π/2) |

The instruction calculates the size of the angle corresponding to the cosine value in the "Tag_InValue" operand. The result of the instruction is stored in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ATAN: Form arctangent value (S7-1500)

##### Description

You use the "Form arctangent value" instruction to calculate the size of the angle that corresponds to the tangent value specified in the operand. It is only permitted to specify valid floating-point numbers (or -NaN/+NaN) at the operand. The calculated angle size can range in value from -π/2 to +π/2.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Tangent value |
| &lt;Result&gt; | Output | Floating-point numbers | I, Q, M, D, L, P | Size of angle in radians |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ATAN("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 1.0 |
| Tag_OutValue | +0.785398 (π/4) |

The instruction calculates the size of the angle corresponding to the tangent value in the "Tag_InValue" operand. The result of the instruction is stored in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Invalid floating-point numbers](Data%20types.md#invalid-floating-point-numbers)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### FRAC: Return fraction (S7-1500)

##### Description

You use the "Return fraction" instruction to determine the decimal places of the value in the operand. If the operand contains the value 1.125, for example, the result returns the value 0.125.

The value of the result is invalid if the value of the operand is not a valid floating-point number.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Floating-point numbers | I, Q, M, D, L, P, or constant | Input value, whose decimal places are determined |
| RET_VAL | Output | Floating-point numbers | I, Q, M, D, L, P | Decimal places of the input value |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL FRAC REAL

(IN := "Tag_InValue"

RET_VAL =&gt; "Tag_OutValue"

)

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 1.125 |
| Tag_OutValue | 0.125 |

The instruction copies the decimal places from the value of the "Tag_InValue" operand to the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Move operations (S7-1500)

This section contains information on the following topics:

- [Deserialize: Deserialize (S7-1500)](#deserialize-deserialize-s7-1500)
- [Serialize: Serialize (S7-1500)](#serialize-serialize-s7-1500)
- [MOVE_BLK: Move block (S7-1500)](#move_blk-move-block-s7-1500)
- [MOVE_BLK_VARIANT: Move block (S7-1500)](#move_blk_variant-move-block-s7-1500)
- [UMOVE_BLK: Move block uninterruptible (S7-1500)](#umove_blk-move-block-uninterruptible-s7-1500)
- [FILL_BLK: Fill block (S7-1500)](#fill_blk-fill-block-s7-1500)
- [UFILL_BLK: Fill block uninterruptible (S7-1500)](#ufill_blk-fill-block-uninterruptible-s7-1500)
- [SCATTER: Parse the bit sequence into individual bits (S7-1500)](#scatter-parse-the-bit-sequence-into-individual-bits-s7-1500)
- [SCATTER_BLK: Parse elements of an ARRAY of bit sequence into individual bits (S7-1500)](#scatter_blk-parse-elements-of-an-array-of-bit-sequence-into-individual-bits-s7-1500)
- [GATHER: Merge individual bits into a bit sequence (S7-1500)](#gather-merge-individual-bits-into-a-bit-sequence-s7-1500)
- [GATHER_BLK: Merge individual bits into multiple elements of an ARRAY of bit sequence (S7-1500)](#gather_blk-merge-individual-bits-into-multiple-elements-of-an-array-of-bit-sequence-s7-1500)
- [SWAP: Swap (S7-1500)](#swap-swap-s7-1500)
- [ARRAY DB (S7-1500)](#array-db-s7-1500)
- [Symbolic move (S7-1500)](#symbolic-move-s7-1500)
- [Legacy (S7-1500)](#legacy-s7-1500)

#### Deserialize: Deserialize (S7-1500)

##### Description

You can use the "Deserialize" instruction to convert back the sequential representation of a PLC data type (UDT), STRUCT or ARRAY of &lt;data type&gt; and to fill its entire contents. You can use the instruction to convert multiple serialized data areas back to their deserialized representation form.

If you only want to convert back a single sequential representation of a PLC data type (UDT), STRUCT or ARRAY of &lt;data type&gt;, you can also directly use the instruction "TRCV: Receive data via communication connection".

The memory area "SRC_ARRAY" in which the sequential representation of a PLC data type (UDT), STRUCT or ARRAY of &lt;data type&gt; is located must have the ARRAY of BYTE or ARRAY of CHAR data type and be declared with standard access in version 1.0. The capacity of the standard memory area is 64 KB. Make sure that there is enough memory space prior to the conversion. Optimized memory areas are also permitted as of version 2.0.

When the "SRC_ARRAY" memory area is filled using the "Serialize" instruction, any required filling bytes are automatically inserted. If you fill the "SRC_ARRAY" memory area by other means, you need to insert any required filling bytes yourself. Filling bytes are ignored during deserialization, regardless of whether "SRC_ARRAY" is in an optimized or a standard memory area.

It is recommended to define the low limit of the ARRAY with "0", because then the index within ARRAY corresponds to the value of the POS parameter, e.g. ARRAY[0] = POS 0. The description and example below have been formed based on this.

##### Size of the memory area

The alignment rules mean that simple structures in the optimized memory area do not contain filling bytes. This results in a structure in the optimized memory area being smaller than in the standard memory area. ARRAYs of structures and nested structures contain filling bytes. There is no general rule as to the memory area in which a composed structure requires more space.

Applies to CPUs of the S7-1500 series:

For a block with the block property "Optimized block access", the BOOL has a length of 1 byte. A structure that consists largely of the data type BOOL can therefore be larger in the optimized memory area than in the standard memory area. Composed structures with a low proportion of BOOL data types are smaller in the optimized memory area than in the standard memory area.

##### Optimized memory area

To deserialize larger structures, you can declare the memory area for sequential representation with optimized access for a CPU of the S7-1200 series as of firmware version &gt;= 4.2, and for a CPU of the S7-1500 series as of firmware version &gt;= 2.0. The content of the sequential representation remains unchanged, as for a standard memory area. Only symbolic access to the bytes in the ARRAY is possible.

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC_ARRAY | Input | ARRAY[*] of BYTE <sup>1)</sup>  or  ARRAY of CHAR | I, Q, D, block interface of an FB (the sections Input, Output, Static and Temp are possible).  No I/O data | ARRAY of BYTE or ARRAY of CHAR in which the data stream which is to be deserialized is saved.  S7-1500:  For optimum performance, do not provide the parameter with a VARIANT pointer. |
| DEST_VARIABLE | InOut | all data types | I, Q, D, block interface of an FB,  No I/O data | Tag to which the deserialized data is to be written.   S7-1500:  For optimum performance, do not provide the parameter with a VARIANT pointer. |
| POS | InOut | DINT | I, Q, M, D, L | The operand at the POS parameter stores the index of the first byte based on the number of bytes occupied by the converted customer data. The POS parameter is calculated zero-based. |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information |

##### RET_VAL parameter

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B0 | The memory areas for the SRC_ARRAY and DEST_VARIABLE parameters overlap. |
| 8136 | The tag at the SRC_ARRAY parameter is not in a block with standard access. |
| 8150 | The VARIANT data type at the SRC_ARRAY parameter contains a ZERO pointer. |
| 8151 | No valid reference at the SRC_ARRAY parameter |
| 8153 | There is not enough free memory available at the SRC_ARRAY parameter. |
| 8154 | Invalid data type at the SRC_ARRAY parameter |
| 8250 | A NULL pointer was transferred at parameter DEST_ARRAY. |
| 8251 | No valid reference at the DEST_VARIABLE parameter |
| 8382 | The value at the POS parameter is outside the limits of the array. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

**Special features as of firmware version 4.2 (S7-1200) and 2.0 (S7-1500):**

The following error code has a different meaning:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 8136 | Access to the memory area at the SRC_ARRAY parameter is invalid. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

**Special features as of firmware version 2.8 (S7-1500):**

To improve the performance of the "Deserialize" instruction (Version 2.1), do not provide the SRC_ARRAY and DEST_VARIABLE parameters with a VARIANT pointer but with a specific data type instead.

Note that the error response to the instruction changes as a result: In individual error scenarios, the CPU does not output any error codes but changes to STOP with an access error. To avoid this, use the local error handling with the instructions "GET_ERROR" and "GET_ERR_ID".

**Special features as of firmware version 2.2 (S7-1200/S7-1500):**

With the "Deserialize" instruction (version 2.2), it is no longer permissible to interconnect an element of a technology object (e.g. TO_SpeedAxis.Statusword) to input or output parameters (SRC_ARRAY/DEST_VARIABLE).

**Special features as of firmware version 2.1 (S7-1200/S7-1500):**

The optimized version of the "Deserialize" instruction (as of version V2.1) requires more work memory than its predecessor version due to the complexity of the processed data.

##### Example

The following example shows how the instruction works:

GRAPH

CALL Deserialize VARIANT

(SRC_ARRAY := "Buffer".Field

DEST_VARIABLE =&gt; "Target".Client

POS := #BufferPos

RET_VAL =&gt; #Error

)

The instruction deserializes the sequential representation of the customer data from the "Buffer" tag and writes it to the "Target" tag. The #BufferPos operand stores the index of the first byte based on the number of bytes occupied by the converted customer data.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Basic information on VARIANT (S7-1200, S7-1500)](Data%20types.md#basic-information-on-variant-s7-1200-s7-1500)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)
  
[Structure of an ARRAY tag](Data%20types.md#structure-of-an-array-tag)
  
[Structure of a STRUCT tag](Data%20types.md#structure-of-a-struct-tag)
  
[Structure of a STRING tag](Data%20types.md#structure-of-a-string-tag)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### Serialize: Serialize (S7-1500)

##### Description

You can use the "Serialize" instruction to convert several PLC data types (UDT), STRUCT or ARRAY of &lt;data type&gt; to a sequential representation without losing parts of their structure.

You use the instruction to temporarily save multiple structured data items from your program in a buffer, which should preferably be in a global data block, and send them to another CPU. The memory area in which the converted data is stored must have the ARRAY of BYTE or ARRAY of CHAR data type and be declared with standard access in version 1.0. Optimized data is also permitted as of version 2.0. Fill data of the source data area is undefined in the target array. These can be fill bytes or fill bits of a data area (e.g. ARRAY, STRUCT or PLC data type (UDT)) as well as the characters of a string currently not in use.

The capacity of the standard memory area is 64 KB. Structures that are larger than 64 KB in accordance with the rules for standard memory areas cannot be serialized if the operand at the DEST_ARRAY parameter is located in a standard memory area.

It is recommended to define the low limit of the ARRAY with "0", because then the index within ARRAY corresponds to the value of the POS parameter, e.g. ARRAY[0] = POS 0. The description and example below have been formed based on this.

The operand at the POS parameter contains information about the number of bytes used by the converted data.

If you want to send a single PLC data type (UDT), STRUCT or ARRAY of &lt;data type&gt;, you can directly call the instruction "TSEND: Send data via communication connection".

##### Size of the memory area

The alignment rules mean that simple structures in the optimized memory area do not contain filling bytes. This results in a structure in the optimized memory area being smaller than in the standard memory area. ARRAYs of structures and nested structures contain filling bytes. There is no general rule as to the memory area in which a composed structure requires more space.

Applies to CPUs of the S7-1500 series:

For a block with the block property "Optimized block access", the length of the data type BOOL depends on the data type that follows. This means if a BYTE follows, for example, the data type BOOL has a length of 1 byte. When a WORD follows, for example, the data type BOOL has a length of 2 bytes. A structure that consists largely of the data type BOOL can therefore be larger in the optimized memory area than in the standard memory area. Composed structures with a low proportion of BOOL data types are smaller in the optimized memory area than in the standard memory area.

We therefore recommend that the source data area for the serialization starts with the large data types and ends with Boolean elements. This greatly reduces the filling with filling bits.

##### Optimized memory area

To serialize larger structures, you can declare the memory area with optimized access for a CPU of the S7-1200 series as of firmware version &gt;= 4.2, and for a CPU of the S7-1500 series as of firmware version &gt;= 2.0. The sequential representation remains unchanged, as for a standard memory area.

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC_VARIABLE | Input | all data types | I, Q, D, block interface of an FB,  No I/O data | Tag to be serialized.   S7-1500:  For optimum performance, do not provide the parameter with a VARIANT pointer. |
| DEST_ARRAY | InOut | ARRAY of BYTE or ARRAY of CHAR | I, Q, D, block interface of an FB (the sections Input, Output, Static and Temp are possible).  No I/O data | ARRAY in which the generated data stream is stored.  S7-1500:  For optimum performance, do not provide the parameter with a VARIANT pointer. |
| POS | InOut | DINT | I, Q, M, D, L | The operand at the POS parameter stores the index of the first byte based on the total number of bytes that the converted customer data has occupied. The POS parameter is calculated zero-based. |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information |

You can find additional information on valid data types under "See also".

##### RET_VAL parameter

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B0 | The memory areas for the SRC_VARIABLE and DEST_ARRAY parameters overlap. |
| 8150 | The VARIANT data type at the SRC_VARIABLE parameter contains a ZERO pointer. |
| 8151 | No valid reference at the SRC_VARIABLE parameter |
| 8236 | The tag at the SRC_ARRAY parameter is not in a block with standard access. |
| 8250 | A NULL pointer was transferred at parameter DEST_ARRAY. |
| 8251 | No valid reference at the DEST_ARRAY parameter |
| 8253 | The tag at the parameter DEST_ARRAY does not provide enough memory space for the content of the tag at the parameter SRC_VARIABLE. Due to the input value of the tag at parameter POS the available memory space is reduced. The input value of the parameter POS decides where to begin within the tag at the parameter DEST_ARRAY. |
| 8254 | Invalid data type at the DEST_ARRAY parameter |
| 8382 | The value at the POS parameter is outside the limits of the array. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

**Special features as of firmware version 4.2 (S7-1200) and 2.0 (S7-1500):**

The following error code has a different meaning:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 8236 | Access to the memory area at the DEST_ARRAY parameter is invalid. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

**Special features as of firmware version 2.8 (S7-1500):**

To improve the performance of the "Serialize" instruction (Version 2.1), do not provide the SRC_VARIABLE and DEST_ARRAY parameters with a VARIANT pointer but with a specific data type instead.

Note that the error response to the instruction changes as a result: In individual error scenarios, the CPU does not output any error codes but changes to STOP with an access error. To avoid this, use the local error handling with the instructions "GET_ERROR" and "GET_ERR_ID".

**Special features as of firmware version 2.2 (S7-1200/S7-1500):**

With the "Serialize" instruction (version 2.2), it is no longer permissible to interconnect an element of a technology object (e.g. TO_SpeedAxis.Statusword) to input or output parameters (SRC_VARIABLE/DEST_ARRAY).

**Special features as of firmware version 2.1 (S7-1200/S7-1500):**

The optimized version of the "Serialize" instruction (as of version V2.1) requires more work memory than its predecessor version due to the complexity of the processed data.

##### Example

The following example shows how the instruction works:

GRAPH

CALL Serialize VARIANT

(SRC_VARIABLE := "Source".Client

DEST_ARRAY =&gt; "Buffer".Field

POS := #BufferPos

RET_VAL =&gt; #Error

)

The instruction serializes the customer data from the "Source" tag and writes the sequential representation to the "Buffer" tag. The index of the next unwritten byte of the "Buffer".Field operand is saved in the #BufferPos operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Basic information on VARIANT (S7-1200, S7-1500)](Data%20types.md#basic-information-on-variant-s7-1200-s7-1500)
  
[Basics of PLC data types (UDT)](Data%20types.md#basics-of-plc-data-types-udt)
  
[Structure of an ARRAY tag](Data%20types.md#structure-of-an-array-tag)
  
[Structure of a STRUCT tag](Data%20types.md#structure-of-a-struct-tag)
  
[Structure of a STRING tag](Data%20types.md#structure-of-a-string-tag)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MOVE_BLK: Move block (S7-1500)

##### Description

You use the "Move block" instruction to move the content of a memory area (source range) to another memory area (target range). The number of elements to be moved to the target range is specified with the COUNT parameter. The width of the elements to be moved is defined by the width of the element at the IN parameter.

The instruction can only be executed if the source range and the target range have the same data type.

The value at the output OUT is invalid if more data is copied than is made available at the input IN or at the output OUT.

> **Note**
>
> **Use of ARRAYs**
>
> The instruction copies the contents from the defined element n elements (n = depending on the value at the parameter COUNT) from the source range to the target range, starting at the specified index.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN<sup> 1)</sup> | Input | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | The first element of the source area that is being copied |
| COUNT | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L, P or constant | Number of elements to be copied from the source range to the target range |
| OUT<sup> 1)</sup> | Output | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | The first element of the target range to which the contents of the source range are being copied |
| <sup>1)</sup> The specified data types can only be used as elements of an ARRAY structure. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL MOVE_BLK INT_UINT

(IN := #a_array[2]

COUNT := "Tag_Count"

OUT =&gt; #b_array[1]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | a_array[2] | The data type of the "a_array" operand is ARRAY[0..5] of INT. It consists of six elements of data type INT. |
| COUNT | Tag_Count | 3 |
| OUT | b_array[1] | The data type of the "b_array" operand is ARRAY[0..6] of INT. It consists of seven elements of data type INT. |

Starting from the third element, the instruction selects three INT elements from the #a_array tag and copies their contents to the #b_array output tag, beginning with the second element.

> **Note**
>
> **You can find more information on the MOVE_BLK instruction in the following article in the Siemens Industry Online Support:**
>
> In STEP 7 (TIA Portal) how do you copy memory areas and structured data from one data block to another?
>
> ![Example](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/42603881](https://support.industry.siemens.com/cs/ww/en/view/42603881)

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MOVE_BLK_VARIANT: Move block (S7-1500)

##### Description

You use the "Move block" instruction to move the content of a memory area (source range) to another memory area (target range). You can copy a complete ARRAY or elements of an ARRAY to another ARRAY of the same data type. The size (number of elements) of source and destination ARRAY may be different. You can copy multiple or single elements within an ARRAY.

The number of elements that are to be copied must not exceed the selected source range or target range.

If you use the instruction at the time the block is being created, the ARRAY does not yet have to be known, as the source and the target are transferred per VARIANT.

Counting at the parameters SRC_INDEX and DEST_INDEX always begins with the low limit "0", regardless of the later declaration of the ARRAY.

The instruction is not executed if more data is copied than is made available.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRC | Input<sup> 2)</sup> | VARIANT (which points to an ARRAY or an individual ARRAY element), ARRAY of &lt;Data_type&gt; | L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Source block from which to copy |
| COUNT | Input | UDINT | I, Q, M, D, L or constant | Number of elements which are copied  Assign the value "1" to the parameter COUNT, if no ARRAY is specified at parameter SRC or at parameter DEST. |
| SRC_INDEX | Input | DINT | I, Q, M, D, L or constant | Defines the first element to be copied:  - The SRC_INDEX parameter is calculated zero-based. If an ARRAY is specified at parameter SRC, the integer at parameter SRC_INDEX specifies the first element within the source area from which it is to be copied. Independent of the declared ARRAY limits. - If no Array is specified at parameter SRC or only one single element of an ARRAY is specified, then assign the value "0" at parameter SRC_INDEX. |
| DEST_INDEX | Input | DINT | I, Q, M, D, L or constant | Defines the start of the destination memory area:  - The DEST_INDEX parameter is calculated zero-based. If an ARRAY is specified at parameter DEST, the integer at parameter DEST_INDEX specifies the first element within the target range that is to be copied into. Independent of the declared ARRAY limits. - If no ARRAY is specified at parameter DEST, then assign the value "0" at parameter DEST_INDEX. |
| DEST | Output <sup>1)</sup> | VARIANT | L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Destination area into which the contents of the source block are copied. |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information:  If an error occurs during execution of the instruction, an error code is output at the RET_VAL parameter. |
| 1) The DEST parameter is declared as Output, since the data flow into the tag. However, the tag itself must be declared as InOut in the block interface.  2) With the SRC parameter, the data types BOOL and ARRAY of BOOL are not permitted. |  |  |  |  |

You can find additional information on valid data types under "See also".

##### RET_VAL parameter

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B4 | The data types do not correspond. Instead of an ARRAY of Struct, use an ARRAY of PLC data type (UDT). |
| 8151 | Access to the SRC parameter is not possible. |
| 8152 | The operand at the SRC parameter is not typed. |
| 8153 | Code generation error at the SRC parameter |
| 8154 | The operand at the SRC parameter has the data type BOOL. |
| 8281 | The COUNT parameter has an invalid value |
| 8382 | The first element to be copied, defined via SRC_INDEX, is outside the source array. |
| 8383 | The first element to be copied, defined via SRC_INDEX, is within the source array, and the last element to be copied, defined via SRC_INDEX + COUNT, is outside the source array. |
| 8482 | The first target element defined via DEST_INDEX is outside the target array. |
| 8483 | The first target element defined via DEST_INDEX is within the target array, and the last target element defined via DEST_INDEX + COUNT is outside the target array. |
| 8534 | The DEST parameter is write protected |
| 8551 | Access to the DEST parameter is not possible. |
| 8552 | The operand at the DEST parameter is not typed. |
| 8553 | Code generation error at the DEST parameter |
| 8554 | The operand at the DEST parameter has the data type BOOL. |
| *The error codes can be displayed as integer or hexadecimal value in the program editor. You can find information on switching the display formats under "See also". |  |

##### Example

The following example shows how the instruction works:

GRAPH

CALL MOVE_BLK_VARIANT

(SRC := #SrcField

COUNT := "Tag_Count"

SRC_INDEX := "Tag_Src_Index"

DEST_INDEX := "Tag_Dest_Index"

DEST =&gt;​ #DestField

RET_VAL := "Tag_Result"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Declaration in the block interface | Operand | Value |
| --- | --- | --- | --- |
| SRC | Input | #SrcField | The local operand #SrcField uses a PLC data type that was still unknown at the time when the block was programmed. (ARRAY[0..10] of "MOVE_UDT") |
| COUNT | Input | Tag_Count | 2 |
| SRC_INDEX | Input | Tag_Src_Index | 3 |
| DEST_INDEX | Input | Tag_Dest_Index | 3 |
| DEST | InOut | #DestField | The local operand #DestField uses a PLC data type that was still unknown at the time when the block was programmed. (ARRAY[10..20] of "MOVE_UDT") |

Two elements are moved from the source range, starting from the fourth element of the ARRAY [0..10] of MOVE_UDT, to the target range. The copies are pasted in the ARRAY [10..20] of MOVE_UDT starting from the fourth element.

> **Note**
>
> **You can find more information on the MOVE_BLK_VARIANT instruction in the following article in the Siemens Industry Online Support:**
>
> In STEP 7 (TIA Portal) how do you copy memory areas and structured data from one data block to another?
>
> ![Example](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/42603881](https://support.industry.siemens.com/cs/ww/en/view/42603881)

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Basic information on VARIANT (S7-1200, S7-1500)](Data%20types.md#basic-information-on-variant-s7-1200-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Example of moving data (S7-1200, S7-1500)](Data%20types.md#example-of-moving-data-s7-1200-s7-1500)

#### UMOVE_BLK: Move block uninterruptible (S7-1500)

##### Description

You use the "Move block uninterruptible" instruction to move the content of a memory area (source range) to another memory area (target range). The instruction cannot be interrupted. The number of elements to be moved to the target range is specified with the COUNT parameter. The width of the elements to be moved is defined by the width of the element at the IN parameter.

The instruction can only be executed if the source range and the target range have the same data type.

> **Note**
>
> **Move uninterruptible**
>
> The move operation cannot be interrupted by other operating system activities. This is why the interrupt reaction times of the CPU increase during the execution of the "Move block uninterruptible" instruction.

The value at the output OUT is invalid if more data is copied than is made available at the input IN or at the output OUT.

You use the "Move block uninterruptible" instruction to move a maximum of 16 KB. Note the CPU-specific restrictions for this.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN<sup> 1)</sup> | Input | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | The first element of the source area that is being copied |
| COUNT | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L, P or constant | Number of elements to be copied from the source range to the target range |
| OUT<sup> 1)</sup> | Output | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | The first element of the target range to which the contents of the source range are being copied |
| <sup>1)</sup> The specified data types can only be used as elements of an ARRAY structure. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL UMOVE_BLK INT_UINT

(IN := #a_array[2]

COUNT := "Tag_Count"

OUT =&gt; #b_array[1]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | a_array[2] | The data type of the "a_array" operand is ARRAY[0..5] of INT. It consists of six elements of data type INT. |
| COUNT | Tag_Count | 3 |
| OUT | b_array[1] | The data type of the "b_array" operand is ARRAY[0..6] of INT. It consists of seven elements of data type INT. |

Starting from the third element, the instruction selects three INT elements from the #a_array tag and copies their contents to the #b_array output tag, beginning with the second element. The move operation cannot be interrupted by other operating system activities.

> **Note**
>
> **You can find more information on the UMOVE_BLK instruction in the following article in the Siemens Industry Online Support:**
>
> In STEP 7 (TIA Portal) how do you copy memory areas and structured data from one data block to another?
>
> ![Example](images/84907645963_DV_resource.Stream@PNG-de-DE.png)
> [https://support.industry.siemens.com/cs/ww/en/view/42603881](https://support.industry.siemens.com/cs/ww/en/view/42603881)

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### FILL_BLK: Fill block (S7-1500)

##### Description

You can use the "Fill block" instruction to fill a memory area (target range) with the value of the IN input. The target range is filled beginning with the address specified at the OUT output. The number of repeated copy operations is specified with the COUNT parameter. When the instruction is executed, the value at the input IN is moved to the target range as often as specified by the value of the COUNT parameter.

The instruction can only be executed if the source range and the target range have the same data type.

The maximum number of elements changed is the number of elements in the ARRAY or structure. If you copy more data than there are elements at the OUT output, you will get an unintended result.

> **Note**
>
> **Use of ARRAYs**
>
> The instruction reads the content from the selected element from the source range and copies this content n-times (n = depending on the value at the parameter COUNT) to the destination, starting at the specified index.

##### Filling structures

As well as the elements of an ARRAY, you can also fill multiple elements of a structure (STRUCT, PLC data type) with the same value. The structure whose elements you want to fill must only contain individual elements of the same elementary data type. The structure itself can, however, be embedded in another structure.

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | I, Q, M, D, L, P or constant | Element used to fill the target range |
| COUNT | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L, P or constant | Number of repeated move operations |
| OUT | Output | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | Address in target range from which filling starts |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example with an ARRAY

The following example shows how the instruction works when you want to fill an ARRAY:

GRAPH

CALL FILL_BLK INT_UINT

(IN := #FillValue

COUNT := "Tag_Count"

OUT =&gt; #TargetArea[1]

)

The following table shows how the instruction works using specific operand values:

| Parameters | Operand | Value |
| --- | --- | --- |
| IN | FillValue | The data type of the operand is INT. |
| COUNT | Tag_Count | 3 |
| OUT | TargetArea | The data type of the operand TargetArea is ARRAY[1..5] of INT. It consists of five elements of data type INT. |

The instruction copies the value of the operand #FillValue to the #TargetArea output tag three times, starting with the first element.

##### Examples with a structure

The following examples show how the instruction works when you want to fill a structure:

Create a global data block with the following elements:

| Data_block_1 |  |  |  |  | Data type |
| --- | --- | --- | --- | --- | --- |
| MyStruct1 |  |  |  |  | STRUCT |
|  | Member_1 |  |  |  | INT |
| Member_2 |  |  |  | INT |  |
| Member_3 |  |  |  | INT |  |
| Member_4 |  |  |  | INT |  |
| MyStruct2 |  |  |  |  | STRUCT |
|  | SubArray |  |  |  | ARRAY[1..2] of STRUCT |
|  | SubArray[1] |  |  | STRUCT |  |
|  | NestedStruct |  | STRUCT |  |  |
|  | Member_1 | INT |  |  |  |
| Member_2 | INT |  |  |  |  |
| Member_3 | INT |  |  |  |  |
| Member_4 | INT |  |  |  |  |
| SubArray[2] |  |  | STRUCT |  |  |
|  | NestedStruct |  | STRUCT |  |  |
|  | Member_1 | INT |  |  |  |
| Member_2 | INT |  |  |  |  |
| Member_3 | INT |  |  |  |  |
| Member_4 | INT |  |  |  |  |

Generate the following program code to address the MyStruct1 tag:

GRAPH

CALL FILL_BLK INT_UINT

(IN := 10

COUNT := 2

OUT =&gt; "Data_block_1".MyStruct1.Member_2

)

Generate the following program code to address the MyStruct2 tag:

GRAPH

CALL FILL_BLK INT_UINT

(IN := 10

COUNT := 2

OUT =&gt; "Data_block_1".MyStruct2.SubArray[1].NestedStruct.Member_2

)

In each of the two examples, the value 10 of the IN parameter is copied twice to the operand at the OUT parameter, starting with the element Member_2. This means that the value 10 is copied to the elements Member_2 and Member_3. The other two elements, Member_1 and Member_4, are not changed.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### UFILL_BLK: Fill block uninterruptible (S7-1500)

##### Description

You can use the "Fill block uninterruptible" instruction to fill a memory area (target range) with the value of the IN input. The instruction cannot be interrupted. The target range is filled beginning with the address specified at the OUT output. The number of repeated copy operations is specified with the COUNT parameter. When the instruction is executed, the value at the input IN is moved to the target range as often as specified by the value of the COUNT parameter.

The instruction can only be executed if the source range and the target range have the same data type.

> **Note**
>
> The move operation cannot be interrupted by other operating system activities. This is why the alarm reaction times of the CPU increase during the execution of the "Fill block uninterruptible" instruction.

The maximum number of elements changed is the number of elements in the ARRAY or structure. If you copy more data than there are elements at the OUT output, you will get an unintended result.

> **Note**
>
> **Use of ARRAYs**
>
> The instruction reads the content from the selected element from the source range and copies this content n-times (n = depending on the value at the parameter COUNT) to the destination, starting at the specified index.

You use the "Fill block uninterruptible" instruction to move a maximum of 16 KB. Note the CPU-specific restrictions for this.

##### Filling structures

As well as the elements of an ARRAY, you can also fill multiple elements of a structure (STRUCT, PLC data type) with the same value. The structure whose elements you want to fill must only contain individual elements of the same elementary data type. The structure itself can, however, be embedded in another structure.

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | I, Q, M, D, L, P or constant | Element used to fill the target range |
| COUNT | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L, P or constant | Number of repeated move operations |
| OUT | Output | Binary numbers, integers, floating-point numbers, timers, TOD, LTOD, DATE, CHAR, WCHAR | D, L | Address in target range from which filling starts |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example with an ARRAY

The following example shows how the instruction works when you want to fill an ARRAY:

GRAPH

CALL UFILL_BLK INT_UINT

(IN := #FillValue

COUNT := "Tag_Count"

OUT =&gt; #TargetArea[1]

)

The following table shows how the instruction works using specific operand values:

| Parameters | Operand | Value |
| --- | --- | --- |
| IN | FillValue | The data type of the operand is INT. |
| COUNT | Tag_Count | 3 |
| OUT | TargetArea | The data type of the operand TargetArea is ARRAY[1..5] of INT. It consists of five elements of data type INT. |

The instruction copies the value of the operand #FillValue to the #TargetArea output tag three times, starting with the first element. The move operation cannot be interrupted by other operating system activities.

##### Examples with a structure

The following examples show how the instruction works when you want to fill a structure:

Create a global data block with the following elements:

| Data_block_1 |  |  |  |  | Data type |
| --- | --- | --- | --- | --- | --- |
| MyStruct1 |  |  |  |  | STRUCT |
|  | Member_1 |  |  |  | INT |
| Member_2 |  |  |  | INT |  |
| Member_3 |  |  |  | INT |  |
| Member_4 |  |  |  | INT |  |
| MyStruct2 |  |  |  |  | STRUCT |
|  | SubArray |  |  |  | ARRAY[1..2] of STRUCT |
|  | SubArray[1] |  |  | STRUCT |  |
|  | NestedStruct |  | STRUCT |  |  |
|  | Member_1 | INT |  |  |  |
| Member_2 | INT |  |  |  |  |
| Member_3 | INT |  |  |  |  |
| Member_4 | INT |  |  |  |  |
| SubArray[2] |  |  | STRUCT |  |  |
|  | NestedStruct |  | STRUCT |  |  |
|  | Member_1 | INT |  |  |  |
| Member_2 | INT |  |  |  |  |
| Member_3 | INT |  |  |  |  |
| Member_4 | INT |  |  |  |  |

Generate the following program code to address the MyStruct1 tag:

GRAPH

CALL UFILL_BLK INT_UINT

(IN := 10

COUNT := 2

OUT =&gt; "Data_block_1".MyStruct1.Member_2

)

Generate the following program code to address the MyStruct2 tag:

GRAPH

CALL UFILL_BLK INT_UINT

(IN := 10

COUNT := 2

OUT =&gt; "Data_block_1".MyStruct2.SubArray[1].NestedStruct.Member_2

)

In each of the two examples, the value 10 of the IN parameter is copied twice to the operand at the OUT parameter, starting with the element Member_2. This means that the value 10 is copied to the elements Member_2 and Member_3. The other two elements, Member_1 and Member_4, are not changed.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SCATTER: Parse the bit sequence into individual bits (S7-1500)

##### Description

The "Parse the bit sequence into individual bits" instruction parses a tag of the BYTE, WORD, DWORD or LWORD data type into individual bits and saves them in an ARRAY of BOOL, an anonymous STRUCT or a PLC data type exclusively with Boolean elements.

> **Note**
>
> **Multi-dimensional ARRAY of BOOL**
>
> With the "Parse the bit sequence into individual bits" instruction, the use of a multidimensional ARRAY of BOOL is not permitted.

> **Note**
>
> **Length of the ARRAY, STRUCT or PLC data type**
>
> The ARRAY, the anonymous STRUCT or the PLC data type must have exactly the number of elements that is specified by the bit sequence.
>
> This means for the data type BYTE, for example, the ARRAY, STRUCT or the PLC data type must have exactly 8 elements (WORD = 16, DWORD = 32 and LWORD = 64).

> **Note**
>
> **Availability of the instruction**
>
> The instruction can be used with a CPU of the S7-1500 series as of firmware version 2.1.

This way you can, for example, parse a status word, and read and change the status of the individual bits using the index. Using GATHER, you can merge the bits once again into a bit sequence.

The ENO enable output returns the signal state "0" if the ARRAY does not provide enough BOOL elements.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | BYTE, WORD, DWORD, LWORD | I, Q, M, D, L | Bit sequence that is parsed.  The values must not be located in the I/O area or in the DB of a technology object. |
| OUT | Output | ARRAY[*] of BOOL, STRUCT or PLC data type  *: 8, 16, 32 or 64 elements | I, Q, M, D, L | ARRAY, STRUCT or PLC data type in which the individual bits are stored |

You can find additional information on valid data types under "See also".

##### Example with an ARRAY

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceWord | Input | WORD |
| DestinationArray | Output | ARRAY[0..15] of BOOL |

The following example shows how the instruction works:

GRAPH

CALL SCATTER

(IN := #SourceWord

OUT =&gt; #DestinationArray

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceWord | WORD (16 bits) |
| OUT | DestinationArray | The operand "DestinationArray" is of the data type ARRAY[0..15] of BOOL. It consists of 16 elements and is therefore just as large as the WORD that is to be parsed. |

The #SourceWord operand of the WORD data type is parsed into its individual bits (16) and assigned to the individual elements of the #DestinationArray operand.

##### Example with a PLC data type (UDT)

Create the following PLC data type "myBits":

![Example with a PLC data type (UDT)](images/100514277003_DV_resource.Stream@PNG-en-US.png)

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceWord | Input | WORD |
| DestinationUDT | Output | "myBits" |

The following example shows how the instruction works:

GRAPH

CALL SCATTER

(IN := #SourceWord

OUT =&gt; #DestinationUDT

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceWord | WORD (16 bits) |
| OUT | DestinationUDT | The "DestinationUDT" operand has the PLC data type (UDT). It consists of 16 elements and is therefore just as large as the WORD that is to be parsed. |

The #SourceWord operand of the WORD data type is parsed into its individual bits (16) and assigned to the individual elements of the #DestinationUDT operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SCATTER_BLK: Parse elements of an ARRAY of bit sequence into individual bits (S7-1500)

##### Description

The "Parse elements of an ARRAY of bit sequence into individual bits" instruction parses one or more elements of an ARRAY of BYTE, WORD, DWORD or LWORD into individual bits and saves them in an ARRAY of BOOL, an anonymous STRUCT or a PLC data type exclusively with Boolean elements. At the COUNT_IN parameter you specify how many elements of the source ARRAY are going to be parsed. The source ARRAY at the IN parameter may have more elements than specified at the COUNT_IN parameter. The ARRAY of BOOL, the anonymous STRUCT or the PLC data type must have sufficient elements to save the bits of the parsed bit sequences. However, the destination memory area may also be larger.

> **Note**
>
> **Multi-dimensional ARRAY of BOOL**
>
> If the ARRAY is a multi-dimensional ARRAY of BOOL, the padding bits of the dimensions contained are counted as well even if they were not explicitly declared and are not accessible.
>
> Example 1: An ARRAY[1..10,0..4,1..2] of BOOL is handled like an ARRAY[1..10,0..4,1..8] of BOOL or like an ARRAY[0..399] of BOOL.
>
> Example 2: At the IN parameter, an ARRAY[0..5] of WORD (sourceArrayWord[2]) is interconnected. The COUNT_IN parameter has the value "3". At the OUT parameter, an ARRAY[0..1,0..5,0..7] of BOOL (destinationArrayBool[0,0,0]) is interconnected. Both the array at the IN parameter and at the OUT parameter has a size of 96 bits. The ARRAY of WORD is parsed into 48 individual bits.

> **Note**
>
> **If the ARRAY low limit of the target ARRAY is not "0", note the following:**
>
> For performance reasons the index must always start at a BYTE, WORD, DWORD or LWORD limit. This means the index must be calculated starting at the low limit of the ARRAY. The following formula is used as basis for this calculation:
>
> Valid indices = ARRAY low limit + n(number of bit sequences) × number of bits of the desired bit sequence
>
> For an ARRAY[-2..45] of BOOL and the bit sequence WORD the calculation looks as follows:
>
> - Valid index (-2) = -2 + 0 × 16
> - Valid index (14) = -2 + 1 × 16
> - Valid index (30) = -2 + 2 × 16
>
> You can find an example described below.

> **Note**
>
> **Availability of the instruction**
>
> The instruction can be used with a CPU of the S7-1500 series as of firmware version 2.1.

This way you can, for example, parse status words, and read and change the status of the individual bits using the index. Using GATHER, you can merge the bits once again into a bit sequence.

The enable output ENO returns signal state "0" if one of the following conditions applies:

- The source ARRAY has fewer elements than specified at the COUNT_IN parameter.
- The index of the destination ARRAY does not start at a BYTE, WORD, DWORD or LWORD limit. In this case, no result is written to the ARRAY of BOOL.
- The ARRAY[*] of BOOL, STRUCT or PLC data type does not provide the required number of elements. In this case as many bit sequences as possible are parsed and written to the ARRAY of BOOL, the anonymous STRUCT or the PLC data type. The remaining bit sequences are no longer taken into account.

> **Note**
>
> **S7-1200-CPU: Enable output ENO = 0**
>
> When the enable output ENO has signal state "0", no data are written to the output parameter OUT.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Element of an ARRAY[*] of  - BYTE  - WORD  - DWORD  - LWORD | I, Q, M, D, L | ARRAY of &lt;bit sequence&gt; that is parsed.  The values must not be located in the I/O area or in the DB of a technology object. |
| COUNT_IN | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L | Counter for the number of elements of the source ARRAY that are going to be parsed.  The value must not be in the I/O area or in the database of a technology object. |
| OUT | Output | Element of an ARRAY[*] of   - BOOL  - STRUCT  - PLC data type | I, Q, M, D, L | ARRAY, STRUCT or PLC data type in which the individual bits are stored |

You can select the required bit sequence from the "???" drop-down list of the instruction box.

You can find additional information on valid data types under "See also".

##### Example of a destination ARRAY with the low limit "0"

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceArrayWord | Input | ARRAY[0..5] of WORD |
| CounterInput | UDINT |  |
| DestinationArrayBool | Output | ARRAY[0..95] of BOOL |

The following example shows how the instruction works:

GRAPH

CALL SCATTER_BLK

(IN := #SourceArrayWord[2]

COUNT_IN := #CounterInput

OUT =&gt; #DestinationArrayBool[0]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceArrayWord[2] | ARRAY[0..5] of WORD (96 bits can be parsed.) |
| COUNT_IN | CounterInput = 3 | UDINT3 (3 WORDs or 48 bits are to be parsed. This means at least 48 bits must be available in the destination ARRAY.) |
| OUT | DestinationArrayBool[0] | The operand "DestinationArrayBool" is of the data type ARRAY[0..95] of BOOL. This means it provides 96 BOOL elements. |

The 3rd, 4th and 5th WORD of the #SourceArrayWord operand is parsed into its individual bits (48) and as of the 1st element assigned to the individual elements of the #DestinationArrayBool operand.​

##### Example of a destination ARRAY with the low limit "-2"

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceArrayWord | Input | ARRAY[0..5] of WORD |
| CounterInput | UDINT |  |
| DestinationArrayBool | Output | ARRAY[-2..93] of BOOL |

The following example shows how the instruction works:

GRAPH

CALL SCATTER_BLK

(IN := #SourceArrayWord[2]

COUNT_IN := #CounterInput

OUT =&gt; #DestinationArrayBool[14]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceArrayWord[2] | ARRAY[0..5] of WORD (96 bits can be parsed.) |
| COUNT_IN | CounterInput = 3 | UDINT3 (3 WORDs or 48 bits are to be parsed. This means at least 48 bits must be available in the destination ARRAY.) |
| OUT | DestinationArrayBool[14] | The operand "DestinationArrayBool" is of the data type ARRAY[-2..93] of BOOL. This means it provides 96 BOOL elements. |

The 3rd, 4th and 5th WORD of the #SourceArrayWord operand is parsed into its individual bits (48) and as of the 16th element assigned to the individual elements of the #DestinationArrayBool operand. The remaining 32 bits are not written.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### GATHER: Merge individual bits into a bit sequence (S7-1500)

##### Description

The "Merge individual bits into a bit sequence" instruction merges the bits from an ARRAY of BOOL, an anonymous STRUCT or a PLC data type exclusively with Boolean elements into a bit sequence. The bit sequence is saved in a tag of the data type BYTE, WORD, DWORD or LWORD.

> **Note**
>
> **Multi-dimensional ARRAY of BOOL**
>
> With the "Merge individual bits into a bit sequence" instruction, the use of a multidimensional ARRAY of BOOL is not permitted.

> **Note**
>
> **Length of the ARRAY, STRUCT or PLC data type**
>
> The ARRAY, STRUCT or the PLC data type must have exactly the number of elements that is specified by the bit sequence.
>
> This means for the data type BYTE, for example, the ARRAY, anonymous STRUCT or the PLC data type must have exactly 8 elements (WORD = 16, DWORD = 32 and LWORD = 64).

> **Note**
>
> **Availability of the instruction**
>
> The instruction can be used with a CPU of the S7-1500 series as of firmware version 2.1.

The ENO enable output returns the signal state "0", if the ARRAY, anonymous STRUCT or the PLC data type has fewer or more BOOL elements than specified by the bit sequence. The BOOL elements are not transferred then. The ENO also returns "0" if fewer than the necessary number of bits is available.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | ARRAY[*] of BOOL, STRUCT or PLC data type  *: 8, 16, 32 or 64 elements | I, Q, M, D, L | ARRAY, STRUCT or PLC data type, the bits of which are merged into a bit sequence.  The values must not be located in the I/O area or in the DB of a technology object. |
| OUT | Output | BYTE, WORD, DWORD, LWORD | I, Q, M, D, L | Merged bit sequence, saved in a tag |

You can select the required bit sequence from the "???" drop-down list of the instruction box.

You can find additional information on valid data types under "See also".

##### Example with an ARRAY

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceArray | Input | ARRAY[0..15] of BOOL |
| DestinationWord | Output | WORD |

The following example shows how the instruction works:

GRAPH

CALL GATHER

(IN := #SourceArray

OUT =&gt; #DestinationWord

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceArray | The operand "SourceArray" is of the data type ARRAY[0..15] of BOOL. It consists of 16 elements and is therefore just as large as the WORD in which the bits are to be merged. |
| OUT | DestinationWord | WORD (16 bits) |

The bits of the #SourceArray operand are merged into a WORD.

##### Example with a PLC data type (UDT)

Create the following PLC data type "myBits":

![Example with a PLC data type (UDT)](images/100514277003_DV_resource.Stream@PNG-en-US.png)

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceUDT | Input | "myBits" |
| DestinationWord | Output | WORD |

The following example shows how the instruction works:

GRAPH

CALL GATHER

(IN := #SourceUDT

OUT =&gt; #DestinationWord

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceUDT | The "SourceUDT" operand has the PLC data type (UDT). It consists of 16 elements and is therefore just as large as the WORD in which the bits are to be merged. |
| OUT | DestinationWord | WORD (16 bits) |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### GATHER_BLK: Merge individual bits into multiple elements of an ARRAY of bit sequence (S7-1500)

##### Description

The "Merge individual bits into multiple elements of an ARRAY of bit sequence" instruction merges the bits from an ARRAY of BOOL, an anonymous STRUCT or a PLC data type exclusively with Boolean elements into one or multiple elements of an ARRAY of &lt;bit sequence&gt;. At the COUNT_OUT parameter you specify how many elements of the destination ARRAY are going to be written. With this step you also implicitly specify how many elements of the ARRAY of BOOL, the anonymous STRUCT or the PLC data type are required. The destination ARRAY at the OUT parameter may have more elements than specified at the COUNT_OUT parameter. The ARRAY of &lt;bit sequence&gt; must have sufficient elements to save the bits that are going to be merged. However, the destination ARRAY may also be larger.

> **Note**
>
> **Multi-dimensional ARRAY of BOOL**
>
> If the ARRAY is a multi-dimensional ARRAY of BOOL, the padding bits of the dimensions contained are counted as well even if they were not explicitly declared and are not accessible.
>
> Example 1: An ARRAY[1..10,0..4,1..2] of BOOL is handled like an ARRAY[1..10,0..4,1..8] of BOOL or like an ARRAY[0..399] of BOOL.
>
> Example 2: At the OUT parameter, an ARRAY[0..5] of WORD (sourceArrayWord[2]) is interconnected. The COUNT_IN parameter has the value "3". At the IN parameter, an ARRAY[0..1,0..5,0..7] of BOOL (destinationArrayBool[0,0,0]) is interconnected. Both the array at the IN parameter and at the OUT parameter has a size of 96 bits. 48 individual bits are merged from the ARRAY of BOOL.

> **Note**
>
> **If the ARRAY low limit of the source ARRAY is not "0", note the following:**
>
> For performance reasons the index must always start at a BYTE, WORD, DWORD or LWORD limit. This means the index must be calculated starting at the low limit of the ARRAY. The following formula is used as basis for this calculation:
>
> Valid indices = ARRAY low limit + n(number of bit sequences) × number of bits of the desired bit sequence
>
> For an ARRAY[-2..45] of BOOL and the bit sequence WORD the calculation looks as follows:
>
> - Valid index (-2) = -2 + 0 × 16
> - Valid index (14) = -2 + 1 × 16
> - Valid index (30) = -2 + 2 × 16
>
> You can find an example described below.

> **Note**
>
> **Availability of the instruction**
>
> The instruction can be used with a CPU of the S7-1500 series as of firmware version 2.1.

The enable output ENO returns signal state "0" if one of the following conditions applies:

- The index of the source ARRAY does not start at a BYTE, WORD, DWORD or LWORD limit. In this case, no result is written to the ARRAY of &lt;bit sequence&gt;.
- The ARRAY[*] of &lt;bit sequence&gt; does not provide the required number of elements. In this case as many bit sequences as possible are merged and written to the ARRAY of &lt;bit sequence&gt;. The remaining bits are no longer taken into account.

> **Note**
>
> **S7-1200-CPU: Enable output ENO = 0**
>
> When the enable output ENO has signal state "0", no data are written to the output parameter OUT.

##### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Element of an ARRAY[*] of   - BOOL  - STRUCT  - PLC data type | I, Q, M, D, L | ARRAY of BOOL, STRUCT or PLC data type whose bits are merged (source ARRAY)  The values must not be located in the I/O area or in the DB of a technology object. |
| COUNT_OUT | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L | Counter how many elements of the target ARRAY are to be described.  The value must not be in the I/O area or in the database of a technology object. |
| OUT | Output | Element of an ARRAY[*] of  - BYTE  - WORD  - DWORD  - LWORD | I, Q, M, D, L | ARRAY of &lt;bit sequence&gt; to which the bits are saved (destination ARRAY) |

You can find additional information on valid data types under "See also".

##### Example of a source ARRAY with the low limit "0"

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceArrayBool | Input | ARRAY[0..95] of BOOL |
| CounterOutput | UDINT |  |
| DestinationArrayWord | Output | ARRAY[0..5] of WORD |

The following example shows how the instruction works:

GRAPH

CALL GATHER_BLK

(IN := #SourceArrayBool[0]

COUNT_OUT := #CounterOutput

OUT =&gt; #DestinationArrayWord[2]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceArrayBool[0] | The operand "SourceArrayBool" is of the data type ARRAY[0..95] of BOOL. This means it provides 96 BOOL elements that can merged into words once again. |
| COUNT_OUT | CounterOutput = 3 | UDINT3 (3 words are to be written. This means 48 bits must be available in the source ARRAY.) |
| OUT | DestinationArrayWord[2] | The operand "DestinationArrayWord" is of the data type ARRAY[0..5] of WORD. This means 6 WORD elements are available. |

As of the 1st element of the #SourceArrayBool operand, 48 bits are merged in the #DestinationArrayWord operand. The starting point in the destination ARRAY is the 3rd element. This means that the first 16 bits are written into the 3rd word, the second 16 nits into the 4th word and the third 16 bits into the 5th word of the destination ARRAY.

##### Example of a source ARRAY with the low limit "-2"

Create the following tags in the block interface:

| Tag | Section | Data type |
| --- | --- | --- |
| SourceArrayBool | Input | ARRAY[-2..93] of BOOL |
| CounterOutput | UDINT |  |
| DestinationArrayWord | Output | ARRAY[0..5] of WORD |

The following example shows how the instruction works:

GRAPH

CALL GATHER_BLK

(IN := #SourceArrayBool[14]

COUNT_OUT := #CounterOutput

OUT =&gt; #DestinationArrayWord[2]

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Data type |
| --- | --- | --- |
| IN | SourceArrayBool[14] | The operand "SourceArrayBool" is of the data type ARRAY[-2..93] of BOOL. Because the starting point is the 16th element, only 80 BOOL elements that can be merged into words again are available. |
| COUNT_OUT | CounterOutput = 3 | UDINT3 (3 words are to be written. This means 48 bits must be available in the source ARRAY.) |
| OUT | DestinationArrayWord[2] | The operand "DestinationArrayWord" is of the data type ARRAY[0..5] of WORD. This means 6 WORD elements are available. |

Starting with the 16th element of the #SourceArrayBool operand, 48 bits are merged into the #DestinationArrayWord operand. The starting point in the destination ARRAY is the 3rd element. This means the first 16 bits of the source ARRAY are ignored. The second 16 Bits are written into the 3rd word, the third 16 bits into the 4th word and the fourth 16 bits into the 5th word of the destination ARRAY. The remaining 64 bits of the source ARRAY are not taken into account either.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SWAP: Swap (S7-1500)

##### Description

You use the "Swap" instruction to change the order of the bytes of the operand.

Depending on the data type used, you can swap all bytes in accumulator 1 or only the bytes in the right word of accumulator 1.

The following figure shows how the bytes of the operand of data type DWORD are swapped:

![Description](images/96822048651_DV_resource.Stream@PNG-en-US.png)

##### Order of bytes in the right word of accumulator 1

For data type WORD, you swap the bytes in the right word of accumulator 1.

The following table shows the contents of accumulator 1 before and after execution of the instruction:

| Status | Bytes in accumulator 1 |  |  |  |
| --- | --- | --- | --- | --- |
| Before execution | Value A | Value B | Value C | Value D |
| After execution | Value A | Value B | Value D | Value C |

The result of the instruction is saved in the right word of accumulator 1. The bytes in the left word of accumulator 1 are not influenced by the instruction and remain unchanged.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | WORD, DWORD, LWORD | I, Q, M, D, L or constant | Operand whose bytes are swapped |
| &lt;Result&gt; | Output | WORD, DWORD, LWORD | I, Q, M, D, L | Result |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SWAP("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |  |  |
| --- | --- | --- | --- | --- |
| Tag_InValue | 0000 | 1111 | 0000 | 1111 |
| Tag_OutValue | 0000 | 1111 | 1111 | 0000 |

Swapping all bytes in accumulator 1:

For data type DWORD, you swap all bytes in accumulator 1.

The following table shows the contents of accumulator 1 before and after execution of the instruction:

| Status | Bytes in accumulator 1 |  |  |  |
| --- | --- | --- | --- | --- |
| Before execution | Value A | Value B | Value C | Value D |
| After execution | Value D | Value C | Value B | Value A |

The result of the instruction is saved in accumulator 1. The content of accumulator 2 remains unchanged.

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tag_InValue | 1111 | 0000 | 0000 | 1111 | 0000 | 0000 | 1111 | 1111 |
| Tag_OutValue | 1111 | 1111 | 0000 | 0000 | 0000 | 1111 | 1111 | 0000 |

The bytes in the "Tag_InValue" operand are swapped and stored in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ARRAY DB (S7-1500)

This section contains information on the following topics:

- [ReadFromArrayDB: Read from array data block (S7-1500)](#readfromarraydb-read-from-array-data-block-s7-1500)
- [WriteToArrayDB: Write to array data block (S7-1500)](#writetoarraydb-write-to-array-data-block-s7-1500)
- [ReadFromArrayDBL: Read from array data block in load memory (S7-1500)](#readfromarraydbl-read-from-array-data-block-in-load-memory-s7-1500)
- [WriteToArrayDBL: Write to array data block in load memory (S7-1500)](#writetoarraydbl-write-to-array-data-block-in-load-memory-s7-1500)

##### ReadFromArrayDB: Read from array data block (S7-1500)

###### Description

The instruction "Read from ARRAY data block" is used to read data from a data block of the ARRAY DB block type and write it to a destination area.

An ARRAY data block is a data block that consists of exactly one ARRAY of [Data type]. The elements of the ARRAY can be of PLC data type or any other elementary data type. Counting of the ARRAY always begins with the low limit "0".

###### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DB | Input | DB_ANY | I, Q, M, D, L | Data block that is read |
| INDEX | Input | DINT | I, Q, M, D, L, P or constant | Element in the DB that is read. The specification can be a constant, a global tag or an indexed value. |
| VALUE | Output <sup>1)</sup> | VARIANT | L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Value that is read and output |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Result of the instruction |
| 1) The VALUE parameter is declared as Output, since the data flow into the tag. However, the tag itself must be declared as InOut in the block interface. |  |  |  |  |

You can find additional information on valid data types under "See also".

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B4 | The element data type stored in the ARRAY data block does not match the element data type transferred in the VARIANT. |
| 80B5 | The copying was interrupted. |
| 8132 | The data block does not exist, is too short, write protected, or is located in load memory. |
| 8135 | The ARRAY data block contains invalid values. |
| 8154 | The data block has the incorrect data type. |
| 8282 | The value at the INDEX parameter is outside the limits of the ARRAY. |
| 8450 | The data type VARIANT at parameter VALUE provides the value "0". |
| 8452 | Code generation error |
| 8453 | There are two possible causes of the error:  - The size of the VALUE parameter does not match the element length in the ARRAY data block. - The two tags are not in a memory area with optimized access. For additional information on the memory area access types, refer to: [Basics of block access](Programming%20basics.md#basics-of-block-access) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL ReadFromArrayDB

(DB := "ArrayDB"

INDEX := 2

VALUE =&gt; "TargetField"

RET_VAL =&gt; "TagResult"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| DB | ArrayDB | The "ArrayDB" operand is an ARRAY DB of the data type Array [0 to 10] of INT. |
| INDEX | 2 | 2nd element of the "ArrayDB" |
| VALUE | TargetField | The "TargetField" operand is a global tag of the data type INT. |

The element is read from "ArrayDB" and written to the "TargetField" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Example of the use of ARRAY data blocks](Programming%20basics.md#example-of-the-use-of-array-data-blocks)

##### WriteToArrayDB: Write to array data block (S7-1500)

###### Description

The instruction "Write to ARRAY data block" is used to write data to a data block of the ARRAY DB block type.

An ARRAY data block is a data block that consists of exactly one ARRAY of [Data type]. The elements of the ARRAY can be of PLC data type or any other elementary data type. Counting of the ARRAY always begins with the low limit "0".

###### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DB | Input | DB_ANY | I, Q, M, D, L | Data block to which data is written |
| INDEX | Input | DINT | I, Q, M, D, L, P or constant | Element in the DB to which data is written. The specification can be a constant, a global tag or an indexed value. |
| VALUE | Input | VARIANT | L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Value to be written |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Result of the instruction |

You can find additional information on valid data types under "See also".

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B4 | The element data type stored in the ARRAY data block does not match the element data type transferred in the VARIANT. |
| 80B5 | The copying was interrupted. |
| 8132 | The data block does not exist, is too short, or is located in load memory. |
| 8134 | The data block is write protected. |
| 8135 | The data block is not an ARRAY data block. |
| 8154 | The data block has the incorrect data type. |
| 8282 | The value at the INDEX parameter is outside the limits of the ARRAY. |
| 8350 | The data type VARIANT at parameter VALUE provides the value "0". |
| 8352 | Code generation error |
| 8353 | There are two possible causes of the error:  - The size of the VALUE parameter does not match the element length in the ARRAY data block. - The two tags are not in a memory area with optimized access. For additional information on the memory area access types, refer to: [Basics of block access](Programming%20basics.md#basics-of-block-access) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL WriteToArrayDB

(DB := "ArrayDB"

INDEX := 2

VALUE := "SourceField"

RET_VAL =&gt; "TagResult"

)

The following table shows how the instruction works using specific operand values:

| Parameters | Operand | Value |
| --- | --- | --- |
| DB | ArrayDB | The "ArrayDB" operand is an ARRAY DB of the data type Array [0 to 10] of INT. |
| INDEX | 2 | 2nd element of the "ArrayDB" |
| VALUE | SourceField | The "SourceField" operand is a global tag of the data type INT. |

The value of the "SourceField" operand is written to the 2nd element of the ARRAY DB.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Example of the use of ARRAY data blocks](Programming%20basics.md#example-of-the-use-of-array-data-blocks)

##### ReadFromArrayDBL: Read from array data block in load memory (S7-1500)

###### Description

The instruction "Read from ARRAY data block in load memory" is used to read data from a data block of the ARRAY DB block type in the load memory and write it to a destination area.

An ARRAY data block is a data block that consists of exactly one ARRAY of [Data type]. The elements of the ARRAY can be of PLC data type or any other elementary data type. Counting of the ARRAY always begins with the low limit "0".

If the ARRAY data block has been designated with the block attribute "Only store in load memory", it will only be stored in the load memory.

The instruction is executed when a positive signal edge is detected at the REQ parameter. The BUSY parameter then has the signal state "1". The instruction is terminated if a negative signal edge is detected at the BUSY parameter. The DONE parameter has the signal state "1" for one program cycle and the read value is output at the VALUE parameter within this cycle. With all other program cycles, the value at the VALUE parameter is not changed.

###### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | REQ = "1": Begin with the reading of the ARRAY DB |
| DB <sup>1)</sup> | Input | DB_ANY | I, Q, M, D, L | ARRAY data block that is read. |
| INDEX | Input | DINT | I, Q, M, D, L, P or constant | Element in the DB that is read. The specification can be a constant, a global tag or an indexed value. |
| VALUE<sup> 1)</sup> | InOut | VARIANT | D (element of a global data block)  L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Pointer to the DB in the work memory that is to be read and the value of which is to be written.  No local constants or tags from the TEMP section must be used. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = "1": The array DB is still being read |
| DONE | Output | BOOL | I, Q, M, D, L | DONE = "1": The instruction was executed successfully |
| ERROR | Output | INT | I, Q, M, D, L, P | Error information:  If an error occurs during execution of the instruction, an error code is output at the ERROR parameter. |
| <sup>1)</sup> The data blocks must be created with the "Optimized" block property. |  |  |  |  |

###### Parameter ERROR

The following table shows the meaning of the values of the ERROR parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B4 | The element data type stored in the ARRAY data block does not match the element data type transferred in the VARIANT. |
| 8230 | The data block number is incorrect. |
| 8231 | The data block does not exist. |
| 8232 | The data block is too short, or is not located in load memory. |
| 8235 | The data block is not an ARRAY DB. |
| 8254 | The data block has the incorrect data type. |
| 8382 | The value at the INDEX parameter is outside the limits of the ARRAY. |
| 8750 | The data type VARIANT at parameter VALUE provides the value "0". |
| 8751 | Code generation error |
| 8752 | Code generation error |
| 8753 | The size of the VALUE parameter does not match the element length in the ARRAY data block. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

You can find descriptions of the error codes triggered by the instructions "READ_DBL" and "WRIT_DBL" in the corresponding descriptions of the instructions.

###### Example

The following example shows how the instruction works:

GRAPH

CALL ReadFromArrayDBL DB_ANY, "ReadFromArrayDBL_DB"

(REQ := "TagReg"

DB := "ArrayDB"

INDEX := 2

VALUE := "TargetField"

BUSY =&gt; "TagBusy"

DONE =&gt; "TagDone"

ERROR =&gt; "TagError"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| REQ | TagReq | BOOL |
| DB | ArrayDB | The "ArrayDB" operand is an ARRAY DB of the data type ARRAY [0 to 10] of INT. |
| INDEX | 2 | 2nd element of the "ArrayDB" |
| VALUE | TargetField | The "TargetField" operand is a global tag of the data type INT. |
| BUSY | TagBusy | BOOL |
| DONE | TagDone | BOOL |

The instruction is executed when a positive signal edge is detected at the "TagReq" operand. The 2nd element is read from "ArrayDB" and output at the "VALUE" parameter. As soon as a negative signal edge is detected at the "TagBusy" operand, the instruction is terminated and the value at the VALUE parameter is no longer changed. After the instruction has been processed, the "TagDone" operand has the signal state TRUE.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Example of the use of ARRAY data blocks](Programming%20basics.md#example-of-the-use-of-array-data-blocks)

##### WriteToArrayDBL: Write to array data block in load memory (S7-1500)

###### Description

The instruction "Write to ARRAY data block in load memory" is used to write data to a data block of the ARRAY DB block type in the load memory.

An ARRAY data block is a data block that consists of exactly one ARRAY of [Data type]. The elements of the ARRAY can be of PLC data type or any other elementary data type. Counting of the ARRAY always begins with the low limit "0".

If the ARRAY data block has been designated with the block attribute "Only store in load memory", it will only be stored in the load memory.

The instruction is executed when a positive signal edge is detected at the REQ parameter. The BUSY parameter then has the signal state "1". If a negative signal edge is detected at the BUSY parameter, the instruction is terminated and the value at the VALUE parameter is written to the data block. The DONE parameter then has the signal state "1" for one program cycle.

###### Parameter

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | REQ = "1": Start writing to the array DB |
| DB <sup>1)</sup> | Input | DB_ANY | I, Q, M, D, L | ARRAY data block to which data is written |
| INDEX | Input | DINT | I, Q, M, D, L, P or constant | Element in the DB to which data is written. The specification can be a constant, a global tag or an indexed value. |
| VALUE<sup> 1)</sup> | Input | VARIANT | D (element of a global data block)  L (The declaration is possible in the "Input", "InOut" and "Temp" sections of the block interface.) | Pointer to the DB in the work memory that is to be read and the value of which is to be written.  No local constants or tags from the TEMP section must be used. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY = "1": The array DB is still being written |
| DONE | Output | BOOL | I, Q, M, D, L | DONE = "1": The instruction was executed successfully |
| ERROR | Output | INT | I, Q, M, D, L, P | Error information:  If an error occurs during execution of the instruction, an error code is output at the ERROR parameter. |
| <sup>1)</sup> The data blocks must be created with the "Optimized" block property. |  |  |  |  |

###### Parameter ERROR

The following table shows the meaning of the values of the ERROR parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B4 | The element data type stored in the ARRAY data block does not match the element data type transferred in the VARIANT. |
| 8230 | The data block number is incorrect. |
| 8231 | The data block does not exist. |
| 8232 | The data block is too short, or is not located in load memory. |
| 8234 | The data block is write protected. |
| 8235 | The data block is not an ARRAY DB. |
| 8254 | The data block has the incorrect data type. |
| 8382 | The value at the INDEX parameter is outside the limits of the ARRAY. |
| 8450 | The data type VARIANT at parameter VALUE provides the value "0". |
| 8751 | Code generation error |
| 8752 | Code generation error |
| 8753 | The size of the VALUE parameter does not match the element length in the ARRAY data block. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

You can find descriptions of the error codes triggered by the instructions "READ_DBL" and "WRIT_DBL" in the corresponding descriptions of the instructions.

###### Example

The following example shows how the instruction works:

GRAPH

CALL WriteToArrayDBL DB_ANY, "WriteToArrayDBL_DB"

(REQ := "TagReg"

DB := "ArrayDB"

INDEX := 2

VALUE := "SourceField"

BUSY =&gt; "TagBusy"

DONE =&gt; "TagDone"

ERROR =&gt; "TagError"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| REQ | TagReq | BOOL |
| DB | ArrayDB | The "ArrayDB" operand is an ARRAY DB of the data type ARRAY [0 to 10] of INT. |
| INDEX | 2 | 2nd element of the "ArrayDB" |
| VALUE | SourceField | The "SourceField" operand is a global tag of the data type INT. |
| BUSY | TagBusy | BOOL |
| DONE | TagDone | BOOL |

The instruction is executed when a positive signal edge is detected at the "TagReq" operand. As soon as a negative signal edge is detected at the "TagBusy" operand, the instruction is terminated and the value at the VALUE parameter is written to the 2nd element of "ArrayDB". After the instruction has been processed, the "TagDone" operand has the signal state TRUE.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Example of the use of ARRAY data blocks](Programming%20basics.md#example-of-the-use-of-array-data-blocks)

#### Symbolic move (S7-1500)

This section contains information on the following topics:

- [Symbolic access during runtime (S7-1500)](#symbolic-access-during-runtime-s7-1500)
- [ResolveSymbols: Resolve several symbols (S7-1500)](#resolvesymbols-resolve-several-symbols-s7-1500)
- [System data type ResolvedSymbol (S7-1500)](#system-data-type-resolvedsymbol-s7-1500)
- [MoveResolvedSymbolsToBuffer: Read values from resolved symbols and write them into buffer (S7-1500)](#moveresolvedsymbolstobuffer-read-values-from-resolved-symbols-and-write-them-into-buffer-s7-1500)
- [MoveResolvedSymbolsFromBuffer: Read values from buffer and write them into resolved symbols (S7-1500)](#moveresolvedsymbolsfrombuffer-read-values-from-buffer-and-write-them-into-resolved-symbols-s7-1500)

##### Symbolic access during runtime (S7-1500)

###### Application

The "Symbolic access during runtime" function gives external applications access to the tags in the PLC program during runtime. External applications can be, for example, HMI applications, OPC UA functions or other communication functions. The tags can be read or written.

Read or write access is not programmed statically when the program is being created. In fact, access takes place dynamically during runtime. Users enter the symbolic tag names they wish to access manually or program-controlled during runtime.

The "Symbolic access during runtime" function can process optimized as well as non-optimized data. This means it is more flexible and efficient than an ANY pointer that can only access non-optimized data.

The function enables, for example, the tracing of tags through external devices or applications.

###### Constraints

The following constraints apply to the symbolic access during runtime:

- The symbolic access is only available for S7-1500 as of firmware version V3.0.
- The tags must have the attribute "Accessible from HMI/OPC UA/Web API" or "Writable from HMI/OPC UA/Web API".

The following table shows the data you can access:

| Access to | V1.0 | V1.1 |
| --- | --- | --- |
| PLC tags (I, Q, M) | ✓ | ✓ |
| Data blocks | - | - |
| Elements of data blocks | ✓ | ✓ |
| Technology objects | - | - |
| Elements of technology objects | - | - |
| Data blocks   based on a PLC data type/system data type | - | ✓ |
| Elementary data types | ✓ | ✓ |
| ARRAY and STRUCT | ✓ Access to individual elements | ✓ Access to individual elements  ✓ Access to the entire structure |
| STRING and WSTRING | - | ✓ |
| DTL | - | ✓ |
| PLC data types and system data types | - | ✓ |
| Hardware data types | ✓ | ✓ |
| IEC timers and counters | - | ✓ |
| I/O (Tag name: P) | - | - |
| Timers (T) and counters (T or C) | - | - |
| Elements in the load memory | - | - |
| Write-protected elements | - | - |
| References | - | - |
| Pointer, Any, Remote, Block_FB, Block_FC, Multi-FB | - | - |
| Data in fail-safe programs | - When accessing fail-safe program parts, the CPU switches to STOP. | - When accessing fail-safe program parts, the CPU switches to STOP. |

###### Principle of operation

Two steps are necessary to access tags during runtime:

1. The symbolic tag names that are entered via HMI, for example, must be "resolved". This means that references to the respective tags are created in the PLC program. References are typed pointers by which you can address the tags in the PLC program. To resolve the symbolic tags, use the asynchronous instruction "ResolveSymbols".
2. Special Move instructions are available to read or write the tag values. The Move instructions are synchronous instructions. They address the tags using the previously generated references.

![Principle of operation](images/155444321163_DV_resource.Stream@PNG-en-US.png)

###### Example of step 1

The following example shows how the symbolic tag names are resolved with the instruction "ResolveSymbols":

- At the parameter "nameList", specify an Array of WSTRING that contains the tag names you wish to resolve.
- At the parameter "referenceList", specify an Array of ResolvedSymbol (SDT) in which the references to the tags are saved.
- The two Arrays must have the same limits.

As a result, you receive a reference for each symbolic tag name at the parameter "referenceList". The reference is contained in a structure of the system data type "ResolvedSymbol".

See also:

[ResolveSymbols: Resolve several symbols](#resolvesymbols-resolve-several-symbols-s7-1500)

[System data type ResolvedSymbol](#system-data-type-resolvedsymbol-s7-1500)

![Example of step 1](images/151349402251_DV_resource.Stream@PNG-de-DE.png)

###### Example of step 2

The following example shows you how to read the tag values with the instruction "MoveResolvedSymbolsToBuffer" and write them to a buffer:

- At the parameter "src", specify the Array of ResolvedSymbol (SDT) that contains the references to the resolved tags.
- At the parameter "dst", specify an Array of BYTE . It serves as a target buffer to which the tag values are written.

When you execute the instruction "MoveResolvedSymbolsToBuffer", the tag values are read using the references and written to the target buffer.

See also:

[MoveResolvedSymbolsToBuffer: Read values from resolved symbols and write them into buffer](#moveresolvedsymbolstobuffer-read-values-from-resolved-symbols-and-write-them-into-buffer-s7-1500)

![Example of step 2](images/166852971403_DV_resource.Stream@PNG-de-DE.png)

##### ResolveSymbols: Resolve several symbols (S7-1500)

###### Description

With the "Resolve several symbols" instruction, you resolve multiple symbolic tag names. As a result, you receive references to the tags. References are typed pointers that give you read or write access to the tags.

At the parameter "nameList", specify an Array of WSTRING . Here, the tag names that are to be resolved are transferred during runtime. The array can be in an optimized or non-optimized memory area.

At the parameter "referenceList", specify an Array of ResolvedSymbol (SDT) in which the references are to be saved. The array must be in an optimized memory area. The two Arrays must have the same limits.

The symbolic tag names are transferred in the format WSTRING and must not exceed a length of 254 UTF-16 characters. Enter the fully qualified name including the namespace. The qualifier # for local tags is not supported. Elements in arrays are supported but they must specify a fixed index for access to an element. Accesses with variable index, e.g., `myArray[myIndexTag]`, are not supported.

Example of a fully-qualified name:

`myNamespace.mySubnamespace.myDataBlock.myArray[7,12,1]`

Using the "firstIndex" and "lastIndex" parameters, you can also only resolve some of the symbols from the list. If you wish to resolve the entire list of symbols, the "firstIndex" parameter can specify the low limit and the "lastIndex" parameter can specify the high limit.

The instruction is executed asynchronously. The execution starts with a rising signal edge at the "execute" parameter. You cannot make any changes at the "nameList" and "referenceList" parameters while the instruction is running (Busy = 1).

Before the symbols are resolved, the values are reset in the Array at the "referenceList" parameter within the specified Array limits ("firstIndex" and "lastIndex").

After the instruction is complete, the "done" parameter has the value = 1 for one cycle. The array at the "referenceList" parameter is filled with the references to the tags.

After a falling signal edge at the "execute" parameter, the instance of "ResolveSymbol" is no longer considered active.

> **Note**
>
> **Configuration limits**
>
> A maximum of 10 "ResolveSymbols" instructions can be active at the same time. In total, all active instances of the instruction can resolve a maximum of 2,000 symbols.

###### Parameters

The following table shows the parameters of the "Resolve several symbols" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| execute | Input | BOOL | I, Q, M, D, L | With a rising signal edge, execution of the instruction is started. |
| firstIndex | Input | DINT | I, Q, M, D, L, C | Index of the first tag name to be resolved. |
| lastIndex | Input | DINT | I, Q, M, D, L, C | Index of the last tag name to be resolved. |
| done | Output | BOOL | I, Q, M, D, L | Done = 1  Execution of the instruction is complete. |
| busy | Output | BOOL | I, Q, M, D, L | Busy = 1  The instruction is currently being executed. |
| error | Output | BOOL | I, Q, M, D, L | ERROR = 1  Error occurred during processing. The error message is output at the STATUS parameter. |
| status | Output | INT | I, Q, M, D, L | Block status / error number (see "STATUS parameter") |
| nameList | InOut | Array of WSTRING | D | List of tag names to be resolved. |
| referenceList | InOut | Array of ResolvedSymbol | D | List of references |

You can find additional information on SDT here: [System data type ResolvedSymbol](#system-data-type-resolvedsymbol-s7-1500)

###### STATUS parameter

The following table shows the meaning of the values of the "STATUS" parameter:

| Error code (W#16#...) | Description |
| --- | --- |
| 0000 | No error occurred. |
| 7000 | No job processing active. |
| 7001 | Start of asynchronous job processing. Parameter BUSY = 1, DONE = 0 |
| 7002 | Intermediate call: Instruction already active; BUSY = 1. |
| 80B3 | The value at the "firstIndex" parameter is greater than the value at the "lastIndex" parameter. |
| 80B4 | The ARRAY limits of "referenceList" and "nameList" have different limits. |
| 80C3 | The maximum possible number of simultaneously active "ResolveSymbols" instructions has already been reached, or the maximum possible number of 2000 simultaneously resolvable symbols has been reached. |
| 8282 | The value at the "firstIndex" parameter is outside the limits of the ARRAY. |
| 8382 | The value at the "lastIndex" parameter is outside the limits of the ARRAY. |
| 8820 | A name in the list of tags that you specified at the "nameList" parameter is invalid. |
| 8831 | The ARRAY of WSTRING that you specified as the actual parameter for "nameList" does not exist. |
| 8833 | The ARRAY of WSTRING that you specified as the actual parameter for "nameList" is only in the load memory and cannot be addressed by the instruction. |
| 8854 | The actual parameter for "nameList" is not of the data type "ARRAY of WSTRING". |
| 8931 | The ARRAY of ResolvedSymbol that you specified as the actual parameter for "referenceList" does not exist. |
| 8933 | The ARRAY of ResolvedSymbol that you specified as the actual parameter for "referenceList" is only in the load memory and cannot be addressed by the instruction. |
| 8934 | The ARRAY of ResolvedSymbol that you specified as the actual parameter for "referenceList" is write-protected. |
| 8936 | The ARRAY of ResolvedSymbol that you specified as the actual parameter for "referenceList" is not in an optimized global data block. |
| 8954 | The actual parameter for "referenceList" is not of the data type "ARRAY of WSTRING". |

###### Example

The following example shows how the instruction works:

GRAPH

CALL ResolveSymbols, "ResolveSymbols_DB"

(execute := #Input_Execute,

firstIndex := 0,

lastIndex := 9,

done =&gt; #Output_Done,

busy =&gt; #Output_Busy,

error =&gt; #Output_Error,

status =&gt; #Output_Status,

nameList := "mySrcDB".InOut_Symbols,

referenceList := "myTargetDB".InOut_ResolvedSymbols

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value/Data type |
| --- | --- | --- |
| nameList | InOut_Symbols | Array[0..99] of WSTRING |
| referenceList | InOut_ResolvedSymbols | Array[0..99] of ResolvedSymbol |
| firstIndex | - | 0 |
| lastIndex | - | 9 |
| execute | Input_Execute | BOOL |
| busy | Output_Busy | BOOL |
| done | Output_Done | BOOL |

If the operand #Input_Execute changes to signal state "1", execution of the instruction has begun. The tag names at the parameter "nameList" are resolved and the references to the tags are written in the operand "#InOut_ResolvedSymbols" at the parameter "referenceList". After the instruction is complete, the "done" parameter has the value = 1 for one cycle.

---

**See also**

[Symbolic access during runtime (S7-1500)](#symbolic-access-during-runtime-s7-1500)

##### System data type ResolvedSymbol (S7-1500)

###### Description

The system data type "ResolvedSymbol" is required to execute the "Symbolic access during runtime" function. It saves references to tags in the PLC program as well as status information for generating the references. The system type must be located in an optimized memory area.

As of FW version 3.0, the system data type "ResolvedSymbol" can be declared as an element of a PLC data type.

###### Structure of the system data type

The system data type "ResolvedSymbol" has the following visible elements:

| Parameter name | Data type | Description |
| --- | --- | --- |
| resolved | BOOL | Provide information on whether the symbol was successfully resolved:  - resolved = FALSE + status = 0  =&gt; No attempt has been made yet to resolve the symbol. - resolved = FALSE + status &lt;&gt; 0  =&gt; The resolution of the symbol failed The value of the status parameter indicates the structure level within the tag that could not be resolved. A negative value means that the symbol could not be resolved, e.g. due to range violations.  A positive value means that the tag is not accessible or not writable by HMI/OPC UA or Web API. - resolved = TRUE + status = 0  =&gt; Symbol was successfully resolved. - resolved = TRUE + status &lt;&gt; 0  =&gt; Symbol was successfully resolved but the DB was overwritten by a subsequent loading in "RUN". |
| status | INT |  |

The element "resolved" indicates whether a symbol was successfully resolved. If the symbol was successfully resolved, the parameter "status" has the value "0" and the "ResolvedSymbol" structure contains reliable information.

In addition to these two parameters, the system data type contains internal parameters that save the information on data type, length and address of the tags. However, you cannot access these parameters.

If the resolution of the symbol was faulty, the "status" parameter returns the following values:

| Error code (W#16#...) | Explanation |
| --- | --- |
| 8021 | The WSTRING for the symbolic tag name is empty. |
| 8022 | The WSTRING for the symbolic tag name contains invalid characters. |
| 8023 | The data type declaration of the referenced tag is missing. |
| 8024 | The reference points to a tag that no longer exists. It may have been overwritten by a loading in "RUN". |
| 8054 | The data type of the referenced tag is not supported. |
| 80B4 | The project is inconsistent. |

###### Invalid references in the system data type "ResolvedSymbol"

The references in the SDT "ResolvedSymbol" can become invalid if the referenced tags are overwritten by a loading in "RUN". The references may point to tags that no longer exist. An error code at the "status" parameter indicates invalid references.

The following example shows how you can use an IF instruction in SCL to interrupt the execution of a Move instruction in case of an error and resolve the symbol once again:

![Invalid references in the system data type "ResolvedSymbol"](images/155063369995_DV_resource.Stream@PNG-de-DE.png)

Before calling the „MoveResolvedSymbolsToBuffer“ instruction, a check is performed to determine whether the symbol was resolved successfully and „MoveResolvedSymbolsToBuffer“ can be executed.

Even if a symbol was resolved successfully, errors can occur when executing „MoveResolvedSymbolToBuffer“, for example, when a tag is overwritten by a loading in RUN. In this case, the return value „err“ provides the number of failed copy processes.

If a failed copy process is recognized, the subsequent IF instruction sets "EnableMove" to FALSE so that "MoveResolvedSymbolsToBuffer" is no longer executed.

Afterwards, a check is performed with a FOR instruction to determine which symbols supply an error code. For these symbols, the error code is copied to the "status" parameter.

At the same time, the „resolved“ parameter is set to FALSE. Now you have to resolve the symbol with the asynchronously operating „ResolveSymbols“ instruction again.

---

**See also**

[Symbolic access during runtime (S7-1500)](#symbolic-access-during-runtime-s7-1500)

##### MoveResolvedSymbolsToBuffer: Read values from resolved symbols and write them into buffer (S7-1500)

###### Description

With the "Read values from resolved symbols and write them into buffer" instruction, you read values from several resolved symbols and write them into a memory area (Array of BYTE). In this way, you can prepare values of resolved symbols for further use, such as sending using communication instructions, e.g. TSEND.

The "src" parameter is an Array of ResolvedSymbol (SDT). It contains references to tags that were previously resolved with the instruction "ResolveSymbols". At the parameter "dst", specify an Array of BYTE. It serves as a target buffer to which the tag values are written. The two arrays must have the same limits.

Use the parameters "firstIndex" and "lastIndex" to restrict the list of values that are to be copied during this call of the instruction. During a later call, you can copy the values of other resolved symbols. If you do not wish to restrict the list, the value at the "firstIndex" parameter must correspond to the low limit of the list and the value at the "lastIndex" parameter must correspond to the high limit of the list.

The value at the "mode" parameter defines the memory format at the "dst" parameter.

With offsets, you determine where the values of the resolved symbols are stored in the destination buffer. You specify the offsets at the "dstOffsets" (Array of DINT) parameter. Each offset is a bit offset and determines the first bit from which the value is written to the buffer. You can store several values of the BOOL data type in one byte. Values of all other data types must start at a bit position divisible by 8.

If the "src[i]" parameter references a tag of the REAL data type, the value at the "dstOffsets[i]" parameter is 88 and 2#1 at the "mode" parameter, for example, then the "Read values from resolved symbols and write them into buffer" instruction copies the value into the bytes 11 to 14, starting with the least significant byte.

If the "src[i]" parameter references a tag of the BOOL data type and the value at the "dstOffsets[i]" parameter is 29, for example, then the "Read values from resolved symbols and write them into buffer" instruction copies the value into byte 3, offset 5 of the destination memory.

The arrays at "dstOffsets" and "src" must have the same limits to ensure that "dstOffsets[i]" contains the offset for "src[i]".

This way, you can define the structure of the target buffer very specifically. However, note that the instruction does not verify whether the specified offsets overlap. An error is not signaled in this case and the content of the target buffer is indeterminate.

The content of the target buffer also depends on whether the values are read from an optimized or non-optimized memory area. Both memory areas have different rules for fill bytes. For more information on fill bytes, refer to "See also".

The "status" parameter is an Array of INT. It must have the same limits as the "src" and "dstOffsets" parameters to ensure that "status[i]" contains the status for "src[i]".

For WSTRING and STRING, the current length of the source string is copied. If the source string is shorter than the destination string, the remaining characters of the destination string remain unchanged.

> **Note**
>
> **Invalid references in the SDT "ResolvedSymbol"**
>
> The references in the SDT "ResolvedSymbol" can become invalid when the referenced tags are overwritten by loading in "RUN". The references may point to tags that no longer exist. An error code at the "status" parameter indicates invalid references.
>
> In this case, resolve the symbols again with the instruction "ResolveSymbols".

###### Parameters

The following table shows the parameters of the "Read values from resolved symbols and write them into buffer" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| firstIndex | Input | DINT | I, Q, M, D, L, C | Index of the first resolved symbol to be copied. |
| lastIndex | Input | DINT | I, Q, M, D, L, C | Index of the last resolved symbol to be copied. |
| src | Input | Array of ResolvedSymbol | D, L | List of resolved symbols |
| dstOffsets | Input | Array of DINT | I, Q, M, D, L | Contains a bit offset for each element in the destination buffer |
| mode | Input | DWORD | I, Q, M, D, L, C | Memory format:  - 2#0 = Big-Endian - 2#1 = Little-Endian |
| dst | InOut | Array of BYTE | D, L | Target buffer to which the values of the resolved symbols are copied |
| status | InOut | Array of INT | D, L | Contains a copy status for each resolved symbol |
| Function value (RET_VAL) |  | INT | I, Q, M, D, L | Error information |

You can find additional information on SDT here: [System data type ResolvedSymbol](#system-data-type-resolvedsymbol-s7-1500)

###### Status parameter

The following table shows the meaning of the values of the Status[i] parameter:

| Error code*(W#16#...) | Explanation |
| --- | --- |
| 8020 | The symbol was not resolved. |
| 8024 | The reference points to a tag that no longer exists. It may have been overwritten by a loading in "RUN". |
| 8031 | src[i]: The data block does not exist. |
| 8033 | src[i]: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8054 | src[i]: The data type of the referenced tag is not supported. |
| 8082 | dstOffsets[i]: The offset is located outside the ARRAY limits of the dst parameter. |
| 8085 | dstOffsets[i]: The offset does not start at a bit position divisible by 8. |

###### RET_VAL parameter

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*(W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B3 | The value at the "firstIndex" parameter is greater than the value at the "lastIndex" parameter. |
| 80B4 | The parameters "src", "dstOffset" and "status" have different ARRAY limits. |
| 8182 | The value at the "firstIndex" parameter is outside the limits of the ARRAY. |
| 8282 | The value at the "lastIndex" parameter is outside the limits of the ARRAY. |
| 8331 | src: The data block does not exist. |
| 8333 | src: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8354 | scr: Invalid data type. |
| 8431 | dstOffsets: The data block does not exist. |
| 8433 | dstOffsets: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8436 | dstOffsets: The ARRAY is not in an optimized memory area. |
| 8454 | dstOffsets: Invalid data type. |
| 8631 | dst: The data block does not exist. |
| 8633 | dst: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8634 | dst: The data block is write-protected. |
| 8636 | dst: The data block is not in an optimized memory area. |
| 8653 | dst: The memory area addressed by VARIANT is too small. |
| 8654 | dst: Invalid data type. |
| 8731 | status: The data block does not exist. |
| 8733 | status: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8734 | status: The data block is write-protected. |
| 8754 | status: Invalid data type. |

###### Example

The following example shows how the instruction works:

GRAPH

CALL MoveResolvedSymbolsToBuffer

(firstIndex := 2,

lastIndex := 7,

src := mySrcDB.Input_ResolvedSymbols,

dstOffsets := #Input_Offset,

mode := 2#0,

Ret_Val =&gt; #RETVAL,

dst := myTargetDB.InOut_Buffer,

status := #InOut_Status

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value/Data type |
| --- | --- | --- |
| firstIndex | - | 2 |
| lastIndex | - | 7 |
| src | Input_ResolvedSymbols | Array[0..99] of ResolvedSymbol |
| dstOffsets | Input_Offset | Array[0..99] of Dint |
| mode | - | 2#0 |
| dst | InOut_Buffer | Array[0..99] of Byte |
| status | InOut_Status | Array[0..99] of Int |

The values of the resolved symbols in the array "Input_ResolvedSymbols" are written in Big-Endian format to the target buffer "#InOut_Buffer" at the "dst" parameter.

Using the two constants at the "firstIndex" and "lastIndex" parameters, you restrict the number of tags whose values are to be copied.

The operand "Input_Offset" contains an offset for each value to be written. Based on the offset, it is determined where the value of the resolved symbol is written in the target buffer.

---

**See also**

[Symbolic access during runtime (S7-1500)](#symbolic-access-during-runtime-s7-1500)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

##### MoveResolvedSymbolsFromBuffer: Read values from buffer and write them into resolved symbols (S7-1500)

###### Description

With the "Read values from buffer and write them into resolved symbols" instruction, you read values from a memory area (Array of BYTE) and write them into the values of several resolved symbols. In this way, you can process a memory area that you have received from a communication instruction, such as TRCV.

The "src" parameter is an Array of BYTE. It serves as the source buffer from which the values are read. The "dst" parameter is an Array of ResolvedSymbol (SDT). It contains references to tags that were previously resolved with the instruction "ResolveSymbols". By using the references, the tags are to be written with the values from the source buffer.

By using the parameters "firstIndex" and "lastIndex", you restrict the selection of tags in the list of resolved symbols whose values are to be written. If you do not wish to restrict the list, the value at the "firstIndex" parameter must correspond to the low limit of the list and the value at the "lastIndex" parameter must correspond to the high limit of the list.

The value at the "mode" parameter defines the memory format at the "src" parameter.

With offsets, you determine from where the value of the resolved symbol is read and copied in the source buffer. You specify the offsets at the "srcOffsets" (Array of DINT) parameter. Each offset is a bit offset and determines the first bit from which the value is read from the buffer. You can store several values of the BOOL data type in one byte. Values of all other data types must start at a bit position divisible by 8.

If, for example, the "dst[i]" parameter references a tag of the REAL data type, the value at the "srcOffsets[i]" parameter is 88 and at the "mode" parameter 2#1, the instruction reads the values from bytes 11 to 14, starting with the least significant byte.

If, for example, the "src[i]" parameter references a tag of the BOOL data type, the value at the "srcOffsets[i]" parameter is 29, the instruction reads the value at byte 3, offset 5 of the source buffer.

The arrays at "srcOffsets" and "dst" must have the same limits to ensure that "srcOffsets[i]" contains the offset for "dst[i]".

This allows you to specify exactly which values are copied from the target buffer. However, note that the instruction does not verify whether the specified offsets overlap. An error is not signaled in this case and the read value can be random.

The "status" parameter is an Array of INT. It must have the same limits as the "dst" and "srcOffsets" parameters to ensure that "status[i]" contains the status for "dst[i]".

For WSTRING and STRING, the current length of the source string is copied. If the source string is longer than the destination string, the remaining characters of the source string are not copied.

> **Note**
>
> **Invalid references in the SDT "ResolvedSymbol"**
>
> The references in the SDT "ResolvedSymbol" can become invalid when the referenced tags are overwritten by loading in "RUN". The references may point to tags that no longer exist. An error code at the "status" parameter indicates invalid references.
>
> In this case, resolve the symbols again with the instruction "ResolveSymbols".

###### Parameters

The following table shows the parameters of the "Read values from buffer and write them into resolved symbols" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| firstIndex | Input | DINT | I, Q, M, D, L, C | Index of the first resolved symbol in the target buffer that is to be written. |
| lastIndex | Input | DINT | I, Q, M, D, L, C | Index of the last resolved symbol in the target buffer that is to be written. |
| mode | Input | DWORD | I, Q, M, D, L, C | Memory format  - 2#0 = Big-Endian - 2#1 = Little-Endian |
| src | Input | Array of BYTE | D, L | Source buffer from which the values are read |
| srcOffsets | Input | Array of DINT | D, L | Offsets of the values in the source buffer |
| dst | InOut | Array of ResolvedSymbol | D, L | Target buffer that contains the references to the resolved symbols |
| status | InOut | Array of INT | D, L | Contains a copy status for each value to be written |
| Function value (RET_VAL) |  | INT | I, Q, M, D, L | Error information |

You can find additional information on SDT here: [System data type ResolvedSymbol](#system-data-type-resolvedsymbol-s7-1500)

###### Status parameter

The following table shows the meaning of the values of the Status[i] parameter:

| Error code*(W#16#...) | Explanation |
| --- | --- |
| 8020 | The symbol was not resolved. |
| 8021 | The WSTRING for the symbolic tag name is empty. |
| 8022 | The WSTRING for the symbolic tag name contains invalid characters. |
| 8023 | The data type declaration of the referenced tag is missing. |
| 8024 | The reference points to a tag that no longer exists. It may have been overwritten by a loading in "RUN". |
| 8054 | The reference points to a tag with invalid data type. |
| 80B4 | The project is inconsistent. |
| 8031 | dst[i]: The data block does not exist. |
| 8033 | dst[i]: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8034 | dst[i]: The data block is write-protected. |
| 8054 | dst[i]: The data type of the referenced tag is not supported. |
| 8082 | srcOffset[i]: The offset is located outside the ARRAY limits of the src parameter. |
| 8085 | srcOffset[i]: The offset does not start at a bit position divisible by 8. |

###### RET_VAL parameter

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*(W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B3 | The value at the firstIndex parameter is greater than the value at the lastIndex parameter. |
| 80B4 | The parameters dst, srcOffsets and status have different ARRAY limits. |
| 8182 | The value at the firstIndex parameter is outside the limits of the ARRAY. |
| 8282 | The value at the lastIndex parameter is outside the limits of the ARRAY. |
| 8431 | src: The data block does not exist. |
| 8433 | src: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8454 | src: Invalid data type. |
| 8531 | srcOffsets: The data block does not exist. |
| 8533 | srcOffsets: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8554 | srcOffsets: Invalid data type. |
| 8631 | dst: The data block does not exist. |
| 8633 | dst: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8634 | dst: The data block is write-protected. |
| 8636 | dst: The data block is not in an optimized memory area. |
| 8654 | dst: Invalid data type. |
| 8731 | status: The data block does not exist. |
| 8733 | status: The data block is only available in the load memory and cannot be addressed by the instruction. |
| 8734 | status: The data block is write-protected. |
| 8736 | status: The data block is not in an optimized memory area. |
| 8754 | status: Invalid data type. |

###### Example

The following example shows how the instruction works:

GRAPH

CALL MoveResolvedSymbolsFromBuffer

(firstIndex := 2,

lastIndex := 7,

mode := 2#0,

src := mySrcDB.Input_Buffer,

srcOffsets := #Input_Offset,

Ret_Val =&gt; #RETVAL,

dst := myTargetDB.InOut_ResolvedSymbols,

status := #InOut_Status

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value/Data type |
| --- | --- | --- |
| firstIndex | - | 2 |
| lastIndex | - | 7 |
| mode | - | 2#0 |
| src | Input_Buffer | Array[0..99] of Byte |
| srcOffsets | Input_Offset | Array[0..99] of Dint |
| dst | InOut_ResolvedSymbols | Array[0..99] of ResolvedSymbol |
| status | InOut_Status | Array[0..99] of Int |

The values of the tags from the source buffer "Input_Buffer" are read in Big-Endian format and written to the resolved symbols via the references in "#InOut_ResolvedSymbols".

If the operand "TagIn" has the signal state "1", the instruction is executed. The values of the tags from the source buffer "Input_Buffer" are read in Big-Endian format and written to the resolved symbols via the references in "#InOut_ResolvedSymbols".

---

**See also**

[Symbolic access during runtime (S7-1500)](#symbolic-access-during-runtime-s7-1500)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

#### Legacy (S7-1500)

This section contains information on the following topics:

- [BLKMOV: Move block (S7-1500)](#blkmov-move-block-s7-1500)
- [UBLKMOV: Move block uninterruptible (S7-1500)](#ublkmov-move-block-uninterruptible-s7-1500)
- [FILL: Fill block (S7-1500)](#fill-fill-block-s7-1500)

##### BLKMOV: Move block (S7-1500)

###### Description

You use the "Move block" instruction to move the content of a memory area (source area) to another memory area (destination area). The move operation takes place in the direction of ascending addresses. You use VARIANT to define the source and destination areas.

> **Note**
>
> The tags of the instruction can only be used within memory areas in which the "Optimized block access" attribute is not activated. This applies to data blocks (DBs), organization blocks (OBs), functions (FCs), bit memory (M), inputs (I), and outputs (Q).
>
> If a tag of the instruction has been declared with the retentivity setting "Set in IDB", however, you can also use this tag in memory areas "with optimized block access".

The following figure shows the principle of the move operation:

![Description](images/43499200011_DV_resource.Stream@PNG-en-US.png)

###### Consistency of source and destination data

Make sure that the source data remains unchanged during execution of the "Move block" instruction. Otherwise, consistency of the destination data cannot be guaranteed.

###### Interruptibility

There is no limit to the nesting depth.

###### Memory areas

You use the "Move block" instruction to move the following memory areas:

- Areas of a data block
- Bit memory
- Process image input
- Process image output

###### General rules for moving

The source and destination areas must not overlap. If the source and destination areas have different lengths, only the length of the smaller area will be moved.

If the source area is smaller than the destination area, the entire source area will be written to the destination area. The remaining bytes of the destination area remain unchanged.

If the destination area is smaller than the source area, the entire destination area will be written. The remaining bytes of the source area are ignored.

If a block of data type BOOL is moved, the tag must be addressed absolutely and the specified length of the area must be divisible by 8, otherwise the instruction cannot be executed.

###### Rules for moving character strings

You can use the "Move block" instruction to also move source and destination areas of the STRING data type. If only the source area is of data type STRING, the characters that are actually contained in the character string will be moved. Information on the actual and maximum length are not written in the destination area. If the source and destination area are both STRING data type, the current length of the character string in the destination area is set to the number of characters actually moved.

If you want to move the information on the maximum and actual length of a character string, specify the areas in bytes in the SRCBLK and DSTBLK parameters. Alternatively, you can use the "Serialize" / "Deserialize" instructions.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRCBLK | Input | VARIANT | I, Q, M, D, L, P | Specifies the memory area to be moved (source area). |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Error information:  If an error occurs during execution of the instruction, an error code is output at the RET_VAL parameter. |
| DSTBLK | Output | VARIANT <sup>1)</sup> | I, Q, M, D, L, P | Specifies the memory area to which the block is moved (destination area). |
| 1) The DSTBLK parameter is declared as Output, since the data flow into the tag. However, the tag itself must be declared as InOut in the block interface. |  |  |  |  |

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8092 | The source or destination area is only available in the load memory. |
| 8152 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the SRCBLK parameter. |
| 8352 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the DSTBLK parameter. |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL BLKMOV VARIANT

(SRCBLK := P#M100.0 BYTE 10

RET_VAL =&gt; "Tag_ErrorCode"

DSTBLK =&gt; P#DB1.DBX0.0 BYTE 10

)

The instruction copies 10 bytes starting from MB100 and writes them to DB1. If an error occurs during the move operation, its error code is output in the "Tag_ErrorCode" tag.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### UBLKMOV: Move block uninterruptible (S7-1500)

###### Description

You use the "Move block uninterruptible" instruction to move the content of a memory area (source area) to another memory area (destination area). The move operation takes place in the direction of ascending addresses. You use VARIANT to define the source and destination areas.

The move operation cannot be interrupted by other operating system activities. As a result, the interrupt reaction time of the CPU can increase during execution of the "Move block uninterruptible" instruction.

> **Note**
>
> The tags of the instruction can only be used within memory areas in which the "Optimized block access" attribute is not activated. This applies to data blocks (DBs), organization blocks (OBs), functions (FCs), bit memory (M), inputs (I), and outputs (Q).
>
> If a tag of the instruction has been declared with the retentivity setting "Set in IDB", however, you can also use this tag in memory areas "with optimized block access".

###### Memory areas

You use the "Move block uninterruptible" instruction to move the following memory areas:

- Areas of a data block
- Bit memory
- Process image input
- Process image output

###### General rules for moving

The source and destination area must not overlap during the execution of the "Move block uninterruptible" instruction. If the source area is smaller than the destination area, the entire source area will be written to the destination area. The remaining bytes of the destination area remain unchanged.

If the destination area is smaller than the source area, the entire destination area will be written. The remaining bytes of the source area are ignored.

If a source or destination area defined as a formal parameter is smaller than a destination or source area specified in the SRCBLK or DSTBLK parameter, no data is transferred.

If a block of data type BOOL is moved, the tag must be addressed absolutely and the specified length of the area must be divisible by 8, otherwise the instruction cannot be executed.

You use the "Move block uninterruptible" instruction to move a maximum of 16 KB. Note the CPU-specific restrictions for this.

###### Rules for moving character strings

You can use the "Move block uninterruptible" instruction to also move source and destination areas of data type STRING. If only the source area is of data type STRING, the characters that are actually contained in the character string will be moved. Information on the actual and maximum length are not written in the destination area. If the source and destination area are both STRING data type, the current length of the character string in the destination area is set to the number of characters actually moved. If areas of the STRING data type are moved, specify "1" as the area length.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| SRCBLK | Input | VARIANT | I, Q, M, D, L, P | Specifies the memory area to be moved (source area). |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Error information:  If an error occurs during execution of the instruction, an error code is output at the RET_VAL parameter. |
| DSTBLK | Output <sup>1)</sup> | VARIANT | I, Q, M, D, L, P | Specifies the memory area to which the block is moved (destination area). |
| 1) The DSTBLK parameter is declared as Output, since the data flow into the tag. However, the tag itself must be declared as InOut in the block interface. |  |  |  |  |

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8091 | The source or destination area is only available in the load memory. |
| 8152 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the SRCBLK parameter. |
| 8352 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the DSTBLK parameter. |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL UBLKMOV VARIANT

(SRCBLK := P#M100.0 BYTE 10

RET_VAL =&gt; "Tag_ErrorCode"

DSTBLK =&gt; P#DB1.DBX0.0 BYTE 10

)

The instruction copies 10 bytes starting from MB100 and writes them to DB1. If an error occurs during the move operation, its error code is output in the "Tag_ErrorCode" tag.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### FILL: Fill block (S7-1500)

###### Description

You use the "Fill block" instruction to fill a memory area (destination area) with the content of another memory area (source area). The "Fill block" instruction moves the content of the source area to the destination area until the destination area is completely written. The move operation takes place in the direction of ascending addresses.

You use VARIANT to define the source and destination areas.

> **Note**
>
> The tags of the instruction can only be used within memory areas in which the "Optimized block access" attribute is not activated. This applies to data blocks (DBs), organization blocks (OBs), functions (FCs), bit memory (M), inputs (I), and outputs (Q).
>
> If a tag of the instruction has been declared with the retentivity setting "Set in IDB", however, you can also use this tag in memory areas "with optimized block access".
>
> For blocks with the "Optimized block access" attribute, you can use the "FILL_BLK instruction: Fill block" instruction.

The following figure shows the principle of the move operation:

![Description](images/43500633099_DV_resource.Stream@PNG-de-DE.png)

Example: The contents of the range MW100 to MW118 are to be preassigned with the contents of the memory words MW14 to MW20.

###### Consistency of source and destination data

Make sure that the source data remain unchanged during execution of the "Fill block" instruction, since otherwise consistency of the destination data cannot be guaranteed.

###### Memory areas

You can use the "Fill block" instruction to move the following memory areas:

- Areas of a data block
- Bit memory
- Process image input
- Process image output

###### General rules for moving

The source and destination areas must not overlap. If the destination area to be preset is not an integer multiple of the length of the BVAL input parameter, the destination area is nevertheless written up to the last byte.

If the destination area to be preset is smaller than the source area, the function only copies as much data as can be written to the destination area.

If the destination or source area actually present is smaller than the assigned memory area for the source or destination area (BVAL, BLK parameters), no data is transferred.

If the ANY pointer (source or destination) is of the data type BOOL, it must be addressed absolutely and the length specified must be divisible by 8; otherwise the instruction is not executed.

If the destination area is STRING data type, the instruction writes the entire string including the administration information.

###### Rules for moving structures

When you transfer a structure as an input parameter you must bear in mind that the length of a structure is always oriented to an even number of bytes. The structure will need one byte of additional memory space if you declare a structure with an odd number of bytes.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| BVAL | Input | VARIANT | I, Q, M, D, L, P | Specification of the memory area (source area), the content of which is used to fill the destination area at the BLK parameter. |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Error information:  If an error occurs during execution of the instruction, an error code is output at the RET_VAL parameter. |
| BLK | Output <sup>1)</sup> | VARIANT | I, Q, M, D, L, P | Specification of the memory area that will be filled with the content of the source area. |
| 1) The BLK parameter is declared as Output, since the data flow into the tag. However, the tag itself must be declared as InOut in the block interface. |  |  |  |  |

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8092 | The source or destination area is only available in the load memory. |
| 8152 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the BVAL parameter. |
| 8352 | The WSTRING, WCHAR, BOOL, and ARRAY of STRING data types are not supported at the BLK parameter. |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL FILL VARIANT

(BVAL := P#M14.0 WORD 4

RET_VAL =&gt; "Tag_ErrorCode"

BLK =&gt; P#M100.0 WORD 10

)

The instruction copies the source area from MW14 to MW20 and fills the destination area from MW100 to MW118 with the content of the 4 words contained in the memory area in the BVAL parameter.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Conversion operations (S7-1500)

This section contains information on the following topics:

- [CONVERT: Convert value (S7-1500)](#convert-convert-value-s7-1500)
- [ROUND: Round numerical value (S7-1500)](#round-round-numerical-value-s7-1500)
- [CEIL: Generate next higher integer from floating-point number (S7-1500)](#ceil-generate-next-higher-integer-from-floating-point-number-s7-1500)
- [FLOOR: Generate next lower integer from floating-point number (S7-1500)](#floor-generate-next-lower-integer-from-floating-point-number-s7-1500)
- [TRUNC: Truncate numerical value (S7-1500)](#trunc-truncate-numerical-value-s7-1500)
- [SCALE_X: Scale (S7-1500)](#scale_x-scale-s7-1500)
- [NORM_X: Normalize (S7-1500)](#norm_x-normalize-s7-1500)
- [Legacy (S7-1500)](#legacy-s7-1500-1)

#### CONVERT: Convert value (S7-1500)

##### Description

You use the "Convert value" instruction to read the content of the operand and convert it according to the assigned data types.

For information on possible conversions, refer to section "Explicit conversion" under "See also".

The value of the result is invalid if errors, such as an overflow, occur during processing.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Binary numbers, integers, floating-point numbers, CHAR, WCHAR, BCD16, BCD32 | I, Q, M, D, L, P or constant | Value to be converted. |
| &lt;Result&gt; | Output | Binary numbers, integers, floating-point numbers, CHAR, WCHAR, BCD16, BCD32 | I, Q, M, D, L, P | Result of the conversion |

You can select the data types of the instruction from the "???" drop-down lists.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := INT_TO_DINT("Tag_InValue")

The content of the "Tag_InValue" operand is read and converted to an integer (32-bit). The result is stored in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)
  
[Explicit conversions (S7-1500)](Data%20type%20conversion%20for%20S7-1500%20%28S7-1500%29.md#explicit-conversions-s7-1500)

#### ROUND: Round numerical value (S7-1500)

##### Description

You use the "Round numerical value" instruction to round the value of the operand to the nearest integer. The instruction interprets the value as a floating-point number and converts it into to the next integer. If the input value is exactly between an even and odd number, the even number is selected.

The value of the result is invalid if errors, such as an overflow, occur during processing.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value to be rounded. |
| &lt;Result&gt; | Output | Integers, floating-point numbers | I, Q, M, D, L, P | Result of rounding |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ROUND("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |
| --- | --- | --- |
| Tag_InValue | 1.50000000 | -1.50000000 |
| Tag_OutValue | 2 | -2 |

The floating-point number in the "Tag_InValue" operand is rounded to the nearest even integer and output in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### CEIL: Generate next higher integer from floating-point number (S7-1500)

##### Description

You use the "Generate next higher integer from floating-point number" instruction to round the value of the operand to the next higher integer. The instruction interprets the value as a floating-point number and converts this number to the next higher integer. The result can be greater than or equal to the input value.

The value of the result is invalid if errors, such as an overflow, occur during processing.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value as floating-point number |
| &lt;Result&gt; | Output | Integers, floating-point numbers | I, Q, M, D, L, P | Result with next higher integer |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := CEIL("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |
| --- | --- | --- |
| Tag_InValue | 0.50000000 | -0.50000000 |
| Tag_OutValue | 1 | 0 |

The floating-point number in the "Tag_InValue" operand is rounded to the next higher integer and output in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### FLOOR: Generate next lower integer from floating-point number (S7-1500)

##### Description

You use the "Generate next lower integer from floating-point number" instruction to round the value of the operand to the next lower integer. The instruction interprets the value as a floating-point number and converts this number to the next lower integer. The result can be less than or equal to the input value.

The value of the result is invalid if errors, such as an overflow, occur during processing.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L, P or constant | Input value as floating-point number |
| &lt;Result&gt; | Output | Integers, floating-point numbers | I, Q, M, D, L, P | Result with next lower integer |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := FLOOR("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |
| --- | --- | --- |
| Tag_InValue | 0.50000000 | -0.50000000 |
| Tag_OutValue | 0 | -1 |

The floating-point number in the "Tag_InValue" operand is rounded to the next lower integer and output in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### TRUNC: Truncate numerical value (S7-1500)

##### Description

You use the "Truncate numerical value" instruction to form an integer from the value of the operand. The value is interpreted as a floating-point number. The instruction selects only the integer part of the floating-point number and outputs it without decimal places as the result.

The value of the result is invalid if errors, such as an overflow, occur during processing.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Floating-point numbers | I, Q, M, D, L or constant | Input value as floating-point number |
| &lt;Result&gt; | Output | Integers, floating-point numbers | I, Q, M, D, L | Result with integer part of the floating-point number |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := TRUNC​("Tag_InValue")

The following table shows how the instruction works using specific operand values:

| Operand | Value |  |
| --- | --- | --- |
| Tag_InValue | 1.50000000 | -1.50000000 |
| Tag_OutValue | 1 | -1 |

The integer part of the floating-point number in the "Tag_InValue" operand is converted to an integer and output in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SCALE_X: Scale (S7-1500)

##### Description

You use the "Scale" instruction to scale the value of the VALUE parameter by mapping it to a specified value range. When the instruction is executed, the floating-point value in the VALUE input is scaled to the value range that was defined by the MIN and MAX parameters. The result of the scaling is an integer, which is stored in the OUT output.

The following figure shows an example of how values can be scaled:

![Description](images/14360154763_DV_resource.Stream@PNG-en-US.png)

The "Scale" instruction works with the following equation:

OUT = [VALUE ∗ (MAX – MIN)] + MIN

The value of the result is invalid if any of the following conditions are met:

- The value of the MIN parameter is greater than or equal to the value of the MAX parameter.
- The value of a specified floating-point number is outside the range of the normalized numbers according to IEEE-754.
- An overflow occurs.
- The value of the VALUE parameter is NaN (Not a Number = result of an invalid arithmetic operation).

> **Note**
>
> For additional information on the conversion of analog values, refer to the respective manual.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MIN | Input | Integers, floating-point numbers | I, Q, M, D, L or constant | Low limit of the value range |
| VALUE | Input | Floating-point numbers | I, Q, M, D, L or constant | Value to be scaled.  If you enter a constant, you must declare it. |
| MAX | Input | Integers, floating-point numbers | I, Q, M, D, L or constant | High limit of the value range |
| RET_VAL | Output | Integers, floating-point numbers | I, Q, M, D, L | Result of scaling |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL SCALE_X INT_REAL

(MIN := "Tag_Minimum"

VALUE := "Tag_Value"

MAX := "Tag_Maximum"

RET_VAL =&gt; "Tag_OutputValue"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| MIN | Tag_Minimum | 10 |
| VALUE | Tag_Value | 0.5 |
| MAX | Tag_Maximum | 30 |
| RET_VAL | Tag_ReturnValue | 20 |

The value of the "Tag_Value" parameter is scaled to the range of values defined by the values of the "Tag_Minimum" and "Tag_Maximum" parameters. The result is stored in the "Tag_ReturnValue" parameter.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### NORM_X: Normalize (S7-1500)

##### Description

You use the "Normalize" instruction to normalize the value of the VALUE parameter by mapping it to a linear scale. You use the MIN and MAX parameters to define the limits of a value range that is applied to the scale. The result is calculated based on the position of the value to be normalized within this value range and stored as a floating-point number in the OUT parameter. If the value to be normalized is equal to the value of the MIN parameter, the OUT parameter has the value "0.0". If the value to be normalized is equal to the value of the MAX parameter, the OUT parameter has the value "1.0".

The following figure shows an example of how values can be normalized:

![Description](images/14360589067_DV_resource.Stream@PNG-en-US.png)

The "Normalize" instruction works with the following equation:

OUT = (VALUE – MIN) / (MAX – MIN)

The value of the result is invalid if any of the following conditions are met:

- The value of the MIN parameter is greater than or equal to the value of the MAX parameter.
- The value of a specified floating-point number is outside the range of the normalized numbers according to IEEE-754.
- An overflow occurs.
- The value of the VALUE parameter is NaN (Not a Number = result of an invalid arithmetic operation).

> **Note**
>
> For additional information on the conversion of analog values, refer to the respective manual.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MIN<sup> 1)</sup> | Input | Integers, floating-point numbers | I, Q, M, D, L or constant | Low limit of the value range |
| VALUE<sup> 1)</sup> | Input | Integers, floating-point numbers | I, Q, M, D, L or constant | Value to be normalized |
| MAX<sup> 1)</sup> | Input | Integers, floating-point numbers | I, Q, M, D, L or constant | High limit of the value range |
| RET_VAL | Output | Floating-point numbers | I, Q, M, D, L | Result of the normalization |
| <sup>1)</sup> If you use constants in these three parameters, you only need to declare one of them. |  |  |  |  |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

For additional information on declaring constants, refer to "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL NORM_X INT_REAL

(MIN := "Tag_Minimum"

VALUE := "Tag_Value"

MAX := "Tag_Maximum"

RET_VAL =&gt; "Tag_OutputValue"

)

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| MIN | Tag_Minimum | 10 |
| VALUE | Tag_Value | 20 |
| MAX | Tag_Maximum | 30 |
| RET_VAL | Tag_ReturnValue | 0.5 |

The value of the "Tag_Value" parameter is assigned to the range of values that were defined with the "Tag_Minimum" and "Tag_Maximum" parameters. The tag value in the "Tag_Value" parameter is normalized according the defined value range. The result is stored as a floating-point number in the "Tag_ReturnValue" parameter.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### Legacy (S7-1500)

This section contains information on the following topics:

- [SCALE: Scale (S7-1500)](#scale-scale-s7-1500)
- [UNSCALE: Unscale (S7-1500)](#unscale-unscale-s7-1500)

##### SCALE: Scale (S7-1500)

###### Description

You use the "Scale" instruction to convert the integer of the IN parameter to a floating-point number that can be scaled in physical units between a low limit and a high limit. You use the LO_LIM and HI_LIM parameters to specify the low limit and high limit of the value range to which the input value is scaled. The result of the instruction is output at the OUT parameter.

The "Scale" instruction works with the following equation:

OUT = [((FLOAT (IN) – K1)/(K2–K1)) ∗ (HI_LIM–LO_LIM)] + LO_LIM

The values of the "K1" and "K2" constants are determined by the signal state at the BIPOLAR parameter. The following signal states are possible at the BIPOLAR parameter:

- Signal state "1": It is assumed that the value at the IN parameter is bipolar and lies in a value range between -27 648 and 27 648. In this case the constant "K1" has the value "-27 648.0" and the constant "K2" the value "+27 648.0".
- Signal state "0": It is assumed that the value of the IN parameter is unipolar and lies in a value range between 0 and 27 648. In this case the constant "K1" has the value "0.0" and the constant "K2" the value "+27 648.0".

When the value at the IN parameter is greater than the value of the constant "K2", the result of the instruction is set to the value of the high limit (HI_LIM) and an error is output.

When the value at the IN parameter is less than the value of the constant "K1", the result of the instruction is set to the value of the low limit (LO_LIM) and an error is output.

When the specified low limit is greater than the high limit (LO_LIM &gt; HI_LIM), the result is scaled inversely proportional to the input value.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | INT | I, Q, M, D, L, P or constant | Input value to be scaled. |
| HI_LIM | Input | REAL | I, Q, M, D, L, P or constant | High limit |
| LO_LIM | Input | REAL | I, Q, M, D, L, P or constant | Low limit |
| BIPOLAR | Input | BOOL | I, Q, M, D, L or constant | Indicates whether the value at the IN parameter is to be interpreted as bipolar or unipolar. The parameter can assume the following values:  1: Bipolar  0: Unipolar |
| RET_VAL | Output | WORD | I, Q, M, D, L, P | Error information |
| OUT | Output | REAL | I, Q, M, D, L, P | Result of the instruction |

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 0008 | The value of the IN parameter is greater than the value of the constant "K2" or less than the value of the constant "K1" |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL SCALE

(IN := "Tag_InputValue"

HI_LIM := "Tag_HighLimit"

LO_LIM := "Tag_LowLimit"

​BIPOLAR := "Tag_Bipolar"

RET_VAL =&gt; "Tag_ErrorCode"

OUT =&gt; "Tag_OutputValue"

)

The following table shows the values of the various operands before execution of the instruction:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | Tag_InputValue | 22 |
| HI_LIM | Tag_HighLimit | 100.0 |
| LO_LIM | Tag_LowLimit | 0.0 |
| BIPOLAR | Tag_Bipolar | 1 |
| RET_VAL | Tag_ErrorCode | W#16#0000 |
| OUT | Tag_OutputValue | 0.0 |

The following table shows the values of the various operands after execution of the instruction:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | Tag_InputValue | 22 |
| HI_LIM | Tag_HighLimit | 100.0 |
| LO_LIM | Tag_LowLimit | 0.0 |
| BIPOLAR | Tag_Bipolar | 1 |
| RET_VAL | Tag_ErrorCode | W#16#0000 |
| OUT | Tag_OutputValue | 50.03978588 |

The "Tag_InputValue" operand indicates the value that is to be converted and scaled. The high and low limits are defined by the "Tag_HighLimit" and "Tag_LowLimit" operands. You use operand "Tag_Bipolar" = TRUE to specify that the value of the IN parameter is to be interpreted as bipolar. The result of the instruction is output at the "Tag_OutputValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### UNSCALE: Unscale (S7-1500)

###### Description

You use the "Unscale" instruction to unscale the floating-point number in the IN parameter into physical units between a low limit and a high limit and convert it into an integer. You use the LO_LIM and HI_LIM parameters to specify the low limit and high limit of the value range to which the input value is unscaled. The result of the instruction is output at the OUT parameter.

The "Unscale" instruction works with the following equation:

OUT = [((IN–LO_LIM)/(HI_LIM–LO_LIM)) ∗ (K2–K1) ] + K1

The values of the "K1" and "K2" constants are determined by the signal state at the BIPOLAR parameter. The following signal states are possible at the BIPOLAR parameter:

- Signal state "1": It is assumed that the value at the IN parameter is bipolar and lies in a value range between -27 648 and 27 648. In this case the constant "K1" has the value "-27 648.0" and the constant "K2" the value "+27 648.0".
- Signal state "0": It is assumed that the value at the IN parameter is unipolar and lies in a value range between 0 and 27 648. In this case the constant "K1" has the value "0.0" and the constant "K2" the value "+27 648.0".

When the value at parameter IN is not within the limits defined by HI_LIM and LO_LIM, an error is output and the result is set to the nearest limit.

When the indicated low limit value is greater than the high limit value (LO_LIM &gt; HI_LIM), the result is scaled in reverse proportion to the input value.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | REAL | I, Q, M, D, L, P or constant | Input value to be unscaled to an integer value. |
| HI_LIM | Input | REAL | I, Q, M, D, L, P or constant | High limit |
| LO_LIM | Input | REAL | I, Q, M, D, L, P or constant | Low limit |
| BIPOLAR | Input | BOOL | I, Q, M, D, L or constant | Indicates whether the value at the IN parameter is to be interpreted as bipolar or unipolar. The parameter can assume the following values:  1: Bipolar  0: Unipolar |
| RET_VAL | Output | WORD | I, Q, M, D, L, P | Error information |
| OUT | Output | INT | I, Q, M, D, L, P | Result of the instruction |

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 0008 | The value of the IN parameter is greater than the value of the high limit (HI_LIM) or less than the value of the low limit (LO_LIM). |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats here: [Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status) |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL UNSCALE

(IN := "Tag_InputValue"

HI_LIM := "Tag_HighLimit"

LO_LIM := "Tag_LowLimit"

​BIPOLAR := "Tag_Bipolar"

RET_VAL =&gt; "Tag_ErrorCode"

OUT =&gt; "Tag_OutputValue"

)

The following table shows the values of the various operands before execution of the instruction:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | Tag_InputValue | 50.03978588 |
| HI_LIM | Tag_HighLimit | 100.0 |
| LO_LIM | Tag_LowLimit | 0.0 |
| BIPOLAR | Tag_Bipolar | 1 |
| RET_VAL | Tag_ErrorCode | W#16#0000 |
| OUT | Tag_OutputValue | 0.0 |

The following table shows the values of the various operands after execution of the instruction:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | Tag_InputValue | 50.03978588 |
| HI_LIM | Tag_HighLimit | 100.0 |
| LO_LIM | Tag_LowLimit | 0.0 |
| BIPOLAR | Tag_Bipolar | 1 |
| RET_VAL | Tag_ErrorCode | W#16#0000 |
| OUT | Tag_OutputValue | 22 |

The "Tag_InputValue" operand indicates the value that is to be converted and unscaled. The high and low limits are defined by the "Tag_HighLimit" and "Tag_LowLimit" operands. You use operand "Tag_Bipolar" = TRUE to specify that the value of the IN parameter is to be interpreted as bipolar. The result of the instruction is output at the "Tag_OutputValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Program control operations (S7-1500)

This section contains information on the following topics:

- [Runtime control (S7-1500)](#runtime-control-s7-1500)

#### Runtime control (S7-1500)

This section contains information on the following topics:

- [ENDIS_PW: Locking and unlocking passwords of the CPU access levels (S7-1500)](#endis_pw-locking-and-unlocking-passwords-of-the-cpu-access-levels-s7-1500)
- [RE_TRIGR: Restart cycle monitoring time (S7-1500)](#re_trigr-restart-cycle-monitoring-time-s7-1500)
- [STP: Exit program (S7-1500)](#stp-exit-program-s7-1500)
- [GET_ERROR: Get error locally (S7-1500)](#get_error-get-error-locally-s7-1500)
- [GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
- [INIT_RD: Initialize all retain data (S7-1500)](#init_rd-initialize-all-retain-data-s7-1500)
- [WAIT: Configure time delay (S7-1500)](#wait-configure-time-delay-s7-1500)

##### ENDIS_PW: Locking and unlocking passwords of the CPU access levels (S7-1500)

###### Description

With the instruction ENDIS_PW (enable / disable password) you lock the passwords for the individual access levels of your CPU or release them again.

By locking the passwords, existing legitimized connections can be terminated.

If you call ENDIS_PW with signal state "0" at the parameter REQ, it is displayed for each access level of your CPU whether the associated password is currently locked (associated output parameter has the value "0") or is released (associated output parameter has the value "1"). When calling ENDIS_PW with REQ=0 no passwords are locked or released.

If you call ENDIS_PW with signal state "1" at the parameter REQ, the effect of the instruction depends on the signal state at the input parameters F_PWD, FULL_PWD, R_PWD and HMI_PWD:

- If the signal state "0" is pending, the password of the associated access level is locked. (If it was already locked, it remains locked.)
- If the signal state "1" is pending, the password of the associated access level is released. (If it was already released, it remains released.)

Each password can be locked or released independently of the other passwords. In this way, you can lock all passwords with the exception of the fail-safe password. In this case you limit the access to your fail-safe CPU to a few users.

The output parameters F_PWD_ON, FULL_PWD_ON, R_PWD_ON and HMI_PWD_ON display the current status of password permissibility for the individual access levels after the instruction has finished processing, namely independently of the state of the REQ parameter when the instruction is called.

Input parameters which belong to access levels for which you have not configured a password, must have the signal state TRUE (if you do not observe this rule, RET_VAL has a value different to "0".). After processing ENDIS_PW the associated output parameter has the value TRUE.

The same applies for the parameter F_PWD. Since the fail-safe password is only configurable for an F-CPU, the associated input parameter F_PWD in a standard CPU must always be interconnected with the signal state TRUE.

If the ENDIS_PW instruction returns an error, its call has no effect, meaning that all passwords can be used after the ENDIS_PW call in the same way as before the ENDIS_PW call.

###### Additional access protection for S7-1500 CPUs with display

In addition to the access protection via the ENDIS_PW instruction, you can also lock or release the passwords at the display of the individual access levels (local lock of the password) at the S7-1500 CPUs with display. The password lock can be set separately on the display for each access level.

The CPU saves the last change made to the password status - independently of whether it was made through a call of ENDIS_PW or through an input on the display.

You determine the currently valid password status for the individual access levels by calling the ENDIS_PW instruction with REQ=0.

###### Users and operating system actions and their effects on the existing password lock

The table below shows the effects of different user and operating system actions on a previously set password lock.

| User or operating system action | Password status after the action |
| --- | --- |
| CPU reset to factory settings | The password is enabled. |
| Memory reset | The password is still locked. |
| The password on the display of the S7-1500-CPU is released | The password is enabled. |
| Call of ENDIS_PW with F_PWD=1 or FULL_PWD=1 or R_PWD=1 or HMI_PWD=1 | The password is enabled. |
| Set the S7-1500 CPU into STOP mode by means of the mode selector switch or the "STOP" mode selector key. | The password is enabled. |
| Then set the S7-1500 CPU into RUN mode by means of the mode selector switch or the "RUN" mode selector key. | The password is locked again.  Note: If something goes wrong with the action "set into operating state RUN" and the CPU falls back again into the STOP operating state, the password is also locked again. |
| In the case of an S7-1200 CPU, insert an empty transfer card or an empty program card. | The password is enabled. |
| Formatting of the WinAC memory partition by WinAC panel | The password is enabled. |
| Transition from POWER OFF to POWER ON | - S7-1200-CPU: The password is enabled. - S7-1500-CPU: The password is still locked. |
| Operating state transitions, e.g. operating state transition to STOP (caused by an error, by the STP instruction or by communication). | The password is still locked. |

> **Note**
>
> **Locking the HMI password through ENDIS_PW**
>
> If you have locked the HMI password by calling ENDIS_PW, the HMI systems cannot access your CPU anymore. Operating and observing your CPU via HMI systems is thus not possible anymore.

> **Note**
>
> **Already legitimized connections**
>
> Existing connections which were legitimized before calling ENDIS_PW can be terminated through the execution of ENDIS_PW. This depends on the current password status for the individual access levels and the values at the inputs x_PWD.
>
> Example: A connection that is authorized with read access is terminated by calling ENDIS_PW with REQ = 1 and R_PWD = 0.

###### Preventing unintentional lockout on an S7-1500 CPU

You have the following two possibilities to prevent an unintentional lockout at an S7-1500 CPU:

- By calling ENDIS_PW you can release accidentally locked passwords on the display of the CPU again. (This is obviously only possible for S7-1500-CPUs with display.)
- Set the CPU into the operating mode STOP with the mode selector switch or the "STOP" mode selector key. This ends the password lock. The subsequent transition to the RUN operating mode (using the mode selector switch or the "RUN" mode selector key) sets the password lock again.

###### Preventing unintentional lockout of an S7-1200 CPU

Existing password locks are removed during the transition POWER OFF - POWER ON at an S7-1200 CPU. This means that it is possible and advisable to prevent unintentional lockout with the help of specific program sequences within your program.

To do so, program a time control either by means of a cyclic interrupt OB or a timer in the OB 1. This gives you the option of calling the ENDIS_PW instruction in the respective OB (for example OB 1 or OB 35) relatively quickly after a transition from POWER OFF to POWER ON. Call the instruction in the startup OB (OB 100) in order to keep as short as possible the time window in which the application is not active and thus ensure that no restrictions exist in the password legitimation. This procedure offers you the greatest possible protection against unauthorized access.

If there has been an accidental lockout, you can skip the call in the startup OB (by querying an input parameter, for example) and you have the set time (for example, 10 seconds up to 1 minute) to establish a connection to the CPU before the lock becomes active once again.

If there is no timer in your program code and a lockout has occurred, insert an empty transfer card or an empty program card into the CPU. The empty transfer card or program card deletes the internal load memory of the CPU. You must then download the user program once again from STEP 7 to the CPU.

###### Procedure for lost passwords with an S7-1200 CPU

If you have lost the password for a password-protected S7-1200 CPU, delete the password-protected program with an empty transfer card or program card. The empty transfer card or program card deletes the internal load memory of the CPU. You can then load a new user program from STEP 7 Basic in the CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Inserting an empty transfer card**  When you insert a transfer card in a CPU during runtime, the CPU goes to STOP mode. If operating states are unstable, controllers may fail and thus cause the uncontrolled operation of the controlled devices. This leads to an unforeseen operation of the automation system which can cause deadly or serious injuries and/or damage to property.  Once you have pulled the transfer card, the content of the transfer card is available in the internal load memory. Make sure that the card does not include a program at this point. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Inserting an empty program card**  When you insert a program card in a CPU during runtime, the CPU goes to STOP mode. If operating states are unstable, controllers may fail and thus cause the uncontrolled operation of the controlled devices. This leads to an unforeseen operation of the automation system which can cause deadly or serious injuries and/or damage to property.  Make sure that the program card is empty. The internal load memory is copied to the empty program card. Once you have pulled the previously empty program card, the internal load memory is empty. |  |

You must remove the transfer card or program card before you put the CPU into RUN mode.

###### Parameter

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | - REQ=0: Determine current password status for the individual access levels in your CPU - REQ=1: Lock or release passwords for the individual access levels of your CPU |
| F_PWD | Input | BOOL | I, Q, M, D, L or constant | - F_PWD = 0: Lock password of the access level "Full access including fail-safe (no protection)" - F_PWD = 1: Release password of the access level "Full access including fail-safe (no protection)" |
| FULL_PWD | Input | BOOL | I, Q, M, D, L or constant | - FULL_PWD = 0: Lock password of the access level "Full access (no protection)" - FULL_PWD = 1: Release password of the access level "Full-access (no protection)" |
| R_PWD | Input | BOOL | I, Q, M, D, L or constant | - R_PWD = 0: Lock password of the access level "Read access" - R_PWD = 1: Release password of the access level "Read access" |
| HMI_PWD | Input | BOOL | I, Q, M, D, L or constant | - HMI_PWD = 0: Lock password of the access level "HMI access" - HMI_PWD = 1: Release password of the access level "HMI access" |
| F_PWD_ON | Output | BOOL | I, Q, M, D, L | Current password status of the access level "Full access including fail-safe (no protection)":  - F_PWD_ON = 0: Password locked - F_PWD_ON = 1: Password released |
| FULL_PWD_ON | Output | BOOL | I, Q, M, D, L | Current password status of the access level "Full access (no protection)":  - FULL_PWD_ON = 0: Password locked - FULL_PWD_ON = 1: Password released |
| R_PWD_ON | Output | BOOL | I, Q, M, D, L | Current password status of the access level "Read access":  - R_PWD_ON = 0: Password locked - R_PWD_ON = 1: Password released |
| HMI_PWD_ON | Output | BOOL | I, Q, M, D, L | Current password status of the access level "HMI access":  - HMI_PWD_ON = 0: Password locked - HMI_PWD_ON = 1: Password released |
| RET_VAL | Output | WORD | I, Q, M, D, L | Error information |

You can find additional information on valid data types under "See also".

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code*  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 8090 | The instruction ENDIS_PW is not supported. |
| 80D0 | - F-CPU: No password was configured for the access level "Full access including fail-safe (no protection)". The signal state of F_PWD must be TRUE. - Standard CPU: The signal state of F_PWD must be TRUE. |
| 80D1 | No password was configured for the access level "Full access (no protection)". The signal state of FULL_PWD must be TRUE. |
| 80D2 | No password was configured for the access level "Read access". The signal state of R_PWD must be TRUE. |
| 80D3 | No password was configured for the access level "HMI access". The signal state of HMI_PWD must be TRUE. |
| *The error codes can be displayed as integer or hexadecimal value in the program editor. You can find information on switching the display formats under "See also". |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### RE_TRIGR: Restart cycle monitoring time (S7-1500)

###### Description

The "Restart cycle monitoring time" instruction is used to restart the cycle monitoring time of the CPU. The cycle monitoring time then restarts with the time you have set in the CPU configuration.

The instruction executes completely within a time span (10 times the maximum program cycle), regardless of the number of calls. Once this time has expired, the program cycle can no longer be prolonged.

###### Calling the instruction

You can call the instruction regardless of the priority in all organization blocks.

###### Parameters

The "Restart cycle monitoring time" instruction has no parameters and supplies no error information.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### STP: Exit program (S7-1500)

###### Description

You use the "Exit program" instruction to set the CPU to STOP mode and therefore to terminate the execution of the program. The effects of changing from RUN to STOP depend on the CPU configuration.

###### Parameters

The "Exit program" instruction has no parameters and supplies no error information.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### GET_ERROR: Get error locally (S7-1500)

###### Description

The "Get error locally" instruction is used to query the occurrence of errors within a program block. This normally involves programming or access errors. If the system reports an error during the execution of the program block, detailed information is stored in the operand at the OUT output for the first error to occur during the execution of the block since the last execution of the instruction.

Only operands of the "ErrorStruct" system data type can be specified at the OUT output. The "ErrorStruct" system data type specifies the exact structure in which the information about the error is stored. Using additional instructions, you can evaluate this structure and program an appropriate response. If several errors occur in the program block, the error information about the next error to occur is output by the instruction only after the first error that occurred has been remedied.

> **Note**
>
> **Output OUT**
>
> The OUT output is only changed if error information is present. To set the output back to "0" after handling an error, you have the following options:
>
> - Declare the tag in the "Temp" section of the block interface.
> - Reset the tag to "0" before calling the instruction.

> **Note**
>
> **Activation of the local error handling**
>
> As soon as you insert the instruction in the program code of a program block, the local error handling is activated and default system reactions are ignored when errors occur.

###### Options for error handling

You can find an overview of the options for error handling here: [Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

For a detailed example of local error handling that contains several error handling options, refer to: [Example of how to handle program execution errors](Programming%20basics.md#example-of-how-to-handle-program-execution-errors)

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| OUT | Output | ErrorStruct | D, L | Error information |

###### Data type "ErrorStruct"

The "ErrorStruct" data type can be inserted in a global data block or in the block interface. You can insert the data type more then once if you assign a different name for the data structure each time. The data structure and the name of individual structure elements cannot be changed. If you save the error information in a global data block, it can also be read out by other program blocks.

The following table shows the structure of the "ErrorStruct" data type:

| Structure component |  | Data type | Description |
| --- | --- | --- | --- |
| ERROR_ID |  | WORD | Error ID |
| FLAGS |  | BYTE | Shows whether the error occurred during a program block call.  16#01: Error during a program block call  16#00: No error during a program block call |
| REACTION |  | BYTE | Default reaction:   0: Ignore (write error)  1: Continue with substitute value "0" (read error)  2: Skip instruction (system error) |
| CODE_ADDRESS |  | CREF | Information about the address and type of the program block |
|  | BLOCK_TYPE | BYTE | Program block type in which the error occurred:  1: Organization block (OB)  2: Function (FC)  3: Function block (FB) |
|  | CB_NUMBER | UINT | Number of the code block |
|  | OFFSET | UDINT | Reference to the internal memory |
| MODE |  | BYTE | Information about the address of an operand |
| OPERAND_NUMBER |  | UINT | Operand number of the machine command |
| POINTER_NUMBER_LOCATION |  | UINT | (A) Internal pointer |
| SLOT_NUMBER_SCOPE |  | UINT | (B) Storage area in internal memory |
| DATA_ADDRESS |  | NREF | Information about the address of an operand |
|  | AREA | BYTE | (C) Memory area:  L: 16#40...16#7F, 16#86, 16#87, 16#8E, 16#8F, 16#C0...16#FF   I: 16#81   Q: 16#82   M: 16#83   DB: 16#40, 16#84, 16#85, 16#8A, 16#8B   PI: 16#01   PQ: 16#02   Technological objects: 16#04 |
|  | DB_NUMBER | UINT | (D) Number of the data block |
|  | OFFSET | UDINT | (E) Relative address of the operand |

###### Structure component "ERROR_ID"

The following table shows the values that can be output at the structure component "ERROR_ID":

| ID* (hexadecimal) | ID* (decimal) | Description |
| --- | --- | --- |
| 0 | 0 | No error |
| 2503 | 9475 | Invalid pointer |
| 2520 | 9504 | Invalid STRING |
| 2522 | 9506 | Read error: Operand outside the valid range |
| 2523 | 9507 | Write error: Operand outside the valid range |
| 2524 | 9508 | Read error: Invalid operand |
| 2525 | 9509 | Write error: Invalid operand |
| 2528 | 9512 | Read error: Data alignment |
| 2529 | 9513 | Write error: Data alignment |
| 252C | 9516 | Invalid pointer |
| 2530 | 9520 | Write error: Data block |
| 2533 | 9523 | Invalid reference used |
| 2534 | 9524 | Block number error FC |
| 2535 | 9525 | Block number error FB |
| 2538 | 9528 | Access error: DB does not exist |
| 2539 | 9529 | Access error: Wrong DB used |
| 253A | 9530 | Global data block does not exist |
| 253C | 9532 | Faulty information or the function does not exist |
| 253D | 9533 | System function does not exist |
| 253E | 9534 | Faulty information or the function block does not exist |
| 253F | 9535 | System block does not exist |
| 2550 | 9552 | Access error: DB does not exist |
| 2551 | 9553 | Access error: Wrong DB used |
| 2575 | 9589 | Error in the program nesting depth |
| 2576 | 9590 | Error in the local data distribution |
| 2577 | 9591 | The block property "Parameter passing via registers" is not selected. |
| 25A0 | 9632 | Internal error in TP |
| 25A1 | 9633 | Tag is write-protected |
| 25A2 | 9634 | Invalid numerical value of tag |
| 2942 | 10562 | Read error: Input |
| 2943 | 10563 | Write error: Output |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Use of the instructions GET_ERROR and GET_ERR_ID](Programming%20basics.md#use-of-the-instructions-get_error-and-get_err_id)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### GET_ERR_ID: Get error ID locally (S7-1500)

###### Description

The "Get error ID locally" instruction is used to query the occurrence of errors within a block. This is usually to access error. If the system reports during the block processing errors within the block execution since the last execution of the instruction, the error ID of the first error that occurred in the tag is stored at the RET_VAL output.

Only operands of the WORD data type can be specified at the RET_VAL output. If several errors occur in the block, the error ID of the next error to occur in the instruction is output only after the first error that occurred has been remedied.

> **Note**
>
> The RET_VAL output is only changed if error information is present. To set the output back to "0" after handling an error, you have the following options:
>
> - Declare the tag in the "Temp" section of the block interface.
> - Reset the tag to "0" before calling the instruction.

The output of the "Get error ID locally" instruction is only set if error information is present. If one of these conditions is not fulfilled, the remaining program execution is not affected by the "Get error ID locally" instruction.

You can find an example of how you can implement the instruction in combination with other troubleshooting options under "See also".

> **Note**
>
> The "Get error ID locally" instruction enables local error handling within a block. If the "Get error ID locally" instruction is inserted in the program code of a block, any predefined system reactions are ignored if errors occur.

###### Options for error handling

You can find an overview of the options for error handling here: [Overview of mechanisms for error handling](Programming%20basics.md#overview-of-mechanisms-for-error-handling)

For a detailed example of local error handling that contains several error handling options, refer to: [Example of how to handle program execution errors](Programming%20basics.md#example-of-how-to-handle-program-execution-errors)

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RET_VAL | Output | WORD | I, Q, M, D, L | Error ID |

###### Parameter RET_VAL

The following table shows the values that can be output at the RET_VAL parameter:

| Error code* (hexadecimal) | Error code* (decimal) | Description |
| --- | --- | --- |
| 0 | 0 | No error |
| 2503 | 9475 | Invalid pointer |
| 2520 | 9504 | Invalid STRING |
| 2522 | 9506 | Read error: Operand outside the valid range |
| 2523 | 9507 | Write error: Operand outside the valid range |
| 2524 | 9508 | Read error: Invalid operand |
| 2525 | 9509 | Write error: Invalid operand |
| 2528 | 9512 | Read error: Data alignment |
| 2529 | 9513 | Write error: Data alignment |
| 252C | 9516 | Invalid pointer |
| 2530 | 9520 | Write error: Data block |
| 2533 | 9523 | Invalid reference used |
| 2534 | 9524 | Block number error FC |
| 2535 | 9525 | Block number error FB |
| 2538 | 9528 | Access error: DB does not exist |
| 2539 | 9529 | Access error: Wrong DB used |
| 253A | 9530 | Global data block does not exist |
| 253C | 9532 | Faulty information or the function does not exist |
| 253D | 9533 | System function does not exist |
| 253E | 9534 | Faulty information or the function block does not exist |
| 253F | 9535 | System block does not exist |
| 2550 | 9552 | Access error: DB does not exist |
| 2551 | 9553 | Access error: Wrong DB used |
| 2575 | 9589 | Error in the program nesting depth |
| 2576 | 9590 | Error in the local data distribution |
| 2577 | 9591 | The block property "Parameter passing via registers" is not selected. |
| 25A0 | 9632 | Internal error in TP |
| 25A1 | 9633 | Tag is write-protected |
| 25A2 | 9634 | Invalid numerical value of tag |
| 2942 | 10562 | Read error: Input |
| 2943 | 10563 | Write error: Output |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Use of the instructions GET_ERROR and GET_ERR_ID](Programming%20basics.md#use-of-the-instructions-get_error-and-get_err_id)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### INIT_RD: Initialize all retain data (S7-1500)

###### Description

You use the "Initialize all retain data" instruction to reset the retentive data of all data blocks, bit memories, and SIMATIC timers and counters at the same time. The instruction can only be executed within a startup OB because the execution exceeds the program cycle duration.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | If the input "REQ" has the signal state "1", all retentive data are reset. |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information:  If an error occurs during execution of the instruction, an error code is output at the RET_VAL parameter. |

You can find additional information on valid data types under "See also".

###### Parameter RET_VAL

The following table shows the meaning of the values of the RET_VAL parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 80B5 | The instruction cannot be executed because it was not programmed within a startup OB. |
| General error information | See also: "GET_ERR_ID: Get error ID locally" |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

###### Example

The following example shows how the instruction works:

GRAPH

CALL INIT_RD

(REQ := "Tag_REQ"

RET_VAL =&gt; "Tag_RET_VAL"

)

If the "Tag_REQ" operand has signal state "1", the instruction is executed. All retentive data of all data blocks, bit memories, and SIMATIC timers and counters are reset.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[GET_ERR_ID: Get error ID locally (S7-1500)](#get_err_id-get-error-id-locally-s7-1500)
  
[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

##### WAIT: Configure time delay (S7-1500)

###### Description

You can use the "Configure time delay" instruction to pause the program execution for a specific period of time. You indicate the period of time in microseconds in the WT parameter.

You can configure time delays from -32768 up to 32767 microseconds (μs). The smallest possible delay time depends on the CPU and corresponds to the execution time of the instruction.

The execution of the instruction can be interrupted by higher priority events and does not return any error information.

> **Note**
>
> **Negative delay time**
>
> If you specify a negative delay time at parameter WT, the enable output ENO, or the RLO and the BR bit, will return the signal state FALSE. A negative delay time does not affect the CPU. The following instructions linked to enable output ENO are not executed in LAD or FBD.

###### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| WT | Input | INT | I, Q, M, D, L, P or constant | Time delay in microseconds (μs) |

###### Example of the influence of the planned delay time

In the following example, you will see the influence of the delay time of the instruction "WAIT" in various scenarios.

The following figure is a schematic representation of the scenarios:

![Example of the influence of the planned delay time](images/109025533323_DV_resource.Stream@PNG-en-US.png)

Remaining time = The period between the end of the planned delay time (via "WAIT") until the end of the interrupt OB

Excess time = The period between the end of the interrupt OB and the end of the planned delay time (via "WAIT").

**Case 1:**

The "WAIT" instruction is called in an OB1. The "WAIT" instruction can be interrupted by higher-priority OBs or higher-priority processes (e.g. System Threads). However, the delay time of the "WAIT" instruction is neither changed nor deferred.

**Cases 2 and 3:**

Processing of the program in OB1 is resumed after a time delay of 20 ms. This time delay is calculated by calling the "WAIT" instruction in OB1 (see OB1 with WAIT). Within these 20 ms, an interrupt OB can run its own program code. The send clock of the CPU is not changed.

**Case 4:**

Processing of the program in OB1 is resumed after the higher-priority process has ended. The 20 ms delay time in OB1 has elapsed, but the higher-priority process still needs to be ended. The send clock of the CPU is increased.

> **Note**
>
> **Order of execution of system or communication processes (System Threads)**
>
> The System Threads usually use the priority "15". There are also System Threads with a higher priority than "26", but these processes cause a lower CPU load. System Threads are not displayed in the figure.

**Runtime measurement of the OB1 using the "RT_INFO" instruction:**

Case 2: 20 ms - 8 ms - System Threads = &lt;12 ms. Send clock: ~20 ms.

Case 3: 20 ms - 11 ms - System Threads - &lt;9 ms. Send clock: ~20 ms.

Case 4: 20 ms - 15 ms - System Threads - &lt;7 ms. Send clock: ~22 ms.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Word logic operations (S7-1500)

This section contains information on the following topics:

- [NOT (INV): Inverting (S7-1500)](#not-inv-inverting-s7-1500)
- [DECO: Decode (S7-1500)](#deco-decode-s7-1500)
- [ENCO: Encode (S7-1500)](#enco-encode-s7-1500)
- [SEL: Select (S7-1500)](#sel-select-s7-1500)
- [MUX: Multiplex (S7-1500)](#mux-multiplex-s7-1500)
- [DEMUX: Demultiplex (S7-1500)](#demux-demultiplex-s7-1500)

#### NOT (INV): Inverting (S7-1500)

##### Description

You use the instruction "Inverting" to invert the signal status of the bits of the operand. When the instruction is executed, the value of the operand is linked by EXCLUSIVE OR to a hexadecimal mask (W#16#FFFF for 16-bit numbers or DW#16#FFFF FFFF for 32-bit numbers). This inverts the signal state of the individual bits that are then output as the result.

##### Parameters

The following table shows the parameters of the instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand&gt; | Input | Bit strings, integers | I, Q, M, D, L, P or constant | Input value |
| &lt;Result&gt; | Output | Bit strings, integers | I, Q, M, D, L, P | Ones complement of the operand value |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"TagOut_Value" := NOT("TagIn_Value")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| TagIn_Value | W#16#000F |
| TagOut_Value | W#16#FFF0 |

The instruction inverts the signal state of the individual bits at "TagIn_Value" operand and writes the result to the "TagOut_Value" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### DECO: Decode (S7-1500)

##### Description

You use the "Decode" instruction to set a bit in the output value that is specified by the input value .

The "Decode" instruction reads the value of the IN parameter and sets the bit in the OUT parameter whose bit position corresponds to the value read. The other bits in the output value are filled with zeroes. When the value of the IN parameter is greater than 31, a modulo-32 operation is executed.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | UINT | I, Q, M, D, L, P or constant | Position of the bit in the output value that is set. |
| OUT | Output | Bit strings | I, Q, M, D, L, P | Output value |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL DECO UINT_DWORD

(IN := "Tag_Input"

OUT =&gt; "Tag_Output"

)

The following figure shows how the instruction functions using specific values:

![Example](images/51492948107_DV_resource.Stream@PNG-de-DE.png)

The instruction reads bit number "3" from the value of the "Tag_Input" operand of the input and sets the third bit in the value of the "Tag_Output" operand of the output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ENCO: Encode (S7-1500)

##### Description

You use the "Encode" instruction to read the bit number of the least significant set bit in the input value and output it in the OUT parameter.

The "Encode" instruction selects the least significant bit of the value in the IN parameter and writes its bit number in the operands in the OUT parameter. If the IN parameter has the value DW#16#00000001 or DW#16#00000000, the value "0" is output in the OUT parameter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Bit strings | I, Q, M, D, L, P or constant | Input value |
| OUT | Output | INT | I, Q, M, D, L, P | Output value |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

CALL ENCO DWORD

(IN := "Tag_Input"

OUT =&gt; "Tag_Output"

)

The following figure shows how the instruction functions using specific values:

![Example](images/51493666315_DV_resource.Stream@PNG-de-DE.png)

The instruction selects the least significant set bit of the "Tag_Input" tag and writes its bit position "3" to the "Tag_Output" tag.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SEL: Select (S7-1500)

##### Description

You use the "Select" instruction to select, dependent on a switch (G input), one of two inputs, IN0 or IN1, and move its content to the OUT output. If the G input has the signal state "0", the value at the IN0 input is moved. If the G input has the signal state "1", the value of the IN1 input is moved to the OUT output.

The instruction is only executed if the tags of all parameters have the same data type.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| G | Input | BOOL | I, Q, M, D, L or constant | Switch |
| IN0 | Input | Bit strings, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | First input value |
| IN1 | Input | Bit strings, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P or constant | Second input value |
| OUT | Output | Bit strings, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L, P | Result |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL SEL CHAR

(G := "Tag_Input_G"

IN0 := "Tag_Input0"

IN1 := "Tag_Input1"

OUT =&gt; "Tag_Output"

​)

The following table shows how the instruction functions using specific values:

| Parameter | Operand | Value |
| --- | --- | --- |
| G | Tag_Input_G | 1 |
| IN0 | Tag_Input0 | W#16#0000 |
| IN1 | Tag_Input1 | W#16#FFFF |
| OUT | Tag_Output | W#16#FFFF |

Based on the signal state of the "Tag_Input_G" input, the value of the "Tag_Input0" or "Tag_Input1" input is selected and moved to the "Tag_Output" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MUX: Multiplex (S7-1500)

##### Description

You use the "Multiplex" instruction to copy the content of a selected input to the RET_VAL output. The number of selectable inputs can be extended to a maximum of 32. Numbering starts at IN0 and continues consecutively with each new input. You use the K parameter to define the input whose content is to be copied to the RET_VAL output. If the value of the K parameter is greater than the number of available inputs, the content of the INELSE parameter is copied to the RET_VAL output.

The "Multiplex" instruction can only be executed if the tags in all inputs and in the RET_VAL output have the same data type. The K parameter is an exception, since only integers can be specified for it.

The value of the RET_VAL parameter is invalid if one of the following conditions is met:

- The input at the K parameter is located outside the available inputs. This reaction is independent of whether the input INELSE is used or not. The value at the output RET_VAL remains unchanged and the enable ouput ENO is set to "0".
- Errors occurred during execution of the instruction.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| K | Input | Integers | I, Q, M, D, L or constant | Specifies the input whose content is to be copied. |
| IN0 | Input | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L or constant | First input value |
| IN1 | Input | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L or constant | Second input value |
| INn | Input | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L or constant | Optional input values |
| INELSE | Input | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L or constant | Specifies the value that is copied when K &gt; n. |
| RET_VAL | Output | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L | Output to which the value is copied. |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL MUX SINT_SINT

(K := "Tag_Number"

IN0 := "Tag_Value_1"

IN1 := "Tag_Value_2"

INELSE := "Tag_Value_3"

RET_VAL =&gt; "Tag_Result"

​ )

The following table shows how the instruction works using specific operand values:

| Parameter | Operand | Value |
| --- | --- | --- |
| K | Tag_Number | 1 |
| IN0 | Tag_Value_1 | DW#16#00000000 |
| IN1 | Tag_Value_2 | DW#16#3E4A7D |
| INELSE | Tag_Value_3 | DW#16#FFFF0000 |
| RET_VAL | Tag_Result | DW#16#3E4A7D |

Depending on the value of the "Tag_Number" operand, the value of the "Tag_Value_1" input is copied and output to the operand in the "Tag_Result" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### DEMUX: Demultiplex (S7-1500)

##### Description

You use the "Demultiplex" instruction to copy the content of the IN input to a selected output. The number of selectable outputs can be extended to a maximum of 32. Numbering starts at OUT0 and continues consecutively with each new output. You use the K parameter to define the output to which the content of the IN input is to be copied. The other outputs are not changed. If the value of the K parameter is greater than the number of available outputs, the content of the IN input is copied to the OUTELSE parameter.

The "Demultiplex" instruction can only be executed if the tags in the IN input and in all outputs have the same data type. The K parameter is an exception, since only integers can be specified for it.

The value of the OUTELSE output is invalid if one of the following conditions is met:

- The value of the K parameter is greater than the number of available outputs.
- Errors occurred during execution of the instruction.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| K | Input | Integers | I, Q, M, D, L or constant | Specifies the output to which the input value (IN) is copied. |
| IN | Input | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L or constant | Input value |
| OUT0 | Output | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L | First output |
| OUT1 | Output | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L | Second output |
| OUTn | Output | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L | Optional outputs |
| OUTELSE | Output | Binary numbers, integers, floating-point numbers, timers, CHAR, WCHAR, TOD, LTOD, DATE, LDT | I, Q, M, D, L | Output to which the input value (IN) is copied when K &gt; n. |

You can select the data type of the instruction from the "???" drop-down list.

For additional information on available data types, refer to "See also".

##### Example

The following example shows how the instruction works:

GRAPH

CALL DEMUX SINT_SINT

(K := "Tag_Number"

IN := "Tag_Value"

OUT0 =&gt; "Tag_Output_1"

OUT1 =&gt; "Tag_Output_2"

OUTELSE =&gt; "Tag_Output_3"

​ )

The following tables show how the instruction works using specific operand values:

Input values of the "Demultiplex" instruction before network execution:

| Parameter | Operand | Values |  |
| --- | --- | --- | --- |
| K | Tag_Number | 1 | 4 |
| IN | Tag_Value | DW#16#FFFFFFFF | DW#16#3E4A7D |

Output values of the "Demultiplex" instruction after network execution:

| Parameter | Operand | Values |  |
| --- | --- | --- | --- |
| OUT0 | Tag_Output_1 | Unchanged | Unchanged |
| OUT1 | Tag_Output_2 | DW#16#FFFFFFFF | Unchanged |
| OUTELSE | Tag_Output_3 | Unchanged | DW#16#3E4A7D |

Based on the value of the "Tag_Number" operand, the value of the IN input is copied to the corresponding output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Shift and Rotate (S7-1500)

This section contains information on the following topics:

- [SHR: Shift right (S7-1500)](#shr-shift-right-s7-1500)
- [SHL: Shift left (S7-1500)](#shl-shift-left-s7-1500)
- [ROR: Rotate right (S7-1500)](#ror-rotate-right-s7-1500)
- [ROL: Rotate left (S7-1500)](#rol-rotate-left-s7-1500)

#### SHR: Shift right (S7-1500)

##### Description

You use the "Shift right" instruction to shift the content of Operand1 to the right bitwise. You use Operand2 to specify the number of bit positions the specified value will be shifted.

If the value of Operand2 is "0", the value of Operand1 is copied to the result.

If the value of Operand2 is greater than the number of available bit positions, the value of Operand1 is shifted to the right by the available number of bit positions.

When unsigned values are shifted, the free bit positions in the left area of Operand1 are filled by zeroes. If the specified value has a sign, the free bit positions are filled with the signal state of the sign bit.

The following figure shows how the content of Operand1 of data type INT is shifted by four bit positions to the right:

![Description](images/51692652299_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Bit strings, integers | I, Q, M, D, L or constant | Value to be shifted |
| &lt;Operand2&gt; | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L or constant | Number of bit positions by which the value is shifted |
| &lt;Result&gt; | Output | Bit strings, integers | I, Q, M, D, L | Result of the instruction |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SHR_INT("Tag_InValue","Tag_Number")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 0011 1111 1010 1111 |
| Tag_Number | 3 |
| Tag_OutValue | 0000 0111 1111 0101 |

The content of the "Tag_InValue" operand is shifted three bit positions to the right. The result is output in the "Tag_OutValue" output.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SHL: Shift left (S7-1500)

##### Description

You use the "Shift left" instruction to shift the content of Operand1 to the left bitwise. You use Operand2 to specify the number of bit positions the specified value will be shifted.

If the value of Operand2 is "0", the value of Operand1 is copied to the result.

If the value of Operand2 is greater than the number of available bit positions, the value of Operand1 is shifted to the left by the available number of bit positions.

The bit positions in the right part of Operand1 freed by shifting are filled with zeros.

The following figure shows how the content of Operand1 of data type WORD is shifted by six bit positions to the left:

![Description](images/51693472267_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Bit strings, integers | I, Q, M, D, L or constant | Value to be shifted |
| &lt;Operand2&gt; | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L or constant | Number of bit positions by which the value is shifted |
| &lt;Result&gt; | Output | Bit strings, integers | I, Q, M, D, L | Result of the instruction |

You can select the data type of the instruction from the "???" drop-down list.

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := SHL_WORD("Tag_InValue","Tag_Number")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 0011 1111 1010 1111 |
| Tag_Number | 4 |
| Tag_OutValue | 1111 1010 1111 0000 |

The content of the "Tag_InValue" operand is shifted four bit positions to the left and output as the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ROR: Rotate right (S7-1500)

##### Description

You use the "Rotate right" instruction to rotate the content of Operand1 to the right bitwise. You use Operand2 to specify the number of bit positions the specified value will be rotated.

If the value of Operand2 is "0", the value of Operand1 is copied to the result.

If the value of Operand2 is greater than the number of available bit positions, the value of Operand1 is rotated by the specified number of bit positions.

The bit positions freed by rotating are filled with the bit positions that are pushed out.

The following figure shows how the content of an operand of data type DWORD is rotated three bit positions to the right:

![Description](images/51693753611_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Bit strings, integers | I, Q, M, D, L or constant | Value to be rotated |
| &lt;Operand2&gt; | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L or constant | Number of bit positions by which the value is rotated |
| &lt;Result&gt; | Output | Bit strings, integers | I, Q, M, D, L | Result of the instruction |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ROR("Tag_InValue","Tag_Number")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 1010 1010 0000 1111 0000 1111 0101 0101 |
| Tag_Number | 5 |
| Tag_OutValue | 1010 1101 0101 0000 0111 1000 0111 1010 |

The content of the "Tag_InValue" operand is rotated five bit positions to the right and output as the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### ROL: Rotate left (S7-1500)

##### Description

You use the "Rotate left" instruction to rotate the content of Operand1 to the left bitwise. You use Operand2 to specify the number of bit positions the specified value will be rotated.

If the value of Operand2 is "0", the value of Operand1 is copied to the result.

If the value of Operand2 is greater than the number of available bit positions, the value of Operand1 is rotated by the specified number of bit positions.

The bit positions freed by rotating are filled with the bit positions that are pushed out.

The following figure shows how the content of an operand of data type DWORD is rotated three bit positions to the left:

![Description](images/51693945355_DV_resource.Stream@PNG-en-US.png)

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Bit strings, integers | I, Q, M, D, L or constant | Value to be rotated |
| &lt;Operand2&gt; | Input | USINT, UINT, UDINT, ULINT | I, Q, M, D, L or constant | Number of bit positions by which the value is rotated |
| &lt;Result&gt; | Output | Bit strings, integers | I, Q, M, D, L | Result of the instruction |

You can find additional information on valid data types under "See also".

##### Example

The following example shows how the instruction works:

GRAPH

"Tag_OutValue" := ROL("Tag_InValue","Tag_Number")

The following table shows how the instruction works using specific operand values:

| Operand | Value |
| --- | --- |
| Tag_InValue | 1111 0000 1010 1010 0000 1111 0000 1111 |
| Tag_Number | 5 |
| Tag_OutValue | 0001 0101 0100 0001 1110 0001 1111 1110 |

The content of the "Tag_InValue" operand is rotated five bit positions to the left and output as the result in the "Tag_OutValue" operand.

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### Legacy (S7-1500)

This section contains information on the following topics:

- [DRUM: Implement sequencer (S7-1500)](#drum-implement-sequencer-s7-1500)
- [DCAT: Discrete control-timer alarm (S7-1500)](#dcat-discrete-control-timer-alarm-s7-1500)
- [MCAT: Motor control-timer alarm (S7-1500)](#mcat-motor-control-timer-alarm-s7-1500)
- [IMC: Compare input bits with the bits of a mask (S7-1500)](#imc-compare-input-bits-with-the-bits-of-a-mask-s7-1500)
- [SMC: Compare scan matrix (S7-1500)](#smc-compare-scan-matrix-s7-1500)
- [LEAD_LAG: Lead and lag algorithm (S7-1500)](#lead_lag-lead-and-lag-algorithm-s7-1500)
- [SEG: Create bit pattern for seven-segment display (S7-1500)](#seg-create-bit-pattern-for-seven-segment-display-s7-1500)
- [BCDCPL: Create tens complement (S7-1500)](#bcdcpl-create-tens-complement-s7-1500)
- [BITSUM: Count number of set bits (S7-1500)](#bitsum-count-number-of-set-bits-s7-1500)

#### DRUM: Implement sequencer (S7-1500)

##### Description

You use the "Implement sequencer" instruction to assign the programmed output bits (OUT1 to OUT16) and the output word (OUT_WORD) with the programmed values of the OUT_VAL parameter of the relevant step. The specific step must thereby satisfy the conditions of the programmed enable mask on the S_MASK parameter while the instruction remains at this step. The instruction advances to the next step if the event for the step is true and the programmed time for the current step elapses, or if the value at the JOG parameter changes from "0" to "1". The instruction is reset when the signal state of the RESET parameter changes to "1". The current step is hereby equated to the preset step (DSP).

The amount of time spent on a step is determined by the product of the preset timebase (DTBP) and the preset counter value (S_PRESET) for each step. At the start of a new step, this calculated value is loaded into the DCC parameter, which contains the time remaining for the current step. If, for example the value at the DTBP parameter is "2" and the preset value for the first step is "100" (100 ms), the DCC parameter has the value "200" (200 ms).

A step can be programmed with a timer value, an event, or both. Steps that have an event bit and the timer value "0" advance to the next step as soon as the signal state of the event bit is "1". Steps that are programmed only with a timer value start the time immediately. Steps that are programmed with an event bit and a time value greater than "0" start the time when the signal state of the event bit is "1". The event bits are initialized with a signal state of "1".

When the sequencer is on the last programmed step (LST_STEP) and the time for this step has expired, the signal state on the Q parameter is set to "1"; otherwise it is set to "0". When the Q parameter is set, the instruction remains on the step until it is reset.

In the configurable mask (S_MASK) you can select the individual bits in the output word (OUT_WORD) and set or reset the output bits (OUT1 to OUT16) by means of the output values (OUT_VAL). When a bit of the configurable mask has a signal state of "1", the OUT_VAL value sets/resets the corresponding bit. If the signal state of a bit of the configurable mask is "0", the corresponding bit is left unchanged. All the bits of the configurable mask for all 16 steps are initialized with a signal state of "1".

The output bit on the OUT1 parameter corresponds to the least significant bit of the output word (OUT_WORD). The output bit on the OUT16 parameter corresponds to the most significant bit of the output word (OUT_WORD).

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| RESET | Input | BOOL | I, Q, M, D, L or constant | The signal state "1" indicates a reset condition. |
| JOG | Input | BOOL | I, Q, M, D, L or constant | When the signal state changes from "0" to "1", the instruction advances to the next step. |
| DRUM_EN | Input | BOOL | I, Q, M, D, L or constant | The signal state "1" allows the sequencer to advance based on the event and time criteria. |
| LST_STEP | Input | BYTE | I, Q, M, D, L or constant | Maximum step number (for example: LST_STEP = 16#08; a maximum of 8 steps is possible.) |
| EVENT(i)  1 ≤ i ≤ 16 | Input | BOOL | I, Q, M, D, L or constant | Event bit (i);  Initial signal state is "1". |
| OUT(j),  1 ≤ j ≤ 16 | Output | BOOL | I, Q, M, D, L | Output bit (j) |
| Q | Output | BOOL | I, Q, M, D, L | The signal state "1" indicates that the time for the last step has elapsed. |
| OUT_WORD | Output | WORD | I, Q, M, D, L, P | Word address to which the sequencer writes the output values. |
| ERR_CODE | Output | WORD | I, Q, M, D, L, P | Error information |
| JOG_HIS | Static | BOOL | I, Q, M, D, L or constant | JOG parameter history bit |
| EOD | Static | BOOL | I, Q, M, D, L or constant | The signal state "1" indicates that the time for the last step has elapsed. |
| DSP | Static | BYTE | I, Q, M, D, L, P or constant | Preset first step of the sequencer (1 to 16) |
| DSC | Static | BYTE | I, Q, M, D, L, P or constant | Current step of the sequencer |
| DCC | Static | DWORD | I, Q, M, D, L, P or constant | Remaining processing time for the current step |
| DTBP | Static | WORD | I, Q, M, D, L, P or constant | Preset timebase of the sequencer |
| PrevTime | Static | TIME | I, Q, M, D, L or constant | System time of the previous call |
| S_PRESET | Static | ARRAY[1..16] of WORD | I, Q, M, D, L or constant | Preset counter value for each step [1 to 16] where one clock pulse = 1 ms. |
| OUT_VAL | Static | ARRAY[1..16, 0..15] of BOOL | I, Q, M, D, L or constant | Output values for each step [1 to 16, 0 to 15]. |
| S_MASK | Static | ARRAY[1..16, 0..15] of BOOL | I, Q, M, D, L or constant | Configurable mask for each step [1 to 16, 0 to 15]. Initial signal states are "1". |

##### Parameter ERR_CODE

The following table shows the meaning of the values of the ERR_CODE parameter:

| ERR_CODE* | Explanation |
| --- | --- |
| W#16#0000 | No error |
| W#16#000B | The value at the LST_STEP parameter is less than 1 or greater than 16. |
| W#16#000C | The value at the DSC parameter is less than 1 or greater than the value at the LST_STEP parameter. |
| W#16#000D | The value at the DSP parameter is less than 1 or greater than the value at the LST_STEP parameter. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Example

In the following example the instruction advances from step 1 to step 2. The output bits (OUT1 to OUT16) and the output word (OUT_WORD) are set according to the mask configured for step 2 and the values of the OUT_VAL parameter.

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL DRUM, "DRUM_DB"

(RESET := "Tag_Reset"

JOG := "Tag_Input_Jog"

DRUM_EN := "Tag_Input_Drum_EN"

LST_STEP := "Tag_Number_LastStep"

EVENTn := "MyTag_Event_n"

OUTn =&gt; "MyTag_Output_n"

Q =&gt; "Tag_Output_Q"

OUT_WORD =&gt; "Tag_OutputWord"

ERR_CODE =&gt; "Tag_ErrorCode"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for initializing the input parameters:

| Parameter | Operand | Address | Value |
| --- | --- | --- | --- |
| RESET | Tag_Reset | M0.0 | FALSE |
| JOG | Tag_Input_JOG | M0.1 | FALSE |
| DRUM_EN | Tag_Input_Drum_EN | M0.2 | TRUE |
| LST_STEP | Tag_Number_LastStep | MB1 | B#16#08 |
| EVENT2 | MyTag_Event_2 | M20.0 | FALSE |
| EVENT4 | MyTag_Event_4 | M20.1 | FALSE |
| EVENT6 | MyTag_Event_6 | M20.2 | FALSE |
| EVENT8 | MyTag_Event_8 | M20.3 | FALSE |
| EVENT10 | MyTag_Event_10 | M20.4 | FALSE |
| EVENT12 | MyTag_Event_12 | M20.5 | FALSE |
| EVENT14 | MyTag_Event_14 | M20.6 | FALSE |
| EVENT16 | MyTag_Event_16 | M20.7 | FALSE |

The following values are saved in the "DRUM_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| JOG_HIS | DBX12.0 | FALSE |
| EOD | DBX12.1 | FALSE |
| DSP | DBB13 | W#16#0001 |
| DSC | DBB14 | W#16#0001 |
| DCC | DBD16 | DW#16#0000000A |
| DTBP | DBW20 | W#16#0001 |
| S_PRESET[1] | DBW26 | W#16#0064 |
| S_PRESET[2] | DBW28 | W#16#00C8 |
| OUT_VAL[1,0] | DBX58.0 | TRUE |
| OUT_VAL[1,1] | DBX58.1 | TRUE |
| OUT_VAL[1,2] | DBX58.2 | TRUE |
| OUT_VAL[1,3] | DBX58.3 | TRUE |
| OUT_VAL[1,4] | DBX58.4 | TRUE |
| OUT_VAL[1,5] | DBX58.5 | TRUE |
| OUT_VAL[1,6] | DBX58.6 | TRUE |
| OUT_VAL[1,7] | DBX58.7 | TRUE |
| OUT_VAL[1,8] | DBX59.0 | TRUE |
| OUT_VAL[1,9] | DBX59.1 | TRUE |
| OUT_VAL[1,10] | DBX59.2 | TRUE |
| OUT_VAL[1,11] | DBX59.3 | TRUE |
| OUT_VAL[1,12] | DBX59.4 | TRUE |
| OUT_VAL[1,13] | DBX59.5 | TRUE |
| OUT_VAL[1,14] | DBX59.6 | TRUE |
| OUT_VAL[1,15] | DBX59.7 | TRUE |
| OUT_VAL[2,0] | DBX60.0 | FALSE |
| OUT_VAL[2,1] | DBX60.1 | FALSE |
| OUT_VAL[2,2] | DBX60.2 | FALSE |
| OUT_VAL[2,3] | DBX60.3 | FALSE |
| OUT_VAL[2,4] | DBX60.4 | FALSE |
| OUT_VAL[2,5] | DBX60.5 | FALSE |
| OUT_VAL[2,6] | DBX60.6 | FALSE |
| OUT_VAL[2,7] | DBX60.7 | FALSE |
| OUT_VAL[2,8] | DBX61.0 | FALSE |
| OUT_VAL[2,9] | DBX61.1 | FALSE |
| OUT_VAL[2,10] | DBX61.2 | FALSE |
| OUT_VAL[2,11] | DBX61.3 | FALSE |
| OUT_VAL[2,12] | DBX61.4 | FALSE |
| OUT_VAL[2,13] | DBX61.5 | FALSE |
| OUT_VAL[2,14] | DBX61.6 | FALSE |
| OUT_VAL[2,15] | DBX61.7 | FALSE |
| S_MASK[2,0] | DBX92.0 | FALSE |
| S_MASK[2,1] | DBX92.1 | TRUE |
| S_MASK[2,2] | DBX92.2 | TRUE |
| S_MASK[2,3] | DBX92.3 | TRUE |
| S_MASK[2,4] | DBX92.4 | TRUE |
| S_MASK[2,5] | DBX92.5 | FALSE |
| S_MASK[2,6] | DBX92.6 | TRUE |
| S_MASK[2,7] | DBX92.7 | TRUE |
| S_MASK[2,8] | DBX93.0 | FALSE |
| S_MASK[2,9] | DBX93.1 | FALSE |
| S_MASK[2,10] | DBX93.2 | TRUE |
| S_MASK[2,11] | DBX93.3 | TRUE |
| S_MASK[2,12] | DBX93.4 | TRUE |
| S_MASK[2,13] | DBX93.5 | TRUE |
| S_MASK[2,14] | DBX93.6 | FALSE |
| S_MASK[2,15] | DBX93.7 | TRUE |

The output parameters are set to the following values before the execution of the instruction:

| Parameter | Operand | Address | Value |
| --- | --- | --- | --- |
| Q | Tag_Output_Q | M6.0 | FALSE |
| OUTWORD | Tag_OutputWord | MW8 | W#16#FFFF |
| OUT1 | MyTag_Output_1 | M4.0 | TRUE |
| OUT2 | MyTag_Output_2 | M4.1 | TRUE |
| OUT3 | MyTag_Output_3 | M4.2 | TRUE |
| OUT4 | MyTag_Output_4 | M4.3 | TRUE |
| OUT5 | MyTag_Output_5 | M4.4 | TRUE |
| OUT6 | MyTag_Output_6 | M4.5 | TRUE |
| OUT7 | MyTag_Output_7 | M4.6 | TRUE |
| OUT8 | MyTag_Output_8 | M4.7 | TRUE |
| OUT9 | MyTag_Output_9 | M5.0 | TRUE |
| OUT10 | MyTag_Output_10 | M5.1 | TRUE |
| OUT11 | MyTag_Output_11 | M5.2 | TRUE |
| OUT12 | MyTag_Output_12 | M5.3 | TRUE |
| OUT13 | MyTag_Output_13 | M5.4 | TRUE |
| OUT14 | MyTag_Output_14 | M5.5 | TRUE |
| OUT15 | MyTag_Output_15 | M5.6 | TRUE |
| OUT16 | MyTag_Output_16 | M5.7 | TRUE |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Address | Value |
| --- | --- | --- | --- |
| OUT1 | MyTag_Output_1 | M4.0 | TRUE |
| OUT2 | MyTag_Output_2 | M4.1 | FALSE |
| OUT3 | MyTag_Output_3 | M4.2 | FALSE |
| OUT4 | MyTag_Output_4 | M4.3 | FALSE |
| OUT5 | MyTag_Output_5 | M4.4 | FALSE |
| OUT6 | MyTag_Output_6 | M4.5 | TRUE |
| OUT7 | MyTag_Output_7 | M4.6 | FALSE |
| OUT8 | MyTag_Output_8 | M4.7 | FALSE |
| OUT9 | MyTag_Output_9 | M5.0 | TRUE |
| OUT10 | MyTag_Output_10 | M5.1 | TRUE |
| OUT11 | MyTag_Output_11 | M5.2 | FALSE |
| OUT12 | MyTag_Output_12 | M5.3 | FALSE |
| OUT13 | MyTag_Output_13 | M5.4 | FALSE |
| OUT14 | MyTag_Output_14 | M5.5 | FALSE |
| OUT15 | MyTag_Output_15 | M5.6 | TRUE |
| OUT16 | MyTag_Output_16 | M5.7 | FALSE |
| Q | Tag_Output_Q | M6.0 | FALSE |
| OUTWORD | Tag_OutputWord | MW8 | W#16#4321 |
| ERR_CODE | Tag_ErrorCode | MW10 | W#16#0000 |

The following values are saved in the "DRUM_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| JOG_HIS | DBX12.0 | FALSE |
| EOD | DBX12.1 | FALSE |
| DSC | DBB14 | W#16#0002 |
| DCC | DBD16 | DW#16#000000C8 |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### DCAT: Discrete control-timer alarm (S7-1500)

##### Description

You can use the "Discrete control-timer alarm" instruction to accumulate the time from the point at which theCMD parameter issues the command to open or close. The time is accumulated until the preset time (PT) is exceeded or the information is received that the device was opened or closed (O_FB or C_FB) within the specified time. If the preset time is exceeded before the information on the opening or closing of the device is received, the corresponding alarm is activated. If the signal state of the command input changes before the preset time, the time is restarted.

The "Discrete control-timer alarm" instruction has the following reactions to the input conditions:

- When the signal state of the CMD parameter changes from "0" to "1", the signal states of the parameters Q, CMD_HIS, ET (only if ET is &lt; PT) OA and CA are influenced as follows:

  - The Q and CMD_HIS parameters are set to "1".
  - The ET, OA, and CA parameters are reset to "0".
- When the signal state at the parameter CMD changes from "1" to "0", the parameters Q, ET (only if ET &lt; PT), OA, CA and CMD_HIS are reset to "0".
- When the signal state at the CMD and CMD_HIS parameters is "1" and the O_FB parameter is set to "0", the time difference (ms) since the last execution of the instruction is added to the value of the parameter ET. If the value of the ET parameter exceeds the value of the PT parameter, the signal state at the OA parameter is set to "1". If the value of the ET parameter does not exceed the value of the PT parameter, the signal state of the OA parameter is reset to "0". The value at the CMD_HIS parameter is reset to the value of the CMD parameter.
- If the signal state of the CMD, CMD_HIS, and O_FB parameters is set to "1" and the C_FB parameter has the value "0", the signal state of the OA parameter is set to "0". The value of the ET parameter is set to the value of the PT parameter. If the signal state of the O_FB parameter changes to "0", the alarm is set the next time the instruction is executed. The value of the CMD_HIS parameter is set to the value of the CMD parameter.
- If the CMD, CMD_HIS, and C_FB parameters have the value "0", the time difference (ms) since the last execution of the instruction is added to the value of the ET parameter. If the value of the ET parameter exceeds the value of the PT parameter, the signal state of the CA parameter is reset to "1". If the value at the PT parameter is not exceeded, the CA parameter has the signal state "0". The value of the CMD_HIS parameter is set to the value of the CMD parameter.
- If the CMD, CMD_HIS, and O_FB parameters have the signal state "0" and the C_FB parameter is set to "1", the CA parameter is set to "0". The value of the ET parameter is set to the value of the PT parameter. If the signal state of the C_FB parameter changes to "0", the alarm is set the next time the instruction is executed. The value of the CMD_HIS parameter is set to the value of the CMD parameter.
- If the parameters O_FB and C_FB simultaneously have the signal state "1", the signal states of both alarm outputs are set to "1".

The "Discrete control-timer alarm" instruction supplies no error information.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CMD | Input | BOOL | I, Q, M, D, L or constant | The signal state "0" indicates the "close" command.  The signal state "1" indicates the "open" command. |
| O_FB | Input | BOOL | I, Q, M, D, L or constant | Feedback input when opening |
| C_FB | Input | BOOL | I, Q, M, D, L or constant | Feedback input when closing |
| Q | Output | BOOL | I, Q, M, D, L | Shows the status of the CMD parameter |
| OA | Output | BOOL | I, Q, M, D, L | Alarm output when opening |
| CA | Output | BOOL | I, Q, M, D, L | Alarm output when closing |
| ET | Static | DINT | D, L or constant | Currently elapsed time, where one clock pulse = 1 ms. |
| PT | Static | DINT | D, L or constant | Preset timer value, where one clock pulse = 1 ms. |
| PREV_TIME | Static | DWORD | D, L or constant | Previous system time |
| CMD_HIS | Static | BOOL | D, L or constant | CMD history bit |

##### Example

In the following example, the CMD parameter changes from "0" to "1". After the execution of the instruction, the Q parameter is set to "1" and the two alarm outputs OA and CA have the signal state "0". The CMD_HIS parameter of the instance data block is set to the signal state "1" and the ET parameter is reset to "0".

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL DCAT, "DCAT_DB"

(CMD := "Tag_Input_CMD"

O_FB := "Tag_Input_O_FB"

C_FB := "Tag_Input_C_FB"

Q =&gt; "Tag_Output_Q"

OA =&gt; "Tag_Output_OA"

CA =&gt; "Tag_Output_CA"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for the input and output parameters:

| Parameter | Operand | Value |
| --- | --- | --- |
| CMD | Tag_Input_CMD | TRUE |
| O_FB | Tag_Input_O_FB | FALSE |
| C_FB | Tag_Input_C_FB | FALSE |
| Q | Tag_Output_Q | FALSE |
| OA | Tag_Output_OA | FALSE |
| CA | Tag_Output_CA | FALSE |

The following values are saved in the "DCAT_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| ET | DBD4 | L#12 |
| PT | DBD8 | L#222 |
| CMD_HIS | DBX16.0 | FALSE |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Value |
| --- | --- | --- |
| Q | Tag_Output_Q | TRUE |
| OA | Tag_Output_OA | FALSE |
| CA | Tag_Output_CA | FALSE |

The following values are saved in the "DCAT_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| ET | DBD4 | L#0 |
| CMD_HIS | DBX16.0 | TRUE |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### MCAT: Motor control-timer alarm (S7-1500)

##### Description

You use the "Motor control-timer alarm" instruction to accumulate the time from the point at which one of the command inputs (open or close) is activated. The time is accumulated until the preset time is exceeded or the relevant feedback input indicates that the device has executed the requested operation within the specified time. If the preset time is exceeded before the feedback is received, the corresponding alarm is triggered.

##### Execution of the "Motor control-timer alarm" instruction

The following table shows the reactions of the "Motor control-timer alarm" instruction to the various input conditions:

| Input parameters |  |  |  |  |  |  |  |  | Output parameters |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ET | O_HIS | C_HIS |  | O_CMD | C_CMD | S_CMD | O_FB | C_FB | OO | CO | OA | CA | ET | O_HIS | C_HIS | Q | Status |
| X | 1 | 1 |  | X | X | X | X | X | 0 | 0 | 1 | 1 | PT | 0 | 0 | 0 | Alarm |
| X | X | X |  | X | X | X | 1 | 1 | 0 | 0 | 1 | 1 | PT | 0 | 0 | 0 | Alarm |
| X | X | X |  | X | X | 1 | X | X | 0 | 0 | 0 | 0 | X | 0 | 0 | 1 | Stop |
| X | X | X |  | 1 | 1 | X | X | X | 0 | 0 | 0 | 0 | X | 0 | 0 | 1 | Stop |
| X | 0 | X |  | 1 | 0 | 0 | X | X | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | Start opening |
| &lt;PT | 1 | 0 |  | X | 0 | 0 | 0 | X | 1 | 0 | 0 | 0 | INC | 1 | 0 | 1 | Open |
| X | 1 | 0 |  | X | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | PT | 1 | 0 | 1 | Opened |
| &gt;=PT | 1 | 0 |  | X | 0 | 0 | 0 | X | 0 | 0 | 1 | 0 | PT | 1 | 0 | 0 | Opening alarm |
| X | X | 0 |  | 0 | 1 | 0 | X | X | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | Start closing |
| &lt;PT | 0 | 1 |  | 0 | X | 0 | X | 0 | 0 | 1 | 0 | 0 | INC | 0 | 1 | 1 | Close |
| X | 0 | 1 |  | 0 | X | 0 | 0 | 1 | 0 | 0 | 0 | 0 | PT | 0 | 1 | 1 | Closed |
| &gt;=PT | 0 | 1 |  | 0 | X | 0 | X | 0 | 0 | 0 | 0 | 1 | PT | 0 | 1 | 0 | Closing alarm |
| X | 0 | 0 |  | 0 | 0 | 0 | X | X | 0 | 0 | 0 | 0 | X | 0 | 0 | 1 | Stopped |
| Legend: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| INC |  |  | Add the time difference (ms) since the last processing of the FB to ET |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PT |  |  | PT is set to the same value as ET |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| X |  |  | Cannot be used |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| &lt;PT |  |  | ET &lt; PT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| &gt;=PT |  |  | ET &gt;= PT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| If the input parameters O_HIS and C_HIS both have the signal state "1", they are immediately set to signal state "0". In this case, the last row in the table (X) mentioned above is valid. Because it is therefore not possible to check whether the input parameters O_HIS and C_HIS have the signal state "1", the output parameters are set as follows in this case:   OO = FALSE  CO = FALSE  OA = FALSE  CA = FALSE  ET = PT  Q = TRUE |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| O_CMD | Input | BOOL | I, Q, M, D, L or constant | "Open" command input |
| C_CMD | Input | BOOL | I, Q, M, D, L or constant | "Close" command input |
| S_CMD | Input | BOOL | I, Q, M, D, L or constant | "Stop" command input |
| O_FB | Input | BOOL | I, Q, M, D, L or constant | Feedback input when opening |
| C_FB | Input | BOOL | I, Q, M, D, L or constant | Feedback input when closing |
| OO | Output | BOOL | I, Q, M, D, L | "Open" output |
| CO | Output | BOOL | I, Q, M, D, L | "Close" output |
| OA | Output | BOOL | I, Q, M, D, L | Alarm output when opening |
| CA | Output | BOOL | I, Q, M, D, L | Alarm output when closing |
| Q | Output | BOOL | I, Q, M, D, L | The signal state "0" indicates an error condition |
| ET | Static | DINT | D, L or constant | Currently elapsed time, where one clock pulse = 1 ms |
| PT | Static | DINT | D, L or constant | Preset timer value, where one clock pulse = 1 ms |
| PREV_TIME | Static | DWORD | D, L or constant | Previous system time |
| O_HIS | Static | BOOL | D, L or constant | "Open" history bit |
| C_HIS | Static | BOOL | D, L or constant | "Close" history bit |

##### Example

The following example shows how the instruction works:

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL MCAT, "MCAT_DB"

(O_CMD := "Tag_Input_O_CMD"

C_CMD := "Tag_Input_C_CMD"

S_CMD := "Tag_Input_S_CMD"

O_FB := "Tag_Input_O_FB"

C_FB := "Tag_Input_C_FB"

OO =&gt; "Tag_OutputOpen"

​CO =&gt; "Tag_OutputClosed"

OA =&gt; "Tag_Output_OA"

CA =&gt; "Tag_Output_CA"

Q =&gt; "Tag_Output_Q"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for the input and output parameters:

| Parameter | Operand | Value |
| --- | --- | --- |
| O_CMD | Tag_Input_O_CMD | TRUE |
| C_CMD | Tag_Input_C_CMD | FALSE |
| S_CMD | Tag_Input_S_CMD | FALSE |
| O_FB | Tag_Input_O_FB | FALSE |
| C_FB | Tag_Input_C_FB | FALSE |
| OO | Tag_OutputOpen | FALSE |
| CO | Tag_OutputClosed | FALSE |
| OA | Tag_Output_OA | FALSE |
| CA | Tag_Output_CA | FALSE |
| Q | Tag_Output_Q | FALSE |

The following values are saved in the "MCAT_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| ET | DBD4 | L#2 |
| PT | DBD8 | L#22 |
| O_HIS | DBX16.0 | TRUE |
| C_HIS | DBX16.1 | FALSE |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Value |
| --- | --- | --- |
| OO | Tag_OutputOpen | TRUE |
| CO | Tag_OutputClosed | FALSE |
| OA | Tag_Output_OA | FALSE |
| CA | Tag_Output_CA | FALSE |
| Q | Tag_Output_Q | TRUE |

The following values are saved in the "MCAT_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| ET | DBD4 | L#0 |
| O_HIS | DBX16.0 | TRUE |
| CMD_HIS | DBX16.1 | FALSE |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### IMC: Compare input bits with the bits of a mask (S7-1500)

##### Description

You use the "Compare input bits with the bits of a mask" instruction to compare the signal state of up to 16 programmed input bits (IN_BIT0 to IN_BIT15) with the corresponding bits of a mask. Up to 16 steps with masks can be programmed. The value of the IN_BIT0 parameter is compared with the value of the CMP_VAL[x,0] mask, where "x" indicates the step number. In the CMP_STEP parameter, you specify the step number of the mask that is used for the comparison. All programmed values are compared in the same manner. Unprogrammed input bits or unprogrammed bits of the mask have the default signal state FALSE.

If a match is found in the comparison, the signal state of the OUT parameter is set to "1". Otherwise, the OUT parameter is set to "0".

If the value of the CMP_STEP parameter is greater than 15, the instruction is not executed. An error message is output at the ERR_CODE parameter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN_BIT0 | Input | BOOL | I, Q, M, D, L or constant | Input bit 0 is compared with bit 0 of the mask. |
| IN_BIT1 | Input | BOOL | I, Q, M, D, L or constant | Input bit 1 is compared with bit 1 of the mask. |
| IN_BIT2 | Input | BOOL | I, Q, M, D, L or constant | Input bit 2 is compared with bit 2 of the mask. |
| IN_BIT3 | Input | BOOL | I, Q, M, D, L or constant | Input bit 3 is compared with bit 3 of the mask. |
| IN_BIT4 | Input | BOOL | I, Q, M, D, L or constant | Input bit 4 is compared with bit 4 of the mask. |
| IN_BIT5 | Input | BOOL | I, Q, M, D, L or constant | Input bit 5 is compared with bit 5 of the mask. |
| IN_BIT6 | Input | BOOL | I, Q, M, D, L or constant | Input bit 6 is compared with bit 6 of the mask. |
| IN_BIT7 | Input | BOOL | I, Q, M, D, L or constant | Input bit 7 is compared with bit 7 of the mask. |
| IN_BIT8 | Input | BOOL | I, Q, M, D, L or constant | Input bit 8 is compared with bit 8 of the mask. |
| IN_BIT9 | Input | BOOL | I, Q, M, D, L or constant | Input bit 9 is compared with bit 9 of the mask. |
| IN_BIT10 | Input | BOOL | I, Q, M, D, L or constant | Input bit 10 is compared with bit 10 of the mask. |
| IN_BIT11 | Input | BOOL | I, Q, M, D, L or constant | Input bit 11 is compared with bit 11 of the mask. |
| IN_BIT12 | Input | BOOL | I, Q, M, D, L or constant | Input bit 12 is compared with bit 12 of the mask. |
| IN_BIT13 | Input | BOOL | I, Q, M, D, L or constant | Input bit 13 is compared with bit 13 of the mask. |
| IN_BIT14 | Input | BOOL | I, Q, M, D, L or constant | Input bit 14 is compared with bit 14 of the mask. |
| IN_BIT15 | Input | BOOL | I, Q, M, D, L or constant | Input bit 15 is compared with bit 15 of the mask. |
| CMP_STEP | Input | BYTE | I, Q, M, D, L, P or constant | The step number of the mask used for the comparison. |
| OUT | Output | BOOL | I, Q, M, D, L | The signal state "1" indicates that a match was found.  The signal state "0" indicates that no match was found. |
| ERR_CODE | Output | WORD | I, Q, M, D, L, P | Error information |
| CMP_VAL | Static | ARRAY OF WORD | I, Q, M, D, L or constant | Comparison masks [0 to 15, 0 to 15]: The first number of the index is the step number and the second number is the bit number of the mask. |

##### Parameter ERR_CODE

The following table shows the meaning of the values of the ERR_CODE parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 000A | The value at the CMP_STEP parameter is greater than 15. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Example

In the following example all 16 input bits are compared with the mask for step 2. The signal state of the OUT parameter is set to TRUE, since the input bits match the mask for step 2.

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL IMC, "IMC_DB"

(IN_BIT0 - 15 := "Tag_Input_BITn"

CMP_STEP := "Tag_CMP_STEP"

OUT =&gt; "Tag_Output"

ERR_CODE =&gt; "Tag_ErrorCode"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for the input and output parameters:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN_BIT0 | Tag_Input_BIT0 | TRUE |
| IN_BIT1 | Tag_Input_BIT1 | TRUE |
| IN_BIT2 | Tag_Input_BIT2 | FALSE |
| IN_BIT3 | Tag_Input_BIT3 | TRUE |
| IN_BIT4 | Tag_Input_BIT4 | TRUE |
| IN_BIT5 | Tag_Input_BIT5 | FALSE |
| IN_BIT6 | Tag_Input_BIT6 | TRUE |
| IN_BIT7 | Tag_Input_BIT7 | TRUE |
| IN_BIT8 | Tag_Input_BIT8 | FALSE |
| IN_BIT9 | Tag_Input_BIT9 | TRUE |
| IN_BIT10 | Tag_Input_BIT10 | TRUE |
| IN_BIT11 | Tag_Input_BIT11 | FALSE |
| IN_BIT12 | Tag_Input_BIT12 | TRUE |
| IN_BIT13 | Tag_Input_BIT13 | TRUE |
| IN_BIT14 | Tag_Input_BIT14 | FALSE |
| IN_BIT15 | Tag_Input_BIT15 | TRUE |
| CMP_STEP | Tag_CMP_STEP | B#16#02 |
| OUT | Tag_Output | FALSE |
| ERR_CODE | Tag_ErrorCode | W#16#0000 |

The following values for the mask of step 2 are saved in the "IMC_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| CMP_VAL [2,0] | DBX12.0 | TRUE |
| CMP_VAL [2,1] | DBX12.1 | TRUE |
| CMP_VAL [2,2] | DBX12.2 | FALSE |
| CMP_VAL [2,3] | DBX12.3 | TRUE |
| CMP_VAL [2,4] | DBX12.4 | TRUE |
| CMP_VAL [2,5] | DBX12.5 | FALSE |
| CMP_VAL [2,6] | DBX12.6 | TRUE |
| CMP_VAL [2,7] | DBX12.7 | TRUE |
| CMP_VAL [2,8] | DBX13.0 | FALSE |
| CMP_VAL [2,0] | DBX13.1 | TRUE |
| CMP_VAL [2,10] | DBX13.2 | TRUE |
| CMP_VAL [2,11] | DBX13.3 | FALSE |
| CMP_VAL [2,12] | DBX13.4 | TRUE |
| CMP_VAL [2,13] | DBX13.5 | TRUE |
| CMP_VAL [2,14] | DBX13.6 | FALSE |
| CMP_VAL [2,15] | DBX13.7 | TRUE |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Value |
| --- | --- | --- |
| OUT | Tag_Output | TRUE |
| ERR_CODE | Tag_ErrorCode | W#16#0000 |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SMC: Compare scan matrix (S7-1500)

##### Description

You use the "Compare scan matrix" instruction to compare the signal state of up to 16 programmed input bits (IN_BIT0 to IN_BIT15) with the corresponding bit of the comparison masks for each step. Processing starts at step 1 and is continued until the last programmed step (LAST) or until a match is found. The input bit of the IN_BIT0 parameter is compared with the value of the CMP_VAL[x,0] mask, where "x" indicates the step number. All programmed values are compared in the same manner. If a match is found the signal state of the OUT parameter is set to "1" and the step number with the matching mask is written in the OUT_STEP parameter. Unprogrammed input bits or unprogrammed bits of the mask have the default signal state FALSE. If more than one step has a matching mask, only the first one found is indicated in the OUT_STEP parameter. If no match is found, the signal state of the OUT parameter is set to "0". In this case the value at the OUT_STEP parameter is greater by "1" than the value at the LAST parameter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN_BIT0 | Input | BOOL | I, Q, M, D, L or constant | Input bit 0 is compared with bit 0 of the mask. |
| IN_BIT1 | Input | BOOL | I, Q, M, D, L or constant | Input bit 1 is compared with bit 1 of the mask. |
| IN_BIT2 | Input | BOOL | I, Q, M, D, L or constant | Input bit 2 is compared with bit 2 of the mask. |
| IN_BIT3 | Input | BOOL | I, Q, M, D, L or constant | Input bit 3 is compared with bit 3 of the mask. |
| IN_BIT4 | Input | BOOL | I, Q, M, D, L or constant | Input bit 4 is compared with bit 4 of the mask. |
| IN_BIT5 | Input | BOOL | I, Q, M, D, L or constant | Input bit 5 is compared with bit 5 of the mask. |
| IN_BIT6 | Input | BOOL | I, Q, M, D, L or constant | Input bit 6 is compared with bit 6 of the mask. |
| IN_BIT7 | Input | BOOL | I, Q, M, D, L or constant | Input bit 7 is compared with bit 7 of the mask. |
| IN_BIT8 | Input | BOOL | I, Q, M, D, L or constant | Input bit 8 is compared with bit 8 of the mask. |
| IN_BIT9 | Input | BOOL | I, Q, M, D, L or constant | Input bit 9 is compared with bit 9 of the mask. |
| IN_BIT10 | Input | BOOL | I, Q, M, D, L or constant | Input bit 10 is compared with bit 10 of the mask. |
| IN_BIT11 | Input | BOOL | I, Q, M, D, L or constant | Input bit 11 is compared with bit 11 of the mask. |
| IN_BIT12 | Input | BOOL | I, Q, M, D, L or constant | Input bit 12 is compared with bit 12 of the mask. |
| IN_BIT13 | Input | BOOL | I, Q, M, D, L or constant | Input bit 13 is compared with bit 13 of the mask. |
| IN_BIT14 | Input | BOOL | I, Q, M, D, L or constant | Input bit 14 is compared with bit 14 of the mask. |
| IN_BIT15 | Input | BOOL | I, Q, M, D, L or constant | Input bit 15 is compared with bit 15 of the mask. |
| OUT | Output | BOOL | I, Q, M, D, L | The signal state "1" indicates that a match was found.  The signal state "0" indicates that no match was found. |
| ERR_CODE | Output | WORD | I, Q, M, D, L, P | Error information |
| OUT_STEP | Output | BYTE | I, Q, M, D, L, P | Contains the step number with the matching mask, or the step number which is greater by "1" than the value at the LAST parameter, provided no match is found. |
| LAST | Static | BYTE | I, Q, M, D, L, P or constant | Specifies the step number of the last step to be scanned for a matching mask. |
| CMP_VAL | Static | ARRAY OF WORD | I, Q, M, D, L or constant | Comparison masks [0 to 15, 0 to 15]: The first number of the index is the step number and the second number is the bit number of the mask. |

##### Parameter ERR_CODE

The following table shows the meaning of the values of the ERR_CODE parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 000E | The value at the LAST parameter is greater than 15. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Example

In this example, all 16 input bits are compared with the mask for steps 0 through 5 until a match is found. Only the masks for steps 0 through 2 are scanned, since the mask for step 2 matches the input bit.

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL SMC, "SMC_DB"

(IN_BIT0 - 15 := "Tag_Input_BITn"

OUT =&gt; "Tag_Output"

OUT_STEP =&gt; "Tag_Output_STEP"

ERR_CODE =&gt; "Tag_ErrorCode"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for the input and output parameters:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN_BIT0 | Tag_Input_BIT0 | TRUE |
| IN_BIT1 | Tag_Input_BIT1 | TRUE |
| IN_BIT2 | Tag_Input_BIT2 | FALSE |
| IN_BIT3 | Tag_Input_BIT3 | TRUE |
| IN_BIT4 | Tag_Input_BIT4 | TRUE |
| IN_BIT5 | Tag_Input_BIT5 | FALSE |
| IN_BIT6 | Tag_Input_BIT6 | TRUE |
| IN_BIT7 | Tag_Input_BIT7 | TRUE |
| IN_BIT8 | Tag_Input_BIT8 | FALSE |
| IN_BIT9 | Tag_Input_BIT9 | TRUE |
| IN_BIT10 | Tag_Input_BIT10 | TRUE |
| IN_BIT11 | Tag_Input_BIT11 | FALSE |
| IN_BIT12 | Tag_Input_BIT12 | TRUE |
| IN_BIT13 | Tag_Input_BIT13 | TRUE |
| IN_BIT14 | Tag_Input_BIT14 | FALSE |
| IN_BIT15 | Tag_Input_BIT15 | TRUE |
| OUT | Tag_Output | FALSE |
| OUT_STEP | Tag_Output_STEP | B#16#00 |
| ERR_CODE | Tag_ErrorCode | W#16#0000 |

The following values for the mask of step 2 are saved in the "SMC_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| CMP_VAL [2,0] | DBX12.0 | TRUE |
| CMP_VAL [2,1] | DBX12.1 | TRUE |
| CMP_VAL [2,2] | DBX12.2 | FALSE |
| CMP_VAL [2,3] | DBX12.3 | TRUE |
| CMP_VAL [2,4] | DBX12.4 | TRUE |
| CMP_VAL [2,5] | DBX12.5 | FALSE |
| CMP_VAL [2,6] | DBX12.6 | TRUE |
| CMP_VAL [2,7] | DBX12.7 | TRUE |
| CMP_VAL [2,8] | DBX13.0 | FALSE |
| CMP_VAL [2,0] | DBX13.1 | TRUE |
| CMP_VAL [2,10] | DBX13.2 | TRUE |
| CMP_VAL [2,11] | DBX13.3 | FALSE |
| CMP_VAL [2,12] | DBX13.4 | TRUE |
| CMP_VAL [2,13] | DBX13.5 | TRUE |
| CMP_VAL [2,14] | DBX13.6 | FALSE |
| CMP_VAL [2,15] | DBX13.7 | TRUE |
| LAST | DB84 | B#16#05 |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Value |
| --- | --- | --- |
| OUT | Tag_Output | TRUE |
| OUT_STEP | Tag_Output_STEP | B#16#02 |
| ERR_CODE | Tag_ErrorCode | W#16#0000 |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### LEAD_LAG: Lead and lag algorithm  (S7-1500)

##### Description

You use the "Lead and lag algorithm" instruction to process signals with an analog tag. The gain value at the GAIN parameter must be greater than zero. The result of the "Lead and lag algorithm" instruction is calculated using the following equation:

![Description](images/50811330187_DV_resource.Stream@PNG-de-DE.png)

The "Lead and lag algorithm" instruction supplies plausible results only when processing is in fixed program cycles. The same units must be specified at the parameters LD_TIME, LG_TIME and SAMPLE_T. At LG_TIME &gt; 4 + SAMPLE_T, the instruction approaches the following function:

OUT = GAIN * ((1 + LD_TIME * s) / (1 + LG_TIME * s)) * IN

When the value of the GAIN parameter is less than or equal to zero, the calculation is not performed and error information is output in the ERR_CODE parameter.

You use the "Lead and lag algorithm" instruction in conjunction with loops as a compensator in dynamic feed-forward control. The instruction consists of two operations. The "Lead" operation shifts the phase of the OUT output so that the output leads the input. The "Lag" operation, on the other hand, shifts the output so that the output lags behind the input. Because the "Lag" operation is equivalent to an integration, it can be used as a noise suppressor or as a low-pass filter. The "Lead" operation is equivalent to a differentiation and can therefore be used as a high-pass filter. The two operations together (Lead and Lag) result in the output phase lagging behind the input at lower frequencies and leading it at higher frequencies. This means that the "Lead and lag algorithm" instruction can be used as a band pass filter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | REAL | I, Q, M, D, L, P or constant | The input value of the current sample time (cycle time) to be processed. |
| SAMPLE_T | Input | INT | I, Q, M, D, L, P or constant | Sample time |
| OUT | Output | REAL | I, Q, M, D, L, P | Result of the instruction |
| ERR_CODE | Output | WORD | I, Q, M, D, L, P | Error information |
| LD_TIME | Static | REAL | I, Q, M, D, L, P or constant | Lead time in the same unit as sample time. |
| LG_TIME | Static | REAL | I, Q, M, D, L, P or constant | Lag time in the same unit as sample time |
| GAIN | Static | REAL | I, Q, M, D, L, P or constant | Gain as % / % (the ratio of the change in output to a change in input as a steady state). |
| PREV_IN | Static | REAL | I, Q, M, D, L, P or constant | Previous input |
| PREV_OUT | Static | REAL | I, Q, M, D, L, P or constant | Previous output |

##### Parameter ERR_CODE

The following table shows the meaning of the values of the ERR_CODE parameter:

| Error code* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error |
| 0009 | The value at the GAIN parameter is less than or equal to zero. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Example

The following example shows how the instruction works:

> **Note**
>
> You can initialize static parameters in the data block.

GRAPH

CALL LEAD_LAG, "LEAD_LAG_DB"

(IN := "Tag_Input"

SAMPLE_T := "Tag_Input_SAMPLE_T"

OUT =&gt; "Tag_Output_Result"

ERR_CODE =&gt; "Tag_ErrorCode"

)

The following tables show how the instruction works using specific values.

##### Before processing

In this example, the following values are used for the input parameters:

| Parameter | Operand | Value |
| --- | --- | --- |
| IN | Tag_Input | 2.0 |
| SAMPLE_T | Tag_Input_SAMPLE_T | 10 |

The following values are saved in the "LEAD_LAG_DB" instance data block of the instruction:

| Parameter | Address | Value |
| --- | --- | --- |
| LD_TIME | DBD12 | 2.0 |
| LG_TIME | DBD16 | 2.0 |
| GAIN | DBD20 | 1.0 |
| PREV_IN | DBD24 | 6.0 |
| PREV_OUT | DBD28 | 6.0 |

##### After processing

The following values are written to the output parameters after the instruction has been executed:

| Parameter | Operand | Value |
| --- | --- | --- |
| OUT | Tag_Output_Result | 2.0 |

The following values are saved in the "LEAD_LAD_DB" instance data block of the instruction:

| Parameter | Operand | Value |
| --- | --- | --- |
| PREV_IN | DBD24 | 2.0 |
| PREV_OUT | DBD28 | 2.0 |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### SEG: Create bit pattern for seven-segment display (S7-1500)

##### Description

The "Create bit pattern for seven-segment display" instruction converts each of the four hexadecimal digits in the specified source word (IN) into four equivalent codes for a 7-segment display and writes these to the double word of the output (OUT).

The instruction does not detect any error conditions.

The relationship between the input hexadecimal values and the output bit patterns is as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| **Digit** | **‑gfedcba** | **Display** | Seven-segment display |
| 0000 | 00111111 | 0 | ![Description](images/7307290891_DV_resource.Stream@PNG-de-DE.png) |
| 0001 | 00000110 | 1 |  |
| 0010 | 01011011 | 2 |  |
| 0011 | 01001111 | 3 |  |
| 0100 | 01100110 | 4 |  |
| 0101 | 01101101 | 5 |  |
| 0110 | 01111101 | 6 |  |
| 0111 | 00000111 | 7 |  |
| 1000 | 01111111 | 8 |  |
| 1001 | 01100111 | 9 |  |
| 1010 | 01110111 | A |  |
| 1011 | 01111100 | B |  |
| 1100 | 00111001 | C |  |
| 1101 | 01011110 | D |  |
| 1110 | 01111001 | E |  |
| 1111 | 01110001 | F |  |

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | WORD | I, Q, M, D, L, P or constant | Source word with four hexadecimal digits |
| OUT | Output | DWORD | I, Q, M, D, L, P | Destination bit pattern with four bytes |

##### Example

The following example shows how the instruction works:

GRAPH

CALL SEG

(IN := "Tag_Input"

OUT =&gt; "Tag_Output"

)

The following table shows how the instruction functions using specific values:

| Parameter | Operand | Value |  |
| --- | --- | --- | --- |
| Hexadecimal | Binary |  |  |
| IN | Tag_Input | W#16#1234 | 0001 0010 0011 0100 |
| OUT | Tag_Output | DW#16065B4F66 | 000 00110 0101 1011 0100 1111 0110 0110  Display: 1234 |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### BCDCPL: Create tens complement (S7-1500)

##### Description

You use the "Create tens complement" instruction to create the tens complement of a seven-digit BCD number specified in the IN parameter. This instruction uses the following mathematical formula to calculate:

10000000 (as BCD)

– 7-digit BCD value

----------------------------------------

Tens complement (as BCD)

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | Bit strings | I, Q, M, D, L, P or constant | 7-digit BCD number |
| ERR_CODE | Output | DWORD | I, Q, M, D, L, P | Result of the instruction |

##### Example

The following example shows how the instruction works:

GRAPH

CALL BCDCPL

(IN := "Tag_Input"

ERR_CODE =&gt; "Tag_Output"

)

The following table shows how the instruction functions using specific values:

| Parameter | Operand | Value* |
| --- | --- | --- |
| IN | Tag_Input | DW#16#01234567 |
| ERR_CODE | Tag_Output | DW#16#08765433 |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

#### BITSUM: Count number of set bits (S7-1500)

##### Description

You use the "Count number of set bits" instruction to count the number of bits of an operand that is set to the signal state "1". The operand whose bits are to be counted is specified in the IN parameter. The result of the instruction is output at the RET_VAL parameter.

##### Parameters

The following table shows the parameters of the instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN | Input | DWORD | I, Q, M, D, L, P or constant | Operand whose set bits are counted |
| RET_VAL | Output | INT | I, Q, M, D, L, P | Number of set bits |

##### Example

The following example shows how the instruction works:

GRAPH

CALL BITSUM

(IN := "Tag_Input"

RET​_VAL =&gt; "Tag_Output"

)

The following table shows how the instruction functions using specific values:

| Parameter | Operand | Value* |
| --- | --- | --- |
| IN | Tag_Input | DW#16#12345678 |
| RET_VAL | Tag_Output | W#16#000D (13 bits) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

## GRAPH LAD instructions (S7-1500)

This section contains information on the following topics:

- [General LAD instructions in GRAPH (S7-1500)](#general-lad-instructions-in-graph-s7-1500)
- [CMP&gt;T: Greater than step activation time (S7-1500)](#cmpt-greater-than-step-activation-time-s7-1500)
- [CMP&gt;U: Greater than uninterrupted step activation time (S7-1500)](#cmpu-greater-than-uninterrupted-step-activation-time-s7-1500)
- [CMP&gt;T_MAX: Greater than maximum step activation time (S7-1500)](#cmpt_max-greater-than-maximum-step-activation-time-s7-1500)
- [CMP&gt;T_WARN: Greater than warning time (S7-1500)](#cmpt_warn-greater-than-warning-time-s7-1500)

### General LAD instructions in GRAPH (S7-1500)

#### Description

Different LAD instructions are available to you when programming in GRAPH.

The following table shows an overview of the instructions and their availability:

| LAD instruction | Permanent instruction | Transition/Supervision/Interlock |
| --- | --- | --- |
| **General** |  |  |
| Insert network | x | - |
| Empty box | x | x |
| Open branch | x | x |
| Close branch | x | x |
| -|: Insert input | x | - |
| **Bit logic operations** |  |  |
| [---| |---: Normally open contact](LAD%20%28S7-1200%2C%20S7-1500%29.md#normally-open-contact-s7-1200-s7-1500) | x | x |
| [---| / |---: Normally closed contact](LAD%20%28S7-1200%2C%20S7-1500%29.md#normally-closed-contact-s7-1200-s7-1500) | x | x |
| [--|NOT|--: Invert RLO](LAD%20%28S7-1200%2C%20S7-1500%29.md#not---invert-rlo-s7-1200-s7-1500) | x | x |
| [---( )---: Assignment](LAD%20%28S7-1200%2C%20S7-1500%29.md#assignment-s7-1200-s7-1500) | x | - |
| [---( / )---: Negate assignment](LAD%20%28S7-1200%2C%20S7-1500%29.md#negate-assignment-s7-1200-s7-1500) | x | - |
| [---( R )---: Reset output](LAD%20%28S7-1200%2C%20S7-1500%29.md#r-----reset-output-s7-1200-s7-1500) | x | - |
| [---( S )---: Set output](LAD%20%28S7-1200%2C%20S7-1500%29.md#s-----set-output-s7-1200-s7-1500) | x | - |
| [SET_BF: Set bit field](LAD%20%28S7-1200%2C%20S7-1500%29.md#set_bf-set-bit-field-s7-1200-s7-1500) | x | - |
| [RESET_BF: Reset bit field](LAD%20%28S7-1200%2C%20S7-1500%29.md#reset_bf-reset-bit-field-s7-1200-s7-1500) | x | - |
| [SR: Set/reset flip-flop](LAD%20%28S7-1200%2C%20S7-1500%29.md#sr-setreset-flip-flop-s7-1200-s7-1500) | x | - |
| [RS: Reset/set flip-flop](LAD%20%28S7-1200%2C%20S7-1500%29.md#rs-resetset-flip-flop-s7-1200-s7-1500) | x | - |
| [--|P|--: Scan operand for positive signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#p---scan-operand-for-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [--|N|--: Scan operand for negative signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#n---scan-operand-for-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [--(P)--: Set operand on positive signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#p---set-operand-on-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [--(N)--: Set operand on negative signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#n---set-operand-on-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [P_TRIG: Scan RLO for positive signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#p_trig-scan-rlo-for-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [N_TRIG: Scan RLO for negative signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#n_trig-scan-rlo-for-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [R_TRIG: Detect positive signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#r_trig-detect-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [F_TRIG: Detect negative signal edge](LAD%20%28S7-1200%2C%20S7-1500%29.md#f_trig-detect-negative-signal-edge-s7-1200-s7-1500) | x | - |
| **Timers** |  |  |
| **IEC timers** |  |  |
| [TP: Generate pulse](LAD%20%28S7-1200%2C%20S7-1500%29.md#tp-generate-pulse-s7-1200-s7-1500) | x | - |
| [TON: Generate on-delay](LAD%20%28S7-1200%2C%20S7-1500%29.md#ton-generate-on-delay-s7-1200-s7-1500) | x | - |
| [TOF: Generate off-delay](LAD%20%28S7-1200%2C%20S7-1500%29.md#tof-generate-off-delay-s7-1200-s7-1500) | x | - |
| [TONR: Time accumulator](LAD%20%28S7-1200%2C%20S7-1500%29.md#tonr-time-accumulator-s7-1200-s7-1500) | x | - |
| [---(TP)---: Start pulse timer](LAD%20%28S7-1200%2C%20S7-1500%29.md#tp-----start-pulse-timer-s7-1200-s7-1500) | x | - |
| [---(TON)---: Start on-delay timer](LAD%20%28S7-1200%2C%20S7-1500%29.md#ton-----start-on-delay-timer-s7-1200-s7-1500) | x | - |
| [---(TOF)---: Start off-delay timer](LAD%20%28S7-1200%2C%20S7-1500%29.md#tof-----start-off-delay-timer-s7-1200-s7-1500) | x | - |
| [---(TONR)---: Time accumulator](LAD%20%28S7-1200%2C%20S7-1500%29.md#tonr-----time-accumulator-s7-1200-s7-1500) | x | - |
| [---(RT)---: Reset timer](LAD%20%28S7-1200%2C%20S7-1500%29.md#rt-----reset-timer-s7-1200-s7-1500) | x | - |
| [---(PT)---: Load time duration](LAD%20%28S7-1200%2C%20S7-1500%29.md#pt-----load-time-duration-s7-1200-s7-1500) | x | - |
| **SIMATIC timers (S7-1500)** |  |  |
| [S_PULSE: Assign pulse timer parameters and start](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_pulse-assign-pulse-timer-parameters-and-start-s7-1500) | x | - |
| [S_PEXT: Assign extended pulse timer parameters and start](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_pext-assign-extended-pulse-timer-parameters-and-start-s7-1500) | x | - |
| [S_ODT: Assign on-delay timer parameters and start](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_odt-assign-on-delay-timer-parameters-and-start-s7-1500) | x | - |
| [S_ODTS: Assign retentive on-delay timer parameters and start](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_odts-assign-retentive-on-delay-timer-parameters-and-start-s7-1500) | x | - |
| [S_OFFDT: Assign off-delay timer parameters and start](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_offdt-assign-off-delay-timer-parameters-and-start-s7-1500) | x | - |
| **Counters** |  |  |
| **IEC counters** |  |  |
| [CTU: Count up](LAD%20%28S7-1200%2C%20S7-1500%29.md#ctu-count-up-s7-1200-s7-1500) | x | - |
| [CTD: Count down](LAD%20%28S7-1200%2C%20S7-1500%29.md#ctd-count-down-s7-1200-s7-1500) | x | - |
| [CTUD: Count up and down](LAD%20%28S7-1200%2C%20S7-1500%29.md#ctud-count-up-and-down-s7-1200-s7-1500) | x | - |
| **SIMATIC counters (S7-1500)** |  |  |
| [S_CU: Assign parameters and count up](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_cu-assign-parameters-and-count-up-s7-1500) | x | - |
| [S_CD: Assign parameters and count down](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_cd-assign-parameters-and-count-down-s7-1500) | x | - |
| [S_CUD: Assign parameters and count up / down](LAD%20%28S7-1200%2C%20S7-1500%29.md#s_cud-assign-parameters-and-count-up-down-s7-1500) | x | - |
| **Comparator operations** |  |  |
| [CMP ==: Equal](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-equal-s7-1200-s7-1500) | x | x |
| [CMP &lt;&gt;: Not equal](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-not-equal-s7-1200-s7-1500) | x | x |
| [CMP &gt;=: Greater or equal](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-greater-or-equal-s7-1200-s7-1500) | x | x |
| [CMP &lt;=: Less or equal](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-less-or-equal-s7-1200-s7-1500) | x | x |
| [CMP &gt;: Greater than](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-greater-than-s7-1200-s7-1500) | x | x |
| [CMP &lt;: Less than](LAD%20%28S7-1200%2C%20S7-1500%29.md#cmp-less-than-s7-1200-s7-1500) | x | x |
| [IN_RANGE: Value within range](LAD%20%28S7-1200%2C%20S7-1500%29.md#in_range-value-within-range-s7-1200-s7-1500) | x | - |
| [OUT_RANGE: Value outside range](LAD%20%28S7-1200%2C%20S7-1500%29.md#out_range-value-outside-range-s7-1200-s7-1500) | x | - |
| [---| OK |---: Check validity](LAD%20%28S7-1200%2C%20S7-1500%29.md#i-ok-i-----check-validity-s7-1200-s7-1500) | x | - |
| [---| NOT_OK |---: Check invalidity](LAD%20%28S7-1200%2C%20S7-1500%29.md#i-not_ok-i-----check-invalidity-s7-1200-s7-1500) | x | - |
| [EQ_Type: Compare data type for EQUAL with the data type of a tag](LAD%20%28S7-1200%2C%20S7-1500%29.md#eq_type-compare-data-type-for-equal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [NE_Type: Compare data type for UNEQUAL with the data type of a tag](LAD%20%28S7-1200%2C%20S7-1500%29.md#ne_type-compare-data-type-for-unequal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [EQ_ElemType: Compare data type of an ARRAY element for EQUAL with the data type of a tag](LAD%20%28S7-1200%2C%20S7-1500%29.md#eq_elemtype-compare-data-type-of-an-array-element-for-equal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [NE_ElemType: Compare data type of an ARRAY element for UNEQUAL with the data type of a tag](LAD%20%28S7-1200%2C%20S7-1500%29.md#ne_elemtype-compare-data-type-of-an-array-element-for-unequal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [IS_NULL: Query for EQUALS ZERO pointer](LAD%20%28S7-1200%2C%20S7-1500%29.md#is_null-check-for-equals-null-pointer-s7-1200-s7-1500) | x | - |
| [NOT_NULL: Query for UNEQUALS ZERO pointer](LAD%20%28S7-1200%2C%20S7-1500%29.md#not_null-check-for-unequals-null-pointer-s7-1200-s7-1500) | x | - |
| [IS_ARRAY: Check for ARRAY](LAD%20%28S7-1200%2C%20S7-1500%29.md#is_array-check-for-array-s7-1200-s7-1500) | x | - |
| [EQ_TypeOfDB: Compare DB_ANY data type with the data type of a tag for EQUAL](LAD%20%28S7-1200%2C%20S7-1500%29.md#eq_typeofdb-compare-data-type-of-an-indirectly-addressed-db-for-equal-with-a-data-type-s7-1200-s7-1500) | x | - |
| [NE_TypeOfDB: Compare DB_ANY data type with the data type of a tag for NOT EQUAL](LAD%20%28S7-1200%2C%20S7-1500%29.md#ne_typeofdb-compare-data-type-of-an-indirectly-addressed-db-for-unequal-with-a-data-type-s7-1200-s7-1500) | x | - |
| [CMP&gt;T: Greater than step activation time](#cmpt-greater-than-step-activation-time-s7-1500) | - | x |
| [CMP&gt;U: Greater than uninterrupted step activation time](#cmpu-greater-than-uninterrupted-step-activation-time-s7-1500) | - | x |
| **Math functions** |  |  |
| [CALCULATE: Calculate](LAD%20%28S7-1200%2C%20S7-1500%29.md#calculate-calculate-s7-1200-s7-1500) | x | - |
| [ADD: Add](LAD%20%28S7-1200%2C%20S7-1500%29.md#add-add-s7-1200-s7-1500) | x | - |
| [SUB: Subtract](LAD%20%28S7-1200%2C%20S7-1500%29.md#sub-subtract-s7-1200-s7-1500) | x | - |
| [MUL: Multiply](LAD%20%28S7-1200%2C%20S7-1500%29.md#mul-multiply-s7-1200-s7-1500) | x | - |
| [DIV: Divide](LAD%20%28S7-1200%2C%20S7-1500%29.md#div-divide-s7-1200-s7-1500) | x | - |
| [MOD: Return remainder of division](LAD%20%28S7-1200%2C%20S7-1500%29.md#mod-return-remainder-of-division-s7-1200-s7-1500) | x | - |
| [NEG: Create twos complement](LAD%20%28S7-1200%2C%20S7-1500%29.md#neg-create-twos-complement-s7-1200-s7-1500) | x | - |
| [INC: Increment](LAD%20%28S7-1200%2C%20S7-1500%29.md#inc-increment-s7-1200-s7-1500) | x | - |
| [DEC: Decrement](LAD%20%28S7-1200%2C%20S7-1500%29.md#dec-decrement-s7-1200-s7-1500) | x | - |
| [ABS: Form absolute value](LAD%20%28S7-1200%2C%20S7-1500%29.md#abs-form-absolute-value-s7-1200-s7-1500) | x | - |
| [MIN: Get minimum](LAD%20%28S7-1200%2C%20S7-1500%29.md#min-get-minimum-s7-1200-s7-1500) | x | - |
| [MAX: Get maximum](LAD%20%28S7-1200%2C%20S7-1500%29.md#max-get-maximum-s7-1200-s7-1500) | x | - |
| [LIMIT: Set limit value](LAD%20%28S7-1200%2C%20S7-1500%29.md#limit-set-limit-value-s7-1200-s7-1500) | x | - |
| [SQR: Form square](LAD%20%28S7-1200%2C%20S7-1500%29.md#sqr-form-square-s7-1200-s7-1500) | x | - |
| [SQRT: Form square root](LAD%20%28S7-1200%2C%20S7-1500%29.md#sqrt-form-square-root-s7-1200-s7-1500) | x | - |
| [LN: Form natural logarithm](LAD%20%28S7-1200%2C%20S7-1500%29.md#ln-form-natural-logarithm-s7-1200-s7-1500) | x | - |
| [EXP: Form exponential value](LAD%20%28S7-1200%2C%20S7-1500%29.md#exp-form-exponential-value-s7-1200-s7-1500) | x | - |
| [SIN: Form sine value](LAD%20%28S7-1200%2C%20S7-1500%29.md#sin-form-sine-value-s7-1200-s7-1500) | x | - |
| [COS: Form cosine value](LAD%20%28S7-1200%2C%20S7-1500%29.md#cos-form-cosine-value-s7-1200-s7-1500) | x | - |
| [TAN: Form tangent value](LAD%20%28S7-1200%2C%20S7-1500%29.md#tan-form-tangent-value-s7-1200-s7-1500) | x | - |
| [ASIN: Form arcsine value](LAD%20%28S7-1200%2C%20S7-1500%29.md#asin-form-arcsine-value-s7-1200-s7-1500) | x | - |
| [ACOS: Form arccosine value](LAD%20%28S7-1200%2C%20S7-1500%29.md#acos-form-arccosine-value-s7-1200-s7-1500) | x | - |
| [ATAN: Form arctangent value](LAD%20%28S7-1200%2C%20S7-1500%29.md#atan-form-arctangent-value-s7-1200-s7-1500) | x | - |
| [FRAC: Return fraction](LAD%20%28S7-1200%2C%20S7-1500%29.md#frac-return-fraction-s7-1200-s7-1500) | - | - |
| [EXPT: Exponentiate](LAD%20%28S7-1200%2C%20S7-1500%29.md#expt-exponentiate-s7-1200-s7-1500) | x | - |
| **Move operations** |  |  |
| [MOVE: Move value](LAD%20%28S7-1200%2C%20S7-1500%29.md#move-move-value-s7-1200-s7-1500) | x | - |
| [Deserialize: Deserialization](LAD%20%28S7-1200%2C%20S7-1500%29.md#deserialize-deserialize-s7-1200-s7-1500) | x | - |
| [Serialize: Serialization](LAD%20%28S7-1200%2C%20S7-1500%29.md#serialize-serialize-s7-1200-s7-1500) | x | - |
| [FieldRead: Read field](LAD%20%28S7-1200%2C%20S7-1500%29.md#fieldread-read-field-s7-1500) | x | - |
| [FieldWrite: Write field](LAD%20%28S7-1200%2C%20S7-1500%29.md#fieldwrite-write-field-s7-1500) | x | - |
| [MOVE_BLK: Move block](LAD%20%28S7-1200%2C%20S7-1500%29.md#move_blk-move-block-s7-1200-s7-1500) | x | - |
| [SCATTER: Parse the bit sequence into individual bits](LAD%20%28S7-1200%2C%20S7-1500%29.md#scatter-parse-the-bit-sequence-into-individual-bits-s7-1200-s7-1500) | x | - |
| [SCATTER_BLK: Parse elements of an ARRAY of bit sequence into individual bits](LAD%20%28S7-1200%2C%20S7-1500%29.md#scatter_blk-parse-elements-of-an-array-of-bit-sequence-into-individual-bits-s7-1200-s7-1500) | x | - |
| [GATHER: Merge individual bits into a bit sequence](LAD%20%28S7-1200%2C%20S7-1500%29.md#gather-merge-individual-bits-into-a-bit-sequence-s7-1200-s7-1500) | x | - |
| [GATHER_BLK: Merge individual bits into multiple elements of an ARRAY of bit sequence](LAD%20%28S7-1200%2C%20S7-1500%29.md#gather_blk-merge-individual-bits-into-multiple-elements-of-an-array-of-bit-sequence-s7-1200-s7-1500) | x | - |
| [MOVE_BLK_VARIANT: Move block](LAD%20%28S7-1200%2C%20S7-1500%29.md#move_blk_variant-move-block-s7-1200-s7-1500) | x | - |
| [UMOVE_BLK: Move block uninterruptible](LAD%20%28S7-1200%2C%20S7-1500%29.md#umove_blk-move-block-uninterruptible-s7-1200-s7-1500) | x | - |
| [FILL_BLK: Fill block](LAD%20%28S7-1200%2C%20S7-1500%29.md#fill_blk-fill-block-s7-1200-s7-1500) | x | - |
| [UFILL_BLK: Fill block uninterruptible](LAD%20%28S7-1200%2C%20S7-1500%29.md#ufill_blk-fill-block-uninterruptible-s7-1200-s7-1500) | x | - |
| [?= Assignment attempt](LAD%20%28S7-1200%2C%20S7-1500%29.md#assignmentattempt-attempt-assignment-to-a-reference-s7-1500) | x | - |
| [SWAP: Swap](LAD%20%28S7-1200%2C%20S7-1500%29.md#swap-swap-s7-1200-s7-1500) | x | - |
| [ReadFromArrayDB: Read from the array data block](LAD%20%28S7-1200%2C%20S7-1500%29.md#readfromarraydb-read-from-arraydata-block-s7-1500) | x | - |
| [WriteToArrayDB: Write to the array data block](LAD%20%28S7-1200%2C%20S7-1500%29.md#writetoarraydb-write-to-array-data-block-s7-1500) | x | - |
| [ReadFromArrayDBL: Read from the array data block in the load memory](LAD%20%28S7-1200%2C%20S7-1500%29.md#readfromarraydbl-read-from-array-data-block-in-load-memory-s7-1500) | x | - |
| [WriteToArrayDBL: Write to array data block in the load memory](LAD%20%28S7-1200%2C%20S7-1500%29.md#writetoarraydbl-write-to-array-data-block-in-load-memory-s7-1500) | x | - |
| [VariantGet: Read VARIANT tag value](LAD%20%28S7-1200%2C%20S7-1500%29.md#variantget-read-out-variant-tag-value-s7-1200-s7-1500) | x | - |
| [VariantPut: Write VARIANT tag value](LAD%20%28S7-1200%2C%20S7-1500%29.md#variantput-write-variant-tag-value-s7-1200-s7-1500) | x | - |
| [CountOfElements: Get number of ARRAY elements](LAD%20%28S7-1200%2C%20S7-1500%29.md#countofelements-get-number-of-array-elements-s7-1200-s7-1500) | x | - |
| [LOWER_BOUND: Read ARRAY low limit](LAD%20%28S7-1200%2C%20S7-1500%29.md#lower_bound-read-out-low-array-limit-s7-1200-s7-1500) | x | - |
| [UPPER_BOUND: Read ARRAY high limit](LAD%20%28S7-1200%2C%20S7-1500%29.md#upper_bound-read-out-high-array-limit-s7-1200-s7-1500) | x | - |
| [BLKMOV: Move block (S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#blkmov-move-block-s7-1500) | x | - |
| [UBLKMOV: Move block uninterruptible (S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#ublkmov-move-block-uninterruptible-s7-1500) | x | - |
| [FILL: Fill block (S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#fill-fill-block-s7-1500) | x | - |
| **Conversion operations** |  |  |
| [CONVERT: Convert value](LAD%20%28S7-1200%2C%20S7-1500%29.md#convert-convert-value-s7-1200-s7-1500) | x | - |
| [ROUND: Round numerical value](LAD%20%28S7-1200%2C%20S7-1500%29.md#round-round-numerical-value-s7-1200-s7-1500) | x | - |
| [CEIL: Generate next higher integer from floating-point number](LAD%20%28S7-1200%2C%20S7-1500%29.md#ceil-generate-next-higher-integer-from-floating-point-number-s7-1200-s7-1500) | x | - |
| [FLOOR: Generate next lower integer from floating-point number](LAD%20%28S7-1200%2C%20S7-1500%29.md#floor-generate-next-lower-integer-from-floating-point-number-s7-1200-s7-1500) | x | - |
| [TRUNC: Truncate numerical value](LAD%20%28S7-1200%2C%20S7-1500%29.md#trunc-truncate-numerical-value-s7-1200-s7-1500) | x | - |
| [SCALE_X: Scale](LAD%20%28S7-1200%2C%20S7-1500%29.md#scale_x-scale-s7-1200-s7-1500) | x | - |
| [NORM_X: Normalize](LAD%20%28S7-1200%2C%20S7-1500%29.md#norm_x-normalize-s7-1200-s7-1500) | x | - |
| [SCALE: Scale (S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#scale-scale-s7-1500) | x | - |
| [UNSCALE: Unscale (S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#unscale-unscale-s7-1500) | x | - |
| **Program control operations** |  |  |
| Runtime control |  |  |
| [ENDIS_PW: Locking and unlocking passwords of the CPU access levels](LAD%20%28S7-1200%2C%20S7-1500%29.md#endis_pw-locking-and-unlocking-passwords-of-the-cpu-access-levels-s7-1200-s7-1500) | x | - |
| [RE_TRIGR: Restart cycle monitoring time](LAD%20%28S7-1200%2C%20S7-1500%29.md#re_trigr-restart-cycle-monitoring-time-s7-1200-s7-1500) | x | - |
| [STP: Exit program](LAD%20%28S7-1200%2C%20S7-1500%29.md#stp-exit-program-s7-1200-s7-1500) | x | - |
| [GET_ERROR: Get error locally](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_error-get-error-locally-s7-1200-s7-1500) | x | - |
| [GET_ERR_ID: Get error ID locally](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500) | x | - |
| [INIT_RD: Initialize all retain data](LAD%20%28S7-1200%2C%20S7-1500%29.md#init_rd-initialize-all-retain-data-s7-1500) | x | - |
| [WAIT: Configure time delay](LAD%20%28S7-1200%2C%20S7-1500%29.md#wait-configure-time-delay-s7-1500) | x | - |
| [RUNTIME: Runtime measurement](LAD%20%28S7-1200%2C%20S7-1500%29.md#runtime-measure-program-runtime-s7-1200-s7-1500) | x | - |
| **Word logic operations** |  |  |
| [AND: AND logic operation](LAD%20%28S7-1200%2C%20S7-1500%29.md#and-and-logic-operation-s7-1200-s7-1500) | x | - |
| [OR: OR logic operation](LAD%20%28S7-1200%2C%20S7-1500%29.md#or-or-logic-operation-s7-1200-s7-1500) | x | - |
| [XOR: EXCLUSIVE OR logic operation](LAD%20%28S7-1200%2C%20S7-1500%29.md#xor-exclusive-or-logic-operation-s7-1200-s7-1500) | x | - |
| [INV: Create ones complement](LAD%20%28S7-1200%2C%20S7-1500%29.md#invert-create-ones-complement-s7-1200-s7-1500) | x | - |
| [DECO: Decode](LAD%20%28S7-1200%2C%20S7-1500%29.md#deco-decode-s7-1200-s7-1500) | x | - |
| [ENCO: Encode](LAD%20%28S7-1200%2C%20S7-1500%29.md#enco-encode-s7-1200-s7-1500) | x | - |
| [SEL: Select](LAD%20%28S7-1200%2C%20S7-1500%29.md#sel-select-s7-1200-s7-1500) | x | - |
| [MUX: Multiplex](LAD%20%28S7-1200%2C%20S7-1500%29.md#mux-multiplex-s7-1200-s7-1500) | x | - |
| [DEMUX: Demultiplex](LAD%20%28S7-1200%2C%20S7-1500%29.md#demux-demultiplex-s7-1200-s7-1500) | x | - |
| **Shift and rotate** |  |  |
| [SHR: Shift right](LAD%20%28S7-1200%2C%20S7-1500%29.md#shr-shift-right-s7-1200-s7-1500) | x | - |
| [SHL: Shift left](LAD%20%28S7-1200%2C%20S7-1500%29.md#shl-shift-left-s7-1200-s7-1500) | x | - |
| [ROR: Rotate right](LAD%20%28S7-1200%2C%20S7-1500%29.md#ror-rotate-right-s7-1200-s7-1500) | x | - |
| [ROL: Rotate left](LAD%20%28S7-1200%2C%20S7-1500%29.md#rol-rotate-left-s7-1200-s7-1500) | x | - |
| **Additional instructions** |  |  |
| [DRUM: Implement sequencer](LAD%20%28S7-1200%2C%20S7-1500%29.md#drum-implement-sequencer-s7-1500) | x | - |
| [DCAT: Discrete control-timer alarm](LAD%20%28S7-1200%2C%20S7-1500%29.md#dcat-discrete-control-timer-alarm-s7-1500) | x | - |
| [MCAT: Motor control-timer alarm](LAD%20%28S7-1200%2C%20S7-1500%29.md#mcat-motor-control-timer-alarm-s7-1500) | x | - |
| [IMC: Compare input bits with the bits of the mask](LAD%20%28S7-1200%2C%20S7-1500%29.md#imc-compare-input-bits-with-the-bits-of-a-mask-s7-1500) | x | - |
| [SMC: Compare scan matrix](LAD%20%28S7-1200%2C%20S7-1500%29.md#smc-compare-scan-matrix-s7-1500) | x | - |
| [LEAD_LAG: Lead and lag algorithm](LAD%20%28S7-1200%2C%20S7-1500%29.md#lead_lag-lead-and-lag-algorithm-s7-1500) | x | - |
| [SEG: Create bit pattern for seven-segment display](LAD%20%28S7-1200%2C%20S7-1500%29.md#seg-create-bit-pattern-for-seven-segment-display-s7-1500) | x | - |
| [BCDCPL: Create tens complement](LAD%20%28S7-1200%2C%20S7-1500%29.md#bcdcpl-create-tens-complement-s7-1500) | x | - |
| [BITSUM: Count number of set bits](LAD%20%28S7-1200%2C%20S7-1500%29.md#bitsum-count-number-of-set-bits-s7-1500) | x | - |

### CMP>T: Greater than step activation time (S7-1500)

#### Description

You use the "Greater than step activation time" instruction to monitor the total duration of a step in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T: Greater than step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T: Greater than step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T: Greater than step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T: Greater than step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T: Greater than step activation time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table shows the parameters of the "Greater than step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| &lt;Operand2&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/67279201035_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.T is less than 100 ms, the RLO is "0". As soon as the activation time exceeds 100 ms, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>U: Greater than uninterrupted step activation time (S7-1500)

#### Description

You use the "Greater than uninterrupted step activation time" instruction to monitor the duration of a step, minus any faults, in supervision conditions. The times of any events or faults are not recorded and only the pure step duration is monitored.

In the programmed condition, the total activation time of the step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;U: Greater than uninterrupted step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;U: Greater than uninterrupted step activation time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table shows the parameters of the "Greater than uninterrupted step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step minus the faults |
| &lt;Operand2&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/30548419083_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.U minus possible faults is less than 100 ms, the RLO is "0". As soon as the activation time exceeds 100 ms, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>T_MAX: Greater than maximum step activation time  (S7-1500)

#### Description

You use the "Greater than maximum step activation time" instruction to monitor the maximum total duration of a step in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with the maximum duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T_MAX: Greater than maximum step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T_MAX: Greater than maximum step activation time" is shown as grayed out in the network in the inactive status.

#### Parameter

The following table shows the parameters of the "Greater than maximum step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| &lt;Operand2&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/67279207179_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.T is less than the maximum step activation time of #Step1.T_MAX, the RLO is "0". As soon as the maximum step activation time is exceeded, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Basics of step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-of-step-time-monitoring-s7-1500)
  
[Programming step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#programming-step-time-monitoring-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>T_WARN: Greater than warning time (S7-1500)

#### Description

You use the "Greater than warning time" instruction to monitor the duration of a step and issue a warning when the time is exceeded in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1" and a warning is output. If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T_WARN: Greater than warning time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T_WARN: Greater than warning time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T_WARN: Greater than warning time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T_WARN: Greater than warning time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T_WARN: Greater than warning time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table lists the parameters of the "Greater than warning time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| &lt;Operand1&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| &lt;Operand2&gt; | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/67761976971_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #Step1.T does not exceed the warning time of #Step1.T_WARN, the RLO is "0". As soon as the warning time is exceeded, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Basics of step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-of-step-time-monitoring-s7-1500)
  
[Programming step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#programming-step-time-monitoring-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

## GRAPH FBD instructions (S7-1500)

This section contains information on the following topics:

- [General FBD instructions in GRAPH (S7-1500)](#general-fbd-instructions-in-graph-s7-1500)
- [CMP&gt;T: Greater than step activation time (S7-1500)](#cmpt-greater-than-step-activation-time-s7-1500-1)
- [CMP&gt;U: Greater than uninterrupted step activation time (S7-1500)](#cmpu-greater-than-uninterrupted-step-activation-time-s7-1500-1)
- [CMP&gt;T_MAX: Greater than maximum step activation time (S7-1500)](#cmpt_max-greater-than-maximum-step-activation-time-s7-1500-1)
- [CMP&gt;T_WARN: Greater than warning time (S7-1500)](#cmpt_warn-greater-than-warning-time-s7-1500-1)

### General FBD instructions in GRAPH (S7-1500)

#### Description

Different FBD instructions are available to you when programming in GRAPH.

The following table shows an overview of the instructions and their availability:

| FBD instruction | Permanent operation | Transition/Supervision/Interlock |
| --- | --- | --- |
| **General** |  |  |
| New network | x | - |
| Empty box | x | x |
| Branch: Open branch | x | x |
| [-|: Insert input](FBD%20%28S7-1200%2C%20S7-1500%29.md#insert-input-s7-1200-s7-1500) | x | x |
| [-o|: Invert RLO](FBD%20%28S7-1200%2C%20S7-1500%29.md#invert-rlo-s7-1200-s7-1500) | x | x |
| **Bit logic operations** |  |  |
| [&amp;: AND logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#and-logic-operation-s7-1200-s7-1500) | x | x |
| [&gt;=1: OR logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#1-or-logic-operation-s7-1200-s7-1500) | x | x |
| [X: EXCLUSIVE OR logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#x-exclusive-or-logic-operation-s7-1200-s7-1500) | x | - |
| [=: Assignment](FBD%20%28S7-1200%2C%20S7-1500%29.md#assignment-s7-1200-s7-1500) | x | - |
| [/=: Negate assignment](FBD%20%28S7-1200%2C%20S7-1500%29.md#negate-assignment-s7-1200-s7-1500) | x | - |
| [R: Reset output](FBD%20%28S7-1200%2C%20S7-1500%29.md#r-reset-output-s7-1200-s7-1500) | x | - |
| [S: Set output](FBD%20%28S7-1200%2C%20S7-1500%29.md#s-set-output-s7-1200-s7-1500) | x | - |
| [SET_BF: Set bit field](FBD%20%28S7-1200%2C%20S7-1500%29.md#set_bf-set-bit-field-s7-1200-s7-1500) | x | - |
| [RESET_BF: Reset bit field](FBD%20%28S7-1200%2C%20S7-1500%29.md#reset_bf-reset-bit-field-s7-1200-s7-1500) | x | - |
| [SR: Set/reset flip-flop](FBD%20%28S7-1200%2C%20S7-1500%29.md#sr-setreset-flip-flop-s7-1200-s7-1500) | x | - |
| [RS: Reset/set flip-flop](FBD%20%28S7-1200%2C%20S7-1500%29.md#rs-resetset-flip-flop-s7-1200-s7-1500) | x | - |
| [P: Scan operand for positive signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#p-scan-operand-for-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [N: Scan operand for negative signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#n-scan-operand-for-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [P=: Set operand on positive signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#p-set-operand-on-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [N=: Set operand on negative signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#n-set-operand-on-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [P_TRIG: Scan RLO for positive signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#p_trig-scan-rlo-for-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [N_TRIG: Scan RLO for negative signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#n_trig-scan-rlo-for-negative-signal-edge-s7-1200-s7-1500) | x | - |
| [R_TRIG: Detect positive signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#r_trig-detect-positive-signal-edge-s7-1200-s7-1500) | x | - |
| [F_TRIG: Detect negative signal edge](FBD%20%28S7-1200%2C%20S7-1500%29.md#f_trig-detect-negative-signal-edge-s7-1200-s7-1500) | x | - |
| **Timers** |  |  |
| **IEC timers** |  |  |
| [TP: Generate pulse](FBD%20%28S7-1200%2C%20S7-1500%29.md#tp-generate-pulse-s7-1200-s7-1500) | x | - |
| [TON: Generate on-delay](FBD%20%28S7-1200%2C%20S7-1500%29.md#ton-generate-on-delay-s7-1200-s7-1500) | x | - |
| [TOF: Generate off-delay](FBD%20%28S7-1200%2C%20S7-1500%29.md#tof-generate-off-delay-s7-1200-s7-1500) | x | - |
| [TONR: Time accumulator](FBD%20%28S7-1200%2C%20S7-1500%29.md#tonr-time-accumulator-s7-1200-s7-1500) | x | - |
| [TP: Start pulse timer](FBD%20%28S7-1200%2C%20S7-1500%29.md#tp-start-pulse-timer-s7-1200-s7-1500) | x | - |
| [TON: Start on-delay timer](FBD%20%28S7-1200%2C%20S7-1500%29.md#ton-start-on-delay-timer-s7-1200-s7-1500) | x | - |
| [TOF: Start off-delay timer](FBD%20%28S7-1200%2C%20S7-1500%29.md#tof-start-off-delay-timer-s7-1200-s7-1500) | x | - |
| [TONR: Time accumulator](FBD%20%28S7-1200%2C%20S7-1500%29.md#tonr-time-accumulator-s7-1200-s7-1500-1) | x | - |
| [RT: Reset timer](FBD%20%28S7-1200%2C%20S7-1500%29.md#rt-reset-timer-s7-1200-s7-1500) | x | - |
| [PT: Load time duration](FBD%20%28S7-1200%2C%20S7-1500%29.md#pt-load-time-duration-s7-1200-s7-1500) | x | - |
| **SIMATIC Timers** |  |  |
| [S_PULSE: Assign pulse timer parameters and start](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_pulse-assign-pulse-timer-parameters-and-start-s7-1500) | x | - |
| [S_PEXT: Assign extended pulse timer parameters and start](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_pext-assign-extended-pulse-timer-parameters-and-start-s7-1500) | x | - |
| [S_ODT: Assign on-delay timer parameters and start](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_odt-assign-on-delay-timer-parameters-and-start-s7-1500) | x | - |
| [S_ODTS: Assign retentive on-delay timer parameters and start](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_odts-assign-retentive-on-delay-timer-parameters-and-start-s7-1500) | x | - |
| [S_OFFDT: Assign off-delay timer parameters and start](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_offdt-assign-off-delay-timer-parameters-and-start-s7-1500) | x | - |
| **Counters** |  |  |
| **IEC counters** |  |  |
| [CTU: Count up](FBD%20%28S7-1200%2C%20S7-1500%29.md#ctu-count-up-s7-1200-s7-1500) | x | - |
| [CTD: Count down](FBD%20%28S7-1200%2C%20S7-1500%29.md#ctd-count-down-s7-1200-s7-1500) | x | - |
| [CTUD: Count up and down](FBD%20%28S7-1200%2C%20S7-1500%29.md#ctud-count-up-and-down-s7-1200-s7-1500) | x | - |
| **SIMATIC Counters** |  |  |
| [S_CU: Assign parameters and count up](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_cu-assign-parameters-and-count-up-s7-1500) | x | - |
| [S_CD: Assign parameters and count down](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_cd-assign-parameters-and-count-down-s7-1500) | x | - |
| [S_CUD: Assign parameters and count up / down](FBD%20%28S7-1200%2C%20S7-1500%29.md#s_cud-assign-parameters-and-count-up-down-s7-1500) | x | - |
| **Comparator operations** |  |  |
| [CMP==: Equal](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-equal-s7-1200-s7-1500) | x | x |
| [CMP &lt;&gt;: Not equal](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-not-equal-s7-1200-s7-1500) | x | x |
| [CMP&gt;=: Greater or equal](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-greater-or-equal-s7-1200-s7-1500) | x | x |
| [CMP&lt;=: Less or equal](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-less-or-equal-s7-1200-s7-1500) | x | x |
| [CMP&gt;: Greater than](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-greater-than-s7-1200-s7-1500) | x | x |
| [CMP&lt;: Less than](FBD%20%28S7-1200%2C%20S7-1500%29.md#cmp-less-than-s7-1200-s7-1500) | x | x |
| [IN_RANGE: Value within range](FBD%20%28S7-1200%2C%20S7-1500%29.md#in_range-value-within-range-s7-1200-s7-1500) | x | - |
| [OUT_RANGE: Value outside range](FBD%20%28S7-1200%2C%20S7-1500%29.md#out_range-value-outside-range-s7-1200-s7-1500) | x | - |
| [---| OK |---: Check validity](FBD%20%28S7-1200%2C%20S7-1500%29.md#ok-check-validity-s7-1200-s7-1500) | x | - |
| [---| NOT_OK |---: Check invalidity](FBD%20%28S7-1200%2C%20S7-1500%29.md#not_ok-check-invalidity-s7-1200-s7-1500) | x | - |
| [EQ_Type: Compare data type for EQUAL with the data type of a tag](FBD%20%28S7-1200%2C%20S7-1500%29.md#eq_type-compare-data-type-for-equal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [NE_Type: Compare data type for UNEQUAL with the data type of a tag](FBD%20%28S7-1200%2C%20S7-1500%29.md#ne_type-compare-data-type-for-unequal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [EQ_ElemType: Compare data type of an ARRAY element for EQUAL with the data type of a tag](FBD%20%28S7-1200%2C%20S7-1500%29.md#eq_elemtype-compare-data-type-of-an-array-element-for-equal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [NE_ElemType: Compare data type of an ARRAY element for UNEQUAL with the data type of a tag](FBD%20%28S7-1200%2C%20S7-1500%29.md#ne_elemtype-compare-data-type-of-an-array-element-for-unequal-with-the-data-type-of-a-tag-s7-1200-s7-1500) | x | - |
| [IS_NULL: Query for EQUALS ZERO pointer](FBD%20%28S7-1200%2C%20S7-1500%29.md#is_null-check-for-equals-null-pointer-s7-1200-s7-1500) | x | - |
| [NOT_NULL: Query for UNEQUALS ZERO pointer](FBD%20%28S7-1200%2C%20S7-1500%29.md#not_null-check-for-unequals-null-pointer-s7-1200-s7-1500) | x | - |
| [IS_ARRAY: Check for ARRAY](FBD%20%28S7-1200%2C%20S7-1500%29.md#is_array-check-for-array-s7-1200-s7-1500) | x | - |
| [EQ_TypeOfDB: Compare DB_ANY data type with the data type of a tag for EQUAL](FBD%20%28S7-1200%2C%20S7-1500%29.md#eq_typeofdb-compare-data-type-of-an-indirectly-addressed-db-for-equal-with-a-data-type-s7-1200-s7-1500) | x | - |
| [NE_TypeOfDB: Compare DB_ANY data type with the data type of a tag for NOT EQUAL](FBD%20%28S7-1200%2C%20S7-1500%29.md#ne_typeofdb-compare-data-type-of-an-indirectly-addressed-db-for-unequal-with-a-data-type-s7-1200-s7-1500) | x | - |
| [CMP&gt;T: Greater than step activation time](#cmpt-greater-than-step-activation-time-s7-1500-1) | - | x |
| [CMP&gt;U: Greater than uninterrupted step activation time](#cmpu-greater-than-uninterrupted-step-activation-time-s7-1500-1) | - | x |
| **Math functions** |  |  |
| [CALCULATE: Calculate](FBD%20%28S7-1200%2C%20S7-1500%29.md#calculate-calculate-s7-1200-s7-1500) | x | - |
| [ADD: Add](FBD%20%28S7-1200%2C%20S7-1500%29.md#add-add-s7-1200-s7-1500) | x | - |
| [SUB: Subtract](FBD%20%28S7-1200%2C%20S7-1500%29.md#sub-subtract-s7-1200-s7-1500) | x | - |
| [MUL: Multiply](FBD%20%28S7-1200%2C%20S7-1500%29.md#mul-multiply-s7-1200-s7-1500) | x | - |
| [DIV: Divide](FBD%20%28S7-1200%2C%20S7-1500%29.md#div-divide-s7-1200-s7-1500) | x | - |
| [MOD: Return remainder of division](FBD%20%28S7-1200%2C%20S7-1500%29.md#mod-return-remainder-of-division-s7-1200-s7-1500) | x | - |
| [NEG: Create twos complement](FBD%20%28S7-1200%2C%20S7-1500%29.md#neg-create-twos-complement-s7-1200-s7-1500) | x | - |
| [INC: Increment](FBD%20%28S7-1200%2C%20S7-1500%29.md#inc-increment-s7-1200-s7-1500) | x | - |
| [DEC: Decrement](FBD%20%28S7-1200%2C%20S7-1500%29.md#dec-decrement-s7-1200-s7-1500) | x | - |
| [ABS: Form absolute value](FBD%20%28S7-1200%2C%20S7-1500%29.md#abs-form-absolute-value-s7-1200-s7-1500) | x | - |
| [MIN: Get minimum](FBD%20%28S7-1200%2C%20S7-1500%29.md#min-get-minimum-s7-1200-s7-1500) | x | - |
| [MAX: Get maximum](FBD%20%28S7-1200%2C%20S7-1500%29.md#max-get-maximum-s7-1200-s7-1500) | x | - |
| [LIMIT: Set limit value](FBD%20%28S7-1200%2C%20S7-1500%29.md#limit-set-limit-value-s7-1200-s7-1500) | x | - |
| [SQR: Form square](FBD%20%28S7-1200%2C%20S7-1500%29.md#sqr-form-square-s7-1200-s7-1500) | x | - |
| [SQRT: Form square root](FBD%20%28S7-1200%2C%20S7-1500%29.md#sqrt-form-square-root-s7-1200-s7-1500) | x | - |
| [LN: Form natural logarithm](FBD%20%28S7-1200%2C%20S7-1500%29.md#ln-form-natural-logarithm-s7-1200-s7-1500) | x | - |
| [EXP: Form exponential value](FBD%20%28S7-1200%2C%20S7-1500%29.md#exp-form-exponential-value-s7-1200-s7-1500) | x | - |
| [SIN: Form sine value](FBD%20%28S7-1200%2C%20S7-1500%29.md#sin-form-sine-value-s7-1200-s7-1500) | x | - |
| [COS: Form cosine value](FBD%20%28S7-1200%2C%20S7-1500%29.md#cos-form-cosine-value-s7-1200-s7-1500) | x | - |
| [TAN: Form tangent value](FBD%20%28S7-1200%2C%20S7-1500%29.md#tan-form-tangent-value-s7-1200-s7-1500) | x | - |
| [ASIN: Form arcsine value](FBD%20%28S7-1200%2C%20S7-1500%29.md#asin-form-arcsine-value-s7-1200-s7-1500) | x | - |
| [ACOS: Form arccosine value](FBD%20%28S7-1200%2C%20S7-1500%29.md#acos-form-arccosine-value-s7-1200-s7-1500) | x | - |
| [ATAN: Form arctangent value](FBD%20%28S7-1200%2C%20S7-1500%29.md#atan-form-arctangent-value-s7-1200-s7-1500) | x | - |
| [FRAC: Return fraction](FBD%20%28S7-1200%2C%20S7-1500%29.md#frac-return-fraction-s7-1200-s7-1500) | x | - |
| [EXPT: Exponentiate](FBD%20%28S7-1200%2C%20S7-1500%29.md#expt-exponentiate-s7-1200-s7-1500) | x | - |
| **Move operations** |  |  |
| [MOVE: Move value](FBD%20%28S7-1200%2C%20S7-1500%29.md#move-move-value-s7-1200-s7-1500) | x | - |
| [Deserialize: Deserialization](FBD%20%28S7-1200%2C%20S7-1500%29.md#deserialize-deserialize-s7-1200-s7-1500) | x | - |
| [Serialize: Serialization](FBD%20%28S7-1200%2C%20S7-1500%29.md#serialize-serialize-s7-1200-s7-1500) | x | - |
| [FieldRead: Read field](FBD%20%28S7-1200%2C%20S7-1500%29.md#fieldread-read-field-s7-1500) | x | - |
| [FieldWrite: Write field](FBD%20%28S7-1200%2C%20S7-1500%29.md#fieldwrite-write-field-s7-1500) | x | - |
| [MOVE_BLK: Move block](FBD%20%28S7-1200%2C%20S7-1500%29.md#move_blk-move-block-s7-1200-s7-1500) | x | - |
| [SCATTER: Parse the bit sequence into individual bits](FBD%20%28S7-1200%2C%20S7-1500%29.md#scatter-parse-the-bit-sequence-into-individual-bits-s7-1200-s7-1500) | x | - |
| [SCATTER_BLK: Parse elements of an ARRAY of bit sequence into individual bits](FBD%20%28S7-1200%2C%20S7-1500%29.md#scatter_blk-parse-elements-of-an-array-of-bit-sequence-into-individual-bits-s7-1200-s7-1500) | x | - |
| [GATHER: Merge individual bits into a bit sequence](FBD%20%28S7-1200%2C%20S7-1500%29.md#gather-merge-individual-bits-into-a-bit-sequence-s7-1200-s7-1500) | x | - |
| [GATHER_BLK: Merge individual bits into multiple elements of an ARRAY of bit sequence](FBD%20%28S7-1200%2C%20S7-1500%29.md#gather_blk-merge-individual-bits-into-multiple-elements-of-an-array-of-bit-sequence-s7-1200-s7-1500) | x | - |
| [MOVE_BLK_VARIANT: Move block](FBD%20%28S7-1200%2C%20S7-1500%29.md#move_blk_variant-move-block-s7-1200-s7-1500) | x | - |
| [UMOVE_BLK: Move block uninterruptible](FBD%20%28S7-1200%2C%20S7-1500%29.md#umove_blk-move-block-uninterruptible-s7-1200-s7-1500) | x | - |
| [FILL_BLK: Fill block](FBD%20%28S7-1200%2C%20S7-1500%29.md#fill_blk-fill-block-s7-1200-s7-1500) | x | - |
| [UFILL_BLK: Fill block uninterruptible](FBD%20%28S7-1200%2C%20S7-1500%29.md#ufill_blk-fill-block-uninterruptible-s7-1200-s7-1500) | x | - |
| [?= Assignment attempt](FBD%20%28S7-1200%2C%20S7-1500%29.md#assignmentattempt-attempt-assignment-to-a-reference-s7-1500) | x | - |
| [SWAP: Swap](FBD%20%28S7-1200%2C%20S7-1500%29.md#swap-swap-s7-1200-s7-1500) | x | - |
| [ReadFromArrayDB: Read from the array data block](FBD%20%28S7-1200%2C%20S7-1500%29.md#readfromarraydb-read-from-array-data-block-s7-1500) | x | - |
| [WriteToArrayDB: Write to the array data block](FBD%20%28S7-1200%2C%20S7-1500%29.md#writetoarraydb-write-to-array-data-block-s7-1500) | x | - |
| [ReadFromArrayDBL: Read from the array data block in the load memory](FBD%20%28S7-1200%2C%20S7-1500%29.md#readfromarraydbl-read-from-array-data-block-in-load-memory-s7-1500) | x | - |
| [WriteToArrayDBL: Write to array data block in the load memory](FBD%20%28S7-1200%2C%20S7-1500%29.md#writetoarraydbl-write-to-array-data-block-in-load-memory-s7-1500) | x | - |
| [VariantGet: Read VARIANT tag value](FBD%20%28S7-1200%2C%20S7-1500%29.md#variantget-read-out-variant-tag-value-s7-1200-s7-1500) | x | - |
| [VariantPut: Write VARIANT tag value](FBD%20%28S7-1200%2C%20S7-1500%29.md#variantput-write-variant-tag-value-s7-1200-s7-1500) | x | - |
| [CountOfElements: Get number of ARRAY elements](FBD%20%28S7-1200%2C%20S7-1500%29.md#countofelements-get-number-of-array-elements-s7-1200-s7-1500) | x | - |
| [LOWER_BOUND: Read ARRAY low limit](FBD%20%28S7-1200%2C%20S7-1500%29.md#lower_bound-read-out-low-array-limit-s7-1200-s7-1500) | x | - |
| [UPPER_BOUND: Read ARRAY high limit](FBD%20%28S7-1200%2C%20S7-1500%29.md#upper_bound-read-out-high-array-limit-s7-1200-s7-1500) | x | - |
| [BLKMOV: Move block (S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#blkmov-move-block-s7-1500) | x | - |
| [UBLKMOV: Move block uninterruptible (S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#ublkmov-move-block-uninterruptible-s7-1500) | x | - |
| [FILL: Fill block (S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#fill-fill-block-s7-1500) | x | - |
| **Conversion operations** |  |  |
| [CONVERT: Convert value](FBD%20%28S7-1200%2C%20S7-1500%29.md#convert-convert-value-s7-1200-s7-1500) | x | - |
| [ROUND: Round numerical value](FBD%20%28S7-1200%2C%20S7-1500%29.md#round-round-numerical-value-s7-1200-s7-1500) | x | - |
| [CEIL: Generate next higher integer from floating-point number](FBD%20%28S7-1200%2C%20S7-1500%29.md#ceil-generate-next-higher-integer-from-floating-point-number-s7-1200-s7-1500) | x | - |
| [FLOOR: Generate next lower integer from floating-point number](FBD%20%28S7-1200%2C%20S7-1500%29.md#floor-generate-next-lower-integer-from-floating-point-number-s7-1200-s7-1500) | x | - |
| [TRUNC: Truncate numerical value](FBD%20%28S7-1200%2C%20S7-1500%29.md#trunc-truncate-numerical-value-s7-1200-s7-1500) | x | - |
| [SCALE_X: Scale](FBD%20%28S7-1200%2C%20S7-1500%29.md#scale_x-scale-s7-1200-s7-1500) | x | - |
| [NORM_X: Normalize](FBD%20%28S7-1200%2C%20S7-1500%29.md#norm_x-normalize-s7-1200-s7-1500) | x | - |
| VARIANT_TO_DB_ANY: Convert VARIANT to DB_ANY | x | - |
| DB_ANY_TO_VARIANT: Convert DB_ANY to VARIANT | x | - |
| [SCALE: Scale (S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#scale-scale-s7-1500) | x | - |
| [UNSCALE: Unscale (S7-1500)](FBD%20%28S7-1200%2C%20S7-1500%29.md#unscale-unscale-s7-1500) | x | - |
| **Program control operations** |  |  |
| Runtime control |  |  |
| [ENDIS_PW: Locking and unlocking passwords of the CPU access levels](FBD%20%28S7-1200%2C%20S7-1500%29.md#endis_pw-locking-and-unlocking-passwords-of-the-cpu-access-levels-s7-1200-s7-1500) | x | - |
| [RE_TRIGR: Restart cycle monitoring time](FBD%20%28S7-1200%2C%20S7-1500%29.md#re_trigr-restart-cycle-monitoring-time-s7-1200-s7-1500) | x | - |
| [STP: Exit program](FBD%20%28S7-1200%2C%20S7-1500%29.md#stp-exit-program-s7-1200-s7-1500) | x | - |
| [GET_ERROR: Get error locally](FBD%20%28S7-1200%2C%20S7-1500%29.md#get_error-get-error-locally-s7-1200-s7-1500) | x | - |
| [GET_ERR_ID: Get error ID locally](FBD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500) | x | - |
| [INIT_RD: Initialize all retain data](FBD%20%28S7-1200%2C%20S7-1500%29.md#init_rd-initialize-all-retain-data-s7-1500) | x | - |
| [WAIT: Configure time delay](FBD%20%28S7-1200%2C%20S7-1500%29.md#wait-configure-time-delay-s7-1500) | x | - |
| [RUNTIME: Runtime measurement](FBD%20%28S7-1200%2C%20S7-1500%29.md#runtime-measure-program-runtime-s7-1200-s7-1500) | x | - |
| **Word logic operations** |  |  |
| [AND: AND logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#and-and-logic-operation-s7-1200-s7-1500) | x | - |
| [OR: OR logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#or-or-logic-operation-s7-1200-s7-1500) | x | - |
| [XOR: EXCLUSIVE OR logic operation](FBD%20%28S7-1200%2C%20S7-1500%29.md#xor-exclusive-or-logic-operation-s7-1200-s7-1500) | x | - |
| [INV: Create ones complement](FBD%20%28S7-1200%2C%20S7-1500%29.md#invert-create-ones-complement-s7-1200-s7-1500) | x | - |
| [DECO: Decode](FBD%20%28S7-1200%2C%20S7-1500%29.md#deco-decode-s7-1200-s7-1500) | x | - |
| [ENCO: Encode](FBD%20%28S7-1200%2C%20S7-1500%29.md#enco-encode-s7-1200-s7-1500) | x | - |
| [SEL: Select](FBD%20%28S7-1200%2C%20S7-1500%29.md#sel-select-s7-1200-s7-1500) | x | - |
| [MUX: Multiplex](FBD%20%28S7-1200%2C%20S7-1500%29.md#mux-multiplex-s7-1200-s7-1500) | x | - |
| [DEMUX: Demultiplex](FBD%20%28S7-1200%2C%20S7-1500%29.md#demux-demultiplex-s7-1200-s7-1500) | x | - |
| **Shift and rotate** |  |  |
| [SHR: Shift right](FBD%20%28S7-1200%2C%20S7-1500%29.md#shr-shift-right-s7-1200-s7-1500) | x | - |
| [SHL: Shift left](FBD%20%28S7-1200%2C%20S7-1500%29.md#shl-shift-left-s7-1200-s7-1500) | x | - |
| [ROR: Rotate right](FBD%20%28S7-1200%2C%20S7-1500%29.md#ror-rotate-right-s7-1200-s7-1500) | x | - |
| [ROL: Rotate left](FBD%20%28S7-1200%2C%20S7-1500%29.md#rol-rotate-left-s7-1200-s7-1500) | x | - |
| **Additional instructions** |  |  |
| [DRUM: Implement sequencer](FBD%20%28S7-1200%2C%20S7-1500%29.md#drum-implement-sequencer-s7-1500) | x | - |
| [DCAT: Discrete control-timer alarm](FBD%20%28S7-1200%2C%20S7-1500%29.md#dcat-discrete-control-timer-alarm-s7-1500) | x | - |
| [MCAT: Motor control-timer alarm](FBD%20%28S7-1200%2C%20S7-1500%29.md#mcat-motor-control-timer-alarm-s7-1500) | x | - |
| [IMC: Compare input bits with the bits of the mask](FBD%20%28S7-1200%2C%20S7-1500%29.md#imc-compare-input-bits-with-the-bits-of-a-mask-s7-1500) | x | - |
| [SMC: Compare scan matrix](FBD%20%28S7-1200%2C%20S7-1500%29.md#smc-compare-scan-matrix-s7-1500) | x | - |
| [LEAD_LAG: Lead and lag algorithm](FBD%20%28S7-1200%2C%20S7-1500%29.md#lead_lag-lead-and-lag-algorithm-s7-1500) | x | - |
| [SEG: Create bit pattern for seven-segment display](FBD%20%28S7-1200%2C%20S7-1500%29.md#seg-create-bit-pattern-for-seven-segment-display-s7-1500) | x | - |
| [BCDCPL: Create tens complement](FBD%20%28S7-1200%2C%20S7-1500%29.md#bcdcpl-create-tens-complement-s7-1500) | x | - |
| [BITSUM: Count number of set bits](FBD%20%28S7-1200%2C%20S7-1500%29.md#bitsum-count-number-of-set-bits-s7-1500) | x | - |

### CMP>T: Greater than step activation time (S7-1500)

#### Description

You can use the "Greater than step activation time" instruction to monitor the total duration of a step in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T: Greater than step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T: Greater than step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T: Greater than step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T: Greater than step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T: Greater than step activation time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table shows the parameters of the "Greater than step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| IN2 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/30548494731_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.T is less than 100 ms, the RLO is "0". As soon as the activation time exceeds 100 ms, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>U: Greater than uninterrupted step activation time (S7-1500)

#### Description

You use the "Greater than uninterrupted step activation time" instruction to monitor the duration of a step, minus any faults, in supervision conditions. The times of any events or faults are not recorded and only the pure step duration is monitored.

In the programmed condition, the total activation time of a step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;U: Greater than uninterrupted step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;U: Greater than uninterrupted step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;U: Greater than uninterrupted step activation time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table shows the parameters of the "Greater than uninterrupted step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step minus the faults |
| IN2 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/30548570891_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.U minus possible faults is less than 100 ms, the RLO is "0". As soon as the activation time exceeds 100 ms, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>T_MAX: Greater than maximum step activation time  (S7-1500)

#### Description

You use the "Greater than maximum step activation time" instruction to monitor the maximum total duration of a step in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with the maximum duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1". If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T_MAX: Greater than maximum step activation time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T_MAX: Greater than maximum step activation time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T_MAX: Greater than maximum step activation time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table shows the parameters of the "Greater than maximum step activation time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| IN2 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/67756963083_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #STEP1.T is less than the maximum step activation time of #Step1.T_MAX, the RLO is "0". As soon as the maximum step activation time is exceeded, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Basics of step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-of-step-time-monitoring-s7-1500)
  
[Programming step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#programming-step-time-monitoring-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

### CMP>T_WARN: Greater than warning time (S7-1500)

#### Description

You use the "Greater than warning time" instruction to monitor the duration of a step and issue a warning when the time is exceeded in supervision conditions. The times of any events or errors are also recorded in the process.

In the programmed condition, the current or the last activation time of the step (Operand1) is compared with a defined duration (Operand2) in milliseconds. If the condition of the comparison is fulfilled, the instruction returns the result of logic operation (RLO) "1" and a warning is output. If the comparison condition is not fulfilled, the instruction returns RLO "0".

> **Note**
>
> **Status still displayed despite "inactive" instruction**
>
> Under the following requirements:
>
> - Prior to the instruction "CMP &gt;T_WARN: Greater than warning time" (with data type STRING, WSTRING), a condition (e.g. of a NO contact) is queried in the network.
> - "Monitoring on" is switched on.
> - A new result of the condition resets the network to FALSE. The instruction "CMP &gt;T_WARN: Greater than warning time" becomes inactive.
>
> Result:
>
> For the instruction "CMP &gt;T_WARN: Greater than warning time" (data type STRING, WSTRING), the previous status is still shown in the network.
>
> When you switch "Monitoring on" off and on again or scroll to a different network, the correct status of the instruction "CMP &gt;T_WARN: Greater than warning time" (data type STRING, WSTRING) is displayed again. The instruction "CMP &gt;T_WARN: Greater than warning time" is shown as grayed out in the network in the inactive status.

#### Parameters

The following table lists the parameters of the "Greater than warning time" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| IN1 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Current or last activation time of the step |
| IN2 | Input | Integers, floating-point numbers, timers, strings, DATE, DT, DTL, TOD, LTOD, LDT | I, Q, M, D, L or constant | Duration used for comparison |

#### Example

The following example shows the instruction in the network:

![Example](images/67777607819_DV_resource.Stream@PNG-de-DE.png)

As long as the activation time of #Step1.T does not exceed the warning time of #Step1.T_WARN, the RLO is "0". As soon as the warning time is exceeded, the RLO changes to "1".

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[Basic information on the status word (S7-1500)](Program%20flow%20control.md#basic-information-on-the-status-word-s7-1500)
  
[Basics of step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basics-of-step-time-monitoring-s7-1500)
  
[Programming step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#programming-step-time-monitoring-s7-1500)
  
[Memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#memory-areas-s7-1500)
  
[Basic information on GRAPH (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#basic-information-on-graph-s7-300-s7-400-s7-1500)

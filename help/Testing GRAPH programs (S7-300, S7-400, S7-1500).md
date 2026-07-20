---
title: "Testing GRAPH programs (S7-300, S7-400, S7-1500)"
package: ProgTestGRAPH34enUS
topics: 11
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing GRAPH programs (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
- [Specifying the test settings (S7-300, S7-400, S7-1500)](#specifying-the-test-settings-s7-300-s7-400-s7-1500)
- [Controlling a sequencer during testing (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-during-testing-s7-300-s7-400-s7-1500)

## Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)

### Introduction

You can display the program status of a GRAPH program to check the logic, consistency and function of a sequential control system.

In the process you can, for example, determine the following errors:

- Program errors, for example, shifts between the programmed steps and conditions and the actual process sequence
- Programming errors in the sequential control system, such as incorrectly defined monitoring times in supervisions

To be able to test a user program, an online connection to the CPU must be available.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger when testing during ongoing plant operation**  Testing while the plant is operating can cause serious damage to property or injury to persons if there are functional disturbances or program errors.  Make sure that no dangerous situations can arise before you conduct a test. |  |

> **Note**
>
> It is possible that another user can carry out a loading process on the selected CPU through joint parallel working on a CPU. If this load operation results in changes to the instance data block of the GRAPH block, the test is ended with program status for the GRAPH block and you receive an alarm in the Inspector window.

### Test functions of GRAPH

The following test functions are available for testing sequential control systems that were created in GRAPH:

- Program status for sequences
- Program status for conditions and actions
- Program status for interlocks and supervision
- Program status for permanent pre-instructions and post-instructions

During a test, you have the option to control the sequencer or to synchronize it with the current process status.

### Operating modes for testing GRAPH programs

The following three operating modes are available for the testing GRAPH programs:

- Automatic mode

  In this operating mode, the sequence automatically advances to the next step as soon as the transition is fulfilled.
- Semiautomatic mode

  In this operating mode, the sequence advances to the next step if one of the following conditions is fulfilled:

  - Transition is satisfied.
  - There is a rising signal edge at the "T_PUSH" parameter.
  - You advance by switching manually with the "Ignore transition" button.
- Manual mode

  In this operating mode, you can either advance from one step to the next manually or specifically select a step.

### System synchronization

If a process is brought to another state in manual mode, it may no longer be synchronized with the sequencer. To synchronize the process with the program once again, you can have the program look for synchronization points and subsequently perform the synchronization.

You can select from the following methods to find the synchronization points:

- Preceding transition satisfied

  All steps whose preceding transition has been fulfilled are selected.
- Interlock condition satisfied

  All steps whose interlock condition has been fulfilled are selected.

Only those steps for which the subsequent transition is not fulfilled are selected for both options. Next you can enable one or more of the proposed steps.

### Learning mode (S7-1500 only)

By testing with program status, you have the option of having the maximum step activation time and warning time determined by the system. You can use these times for your supervision conditions.

> **Note**
>
> For GRAPH blocks with a version lower than 2.0, the learning mode for determining the values of "T_MAX" and "T_WARN" is not available. You can change the version in the properties of the GRAPH block under "General &gt; Block".

---

**See also**

[Basics of testing the user program](Testing%20the%20user%20program.md#basics-of-testing-the-user-program)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)
  
[Overview of the test settings for GRAPH (S7-300, S7-400, S7-1500)](#overview-of-the-test-settings-for-graph-s7-300-s7-400-s7-1500)
  
[Controlling a sequencer (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-s7-300-s7-400-s7-1500)
  
[Acknowledging supervision errors (S7-300, S7-400, S7-1500)](#acknowledging-supervision-errors-s7-300-s7-400-s7-1500)
  
[Testing in various operating modes (S7-300, S7-400, S7-1500)](#testing-in-various-operating-modes-s7-300-s7-400-s7-1500)
  
[Performing a system synchronization (S7-300, S7-400, S7-1500)](#performing-a-system-synchronization-s7-300-s7-400-s7-1500)
  
[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)

## Specifying the test settings (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Overview of the test settings for GRAPH (S7-300, S7-400, S7-1500)](#overview-of-the-test-settings-for-graph-s7-300-s7-400-s7-1500)
- [Changing test settings (S7-300, S7-400, S7-1500)](#changing-test-settings-s7-300-s7-400-s7-1500)

### Overview of the test settings for GRAPH (S7-300, S7-400, S7-1500)

#### Overview

The following table provides an overview of the settings for testing GRAPH programs:

| Setting | Description |
| --- | --- |
| Track active step | The step of the sequencer which is active in each case is displayed in the single-step view or in the sequence view. |
| Skip steps | A step whose preceding or subsequent transition is valid will not be activated. The default setting of this option is adopted from the corresponding block settings.  This option is not available when you use the "Create minimized DB" option for the GRAPH function block. |
| Acknowledge supervision alarms | Specifies that supervision errors must be acknowledged before the program continues. This option overwrites the sequence property "Acknowledge supervision alarms" in the settings of the GRAPH function block and applies until the next download of the GRAPH instance data block. |
| Stop sequence | The sequencer is stopped, even if the next transition is fulfilled. |
| Stop timers | If this option is enabled, all step activation timers are stopped. If this option is disabled, all timers continue to run. |
| Process all interlocks | All interlocks, even those in step that are not active, are processed.  You can recognize the interlocks that are fulfilled in the sequence view. |
| Process all transitions | All transitions are always processed. You can recognize the transitions that are fulfilled in the sequence view. |
| Activate actions | Activates the actions in active steps. This option is enabled by default. When you disable this option, no additional actions are executed in active steps. |
| Activate supervisions | Activates the supervisions in active steps. This option is enabled by default. When you disable this option, the conditions of supervision are ignored in active steps. |
| Activate interlocks | Activates the interlocks in active steps. This option is enabled by default. When you disable this option, the conditions of the interlock are ignored in active steps. |

---

**See also**

[Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
  
[Changing test settings (S7-300, S7-400, S7-1500)](#changing-test-settings-s7-300-s7-400-s7-1500)

### Changing test settings (S7-300, S7-400, S7-1500)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Changing the test settings**  Keep in mind that changes to the test settings can have unintended effects on the process. Make sure that no dangerous states can occur before you change the test settings. |  |

#### Requirement

A GRAPH function block is open.

#### Procedure

To change the test settings of GRAPH, follow these steps:

1. Start the test with program status for the GRAPH function block.

   See also: [Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)
2. Open the "Testing" task card.
3. Change the settings in the "Test settings" pallet.

---

**See also**

[Overview of the test settings for GRAPH (S7-300, S7-400, S7-1500)](#overview-of-the-test-settings-for-graph-s7-300-s7-400-s7-1500)

## Controlling a sequencer during testing (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Controlling a sequencer (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-s7-300-s7-400-s7-1500)
- [Acknowledging supervision errors (S7-300, S7-400, S7-1500)](#acknowledging-supervision-errors-s7-300-s7-400-s7-1500)
- [Testing in various operating modes (S7-300, S7-400, S7-1500)](#testing-in-various-operating-modes-s7-300-s7-400-s7-1500)
- [Performing a system synchronization (S7-300, S7-400, S7-1500)](#performing-a-system-synchronization-s7-300-s7-400-s7-1500)
- [Calculating times for T_MAX and T_WARN when testing (S7-1500)](#calculating-times-for-t_max-and-t_warn-when-testing-s7-1500)

### Controlling a sequencer (S7-300, S7-400, S7-1500)

You can re-initialize the sequencer during testing with the program status. The sequencer then starts with the initial steps once again. You also have the option to disable all steps for testing.

#### Requirement

The program status is displayed.

#### Initialize sequencer

To initialize the sequencer, follow these steps:

1. Open the "Testing" task card.
2. Click the "Initialize" in the "Sequence control" pallet.

   The sequencer is executed starting with the initial steps.

#### Disable all steps

To disable all steps for testing of a sequencer, follow these steps:

1. Open the "Testing" task card.
2. Click "Disable all" in the "Sequence control" pallet.

   All steps of the sequencer are disabled.

---

**See also**

[Acknowledging supervision errors (S7-300, S7-400, S7-1500)](#acknowledging-supervision-errors-s7-300-s7-400-s7-1500)
  
[Testing in various operating modes (S7-300, S7-400, S7-1500)](#testing-in-various-operating-modes-s7-300-s7-400-s7-1500)
  
[Performing a system synchronization (S7-300, S7-400, S7-1500)](#performing-a-system-synchronization-s7-300-s7-400-s7-1500)
  
[Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)
  
[Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)

### Acknowledging supervision errors (S7-300, S7-400, S7-1500)

You can specify in the test settings that supervision errors have to acknowledged during testing before the program continues.

#### Requirement

The program status is displayed.

#### Procedure

To acknowledge supervision errors, follow these steps:

1. Open the "Testing" task card.
2. Click "Acknowledge - (V) -" in the "Sequence control" pallet.

---

**See also**

[Controlling a sequencer (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-s7-300-s7-400-s7-1500)
  
[Testing in various operating modes (S7-300, S7-400, S7-1500)](#testing-in-various-operating-modes-s7-300-s7-400-s7-1500)
  
[Performing a system synchronization (S7-300, S7-400, S7-1500)](#performing-a-system-synchronization-s7-300-s7-400-s7-1500)
  
[Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
  
[Overview of the test settings for GRAPH (S7-300, S7-400, S7-1500)](#overview-of-the-test-settings-for-graph-s7-300-s7-400-s7-1500)
  
[Changing test settings (S7-300, S7-400, S7-1500)](#changing-test-settings-s7-300-s7-400-s7-1500)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)
  
[Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)

### Testing in various operating modes (S7-300, S7-400, S7-1500)

#### Requirement

The program status is displayed.

#### Testing in automatic mode

Proceed as follows to test a sequencer in automatic mode:

1. Open the "Testing" task card.
2. Select "Automatic" as operating mode in the "Sequence control" pallet.

#### Testing in semiautomatic mode

Proceed as follows to test a sequencer in semiautomatic mode:

1. Open the "Testing" task card.
2. Select "Semiautomatic mode" as operating mode in the "Sequence control" pallet.
3. When switching does not continue automatically by a fulfilled transition or via the parameter "T_PUSH", click the "Ignore transition" button.

#### Testing in manual mode

To test a sequencer in manual mode, follow these steps:

1. Open the "Testing" task card.
2. Select "Manual mode" as operating mode in the "Sequence control" pallet.
3. Advance to another step:

   - If you want to enable the next step, click the "Next" button.
   - If you want to enable or disable any given step, enter the step number in the "Select step manually" field or select a step in the sequencer and click the "Enable" or "Disable" button.

---

**See also**

[Controlling a sequencer (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-s7-300-s7-400-s7-1500)
  
[Acknowledging supervision errors (S7-300, S7-400, S7-1500)](#acknowledging-supervision-errors-s7-300-s7-400-s7-1500)
  
[Performing a system synchronization (S7-300, S7-400, S7-1500)](#performing-a-system-synchronization-s7-300-s7-400-s7-1500)
  
[Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)
  
[Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)

### Performing a system synchronization (S7-300, S7-400, S7-1500)

#### Requirement

- The program status is displayed.
- The test takes place in "Manual mode" operating mode.

#### Procedure

Proceed as follows to perform a system synchronization:

1. Open the "Testing" task card.
2. Select the "Enable synchronization" check box in the "Sequence control" pallet.
3. Select one of these two methods for locating synchronization points:

   - "Preceding transition satisfied"

     All steps are marked whose preceding transitions are satisfied and whose subsequent transitions are not satisfied.
   - "Interlock condition satisfied"

     All steps are marked whose interlocks are satisfied and whose subsequent transitions are not satisfied.
4. Select a step with which the system synchronization should start. You can also select multiple steps.
5. Click the "Activate" button.

#### Result

The process and the sequencers are synchronized with each other.

---

**See also**

[Basics on testing GRAPH programs (S7-300, S7-400, S7-1500)](#basics-on-testing-graph-programs-s7-300-s7-400-s7-1500)
  
[Controlling a sequencer (S7-300, S7-400, S7-1500)](#controlling-a-sequencer-s7-300-s7-400-s7-1500)
  
[Acknowledging supervision errors (S7-300, S7-400, S7-1500)](#acknowledging-supervision-errors-s7-300-s7-400-s7-1500)
  
[Testing in various operating modes (S7-300, S7-400, S7-1500)](#testing-in-various-operating-modes-s7-300-s7-400-s7-1500)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)
  
[Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)

### Calculating times for T_MAX and T_WARN when testing (S7-1500)

With the learning mode, you can have the values for the maximum step activation time and warning time for the entire duration of a step determined by the system. To be able to do this, each step must be executed at least once. The longer the learning mode is active, the more often a step is executed and the more precise the learned values are. The maximum step activation time and the warning time for a step are made up of the learned time and an additive threshold. You specify the additive thresholds for the supervision and the warning yourself.

When learning mode is ended, the values are stored in the instance data block on the device. You can also save the values in the offline instance data block. The values are adopted as the start values for the static parameters "T_MAX" and "T_WARN". Following this, the learned values are used in the comparison instructions "CMP&gt;T_MAX" and "CMP&gt;T_WARN".

You can reset the times for "T_MAX" and "T_WARN" determined in the learning mode to their default values at any time. This resets both the online and the offline data block.

> **Note**
>
> For GRAPH blocks with a version lower than 2.0, the learning mode for determining the values of "T_MAX" and "T_WARN" is not available. You can change the version in the properties of the GRAPH block under "General &gt; Block".

#### Requirement

- The identical GRAPH function block exists in the device.
- Step time monitoring is programmed for at least one step.

#### Determining times

To determine the maximum step activation time and the warning time using the learning mode, follow these steps:

1. Open the GRAPH function block.
2. Enable the test with program status for the GRAPH function block.

   See also: [Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)
3. Open the "Testing" task card.
4. Enter the additive threshold for the supervision as a percentage.
5. Enter the additive threshold for warnings as a percentage.
6. Select the "Enable learning mode" check box.
7. Wait until each step has been active at least once.
8. Clear the "Enable learning mode" check box.

   The "Save learned times" dialog opens.
9. If you want to save the learned times in the offline instance data block, click "OK".

   The learned times are entered in the static parameters "T_MAX" and "T_WARN" of the steps that were active during learning mode.

**Note**

Regardless of your selection, the learned times are entered in the online instance data block.

#### Resetting times

To reset the times, follow these steps:

1. Open the GRAPH function block.
2. Enable the test with program status for the GRAPH function block.

   See also: [Switching test with program status on/off](Testing%20the%20user%20program.md#switching-test-with-program-status-onoff)
3. Open the "Testing" task card.
4. Click the "Reset learned times" button.

   The values for "T_MAX" and "T_WARN" in the instance data block are reset to the default values.

---

**See also**

[Using step time monitoring (S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#using-step-time-monitoring-s7-1500)

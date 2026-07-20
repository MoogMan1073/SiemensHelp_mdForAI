---
title: "Testing with breakpoints (S7-300, S7-400, S7-1500)"
package: ProgTestBreakpoints34enUS
topics: 17
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing with breakpoints (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
- [Security information for testing with breakpoints (S7-300, S7-400, S7-1500)](#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
- [Safety information for testing with breakpoints (S7-300, S7-400, S7-1500)](#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
- [Rules for testing with breakpoints (S7-300, S7-400, S7-1500)](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
- [Status display for breakpoints (S7-300, S7-400, S7-1500)](#status-display-for-breakpoints-s7-300-s7-400-s7-1500)
- [Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)](#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)
- [Setting breakpoints (S7-300, S7-400, S7-1500)](#setting-breakpoints-s7-300-s7-400-s7-1500)
- [Enabling breakpoints (S7-300, S7-400, S7-1500)](#enabling-breakpoints-s7-300-s7-400-s7-1500)
- [Disabling breakpoints (S7-300, S7-400, S7-1500)](#disabling-breakpoints-s7-300-s7-400-s7-1500)
- [Navigating to the breakpoints (S7-300, S7-400, S7-1500)](#navigating-to-the-breakpoints-s7-300-s7-400-s7-1500)
- [Deleting breakpoints (S7-300, S7-400, S7-1500)](#deleting-breakpoints-s7-300-s7-400-s7-1500)
- [Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)](#testing-with-breakpoints-in-single-step-mode-s7-300-s7-400-s7-1500)
- ["Run to cursor" function (S7-300, S7-400, S7-1500)](#run-to-cursor-function-s7-300-s7-400-s7-1500)
- [Monitoring tags when the breakpoint is reached (S7-1500)](#monitoring-tags-when-the-breakpoint-is-reached-s7-1500)
- [Modifying tags when the breakpoint reached (S7-300, S7-400, S7-1500)](#modifying-tags-when-the-breakpoint-reached-s7-300-s7-400-s7-1500)
- [Resuming program execution (S7-300, S7-400, S7-1500)](#resuming-program-execution-s7-300-s7-400-s7-1500)

## Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)

### Introduction

You can test blocks you created in the textual programming languages STL and SCL by having each instruction individually executed, step by step. To do this, you set breakpoints into the program code, establish an online connection and enable the breakpoints in the CPU.

The program code in STL and SCL can also be tested with breakpoints if this code is inserted into a LAD/FBD block.

As of TIA Portal V15, the following CPU families support the setting of breakpoints:

- S7-300 and S7-400
- S7-1500, as of firmware version V2.5

> **Note**
>
> **Safety information for testing with breakpoints**
>
> Because you are interfering with the running process when testing with breakpoints, you should first be become familiar and follow the safety instructions for testing with breakpoints.
>
> For more details, see:
>
> [Safety information for testing with breakpoints](#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
>
> [Security information for testing with breakpoints](#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

> **Note**
>
> **Compatibility rules for breakpoints**
>
> - S7-1500 CPUs with older firmware versions (&lt;2.5) do not support breakpoints.
> - Breakpoints are not available for projects with older firmware versions that have been upgraded to the TIA Portal V15.
> - Breakpoints are also not supported if a CPU S7-1500 with firmware version V2.5 is reset to an older firmware version. In this case, any breakpoints in the code are no longer displayed.
> - Blocks that were created in older TIA Portal versions must be re-compiled on a CPU S7-1500 as of firmware V2.5 in order to use breakpoints.

### Testing with breakpoints

If you have set valid breakpoints and have enabled them, you can run the program up to the first breakpoint in single-step testing and continue from there step-by-step using the following functions:

- Run

  Continue to the next enabled breakpoint.
- Run to cursor

  Continue to the cursor position.
- Step over (for S7-300/400 only)

  The currently selected instruction is executed.
- Step into (for S7-300/400 only)

  Jump into a lower-level block or call a lower-level block.
- Step out (for S7-300/400 only)

  If a block call is being processed and the program execution in the called block was interrupted at a breakpoint, you can use "Step out" to jump back to the called block.

You can set any number of breakpoints in the program code. The number of breakpoints that can be enabled in the CPU depends on the CPU. You can specify the time at which the program execution of individual breakpoints should be interrupted for a CPU S7-400 via the call environment.

> **Note**
>
> - If you terminate the online connection to the CPU, the breakpoints are disabled.
> - The breakpoints are not saved with the project.
> - If you close the project, the breakpoints are lost.

---

**See also**

[Safety information for testing with breakpoints (S7-300, S7-400, S7-1500)](#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Rules for testing with breakpoints (S7-300, S7-400, S7-1500)](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

## Security information for testing with breakpoints (S7-300, S7-400, S7-1500)

### Disclaimer for the use of breakpoints with SIMATIC S7-1500

The SIMATIC S7-1500 supports the use of breakpoints for specifically stopping the program sequence for locating errors in the user program. When a configured breakpoint is reached by the user program, the processing cycle of the SIMATIC S7-1500 is stopped at it. The output values for the connected output modules are stopped in their respective states and (in contrast to the SIMATIC S7-300/S7-400) neither reset nor set to the configured substitute values. In addition, the SIMATIC S7-1500 can no longer react to input values of input groups in this state.

Keep this information in mind when operating your system and use breakpoints only if the above-described behavior in your application cannot result in damage to the environment, objects or injuries to persons.

Each customer is responsible for the proper and safe operation of the products and their installation within the applicable regulations.

Our liability for damages resulting from your use of breakpoints is excluded regardless of the legal basis unless required by law, e.g. according to the product liability act in cases of willful misconduct, gross negligence, personal injury or death, failure to achieve guaranteed characteristics, fraudulent concealment of a defect or in case of breach of fundamental contractual obligations.

The liability in case of a breach of fundamental contractual obligations, however, is limited to the foreseeable damages typical of the contract, unless intention or gross negligence are present or in case of mandatory liability due to injuries to life, body or health.

A change in the burden of proof to your disadvantage is not associated with this provision.

## Safety information for testing with breakpoints (S7-300, S7-400, S7-1500)

### Safety information for testing with breakpoints

You can test with breakpoints on all CPU series from the TIA Portal V15. However, the behavior is different when testing with breakpoints within the CPU series.

Since you interrupt the running process when testing with breakpoints, you should pay attention to the following safety instructions.

### Testing with breakpoints on an S7-300, S7-400 and S7-1500 CPU

The following information applies when testing with breakpoints on an S7-300, S7-400 and S7-1500 CPU!

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  Be aware that an incorrect action when executing the "Test with breakpoints" function can:  - Harm persons or pose a health hazard. - Cause damage to machinery or the entire plant.   Testing with breakpoints should **not** be used during plant operation!  Setting breakpoints in the standard user program results in errors in the safety program.   If you nevertheless want to use breakpoints for testing, you must disable safety mode.   The following errors will occur even when safety mode is disabled and breakpoints are used:  - Error in communication with the fail-safe I/O - Errors during safety-related CPU‑CPU communication |  |

### Testing with breakpoints on an S7-1500 CPU

The following information only applies when testing with breakpoints on an S7-1500 CPU, as of firmware V2.5!

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **Prevent personal injury and material damage!**  - If you enable the "Test with breakpoints" function, the outputs remain enabled. The outputs retain their last status and are no longer updated when the CPU goes to "HOLD" mode! - When testing with breakpoints, enabled outputs are **not** disabled and are **not** reset to safe substitute values.    This can, for example, cause motors to continue running and valves to remain open. - Testing with breakpoints should **not** be used during plant operation! - Especially where a Motion Control TO object is used in the CPU, it must **not** be tested with breakpoints. In this case, if a breakpoint is enabled and is reached, the CPU immediately goes to "STOP" after "HOLD".    For example, this can cause connected motors and drives to be stopped, the loss of axis homing and the synchronous operation to be canceled in an uncontrolled manner. - Testing with breakpoints can increase the cycle time of the CPU. - Before you start the "Test with breakpoints" function, make sure that no one is running this function on the same CPU. - Setting breakpoints in the standard user program results in errors in the safety program. When testing with breakpoints, enabled outputs of the S7-1500 are **not** disabled. This means that the F-modules automatically switch to the safe state after the configured monitoring time has elapsed. |  |

### Testing with breakpoints on an S7-1500 CPU

The following information only applies when testing with breakpoints on an S7-1500 CPU, as of firmware V2.5!

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Incorrect display of tag values during monitoring**  - Due to the optimization of the code, values that have not yet been reached can also be displayed as already assigned. Because these values could already be calculated, they are also displayed in black. - When monitoring arrays within loops it may happen that incorrect values are displayed. In these cases only those values are displayed as correct that are within the loop and before a breakpoint. Displayed values that are located after the breakpoint within the loop and the displayed value at the breakpoint may not be correct. The code is correctly executed independent of the incorrect display. - Loops can also be generated through specific instructions (for example, "Label" and "GOTO" in SCL and "LOOP" in STL). In these cases, too, only those values are displayed as correct that are within the loop and before a breakpoint. Displayed values that are located after the breakpoint within the loop and the displayed value at the breakpoint may not be correct. The code is correctly executed independent of the incorrect display. |  |

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Rules for testing with breakpoints (S7-300, S7-400, S7-1500)](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

## Rules for testing with breakpoints (S7-300, S7-400, S7-1500)

### Introduction

Depending on the CPU and programming language used, the rules for setting breakpoints listed below apply.

> **Note**
>
> Breakpoints must be enabled after they are set before you can execute them.
>
> Breakpoints are **not** saved in the project. If you close the project, the breakpoints are lost.

### Rules for setting breakpoints for S7-1500 CPUs in STL and SCL

Breakpoints can be set at the beginning of each line of code, but may be invalidated if this code is optimized during compilation.

If a breakpoint is set on a line of code optimized during compilation, this breakpoint is marked as "invalid" and cannot be enabled.

Therefore, it is helpful to set breakpoints at the beginning of logically related sections of code.

### Valid breakpoints in STL

Valid breakpoints can be set in STL, for example, at the following positions:

- On the first instruction at the beginning of an STL network.
- Before an instruction with operand read access following an instruction with write operand access.
- On the first instruction after a conditional jump.
- Before and after block calls.

### Valid breakpoints in SCL

Valid breakpoints can be always be set in all instructions in SCL.

Exceptions are:

- If more than one instruction is compiled by the compiler, only the first breakpoint before the start of the first instruction remains valid.
- No breakpoints are possible at the start or end of control structures (REPEAT, END_IF, END_FOR, END_WHILE, END_CASE).

## Status display for breakpoints (S7-300, S7-400, S7-1500)

### Introduction

The display for breakpoints is identical in the left column of the open program editor as well as under "Breakpoints" in the "Testing" task card.

Changes you make are immediately updated in the Program editor as well as in the "Testing" task card.

Breakpoints are visualized with different symbols depending on their respective status.

### Displaying the status for breakpoints

The following table shows how breakpoints are displayed in the Program editor depending on their status in the program code:

Displaying the status for breakpoints in an S7-300/400 and S7-1500 CPU:

| Icon | Meaning |
| --- | --- |
| ![Displaying the status for breakpoints](images/100865231627_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is inactive |
| ![Displaying the status for breakpoints](images/102079813387_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is inactive with condition, (for example, call environment for the breakpoint is defined) |
| ![Displaying the status for breakpoints](images/102079822219_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is inactive, program execution is at this point |
| ![Displaying the status for breakpoints](images/102079869451_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is inactive, has a condition (for example, call environment for the breakpoint is defined) and the program execution is at this point. |
| ![Displaying the status for breakpoints](images/102080010635_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is active |
| ![Displaying the status for breakpoints](images/102080070667_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is active with condition, (for example, call environment for the breakpoint is defined) |
| ![Displaying the status for breakpoints](images/102080079499_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is active and the program execution is at this point. |
| ![Displaying the status for breakpoints](images/102080101131_DV_resource.Stream@PNG-de-DE.png) | Breakpoint is active, has a condition (for example, call environment for the breakpoint is defined) and the program execution is at this point. |
| ![Displaying the status for breakpoints](images/102080157195_DV_resource.Stream@PNG-de-DE.png) | Program execution is at this point |

The following symbols are also available in the S7-1500 CPU family as of firmware V2.5:

| Icon | Meaning |
| --- | --- |
| ![Displaying the status for breakpoints](images/104102654475_DV_resource.Stream@PNG-de-DE.png) | The breakpoint is disabled and cannot be enabled.   Possible causes:  - This breakpoint can no longer be reached after compiling because of code optimizations. - The breakpoint cannot be enabled because a call environment has been defined for monitoring the block.   For more on this, see: [Rules for testing with breakpoints](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500) |
| ![Displaying the status for breakpoints](images/104056774027_DV_resource.Stream@PNG-de-DE.png) | The breakpoint is inactive and cannot be enabled and the program execution is at this point.  Possible causes:  - The breakpoint cannot be enabled because a call environment has been defined for monitoring the block.   For more on this, see: [Rules for testing with breakpoints](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500) |

---

**See also**

[Rules for testing with breakpoints (S7-300, S7-400, S7-1500)](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

## Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)

### Introduction

By setting the call environment, you can specify when the program is interrupted at the breakpoints.

However, you can only set a call environment for S7-400 CPUs. If you are using a different CPU, it is **not** possible to set a call environment for a breakpoint.

The following rules apply to setting a call environment for monitoring blocks:

**Valid for S7-1500er CPUs as of firmware version V2.5:**

- As soon as a breakpoint is enabled in a block, it is **not** possible to configure a call environment for monitoring.
- In the other direction, a breakpoint in a block **cannot** be enabled if a call environment has already been configured.
- If you attempt to use both functionalities, you are shown an error message with information about how to proceed.

### Requirement

- There are valid breakpoints in the program.

- The CPU supports the use of breakpoints and configuration of a call environment.

### Procedure

To set the call environment for a breakpoint, follow these steps:

1. Open the "Testing" task card.
2. On the "Breakpoints" pane, click the "..." button after the breakpoint for which you want to set the call environment.

   The "Call environment of a block" dialog opens.
3. Select the condition you want to apply.

   See also: [Basics of the call environment](Testing%20the%20user%20program.md#basics-of-the-call-environment)
4. Confirm your selection with "OK".

### Result

The call environment is specified for the breakpoint and the symbol for the breakpoint changes from a single gray circle to a gray circle with vertical lines before and after it.

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting breakpoints (S7-300, S7-400, S7-1500)](#setting-breakpoints-s7-300-s7-400-s7-1500)
  
[Enabling breakpoints (S7-300, S7-400, S7-1500)](#enabling-breakpoints-s7-300-s7-400-s7-1500)
  
[Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)](#testing-with-breakpoints-in-single-step-mode-s7-300-s7-400-s7-1500)
  
[Deleting breakpoints (S7-300, S7-400, S7-1500)](#deleting-breakpoints-s7-300-s7-400-s7-1500)

## Setting breakpoints (S7-300, S7-400, S7-1500)

### Introduction

Breakpoints can be set in the program code beginning with TIA Portal V15 for STL and SCL with a CPU S7-300, S7-400 and S7-1500 as of firmware V2.5.

To use the breakpoint functionality, older projects must be re-compiled with the new version of the TIA Portal.

There are several ways to set breakpoints:

- From the "Online" menu &gt; "Breakpoints" &gt; "Set breakpoint".

  This menu command is only visible if the cursor is not placed in the block interface in an open block.
- Via the shortcut menu "Set breakpoint".
- Use the icons under the "Breakpoints" button in the "Testing" task card.
- Via the keyboard command "CTRL+Shift+F9"
- Click on the gray column before the line number in the opened block.

Newly set breakpoints are initially disabled by default and must first be enabled before execution.

See also:

[Security information for testing with breakpoints](#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

[Safety information for testing with breakpoints](#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

[Rules for testing with breakpoints](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

### Requirement

You are working on a CPU S7-300, S7-400 or S7-1500 as of firmware V2.5, which supports breakpoints.

The block was created in STL or SCL.

To set breakpoints in the startup OB (OB 100), the CPU must be in STOP mode.

### Procedure

To set a breakpoint in the program code, follow these steps:

1. Open the block in which you want to set a breakpoint.
2. Right-click in the line in which you want to set the breakpoint and double-click in the gray column in front of the line number.
3. Select the "Set breakpoint" command in the shortcut menu.

Or:

1. Open the block in which you want to set a breakpoint.
2. On the line for which you want to set the breakpoint, click on the gray column in front of the line number.

### Result

A breakpoint is set in the program code. The breakpoint is displayed in the "Breakpoints" pane of the "Testing" task card and the breakpoint is also displayed as a grey circle in front of the corresponding line in the program code. Before the program is interrupted at the newly set breakpoint, the breakpoint must first be enabled.

> **Note**
>
> **Setting and enabling breakpoints during monitoring**
>
> As of TIA Portal V15, you can also set breakpoints while block monitoring is active.
>
> You can also enable breakpoints with a CPU S7-1500 as of firmware V2.5 while block monitoring is active.

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)](#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)
  
[Enabling breakpoints (S7-300, S7-400, S7-1500)](#enabling-breakpoints-s7-300-s7-400-s7-1500)
  
[Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)](#testing-with-breakpoints-in-single-step-mode-s7-300-s7-400-s7-1500)
  
[Deleting breakpoints (S7-300, S7-400, S7-1500)](#deleting-breakpoints-s7-300-s7-400-s7-1500)
  
[Security information for testing with breakpoints (S7-300, S7-400, S7-1500)](#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Safety information for testing with breakpoints (S7-300, S7-400, S7-1500)](#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Rules for testing with breakpoints (S7-300, S7-400, S7-1500)](#rules-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

## Enabling breakpoints (S7-300, S7-400, S7-1500)

### Introduction

To be able to use breakpoints when testing, the set breakpoints must first be enabled.

Enabling breakpoints installs and activates them on the CPU.

You can enable breakpoints either individually or all together.

You have the option to edit breakpoints using the "Testing" task card or alternatively using the Online menu and the shortcut menu.

**Valid for S7-1500er CPUs as of firmware version V2.5:**

- As soon as a breakpoint is enabled in a block, it is **not** possible to configure a call environment for monitoring.
- In the other direction, a breakpoint in a block **cannot** be enabled if a call environment has already been configured.
- If you attempt to use both functionalities, you are shown an error message with information about how to proceed.

> **Note**
>
> The number of breakpoints that can be enabled on the CPU depends on the particular CPU.
>
> Once you have reached the maximum number, you cannot enable any more breakpoints.
>
> Because the single step functions "Step over", "Step into" and "Run to cursor" are also used as breakpoints, they also cannot be performed when the maximum number of breakpoints is reached. Before you can enable further breakpoints or use these single step functions, you first need to disable breakpoints already enabled.

> **Note**
>
> **Enabling breakpoints during monitoring**
>
> As of TIA Portal V15, breakpoints can be enabled with CPU S7-1500 as of firmware V2.5 even when the block monitoring is active.

### Requirement

- Valid breakpoints were set.
- There is an online connection to the CPU and this CPU supports the use of breakpoints.
- The maximum number of breakpoints that can be enabled for the CPU has not been reached.
- The offline and the online blocks on the CPU are identical.

### Enabling individual breakpoints

To enable individual breakpoints, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Right-click on the breakpoint you want to enable.
3. Select the "Enable breakpoint" command in the shortcut menu.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Enabling breakpoints on a CPU S7-1500 as of firmware version V2.5**  As soon as you enable a breakpoint on a CPU S7-1500 as of V2.5, you are informed that the output values for the connected output modules are stopped in their respective state and (in contrast to SIMATIC S7-300/S7-400) neither reset nor set to the configured substitute values. In addition, the SIMATIC S7-1500 can no longer react to input values of input groups in this state.  This information is shown to you only once in each online session. |  |

### Result

The selected breakpoint is installed on the CPU and enabled and the program is interrupted at the breakpoint when it reaches that point in the program. The display of the breakpoint changes from a gray circle to a red circle.

### Enabling all breakpoints

To enable all breakpoints, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Make sure that no breakpoint is selected.
3. Click "Enable all breakpoints" in the toolbar of the "Breakpoints" pane.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Enabling breakpoints on a CPU S7-1500 as of firmware version V2.5**  As soon as you enable a breakpoint on a CPU S7-1500 as of firmware version V2.5, you are informed that the output values for the connected output modules are stopped in their respective state and (in contrast to SIMATIC S7-300/S7-400) neither reset nor set to the configured substitute values. In addition, the SIMATIC S7-1500 can no longer react to input values of input groups in this state.  This information is shown to you only once in each online session. |  |

### Result

Depending on the capacity of the CPU, all breakpoints are installed and enabled on the CPU and the program is interrupted at all breakpoints that are reached when it executes.

- If you have set more breakpoints than allowed by the CPU, only the permitted number of breakpoints is enabled.
- The selection of which breakpoints are enabled can change in runtime.
- Repeatedly executing the function can produce different results.

The display of the enabled breakpoints changes from gray circles to red circles.

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting breakpoints (S7-300, S7-400, S7-1500)](#setting-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)](#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)
  
[Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)](#testing-with-breakpoints-in-single-step-mode-s7-300-s7-400-s7-1500)
  
[Deleting breakpoints (S7-300, S7-400, S7-1500)](#deleting-breakpoints-s7-300-s7-400-s7-1500)
  
[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)

## Disabling breakpoints (S7-300, S7-400, S7-1500)

### Introduction

You can disable enabled breakpoints either individually or all together. After you have disabled breakpoints, they are ignored when the program executes.

You have the option to edit breakpoints using the "Testing" task card or alternatively using the Online menu and the shortcut menu.

> **Note**
>
> **Important facts about breakpoints**
>
> - If you terminate the online connection to the CPU, the breakpoints are disabled.
> - The breakpoints are not saved with the project.
> - If you close the project, the breakpoints are lost.

> **Note**
>
> **Disabling breakpoints during monitoring**
>
> As of TIA Portal V15, breakpoints can also be disabled while block monitoring is active.

### Requirement

- Valid breakpoints were set and enabled.
- There is an online connection to the CPU and this CPU supports the use of breakpoints.

### Disabling individual breakpoints

To disable individual breakpoints, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Right-click the breakpoint that you want to disable.
3. Select the "Disable breakpoint" command in the shortcut menu.

### Result

The selected breakpoint is uninstalled on the CPU and disabled and the program is no longer interrupted at the breakpoint. The display of the breakpoint changes from a red circle to a gray circle.

### Disabling all breakpoints

To disable all breakpoints, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Make sure that no breakpoint is selected.
3. Click "Disable all breakpoints" on the toolbar of the "Breakpoints" pane.

### Result

All breakpoints are uninstalled on the CPU and disabled and the program is no longer interrupted at any breakpoint. The display of the breakpoints changes from red circles to gray circles.

## Navigating to the breakpoints (S7-300, S7-400, S7-1500)

### Introduction

To navigate to the breakpoints in your program, you can either jump from breakpoint to breakpoint or to the point in the program where a specific breakpoint is located.

### Navigating from breakpoint to breakpoint

To navigate from breakpoint to breakpoint in your program, follow these steps:

1. Open a block and select the programming editor.
2. In the menu "Online &gt; Breakpoints", select "Go to next breakpoint" to jump to the next breakpoint after the current cursor position. When you reach the last breakpoint, you jump to the first breakpoint.
3. In the menu "Online &gt; Breakpoints", select "Go to previous breakpoint" to jump to the previous breakpoint before the current cursor position. When you reach first breakpoint, you jump to the last breakpoint.

### Navigating to a specific breakpoint

To navigate to a specific breakpoint in your program, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Double-click on the breakpoint to which you want to navigate.

   The block with the breakpoint is displayed in the programming editor and the line with the breakpoint is highlighted.

Or:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Right-click on the breakpoint to which you want to navigate.
3. Select the "Go to breakpoint" command in the shortcut menu.

   The block with the breakpoint is displayed in the programming editor and the line with the breakpoint is highlighted.

## Deleting breakpoints (S7-300, S7-400, S7-1500)

### Introduction

You can delete breakpoints either individually or all together.

Alternatively, you can delete breakpoints as follows:

- From the menu "Online &gt; Breakpoints &gt; Set/delete breakpoints", or "Online &gt; Breakpoints &gt; Delete all".
- Via the corresponding shortcut menu commands.
- Using the corresponding keyboard commands (CTRL+Shift+F9).
- Using the commands in the "Testing" task card.

> **Note**
>
> - If you terminate the online connection to the CPU, the breakpoints are disabled.
> - The breakpoints are not saved with the project.
> - If you close the project, the breakpoints are lost.

> **Note**
>
> **Deleting breakpoints during monitoring**
>
> As of TIA Portal V15, breakpoints can be deleted with CPU S7-1500 as of firmware V2.5 even when the block monitoring is active.

### Deleting individual breakpoints

To delete an individual breakpoint from the program, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Select the breakpoint you want to delete.
3. Right-click on the selected breakpoint.
4. Select the "Delete breakpoint" command in the shortcut menu.

Or:

1. Open the block in which you want to delete a breakpoint.
2. Click in the line containing the breakpoint you want to delete and click in the gray column in front of the row number.

### Result

The selected breakpoint is deleted.

### Deleting all breakpoints

To delete all breakpoints, follow these steps:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Click "Delete Breakpoints" in the toolbar of the "Breakpoints" pane.

### Result

All existing breakpoints are deleted.

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting breakpoints (S7-300, S7-400, S7-1500)](#setting-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)](#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)
  
[Enabling breakpoints (S7-300, S7-400, S7-1500)](#enabling-breakpoints-s7-300-s7-400-s7-1500)
  
[Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)](#testing-with-breakpoints-in-single-step-mode-s7-300-s7-400-s7-1500)

## Testing with breakpoints in single step mode (S7-300, S7-400, S7-1500)

### Introduction

If the program has been interrupted at a breakpoint, you can continue the program step-by-step.

### Requirement

- Breakpoints are set and enabled in the program code.
- The maximum number of breakpoints that can be enabled for the CPU has not been reached.
- A block is open.

### Procedure

To run the program in single step mode, follow these steps:

1. Establish an online connection to the CPU.
2. Enabling breakpoints

   The program code executes as far as the enabled breakpoint and is then interrupted, in other words, the CPU changes to "HOLD" mode. The red circle for the breakpoint has a yellow arrow superimposed on it.
3. To continue running the program step by step, select one of the following commands from the toolbar:

   - Run

     The program is continued. If there are other breakpoints, the program is interrupted at the next breakpoint.
   - Run to cursor

     The program continues as far as the point at which the insert point is set. If there is a further breakpoint before the insert point, the program is interrupted first at this breakpoint.
   - Step over (for S7-300/400 only)

     The next instruction after the breakpoint is executed. If the instruction is a block call, the call is processed and execution jumps to the next instruction following the block call.
   - Step into (for S7-300/400 only)

     The next instruction after the breakpoint is executed. If the instruction is a block call, execution jumps to the called block. There, you can continue testing in single step mode or set further breakpoints. At the end of the block, execution jumps back to the next instruction following the block call.
   - Step out (for S7-300/400 only)

     If a block call is being processed and the program execution in the called block was interrupted at a breakpoint, you can use "Step out" to jump back to the called block. In the process the remaining instructions of the called block will be executed and the program execution is halted again in the calling block after the block call.

---

**See also**

[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting breakpoints (S7-300, S7-400, S7-1500)](#setting-breakpoints-s7-300-s7-400-s7-1500)
  
[Setting the call environment for breakpoints (S7-300, S7-400, S7-1500)](#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)
  
[Enabling breakpoints (S7-300, S7-400, S7-1500)](#enabling-breakpoints-s7-300-s7-400-s7-1500)
  
[Deleting breakpoints (S7-300, S7-400, S7-1500)](#deleting-breakpoints-s7-300-s7-400-s7-1500)
  
[Introduction to testing with program status](Testing%20the%20user%20program.md#introduction-to-testing-with-program-status)

## "Run to cursor" function (S7-300, S7-400, S7-1500)

### Introduction

The "Run to cursor" function sets a temporary breakpoint at the insertion point and deletes it again once it is reached.

You can perform this function using the corresponding icon in the "Testing" task card as well as using the shortcut menu and also with the keyboard combination "CTL + Shift + 8".

> **Note**
>
> The number of breakpoints that can be enabled on the CPU depends on the particular CPU.
>
> Once you have reached the maximum number, you cannot enable any more breakpoints.
>
> Because the single step functions "Step over", "Step into" and "Run to cursor" are also used as breakpoints, they also cannot be performed when the maximum number of breakpoints is reached. Before you can enable further breakpoints or use these single step functions, you first need to disable breakpoints already enabled.

### Requirement

- There is an online connection to the CPU and this CPU supports the use of breakpoints.
- Valid breakpoints were set and enabled.
- The maximum number of breakpoints that can be enabled for the CPU has not been reached.
- The offline and the online blocks on the CPU are identical.

### Run to cursor

To enable the "Run to cursor" function, proceed as follows:

1. Open the "Testing" task card.

   In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
2. Right-click on the breakpoint you want to enable.
3. Select the "Enable breakpoint" command in the shortcut menu.
4. Wait until the breakpoint is reached and the CPU at the defined breakpoint goes to the "HOLD" state.
5. Move the insertion point in the program code to another location that is valid for inserting another breakpoint.
6. Start the "Run to cursor" function with the icon in the "Testing" task card or via the shortcut menu.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Enabling breakpoints on a CPU S7-1500 as of firmware version V2.5**  As soon as you enable a breakpoint on a CPU S7-1500 as of V2.5, you are informed that the output values for the connected output modules are stopped in their respective state and (in contrast to SIMATIC S7-300/S7-400) neither reset nor set to the configured substitute values. In addition, the SIMATIC S7-1500 can no longer react to input values of input groups in this state.  This information is shown to you only once in each online session. |  |

### Result

The function is executed and a temporary breakpoint is set at the cursor. The CPU goes to "HOLD" at the location indicated by the insertion point.

The position at which the breakpoint was set is indicated as "reached" by the small yellow triangle, the temporary breakpoint has been deleted.

## Monitoring tags when the breakpoint is reached (S7-1500)

### Introduction

For a CPU S7-1500 as of firmware V2.5, you can also monitor tags in conjunction with breakpoints, for example, if the CPU is "HOLD" when a breakpoint is reached in the operating state.

This functionality is only available for global operands (inputs, outputs, bit memory, SIMATIC timers, SIMATIC counters and DBs) in elementary data types.

When you position the mouse pointer over the tags, the value of the operand is displayed in a tooltip.

### Requirement

- There is an online connection to the CPU.
- Valid breakpoints were set and enabled.
- A breakpoint is shown as "reached" in both the "Testing" task card as well as in the Program editor.
- The CPU is in "HOLD" mode, which is shown in the "Testing" task card for both the operating panel as well as for the breakpoints.

### Monitoring tags when the breakpoint reached (S7-1500)

To monitor tags in "HOLD", proceed as follows:

1. Open an STL or SCL block that contains valid breakpoints in the Program editor.
2. Open the "Testing" task card. In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
3. Right-click on the breakpoint you want to enable.
4. Select the "Enable breakpoint" command in the shortcut menu.
5. Wait until the breakpoint is reached during the program execution and the CPU goes to "HOLD".
6. Position the mouse pointer in the program code over a global tag.

### Result

The monitor value for this global tag is displayed in a yellow tooltip.

### Rules for monitoring tags with active breakpoints

In order to be able to monitor tags, this functionality must be enabled via the "Monitoring on/off" button in the toolbar of the programming editor.

Depending on the time you enable tag monitoring during program execution, you obtain different results in the program status display:

- If a breakpoint is reached before you have enabled monitoring, no values are displayed in the program status.
- If a breakpoint is reached during the first run after the monitoring is switched on, the program status only shows the values up to the breakpoint reached.
- If a breakpoint is reached only after the block has been called several times, the monitoring values are displayed with the program status as follows:

  - Values from previous cycles are displayed in gray.
  - Values from the current cycle in which the CPU reached the breakpoint are displayed in black.

> **Note**
>
> - The breakpoints are not saved with the project. If you close the project, the breakpoints are lost.
> - If you terminate the online connection to the CPU, the breakpoints are disabled.

---

**See also**

[Modifying tags during monitoring](Testing%20the%20user%20program.md#modifying-tags-during-monitoring)

## Modifying tags when the breakpoint reached (S7-300, S7-400, S7-1500)

### Introduction

For a CPU S7-1500 from firmware V2.5, you can also control tags in conjunction with breakpoints, for example, if the CPU is "HOLD" when a breakpoint is reached in the operating state.

This functionality is only available for global operands (inputs, outputs, bit memory, SIMATIC timers, SIMATIC counters and DBs) in elementary data types.

The following control options are available in the shortcut menu:

- Modify to 0
- Modify to 1
- Modify operand: Enter the desired modify value in the following dialog.

The selected operand is modified immediately and once.

With a CPU S7-1500 as of firmware V2.5, you can also control global operands directly in the code during monitoring.

With a CPU S7-300/400, you can also control global operands in an SCL block directly in the code during monitoring.

If the CPU has reached a breakpoint and is in the "HOLD" state, you can also control global operands via the watch table.

### Requirement

- There is an online connection to the CPU.
- Valid breakpoints were set and enabled.
- A breakpoint is shown as "reached" in both the "Testing" task card as well as in the Program editor.
- The CPU is in "HOLD" mode, which is shown in the "Testing" task card for both the operating panel as well as for the breakpoints.

### Modifying tags when the breakpoint reached (S7-1500)

To modify tags in "HOLD", proceed as follows:

1. Open an STL or SCL block that contains valid breakpoints in the Program editor.
2. Start monitoring via the button in the "Monitoring on/off" toolbar.
3. Open the "Testing" task card. In the "Breakpoints" pane, you will see a list with all the breakpoints set for the current CPU.
4. Right-click on the breakpoint you want to enable.
5. Select the "Enable breakpoint" command in the shortcut menu.
6. Wait until the breakpoint is reached during the program execution and the CPU goes to "HOLD".
7. Modify the operand to the desired value by clicking on the corresponding command in the shortcut menu.

   - "Modify &gt; Modify to 1"

     Modifies tags of the "BOOL" data type to the value "TRUE".
   - "Modify &gt; Modify to 0"

     Modifies tags of the "BOOL" data type to the value "FALSE".
   - "Modify &gt; Modify operand"

     If you select "Modify operand", the "Modify operand" dialog opens.

     In the subsequent dialog enter the value you require in the "Modify value" box and confirm with "OK".
8. You can also double-click the online value (not for data type BOOL) that you wish to modify.
9. In the subsequent dialog enter the value you require in the "Modify value" box and confirm with "OK".

   Or confirm the query in the subsequent dialog whether the Boolean online value is to be switched over.

- **Example**:

  - If the Boolean tag has the value "0", the value is switched over to the value "1" if the query has been confirmed with "Yes".
  - If the Boolean tag has the value "1", the value is switched over to the value "0" if the query has been confirmed with "Yes".
  - If you click "No" or exit the dialog by using " Close", the existing value remains.

    > **Note**
    >
    > **Modifying tags in operating mode "HOLD"**
    >
    > Note that the displayed tags are no longer updated if the CPU is in the operating mode "HOLD".
    >
    > The tags displayed in "HOLD" are always modified.

### Result

The selected operand is modified to the desired value.

---

**See also**

[Modifying tags during monitoring](Testing%20the%20user%20program.md#modifying-tags-during-monitoring)

## Resuming program execution (S7-300, S7-400, S7-1500)

### Introduction

When you have set valid breakpoints and enable them, you can run the program up to any breakpoint for testing. As soon as a valid breakpoint has been reached, the CPU is in the "HOLD" state.

Program execution on a CPU S7-1500 is not resumed until you reset the CPU to the "RUN" mode.

You can resume the program execution with or without breakpoints.

### Requirement

- There is an online connection to the CPU.
- Valid breakpoints were set and enabled.
- A breakpoint is shown as "reached" in both the "Testing" task card as well as in the Program editor.
- The CPU is in "HOLD" mode, which is shown in the "Testing" task card for both the operating panel as well as for the breakpoints.

### Resuming program execution

You have the following options for resuming program execution after reaching a breakpoint:

- Click the "RUN" button in the "Testing" task card under "Breakpoints".
- Select the "RUN" option from the shortcut menu in the opened Program editor.
- Use the keyboard command "Ctrl+Shift+F7" in the open Program editor.

### Result

The CPU changes from "HOLD" to "RUN" and the normal program processing continues to the next breakpoint.

If it is not possible to resume program execution, you receive a corresponding alarm.

If no other breakpoints are enabled, the program execution resumes without any breakpoints.

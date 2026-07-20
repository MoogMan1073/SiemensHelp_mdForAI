---
title: "Testing the user program"
package: ProgTest2MenUS
topics: 20
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Testing the user program

This section contains information on the following topics:

- [Basics of testing the user program](#basics-of-testing-the-user-program)
- [Testing with program status](#testing-with-program-status)
- [Testing with breakpoints (S7-300, S7-400, S7-1500)](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#testing-with-breakpoints-s7-300-s7-400-s7-1500)
- [Testing with the watch table](Testing%20with%20the%20watch%20table.md#testing-with-the-watch-table)
- [Testing with the force table](Testing%20with%20the%20force%20table.md#testing-with-the-force-table)

## Basics of testing the user program

### Introduction

You have the option of testing the running of your user program on the device. You can then monitor signal states and values of tags and can assign values to tags to simulate certain situations in the running of the program.

### Requirement

There must be an executable program loaded on the device.

### Test options

The following test options are available:

- Testing with program status

  The program status allows you to monitor the running of the program. You can display the values of operands and the results of logic operations (RLO) allowing you to recognize and fix logical errors in your program. You can test either with program status or in single step mode within a S7-300/400 CPU. You cannot, however, use both test options at the same time.
- Testing with breakpoints

  You can test blocks you created in STL or SCL with breakpoints. You do this by setting breakpoints in the program code at which program execution stops. You can then continue to run the program one step at a time. You can test either with program status or in single step mode within a S7-300/400 CPU. You cannot, however, use both test options at the same time.

  Be sure to read the following before you start testing with breakpoints:

  [Safety information for testing with breakpoints](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)

  [Security information for testing with breakpoints](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
- Testing with the watch table

  With the watch table, you can monitor and modify the current values of individual tags in the user program or on a CPU. You can assign values to individual tags for testing and run the program in a variety of different situations. You can also assign fixed values to the I/O outputs of a CPU in STOP mode, for example to check the wiring.
- Testing with the force table

  With the force table, you can monitor and force the current values of individual tags in the user program or on a CPU. When you force, you overwrite individual tags with specified values. This allows you to test your user program and run through various situations.

  When forcing, make sure that you keep to the necessary [Safety precautions when forcing tags](Testing%20with%20the%20force%20table.md#safety-precautions-when-forcing-tags-1)!

---

**See also**

[Introduction to testing with program status](#introduction-to-testing-with-program-status)
  
[Introduction to testing with breakpoints (S7-300, S7-400, S7-1500)](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#introduction-to-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Security information for testing with breakpoints (S7-300, S7-400, S7-1500)](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#security-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Safety information for testing with breakpoints (S7-300, S7-400, S7-1500)](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#safety-information-for-testing-with-breakpoints-s7-300-s7-400-s7-1500)
  
[Introduction to testing with the watch table](Testing%20with%20the%20watch%20table.md#introduction-to-testing-with-the-watch-table)
  
[Introduction for testing with the force table](Testing%20with%20the%20force%20table.md#introduction-for-testing-with-the-force-table)

## Testing with program status

This section contains information on the following topics:

- [Introduction to testing with program status](#introduction-to-testing-with-program-status)
- [Setting the call environment](#setting-the-call-environment)
- [Switching test with program status on/off](#switching-test-with-program-status-onoff)
- [Monitoring loops](#monitoring-loops)
- [Monitoring structures](#monitoring-structures)
- [Editing blocks during the program test](#editing-blocks-during-the-program-test)
- [Modifying tags during monitoring](#modifying-tags-during-monitoring)
- [Switching display formats in the program status](#switching-display-formats-in-the-program-status)
- [Testing GRAPH programs (S7-300, S7-400, S7-1500)](Testing%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#testing-graph-programs-s7-300-s7-400-s7-1500)
- [Testing CEM programs (S7-1200, S7-1500)](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#testing-cem-programs-s7-1200-s7-1500)
- [Examples of program status display](#examples-of-program-status-display)

### Introduction to testing with program status

#### Program status function

You can monitor the execution of the program by displaying the program status. This shows you the values of the individual operands and their results of logic operations. This allows you to check whether the components of the automation system are being correctly controlled.

The display of the program execution in the program status can differ slightly, depending on the CPU series used.

#### Testing with program status for S7-300/400

During testing with program status, the CPU cycle time can become extended because the recording of the data affects the duration of the programmed instructions.

During execution of the following test functions, an alarm is displayed once for each online session indicating that there is a risk of a timeout:

- During testing with call conditions
- During testing with breakpoints

You can only perform these test functions after you have acknowledged the alarm.

> **Note**
>
> With older CPUs from the S7-300/400 CPU series, you will need to change the operating response using the hardware configuration and then load the hardware configuration to the device. You have the option to set the "Process operation" or "Test mode" operating response.

#### Testing with program status for S7-1200/1500

When you run the "Testing with program status" function with a CPU from the S7-1500 series, the cycle time can increase significantly when monitoring loops due to the fast program execution. The CPU may go to STOP, especially when it exceeds the configured cycle clock for interrupt OBs or the configured maximum cycle time.

> **Note**
>
> To avoid a possible STOP in the CPU, ensure that no programmed loops are displayed in the active monitoring window during "Testing with program status". Alternatively, you can also increase the maximum permissible cycle time of the CPU.

#### Restrictions with the "Program status" function

The monitoring of loops can increase the cycle time significantly, depending in each case on the number of tags to be monitored and on the actual number of loops processed.

To ensure that the cycle time is influenced as little as possible, the "Program status" function is restricted as described below:

For CPUs from the S7-300/400 series:

- The status display of a programmed loop is stopped at the return point.

For CPUs from the S7-1200/1500 series:

- The monitoring of loops is deactivated by default. If required, monitoring can be activated via the shortcut menu.
- If the monitoring of loops is enabled with an S7-1200 CPU, the program status for the area is not displayed after a loop that is processed multiple times. In this case, move the visible editor window to the area after the loop so that the monitor values are displayed again.
- The first occurrence of an instruction is always observed for a CPU S7-1200 as of V4.2 and for a CPU S7-1500.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Testing with program status**  A test with the "Program status" function can cause serious damage to property or injury to persons if malfunctions or program errors occur.  Make sure that no dangerous situations can arise before you conduct a test with the "Program status" function. |  |

#### Recommended procedure if there is a risk of a timeout

If there is a risk of a timeout during monitoring with program status, you are alerted by the system with a corresponding alarm.

To continue monitoring, you have to acknowledge the alarm with "Yes".

In this case, you also have the following option to avoid exceeding the maximum permissible cycle time during testing with program status:

- Reduce the size of the editor window so that fewer tags are displayed and thus fewer tags are monitored.
- Monitor the required tags within the watch table.

### Setting the call environment

This section contains information on the following topics:

- [Basics of the call environment](#basics-of-the-call-environment)
- [Setting the call environment for block monitoring](#setting-the-call-environment-for-block-monitoring)

#### Basics of the call environment

##### Function

Depending on the CPU used, you can define the call environment for monitoring blocks and for breakpoints (not with S7-1500). With this, you specify the conditions for recording the program status of a block or for stopping program execution at a breakpoint.

**Valid for S7-1500er CPUs as of firmware version V2.5:**

Call environment for monitoring blocks:

- As soon as a breakpoint is enabled in a block, it is **not** possible to configure a call environment for monitoring.
- In the other direction, a breakpoint in a block **cannot** be enabled if a call environment has already been configured.
- If you attempt to use both functionalities, you are shown an error message with information about how to proceed.

**Specification of the call environment for block monitoring**

Alternatively, you can activate one of the following options to specify the call environment:

- No condition defined

  If no other option was selected this option is the default.
- Instance data block

  The program status of a function block will then only be recorded when you call the function block with the selected instance data block. Multi-instances cannot be specified here.
- Call path

  The program status of a block is recorded only if the block is called from a specific block, from a specific path, or in conjunction with a specific instance data block.
- Manually adapted call path

  You can enter the desired call environment manually in this field. The "Transfer to 'adjusted manually'" button is used to transfer the content selected under "Call environment", which you can edit further if required.  
  The program status of a block will then only be recorded when you call the block with a specific block or from a specific path.

  You do not have the option here to define a call together with a specific instance data block or a specific call location as the call environment. Use the "Call path" area instead.

**Specification of the call environment for breakpoints**

When working with a CPU S7-300/400, you can define a separate call condition for each breakpoint.

When working with a CPU S7-1500 as of V2.5, you cannot specify a call environment for breakpoints.

If you do not define a call environment, the program status of any block call is recorded within the call structure and the program execution is always interrupted at the given breakpoint. If possible, set a call environment to display the program status for a particular call.

---

**See also**

[Setting the call environment for block monitoring](#setting-the-call-environment-for-block-monitoring)

#### Setting the call environment for block monitoring

By setting the call environment, you can specify when the program status of a block is recorded.

The section "[Setting the call environment for breakpoints](Testing%20with%20breakpoints%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#setting-the-call-environment-for-breakpoints-s7-300-s7-400-s7-1500)" describes how to set the call environment for breakpoints.

##### Requirement

- The block is open.

##### Specifying the call environment

To set the call environment, follow these steps:

1. Open the "Testing" task card.
2. Click "Change" in the "Call environment" pane.

   The "Call environment of the block" dialog opens.
3. Select the condition you want to apply.

   See also: [Basics of the call environment](#basics-of-the-call-environment)
4. Confirm your selection with "OK".

##### Result

The selected call environment is displayed in the "Testing" task card within the "Call environment" pane. The program status is now carried out in accordance with the set call environment.

##### Changing the call environment

Proceed as follows to change the call environment:

1. Open the "Testing" task card.  
   If a call environment is already set, this is displayed in the "Call environment" pane.
2. Click "Change" in the "Call environment" pane.

   The "Call environment of the block" dialog opens.
3. Select the condition you want to apply.

   See also: [Basics of the call environment](#basics-of-the-call-environment)
4. Confirm your selection with "OK".

##### Result

The selected call environment is displayed in the "Testing" task card within the "Call environment" pane. The program status is now carried out in accordance with the set call environment.

---

**See also**

[Basics of the call environment](#basics-of-the-call-environment)
  
[Introduction to testing with program status](#introduction-to-testing-with-program-status)

### Switching test with program status on/off

You can monitor all blocks by switching on the program status of the block. This function is available to you for all code blocks, regardless of the programming language used. For blocks that were programmed with LAD, FBD or SCL you can also enable the program status from a specific position or for a specific selection. You can switch on the program status for an open block directly, or open a block from the calling block and view the program status.

A tooltip shows you whether or not data about the program status is currently being received. To do his, place the mouse over the blue dashed "Indicator" in the upper right corner of the workspace.

> **Note**
>
> Note the following:
>
> - The resources for testing with program status are limited. If there are not enough resources for an additional test, the tests that are already running are terminated.
> - It is possible that another user can carry out a loading process on the selected CPU through joint parallel working on a CPU. It is therefore possible in the following cases that you can either not start the test with program status or that a running test is terminated:
>
>   - Through the loading process the block for which you want to start or already have carried out the test with program status is loaded.
>   - You use an instance data block as the call environment for the test with program status and the block changes structurally through the loading process, e.g. by renumbering.
>   - You use a call path as the test condition for the test with program status and a block within the call path changes through the loading process.
>
>   If a running test is terminated, a corresponding message is displayed in the Inspector window.

#### Requirement

- Code block: The code of the offline block is identical with the code of the online block. In this case the "Code time stamps" of the blocks are identical.
- Data block: The structure of the offline block is identical with the structure of the online block. In this case the "Interface time stamps" of the blocks are identical.

#### Switching the program status on or off directly in the block

To switch the program status for a block on or off directly in the block, follow these steps:

1. Open the block for which you wish to switch on the program status.
2. Click "Monitoring on/off" in the toolbar.

   If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. Click "Monitoring on/off" in the toolbar again to switch the program status off.

#### Switching on or off program status starting at a specific point in a network

**To start the program status for LAD and FBD at a specific point, follow these steps:**

1. Open the block for which you wish to switch on the program status.
2. Click "Monitoring on/off" in the toolbar.
3. Right-click on the tag you want program status to start from.
4. Select "Modify &gt; "Monitor from here" in the shortcut menu.
5. Click "Monitoring on/off" in the toolbar again to switch the program status off.

**To start the program status in SCL at a specific point, follow these steps:**

1. Open the block for which you wish to switch on the program status.
2. Click "Monitoring on/off" in the toolbar.
3. Select the tag from which you want to start the program status.
4. After this, click "Display program status from the selected line" in the toolbar.
5. Click "Monitoring on/off" in the toolbar again to switch the program status off.
6. To make matters clearer, you can use the shortcut menu commands "Open" and "Close" or "Open all" and "Close all" to expand or collapse individual or all closed code sections within the block.

#### Switching on or off program status for selected tags

To start the program status for LAD and FBD for selected tags, follow these steps:

1. Open the block for which you wish to switch on the program status.
2. Click "Monitoring on/off" in the toolbar.
3. Select the tags for which you want to start the program status.
4. Select "Modify &gt; Monitor selection" in the shortcut menu.
5. Click "Monitoring on/off" in the toolbar again to switch the program status off.

#### Switching on program status from the calling block

To switch on the program status for a block from the calling block (e.g. OB1), follow these steps:

1. Open the calling block.
2. Right-click on the block call.
3. Select the command "Open and monitor" in the shortcut menu.

   The block will open in the program editor. An online connection is established and the program status is displayed. The calling block is set in the call path.

#### Result

If you enable the display of the program status, an online connection is established and the program status is displayed. When you turn off the display of the program status, you can terminate the online connection at the same time.

The call path of the block is shown under the block interface. If necessary, you can change the call environment in the "Call environment" section at the right-hand edge at "Test" and "Options". In the case of CPUs of the S7-1200/1500 series the "Call hierarchy" is displayed additionally on the right-hand edge. You can open the calling block by clicking the link.

---

**See also**

[Setting the call environment](#setting-the-call-environment)

### Monitoring loops

#### Introduction to monitoring loops

If you display the program status, you can monitor the execution of the program with a block. This provides you with an overview of the values of the individual operands and the results of the logic operations and you can check whether the components of the automation system are correctly controlled.

If the values are shown in a lighter, less saturated font, these values do not come from the current cycle.

> **Note**
>
> The monitoring of loops can increase the cycle time of the CPU significantly, depending in each case on the number of tags to be monitored and on the actual number of loops processed.

Special rules apply to loop monitoring, depending on the specific CPU and the programming language that are used.

#### Rules for loop monitoring (S7-300/400)

To ensure that the cycle time is influenced as little as possible, the "Program status" function is restricted as follows during the monitoring of loops with CPU from the S7-300/400 family in all programming languages:

- The status display of a programmed loop is stopped at the return point.

#### Rules for loop monitoring in STL (S7-1500)

The display of the program status within programmed loops is disabled by default during the monitoring of loops in STL. To avoid any lengthening of the cycle time, no values are displayed for the tags within loops between the "Label" and the associated "Loop" instruction.

If you are monitoring an STL block with programmed loops, a tooltip informs you that the monitoring of loops is currently disabled and can be enabled if required via the shortcut menu.

> **Note**
>
> Please note that only those loops that are programmed within a network are recognized.

#### Enabling/disabling the monitoring of loops in STL (S7-1500)

To enable the monitoring of loops in STL, follow these steps:

1. Open the STL block that you want to monitor.
2. Click "Monitoring on/off" in the toolbar.

   If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. Enable the monitoring within the program editor with the shortcut menu command "Monitoring" &gt; "Monitor loops".
4. Confirm the next prompt with "Yes".

   Result: The monitoring of loops is enabled for the entire block and is active until monitoring of loops is once again disabled or the online connection to the CPU is terminated.
5. Click "Monitoring on/off" in the toolbar again to switch the program status off.

#### Rules for loop monitoring in SCL (S7-1200/1500)

When monitoring loops in SCL, the display of the program status within programmed loops is switched off by default.

This affects the instructions "FOR", "WHILE" and REPEAT-UNTIL": No values are displayed for the tags within these instructions to avoid affecting the cycle time.

If you are monitoring an SCL block with programmed loops, a tooltip informs you that the monitoring of loops is currently disabled and can be enabled if required via the shortcut menu.

#### Enabling/disabling the monitoring of loops in SCL (S7-1200/1500)

To enable the monitoring of loops in SCL, follow these steps:

1. Open the SCL block that you want to monitor.
2. Click "Monitoring on/off" in the toolbar.

   If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. Right-click within the loop, in the column "value, for example, and enable monitoring with the shortcut menu command "Monitor loops".
4. Confirm the next prompt with "Yes".

   Result: The monitoring of loops is enabled for the entire block and is active until monitoring of loops is once again disabled or the online connection to the CPU is terminated.
5. Click "Monitoring on/off" in the toolbar again to switch the program status off.

### Monitoring structures

#### Introduction to monitoring structures

You can monitor the execution of the program with a block. This provides you with an overview of the values of the individual operands and the results of the logic operations and you can check whether the components of the automation system are correctly controlled.

As of TIA Portal V14, it is also possible to monitor structured PLC tags.

There are special rules for monitoring structures, depending on the particular CPU and programming language in use, and the properties of the respective structures.

#### Rules for monitoring structures (S7-1200/1500)

During the monitoring of structures, the values of a structured PLC tag are displayed in the program editor and in the Inspector window, with the following exception:

- It is not possible to monitor structures whose elements have adjustable retentivity properties.

To display the monitor values for a structure, you must first enable monitoring via the shortcut menu.

#### Displaying the monitor values for structures in the Inspector window

If the monitoring of structures is enabled and a structure tag is selected in the program editor, the associated monitor values are displayed in the Inspector window in the tab "Diagnostics" &gt; "Monitor values".

The Inspector window is structured as follows:

- "Name" column shows the selected structure tag with the elements under the first level opened. If you click the name of the structure tag, the program editor jumps to this tag's point of use.
- The "Data type" column shows the associated data type.
- The "Value" columns shows the associated monitor values. If dashes are shown here instead of values, the monitoring of loops is disabled. In this case, enable the monitoring of loops again by means of the shortcut menu in the program editor.
- Columns "Value - IN" and "Value - OUT": These columns with the corresponding values are only displayed if the selected structure is used as an IN/OUT parameter.
- If the monitor values are displayed in a font with only 50 % saturation, this means that these vales are not from the current cycle.
- The monitor values displayed in the Inspector window use the same call path that is set as default for the block.
- The table with monitor values displayed in the Inspector window can be copied to an Excel file.
- If it is not possible to display any monitor values in the Inspector window, you will receive information that these are not available.

#### Procedure for monitoring structures

To enable the monitoring of structures, follow these steps:

1. Open the block in the program editor.
2. Click "Monitoring on/off" in the toolbar.

   If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.

   See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
3. If the structure to be monitored is located in a loop, first enable the monitoring of loops.

   See also: [Monitoring loops](#monitoring-loops)
4. Right-click on a structure and enable the monitoring of structures by means of the shortcut menu command "Monitoring" &gt; "Monitor values".

   Result: The selected structure tag is displayed in the Inspector window in the tab "Diagnostics" &gt; "Monitor values" is open up to the first level with the current values displayed.
5. If needed, open the closed elements of the structure to display all the lower-level elements and their values.
6. Click "Monitoring on/off" in the toolbar again to switch the program status off.

> **Note**
>
> **Monitoring a structure within an array**
>
> Click directly behind the closing bracket to select the relevant structure for monitoring.

---

**See also**

[Monitoring loops](#monitoring-loops)

### Editing blocks during the program test

If you edit blocks while they are being monitored, monitoring will be interrupted and you will be able to edit the block offline. If the block is not available offline in the project, you will first have to load it from the device to the project. After editing the block, you will also have to compile and download it again.

#### Procedure

To edit blocks while these are being monitored, follow these steps:

1. Edit the block as necessary.

   Monitoring is interrupted and the block is switched offline mode assuming it exists offline.
2. If the block does not exist offline, load it to the project from the device.
3. Compile the block.

   See also: [Compiling blocks](Compiling%20and%20downloading%20PLC%20programs.md#compiling-blocks)
4. Download the block to the device.

   See also: [Downloading blocks for S7-1200/1500](Compiling%20and%20downloading%20PLC%20programs.md#downloading-blocks-for-s7-12001500-s7-1200-s7-1500)

#### Result

The block now contains your modifications both online and offline. The online connection is re-established and monitoring continues.

### Modifying tags during monitoring

During monitoring, you have the option of modifying tags immediately and once in the program status.

For Boolean values you can switch between the values "0" and "1".

You can enter a modify value for tags that do not belong to the "BOOL" data type.

Note that you cannot modify peripheral inputs, for example, via TagName:P.

You can control tags during monitoring either by double-clicking the online value (not for data type BOOL) or after the tags have been clicked by using the shortcut menu.

#### Procedure

To modify tags during monitoring, follow these steps:

1. Open the desired block and start the monitoring of tags by clicking "Monitoring on/off" in the toolbar.
2. Double-click the online value (not for data type BOOL) that you wish to modify.

   Alternatively, you can click the desired tag and start modifying by using the shortcut menu.
3. In the subsequent dialog enter the value you require in the "Modify value" box and confirm with "OK".

   Or confirm the query in the subsequent dialog whether the Boolean online value is to be switched over.

   Example:

   - If the Boolean tag has the value "0", the value is switched over to the value "1" if the query has been confirmed with "Yes".
   - If the Boolean tag has the value "1", the value is switched over to the value "0" if the query has been confirmed with "Yes".
   - If you click "No" or exit the dialog by using " Close", the existing value remains.
4. Alternatively, select one of the following commands in the shortcut menu:

   - "Modify &gt; Modify to 1"

     Modifies tags of the "BOOL" data type to the value "TRUE".
   - "Modify &gt; Modify to 0"

     Modifies tags of the "BOOL" data type to the value "FALSE".
   - "Modify &gt; Modify operand"
5. If you select "Modify operand", the "Modify operand" dialog opens.
6. In the subsequent dialog enter the value you require in the "Modify value" box and confirm with "OK".

---

**See also**

[Switching test with program status on/off](#switching-test-with-program-status-onoff)

### Switching display formats in the program status

#### Introduction

The display formats for tags depend on the respective tag type. During monitoring, you have the option of switching the current display format by means of the shortcut menu. The possible display formats for a tag are offered in the shortcut menu.

You can modify the display format for the selected tag, for all tags in the network or for all tags in the block.

This is useful, for example, when you need a hexadecimal display in order to search for a hexadecimal error code.

#### Procedure

To switch the display format, follow these steps:

1. Open the desired block in the programming editor.
2. Switch on the program status by clicking "Monitoring on/off" in the toolbar.

   If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.
3. Select the tag you want to monitor and select the desired display format in the shortcut menu under "Display format".

#### Result

The display format is modified accordingly.

> **Note**
>
> **Switching display format during monitoring**
>
> Please note that it is not possible to switch the display format for unconnected outputs, as no monitoring value is output in this case.

### Examples of program status display

This section contains information on the following topics:

- [Program status display for LAD programs](#program-status-display-for-lad-programs)
- [Program status display for FBD programs](#program-status-display-for-fbd-programs)
- [Program status display for STL programs (S7-300, S7-400, S7-1500)](#program-status-display-for-stl-programs-s7-300-s7-400-s7-1500)
- [Program status display for SCL programs](#program-status-display-for-scl-programs)
- [Program status display for GRAPH programs (S7-300, S7-400, S7-1500)](#program-status-display-for-graph-programs-s7-300-s7-400-s7-1500)
- [Program status display for CEM programs (S7-1200, S7-1500)](#program-status-display-for-cem-programs-s7-1200-s7-1500)

#### Program status display for LAD programs

##### Displays in program status

The display of the program status is updated cyclically.

The following figure shows an example of the program status display for LAD:

![Displays in program status](images/25434896139_DV_resource.Stream@PNG-en-US.png)

##### Representation of the program status

You can recognize the status of individual instructions and lines of a network quickly based on the color and type of lines and symbols. The following table shows the relationship between representation and status:

| Representation | Status |
| --- | --- |
| Green solid | Satisfied |
| Blue dashed | Not satisfied |
| Gray solid | Unknown or not executed |
| Black | Not interconnected |
| Lines or parameters in a frame with a saturation of 100 % | Value is current |
| Lines or parameters in a frame with a saturation of 50 % | Value originates from an earlier cycle. The point in the program was not executed in the current cycle. |

#### Program status display for FBD programs

##### Displays in program status

The display of the program status is updated cyclically.

The following figure shows an example of the program status display for FBD:

![Displays in program status](images/25434968843_DV_resource.Stream@PNG-en-US.png)

##### Representation of the program status

You can recognize the status of individual instructions and lines of a network quickly based on the color and type of lines and symbols. The following table shows the relationship between representation and status:

| Representation | Status |
| --- | --- |
| Green solid | Satisfied |
| Blue dashed | Not satisfied |
| Gray solid | Unknown or not executed |
| Black | Not interconnected |
| Lines or parameters in a frame with a saturation of 100 % | Value is current |
| Lines or parameters in a frame with a saturation of 50 % | Value originates from an earlier cycle. The point in the program was not executed in the current cycle. |

The values of the operands are displayed above the relevant operand name in a gray box.

> **Note**
>
> **Program status display for outputs which are not interconnected**
>
> Please note that a monitor value cannot be displayed for outputs which are not interconnected.

#### Program status display for STL programs (S7-300, S7-400, S7-1500)

##### Displays in program status

The display of the program status is updated cyclically and shown in tables. The tables are shown directly next to the STL program. You can read the program status for each line of the program. The display depends on the CPU in use (S7-300, S7-400, or S7-1500).

The tables to be displayed in the program status always contain the following information:

- RLO

  The "RLO" column shows the result of logic operation for each line of program. You can recognize the value of the RLO based on the background color of the table cell. Here, green means an RLO of 1 and lilac an RLO of 0.
- Value

  The current value of the operand is shown in the "Value" column.
- Extra

  The "Extra" column shows additional information depending on the particular operation, for example, relevant status bits for mathematical instructions, time or count values for timers and counters or memory addresses for indirect addressing.

The following figure shows an example of the program status display of a CPU S7-300 under STL:

![Displays in program status](images/30867313675_DV_resource.Stream@PNG-en-US.png)

#### Program status display for SCL programs

##### Displays in program status

The display of the program status is updated cyclically and shown in a table. The table is displayed immediately beside the SCL program and you can see the program status for each line of the program. The table contains the following information:

- Tag names
- Value

You can move the table to the left or right at any time.

The following figure shows two examples of the program status display for SCL:

![Displays in program status](images/156751456139_DV_resource.Stream@PNG-de-DE.png)

##### Explanation on monitoring

The upper part of the picture shows possible results when monitoring in the programming editor:

- If the code of the line is not executed, the tag name is displayed in the values table in gray text.
- The current values of the tags are displayed in the last column. If no values can be displayed for a tag, the corresponding cell has a yellow background and three question marks are shown. In this case, select the "Create extended status information" check box in the properties of the block and download the block to the device again. All values are then displayed.
- In the first column, you can see the name of the tag for which the current value is being displayed.
- If the line includes the "IF", "WHILE" or "REPEAT" instruction, the result of the instruction is displayed in the line as "True" or "False".
- If the line contains more than one tag, the value of the first tag is displayed. In both cases, all tags of these lines are displayed with their values in a separate list as soon as you select a line.
- If you place the cursor in a tag in the program code, this is shown in bold face in the list. You can also display the other tags of a line explicitly by clicking the arrow right located in front of lines containing more than one tag.

The lower part of the picture shows possible results for through in-out parameters of FBs and FCs. The value at the "In" time is in front of the arrow, the value at the "Out" time is behind the arrow.

#### Program status display for GRAPH programs (S7-300, S7-400, S7-1500)

##### Displays in program status

For GRAPH programs you can have the program status displayed in sequence view and in single step view and for the permanent instructions. The program status display of permanent instructions corresponds to the program status display for LAB/FBD programs. The display of the program status is updated cyclically.

The following table shows the relationship between representation and status:

| Representation | Area | Status |
| --- | --- | --- |
| Green | Step, sequencer | There are no faults. |
| Light green | Step, sequencer | There are no faults.   The values are from elapsed cycles. |
|  | Condition | The transition is fulfilled. |
| Red | Step, sequencer | There is a supervision error. |
| Yellow | Step, sequencer | There is an interlock error. |
| Black | Condition | The transition is not fulfilled. |

The following figures show examples of the display for the program status in the sequence view:

![Displays in program status](images/52601620363_DV_resource.Stream@PNG-en-US.png)

Step 2 contains a supervision error. The transition for switching from step 2 to step 3 is fulfilled.

![Displays in program status](images/52601515659_DV_resource.Stream@PNG-en-US.png)

Step 2 contains an interlock error. The transition for switching to step 3 is fulfilled.

The figure below shows an example of the display for the program status in the single step view of a S7-300:

![Displays in program status](images/25537311115_DV_resource.Stream@PNG-en-US.png)

The step does not contain an interlock error. The subsequent transition is not satisfied.

#### Program status display for CEM programs (S7-1200, S7-1500)

In CEM programs, you can display the program status of causes, effects, and intersections.

##### Program status of causes and effects

You can display the program status of causes and effects to monitor the program sequence. The program status is updated cyclically.

The display corresponds to the program status display for FBD programs:

- Green markings indicate that a signal state of "1" is pending at the element.
- Blue markings indicate the signal state "0".
- The values of the operands are displayed above the operand in a gray box.
- The current timer values are displayed in the top left area of the cause.

##### Program status of intersections

You can read out the following information in the program status display of intersections:

- The filling shows the status of the intersection.

  - Active intersections have a green filling.
  - Inactive intersections have a blue filling.
- The border indicates whether the intersection has an influence on the effect.

  - Intersections with a green border set the effect to "1".
  - A blue border shows that the effect is set to "0".
  - A gray border indicates that the intersection does not influence the effect because the column contains active intersections with a higher priority number.

##### Representation of the program status in CEM

The figure below shows an example of the display for the program status in CEM:

![Representation of the program status in CEM](images/140023462027_DV_resource.Stream@PNG-en-US.png)

The cause "SecurityGate1" is not active. The N action sets the signal state at the input of the effect "Belt1" to "0".

The cause "SecurityGate2" is active. The N action sets the signal state at the input of the effect "Belt2" to "1".

---
title: "Supervision of machinery and plants with ProDiag (S7-1500)"
package: ProgProDiag1500enUS
topics: 164
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Supervision of machinery and plants with ProDiag (S7-1500)

This section contains information on the following topics:

- [System requirements for ProDiag (S7-1500)](#system-requirements-for-prodiag-s7-1500)
- [Technical specifications for ProDiag (S7-1500)](#technical-specifications-for-prodiag-s7-1500)
- [Basics of supervision with ProDiag (S7-1500)](#basics-of-supervision-with-prodiag-s7-1500)
- [Creating ProDiag function blocks (S7-1500)](#creating-prodiag-function-blocks-s7-1500)
- [Using a central time stamp (S7-1500)](#using-a-central-time-stamp-s7-1500)
- [Using ProDiag instance data bases (S7-1500)](#using-prodiag-instance-data-bases-s7-1500)
- [Defining properties for a ProDiag function block (S7-1500)](#defining-properties-for-a-prodiag-function-block-s7-1500)
- [Defining the ProDiag supervision settings (S7-1500)](#defining-the-prodiag-supervision-settings-s7-1500)
- [Creating and instantiating ProDiag supervisions (S7-1500)](#creating-and-instantiating-prodiag-supervisions-s7-1500)
- [Copying ProDiag function blocks (S7-1500)](#copying-prodiag-function-blocks-s7-1500)
- [Assigning ProDiag function blocks (S7-1500)](#assigning-prodiag-function-blocks-s7-1500)
- [Editing ProDiag function blocks (S7-1500)](#editing-prodiag-function-blocks-s7-1500)
- [Calling the ProDiag function blocks (S7-1500)](#calling-the-prodiag-function-blocks-s7-1500)
- [Load ProDiag blocks (S7-1500)](#load-prodiag-blocks-s7-1500)
- [Displaying, adding and editing ProDiag supervisions (S7-1500)](#displaying-adding-and-editing-prodiag-supervisions-s7-1500)
- [Displaying supervisions in detail view of the project tree (S7-1500)](#displaying-supervisions-in-detail-view-of-the-project-tree-s7-1500)
- [Exporting and importing ProDiag supervisions (S7-1500)](#exporting-and-importing-prodiag-supervisions-s7-1500)
- [Displaying ProDiag cross-references (S7-1500)](#displaying-prodiag-cross-references-s7-1500)
- [Acquiring initial values (S7-1500)](#acquiring-initial-values-s7-1500)

## System requirements for ProDiag (S7-1500)

This section contains information on the following topics:

- [Notes on licenses (S7-1500)](#notes-on-licenses-s7-1500)
- [Setting ProDiag licenses (S7-1500)](#setting-prodiag-licenses-s7-1500)
- [Software and hardware requirements (S7-1500)](#software-and-hardware-requirements-s7-1500)

### Notes on licenses (S7-1500)

#### Description

The configuration of supervisions is completely integrated in STEP 7 Professional. It can be used on any STEP 7 engineering station and independent of the application. Only the number of instantiated supervisions (including global supervisions) used in the program code is licensed, whereby the first 25 supervisions can be used free of charge.

The table below shows you how many licenses you need:

| Number of supervisions in use | &lt;= 25 | &lt;= 250 | &lt;= 500 | &lt;= 750 | &lt;= 1000 | &gt; 1000 |
| --- | --- | --- | --- | --- | --- | --- |
| Number of licenses required | None | 1 | 2 | 3 | 4 | 5 |

There are two places in the TIA Portal where you can display the number of supervisions:

- In the properties of the ProDiag function block

  Here you can see how many supervisions are contained in the respective ProDiag function block and how many supervisions are possible. The maximum number of supervisions depends on the version of the respective ProDiag function block.

  ProDiag FB V1.0: Maximum 250 supervisions

  ProDiag FB V2.0: Maximum 1000 supervisions

  Additional information is available here: [Displaying the number of supervisions for a ProDiag FB](#displaying-the-number-of-supervisions-for-a-prodiag-fb-s7-1500)
- In the device properties of the CPU

  Here you can see the total number of all supervisions used within a CPU that have been assigned to a ProDiag function block. With this information, you can decide how many licenses you need or how many supervisions you can still create with the current license.

  Additional information is available here: [Setting ProDiag licenses](#setting-prodiag-licenses-s7-1500)

For additional information on general allocation of licenses is available at: "Installation &gt; System requirements for installation &gt; Notes on licenses".

### Setting ProDiag licenses (S7-1500)

#### Requirement

You have created an S7-1500 CPU.

#### Procedure

Proceed as follows to set the licenses for ProDiag:

1. Double-click the Device configuration of the S7-1500 CPU in the project tree.

   The Device configuration is opened in the Device view.
2. Click the subordinate tab "General" in the "Properties" Inspector window.
3. Click the arrow next to the "Runtime licenses" section.

   The available Runtime licenses are displayed.
4. Click the "ProDiag" entry.

   All the supervisions used within the S7-1500 CPU are displayed in the "Supervisions" section.
5. Select the number of licenses required in the "Runtime licenses" section in accordance with the number of supervisions used.

#### Result

The required licenses are set.

![Result](images/100073025675_DV_resource.Stream@PNG-en-US.png)

### Software and hardware requirements (S7-1500)

#### Requirements for ProDiag

The table below shows the minimum software and hardware requirements that have to be met for use of ProDiag:

| Software/Hardware | Requirement |
| --- | --- |
| TIA Portal | STEP 7 Professional |
| CPU of the S7-1500 series | &gt;= Firmware V2.0 |

## Technical specifications for ProDiag (S7-1500)

This section contains information on the following topics:

- [Technical specifications for ProDiag (S7-1500)](#technical-specifications-for-prodiag-s7-1500-1)

### Technical specifications for ProDiag (S7-1500)

#### Description

The following table shows the maximum values possible:

| Object | Number of objects |
| --- | --- |
| ProDiag function blocks | There is a maximum of 100 ProDiag FBs that can be used in a project. |
| ProDiag supervisions | ProDiag FB V1.0:  A ProDiag FB can be assigned a maximum of 250 supervisions.  ProDiag FB V2.0:  A ProDiag FB can be assigned a maximum of 1000 supervisions. |

## Basics of supervision with ProDiag (S7-1500)

This section contains information on the following topics:

- [Introduction to ProDiag (S7-1500)](#introduction-to-prodiag-s7-1500)
- [Requirements for using ProDiag (S7-1500)](#requirements-for-using-prodiag-s7-1500)
- [Example for creating a supervision based on an operand supervision (S7-1500)](#example-for-creating-a-supervision-based-on-an-operand-supervision-s7-1500)
- [Types of supervision (S7-1500)](#types-of-supervision-s7-1500)
- [Examples for individual types of supervision (S7-1500)](#examples-for-individual-types-of-supervision-s7-1500)
- [Application examples for supervisions with ProDiag (S7-1500)](#application-examples-for-supervisions-with-prodiag-s7-1500)

### Introduction to ProDiag (S7-1500)

#### Description

Starting in the TIA Portal Version V14, you have the option of supervising your machine or plant using the ProDiag functionality and intervening in case of a fault. The supervision alarms that you can create for different kinds of faults give you specific information on the supervision type, on the location and cause of the fault. You can also output notes on the removal of the determined faults. This means you cannot only detect faults, but you can also identify a possible risk of error in advance and take appropriate countermeasures.

You can integrate simple supervisions in your program with just a few configuring steps and without having to change the program code. For example, you can create a supervision by monitoring a Boolean operand for its signal state. As soon as the operand has the set signal state, a ProDiag supervision alarm is output based on the configured ProDiag supervision settings. The configuration of the supervisions is independent of the programming languages of the TIA Portal because only individual operands are supervised and you do not need any additional programming sections.

![Description](images/131985526923_DV_resource.Stream@PNG-en-US.png)

For an introductory example of how to create supervisions with the help of ProDiag, go to: [Example for creating a supervision based on an operand supervision](#example-for-creating-a-supervision-based-on-an-operand-supervision-s7-1500)

#### Benefits

The supervision of your machine or plant with ProDiag has the following benefits:​

- Your program code is not changed when you create supervisions and the ProDiag function blocks are automatically called in the ProDiag organization block, as long as you do not want to call them yourself in your program code.
- With the help of the ProDiag function blocks, you can create units and group all supervisions of a unit, such as a motor, according to technological aspects.
- You can reduce downtimes and production outages after a fault occurs or in the case of foreseeable events with the help of early warnings or information.
- Fault removal and possible maintenance work are made much easier because specific information about the cause of a fault is made available to the machine operator on site.
- Regardless of which S7-1500 CPU you are using, the configuration of supervisions is simple and easy to understand.
- You can also supervise both F blocks as well as know-how protected function blocks without problems with ProDiag since they are not changed and therefore do not need to be recompiled.
- Alarm texts are automatically derived from texts in the project, for example:

  - Category
  - CPU name
  - FB name
  - Instance name, etc.
- Changes in the CPU configuration are applied automatically by the HMI device. The alarm texts are managed directly in the CPU.
- Relatively low influence on the cycle time.
- The change management of the supervisions is completely managed in the TIA Portal, which means users do not have to focus on ensuring consistency. This means the error probability of incorrect alarm texts is largely eliminated.

### Requirements for using ProDiag (S7-1500)

#### No ProDiag supervisions available

If no ProDiag supervisions are available, this may be for various reasons:

- The selected object does not support ProDiag.
- The selected parameter or the tag are not of the data type BOOL.
- The selected block is not a function block.
- The CPU does not support ProDiag. Use an S7-1500.
- The CPU version is &lt;2.0.

> **Note**
>
> **ProDiag with Multiuser Engineering**
>
> Blocks supervised with ProDiag, such as FBs or global DBs, Software Units, PLC data types or tags, are consistently supported by Multiuser Engineering.

### Example for creating a supervision based on an operand supervision (S7-1500)

#### Description

The example below provides you with a brief overview of how to create a supervision based on an operand supervision: Detailed Information on the individual steps can be found in the following sections.

1. Create a ProDiag supervision group. To do this insert a new function block of the type PRODIAG with the name "Station_1":

   ![Description](images/87461653131_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/87461653131_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/84698348555_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/84698348555_DV_resource.Stream@PNG-en-US.png)
2. Call up the ProDiag supervision settings in the project tree in the "Common data" folder.

   ![Description](images/88412368395_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/88412368395_DV_resource.Stream@PNG-en-US.png)
3. Specify the ProDiag supervision settings

   ![Description](images/85210148107_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/85210148107_DV_resource.Stream@PNG-en-US.png)
4. In the default tag table declare a Boolean tag and add a supervision.

   ![Description](images/87464405131_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/87464405131_DV_resource.Stream@PNG-en-US.png)
5. In the Inspector window define the properties of the operand supervision in "Properties &gt; Supervisions":

   ![Description](images/89883305995_DV_resource.Stream@PNG-en-US.png)

   ![Description](images/89883305995_DV_resource.Stream@PNG-en-US.png)

   You can create either a global tag supervision or a local parameter supervision at the function block or a supervision at the PLC data type. To do so, you can either use an operand that is already included in the program code or you create a new operand and subsequently call it in the program code. When you create a parameter supervision, you must call the function block in the program code.
6. Compile and download the project.

   The ProDiag function block "Station_1" is automatically called in the ProDiag organization block.

---

**See also**

[Creating ProDiag function blocks (S7-1500)](#creating-prodiag-function-blocks-s7-1500)
  
[Defining the ProDiag supervision settings (S7-1500)](#defining-the-prodiag-supervision-settings-s7-1500)
  
[Creating and instantiating ProDiag supervisions (S7-1500)](#creating-and-instantiating-prodiag-supervisions-s7-1500)

### Types of supervision (S7-1500)

This section contains information on the following topics:

- [Overview of the types of supervision (S7-1500)](#overview-of-the-types-of-supervision-s7-1500)
- [Operand supervision (S7-1500)](#operand-supervision-s7-1500)
- [Interlock supervision (S7-1500)](#interlock-supervision-s7-1500)
- [Action supervision (S7-1500)](#action-supervision-s7-1500)
- [Reaction supervision (S7-1500)](#reaction-supervision-s7-1500)
- [Position supervision (S7-1500)](#position-supervision-s7-1500)
- [Text message (S7-1500)](#text-message-s7-1500)
- [Error message (S7-1500)](#error-message-s7-1500)

#### Overview of the types of supervision (S7-1500)

##### Description

With the ProDiag functionality you can define different alarm texts for the following types of supervision:

![Description](images/85152118539_DV_resource.Stream@PNG-en-US.png)

Additional information on the definition of the alarm texts is available here:[Specifying central ProDiag alarm texts](#specifying-central-prodiag-alarm-texts-s7-1500)

> **Note**
>
> **You can find more detailed information on the types of supervision here:**
>
> [Operand supervision](#operand-supervision-s7-1500)
>
> [Interlock supervision](#interlock-supervision-s7-1500)
>
> [Action supervision](#action-supervision-s7-1500)
>
> [Reaction supervision](#reaction-supervision-s7-1500)
>
> [Position supervision](#position-supervision-s7-1500)
>
> [Text message](#text-message-s7-1500)
>
> [Error message](#error-message-s7-1500)

> **Note**
>
> **You will find examples of the types of supervision here:**
>
> [Example of an operand supervision](#example-of-an-operand-supervision-s7-1500)
>
> [Example of an interlock supervision](#example-of-an-interlock-supervision-s7-1500)
>
> [Example of an action supervision](#example-of-an-action-supervision-s7-1500)
>
> [Example of a reaction supervision](#example-of-a-reaction-supervision-s7-1500)
>
> [Example of a position supervision](#example-of-a-position-supervision-s7-1500)
>
> [Example for a text message](#example-for-a-text-message-s7-1500)
>
> [Example of an error message](#example-of-an-error-message-s7-1500)

#### Operand supervision (S7-1500)

##### Description

Operand supervision monitors the signal state (TRUE or FALSE) of a Boolean operand and is mainly used for supervision of so-called "static signals", such as pressure, temperature, signal from the plant, etc.

You can also use operand supervision to monitor two interdependent Boolean operands.

The triggering of an operand supervision sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of an operand supervision:

| Properties | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Delay time | Optional | Time value, e.g. T#2s or a tag of the data type TIME. | Time that is allowed to expire while the supervised signal state of the operand is queued. If the time, e.g. a bounce time, is exceeded, a fault is present and a supervision alarm is displayed. |
| Condition 1 | Optional | TRUE or FALSE | If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.   You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.  You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.   You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Example of an operand supervision (S7-1500)](#example-of-an-operand-supervision-s7-1500)

#### Interlock supervision (S7-1500)

##### Description

The interlock supervision monitors if the action is executed after triggering the action (trigger) and after expiration of the delay time (optional), and if the interlock conditions are met. If the interlock conditions are not met, a fault is present and the action is not executed.

The interlock supervision is often used for supervision of outputs that drive a motor.

The triggering of an interlock supervision sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of an interlock supervision:

| Properties | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Delay time | Optional | Time value, e.g. T#2s or a tag of the data type TIME. | Time that is allowed to expire while the supervised signal state of the operand is queued. If the time, e.g. a bounce time, is exceeded, a fault is present and a supervision alarm is displayed. |
| Actuator (Condition 1) | Mandatory | TRUE or FALSE | Condition 1 must be present.  If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.   You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.  You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
  
[Example of an interlock supervision (S7-1500)](#example-of-an-interlock-supervision-s7-1500)

#### Action supervision (S7-1500)

##### Description

Action supervision monitors whether the production part on the conveyor belt has left the start position within the start-up time after the machine operation. For example, this is not the case if the production part is blocked in its movement. The use of action supervision is especially practical for slow processes, such as the filling of a silo.

The triggering of an action supervision sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of an action supervision:

| Settings | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Start-up time | Mandatory | Time value, min. T#150s or a tag of the data type TIME. | Time that may elapse until the start position must be left. The start-up time must be greater than the cycle time. |
| Action (Condition 1) | Mandatory | TRUE or FALSE | Condition 1 must be present.  If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.   You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.   You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
  
[Example of an action supervision (S7-1500)](#example-of-an-action-supervision-s7-1500)

#### Reaction supervision (S7-1500)

##### Description

The reaction supervision monitors whether the production part on the conveyor belt has reached the desired end position within the reaction time after a machine operation. That cannot happen, for example, if the production part has fallen down or is jammed. The use of reaction supervision is especially practical for fast processes.

The triggering of a reaction supervision sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of a reaction supervision:

| Settings | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Reaction time | Mandatory | Time value, e.g. T#5000 ms or a tag of the data type TIME. | Maximum time that may elapse until the end position must be reached. If the time is exceeded, a fault is present and a supervision alarm is displayed. |
| Action (Condition 1) | Mandatory | TRUE or FALSE | Condition 1 must be present.  If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.   You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.  You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
  
[Example of a reaction supervision (S7-1500)](#example-of-a-reaction-supervision-s7-1500)

#### Position supervision (S7-1500)

##### Description

Position supervision monitors whether the currently reached end position (start or target) of the production part is maintained in a stable manner after expiration of the delay time. The end position should not be left again without a trigger. For example, this is the case if the production part is knocked from a conveyor belt by a forklift truck.

The triggering of a position supervision sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of a position supervision:

| Settings | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Delay time | Optional | Time value, e.g. T#2s or a tag of the data type TIME. | Time that is allowed to expire while the supervised signal state of the operand is queued. If the time, e.g. a bounce time, is exceeded, a fault is present and a supervision alarm is displayed. |
| Action (Condition 1) | Mandatory | TRUE or FALSE | Condition 1 must be present.  If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be adjusted at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.  You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.   You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
  
[Example of a position supervision (S7-1500)](#example-of-a-position-supervision-s7-1500)

#### Text message (S7-1500)

##### Description

Through this additional type of supervision you have the possibility to output only one text that you define in the specific text field. Triggering a text message does not set the group error bit "All" of the "State" status tag in the ProDiag instance data block.

##### Configuration

The following table shows the configuration of a text message:

| Settings | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Delay time | Optional | Time value, e.g. T#2s or a tag of the data type TIME. | Time that is allowed to expire while the supervised signal state of the operand is queued. If the time, e.g. a bounce time, is exceeded, a fault is present and a text message is displayed. |
| Condition 1 | Optional | TRUE or FALSE | If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.   You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Text message was triggered - FALSE = No text message, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.  You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

---

**See also**

[Example for a text message (S7-1500)](#example-for-a-text-message-s7-1500)

#### Error message (S7-1500)

##### Description

The "Error message" type of supervision outputs a simple text message plus an error number. Through this additional type of supervision you have the possibility to output only one text that you define in the specific text field and the error number.

The triggering of an error message sets the error flag in the assigned ProDiag function block. As a result, you can visualize the fault/error on an HMI device with the "ProDiag overview" object and query it in your program, for example, to shut down the machine in case of specific faults/errors.

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Configuration

The following table shows the configuration of an error message:

| Settings | Entry | Operand status | Description |
| --- | --- | --- | --- |
| Supervised tag / parameter * | Mandatory | TRUE or FALSE | Operand to be supervised |
| Delay time | Optional | Time value, e.g. T#2s or a tag of the data type TIME. | Time that is allowed to expire while the supervised signal state of the operand is queued. If the time, e.g. a bounce time, is exceeded, a fault is present and an error message is displayed. |
| Condition 1 | Optional | TRUE or FALSE | If you are using multiple conditions, they are automatically linked with an AND logic operation. |
| Condition 2 | Optional |  |  |
| Condition 3 | Optional |  |  |
| Category | Mandatory | - | You can define up to 8 categories. The first three categories are preassigned by default. However, they can be changed at any time.  1. Error 2. Warning 3. Info   You can specify which categories are available in the ProDiag supervision settings.  You can find additional information here: [Overview of the categories](#overview-of-the-categories-s7-1500) |
| Subcategory 1 | Optional | - | You can define up to 16 entries per subcategory.  You can find additional information here: [Overview of the subcategories](#overview-of-the-subcategories-s7-1500) |
| Subcategory 2 | Optional | - |  |
| ProDiag FB (only for global supervisions) | Mandatory | - | Each supervision must be explicitly assigned to a ProDiag function block.  You can find additional information here: [Overview of the ProDiag function blocks](#overview-of-the-prodiag-function-blocks-s7-1500) |
| Error flag (only for global supervisions) | Is entered by the system. | - | Indicates whether a fault has occurred:  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   The error flag is accessible from HMI and visible in HMI. |
| Alarm text (see settings) | Is entered by the system. | - | You define the content of the alarm text in the ProDiag supervision settings.  You can find additional information here: [Structure of the alarm text editor](#structure-of-the-alarm-text-editor-s7-1500) |
| * Depending on whether you create a local or a global supervision either a supervised tag (global) or a supervised parameter (local) is displayed in the "Properties" tab. |  |  |  |

### Examples for individual types of supervision (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Example of an operand supervision (S7-1500)](#example-of-an-operand-supervision-s7-1500)
- [Example of an interlock supervision (S7-1500)](#example-of-an-interlock-supervision-s7-1500)
- [Example of an action supervision (S7-1500)](#example-of-an-action-supervision-s7-1500)
- [Example of a reaction supervision (S7-1500)](#example-of-a-reaction-supervision-s7-1500)
- [Example of a position supervision (S7-1500)](#example-of-a-position-supervision-s7-1500)
- [Example for a text message (S7-1500)](#example-for-a-text-message-s7-1500)
- [Example of an error message (S7-1500)](#example-of-an-error-message-s7-1500)

#### Introduction (S7-1500)

##### Description

Based on the following example, we will explain all types of supervision to you by gradually moving the production part from the left to the right on the conveyor belt. Different faults can occur during the process; for example, the production part does not leave its start position or the production part does not reach its end position in time. To supervise the entire process and identify all problems, you can implement different supervisions with the ProDiag functionality.​

The figure below serves as template for all subsequent examples:

![Description](images/82256744459_DV_resource.Stream@PNG-en-US.png)

The operands that are required in the respective examples are highlighted in gray.

The following sections include examples for all possible types of supervision:

- [Example of an operand supervision](#example-of-an-operand-supervision-s7-1500)
- [Example of an interlock supervision](#example-of-an-interlock-supervision-s7-1500)
- [Example of an action supervision](#example-of-an-action-supervision-s7-1500)
- [Example of a reaction supervision](#example-of-a-reaction-supervision-s7-1500)
- [Example of a position supervision](#example-of-a-position-supervision-s7-1500)

#### Example of an operand supervision (S7-1500)

##### Requirement

You have created a supervision for the "Conv_Switch_Left" operand and have selected "Operand" as the type of supervision.

##### Description

The figure below shows a conveyor belt at standstill on which the production part is located. The production part is to the left in the start position and is currently not triggered. The arrows visualize the movement of the production part from left to right and from right to left as soon as production starts:

![Description](images/82184954123_DV_resource.Stream@PNG-en-US.png)

The operands required for this supervision are highlighted in gray.

| Operand | Explanation |
| --- | --- |
| Conv_Actor_Forward  Conv_Actor_Backward | These are the control signals (output of the motor) from the user program for movements to the left and right. |
| Conv_Forward_Trigger  Conv_Backward_Trigger | These are the control signals from the user program (e.g. from a GRAPH function block) for triggering the movements to the left and right. |
| Conv_Switch_Left  Conv_Switch_Right | This is the start and target position of the production part. |
| Conv_Auto / Hand | This is the switch for selecting the operating mode. |
| Conv_Push_Button_Forward  Conv_Push_Button_Backward | These are the respective pushbuttons for the forward and backward motion. |

##### Procedure

Enter the following values into the properties of the operand supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Operand | - |
| Supervised tag | Conv_Switch_Left | TRUE  As soon as the operand switches to the signal state TRUE and all conditions are met, the supervision alarm is triggered. |
| Delay time | T#0ms | This fault must be detected and reported immediately. Therefore, 0ms is specified as delay time. |
| Condition 1 | Conv_Switch_Right | TRUE  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | - | The conditions are not required. |
| Condition 3 | - |  |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Switch_Left_O_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | Both operands have the signal state TRUE | Text with explanation that can be output with the supervision alarm. |

##### Result

The supervised operand "Conv_Switch_Left" and the condition 1 "Conv_Switch_Right" are both monitored for the signal state TRUE. This means there is no fault as long as only one of the two changes from the signal state FALSE to TRUE. As soon as both switch to the signal state TRUE, however, a fault is present and a supervision alarm is displayed.

Depending on the settings you have made for basic supervision in the ProDiag supervision settings, the supervision alarm may look as follows:

Supervision alarm for an operand error

Error: Operand: CPU_50: Default_SupervisionFB: I 60.3: Conv_Switch_Left: Both operands have the signal state TRUE

---

**See also**

[Operand supervision (S7-1500)](#operand-supervision-s7-1500)

#### Example of an interlock supervision (S7-1500)

##### Requirement

You have created two supervisions for the "Conv_Actor_Forward" operand and have selected "Interlock" as the type of supervision.

- Supervision_ID_1 (Default_SupervisionFB)
- Supervision_ID_2 (Default_SupervisionFB)

You can implement OR operations in this way. For example, you can define "Automatic mode" as a condition for &lt;Supervision_ID_1&gt; and "Manual mode" as a condition for &lt;Supervision_ID_2&gt;.

> **Note**
>
> **Possible applications**
>
> Ensure that the global tag "Conv_Actor_Forward" is not declared as an input.
>
> You can find additional information on possible applications here: [Possible uses of supervisions](#possible-uses-of-supervisions-s7-1500)

##### Description

The figure below shows a conveyor belt at standstill on which the production part is located. The production part is to the left in the start position and is currently not triggered. The arrows visualize the movement of the production part from left to right and from right to left as soon as production starts:

![Description](images/82193319819_DV_resource.Stream@PNG-en-US.png)

The operands required for this supervision are highlighted in gray.

| Operand | Explanation |
| --- | --- |
| Conv_Actor_Forward  Conv_Actor_Backward | These are the control signals (output of the motor) from the user program for movements to the left and right. |
| Conv_Forward_Trigger  Conv_Backward_Trigger | These are the control signals from the user program (e.g. from a GRAPH function block) for triggering the movements to the left and right. |
| Conv_Switch_Left  Conv_Switch_Right | This is the start and target position of the production part. |
| Conv_Auto / Hand | This is the switch for selecting the operating mode. |
| Conv_Push_Button_Forward  Conv_Push_Button_Backward | These are the respective pushbuttons for the forward and backward motion. |

##### Procedure for automatic mode

Enter the following values into the properties of the interlock supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Interlock | - |
| Supervised tag | Conv_Actor_Forward | FALSE  As soon as the operand switches to the signal state FALSE or even retains the signal state TRUE and all conditions are met, the supervision alarm is triggered. |
| Delay time | T#0ms | This fault must be detected and reported immediately. Therefore, 0ms is specified as delay time. |
| Actuator (Condition 1) | Conv_Forward_Trigger | TRUE  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | Conv_Auto / Manu | TRUE = Automatic mode |
| Condition 3 | - | The condition is not required. |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Actor_Forward_I_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | Automatic mode | Text with explanation that can be output with the supervision alarm. |

##### Procedure for manual mode

Enter the following values into the properties of the operand supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Interlock | - |
| Supervised operand | Conv_Actor_Forward | FALSE  As soon as the operand switches to the signal state FALSE and all conditions are met, the supervision alarm is triggered. |
| Delay time | T#0ms | This fault must be detected and reported immediately. Therefore, 0ms is specified as delay time. |
| Actuator (Condition 1) | Conv_Push_Button_Forward | TRUE  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | Conv_Auto / Manu | FALSE = Manual mode |
| Condition 3 | - | The condition is not required. |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Actor_Forward_I_1.Err | This error bit is set as soon as a fault occurs. |
| Specific text field | Manual mode | Text with explanation that can be output with the supervision alarm. |

##### Result

The movement of the production part from left to right was triggered either by the program with the operand "Conv_Forward_Trigger" or with the pushbutton and the operand "Conv_Push_Button_Forward". The production part has not left the start position on the left, however, and the operand "Conv_Actor_Forward" therefore does not change to the signal state TRUE. This may also happen, for example, in the middle of the motion. This means all requirements for triggering the supervision alarm have been met.

Depending on the settings you have made for basic supervision in the ProDiag supervision settings, the supervision alarms can look like this:

Supervision alarm for an interlock error in automatic mode

Error: Interlock: CPU_50: Default_SupervisionFB: I 61.5: Conv_Actor_Forward: Automatic mode

Supervision alarm for an interlock error in manual mode

Error: Interlock: CPU_50: Default_SupervisionFB: I 61.5: Conv_Actor_Forward: Manual mode

---

**See also**

[Interlock supervision (S7-1500)](#interlock-supervision-s7-1500)

#### Example of an action supervision (S7-1500)

##### Requirement

You have created a supervision for the "Conv_Switch_Left" operand and have selected "Action" as the type of supervision.

> **Note**
>
> **Possible applications**
>
> Ensure that the global tag "Conv_Switch_Left" is not declared as an output.
>
> You can find additional information on possible applications here: [Possible uses of supervisions](#possible-uses-of-supervisions-s7-1500)

##### Description

The figure below shows a conveyor belt at standstill on which the production part is located. The production part is on the left in the start position. The arrows visualize the movement of the production part from left to right and from right to left as soon as production starts. The movement of the production part from left to right is currently triggered by the user program, but the production part does not leave the start position in time:

![Description](images/82214293131_DV_resource.Stream@PNG-en-US.png)

The operands required for this supervision are highlighted in gray.

| Operand | Explanation |
| --- | --- |
| Conv_Actor_Forward  Conv_Actor_Backward | These are the control signals (output of the motor) from the user program for movements to the left and right. |
| Conv_Forward_Trigger  Conv_Backward_Trigger | These are the control signals from the user program (e.g. from a GRAPH function block) for triggering the movements to the left and right. |
| Conv_Switch_Left  Conv_Switch_Right | This is the start and target position of the production part. |
| Conv_Auto / Hand | This is the switch for selecting the operating mode. |
| Conv_Push_Button_Forward  Conv_Push_Button_Backward | These are the respective pushbuttons for the forward and backward motion. |

##### Procedure

Enter the following values into the properties of the action supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Action | - |
| Supervised tag | Conv_Switch_Left | TRUE  When the production part does not leave its start position on the left of the conveyor belt, the operand "Conv_Switch_Left" remains in the signal state TRUE. When all conditions are met as well, the supervision alarm is triggered. |
| Start-up time | T#200ms | The production part must leave its start position within 200ms. |
| Action (Condition 1) | Conv_Actor_Forward | TRUE  The control signal for the movement is present.  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | - | The conditions are not required. |
| Condition 3 | - |  |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Switch_Left_A_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | - | Text with explanation that can be output with the supervision alarm. |

##### Result

The movement of the production part from left to right was triggered either by the program with the operand "Conv_Forward_Trigger". The operand "Conv_Actor_Forward" changes to the signal state TRUE and the forward motion of the production part is to start from left to right. The production part does not leave the start position on the left in time, however, and the operand "Conv_Switch_Left" therefore remains in the signal state TRUE. This means all requirements for triggering the supervision alarm have been met.

Depending on the settings you have made for basic supervision in the ProDiag supervision settings, the supervision alarms can look like this:

Supervision alarm for an interlock error in automatic mode

Error: Action: CPU_50: Default_SupervisionFB: I 60.3: Conv_Switch_Left

---

**See also**

[Action supervision (S7-1500)](#action-supervision-s7-1500)

#### Example of a reaction supervision (S7-1500)

##### Requirement

You have created a supervision for the "Conv_Switch_Right" operand and have selected "Reaction" as the type of supervision.

> **Note**
>
> **Possible applications**
>
> Ensure that the global tag "Conv_Switch_Right" is not declared as an output.
>
> You can find additional information on possible applications here: [Possible uses of supervisions](#possible-uses-of-supervisions-s7-1500)

##### Description

The figure below shows a conveyor belt at standstill on which the production part is located. The production part is on the way from left (start position) to right (end position). The arrows visualize the movement of the production part from left to right and from right to left as soon as production starts. The movement of the production part from left to right was triggered by the user program, but the production part does not reach its end position in time:

![Description](images/82223829771_DV_resource.Stream@PNG-en-US.png)

The operands required for this supervision are highlighted in gray.

| Operand | Explanation |
| --- | --- |
| Conv_Actor_Forward  Conv_Actor_Backward | These are the control signals (output of the motor) from the user program for movements to the left and right. |
| Conv_Forward_Trigger  Conv_Backward_Trigger | These are the control signals from the user program (e.g. from a GRAPH function block) for triggering the movements to the left and right. |
| Conv_Switch_Left  Conv_Switch_Right | This is the start and target position of the production part. |
| Conv_Auto / Hand | This is the switch for selecting the operating mode. |
| Conv_Push_Button_Forward  Conv_Push_Button_Backward | These are the respective pushbuttons for the forward and backward motion. |

##### Procedure

Enter the following values into the properties of the reaction supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Reaction | - |
| Supervised tag | Conv_Switch_Right | FALSE  As soon as the production part reaches its end position, the operand changes to the signal state TRUE. If this does not happen within the reaction time and all conditions are met, the supervision alarm is triggered. |
| Reaction time | T#5000ms | The movement of the production part from left (start position) to right (end position) must not take longer than 5 seconds. |
| Action (Condition 1) | Conv_Actor_Forward | TRUE  The control signal for the movement is present.  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | - | The conditions are not required. |
| Condition 3 | - |  |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Switch_Right_R_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | - | Text with explanation that can be output with the supervision alarm. |

##### Result

The movement of the production part from left to right was triggered either by the program with the operand "Conv_Forward_Trigger". The operand "Conv_Actor_Forward" changes to the signal state TRUE and the forward motion of the production part starts from left to right. The production part does not reach its end position on the right within 5 seconds, however, and the operand "Conv_Switch_Right" remains in the signal state FALSE. This means all requirements for triggering the supervision alarm have been met.

Depending on the settings you have made for basic supervision in the ProDiag supervision settings, the supervision alarms can look like this:

Supervision alarm for a reaction error

Error: Reaction: CPU_50: Default_SupervisionFB: I 60.1: Conv_Switch_Right

---

**See also**

[Reaction supervision (S7-1500)](#reaction-supervision-s7-1500)

#### Example of a position supervision (S7-1500)

##### Requirement

You have created a supervision for the "Conv_Switch_Left" operand and have selected "Position" as the type of supervision.

> **Note**
>
> **Possible applications**
>
> Ensure that the global tag "Conv_Switch_Left" is not declared as an output.
>
> You can find additional information on possible applications here: [Possible uses of supervisions](#possible-uses-of-supervisions-s7-1500)

##### Description

The figure below shows a conveyor belt at standstill on which the production part is located. The production part is on the way from left (start position) to right (end position). The arrows visualize the movement of the production part from left to right and from right to left as soon as production starts. The movement of the production part from left to right was not triggered by the user program, however, and the production part has left its start position without permission:

![Description](images/82226176139_DV_resource.Stream@PNG-en-US.png)

The operands required for this supervision are highlighted in gray.

| Operand | Explanation |
| --- | --- |
| Conv_Actor_Forward  Conv_Actor_Backward | These are the control signals (output of the motor) from the user program for movements to the left and right. |
| Conv_Forward_Trigger  Conv_Backward_Trigger | These are the control signals from the user program (e.g. from a GRAPH function block) for triggering the movements to the left and right. |
| Conv_Switch_Left  Conv_Switch_Right | This is the start and target position of the production part. |
| Conv_Auto / Hand | This is the switch for selecting the operating mode. |
| Conv_Push_Button_Forward  Conv_Push_Button_Backward | These are the respective pushbuttons for the forward and backward motion. |

##### Procedure

Enter the following values into the properties of the reaction supervision:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Position | - |
| Supervised tag | Conv_Switch_Left | FALSE  As soon as the operand switches to the signal state FALSE without permission and all conditions are met, the supervision alarm is triggered. |
| Delay time | T#0ms | This fault must be detected and reported immediately. Therefore, 0ms is specified as delay time. |
| Action (Condition 1) | Conv_Actor_Forward | FALSE  No control signal for the movement is present.  You can use Condition 1 to supervise the two interdependent Boolean operands. |
| Condition 2 | - | The conditions are not required. |
| Condition 3 | - |  |
| Category | 2: Warning | Triggering a supervision alarm is classified as a warning. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Conv_Switch_Left_P_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | Left start position without permission | Text with explanation that can be output with the supervision alarm. |

##### Result

The movement of the production part from left to right was not triggered by the program with the operand "Conv_Forward_Trigger". The operand "Conv_Actor_Forward" remains in the signal state FALSE. The forward motion of the production part from left to right is not supposed to start. However, the production part leaves its start position without permission. This means all requirements for triggering the supervision alarm have been met.

Depending on the settings you have made for basic supervision in the ProDiag supervision settings, the supervision alarms can look like this:

Supervision alarm for an interlock error in automatic mode

Warning: Position: CPU_50: Default_SupervisionFB: I 60.3: Conv_Switch_Left: Left start position without permission

---

**See also**

[Position supervision (S7-1500)](#position-supervision-s7-1500)

#### Example for a text message (S7-1500)

##### Requirement

You have created a supervision for the "Trigger_Message" operand and have selected "Text message" as the type of supervision.

##### Description

You wish to send a text message from the central computer to all the HMI devices, for example, stating that the system will be shut down in an hour in order to carry out maintenance. You can use the "Text message" type of supervision to ensure that you send only this brief information in the supervision alarm, and nothing in addition, such as the CPU name, etc.

The desired text that is to be contained in the supervision alarm is entered into the specific text field.

The tag required for this supervision is as follows:

| Operand | Explanation |
| --- | --- |
| Trigger_Message | A Boolean variable as actuator for the supervision alarm. |

##### Procedure

Enter the following values into the properties of the text message:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Text message | - |
| Supervised tag | Trigger_Message | TRUE  As soon as the tag switches to the signal state TRUE, the supervision alarm is triggered. |
| Delay time | T#0ms | The supervision alarm is to be output immediately. |
| Condition 1 | - | The conditions are not required. |
| Condition 2 | - |  |
| Condition 3 | - |  |
| Category | 3: Info | Triggering a supervision alarm is classified as information. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Trigger_Message_O_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | The system will be shut down in 1 hour. | Text with explanation that is output with the supervision alarm. |

##### Result

As soon as the "Trigger_Message" tag assumes the signal state TRUE, the supervision alarm with the text from the specific text field is output.

The supervision alarm has the following form:

Text message

The system will be shut down in 1 hour.

---

**See also**

[Text message (S7-1500)](#text-message-s7-1500)

#### Example of an error message (S7-1500)

##### Requirement

You have created a supervision for the tag "+01R01_Error" and have selected "Error message" as the type of supervision.

##### Description

You have received a robot from a supplier. In addition to the hardware you have also received a text list with error texts, specially for this robot, and a function block for the robot control. The function block communicates with your program via PROFINET. This means that the robot can signal errors autonomously through its control system. You can have these error texts output in a supervision alarm in the event of a fault.

The function block has, for example, the following form:

![Description](images/87476320651_DV_resource.Stream@PNG-de-DE.png)

The text list with the error texts of the robot has, for example, the following form:

| Text list number | Entry |
| --- | --- |
| 1 | Alarm / Problem 1111 |
| 2 | Alarm / Problem 2222 |
| 3 | Alarm / Problem 3333 |
| 4 | Alarm / Problem 4444 |

The following tags are required to use this function block in your program code:

| Tags | Explanation |
| --- | --- |
| +01R01_Error | A Boolean variable as actuator for the error text. |
| +01R01_Status | Corresponds to the error number |

##### Procedure

Proceed as follows to realize outputting of the error texts of the robot:

1. Create the two required tags in the default tag table.

   ![Procedure](images/87476268299_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/87476268299_DV_resource.Stream@PNG-en-US.png)
2. Call the supplied function block in your program code.
3. Enter the following values into the properties of the alarm:

| Properties | Values | Operand status / Explanation |
| --- | --- | --- |
| Type of supervision | Error message | - |
| Supervised tag | +01R01_Error | TRUE  As soon as the function block of the robot outputs an error and sets the error flag, the tag is set to the signal state TRUE and the supervision alarm is triggered. |
| Delay time | T#0ms | The supervision alarm is to be output immediately. |
| Condition 1 | - | The conditions are not required. |
| Condition 2 | - |  |
| Condition 3 | - |  |
| Category | 1: Error | Triggering a supervision alarm is classified as an error. |
| Subcategory 1 | - | The subcategories are not required. |
| Subcategory 2 | - |  |
| ProDiag FB | Default_SupervisionFB | This is the associated ProDiag function block. As long as you are not using your own function block, the Default_SupervisionFB is used by default. |
| Error flag | Default_SupervisionDB.Trigger_Message_O_1.Err | This error flag is set as soon as a fault occurs. |
| Specific text field | Following associated values  - @4%4d@ (error message) - @4%t#T_Robotor@ (text from text list) | Error text that is output in the supervision alarm. |

You can find additional information on the associated values here: [Structure of the associated values](#structure-of-the-associated-values)

##### Result

As soon as the "+01R01_Error" tag assumes the signal state TRUE, the supervision alarm with the text from the specific text field is output. The error number in three-digit decimal form and the error text from the text list are displayed.

Depending on the settings you have made for error text in the ProDiag supervision settings, an error message may look as follows:

Error message

Error: Err_Txt: CPU_50: Default_SupervisionFB : +01R01_Error : 3: Alarm / Problem 3333

### Application examples for supervisions with ProDiag (S7-1500)

#### Description

You can find a detailed application example for supervisions with ProDiag in the Siemens Industry online support here: [Application example for ProDiag](https://support.industry.siemens.com/cs/ww/en/view/109740151)

## Creating ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Overview of the ProDiag function blocks (S7-1500)](#overview-of-the-prodiag-function-blocks-s7-1500)
- [Structure of a ProDiag function block (S7-1500)](#structure-of-a-prodiag-function-block-s7-1500)
- [Saving the layout of the columns in the ProDiag FB (S7-1500)](#saving-the-layout-of-the-columns-in-the-prodiag-fb-s7-1500)
- [Creating ProDiag function blocks (S7-1500)](#creating-prodiag-function-blocks-s7-1500-1)

### Overview of the ProDiag function blocks (S7-1500)

#### Description

To structure the program code according to the machine and plant units, e.g. Station_1, Station_2, etc., you can create a ProDiag function block for each unit and name it accordingly. A ProDiag function block is created in the PRODIAG programming language and can have a maximum of 250 supervisions in version 1.0 and 1000 supervisions in version 2.0.

As soon as you create a new ProDiag function block, a corresponding ProDiag instance data block is created.

A detailed view of the ProDiag blocks used in your program code and how they relate to one another can be found here:[Displaying supervised user-defined blocks](#displaying-supervised-user-defined-blocks-s7-1500)

#### Advantages of user-defined ProDiag function blocks

The user-defined units offer a number of advantages:

- ProDiag units allow you to better structure your program and benefit from performance advantages.
- Each unit offers group error bits that you can use to define reactions in the user program. In addition, you can implement a simple display on the HMI device.
- You can use the "ProDiag overview" object to create a general overview of all group error bits of this unit on an HMI device.

---

**See also**

[Creating ProDiag function blocks when creating global supervisions (S7-1500)](#creating-prodiag-function-blocks-when-creating-global-supervisions-s7-1500)
  
[Structure of a ProDiag function block (S7-1500)](#structure-of-a-prodiag-function-block-s7-1500)
  
[Overview of calling the ProDiag function blocks (S7-1500)](#overview-of-calling-the-prodiag-function-blocks-s7-1500)
  
[Assigning ProDiag function blocks (S7-1500)](#assigning-prodiag-function-blocks-s7-1500)
  
[Creating ProDiag function blocks (S7-1500)](#creating-prodiag-function-blocks-s7-1500-1)
  
[Editing ProDiag function blocks (S7-1500)](#editing-prodiag-function-blocks-s7-1500)

### Structure of a ProDiag function block (S7-1500)

#### Structure of a ProDiag function block

The following graphic shows the components of a ProDiag function block as an example:

![Structure of a ProDiag function block](images/139840788235_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | Overview of all global supervisions | All supervisions that are assigned to this ProDiag function block. |
| 2 | Overview of all instantiated supervisions |  |

### Saving the layout of the columns in the ProDiag FB (S7-1500)

You can adapt the display of the columns in the ProDiag function block to meet your requirements. For example, you can hide columns that you do not need. You cannot change the sorting order of columns. You can then save your customized view.

#### Procedure

Proceed as follows to save the layout of the columns:

1. Adapt the columns according to your requirements.
2. Click the "Save window settings" button in the ProDiag function block.

#### Result

The layout is saved. When you reopen the ProDiag function block, this layout will be used.

### Creating ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Creating ProDiag function blocks when creating global supervisions (S7-1500)](#creating-prodiag-function-blocks-when-creating-global-supervisions-s7-1500)
- [Creating ProDiag function blocks during the block call (S7-1500)](#creating-prodiag-function-blocks-during-the-block-call-s7-1500)
- [Creating ProDiag function blocks at the instance data block of a function block (S7-1500)](#creating-prodiag-function-blocks-at-the-instance-data-block-of-a-function-block-s7-1500)
- [Creating ProDiag function blocks by using the "Add new block" dialog. (S7-1500)](#creating-prodiag-function-blocks-by-using-the-add-new-block-dialog-s7-1500)
- [Creating ProDiag function blocks in the ProDiag overview tables (S7-1500)](#creating-prodiag-function-blocks-in-the-prodiag-overview-tables-s7-1500)

#### Creating ProDiag function blocks when creating global supervisions (S7-1500)

##### Requirement

You have created at least one global tag.​

##### Procedure

To create a ProDiag function block directly when creating a global supervision, follow these steps:

1. Create a supervision for a global tag.

   The "Supervisions" tab opens in the "Properties" Inspector window and a supervision for the tag is created. When creating the first supervision, the ProDiag function block "Default_SupervisionFB" is created automatically.
2. Enter the desired properties.
3. Click the "…" selection field at ProDiag FB.

   A selection dialog opens.
4. All existing ProDiag function blocks are displayed in the right-hand column.
5. To create a new ProDiag function block, click "Add new".

   The "Add new block" dialog opens.
6. Enter a name for the new ProDiag function block.
7. To enter additional properties for the new ProDiag function block, click "Additional information".

   An area with additional entry fields is displayed.
8. Enter the desired properties.
9. Confirm your entries with "OK".​

##### Result

In addition to the new ProDiag function block, a corresponding ProDiag instance data block is also created. You can find the blocks in the project tree in the "Program blocks" folder.

#### Creating ProDiag function blocks during the block call (S7-1500)

##### Requirement

You have created a function module that contains at least one local supervision.

##### Procedure

Proceed as follows to create a ProDiag function block directly when calling a function block:

1. Call the function block that contains the supervisions in the program code.

   The "Call options" dialog opens.
2. Click the "…" selection field at ProDiag FB.

   A selection dialog opens. If it exists, the ProDiag function block "Default_SupervisionFB" is displayed automatically. If this does not exist, the first user-defined ProDiag function block to be found is displayed.
3. To create a new ProDiag function block, click "Add new".

   The "Add new block" dialog opens.
4. Enter a name for the new ProDiag function block.
5. To enter additional properties for the new ProDiag function block, click "Additional information".

   An area with additional entry fields is displayed.
6. Enter the desired properties.
7. Confirm your entries with "OK".​

##### Result

In addition to the new ProDiag function block, a corresponding ProDiag instance data block is also created. You can find the blocks in the project tree in the "Program blocks" folder. The supervisions of the function block are instantiated.

#### Creating ProDiag function blocks at the instance data block of a function block (S7-1500)

##### Requirement

You have created and compiled a function module that contains at least one local supervision.

##### Procedure

Proceed as follows to create a ProDiag function block in the properties of the instance data block:

1. Right-click the instance data block of a function block that contains local supervisions.
2. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the instance data block opens.
3. Click the "Attributes" section.
4. In "Assigned ProDiag FB", click the selection box "...".

   A selection dialog opens.
5. All existing ProDiag function blocks are displayed in the right-hand column.
6. To create a new ProDiag function block, click "Add new".

   The "Add new block" dialog opens.
7. Enter a name for the new ProDiag function block.
8. To enter additional properties for the new ProDiag function block, click "Additional information".

   An area with additional entry fields is displayed.
9. Enter the desired properties.
10. Confirm your entries with "OK".​

##### Result

In addition to the new ProDiag function block, a corresponding ProDiag instance data block is also created. You can find the blocks in the project tree in the "Program blocks" folder. The supervisions of the function block are instantiated.

#### Creating ProDiag function blocks by using the "Add new block" dialog. (S7-1500)

##### Requirement

The "Program blocks" folder in the project tree is open.

##### Procedure

To create a ProDiag function block using the "Add new block" dialog, follow these steps:

1. Double-click the "Add new block" command.

   The "Add new block" dialog opens.
2. Click the "Function block" button.
3. Enter a name for the new ProDiag function block.
4. Select in the "Language &gt; PRODIAG (incl. IDB)" section.
5. To enter additional properties for the new ProDiag function block, click "Additional information".

   An area with additional entry fields is displayed.
6. Enter the desired properties.
7. Select the "Add new and open" check box if the ProDiag function block does not open as soon as it is created.
8. Confirm your entries with "OK".

Or:

Proceed as follows to assign a ProDiag function block to an existing user-defined function block that contains local supervisions by using the "Add new block" dialog:

1. Double-click the "Add new block" command.

   The "Add new block" dialog opens.
2. Click "Data block".
3. For type, select from the drop-down list the already created user-defined function block which contains the local supervisions.
4. Click the "…" selection field at ProDiag FB.

   A selection dialog opens.
5. All existing ProDiag function blocks are displayed in the right-hand column.
6. To create a new ProDiag function block, click "Add new".

   The "Add new block" dialog opens.
7. From this point, the procedure described above from item 2 applies.

##### Result

In addition to the new ProDiag function block, a corresponding ProDiag instance data block is also created. You can find the blocks in the project tree in the "Program blocks" folder. The local supervisions are instantiated.

#### Creating ProDiag function blocks in the ProDiag overview tables (S7-1500)

##### Requirement

You have created local and global supervisions.

The ProDiag overview under "PLC supervisions and alarms" is open.

##### Procedure

To create a ProDiag function block in the ProDiag overview tables "Global supervisions" or "Supervision instances", follow these steps:

1. Click the "…" selection field in the "ProDiag FB" column.

   A selection dialog opens.
2. All existing ProDiag function blocks are displayed in the right-hand column.
3. To create a new ProDiag function block, click "Add new".

   The "Add new block" dialog opens.
4. Enter a name for the new ProDiag function block.
5. To enter additional properties for the new ProDiag function block, click "Additional information".

   An area with additional entry fields is displayed.
6. Enter the desired properties.
7. Confirm your entries with "OK".​

##### Result

In addition to the new ProDiag function block, a corresponding ProDiag instance data block is also created. You can find the blocks in the project tree in the "Program blocks" folder. The local supervisions are instantiated.

## Using a central time stamp (S7-1500)

This section contains information on the following topics:

- [Using a central time stamp (S7-1500)](#using-a-central-time-stamp-s7-1500-1)
- [Multiple supervision alarms of a ProDiag FB within one cycle time (S7-1500)](#multiple-supervision-alarms-of-a-prodiag-fb-within-one-cycle-time-s7-1500)

### Using a central time stamp (S7-1500)

#### Description

As of ProDiag function block version 2.0, you have the option to specify a central time stamp tag in the ProDiag supervision settings and then use it in every CPU in the entire project.

The central time stamp tag is defined as a global tag or as a global data component in the relevant CPU.

The same system time is assigned to all ProDiag supervision alarms within a program cycle that are sent by ProDiag function blocks when the "Use central time stamps" option is enabled.

#### Requirement

The ProDiag function block has version 2.0.

> **Note**
>
> **ProDiag function block version 1.0**
>
> The local block time stamp continues to be assigned to all ProDiag supervision alarms that are sent by a version 1.0 ProDiag function block.

#### Procedure

To use a central time stamp, follow these steps:

1. Ensure that the block has version 2.0 in the block properties of the ProDiag function block.
2. In the project tree under "Common data" &gt; "Supervision settings" &gt; "General", open the "Central time stamp" area.
3. Define a time stamp tag by entering a free text into the text field.

   ![Procedure](images/102602503563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/102602503563_DV_resource.Stream@PNG-en-US.png)
4. In each CPU in which you want to use this time stamp, define a global tag or global data block with the label from the free text field of the LDT data type.

   ![Procedure](images/102604220555_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/102604220555_DV_resource.Stream@PNG-de-DE.png)
5. To copy the current time tamp "TimeStampTag" to the global time tamp tag, expand your program code (for example, Main[OB1]) in the corresponding CPUs with a time function, for example "RD_SYS_T":

   ![Procedure](images/102605624843_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/102605624843_DV_resource.Stream@PNG-de-DE.png)
6. If you want to use the central time stamp in existing ProDiag function blocks, you need to select the "Use central time stamp" option in the block properties of the respective ProDiag function block.

   If you create the ProDiag function blocks only after defining the central time stamp tag, this option is activated automatically.

#### Result

All ProDiag supervision alarms whose function block has enabled the "Use central time stamp" option are given a uniform time stamp within a program cycle.

### Multiple supervision alarms of a ProDiag FB within one cycle time (S7-1500)

#### Description

Only one supervision alarm can be displayed for each ProDiag function block per CPU cycle time, even if several faults have occurred simultaneously. All simultaneously triggered ProDiag supervision alarms of a ProDiag function block receive the same time stamp, which contains the time of the triggering fault. The remaining supervision alarms, i.e. one for each CPU cycle time, can be processed one after the other. This prevents jumps in the cycle time caused by alarm storms.

You can display the time stamps of the supervision alarms, for example, in the "Time" column in the alarm display.

Depending on whether or not you have enabled the "Use central time stamp" option in the ProDiag function block, either the current system time or the local block time is used as a time stamp.

---

**See also**

[Using a central time stamp (S7-1500)](#using-a-central-time-stamp-s7-1500-1)

## Using ProDiag instance data bases (S7-1500)

This section contains information on the following topics:

- [Structure of a ProDiag instance data block of version 1.0 (S7-1500)](#structure-of-a-prodiag-instance-data-block-of-version-10-s7-1500)
- [Content of a ProDiag instance data block of version 1.0 (S7-1500)](#content-of-a-prodiag-instance-data-block-of-version-10-s7-1500)
- [Structure of a ProDiag instance data block of version 2.0 (S7-1500)](#structure-of-a-prodiag-instance-data-block-of-version-20-s7-1500)
- [Content of a ProDiag instance data block of version 2.0 (S7-1500)](#content-of-a-prodiag-instance-data-block-of-version-20-s7-1500)

### Structure of a ProDiag instance data block of version 1.0 (S7-1500)

#### Structure of a ProDiag instance data block of version 1.0

The following graphic shows the components of a ProDiag instance data block as an example:

![Structure of a ProDiag instance data block of version 1.0](images/100697180299_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | The block interface of the ProDiag instance data block | The block interface cannot be edited. |
| 2 | The "State" status tag in the "Static" section | The "State" status tag of the "SV_FB_State" PLC data type contains the group error bits of all the supervisions that are assigned to this ProDiag instance data block.  There are two different types of group error bits:  - Group error bit for the supervision types (All, O, I, R, A, P, Merr and Mtxt) - Group error bit for the categories (C1, C2, C3, C4, C5, C6, C7, and C8)   You can visualize these group error bits either in your HMI device with the "ProDiag overview" object or you can program them in your program code as condition for further execution of the program code. You only have read access to the group error bits in the program code. As soon as a supervision alarm is triggered, the group error bits of the assigned ProDiag instance data block are set. |
| 3 | Status tags | These tags are displayed if supervisions have been created and are assigned to this ProDiag instance data block. |

### Content of a ProDiag instance data block of version 1.0 (S7-1500)

#### Block interface

As soon as you create a new ProDiag function block, a corresponding ProDiag instance data block is created.

The following elements are available in the "Static" section:

#### State

| Name |  | Data type | Explanation |
| --- | --- | --- | --- |
| State |  | SV_FB_State | System-internal, know-how-protected PLC data type |
|  | Total_Number | UINT | Total number of all supervisions to which this ProDiag function block was assigned. |
| All | BOOL | Group error bit for all contained types of supervision, except text message:  - TRUE =&gt; At least one supervision has been triggered in the current program cycle. - FALSE =&gt; No supervision has been triggered.   Accessible from HMI and visible in HMI. |  |
| O (Operand) | BOOL | Group error bit for all operand supervisions:  - TRUE =&gt; At least one operand supervision has been triggered in the current program cycle. - FALSE =&gt; No operand supervision has been triggered. |  |
| I (Interlock) | BOOL | Group error bit for all interlock supervisions:  - TRUE =&gt; At least one interlock supervision has been triggered in the current program cycle. - FALSE =&gt; No interlock supervision has been triggered. |  |
| R (Reaction) | BOOL | Group error bit for all reaction supervisions:  - TRUE =&gt; At least one reaction supervision has been triggered in the current program cycle. - FALSE =&gt; No reaction supervision has been triggered. |  |
| A (Action) | BOOL | Group error bit for all action supervisions:  - TRUE =&gt; At least one action supervision has been triggered in the current program cycle. - FALSE =&gt; No action supervision has been triggered. |  |
| P (Position) | BOOL | Group error bit for all position supervisions:  - TRUE =&gt; At least one position supervision has been triggered in the current program cycle. - FALSE =&gt; No position supervision has been triggered. |  |
| Merr (Message error) | BOOL | Group error bit for all error messages:  - TRUE =&gt; At least one error message has been triggered in the current program cycle. - FALSE =&gt; No error message has been triggered. |  |
| Mtxt (Message text) | BOOL | Group error bit for all text messages:  - TRUE =&gt; At least one text message was triggered in the current program cycle. - FALSE =&gt; No text message was triggered. |  |
| SV_Types (Types of supervision) | BYTE | Byte for all group error bits of the types of supervision  A type of supervision is assigned to each individual bit. As a result, you can use this byte, for example, in the "ProDiag overview" object on the HMI device to create a display that shows at first glance when a supervision of a certain type of supervision has been triggered.  - Bit 1 =&gt; Operand - Bit 2 =&gt; Interlock - etc.   Accessible from HMI and visible in HMI. |  |
| C1 (Category) | BOOL | First category (The first category = Error by default. This cannot be changed.)  - TRUE =&gt; At least one supervision alarm of category C1 has been triggered in the current program cycle. - FALSE =&gt; No error has occurred. |  |
| C2 (Category) | BOOL | Second category (The second category = Warning by default. You can change the setting at any time.)  - TRUE =&gt; At least one supervision alarm of category C2 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C3 (Category) | BOOL | Third category (The third category = Info by default. You can change the setting at any time.)  - TRUE =&gt; At least one supervision alarm of category C3 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C4 (Category) | BOOL | Fourth category  - TRUE =&gt; At least one supervision alarm of category C4 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C5 (Category) | BOOL | Fifth category  - TRUE =&gt; At least one supervision alarm of category C5 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C6 (Category) | BOOL | Sixth category  - TRUE =&gt; At least one supervision alarm of category C6 has been triggered in the current program cycle. - FALSE =&gt;There are no faults. |  |
| C7 (Category) | BOOL | Seventh category  - TRUE =&gt; At least one supervision alarm of category C7 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C8 (Category) | BOOL | Eighth category  - TRUE =&gt; At least one supervision alarm of category C8 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| Categories | BYTE | Group error byte for all categories  A category is assigned to each individual bit. As a result, you can use this byte, for example, in the ProDiag overview object on the HMI device to create a display that shows at first glance when a supervision of a certain category has been triggered.  - Bit 1 =&gt; Category 1 (C1) - Bit 2 =&gt; Category 2 (C2) - etc.   Accessible from HMI and visible in HMI. |  |
| Sub_Cat_1 (Subcategory 1) | DWORD | Group error bits for subcategories 1 (Bit 1 to 16) |  |
| Sub_Cat_2 (Subcategory 2) | DWORD | Group error bits for subcategories 2 (Bit 1 to 16) |  |
| Reserved | BYTE | Reserve byte |  |

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

#### Optional status tag as soon as a supervision has been created

As soon as you create a supervision, this section is displayed in the block interface in addition:

| Name |  |  | Data type | Explanation |
| --- | --- | --- | --- | --- |
| e.g. Conv_Push_Button_Forward_O_1  - Conv_Push_Button_Forward = Name of the supervised operand - O = "Operand" type of supervision - 1 = Total number of supervisions of the "Operand" type of supervision |  |  | SV_State | System-internal, know-how-protected PLC data type |
|  | Err (Error) |  | BOOL | Error that is also displayed in the properties of the supervision. Indicates whether a supervision alarm has been triggered.  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   Accessible from HMI and visible in HMI |
| Err_Neg_Flag (Error_Negativ_Flag) |  | BOOL | For the negative edge evaluation of the error flag |  |
| T_D_E_Going (Time_Date_Error_Going) |  | LDT | Time and day in the program cycle at which the fault went out |  |
| E_Flag (Error_Flag) |  | BOOL | Error flag: Only one supervision alarm is sent per ProDiag function block and per program cycle. |  |
| E_Pos_Flag (Error_Positive_Flag) |  | BOOL | For the positive edge evaluation of the error flag |  |
| T_D_E_Coming (Time_Date_Error_Coming) |  | LDT | Time and day in the program cycle at which the fault occurred. |  |
| S_Coming (Signal_Coming) |  | BOOL | Bit memory  - TRUE = Supervision alarm was sent fault-free - FALSE = There is a fault/error. |  |
| Pos_Flag (Positive_Flag) |  | BOOL | This bit memory is only needed for the "Position" type of supervision. |  |
| Ti (Timer) |  | TON_TIME | This time is needed to generate the delay time. |  |
|  | PT (Preset Time) | TIME | Preset time value |  |
| ET (Elapsed Time) | TIME | Current time value |  |  |
| IN (Input) | TIME | Start input |  |  |
| Q (Output) | TIME | Output that is set after expiration of time PT |  |  |

### Structure of a ProDiag instance data block of version 2.0 (S7-1500)

#### Structure of a ProDiag instance data block of version 2.0

The following graphic shows the components of a ProDiag instance data block as an example:

![Structure of a ProDiag instance data block of version 2.0](images/100698073995_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation |  | Additional information |
| --- | --- | --- | --- |
| 1 | The block interface of the ProDiag instance data block |  | The block interface cannot be edited. |
| 2 | The status tag "PC_Flags" |  | The "PC_Flags" status tag of the "PC_Flags_V2" PLC data type contains the version of the ProDiag function block (Version parameter) and the CRIT_ON parameter which indicates whether initial value acquisition is enabled. |
| 3 | The status tag "State" |  | The "State" status tag of the "SV_FB_State_V2" PLC data type contains the group error bits of all the supervisions that are assigned to this ProDiag instance data block.  There are two different types of group error bits:  - Group error bit for the supervision types (All, O, I, R, A, P, Merr and Mtxt) - Group error bit for the categories (C1, C2, C3, C4, C5, C6, C7, and C8)   You can visualize these group error bits either in your HMI device with the "ProDiag overview" object or you can program them in your program code as condition for further execution of the program code. You have read and write access to the group error bits in the program code. As soon as a supervision alarm is triggered, the group error bits of the assigned ProDiag instance data block are set. |
| 4 | Status tags |  | These tags of the "SV_State_V2" PLC data type are displayed if supervisions have been created and are assigned to this ProDiag instance data block. |
| 5 |  | The parameters Crit_Avail and Crit_Err | - Crit_Avail:   Signal state = TRUE: Initial values were recorded. - Crit_Err:   Storing the 32 signal states per network of a LAD or FBD block. |

### Content of a ProDiag instance data block of version 2.0 (S7-1500)

#### Block interface

As soon as you create a new ProDiag function block, a corresponding ProDiag instance data block is created.

The following elements are available in the "Static" section:

#### State

| Name |  | Data type | Explanation |
| --- | --- | --- | --- |
| PC_Flags |  | PC_Flags_V2 | System-internal, know-how-protected PLC data type |
|  | Version | String[10] | Version of the ProDiag function block |
|  | Crit_On | BOOL | Indicates whether the initial value acquisition is enabled. |
| State |  | SV_FB_State_V2 | System-internal, know-how-protected PLC data type |
|  | Total_Number | UINT | Total number of all supervisions to which this ProDiag function block was assigned. |
| All | BOOL | Group error bit for all contained types of supervision, except text message:  - TRUE =&gt; At least one supervision has been triggered in the current program cycle. - FALSE =&gt; No supervision has been triggered.   Accessible from HMI and visible in HMI. |  |
| O (Operand) | BOOL | Group error bit for all operand supervisions:  - TRUE =&gt; At least one operand supervision has been triggered in the current program cycle. - FALSE =&gt; No operand supervision has been triggered. |  |
| I (Interlock) | BOOL | Group error bit for all interlock supervisions:  - TRUE =&gt; At least one interlock supervision has been triggered in the current program cycle. - FALSE =&gt; No interlock supervision has been triggered. |  |
| R (Reaction) | BOOL | Group error bit for all reaction supervisions:  - TRUE =&gt; At least one reaction supervision has been triggered in the current program cycle. - FALSE =&gt; No reaction supervision has been triggered. |  |
| A (Action) | BOOL | Group error bit for all action supervisions:  - TRUE =&gt; At least one action supervision has been triggered in the current program cycle. - FALSE =&gt; No action supervision has been triggered. |  |
| P (Position) | BOOL | Group error bit for all position supervisions:  - TRUE =&gt; At least one position supervision has been triggered in the current program cycle. - FALSE =&gt; No position supervision has been triggered. |  |
| Merr (Message error) | BOOL | Group error bit for all error messages:  - TRUE =&gt; At least one error message has been triggered in the current program cycle. - FALSE =&gt; No error message has been triggered. |  |
| Mtxt (Message text) | BOOL | Group error bit for all text messages:  - TRUE =&gt; At least one text message was triggered in the current program cycle. - FALSE =&gt; No text message was triggered. |  |
| SV_Types (Types of supervision) | BYTE | Byte for all group error bits of the types of supervision  A type of supervision is assigned to each individual bit. As a result, you can use this byte, for example, in the "ProDiag overview" object on the HMI device to create a display that shows at first glance when a supervision of a certain type of supervision has been triggered.  - Bit 1 =&gt; Operand - Bit 2 =&gt; Interlock - etc.   Accessible from HMI and visible in HMI. |  |
| C1 (Category) | BOOL | First category (The first category = Error by default. This cannot be changed.)  - TRUE =&gt; At least one supervision alarm of category C1 has been triggered in the current program cycle. - FALSE =&gt; No error has occurred. |  |
| C2 (Category) | BOOL | Second category (The second category = Warning by default. You can change the setting at any time.)  - TRUE =&gt; At least one supervision alarm of category C2 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C3 (Category) | BOOL | Third category (The third category = Info by default. You can change the setting at any time.)  - TRUE =&gt; At least one supervision alarm of category C3 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C4 (Category) | BOOL | Fourth category  - TRUE =&gt; At least one supervision alarm of category C4 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C5 (Category) | BOOL | Fifth category  - TRUE =&gt; At least one supervision alarm of category C5 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C6 (Category) | BOOL | Sixth category  - TRUE =&gt; At least one supervision alarm of category C6 has been triggered in the current program cycle. - FALSE =&gt;There are no faults. |  |
| C7 (Category) | BOOL | Seventh category  - TRUE =&gt; At least one supervision alarm of category C7 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| C8 (Category) | BOOL | Eighth category  - TRUE =&gt; At least one supervision alarm of category C8 has been triggered in the current program cycle. - FALSE =&gt; There are no faults. |  |
| Categories | BYTE | Group error byte for all categories  A category is assigned to each individual bit. As a result, you can use this byte, for example, in the ProDiag overview object on the HMI device to create a display that shows at first glance when a supervision of a certain category has been triggered.  - Bit 1 =&gt; Category 1 (C1) - Bit 2 =&gt; Category 2 (C2) - etc.   Accessible from HMI and visible in HMI. |  |
| Sub_Cat_1 (Subcategory 1) | DWORD | Group error bits for subcategories 1 (Bit 1 to 16) |  |
| Sub_Cat_2 (Subcategory 2) | DWORD | Group error bits for subcategories 2 (Bit 1 to 16) |  |
| Reserved | BYTE | Reserve byte |  |

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> For additional information, refer to the information system of the TIA Portal. "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

#### Optional status tag as soon as a supervision has been created

As soon as you create a supervision, this section is displayed in the block interface in addition:

| Name |  |  | Data type | Explanation |
| --- | --- | --- | --- | --- |
| e.g. Conv_Push_Button_Forward_O_1  - Conv_Push_Button_Forward = Name of the supervised operand - O = "Operand" type of supervision - 1 = Total number of supervisions of the "Operand" type of supervision |  |  | SV_State_V2 | System-internal, know-how-protected PLC data type |
|  | Err (Error) |  | BOOL | Error that is also displayed in the properties of the supervision. Indicates whether a supervision alarm has been triggered.  - TRUE = Supervision alarm was triggered - FALSE = No supervision alarm, which means the fault has not occurred   Accessible from HMI and visible in HMI |
| Err_Neg_Flag (Error_Negativ_Flag) |  | BOOL | For the negative edge evaluation of the error flag |  |
| T_D_E_Going (Time_Date_Error_Going) |  | LDT | Time and day in the program cycle at which the fault went out |  |
| E_Flag (Error_Flag) |  | BOOL | Error flag: Only one supervision alarm is sent per ProDiag function block and per program cycle. |  |
| E_Pos_Flag (Error_Positive_Flag) |  | BOOL | For the positive edge evaluation of the error flag |  |
| T_D_E_Coming (Time_Date_Error_Coming) |  | LDT | Time and day in the program cycle at which the fault occurred. |  |
| S_Coming (Signal_Coming) |  | BOOL | Bit memory  - TRUE = Supervision alarm was sent fault-free - FALSE = There is a fault/error. |  |
| Pos_Flag (Positive_Flag) |  | BOOL | This bit memory is only needed for the "Position" type of supervision. |  |
| Ti (Timer) |  | TON_TIME | This time is needed to generate the delay time. |  |
|  | PT (Preset Time) | TIME | Preset time value |  |
| ET (Elapsed Time) | TIME | Current time value |  |  |
| IN (Input) | TIME | Start input |  |  |
| Q (Output) | TIME | Output that is set after expiration of time PT |  |  |
| Crit_Avail |  | BOOL | Signal state = TRUE: Initial values were recorded. |  |
| Crit_Err |  | DWORD | Storing the 32 signal states per network of a LAD or FBD block. |  |

## Defining properties for a ProDiag function block (S7-1500)

This section contains information on the following topics:

- [Structure of supervision settings at a ProDiag FB (S7-1500)](#structure-of-supervision-settings-at-a-prodiag-fb-s7-1500)
- [Creating the enablers for supervision alarms (S7-1500)](#creating-the-enablers-for-supervision-alarms-s7-1500)
- [Defining an acknowledge tag for individual categories (S7-1500)](#defining-an-acknowledge-tag-for-individual-categories-s7-1500)
- [Setting display classes (S7-1500)](#setting-display-classes-s7-1500)
- [Displaying the number of supervisions for a ProDiag FB (S7-1500)](#displaying-the-number-of-supervisions-for-a-prodiag-fb-s7-1500)

### Structure of supervision settings at a ProDiag FB (S7-1500)

#### Structure of supervision settings

The following figure shows the components of the supervision settings:

![Structure of supervision settings](images/87574562315_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | Global enabler of a ProDiag function block | You can use the global enabler to control the call of a ProDiag function blocks in the ProDiag organization block.  You can find additional information here: [Using the global enabler](#using-the-global-enabler-s7-1500) |
| 2 | The "Use in ProDiag FB" cannot be edited. | If a supervision of this category is assigned to the ProDiag function block, the category is activated. |
| 3 | Category enabler | You can use the category enabler to define an enabler (global Boolean tag) for the ProDiag function block and for each individual category contained therein and use this to activate or deactivate the supervisions of this category.  You can find additional information here: [Using the category enabler](#using-the-category-enabler-s7-1500) |
| 4 | Acknowledge tag | You can use the acknowledge tag to acknowledge a supervision alarm of a category within the STEP 7 project. This ensures that the supervision alarm only goes again when the problem has been eliminated. You can control the program sequence with the relevant error flag.  You can find additional information here: [Use acknowledge tag](#use-acknowledge-tag-s7-1500) |
| 5 | Display class | You can use the display class to define which supervisions are to be displayed on an HMI device.  You can find additional information here: [Setting the display class](#setting-the-display-class-s7-1500) |

### Creating the enablers for supervision alarms (S7-1500)

This section contains information on the following topics:

- [Overview of the enablers (S7-1500)](#overview-of-the-enablers-s7-1500)
- [Using the global enabler (S7-1500)](#using-the-global-enabler-s7-1500)
- [Using the category enabler (S7-1500)](#using-the-category-enabler-s7-1500)

#### Overview of the enablers (S7-1500)

##### Description

You have the option of creating enablers (Boolean tags) in the settings of a ProDiag function block. Two different types of enablers are available for this:

- Global enabler
- Category enabler

##### Global enabler

You can control the call of the ProDiag function blocks in the ProDiag organization block using the global enabler. The ProDiag is created automatically as soon as you compile your project. For example, you can deactivate all supervisions of a ProDiag function block by defining a global enabler that is used automatically by the system as a call condition as soon as the ProDiag function block is called in the ProDiag organization block. If the call condition is not met (signal state = False), the ProDiag function block is not called and no supervision alarms are displayed. The global enabler must be a global Boolean tag.

However, when you do not call the ProDiag function block in ProDiag OB but in another block within your program, you must integrate the global enabler in the program code yourself if you wish to use it.

The global enabler offers you the following advantages:

- You can control which ProDiag function block is to be processed in which program cycle. All ProDiag function blocks that have not been processed do not display any supervision alarms even if a fault has occurred.
- If you assign the same tag as an enabler to all ProDiag function blocks, you can easily program, for example, that no undesired supervisions are to be triggered during commissioning.
- In the case of very critical cycle times, you can achieve performance improvements by assigning different global Boolean tags as enablers to the ProDiag function blocks and using this to selectively call the blocks in the program code.
- If a supervision alarm has already been triggered, it exists until the corresponding ProDiag function block is called again. As soon as the ProDiag function block is processed again, the supervision alarm is displayed.

##### Category enabler

You can use the category enabler to define an enabler (global Boolean tag) for each ProDiag function block and for each individual category contained therein and use this to activate or deactivate the supervisions of this category. In this way, you can influence all supervisions of the "Error" category of a ProDiag function block, for example. If you use the category enabler as a call condition within your program code and the call condition (signal state = False) is not met during runtime, none of the supervisions of this category are executed. This means that the group error bits in the block interface of the ProDiag function block are not changed and no supervision alarms are displayed.

The category enabler offers you the following advantages:

- You can selectively deactivate the supervision alarms of an individual category within a ProDiag function block.
- If a supervision alarm has already been triggered, it is revoked (identified as "Going"). As long as the global Boolean tag has the signal state = False, for example, during maintenance work, no unnecessary supervision alarms are displayed.

---

**See also**

[Using the global enabler (S7-1500)](#using-the-global-enabler-s7-1500)
  
[Using the category enabler (S7-1500)](#using-the-category-enabler-s7-1500)

#### Using the global enabler (S7-1500)

##### Requirement

You have created a ProDiag function block and a supervision.

##### Procedure

To use a global enabler, follow these steps:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. In the "General" tab, select the "Supervision settings" entry.
3. Specify a global Boolean tag as global enabler.

   For the global enabler to have an effect on the sequence of the program code, you must not call the ProDiag function block in a user-defined program block. This means that ProDiag function block is automatically called in the ProDiag organization block.

##### Result

Only those supervision alarms of the ProDiag function blocks whose global enabler has the signal state "1" are displayed.

#### Using the category enabler (S7-1500)

##### Requirement

You have created a ProDiag function block and a supervision.

##### Procedure

To use a category enabler, follow these steps:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. In the "General" tab, select the "Supervision settings" entry.
3. Use an enabler for the individual categories in the "Categories" area.

   For the enabler to also have an effect on the sequence of the program code, you must use it as step enabling condition in the program code.

##### Result

Only those supervision alarms of the categories of the ProDiag function block whose enabler has the signal state "1" are displayed.

### Defining an acknowledge tag for individual categories (S7-1500)

This section contains information on the following topics:

- [Overview of the acknowledge tags (S7-1500)](#overview-of-the-acknowledge-tags-s7-1500)
- [Use acknowledge tag (S7-1500)](#use-acknowledge-tag-s7-1500)

#### Overview of the acknowledge tags (S7-1500)

##### Description

You have the option of using a global Boolean tag as an acknowledge tag for each individual category in each ProDiag function block.

By using the acknowledge tag you initially bring about that the error flag and the group error bits retain the signal status TRUE and that the supervision alarm does not go. So that, for example, the conveyor belt is stopped immediately you need to use these error bits explicitly in your program code. This provides you with the option that the conveyor belt, for example, does not start up again until the supervision error has been explicitly acknowledged by the machine operator even if the cause of the fault, such as a breached light barrier, has already been corrected. There is also the acknowledgment of the supervision alarm on an HMI device; however, it does not have an impact on the processing of the program code.

You can use a separate acknowledge tag for each of the 8 categories and incorporate this in your program code as a step enabling condition for the ongoing program sequence.

The error bits are retained in the ProDiag function block once the fault has been corrected until the signal state of the acknowledge tag changes from "0" to "1". The processing of the program code cannot continue until you confirm the acknowledge tag, which means the signal state changes from "0" to "1":

- The error flag is reset to the signal state "0" once again.
- The group error bits for HMI are also reset to "0".
- The supervision alarm on the HMI device disappears.

#### Use acknowledge tag (S7-1500)

##### Requirement

You have created a ProDiag function block and a supervision.

##### Procedure

To use an acknowledge tag, follow these steps:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. In the "General" tab, select the "Supervision settings" entry.
3. Use acknowledge tags for the individual categories in the "Categories" area.

   For the acknowledge tags to have an effect on the sequence of the program code, you must use the error flag as a step enabling condition in the program code.

##### Result

A fault has occurred and the supervision alarm was triggered. The program code is not processed further until the fault has been corrected and the acknowledge tag has been confirmed.

### Setting display classes (S7-1500)

This section contains information on the following topics:

- [Overview of display classes (S7-1500)](#overview-of-display-classes-s7-1500)
- [Setting the display class (S7-1500)](#setting-the-display-class-s7-1500)

#### Overview of display classes (S7-1500)

##### Description

You have the option of defining a display class for each individual category in each ProDiag function block.

You can use the display classes to define which supervisions are to be displayed on an HMI device. This is useful, in particular, when multiple HMI devices are connected to a CPU. In order for the supervisions to be correctly displayed, you must activate the display classes that are to be displayed for each HMI device.

A maximum of 17 display classes are possible.

#### Setting the display class (S7-1500)

##### Requirement

You have created a ProDiag function block and a supervision.

##### Procedure

To set a display class, follow these steps:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. In the "General" tab, select the "Supervision settings" entry.
3. Set the display classes for the individual categories in the "Categories" area.

##### Result

If you have assigned display class "1" to the "Error" category, for example, and you activate this display class for an HMI device, only the supervision alarms that are assigned to the "Error" category are displayed on this HMI device.

### Displaying the number of supervisions for a ProDiag FB (S7-1500)

#### Description

From the properties of the ProDiag function block you can read out how many ProDiag supervisions are assigned to this ProDiag FB.

#### Procedure

To read out the number of assigned ProDiag supervisions, follow these steps:

1. Open the properties of the ProDiag function block with a right-click on the ProDiag FB and selecting "Properties ..." in the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. Click the "General &gt; Information" tab.

#### Result

The actual number of maximum possible ProDiag supervisions is shown.

## Defining the ProDiag supervision settings (S7-1500)

This section contains information on the following topics:

- [Overview of the ProDiag supervision settings (S7-1500)](#overview-of-the-prodiag-supervision-settings-s7-1500)
- [Defining general ProDiag supervision settings (S7-1500)](#defining-general-prodiag-supervision-settings-s7-1500)
- [Specifying central ProDiag alarm texts (S7-1500)](#specifying-central-prodiag-alarm-texts-s7-1500)
- [Exporting ProDiag supervision settings (S7-1500)](#exporting-prodiag-supervision-settings-s7-1500)
- [Importing ProDiag supervision settings (S7-1500)](#importing-prodiag-supervision-settings-s7-1500)

### Overview of the ProDiag supervision settings (S7-1500)

#### Description

In order to edit the ProDiag supervision settings, you must have created either a GRAPH function block or a supervision in your program beforehand.

You specify the settings that apply to all supervisions in the entire TIA Portal project in the ProDiag supervision settings. You can add and modify settings.

You can find the ProDiag supervision settings in the project tree under "Common data".

---

**See also**

[Defining general ProDiag supervision settings (S7-1500)](#defining-general-prodiag-supervision-settings-s7-1500)
  
[Specifying central ProDiag alarm texts (S7-1500)](#specifying-central-prodiag-alarm-texts-s7-1500)

### Defining general ProDiag supervision settings (S7-1500)

This section contains information on the following topics:

- [Structure of the ProDiag supervision settings (S7-1500)](#structure-of-the-prodiag-supervision-settings-s7-1500)
- [Categories (S7-1500)](#categories-s7-1500)
- [Subcategories (S7-1500)](#subcategories-s7-1500)
- [Types of supervision (S7-1500)](#types-of-supervision-s7-1500-1)

#### Structure of the ProDiag supervision settings (S7-1500)

##### Structure of the ProDiag supervision settings

The following graphic shows the components of the ProDiag supervision settings as an example:

![Structure of the ProDiag supervision settings](images/102830804363_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | 8 categories can be defined. | You can use categories to divide faults into different priority levels such as errors, warnings, etc.  You can find additional information on the categories here: [Categories](#categories-s7-1500) |
| 2 | 32 subcategories can be defined. | You can use the subcategories to specify the information within a supervision alarm in more detail.  You can find additional information on the subcategories here: [Subcategories](#subcategories-s7-1500) |
| 3 | There are 10 supervision types. | For each supervision type, you can either use the pre-specified name or define your own.  You can find additional information on the supervision types here: [Types of supervision](#types-of-supervision-s7-1500-1) |
| 4 | A central time stamp for all ProDiag function blocks in the project. | The time stamp tag is centrally assigned in the supervision settings for the entire project and can be used by every CPU in the project.  You can find additional information on the central time stamp here: [Using a central time stamp](#using-a-central-time-stamp-s7-1500-1) |

#### Categories (S7-1500)

This section contains information on the following topics:

- [Overview of the categories (S7-1500)](#overview-of-the-categories-s7-1500)
- [Defining categories (S7-1500)](#defining-categories-s7-1500)
- [Displaying translations of the category names (S7-1500)](#displaying-translations-of-the-category-names-s7-1500)

##### Overview of the categories (S7-1500)

###### Description

You can use categories to divide faults into different priority levels. You can assign an alarm class to each category.

The categories can either be displayed as a component of a supervision alarm or they can be displayed on the HMI device as group error bit in the "ProDiag overview" object.

The figure below shows the "Categories" section in the ProDiag supervision settings editor with preset values:

![Description](images/83962724235_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> More information is available here in the information system of the TIA Portal: "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

###### Alarm class

If you assign categories different alarm classes, you can create different areas in the alarm display on your HMI device based on the defined alarm classes.

If you additionally assign the alarm classes different priorities, you can use this to control the sequence of supervision alarms in the "Alarm view" object. For each alarm class, you can also specify whether the supervision alarm is output with or without requiring acknowledgement.

---

**See also**

[Creating alarm classes (S7-300, S7-400, S7-1500)](Configuring%20alarms.md#creating-alarm-classes-s7-300-s7-400-s7-1500)

##### Defining categories (S7-1500)

You can change the settings of a category ("Category", "Activation" or "Alarm class") at any time, even if this category has already been assigned to a supervision. The changes are applied automatically to the supervision.

###### Requirement

You have opened the "Common data" folder in the project tree.

###### Procedure

To create a category, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. On the "General" tab, select the "Categories" section.

   The three categories "Error", "Warning" and "Info" are already available by default. In addition, there are five other placeholder categories. You can change and translate the names of the categories. You can find additional information on translating the names here: [Displaying translations of the category names](#displaying-translations-of-the-category-names-s7-1500)
3. Activate or deactivate the category in the "Activation" column.
4. In the "Alarm class" column, the system's own alarm class is set to "No acknowledgment" by default. Besides the system's own alarm class "No acknowledgment" (= Does not require acknowledgement), the "Acknowledgment" (= Requires acknowledgement) alarm class or self-defined alarm classes are available. Change the default settings, if necessary.

   The "Acknowledgement" and "Priority" columns cannot be edited because these alarm class settings can only be changed in the alarm class editor. You can find additional information on creating alarm classes here: [Creating alarm classes](Configuring%20alarms.md#creating-alarm-classes-s7-300-s7-400-s7-1500)
5. Save the project.

**Note**

**"Error" category**

The pre-selected "Error" category cannot be deactivated. It remains activated at all times.

**Note**

**"Acknowledgment" alarm class**

If you select the "Acknowledgment" alarm class, a supervision alarm requiring acknowledgement appears on your HMI device. This acknowledgement has no effect on the progress of your program. If you want to influence the progress of your program after a fault has occurred, you must use the acknowledgement for a category with the acknowledge tag. You can set this acknowledgment in the block properties of the ProDiag function block.

##### Displaying translations of the category names (S7-1500)

You can display the names of all categories in all project languages that have been activated in the setting options for the project languages and for which translations already exist. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

###### Requirement

You have opened the "Common data" folder in the project tree.

###### Procedure

To display the name of a category in all project languages, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. On the "General" tab, select the "Categories" section.
3. Select the line with the category whose translations you want to display.

   If you want to display the translations of multiple categories simultaneously, select the corresponding lines.
4. Open the "Properties" tab in the Inspector window.

   If the names of the categories appear only in the current user interface language, either you have not yet selected any project languages or translations are not yet available. You can enter the translations directly in the table on the "Texts" tab or you can enter the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts".

You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

###### Result

You see the selected lines in the desired project languages and, if available, the translations of the category names on the lower-level "Texts" tab.

![Result](images/84731235851_DV_resource.Stream@PNG-en-US.png)

#### Subcategories (S7-1500)

This section contains information on the following topics:

- [Overview of the subcategories (S7-1500)](#overview-of-the-subcategories-s7-1500)
- [Defining subcategories (S7-1500)](#defining-subcategories-s7-1500)
- [Displaying and editing translations of the subcategory names and description texts (S7-1500)](#displaying-and-editing-translations-of-the-subcategory-names-and-description-texts-s7-1500)

##### Overview of the subcategories (S7-1500)

###### Description

In addition to the 16 subcategories of "Subcategory 1", you can also activate 16 subcategories of "Subcategory 2". The categories and subcategories are independent of one another and can be freely combined with one another within a supervision.

With the help of subcategories, you have the option of specifying the information within a supervision alarm in more detail. For example, if you have already created the "Error", "Warning" and "Information" categories, you can expand these with subcategories "Technical" or "Organizational". In this way, you receive detailed information on a fault that has occurred.

The subcategories can either be displayed as a component of a supervision alarm or they can be displayed on the HMI device as group error bit in the "ProDiag overview" object.

The figure below shows the "Subcategories 1" section in the ProDiag supervision settings:

![Description](images/101304062987_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Additional information on the HMI object "ProDiag overview"**
>
> More information is available here in the information system of the TIA Portal: "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag &gt; Visualizing supervisions &gt; Configuring the ProDiag overview"

##### Defining subcategories (S7-1500)

You can change the settings of a subcategory ("Subcategory x", "Activation" or "Description") even if this subcategory has already been assigned to a supervision. The changes are applied automatically to the supervision.

###### Requirement

You have opened the "Common data" folder in the project tree.

###### Procedure

To activate a subcategory, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. On the "General" tab, select the "Subcategories 1" or "Subcategories 2" section.
3. Enter the desired subcategory names.

   The names of the subcategories can be translated. You can find additional information on translating the names here: [Displaying and editing translations of the subcategory names and description texts](#displaying-and-editing-translations-of-the-subcategory-names-and-description-texts-s7-1500)
4. Activate or deactivate the desired subcategories in the "Activation" column.
5. Enter a text in the "Description" column, if necessary.

   You can use the "Description" column to forward information to the programmer creating the STEP 7 project. This information is available only within the TIA Portal and is not forwarded to Runtime Professional.

   In addition to the names of the subcategories, you also see the description texts in the lower-level "Texts" tab of the "Properties" Inspector window.
6. Save the project.

###### Result

A new subcategory 1 is created, which you can combine with a category when creating a supervision.

![Result](images/101305863563_DV_resource.Stream@PNG-en-US.png)

##### Displaying and editing translations of the subcategory names and description texts (S7-1500)

You can display the names of all categories in all project languages that have been activated in the setting options for the project languages and for which translations already exist. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

###### Requirement

You have opened the "Common data" folder in the project tree.

###### Procedure

To display the name of a subcategory in all project languages, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. On the "General" tab, select the "Subcategories x" section.
3. Select the line with the subcategory whose translations you want to display.

   If you want to display the translations of multiple subcategories simultaneously, select the corresponding lines.
4. Open the "Properties" tab in the Inspector window.

   If the names of the subcategories appear only in the current user interface language, either you have not yet selected any project languages or translations are not yet available. You can enter the translations directly in the table on the "Texts" tab or you can enter the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts".

You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).​

###### Result

You see the selected lines in the desired project languages and, if available, the translations of the subcategory names and their description texts in the lower-level "Texts" tab.

![Result](images/84387240075_DV_resource.Stream@PNG-en-US.png)

#### Types of supervision (S7-1500)

This section contains information on the following topics:

- [Overview of the types of supervision (S7-1500)](#overview-of-the-types-of-supervision-s7-1500-1)
- [Displaying translations of the type of supervision names (S7-1500)](#displaying-translations-of-the-type-of-supervision-names-s7-1500)

##### Overview of the types of supervision (S7-1500)

###### Description

There are ten types of supervision with preset names. The names are write-protected and the translations are made available in the selected user interface languages by the system. In addition, you can define your own display name of the type of supervision in the alarm text for each type of supervision and translate it into all user interface languages. You can define default settings for each type of supervision within your project and thereby define the signal state for which an operand or condition is to be supervised. The defaults apply to newly created supervisions or if you change the type of supervision. In addition, you can preset a delay time for each type of supervision.

The figure below shows the "Types of supervision" section in the ProDiag supervision settings editor with preset values:

![Description](images/84732888075_DV_resource.Stream@PNG-en-US.png)

###### Activation

When you create a GRAPH function block or a supervision, all options, except for the GRAPH settings, are automatically activated by the operating system by default. You can change the default settings for the triggers and the delay time at any time by activating or deactivating the relevant columns. If you select the check box, the state of the operand is supervised for the TRUE signal state. If you clear the check box, the operand status is supervised for the FALSE signal state.

##### Displaying translations of the type of supervision names (S7-1500)

You can display the names of all types of supervision in all project languages that have been activated in the setting options for the project languages and for which translations already exist. You can find additional information on activating project languages under "Editing project data &gt; Working with multi-language projects &gt; Select project languages".

###### Requirement

You have opened the "Common data" folder in the project tree.

###### Procedure

To display the name of a type of supervision in all project languages, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. In the "General" tab, select the "Types of supervision" section.
3. Select the line with the type of supervision whose translations you want to display.

   If you want to display the translations of multiple types of supervision simultaneously, select the corresponding lines.
4. Open the "Properties" tab in the Inspector window.

   If you have not yet translated the names of the types of supervision in all selected project languages, you will see the texts in the current user interface language by default. If the translations are not yet available, you can enter them directly in the table on the "Texts" tab or you can enter the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts".

You can find additional information on translating texts under "Editing project data &gt; Working with multi-language projects &gt; Project text basics".​

###### Result

You see the desired project languages and, if available, the translations of the type of supervision names in the lower-level "Texts" tab.

![Result](images/85241029643_DV_resource.Stream@PNG-en-US.png)

### Specifying central ProDiag alarm texts (S7-1500)

This section contains information on the following topics:

- [Structure of the alarm text editor (S7-1500)](#structure-of-the-alarm-text-editor-s7-1500)
- [Structure of a GRAPH supervision alarm (S7-1500)](#structure-of-a-graph-supervision-alarm-s7-1500)
- [Structure of a global supervision alarm (tag) (S7-1500)](#structure-of-a-global-supervision-alarm-tag-s7-1500)
- [Structure of a local supervision alarm (parameter) (S7-1500)](#structure-of-a-local-supervision-alarm-parameter-s7-1500)
- [Creating alarm texts (S7-1500)](#creating-alarm-texts-s7-1500)
- [Exporting ProDiag and GRAPH texts (S7-1500)](#exporting-prodiag-and-graph-texts-s7-1500)

#### Structure of the alarm text editor (S7-1500)

##### Structure of the alarm text editor

The following graphic shows an example of the components in the alarm text editor:

![Structure of the alarm text editor](images/111921766539_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | Creating alarm text structures for GRAPH supervisions (only in connection with the GRAPH programming language) | You can find additional information on the GRAPH supervision messages here: [Structure of a GRAPH supervision alarm](#structure-of-a-graph-supervision-alarm-s7-1500) |
| 2 | Creating alarm text structures for the basic supervisions:  - Operand - Interlock - Action - Reaction - Position   You can create a separate alarm text for global supervisions (tag) and local supervisions (function block-parameter) for each basic supervision. | You can find additional information on the global supervision messages here: [Structure of a global supervision alarm (tag)](#structure-of-a-global-supervision-alarm-tag-s7-1500)  You can find additional information on the local supervision messages here: [Structure of a local supervision alarm (parameter)](#structure-of-a-local-supervision-alarm-parameter-s7-1500) |
| 3 | Creating alarm text structures for Supervisions with an error message. You can create a separate alarm text structure for all global supervisions (tags) and local supervisions (FB parameters) for each supervision with an error message. |  |
| 4 | Creating alarm text structures for Supervisions with a text message. You can create a separate alarm text structure for all global supervisions (tags) and local supervisions (FB parameters) for each supervision with a text message. |  |
| 5 | Listing of all the supported alarm text fields that you can drag-and-drop into the individual text frame. |  |
| 6 | Various text frames that you can fill with alarm text fields in order to configure the desired supervision alarms. | You can define up to 11 text frames (alarm text, information text and nine additional alarm texts). The nine additional alarm texts can only be displayed in WinCC Runtime Professional. |
| 7 | Separator for alarm text fields | A colon is used by default to separate the alarm text fields within a text frame. You can change or delete the separator at any time if you do not want to use any separator. The previously used separator, e.g. a colon, is then automatically replaced in all text frames by the new separator, e.g. a semicolon. |

##### Description

A preset text field structure which you can change at any time is provided for the "Alarm text" text frame.

From the "Supported alarm text fields" area, you can drag or copy available alarm text fields into one of the text frames. Each alarm text field can be used only once within a text frame. The alarm text fields that are available depend on the area you clicked on below "Alarm texts" in the tree. You can change the order of the alarm text fields within a text frame using drag-and-drop.

When you use the "&lt;Specific text field&gt;" alarm text box, you can have a specific text displayed for this supervision in the supervision alarm. For the alarm text field to display the requested information, you must configure specific information for this supervision in the settings of the individual supervisions in the lower-level "Specific text field" tab.

---

**See also**

[Creating a specific text field (S7-1500)](#creating-a-specific-text-field-s7-1500)

#### Structure of a GRAPH supervision alarm (S7-1500)

##### Description

This alarm text structure for a GRAPH supervision applies to all three GRAPH types of supervision:

- GRAPH-Interlock
- GRAPH-Supervision
- GRAPH-Warning (step-time supervision)

The table below shows you all components that can be included in a GRAPH supervision. You can, however, reduce the number of components at any time:

| Components of a GRAPH supervision alarm | Description | Specified by default | Translation-related |
| --- | --- | --- | --- |
| &lt;Category&gt; | Name of the category | x | Yes |
| &lt;Subcategory 1&gt; | Name of the subcategory 1 | - |  |
| &lt;Subcategory 2&gt; | Name of the subcategory 2 | - |  |
| &lt;Type of supervision&gt; | Name of the type of supervision | x |  |
| &lt;PLC name&gt; | Name of the PLC | x | No |
| &lt;FB name&gt; | Name of the function block | x |  |
| &lt;FB number&gt; | Number of the function block | - |  |
| &lt;Step name&gt; | Step name | x |  |
| &lt;Step number&gt; | Step number | x |  |
| &lt;Instance DB name&gt; | Name of the instance data block | - |  |
| &lt;Instance DB number&gt; | Number of the instance data block | - |  |
| &lt;Step specific field&gt; | Specific interlock or supervision information that you have defined at each step. | x |  |

You can change the number of supervision alarms at any time by adding new components or removing those already included. All components can be used optionally.

---

**See also**

[Creating alarm texts (S7-1500)](#creating-alarm-texts-s7-1500)
  
[Editing alarms (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#editing-alarms-s7-300-s7-400-s7-1500)
  
[Enabling and disabling the alarm view (S7-300, S7-400, S7-1500)](Creating%20GRAPH%20programs%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#enabling-and-disabling-the-alarm-view-s7-300-s7-400-s7-1500)

#### Structure of a global supervision alarm (tag) (S7-1500)

##### Description

You can create global supervision alarms for supervisions of a tag that was defined in a tag table or in a data block.

The table below shows you all components that can be included in a global supervision alarm. You can, however, reduce the number of components at any time:

| Components of a global supervision alarm | Description | Specified by default | Translation-related |
| --- | --- | --- | --- |
| &lt;Category&gt; | Name of the category | x | Yes |
| &lt;Subcategory 1&gt; | Name of the subcategory 1 | - |  |
| &lt;Subcategory 2&gt; | Name of the subcategory 2 | - | No |
| &lt;Type of supervision&gt; | Name of the type of supervision | x | Yes |
| &lt;PLC name&gt; | Name of the PLC | - | No |
| &lt;ProDiag FB name&gt; | Name of the ProDiag function block | x |  |
| &lt;ProDiag FB number&gt; | Number of the ProDiag function block | - |  |
| &lt;Supervision ID&gt; | ID of the supervision | x |  |
| &lt;Tag address&gt; | - Tag address from the tag table - An address is not output for Boolean elements from a data block. | x |  |
| &lt;Tag name&gt; | Name of the supervised tag  If this is a structure element (PLC data type, ARRAY or STRUCT), all higher-level structure levels are displayed, e.g. "Motors".Motor_1.Element_BOOL | x |  |
| &lt;Tag comment&gt; | - Comment of the tag from the tag table - Comment of the element from the data block | x | Yes |
| &lt;Tag comment path&gt; | Comments of the tags of all levels of a structured tag, separated by dots | - |  |
| &lt;Specific text field&gt; | Specific information for a supervision (text with 3 tags)  - &lt;Associated value SD_5&gt; - &lt;Associated value SD_6&gt; - &lt;Associated value SD_7&gt; | - |  |

You can change the number of supervision alarms at any time by adding new components or removing those already included. All components can be used optionally.

---

**See also**

[Creating alarm texts (S7-1500)](#creating-alarm-texts-s7-1500)

#### Structure of a local supervision alarm (parameter) (S7-1500)

##### Description

You can create local supervision alarms either for parameter supervisions of a parameter that is defined in the block interface of a function block, or for PLC data type supervisions, if the PLC data type is used in the block interface of a function block.

> **Note**
>
> **Structured tags**
>
> Boolean elements of a structured tag (PLC data type, ARRAY or STRUCT) can be supervised in the block interface only in the section "Static".

The table below shows you all components that can be included in a local supervision alarm. You can, however, reduce the number of components at any time:

| Components of a local supervision alarm | Description | Specified by default | Translation-related |
| --- | --- | --- | --- |
| &lt;Category&gt; | Name of the category | x | Yes |
| &lt;Subcategory 1&gt; | Name of the subcategory 1 | - |  |
| &lt;Subcategory 2&gt; | Name of the subcategory 2 | - | No |
| &lt;Type of supervision&gt; | Name of the type of supervision | x | Yes |
| &lt;PLC name&gt; | Name of the CPU | - | No |
| &lt;ProDiag FB name&gt; | Name of the ProDiag function block | x |  |
| &lt;ProDiag FB number&gt; | Number of the ProDiag function block | - |  |
| &lt;Supervision ID&gt; | ID of the supervision | x |  |
| &lt;Type name&gt; | Name of the function block or the PLC data type | - |  |
| &lt;Instance path&gt; | Name and path of the instance data block | - |  |
| &lt;Instance name&gt; | Name of the instance data block (for example Block_9_DB) | x |  |
| &lt;Instance number&gt; | Number of the instance data block | - |  |
| &lt;Instance comment&gt; | - At a single instance:   The title of the instance DB is output. - At a multiple instance:   The comment of the multiple instance from the block interface is output. | - | Yes |
| &lt;Parameter name&gt; | Name of the supervised parameter | x | No |
| &lt;Parameter comment&gt; | Parameter comment | - | Yes |
| &lt;Tag address&gt; | - Tag address from the tag table - An address is not output for Boolean elements from a data block. | x | No |
| &lt;Tag name&gt; | In this case, the parameter (&lt;Parameter name&gt;) is supervised and the tag (&lt;Tag name&gt;) is the preceding tag, if one exists. | x |  |
| &lt;Tag comment&gt; | - Comment of the tag from the tag table - Comment of the element from the data block | x | Yes |
| &lt;Tag comment path&gt; | Comments of the tags of all levels of a structured tag, separated by dots | - |  |
| &lt;Specific text field&gt; | Specific information for a supervision (text with 3 tags)  - &lt;Associated value SD_5&gt; - &lt;Associated value SD_6&gt; - &lt;Associated value SD_7&gt; | - |  |

You can change the number of supervision alarms at any time by adding new components or removing those already included. All components can be used optionally.

---

**See also**

[Creating alarm texts (S7-1500)](#creating-alarm-texts-s7-1500)

#### Creating alarm texts (S7-1500)

##### Requirement

You have opened the "Common data" folder in the project tree.

##### Procedure

To create an alarm text, follow these steps:

1. Double-click the "Supervision settings" entry in the project tree.

   The ProDiag supervision settings are opened.
2. In the "Alarm texts" tab, select the area for which you want to create an alarm text, e.g. Basic supervisions &gt; Tags.
3. Use drag-and-drop to move the desired alarm text fields from the "Supported alarm text fields" field to the "Alarm text" text frame.

   You can change the order of the individual text fields at any time.
4. If you want to delete a text field again, right-click the corresponding text field and select "Delete" from the shortcut menu.
5. Select the desired delimiter for the text fields.

##### Result

The text fields serve as placeholders and are filled with current process values as soon as a supervision alarm is triggered.

#### Exporting ProDiag and GRAPH texts (S7-1500)

##### Description

You can filter project texts from ProDiag and GRAPH and export them for translation. The texts are exported to an Office Open XML file with the extension ".xlsx". This can be edited in Microsoft Excel or a number of other spreadsheet programs.

You define the export of ProDiag and GRAPH texts using the following filter options:

| Option | Contents of the export |
| --- | --- |
| ProDiag / GRAPH: Alarm texts | - User-defined text lists for supervisions - Display names for the steps and transitions in GRAPH - Comments and comment paths of the supervised tags and PLC data type elements in tag tables, global DBs and array DBs. - Comments of the supervised elements in the block interface - Title of the supervised instance data blocks and instance comments in the case of a multi-instance or a supervised PLC data type. - Comments and comment paths of the tags that are series-connected with supervised elements of the block interface (if only one operand is series-connected) - Comments of an instance of a supervised PLC data type that is used in "Static" section of a function block (in the case of a multi-instance). - Step-specific interlock and supervision alarm texts for GRAPH |
| ProDiag / GRAPH: Texts for HMI display | - Tag comments in transition and interlock networks - Tag comments in permanent networks supervised with ProDiag - Tag comments in networks supervised with ProDiag - Titles of networks supervised with ProDiag (including permanent networks) |
| ProDiag / GRAPH: All texts | - ProDiag / GRAPH alarm texts - ProDiag / GRAPH texts for HMI display |

> **Note**
>
> These filter options are not available for CPU S7-300/400.​

Additional information is available here: [Exporting project texts](Editing%20project%20data.md#exporting-project-texts)

##### Procedure

To export the project texts for ProDiag and GRAPH, follow these steps:

1. Right-click the CPU in the project tree.
2. Select the "Properties" command from the shortcut menu.
3. Click the "Text" tab.
4. Select one of the required filters.

##### Result

Only the desired project texts are exported.

### Exporting ProDiag supervision settings (S7-1500)

You can export the entire ProDiag supervision settings to a .dat file and import them into a new project.

#### Requirement

You have defined the ProDiag supervision settings for a project.

#### Procedure

To export the ProDiag Monitor settings, follow these steps:

1. Open the "Common data" folder in the project navigation.
2. Double-click the "Supervision settings" entry.
3. Click "Export supervision settings". If the option is not selected, you have not yet created a ProDiag supervision or a GRAPH function block.

   The "Save as" dialog opens.
4. Select a storage location and assign a file name.
5. Click "Save".

#### Result

A .dat file is created at the selected memory location. This file cannot be edited.

### Importing ProDiag supervision settings (S7-1500)

#### Requirement

You have exported the ProDiag supervision settings of a project to a .dat file.

You can import the ProDiag supervision settings into your project even if you have not yet created a ProDiag supervision function or a GRAPH function block.

> **Note**
>
> **Upgrading project**
>
> If you have upgraded your project to TIA Portal version 15 and the "Repair" button is visible in the subcategories area of the ProDiag supervision settings, you must first press this button before you can import the ProDiag supervision settings from another project.

#### Procedure

To import the ProDiag supervision settings into a new project, follow these steps:

1. Open the "Supervision settings" in the "Common data" folder of the project tree.
2. Click "Import supervision settings".

   If "Import supervision settings" is grayed out and the "Repair" button is visible in the subcategories area, you must first press this button. This repairs the subcategories. You can then import the remaining ProDiag supervision settings.
3. The "Open" dialog opens.

   Select the path where the file to be imported is stored.
4. Select the required .dat file.
5. Confirm the dialog with "Open".

#### Result

All ProDiag supervision settings entered in the .dat file are transferred to the new project.

> **Note**
>
> **Importing non-existent ProDiag supervision settings**
>
> For example, if you import alarm classes that do not yet exist in the new project, the system displays an error message and the alarm classes defined by default are assigned to the categories.
>
> If you create the alarm classes after the import, you must then assign them manually to the desired categories.

> **Note**
>
> **Importing of FB or PLC data type names**
>
> Although only the "Type name" component is exported when exporting from TIA Portal Version 17, you can still specify the "FB name" component when importing the supervision settings. The two components "FB name" and "Type name" are treated in the same way during import. This ensures compatibility with TIA Portal versions &lt;17.

## Creating and instantiating ProDiag supervisions (S7-1500)

This section contains information on the following topics:

- [Overview of the supervisions (S7-1500)](#overview-of-the-supervisions-s7-1500)
- [Information on the type-instance concept (S7-1500)](#information-on-the-type-instance-concept-s7-1500)
- [Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
- [Copying supervisions (S7-1500)](#copying-supervisions-s7-1500)
- [Creating global supervisions (S7-1500)](#creating-global-supervisions-s7-1500)
- [Creating supervisions at the FB (local) (S7-1500)](#creating-supervisions-at-the-fb-local-s7-1500)
- [Instantiating FB supervisions (S7-1500)](#instantiating-fb-supervisions-s7-1500)
- [Creating supervisions at PLC data types (S7-1500)](#creating-supervisions-at-plc-data-types-s7-1500)
- [Instantiating PLC data type supervisions (S7-1500)](#instantiating-plc-data-type-supervisions-s7-1500)
- [Creating a specific text field (S7-1500)](#creating-a-specific-text-field-s7-1500)
- [Deleting supervisions (S7-1500)](#deleting-supervisions-s7-1500)

### Overview of the supervisions (S7-1500)

#### Description

In addition to global supervisions, you can also create supervisions at the FB and at PLC data types (local supervisions) in a tag table, for example. You can create more than one supervision for each operand.

For each supervision you create, a new entry is created in the "Supervisions" tab of the "Properties" Inspector window. You can define the settings of each individual supervision in the "Supervisions" tab. If you create multiple supervisions for an operand, these are then numbered in ascending order by adding the suffix "ID_&lt;consecutive supervision ID&gt; (assigned ProDiag FB)" (only applies to global and instantiated supervisions).

> **Note**
>
> **Creating supervisions in an F-instance data block**
>
> Only in the block interface of a fail-safe instance data block can you create global ProDiag supervisions for the Boolean parameters.

As soon as you create the first global supervision within your project, the "Default_SupervisionFB" and "Default_SupervisionDB" ProDiag blocks are automatically created in the "Program blocks" folder of the project tree.

You can see at a glance how many ProDiag supervisions are assigned to a ProDiag function block. You can find additional information under: [Displaying the number of supervisions for a ProDiag FB](#displaying-the-number-of-supervisions-for-a-prodiag-fb-s7-1500)

#### Global supervisions

Supervision of a Boolean variable within a tag table, a global data block or an ARRAY data block.

The figure below shows you based on a global data block which data types you can supervise globally:

![Global supervisions](images/139765665931_DV_resource.Stream@PNG-en-US.png)

The symbol ![Global supervisions](images/133597523083_DV_resource.Stream@PNG-de-DE.png) indicates that a global supervision instance has been created directly in the global DB.

The symbol ![Global supervisions](images/85248238347_DV_resource.Stream@PNG-de-DE.png)shows you instantiated type supervisions of PLC data types that were instantiated directly in the global DB.

#### Supervisions of parameters of a function block (local)

In the Input and Output sections, the supervisions can only be created on the first level. Supervisions can be created on all levels in the Static section.

Supervisions of parameters of a function block in the Input, Output and Static sections of the block interface:

![Supervisions of parameters of a function block (local)](images/139765680011_DV_resource.Stream@PNG-en-US.png)

The symbol ![Supervisions of parameters of a function block (local)](images/133901181067_DV_resource.Stream@PNG-de-DE.png) indicates that a type definition for a supervision has been created directly in the block interface of the function block. This is possible at a Boolean parameter (e.g. Input_1) or at a Boolean element of a PLC data type (Static_2.Conv_Actor_Backward).

The symbol ![Supervisions of parameters of a function block (local)](images/133902783243_DV_resource.Stream@PNG-de-DE.png) indicates inherited supervisions of PLC data types and function blocks (multi-instances).

All supervisions contained in the block interface are instantiated in the instance data block when the function block is called.

#### Supervisions at elements of a PLC data type (local)

Supervisions of Boolean variables within a PLC data type:

![Supervisions at elements of a PLC data type (local)](images/139770737291_DV_resource.Stream@PNG-en-US.png)

The symbol ![Supervisions at elements of a PLC data type (local)](images/133901181067_DV_resource.Stream@PNG-de-DE.png) indicates that a type definition for a supervision was created directly at a Boolean element of a PLC data type. Supervisions can be created on all levels in the PLC data types.

The symbol ![Supervisions at elements of a PLC data type (local)](images/133902783243_DV_resource.Stream@PNG-de-DE.png) indicates inherited supervisions of other PLC data types.

All supervisions contained in the PLC data type are instantiated when using the PLC data type in the program code.

#### "Supervisions" tab in the "Properties" Inspector window

In this tab, you can specify the settings for each created supervision of an operand:

| Group | Property | Description |
| --- | --- | --- |
| General | Type of supervision | The following types of supervision are available:  - Operand, e.g. for supervision of static signals - Interlock, e.g. for supervision of control signals - Action, e.g. for supervising whether the start position has been left - Reaction, e.g. for supervising whether the end position has been reached - Position, e.g. for supervising whether the end position has been left without permission - Text message (displays a simple text message) - Error message (displays an error number and the associated text)   Some of the fields in the properties are mandatory fields and must be filled out, depending on which type of supervision you select. You can find out which fields are mandatory here: [Types of supervision](#types-of-supervision-s7-1500) |
| Supervised tag / parameter | Indicates which operand is being supervised. The signal states TRUE and FALSE of the supervised operand indicate the signal state for which the operand is to be monitored. |  |
| Delay time / reaction time / start-up time | A different time is displayed depending on which type of supervision you select:  - Delay time: Operand, Interlock, Position, Text message, Error message - Reaction time Reaction - Start-up time: Action |  |
| Conditions | You can only use Boolean tags and slice access operations of the BIT data type as conditions. The signal states TRUE and FALSE of the individual conditions indicate the signal state for which the operand is to be monitored. |  |
| Error flag (only for global tags) | The error flag is written to the data block with the same name of the ProDiag function block. |  |
| ProDiag FB (for global tags only) | If you do not assign a user-defined ProDiag function block to a supervision, it is automatically assigned to the ProDiag function block "Default_SupervisionFB". This ProDiag function block contains all global supervisions and already instantiated local supervisions which were assigned to this block. However, you can also create your own ProDiag function blocks in order to group supervisions into technological units.  For instructions on how to create ProDiag function blocks, refer to: [Creating ProDiag function blocks](#creating-prodiag-function-blocks-s7-1500) |  |
| Category | All 8 categories are displayed in the "Category" drop-down list. |  |
| Subcategory 1 and 2 | In order to have possible selections in the drop-down lists of the "Subcategory" fields, you must define them in the ProDiag supervision settings.   You can find an example here: [Defining the ProDiag supervision settings](#defining-the-prodiag-supervision-settings-s7-1500) |  |
| Alarm text | The alarm text cannot be edited because it is also defined in the ProDiag supervision settings. |  |
| Specific text field | - | Here you can create a specific text field for each supervision with the help of associated values. You can create the associated values manually using the character @ or using a shortcut menu item.  You can find an example of manual creation here: [Manually creating associated values](#manually-creating-associated-values-s7-1500)  You can find an example of creation with the help of the shortcut menu item here: [Creating accompanying values using the shortcut menu](#creating-accompanying-values-using-the-shortcut-menu-s7-1500) |

---

**See also**

[Display supervision definitions of all called function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-called-function-blocks-and-plc-data-types-s7-1500)
  
[Display supervisions of all global tags (S7-1500)](#display-supervisions-of-all-global-tags-s7-1500)
  
[Creating global supervisions (S7-1500)](#creating-global-supervisions-s7-1500)
  
[Possible uses of supervisions (S7-1500)](#possible-uses-of-supervisions-s7-1500)
  
[Multiple supervision alarms of a ProDiag FB within one cycle time (S7-1500)](#multiple-supervision-alarms-of-a-prodiag-fb-within-one-cycle-time-s7-1500)
  
[Creating supervisions at the FB (local) (S7-1500)](#creating-supervisions-at-the-fb-local-s7-1500)
  
[Creating supervisions at PLC data types (S7-1500)](#creating-supervisions-at-plc-data-types-s7-1500)
  
[Creating a specific text field (S7-1500)](#creating-a-specific-text-field-s7-1500)

### Information on the type-instance concept (S7-1500)

#### Description

The type-instance concept is the basis for all local supervisions (supervisions of PLC data types and function blocks). To activate the created supervisions (type definitions) in the program, they must be instantiated (instances). The type definition functions like a template that can be used and instantiated several times.

The type-instance concept is structured as follows:

![Description](images/135678802059_DV_resource.Stream@PNG-en-US.png)

In the yellow boxed area, you see all instantiation options that are available for the respective type definition.

### Possible uses of supervisions (S7-1500)

#### Description

You can create global supervisions for the following memory areas:

| Memory area/Section of the block interface | Storage location |
| --- | --- |
| Inputs | Tag table |
| Outputs |  |
| Bit memory |  |
| Elements of a data block | Global data block or an ARRAY data block of data type BOOL |

You can create supervisions at the function block for the following memory areas:

| Memory area/Section of the block interface | Storage location |
| --- | --- |
| Input | Block interface |
| Output |  |
| Static |  |

You can use PLC data type with created supervisions in the following memory areas as a data type:

| Memory area/Section of the block interface | Storage location |
| --- | --- |
| Static | Block interface |
| Inputs | Tag table |
| Outputs |  |
| Bit memory |  |
| Elements of a data block | Global data block or an ARRAY data block |

> **Note**
>
> **PLC data types with supervisions in the section "Temp" or "InOut"**
>
> The PLC data types with created supervisions can also be used in the sections "Temp" or "InOut"; however, the supervisions are then not available at this location of use and therefore are not displayed, not inherited and cannot be used in the program.

> **Note**
>
> **Structured tags**
>
> Boolean elements of a structured tag (PLC data type, ARRAY or STRUCT) can be monitored in the block interface of a user block if this has been declared in the "Static" section.

A variety of possible uses of supervisions are available for each type of supervision:

|  | Global supervisions |  |  | Local supervisions |  |  | PLC data types |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Type of supervision | Inputs | Outputs | Bit memory/elements of a data block of data type BOOL | Input | Output | Static | Static |
| Operand | x | x | x | x | x | x | x |
| Interlock | - | x | x | x | - | - | x |
| Action | x | - | x | x | - | - | x |
| Reaction | x | - | x | x | - | - | x |
| Position | x | - | x | x | - | - | x |
| Error message | x | x | x | x | x | x | x |
| Text message | x | x | x | x | x | x | x |
| x: The supervision can be used.  -: The supervision cannot be used. |  |  |  |  |  |  |  |

### Copying supervisions (S7-1500)

#### Description

Instead of creating new supervisions, you can also copy them. You can copy the supervisions within an object, such as a tag table, or from one CPU to another CPU or from one project to another project.

The table below shows all options for when you can copy supervisions:

**Tag table**

| There are partly different behaviors, depending on whether you want to copy the entire tag table or individual tags. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete table | The supervisions are not included in the copy operation because they are stored in the associated ProDiag FB. | - | The supervisions are included in the copy operation or they are created at the new instances. | The assignments are also copied. |
| Copying individual tags within the tag table | The supervisions are not included in the copy operation because they are stored in the associated ProDiag FB. | - | The supervisions are included in the copy operation or they are created at the new instance. | The assignments are not included in the copy operation but must be created manually after copying. |

**Global data block**

| There are partly different behaviors, depending on whether you want to copy the entire data block or individual elements. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete data block | The supervisions are not included in the copy operation because they are stored in the associated ProDiag FB. | - | The supervisions are included in the copy operation or they are created at the new instances. | The assignments are also copied. |
| Copy individual elements within the data block | The supervisions are not included in the copy operation because they are stored in the associated ProDiag FB. | - | The supervisions are included in the copy operation or they are created at the new instance. | The assignments are not included in the copy operation but must be created manually after copying. |

**User-defined function block**

| There are partly different behaviors, depending on whether you want to copy the entire function block or individual parameters. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete function block | - | The supervisions at the parameters of the function block (locally and inherited from a PLC data type) are included in the copy operation because this is a type definition. | - | - |
| Copy individual parameters within the function block | - | The supervisions at the parameter of the function block are not included in the copy operation.  The inherited supervisions of a PLC data type at the function block parameter are included in the copy operation because this is a type definition. | - | - |

**PLC data type**

| There are partly different behaviors, depending on whether you want to copy the entire PLC data type or individual elements. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete PLC data type | - | The supervisions at the parameters of the function block (locally and inherited from a PLC data type) are included in the copy operation because this is a type definition. | - | - |
| Copy individual elements within the PLC data type | - | The supervisions at the element of the PLC data type are not included in the copy operation.  The inherited supervisions of a PLC data type at the element of the PLC data type are included in the copy operation because this is a type definition. | - | - |

**ProDiag function block**

| There are partly different behaviors, depending on whether you want to copy the entire ProDiag function block or individual elements. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete ProDiag function block | The supervisions are also copied. | - | The supervision instances are not copied. | - |
| Copy individual elements within a ProDiag function block | The supervisions are also copied. | - | Individual instances cannot be copied. | - |

**Data block of "**
**PLC data type**
**" type**

| There are partly different behaviors, depending on whether you want to copy the entire data block or individual elements. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete data block | The global supervisions are not copied. | - | The supervision instances are also copied. | The assignments are also copied. |
| Copy individual elements within a data block | Individual global supervisions cannot be copied. | - | Individual instances cannot be copied. | - |

**Instance data block of the "User-defined function block" type**

| There are partly different behaviors, depending on whether you want to copy the entire data block or individual elements. | Global supervisions | Supervisions at type definitions of PLC data types or function blocks | Supervisions at type instances of a PLC data type or function block | Assignments to ProDiag function blocks |
| --- | --- | --- | --- | --- |
| Copy complete data block | - | - | - | - |
| Copy individual elements within a data block | - | Individual global supervisions cannot be copied. | Individual instances cannot be copied. | - |

> **Note**
>
> **Copy data type "PLC data type" and PLC data type instances**
>
> When you copy a PLC data type definition from one CPU to another CPU or from one project to another project, the supervisions are included in the copy operation.
>
> When you copy a PLC data type instance from one CPU to another CPU or from one project to another project, the ProDiag FB assignment is not included in the copy operation. You must manually assign a new ProDiag FB to the instance.

### Creating global supervisions (S7-1500)

#### Requirement

You have created at least one Boolean tag in a tag table, for example:

![Requirement](images/83883403147_DV_resource.Stream@PNG-en-US.png)

#### Procedure for creating global supervisions

Proceed as follows to create global supervision:

1. Select one or more tags with the right mouse button and select "Add new supervision" from the shortcut menu. The shortcut menu entry is only available when all selected tags (Boolean tags) can be supervised.

   The "Supervisions" tab opens in the "Properties" Inspector window and a supervision for the tag is created. The supervisions are numbered in ascending order (Supervision_&lt;consecutive supervision ID&gt;(assigned ProDiag FB)):

   ![Procedure for creating global supervisions](images/139773775755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for creating global supervisions](images/139773775755_DV_resource.Stream@PNG-en-US.png)
2. The "Operand" type of supervision is selected by default. Select a different type of supervision, if necessary.

   The type of supervision you have selected determines which settings must be filled out.

   You can find additional information on the types of supervision here: [Types of supervision](#types-of-supervision-s7-1500)
3. Set a delay time, if applicable.
4. Select conditions under which a supervision alarm is to be triggered, if necessary.
5. Select a category and, if necessary, subcategories.
6. If you do not wish to use the default ProDiag FB "Default_SupervisionFB", you can either select an existing ProDiag FB or create a new ProDiag FB.

**Note**

**Settings are overwritten**

If you change the type of supervision of a previously created supervision, your settings will be overwritten by the preset values of the new type of supervision.

Or:

1. Click the desired tag.
2. Double-click the entry "Add new supervision" in the "Supervisions" in the "Properties" Inspector window.

   A new supervision is created. The supervisions are numbered in ascending order (Supervision_ID_&lt;consecutive supervision ID&gt;(assigned ProDiag FB)).
3. From this point, the procedure described above from item 2 applies.

#### Result

The supervised tags are marked with the ![Result](images/133597523083_DV_resource.Stream@PNG-de-DE.png) icon:

![Result](images/139775094795_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Copying tags**
>
> If you copy a global tag for which you have already created supervisions from one CPU to another CPU or from one project to another project, the supervisions are not included in the copy operation.

### Creating supervisions at the FB (local) (S7-1500)

#### Requirement

You have created at least one parameter with the following data types in the block interface of a function block in one of the three sections (Input, Output or Static):

- Parameters of the Bool data type
- Parameters with a multi-instance that contain Boolean elements
- Parameters of the PLC data type that contain Boolean elements

![Requirement](images/139778621835_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **ProDiag function blocks**
>
> ProDiag function blocks cannot be used in the block interface.

> **Note**
>
> **Structured tags**
>
> In the "Static" section, Boolean elements of a structured tag of the data type ARRAY, STRUCT or PLC data type can be monitored in the block interface. The elements may be defined on all levels.

> **Note**
>
> **Properties of a local supervision**
>
> All properties of a local supervision (tags for the conditions, delay time or the specific text field) must also be declared locally in the block interface.

#### Procedure for creating supervisions at the FB

To create a supervision in the block interface of a function block, follow these steps:

1. Right-click the parameter and select "Add new supervision" from the shortcut menu.

   The "Supervisions" tab opens in the "Properties" Inspector window and a supervision for the parameter is created. The supervisions are numbered in ascending order (Supervision_&lt;consecutive supervision ID&gt;).
2. The "Operand" type of supervision is selected by default. Select a different type of supervision, if necessary.

   The type of supervision you have selected determines which settings must be filled out.

   You can find additional information on the types of supervision here: [Types of supervision](#types-of-supervision-s7-1500)
3. Set a delay time, if applicable.
4. Select conditions under which a supervision alarm is to be triggered, if necessary.
5. Select a category and, if necessary, subcategories.

**Note**

**Settings are overwritten**

If you change the type of supervision of a previously created supervision, your settings will be overwritten by the preset values of the new type of supervision.

Or:

1. Click the desired parameter.
2. Double-click the entry "Add new supervision" in the "Supervisions" in the "Properties" Inspector window.

   A new supervision is created. The supervisions are numbered in ascending order (Supervision_&lt;consecutive supervision ID&gt;).
3. From this point, the procedure described above from item 2 applies.

#### Result

The supervised parameters are marked with the symbols ![Result](images/133901181067_DV_resource.Stream@PNG-de-DE.png) and ![Result](images/133902783243_DV_resource.Stream@PNG-de-DE.png):

![Result](images/139765680011_DV_resource.Stream@PNG-en-US.png)

The symbol![Result](images/133901181067_DV_resource.Stream@PNG-de-DE.png) indicates that a type definition for a supervision has been created directly in the block interface of the function block. This is possible at a Boolean parameter (e.g. Input_1) or at a Boolean element of a PLC data type (Static_2.Conv_Actor_Backward).

The symbol![Result](images/133902783243_DV_resource.Stream@PNG-de-DE.png) indicates inherited supervisions of PLC data types and function blocks (multi-instances).

> **Note**
>
> **Code Viewer**
>
> When supervising input parameters of a function block, you can display the series connection of the input parameters in the Code Viewer.
>
> When supervising the output and/or static parameters of a function block, you can display the complete call of the function block in the Code Viewer.

#### Displaying supervisions of the function block

When you right-click the function block in the project tree, the properties dialog of the function block is displayed. You can see all supervisions you have created for this function block in the "FB supervision definitions" tab.

You can find additional information on the overview of the supervisions in a function block here: [Displaying supervision definitions of a function block](#displaying-supervision-definitions-of-a-function-block-s7-1500)

### Instantiating FB supervisions (S7-1500)

#### Procedure for instantiating supervisions at the function block

To instantiate the function block and the supervisions contained therein and to activate them, follow, for example, these steps:

1. Use the supervised parameter in the program code.
2. Call the function block in the program.
3. Select an instance data block and a ProDiag FB in the "Call options" dialog in the "Single instance" area.

   The supervisions in your project are only instantiated after this. Inherited supervisions are also instantiated.

### Creating supervisions at PLC data types (S7-1500)

#### Requirement

You have created at least one Boolean tag in a PLC data type:

![Requirement](images/139834427659_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Creating supervisions at existing PLC data types**
>
> When you create supervisions at an existing PLC data type that has already been instantiated, these supervisions are automatically instantiated. The default ProDiag FB "Default_SupervisionFB" is assigned when there is no other ProDiag FB.

> **Note**
>
> **No ProDiag supervisions are available**
>
> If you see this alarm in the inspector window, then you have used the supervised PLC data type in one of the following places in your program:
>
> - You have used the supervised PLC data type in an OB.
> - You have used the supervised PLC data type in an FC.
> - You have used the supervised PLC data type in an FB outside of the "Static" section in the block interface.
>
> You can use the PLC data type at these points, but the ProDiag supervisions contained there are not supported.

#### Procedure for creating supervisions at an element of a PLC data type

To create a supervision at an element of a PLC data type, follow these steps:

1. Select one or more tags and right-click the selected tags.
2. Select "Add new supervision" from the shortcut menu. The shortcut menu entry is only available when all selected tags (Boolean tags) can be supervised.

   The "Supervisions" tab opens in the "Properties" Inspector window and a supervision for the tag is created. The supervisions are numbered in ascending order (Supervision_&lt;consecutive supervision ID&gt;).
3. The "Operand" type of supervision is selected by default.

   The type of supervision you have selected determines which settings must be filled out.

   You can find additional information on the types of supervision here: [Types of supervision](#types-of-supervision-s7-1500)
4. Set a delay time, if applicable.
5. Select conditions under which a supervision alarm is to be triggered, if necessary.
6. Select a category and, if necessary, subcategories.

**Note**

**Possible supervision types**

Only the "Operand" supervision type is available for supervising PLC data types.

**Note**

**Settings are overwritten**

If you change the type of supervision of a previously created supervision, your settings will be overwritten by the preset values of the new type of supervision.

Or:

1. Click the desired tag.
2. Double-click the entry "Add new supervision" in the "Supervisions" in the "Properties" Inspector window.

   A new supervision is created. The supervisions are numbered in ascending order (Supervision_&lt;consecutive supervision ID&gt;).
3. From this point, the procedure described above from item 2 applies.

The supervision is displayed in the "Supervisions" tab in the "Properties" Inspector window. PLC_data_type_supervision_&lt;continuous supervision ID&gt; [lower-level PLC data type].

> **Note**
>
> **Use of the PLC data type in a global data block or in a tag table**
>
> If you use the PLC data type as a tag declaration in a global data block or a tag table, then the supervisions are directly instantiated. The supervisions are marked with this symbol: ![Procedure for creating supervisions at an element of a PLC data type](images/85248238347_DV_resource.Stream@PNG-de-DE.png)

#### Result

The supervised elements are marked with the symbols![Result](images/133901181067_DV_resource.Stream@PNG-de-DE.png) and![Result](images/133902783243_DV_resource.Stream@PNG-de-DE.png):

![Result](images/139770737291_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating PLC data types](Declaring%20PLC%20data%20types%20%28UDT%29.md#creating-plc-data-types)

### Instantiating PLC data type supervisions (S7-1500)

#### Procedure for instantiating supervisions at PLC data types

If you use the PLC data type, for example, in a tag table, the supervisions are immediately instantiated.

If you use the PLC data type in the block interface of a function block, then all supervisions are automatically instantiated when the block is called.

> **Note**
>
> **Changing the data type**
>
> - When you change the data type from one PLC data type, such as UDT_1, to another PLC data type, such as UDT_2, the supervision instances are updated and the ProDiag FB assignments are retained.
> - When you change the data type from a PLC data type, such as UDT_1, to another data type, such as INT, the supervisions and ProDiag FB assignments are deleted.

### Creating a specific text field (S7-1500)

This section contains information on the following topics:

- [Overview of the specific text box (S7-1500)](#overview-of-the-specific-text-box-s7-1500)
- [Manually creating associated values (S7-1500)](#manually-creating-associated-values-s7-1500)
- [Structure of the associated values](#structure-of-the-associated-values)
- [Creating accompanying values using the shortcut menu (S7-1500)](#creating-accompanying-values-using-the-shortcut-menu-s7-1500)
- [Examples of associated values (S7-1500)](#examples-of-associated-values-s7-1500)
- [Displaying and editing translations of the specific text field (S7-1500)](#displaying-and-editing-translations-of-the-specific-text-field-s7-1500)

#### Overview of the specific text box (S7-1500)

##### Description

With the help of specific text fields, you can display additional information for each supervision in a supervision alarm with the help of associated values. This information can be combined freely in the specific text field and consists of the following elements:

- Free text (for example, temperature, manual mode, automatic mode)
- Value of the three different tags (associated values SD_4 to SD_6) that are read out during runtime
- Text list name
- Text list ID

---

**See also**

[Examples of associated values (S7-1500)](#examples-of-associated-values-s7-1500)

#### Manually creating associated values (S7-1500)

> **Note**
>
> **Use the @ character in the specific text field**
>
> Please use the @ character only for declaring the associated values, for example @4%6d@. Also, if you use the @ character in the text-specific text field, you may not be able to resolve the associated values contained in the free text of the supervision alarm.

##### Requirement

You have created either a global or a local supervision and opened the "Supervisions" tab in the "Properties" Inspector window is open.

##### Procedure

To create the specific text field for a supervision, follow these steps:

1. Select the "Specific text field" group.
2. Select the required tags from the autocomplete of the three associated values SD_4 to SD_6.

   The tags must be of the data type BOOL, BYTE, WORD, DWORD, SINT, INT, DINT, USINT, UINT, UDINT, REAL, LREAL, CHAR, WCHAR, STRING or WSTRING.
3. Enter the desired text in the text field. It can, for example, consist of a free text and a reference to the tags which you have defined as associated values. (for example, @4 references to the tag of the associated value SD_4)

   For information on what the syntax of the reference to a tag must look like, refer to: [Structure of the associated values](#structure-of-the-associated-values)

> **Note**
>
> **Display of the specific text field**
>
> This information is only output in the supervision alarm when you have used the text field "&lt;Specific text field&gt;" when configuring the alarm texts in the ProDiag supervision settings. You can find additional information on the alarm texts in the ProDiag supervision settings here: [Specifying central ProDiag alarm texts](#specifying-central-prodiag-alarm-texts-s7-1500)

##### Result

When a supervision alarm is triggered by a fault/error, the information from the specific text field is displayed if you have used the alarm text field "&lt;Specific text field&gt;" in the alarm text structure.

![Result](images/87459313803_DV_resource.Stream@PNG-en-US.png)

#### Structure of the associated values

The associated values SD_4, SD_5 and SD_6 can be referenced as follows:

@&lt;Number of the associated value&gt;&lt;Format&gt;&lt;Text library (name or number&gt;@

The character "@" initiates the use of an associated value and also closes it.

##### Number of the associated value

The number specifies which associated value or which tag is to be read:

| Number | Explanation |
| --- | --- |
| 4 | Associated value SD_4 (tag 1) |
| 5 | Associated value SD_5 (tag 2) |
| 6 | Associated value SD_6 (tag 3) |

##### Maximum permitted size of the associated values

The reason for the total size of the associated values to exceed the maximum permitted size is usually that one or more of the associated values are of the data type STRING or WSTRING and an actual length was not specified. If no actual length is specified for WSTRING, for example, the maximum permitted length is used, and the maximum permitted size is already exceeded with one associated value.

Always use brackets [] for the data types STRING and WSTRING to define the actual length.

##### Format

Determine the output format for the associated value on the display device. The format is preceded by the "%" sign. The following fixed formats apply to associated values:

| Format | Description |
| --- | --- |
| %[i]X | Hexadecimal number with i digits |
| %[i]u | Decimal number without sign with i digits |
| %[i]d | Decimal number with sign with i digits |
| %[i]b | Binary number with i digits |
| %[i][.y]f | Floating-point number with sign with y digits after the decimal point and total number of digits i |
| %[i]s | String (ANSI string) with i digits  Characters are printed up to the first 0 Byte (00Hex). |
| %t#&lt;Name of text library&gt; | Access to text library |
| %t#&lt;Associated value that references the number of the text library&gt; | Access to text library |

If the number of digits [i] is too small, the value is nevertheless output in full.

If the number of digits [i] is too large, an appropriate number of fill characters is output before the value.

If the number of digits [i] is too large and if a sign is output (for decimal/floating-point numbers), the number of fill characters is reduced by one. The same applies to periods or commas within floating-point numbers.

> **Note**
>
> Please note that you can optionally enter "[i]" (without the square brackets).

##### Examples

The table below shows some examples:

| Tag value | Associated value | Explanation | Output |
| --- | --- | --- | --- |
| 123* | @4%6d@ | The value of associated value SD_4 is shown as a decimal number with sign and a total number of 6 digits. | 000123 |
| 1234.567 | @4%8.3f@ | The value of associated value SD_4 is shown as a floating-point number with sign with 3 digits after the decimal point and a total number of 8 digits.   A fill character is not added because the decimal point represents the eighth character. | 1234.567 |
| 5.4* | @5%6f@ | The value of associated value SD_5 is shown as an integer with a total number of 6 digits.  The number of places after the decimal point has not been defined. | 0005.4 |
| 5.4 | @5%2f@ | The value of associated value SD_5 is shown as an integer with a total number of 3 digits.  The value is not shortened. | 5.4 |
| Contents of the text library &lt;TextLib1&gt; | @6%t#TextLib1@ | The associated value SD_6 of the data type WORD is the index which references the text library used "TextLib1". | 90° |
| Content of the text library that is reference during runtime using the associated value SD_5 | @4%t#5@ | The associated value SD_4 of the data type WORD is the index. The associated value SD_5 references the text list number. | The text list entry is read out during runtime and displayed in the alarm text:  - the tag of the associated value SD_4 points to the desired text list entry  - the tag of the associated value SD_5 specifies the desired text list number |

> **Note**
>
> **Firmware version of the CPU**
>
> For use of the text list number via associated value, we recommend using an S7-1500 CPU with firmware version 2.9 or higher.

The type of the fill character (for example, zeros or blanks) depends on the output system.

#### Creating accompanying values using the shortcut menu (S7-1500)

##### Description

In addition to manual notation with the syntax @&lt;number of the accompanying value&gt;%&lt;Format&gt;@ you also have the option to create the accompanying values using the shortcut menu.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Requirements in the CPU**  The tags are only resolved for CPUs with a firmware version 2.9 or higher if the "Central alarm management in the PLC" setting is enabled. |  |

##### Entering a tag as an associated value

In the selection box "Tag", select the desired tag (tag 1 SD_4, tag 2 SD_5, or tag 3 SD_6). In the "Format" section, you must now define the display type suitable for the specified tag, the minimum length, and, if applicable, the number of decimal places.

##### Entering a text list name as an associated value

You select the desired text list in the drop-down list. In the "Tag for text list entry" selection box, select the tag which includes the index for the text list during program runtime.

##### Entering a text list ID as an associated value

In the "Tag for text list ID" selection box, select the desired tag for the text list ID from the drop-down list. In the "Tag for text list entry" selection box, select the tag which includes the index for the text list during program runtime.

##### Procedure

To insert an associated value into an alarm, follow these steps:

1. Open the shortcut menu at the desired position in the specific text box, and use the corresponding command to select whether you want to insert a tag, a text list name or a text list number.
2. Enter the desired parameters in the dialog that appears, and confirm your entries.

##### Result

The associated value is integrated into the supervision alarm.

If there is a syntax error, the text is displayed with a red background and must be corrected. Not every combination of tag and formatting is possible.

#### Examples of associated values (S7-1500)

##### Examples of associated values that can be entered in the shortcut menu:

**Tag:**

&lt;Tag: #Temperature&gt;

The value of the "#Temperature" tag is displayed at this point in the alarm text.

**Text list name:**

&lt;Text list: USER_1: "tag_1"&gt;

The content of the "tag_1" tag is used as index for the "USER_1" text list. The entry from the text list is displayed at this point in the alarm text.

**Text list ID:**

&lt;Text list: "Tag 1(SD_4)": "Tag 2(SD_5)"&gt;

The "Tag 1"(SD_4) tag reads out the text list ID during runtime, and the content of the "Tag 2"(SD_5) tag is used as index for the reference text list. The entry from the text list is displayed at this point in the alarm text.

> **Note**
>
> **Firmware version of the CPU**
>
> For use of the text list ID via shortcut menu item, we recommend using a CPU S7-1500 with firmware version 2.9 or higher.

##### Examples of associated values that can be entered without the shortcut menu:

@4%6d@: The value from associated value 1 (SD_4) is shown as a decimal number with up to six digits.

@5%6f@: The value "5.4", for instance from associated value 2 (SD_5), is shown as the fixed-point number "5.4" (three leading spaces).

@5%2f@: The value "5.4", for instance from associated value 2 (SD_5), is shown as the fixed-point number "5.4" (if number of digits is too small, then these are not cut off).

#### Displaying and editing translations of the specific text field (S7-1500)

You can display the specific text field in all project languages that have been activated in the setting options for the project languages and for which translations already exist. You can find additional information on activating project languages under [Select project languages](Editing%20project%20data.md#select-project-languages).

##### Requirement

You have created a specific text field for at least one ProDiag supervision.

##### Procedure

You have several options for displaying the translations of the specific text field:

- In the ProDiag overview editor
- In the block properties of the ProDiag function block
- In the ProDiag function block

To display the translations in the ProDiag overview editor, follow these steps:

1. Double-click the "PLC supervisions &amp; alarms" entry in the project tree below the CPU.

   The alarm and supervision editor opens.
2. Click either the "Global supervisions" tab or the "Supervision definitions" tab.
3. Select either the entire row of the desired supervision or the cell that contains the text of the specific text field. If you want to display multiple texts in the "Texts" tab, select multiple cells with specific texts.

   The text of the specific text fields is displayed in the Inspector window in the "Texts" tab.

To display the translations in the block properties of the ProDiag function block, follow these steps:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. Click on the "Texts" tab.

   The texts of the specific text fields are displayed.

To display translations in the ProDiag function block, follow these steps:

1. Double-click the ProDiag function block.

   The ProDiag function block opens.
2. In the Inspector window, click on the "Texts" tab.

   The texts of the specific text fields are displayed.

If the names of the categories appear only in the current user interface language, either you have not yet selected any project languages or translations are not yet available. You can enter the translations directly in the table on the "Texts" tab or you can enter the translations for the individual project languages in the global "Project texts" table. You can find the table in the project tree under "Languages &amp; Resources &gt; Project texts".

You can find additional information on translation of texts under [Project text basics](Editing%20project%20data.md#project-text-basics).

### Deleting supervisions (S7-1500)

#### Requirement

You have created at least one supervision.

#### Procedure for deleting all supervisions of an operand

To delete all supervisions, follow these steps:

1. Right-click in the "Supervision" column on the operand.
2. Click "Delete" in the shortcut menu.

#### Procedure for deleting individual supervisions of an operand

To delete a single supervision, follow these steps:

1. Click the tag or the parameter with the supervision to be deleted.

   The "Supervisions" tab opens in the "Properties" Inspector window.
2. Right-click the desired supervision and select "Delete supervision" from the shortcut menu.

#### Result

The supervision has been deleted.

> **Note**
>
> **Monitoring is not deleted.**
>
> If you change the data type of a monitored operand or delete the monitored operand, the monitoring is not automatically deleted at the same time. If you really want to delete the operand including monitoring, then you must delete the monitoring separately.

## Copying ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Overview of copying ProDiag function blocks (S7-1500)](#overview-of-copying-prodiag-function-blocks-s7-1500)
- [Copying ProDiag function block (S7-1500)](#copying-prodiag-function-block-s7-1500)
- [Pasting a ProDiag function block (S7-1500)](#pasting-a-prodiag-function-block-s7-1500)

### Overview of copying ProDiag function blocks (S7-1500)

#### Description

Instead of creating the ProDiag function blocks, you can also copy them. The following options are available for copying:

- You can copy the ProDiag FB within a project from one S7-1500-CPU to another S7-1500-CPU.
- You can copy the ProDiag FB from one project to another.
- You can copy the ProDiag FB from a project to a project library.
- You can copy the ProDiag FB from a project to a global library.
- You can copy the ProDiag FB from a project library to a global library and vice versa.

All global supervisions included in the ProDiag function block are retained during copying. We therefore recommend to also copy the supervised global tags; otherwise you may encounter a compilation error.

The included local supervisions are not copied.

> **Note**
>
> **Guaranteeing consistency of the ProDiag configuration**
>
> A ProDiag function block has to be compiled after copying in order to ensure the consistency of the ProDiag configuration. Any difference is always displayed in an offline comparison after copying.

---

**See also**

[Copying ProDiag function block (S7-1500)](#copying-prodiag-function-block-s7-1500)
  
[Pasting a ProDiag function block (S7-1500)](#pasting-a-prodiag-function-block-s7-1500)

### Copying ProDiag function block (S7-1500)

#### Requirement

You have selected the ProDiag function block.

#### Procedure

To copy the ProDiag function block, follow these steps:

1. Right-click the ProDiag function block.
2. Select the "Copy" command from the shortcut menu.

#### Result

A copy of the ProDiag function block is now on the clipboard and can be pasted to the desired location.

### Pasting a ProDiag function block (S7-1500)

#### Requirement

You have copied a ProDiag function block.

#### Procedure

To paste a copied ProDiag function block and its global supervisions, follow these steps:

1. Open the desired location to which you want to paste the copied block.
2. Right-click and select the "Paste" command from the shortcut menu.

   - If you are pasting the ProDiag function block into the same S7-1500 CPU as the original block, the copy is pasted with the extension "_&lt;consecutive number&gt;".
   - If you are pasting the ProDiag function block into a different S7-1500 CPU where a ProDiag function block of the same name already exists, the "Paste" dialog box opens. Select the required option and confirm with "OK".

#### Result

The copied ProDiag function block has been pasted.

## Assigning ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Overview of the assignment options (S7-1500)](#overview-of-the-assignment-options-s7-1500)
- [Assigning global supervisions to a ProDiag FB (S7-1500)](#assigning-global-supervisions-to-a-prodiag-fb-s7-1500)
- [Assigning supervisions at the FB to a ProDiag function block (S7-1500)](#assigning-supervisions-at-the-fb-to-a-prodiag-function-block-s7-1500)
- [Assigning supervisions of PLC data types to a ProDiag FB (S7-1500)](#assigning-supervisions-of-plc-data-types-to-a-prodiag-fb-s7-1500)
- [Assigning an instance data block to a ProDiag FB (local supervisions) (S7-1500)](#assigning-an-instance-data-block-to-a-prodiag-fb-local-supervisions-s7-1500)
- [Changing the existing assignment of a ProDiag FB (S7-1500)](#changing-the-existing-assignment-of-a-prodiag-fb-s7-1500)
- [Removing the existing assignment of a ProDiag FB (S7-1500)](#removing-the-existing-assignment-of-a-prodiag-fb-s7-1500)

### Overview of the assignment options (S7-1500)

#### Description

Each ProDiag supervision must be assigned to a ProDiag function block so that it is activated in the user program.

The following assignment options are available:

| Location of assignment | Global supervisions | Supervisions of parameters of a function block | Supervisions at elements of a PLC data type |
| --- | --- | --- | --- |
| Tag table | The supervisions are automatically assigned to a ProDiag function block (for example, Default_SupervisionFB). You can change this assignment:  - Inspector window "Properties &gt; Supervisions" | - | The supervisions are automatically assigned to a ProDiag function block (for example, Default_SupervisionFB). You can change this assignment:  - Inspector window "Properties &gt; Supervisions" |
| Global data block | The supervisions are automatically assigned to a ProDiag function block (for example, Default_SupervisionFB). You can change this assignment:  - Inspector window "Properties &gt; Supervisions" | - | 1. For a tag of data type "PLC data type" in the Global DB, the supervisions are assigned automatically to a ProDiag function block (for example Default_SupervisionFB):    - Inspector window "Properties &gt; Supervisions" 2. For a global data block of the type "PLC data type":    - In the "Add new block" dialog 3. For a global data block of the type "ARRAY-DB" with the data type "PLC data type"    - In the "Add new block" dialog |
| ProDiag overview table | You can also change the assignments here:  - ProDiag overview table &gt; "Global supervisions" tab | You can also change the assignments here:  - ProDiag overview table &gt; "Instantiated supervisions" tab | For supervisions that were created directly at the instance, the assignments can also be changed here:  - ProDiag overview table &gt; "Global supervisions" tab   For supervisions that were created at the definition (type) of the PLC data type, the assignments can also be changed here:  - ProDiag overview table &gt; "Instantiated supervisions" tab |
| Call options for FB block call | - | When calling the user-defined function block in the program code, you can specify the assignment directly in the call options for all supervisions of the function block.  You can change the assignment by clicking "...".   **Note:**   When you use PLC data types with created supervisions in a function block, the supervisions are automatically instantiated when the block is called. |  |
| Instance data block of the user-defined function block | - | You can also change the assignments here:  - "Properties &gt; General &gt; Attributes" |  |
|  | You can find additional information here:   [Assigning global supervisions to a ProDiag FB](#assigning-global-supervisions-to-a-prodiag-fb-s7-1500) | You can find additional information here:   [Assigning supervisions at the FB to a ProDiag function block](#assigning-supervisions-at-the-fb-to-a-prodiag-function-block-s7-1500) | You can find additional information here:   [Assigning supervisions of PLC data types to a ProDiag FB](#assigning-supervisions-of-plc-data-types-to-a-prodiag-fb-s7-1500) |

If you do not select a user-defined ProDiag function block, the supervisions are assigned by default either to the ProDiag function block "Default_SupervisionFB" or the first user-defined ProDiag function block found.

You can change the assignment of a supervision to a ProDiag function block at any time later on.

---

**See also**

[Assigning an instance data block to a ProDiag FB (local supervisions) (S7-1500)](#assigning-an-instance-data-block-to-a-prodiag-fb-local-supervisions-s7-1500)
  
[Changing the existing assignment of a ProDiag FB (S7-1500)](#changing-the-existing-assignment-of-a-prodiag-fb-s7-1500)
  
[Removing the existing assignment of a ProDiag FB (S7-1500)](#removing-the-existing-assignment-of-a-prodiag-fb-s7-1500)

### Assigning global supervisions to a ProDiag FB (S7-1500)

#### Requirement

You have created at least one global supervision.

#### Procedure

You have several options to assign global supervisions to a ProDiag function block.

**In a tag table or a global data block, follow these steps:**

1. Click the desired tag.
2. Click the "Supervisions" tab in the "Properties" Inspector window.
3. Click the desired supervision.
4. Click the "…" selection field at ProDiag FB.

   A selection dialog opens.
5. Select the corresponding ProDiag function block.

**In the ProDiag overview table, follow these steps:**

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click on the "Supervisions &gt; Global supervisions" tab.

   All global supervisions are displayed.
3. Click the "..." selection box either in the "ProDiag FB" column of the editor or in the Inspector window "Properties &gt; Supervisions".

   A selection dialog opens.
4. Select the corresponding ProDiag function block.

#### Result

The supervision has been assigned to a ProDiag function block.

---

**See also**

[Creating global supervisions (S7-1500)](#creating-global-supervisions-s7-1500)

### Assigning supervisions at the FB to a ProDiag function block (S7-1500)

#### Description

The supervision instances that you have created at the function block inn the block interface are assigned to a ProDiag function block.

#### Requirement

You have created at least one local supervision at a function block.

#### Procedure

You have several options to assign local supervisions of a function block to a ProDiag function block:

**During the block call, follow these steps:**

1. Call the function block in the program code.

   The "Call options" dialog opens.
2. Click the "Single instance" button.
3. Select the desired ProDiag function block from the selection box "...".
4. Confirm your entries with "OK".

Or:

1. Call the function block in the program code.

   The "Call options" dialog opens.
2. Click the "Multi instance" button.
3. Select the desired multi-instance.
4. Confirm your entries with "OK".
5. Call the function block that contains the multi-instance, also in the program code.

   The "Call options" dialog opens.
6. Click the "Single instance" button.
7. Select the desired ProDiag function block from the selection box "...".
8. Confirm your entries with "OK".

Or:

**To add local supervisions to a ProDiag function block using the "**
**Add new block**
**" dialog, follow these steps:**

1. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
2. Click "Data block".
3. At "Type" select the existing function block which contains local supervisions from the drop-down list.
4. Select the desired ProDiag function block from the selection box "...".
5. Confirm your entries with "OK".

Or:

**To assign local supervisions to a ProDiag function block in the ProDiag overview editor "**
**PLC supervisions &amp; alarms**
**", follow these steps:**

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click the tab "Supervisions &gt; Instantiated supervisions".

   All the local supervisions are displayed.
3. Click the desired instance.
4. Click the "…" selection field in the "ProDiag FB" column.

   A selection dialog opens.
5. Select the corresponding ProDiag function block.

> **Note**
>
> **Function blocks with supervised PLC data types**
>
> When you use PLC data types with supervisions in the function block, these supervisions will also be assigned the ProDiag function block that you have selected, for example, during the block call.

#### Result

The ProDiag supervisions of the user-defined function block are instantiated.

### Assigning supervisions of PLC data types to a ProDiag FB (S7-1500)

#### Description

The instances of the PLC data type supervisions are assigned to a ProDiag function block.

> **Note**
>
> **PLC data type without supervisions**
>
> When you create an element with a PLC data type that does not contain any supervisions yet, you can still assign a ProDiag function block. All later created supervisions are assigned to this ProDiag FB at the PLC data type.
>
> You can find all assignment options here: [Overview of the assignment options](#overview-of-the-assignment-options-s7-1500)

#### Requirement

You have created at least one supervision for an element of a PLC data type.

#### Working with a global DB

**You can create a tag of the data type "**
**PLC data type**
**" in a global data block:**

1. Double-click "Add new block" in the project tree.

   The "Add new block" dialog box opens.
2. Click "Data block".
3. Select the type from the "Global DB" drop-down list.
4. Open the created global data block.
5. Create an element and select a PLC data type with created supervisions as the data type.

   The included supervisions are automatically assigned, for example, to "Default_SupervisionFB":
6. If you want to change this assignment, click on the element in the global data block.
7. In the "Properties &gt; Supervisions" tab of the Inspector window, you can change the assignment in the "ProDiag FB" column by clicking "...".
8. You can also create a new ProDiag FB directly in the open dialog by clicking "Add".

or:

**You can create a global DB of the type "**
**PLC data type**
**":**

1. Double-click "Add new block" in the project tree.

   The "Add new block" dialog box opens.
2. Click "Data block".
3. For the type, select a PLC data type with already created supervisions from the drop-down list.
4. If you want to assign a function block other than the default ProDiag FB "Default_SupervisionFB", click the selection box "...".

   If you do not want to select any of the available ProDiag FBs, you can also create a new one directly by clicking "Add".
5. Confirm your entries with "OK".

**Note**

**Assigning ProDiag function blocks**

The section "Assign ProDiag function block" only appears in the dialog if the PLC data type contains supervisions.

or:

**You can create a global data block of the type "**
**ARRAY-DB**
**" with the data type "**
**PLC data type**
**":**

1. Double-click "Add new block" in the project tree.

   The "Add new block" dialog box opens.
2. Click "Data block".
3. Select the type from the "Array DB" drop-down list.
4. For the Array data type, select a PLC data type with already created supervisions.
5. If you want to assign a function block other than the default ProDiag FB "Default_SupervisionFB", click the selection box "...".

   If you do not want to select any of the available ProDiag FBs, you can also create a new one directly by clicking "Add".
6. Confirm your entries with "OK".

**Note**

**Assigning ProDiag function blocks**

The section "Assign ProDiag function block" only appears in the dialog if the PLC data type contains supervisions.

#### Working with a tag table

If you create an element of the data type "PLC data type" in a tag table and this PLC data type contains supervisions, the supervisions are then automatically assigned, for example, to the "Default_SupervisionFB".

If you want to change this assignment, follow these steps:

1. Click the element in the tag table.
2. In the "Properties &gt; Supervisions" tab, you can change the assignment in the "ProDiag FB" column by clicking "...".
3. You can also create a new ProDiag FB directly in the open dialog by clicking "Add".

### Assigning an instance data block to a ProDiag FB (local supervisions) (S7-1500)

#### Description

You can assign an instance data block of a user-defined function block directly to a ProDiag function block.

You can make this assignment even if the user-defined function block does not yet contain any supervisions. In addition, the assignment to the ProDiag function block is retained when the user defined function block is deleted.

#### Procedure

Proceed as follows to assign an instance data block of a user-defined function block to a ProDiag function block:

1. Right-click the instance data block of a function block.
2. Select the "Properties" command in the shortcut menu.

   The properties dialog of the instance data block opens.
3. Click the "Attributes" section.
4. Click the "…" selection field at "Assign ProDiag FB" to select a ProDiag function block.

   A selection dialog opens.
5. Click the "Program blocks" folder in the left-hand column.

   All existing ProDiag function blocks are displayed in the right-hand column.
6. Select the corresponding ProDiag function block.

#### Result

The ProDiag supervisions of the user-defined function block are instantiated.

### Changing the existing assignment of a ProDiag FB (S7-1500)

#### Requirement

You have already created global or local supervisions and have assigned a ProDiag function block to them.

#### Procedure at global supervisions

You have the following options to change the existing assignments of global supervisions to ProDiag function blocks:

| Location of the assignment options | Procedure |
| --- | --- |
| In the "PLC supervisions &amp; alarms" folder in the project tree | | Symbol | Meaning | | --- | --- | | 1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.    The alarm and supervision editor opens. 2. Click on the "Supervisions &gt; Global supervisions" tab.    All global supervisions are displayed. 3. Assign a different ProDiag function block to the corresponding supervisions in the "ProDiag FB" column. |  | |
| In a tag table or in a global data block with individual elements | | Symbol | Meaning | | --- | --- | | 1. Click the supervised tag, for example, in the default tag table.    The "Supervisions" tab opens in the "Properties" Inspector window and the properties of the supervision are displayed. 2. Click the "…" selection field at ProDiag FB.    A selection dialog opens. 3. Click the "Program blocks" folder in the left-hand column.    All existing ProDiag function blocks are displayed in the right-hand column. 4. Select the corresponding ProDiag function block. |  | |
| In the global data block of the type "PLC data type" | | Symbol | Meaning | | --- | --- | | 1. Right-click the global data block in the project tree. 2. Select the "Properties" command from the shortcut menu.    The properties dialog of the global data block opens. 3. Click the "Attributes" section. 4. Click the "…" selection field at "Assigned ProDiag FB" to select a different ProDiag function block.    A selection dialog opens. 5. Click the "Program blocks" folder in the left-hand column.    All existing ProDiag function blocks are displayed in the right-hand column. 6. Select the corresponding ProDiag function block. |  | |
| In the global data block of the type "ARRAY-DB" with the data type "PLC data type" | | Symbol | Meaning | | --- | --- | | 1. Click one of the array elements with a PLC data type.    The "Supervisions" tab opens in the "Properties" Inspector window and the properties of the supervisions are displayed. 2. Click the "…" selection field at ProDiag FB.    A selection dialog opens. 3. Click the "Program blocks" folder in the left-hand column.    All existing ProDiag function blocks are displayed in the right-hand column. 4. Select the corresponding ProDiag function block. |  | |
| Click the relevant ProDiag function block in the project tree | | Symbol | Meaning | | --- | --- | | 1. Double-click the relevant ProDiag function block in the project tree.    The ProDiag function block opens. 2. Click the "…" selection field in the "ProDiag FB" column.    A selection dialog opens. 3. Click the "Program blocks" folder in the left-hand column.    All existing ProDiag function blocks are displayed in the right-hand column. 4. Select the corresponding ProDiag function block. |  | |

#### Procedure at local supervisions

Proceed as follows to assign an instance data block of a user-defined function block to a ProDiag function block:

1. Right-click the instance data block of a function block.
2. Select the "Properties" command in the shortcut menu.

   The properties dialog of the instance data block opens.
3. Click the "Attributes" section.
4. Click the "…" selection field at "Assign ProDiag FB" to select a ProDiag function block.

   A selection dialog opens.
5. Click the "Program blocks" folder in the left-hand column.

   All existing ProDiag function blocks are displayed in the right-hand column.
6. Select the corresponding ProDiag function block.

Or:

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click the "Supervisions &gt; FB supervision instances" tab.

   All the local supervisions are displayed.
3. Click the "…" selection field in the "ProDiag FB" column to select a ProDiag function block.

   A selection dialog opens.
4. Click the "Program blocks" folder in the left-hand column.

   All existing ProDiag function blocks are displayed in the right-hand column.
5. Select the corresponding ProDiag function block.

#### Result

The assignment of the ProDiag function block has been changed.

---

**See also**

[Display supervision definitions of all called function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-called-function-blocks-and-plc-data-types-s7-1500)
  
[Display supervisions of all global tags (S7-1500)](#display-supervisions-of-all-global-tags-s7-1500)

### Removing the existing assignment of a ProDiag FB (S7-1500)

#### Requirement

You have already created local supervisions and have assigned a ProDiag function block to them.

#### Procedure

To change the existing assignment of an instance data block to a ProDiag function block, follow these steps:

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click the "Supervisions &gt; FB supervision instances" tab.

   All the local supervisions are displayed.
3. Click the "…" selection field in the "ProDiag FB" column.

   A selection dialog opens.
4. Click "None".

or:

1. Right-click the instance data block of a function block that contains local supervisions.
2. Select the "Properties" command in the shortcut menu.

   The properties dialog box of the instance data block opens.
3. Click the "Attributes" section.
4. Click the "…" selection field at Assign ProDiag FB.

   A selection dialog opens.
5. Click "None".

#### Result

The assignment of the ProDiag function block has been removed.

## Editing ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Inserting new supervisions in the ProDiag FB (S7-1500)](#inserting-new-supervisions-in-the-prodiag-fb-s7-1500)
- [Copying supervisions in the ProDiag FB (S7-1500)](#copying-supervisions-in-the-prodiag-fb-s7-1500)
- [Deleting supervisions in the ProDiag FB (S7-1500)](#deleting-supervisions-in-the-prodiag-fb-s7-1500)
- [Sorting supervisions in the ProDiag FB (S7-1500)](#sorting-supervisions-in-the-prodiag-fb-s7-1500)

### Inserting new supervisions in the ProDiag FB (S7-1500)

#### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also add new supervisions.

#### Requirement

You have assigned global supervisions to a ProDiag function block and have opened it.

#### Procedure

You have two options for adding a new supervision:

1. Right-click the last line of the table and select "Add new supervision" from the shortcut menu.

   A new supervision is created with the default values (type of supervision: "Operand", category: "1: Error", delay time: T#0ms).
2. Select a tag to be supervised.
3. Overwrite the default settings by changing the settings correspondingly.

or:

1. Enter a tag to be supervised in the last line in the "Supervised tag" column.

   A new supervision is created with the default values (type of supervision: "Operand", category: "1: Error", delay time: T#0ms).
2. If you specify a tag that you have not yet defined, the "Supervised tag" field turns red.
3. Define the tag in a tag table or data block.

#### Result

The new supervisions have been added.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Copying supervisions in the ProDiag FB (S7-1500)

#### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also copy individual or multiple supervisions within the tab or to another "Global supervisions" tab.

#### Requirement

You have created global supervisions.

#### Procedure

Proceed as follows to copy the complete line of a supervision:

1. Select the line you want to copy.

   You can also select several lines by clicking them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking the first and last row.
2. Select the "Copy" command from the shortcut menu.
3. Position the cursor at the end of the table.
4. Select "Paste" in the shortcut menu.

#### Result

- The supervision is copied to the destination.
- A new ID is assigned to the copied supervision.
- All other properties of the supervision remain unchanged.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Deleting supervisions in the ProDiag FB (S7-1500)

#### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also delete individual or multiple supervisions.

#### Requirement

You have created global supervisions.

#### Procedure

Proceed as follows to delete the complete line of a supervision:

1. Select the line with the supervision to be deleted.

   You can also select several lines by clicking them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking the first and last row.
2. Select the "Delete" command in the shortcut menu.

#### Result

The supervision is deleted.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

### Sorting supervisions in the ProDiag FB (S7-1500)

#### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also sort the supervisions in the columns "Supervised tag" and "ProDiag FB".

#### Requirement

You have created global supervisions.

#### Procedure

Proceed as follows to sort the supervisions:

1. Select one of the two columns by which you want to sort.
2. Click the column header.

   The column is sorted in the order of increasing values.

   An up arrow shows the sort sequence.
3. In order to change the sort sequence, click the arrow.

   The column is sorted in the order of decreasing values. A down arrow shows the sort sequence.
4. To restore the original sequence, click a third time on the column header.

#### Result

The supervisions are sorted as desired.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

## Calling the ProDiag function blocks (S7-1500)

This section contains information on the following topics:

- [Overview of calling the ProDiag function blocks (S7-1500)](#overview-of-calling-the-prodiag-function-blocks-s7-1500)

### Overview of calling the ProDiag function blocks (S7-1500)

#### Description

Once you have created and configured the supervisions and compiled your project, the created ProDiag function blocks are automatically called in the ProDiag organization block.

This activates the supervisions in your project. You now have various options for visualizing the supervisions on your HMI device.

If you do not want to call the ProDiag function blocks in the ProDiag OB, you can also call them in other blocks (FCs, FBs or OBs). We recommend that you program the calls either directly in a cycle OB or in a block that is called in a cycle OB. In this case, the respective ProDiag function block is no longer called in the ProDiag OB.

---

**See also**

[Displaying supervised user-defined blocks (S7-1500)](#displaying-supervised-user-defined-blocks-s7-1500)

## Load ProDiag blocks (S7-1500)

This section contains information on the following topics:

- [Load ProDiag blocks (S7-1500)](#load-prodiag-blocks-s7-1500-1)

### Load ProDiag blocks (S7-1500)

#### Description

During the loading operation, all information that is required for the reconstruction of the program, including symbolic information such as the names and comments for code and data blocks, is also loaded in the current project language.

The ProDiag blocks have no memory reserve and you can only load with re-initialization.

You can find additional information about loading blocks here: [Downloading blocks for S7-1200/1500](Compiling%20and%20downloading%20PLC%20programs.md#downloading-blocks-for-s7-12001500-s7-1200-s7-1500)

## Displaying, adding and editing ProDiag supervisions (S7-1500)

This section contains information on the following topics:

- [Overview of the display options (S7-1500)](#overview-of-the-display-options-s7-1500)
- [Displaying supervisions in the ProDiag overview editor (S7-1500)](#displaying-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Adding and editing supervisions in the ProDiag overview editor (S7-1500)](#adding-and-editing-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Displaying supervision definitions of a function block (S7-1500)](#displaying-supervision-definitions-of-a-function-block-s7-1500)
- [Displaying supervision definitions of a PLC data type (S7-1500)](#displaying-supervision-definitions-of-a-plc-data-type-s7-1500)
- [Displaying supervisions of a ProDiag function block (S7-1500)](#displaying-supervisions-of-a-prodiag-function-block-s7-1500)

### Overview of the display options (S7-1500)

#### Description

You have the option to have all the created supervisions displayed in different overviews. Depending on whether the supervision is local (supervisions at the parameters of a function block or at elements of a PLC data type) or global, the following display options are available:

| Display option | Description |
| --- | --- |
| ProDiag overview editor (PLC supervisions and alarms) | In the ProDiag overview editor you can have both the global and the local supervisions of a CPU displayed. |
| Properties of a function block | You can have all local supervisions that you have created either in the block interface of the function block or in a PLC data type displayed in the properties of a function block. |
| ProDiag function block | You can have all the global and instantiated local supervisions to which you have assigned this ProDiag function block displayed in the opened ProDiag function block. |

---

**See also**

[Displaying supervision definitions of a function block (S7-1500)](#displaying-supervision-definitions-of-a-function-block-s7-1500)
  
[Display supervision definitions of all function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-function-blocks-and-plc-data-types-s7-1500)
  
[Display supervision definitions of all called function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-called-function-blocks-and-plc-data-types-s7-1500)
  
[Display supervisions of all global tags (S7-1500)](#display-supervisions-of-all-global-tags-s7-1500)
  
[Adding new global supervisions in the ProDiag overview editor (S7-1500)](#adding-new-global-supervisions-in-the-prodiag-overview-editor-s7-1500)
  
[Displaying supervisions of a ProDiag function block (S7-1500)](#displaying-supervisions-of-a-prodiag-function-block-s7-1500)
  
[Displaying supervisions in the ProDiag overview editor (S7-1500)](#displaying-supervisions-in-the-prodiag-overview-editor-s7-1500)

### Displaying supervisions in the ProDiag overview editor (S7-1500)

This section contains information on the following topics:

- [Structure of the ProDiag overview editor (S7-1500)](#structure-of-the-prodiag-overview-editor-s7-1500)
- [Display supervisions of all global tags (S7-1500)](#display-supervisions-of-all-global-tags-s7-1500)
- [Display supervision definitions of all function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-function-blocks-and-plc-data-types-s7-1500)
- [Display supervision definitions of all called function blocks and PLC data types (S7-1500)](#display-supervision-definitions-of-all-called-function-blocks-and-plc-data-types-s7-1500)

#### Structure of the ProDiag overview editor (S7-1500)

##### Description

The following graphic shows an example of the components of the ProDiag overview editor:

![Description](images/139837229067_DV_resource.Stream@PNG-en-US.png)

| Numbering | Explanation | Additional information |
| --- | --- | --- |
| 1 | The "Global supervisions" tab shows all global supervisions. | Additional information is available here: [Display supervisions of all global tags](#display-supervisions-of-all-global-tags-s7-1500) |
| 2 | The "Supervision definitions" tab shows the following supervisions:  - all supervisions defined in the block interface of user-defined function blocks even when this user-defined function block has not yet been called in the program code - all supervisions defined in PLC data types even when the PLC data type has not been used in the program code yet | Additional information is available here: [Display supervision definitions of all function blocks and PLC data types](#display-supervision-definitions-of-all-function-blocks-and-plc-data-types-s7-1500) |
| 3 | The "Supervision instances" tab shows all supervisions of the function blocks and PLC data types that have already been called or used in the program code. | Additional information is available here: [Display supervision definitions of all called function blocks and PLC data types](#display-supervision-definitions-of-all-called-function-blocks-and-plc-data-types-s7-1500) |
| 4 | You have various filter options in each tab to only display the desired supervisions. |  |

#### Display supervisions of all global tags (S7-1500)

##### Description of the filter options

In the "Global supervisions" tab you can display the following supervisions using the filter:

- All global supervisions:

  All global supervisions from tag tables, global data blocks and at PLC data type instances are displayed.
- Global supervisions at PLC data type instances:

  Only the global supervisions that you have created at PLC data type instances are displayed.

##### Requirement

At least one supervision was created in a global data block, a tag table or at an element of a PLC data type instance.

##### Procedure

To display all global supervisions of a CPU, for example, follow these steps:

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click on the "Supervisions &gt; Global supervisions" tab.
3. Select the filter option "All global supervisions".

   All global supervisions of the CPU are displayed.
4. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
5. To show a column, select the column's check box.
6. To hide a column, clear the column's check box.
7. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

##### Result

All global supervisions and the desired columns are displayed in the "Global supervisions" tab.

#### Display supervision definitions of all function blocks and PLC data types (S7-1500)

##### Description of the filter options

In the "Supervision definitions" tab you can display the following supervisions using the filter:

- All supervision definitions

  All supervision definitions of function blocks and PLC data types are displayed.
- Supervision definitions in FBs

  All supervision definitions that you have created in the block interface of a function block and all those that have been created at a PLC data type element are displayed.
- Supervision definitions in PLC data types

  All supervision definitions that you have created in PLC data types are displayed.
- Supervision definitions in FBs at elements of PLC data types

  All supervision definitions that you have created in the block interface of a function block at a PLC data type element are displayed. (The supervisions created in a subordinate PLC data type are not displayed here.)

##### Requirement

At least one supervision was created in the block interface of the function block or in a PLC data type.

##### Procedure

To display all supervision definitions, for example, follow these steps:

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click on the "Supervisions &gt; Supervision definitions" tab.
3. Select the filter option "All supervision definitions".

   All supervision definitions of the CPU are displayed.
4. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
5. To show a column, select the column's check box.
6. To hide a column, clear the column's check box.
7. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

##### Result

All supervision definitions and the desired columns are displayed in the "Supervision definitions" tab.

#### Display supervision definitions of all called function blocks and PLC data types (S7-1500)

##### Description of the filter options

In the "Supervision instances" tab, you can display the following supervisions using the filter:

- All supervision instances

  All supervision instances from function blocks and PLC data types are displayed.
- FB supervision instances

  All supervision instances from the block interface are displayed. This includes supervisions at parameters directly in the block interface as well as inherited supervisions from PLC data types and inherited supervisions from function blocks.
- Supervision instances defined in PLC data types

  All the PLC data type supervision instances, for example, from a tag table or the PLC data type supervisions created in function blocks are displayed.

> **Note**
>
> **Changes with active filter**
>
> Changes to the assignments of ProDiag function blocks affect all supervisions (FB and PLC data type) of an instance, e.g. an instance DB, and not only the filtered view, e.g. only PLC data type instances.

##### Requirement

At least one supervision definition was instantiated.

##### Procedure

To display all supervision instances, for example, follow these steps:

1. Double-click the "PLC supervisions &amp; alarms" folder in the project tree.

   The alarm and supervision editor opens.
2. Click the tab "Supervisions &gt; Supervision instances".
3. Select the filter option "All supervision instances".

   All supervision instances are displayed.
4. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
5. To show a column, select the column's check box.
6. To hide a column, clear the column's check box.
7. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

##### Result

All supervision instances and the desired columns are displayed in the "Supervision instances" tab.

### Adding and editing supervisions in the ProDiag overview editor (S7-1500)

This section contains information on the following topics:

- [Adding new global supervisions in the ProDiag overview editor (S7-1500)](#adding-new-global-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Copying global supervisions in the ProDiag overview editor (S7-1500)](#copying-global-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Deleting global supervisions in the ProDiag overview editor (S7-1500)](#deleting-global-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Sorting global supervisions in the ProDiag overview editor (S7-1500)](#sorting-global-supervisions-in-the-prodiag-overview-editor-s7-1500)
- [Editing supervision definitions in the ProDiag overview editor (S7-1500)](#editing-supervision-definitions-in-the-prodiag-overview-editor-s7-1500)
- [Deleting supervision definitions in the ProDiag overview editor (S7-1500)](#deleting-supervision-definitions-in-the-prodiag-overview-editor-s7-1500)

#### Adding new global supervisions in the ProDiag overview editor (S7-1500)

##### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also add new supervisions.

##### Procedure

You have two options for adding a new supervision:

1. Right-click the last line of the table and select "Add new supervision" from the shortcut menu.

   A new supervision is created with the default values (type of supervision: "Operand", category: "1: Error", delay time: T#0ms).
2. Select a tag to be supervised.
3. Overwrite the default settings by changing the settings correspondingly.

or:

1. Enter a tag to be supervised in the last line in the "Supervised tag" column.

   A new supervision is created with the default values (type of supervision: "Operand", category: "1: Error", delay time: T#0ms).
2. If you specify a tag that you have not yet defined, the "Supervised tag" field turns red.
3. Define the tag in a tag table or in a global data block.

##### Result

The new supervisions have been added.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Copying global supervisions in the ProDiag overview editor (S7-1500)

##### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also copy individual or multiple supervisions within the tab or to a different tab.

##### Requirement

You have created global supervisions.

##### Procedure

Proceed as follows to copy the complete line of a supervision:

1. Select the line you want to copy.

   You can also select several lines by clicking them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking the first and last row.
2. Select the "Copy" command from the shortcut menu.
3. Position the cursor at the end of the table.
4. Select "Paste" in the shortcut menu.

##### Result

- The supervision is copied to the destination.
- A new ID is assigned to the copied supervision.
- All other properties of the supervision remain unchanged.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Deleting global supervisions in the ProDiag overview editor (S7-1500)

##### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also delete individual or multiple supervisions.

##### Requirement

You have created global supervisions.

##### Procedure

Proceed as follows to delete the complete line of a supervision:

1. Select the line with the supervision to be deleted.

   You can also select several lines by clicking them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking the first and last row.
2. Select the "Delete" command in the shortcut menu.

##### Result

The supervision is deleted.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Sorting global supervisions in the ProDiag overview editor (S7-1500)

##### Description

In addition to displaying the information for the created global supervisions in the "Global supervisions" tab, you can also sort them. The text columns are sorted alphabetically.

##### Requirement

You have created global supervisions.

##### Procedure

To sort the supervision by columns, follow these steps:

1. Select one of the columns by which you want to sort.
2. Click on the column header.

##### Result

The table is sorted by the selected column. A triangle with it pointing tip upwards appears in the column header.

Repeated clicking on the column header changes the sorting as follows:

- Symbol "▲": The column is sorted in the order of increasing values.
- Symbol "▼": The column is sorted in the order of decreasing values.
- No symbol: The sorting is canceled. The table assumes with default display.

---

**See also**

[Editing tables](Introduction%20to%20the%20TIA%20Portal.md#editing-tables)

#### Editing supervision definitions in the ProDiag overview editor (S7-1500)

##### Description

In the "Supervision definitions" tab, you can not only display the supervision functions but you can also edit them.

##### Requirement

You have created supervision definitions.

##### Procedure

To edit a supervision definition, follow these steps:

1. Select the supervision field to be edited.
2. Change the supervision property to be edited.

##### Result

The supervision is edited.

#### Deleting supervision definitions in the ProDiag overview editor (S7-1500)

##### Description

In the "Supervision definitions" tab, you can not only display the supervision functions but you can also delete individual or multiple supervisions.

##### Requirement

You have created supervision definitions.

##### Procedure

To delete a complete supervision definition, proceed as follows:

1. Select the row with the supervision definition to be deleted.

   You can also select several lines by clicking them one after the other while holding down the &lt;Ctrl&gt; key or by pressing and holding down &lt;Shift&gt; and clicking the first and last row.
2. In the shortcut menu, select the "Delete" command   
   or  
    press the "Del" key.

##### Result

The supervision definition is deleted.

### Displaying supervision definitions of a function block (S7-1500)

#### Requirement

Supervision definitions have been created in the block interface of a user-defined function block.

#### Procedure

To display the supervision definitions of the function block, follow these steps:

1. Right-click the function block in the project tree and select "Properties..." from the shortcut menu.

   The properties dialog box of the function block opens.
2. Click on the "Supervision definitions" tab.
3. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
4. To show a column, select the column's check box.
5. To hide a column, clear the column's check box.
6. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

Or:

1. Double-click the function block in the project tree.

   As long as you do not select anything in the block interface, the supervision definitions are displayed in the Inspector window "Properties" in the "Supervision definitions" tab.
2. From this point, the procedure described above from item 3 applies.

Or:

1. Select the "Program blocks" folder in the project tree.
2. Click on the "Maximizes/minimizes overview" button in the overview of the project tree.
3. Click on the desired function block.

#### Result

All supervision definitions of the user-defined function block and the desired columns are displayed in the "Supervision definitions" tab.

### Displaying supervision definitions of a PLC data type (S7-1500)

#### Requirement

Supervision definitions have been created in a PLC data type.

#### Procedure

To display the supervision definitions of the PLC data type, follow these steps:

1. Right-click the PLC data type in the project tree and select "Properties..." from the shortcut menu.

   The properties dialog of the PLC data type opens.
2. Click on the "Supervision definitions" tab.
3. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
4. To show a column, select the column's check box.
5. To hide a column, clear the column's check box.
6. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

Or:

1. Select the "PLC data types" folder in the project tree.
2. Click on the "Maximizes/minimizes overview" button in the overview of the project tree.
3. Click on the desired PLC data type.

#### Result

All supervision definitions of the PLC data type and the desired columns are displayed in the "Supervision definitions" tab.

### Displaying supervisions of a ProDiag function block (S7-1500)

#### Description of the filter options

In the "Global supervisions" tab, you can display the following supervisions using the filter:

- All global supervisions:

  All global supervisions from tag tables, global data blocks and at PLC data type instances are displayed.
- Global supervisions at PLC data type instances:

  Only the global supervisions that you have created at PLC data type instances are displayed.

In the "Supervision instances" tab, you can display the following supervisions using the filter:

- All supervision instances

  All supervision instances from function blocks and PLC data types are displayed.
- FB supervision instances

  All supervision instances from the block interface are displayed. This includes supervisions at parameters directly in the block interface as well as inherited supervisions from PLC data types and inherited supervisions from function blocks.
- Supervision instances defined in PLC data types

  All the PLC data type supervision instances, for example, from a tag table or the PLC data type supervisions created in function blocks are displayed.

#### Requirement

At least one supervision has been assigned to the ProDiag function block.

#### Procedure

To display all global and local supervisions of a ProDiag function block, follow these steps:

1. Double-click the desired ProDiag function block in the project tree.

   The ProDiag function block opens.
2. Click either the "Global supervisions" tab or the "Supervision instances" tab.
3. If necessary, you can filter the supervisions.
4. You can display and hide other columns in the table as needed. To do so, click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
5. To show a column, select the column's check box.
6. To hide a column, clear the column's check box.
7. To show or hide multiple columns, click "More" and select or clear the check boxes of the corresponding columns in the "Show/Hide" dialog.

   The sorting order of the columns cannot be changed.

#### Result

All the global supervisions are displayed in the "Global supervisions" tab, and all locally instantiated supervision instances that are assigned to this ProDiag function block are displayed in the "Supervision instances" tab.

## Displaying supervisions in detail view of the project tree (S7-1500)

This section contains information on the following topics:

- [Displaying supervised user-defined blocks (S7-1500)](#displaying-supervised-user-defined-blocks-s7-1500)
- [Displaying supervised PLC data types (S7-1500)](#displaying-supervised-plc-data-types-s7-1500)

### Displaying supervised user-defined blocks (S7-1500)

You have the option of displaying all blocks of a CPU in which you have created supervisions in the overview of the project tree.

#### Requirements

You have created ProDiag supervisions and compiled your program.

#### Procedure

To display the overview, follow these steps:

1. Select the "Program blocks" folder in the project tree.
2. Click "Maximizes/minimizes the Overview".
3. Click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
4. Select the check box in the "Supervisions" column to display the desired column.

#### Result

For all blocks that contain supervisions, the ProDiag symbol appears in the "Supervisions" column.

---

**See also**

[Overview window](Introduction%20to%20the%20TIA%20Portal.md#overview-window-1)

### Displaying supervised PLC data types (S7-1500)

You have the option of displaying all blocks of a CPU in which you have created supervisions in the overview of the project tree.

#### Requirements

You have created ProDiag supervisions at a PLC data type and compiled your program.

#### Procedure

To display the overview, follow these steps:

1. Select the "PLC data types" folder in the project tree.
2. Click "Maximizes/minimizes the Overview".
3. Click in the column header and select the "Show/Hide" command in the shortcut menu.

   The selection of available columns is displayed.
4. Select the check box in the "Supervisions" column to display the desired column.

#### Result

For all PLC data types that contain supervisions, the ProDiag symbol appears in the "Supervisions" column.

## Exporting and importing ProDiag supervisions (S7-1500)

This section contains information on the following topics:

- [Exporting and importing ProDiag supervisions and properties of a ProDiag FB (S7-1500)](#exporting-and-importing-prodiag-supervisions-and-properties-of-a-prodiag-fb-s7-1500)
- [Importing and exporting supervision definitions (S7-1500)](#importing-and-exporting-supervision-definitions-s7-1500)
- [Exporting and importing assignments of ProDiag FBs to instances (S7-1500)](#exporting-and-importing-assignments-of-prodiag-fbs-to-instances-s7-1500)

### Exporting and importing ProDiag supervisions and properties of a ProDiag FB (S7-1500)

This section contains information on the following topics:

- [Overview of exporting and importing supervisions and properties of a ProDiag FB (S7-1500)](#overview-of-exporting-and-importing-supervisions-and-properties-of-a-prodiag-fb-s7-1500)
- [Exporting supervisions and properties of a ProDiag FB (S7-1500)](#exporting-supervisions-and-properties-of-a-prodiag-fb-s7-1500)
- [Importing supervisions and properties of a ProDiag FB (S7-1500)](#importing-supervisions-and-properties-of-a-prodiag-fb-s7-1500)

#### Overview of exporting and importing supervisions and properties of a ProDiag FB (S7-1500)

##### Description

It is possible to export the properties of one or more ProDiag function blocks in addition to the created supervisions from the ProDiag overview tables "Global supervisions" and "Supervision definitions".

You can export these supervisions and properties to a standard XLSX format (Excel Spreadsheet) and work with external table editors (for example, to translate). You can also import new supervisions, properties, and new ProDiag function blocks added with external table editors to the TIA Portal. The supervision, properties and ProDiag function blocks are created automatically by the system.

From the ProDiag overview table "Supervision instances", you can export and import assignments of ProDiag function blocks to local supervisions.

##### Format of the export file

The names of the column titles are fixed by the system and must not be modified. All columns are exported even if you have hidden them in the ProDiag overview table. Each supervision has a separate line in the file.

The following table specifies the contents expected for the individual columns of the "ProDiag Supervisions" tab:

| Column | Explanation |
| --- | --- |
| ProDiag FB namespace | Corresponding namespace |
| ProDiag FB name | Name of the associated ProDiag function block |
| ID | Number of the supervision |
| Supervised tag / parameter | Supervised tag / parameter |
| Trigger | Signal state for which the operand is supervised:  - TRUE - FALSE |
| Type of supervision | Type of supervision:  - Operand - Interlock - Reaction - Action - Position - Text message - Error message |
| Category | Category:  - 1 (Error) - 2 (Warning) - 3 (Info) |
| Subcategory 1 and 2 | Subcategories that you have created in the ProDiag supervision settings |
| Delay time | Depending on the type of supervision, either:  - Delay time - Reaction time - Start-up time |
| C1, C2 or C3 trigger | Signal state for which the conditions are to be supervised:  - TRUE - FALSE |
| Condition 1, 2 or 3 | Operand used as the condition |
| Specific text field | Specific text field: Texts from manually created associated values with the character @ and free text  One column is created per project language. |
| FieldInfo "Specific text field" | Specific text field: Texts from associated values that were created using a shortcut menu item |
| Tag 1 (SD_4), Tag 2 (SD_5) or Tag 3 (SD_6) | Associated values of the text field that are read out during runtime |
| BelongsToUnit | Software Unit in which the supervision has been created. |

The following table specifies the contents expected for the individual columns of the "ProDiag Settings" tab:

| Column | Explanation |
| --- | --- |
| ProDiag FB | Name of the associated ProDiag function block |
| Version | Version of the ProDiag function block |
| Initial value acquisition | Initial value acquisition activated/deactivated |
| Use central time stamp | Use central time stamp enabled/disabled |
| Global enabler | Global enabler |
| Category | Category:  - 1 (Error) - 2 (Warning) - 3 (Info) |
| Category enabler | Enable criteria of the categories |
| Acknowledge tag | Acknowledgment tags for individual categories |
| Display class | Display class |

##### Example

The figure below shows an excerpt from the export file as an example:

![Example](images/84738345483_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Exporting supervisions and properties of a ProDiag FB (S7-1500)](#exporting-supervisions-and-properties-of-a-prodiag-fb-s7-1500)
  
[Importing supervisions and properties of a ProDiag FB (S7-1500)](#importing-supervisions-and-properties-of-a-prodiag-fb-s7-1500)

#### Exporting supervisions and properties of a ProDiag FB (S7-1500)

##### Requirement

You have created supervisions and defined properties for one or more ProDiag function blocks.

The supervision settings and the following settings are exported from the block properties:

- "General" area: The block version
- "Attributes" area: The "Initial value acquisition" and "Use central time stamp" options
- "Supervision settings" area: All settings

> **Note**
>
> **Exporting the properties of a ProDiag function block**
>
> The properties of a ProDiag function block can only be exported from the "Global supervisions" tab.

##### Procedure

To export the supervisions and properties of one or more ProDiag function blocks, follow these steps:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click on the "Supervisions" tab.
3. In the "Global supervisions" tab, click "Exports global supervisions" in the toolbar.

   The "Save as" dialog opens.
4. Select a storage location and assign a file name.
5. Click "Save".

   If the file was successfully saved, the "Export successfully completed" dialog opens.
6. Click "OK" to confirm.

or:

1. Open the ProDiag function block with a double-click.
2. Click "Exports global supervisions" in the toolbar. You can only export global supervisions from the ProDiag function block.

   The "Save as" dialog opens.
3. Select a storage location and assign a file name.
4. Click "Save".

   Once the file was successfully saved, the "Export successfully completed" dialog opens.
5. Click "OK" to confirm.

##### Result

An .xlsx file is created at the selected storage location.

- You can find the exported supervisions in the "ProDiag Supervisions" tab.

  ![Result](images/102353135115_DV_resource.Stream@PNG-de-DE.png)
- You can find all ProDiag-specific properties that you have defined for the ProDiag function blocks in the "ProDiag Settings" tab.

  ![Result](images/139838392971_DV_resource.Stream@PNG-de-DE.png)

#### Importing supervisions and properties of a ProDiag FB (S7-1500)

##### Requirement

You have exported the supervisions and properties of a ProDiag function block to an .xlsx file.

##### Procedure

To import the supervisions and properties of one or more ProDiag function blocks, follow these steps:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click on the "Supervisions" tab.
3. In the "Global supervisions" tab, click "Imports global supervisions" in the toolbar.

   The "Imports global supervisions" dialog box opens.
4. Select the path where the file to be imported is stored.

   The "Open" dialog opens.
5. Select the desired .xlsx file.
6. Confirm the dialog with "Open".
7. You have several options in the "Imports global supervisions" dialog:

   - "Import supervisions"

     If you enable the options "Import supervisions" and "Delete existing supervisions", the existing supervisions of ProDiag function blocks for which there are also supervisions in the .xlsx import file are deleted in the overview table and the newly created supervisions are added from the .xlsx file. If there are no supervisions for A ProDiag function block in the .xlsx import file, this is also excluded from the deletion.

     If you disable the "Delete existing supervisions" option, the existing supervisions are kept and the newly created supervisions are added.
   - "Import and overwrite supervision settings"

     If you enable the option "Import and overwrite supervision settings" and the ProDiag function block already contains supervision settings, the old settings are overwritten with the new settings.
8. Click the "Import" button.

   The "Import global supervisions" dialog opens. The dialog displays the current status of the import.
9. If the import was successful, the "Import completed" dialog opens.
10. If an error occurred during the import, the "Import completed with warnings" dialog opens.

    The following errors can occur:

    - The .xlsx file contains incorrect entries.
    - The maximum number of supervisions for a ProDiag function block was exceeded.
    - The function block specified in the .xlsx file is not contained in your program. (Can only occur when supervisions are imported within the "Supervision definitions" overview table.)
11. In this case, click on "Click here to view the log file".
12. Click "OK" to confirm.

Or:

1. Open the ProDiag function block with a double-click.
2. Click "Imports global supervisions" in the toolbar.

   The "Imports global supervisions" dialog box opens.
3. All other steps are the same as described above, starting with step 4.

##### Result

The ProDiag overview table now shows the imported supervisions and the block properties in the ProDiag function blocks correspond to the previously exported properties.

For global supervisions the following applies:

If you have added new supervisions in the .xlsx file, these are automatically assigned to the corresponding ProDiag function block after the import.

For local supervisions the following applies:

With local supervisions initially only the supervision definitions are imported and only through the import of the assignments are the supervisions assigned to concrete ProDiag function blocks.

### Importing and exporting supervision definitions (S7-1500)

This section contains information on the following topics:

- [Overview of the supervision definitions (S7-1500)](#overview-of-the-supervision-definitions-s7-1500)
- [Exporting supervision definitions (S7-1500)](#exporting-supervision-definitions-s7-1500)
- [Importing supervision definitions (S7-1500)](#importing-supervision-definitions-s7-1500)

#### Overview of the supervision definitions (S7-1500)

##### Description

It is possible to export the supervision definitions from the ProDiag "Supervision definitions" overview table.

You can export the supervision definitions to a standardized XLSX format (Excel spreadsheet) and edit (e.g. translate) them with external spreadsheet programs. Similarly, you can import new supervision definitions that were added with external spreadsheet programs into the TIA Portal.

##### Format of the export file

The names of the column titles are fixed by the system and must not be modified. Each supervision definition has a separate line in the file.

The following table specifies the contents expected in the individual columns:

| Column | Explanation |
| --- | --- |
| Supervised type name | Name of the supervised type (function block or PLC data type) |
| Supervised member | Supervised items of the type |

##### Example

The figure below shows an excerpt from the export file as an example:

![Example](images/139652154507_DV_resource.Stream@PNG-de-DE.png)

#### Exporting supervision definitions (S7-1500)

##### Requirement

You have created local supervisions.

##### Procedure

To export the supervision definitions file, proceed as follows:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click "Supervision definitions" in the "Supervisions" tab.
3. If necessary, select a filter to limit the number of supervision definitions.
4. Click "Exports supervision definitions" in the toolbar.

   The "Save as" dialog opens.
5. Select a storage location and assign a file name.
6. Click "Save".

   If the file was successfully saved, the "Export completed" dialog opens.
7. Click "OK" to confirm.

##### Result

An .xlsx file is created at the selected memory location.

#### Importing supervision definitions (S7-1500)

##### Requirement

You have exported supervision definitions to an .xlsx file.

##### Procedure

To import the supervision definitions file, proceed as follows:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click "Supervision definitions" in the "Supervisions" tab.
3. Click "Imports supervision definitions" in the toolbar.

   The "Imports supervision definitions" dialog box opens.
4. Select the path where the file to be imported is stored.

   The "Open" dialog opens.
5. Select the desired .xlsx file.
6. Confirm the dialog with "Open".
7. Click the "Import" button.

   The "Imports supervision definitions" dialog box opens. The dialog displays the current status of the import.
8. If the import was successful, the "Import completed" dialog opens.
9. If an error occurred during the import, the "Import completed with warnings" dialog opens.

   The following errors can occur:

   - The .xlsx file contains incorrect entries.
   - The .xlsx file contains missing assignments.
10. In this case, click on "Click here to view the log file".
11. Click "OK" to confirm.

##### Result

The imported supervision definitions are displayed in the ProDiag overview table.

### Exporting and importing assignments of ProDiag FBs to instances (S7-1500)

This section contains information on the following topics:

- [Overview of exporting and importing assignments (S7-1500)](#overview-of-exporting-and-importing-assignments-s7-1500)
- [Exporting assignments (S7-1500)](#exporting-assignments-s7-1500)
- [Importing assignments (S7-1500)](#importing-assignments-s7-1500)

#### Overview of exporting and importing assignments (S7-1500)

##### Description

You can export the created assignments of ProDiag function blocks to instances from the ProDiag overview table "Supervision instances".

You can export these assignments to a standardized XLSX format (Excel spreadsheet) and edit (e.g. translate) them with external spreadsheet programs. Similarly, you can import new assignments that were added with external spreadsheet programs into the TIA Portal.

##### Format of the export file

The names of the column titles are fixed by the system and must not be modified. Each assignment has a separate line in the file.

The following table specifies the contents expected in the individual columns:

| Column | Explanation |
| --- | --- |
| Instance | Name of the associated instance |
| ProDiag FB | Name of the ProDiag function block |

##### Example

The figure below shows an excerpt from the export file as an example:

![Example](images/84111014411_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Exporting assignments (S7-1500)](#exporting-assignments-s7-1500)
  
[Importing assignments (S7-1500)](#importing-assignments-s7-1500)

#### Exporting assignments (S7-1500)

##### Requirement

You have created local supervisions and called the function block in the program code.

##### Procedure

Proceed as follows to export the assignment:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click "FB supervision instances" in the "Supervisions" tab.
3. Click "Exports assignments of ProDiag FBs to instance DBs and PLC data type instances" in the toolbar.

   The "Save as" dialog opens.
4. Select a storage location and assign a file name.
5. Click "Save".

   If the file was successfully saved, the "Export completed" dialog opens.
6. Click "OK" to confirm.

##### Result

An .xlsx file is created at the selected memory location.

#### Importing assignments (S7-1500)

##### Requirement

You have exported assignments into an .xlsx file.

##### Procedure

Proceed as follows to import the assignments:

1. Open the "PLC supervisions &amp; alarms" folder in the project tree.
2. Click "FB supervision instances" in the "Supervisions" tab.
3. Click "Imports assignments of ProDiag FBs to instance DBs and PLC data type instances" in the toolbar.

   The "Imports assignments of ProDiag FBs to instance DBs and PLC data type instances" dialog is opened.
4. Select the path where the file to be imported is stored.

   The "Open" dialog opens.
5. Select the desired .xlsx file.
6. Confirm the dialog with "Open".
7. Click the "Import" button.

   The "Imports assignments of ProDiag FBs to instance DBs and PLC data type instances" dialog is opened. The dialog displays the current status of the import.
8. If the import was successful, the "Import completed" dialog opens.
9. If an error occurred during the import, the "Import completed with warnings" dialog opens.

   The following errors can occur:

   - The .xlsx file contains incorrect entries.
   - The .xlsx file contains missing assignments.
10. In this case, click on "Click here to view the log file".
11. Click "OK" to confirm.

##### Result

The imported assignments are displayed in the ProDiag overview table.

## Displaying ProDiag cross-references (S7-1500)

This section contains information on the following topics:

- [Overview of cross-references (S7-1500)](#overview-of-cross-references-s7-1500)
- [Displaying cross-references (S7-1500)](#displaying-cross-references-s7-1500)

### Overview of cross-references (S7-1500)

#### Description

Within your user program the cross-reference list provides you with an overview of the points of use of supervised tags and for example tags used as a condition within a ProDiag supervison.

You can jump directly to the point of use of a supervised tag from the cross-reference list.

You can find additional information displaying cross-references here: [General information about cross references](Displaying%20cross-references.md#general-information-about-cross-references)

### Displaying cross-references (S7-1500)

#### Description

The cross-reference information for a selected supervised tag (global supervisions) is displayed in the Inspector window in the tab "About &gt; Cross reference list in the programming window. For each selected supervised tag, it shows which ProDiag function block it is assigned to and at which points it is used. If the supervised tag is not only supervised but is for example used as a condition in another ProDiag supervision this use is also listed. You can recognize a supervised tag because the identifier "PRODIAG Supervision" is entered in the "Access" column. If the tag is used as a condition, this is indicated in the "Access" column by the identifier "Read-only"

You can display the cross-references at the following locations in the TIA Portal:

- Default tag table
- ProDiag overview editor

  - "Global supervisions" tab
- ProDiag function blocks

  - "Global supervisions" tab

#### Procedure

To display the cross references in the Inspector window , follow these steps:

1. Click the supervised tag, for example, in the default tag table.

   In the Inspector window in the tab "About &gt; Cross reference list" you will see the supervised tag and the assigned ProDiag function block.
2. Click the arrow to the left of the ProDiag function block.

   All points of use of this tag are displayed (supervision IDs).
3. Click on one of the displayed points of use, to jump directly to it.

   The corresponding ProDiag function block is opened and the relevant cell marked.

   > **Note**
   >
   > **Marking of a cell**
   >
   > If no cell is marked the corresponding column containing the tag is not displayed.

## Acquiring initial values (S7-1500)

This section contains information on the following topics:

- [Overview of initial value acquisition (S7-1500)](#overview-of-initial-value-acquisition-s7-1500)
- [Activating initial value acquisition (S7-1500)](#activating-initial-value-acquisition-s7-1500)
- [Example of order of the list (S7-1500)](#example-of-order-of-the-list-s7-1500)

### Overview of initial value acquisition (S7-1500)

#### Requirement

In order to enable initial value acquisition, you need to set version 2.0 in the ProDiag function block instead of version 1.0.

Initial value acquisition for ProDiag is available in the LAD and FBD programming languages.

The following requirements must be met in the user program for the initial values to be acquired:

- A maximum of 32 signal states is recorded. If a LAD/FBD network has more than 32 elements, no recording takes place.
- For global supervisions: The user program must have only one write access to the supervised tag and this write access must be placed on the right power rail.
- For local supervisions: A separate instance supervision is created for each new instance. However, if local tags are used as prefix in the calling block, the recording of the initial value works if either the associated single instance of the calling block has the name "FBName_DB" or the monitored block is called as a multi-instance.  
  In addition, only the Input, Output and Static sections may have been used in the function block interface.

You can find additional information here: [Activating initial value acquisition](#activating-initial-value-acquisition-s7-1500)

#### Recording of the initial values

The initial values can be recorded for the following supervision types:

| Types of supervision | Global supervisions |  |  | Local supervisions |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Input | Output | Bit memory | Input | Output | Static |  |
| Operand | - | - | - | x | - | - |
| Interlock | - | x | x | x | - | - |
| Action | - | - | - | x | - | - |
| Reaction | - | - | - | x | - | - |
| Position | - | - | - | x | - | - |
| Text message | - | - | - | - | - | - |
| Error message | - | - | - | - | - | - |

#### Description

The initial value acquisition gives you the option of analyzing why a supervision alarm was triggered. The initial values of the operands that are programmed in the user program prior to the supervised operand are recorded for this purpose.

You have the option of testing the execution of your user program on the HMI device. The data and values on the HMI device are continuously synchronized with the CPU and updated. You can always see the current program status for each LAD or FBD block on the HMI device.

For global supervisions the initial values of all Boolean operands in the network are recorded. If the network contains multiple individual power rails that are not connected to each other, only the initial values of the respective power rail are recorded.

For local supervisions only the initial values that are specified as conditions for the supervised parameter with the block call are recorded.

The initial values are recorded as soon as an event occurs that triggers a supervision alarm. The initial values are saved in a DWORD in the static CRIT_ERR parameter in the ProDiag instance data block; each individual signal state takes up one bit. The initial values are recorded in the cycle in which the event occurred. The supervision alarm is then sent in the next cycle. A maximum of 32 signal states per network can be recorded in an LAD or FBD block. The initial values are not changed until a new event occurs in the active network.

You can display the actual values with the help of the PLC code view. As soon as an event occurs, you can have the initial values displayed and the bad operands can be immediately recognized (criteria analysis). You can switch between display of the actual values and display of the initial values.

For criteria analysis on the HMI device, the operands are always read starting from the right at the coil against the circuit to the left.

You can find additional information on visualization on the HMI device here: "Visualize processes &gt; Using diagnostics functions &gt; Supervising machinery and plants with ProDiag"

#### Supported instructions

The following instructions are supported in LAD and FBD for initial value acquisition:

| Instructions | Display on the HMI device (HMI) |
| --- | --- |
| **Bit logic operations** |  |
| Normally open contact | Initial values and criteria analysis |
| Normally closed contact |  |
| Invert RLO | The instruction is supported but it is not relevant for initial values or criteria analysis. |
| Assignment |  |
| Negate assignment |  |
| Reset output | Initial values |
| Set output |  |
| Set/reset flip-flop | Initial values and criteria analysis up to and including the instruction box |
| Reset/set flip-flop |  |
| AND (FBD) | Initial values and criteria analysis |
| OR (FBD) |  |
| **Comparator operations** |  |
| Equal | Initial values and criteria analysis |
| Not equal |  |
| Greater or equal |  |
| Less or equal |  |
| Greater than |  |
| Less than |  |
| **Timers** |  |
| TP | Initial values and criteria analysis up to and including the instruction box |
| TON | Initial values and criteria analysis |
| TOF | Initial values and criteria analysis up to and including the instruction box |
| TONR |  |
| **Counters** |  |
| CTU | Initial values and criteria analysis up to and including the instruction box |
| CTD |  |
| CTUD |  |

For bit logic operations, the status of the operand is recorded. For comparators, the result of the comparison is recorded.

For flip-flops, both inputs (R and S) are recorded if they are interconnected.

For timers and counters, the status of the operand at the output, and the inputs if they are interconnected, are recorded. (for example with CTUD: CU, CD, R, LD)

#### Evaluation order on the HMI device in the PLC code view

The recording of the signal status in the respective DWORD or the list of operands in the symbol table of the PLC code view is carried out in a defined order. In an LAD network, for example, the process always starts in the power rail at the top left and ends at the bottom right.

> **Note**
>
> **Observe the evaluation order during programming**
>
> Also in the criteria analysis on the HMI device, this order is adhered to for the list of the bad operands in the symbol table. Observe this evaluation order for the programming of the networks.

Additional information on the order of the list is available here: [Example of order of the list](#example-of-order-of-the-list-s7-1500)

---

**See also**

[Structure of a ProDiag instance data block of version 2.0 (S7-1500)](#structure-of-a-prodiag-instance-data-block-of-version-20-s7-1500)
  
[Content of a ProDiag instance data block of version 2.0 (S7-1500)](#content-of-a-prodiag-instance-data-block-of-version-20-s7-1500)

### Activating initial value acquisition (S7-1500)

#### Procedure

Proceed as follows to activate initial value acquisition:

1. Right-click the ProDiag function block and select "Properties..." from the shortcut menu.

   The properties dialog box of the ProDiag function block opens.
2. Select version V2.0 in the "General &gt; Block" tab.
3. Click on the "Attributes" tab.
4. Activate the "Initial value acquisition (for criteria analysis on HMI devices)" option.
5. Click "OK".
6. Compile and download the user program.

#### Result

Initial value acquisition is activated as soon as the user program has been compiled. This means that the corresponding signal states are recorded in case of error.

### Example of order of the list (S7-1500)

The recording of the actual or initial values and the list of operands in the symbol table of the PLC code view are subject to the same defined order.

Using the following examples you can see how the recording of the signal states within an LAD network and the listing of operands on the HMI device work.

#### Recording the signal states in case of error

The signal states are written to the static parameter CRIT_ERR in the following order:

![Recording the signal states in case of error](images/101001910539_DV_resource.Stream@PNG-en-US.png)

On the HMI device, all operands are listed in exactly this order in the PLC code view:

| Symbol name | Operand | Comment |
| --- | --- | --- |
| Tag_1 | e.g. %M2xy | Automatic mode / manual mode |
| Tag_3 | Switch on the motor |  |
| Tag_2 | Interlock_1 |  |
| Tag_1 | Automatic mode / manual mode |  |
| Tag_5 | Manual switch |  |
| Tag_4 | Light barrier |  |

#### List of operands in case of error

If errors occur in the network, the bad operands are marked in color and only the bad operands are listed in the symbol table:

![List of operands in case of error](images/101002358795_DV_resource.Stream@PNG-de-DE.png)

List of the bad operands in the symbol table of the PLC code view:

| Symbol name | Operand | Comment |
| --- | --- | --- |
| Tag_2 | e.g. %M2xy | Interlock_1 |
| Tag_1 | Automatic mode / manual mode |  |
| Tag_5 | Manual switch |  |
| Tag_4 | Light barrier |  |

#### Optimized programming of the network in case of error

In order that you can see at first glance that the light barrier is responsible for the error, in this example it is beneficial to program the operand "Tag_4: Light barrier" first:

![Optimized programming of the network in case of error](images/101002435851_DV_resource.Stream@PNG-de-DE.png)

The information about the open light barrier is then displayed in the first line of the symbol table.

| Symbol name | Operand | Comment |
| --- | --- | --- |
| Tag_4 | e.g. %M2xy | Light barrier |
| Tag_2 | Interlock_1 |  |
| Tag_1 | Automatic mode / manual mode |  |
| Tag_5 | Manual switch |  |

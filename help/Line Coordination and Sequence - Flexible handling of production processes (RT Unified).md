---
title: "Line Coordination and Sequence - Flexible handling of production processes  (RT Unified)"
package: WCCULCSSESESenUS
topics: 92
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Line Coordination and Sequence - Flexible handling of production processes  (RT Unified)

This section contains information on the following topics:

- [Important notes (RT Unified)](#important-notes-rt-unified)
- [Migrating V16 project (RT Unified)](#migrating-v16-project-rt-unified)
- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring SES function blocks in the PLC (SES) (RT Unified)](#configuring-ses-function-blocks-in-the-plc-ses-rt-unified)
- [Structuring the plant (RT Unified)](#structuring-the-plant-rt-unified)
- [Configuring the controls (RT Unified)](#configuring-the-controls-rt-unified)
- [Compiling configuration data and loading it into Runtime (RT Unified)](#compiling-configuration-data-and-loading-it-into-runtime-rt-unified)
- [Validation of the configuration of plant objects (RT Unified)](#validation-of-the-configuration-of-plant-objects-rt-unified)
- [Configuring and operating production processes in Runtime (RT Unified)](#configuring-and-operating-production-processes-in-runtime-rt-unified)
- [Local reporting for Line Coordination (LCS) (RT Unified)](#local-reporting-for-line-coordination-lcs-rt-unified)

## Important notes (RT Unified)

### Internet browser

To make optimal use of WinCC Unified Line Coordination and WinCC Unified Sequence, you should use Google Chrome or Microsoft Edge.

## Migrating V16 project (RT Unified)

### Introduction

When you open your V16 project with LCS and/or SES configuration in TIA Portal V17, you have the option of upgrading the project to V17.

The configured Runtime version of the HMI device must be changed to V17 after upgrading. The LCS controls and the SES control are implicitly migrated through this step. Manual migration of the control within a screen is not necessary.

### Upgrade project

1. Open your V16 project in TIA Portal V17.

   The "Open project" dialog opens:

   ![Upgrade project](images/140319964811_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > When a product is not installed in V17 but is used in the V16 project, an upgrade is not possible. Install the missing product and then perform the upgrade.
2. Click "Upgrade".

   The upgrade will take a few minutes.

   The project is opened.

**Result**

- The contents of the V16 project are saved in a new project with the V17 project version.
- The original project is not overwritten and can still be edited with TIA Portal V16.

### Changing the configured Runtime version of the HMI device

1. Right-click on the HMI device in the project tree.
2. Select "Change device / version".

   The "Change device - SIMATIC WinCC Unified PC" dialog opens.
3. Navigate to "SIMATIC WinCC Unified PC" in the right tree.

   The existing HMI device with version V17 is automatically displayed under "New device".

   ![Changing the configured Runtime version of the HMI device](images/140357886091_DV_resource.Stream@PNG-en-US.png)
4. Confirm your change with "OK".

### Updating SES function blocks

When SES function blocks are used in the project, follow these steps:

1. Delete all SES equipment modules (instances) from the plant hierarchy.

   > **Note**
   >
   > When you have linked a screen at the plant object in the "Visualization" tab, deleting the plant object not only deletes the link but the entire screen.
   >
   > Create a copy of the screen and link the screen to the new plant object after updating the SES function blocks.
2. Open the "Library" task card.
3. Under "Global libraries", open the shortcut menu of the "SES-Sequence Execution System".
4. Click on "Project" under "Update types".

   The "Update types in the project" dialog box opens.

   ![Updating SES function blocks](images/143561552523_DV_resource.Stream@PNG-en-US.png)
5. Click "OK".
6. Compile the PLC.
7. Recreate all SES equipment modules (instances) in the plant hierarchy.
8. Change the names of the SES equipment modules (instances).
9. Compile and download your project.

> **Note**
>
> Alternatively, delete the interconnection of the PLC tag at the plant object type, run the update and interconnect the PLC tag at the plant object type again.
>
> Due to the high configuration effort for this alternative, we do not recommend it because the SES configuration at the plant object type is lost and must be reconfigured.

### Line tags

The old names of the tags are retained under "Interface" in the plant object type of the line during migration. In addition, two new tags are added:

- @JobDataForLcsJobOrder
- @JobDataResultForLcsJobOrder

![Line tags](images/143561562891_DV_resource.Stream@PNG-en-US.png)

When you create a new line as plant object type, the new names of the tags are displayed under "Interface".

![Line tags](images/143561918859_DV_resource.Stream@PNG-en-US.png)

## Basics (RT Unified)

This section contains information on the following topics:

- [Introduction to Line Coordination (LCS) (RT Unified)](#introduction-to-line-coordination-lcs-rt-unified)
- [Introduction to Sequence (SES) (RT Unified)](#introduction-to-sequence-ses-rt-unified)
- [Possible applications (RT Unified)](#possible-applications-rt-unified)
- [Requirements (RT Unified)](#requirements-rt-unified)
- [Line Coordination configuration concept (LCS) (RT Unified)](#line-coordination-configuration-concept-lcs-rt-unified)
- [Sequence configuration concept (SES) (RT Unified)](#sequence-configuration-concept-ses-rt-unified)
- [ISA-88 type definition (RT Unified)](#isa-88-type-definition-rt-unified)
- [Procedures, recipes and materials (LCS) (RT Unified)](#procedures-recipes-and-materials-lcs-rt-unified)
- [Jobs (RT Unified)](#jobs-rt-unified)
- [Steps and operations (SES) (RT Unified)](#steps-and-operations-ses-rt-unified)
- [States and transient states (RT Unified)](#states-and-transient-states-rt-unified)
- [Status (RT Unified)](#status-rt-unified)

### Introduction to Line Coordination (LCS) (RT Unified)

#### Introduction

SIMATIC WinCC Unified Line Coordination is an option package of the Plant Intelligence options of the TIA Portal.

With WinCC Unified Line Coordination, you coordinate and synchronize the processes in the production lines in your plant. You manage materials, create procedures and recipes for production and manage jobs for production.

In the following documentation, the term "LCS" (Line Coordination System) is also used to refer to "WinCC Unified Line Coordination".

![Introduction](images/118703851531_DV_resource.Stream@PNG-de-DE.png)

#### Functional scope

You create and configure the following functions with WinCC Unified Line Coordination:

- You define the sequence of production in the form of procedures based on operations. You define operations either directly with WinCC Unified Line Coordination or with WinCC Unified Sequence.
- You create recipes from previously created procedures and parameters, which yield various end products having different compositions.
- On the basis of recipes and procedures, you create jobs that you plan, configure and monitor.
- You visualize the processes of the production line in Runtime using different controls and operate the production line on the HMI device.

#### Benefits

With WinCC Unified Line Coordination, you create, edit and control the production processes of the plant on the HMI device.

- You monitor and modify the production processes in the production lines.
- You reduce the workload by standardizing processes.
- You monitor and coordinate the production jobs.

### Introduction to Sequence (SES) (RT Unified)

#### Introduction

SIMATIC WinCC Unified Sequence is an option package of the Plant Intelligence options of the TIA Portal.

With WinCC Unified Sequence you can implement your sequential control system for recipe-based and sequence-based processes such as mixing, dosing and material transport, for example in food production and other fields.

In the following documentation, the term "SES" (Sequence Execution System) is also used to refer to "WinCC Unified Sequence".

#### Functional scope

You create and configure the following functions with WinCC Unified Sequence:

- You configure simple production steps.
- You visualize current manufacturing steps and states.
- You change production parameters and production processes in runtime.
- You perform a clear comparison of actual values with setpoints for each individual step.
- You activate single step mode, in which the operator switches to the next step independently.
- You intervene with manual jumps to a certain step in the active process.
- You use your SES configuration in recipes and procedures.
- You start the production steps via a job.

#### Benefits

With WinCC Unified Sequence, you control production steps of your plant.

- You reduce the configuration workload by standardizing the control and visualization.
- You monitor and modify the recipe- and sequence-based process of your plant.

### Possible applications (RT Unified)

#### Using recipes, procedures and jobs

For flexible and efficient coordination of production processes in the production plant on an HMI device, you use recipes, procedures and jobs.

In production plants with a high degree of standardization, WinCC Unified Line Coordination allows you to minimize the engineering workload with reusable elements, map the production sequence efficiently and adjust it at any time.

**Area of application and advantages**

WinCC Unified Line Coordination provides added value in the following areas of application:

- Planning and quality assurance

  You define standardized processes for the entire production line.
- Maintenance and service

  You monitor production and detect problems in production processes.
- Coordination of production line and operation

  You coordinate, manage and control the jobs in a centralized manner at a configuration station or on individual machines.
- Flexible process changes

  You adapt the processes as required without having to change the control program.

#### Using steps and operations

You create steps and operations for flexible and efficient coordination of the sequential production processes in the production plant on an HMI device.

WinCC Unified Sequence is used in production plants in which dosing, mixing and material transport play an important role. In such plants, raw materials stored in tanks, silos or containers can be combined in the correct process sequence with reaction tanks and processing machines – across multiple processing steps all the way to the finished end product.

**Area of application and advantages**

In WinCC Unified Sequence the plant operator defines the production steps of the production units, specifies the production parameters, such as the setpoints, and defines the production processes in the form of sequencers. By means of prepared controls and function blocks, high engineering efficiency is guaranteed because the plant constructor or configuration engineer saves time during engineering as well as testing and commissioning.

This results in the following advantages:

- Minimal engineering workload through standardization
- Increased quality due to efficient operations management
- Flexible routes through production resulting in even utilization of individual production plants
- Fine tuning of production processes when behavior deviates due to variations, such as natural raw materials
- Fulfillment of real-time requirements, because an operation is running after start in the PLC
- Low training and operating costs

### Requirements (RT Unified)

#### Introduction

You have the possibility to install the optional packages WinCC Unified Line Coordination and WinCC Unified Sequence independent of each other. You require a separate license for each of the optional packages. For information about licenses, see the Plant Intelligence Options installation guide in the "Licensing PI Options" section.

When you install WinCC Unified Sequence without WinCC Unified Line Coordination, you can still add SES units and SES operations to procedures. You can include this procedure in a recipe and this recipe in a job. By starting this job, you ensure that several SES operations are executed consecutively without gaps. Only one unit per procedure is included within the SES license.

> **Note**
>
> If you need several units in one procedure, install and license WinCC Unified Line Coordination.

#### Software requirements

You require the following products before you install the optional packages WinCC Unified Line Coordination and/or WinCC Unified Sequence:

- TIA Portal V17 with STEP 7 Professional and WinCC Advanced/Unified PC
- WinCC Unified PC V17

#### Hardware requirements

WinCC Unified Line Coordination and WinCC Unified Sequence are available for the CPUs of the S7-1500 series.

#### User knowledge

You have the following knowledge:

- General knowledge about TIA Portal
- Configuration of plant views, plant objects and plant object types

### Line Coordination configuration concept (LCS) (RT Unified)

#### Introduction

Configuration with Line Coordination is divided into the following tasks:

**TIA Portal project**

- Definition of one or more production lines, units and equipment operations
- Creation of screens and screen objects

**HMI Runtime**

![Introduction](images/141004269707_DV_resource.Stream@PNG-de-DE.png)

① Planning and defining materials and material classes

② Planning and defining procedures and recipes

③ Creating, defining, controlling and monitoring production jobs

These tasks are carried out by users with different roles.

- A system integrator creates the visualization of the production line in a WinCC project.
- A technologist drafts procedures and recipes in Runtime, which the operator issues to the production as jobs.
- An operator can monitor the production jobs in Runtime.

#### Requirement

- The TIA Portal project has been created.
- The WinCC Unified PC RT HMI device has been created.
- The plant is configured in the plant view.

#### Configuration in the engineering system (system integrator)

1. To plan your plant, you define a plant structure with plant object types according to ISA-88 type definition.

   - Line
   - Unit
   - Equipment operation
2. You configure units and equipment operations.
3. You configure the controls for the configuration and operator control in Runtime.

   The following controls are available:

   - Recipe control
   - Job overview
   - Job control
   - Material overview

#### Configuration in runtime (technologist)

In the plant, the operator configures the procedures, recipes and materials, the process and relationships in the production in Runtime.

1. You define procedures and recipes in the recipe control.
2. You add units and operations to the procedures and synchronize them.
3. You assign procedures to the recipes.
4. You adjust the recipe data.
5. You define materials and material classes in the material overview.

#### Job assignment and operation in runtime (operator)

In the job overview and job control you plan, create, control and monitor the jobs.

1. You define jobs in the job overview.
2. You start and monitor the jobs in the job overview.
3. You start and monitor the job details in the job control.

### Sequence configuration concept (SES) (RT Unified)

#### Introduction

Configuration with Sequence is divided into the following tasks:

**TIA Portal project**

- Definition of one or more production lines, units and equipment modules
- Creation of screens and screen objects

**HMI Runtime**

![Introduction](images/141002401163_DV_resource.Stream@PNG-de-DE.png)

① Planning and configuration of steps, operations and operation parameters of the equipment module

② Operating and monitoring steps and operations of the equipment module

These tasks are carried out by users with different roles.

- A system integrator creates the visualization of the equipment modules and units in a WinCC project.
- A technologist drafts steps and operations in Runtime.
- On operator can control and monitor the steps and operations in Runtime.

#### Requirement

- The TIA Portal project has been created.
- The WinCC Unified PC RT HMI device has been created.
- The plant is configured in the plant view.

#### Configuration in the engineering system (system integrator)

You prepare the equipment module for your plant using the following steps:

1. You call SES function blocks in the PLC and create instance data blocks.
2. You interconnect the instance data blocks in your program blocks.
3. To plan your plant, you define a plant structure with plant object types according to ISA-88 type definition:

   - Line
   - Unit
   - Equipment module
4. You configure units and equipment modules.
5. You configure the control for configuration and operation of the equipment module in Runtime.

#### Configuration in runtime (technologist)

You configure the equipment module for your plant in the following steps:

1. You define operations and steps.
2. You assign parameters and control elements to the steps.
3. You assign operation parameters to the parameters instead of a static setpoint.
4. You assign steps to the transitions of an operation in order to define the run sequence.
5. You load the operations into the PLC.

#### Operating and monitoring in Runtime (operator)

You monitor and control all operations and their steps that are loaded into the PLC.

### ISA-88 type definition (RT Unified)

Create a plant structure for your project. You can find more information in the manual "Working with plant objects and plant views".

To define the plant structure, you create plant object types according to the ISA-88 type definition.

| Elements of the ISA-88 type definition | Definition | Validation |
| --- | --- | --- |
| None | Is not an element of the ISA-88 type definition. | - |
| Line  (Line) | A grouping of one or more units and associated subordinate groups of modules that are suitable for usage for the creation of a charge. | The line is at a higher level than the unit.   At least one plant object type with ISA-88 type definition "Unit" or "None" must be defined below a line. |
| Unit (LCS)   (Unit) | A grouping of coherent control modules and/or equipment modules and other modules, in which one or more larger processing activities can be executed. | The unit is at a higher level than the equipment operation.   At least one plant object type with ISA-88 type definition "Equipment operation" or "None" must be defined below a unit. |
| Equipment operation (LCS)  (EquipmentOperation) | An operation that is part of the equipment control. | The equipment operation is at a lower level than the unit.   An equipment operation without a higher-level unit is not permitted.   Only plant object types with ISA-88 type definition "None" are permitted below an equipment operation. |
| Unit (SES)   (Unit) | A grouping of coherent control modules and/or equipment modules and other modules, in which one or more larger processing activities can be executed. | The unit is at a higher level than the equipment module.   At least one plant object type with ISA-88 type definition "Equipment module" or "None" must be defined below a unit.  A maximum of three equipment modules are permitted within one unit. |
| Equipment module (SES)   (Equipment Module) | A functional grouping of modules that can execute a finite number of specific smaller processing activities. | The equipment module is at a lower level than the unit.   An equipment module without a higher-level unit is not permitted.   Only plant object types with the ISA-88 type definition "None" are permissible below an equipment module. |

> **Note**
>
> **Control module (Control Module)**
>
> The control module is integrated into the equipment module.

> **Note**
>
> **ISA-88 type definition "None"**
>
> All objects that are not used for LCS or SES have the ISA-88 type definition "None". When a plant object type is created, the ISA-88 type definition "None" is defined by default.

### Procedures, recipes and materials (LCS) (RT Unified)

#### Introduction

The design phase for production processes can be divided into the following steps:

- Design of procedures
- Design of recipes
- Design of materials and material classes

#### Procedure

You describe the method for producing a product in a procedure. You use units, equipment operations and equipment modules to create a procedure. A procedure can contain multiple units of a line.

In the recipe control you define, manage and delete procedures in Runtime.

#### Recipe

You define the quantity of ingredients needed and the values of parameters to be set for production of a product in a recipe.

You define a procedure for each recipe. Recipe operations and formula parameters are derived from the operations defined in the procedure. You define the setpoints of the formula parameters for each recipe operation.

In the recipe control you define, manage and clear recipes in Runtime.

#### Material

You define the end product of a production process as a material.

You combine individual materials of the same type into material classes. For example, the materials "Brown sugar", "White sugar" and "Fructose" belong to the "Sugar" material class.

In the material overview, you define, manage and clear the materials and material classes for the production.

### Jobs (RT Unified)

#### Introduction

The operator of the plant works with jobs. To manufacture a defined quantity of a specific product, a job is created that is composed of a recipe and a quantity specification. You have the option of adjusting the quantity prior the job start. You can start the production jobs either manually or time-controlled.

The operator checks that the jobs are completed without errors and intervenes in the event of an error.

> **Note**
>
> **Active Runtime**
>
> In the following cases, an active HMI Runtime is mandatory to run the jobs:
>
> - Jobs that should start according to a schedule.
> - The job contains synchronization points.

#### Job

You have the option of creating, managing and clearing jobs in the job overview. You can modify jobs before releasing them. As soon as a job is released, a modification is no longer possible and the job can be started.

A job to production is made up of the following components:

| Elements | Description |
| --- | --- |
| Name | The language neutral unique name of the job defines the job. |
| Status | A job can be in different states. |
| Display name | The display name is defined in a language-dependent manner. |
| Job ID | The job ID is unique and sorts the jobs by order of their processing. |
| Recipe name | Assign a previously defined recipe to each job. |
| Quantity | You define the quantity to be produced during the job. |
| Unit of measure | Unit of measure of the defined quantity. |
| Start mode | A job will be started manually or time-controlled. |
| Start time | The start time sorts the jobs chronologically and is relevant for the time-controlled job. |

#### Job status

A job can have one of the following states:

| Status | Description |
| --- | --- |
| Planned | A job has been created. The job can be changed, but it cannot be started yet. |
| Released | This job has been configured and released. The job can no longer be changed. The job can be started or withdrawn. When a job has been withdrawn, it returns to the "Planned" state. |
| Queued | When a job is started and the start unit is occupied by another job or is in "manual mode", the job changes to the "Queued" state. |

#### Job archiving

The Runtime configuration data is saved in an SQLite database or MS SQL database.

#### Job history

When a job is completed, stopped, aborted or cleared, the job is displayed in the job overview in the "Job history" tab.

---

**See also**

[States and transient states (RT Unified)](#states-and-transient-states-rt-unified)

### Steps and operations (SES) (RT Unified)

#### Introduction

The design phase for the sequential production processes can be divided into the following steps:

- Design of steps
- Design of operations
- Design of operation parameters

#### Step

In a step, you define a process that is part of an operation. Each step contains a step enabling condition to the next step. For example, in one step a weighing procedure is configured whose step enabling condition is a specific amount. The amount is determined with a setpoint.

Setpoints can also be set using operation parameters.

You define, manage and delete the steps in Runtime in the SES control in the "Configuration" tab under "Steps".

#### Operation

In an operation, the steps are assigned to transition states and executed.

You define, manage and delete the operations in Runtime in the SES control in the "Configuration" tab under "Operations"

You execute the operations in Runtime in the SES control in the "Monitoring" tab.

You use operations in procedures in the recipe control.

#### Operation parameters

You define, manage and delete the operation parameters in Runtime in the SES control in the "Configuration" tab under "Operations".

### States and transient states (RT Unified)

#### States and transient states of a job

If a job has the "Released" status, you can start the job both in the job overview and in the job control.

In the two controls, the state of the job is displayed in the "Status" column. In the job control, the state of individual parts of the job is displayed in color.

The following diagram shows possible states (grey) and transient states (white) of a job:

![States and transient states of a job](images/141819517323_DV_resource.Stream@PNG-en-US.png)

#### States and transient states of an operation (SES)

Transient states are available for each operation. The configured steps are assigned to the individual transient states. In an operation, at least one step must be assigned to the "Running" transient state. The other transient states are optional.

The following diagram shows possible states (grey) and transient states (white) of an operation:

![States and transient states of an operation (SES)](images/141005580171_DV_resource.Stream@PNG-en-US.png)

The diagram is displayed in the SES control in the "Monitoring" tab. If a transient state is configured, the transient state is displayed in dark blue in the diagram.

#### Interaction of buttons, transient states and states

A state describes the current processing status of a job/operation by the system at a given time. Using the operator controls, you have the option to influence the execution at any time and thus to change the states. Before the job/operation enters a state, it passes through a transition state. The initial state of every operation is the "Idle" state. The initial state of each job is the "Released" state.

The following table shows which states are displayed when the buttons are pressed in the controls:

| Button | Transient state | State | Description |
| --- | --- | --- | --- |
| Start | Starting | - | The transition state is called immediately after the start. When the transient state "Starting" is completed, the "Running" transient state becomes active. |
| - | Running | Completed | In an operation, at least one step must be assigned to the "Running" transient state.   When the transient state "Running" is completed, the "Completing" transient state becomes active.   If the "Completing" transient state is not configured, the transient state "Running" changes directly to the "Completed" state.  In the "Completed" state, a "Reset" is performed internally.   Through resetting, the operation returns to the initial state "Idle" (SES).   The job has been successfully processed and moved to the job history (LCS). |
| - | Completing | Completed | "Completing" is called automatically after completion of the "Running" operation or job and can, for example, be used to shut down the plant.  When the "Completing" transient state is completed, the transient state changes to the "Completed" state.  In the "Completed" state, a "Reset" is performed internally.   Through resetting, the operation returns to the initial state "Idle" (SES).  The job has been successfully processed and moved to the job history (LCS). |
| Pause | Pausing | Paused | When you interrupt the "Running" transient state by pressing the "Pause" button, the "Pausing" transient state becomes active. When the "Pausing" transient state is completed, the transient state changes to the "Paused" state.  If the "Pausing" transient state is not configured, the "Running" transient state changes directly to the "Paused" state. |
| Resume | Resuming | Paused | To leave the "Paused" state, press the "Resume" button. The "Resuming" transient state becomes active. When the "Resuming" transient state is completed, the "Running" transient state becomes active again. The "Running" transient state starts at the step at which it was interrupted.   When the "Resuming" transient state is completed, the "Running" transient state becomes directly active. |
| Hold | Holding | Held | When you interrupt the transient states or states by pressing the "Hold" button, the "Holding" transient state becomes active. When the "Holding" transient state is completed, the transient state changes to the "Held" state.   If the "Holding" transient state is not configured, the state or the transient state changes directly to the "Held" state.  You can interrupt the following transient states and states with the "Hold" button:  - Running - Pausing - Paused - Resuming - Restarting |
| Restart | Restarting | Held | To leave the "Held" state, press the "Restart" button. The "Restarting" transient state becomes active. When the "Restarting" transient state is completed, the "Running" transient state becomes active again. The "Running" transient state restarts from the beginning, at the first step.  When the "Restarting" transient state is not configured, the "Running" transient state becomes directly active. |
| Stop | Stopping | Stopped | When you interrupt the transient states or states by pressing the "Stop" button, the "Stopping" transient state becomes active. When the "Stopping" transient state is completed, the transient state changes to the "Stopped" state.   If the "Stopping" transient state is not configured, the state or the transient state changes directly to the "Stopped" state.  In the "Stopped" state, a "Reset" is performed internally.   Through resetting, the operation returns to the initial state "Idle" (SES).  The job was stopped and moved to the job history (LCS).  You can interrupt the following transient states and states with the "Stop" button:  - Starting - Running - Pausing - Paused - Resuming - Holding - Held - Restarting - Completing |
| Abort | Aborting | Aborted | When you interrupt the transient states or states by pressing the "Abort" button, the "Aborting" transient state becomes active. When the "Aborting" transient state is completed, the transient state changes to the "Aborted" state.   If the "Aborting" transient state is not configured, the state or the transient state changes directly to the "Aborted" state.  In the "Aborted" state, a "Reset" is performed internally.   Through resetting, the operation returns to the initial state "Idle" (SES).  The job was aborted and moved to the job history (LCS).  You can interrupt the following transient states and states with the "Abort" button:  - Starting - Running - Pausing - Paused - Resuming - Holding - Held - Restarting - Stopping - Stopped - Completing |

**State: Error**

An error can occur in each state or transient state. The "Error" state can only be acknowledged with the "Abort" or "Stop" button.

### Status (RT Unified)

In the design in Runtime, you mark defined elements according to three different statuses:

| Icon | Status | Description |
| --- | --- | --- |
| ![Figure](images/129538520971_DV_resource.Stream@PNG-de-DE.png) | Draft | In this status, the element can be changed but cannot be used productively yet. |
| ![Figure](images/129538529803_DV_resource.Stream@PNG-de-DE.png) | Effective | In this status, the element can be used in production. Changes are not possible. |
| ![Figure](images/129547600779_DV_resource.Stream@PNG-de-DE.png) | Withdrawn | In this status, the element has been withdrawn from the production. The element can neither be changed nor used in production. |

The following elements are equipped with a status:

- Materials
- Material classes
- Procedures
- Recipes
- Steps
- Operations

You can change the status manually in Runtime in the controls. If a change has taken place in Engineering, the elements involved are automatically set to "Withdrawn" in Runtime.

**Changes when operation is active**

An operation is executed in the SES control in the "Monitoring" tab. You can simultaneously set the operation or steps to the "Draft" status and make changes in the "Configuration" tab. The operation being executed is not affected by the changes.

The operation can be loaded into the PLC in the status "Effective" only after you have set the elements back to the status "Effective" and if no operation is running. The operation is then displayed in the "Monitoring" tab and can be started with the changes.

## Configuring SES function blocks in the PLC (SES) (RT Unified)

This section contains information on the following topics:

- [Library - Sequence Execution System (SES) (RT Unified)](#library---sequence-execution-system-ses-rt-unified)
- [Unit function block (SES) (RT Unified)](#unit-function-block-ses-rt-unified)
- [Equipment module function blocks (SES) (RT Unified)](#equipment-module-function-blocks-ses-rt-unified)
- [Calling SES function blocks and creating an instance data block (SES) (RT Unified)](#calling-ses-function-blocks-and-creating-an-instance-data-block-ses-rt-unified)

### Library - Sequence Execution System (SES) (RT Unified)

#### Opening the library

The "SES - Sequence Execution System" library is part of the scope of delivery of the SES option package and contains SES function blocks.

To open the library, follow these steps:

1. Open the "Libraries" tab.
2. Expand "Global libraries".
3. Expand the "SES - Sequence Execution System" library.
4. Expand the "Types" folder.

   The SES function blocks are displayed.

#### Function blocks of the SES library

Four function blocks are available in the open library:

- EquipmentModuleLarge
- EquipmentModuleMedium
- EquipmentModuleSmall
- Unit

#### SES PLC data types

The PLC data types in the library in the folder "SES PLC datatypes" are used internally by the four function blocks.

### Unit function block (SES) (RT Unified)

#### Introduction

Before you configure a plant object type as unit, you must call the SES function block "Unit" in a cyclic program. You must call the function block for each unit.

#### Structure overview of the "Unit" function block

![Structure overview of the "Unit" function block](images/134091806347_DV_resource.Stream@PNG-de-DE.png)

### Equipment module function blocks (SES) (RT Unified)

#### Introduction

The library provides you with three function blocks for the equipment module:

- EquipmentModuleSmall
- EquipmentModuleMedium
- EquipmentModuleLarge

#### Comparison table of the function blocks

The function block that you will use depends on how complex your sequential control system is. For example, there is a difference in the number of outputs and the number of executable steps.

**Maximum values for the engineering configuration**

| Property | EquipmentModuleSmall | EquipmentModuleMedium | EquipmentModuleLarge | Description |
| --- | --- | --- | --- | --- |
| Digital inputs/outputs (ports) | 30 | 90 | 160 | Number of the available digital inputs/outputs that can be configured under "Block input/output".  Parameters and control modules share the number of digital outputs. |
| Parameter | 10 | 30 | 60 | Number of parameters (analog inputs/outputs) that can be configured under "Setpoint block input/output". |

Each parameter of an equipment module requires an analog input/output and a digital input/output. Each control module requires only one digital input/output.

The following table shows an example of a possible distribution of parameters:

| Function block | Number of parameters of an equipment module | Number of control modules |
| --- | --- | --- |
| EquipmentModuleSmall | 10 | 20 |
| 0 | 30 |  |
| 5 | 25 |  |
| EquipmentModuleMedium | 30 | 60 |
| 0 | 90 |  |
| 15 | 75 |  |
| EquipmentModuleLarge | 60 | 100 |
| 0 | 160 |  |
| 30 | 130 |  |

**Maximum values for the Runtime configuration**

| Property | EquipmentModuleSmall | EquipmentModuleMedium | EquipmentModuleLarge | Description |
| --- | --- | --- | --- | --- |
| Steps | 50 | 100 | 200 | Number of steps that can be created within an equipment module. |
| Setpoints | 250 | 500 | 1500 | Number of setpoints that can be distributed. |
| Step sequence | 100 | 200 | 500 | Number of steps that can be referenced in all operations. |
| Operation | 10 | 20 | 30 | Number of the operations that can be used for an equipment module. |
| Operation parameters | 10 | 10 | 10 | Number of operation parameters that can be used in an operation. |

#### Structure overview

The structure of the function blocks is identical for all three types. There are differences in the length of the arrays for the parameters.

Example "EquipmentModuleSmall":

![Structure overview](images/143224643467_DV_resource.Stream@PNG-de-DE.png)

**Connection to LCS**

To start an SES operation in a job, the following elements of the unit instance data block must be interconnected with the EquipmentModule function block (see screenshot above):

- automaticStartInformation
- command
- eqmInformation
- jobInformation

The elements of the unit instance data block must have the same port index as specified in the equipment module under "Block input/output of equipment module".

You can find additional information under AUTOHOTSPOT.

#### Input "cmfbonoff" and output "cmcommand"

Input "cmfbonoff" and output "cmcommand" are configured in the editor of the equipment module under "Block input/output". The data type is Bool. Depending on which function block of the equipment module is used, up to 160 parameters can be controlled (see table above).

| Input/output | Description |
| --- | --- |
| cmfbonoff | The status of the inputs [0 ... ] is evaluated in the SES function blocks, dependent on the selected parameter type and the activated "Check" setting. |
| cmcommand | Outputs [0 ... ], which are influenced dependent on the "Set" setting. |

"cmcommand" and "cmfbonoff" have the same port index because the "Block input/output" input field applies to both.

**Example:**

cmcommand[0]

cmfbonoff[0]

Port index "0" is used in this example. To select this port, you enter the number 0 under "Block input/output" in the editor of the equipment module.

#### Input "actualvalue" and output "parametersetpoint"

Input "actualvalue" and output "parametersetpoint" are configured in the editor of the equipment module under "Setpoint block input/output". The data type is Real. Depending on which function block of the equipment module is used, up to 60 parameters can be configured.

**Input "actualvalue"**

The following table shows the output at input "actualvalue", depending on the selected parameter type.

| Parameter types | Input "actualvalue" |
| --- | --- |
| External | If the "Setting" setting is activated in the current step, the actual value of input "actualvalue[x]" is displayed. |
| Counter forwards | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is increased or decreased by the value in "Increment". |
| Counter backwards |  |
| Timer forwards | The input "actualvalue[x]" is irrelevant in this case and is not displayed. The seconds are counted forwards and backwards in "statactualvalue[x]". |
| Timer backwards |  |
| Actual value >= setpoint | Compares the value at input "actualvalue[x]" with the setpoint taking into account the hysteresis. |
| Actual value <= setpoint |  |
| Integrator | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of 1 second and added to the value in "statactualvalue[x]". |
| Integrator with hold | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of "x" milliseconds (variable) and added to the value in "statactualvalue[x]". |

You will find the "Increment" value in the editor of the equipment module.

**Output "parametersetpoint"**

If the "Setting" setting is activated, the setpoint is output at output "parametersetpoint[x]".

"parametersetpoint" and "actualvalue" have the same port index because the "Setpoint block input/output" input field applies to both.

**Example:**

parametersetpoint[1]

actualvalue[1]

Port index "1" is used in this example. To select this port, you enter the number 1 under "Setpoint block input/output" in the editor of the equipment module.

---

**See also**

[Settings for parameters and control modules (SES) (RT Unified)](#settings-for-parameters-and-control-modules-ses-rt-unified)

### Calling SES function blocks and creating an instance data block (SES) (RT Unified)

#### Introduction

The function blocks for unit and equipment module appear with the installation in the global libraries under "SES - Sequence Execution System".

You can find additional information under [Library - Sequence Execution System (SES)](#library---sequence-execution-system-ses-rt-unified)

> **Note**
>
> The SES function blocks are password-protected and cannot be changed.

#### Procedure

To call a function block, follow these steps:

1. Move the SES function block from the global library into the "Program blocks" folder of your created PLC using drag-and-drop.
2. Call the SES function block according to your circumstances

#### Result

An instance data block was created.

## Structuring the plant (RT Unified)

This section contains information on the following topics:

- [Configuration workflows (RT Unified)](#configuration-workflows-rt-unified)
- [Configuring a line (LCS) (RT Unified)](#configuring-a-line-lcs-rt-unified)
- [Configuring an LCS unit (LCS) (RT Unified)](#configuring-an-lcs-unit-lcs-rt-unified)
- [Configuring an SES unit (SES) (RT Unified)](#configuring-an-ses-unit-ses-rt-unified)
- [Configuring an equipment operation (LCS) (RT Unified)](#configuring-an-equipment-operation-lcs-rt-unified)
- [Configuring an equipment module (SES) (RT Unified)](#configuring-an-equipment-module-ses-rt-unified)

### Configuration workflows (RT Unified)

#### Basics

The existing plant structure is the starting point for defining standardized production lines. You map the machines and equipment of your plant in the plant view and define the production processes with the WinCC Unified Line Coordination and WinCC Unified Sequence options.

You configure your production lines in the engineering system with the following steps:

- You create a plant object type for the production line.
- You define, e.g. the components of the production line as plant object types.
- You define the equipment of the plant as plant object types and use the instances in the plant view.

#### Using Sequence

When using sequence, you can create steps and operations. You reuse these elements when coordinating the production line with Line Coordination. Setting synchronization points results in operations that you use in production processes from the operations in Line Coordination. Operations group together several steps between the synchronization points. Via the synchronization points you have the option of interconnecting different units in Line Coordination.

With Sequence you define the units, equipment modules and control modules of your production line in the plant view. In Line Coordination, these plant components are arranged in the node of a line.

#### Using your own data

Besides using Sequence, you have the option of basing your production line on your own function blocks. You define units and equipment operations in Line Coordination that you link with your function blocks.

To configure procedures, you use units and equipment operations in Runtime. You can connect the resulting operations with synchronization lines.

#### Compiling and loading a project

Once you have mapped your plant structure and configured the visualization of the production processes, you compile and download the project.

You can find additional information under [Compiling configuration data and loading it into Runtime](#compiling-configuration-data-and-loading-it-into-runtime-rt-unified)

### Configuring a line (LCS) (RT Unified)

#### Introduction

To map the production line in an object-oriented manner in the plant view, create the production line as a plant object type. You define the created plant object type as a line in accordance with the ISA-88 type definition. You then use the plant object type as a plant object in the plant view.

> **Note**
>
> **Changing the ISA-88 type definition**
>
> If you change the previously set ISA-88 type definition, all previously made settings are lost.

#### Type/instance concept

The line created under "Plant object types" can be used multiple times in the plant view. A line may not be located at a lower level than another line.

If you are using a plant object type in your plant view, an instance (plant object) is generated.

#### Internal member tags

Internal member tags are created when configuring a line.

The following tags are required for reporting and must not be changed:

- @JobIdForLcsReporting
- @JobNameForLcsReporting
- @LineForLcsReporting
- @StartTimeForLcsReporting
- @EndTimeForLcsReporting

The following tags are used for creating, releasing and starting jobs including feedback of LCS Runtime:

- @JobDataForLcsJobOrder
- @JobDataResultForLcsJobOrder

**@JobDataForLcsJobOrder**

With this tag you can create, release and start a job via a string in the job overview. The string has the following elements:

| Element | Description |
| --- | --- |
| JobName | - Describes the object name of the job to be processed. - The object name is also used as display name. - The value of the string must be unique and not empty. |
| RecipeName | - Describes the object name of the recipe that is used in the job. - The recipe must be in the "Effective" status. - The value of the string must be unique and not empty. |
| JobQuantity (optional) | - Describes the quantity of the job. - The Real value or Int value must be within the minimum value and maximum value of the procedure. - When the job quantity is missing, the standard quantity is used. |
| JobCommand | The "Start" command must be specified to create, release and start the job. |
| JobParameter (optional) | - A list of the object names of the job parameters (complete path) and value can be specified. - The job parameter name describes the object name and must not be empty. - The job parameter value describes the setpoint and must not be empty. - The job parameter value must match the job parameter type (INT to REAL is accepted). - The job parameter value must be within the minimum value and maximum value. |

**Example:**

This example shows the structure of the string:

`{`

`"JobName" : "Job1",`

`"RecipeName" : "Bread",`

`"JobQuantity" : "100",`

`"JobCommand" : "Start",`

`"JobParameter" :`

`{`

`"Temperature" : "30",`

`"Milk" : "400"`

`}`

`}`

> **Note**
>
> Only one job at a time can be created with the script.

**@JobDataResultForLcsJobOrder**

LCS Runtime uses this tag to signal the result of the job. The following messages are possible:

| Messages | Description |
| --- | --- |
| Job <JobName> was successfully started | The job was successfully started. |
| Job not started – Job data string format error | The job was not started. Error in the string format. |
| Job <JobName> not started – Duplicate Job Name | The job was not started. The job name already exists. |
| Job <JobName> not started - Recipe not found | The job was not started. The recipe was not found or is not in the "Effective" status. |
| Job <JobName> not started – Unknown JobCommand | The job was not started. Unknown command. |
| Job <JobName> not started – Job quantity out of range | The job was not started. The job quantity is out of range. |
| Job <JobName> not started – Job parameter <Job parameter name> value out of range | The job was not started. Job parameter value is out of range. |
| Job <JobName> not started – Job parameter <Job parameter name> name not found | The job was not started. Job parameter value was not found. |
| Job <JobName> not started – Job parameter <Job parameter name> type does not fit | The job was not started. Job parameter type does not match. |
| MaxJobLimitError | No new job was created. The maximum number of 1000 planned, released or active jobs has been reached. |

> **Note**
>
> A new string can only be created when a job has been started successfully. After the execution of the script, the "@JobDataForLcsJobOrder" tag is not reset.

#### Requirement

- A plant object type has been created.

#### Procedure

Proceed as follows to configure a plant object type as a line:

1. In the "Plant object types" task card, double-click on the plant object type.

   Alternatively, select "Open" in the shortcut menu of the plant object type.
2. Select the "SES / LCS" tab.
3. Select "Line" under "ISA-88 type definition" on the "SES / LCS" tab.

   The internal members are created automatically in the "Interface" tab.
4. Move the plant object type into your plant view using drag-and-drop.

**Note**

When the internal members are not fully displayed, close the plant object type and open the plant object type again.

### Configuring an LCS unit (LCS) (RT Unified)

#### Introduction

To map the unit in an object-oriented manner in the plant view, create the unit as a plant object type. You define the created plant object type as a "unit" in accordance with the ISA-88 type definition. You then use the plant object type as a plant object in the plant view.

> **Note**
>
> **Changing the ISA-88 type definition**
>
> If you change the previously set ISA-88 type definition, all previously made settings are lost.

#### Type/instance concept

The unit created under "Plant object types" can be used multiple times in the plant view.

If you are using a plant object type in your plant view, an instance (plant object) is generated.

**Type**

You define the following properties in the plant object type:

- Tag for job ID
- Tag for process mode

#### Requirement

- A plant object type has been created.
- In the PLC, the unit function block is called in a cyclic program with at least the following parameters:

  | Parameter | Type | Description |
  | --- | --- | --- |
  | Job ID | DInt | When a job is started in Runtime, LCS writes the job ID of the started job to the tag of the instance data block.  The parameter can be an input or in/out and is written by the Runtime. |
  | Process mode | Bool | 0 = Manual  1 = Automatic  A job can only be started when the process mode is set to "Automatic".  The parameter can be an output, in/out or static parameter. |

#### Procedure

Proceed as follows to configure a plant object type as a unit:

1. In the "Plant object types" task card, double-click on the plant object type.

   Alternatively, select "Open" in the shortcut menu of the plant object type.
2. Select the "Interface" tab.
3. Under "Communication driver", select your "SIMATIC S7 1200/1500" PLC.
4. Select the unit function block under "PLC tag".
5. Select "Unit" under "ISA-88 type definition" of the "SES / LCS" tab.
6. Under "Job ID" and "Process mode", select the input/output on the function block.
7. Using a drag-and-drop operation, move the plant object type into your plant view below the line.

   A plant object is created.
8. Double-click to open the created plant object in the plant view.

   Alternatively, select "Open" in the shortcut menu of the plant object.
9. Select the "Interface" tab.
10. Under "PLC tag", select the instance data block of the previously interconnected function block.

### Configuring an SES unit (SES) (RT Unified)

#### Introduction

To map the unit in an object-oriented manner in the plant view, create the unit as a plant object type. You define the created plant object type as a "unit" in accordance with the ISA-88 type definition. You then use the plant object type as a plant object in the plant view.

> **Note**
>
> **Changing the ISA-88 type definition**
>
> If you change the previously set ISA-88 type definition, all previously made settings are lost.

#### Type/instance concept

The unit created under "Plant object types" can be used multiple times in the plant view.

If you are using a plant object type in your plant view, an instance (plant object) is generated.

#### Requirement

- A plant object type has been created.
- In the PLC, the unit function block is called in the program.

#### Procedure

> **Note**
>
> **Compliance with the sequence**
>
> To configure the unit correctly, it is essential that you follow the sequence of the procedure.

Proceed as follows to configure a plant object type as a unit:

1. In the "Plant object types" task card, double-click on the plant object type.

   Alternatively, select "Open" in the shortcut menu of the plant object type.
2. Select the "Interface" tab.
3. Select the "SIMATIC S7 1200/1500" PLC under "Communication driver".
4. Select the unit function block under "PLC tag".

   The ISA-88 type definition "Unit" is selected automatically on the "SES / LCS" tab.
5. Using a drag-and-drop operation, move the plant object type into your plant view below the line.
6. Double-click to open the created plant object in the plant view.

   Alternatively, select "Open" in the shortcut menu of the plant object.
7. Select the "Interface" tab.
8. Under "PLC tag", select the instance data block of the previously interconnected function block.

### Configuring an equipment operation (LCS) (RT Unified)

#### Introduction

To map the equipment operation in an object-oriented manner in the plant view, create the equipment operation as a plant object type. You define the created plant object type as an "equipment operation" in accordance with the ISA-88 type definition. You then use the plant object type as a plant object in the plant view.

> **Note**
>
> **Changing the ISA-88 type definition**
>
> If you change the previously set ISA-88 type definition, all previously made settings are lost.

In the equipment operation, you define the commands and states for executing a procedure. You also define the operation parameters.

| Parameter | Description |
| --- | --- |
| Commands | If a command is given in Runtime, e.g. by pressing the Start button, the configured value is written to the associated tag. The combination of value and tag must be unique.  The value 0 cannot be used because 0 is the start value in the instance data block. |
| Status | Feedback to LCS Runtime indicating the status of the process.   For each status, a combination of value, mask and tag must be entered, which must be unique. The mask hides values that are not relevant to LCS. The value and the mask are logically linked with AND bit-by-bit. |
| Operation parameters | You use operation parameters to define parameters for recipe operations. Each operation parameter describes an actual value and setpoint that is used in a recipe operation. When an equipment operation is created, you define the following properties of the operation parameters:  - Setpoint - Actual value (data type must be identical to the data type of the setpoint) - Default value - Minimum value - Maximum value - Unit of measure   You can adjust the setpoint for each recipe operation in Runtime and draft recipe formulas in this way. You thus have the option of using operations in various recipes. |

> **Note**
>
> **Setpoint of formula parameters**
>
> Note the following information when defining operation parameters:
>
> - If the setpoints of the formula parameters are changed in Runtime, the changes are retained the next time Runtime is loaded.
> - If a setpoint that was changed in Runtime is outside the range configured in the engineering system when Runtime is completely loaded again, the status of the recipe is changed to "Withdrawn". The setpoint involved is marked in red in Runtime.

#### Type/instance concept

The equipment operation created under "Plant object types" can be used multiple times in the plant view.

If you are using a plant object type in your plant view, an instance (plant object) is generated.

You define the following properties in the plant object type:

- Values and tags for commands
- Values, masks and tags for status
- Operation parameters

  - Setpoint
  - Actual value
  - Default value
  - Minimum value
  - Maximum value
  - Unit of measure

**Instance**

In the plant object, you can change the following properties if required:

- Operation parameters

  - Default value
  - Minimum value
  - Maximum value

#### Requirement

- A plant object type has been created.
- In the PLC, a function block is called in a cyclic program with at least the following parameters:

  | Parameter | Type | Description |
  | --- | --- | --- |
  | Command | Bool, Int, DInt | LCS writes the value to the tag of the instance data block.  The tag is written by the Runtime. |
  | Status | Byte, Word, DWord | LCS writes the value to the tag of the instance data block.  The tag is read by the Runtime.  The parameter can be an output, in/out or static parameter. |

#### Procedure

Proceed as follows to configure a plant object type as an equipment operation:

1. In the "Plant object types" task card, double-click on the plant object type.

   Alternatively, select "Open" in the shortcut menu of the plant object type.
2. Select the "Interface" tab.
3. Select the "SIMATIC S7 1200/1500" PLC under "Communication driver".
4. Select the EquipmentModule function block under "PLC tag".
5. Select "Equipment operation" under "ISA-88 type definition" in the "SES / LCS" tab.
6. Specify the values under "Commands" and assign the configured tags.

   Each line must be filled out.
7. Specify the values and masks under "Status" and assign the configured tags.

   Each line must be filled out.
8. Create all needed operation parameters.
9. Assign the "Setpoint" and "Current value" for each operation parameter.

   "Setpoint" and "Current value" must be specified.
10. If necessary, define the properties of the operation parameter.

    Operation parameters can be deleted via the shortcut menu of the respective parameter.
11. Using a drag-and-drop operation, move the plant object type into your plant view below the line.
12. Double-click to open the created plant object in the plant view.

    Alternatively, select "Open" in the shortcut menu of the plant object.
13. Select the "Interface" tab.
14. Under "PLC tag", select the instance data block of the previously interconnected function block.

### Configuring an equipment module (SES) (RT Unified)

This section contains information on the following topics:

- [Configuring an equipment module (SES) (RT Unified)](#configuring-an-equipment-module-ses-rt-unified-1)
- [Setting parameters (SES) (RT Unified)](#setting-parameters-ses-rt-unified)

#### Configuring an equipment module (SES) (RT Unified)

##### Introduction

To map the equipment module in an object-oriented manner in the plant view, create the equipment module as a plant object type. You define the created plant object type as an "equipment module" according to the ISA-88 type definition. You then use the plant object type as a plant object in the plant view.

> **Note**
>
> **Changing the ISA-88 type definition**
>
> If you change the previously set ISA-88 type definition, all previously made settings are lost.

##### Type/instance concept

The equipment module created under "Plant object types" can be used multiple times in the plant view.

If you are using a plant object type in your plant view, an instance (plant object) is generated.

**Type**

You define the following properties in the plant object type:

- Parameter
- Control modules and lower-level parameters

You can find additional information under [Setting parameters (SES)](#setting-parameters-ses-rt-unified)

**Instance**

You define the following properties in the plant object:

- Equipment module block input/output

  A maximum of three equipment modules may be subordinated to a unit. Enter a value between 0 and 2.

##### Requirement

- A plant object type has been created.
- A function block of type "EquipmentModuleSmall", "EquipmentModuleMedium" or "EquipmentModuleLage" is called in a program block in the PLC.

##### Procedure

Proceed as follows to configure a plant object type as an equipment module:

1. In the "Plant object types" task card, double-click on the plant object type.

   Alternatively, select "Open" in the shortcut menu of the plant object type.
2. Select the "Interface" tab.
3. Select the "SIMATIC S7 1200/1500" PLC under "Communication driver".
4. Select the EquipmentModule function block under "PLC tag".

   The ISA-88 type definition "Equipment module" is selected automatically on the "SES / LCS" tab.
5. Move the plant object type into your plant view below the SES unit using a drag-and-drop operation.
6. Double-click to open the created plant object in the plant view.

   Alternatively, select "Open" in the shortcut menu of the plant object.
7. Select the "Interface" tab.
8. Under "PLC tag", select the instance data block of the previously interconnected function block.
9. Open the "SES / LCS" tab.
10. Enter a value between 0 and 2 under "Equipment module block input/output".

#### Setting parameters (SES) (RT Unified)

##### Introduction

You can add parameters and configure control modules within an equipment module. You group digital parameters whose conditions are closed in a control module. The control module has a digital interface that can also be interconnected in the process.

Depending on which SES function block is used, up to 160 inputs and outputs are permitted within an equipment module. Control modules and parameters share these inputs and outputs.

You can find additional information under [Equipment module function blocks (SES)](#equipment-module-function-blocks-ses-rt-unified)

> **Note**
>
> **Copying, pasting and deleting**
>
> The "Copy", "Paste" and "Delete" functions can be used within the equipment module editor.
>
> For this you select the desired range in the editor and choose the function via the shortcut menu. You can also use the usual keyboard shortcuts.

##### Editor

| Column header | Description |
| --- | --- |
| Name | Give the parameter a name. |
| Type | Select the parameter type from a list. |
| Comment | Describe the parameter. |
| Display name | Assign a language-dependent display name for the parameter. The display name is visible in Runtime. |
| Block input/output | The output "cmcommand" and the input "cmfbonoff" are assigned to a port index. |
| Setpoint block input/output | The output "parametersetpoint" and the input "actualvalue" are assigned to a port index. |
| Unit of measurement | Assign a unit of measurement for your setpoint, for example, kg. |
| Increment | Value that is relevant for the following parameter types:  - Counter forwards - Counter backwards - Integrator - Integrator with hold   Depending on the parameter type, a value is increased, decreased or multiplied by the value.  The type of the column is a floating-point number. |
| Low limit | Low limit of the parameter. The type of the column is a floating-point number. |
| High limit | High limit of the parameter. The type of the column is a floating-point number. |
| Hysteresis | Tolerance range for parameter type "Actual value >= setpoint" and "Actual value <= setpoint". The tolerance range is subtracted for "Actual value >= setpoint" and added for "Actual value <= setpoint".  The type of the column is a floating-point number. |

##### Parameter types

| Parameter types | Description |
| --- | --- |
| External | If the "Setting" setting is activated, the actual value of input "actualvalue[x]" is displayed. |
| Counter forwards | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is increased or decreased by the value in "Increment". |
| Counter backwards |  |
| Timer forwards | The input "actualvalue[x]" is irrelevant in this case and is not displayed. The seconds are counted forwards and backwards in "statactualvalue[x]". |
| Timer backwards |  |
| Actual value >= setpoint | Compares the value at input "actualvalue[x]" with the setpoint taking into account the hysteresis. |
| Actual value <= setpoint |  |
| Integrator | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of 1 second and added to the value in "statactualvalue[x]". |
| Integrator with hold | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of "x" milliseconds (variable) and added to the value in "statactualvalue[x]". |

##### Procedure

1. In the "Plant object types" task card, double-click on equipment module.

   Alternatively, select "Open" in the shortcut menu of the equipment module.
2. Open the "SES / LCS" tab.
3. Under "Parameters", click <Add new parameter> in the "Name" column.
4. Assign a name and a display name.
5. Set your settings.
6. Under "Control module", click <Add new control module> in the "Name" column.
7. Assign a name and a display name.
8. Set your settings.

## Configuring the controls (RT Unified)

This section contains information on the following topics:

- [Configuring the recipe view (LCS) (RT Unified)](#configuring-the-recipe-view-lcs-rt-unified)
- [Configuring the job overview (LCS) (RT Unified)](#configuring-the-job-overview-lcs-rt-unified)
- [Configuring the job control (LCS) (RT Unified)](#configuring-the-job-control-lcs-rt-unified)
- [Configuring the material overview (LCS) (RT Unified)](#configuring-the-material-overview-lcs-rt-unified)
- [Configuring the SES control (SES) (RT Unified)](#configuring-the-ses-control-ses-rt-unified)
- [Setting up access control for LCS controls (LCS) (RT Unified)](#setting-up-access-control-for-lcs-controls-lcs-rt-unified)
- [Setting up access control for SES control (SES) (RT Unified)](#setting-up-access-control-for-ses-control-ses-rt-unified)

### Configuring the recipe view (LCS) (RT Unified)

#### Introduction

With the recipe control you create and manage procedures and recipes for your production line.

![Introduction](images/134163365003_DV_resource.Stream@PNG-en-US.png)

With the installation, the recipe control is included under "My Controls" in the "Toolbox" task card.

![Introduction](images/138351809931_DV_resource.Stream@PNG-de-DE.png)

#### Layout

You change the settings for the position, geometry, style, color, and font of the control in the Inspector window. You can adapt the following properties in particular:

- Window settings: Specifies which window elements are displayed.
- Text format: Determines the font type and size.
- Under interface:

  - Plant object: Assign configured line
  - Read: Assigning a function right
  - Write: Assigning a function right

    You can find additional information under [Setting up access control for LCS controls (LCS)](#setting-up-access-control-for-lcs-controls-lcs-rt-unified).

#### Requirement

- An HMI device is assigned to the plant view.
- A production line is created in the plant view.
- A screen is configured and open.

#### Assign configured line

To be able to create recipes and procedures for a line, assign the relevant plant object to the recipe control in the Inspector window.

1. Using drag-and-drop, move the recipe control from the "Toolbox" task card onto the screen.
2. In the Inspector window, expand the "Properties > Properties > Miscellaneous" group.
3. Under "Interface", click on the selection button in the "Static value" column.

   The selection dialog opens.
4. Select a configured line and confirm the selection.

   The selected plant object has been added under "Plant object".

   This value must be selected statically and cannot be dynamized.

> **Note**
>
> A separate recipe control must be used for each line configured in the plant view.

### Configuring the job overview (LCS) (RT Unified)

#### Introduction

With the job overview you obtain an overview of the planned and running production jobs.

![Introduction](images/134163819659_DV_resource.Stream@PNG-en-US.png)

The job overview appears with the installation in the "Toolbox" task card under "My Controls".

![Introduction](images/138349776139_DV_resource.Stream@PNG-de-DE.png)

#### Layout

You change the settings for the position, geometry, style, color, and font of the control in the Inspector window. You can adapt the following properties in particular:

- Window settings: Specifies which window elements are displayed.
- Text format: Determines the font type and size.
- Under interface:

  - Plant object: Assign configured line
  - Job Companion Control: Connection with the job control
  - Read: Assigning a function right
  - Operate: Assigning a function right
  - Write: Assigning a function right

    You can find additional information under [Setting up access control for LCS controls (LCS)](#setting-up-access-control-for-lcs-controls-lcs-rt-unified).

#### Requirement

- An HMI device is assigned to the plant view.
- A production line is created in the plant view.
- A screen is configured and open.

#### Assign configured line

To manage jobs for a line, assign the relevant plant object to the job overview in the Inspector window.

1. Using a drag-and-drop operation, move the job overview from the "Toolbox" task card onto the screen.
2. In the Inspector window, expand the "Properties > Properties > Miscellaneous" group.
3. Under "Interface", click on the selection button in the "Static value" column.

   The selection dialog opens.
4. Select a configured line and confirm the selection.

   The selected plant object has been added under "Plant object".

   This value must be selected statically and cannot be dynamized.

> **Note**
>
> A separate job overview must be used for each line configured in the plant view.

### Configuring the job control (LCS) (RT Unified)

#### Introduction

With the job control you check the sequence of a job in graphic form. In the "Job monitoring" area, you see the production processes of the individual units.

You configure the job control in the same screen in which you configured the job overview. For referencing the currently selected job, configure the connection between the job control and the job overview.

![Introduction](images/134369977867_DV_resource.Stream@PNG-en-US.png)

The job control appears with the installation in the "Toolbox" task card under "My Controls".

![Introduction](images/138349089163_DV_resource.Stream@PNG-de-DE.png)

#### Layout

You change the settings for the position, geometry, style, color, and font of the control in the Inspector window. You can adapt the following properties in particular:

- Window settings: Specifies which window elements are displayed.
- Text format: Determines the font type and size.
- Under interface:

  - Read: Assigning a function right
  - Operate: Assigning a function right
  - Write: Assigning a function right

    You can find additional information under [Setting up access control for LCS controls (LCS)](#setting-up-access-control-for-lcs-controls-lcs-rt-unified).

#### Requirement

- A screen is configured and open.
- The job overview is configured in a screen.
- The job overview is assigned to a production line.

#### Connect job control with job overview

To check the sequence of a job in Runtime, use the control in a screen.

1. Drag the job control from the "Toolbox" task card onto the screen.
2. Copy the name of the job control.
3. Select the job overview.
4. Open the "Interface" group in the Inspector window under "Miscellaneous".
5. Under "Job Companion Control", insert the name of the job control, for example, "Job control_1".

### Configuring the material overview (LCS) (RT Unified)

#### Introduction

With the material overview you configure and manage the materials that you use for production.

The control functions like a database, independently of the configured plant objects. Materials and material classes are created and configured in Runtime.

![Introduction](images/134174932107_DV_resource.Stream@PNG-en-US.png)

With the installation, the material overview is included under "My Controls" in the "Toolbox" task card.

![Introduction](images/138351818507_DV_resource.Stream@PNG-de-DE.png)

#### Layout

You change the settings for the position, geometry, style, color, and font of the control in the Inspector window. You can adapt the following properties in particular:

- Window settings: Specifies which window elements are displayed.
- Text format: Determines the font type and size.
- Under interface:

  - Read: Assigning a function right
  - Write: Assigning a function right

    You can find additional information under [Setting up access control for LCS controls (LCS)](#setting-up-access-control-for-lcs-controls-lcs-rt-unified).

#### Requirement

- A screen is configured and open.

#### Procedure

To create the materials and material classes in Runtime, use the control in a screen.

1. Drag the material overview from the "Toolbox" task card onto the screen.
2. In the Inspector window, change the desired settings.

### Configuring the SES control (SES) (RT Unified)

#### Introduction

With the SES control, you create and manage the steps and operations of an equipment module. You monitor and control the operations.

![Introduction](images/144993862667_DV_resource.Stream@PNG-en-US.png)

With the installation, the SES control is displayed under "My Controls" in the "Toolbox" task card.

![Introduction](images/138349081227_DV_resource.Stream@PNG-de-DE.png)

#### Layout

You change the settings for the position, geometry, style, color, and font of the control in the Inspector window. You can adapt the following properties in particular:

- Window settings: Specifies which window elements are displayed.
- Text format: Determines the font type and size.
- Under interface:

  - Plant object: Assign configured equipment module
  - Read: Assigning a function right
  - Operate: Assigning a function right
  - Write: Assigning a function right

    You can find additional information under [Setting up access control for SES control (SES)](#setting-up-access-control-for-ses-control-ses-rt-unified).

#### Requirement

- An HMI device is assigned to the plant view.
- A production line is created in the plant view.
- A screen is configured and open.

#### Assign configured equipment module

To create steps and operations for an equipment module, use the control in a screen. This procedure is optional, you can also open the equipment module directly in Runtime in the control.

1. Using drag-and-drop, move the SES control from the "Toolbox" task card onto the screen.
2. In the Inspector window, expand the "Properties > Properties > Miscellaneous" group.
3. Under "Interface > Plant objects", click the selection button in the "Static value" column.

   The selection dialog opens.
4. Select a configured equipment module and confirm the selection.

### Setting up access control for LCS controls (LCS) (RT Unified)

#### Introduction

You can set up access control for the individual LCS controls. You do this to determine the rights the runtime user gets in the respective control. To do this, you can assign pre-defined or user-specific Runtime rights to the properties "Read", "Write" or "Operate".

*The "Operate" property is only available in the job overview and job control.

| Property | Description |
| --- | --- |
| Read | Read right  All data in the control is displayed to the runtime user with this right. The runtime user can select all tabs, but cannot make any changes or perform any operations. |
| Write | Write rights  With this right, the runtime user can make all changes and operations, e.g. change the configuration data and start jobs. In order to be able to perform the above-mentioned operations and changes, the runtime user also needs the read right. |
| Operate | Operating right*  With this right, the runtime user can operate the following buttons:  - Start - Pause - Hold - Resume - Restart   The runtime user can additionally change the setpoints of the formula parameters. In order to be able to perform the operations and changes listed above, the runtime user also requires the read right. |

If no function right is assigned to a property, all runtime users have the right.

#### Function rights of the runtime user

| Read | Write | Operate* | Function rights of the runtime user |
| --- | --- | --- | --- |
| X | X / ✓ | X / ✓ | **"Know-how protection"**   User has no rights. No data is displayed in the control. |
| ✓ | X | X | User has only read rights. |
| ✓ | ✓ | X / ✓ | User has read and write rights. |
| ✓ | X | ✓ | User has read rights and operating rights*. |

**Legend:**

X = The runtime user does not have the function right that is set in the property.

✓ = The runtime user has the function right that is set in the property.

Or the property is empty.

#### Requirement

- In the security settings, you have configured "Users and roles" in accordance with your needs.

  You can find more information in the section "Configuring users and roles" in the WinCC Unified help.
- The "Allow operator control" option is activated in the control properties under "Security".
- The "Authorization" option is empty in the control properties under "Security".
- The "Require explicit unlock" option is disabled under the "Read", "Write" and "Operate" property in the control properties under "Properties > Miscellaneous > Interface".

  This control property is for multipoint touch displays and is not supported in V17.

#### Procedure

1. Select the desired control in the screen.
2. Expand the property "Read", "Write" or "Operate" under "Properties > Miscellaneous > Interface".
3. Expand the drop-down list in the "Static value" column under "Authorization".

   The function rights are displayed.
4. Select a function right.
5. If necessary, repeat steps 2-4 to configure the additional properties.

### Setting up access control for SES control (SES) (RT Unified)

#### Introduction

You can set up access control for the SES control. With this, you determine which rights the runtime user gets in the SES control. To do this, you can assign pre-defined or user-specific Runtime rights to the properties "Read", "Write" or "Operate".

| Property | Description |
| --- | --- |
| Read | Read right  With this right, the runtime user can view the control configurations. For example, the user can switch between the individual tabs. The user cannot perform any operations with read rights. |
| Write | Write rights  With this right, the runtime user can operate the control. The user can, for example, create and configure steps and operations, execute operations and perform an import/export. The user needs read rights in addition. |
| Operate | Operating rights for the following buttons in the "Monitoring" tab:  - Automatic/Manual mode - Pause - Hold   All other buttons in the "Monitoring" tab cannot be operated. Operation is not possible in the "Configuration" tab. The user needs read rights in addition. |

If no function right is assigned to a property, all runtime users have the right.

#### Function rights of the runtime user

| Read | Write | Operate | Function rights of the runtime user |
| --- | --- | --- | --- |
| X | X / ✓ | X / ✓ | **"Know-how protection"**   User has no rights. No data is displayed in the control. |
| ✓ | X | X | User has only read rights. |
| ✓ | ✓ | X / ✓ | User has read and write rights. |
| ✓ | X | ✓ | User has read rights and operating rights. |

**Legend:**

X = The runtime user does not have the function right that is set in the property.

✓ = The runtime user has the function right that is set in the property.

Or the property is empty.

#### Requirement

- In the security settings, you have configured "Users and roles" in accordance with your needs.

  You can find more information in the section "Configuring users and roles" in the WinCC Unified help.
- The "Allow operator control" option is activated in the control properties under "Security".
- The "Authorization" option is empty in the control properties under "Security".
- The "Require explicit unlock" option is disabled under the "Read", "Write" and "Operate" property in the control properties under "Properties > Miscellaneous > Interface".

  This control property is for multipoint touch displays and is not supported in V17.

#### Procedure

1. Select the desired control in the screen.
2. Expand the property "Read", "Write" or "Operate" under "Properties > Miscellaneous > Interface".
3. Expand the drop-down list in the "Static value" column under "Authorization".

   The function rights are displayed.
4. Select a function right.
5. If necessary, repeat steps 2-4 to configure the additional properties.

## Compiling configuration data and loading it into Runtime (RT Unified)

### Introduction

There are two different procedures for obtaining configuration data in Runtime. The procedures depend on the type of change you have made.

1. Complete download

   If no Runtime data has been loaded yet, only a complete download is possible.
2. Delta compile and delta download

   As of the second compile and download, you can select the Delta mode. This means that only the modified data is compiled and transferred. Runtime is not terminated with this procedure and remains active. You can run delta compile several times before you initiate a delta download.

   If you want to load the data into Runtime directly after the configuration change, it is sufficient to start a delta download, because a delta compile is implicitly performed.

### Configuration changes to LCS data and SES data

Not all configuration changes can be compiled and downloaded in delta mode. The following table shows you the changes to the LCS data and SES data for which delta compile and delta download are possible:

| Element | Delta download capability | No delta download capability |
| --- | --- | --- |
| LCS plant object | **Equipment operation**   Value change in the "Operation parameters" area:  - Default value - Minimum value - Maximum value | General:  - Create, rename or delete - Copy and paste - Move within the plant view - Exchange instance data block |
| SES plant object | **Equipment module**   Value changes in the "Parameters" area:  - Increment - Low limit - High limit - Hysteresis     "Equipment module configuration > Equipment module block input/output" area:  - Change value |  |
| LCS plant object type | **Unit**   Assign new tag:  - Job ID - Process mode      **Equipment operation**   "Commands" area:  - Change values - Change tags     "Status" area:  - Change values - Change mask - Change tags     "Operation parameters" area:  - Changing an existing parameter - Creating a new parameter - Delete existing parameter | In general, if an instance of the plant object type exists:  - Change an ISA-88 type definition - Exchange function block - Rename or delete |
| SES plant object type | **Equipment module**   "Parameters" area:  - Changing an existing parameter - Creating a new parameter - Delete existing parameter     "Control module" area:  - Change existing control module - Create new control module - Delete existing control module - Change existing parameters within a control module - Create a new parameter within a control element - Clear existing parameters within a control element |  |
| LCS controls | - Assign or change a line in the properties of the recipe control or job overview. - Assigning or changing the function rights. | - |
| SES control | - Assign or change an equipment module in the properties of the SES control. - Assigning or changing the function rights. |  |

### Messages during compilation

When messages occur during compilation of the project and you subsequently change the user interface language, some of these messages are not switched immediately to the new language. Compile again to display the messages in the new language.

### Effects on the active RT project

Active Runtime is not terminated by delta download. The changes are applied immediately in the active RT project. Steps, operations, procedures and recipes are set to the status "Withdrawn" if they contain changed RT data. Existing jobs are not affected regardless of their status.

## Validation of the configuration of plant objects (RT Unified)

### Introduction

If validation errors in the plant view, missing or faulty properties of plant objects or plant object types have arisen, these errors are displayed during compilation. With the "Go to" function, you have the possibility to jump directly to the error location and eliminate the error immediately.

In addition, the number of plant objects (instances) used is displayed during compilation. This information helps you to decide which RT licenses you need and how many.

### Solve causes of errors during validation

1. Navigate in the Inspector window to "Info > Compile".
2. ![Solve causes of errors during validation](images/122765203595_DV_resource.Stream@PNG-de-DE.png) Set the filter so that error messages are displayed.

   If a green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png) is displayed in the "Go to" column for a message, you can go directly to the appropriate tab for correcting the cause of the alarm.
3. Select the green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png).

   The tab in which corrections are expected is displayed. The corresponding property is selected.

### Showing the number of plant objects (instances)

The quantities of the following instances that are defined as ISA-88 type definitions and used in the plant view are displayed under "Info > Compile" in the Inspector window:

- Instances of LCS units
- Instances of SES units
- Instances of the equipment modules

If no instances exist, the count is not displayed in the Inspector window.

## Configuring and operating production processes in Runtime (RT Unified)

This section contains information on the following topics:

- [Procedures and recipes (LCS) (RT Unified)](#procedures-and-recipes-lcs-rt-unified)
- [Jobs (LCS) (RT Unified)](#jobs-lcs-rt-unified)
- [Materials (LCS) (RT Unified)](#materials-lcs-rt-unified)
- [Steps and operations (SES) (RT Unified)](#steps-and-operations-ses-rt-unified-1)

### Procedures and recipes (LCS) (RT Unified)

This section contains information on the following topics:

- [Operating the recipe view (LCS) (RT Unified)](#operating-the-recipe-view-lcs-rt-unified)
- [Creating and managing procedures (LCS) (RT Unified)](#creating-and-managing-procedures-lcs-rt-unified)
- [Configuring procedures (LCS) (RT Unified)](#configuring-procedures-lcs-rt-unified)
- [Synchronizing recipe operations (LCS) (RT Unified)](#synchronizing-recipe-operations-lcs-rt-unified)
- [Using SES units and SES operations in a procedure (SES) (RT Unified)](#using-ses-units-and-ses-operations-in-a-procedure-ses-rt-unified)
- [Creating and managing recipes (LCS) (RT Unified)](#creating-and-managing-recipes-lcs-rt-unified)
- [Configuring recipes (LCS) (RT Unified)](#configuring-recipes-lcs-rt-unified)
- [Scaling setpoints (LCS) (RT Unified)](#scaling-setpoints-lcs-rt-unified)
- [Exporting procedures and recipes (LCS) (RT Unified)](#exporting-procedures-and-recipes-lcs-rt-unified)
- [Importing procedures and recipes (LCS) (RT Unified)](#importing-procedures-and-recipes-lcs-rt-unified)
- [Delete Runtime configuration data (LCS) (RT Unified)](#delete-runtime-configuration-data-lcs-rt-unified)

#### Operating the recipe view (LCS) (RT Unified)

##### Use

With the recipe control you create and manage procedures and recipes for your production line. You choose between 3 tabs in the recipe control.

The column width is adjustable. After a screen change or a browser update, the column width returns to its default size.

##### "Overview" tab

In the "Overview" tab, you create, edit and delete recipes and procedures. You define attributes such as names and quantities for the individual elements. To change the sorting order, click on the respective symbol in the desired column. The texts are sorted in alphabetical order, numbers are sorted by size.

You switch between the recipe list and procedure list to see all elements at a glance.

!["Overview" tab](images/134168829835_DV_resource.Stream@PNG-en-US.png)

**Operator controls**

| Button | Name | Function |
| --- | --- | --- |
| !["Overview" tab](images/111307899787_DV_resource.Stream@PNG-de-DE.png) | Add | Creates a new entry. |
| !["Overview" tab](images/111307908363_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected entry. |
| !["Overview" tab](images/133626352523_DV_resource.Stream@PNG-de-DE.png) | Export | Exports all procedures and recipes created in the recipe control regardless of their status. |
| !["Overview" tab](images/133626361099_DV_resource.Stream@PNG-de-DE.png) | Import | Imports all procedures and recipes from a file. |
| !["Overview" tab](images/143224651403_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes all Runtime configuration data from the control and from the LCS recipe service. |
| !["Overview" tab](images/111308027915_DV_resource.Stream@PNG-de-DE.png) | Draft | Marks the selected entry as "Draft". A recipe/procedure with this status cannot yet be used in productive operation. |
| !["Overview" tab](images/111308036491_DV_resource.Stream@PNG-de-DE.png) | Effective | Marks the selected entry as "Effective". A recipe/procedure with this status is being used in production. |
| !["Overview" tab](images/111308104843_DV_resource.Stream@PNG-de-DE.png) | Withdrawn | Marks the selected entry as "Withdrawn". A recipe or procedure with this status has been withdrawn from production. |
| !["Overview" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png) | Filter | Filters the entries according to defined criteria. |

**Sorting recipes or procedures**

1. Click on the symbol in the column header that you want to sort.

   The texts are sorted in alphabetical order, numbers are sorted by size.
2. Click again on the symbol in the header to change the sorting order.

**Filtering recipes or procedures**

1. Activate the filter criteria using the "Filter"!["Overview" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png) button.
2. Enter the criteria according to which the list is to be filtered.

   Only the recipes or procedures that meet the filter criteria are displayed.

**Note**

**Filter status**

To filter according to the "Status" criterion, enter the first letter of "Draft", "Effective" or "Withdrawn" in the filter field.

##### "Recipes" tab

In the "Recipes" tab you create new recipes, link the recipes with procedures and define formula parameters.

!["Recipes" tab](images/134168676491_DV_resource.Stream@PNG-en-US.png)

**Operator controls**

| Button | Name | Function |
| --- | --- | --- |
| !["Recipes" tab](images/129712435083_DV_resource.Stream@PNG-de-DE.png) | Add | Creates a new recipe. |
| !["Recipes" tab](images/129712443659_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes a recipe. |
| !["Recipes" tab](images/129707924363_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands an element. |
| !["Recipes" tab](images/129712054539_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses an element. |
| !["Recipes" tab](images/138560668555_DV_resource.Stream@PNG-en-US.png) | Status | Marks the recipe as "Draft", "Effective", or "Withdrawn". |

##### "Procedure" tab

In the "Procedure" tab, you create procedures for the production and see the procedures that have already been created in a graphic overview with all relevant units and equipment operations. You create procedures by means of drag-and-drop using the predefined elements.

!["Procedure" tab](images/134165591179_DV_resource.Stream@PNG-en-US.png)

The view is divided into the following areas:

- List of the already created procedures
- Work area in which you combine units and operations while using synchronization points to form a procedure.
- List of the units and operations available in the linked line

  You see the linked line at the top left in the control.

**Operator controls**

| Button | Name | Function |
| --- | --- | --- |
| !["Procedure" tab](images/129712435083_DV_resource.Stream@PNG-de-DE.png) | Add | Creates a new procedure. |
| !["Procedure" tab](images/129712443659_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes a procedure. |
| !["Procedure" tab](images/141796920331_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the display of the procedure. |
| !["Procedure" tab](images/141796928651_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the display of the procedure. |
| !["Procedure" tab](images/141797244171_DV_resource.Stream@PNG-de-DE.png) | Reset | Sets the display of the procedure back to the default size. |
| !["Procedure" tab](images/129707924363_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands an element. |
| !["Procedure" tab](images/129712054539_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses an element. |
| !["Procedure" tab](images/138560668555_DV_resource.Stream@PNG-en-US.png) | Status | Marks the procedure as "Draft", "Effective", or "Withdrawn". |

#### Creating and managing procedures (LCS) (RT Unified)

##### Introduction

In the recipe control, you have two options for creating and managing procedures:

- In the "Overview" tab

  ![Introduction](images/138500403723_DV_resource.Stream@PNG-en-US.png)
- In the "Procedure" tab

  ![Introduction](images/138493144587_DV_resource.Stream@PNG-en-US.png)

A procedure has the following properties:

| Property | Description |
| --- | --- |
| Name | Unique, language neutral name of the procedure. |
| Status | Status of the procedure:  - Draft - Effective - Withdrawn |
| Display name | Language-dependent display name of the procedure, which you store in various languages. |
| Minimum quantity | Defines the minimum required quantity of the product for this procedure. |
| Maximum quantity | Defines the maximum permitted quantity of the product for this procedure. |
| Unit of measure | Defines the unit of measure for this procedure. |
| Description | Description of the procedure. |
| Creation time | The creation time is automatically assigned by the system. |
| Last modified | The time of the last modification is automatically updated by the system. |

> **Note**
>
> **Response to status change**
>
> You edit the definition of a procedure that is already being used in recipes in the project. If you change the status of the procedure from "Effective" to "Draft" or "Withdrawn", the status of the associated recipe also changes to "Withdrawn". If the recipe is used by a job that has already been released, the status of the job changes to "Planned". Active jobs and jobs in "Queued" state are not affected by such changes.

##### Creating a procedure

1. Select the "Add" button in the "Procedures" tab.

   Alternatively, click the "<Add>" entry in the "Overview > Procedure list" tab.

   A procedure is created with "Draft" status.

   The mandatory properties are assigned automatically.

   The header is expanded in the "Procedure" tab.
2. Change the name of the procedure, e.g. "MT".
3. Change the display name of the procedure, e.g. "Mashing".
4. Change the maximum and minimum quantity, for example, "30" and "200".
5. Change the unit of measure, e.g. "kg".
6. Assign a description for the procedure.
7. Change the status from "Draft" to "Effective".

   All changes are applied automatically.

##### Editing a procedure

1. Select a procedure.
2. Change the status from "Effective" to "Draft".
3. In the "Procedure" tab: Expand the header.
4. Change the values of the procedure properties as needed.
5. Change the status from "Draft" to "Effective".

   All changes are applied automatically.

##### Delete procedure

You can only delete procedures in the "Draft" or "Withdrawn" status.

1. Select a procedure.
2. Click "Delete"

#### Configuring procedures (LCS) (RT Unified)

##### Introduction

In the "Procedure" tab in the recipe control, you define the units and equipment operations for the selected procedure.

You define the unit that starts the processing of the procedure. You connect equipment operations from different units to synchronization lines.

![Introduction](images/138526207883_DV_resource.Stream@PNG-en-US.png)

**Status changes**

The status of a procedure changes from "Effective" to "Withdrawn" when the status of the SES operation in use changes from "Effective" to "Draft" or "Withdrawn".

When the status of a procedure is changed from "Effective" to "Withdrawn", the status of the linked recipe is also changed to "Withdrawn".

##### Configuring a procedure

1. Switch to the "Procedure" tab in the recipe control.
2. On the left-hand side under "Procedures", select the procedure that you want to configure.
3. On the right-hand side under "Units", select a unit and move it into a marked field in the work area using drag-and-drop.

   The unit will be used in the procedure. As soon as the unit is used in a procedure, the unit is referred to as "Recipe unit procedure".

   The recipe unit procedure is given a name and a display name at the point of use.

   The available equipment operations for the selected unit are displayed under "Equipment operations".
4. Change the name of the recipe unit procedure at the point of use.
5. Change the display name of the recipe unit procedure at the point of use.

   You can only change the display name for the activated language. The display name of the recipe unit procedure is used in the job control.
6. Under "Equipment operations", select the desired equipment operation and move it below the corresponding recipe unit procedure in the work area using a drag-and-drop operation.

   The equipment operation is inserted at the end of the existing procedure. As soon as the equipment operation is used in a procedure, the equipment operation is referred to as "recipe operation".

   At the point of use, the recipe operation is given a name, which cannot be changed.
7. Repeat steps 3 to 6 until all required recipe unit procedures and recipe operations are defined.
8. Link the recipe unit procedure with synchronization lines.

   You can find additional information under [Synchronizing recipe operations (LCS)](#synchronizing-recipe-operations-lcs-rt-unified)
9. Select the "Start" button of the recipe unit procedure that is to be the starting unit.
10. To use the procedure in a recipe, select the "Effective" status in the selection menu.

    When all recipe operations are appropriately linked, the "Change status" dialog box opens. Otherwise, the message "You have an invalid procedure" is displayed at the bottom of the control.
11. Confirm the status change.

**Note**

While a recipe unit procedure is running, no recipe can be started that uses the same recipe unit procedure.

##### Deleting recipe unit procedure and recipe operations

1. Open the shortcut menu of the corresponding recipe unit procedure or recipe operation.
2. Select "Delete".
3. Confirm the delete operation.

To close the shortcut menu without deleting an element, select "Cancel".

##### Result

You have configured a recipe unit procedure and recipe operations for the procedure. The procedure has "Effective" status.

The name of the recipe operation in the recipe is made up of the unit and the associated equipment operation that is used in the procedure (unit/equipment operation).

#### Synchronizing recipe operations (LCS) (RT Unified)

##### Introduction

You synchronize processes over multiple recipe unit procedures at the level of the recipe operations. For this you connect the synchronization points of individual recipe operations of multiple recipe unit procedures to one another to define the run sequence. The synchronization line defines which recipe operations of the recipe unit procedure are synchronized. Synchronization points can be used before or after a recipe operation to define the synchronization line.

Two different synchronization lines are available to you:

- Blocking synchronization line

  The following recipe operation only starts if all other synchronization points of the same synchronization line have been run through.

  A blocking synchronization line is represented by a double line.
- Non-blocking synchronization line

  The following recipe operation is started immediately after the synchronization point has been reached.

  A non-blocking synchronization line is represented by a single line.

![Introduction](images/134166872203_DV_resource.Stream@PNG-en-US.png)

There are no restrictions on the number of synchronization lines. Our recommendation is a maximum of 30 synchronization lines for each procedure.

> **Note**
>
> Two previously configured synchronization lines cannot be connected to one another. A synchronization point that has not yet been connected can be added to an already configured synchronization line.

##### Configuring a synchronization line

1. Select synchronization point in the work area.

   All connectable synchronization points are highlighted.
2. Select the synchronization point from another recipe unit procedure that will synchronize the next recipe operation.

   The two points are connected with a blocking synchronization line.
3. To define a synchronization point as a non-blocking synchronization line, open the shortcut menu and select "Blocking/Not blocking".

##### Deleting a synchronization line

1. Select the synchronization line.
2. Open the shortcut menu.
3. Select "Remove synchronization"

##### Result

Recipe operations of various recipe unit procedures are synchronized and visualized with a synchronization line.

#### Using SES units and SES operations in a procedure (SES) (RT Unified)

With the sequence option, you can use SES units and SES operations in a procedure. If an SES operation is used in a procedure, the SES operation must be in "Effective" status.

SES units and SES operations are handled in the same way as LCS units and equipment operations.

**SES units**

As soon as an SES unit has been created in the Engineering System, the SES unit is displayed in the recipe control in the "Procedure" tab. If the SES unit is deleted, it is automatically removed from the recipe control. If the deleted SES unit is already being used in a procedure in the "Effective" status, the status of the procedure is changed to "Withdrawn" and the used recipe unit procedure removed from the procedure.

**SES operations**

As soon as an SES operation has been created in the SES control, regardless of the status, it is displayed in the recipe control in the "Procedure" tab. If the SES operation is deleted in the SES control, the SES operation is automatically removed from the recipe control. If the deleted SES operation is already being used in a procedure in the "Effective" status, the status of the procedure is changed to "Withdrawn" and the recipe operation in use is removed from the procedure.

**Status change in SES operations**

If you change the status of the SES operations from "Effective" to "Draft" or "Withdrawn" in the SES control, the status of the corresponding procedure is changed to "Withdrawn".

#### Creating and managing recipes (LCS) (RT Unified)

##### Introduction

In the recipe control, you have two options for creating and managing recipes:

- In the "Overview" tab

  ![Introduction](images/139000304523_DV_resource.Stream@PNG-en-US.png)
- In the "Recipes" tab

  ![Introduction](images/139009125515_DV_resource.Stream@PNG-en-US.png)

A recipe has the following properties:

| Property | Description |
| --- | --- |
| Name | Unique language-neutral name of the recipe. |
| Status | Status of the recipe:  - Draft - Effective - Withdrawn |
| Display name | Language-dependent display name of the recipe, which you store in various languages. |
| Procedure | The name of the assigned procedure from the selection list. |
| Product name | The name of the assigned material from the selection list. |
| Unit of measure | The unit of measure is automatically set by the system from the assigned procedure. |
| Default quantity | The defined quantity for manufacturing the end product from the specified recipe. |
| Description | Description of the recipe. |
| Creation time | The creation time is automatically assigned by the system. |
| Last modified | The time of the last modification is automatically updated by the system. |

> **Note**
>
> **Response to status change**
>
> You edit the definition of a recipe that is already being used in jobs. When you change the status of the recipe from "Effective" to "Draft" or "Withdrawn", the status of the already effective job changes to "Planned". Active jobs and jobs with the "Queued" state are not affected by such changes.

##### Requirement

- A procedure has been configured and has "Effective" status.

##### Create recipe

1. Select the "Add" button in the "Recipes" tab.

   Alternatively, click the "<Add>" entry in the "Overview > Recipe list" tab.

   A recipe with the "Draft" status is created.

   The mandatory properties are assigned.

   The header is expanded in the "Recipe" tab.

   The first procedure with the status "Effective" in the list is assigned.
2. Change the name of the recipe, e.g. "Beer_PaleAle".
3. Change the display name of the recipe, e.g. "Pale Ale".
4. If the automatically connected procedure is not the correct procedure, select the corresponding procedure from the drop-down list, e.g. "Brew beer".
5. Confirm the warning.
6. Change the default quantity, e.g. "70".

   The unit of measure is taken from the procedure.

   You define the maximum and minimum quantities in the procedure.
7. Select the material that is to be produced with this recipe (optional).
8. Assign a description for the recipe.
9. Change the status from "Draft" to "Effective".

   All changes are applied automatically.

**Note**

If no procedure with "Effective" status is available, the recipe cannot be created. An error message is displayed.

**Note**

If you change the procedure, a warning appears, because already defined setpoints of the formula parameters can be lost.

##### Editing a recipe

1. Select a recipe.
2. Change the status from "Effective" to "Draft".
3. Change the values of the recipe properties as required.
4. Change the status from "Draft" to "Effective".

   All changes are applied automatically.

##### Delete recipe

You can only delete recipes in the "Draft" or "Withdrawn" status.

1. Select a recipe.
2. Click "Delete"

#### Configuring recipes (LCS) (RT Unified)

##### Introduction

A recipe consists of a procedure for producing a specific end product. If you use operations in this procedure, this results in recipe operations that you define more precisely with formula parameters. The formula parameters allow the procedure to be used in various recipes independent of the product.

In the "Recipes" tab, you define the setpoints of the formula parameters. The setpoint specifies the quantity of an ingredient used in a recipe operation, for example.

You can only edit and configure recipes with "Draft" status.

![Introduction](images/137841817483_DV_resource.Stream@PNG-en-US.png)

A recipe operation has the following properties:

| Property | Description |
| --- | --- |
| Recipe operation | Name of the recipe operation. The name cannot be changed and is made up of the unit and the associated equipment operation that is used in the procedure (unit/equipment operation). |
| Formula parameter | The name of the operation parameter of the equipment operation that is defined in the Engineering System.  The formula parameter cannot be changed in RT. |
| Setpoint | The default value of the operation parameter of the equipment operation that is defined in the Engineering System.  The setpoint can be changed in RT. |
| Maximum value | The maximum value of the operation parameter of the equipment operation that is defined in the Engineering System.  The value cannot be changed in RT. |
| Minimum value | The minimum value of the operation parameter of the equipment operation that is defined in the Engineering System.  The value cannot be changed in RT. |
| Unit | The unit of the operation parameter of the equipment operation that is defined in the Engineering System.  The unit cannot be changed in RT. |
| Scalable | The setpoint is scaled when the option is activated in the "Scale" column. This means that the setpoint is changed proportionally to the defined quantity that you specify in the job overview. |
| Job parameter | If you have created a job, all formula parameters used in the job are displayed. By activating the option in the "Job parameter" column, you can change the setpoint of a formula parameter before starting the job. |

##### Setpoint

**Setpoint change**

Changing the setpoint has various effects:

- If, after changing the minimum or maximum value in the engineering system, the setpoint is now outside the range, the status of the recipe is changed to "Withdrawn". The setpoint involved is marked in red in Runtime.

**Resetting a changed setpoint**

If a setpoint has been changed in Runtime, the value can be reset in the following scenarios:

- The value is not in the specified range.
- The linked procedure has been changed.
- Loading is carried out in the engineering system.

##### Configuring a recipe operation

1. Click on the "Recipes" tab.
2. Select a recipe in the list.

   All operations that are configured in the procedure used are displayed as "Recipe operations".
3. Expand a recipe operation.

   The formula parameters and associated properties are displayed.
4. Define the setpoint.
5. If needed, enable the "Scalable" option.
6. If needed, enable the "Job parameter" option.
7. Change the status from "Draft" to "Effective".

##### Result

You have configured recipe operations in a recipe. You use the recipe in a job.

#### Scaling setpoints (LCS) (RT Unified)

##### Introduction

You have the option of scaling the setpoint specified in the recipe. The setpoint is changed proportionally to the defined quantity that you specify in the job overview.

**Example:**

The setpoint has the value 10 and the default quantity in the recipe has the value 50. If the quantity in the job is increased to 100, the setpoint is scaled to 20.

##### Requirement

- A procedure is used in the recipe and the default quantity does not have the value 0.

##### Configuring the scaling of the formula parameter

1. In the recipe control, click on the "Recipes" tab.
2. Select a recipe in the list.

   All operations that are configured in the procedure used are displayed as "Recipe operations".
3. Expand a recipe operation.

   The formula parameters and associated properties are displayed.
4. For the formula parameter, e.g. with the setpoint 10, enable the "Scalable" option.
5. Change the status from "Draft" to "Effective".

##### Configuring a job

1. In the job overview, select the planned job in the "Jobs" tab.
2. Change the "Quantity" job property, e.g. from 50,000 to 100,000.
3. Select the "Release" button.

   The "Change status" dialog box opens.
4. Confirm the status change.

   The status of the selected job changes to "Released".
5. Double-click the job.

   The job is displayed in the job control.

##### Result

In the job control in the expandable parameter view, the scaled setpoint is displayed and used on start of the job.

#### Exporting procedures and recipes (LCS) (RT Unified)

##### Introduction

You have the option of exporting procedures and recipes created in a recipe control to a file. You can then import the exported data to the same or another Runtime project.

The export file contains the following information:

- Properties of the procedures/recipes

  The material assigned to the recipe is not exported.
- Procedures together with the utilized units, operations and synchronizations
- Recipes together with the defined formula parameters and their setpoint, tag type and scalability properties

##### Requirement

- Runtime contains a recipe control that is connected to a line.
- At least one recipe exists.

##### Procedure

To perform an export, follow these steps:

1. Change to the overview of the recipe control.
2. Click the "Export" button.

   By default, the export file is stored in the download path defined in the browser.

   As soon as the export is started, the progress is displayed in the status bar.

**Note**

If the export file cannot be stored in the download path defined in the browser, the "Save as" dialog is displayed with an alternative path.

##### Result

All created procedures and recipes are saved regardless of status in the "Procedures_Recipes_<Line name>.json" file.

#### Importing procedures and recipes (LCS) (RT Unified)

##### Introduction

Exported procedures and recipes can be imported into a Runtime project.

> **Note**
>
> Note the following restrictions:
>
> - You can only import procedures and recipes that are not present in the destination project.
> - The language of imported procedures and recipes must correspond to the Runtime language.

##### Requirement

- Procedures and recipes have been exported to a json file beforehand.
- Runtime contains a recipe control.
- The line on which the exported procedures and recipes are based has been configured in the destination project and connected to the recipe control.
- LCS units and equipment operations used in the exported procedures must have been configured in the destination project.
- If SES units and equipment modules are used in the exported procedures, SES units and equipment modules including steps and operations must exist in the target project in Runtime.

##### Importing procedures and recipes

1. Select the "Import" button in the overview of the recipe control.

   A selection dialog opens.
2. Select the json file you want to import.
3. Select the "Open" button.

   A confirmation dialog appears.
4. Confirm the input.

   The progress is displayed in the status bar.

**Note**

Recipe operations and formula parameters are displayed in the destination system based on the linked procedures.

If the name of a formula parameter in an exported recipe matches the name of a formula parameter in the destination project, the setpoint, tag type and scalability properties will be overwritten during the import.

**Note**

**Dragging-and-Dropping the json file**

It is not possible to drag and drop the json file. Use the "Open" button.

If you have already tried to drag and drop the file, close the browser and reopen it.

##### Result

- Procedures have been imported.
- Recipes have been imported.

  Materials linked to recipes are not imported.
- A log file is stored in the folder configured in the download settings of the browser. The file named LcsImportLog_<Name of import file>.txt contains the following information:

  - Time stamp
  - Information: List of successfully imported procedures and recipes
  - Warnings: The import of the respective recipe is complete. Imported formula parameters are not present in the destination project or the properties of the formula parameters differ from the destination project.
  - Error: The procedure / recipe is already present in the destination project or the needed units or equipment operations have not been created in the destination project.

    The import of the procedure or recipe will be skipped.

> **Note**
>
> If a line on which the exported procedures and recipes are based is not configured in the target project, no log file is created. An error message is displayed.

#### Delete Runtime configuration data (LCS) (RT Unified)

##### Introduction

You have the possibility to clear all Runtime configuration data of the line.

> **Note**
>
> Only runtime users with the "Read" and "Write" rights are allowed to delete runtime data.

##### Requirement

- The recipe control is open.
- Runtime configuration data is available.

##### Procedure

1. Click the "Clear" button in the toolbar.

   The "Clear runtime configuration" dialog opens.
2. Click "Yes".

##### Result

All procedures and recipes are deleted from the control and from the LCS recipe service.

### Jobs (LCS) (RT Unified)

This section contains information on the following topics:

- [Operating the job overview (LCS) (RT Unified)](#operating-the-job-overview-lcs-rt-unified)
- [Creating and managing jobs (LCS) (RT Unified)](#creating-and-managing-jobs-lcs-rt-unified)
- [Changing the setpoint of a job parameter (LCS) (RT Unified)](#changing-the-setpoint-of-a-job-parameter-lcs-rt-unified)
- [Executing jobs in the job overview (LCS) (RT Unified)](#executing-jobs-in-the-job-overview-lcs-rt-unified)
- [Executing jobs with SES units and SES operations (SES) (RT Unified)](#executing-jobs-with-ses-units-and-ses-operations-ses-rt-unified)
- [Operating the job control (LCS) (RT Unified)](#operating-the-job-control-lcs-rt-unified)
- [Executing jobs in the job control (LCS) (RT Unified)](#executing-jobs-in-the-job-control-lcs-rt-unified)
- [Colored representation during job execution (LCS) (RT Unified)](#colored-representation-during-job-execution-lcs-rt-unified)
- [Changing setpoints during job execution (LCS) (RT Unified)](#changing-setpoints-during-job-execution-lcs-rt-unified)
- [Example: Start job automatically (RT Unified)](#example-start-job-automatically-rt-unified)

#### Operating the job overview (LCS) (RT Unified)

##### Use

The job overview provides you with an overview of the production jobs. You choose between 2 tabs in the job overview:

The column width is adjustable. After a screen change or a browser update, the column width returns to its default size.

##### "Jobs" tab

In the "Jobs" tab, you create, manage and operate jobs for the production.

!["Jobs" tab](images/134376927755_DV_resource.Stream@PNG-en-US.png)

The control shows a maximum of 15 jobs on one page. When more jobs are created, you can scroll to the next page.

**Operator controls**

The following operator controls are available for the job overview:

| Button | Name | Function |
| --- | --- | --- |
| !["Jobs" tab](images/111307899787_DV_resource.Stream@PNG-de-DE.png) | Add | Creates a new entry. |
| !["Jobs" tab](images/111307908363_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected entry. |
| !["Jobs" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png) | Filter | Filters the entries according to defined criteria. |

You change the status of a job using the following operator controls:

| Button | Name | Function |
| --- | --- | --- |
| !["Jobs" tab](images/114675376523_DV_resource.Stream@PNG-de-DE.png) | Release | Marks the selected entry as "Released". A job with this status is being used in production. |
| !["Jobs" tab](images/114675367947_DV_resource.Stream@PNG-de-DE.png) | Withdraw | Marks the selected entry as "Withdrawn". A job with this status has been withdrawn from production. |

Use the following operator controls to execute a job:

| Button | Name | Function |
| --- | --- | --- |
| !["Jobs" tab](images/113358466571_DV_resource.Stream@PNG-de-DE.png) | Start | Starts a job.  A job for which an error has been reported can only be started when the error is no longer present. |
| !["Jobs" tab](images/113358424075_DV_resource.Stream@PNG-de-DE.png) | Pause | Pauses a job. |
| !["Jobs" tab](images/113358432523_DV_resource.Stream@PNG-de-DE.png) | Resume | Resumes execution of the job. |
| !["Jobs" tab](images/113358705675_DV_resource.Stream@PNG-de-DE.png) | Hold | Halts a job. |
| !["Jobs" tab](images/113358715019_DV_resource.Stream@PNG-de-DE.png) | Restart | Restarts a job. |
| !["Jobs" tab](images/113355283467_DV_resource.Stream@PNG-de-DE.png) | Stop | Stops a job. |
| !["Jobs" tab](images/113358236043_DV_resource.Stream@PNG-de-DE.png) | Abort | Completely aborts a job. |
| !["Jobs" tab](images/143383319307_DV_resource.Stream@PNG-de-DE.png) | Remove | Removes a job.  The button appears 30 sec. after clicking the "Abort" button if the "Aborted" state has not been reached. |

The job parameter control can be expanded or collapsed using the following operator controls:

| Button | Name | Function |
| --- | --- | --- |
| !["Jobs" tab](images/129707924363_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands the job parameter control.   The job parameter view only shows job parameters for which the "Job parameter" option is enabled in the recipe, including the following properties:  - Setpoint - Minimum value - Maximum value - Unit of measure - Scalable |
| !["Jobs" tab](images/129712054539_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses the job parameter control. |

**Sorting jobs**

1. Click on the arrow symbol in the header of column that you want to sort.

   The texts are sorted in alphabetical order, numbers are sorted by size.
2. Click again on the symbol in the header to change the sorting order.

**Filtering jobs**

1. Activate the filter criteria using the "Filter" button !["Jobs" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png).
2. Enter the criteria according to which the job list is filtered.

   Only the jobs that meet the filter criteria are displayed.

##### "Job history" tab

In the "Job history" tab, you see an overview of all jobs that were completed, stopped, aborted or removed. You can create a report for the jobs.

!["Job history" tab](images/144589482891_DV_resource.Stream@PNG-en-US.png)

**Operator controls**

The following operator controls are available for the job history:

| Button | Name | Function |
| --- | --- | --- |
| !["Job history" tab](images/111307899787_DV_resource.Stream@PNG-de-DE.png) | Generate report | Generates a report. You can find additional information under [Local reporting for Line Coordination (LCS)](#local-reporting-for-line-coordination-lcs-rt-unified) |
| !["Job history" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png) | Filter | Filters the entries according to defined criteria. |

**Filtering jobs**

1. Activate the filter criteria using the "Filter"!["Job history" tab](images/114645927435_DV_resource.Stream@PNG-de-DE.png) button.
2. Enter the criteria according to which the job list is filtered.

   Only the jobs that meet the filter criteria are displayed.

**Note**

A maximum of 150 jobs are displayed in the job history. Define additional filter criteria, if necessary, to further limit the filtering.

#### Creating and managing jobs (LCS) (RT Unified)

##### Introduction

You create jobs for production which are executed manually or automatically at a defined time in your plant. This means that you have the option to plan a number of jobs at line level in advance, to create them in standardized form and to execute them automatically.

A recipe is assigned to each job. You have the option of using recipes based on sequence data as well as recipes based on your own data.

You create and manage the production jobs in the "Jobs" tab of the job overview.

![Introduction](images/139675338891_DV_resource.Stream@PNG-en-US.png)

A job has the following properties:

| Property | Description |
| --- | --- |
| Job name | Unique language neutral name of the job. |
| Status | Status of the job or the running job. |
| Display name | Language-dependent display name of the job, which you store in various languages. |
| Job ID | The job ID orders the jobs in the order of creation. The job ID is assigned automatically by the system and cannot be changed. |
| Recipe name | Assign a previously defined recipe to each job. |
| Quantity | You define which quantity is produced in the job. Define a valid quantity range for each recipe. By default, the amount specified is given in the recipe used.  If a scalable setpoint is contained in the job, the setpoint is automatically scaled proportionally to the specified quantity. |
| Unit of measure | Is filled in automatically by the system as soon as you select a recipe. |
| Start mode | A job can be started in the following modes:  - "Manual"    The user starts the job manually. - "On time"   The job starts automatically at the defined start time. The system automatically fills the start time with the current time. Adjust the start time to your specifications. The start time can only be defined in "Planned" status. |
| Start time | The start time defines the time at which a job starts in "On time" start mode. |
| Description | Description of the job. |
| Creation time | The creation time is automatically assigned by the system. |
| Last modified | The time of the last modification is automatically updated by the system. |

##### Requirement

- A recipe has been configured and has "Effective" status.

##### Create job

1. Select the "Add" button or click the "<Add>" entry in the list.

   A job is created in "Planned" status.

   The mandatory properties are assigned.

   The first recipe with the status "Effective" in the list is linked to the job.
2. Change the name of the job, e.g. "Bake".
3. Change the display name of the job, for example "Bake bread".
4. Select the corresponding recipe from the selection list, e.g. "Bread".
5. Adjust the quantity.
6. Optional: Expand the job parameter control and change the setpoint of the formula parameter.
7. Define the start mode, e.g. "Manual".
8. Assign a description of the job.

   All changes are applied automatically.

##### Release job

> **Note**
>
> When a job is released, a setpoint change in the job parameter control is no longer possible.

1. Select a planned job in the "Jobs" tab.
2. Select the "Release" button.

   The "Change status" dialog box opens.
3. Confirm the status change.

   The status of the selected job changes to "Released".

##### Edit job

1. Select a planned job in the "Jobs" tab.
2. Select the "Withdraw" button.

   The "Change status" dialog box opens.
3. Confirm the status change.

   The status of the selected job changes to "Planned".
4. Change the job properties as required, e.g. the quantity of the product.
5. Change the status from "Withdrawn" to "Released".

   All changes are applied automatically.

##### Delete job

You can only delete jobs with "Planned" status.

1. Go to the job list in the job overview.
2. Select a job.
3. Click "Delete"

##### Create job report

1. Change to the "Job history" view.
2. Select the job for which you want to create a report.
3. Click the "Generate report" button on the toolbar.

   The report for the selected job is created and can be downloaded from the "Reports" control.

You can find additional information at [Local reporting for Line Coordination (LCS)](#local-reporting-for-line-coordination-lcs-rt-unified).

#### Changing the setpoint of a job parameter (LCS) (RT Unified)

##### Introduction

You have the option of changing the setpoint specified in the recipe in a planned job. When the job is released, the setpoint cannot be changed in the job overview.

##### Configuring a recipe

1. In the recipe control, click on the "Recipes" tab.
2. Select a recipe in the list.

   All operations that are configured in the procedure used are displayed as "Recipe operations".
3. Expand a recipe operation.

   The formula parameters and associated properties are displayed.
4. Enable the "Job parameter" option for the desired formula parameter.

   The setpoint can be changed in the planned job using this formula parameter.
5. Change the status from "Draft" to "Effective".

##### Configuring a job

1. In the job overview, select the planned job in the "Jobs" tab.
2. Expand the job parameter control.

   All configured job parameters are shown in the job parameter control.
3. Change the setpoint.
4. Click on the "Release" button.

   The "Change status" dialog box opens.
5. Confirm the status change.

   The status of the selected job changes to "Released".
6. Double-click the job.

   The job is displayed in the job control.

##### Result

In the job control in the expandable parameter view, the changed setpoint is displayed and used at the start of the job.

#### Executing jobs in the job overview (LCS) (RT Unified)

##### Introduction

You have the option to intervene in job execution at any time: to hold, stop, resume or abort a job. You can execute multiple jobs in parallel.

The buttons for job execution are activated and deactivated based on the job state.

A maximum of 1000 jobs can be planned, released or active in the job overview.

> **Note**
>
> **Restriction for starting the jobs**
>
> Manually starting multiple jobs at the same time is not supported.

##### Requirement for executing jobs

For the execution of the jobs it is necessary that all involved recipe unit procedures are switched to automatic mode.

Make sure that no recipe unit procedure used is in manual mode.

##### Starting a job manually

You can start a job manually at the line level. All recipe operations that are being used in the job are executed in the order of the synchronization lines.

To do so, the function blocks of the unit must be connected to the function blocks of the equipment modules in the PLC program.

1. Select a job with "Released" status in the job overview by selecting the check box in the "Name" column.
2. Select the "Start" button.
3. The system changes the status of the job to "Running" and the cell of the job is visually highlighted.
4. After all operations are executed, the system sets the status of the job to "Completed".

**Note**

- If the start unit is allocated, the status of the job changes to "Waiting".
- If two jobs use the same recipe unit procedure, the first job is executed and the second job waits until the relevant recipe unit procedure is free.
- A job in "Error" state can only be continued if the error state is no longer present.

##### Withdrawing a job

You can withdraw a job with "Released" status from production again.

1. Select a job from the job list.
2. Click the "Withdraw" button.

   The system changes the status of the job to "Planned" status.

   Jobs that were already transmitted to the PLC are discarded.

##### Pausing and resuming a job

You can pause the execution of a job which is in the "Running" state for a moment at any time and resume it again.

1. In the job list, select a job that is currently being executed and has the "Running" state.
2. Click the "Pause" button.

   All active recipe operations are transferred to the "Paused" state. The execution of the job is paused.

   The equipment waits for the next command.
3. To continue running the job, click "Resume".

   Execution of the job is continued from the paused state.

##### Holding and restarting a job

You have the option to hold the execution of a job which is in the "Running", "Paused" or "Resuming" state and then restart it.

1. Select the job in the job list.
2. Click the "Hold job" button.

   The execution of the job is held by the system.
3. To restart the job subsequently, click "Restart".

   In this case, the execution of the job starts again from the beginning of the running recipe operation.

##### Stopping a job

You can stop a job in the "Running", "Paused", "Held" and "Error" states.

1. Select the job in the job list.
2. Click the "Stop" button.

   The job is brought to a controlled standstill by the system.

##### Aborting a job

With the "Abort" button, you abort a job in a quick but not necessarily controlled manner. If no sequencing is required, the state is immediately changed to "Aborted".

1. Select the job in the job list.
2. Click the "Abort" button.

   The job is completely aborted by the system. The aborted job cannot be restarted.

---

**See also**

[States and transient states (RT Unified)](#states-and-transient-states-rt-unified)

#### Executing jobs with SES units and SES operations (SES) (RT Unified)

##### Introduction

If you have configured SES units and SES operations in a procedure, you can execute the recipe with a job.

While the job is being executed, the setpoints defined in the recipe control are loaded into the respective instance data block of the SES unit. The previously used setpoints in the instance data block are overwritten. If an SES operation is restarted via the SES control using the "Restart" button, the setpoints in the instance data block are not overwritten. If the operation parameters are updated in the SES control while the respective job is running, the modified properties are used immediately for the job execution.

##### Requirement for executing jobs

- The SES operations used are loaded in the SES control.
- Automatic mode is activated for the associated equipment module in the "Monitoring" tab in the SES control.

##### Job status "Queued"

If manual mode is activated in the SES Control, the job switches to "Waiting" status. Activate automatic mode to continue the job.

##### Job status "Error"

If a changed SES operation has not been loaded into the PLC and the versions of the operation used differ, the job changes to the "Error" state. The "Start" button is deactivated.

The job cannot be started in the job overview or job control. You need to load the operation into the SES control again.

#### Operating the job control (LCS) (RT Unified)

##### Use

With the job control you check the sequence of a job in graphic form.

![Use](images/139758180491_DV_resource.Stream@PNG-en-US.png)

In the "Job monitoring" area, you see the production processes of the individual recipe unit procedures with the recipe operations.

To display the detailed sequence of the job in the job control, double-click a job in the job overview. The different colors indicate the change in state of the active recipe operations, synchronization points and synchronization lines. You see the current status of an executed job in the bottom right corner of the job control. You can find additional information at [Colored representation during job execution (LCS)](#colored-representation-during-job-execution-lcs-rt-unified).

You can use the parameter view to change the setpoints of the formula parameters and job parameters during the execution of the job. The linked setpoints of a recipe operation can only be changed in the "Inactive" or "Running" state.

While the job is being executed, the actual value is displayed next to the setpoint display.

The column width is adjustable. After a screen change or a browser update, the column width returns to its default size.

##### Operator controls

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/141796920331_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the display of the job. |
| ![Operator controls](images/141796928651_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the display of the job. |
| ![Operator controls](images/141797244171_DV_resource.Stream@PNG-de-DE.png) | Reset | Sets the display of the job back to the default size. |
| ![Operator controls](images/129707924363_DV_resource.Stream@PNG-de-DE.png) | Expand | Opens the parameter view. The parameter view shows the formula parameters of the recipe used in the job and their properties:  - Setpoint - Actual value - Minimum value - Maximum value - Unit of measure - Scalable |
| ![Operator controls](images/129712054539_DV_resource.Stream@PNG-de-DE.png) | Collapse | Closes the parameter view. |

The following operator controls are available for operating the jobs:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/113358466571_DV_resource.Stream@PNG-de-DE.png) | Start | Starts a job.  A job for which an error has been reported can only be started if the error is no longer present. |
| ![Operator controls](images/113358424075_DV_resource.Stream@PNG-de-DE.png) | Pause | Pauses a job. |
| ![Operator controls](images/113358432523_DV_resource.Stream@PNG-de-DE.png) | Resume | Resumes the execution of the job. |
| ![Operator controls](images/113358705675_DV_resource.Stream@PNG-de-DE.png) | Hold | Halts a job. |
| ![Operator controls](images/113358715019_DV_resource.Stream@PNG-de-DE.png) | Restart | Restarts a job. |
| ![Operator controls](images/113355283467_DV_resource.Stream@PNG-de-DE.png) | Stop | Stops a job. |
| ![Operator controls](images/113358236043_DV_resource.Stream@PNG-de-DE.png) | Abort | Completely aborts a job. |

#### Executing jobs in the job control (LCS) (RT Unified)

##### Introduction

You have the possibility to execute the jobs also in the job control. The advantage of this is that you have a detailed overview, e.g. which recipe unit procedure and recipe operation is currently active. You can also intervene in the job and control the individual recipe operations.

While the job is being executed, the recipe unit procedures are marked with the following symbols:

| Symbol |  | Description |
| --- | --- | --- |
| ![Introduction](images/143345536523_DV_resource.Stream@PNG-de-DE.png) | Unit is requested (manual mode) | The recipe unit procedure is requested by the current job, but not available through manual mode.  To start the recipe unit procedure, set the mode to automatic. |
| ![Introduction](images/143345527947_DV_resource.Stream@PNG-de-DE.png) | Unit is requested | The recipe unit procedure is requested by the current job, but has been allocated, e.g. by another job. |
| ![Introduction](images/143345775499_DV_resource.Stream@PNG-de-DE.png) | Unit is allocated | The recipe unit procedure has been allocated to the current job. |
| ![Introduction](images/143346155275_DV_resource.Stream@PNG-de-DE.png) | Unit is not allocated | The recipe unit procedure is neither requested nor allocated to the current job. |
| ![Introduction](images/144512265099_DV_resource.Stream@PNG-de-DE.png) | Unit is in use (manual mode) | The recipe unit procedure has been allocated in the current job, but cannot be operated in manual mode.  To start the recipe unit procedure, set the mode to automatic. |

##### Operating a job at the job level

Operating at job level is the same operation as operating a job in the job overview.

You can find additional information under [Executing jobs in the job overview (LCS)](#executing-jobs-in-the-job-overview-lcs-rt-unified)

##### Operating the job at the recipe operation level

You have the option of controlling individual recipe operations during job execution.

1. Select the desired recipe operation.

   The recipe operation is highlighted in blue. The name of the recipe operation and the recipe unit procedure is displayed to the left of the toolbar and in the parameter view.
2. Click on the desired button.

   The following buttons can be operated, depending on the state of the recipe operation:

   - Pause
   - Resume
   - Hold
   - Restart
3. To deselect the recipe operation, click anywhere within the job control (except on the job elements).

#### Colored representation during job execution (LCS) (RT Unified)

##### Color representation of the job

The recipe operations and recipe unit procedures are shown in color while a job is being executed. You can identify the status in which the element is based on the colors. The colored representation is also shown in the status bar of the job control, as well as in the job overview in the column "Status" and in the status bar.

![Color representation of the job](images/134377480331_DV_resource.Stream@PNG-en-US.png)

The following statuses are possible:

![Color representation of the job](images/143381533067_DV_resource.Stream@PNG-en-US.png)

##### Divided color representation of the recipe operation

In addition to the described color display of the status, the recipe operation is shown in two colors when it is in the transient state.

Example:

![Divided color representation of the recipe operation](images/143428214923_DV_resource.Stream@PNG-de-DE.png)

The "Pause" button has been clicked at recipe operation level or at job level. The recipe operation that is currently active goes from "Running" to the "Paused" state and is currently in the "Pausing" transient state. The upper color (green) indicates the origin, and the lower color indicates the destination (yellow).

#### Changing setpoints during job execution (LCS) (RT Unified)

##### Introduction

You can change the setpoints of formula parameters and job parameters during an active job. The changed setpoint is written directly to the PLC tag. The setpoint of a recipe operation cannot be changed if the recipe operation is completed, aborted or stopped.

##### Requirement

- The job is displayed in the job control and has started.

##### Procedure

1. Expand the parameter view.

   All formula parameters used in the job are displayed.
2. Click in the input field of the setpoint you want to change.
3. Enter a new setpoint.

   If the value entered is outside the minimum or maximum value, the previous setpoint is restored.
4. Click on any field outside the setpoint field to apply the value.

#### Example: Start job automatically (RT Unified)

##### Example

A new type of beer is being introduced in a brewery. A technologist has already designed and released the procedure and the recipe for this. The recipe uses the procedure that controls the production process. The formula parameters of the recipe operations for producing the new type of beer are defined in the recipe.

The production processes should start automatically at a defined time.

The utilized function blocks come from Sequence.

##### Objective

The new type of beer should be produced according to a recipe predefined by the technologist. The new production job should start automatically at the line level at a specific time.

![Objective](images/114645936267_DV_resource.Stream@PNG-de-DE.png)

##### Requirement

- The unit and the function block of the equipment module are interconnected in the PLC program.
- The "SmokedBeerType1" recipe for the new "Smoked beer" type has been created and has "Effective" status.

##### Creating job with automatic start

1. Go to the job list in the job overview.
2. Click "Add".

   A new job is created.

   The mandatory properties are assigned.
3. Change the name of the job, e.g. "SmokedBeerType1".
4. Change the display name of the job, e.g. "Smoked beer".
5. Select the corresponding recipe from the selection list, e.g. "SmokedBeerType1".
6. Adjust the quantity as required, e.g. 10000.

   The unit of measure is taken from the recipe.
7. Define the start mode, e.g. "On time".
8. Define the start time, e.g. on the next day at 10:00 AM.
9. Enter the description of the job in the "Description" field.
10. Set the job to "Released" status.

    The job starts automatically at the defined time if the defined starting unit is free.

### Materials (LCS) (RT Unified)

This section contains information on the following topics:

- [Operating the material overview (LCS) (RT Unified)](#operating-the-material-overview-lcs-rt-unified)
- [Creating and managing material classes (LCS) (RT Unified)](#creating-and-managing-material-classes-lcs-rt-unified)
- [Creating and managing materials (LCS) (RT Unified)](#creating-and-managing-materials-lcs-rt-unified)

#### Operating the material overview (LCS) (RT Unified)

##### Use

With the material overview you configure and manage the materials that you use for production.

![Use](images/138488105867_DV_resource.Stream@PNG-en-US.png)

You choose between 2 tabs in the material overview:

- Material

  In the "Material" tab, you create new entries for different materials that you use during production.
- Material class

  In the "Material class" tab, you define new material classes. Based on the material classes, you group the materials according to similar properties, e.g. different types of flour in the material class "Flour".

The column width is adjustable. After a screen change or a browser update, the column width returns to its default size.

##### Operator controls

The following operator controls are available for the material overview:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/111307899787_DV_resource.Stream@PNG-de-DE.png) | Add | Creates a new entry. |
| ![Operator controls](images/111307908363_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected entry. |
| ![Operator controls](images/111308027915_DV_resource.Stream@PNG-de-DE.png) | Draft | Marks the selected entry as "Draft". A material with this status cannot be used in productive operation yet. |
| ![Operator controls](images/111308036491_DV_resource.Stream@PNG-de-DE.png) | Effective | Marks the selected entry as "Effective". A material with this status is being used in production. |
| ![Operator controls](images/111308104843_DV_resource.Stream@PNG-de-DE.png) | Withdrawn | Marks the selected entry as "Withdrawn". In this status, the material has been withdrawn from the production. |
| ![Operator controls](images/114645927435_DV_resource.Stream@PNG-de-DE.png) | Filter | Filters the entries according to defined criteria. |

##### Sorting materials or material classes

1. Click on the symbol in the column header that you want to sort.

   The texts are sorted in alphabetical order, numbers are sorted by size.
2. Click on the symbol in the header again to change the order of sorting.

##### Filtering materials or material classes

1. Activate the filter criteria using the "Filter"![Filtering materials or material classes](images/114645927435_DV_resource.Stream@PNG-de-DE.png) button.
2. Enter the criteria according to which the list is to be filtered.

   Only the materials or material classes that meet the filter criteria are displayed.

**Note**

**Filter status**

To filter according to the "Status" criterion, enter the first letter of "Draft", "Effective" or "Withdrawn" in the filter field.

#### Creating and managing material classes (LCS) (RT Unified)

##### Introduction

A material class combines materials of the same type. You define material classes in Runtime in the material overview.

![Introduction](images/138492066827_DV_resource.Stream@PNG-en-US.png)

In the material overview, you define the following properties in the "Material class" tab:

| Property | Description |
| --- | --- |
| Name | Unique, language-neutral name of the material class. |
| Display name | Language-dependent display name of the material class that you save in different languages. |
| Description | Description of the material class. |
| Creation time | The creation time is automatically assigned by the system. |
| Last modified | The time of the last modification is automatically updated by the system. |

##### Creating a material class

1. Select the "Add" button or click the "<Add>" entry in the list.

   A material class is created in "Draft" status.

   The name and display name of the material class are assigned automatically.
2. Change the name of the material class according to your requirements, e.g. "Grains".
3. Change the display name of the material class according to your requirements, e.g. "Grains_domestic".
4. Enter a description for the material.

   All changes are applied automatically.

##### Editing a material class

1. Select a material class.
2. Change the values of the material class properties as required.

##### Deleting a material class

1. Select a material class.
2. Click "Delete"

#### Creating and managing materials (LCS) (RT Unified)

##### Introduction

Define the end product of the production as a material. In the material overview, you define and manage materials in Runtime.

![Introduction](images/138488105867_DV_resource.Stream@PNG-en-US.png)

In the material overview, you define the following properties in the "Material" tab:

| Property | Description |
| --- | --- |
| Name | Unique, language-neutral name of the material |
| Status | Status of the material entry:  - Draft - Effective - Withdrawn |
| Display name | Language-dependent display name of the material that you save in different languages. |
| Material ID | Unique ID of the material. |
| Material class | Material class to which this material belongs. |
| Unit of measure | The unit of measure of a material. |
| Description | Description of the material. |
| Creation time | The creation time is automatically assigned by the system. |
| Last modified | The time of the last modification is automatically updated by the system. |

> **Note**
>
> **Response to status change**
>
> You edit the definition of the material that is already used in recipes in your project. If you change the status of the material from "Effective" to "Draft" or "Withdrawn", the status of the associated recipe also changes to "Withdrawn". If the recipe is used by a job that has already been released, the status of the job changes to "Planned". Active jobs and jobs in "Queued" state are not affected by such changes.

##### Creating material

1. Select the "Add" button or click the "<Add>" entry in the list.

   A material in "Draft" status is created.

   Name, display name, material ID and unit of measure are assigned automatically.
2. Change the name of the material according to your requirements, e.g. "Barley".
3. Change the display name of the material according to your requirements, e.g. "Dried barley".
4. Change the material ID according to your requirements.
5. Select the material class for this material, e.g. "Grains domestic" (optional).
6. Change the unit of measure of the material according to your requirements, e.g. "kg".
7. Enter a description for the material.
8. Change the status from "Draft" to "Effective".

   All changes are applied automatically.

> **Note**
>
> **Using material in a recipe**
>
> In the drop-down list, select the material in "Effective" status in the recipe under "Product name".

##### Editing material

1. Select a material.
2. Change the status from "Effective" to "Draft".
3. Change the values of the material properties as required.
4. Change the status from "Draft" to "Effective".

##### Deleting material

You can only delete materials in the "Draft" or "Withdrawn" status.

1. Select a material.
2. Click "Delete"

### Steps and operations (SES) (RT Unified)

This section contains information on the following topics:

- [Operating the SES control in the "Configuration" tab (SES) (RT Unified)](#operating-the-ses-control-in-the-configuration-tab-ses-rt-unified)
- [Settings for parameters and control modules (SES) (RT Unified)](#settings-for-parameters-and-control-modules-ses-rt-unified)
- [Creating and managing steps (SES) (RT Unified)](#creating-and-managing-steps-ses-rt-unified)
- [Creating and managing operations (SES) (RT Unified)](#creating-and-managing-operations-ses-rt-unified)
- [Defining setpoints (SES) (RT Unified)](#defining-setpoints-ses-rt-unified)
- [Creating and using operation parameters (SES) (RT Unified)](#creating-and-using-operation-parameters-ses-rt-unified)
- [Exporting steps and operations (SES) (RT Unified)](#exporting-steps-and-operations-ses-rt-unified)
- [Importing steps and operations (SES) (RT Unified)](#importing-steps-and-operations-ses-rt-unified)
- [Delete Runtime configuration data (SES) (RT Unified)](#delete-runtime-configuration-data-ses-rt-unified)
- [Executing operations (RT Unified)](#executing-operations-rt-unified)

#### Operating the SES control in the "Configuration" tab (SES) (RT Unified)

##### Introduction

In the SES control in the "Configuration" tab, you create and manage the steps and operations of an equipment module.

![Introduction](images/144993862667_DV_resource.Stream@PNG-en-US.png)

You choose between two tabs in the SES control in the "Configuration" tab:

- Operations

  In the "Operations" tab, you create and edit operations. Within the operation, you define the transitions and add individual steps to the transitions. You create and edit operation parameters for individual steps and specify setpoints.
- Steps

  In the "Steps" tab, you create and edit the steps. You add control modules and parameters to the steps and make settings for the inputs/outputs and setpoints.

##### Operator controls

The following operator controls are available:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/129666454027_DV_resource.Stream@PNG-en-US.png) | Open equipment module | Opens a dialog window to select an equipment module. |
| ![Operator controls](images/139841304587_DV_resource.Stream@PNG-de-DE.png) | Export | Exports steps and operations into a   JSON file. |
| ![Operator controls](images/139841313163_DV_resource.Stream@PNG-de-DE.png) | Import | Imports steps and operations from a JSON file. |
| ![Operator controls](images/143224651403_DV_resource.Stream@PNG-de-DE.png) | Clear | Deletes all runtime configuration data from the control and from the SES memory system. |
| ![Operator controls](images/129712435083_DV_resource.Stream@PNG-de-DE.png) | Add object | Adds a new object. |
| ![Operator controls](images/129712443659_DV_resource.Stream@PNG-de-DE.png) | Delete object | Deletes an object. |
| ![Operator controls](images/129707915787_DV_resource.Stream@PNG-de-DE.png) | Load | All operations in "Effective" status are loaded into the PLC. After successful loading, the operations are displayed in the "Monitor" tab and can be started there.   This button only becomes active when the "Manual mode" button is activated in the "Monitoring" tab. |
| ![Operator controls](images/129666091787_DV_resource.Stream@PNG-de-DE.png) | Expand all | Shows all details of a step in the "Operations" tab. |
| ![Operator controls](images/129666095499_DV_resource.Stream@PNG-de-DE.png) | Collapse all | Hides all details of a step in the "Operations" tab. |
| ![Operator controls](images/129712631435_DV_resource.Stream@PNG-de-DE.png) | Show commands | Shows all commands of an operation.  Not released in the "Steps" tab. |
| ![Operator controls](images/129713254411_DV_resource.Stream@PNG-de-DE.png) | Follow step | When an operation is started, the current step is always displayed in the detail window.  Not released in the "Monitoring" tab. |
| ![Operator controls](images/129665516683_DV_resource.Stream@PNG-de-DE.png) | Select filter | No function |
| ![Operator controls](images/129665512971_DV_resource.Stream@PNG-de-DE.png) | Enable filter | No function |
| ![Operator controls](images/129666222347_DV_resource.Stream@PNG-de-DE.png) | Full screen | Enabling / disabling full-screen mode |
| ![Operator controls](images/129707924363_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands all elements. |
| ![Operator controls](images/129712054539_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses all elements. |
| ![Operator controls](images/138560668555_DV_resource.Stream@PNG-en-US.png) | Status | Marks the steps or operations as "Draft", "Effective" or "Withdrawn". |

#### Settings for parameters and control modules (SES) (RT Unified)

##### Introduction

You have the option to make settings for control modules and parameters. By default, all settings are grayed out and not active. Define the following settings in a step:

| Setting |  | Description |
| --- | --- | --- |
| ![Introduction](images/129729182347_DV_resource.Stream@PNG-de-DE.png) | Set | The binary output that is configured under "Block input/output" in TIA Portal is output at the function block under "cmcommand".  If the "Set" setting is active, the binary output is influenced by the "Value" setting.  If a step is active, the value under "cmcommand" is changed. If the step is completed and the binary output is not used again in the next step, "cmcommand" is reset.   If the "Set" setting is not active, no setpoint field appears under "Operations".  The parameter types "Timer forwards" and "Timer backwards" have a different behavior (see table below). |
| ![Introduction](images/129729103499_DV_resource.Stream@PNG-de-DE.png)     ![Introduction](images/129729107211_DV_resource.Stream@PNG-de-DE.png)     ![Introduction](images/143283152523_DV_resource.Stream@PNG-de-DE.png)     ![Introduction](images/143283161099_DV_resource.Stream@PNG-de-DE.png) | Value | If the "Set" setting is active, the value at "cmcommand" is influenced.  If the "Check" setting is active, the value at "cmfbonoff" is checked dependent on the configured parameter type.    Under "Value", the "0" or "1" value is displayed for the following parameter types:  - External - Counter forwards - Counter backwards - Actual value >= setpoint - Actual value <= setpoint - Integrator - Integrator with hold   Under "Value", the "Play" or "Pause" symbol is displayed for the following parameter types:  - Timer forwards - Timer backwards |
| ![Introduction](images/115226877835_DV_resource.Stream@PNG-de-DE.png) | Check | This setting checks whether all conditions are met.  If "Check" is not activated, the condition is immediately fulfilled. |
| ![Introduction](images/115237301387_DV_resource.Stream@PNG-de-DE.png) | Status | Shows the status of the control module or parameter if the step is being executed in "Monitoring" tab:    ![Introduction](images/133440073995_DV_resource.Stream@PNG-de-DE.png) Idle    ![Introduction](images/133440082571_DV_resource.Stream@PNG-de-DE.png) Active    ![Introduction](images/133439941643_DV_resource.Stream@PNG-de-DE.png) Conditions met    ![Introduction](images/133440027019_DV_resource.Stream@PNG-de-DE.png) Error |
| ![Introduction](images/129729110923_DV_resource.Stream@PNG-de-DE.png) | Logic | OR logic operation: If the "OR" setting is set for all parameters, at least one parameter must be fulfilled.  Parameters without the "OR" setting have an AND logic operation. |

The following tables show the effects on the settings in the step configuration of the respective parameter types.

> **Note**
>
> The tables also apply to the configuration of control modules, apart from "actualvalue" and "parametersetpoint".

##### Effect of the settings

The following table applies to all parameter types except for "Timer forwards" and "Timer backwards":

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | - | - | Set to 1. | The entered setpoint is output. | Not relevant. | Not relevant. | The parameter condition is met immediately. |
| x | 0 | - | - | Set to 0. | The entered setpoint is output. | Not relevant. | Not relevant. | The parameter condition is met immediately. |
| - | 1 | x | - | Not set. | Not set. | Not relevant. | The parameter condition is met when "cmfbonoff" = 1. | - |
| - | 0 | x | - | Not set. | Not set. | Not relevant. | The parameter condition is met when "cmfbonoff" = 0. | - |

##### "External" parameter type

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | Not relevant. | The parameter condition is met when "cmfbonoff" = 1. | - |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | Not relevant. | The parameter condition is met when "cmfbonoff" = 0. | - |

##### Parameter type "Counter forwards"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is increased by the value in "Increment". | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is increased by the value in "Increment". | Not relevant. | - |

##### Parameter type "Counter backwards"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is decreased by the value in "Increment". | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | At each signal change from 0.0 to 1.0 at assigned input "actualvalue[x]", the value in "statactualvalue[x]" is decreased by the value in "Increment". | Not relevant. | - |

##### Parameter type "Actual value >= Setpoint"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | The value at input "actualvalue[x]" is compared with the setpoint taking into account the hysteresis. | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | The value at input "actualvalue[x]" is compared with the setpoint taking into account the hysteresis. | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |

##### Parameter type "Actual value <= Setpoint"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | The value at input "actualvalue[x]" is compared with the setpoint taking into account the hysteresis. | Not relevant. | The parameter condition is fulfilled if "statactualvalue[x]" <= setpoint and is output in bit x (x = block input/output) of the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | The value at input "actualvalue[x]" is compared with the setpoint taking into account the hysteresis. | Not relevant. | The parameter condition is fulfilled if "statactualvalue[x]" <= setpoint and is output in bit x (x = block input/output) of the "statcmfbonoff" element. |

##### Parameter type "Integrator"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of 1 second and added to the value in "statactualvalue[x]". | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of 1 second and added to the value in "statactualvalue[x]". | Not relevant. | - |

##### Parameter type "Integrator with hold"

| Setting |  |  |  | Effect |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Set | Value | Check | OR | cmcommand | parametersetpoint | actualvalue | cmbonoff | Other effect |
| x | 1 | x | - | Set to 1. | The entered setpoint is output. | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of "x" milliseconds (variable) and added to the value in "statactualvalue[x]". | Not relevant. | The parameter condition is met when "statactualvalue[x]" >= setpoint and is output in bit x (x = block input/output) at the "statcmfbonoff" element. |
| x | 0 | x | - | Set to 0. | The entered setpoint is output. | The value at input "actualvalue[x]" is multiplied by the value in "Increment" and the time interval of "x" milliseconds (variable) and added to the value in "statactualvalue[x]". | Not relevant. | - |

##### "Timer forwards" and "Timer backwards" parameter type

| Setting | Effect |
| --- | --- |
| Set activated | Time value is reset to 0 for "Timer forwards", and the setpoint is set to the entered value.  Time value is reset to the setpoint at "Timer backwards". |
| Value !["Timer forwards" and "Timer backwards" parameter type](images/143283152523_DV_resource.Stream@PNG-de-DE.png) | - Timer running - cmcommand is set to 1. |
| Value !["Timer forwards" and "Timer backwards" parameter type](images/143283161099_DV_resource.Stream@PNG-de-DE.png) | - Timer paused - cmcommand is set to 0. |
| Check activated | If "Check" is not activated, the condition is immediately fulfilled. |

You can decide according to your specifications in which step you:

- Reset the time
- Let the time run
- Pause the time
- Perform the check

You can freely decide in which transition state you implement the above specifications.

If the setpoint of "Timer forwards" is reached or the setpoint of "Timer backwards" is 0, the condition is fulfilled.

**"**
**Timer forwards**
**"**

The seconds are counted forwards in "statactualvalue[x]". The parameter condition is met when "statactualvalue[x]" >= setpoint.

**"**
**Timer backwards**
**"**

The seconds are counted backwards in "statactualvalue[x]". The parameter condition is met when "statactualvalue[x]" <= 0.

#### Creating and managing steps (SES) (RT Unified)

##### Introduction

You assign control modules with parameters and unassigned parameters to a step. You also define settings for individual parameters and control modules.

You can find additional information under [Settings for parameters and control modules (SES)](#settings-for-parameters-and-control-modules-ses-rt-unified)

##### Requirement

- An equipment module is open in the SES control.
- The "Configuration" tab is open.

##### Creating a step

1. Click on the "Steps" tab.
2. Click the "+" icon in the left area under "Steps".

   A step in "Draft" status is created in the step list.

   The content of the step is displayed in the work area.
3. In the work area, change the display name (1st name) and the name (2nd name).
4. Select the desired control module in the right area under "Control modules" or the desired "Parameter" under "Parameters".
5. Drag the selected object into the work area.

   The object is displayed in the work area.
6. Define the settings for the control module or parameter.
7. Change the status from "Draft" to "Effective".

**Note**

When you select a control module, the parameters configured in the control module are displayed in the right-hand area under "Parameters".

If you select "Unassigned parameters" in the "Control modules" area, all other configured parameters will appear in the "Parameters" area.

##### Editing a step

1. Click on the "Steps" tab.
2. In the left area under "Steps", click on the required step.

   The step with content is displayed in the work area.
3. Change the status from "Effective" to "Draft".
4. Change the values of the step as required.
5. Change the status from "Draft" to "Effective".

##### Deleting a step

You can only delete steps in the "Draft" or "Withdrawn" status.

1. Select a step in the step list.
2. Click "Delete"

#### Creating and managing operations (SES) (RT Unified)

##### Introduction

An operation can contain one or more steps. Only steps with "Effective" status can be added to an operation. One step can be used multiple times.

The permissible number of steps, etc., within the equipment module varies depending on which SES function block is configured.

| Property | EquipmentModuleSmall | EquipmentModuleMedium | EquipmentModuleLarge | Description |
| --- | --- | --- | --- | --- |
| Steps | 50 | 100 | 200 | Number of steps that can be created within an equipment module. |
| Setpoints | 250 | 500 | 1500 | Number of setpoints that can be distributed. |
| Step sequence | 100 | 200 | 500 | Number of steps that can be referenced in all operations. |
| Operations | 10 | 20 | 30 | Number of operations that can be used for an equipment module. |
| Operation parameters | 10 | 10 | 10 | Number of operation parameters that can be used in an operation. |

##### Requirement

- An equipment module is open in the SES control.
- The "Configuration" tab is open.
- At least one step has "Effective" status.

##### Creating an operation and assigning steps

1. Click on the "Operations" tab.
2. Click the "+" icon in the left-hand area under "Operations".

   An operation is created in "Draft" status in the operation list. The work area shows an empty list of the operation parameters. You can find additional information at [Creating and using operation parameters (SES)](#creating-and-using-operation-parameters-ses-rt-unified)
3. In the work area, change the display name (1st name) and the name (2nd name) of the created operation.
4. Expand the operation in the left area.
5. Under "Add transient state", select the desired transient state and click the "+" icon. A multiple selection is possible.

   The content of the transient state is displayed below the operation in the operation list.
6. Click a transient state.

   The transient state is displayed in the work area.
7. In the right-hand area under "Steps", select the desired step and drag it into the work area.

   The step is displayed in the work area with the configured control modules and parameters.

   A "1" appears at the transient state, as you have added 1 step.
8. Add additional steps, if needed.
9. If necessary, change the step sequence by moving the steps.
10. Select the operation.
11. Change the status from "Draft" to "Effective".
12. Click the "Load" button so that you can execute the operation later in the "Monitoring" tab.

**Note**

Loading is only possible if the "Manual mode" button is enabled in the "Monitoring" tab.

Because **all** operations with "Effective" status are included when loading, this can take some time. The progress is displayed in the status bar.

##### Editing an operation

1. Click on the "Operations" tab.
2. Click on the desired operation in the left-hand area under "Operations".
3. Change the status from "Effective" to "Draft".
4. Select the transition state.
5. Change the values or settings within the steps.
6. Select the operation.
7. Change the status from "Draft" to "Effective".

##### Deleting an operation

You can only delete operations in the "Draft" or "Withdrawn" status.

1. Select an operation in the "Operations" area.
2. Click "Delete"

#### Defining setpoints (SES) (RT Unified)

##### Introduction

You have the option of setting setpoints for parameters. You define the setpoint in the "Operations" tab.

![Introduction](images/134090883851_DV_resource.Stream@PNG-en-US.png)

| Setting | Description |
| --- | --- |
| Setpoint | Enter your setpoint in the "Setpoint" input field. The unit of measurement configured in the TIA Portal is displayed next to the field.  The entered setpoint is output at the "parametersetpoint" function block. |
| Apply setpoint | "Apply setpoint" is set by default in the drop-down box. With this setting, the specified setpoint is applied. |

To set a setpoint using an operation parameter, you can find additional information at [Creating and using operation parameters (SES)](#creating-and-using-operation-parameters-ses-rt-unified).

##### Requirement

- The step is used in an operation.
- The operation is in the "Draft" status.
- The "Set" setting is activated in the step. This requirement is not relevant for the parameter types "Timer forwards" and "Timer backwards".
- The "Use setpoint" setting is selected.

##### Procedure

1. Click on the "Operations" tab.
2. Expand the operation in the left area under "Operations".
3. Click the transient state in which the step is being used.
4. Enter your setpoint in the step under "Setpoint".

**Note**

If the specified setpoint is outside the configured range, an error message is displayed. The previously set setpoint is displayed.

#### Creating and using operation parameters (SES) (RT Unified)

##### Introduction

You can change the setpoint of a parameter via an operation parameter.

![Introduction](images/139829218443_DV_resource.Stream@PNG-en-US.png)

##### Requirement

- The step is used in an operation.
- The operation is in the "Draft" status.
- The "Set" setting is activated in the step. This requirement is not relevant for the parameter types "Timer forwards" and "Timer backwards".

##### Creating operation parameters

1. Open the "Operations" tab.
2. In the left area under "Operations", select the operation that includes the step.

   The work area shows the list of operation parameters.
3. Drag your desired parameters or parameters of the control module into the operation list.

   A new operation parameter with default values has been created.
4. If necessary, change the name and display name for the operation parameter.
5. Enter your setpoint under "Value".

**Note**

Unit of measurement, minimum value and maximum value cannot be changed. These values have already been configured in the TIA Portal in the parameter or parameters of the control module.

**Result**

The created operation parameter can be selected in the drop-down list in the step.

##### Using operation parameters

1. Open the "Operations" tab.
2. Expand the operation in the left area under "Operations".
3. Select the transient state that contains the step.
4. In the display window, select the step in which you want to use the operation parameter.
5. Select your created operation parameter in the drop-down list.

**Result**

![Using operation parameters](images/139829214731_DV_resource.Stream@PNG-en-US.png)

The former input field "Setpoint" is grayed out and replaced by the value of the operation parameter. The configured setpoint of the selected operation parameter is displayed as a setpoint in the step and cannot be changed in the step.

#### Exporting steps and operations (SES) (RT Unified)

##### Introduction

You can export the steps and operations created in the SES control and the engineering data in the TIA Portal to a file. You can then import the exported data into another Runtime project, for example. The export is only possible in the "Configuration" tab. Editing of the equipment module is blocked and the SES Control cannot be operated during the export.

The export file contains:

- All created steps with the parameters, control modules and parameter settings used
- All operation parameters with their settings
- All created operations including transient states, assigned steps, step sequence and setpoints
- All steps and operations contain the attributes:

  - Name
  - Display name
  - Status
  - Reference to the unit and the equipment module in which the steps or operations are configured
- Engineering data including the maximum number of permitted operations of the configured equipment module

##### Requirement

- An equipment module is open in the SES control.
- The "Configuration" tab is open.
- Steps and operations have been created.

##### Procedure

To perform an export, follow these steps:

1. Click the "Export" button.

   By default, the export file is stored in the download path defined in the browser.

   As soon as the export is started, the progress is displayed in the status bar.

**Note**

If the export file cannot be stored in the download path defined in the browser, the "Save as" dialog is displayed with an alternative path.

##### Result

The engineering data and all steps and operations created in Runtime are saved independent of the status in the file "<Name of the unit>_<Name of the equipment module>.json".

#### Importing steps and operations (SES) (RT Unified)

##### Introduction

Exported steps and operations can be imported into a Runtime project.

> **Note**
>
> Note the following restrictions:
>
> - You can only import steps and operations that are based on the equipment module that is open.
> - You can only import steps and operations that do not exist in the target project.
> - The language of imported steps and operations must match the Runtime language.
> - Import of engineering data is not supported in V17.

The import is only possible in the "Configuration" tab. Editing of the equipment module and the SES Control is blocked during the import.

**Import scenarios**

- All steps and operations are imported because they match the data in the TIA Portal. The information bar displays the message "Import completed successfully".
- If the match exists in general, but individual parameters and/or control modules are different, the affected step or operation goes into the "Withdrawn" status. The information bar displays the message "Import completed with warnings".
- When a step that is assigned to an operation does not match, it is not used in the operation. The operation goes into the "Withdrawn" status. The information bar shows the message "Import completed with errors".
- When an error is contained in the definition of the step sequence of an operation, the operation is imported empty in the "Withdrawn" status. The information bar shows the message "Import completed with errors".
- If the name of the unit and/or the name of the equipment module does not match the data in the TIA Portal, the import is aborted. The information bar displays the message "Import aborted".

  You can find the correct name of the unit or the equipment module in the log file.

##### Requirement

- A JSON file for import exists.
- The equipment module that is open in SES Control must have the same name as in the JSON file.

  The name of the equipment module is specified in the engineering system in the "Interface" tab.
- The "Configuration" tab is open.

##### Procedure

1. Select the "Import" button.

   A selection dialog opens.
2. Select the JSON file you want to import.
3. Select the "Open" button.

   A confirmation dialog appears.
4. Confirm the input.

   By default, a log file is stored in the download path defined in the browser.

   As soon as the import is started, the progress is displayed in the status bar.

**Note**

**Dragging-and-dropping the JSON file**

It is not possible to import the JSON file using a drag-and-drop operation. Use the "Open" button.

If you have already tried to drag and drop the file, close the browser and reopen it.

**Note**

If the log file cannot be stored in the download path defined in the browser, the "Save as" dialog is displayed with an alternative path.

##### Result

All steps and operations are imported when they match the data in the TIA Portal.

A log file with the name "SESImportLog_<Name of the unit> _<Name of the equipment module>.txt" is created; it contains the following information:

- Time stamp
- List of successfully imported steps and operations
- Warnings and errors

#### Delete Runtime configuration data (SES) (RT Unified)

##### Introduction

You have the possibility to clear all Runtime configuration data of the opened equipment module.

> **Note**
>
> Only runtime users with the "Read" and "Write" rights are allowed to delete runtime data.

##### Requirement

- The "Configuration" tab is opened in the SES control.
- Runtime configuration data is available.

##### Procedure

1. Click the "Clear" button in the toolbar.

   The "Clear runtime configuration" dialog opens.
2. Click "Yes".

##### Result

All steps, operations and operation parameters are deleted from the control and from the SES memory system.

#### Executing operations (RT Unified)

This section contains information on the following topics:

- [Operating the SES control in the "Monitoring" tab (SES) (RT Unified)](#operating-the-ses-control-in-the-monitoring-tab-ses-rt-unified)
- [Colored representation during operation execution (SES) (RT Unified)](#colored-representation-during-operation-execution-ses-rt-unified)
- [Executing operations (SES) (RT Unified)](#executing-operations-ses-rt-unified)
- [Making a jump in the step order (SES) (RT Unified)](#making-a-jump-in-the-step-order-ses-rt-unified)

##### Operating the SES control in the "Monitoring" tab (SES) (RT Unified)

###### Introduction

In the SES control in the "Monitoring" tab, you perform steps and operations of an equipment module and intervene in the execution process.

![Introduction](images/144998870411_DV_resource.Stream@PNG-en-US.png)

The following tab is only available in the SES control in the "Monitoring" tab:

- Operations

  In the "Operations" tab, you perform operations and intervene in the execution by means of the control elements.

The "Steps" tab is grayed out and cannot be opened.

###### Control elements

The following control elements are available:

| Button | Name | Function |
| --- | --- | --- |
| ![Control elements](images/129712631435_DV_resource.Stream@PNG-de-DE.png) | Show commands | Shows all commands of an operation. |
| ![Control elements](images/129713254411_DV_resource.Stream@PNG-de-DE.png) | Follow step | When an operation is started, the current step is always displayed in the detail window. |
| ![Control elements](images/132517914251_DV_resource.Stream@PNG-de-DE.png) | Automatic mode | Automatic mode is set as the default value. When the automatic mode is active, all other control elements are grayed out. LCS can only use the operations if automatic mode is active. |
| ![Control elements](images/129713262987_DV_resource.Stream@PNG-de-DE.png) | Manual mode | When manual mode is active, you can use all other control elements. For example, you can start the operation with the "Start" button. |
| ![Control elements](images/132516894219_DV_resource.Stream@PNG-de-DE.png) | Start | Starts the operation. When the "Pause" button is activated, the operation can be restarted. |
| ![Control elements](images/129713476363_DV_resource.Stream@PNG-de-DE.png) | Stop/Reset | Stops the entire operation. If the operation is in the "Error" state, use this button to reset the operation.  Only use this control element with caution, such as in case of error messages. |
| ![Control elements](images/132516902795_DV_resource.Stream@PNG-de-DE.png) | Pause | Pauses the operation. |
| ![Control elements](images/132517649547_DV_resource.Stream@PNG-de-DE.png) | Restart | The operation is restarted. "Restart" is activated when the operation is in "Hold" state. |
| ![Control elements](images/132517512971_DV_resource.Stream@PNG-de-DE.png) | Hold | The operation is held immediately. |
| ![Control elements](images/132517658123_DV_resource.Stream@PNG-de-DE.png) | Cancel | Cancels the operation. |
| ![Control elements](images/129713830539_DV_resource.Stream@PNG-de-DE.png) | Single step mode activated | The single step mode is activated. |
| ![Control elements](images/132517905675_DV_resource.Stream@PNG-de-DE.png) | Single step mode deactivated | The single step mode is deactivated. |
| ![Control elements](images/129713839115_DV_resource.Stream@PNG-de-DE.png) | Finish step | Executes the active step, independent of its conditions. Then jumps to the next step. |
| ![Control elements](images/134230858507_DV_resource.Stream@PNG-de-DE.png) | Jump to step | The active step is aborted immediately, and the selected step becomes active. |
| ![Control elements](images/132517730699_DV_resource.Stream@PNG-de-DE.png) | Complete | Completes an operation. Suitable for operations that cannot be completed on their own. |

##### Colored representation during operation execution (SES) (RT Unified)

###### Introduction

In the "Monitoring" tab, you execute the loaded operations. The operations, transient states and steps are displayed in color during execution.

###### Color representation of the operations

The operations are displayed in color as follows:

![Color representation of the operations](images/133345918219_DV_resource.Stream@PNG-de-DE.png)

| Color | Description |
| --- | --- |
| ![Color representation of the operations](images/133345908619_DV_resource.Stream@PNG-de-DE.png) | Default color, the operation is inactive. |
| ![Color representation of the operations](images/133345823243_DV_resource.Stream@PNG-de-DE.png) | The operation is selected. |
| ![Color representation of the operations](images/133345814667_DV_resource.Stream@PNG-de-DE.png) | The operation is being executed. |

After the operation has been completed, it is shown again in the default color.

###### Color representation of the transient states

The transient states within the operation are displayed in color as follows:

![Color representation of the transient states](images/134370606091_DV_resource.Stream@PNG-en-US.png)

| Color | Description |
| --- | --- |
| ![Color representation of the transient states](images/133345908619_DV_resource.Stream@PNG-de-DE.png) | Default color, the transient state is inactive. |
| ![Color representation of the transient states](images/133345823243_DV_resource.Stream@PNG-de-DE.png) | The operation is selected. |
| ![Color representation of the transient states](images/133435645835_DV_resource.Stream@PNG-de-DE.png) | The transient state within the operation is selected. |
| ![Color representation of the transient states](images/133345814667_DV_resource.Stream@PNG-de-DE.png) | The transient state is being executed. |
| ![Color representation of the transient states](images/133435654411_DV_resource.Stream@PNG-de-DE.png) | The transient state has been carried out. |
| ![Color representation of the transient states](images/133435714187_DV_resource.Stream@PNG-de-DE.png) | The transient state is selected. |

**Color representation of the transient states in the status bar**

![Color representation of the transient states](images/143381533067_DV_resource.Stream@PNG-en-US.png)

###### Color representation of the steps

The steps of the transient states are displayed in color as follows.

![Color representation of the steps](images/134371852939_DV_resource.Stream@PNG-en-US.png)

| Color | Description |
| --- | --- |
| ![Color representation of the steps](images/133345908619_DV_resource.Stream@PNG-de-DE.png) | Default color, the step is inactive. |
| ![Color representation of the steps](images/133345814667_DV_resource.Stream@PNG-de-DE.png) | The step is being executed. |
| ![Color representation of the steps](images/133435654411_DV_resource.Stream@PNG-de-DE.png) | The step has been completed. |
| ![Color representation of the steps](images/133435714187_DV_resource.Stream@PNG-de-DE.png) | The step is selected, for example, to execute a jump. |

##### Executing operations (SES) (RT Unified)

###### Introduction

In the "Monitoring" tab, you execute the loaded operations. All setpoints displayed in the step can be changed during execution.

You can find additional information under [Operating the SES control in the "Monitoring" tab (SES)](#operating-the-ses-control-in-the-monitoring-tab-ses-rt-unified)

###### Requirement

- The operation was loaded in the "Configuration" tab

###### Procedure

1. Select the "Monitoring" tab.

   All loaded operations are displayed.
2. Select an operation.
3. Click the "Start" button.

###### Result

The operation is started in manual mode. When the "Set" setting is activated in the step, the setpoint and the actual value are displayed in the step. The setpoint can be changed when the step is active.

![Result](images/133466194443_DV_resource.Stream@PNG-de-DE.png)

**"Timer forwards" and "Timer backwards" parameter type**

When the parameter type "Timer forwards" or "Timer backwards" is used in the step, the setpoint and the actual value are always displayed. Regardless of whether or not the "Set" setting is activated in the step.

##### Making a jump in the step order (SES) (RT Unified)

###### Introduction

You can make a jump within a transient state. A jump allows you to disrupt the step order and immediately start a different step. Steps that have already been completed can also be used as jump destinations.

###### Requirement

- An operation contains at least two steps.

###### Procedure

1. Select a step in an active operation (jump destination).

   The step is marked with a blue frame.
2. Select "Jump to" in the shortcut menu.

   Alternatively, click the "![Procedure](images/134230752395_DV_resource.Stream@PNG-de-DE.png)" button.

###### Result

The active step is aborted immediately. The selected step becomes active immediately.

> **Note**
>
> **Jump to active step**
>
> If you make a jump to the active step, the step is restarted.

## Local reporting for Line Coordination (LCS) (RT Unified)

This section contains information on the following topics:

- [Basic information (LCS) (RT Unified)](#basic-information-lcs-rt-unified)
- [Workflow (LCS) (RT Unified)](#workflow-lcs-rt-unified)
- [Define report template with time series segment (LCS) (RT Unified)](#define-report-template-with-time-series-segment-lcs-rt-unified)
- [Define report template with hierarchical segment (LCS) (RT Unified)](#define-report-template-with-hierarchical-segment-lcs-rt-unified)
- [Creating a report job and defining triggers (LCS) (RT Unified)](#creating-a-report-job-and-defining-triggers-lcs-rt-unified)
- [Creating a job report (LCS) (RT Unified)](#creating-a-job-report-lcs-rt-unified)

### Basic information (LCS) (RT Unified)

This section contains information on the following topics:

- [Introduction (LCS) (RT Unified)](#introduction-lcs-rt-unified)
- [Requirements (LCS) (RT Unified)](#requirements-lcs-rt-unified)

#### Introduction (LCS) (RT Unified)

When the Line Coordination option package is installed, you can generate job reports in Runtime with WinCC Unified Reporting. You can then continue to edit the data in Excel or save the report as PDF and distribute or archive it.

![Figure](images/115612377099_DV_resource.Stream@PNG-de-DE.png)

#### Requirements (LCS) (RT Unified)

To create job reports with Line Coordination, the Excel add-in must be installed. In addition, you must be familiar with the basic operation of WinCC Unified Reporting. The documentation for this can be found in the TIA Portal Help under "Creating production logs".

**Basic information on report templates**

Information on creating report templates is available in the TIA Portal help, in the "Creating templates for production reports" section.

In the Excel add-in, this information is also available after you have connected a server and logged in. For this purpose, click the "?" icon in the "WinCC Unified Reporting" tab.

**Basic information on production reports in Runtime**

Information on creating production logs in Runtime is available in the TIA Portal help in the section "Working with production logs in Runtime".

### Workflow (LCS) (RT Unified)

#### Requirement

- The Line Coordination option package is installed.
- Position the "Reports" control in a screen of a WinCC Unified device.
- LCS must be configured in the Runtime project.
- The same requirements apply to the use of Reporting with the WinCC Unified basic installation.

#### Run sequence

1. Define a report template for your jobs in the Excel add-in.
2. Define a trigger for the job reports in the "Reports" control.
3. Create a job report in the job history of the "Job overview" LCS control.

### Define report template with time series segment (LCS) (RT Unified)

#### Introduction

You define report templates in the Excel add-in.

#### Requirement

- Microsoft Excel is open and the "WinCC Unified" tab is visible.
- The server on which an active Runtime project with LCS configuration is running is selected in the "WinCC Unified" tab under "Connections".
- The list of options that is called from the server includes "LCS time series".

#### Defining a time series segment

1. In the "WinCC Unified" tab, click on "Segments".

   The list of segments is loaded.
2. Select "New segment".

   The selection menu opens.
3. Select "New time series segment".

   A new time series segment is created.
4. Assign a name.
5. Specify the storage location, the table and the cell in which the time series segment is to start.
6. Confirm with "OK".

#### Adding a data source item

1. Click the created time series segment.
2. Click the "+" icon.

   The menu for selecting a data source item opens.
3. Select the "LCS time series segment" option.
4. Select the "LCS Job order report".
5. Select the "LCS job order report" option under "Selected data source items".

   ![Adding a data source item](images/134415600907_DV_resource.Stream@PNG-en-US.png)

   ![Adding a data source item](images/134415600907_DV_resource.Stream@PNG-en-US.png)
6. Confirm your entries with "OK".

   The template is generated.
7. Save the report template.

**Adjusting columns**

1. Select the "Edit" button of the data source item.
2. Select the desired columns.
3. Make your changes.
4. Confirm your entries with "OK".

   The template is updated.

**Testing the template**

1. Navigate to the job overview in your Runtime project.
2. Select the "Job history" tab.
3. Select a job.
4. Click the "Generate report" button.
5. Switch to Excel.
6. Click the ![Adding a data source item](images/143423888779_DV_resource.Stream@PNG-de-DE.png) button next to the time series segments.

   The template is displayed.

   Example:

   ![Adding a data source item](images/143424200587_DV_resource.Stream@PNG-de-DE.png)

   ![Adding a data source item](images/143424200587_DV_resource.Stream@PNG-de-DE.png)

### Define report template with hierarchical segment (LCS) (RT Unified)

#### Introduction

You define report templates with hierarchical view in the Excel add-in.

#### Requirement

- Microsoft Excel is open and the "WinCC Unified" tab is visible.
- The server on which an active Runtime project with LCS configuration is running is selected in the "WinCC Unified" tab under "Connections".
- The list of options that is called from the server includes "LCS Hierarchical".

#### Defining a hierarchical segment

1. In the "WinCC Unified" tab, click on "Segments".

   The list of segments is loaded.
2. Select "New segment".

   The selection menu opens.
3. Select "New hierarchical segment".

   A new hierarchical segment is created.
4. Assign a name.
5. Specify the storage location, the table and the cell in which the hierarchical segment is to start.
6. Confirm with "OK".

#### Adding a data source item

1. Click the created hierarchical segment.
2. Click the "+" icon.

   The menu for selecting a data source item opens.
3. Select the "LCS hierarchical" option.
4. Select the "LCS Job order report".
5. Select the "LCS job order report" option under "Selected data source items".

   ![Adding a data source item](images/134415600907_DV_resource.Stream@PNG-en-US.png)

   ![Adding a data source item](images/134415600907_DV_resource.Stream@PNG-en-US.png)
6. Confirm your entries with "OK".

   The template is generated.
7. Save the report template.

**Adjusting columns**

1. Select the "Edit" button of the data source item.
2. Select the desired columns.
3. Make your changes.
4. Confirm your entries with "OK".

   The template is updated.

**Testing the template**

1. Navigate to the job overview in your Runtime project.
2. Select the "Job history" tab.
3. Select a job.
4. Click the "Generate report" button.
5. Switch to Excel.
6. Click the ![Adding a data source item](images/143423888779_DV_resource.Stream@PNG-de-DE.png) button next to the hierarchical segments.

   The template is displayed.

   Example:

   ![Adding a data source item](images/143423897611_DV_resource.Stream@PNG-de-DE.png)

   ![Adding a data source item](images/143423897611_DV_resource.Stream@PNG-de-DE.png)

### Creating a report job and defining triggers (LCS) (RT Unified)

#### Introduction

Before you create a job report, create a report job in the "Reports" control and define a trigger.

#### Requirement

- A report template has been created in Excel.
- The "Reports" control is opened in runtime.

#### Procedure

1. Select the "Job parameters" tab in the "Reports" control.
2. Under "Templates", select the "Add new" button.

   A selection dialog opens.
3. Select the report template previously created in the Excel add-in.
4. Select "Open".

   The report template is added.
5. Under "Trigger", select the "Add new" button.
6. Select "Tag trigger" from the list and click "OK".
7. Click "Select tag".
8. To filter the selection, enter "*@JobIdForLcsReporting" in the input field.

   If you are using a migrated project, enter "*JobId*" in the input field.
9. Select the tag of your line, e.g. "HMI_RT_1::Line_1.@JobIdForLcsReporting"
10. Define the following settings:

    - Condition: ">"
    - Condition value: "0"
11. Add a report job in the "Report jobs" area.
12. Define the template for the report job.
13. Select the trigger created for the report job.

**Note**

A separate report job must be created for each line.

#### Result

You have created a report job and the trigger for a line.

![Result](images/137841957643_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Working with production reports in Runtime (RT Unified)](Creating%20production%20reports%20%28RT%20Unified%29.md#working-with-production-reports-in-runtime-rt-unified)

### Creating a job report (LCS) (RT Unified)

#### Introduction

You can create the job report and download it as xlsx file or pdf file.

#### Procedure

1. Select a job in the LCS control "Job overview" in the "Job history" tab.
2. Click the "Generate report" button.
3. Switch to the "Reports" control.

   A new entry has been created in the "Reports" area of the "Reports" control.
4. Select the file format.
5. Click "Export".

   The file is downloaded to the download directory of the browser.
6. To view the job report, open the file.

---
title: "Performance Insight - Optimizing processes with KPIs   (RT Unified)"
package: WCCUPFIESenUS
topics: 103
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Performance Insight - Optimizing processes with KPIs   (RT Unified)

This section contains information on the following topics:

- [Migrating V16 project (RT Unified)](#migrating-v16-project-rt-unified)
- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring KPIs (RT Unified)](#configuring-kpis-rt-unified)
- [Create and save data log (RT Unified)](#create-and-save-data-log-rt-unified)
- [Resetting the data log (RT Unified)](#resetting-the-data-log-rt-unified)
- [Configuring the controls (RT Unified)](#configuring-the-controls-rt-unified)
- [Compiling configuration data and loading it into Runtime (RT Unified)](#compiling-configuration-data-and-loading-it-into-runtime-rt-unified)
- [Validation of the configuration of plant objects (RT Unified)](#validation-of-the-configuration-of-plant-objects-rt-unified)
- [Configuring and visualizing KPIs in Runtime (RT Unified)](#configuring-and-visualizing-kpis-in-runtime-rt-unified)
- [Examples (RT Unified)](#examples-rt-unified)
- [Local reporting for Performance Insight (RT Unified)](#local-reporting-for-performance-insight-rt-unified)

## Migrating V16 project (RT Unified)

### Introduction

When you open your V16 project with PFI configuration in TIA Portal V17, you have the option of upgrading the project to V17.

The configured Runtime version of the HMI device must be separately changed to V17. The PFI controls used in the screen must then be updated.

### Delete "Performance overview" control

The "Performance overview" control is no longer supported in V17. If the control is configured in the V16 project, you must delete the control from the screen before you upgrade the project. Configure the "Performance analyzer" control instead.

### Upgrade project

1. Open your V16 project in TIA Portal V17.

   The "Open project" dialog opens:

   ![Upgrade project](images/141778795531_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > When a product is used in the V16 project but is not installed, an upgrade is not possible. Install the missing product and then perform the upgrade.
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

### Updating PFI controls

1. Open a screen in your project.
2. Click the "Update" button in the task card "Toolbox > My controls".

   ![Updating PFI controls](images/141884950027_DV_resource.Stream@PNG-en-US.png)

### Time ranges

The time ranges and refresh rates were harmonized in V17. Due to the change, the configured time ranges and refresh rates of the PFI controls in the V16 project are set to the default setting after the migration.

## Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Applications (RT Unified)](#applications-rt-unified)
- [Requirements (RT Unified)](#requirements-rt-unified)
- [Configuration concept (RT Unified)](#configuration-concept-rt-unified)
- ["Performance indicators" editor and tab (RT Unified)](#performance-indicators-editor-and-tab-rt-unified)
- [KPI, operand and KPI formula (RT Unified)](#kpi-operand-and-kpi-formula-rt-unified)
- [Contexts (RT Unified)](#contexts-rt-unified)
- [Global and used KPIs and operands (RT Unified)](#global-and-used-kpis-and-operands-rt-unified)
- [Global calculation cycle (RT Unified)](#global-calculation-cycle-rt-unified)
- [Microstops (RT Unified)](#microstops-rt-unified)

### Introduction (RT Unified)

#### Introduction

SIMATIC WinCC Unified Performance Insight is an option package in the TIA Portal.

The Performance Insight option helps you to optimize production processes and minimize downtimes. Performance Insight allows you to measure the efficiency of a plant or line and troubleshoot inefficiencies using various controls.

You use Performance Insight to calculate the individual "Key Performance indicators" (KPIs) for individual machines or entire production lines in the plant. You use these plant-specific KPIs to you analyze and examine, for example, the overall effectiveness, the fault frequency or the repair time of the plant. The resulting data provides information on the effectiveness of individual machines and entire production plants. You can react quickly to malfunctions and take countermeasures.

You can visualize the KPIs of your machine or plant on an HMI device during runtime using various charts. You can thus correct the input values at a later date.

![Introduction](images/113044841483_DV_resource.Stream@PNG-de-DE.png)

#### Functional scope

Create and configure the following functions using Performance Insight:

- You create global operands containing values from tags or formulas.
- You define KPIs for calculating and analyzing global operands.
- You define global KPIs for analyzing processes in the plant from one or several operands and KPI formulas.
- You analyze the calculated data and visualize the results in runtime using various controls.

#### Benefits

Detect weak points in production processes and recognize potential for optimization using Performance Insight.

1. Detect problems and performance losses

   You create transparency for the machines in the plant by means of plant-specific KPIs, controls and reports.
2. Find causes

   You calculate the failure times and find the causes in the event of an error.
3. Optimize

   Use the acquired data to analyze vulnerabilities in production processes and optimize the processes in your plant.

---

**See also**

[Applications (RT Unified)](#applications-rt-unified)

### Applications (RT Unified)

#### Overview

Performance Insight supports you in analyzing and optimizing production based on plant-specific KPIs.

For example, you can implement the following KPIs:

- With Overall Equipment Effectiveness (OEE), you analyze the overall effectiveness of the plant with respect to productivity and losses.
- With Mean Time Between Failures (MTBF), you analyze the fault frequency based on the operating time between failures of a unit.
- With Comprehensive Energy Consumption (CEC), you analyze the power consumption in a production cycle in the plant.

![Overview](images/109452874635_DV_resource.Stream@PNG-en-US.png)

#### Area of application and advantages

Evaluating KPIs provides added value in the following areas of application:

- Management and quality assurance

  - You record the failure times, find the causes of the failure times and monitor the efficiency of the plant.
  - You identify the production relationships through the combination of KPIs.
  - You create transparency for the plant as a basis to optimize plant productivity.
- Maintenance and service

  - You analyze weak points in production processes.
  - You can troubleshoot errors in the plant directly at your workstation.
  - You identify and log the events of undesired process behavior.
- Line management and operation of the plant

  - You visualize the analysis results as tables and charts.
  - You correct the logged values retrospectively.
  - You identify weak points in the process through cyclic calculation of the KPIs.

### Requirements (RT Unified)

#### Introduction

Configure and evaluate plant-specific KPIs using Performance Insight. You require a license to use this option. You can find information on licenses in the Plant Intelligence Options Installation Guide, section "Licensing PI Options".

#### Software requirements

To use Performance Insight both in the engineering system and in runtime, you need the following products:

- TIA Portal V17 or higher with STEP 7 Professional
- WinCC Unified Runtime/PC V17
- WinCC Unified Performance Insight option package

#### User knowledge

You have the following knowledge:

- General knowledge about TIA Portal
- Configuration of plant views, plant objects and plant object types

#### Requirements in the TIA Portal

Your TIA Portal project must meet the following requirements so that you can prepare the calculations for WinCC Unified Runtime:

- The project is open.
- Devices and an HMI device are created in the "Devices" tab.
- A plant view is created in the "Plant objects" tab.
- The plant objects of the plant view have tags for communication between a controller and an HMI device.
- An HMI device is assigned to the plant view.

You can find more information under "Working with plant objects and plant hierarchies".

### Configuration concept (RT Unified)

#### Overview

Configuration with Performance Insight is divided into the following tasks:

- Planning and definition of KPIs
- Configuring operands, machine states, KPIs, and calculation cycles
- Configuration of controls for visualization of KPIs

The mapping of the real plant, which you configure in the plant view, serves as the basis for determining and planning individual KPIs.

#### Configuration sequence in the engineering system

You configure KPIs for the plant in the following steps:

1. Define equipment and machines whose data is visualized with Performance Insight as plant object types.
2. You map the plant structure in the plant view.
3. Create interface variables in the plant object types.
4. You configure global operands to transfer the process data for calculating KPIs.
5. You plan and define global KPIs.
6. To calculate the KPIs from the process data, configure the KPI formulas.
7. To log and efficiently compare KPIs, define calculation cycles.
8. You use the global KPIs on the plant object types.
9. Interconnect the interface tags with the operands in the plant object type.
10. To include KPIs of other plant objects in the calculation, configure independent KPIs directly at the plant objects (independent of the global elements).
11. You configure the controls to visualize the KPIs.

#### Visualizing the efficiency of the plant in runtime

With the controls for plant optimization, you have the option of displaying the current evaluations in Runtime. Configure the controls in the engineering system and specify which data is displayed in runtime.

The following controls are available:

- Performance pie chart
- Performance bar chart
- Performance Gantt chart
- Performance control
- Performance analyzer

You can perform the following in Runtime:

- Show the efficiency of the plant at a glance
- Display detailed information on process values
- Compare the data between the machines
- Edit machine states
- Print or export the displayed data
- Insert, delete or modify archived operands or machine states.
- Recalculate logged KPIs

#### Notes on calculating KPIs

You can calculate KPIs as follows:

- In real time after a data change
- As needed for specific data records
- Periodically at defined intervals, e.g. once per day
- In calculating the KPIs, you decide whether short tool lives (microstops) are to be taken into account.

The time required to calculate KPIs depends mainly on the period, the number of recorded values and the number of KPIs to be calculated.

Observe the following notes for calculating KPIs:

- Use only values in the minute range or higher as an update cycle.
- On a WinCC Client, calculate KPIs for a period of up to one day, for example, evaluations after shift end.
- Calculate longer periods on devices without process connection, for example, evaluations covering weeks or a month.

#### Planning and defining KPIs

You are not bound to a fixed workflow for the definition and evaluation of KPIs for the plant.

The steps can also be distributed to multiple people, for example, manager and configuration engineer:

- The manager defines plant objects, KPIs, operands and the calculation.
- The configuration engineer assigns the KPIs to the equipment and interconnects the operands with tags.

> **Note**
>
> **Structuring the plant**
>
> Performance Insight calculates the KPIs, but does not check the evaluations for plausibility. The user is responsible for meaningful KPI definition and linking the relevant parameter/process values.

#### Using SIMATIC WinCC Unified Calendar

You can use the Plant Intelligence option Calendar together with Performance Insight.

After the installation of Calendar, you see the "Calendar" tab in the plant object editor. You have the possibility to configure schedules, shifts and time categories in the calendar and use these time categories when defining the KPIs. In Runtime, the "Calendar Control" control is available to you for creating and managing the schedules.

Performance Insight and Calendar share a time model.

The time model defines:

- Available time categories
- Options for which the time categories are relevant
- How time categories are visualized
- Whether time categories belong to the working time

You define machine states in the time model.

You can find the "Time model" editor in the project tree under "Common data".

You define time categories in the time model. Time categories are combined as time intervals into shifts in Calendar.

#### Using multiuser engineering

If you use Multiuser Engineering when using KPIs, you can only save your changes in the server project view. The changes that you make in the local session are not applied to the server project.

You can find more information on "Multiuser Engineering" under "Multiuser Engineering".

---

**See also**

[Configuring the time model. (RT Unified)](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#configuring-the-time-model-rt-unified)

### "Performance indicators" editor and tab (RT Unified)

#### Introduction

The "Performance indicators" editor and the "Performance indicators" tab are available to you to use Performance Insight.

#### "Performance indicators" editor

In the "Performance indicators" editor, you configure:

- Global KPIs
- Global operands
- Global calculation cycles
- Data logs

The global elements are created once and can be used multiple times on plant object types.

**Opening an editor**

Under "Plant objects > <project name> > Common data", double-click "Performance indicators" or select "Open" in the shortcut menu.

After opening, the editor is available to you as task card on the right side.

**Structure of the editor**

The "Performance indicators" editor consists of the following areas:

!["Performance indicators" editor](images/144846802571_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | "Global KPIs" tab |
| ② | "Global operands" tab |
| ③ | "Global Calculation Cycle" tab |
| ④ | "Data logs" tab |
| ⑤ | Panes: "Global KPIs", "Global operands", "Global time categories and machine states", "Global Calculation Cycle" |
| ⑥ | "KPI formula" editor in the Inspector window |

#### "Performance indicators" tab

With the "Performance indicators" tab, you define the following for your plant object type:

- KPIs
- Operands
- Machine states
- Calculation cycles
- Settings

You drag the configured global elements into the "Performance indicators" tab on the plant object type.

**Opening the tab**

- On the plant object type

  Under "Plant object types", double-click on the desired plant object type.
- On the plant object

  Under "Plant object", double-click on the desired plant object.

### KPI, operand and KPI formula (RT Unified)

#### KPI

The Key Performance Indicator is calculated for a specified period to determine the effectiveness of a plant with respect to power, availability, quality, and other measured variables.

The definition of the KPI contains one or more operands, time categories, and machine states. KPIs are defined for plant object types. To calculate a KPI in Runtime, assign a KPI to the respective plant object type.

#### Operand

An operand returns a process value for calculating KPIs including time stamp.

#### KPI formula

The KPI formula calculates a value from operand values, time categories, and machine states. The result is returned to a KPI.

### Contexts (RT Unified)

Contexts allow you to view plant units according to a certain viewpoint, e.g. according to a certain customer, product, job or shift.

System-generated contexts always belong to a plant object. With installed Performance Insight and Calendar option packages, the contexts are automatically created and executed during runtime:

Example: When a shift starts in Calendar, an archived context value is created with the shift ID.

Each time a context (e.g. "Product") is executed, a log entry is generated in the context log. The logged context saves:

- The context value (e.g. "orange lemonade")
- Start time and end time of the execution time
- The quality code

### Global and used KPIs and operands (RT Unified)

#### Overview

In Performance Insight, you define global elements that you use in plant object types. Used elements inherit all properties of global elements.

#### Global KPIs and operands

First, define the usable global KPIs and operands for your plant:

1. You define the global operands.
2. In the time model, you define time categories and machine states that are included in the calculation of the KPIs.
3. You define the global KPIs.

   You can structure global KPIs using groups.
4. You define the calculation formulas for KPIs based on the global operands, global time categories and global machine states.
5. Define a global calculation cycle.
6. You create a data log to back up the Runtime data.

![Global KPIs and operands](images/131891352203_DV_resource.Stream@PNG-en-US.png)

#### Using global KPIs and operands in plant object types

You use global KPIs, operands, calculation cycles and machine states in plant object types:

1. After you have defined the global elements, you assign these to the plant object types.
2. You define the interface tags at each plant object type.
3. Assign the interface tags to the used operands as source tags.
4. Use the plant object types in the plant hierarchy as plant objects.

![Using global KPIs and operands in plant object types](images/131891355915_DV_resource.Stream@PNG-en-US.png)

#### Retroactive changes in global elements

Changes to global elements also have an effect on used elements.

When a property is changed in a global KPI or operand, all uses of the KPI and operand are automatically adapted. The parameter assignment is retained. When you change the calculation formula of a global KPI, you need to connect the source tag of the added operand in the plant object type.

Operands deleted in the calculation formula are automatically deleted in the plant object types and their instances.

#### Creating independent KPIs (KPI in KPI)

You have the possibility to create an independent KPI directly in the plant object. This KPI is not based on a global KPI. The calculation of the KPI is based exclusively on a KPI of other plant objects (KPI in KPI). Operands, machine states, and time categories are not available.

> **Note**
>
> Independent KPIs that are not based on a global KPI cannot be connected to a calculation cycle. If the name of the independent KPI is already used once, an error message is displayed when loading.
>
> Independent operands cannot be defined.

### Global calculation cycle (RT Unified)

#### Introduction

To calculate and log KPIs cyclically, use global calculation cycles.

This allows you to compare KPIs of different times without having to recalculate them. This approach improves performance and saves computing power.

Logging takes place at fixed intervals and is controlled by various modes:

- Tag
- Context

In addition, a "Condition" can be configured for the individual modes. This condition causes that the calculation cycle can be started and stopped by a Boolean tag.

You can assign multiple calculation cycles to a KPI. The results are stored and can be output with the PFI controls or the Local Reporting option.

#### Tag

Tag that is assigned to the calculation cycle at the plant object type. When the tag value changes, a new calculation cycle starts.

![Tag](images/144619207691_DV_resource.Stream@PNG-en-US.png)

#### Context

Logging can be controlled by a shift in the calendar or a custom context.

![Context](images/144619627659_DV_resource.Stream@PNG-en-US.png)

**Calculation cycle from a shift**

If you use shifts on higher levels in the plant hierarchy you created previously, the shifts also apply to all lower-level objects. A calculation cycle can be triggered from these shifts. The calculation cycle is used in a KPI.

**Example 1:**

If you use a shift on the top level at the "Plant" object, the shift applies to the following lower-level objects:

- Line 1

  - Motor_1
  - Equipment_1
- Line 2

  - Motor_1
  - Equipment_1

![Context](images/131684917643_DV_resource.Stream@PNG-de-DE.png)

The shift is valid for all objects marked green.

**Example 2:**

If you also use a shift at the "Line 1" object, this shift applies in addition to the lower-level objects of "Line 1":

- Line 1

  - Motor_1
  - Equipment_1

![Context](images/131687635851_DV_resource.Stream@PNG-de-DE.png)

This additional shift is valid for all objects marked yellow. These objects now have two shifts.

**Calculation cycle from user-defined context**

A calculation cycle from user-defined context can only be triggered by the defined object in the plant hierarchy. There is no reference to lower-level objects. A calculation cycle can be triggered from this context. The calculation cycle is reused in a KPI.

#### Condition

The calculation cycle can be started or stopped by a Boolean tag.

When the tag value is "TRUE", the active calculation cycle is triggered. When the tag value is "FALSE", the active calculation cycle is stopped immediately.

![Condition](images/144620585227_DV_resource.Stream@PNG-en-US.png)

### Microstops (RT Unified)

Machines or units can be at a standstill for short periods without these downtimes being taken into account in KPIs.

Performance Insight allows setting machine states as stop states (microstops). When calculating KPIs, you can specify whether these short-term machine states are to be taken into account.

#### Using microstops

To use microstops for a plant object type, follow these steps:

1. Define a global machine state with the "Stop state" setting.
2. Define the microstop time and the microstop unit for the plant object type.
3. Use the machine state in a KPI formula.

## Configuring KPIs (RT Unified)

This section contains information on the following topics:

- [Configuration sequence (RT Unified)](#configuration-sequence-rt-unified)
- [Configuring global operands of the "Counter" type (RT Unified)](#configuring-global-operands-of-the-counter-type-rt-unified)
- [Configuring global operands of the type "Numerical operands" (RT Unified)](#configuring-global-operands-of-the-type-numerical-operands-rt-unified)
- [Configuring global calculation cycles (RT Unified)](#configuring-global-calculation-cycles-rt-unified)
- [Time categories and machine states (RT Unified)](#time-categories-and-machine-states-rt-unified)
- [Configuring KPIs (RT Unified)](#configuring-kpis-rt-unified-1)
- [Example: Calculating quality rate (RT Unified)](#example-calculating-quality-rate-rt-unified)
- [Example: Using KPIs from other plant objects (RT Unified)](#example-using-kpis-from-other-plant-objects-rt-unified)
- [Example: Using global calculation cycle (RT Unified)](#example-using-global-calculation-cycle-rt-unified)
- [Exporting and importing configuration data (RT Unified)](#exporting-and-importing-configuration-data-rt-unified)

### Configuration sequence (RT Unified)

#### Introduction

The existing plant structure represents the starting point for defining a standardized KPI concept in object-oriented configuration.

Map the components of your plant by means of the plant object types that you use as instances in the plant view. You define global operands and KPIs in the "Performance indicators" global editor, and use standardized KPIs in plant object types. If you want to create a KPI that is based on other KPIs, configure the KPI directly at the plant object.

The definition and use of KPIs can be illustrated as follows:

![Introduction](images/136521758219_DV_resource.Stream@PNG-en-US.png)

#### Requirements

- You have experience in configuring with WinCC.
- The project has been created in the TIA Portal.
- The HMI device WinCC Unified SCADA RT has been created.
- The plant is mapped in the plant view.
- The HMI device is assigned to the plant view.
- Process tags have been created in the project.

#### Configuration sequence in the plant structure

The configured plant view is used as the basis for creating and configuring the KPIs and operands for the plant.

Configure global KPIs and operands in the "Performance indicators" editor.

1. Configure global operands to transfer the process data for calculating KPIs:

   - Counters
   - Numerical operands
2. In the "Time model" editor you create time categories and corresponding machine states.
3. You create global, plant-specific KPIs.
4. Configure a KPI formula for each KPI to calculate the KPIs. To do this, use the following:

   - Counters
   - Numerical operands
   - Time categories
   - Machine states
5. You assign the KPIs to the plant object types.
6. You select interface tags for the tags that provide data to the operands.
7. Use global calculation cycles to log the calculated KPIs.

The "Performance indicators" task card provides an overview of the configured global KPIs, operands, and calculation cycles.

---

**See also**

### Configuring global operands of the "Counter" type (RT Unified)

#### Introduction

As counters you store, for example, the number of products manufactured within a certain quality. This gives you the possibility to evaluate the quality of production for a period of time or to compare the production results of individual machines or equipment.

You define global operands in the "Global operands" tab and use them when creating formulas for the global KPIs.

| Property |  | Description |
| --- | --- | --- |
| General | Name | Unique, language-neutral name of the operand.  The operand name must contain a maximum of 128 characters.  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Language-dependent display name of the operand, which you store in various languages. |  |
| Unit of measure | Unit of measure for this global operand. Use up to 16 characters. |  |
| Counter type | - Incremental   The delta value is written to the tag on every change of the source value. The values are automatically logged in the Performance Insight database. - Manually   The value is applied manually. The values are automatically logged in the Performance Insight database. - Incremental with limits   Like an "Incremental" counter type, high limit and low limit are defined in addition. |  |
| Tag | Interface tag that manages the counter value. You configure the tag at the use of the operand in the plant object type. |  |
| Limits  (High limit/ Low limit) | Limit type | - None (default setting)   Only the defined limits of the tags apply. - Constant   You define the limits using constant values. - Dynamic   You define the tags that specify the limits. |
| Limit value | Limit value for the "Constant" limit type.  The permitted value range is between -1.7E + 308 to 1.7E + 308. |  |
| Dynamic limit | A tag that belongs to the plant object types (e.g. Line) and defines the corresponding dynamic value. |  |
| Description |  | Brief description that serves as a tooltip in runtime and is shown in reports.  The description can contain up to 32767 characters. |

The "Limits" property is only displayed when the "Incremental with limits" counter type is set.

#### Requirements

- A project has been created.
- The "Performance indicators" editor is open.

#### Configuring counters

1. Expand the "Counter" entry in the "Global operands" tab.
2. Click "Add".

   A new global operand of the type "Counter" is created.
3. Enter a meaningful name for the counter, for example, "PartsProduced".
4. Open the Inspector window.
5. Specify the counter type under "Properties > General > General":

   - Incremental
   - Incremental with limits
   - Manual
6. If you have selected the "Incremental with limits" counter type, define the high limit and low limit for the counter under "Properties > General > Limits".
7. Under "Properties > General > Description", enter a comment for the counter that will appear as a tooltip in runtime.

#### Result

Configured global operands are available for use in KPIs in the "Performance indicators > Global operands" task card.

### Configuring global operands of the type "Numerical operands" (RT Unified)

#### Introduction

You define numeric operands in the "Global operands" tab and use them when creating formulas for the global KPIs.

| Property |  | Description |
| --- | --- | --- |
| General | Name | Unique, language-neutral name of the operand.  The operand name must contain a maximum of 128 characters.  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Language-dependent display name of the operand, which you store in various languages. |  |
| Unit of measure | Unit of measure for this global operand. Use up to 16 characters. |  |
| Tag | Interface tag that manages the value. You configure the tag at the use of the operand in the plant object type. |  |
| Description |  | Brief description that serves as a tooltip in runtime and is shown in reports.  The description can contain up to 32767 characters. |

#### Requirements

- A project has been created.
- The "Performance indicators" editor is open.

#### Configuring numerical operands

1. Expand the "Numerical operands" entry in the "Global operands" tab.
2. Click "Add".

   A new global operand of the type "Numerical operand" is created.
3. Enter a meaningful name for the numerical operand.
4. Open the Inspector window.
5. Under "Properties > General > Description", enter a comment for the operand that will appear as a tooltip in runtime.

#### Result

Configured global operands are available for use in KPIs in the "Performance indicators > Global operands" task card.

### Configuring global calculation cycles (RT Unified)

#### Introduction

You define a calculation cycle to calculate the KPIs during a production process and archive them in the database. The archived KPIs can then be output as a report.

You can find additional information under [Local reporting for Performance Insight](#local-reporting-for-performance-insight-rt-unified)

If you want to additionally use a condition to trigger a calculation cycle, configure the condition on the plant object type. You can find additional information under [Configuring KPIs with global calculation cycle](#configuring-kpis-with-global-calculation-cycle-rt-unified)

You define global calculation cycles in the "Global calculation cycle" tab:

| Property |  | Description |
| --- | --- | --- |
| General | Name | Unique, language-neutral name of the calculation cycle.  The name cannot contain more than 128 characters.  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Language-dependent display name of the calculation cycle, which you store in various languages. |  |
| Calculation | Mode | Specifies how the calculation cycle is initiated:  - Tag   A calculation cycle is started by changing the tag value. - Context   A calculation cycle is started by the start of a shift in the calendar or by a custom context. |
| Tag | Tag that initiates the calculation cycle.  Only available in "Tag" mode.  You configure the tag at the use of the calculation cycle in the plant object type. |  |
| Context provider | Specifies the tool that is used to control the calculation cycle:  - Calendar - Custom   Only available in "Context" mode. |  |
| Context | Specifies the context that controls the calculation cycle:  - ShiftID    For the "Calendar" context provider - String   For the "Custom" context provider |  |
| Interval value | Duration of a cycle that serves as the time span to calculate the KPI.  If the value is 0, the calculation cycle has no time span. |  |
| Unit | Unit of the interval:  - Minutes - Hours - Days - Weeks - Month |  |
| Description |  | Brief description that serves as a tooltip in runtime and is shown in reports.  The description can contain up to 32767 characters. |

#### Requirement

- A project has been created.
- The "Performance indicators" editor is open.

#### Creating a calculation cycle with tag

1. Select the "Global calculation cycle" tab.
2. Click "Add".

   A new global calculation cycle is created.
3. Enter a meaningful name for the global calculation cycle.
4. Open the Inspector window.
5. Select the "Tag" mode under "Properties > General > Calculation > Mode".

   Alternative: In the row of your created calculation cycle, select the "Tag" entry from the drop-down list under "Data type".
6. Specify the length of the calculation cycle under "Properties > General > Calculation > Interval value".
7. Specify the unit for the calculation cycle under "Properties > General > Calculation > Unit".
8. Under "Description > Description", enter a comment for the calculation cycle that will appear as a tooltip in Runtime.

Specify the tag as soon as the calculation cycle is used in a KPI, and this KPI is assigned to a plant object type.

#### Creating a calculation cycle via a calendar or custom context

To start the calculation cycle via a calendar, a calendar needs to be configured.

You can find additional information in the Calendar manual under "Defining time schedules for production lines and stations".

1. Select the "Global calculation cycle" tab.
2. Click "Add".

   A new global calculation cycle is created.
3. Enter a meaningful name for the global calculation cycle.
4. Open the Inspector window.
5. Select the "Context" mode under "Properties > General > Calculation > Mode".

   Alternative: In the row of your created calculation cycle, select the "Context" entry from the drop-down list under "Data type".
6. Specify whether the calculation cycle is started via a calendar or custom under "Properties > General > Calculation > Context provider".
7. Specify the length of the calculation cycle under "Properties > General > Calculation > Interval value".
8. Specify the unit for the calculation cycle under "Properties > General > Calculation > Unit".
9. Under "Description > Description", enter a comment for the calculation cycle that will appear as a tooltip in Runtime.

> **Note**
>
> **Availability of calendar**
>
> If the context provider "Calendar" or the selected context is not available, an alarm is output in Runtime.

#### Result

Configured global calculation cycles are available for use in KPIs in the "Performance indicators > Global calculation cycle" task card.

### Time categories and machine states (RT Unified)

This section contains information on the following topics:

- [Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
- [Configuring machine states (RT Unified)](#configuring-machine-states-rt-unified)
- [Configuring machine state at the plant object type (RT Unified)](#configuring-machine-state-at-the-plant-object-type-rt-unified)

#### Configuring time categories (RT Unified)

##### Introduction

The Plant Intelligence options SIMATIC WinCC Unified Performance Insight and SIMATIC WinCC Unified Calendar share a time model.

The time model defines:

- Available time categories
- Options for which the time categories are relevant
- How time categories are visualized
- Whether time categories belong to the working time

You define the time categories that you use in connection with Performance Insight to evaluate and visualize KPIs in runtime. You have the option with each performance control to evaluate the period by calendar.

You define time categories in the "Time model" editor.

| Property | Description |
| --- | --- |
| Name | Unique, language neutral name of the time category  The name of the time category can contain a maximum of 128 characters.  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Language-dependent display name of the time category, which you store in various languages. |
| Description | Brief description that serves as a tooltip in runtime and is shown in reports.   The description can contain up to 32767 characters. |
| Color | Color that is used for visualization. |
| Relevance | Information about where the time category can be used. |

> **Note**
>
> You create machine states within a time category.

##### Requirement

- The plant hierarchy and plant objects have been configured.

##### Procedure

1. In the project tree, open the "Time model" editor under "Common data" in the "Plant objects" tab.
2. To create a time category, double-click the "<Add>" entry in the top line of the editor or select the button ![Procedure](images/122813604363_DV_resource.Stream@PNG-de-DE.png) "Add time category".
3. To create additional time categories, select an existing time category and click "Add time category" ![Procedure](images/122813604363_DV_resource.Stream@PNG-de-DE.png).
4. Open the Inspector window under "Properties > General > General".
5. Define the properties of the time category in the Inspector window.

   You can also change the properties in the table overview of the editor.

##### Result

Configured time categories are available for use in KPIs in the "Performance indicators > Global time categories and machine states" task card.

##### Importing and exporting the time model

- To import time categories from an Excel workbook, select the button ![Importing and exporting the time model](images/122819761291_DV_resource.Stream@PNG-de-DE.png) "Import time categories".
- To export the time categories to an Excel workbook, select the "Export time categories" button ![Importing and exporting the time model](images/122819471115_DV_resource.Stream@PNG-de-DE.png).

> **Note**
>
> Do not rename the sheet if you are planning on a reimport.

---

**See also**

[Configuring the time model. (RT Unified)](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#configuring-the-time-model-rt-unified)

#### Configuring machine states (RT Unified)

##### Introduction

With the help of machine states, you record the states of a machine in your plant, for example, to evaluate runtimes, standstill times, and utilization of the machine. Each machine state is assigned to a time category.

Define machine states in the "Time model" editor and use them when creating formulas for the global KPIs.

| Property |  | Description |
| --- | --- | --- |
| General | Name | Unique, language-neutral name of the machine state.  The name cannot contain more than 128 characters.  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Language-dependent display name of the machine state, which you store in various languages. |  |
| Default state | The user-defined state that is displayed by default, e.g. on connection loss. |  |
| Color | Is transferred automatically by the defined time category. |  |
| Priority | Priority for this state as compared to other machine states prevailing at the same time.  The information must be unique and different for each machine state. |  |
| Sort index | The machine states are sorted in runtime according to this index. |  |
| Machine state type | Data type | When assigning a KPI, configure also the data type for the machine state:  - "Bit-based machine state" is set via the bit values. The corresponding bits are controlled by means of conditions. - "Value-based machine state" is specified automatically by a numerical value or a value range. This value is set as default value. |
| Source | Specifies the source tag.  Define the source tag in the editor of the plant object type in the "Performance indicators > Machine states" tab. |  |
| Condition | - "1" - State is active when the bit is set. - "0" - State is active when the bit is not set. - "X" - The bit is not considered in the evaluation of the state.  The condition is only relevant for the bit-based machine state. |  |
| High limit | Specifies the high limit.  The high limit is only relevant for the value-based machine state. |  |
| Low limit | Specifies the low limit.  High and low limit can have the same value assigned. In this case, the machine state only uses this one value. The limits must not overlap with the limits of other machine states.  The low limit is only relevant for the value-based machine state. |  |
| Stop state | Stop state | If this option is selected, the machine state is defined as the "Stop state". This stop state can be configured with the microstop settings in the plant object type. |

> **Note**
>
> **Time and unit of microstops**
>
> In the editor of the plant object type in the "Performance indicators > Settings" tab, specify the microstop time and unit.

##### Requirements

- A project has been created.
- The "Time model" editor is open.

##### Defining time categories

To define the machine states, first define time categories. You create time categories under "Common data > Time model". You can find additional information at "[Configuring time categories](#configuring-time-categories-rt-unified)".

You can find additional information on creating and editing time categories in the documentation of WinCC Unified Option "Calendar".

##### Configuring the machine state

1. In the project tree, open the "Time model" editor under "Common data" in the "Plant objects" tab.
2. To create a machine state, select a time category in the editor.
3. Select the button ![Configuring the machine state](images/122819462539_DV_resource.Stream@PNG-de-DE.png) "Add machine state".
4. Open the Inspector window under "Properties > General > General" and define the properties.

   You can also change some properties in the table overview of the editor.
5. Select the "Properties > General > Description" area. Define a brief description that serves as a tooltip in Runtime and is shown in reports.

   The description can contain up to 32767 characters.

##### Result

Configured machine states are available for use in KPIs in the "Performance indicators > Global time categories and machine states" task card.

#### Configuring machine state at the plant object type (RT Unified)

##### Introduction

For the configured machine state to be visible in Runtime, it is configured at the plant object type.

##### Requirement

- A machine state has been created in the "Time model" editor.
- The editor of a plant object type is open.

##### Procedure

1. In the editor of the plant object type, switch to the "Performance indicators > Machine states" tab.
2. In the Inspector window, configure the source tag in the "Properties > General > Machine state type" area.

   If you specify the source for a machine state, the value is transferred to all machine states used in this plant object type.

   > **Note**
   >
   > **Specific properties for plant object types**
   >
   > You can edit the following machine state properties in the "Performance indicators" editor or in the editor of the plant object type in the "Performance indicators" tab:
   >
   > - Data type
   > - Condition (only for bit-based machine state)
   > - High limit (only for value-based machine state)
   > - Low limit (only for value-based machine state)
   >
   > Changes to these properties in the plant object type editor are not transferred to the "Performance indicators" editor.
3. The "Used in KPI / Plant object relevant" column indicates whether a machine state can be visualized via a KPI or directly.

   ![Procedure](images/144851206411_DV_resource.Stream@PNG-en-US.png)

   | Symbol | Meaning |
   | --- | --- |
   | ![Procedure](images/124398118283_DV_resource.Stream@PNG-de-DE.PNG) | The machine state can be visualized in Runtime, as it is used in a KPI.   The option is write-protected. |
   | ![Procedure](images/124398109707_DV_resource.Stream@PNG-de-DE.PNG) | The machine state can be visualized in Runtime without being used in a KPI.  Select the check box. |
   | ![Procedure](images/124397793931_DV_resource.Stream@PNG-de-DE.PNG) | The machine state is not visualized in Runtime.  Clear the check box. |

##### Defining the microstop

Specify the length of a microstop in the editor of the plant object type in the "Performance indicators> Settings" area. When calculating a KPI, microstops can be either included, omitted, or displayed separately.

**Settings**

| Symbol | Meaning |
| --- | --- |
| Microstop time | Size of the period that represents a microstop for this machine state. |
| Microstop unit | Selection list, unit for the microstop: Minutes, seconds, milliseconds  Default value: 0 minutes |

### Configuring KPIs (RT Unified)

This section contains information on the following topics:

- [Configure global KPIs (RT Unified)](#configure-global-kpis-rt-unified)
- [KPI formula (RT Unified)](#kpi-formula-rt-unified)
- [Assigning a KPI to the plant object type (RT Unified)](#assigning-a-kpi-to-the-plant-object-type-rt-unified)
- [KPI parameter assignment (RT Unified)](#kpi-parameter-assignment-rt-unified)
- [Configuring KPIs with global calculation cycle (RT Unified)](#configuring-kpis-with-global-calculation-cycle-rt-unified)
- [Configuring independent KPIs on a plant object (RT Unified)](#configuring-independent-kpis-on-a-plant-object-rt-unified)

#### Configure global KPIs (RT Unified)

##### Introduction

You create global KPIs in the "Global KPIs" tab of the ["Performance indicators" editor](#global-and-used-kpis-and-operands-rt-unified).

For each KPI, you define a calculation formula and how this KPI is displayed.

##### Targets and thresholds

You have the option of defining target and thresholds in the KPI. The "Constant" setting must be selected for the target type or limit type of each property.

You can define the following properties:

- Target
- High limit 2
- High limit 1
- Low limit 1
- Low limit 2

The values must rise from "Low limit 2" to "Target" and fall from "High limit 2" to "Target" (High limit 2 > High limit 1 > Target > Low limit 1 > Low limit 2).

##### Requirements

- A project has been created.
- Global operands, time categories, and machine states required for the KPI are configured.
- The "Performance indicators" editor is open.

##### Configure global KPIs

1. In the work area, click "<Add>" under "Global KPIs".

   A new KPI is created.
2. Assign a descriptive display name for the KPI in the Inspector window in the "Properties" tab under "General > General".
3. Under "Unit of measure", specify the unit of measure in which the KPI is calculated.
4. In the Inspector window under "General > Color > Bar color", specify the color with which the bar for this KPI is visualized in runtime.
5. Under "General > Color > Text color", specify the color in which the text label for the KPI is displayed in runtime.
6. Create the calculation formula for the KPI under "KPI formula".
7. Define a type and value for each property under "Target and thresholds".
8. Enter a brief description that serves as a tooltip in Runtime and is shown in reports.

   The description can contain up to 32767 characters.

> **Note**
>
> Set the calculation cycles and dynamic targets and thresholds as soon as you use the KPI in a plant object type. To do this, use the "Performance indicators" tab in the editor of the plant object type.

**Group KPIs**

1. In the work area, right-click "Add" under "Global KPIs".
2. Select "Add a new group" in the shortcut menu.
3. Assign a meaningful name to the group.
4. Confirm your entry with the <Enter> key or by clicking on any field.
5. Right-click on the name of a group in the work area under "Global KPIs".
6. Select "Add new KPI" or "Add a new group" again in the shortcut menu.
7. Move KPIs or groups using drag & drop. To do this, drag the icon of the KPI or group to a different location.

**Delete KPIs**

1. Click the left, dark gray column in front of the entry of the KPI that you want to delete.
2. Press <Del> or select "Delete" in the shortcut menu.  
   The selected KPI or group is deleted without a prompt for confirmation.

##### Result

Configured KPIs are available in the "Performance indicators > Global KPIs" task card.

---

**See also**

[Configuring a KPI formula (RT Unified)](#configuring-a-kpi-formula-rt-unified)
  
[Frequently used KPIs, microstops and scripts (RT Unified)](#frequently-used-kpis-microstops-and-scripts-rt-unified)

#### KPI formula (RT Unified)

This section contains information on the following topics:

- [Formula syntax (RT Unified)](#formula-syntax-rt-unified)
- [Evaluation types (RT Unified)](#evaluation-types-rt-unified)
- [Arithmetic operators (RT Unified)](#arithmetic-operators-rt-unified)
- [Aggregate functions (RT Unified)](#aggregate-functions-rt-unified)
- [Using KPI in KPI (RT Unified)](#using-kpi-in-kpi-rt-unified)
- [Configuring a KPI formula (RT Unified)](#configuring-a-kpi-formula-rt-unified)

##### Formula syntax (RT Unified)

> **Note**
>
> Syntax parts within pointed brackets in this section must be replaced by other syntax parts during entry in the formula editor, for example, by a specific arithmetic operator, the name of a function or an operand, an operand type or evaluation type.

###### Introduction

You configure KPI formulas in the KPI formula editor for every global KPI.

The following elements are permitted in the calculation of a KPI formula:

- Counters
- Numerical operands
- Other KPIs
- Time categories
- Machine states
- Aggregate functions
- Arithmetic operators

###### Syntax

You create the formulas for calculating the KPIs in the "KPI formula" editor according to the following pattern:

| Operation | Syntax | Example |
| --- | --- | --- |
| Arithmetic operators  (only within aggregate functions or as a mathematical operation of aggregate functions) | <Operand> <Operator> <Operand> | `SUM(NumericOperands("Speed").Value * NumericOperands("Speed").Duration)` |
| Aggregate functions | <Aggregate function name>(<Operand>) | `AVG(NumericOperands("Speed_1").Value)` |
| Evaluation types | <Operand type>("<operand name>").<evaluation type> | `SUM(MachineStates("Running").Occurrences)` |
| KPI in KPI | KPIs("<NamePlantHierarchy>/<NamePlantObject>/>NameLowerLevelPlantObject>/<NameKPI>") | `KPIs("Plantview/Station_1/Motor_1/Performance")` |

> **Note**
>
> **Restrictions for the formula syntax**
>
> KPIs cannot be used reciprocally in formulas.

> **Note**
>
> Operands, time categories, and machine states must only be used within aggregate functions.
>
> The aggregate functions **SUM**, **AVG**, **AVG_T, VAR**, **STD**, **VARP**, **STDP**, **MIN**, and **MAX** are supported.

The syntax highlighting in the formula editor helps you to distinguish between different operands and detect errors. Invalid elements and syntax errors are highlighted in a formula with a red text color, and you will receive a tooltip.

![Syntax](images/113127135627_DV_resource.Stream@PNG-en-US.png)

##### Evaluation types (RT Unified)

###### Introduction

Evaluation types determine which values are used for the calculation. The following evaluation types are available in the formula editor:

| Evaluation type | Meaning |
| --- | --- |
| Value | Specifies that the value of the numerical operand is calculated in the formula.  Only available for numerical operands. |
| Occurrences | Default value  Specifies that the occurrence of the operand is calculated in the formula. |
| Duration | Default value  Specifies that the duration of the state is calculated in the formula. |
| Planned | Specifies that the time category is requested from the calendar. For the query to take place, the time category or at least one lower-level time category must be marked as "Relevant for calendar" in the time model during the configuration. If the Planned parameter is not specified, the data from the machine states is requested.  Only available as an option for time categories. |
| WithoutMicroStops | Microstops are not taken into consideration.  Only available as an option for time categories and machine states. |
| OnlyMicroStops | Only microstops are considered.  Only available as an option for time categories and machine states. |

###### Operands

For operands, the evaluation types must be specified as follows:

- "Counter" operand type: Evaluation type must not be specified.
- "Numerical operand" operand type: Evaluation type must be specified.

| Syntax | Example |
| --- | --- |
| Counters("<Counter name>") | `SUM(Counters("TotalIncrementWithLimits"))` |
| NumericOperands("<Name of the numerical operand>").Value | `SUM(NumericOperands("Speed_1").Value)` |
| NumericOperands("<Name of the numerical operand>").Duration | `SUM(NumericOperands("Speed_1").Duration)` |
| NumericOperands("<Name of the numerical operand>").Occurences | `SUM(NumericOperands("Speed_1").Occurrences)` |

###### Time categories

For time categories, the evaluation type "Duration" or "Occurences" must be used. A second optional evaluation type is also available.

| Syntax | Example |
| --- | --- |
| TimeCategories("<Name of the time category>").Duration | `SUM(TimeCategories("ReducedSpeed").Duration)` |
| TimeCategories("<Name of the time category>").Duration.Planned | `SUM(TimeCategories("ReducedSpeed").Duration.Planned)` |
| TimeCategories("<Name of the time category>").Duration.WithOutMicroStops | `SUM(TimeCategories("ReducedSpeed").Duration.WithOutMicroStops)` |
| TimeCategories("<Name of the time category>").Duration.OnlyMicroStops | `SUM(TimeCategories("ReducedSpeed").Duration.OnlyMicroStops)` |
| TimeCategories("<Name of the time category>").Occurrences | `SUM(TimeCategories("ReducedSpeed").Occurrences)` |
| TimeCategories("<Name of the time category>").Occurrences.Planned | `SUM(TimeCategories("ReducedSpeed").Occurrences.Planned)` |
| TimeCategories("<Name of the time category>").Occurrences.WithOutMicroStops | `SUM(TimeCategories("ReducedSpeed").Occurrences.WithOutMicroStops)` |
| TimeCategories("<Name of the time category>").Occurrences.OnlyMicroStops | `SUM(TimeCategories("ReducedSpeed").Occurrences.OnlyMicroStops)` |

###### Machine states

For machine states, the evaluation type "Duration" or "Occurences" must be used. A second optional evaluation type is also available.

| Syntax | Example |
| --- | --- |
| MachineStates("<Name of the machine state>").Duration | `SUM(MachineStates("Running").Duration)` |
| MachineStates("<Name of the machine state>").Duration.WithOutMicroStops | `SUM(MachineStates("Running").Duration.WithOutMicroStops` |
| MachineStates("<Name of the machine state>").Duration.OnlyMicroStops | `SUM(MachineStates("Running").Duration.OnlyMicroStops` |
| MachineStates("<Name of the machine state>").Occurrences | `SUM(MachineStates("Running").Occurrences)` |
| MachineStates("<Name of the machine state>").Occurrences.WithOutMicroStops | `SUM(MachineStates("Running").Occurences.WithOutMicroStops` |
| MachineStates("<Name of the machine state>").Occurences.OnlyMicroStops | `SUM(MachineStates("Running").Occurences.OnlyMicroStops` |

> **Note**
>
> **Time and unit of microstops**
>
> In the editor of the plant object type in the "Performance indicators > Settings" tab, specify the microstop time and unit.

##### Arithmetic operators (RT Unified)

With arithmetic operators, you calculate numerical values, such as the product of two counters.

The following arithmetic operators are available:

| Operator | Meaning |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Division with remainder |

##### Aggregate functions (RT Unified)

###### Introduction

Aggregate functions can be operands, time categories, machine states, or related arithmetic operations.

The following aggregate functions are available:

| Function | Meaning | Example |
| --- | --- | --- |
| SUM | Adds one or more values to form a sum. | SUM(Counters("Counter_1")) SUM(Counters("Counter_1") + NumericOperands("NumericOperand_1").Value) |
| AVG | Calculates the arithmetic average between the given values. | AVG(TimeCategories("Category_1").Occurences) AVG(Counters("Counter_1") + Counters("Counter_2")) |
| AVG_T | Calculates the time-weighted mean value between the given values. The timestamps of the individual values are subtracted for this purpose.  It can be used only for the "Counter" operand type or for the "Numeric operand" type in conjunction with the "Value" evaluation type. | AVG_T(NumericOperands("NumericOperand_1").Value) |
| VAR | Estimates the variance based on a random sample. This function assumes that the values represent a random sample of the entire population. | VAR(NumericOperands(“NumericOperand_1”).Value) VAR(Counters("Counter_1") + Counters("Counter_2")) |
| STD | Estimates the standard deviation based on a random sample. | STD(NumericOperands(“NumericOperand_1”).Value) STD(Counters("Counter_1") + Counters("Counter_2")) |
| VARP | Estimates the statistical variance based on the entire population. | VARP(NumericOperands(“NumericOperand_1”).Value) VARP(Counters("Counter_1") + Counters("Counter_2")) |
| STDP | Calculates the standard deviation based on an entire population. | STDP(NumericOperands(“NumericOperand_1”).Value) STDP(Counters("Counter_1") + Counters("Counter_2")) |
| MIN | Calculates the minimum of the values. | MIN(NumericOperands(“NumericOperand_1”).Value) MIN(Counters("Counter_1") + Counters("Counter_2")) |
| MAX | Calculates the maximum of the values. | MAX(NumericOperands(“NumericOperand_1”).Value) MAX(Counters("Counter_1") + Counters("Counter_2")) |

> **Note**
>
> **Restrictions for the aggregate functions**
>
> - The use of an aggregate function in another aggregate function is not permitted.
> - Use of KPIs in aggregate functions is not permitted.

###### Special feature of aggregate functions

When you use aggregate functions in combination with an evaluation type, such as "Occurences", there are various ways to calculate numerical operands.

Timeslicing takes place with the aggregate functions.

**Add values**

The number of changed values within the calculation period are added.

The start value is included.

![Special feature of aggregate functions](images/131629501963_DV_resource.Stream@PNG-de-DE.png)

| Example | Result |
| --- | --- |
| `SUM(NumericOperands("Speed_1").Occurrences)+SUM(NumericOperands("Speed_2").Occurrences)` | 2+3=5 |

**Add time stamps**

The number of time stamps of all operands are added.

An output time stamp is added even if no new value is output by the operand.

![Special feature of aggregate functions](images/131650003339_DV_resource.Stream@PNG-de-DE.png)

| Example | Result |
| --- | --- |
| `SUM(NumericOperands("Speed_1").Occurrences)+NumericOperands("Speed_2").Occurrences)` | 4+4=8 |

##### Using KPI in KPI (RT Unified)

You can use other KPIs in a KPI formula:

- KPIs of the same plant object type
- KPIs of other plant objects

In a formula, you define both KPIs from lower-level plant objects and KPIs from plant objects of other hierarchy levels.

The syntax for using KPIs from other plant objects in a KPI is as follows:

`KPIs("<Name_PlantHierarchy>/<Name_PlantObject>/<Name_LowerLevelPlantObject>/<Name_KPI>")`

The path of a plant object in the plant hierarchy serves as plant object path.

> **Note**
>
> Observe the following notes on the usage of KPIs in KPI formulas:
>
> - KPIs must not be used in aggregate functions.
> - KPIs cannot be used reciprocally in formulas.

##### Configuring a KPI formula (RT Unified)

###### Configuring a KPI formula

In the calculation formula, define dependencies between the following elements:

- Global operands
- Time categories
- Machine states
- Other KPIs

To configure a KPI formula, follow these steps:

1. Open the "Performance indicators" editor.
2. Select a KPI in the "Global KPIs" tab.
3. In the Inspector window, switch to "General > KPI formula" in the "Properties" area.
4. Define the KPI formula:

   - Drag and drop global operands, time categories, and machine states from the "Performance indicators" task card to the definition area of the formula editor.
   - Set the calculation using arithmetic operators and aggregate functions.

   Alternatively, enter the operand, taking the [syntax rules](#formula-syntax-rt-unified) into account.

###### Configuration support

Incomplete or incorrect configurations are shown with a colored background in the KPI editor.

The validity of the entries in the "Performance indicators" editor is constantly checked. When an operand is no longer valid, for example, or the formula syntax is not observed, the corresponding area is highlighted in red. If there are several errors, the errors are marked in red step-by-step. You will receive a tooltip.

![Configuration support](images/124266403851_DV_resource.Stream@PNG-de-DE.PNG)

**Support with inputting formulas**

Autocomplete offers suggestions during input.

![Configuration support](images/124267129227_DV_resource.Stream@PNG-en-US.png)

Examples:

- When the single letter "C" is entered, the entries permitted at this point are offered.
- When a period is entered after an operand, the permitted evaluation types are offered.

#### Assigning a KPI to the plant object type (RT Unified)

##### Introduction

After you have configured the global KPIs and operands, assign the global KPIs to the individual plant object types. The operands configured in the KPI are automatically visible at the plant object type in the "Performance indicators > Operands" tab.

##### Requirements

- A plant object type is configured.
- The plant hierarchy is configured.
- Global operands, time categories, and machine states required for the KPI are configured.
- At least one global KPI is configured.

##### Assigning KPIs

1. Open the "Performance indicators > KPIs" tab in the editor of a plant object type.
2. To view the previously configured KPIs and operands at a glance, click on the "Performance indicators" task card.
3. Drag-and-drop the KPI relevant to this plant object type from the "Performance indicators" task card to the "KPIs" area.

   A reuse of the KPI and the operands used is created.
4. Open the Inspector window under "Properties > General > Targets and thresholds".
5. Define dynamic targets and thresholds for the KPI.
6. Change to the "Operands" area.
7. Configure the properties of the operands, for example, the tag.

**Note**

To edit global KPIs and operands, click on the "Open Performance indicators editor" button ![Assigning KPIs](images/110183660171_DV_resource.Stream@PNG-de-DE.png).

| Symbol | Meaning |
| --- | --- |
| ![Assigning KPIs](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for effective procedure** |
| To use a number of KPIs in a plant object type, you have the following option:  - Select several global KPIs by multiple selection and add them to the "KPI" area of the plant object type using drag-and-drop. |  |

##### Result

A global KPI is reused on the plant object type.

---

**See also**

[Configuration sequence (RT Unified)](#configuration-sequence-rt-unified)
  
[KPI parameter assignment (RT Unified)](#kpi-parameter-assignment-rt-unified)
  
[Configure plant object types (RT Unified)](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#configure-plant-object-types-rt-unified)

#### KPI parameter assignment (RT Unified)

##### Introduction

You configure the tags of the operands in the usage at the plant object type. In this way, data of the plant objects can be calculated and combined in the KPIs. The tags that need to be defined depend on the operand type.

Interconnect the tags with the interface tags that you configured beforehand at the corresponding plant object type.

##### Requirements

- The plant view is configured.
- A plant object type is configured.
- Interface tags are created at the plant object type.
- KPI is assigned to a plant object type.

##### KPI parameter assignment

To supply the operands with process data, you configure the tags at the use of the KPI at the plant object type.

1. Open the respective plant object type.
2. To expand all operands, open the overview of all operands used using the "Expand hierarchical structure" button ![KPI parameter assignment](images/126132978827_DV_resource.Stream@PNG-de-DE.png).
3. Select the desired operand.
4. Select the interface tag from the data structure in the Inspector window under "General > General > Source".

##### Result

You have configured a KPI by connecting the operand with the interface tag of the plant object type.

---

**See also**

[Assigning a KPI to the plant object type (RT Unified)](#assigning-a-kpi-to-the-plant-object-type-rt-unified)
  
[Configure plant object types (RT Unified)](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#configure-plant-object-types-rt-unified)

#### Configuring KPIs with global calculation cycle (RT Unified)

##### Introduction

You can configure a calculation cycle.

In addition to the interface tag, you configure a tag that triggers or stops the calculation cycle in runtime. The tag must be defined as Bool. When the tag value is "TRUE", the active calculation cycle is triggered. When the tag value is "FALSE", the active calculation cycle is stopped immediately. You configure the tag at the plant object type in the "Calculation cycle" tab under "Properties > General > Calculation > Condition".

##### Requirement

- Global KPIs have been created.
- KPIs are assigned to at least one plant object type.
- Interface tags have been created.
- The calculation cycle has been created.

  You can find additional information at [Configuring global calculation cycles](#configuring-global-calculation-cycles-rt-unified).

##### Assigning a calculation cycle to a KPI

1. Open the "Performance indicators > KPIs" tab in the editor of a plant object type.
2. Select a KPI.
3. In the Inspector window go to "Properties > General > Calculation cycles".
4. Open the "Performance indicators" task card.
5. Drag a calculation cycle from the "Global Calculation Cycles" pane to the "Calculation Cycles" table in the Inspector window under "Properties > General > Calculation Cycles".

   The calculation cycle is assigned to the KPI.
6. In the "Target" column, as an option, select the interface tag in which the KPI results are stored during a calculation cycle. You can use these interface tags in an EA field, for example.
7. Under "Condition", click on the![Assigning a calculation cycle to a KPI](images/124299151755_DV_resource.Stream@PNG-de-DE.png) button.

   The dialog for selecting a tag opens.
8. Select a boolean tag and click on the![Assigning a calculation cycle to a KPI](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button.

   ![Assigning a calculation cycle to a KPI](images/139625937547_DV_resource.Stream@PNG-en-US.png)

If the assigned calculation cycle has been created in "Tag" mode, assign the tag as follows:

1. Double-click on the required plant object type.
2. In the editor of the plant object type under "Performance indicators > Calculation cycle", select the calculation cycle.
3. Open the Inspector window under "Properties > General > Calculation".
4. Under "Tag", click the ![Assigning a calculation cycle to a KPI](images/124299151755_DV_resource.Stream@PNG-de-DE.png) button.

   The dialog for selecting a tag opens.
5. Select an interface tag and click on the![Assigning a calculation cycle to a KPI](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button.
6. Under "Condition", click on the![Assigning a calculation cycle to a KPI](images/124299151755_DV_resource.Stream@PNG-de-DE.png) button.

   The dialog for selecting a tag opens.
7. Select a boolean tag and click on the![Assigning a calculation cycle to a KPI](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button.

   ![Assigning a calculation cycle to a KPI](images/139628423179_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Assigning a KPI to the plant object type (RT Unified)](#assigning-a-kpi-to-the-plant-object-type-rt-unified)

#### Configuring independent KPIs on a plant object (RT Unified)

##### Introduction

You create independent KPIs in the editor of the plant object in the "Performance indicators > KPIs" tab.

For each KPI, you define a calculation formula and how this KPI is displayed. In the KPI formulas, you use only KPIs from other plant objects. Operands, time categories, and machine states are not available.

The "Performance indicators > KPIs" tab of the plant object show the elements that were previously configured on the plant object type. These cannot be edited.

> **Note**
>
> Independent KPIs that are not based on a global KPI cannot be connected to a calculation cycle.

##### Targets and thresholds

When you choose the "Constant" type, you can define the following optional targets and thresholds:

- Target
- High limit 2
- High limit 1
- Low limit 1
- Low limit 2

The values must rise from "Low limit 2" to "Target" and fall from "High limit 2" to "Target" (High limit 2 > High limit 1 > Target > Low limit 1 > Low limit 2).

##### Requirement

- Multiple plant objects are created in the plant hierarchy.
- Global KPIs are used in the plant objects.
- The "Performance indicators > KPIs" tab is open on the plant object.

##### Procedure

1. Click "<Add>" in the work area.

   A new KPI is created.
2. Assign a unique display name for the KPI in the Inspector window in the "Properties" tab under "General > General".
3. Under "Unit of measure", specify the unit of measure in which the KPI is calculated.
4. In the Inspector window under "General > Color > Bar color", specify the color with which the bar for this KPI is visualized in runtime.
5. Under "General > Color > Text color", specify the color in which the text label for the KPI is displayed in runtime.
6. Create the calculation formula for the KPI under "KPI formula". To use the KPI of a different plant object in the formula, follow these steps:

   - Select the specific plant object in the plant hierarchy.

     The available KPIs are shown in the Details view.
   - Drag the KPI from the Details view to the "KPI formula" editor.

   The KPI is used in the formula.
7. If required, define the type and value under "Target and thresholds".
8. Enter a brief description that serves as a tooltip in Runtime and is shown in reports. The description can contain up to 32767 characters

**Note**

You can also drag-and-drop multiple KPIs into the "KPI formula" editor. Enter a "+" between the KPIs.

##### Result

You have created an independent KPI on a plant object and use another KPI in the KPI formula.

### Example: Calculating quality rate (RT Unified)

#### Sample scenario

The quality rate over a specific period of time is to be calculated for a machine in an existing plant. The process tags for calculating good parts and all produced parts have already been created. The plant and the machines are mapped in the plant view. The interface tags for connection to the HMI device are defined.

#### Implementation concept

You create global operands and define the corresponding KPI formula for calculating the quality rate. You then assign the KPI to a plant object type and configure the operands in such a way that the process values are calculated.

#### Defining KPI for quality rate

1. Open the "Common data" folder in the "Plant objects" area in the project tree.
2. Double click on "Performance indicators".

   The "Performance indicators" editor opens.
3. Open the "Counters" folder in the "Global operands" tab.
4. Select "<Add>".

   A new global operand of the type "Counter" is created.
5. Enter a meaningful name for the operand, for example, "RejectionCounts".

   This operand is used to calculate good parts.
6. Create the second global operand of the "Counter" type for the total number of all produced parts, e.g. "ActualProductionCount".
7. Configure the counter type "Incremental" for both operands.
8. Click "Add" in the "Global KPIs" tab.

   A new KPI is created.
9. Enter a meaningful name for the KPI, for example, "Quality".
10. In the Inspector window, under "General" in the "Properties" tab, configure the following:

    - Display name
    - Unit of measure
    - Colors
11. Define the KPI formula:

    - Drag the two operands from the "Global operands" pane into the KPI formula editor.
    - Set a division operator in-between.

    Alternatively, enter the formula manually with consideration of the formula syntax.

    When manually entering a KPI formula, you are supported by the autocomplete. You can find additional information at [Configuring a KPI formula](#configuring-a-kpi-formula-rt-unified).

    ![Defining KPI for quality rate](images/144853961099_DV_resource.Stream@PNG-en-US.png)

    ![Defining KPI for quality rate](images/144853961099_DV_resource.Stream@PNG-en-US.png)

#### Assigning and configuring KPIs

1. Click "Plant objects" in the project tree.
2. Click "Show plant object types" ![Assigning and configuring KPIs](images/126166563211_DV_resource.Stream@PNG-de-DE.png).
3. Double-click on the plant object type of the machine for which you want to calculate the quality rate.

   The editor of the plant object type opens.
4. Go to the "Performance indicators" tab.
5. Open the "Performance indicators" task card.
6. Drag the "Quality" KPI from the "Performance indicators" task card to the "KPI" area.

   The corresponding operands "ActualProductionCount" and "RejectionCounts" are automatically created.
7. Go to the lower-level "Operands" tab.
8. Define a tag for each operand.

   ![Assigning and configuring KPIs](images/144983431179_DV_resource.Stream@PNG-en-US.png)

   ![Assigning and configuring KPIs](images/144983431179_DV_resource.Stream@PNG-en-US.png)

#### Result

You have created a KPI to calculate the quality rate, used it in the plant object type and supplied it with process values.

### Example: Using KPIs from other plant objects (RT Unified)

#### Introduction

You configure the plant in the plant hierarchy and map the equipment as plant objects. With Performance Insight, you have the option of using KPIs of different plant objects within the same plant hierarchy in a KPI formula. In a formula, you define both KPIs from lower-level plant objects as well as KPIs from plant objects of the same and higher-level hierarchy levels.

In the following example, you define a KPI for a station in which you use KPIs from lower-level plant objects.

#### Requirement

- Two plant object types are created:

  - Station
  - Engine
- The "Engine" plant object type contains a "KPI_1" KPI.
- In the plant hierarchy, Engine is used twice as a plant object under Station, for example, Engine_1 and Engine_2.
- The editor of the "Station" plant object is open.

#### Procedure

1. Switch to the "Performance indicators > KPIs" tab.
2. Select "<Add>".

   A new KPI is created.
3. Open the Inspector window under "Properties > General > KPI formula".
4. Select the plant object "Engine_1" in the plant hierarchy.

   The available KPIs of "Engine_1" are shown in the Details view.
5. Drag the KPI "KPI_1" from the Details view to the "KPI-Formel" editor.

   "KPI_1" of "Engine_1" is used in the KPI formula.
6. Select the plant object "Engine_2" in the plant hierarchy.

   The available KPIs of "Engine_2" are shown in the Details view.
7. Drag the KPI "KPI_1" from the Details view to the "KPI formula" editor.

   "KPI_1" of "Engine_2" is used in the KPI formula.
8. Connect the two KPIs with the "+" sign.

   ![Procedure](images/129463006219_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/129463006219_DV_resource.Stream@PNG-en-US.png)

#### Result

You have configured a KPI in which KPIs from other plant objects of the same plant hierarchy are used. This means you can access data of other plant objects or plant objects and use them in KPI formulas.

> **Note**
>
> **Restrictions for the formula syntax**
>
> KPIs cannot be used reciprocally in formulas.

### Example: Using global calculation cycle (RT Unified)

#### Introduction

Calculation cycles are used to calculate and log KPIs at specified time intervals. This allows you to compare KPIs at different times without having to recalculate them. In the following example, the calculation cycle of the KPI is tag-controlled without condition.

#### Requirement

- A plant object type (e.g. "Station") has been created.
- The plant object type contains a KPI, e.g. "QualityRate".
- Two interface tags (e.g. "CC_Trigger" and "Status") are configured at the plant object type.
- A Boolean tag (e.g. "CC_Condition") is configured.
- The "Performance indicators" editor is open.

#### Procedure

1. Change to the "Global calculation cycle" tab of the "Performance indicators" editor.
2. To create a global calculation cycle, click on " <Add> ".
3. Assign a meaningful name, e.g. "CalculationCycle_Quality".
4. Enter a display name for the calculation cycle in the Inspector window under "Properties > General > General".
5. In the Inspector window, under "Properties > General > Calculation", specify the following calculation properties:

   - Mode: "Tag"
   - Interval value: 10
   - Unit: Minutes
6. Under "Properties > General > Description" in the Inspector window, enter a description that will appear as a tooltip in runtime.
7. Open the editor of the plant object type.
8. Switch to the "Performance indicators > KPIs" tab.
9. Select the "QualityRate" KPI.
10. Open the Inspector window of the KPI under "Properties > General > Calculation cycles".
11. Drag the configured calculation cycle from the "Performance indicators > Global calculation cycle" task card to the "Calculation cycles" workspace of the inspector window.
12. In the "Target" column, define an interface tag of the plant object type in which the value of the KPI is recorded, for example, "Status".
13. Change to the "Performance indicators > Calculation cycles of the plant object type" tab.
14. In the "Tag" column, define an interface tag of the plant object type which triggers the calculation cycles, for example, "CC_Trigger".
15. In the "Condition" column, define a Boolean tag that starts or stops the calculation cycles, e.g. "CC_Condition".

#### Result

- The calculation cycle of the "QualityRate" KPI has been configured.
- The "CalculationCycle_Quality" calculation cycle is used in a plant object type.
- The "CalculationCycle_Quality" calculation cycle is connected to one trigger and one target tag each.
- The "CalculationCycle_Quality" calculation cycle is connected with a Boolean tag.

As soon as the calculation cycle is triggered, the calculation cycle starts to calculate and archive the KPI.

With the specified calculation properties, the KPI is calculated and logged at the intervals shown:

![Result](images/128452139275_DV_resource.Stream@PNG-en-US.png)

#### Interval value = 0

When you set the interval value 0, the following graphic results:

![Interval value = 0](images/131621344267_DV_resource.Stream@PNG-de-DE.png)

### Exporting and importing configuration data (RT Unified)

#### Introduction

To save time during configuration, you can distribute these configuration files to multiple WinCC projects, for example, and import them into Performance Insight.

You can export and import the following configuration data as .xlsx file:

- Global KPIs with operands
- Time model

Before the import, the plausibility of the files with respect to validity and logic of the configuration data is checked. When the plausibility check reports a valid file structure, all configuration data is imported in full. You have the possibility to choose whether configuration data of the same name is overwritten during the import.

![Introduction](images/115390386699_DV_resource.Stream@PNG-de-DE.png)

① KPIs before the import

② KPIs after the import. The configuration data of the KPIs "A", "B" and "D" was overwritten during the import. The configuration data of KPI "C" is unchanged after the import.

If the plausibility check evaluates the file structure as invalid, the data is not imported.

#### **Exporting configuration data**

The configuration data is stored in the "Performance indicators" editor.

1. In the editor, click "Performance indicators" in the "Global KPIs" tab.
2. In the menu bar, select "Export KPIs and operands" ![Exporting configuration data](images/111430963083_DV_resource.Stream@PNG-de-DE.png).

   The file selection dialog opens.
3. Enter the file name for the export file.
4. Select the required file format.
5. Navigate to your chosen storage location.
6. Click "Export".

#### **Importing configuration data**

The import file with exported configuration data is stored in the file system.

1. In the editor, click "Performance indicators" in the "Global KPIs" tab.
2. In the menu bar, select "Import KPIs and operands" ![Importing configuration data](images/111431048459_DV_resource.Stream@PNG-de-DE.png).

   The file selection dialog opens.
3. Select the file for import.
4. When importing the file, select one of the two options:

   - whether objects with already existing names are renamed during the import
   - whether existing objects are overwritten
5. Click "Import".
6. Save the configuration with <Ctrl+S> or select "File > Save" in the menu bar.

## Create and save data log (RT Unified)

### Introduction

Create a data log to log the Runtime data of the operands, KPIs and calculation cycles. You also have the option of creating a backup of the data log.

The following settings are available:

| Property |  | Description |
| --- | --- | --- |
| General | Name | Name of the data log. |
| Storage medium | - Standard   The data log is stored in the "Main database directory" of the TIA Portal. - Local   The data log is saved locally. |  |
| Storage directory | If the "Standard" storage medium is selected, the field cannot be edited.  If the "Local" storage medium is selected, specify your storage directory here. |  |
| Log time period | Log time period of the data log. The default setting is 8.00:00:00, equivalent to 8 days.  The period must be between 1 day and 32 days. |  |
| Maximum log size (MB) | Maximum log size (MB) of the data log 10000 (10 GB) is set by default.  The maximum log size may not be smaller than 200 MB.  If no backup of the data log is set, the maximum log size must not exceed twice the value specified under "Maximum segment size (MB)".  If a backup of the data log is set, the maximum log size must not exceed three times the value specified under "Maximum segment size (MB)". |  |
| Segment | Segment time period | Time period of logged segment in days. The default setting is 1.00:00:00, equivalent to 1 day.  The time period may not be greater than the specified log period. |
| Maximum segment size (MB) | Maximum segment size 100 MB is set by default.  The maximum segment size may not be smaller than 20 MB. |  |
| Segment start time | Start time of the logged segment. |  |
| Backup | Backup mode | - No backup   A backup of the data log is not created. - Path   A backup of the data log is created.  If the "SQLite" database type is used as the storage medium in the Runtime settings, only the "No backup" backup mode is available. |
| Path | If the "Default" storage medium is selected, the field cannot be edited.  If the "Local" storage medium is selected, specify your storage directory here. |  |

> **Note**
>
> The number of data logs is limited to 1.

### Create database

1. Select the "Performance Indicators" task card.
2. Click on the![Create database](images/143054508555_DV_resource.Stream@PNG-de-DE.png) button.

   The "Performance Insight" editor opens.
3. Click on the "Data log" tab.
4. Click on the "<Add>" row in the "Name" column.

   A data log is created with the default values.
5. Open the Inspector window.
6. Change the properties of the database under "Properties > General".
7. Compile and download your project.

**Note**

A delta download and delta compile is not possible.

### Back up database

**Requirement**

- The "Microsoft SQL" database type is used as the storage medium for the project in the Runtime settings.

1. Select the "Performance Indicators" task card.
2. Click on the![Back up database](images/143054508555_DV_resource.Stream@PNG-de-DE.png) button.

   The "Performance Insight" editor opens.
3. Click on the "Data log" tab.
4. Open the Inspector window.
5. Select the "Path" option under "Properties > Backup".
6. Specify the storage location under "Path".
7. Compile and download your project.

**Note**

A delta download and delta compile is not possible.

## Resetting the data log (RT Unified)

### Introduction

You have the option to reset the data log. All Runtime data in the data log is cleared.

### Procedure

1. Download your project.

   The "Load preview" dialog opens.

   ![Procedure](images/143084503819_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/143084503819_DV_resource.Stream@PNG-en-US.png)
2. Make your usual settings.
3. Under "Reset logs", select the "Reset all" option.
4. Click "Load".

**Note**

A delta download is not possible.

## Configuring the controls (RT Unified)

This section contains information on the following topics:

- [Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)
- [Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
- [Configuring time ranges (RT Unified)](#configuring-time-ranges-rt-unified)
- [Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified)
- [Configuring the Performance bar chart (RT Unified)](#configuring-the-performance-bar-chart-rt-unified)
- [Configuring the Performance Gantt chart (RT Unified)](#configuring-the-performance-gantt-chart-rt-unified)
- [Configuring the performance control (RT Unified)](#configuring-the-performance-control-rt-unified)
- [Configuring the Performance analyzer (RT Unified)](#configuring-the-performance-analyzer-rt-unified)
- [Set up access control for PFI controls (RT Unified)](#set-up-access-control-for-pfi-controls-rt-unified)

### Basics on outputting KPIs (RT Unified)

#### Introduction

The visualized performance lets you display critical information relating to the following areas:

- Efficiency
- Production figures
- Quality of production processes.

With the display of the values you obtain an overview of the production rate and the opportunity of detecting potential for improvement.

You can visualize KPIs, operands, and other production data in different ways in a screen of the HMI device. The following controls are available for visualizing the performance:

| PFI control | Visualization |
| --- | --- |
| [Performance pie chart](#operating-a-performance-pie-chart-rt-unified) | Free KPI calculation |
| [Performance bar chart](#operating-a-performance-bar-chart-rt-unified) | Free KPI calculation |
| [Performance control](#operating-the-performance-control-rt-unified) | Free KPI calculation |
| [Performance Gantt chart](#operating-a-performance-gantt-chart-rt-unified) | Machine states |
| [Performance Analyzer](#operating-the-performance-analyzer-rt-unified) | Logged KPIs, operands and machine states |

#### Configuration

You can change the configuration of the controls both in the engineering system and during runtime using the configuration dialog. You can configure the following properties in particular:

- KPIs and operands

  Define KPIs that are calculated and visualized in the respective control system.
- Time ranges

  Define time ranges in which the KPIs are calculated.

#### Time ranges

A time range is the basis for outputting indicators. The indicators are shown within this time range. There are several options to configure a time range:

- Duration with relative time

  ![Time ranges](images/94421200907_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | t<sub>a</sub> | Current time |

  You select a duration starting from the current time into the past (start time). The following units of measure are available:

  - Hour
  - Day
  - Week
  - Fiscal week (for the period by calendar when a calendar is configured)

  **Example:**

  The current time is 10:00 AM and you specify a relative time of -1 hour. You want to output the values for the KPI "GoodCounter" during this time period:

  ![Time ranges](images/144146497035_DV_resource.Stream@PNG-en-US.png)

  The following values are output for the KPI "GoodCounter":

  | KPI | Time stamp | Value | Delta value |
  | --- | --- | --- | --- |
  | GoodCounter | 10:00 | 8 | 4 |
  |  | 9:30 | 4 | 2 |
  |  | 9:15 | 2 | 2 |
  |  | 9:00 | 0 | 0 |

  When the end time is reached, the value "0" is output.
- Time duration with fixed time range (absolute time)

  ![Time ranges](images/94421251211_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | t<sub>a</sub> | Current time |
  | t<sub>1</sub> | Start time |
  | t<sub>2</sub> | End time |

#### Contexts

Context information is evaluation and filter criteria that describe equipment in greater detail. To filter the display of indicators depending on the equipment according to these criteria, assign context information. This context information comes from context providers, such as the calendar of an item of equipment. You have the option of using custom context providers. You define the context information in the following controls:

- Performance control
- Performance bar chart
- Performance pie chart

#### Grouping

During "Grouping", the KPIs are grouped according to context information. You define the grouping of the equipment module in the configuration dialog of the "Performance control".

---

**See also**

[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Outputting time ranges according to calendar (RT Unified)](#outputting-time-ranges-according-to-calendar-rt-unified)

### Configuring the output of KPIs (RT Unified)

In the engineering system, you define the data that is displayed in a control.

- Assign KPIs, operands and machine states to a plant object type.

Define properties that influence the representation of controls and the displayed data in the engineering system or in runtime.

- To change properties in Runtime, you must activate the following options in the engineering system:

  - Activate the option "Allow operator control" in the properties of the control under "Security".
  - Activate the "Visibility" option.

An overview of which elements can be selected, and in which control, can be found in the table:

| Control | Element |
| --- | --- |
| Performance pie chart | KPI |
| Performance bar chart | KPI |
| Performance Gantt chart | Equipment |
| Performance display | KPI |
| Performance Analyzer | Entities  Available types: Counter, numeric operand, calculation cycle |

---

**See also**

[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)
  
[Configuring the performance control (RT Unified)](#configuring-the-performance-control-rt-unified)
  
[Configuring the Performance analyzer (RT Unified)](#configuring-the-performance-analyzer-rt-unified)
  
[Configuring the Performance Gantt chart (RT Unified)](#configuring-the-performance-gantt-chart-rt-unified)
  
[Configuring the Performance bar chart (RT Unified)](#configuring-the-performance-bar-chart-rt-unified)
  
[Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Outputting time ranges according to calendar (RT Unified)](#outputting-time-ranges-according-to-calendar-rt-unified)

### Configuring time ranges (RT Unified)

#### Introduction

A time range is the basis for outputting operands and KPIs. You define a time range based on a time t and a duration. Within this time range, the KPIs are calculated from the recorded operands.

In the Inspector window, define the time ranges in which the operands and KPIs are calculated and displayed. The following modes are available for the times:

- Absolute time

  You define a fixed start time and a fixed end time for a time range.
- Relative time

  You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now.

#### Requirement

- The plant hierarchy and plant objects have been configured.
- At least one KPI is configured.
- A screen is configured.
- The corresponding control has been configured

#### Procedure

1. Expand the "Selected time" entry in the Inspector window under "Properties > Properties > Miscellaneous > Interface".
2. Select the desired mode under "Time mode".
3. If you select "Absolute time" mode, set a start time and end time under the "Absolute time" entry.
4. If you select "Relative time" mode, set a time offset and the time unit under the "Relative time" entry.

### Configuring a Performance pie chart (RT Unified)

#### Introduction

The "Performance pie chart" shows partial values which together add up to a complete circle or pie.

With the installation, the control is appears under "My Controls" in the "Toolbox" task card.

![Introduction](images/144669108875_DV_resource.Stream@PNG-de-DE.png)

You have the option to define the data displayed in the control in the engineering system or configure it in Runtime:

- To configure the displayed data in Runtime:

  - Use the control in a screen.
  - Assign the HMI device to the plant hierarchy.
  - Use the indicators you wish to display in a plant object of the plant hierarchy.
- To configure the displayed data in the engineering system, define the KPIs and time ranges in the properties of the control.

#### Layout

You change the settings for the position, visibility, geometry, style, color, and font of the control in the Inspector window.

You can find more information in the WinCC Unified help under "Visualizing processes > Configuring screens > Basic information".

#### Properties of the Performance pie chart

The following properties are available for the Performance pie chart in the Inspector window under "Properties > Miscellaneous > Interface":

| Property | Description |
| --- | --- |
| Display | Specifies whether the chart is displayed. |
| Selected KPIs | Adding KPIs that are displayed as pie slice. |
| Selected time | Adding one or more time spans. |
| Auto refresh | Specifies the time interval for the automatic update in minutes. |
| Display mode | The following display modes are available:  - Circle - Circle and ring |
| Opacity | Specifies the opacity. |
| Background color | Specifies the background color. |
| Indicator format | Data is formatted automatically. |
| Indicator mode | Operands are displayed with or without label. |
| Donut separator size | Information on the size of the separation line with the display type "Circle and ring" |
| Change runtime configuration | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Foreground color | Specifies the foreground color. |
| Counter calculation without the next archived value | The delta between the archived values of a counter cannot be fully calculated if the next archived value begins within the selected time range and ends outside the selected time range. In order to not include the next archived value in the calculation, activate the option. To include the next archived value in the calculation, deactivate the option. |

#### Requirement

- A screen is configured and open.
- KPIs are configured.

#### Inserting a control in a screen

1. Insert the "Performance pie chart" control from the "Toolbox > My controls" task card into the screen.
2. Select the control.
3. In the Inspector window under "Properties > Properties", you define the properties of the control.

#### Adding KPIs

1. Select the control in the screen.
2. In the "Properties" tab, select the lower-level "Properties" tab.
3. Open the "Interface" group in the Inspector window under "Miscellaneous".
4. In the "Selected KPIs" row, click on the "0 entries" field in the "Static value" column.

   The "Selected KPIs" editor is opened on the right side of the Inspector window.
5. Click "<Add>".

   A new element (starting with 0) is created.
6. Under "KPI", navigate to the plant view and then to the unit for which you have already configured KPIs.
7. Select the KPI and click the ![Adding KPIs](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button to apply the KPI for display in the control.
8. Repeat steps 5 to 7 for all configured elements.

#### Result

The created elements are displayed in the Inspector window under "Miscellaneous > Interface" and can be changed there in the "Static value" column if required.

![Result](images/144987079179_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Operating a Performance pie chart (RT Unified)](#operating-a-performance-pie-chart-rt-unified)
  
[Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified-1)

### Configuring the Performance bar chart (RT Unified)

#### Introduction

The "Performance bar chart" control shows KPIs as bars and thereby illustrates a quantity or frequency.

With the installation, the control is appears under "My Controls" in the "Toolbox" task card.

![Introduction](images/144666656523_DV_resource.Stream@PNG-de-DE.png)

You have the option to define the data displayed in the control directly in the engineering system or configure it in Runtime:

- To configure the displayed data in Runtime:

  - Use the control in a screen.
  - Assign the HMI device to the plant hierarchy.
  - Use the indicators you wish to display in a plant object of the plant hierarchy.
- To configure the displayed data in the engineering system, define the KPIs and time ranges in the properties of the control.

#### Layout

You change the settings for the position, visibility, geometry, style, color, and font of the control in the Inspector window.

You can find more information in the WinCC Unified help under "Visualizing processes > Configuring screens > Basic information".

#### Properties of the Performance bar chart

The following properties are available for the Performance bar chart in the Inspector window under "Properties > Miscellaneous > Interface":

| Property | Description |
| --- | --- |
| Axes | Formatting of axes (values, label, alignment, color, ...) |
| Display | Specifies whether the chart is displayed. |
| Selected KPIs | Adding KPIs that are displayed as bars. |
| Selected time | Adding one or more time spans. |
| Auto refresh | Specifies the time interval for the automatic update in minutes. |
| Bar mode: | The following display modes are available:  - Columns - Bar |
| Opacity | Specifies the opacity. |
| Background color | Specifies the background color. |
| Indicator format | Data is formatted automatically. |
| Indicator mode | Operands are displayed with or without label. |
| Grid | Specifies the properties for grid. |
| Change runtime configuration | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Scales | Specifies the properties for scales. |
| Foreground color | Specifies the foreground color. |
| Counter calculation without the next archived value | The delta between the archived values of a counter cannot be fully calculated if the next archived value begins within the selected time range and ends outside the selected time range. In order to not include the next archived value in the calculation, activate the option. To include the next archived value in the calculation, deactivate the option. |

#### Requirement

- A screen is configured.
- KPIs are configured.

#### Inserting a control in a screen

1. Insert the "Performance bar chart" control from the "Toolbox > My controls" task card into the screen.
2. Select the control.
3. In the Inspector window under "Properties > Properties", you define the properties of the control.

#### Adding KPIs

1. Select the control in the screen.
2. In the "Properties" tab, select the lower-level "Properties" tab.
3. Open the "Interface" group in the Inspector window under "Miscellaneous".
4. In the "Selected KPIs" row, click on the "0 entries" field in the "Static value" column.

   The "Selected KPIs" editor is opened on the right side of the Inspector window.
5. Click "<Add>".

   A new element (starting with 0) is created.
6. Under "KPI", navigate to the plant view and then to the unit for which you have already configured KPIs.
7. Select the KPI and click the ![Adding KPIs](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button to apply the KPI for display in the control.
8. Repeat steps 5 to 7 for all configured elements.

#### Result

The created elements are displayed in the Inspector window under "Miscellaneous > Interface" and can be changed there in the "Static value" column if required.

![Result](images/144987082891_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Operating a Performance bar chart (RT Unified)](#operating-a-performance-bar-chart-rt-unified)
  
[Configuring a Performance bar chart (RT Unified)](#configuring-a-performance-bar-chart-rt-unified)

### Configuring the Performance Gantt chart (RT Unified)

#### Introduction

The "Performance Gantt chart" control shows the chronological sequence of machine states as a bar on a time axis. You can see at a glance which machine states occurred at which times.

With the installation, the control is appears under "My Controls" in the "Toolbox" task card.

![Introduction](images/144669075083_DV_resource.Stream@PNG-de-DE.png)

You have the option to define the data displayed in the control directly in the engineering system or configure it in runtime:

- To configure the displayed data in Runtime:

  - Use the control in a screen.
  - Assign the HMI device to the plant hierarchy.
  - Use the indicators you wish to display in a plant object of the plant hierarchy.
- To configure the displayed data in the engineering system, define the equipment and time ranges in the properties of the control.

#### Layout

You change the settings for the position, visibility, geometry, style, color, and font of the control in the Inspector window.

You can find more information in the WinCC Unified help under "Visualizing processes > Configuring screens > Basic information".

#### Properties of the Performance Gantt chart

The following properties are available for the Performance Gantt chart in the Inspector window under "Properties > Miscellaneous > Interface":

| Property | Description |
| --- | --- |
| View mode | Details view or equipment view |
| Display | Specifies whether the chart is displayed. |
| Selected equipment | Adding equipment whose machine states is displayed. |
| Selected time | Adding one or more time spans. |
| Auto refresh | Specifies the time interval for the automatic update in minutes. |
| Scroll bar | Selection of width, color, and visibility of the scroll bar |
| Columns | Show or hide individual columns in the detail view |
| Opacity | Specifies the opacity. |
| Show overall status | - None - First line - Last line |
| Background color | Specifies the background color. |
| Grid | Specifies the properties for grid. |
| Change runtime data | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Change runtime configuration | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Foreground color | Specifies the foreground color. |
| Zoom | Specifies the zoom factor. |

#### Requirement

- A screen is configured.
- KPIs are configured.

#### Inserting a control in a screen

1. Insert the "Performance Gantt chart" control from the "Toolbox > My controls" task card into the screen.
2. Select the control in the screen.
3. In the Inspector window under "Properties > Properties", you define the properties of the control.

#### Adding equipment

1. Select the control in the screen.
2. In the "Properties" tab, select the lower-level "Properties" tab.
3. Open the "Interface" group in the Inspector window under "Miscellaneous".
4. In the "Selected equipment" row, click the "0 items" field in the "Static value" column.

   The "Selected equipment" editor opens on the right side of the Inspector window.
5. Click "<Add>".

   A new element (starting with 0) is created.
6. Navigate under "Equipment" to the plant view and further to the unit for which you have already configured equipment.
7. Select the equipment and click the ![Adding equipment](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button to accept the equipment for display in the control.
8. Repeat steps 5 to 7 for all configured elements.

#### Result

The created elements are displayed in the Inspector window under "Miscellaneous > Interface" and can be changed there in the "Static value" column if required.

![Result](images/144987086603_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Operating a Performance Gantt chart (RT Unified)](#operating-a-performance-gantt-chart-rt-unified)
  
[Configuring a Performance Gantt chart (RT Unified)](#configuring-a-performance-gantt-chart-rt-unified)

### Configuring the performance control (RT Unified)

#### Introduction

The "Performance control" represents the KPIs in relation to relevant equipment. In this way, you can compare the data of parallel production lines, for example.

With the installation, the control is appears under "My Controls" in the "Toolbox" task card.

![Introduction](images/144669028491_DV_resource.Stream@PNG-de-DE.png)

You have the option to define the data displayed in the control in the engineering system or configure it in Runtime:

- To configure the displayed data in Runtime:

  - Use the control in a screen.
  - Assign the HMI device to the plant hierarchy.
  - Use the indicators you wish to display in a plant object of the plant hierarchy.
- To configure the displayed data in the engineering system, define the KPIs and time ranges in the properties of the control.

#### Layout

You change the settings for the position, visibility, geometry, style, color, and font of the control in the Inspector window.

You can find more information in the WinCC Unified help under "Visualizing processes > Configuring screens > Basic information".

#### Properties of the performance display

The following properties are available for the Performance display in the Inspector window under "Properties > Miscellaneous > Interface":

| Property | Description |
| --- | --- |
| Fit to window | Specifies the "Fit to window" property. |
| Display | Specifies whether the chart is displayed. |
| Selected KPIs | Adding KPIs that are displayed. |
| Selected time | Adding one or more time spans. |
| Auto refresh | Specifies the time interval for the automatic update in minutes. |
| Bar style | Options for the appearance of the bar style. |
| Bar window | Options for appearance of the bar window. |
| Opacity | Specifies the opacity. |
| Background color | Specifies the background color. |
| Indicator format | Data is formatted automatically. |
| Sort KPIs | Specifies the sorting of the KPIs:  - Default - Value ascending - Value descending - Alphabetical - Reverse alphabetical |
| Change runtime configuration | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Scales | Specifies the "Y rotation label". |
| Foreground color | Specifies the foreground color. |
| Value axes | Options for the appearance of the value axes. |
| Counter calculation without the next archived value | The delta between the archived values of a counter cannot be fully calculated if the next archived value begins within the selected time range and ends outside the selected time range. In order to not include the next archived value in the calculation, activate the option. To include the next archived value in the calculation, deactivate the option. |

#### Requirement

- A screen is configured.
- KPIs are configured.

#### Inserting a control in a screen

1. Insert the "Performance control" from the "Toolbox > My controls" task card into the screen.
2. Select the control.
3. In the Inspector window under "Properties > Properties", you define the properties of the control.

#### Adding KPIs

1. Select the control in the screen.
2. In the "Properties" tab, select the lower-level "Properties" tab.
3. Open the "Interface" group in the Inspector window under "Miscellaneous".
4. In the "Selected KPIs" row, click on the "0 entries" field in the "Static value" column.

   The "Selected KPIs" editor is opened on the right side of the Inspector window.
5. Click "<Add>".

   A new element (starting with 0) is created.
6. Under "KPI", navigate to the plant view and then to the unit for which you have already configured KPIs.
7. Select the KPI and click the ![Adding KPIs](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button to apply the KPI for display in the control.
8. Repeat steps 5 to 7 for all configured elements.

#### Result

The created elements are displayed in the Inspector window under "Miscellaneous > Interface" and can be changed there in the "Static value" column if required.

![Result](images/144987090315_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Operating the Performance control (RT Unified)](#operating-the-performance-control-rt-unified)
  
[Configuring the Performance control (RT Unified)](#configuring-the-performance-control-rt-unified-1)

### Configuring the Performance analyzer (RT Unified)

#### Introduction

The "Performance analyzer" control represents indicators as a function display.

With the installation, the control is appears under "My Controls" in the "Toolbox" task card.

![Introduction](images/144669020299_DV_resource.Stream@PNG-de-DE.png)

You have the option to define the data displayed in the control directly in the engineering system or configure it in Runtime:

- To configure the displayed data in Runtime:

  - Use the control in a screen.
  - Assign the HMI device to the plant hierarchy.
  - Use the indicators you wish to display in a plant object of the plant hierarchy.
- To configure the displayed data in the engineering system, define the KPIs and time ranges in the properties of the control.

#### Layout

You change the settings for the position, visibility, geometry, style, color, and font of the control in the Inspector window.

You can find more information in the WinCC Unified help under "Visualizing processes > Configuring screens > Basic information".

#### Properties of the Performance analyzer

The following properties are available for the Performance analyzer in the Inspector window under "Properties > Miscellaneous > Interface":

| Property | Description |
| --- | --- |
| Selected objects | Adding indicators that are displayed. |
| Selected time | Adding one or more time spans. |
| Auto refresh | Specifies the time interval for the automatic update in minutes. |
| Change runtime data | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |
| Change runtime configuration | Defines the function right for the Runtime user. You can find additional information under [Set up access control for PFI controls](#set-up-access-control-for-pfi-controls-rt-unified) |

#### Requirement

- A screen is configured.
- KPIs are configured.

#### Inserting a control in a screen

1. Insert the "Performance analyzer" control from the "Toolbox > My controls" task card into the screen.
2. Select the control.
3. In the Inspector window under "Properties > Properties", you define the properties of the control.

#### Adding entities

1. Select the control in the screen.
2. In the "Properties" tab, select the lower-level "Properties" tab.
3. Open the "Interface" group in the Inspector window under "Miscellaneous".
4. In the "Selected objects" row, click on the "0 items" field in the "Static value" column.

   The "Selected objects" editor opens on the right side of the Inspector window.
5. Click "<Add>".

   A new element (starting with 0) is created.
6. Navigate under "Object" to the plant view and further to the unit for which you have already configured items.
7. Select the entity and click the ![Adding entities](images/124346167947_DV_resource.Stream@PNG-de-DE.png) button to apply the entity for display in the control.
8. Set the type of entity to be displayed under "SelectedEntityType":

   - Counters
   - Numerical operand
   - Calculation cycle
9. Repeat steps 5 to 8 for all configured elements.

#### Result

The created elements are displayed in the Inspector window under "Miscellaneous > Interface" and can be changed there in the "Static value" column if required.

![Result](images/144987273227_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Performance analyzer (RT Unified)](#performance-analyzer-rt-unified)

### Set up access control for PFI controls (RT Unified)

#### Introduction

You can set up access control for the individual PFI controls. You do this to determine the rights the runtime user gets in the respective control. To do this, you can assign pre-defined or user-specific Runtime rights to the "Change runtime configuration" or "Change runtime data" properties.

*The property "Change runtime configuration" is only available in the "Performance Gantt chart" and "Performance analyzer" controls.

| Property | Description |
| --- | --- |
| Change runtime configuration | With this right, the Runtime user can configure the control and change runtime data. * |
| Change runtime data | With this right, the Runtime user can change runtime data in the control but cannot perform any runtime configuration.  The "Settings" button is not operable in any of the PFI controls. Other buttons that are not operable:  - "Edit" button in Performance Gantt control - "Recalculation" button and "Expand" button in the Performance Analyzer control |

If no function right is assigned to a property, all Runtime users have the right.

#### Function rights of the runtime user

| Change runtime configuration* | Change runtime data | Function rights of the runtime user |
| --- | --- | --- |
| X | X | User has only read rights. Operation is not possible. |
| ✓ | X | The user has the right to "Change runtime configuration". |
| X/✓ | ✓ | The user has the right to "Change runtime configuration" and "Change runtime data". |

**Legend:**

X = The runtime user does not have the function right that is set in the property.

✓ = The runtime user has the function right that is set in the property.

Or the property is empty.

#### Requirement

- In the security settings, you have configured "Users and roles" in accordance with your needs.

  You can find more information in the section "Configuring users and roles" in the WinCC Unified help.
- The "Allow operator control" option is activated in the control properties under "Security".
- The "Authorization" option is empty in the control properties under "Security".
- The "Require explicit unlock" option is deactivated under the "Change runtime configuration" and "Change runtime data" properties in the control properties under "Properties > Miscellaneous > Interface".

  This control property is for multipoint touch displays and is not supported in V17.

#### Procedure

1. Select the desired control in the screen.
2. Expand the "Change runtime configuration" or "Change runtime data" property under "Properties > Miscellaneous > Interface".
3. Expand the drop-down list in the "Static value" column under "Authorization".

   The function rights are displayed.
4. Select a function right.
5. If necessary, repeat steps 2-4 to configure the additional properties.

## Compiling configuration data and loading it into Runtime (RT Unified)

### Introduction

To receive configuration data in runtime, you have the option of performing a delta compile and delta download.

You can find more information in the WinCC Unified help under "Visualize processes > Compile and load".

### Configuration changes to PFI data

Not all configuration changes can be compiled and downloaded in delta mode. The following table shows you the changes to the PFI data for which a delta compile and delta download are possible:

| Element | Delta download capability | No delta download capability |
| --- | --- | --- |
| Global elements that are used in the plant object | **Global KPIs**   - Create new KPI - Delete KPI - Change KPI - Add operand to KPI formula - Remove operand from KPI formula      **Global operands**   - Create new parameter - Delete operand - Change operand      **Global calculation cycle**   - Create calculation cycle - Delete calculation cycle - Change calculation cycle      **Global time categories**   - Create new time category - Delete time category - Change time category      **Global machine states**   - Create new machine status - Delete machine state - Change the machine state | **Data logs**   - Change data log      **Global calculation cycle (Context mode)**   - Change context provider - Change context - Change interval value - Change unit |
| Plant object | **KPI**   - Create new KPI - Delete KPI - Change KPI | **Plant object general:**   - Create, rename or delete - Copy and paste - Move within the plant view |
| Plant object type | **KPIs**   - Store KPI - Removing KPI - Change targets and thresholds - Store calculation cycle - Remove calculation cycle      **Operands**   - Change the source tag      **Machine states**   - Change the data type - Use in KPI / plant object relevant - Change the source tag      **Calculation cycles (Tag mode)**   - Change tag under "Tag" - Change tag under "Condition"      **Calculation cycles (Context mode)**   - Change tag under "Condition"      **Settings**   - Change MicroStop settings | **Plant object general, if an instance of the plant object type exists:**   - Rename or delete |
| PFI controls | - Assign or change KPIs, equipment and entities in the properties of PFI controls. - Assigning or changing the function rights. | - |

### Effects on the active RT project

Active Runtime is not terminated by delta download. The changes are immediately applied in the active RT project and are visible in Runtime after a screen change or browser refresh.

If a KPI formula is changed and a Delta download is performed, the calculation cycle is stopped in runtime. The calculation cycle is automatically started again with the next trigger.

When the tag under "Condition" is changed in the calculation cycle and a delta download is performed, the calculation cycle is stopped in Runtime. The calculation cycle is only triggered when the tag value is "TRUE". When the tag value is "FALSE", the calculation cycle remains in the stop state.

## Validation of the configuration of plant objects (RT Unified)

### Introduction

If validation errors in the plant view, missing or faulty properties of plant objects or plant object types have arisen, these errors are displayed during compilation. With the "Go to" function, you have the possibility to jump directly to the error location and eliminate the error immediately.

In addition, the number of plant objects (instances) used that are relevant for PFT are displayed during compilation. This information helps you to decide which RT licenses you need and how many.

### Solve causes of errors during validation

1. Navigate in the Inspector window to "Info > Compile".
2. ![Solve causes of errors during validation](images/122765203595_DV_resource.Stream@PNG-de-DE.png) Set the filter so that error messages are displayed.

   If a green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png) is displayed in the "Go to" column for messages, you can go directly to the appropriate tab to correct the cause.
3. Select the green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png).

   The tab in which corrections are expected is displayed. The corresponding property is selected.

### Exceptions and special cases

For errors that are found for an instance of a plant object type, navigation takes you to the property of the plant object type or to the global object.

Examples:

- An invalid limit has been configured for a counter. The properties of the corresponding plant object type are displayed.
- An invalid formula has been specified. The editor for global KPIs is opened.

### Showing the number of plant objects (instances)

The number of plant objects that are used in the plant view and in which at least one PFI object (KPI, operand or machine state) is configured are displayed under "Info > Compile" in the Inspector window.

If no instances exist, the count is not displayed in the Inspector window.

## Configuring and visualizing KPIs in Runtime (RT Unified)

This section contains information on the following topics:

- [Information on operator control in Runtime (RT Unified)](#information-on-operator-control-in-runtime-rt-unified)
- [Visualization of operands that are not used in KPIs (RT Unified)](#visualization-of-operands-that-are-not-used-in-kpis-rt-unified)
- [Outputting time ranges according to calendar (RT Unified)](#outputting-time-ranges-according-to-calendar-rt-unified)
- [Quality code (RT Unified)](#quality-code-rt-unified)
- [Performance pie chart (RT Unified)](#performance-pie-chart-rt-unified)
- [Performance bar chart (RT Unified)](#performance-bar-chart-rt-unified)
- [Performance Gantt chart (RT Unified)](#performance-gantt-chart-rt-unified)
- [Performance control (RT Unified)](#performance-control-rt-unified)
- [Performance analyzer (RT Unified)](#performance-analyzer-rt-unified)

### Information on operator control in Runtime (RT Unified)

#### Display of the buttons

![Display of the buttons](images/110572027403_DV_resource.Stream@PNG-de-DE.png)

The buttons on the toolbar are hidden.

To display the buttons again, double-click in the display area of the control.

#### Highlighting of a KPI in the pie chart

- For example, to highlight the pie slice for a KPI for a printout, click the pie slice.

  The pie slice is moved out of the center and thus highlighted.
- With <Ctrl>-click, you highlight another pie slice.

#### Chinese representation

- To display localized texts for Chinese (simplified), select the SimSun font family from the "Fonts" tab.

### Visualization of operands that are not used in KPIs (RT Unified)

#### Introduction

You have the option to use operands directly in plant object types without the operands being used in a KPI. The Runtime user can, for example, view the current value of a counter.

Operands are displayed in the "Performance Analyzer" control.

#### Requirement

- WinCC Unified SCADA RT has been created.
- The plant hierarchy and plant objects have been configured.
- A screen is configured.
- The "Performance Analyzer" control is configured on the screen.
- Interface tags and the associated logging tags are configured.

#### Procedure

1. Configure a global operand in the "Performance indicators" editor.
2. Assign the operand to a plant object type by dragging it from the "Performance indicators" task card to the plant object type.
3. Assign a source tag to the operand.
4. Compile the project and start Runtime.
5. In runtime, select the operands for visualization in the "Performance Analyzer" control.

### Outputting time ranges according to calendar (RT Unified)

#### Introduction

The Plant Intelligence options WinCC Unified Performance Insight and WinCC Unified Calendar share a time model. The time model defines which time categories are available, for which options they are relevant, how they are visualized, and whether or not they belong to the working time.

For your production line or plant, you define the plant-specific time model and time categories that you use in connection with the Performance Insight option to evaluate and visualize KPIs in runtime. You have the option with each PFI control to evaluate the following period by calendar:

- Fiscal week

#### Requirement

- The plant objects of the configured plant view have tags for communication between a controller and an HMI device.
- The time model with at least one user-defined time category has been created.
- A performance control for visualizing KPIs has been configured.
- The project is in runtime.

#### Procedure

1. Open the settings of the control.
2. Go to the "Indicators" tab.
3. Select the equipment whose entities you want to evaluate.
4. Go to the "Time" tab.
5. Under "Mode", select the "Relative time" setting.
6. Under "Relative time", specify the period starting with the current time.
7. Under "Unit of measure", select "Fiscal week".
8. Confirm your selection with "Apply".

   The selected time from the calendar is used for evaluating the entities.

---

**See also**

[Configuring time categories (RT Unified)](#configuring-time-categories-rt-unified)
  
[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)
  
[Configuring the output of KPIs (RT Unified)](#configuring-the-output-of-kpis-rt-unified)
  
[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)
  
[Configuring the time model. (RT Unified)](Calendar%20-%20Defining%20schedules%20for%20production%20%28RT%20Unified%29.md#configuring-the-time-model-rt-unified)

### Quality code (RT Unified)

#### Introduction

The quality code has the binary 8-bit structure QQSSSSLL. The two positions 1 and 2 (QQ) of the quality code define the quality of the KPI:

| Quality | Description |
| --- | --- |
| Bad | KPI cannot be used. |
| Uncertain | Quality of the KPI is worse than usual. However, it might still be possible to use the KPI. |
| Good (non-cascade) | Quality of the KPI is good. Pay attention to substatus. |
| Good (cascade) | Quality of the KPI is good. KPI can be used. |

Positions 3 to 6 (SSSS) of the quality code specify the substatus of the quality. Positions 7 and 8 (LL) are optional and define possible limits.

The concept of the quality code for KPIs corresponds to that of the quality code for tags in the WinCC Unified object model. You can find additional information on the quality code in the WinCC Unified object model.

#### Show quality code

The quality code is displayed in the following controls:

- Performance pie chart
- Performance bar chart

1. Move the mouse pointer over the respective pie slice or bar.

   The quality code is displayed as a tooltip.

   ![Show quality code](images/130306590475_DV_resource.Stream@PNG-en-US.png)

   ![Show quality code](images/130337155851_DV_resource.Stream@PNG-en-US.png)

### Performance pie chart (RT Unified)

This section contains information on the following topics:

- [Operating a Performance pie chart (RT Unified)](#operating-a-performance-pie-chart-rt-unified)
- [Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified-1)

#### Operating a Performance pie chart (RT Unified)

##### Use

The "Performance pie chart" shows partial values which together add up to a complete circle or pie.

![Use](images/132290000907_DV_resource.Stream@PNG-en-US.png)

The color of the pie slices is taken from the configured color of the respective KPI. The default values are used when no color is configured.

> **Note**
>
> When you move the mouse pointer over the respective pie slice, the following information is displayed:
>
> - Name of the plant object
> - Name of the KPI
> - Value of the KPI
> - Description of the KPI
> - Value of the quality code

##### Display modes

In the Performance pie chart, you represent KPIs from one or more items of equipment. Using different display modes, you have the option of visualizing data as follows:

- To display the KPIs of a single item of equipment, use the display mode "Circle".
- To clearly display the KPIs of multiple items of equipment, use the display mode "Circle and ring". In this mode, an item of equipment is displayed as circle and the next item of equipment is displayed as ring.

  ![Display modes](images/111166207499_DV_resource.Stream@PNG-de-DE.png)

Define the distance between the concentric arcs with the help of the "Donut chart separation line width" property.

##### Operator controls

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/141918702731_DV_resource.Stream@PNG-de-DE.png) |  | Only with "Pie" display mode:  Selection list with plant objects.  Select a plant object. All KPIs assigned to this plant object are displayed.  On the "Indicators" tab, you determine which KPIs are available.  Only those plant objects for which KPIs are activated as indicators are available. |
| ![Operator controls](images/130289644299_DV_resource.Stream@PNG-de-DE.png) | "Settings" | Opens the configuration dialog [Settings](#configuring-a-performance-pie-chart-rt-unified-1).  Configure the display of the data in Runtime.  Requirement: The configuration of the control allows operator control. |
| ![Operator controls](images/110571319051_DV_resource.Stream@PNG-de-DE.png) | "Data request to the server" | Updates the data. |
| ![Operator controls](images/130288257547_DV_resource.Stream@PNG-de-DE.png) | "Automatic data refresh" | Refreshes the displayed data automatically in a configured cycle.   Default value: 10 seconds. |
| ![Operator controls](images/110572027403_DV_resource.Stream@PNG-de-DE.png) | "Show data only" | Hides the toolbar buttons.  To display the buttons again, double-click in the display area of the control. |
| ![Operator controls](images/110572035979_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the output. |
| ![Operator controls](images/110572364555_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports the output of the displayed data in a CSV file. |

---

**See also**

[Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified)
  
[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)

#### Configuring a Performance pie chart (RT Unified)

##### Introduction

You configure the graphic output of the KPIs in Runtime in the configuration dialog of the control.

To open the configuration dialog, click the "Settings" button.

![Introduction](images/130289644299_DV_resource.Stream@PNG-de-DE.png)

A message is output if you have selected a combination of settings that cannot be displayed. For example, the end time of the visualization cannot be before the start time.

**General buttons**

| Symbol | Meaning |
| --- | --- |
| OK | Applies the settings and closes the configuration dialog. |
| Cancel | Closes the configuration dialog without applying the changes. |
| Apply | Applies the changes. The configuration dialog remains open.   The changes are immediately visualized. |

##### Configuring general settings

![Configuring general settings](images/130331985419_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Settings** |  |  |
| Display mode | Selection | Specifies the display mode. You choose from the following modes:  - Pie:    KPIs of an item of equipment are visualized as a circle - Pie and donut:    KPIs of several items of equipment are visualized as a circle with surrounding rings. |
| Donut separator size | Number | Specifies the width of the separation line. |
| **Design** |  |  |
| Display chart | Boolean value | Specifies whether the chart is visible.  - Default setting: True |
| Opacity | Number | Specifies the degree of transparency for the chart.   - 1: Not transparent (default value) - 0.5: 50% transparent - 0: Completely transparent |
| Background color | Color | Specifies the background color in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |
| Foreground color | Color | Specifies the foreground color, for example, the font color for values in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |

##### Configuring the time

![Configuring the time](images/144799686283_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Time range** |  | Displays the time range that is defined under "Settings". |
| **Settings** |  |  |
| Mode | Selection | Defines the mode for calculating the time:  - Absolute time: You define a fixed start time and a fixed end time for a time range. - Relative time: You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now. |
| Start time | Number | Specifies the standard starting time for the calculation.  Only available in "Absolute time" mode. |
| End time | Number | Specifies the standard end time for the calculation.  Only available in "Absolute time" mode. |
| Relative time | Number | Specifies the period starting with the current time.  Only available in "Relative time" mode. |
| Unit | Selection | Specifies the duration of the calculation in hours, days or weeks. When you select "Fiscal week", the [period by calendar](#outputting-time-ranges-according-to-calendar-rt-unified) is output.  Only available in "Relative time" mode. |
| **Automatic update** |  |  |
| Refresh rate | Number | Specifies the refresh rate in minutes.   Default value: 1 minute  When you enter the value 0, the automatic update is disabled. |

> **Note**
>
> If the user-defined time range is in the future, no results of the KPI calculation are displayed in the control.

##### Configuring indicators

![Configuring indicators](images/130331997323_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **KPI selection** |  |  |
| Equipment | String | Specifies which equipment and KPIs thereof are visualized in the control.  - Select the KPIs of the equipment you want to visualize. - Select the display color and the text color for the corresponding KPI or activate the use of the standard color. |
| KPI color: Apply default | Boolean value | Specifies whether the default color is used to display the KPI. The color can be set individually using the color icon. |
| Text color: Apply default | Boolean value | Specifies whether the default color is used to display the text. The color can be set individually using the color icon. |
| **KPI display options** |  |  |
| Indicator mode | Selection | Specifies the mode for the display of the KPIs.  - Indicator: Only the slices of the pie (circle segments corresponding to the KPI value) are displayed. - Indicator with label: The plant object, name of the KPI and the value of the KPI are displayed for each visualized KPI. |
| Automatic decimal format | Boolean value | Specifies whether the decimal format is set automatically. |
| Decimal places | Number | Specifies the number of decimal places between 0 and 10.   Default value: 2. |
| Counter calculation without the next archived value | Boolean value | The last archived value of a counter cannot be fully calculated if the calculation begins in the specified time range and ends outside the specified time range.  If the option "Counter calculation without the next archived value" is activated, this value is not taken into account in the calculation. |

##### Configuring fonts

![Configuring fonts](images/130331993355_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Slider, specifies the font size in the range between 5 pt and 20 pt. |
| Font family | Selection | Specifies the font family. |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the texts in the control are displayed in italics. |
| Underline | Boolean value | Specifies whether the texts in the control are displayed underlined. |
| Strikethrough | Selection | Specifies whether the texts in the control are displayed struck-out. The following values are available:  - None: The texts are not displayed struck-out. - Single: The texts are displayed struck-out with one horizontal line. |

##### Context configuration

![Context configuration](images/130336465035_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Context filter** |  |  |
| Logical operator | Selection | Specifies the logical operator for linking the filter rules:  - ( - ) - AND - OR |
| Context provider | Selection | Specifies the tool on which the filter rule is based:  - Calendar - None |
| Context | Selection | Specifies the context:  - ShiftID    For the "Calendar" context provider |
| Condition | Selection | Specifies the condition for the filter rule:  - = - <   Only available for "Calendar" context provider - <=   Only available for "Calendar" context provider - >   Only available for "Calendar" context provider - >=   Only available for "Calendar" context provider |
| Value | Number | Specifies the value for the condition. |

---

**See also**

[Operating a Performance pie chart (RT Unified)](#operating-a-performance-pie-chart-rt-unified)
  
[Configuring a Performance pie chart (RT Unified)](#configuring-a-performance-pie-chart-rt-unified)
  
[Information on operator control in Runtime (RT Unified)](#information-on-operator-control-in-runtime-rt-unified)

### Performance bar chart (RT Unified)

This section contains information on the following topics:

- [Operating a Performance bar chart (RT Unified)](#operating-a-performance-bar-chart-rt-unified)
- [Configuring a Performance bar chart (RT Unified)](#configuring-a-performance-bar-chart-rt-unified)

#### Operating a Performance bar chart (RT Unified)

##### Use

The "Performance bar chart" control shows KPIs as bars and thereby illustrates a quantity or frequency. For example, you represent multiple KPIs of an item of equipment in a bar chart for comparison.

![Use](images/132293960843_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> When you move the mouse pointer over the respective bar, the following information is displayed:
>
> - Name of the plant object
> - Name of the KPI
> - Value of the KPI
> - Description of the KPI
> - Value of the quality code

##### Display modes

The Performance bar chart can be displayed in two different modes:

- Columns
- Bar

##### Operator controls

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/130289644299_DV_resource.Stream@PNG-de-DE.png) | "Settings" | Opens the configuration dialog [Settings](#configuring-a-performance-bar-chart-rt-unified).  Configure the display of the data in Runtime.  Requirement: The configuration of the control allows operator control. |
| ![Operator controls](images/110571319051_DV_resource.Stream@PNG-de-DE.png) | "Data request to the server" | Updates the data. |
| ![Operator controls](images/130288257547_DV_resource.Stream@PNG-de-DE.png) | "Automatic data refresh" | Refreshes the displayed data automatically in a configured cycle.   Default value: 10 seconds. |
| ![Operator controls](images/110572027403_DV_resource.Stream@PNG-de-DE.png) | "Show data only" | Hides the toolbar buttons.  To display the buttons again, double-click in the display area of the control. |
| ![Operator controls](images/110572035979_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the output. |
| ![Operator controls](images/110572364555_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports the output of the displayed data in a CSV file. |

---

**See also**

[Configuring the Performance bar chart (RT Unified)](#configuring-the-performance-bar-chart-rt-unified)
  
[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)

#### Configuring a Performance bar chart (RT Unified)

##### Introduction

You configure the graphic output of the KPIs in Runtime in the configuration dialog of the control.

To open the configuration dialog, click the "Settings" button.

![Introduction](images/130289644299_DV_resource.Stream@PNG-de-DE.png)

A message is output if you have selected a combination of settings that cannot be displayed. For example, the end time of the visualization cannot be before the start time.

**General buttons**

| Symbol | Meaning |
| --- | --- |
| OK | Applies the settings and closes the configuration dialog. |
| Cancel | Closes the configuration dialog without applying the changes. |
| Apply | Applies the changes. The configuration dialog remains open.   The changes are immediately visualized. |

##### Configuring general settings

![Configuring general settings](images/130346777483_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Settings** |  |  |
| Bar mode | Selection | Specifies the display mode in the bar graph:  - Columns   Horizontal - Bar   Vertical |
| **Design** |  |  |
| Display chart | Boolean value | Specifies whether the chart is visible.  - Default setting: True |
| Opacity | Number | Specifies the degree of transparency for the chart.   - 1: Not transparent (default value) - 0.5: 50% transparent - 0: Completely transparent |
| Background color | Color | Specifies the background color in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |
| Foreground color | Color | Specifies the foreground color, for example, the font color for values in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |

##### Configuring the time

![Configuring the time](images/144802328203_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Time range** |  | Displays the time range that is defined under "Settings". |
| **Settings** |  |  |
| Mode | Selection | Defines the mode for calculating the time:  - Absolute time: You define a fixed start time and a fixed end time for a time range. - Relative time: You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now. |
| Start time | Number | Specifies the standard starting time for the calculation.  Only available in "Absolute time" mode. |
| End time | Number | Specifies the standard end time for the calculation.  Only available in "Absolute time" mode. |
| Relative time | Number | Specifies the period starting with the current time.  Only available in "Relative time" mode. |
| Unit | Selection | Specifies the duration of the calculation in hours, days or weeks. When you select "Fiscal week", the period by calendar is output.  Only available in "Relative time" mode. |
| **Automatic update** |  |  |
| Refresh rate | Number | Specifies the refresh rate in minutes.   Default value: 1 minute  When you enter the value 0, the automatic update is disabled. |

> **Note**
>
> If the user-defined time range is in the future, no results of the KPI calculation are displayed in the control.

##### Configuring indicators

![Configuring indicators](images/130347540619_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **KPI selection** |  |  |
| Equipment | String | Specifies which equipment and KPIs thereof are visualized in the control.  If you activate KPIs of different plant objects, they are displayed next to each other in the chart.  - Select the KPIs of the equipment you want to visualize. - Select the display color and the text color for the corresponding KPI or activate the use of the standard color. |
| KPI color: Apply default | Boolean value | Specifies whether the default color is used to display the KPI. The color can be set individually using the color icon. |
| Text color: Apply default | Boolean value | Specifies whether the default color is used to display the text. The color can be set individually using the color icon. |
| **KPI display options** |  |  |
| Indicator mode | Selection | Specifies the mode for the display of the KPIs.  - Indicator: Only the bars are displayed. - Indicator with label: The name of the KPI and the value of the KPI are displayed for each visualized KPI. |
| Automatic decimal format | Boolean value | Specifies whether the decimal format is set automatically. |
| Decimal places | Number | Specifies the number of decimal places between 0 and 10.   Default value: 2. |
| Counter calculation without the next archived value | Boolean value | The last archived value of a counter cannot be fully calculated if the calculation begins in the specified time range and ends outside the specified time range.  If the option "Counter calculation without the next archived value" is activated, this value is not taken into account in the calculation. |

##### Configuring fonts

![Configuring fonts](images/130347544331_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Slider, specifies the font size in the range between 5 pt and 20 pt. |
| Font family | Selection | Specifies the font family. |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the texts in the control are displayed in italics. |
| Underline | Boolean value | Specifies whether the texts in the control are displayed underlined. |
| Strikethrough | Selection | Specifies whether the texts in the control are displayed struck-out. The following values are available:  - None: The texts are not displayed struck-out. - Single: The texts are displayed struck-out with one horizontal line. |

##### Configuring axes

![Configuring axes](images/130347548043_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Axis** |  |  |
| Visibility | Boolean value | Specifies whether the axes are displayed in the control. |
| Axis width | Number | Specifies the width of the axis. The permissible value range is between 1 and 10. |
| Color | Color | Specifies the axis color. |
| **Values** |  |  |
| Adjust value range automatically | Boolean value | Specifies whether automatic scaling is activated. |
| Start value | Number | Specifies the minimum value for the axis. Only configurable when automatic scaling is disabled. |
| End value | Number | Specifies the maximum value for the axis. Only configurable when automatic scaling is disabled. |
| Align | Selection | Specifies the alignment of the axis:  - Left/bottom - Right/top |
| Show labels | Boolean value | Specifies whether the labels of the value axes are displayed. |

##### Configuring the grid

![Configuring the grid](images/130347590155_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Grid format** |  |  |
| Coarse grid lines weight | Number | Specifies the width of the coarse grid lines in the control.   - Permitted value range: 0.1 … 3 - Default setting: 0.4. |
| Fine grid lines weight | Number | Specifies the width of the fine grid lines in the control.  - Permitted value range: 0.1 … 3 - Default setting: 0.1. |
| Coarse grid lines color | Color | Specifies the color of the coarse grid lines in the control. |
| Fine grid lines color | Color | Specifies the color of the fine grid lines in the control. |
| **Grid** |  |  |
| Visibility | Boolean value | Specifies whether the grid is displayed in the control. |
| Show coarse grid lines | Boolean value | Specifies whether coarse grid lines are displayed in the control. |
| Show fine grid lines | Boolean value | Specifies whether fine grid lines are displayed in the control. |

##### Configuring scales

![Configuring scales](images/130347594123_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Scale** |  |  |
| Visibility | Boolean value | Specifies whether the scales are displayed in the control. |
| X rotation label | Number | Specifies the rotation of the label on position X. The default value is 0. |
| Y rotation label | Number | Specifies the rotation of the label on position Y. The default value is 0. |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Specifies the font size in the range between 0 and 20 pt. |
| Font family | Selection | Specifies the font family.  - Arial (default) - Times New Roman - SimSun (required for Chinese) - Siemens Sans |
| **Scale format** |  |  |
| Foreground color | Color | Specifies the color of the scale. |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the label of the scale is displayed in italics in the control. |
| Underline | Boolean value | Specifies whether the label of the scale is displayed underlined in the control. |
| Strikethrough | Selection | Specifies whether the label of the scale is displayed struck-out in the control. The following values are available:  - None: The text is not displayed struck-out. - Single: The text is displayed struck-out with one horizontal line. |

##### Context configuration

![Context configuration](images/130348284299_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Context filter** |  |  |
| Logical operator | Selection | Specifies the logical operator for linking the filter rules:  - ( - ) - AND - OR |
| Context provider | Selection | Specifies the tool on which the filter rule is based:  - Calendar - None |
| Context | Selection | Specifies the context:  - ShiftID   For the "Calendar" context provider |
| Condition | Selection | Specifies the condition for the filter rule:  - = - <   Only available for "Calendar" context provider - <=   Only available for "Calendar" context provider - >   Only available for "Calendar" context provider - >=   Only available for "Calendar" context provider |
| Value | Number | Specifies the value for the condition. |

---

**See also**

[Operating a Performance bar chart (RT Unified)](#operating-a-performance-bar-chart-rt-unified)
  
[Configuring the Performance bar chart (RT Unified)](#configuring-the-performance-bar-chart-rt-unified)
  
[Information on operator control in Runtime (RT Unified)](#information-on-operator-control-in-runtime-rt-unified)

### Performance Gantt chart (RT Unified)

This section contains information on the following topics:

- [Operating a Performance Gantt chart (RT Unified)](#operating-a-performance-gantt-chart-rt-unified)
- [Configuring a Performance Gantt chart (RT Unified)](#configuring-a-performance-gantt-chart-rt-unified)
- [Modify machine states (RT Unified)](#modify-machine-states-rt-unified)

#### Operating a Performance Gantt chart (RT Unified)

##### Use

The "Performance Gantt chart" control shows the chronological sequence of machine states as a bar on a time axis. You can see at a glance which machine states occurred at which times. The control also offers the option of assigning data about standstill times to a machine. In this way, you can understand why certain events have occurred on a machine or production line.

The time ranges are arranged according to the names of the equipment and priorities, but the order can be changed. Each bar with its own color is proportional to the duration of an item of equipment in terms of its length and is standardized to the scale used. This means that each bar can show sections in different colors (e.g. red for irrelevant data).

The Performance Gantt chart consists of the following areas:

- Detail view

  The machine states of the selected equipment are shown as a table.
- Equipment view

  The chronological order of all machine states of the selected equipment is displayed.

The following filter methods are available in both areas:

- Filter by plant object
- Filter machine states by MicroStops

The data is arranged according to the names of the equipment and priorities, but the order can be changed. Each bar has its own color which is either taken from the color of the state or automatically assigned by the control. The width of the bar is adjusted to the size of the control.

![Use](images/144998880395_DV_resource.Stream@PNG-en-US.png)

You can edit machine states in Runtime using the following functions:

- Change
- Split
- Merge

##### Operator controls

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/130288363915_DV_resource.Stream@PNG-en-US.png) |  | Provides the option to edit machine states. |
| ![Operator controls](images/130288805771_DV_resource.Stream@PNG-de-DE.png) |  | Selection list with items of equipment.  Select a plant object.  All machine states assigned to this plant object are displayed.  On the "Equipment" tab, you determine which plant objects are available.  Only those plant objects for which machine states are enabled as indicators are available. |
| ![Operator controls](images/130288248075_DV_resource.Stream@PNG-en-US.png) |  | Selection list for displaying the machine states:  - With microstops - Only microstops |
| ![Operator controls](images/130288373643_DV_resource.Stream@PNG-en-US.png) |  | Toggles between detail view and equipment view |
| ![Operator controls](images/130289644299_DV_resource.Stream@PNG-de-DE.png) | "Settings" | Opens the configuration dialog [Settings](#configuring-a-performance-gantt-chart-rt-unified).  Configure the display of the data in Runtime.  Requirement: The configuration of the control allows operator control. |
| ![Operator controls](images/110571319051_DV_resource.Stream@PNG-de-DE.png) | "Data request to the server" | Updates the data. |
| ![Operator controls](images/130288257547_DV_resource.Stream@PNG-de-DE.png) | "Automatic data refresh" | Refreshes the displayed data automatically in a configured cycle.  Default value: 10 seconds. |
| ![Operator controls](images/110572027403_DV_resource.Stream@PNG-de-DE.png) | "Show data only" | Hides the toolbar buttons.  To display the buttons again, double-click in the display area of the control. |
| ![Operator controls](images/110572035979_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the output. |
| ![Operator controls](images/110572364555_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports the output of the displayed data in a CSV file. |

---

**See also**

[Configuring the Performance Gantt chart (RT Unified)](#configuring-the-performance-gantt-chart-rt-unified)
  
[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)

#### Configuring a Performance Gantt chart (RT Unified)

##### Introduction

In Runtime, you configure the graphic output of the chronological sequence of the machine states of the individual items of equipment in the configuration dialog of the control.

To open the configuration dialog in Runtime, select the "Settings" button.

![Introduction](images/130289644299_DV_resource.Stream@PNG-de-DE.png)

A message is output if you have selected a combination of settings that cannot be displayed. For example, the end time of the visualization cannot be before the start time.

**General buttons**

| Symbol | Meaning |
| --- | --- |
| OK | Applies the settings and closes the configuration dialog. |
| Cancel | Closes the configuration dialog without applying the changes. |
| Apply | Applies the changes. The configuration dialog remains open.   The changes are immediately visualized. |

##### Configuring general settings

![Configuring general settings](images/130289326091_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Settings** |  |  |
| Show overall status | Selection | Specifies whether the overall status is displayed as an overview of all machine states for an item of equipment for a period of time in one row. Available modes:  - None: Do not show overall status - First line: Summarize overall status in the first line - Last line: Summarize overall status in the last line |
| Zoom factor | Number | Slider; sets the zoom factor in the range between 0.5 and 5.  Default value: 1. |
| **Design** |  |  |
| Display chart | Boolean value | Specifies whether the chart is visible.  - Default setting: True |
| Opacity | Number | Specifies the degree of transparency for the chart.   - 1: Not transparent (default value) - 0.5: 50% transparent - 0: Completely transparent |
| Background color | Color | Specifies the background color in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |
| Foreground color | Color | Specifies the foreground color, for example, the font color for values in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |
| **Show/hide columns** |  |  |
| No. | Boolean value | It determines whether the "No." column is visible in the details view.  - Default setting: True |
| Equipment | Boolean value | It determines whether the "Equipment" column is visible in the details view.  - Default setting: True |
| State | Boolean value | It determines whether the "Status" column is visible in the details view.  - Default setting: True |
| Priority | Boolean value | It determines whether the "Priority" column is visible in the details view.  - Default setting: True |
| Period | Boolean value | It determines whether the "Period" column is visible in the details view.  - Default setting: True |
| Frequency | Boolean value | It determines whether the "Frequency" column is visible in the details view.  - Default setting: True |

##### Configuring the time

![Configuring the time](images/144802919435_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Time range** |  | Displays the time range that is defined under "Settings". |
| **Settings** |  |  |
| Mode | Selection | Defines the mode for calculating the time:  - Absolute time: You define a fixed start time and a fixed end time for a time range. - Relative time: You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now. |
| Start time | Number | Specifies the standard starting time for the calculation.  Only available in "Absolute time" mode. |
| End time | Number | Specifies the standard end time for the calculation.  Only available in "Absolute time" mode. |
| Relative time | Number | Specifies the period starting with the current time.  Only available in "Relative time" mode. |
| Unit | Selection | Specifies the duration of the calculation in hours, days or weeks. When you select "Fiscal week", the period by calendar is output.  Only available in "Relative time" mode. |
| **Automatic update** |  |  |
| Refresh rate | Number | Specifies the refresh rate in minutes.   Default value: 1 minute  When you enter the value 0, the automatic update is disabled. |

> **Note**
>
> If the user-defined time range is in the future, no results of the KPI calculation are displayed in the control.

##### Configuring equipment

![Configuring equipment](images/144804419467_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Equipment selection** |  |  |
| (Check box for configured equipment) | Boolean value | Activates the display for one or more items of equipment.   You can only activate equipment whose plant objects were assigned to the control during configuring. |

##### Configuring fonts

![Configuring fonts](images/130289632395_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Slider, specifies the font size in the range between 5 pt and 20 pt. |
| Font family | Selection | Specifies the font family. |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the texts in the control are displayed in italics. |
| Underline | Boolean value | Specifies whether the texts in the control are displayed underlined. |
| Strikethrough | Selection | Specifies whether the texts in the control are displayed struck-out. The following values are available:  - None: The texts are not displayed struck-out. - Single: The texts are displayed struck-out with one horizontal line. |

##### Configuring the grid

![Configuring the grid](images/130289636363_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Grid** |  |  |
| Show duration | Boolean value | Determines whether the duration is displayed in the columns. |
| Duration format | Input | Specifies the time duration format. |
| Time format | Selection | Specifies the format for the time. Available values:  - Date and time - Time only |
| **Show grid lines** |  |  |
| Visibility | Boolean value | Specifies whether grid lines are shown in the control. |
| Font size | Number | Specifies the font size. Default value: 1. |
| Color | Color | Specifies the color of the grid lines. |

##### Configuring scroll bars

![Configuring scroll bars](images/130289640331_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Scroll bar** |  |  |
| Visibility | Selection | Specifies whether scroll bars are shown in the control.   Available values:  - Automatic: Scroll bars are shown when necessary. - Visibility: Scroll bars are always shown. - Collapsed: Scroll bars are not shown. |
| Width | Number | Specifies the width of the scroll bar.   Default value: 10. |
| **Style** |  |  |
| Color | Color | Specifies the color of the scroll bar. |

---

**See also**

[Operating a Performance Gantt chart (RT Unified)](#operating-a-performance-gantt-chart-rt-unified)
  
[Configuring the Performance Gantt chart (RT Unified)](#configuring-the-performance-gantt-chart-rt-unified)
  
[Information on operator control in Runtime (RT Unified)](#information-on-operator-control-in-runtime-rt-unified)
  
[Modify machine states (RT Unified)](#modify-machine-states-rt-unified)

#### Modify machine states (RT Unified)

##### Introduction

In the "Performance Gantt chart" control, you can modify the displayed machine states in Runtime in the corresponding views.

| Modify machine state | Available in view | Description |
| --- | --- | --- |
| Change | Detail view | Change start time and end time |
| Split | Detail view and equipment view | Split machine state |
| Merge | Equipment view | Merge two machine states that are on the same level. |
| Adjacent (side by side) | Equipment view | An undefined machine state (gap) exists between two machine states. For the machine states to be adjacent to each other, the machine state is merged with the undefined machine state. |

The machine states are logged according to the settings in the engineering system. When processing is currently being performed by another Performance Gantt chart, the "Edit" button cannot be operated. As soon as processing is completed, the data in the control is updated automatically and you can perform the modification using the "Edit" button.

> **Note**
>
> Only available for machine states that are inactive at the time of processing and that are located within the time period shown in the control.

##### Changing the machine state

> **Note**
>
> **Machine state adjacent to other machine state (side by side)**
>
> Do not set the end time of the first machine state to the start time of the second machine state. Instead, merge the first machine state with the undefined machine state that is adjacent to the second machine state (see "Adjacent machine state (side by side)").

1. Click on the "Detail view" in the Performance Gantt chart.
2. Select a bar of a machine in the Performance Gantt chart.
3. Click "Edit".
4. Click "Change".

   The "Change machine state" dialog opens.

   ![Changing the machine state](images/142635146379_DV_resource.Stream@PNG-en-US.png)

   ![Changing the machine state](images/142635146379_DV_resource.Stream@PNG-en-US.png)
5. Define the start time in the "From" input field.
6. Define the end time in the "To" input field.
7. Click "OK" to confirm your input.

   The machine state is updated.

   The machine state is logged according to the specifications in the engineering system.

##### Splitting machine state

1. Select a bar of a machine in the Performance Gantt chart.
2. Click "Edit".
3. Select the "Split" button.

   The "Split machine state" dialog opens.

   ![Splitting machine state](images/142635150731_DV_resource.Stream@PNG-en-US.png)

   ![Splitting machine state](images/142635150731_DV_resource.Stream@PNG-en-US.png)
4. In the "State" selection boxes, define the two machine states into which the original machine state is going to be divided.
5. You have two options to define the time of the split:

   - Used the slider.
   - Enter the time in the "Split date" input field.

   The selected time must be later than the shown start time and before the shown end time.
6. Save your input.

   The machine states are updated.

   The machine states are logged according to the specifications in the engineering system.

##### Merging machine states

1. Click on the "Equipment view" in the Performance Gantt chart.
2. Use multiple selection to select the two machine states you want to combine. Use the <Ctrl> key for multiple selection.
3. Click "Edit".
4. Select the "Merge" button.

   The "Merge machine state" dialog opens.

   ![Merging machine states](images/142644345483_DV_resource.Stream@PNG-en-US.png)

   ![Merging machine states](images/142644345483_DV_resource.Stream@PNG-en-US.png)
5. Select the machine state in the selection list.
6. Save your input.

   The machine state is updated.

   The machine state is logged according to the specifications in the engineering system.

##### Adjacent machine state (side by side)

1. Click on the "Equipment view" in the Performance Gantt chart.
2. Using multiple selection, select the machine state and the undefined machine state that are to be merged. Use the <Ctrl> key for multiple selection.
3. Click "Edit".
4. Select the "Merge" button.

   The "Merge machine state" dialog opens.

   ![Adjacent machine state (side by side)](images/142644345483_DV_resource.Stream@PNG-en-US.png)

   ![Adjacent machine state (side by side)](images/142644345483_DV_resource.Stream@PNG-en-US.png)
5. Select the machine state in the selection list.
6. Save your input.

   The machine state is updated.

   The machine state is logged according to the specifications in the engineering system.

---

**See also**

[Configuring a Performance Gantt chart (RT Unified)](#configuring-a-performance-gantt-chart-rt-unified)

### Performance control (RT Unified)

This section contains information on the following topics:

- [Operating the Performance control (RT Unified)](#operating-the-performance-control-rt-unified)
- [Configuring the Performance control (RT Unified)](#configuring-the-performance-control-rt-unified-1)

#### Operating the Performance control (RT Unified)

##### Use

The "Performance control" represents the KPIs in relation to relevant equipment. You can thus compare the data of different equipment, for example.

You have the option to sort the operands according to equipment or according to context.

![Use](images/132326408843_DV_resource.Stream@PNG-en-US.png)

The bar for a KPI is divided into the following sections:

- A horizontal bar at the bottom, with the period of the calculation
- One or more bars, each with the name of an equipment that is included in the calculation
- One or more bars, each for a calculated KPI with the result value
- A vertical bar for each calculated value with a height that is proportional to the value

If the bar color is configured, it will be copied from the KPI color. Otherwise, the bar color is automatically assigned by the control.

> **Note**
>
> When you move the mouse pointer over the respective bar, the following information is displayed:
>
> - Name of the plant object
> - Name of the KPI
> - Value of the KPI
> - Description of the KPI
> - Value of the quality code

##### Operator controls

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/130289644299_DV_resource.Stream@PNG-de-DE.png) | "Settings" | Opens the configuration dialog [Settings](#configuring-the-performance-control-rt-unified-1).  You configure the display of the data in runtime.  Requirement: The configuration of the control allows operator control. |
| ![Operator controls](images/110571319051_DV_resource.Stream@PNG-de-DE.png) | "Data request to the server" | Updates the data. |
| ![Operator controls](images/130288257547_DV_resource.Stream@PNG-de-DE.png) | "Automatic data refresh" | Refreshes the displayed data automatically in a configured cycle.  Default value: 10 seconds. |
| ![Operator controls](images/110572027403_DV_resource.Stream@PNG-de-DE.png) | "Show data only" | Hides the toolbar buttons.  To display the buttons again, double-click in the display area of the control. |
| ![Operator controls](images/110572035979_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the output. |
| ![Operator controls](images/110572364555_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports the output of the displayed data in a CSV file. |

---

**See also**

[Configuring the performance control (RT Unified)](#configuring-the-performance-control-rt-unified)
  
[Basics on outputting KPIs (RT Unified)](#basics-on-outputting-kpis-rt-unified)

#### Configuring the Performance control (RT Unified)

##### Introduction

You configure the graphic output of the KPIs in Runtime in the configuration dialog of the control.

To open the configuration dialog, click the "Settings" button.

![Introduction](images/130289644299_DV_resource.Stream@PNG-de-DE.png)

A message is output if you have selected a combination of settings that cannot be displayed. For example, the end time of the visualization cannot be before the start time.

**General buttons**

| Symbol | Meaning |
| --- | --- |
| OK | Applies the settings and closes the configuration dialog. |
| Cancel | Closes the configuration dialog without applying the changes. |
| Apply | Applies the changes. The configuration dialog remains open.  The changes are immediately visualized. |

##### Configuring general settings

![Configuring general settings](images/130341163147_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Settings** |  |  |
| Fit bars to window | Boolean value | Specifies whether the height of the bar is scaled to the window size. |
| **Design** |  |  |
| Display chart | Boolean value | Specifies whether the chart is visible.  - Default setting: True |
| Opacity | Number | Specifies the degree of transparency for the chart.   - 1: Not transparent (default value) - 0.5: 50% transparent - 0: Completely transparent |
| Background color | Color | Specifies the background color in the control.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |
| Foreground color | Color | Specifies the foreground color.   Select the appropriate color in the color dialog or enter the hexadecimal code of the color. |

##### Configuring the time

![Configuring the time](images/144801339915_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Time ranges** |  | Specifies the time ranges for the calculation.   You have the option of defining multiple time ranges. The data for the time ranges defined here are displayed next to each other in the control.  - "New": Creates a time range from the settings.   Select a defined time range to change the settings for this range. |
| **Settings** |  |  |
| Mode | Selection | Defines the mode for calculating the time:  - Absolute time: You define a fixed start time and a fixed end time for a time range. - Relative time: You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now. |
| Start time | Number | Specifies the standard starting time for the calculation.  Only available in "Absolute time" mode. |
| End time | Number | Specifies the standard end time for the calculation.  Only available in "Absolute time" mode. |
| Relative time | Number | Specifies the period starting with the current time.  Only available in "Relative time" mode. |
| Unit | Selection | Specifies the duration of the calculation in hours, days or weeks. When you select "Fiscal week", the [period by calendar](#outputting-time-ranges-according-to-calendar-rt-unified) is output.  Only available in "Relative time" mode. |
| **Automatic update** |  |  |
| Refresh rate | Number | Specifies the refresh rate in minutes.   Default value: 1 minute  When you enter the value 0, the automatic update is disabled. |

> **Note**
>
> If the user-defined time range is in the future, no results of the KPI calculation are displayed in the control.

##### Configuring a bar window

With a user-defined bar window, you create an additional display area in the control. The display is split proportionally to the number of bar windows. The individual diagrams are shown one above the other.

![Configuring a bar window](images/130339699979_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Display area** |  |  |
|  | String | Shows the user-defined bar window. |
| Name of display area | String | Specifies a unique name for the bar window.   - Add   Create a new bar window. - Remove   Remove a configured bar window. |

##### Configuring indicators

![Configuring indicators](images/130341171083_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **KPIs by equipment** |  |  |
| <Equipment> | String selection list | Specifies the equipment for which KPIs are visualized in the control.  - Select the KPI of the equipment you would like to visualize. - Select the display color and the text color for the corresponding KPI or activate the use of the standard color. |
| <Context> | String selection list | Specifies the context for the display. |
| <KPIs of the selected equipment> | Boolean value | Specifies whether a KPI is displayed for the selected equipment. |
| KPI color: Apply default | Boolean value | Specifies whether the default color is used to display the KPI. The color can be set individually using the color icon. |
| Text color: Apply default | Boolean value | Specifies whether the default color is used to display the text. The color can be set individually using the color icon. |
| Activate targets and thresholds | Boolean value | Specifies whether the targets and thresholds are displayed in the control. |
| **KPI display options** |  |  |
| Automatic decimal format | Boolean value | Specifies whether the decimal format is set automatically. |
| Decimal places | Number | Specifies the number of decimal places between 0 and 10.   Default value: 2. |
| <Sort order> | Selection list | Defines the order in which the KPIs are displayed. |
| Counter calculation without the next archived value | Boolean value | The last archived value of a counter cannot be fully calculated if the calculation begins in the specified time range and ends outside the specified time range. If the option "Counter calculation without the next archived value" is activated, this value is not taken into account in the calculation. |

##### Configuring fonts

![Configuring fonts](images/130341175051_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Slider, specifies the font size in the range between 5 pt and 20 pt. |
| Font family | Selection | Specifies the font family. |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the texts in the control are displayed in italics. |
| Underline | Boolean value | Specifies whether the texts in the control are displayed underlined. |
| Strikethrough | Selection | Specifies whether the texts in the control are displayed struck-out. The following values are available:  - None: The texts are not displayed struck-out. - Single: The texts are displayed struck-out with one horizontal line. |

##### Configuring value axes

![Configuring value axes](images/130341179019_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Axis** |  |  |
| Visibility | Boolean value | Specifies whether the axes are displayed in the control. |
| Axis width | Number | Specifies the width of the axis.   The permissible value range is between 1 and 10. |
| Color | Color | Specifies the axis color. |
| **Values** |  |  |
| Adjust value range automatically | Boolean value | Specifies whether automatic scaling is activated. |
| Start value | Number | Specifies the minimum value for the axis. Only configurable when automatic scaling is disabled. |
| End value | Number | Specifies the maximum value for the axis. Only configurable when automatic scaling is disabled. |
| Align | Selection | Specifies the alignment of the axis:  - Left - Right |
| Show labels | Boolean value | Specifies whether the labels of the value axes are displayed. |

##### Configuring a scale

![Configuring a scale](images/130341182987_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Scale** |  |  |
| Y rotation label | Number | Specifies the rotation of the label on position Y.   Default value: 0. |
| **Font** |  |  |
| Weight | Selection | Specifies the font weight of the displayed texts. |
| Font size | Number | Specifies the font size in the range between 5 and 20 pt. |
| Font family | Selection | Specifies the font family.  - Arial (default) - Times New Roman - SimSun (required for Chinese) - Siemens Sans |
| **Font style** |  |  |
| Italic | Boolean value | Specifies whether the label of the scale is displayed in italics in the control. |
| Underline | Boolean value | Specifies whether the label of the scale is displayed underlined in the control. |
| Strikethrough | Selection | Specifies whether the label of the scale is displayed struck-out in the control. The following values are available:  - None: The text is not displayed struck-out. - Single: The text is displayed struck-out with one horizontal line. |

##### Configuring the grid

![Configuring the grid](images/130341186955_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Grid format** |  |  |
| Coarse grid lines weight | Number | Specifies the width of the coarse grid lines in the control.   - Permitted value range: 0.1 … 3 - Default setting: 0.4. |
| Fine grid lines weight | Number | Specifies the width of the fine grid lines in the control.  - Permitted value range: 0.1 … 3 - Default setting: 0.1. |
| Coarse grid lines color | Color | Specifies the color of the coarse grid lines in the control. |
| Fine grid lines color | Color | Specifies the color of the fine grid lines in the control. |
| **Grid** |  |  |
| Visibility | Boolean value | Specifies whether the grid is displayed in the control. |
| Show coarse grid lines | Boolean value | Specifies whether coarse grid lines are displayed in the control. |
| Show fine grid lines | Boolean value | Specifies whether fine grid lines are displayed in the control. |

##### Configuring a bar type

![Configuring a bar type](images/130341229323_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Bar style** |  |  |
| Border color | Color | Specifies the border color of the bar. |
| **Bar** |  |  |
| Line width | Number | Specifies the line width of the bar. |
| Set bars to same width | Boolean value | Specifies whether the width of the displayed bars is aligned. |

##### Context configuration

![Context configuration](images/130342332299_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Context filter** |  |  |
| Logical operator | Selection | Specifies the logical operator for linking the filter rules:  - ( - ) - AND - OR |
| Context provider | Selection | Specifies the tool on which the filter rule is based:  - Calendar - Custom |
| Context | Selection | Specifies the context:  - ShiftID    For the "Calendar" context provider |
| Condition | Selection | Specifies the condition for the filter rule:  - = - <   Only available for "Calendar" context provider - <=   Only available for "Calendar" context provider - >   Only available for "Calendar" context provider - >=   Only available for "Calendar" context provider |
| Value | Number | Specifies the value for the condition. |

> **Note**
>
> **Context restrictions**
>
> Only numeric contexts are supported at this time.

---

**See also**

[Operating the Performance control (RT Unified)](#operating-the-performance-control-rt-unified)
  
[Configuring the performance control (RT Unified)](#configuring-the-performance-control-rt-unified)

### Performance analyzer (RT Unified)

This section contains information on the following topics:

- [Operating the Performance Analyzer (RT Unified)](#operating-the-performance-analyzer-rt-unified)
- [Configuring the Performance Analyzer (RT Unified)](#configuring-the-performance-analyzer-rt-unified-1)
- [Evaluating data (RT Unified)](#evaluating-data-rt-unified)
- [Modifying logged operands (RT Unified)](#modifying-logged-operands-rt-unified)
- [Inserting logged operands (RT Unified)](#inserting-logged-operands-rt-unified)
- [Deleting logged operands (RT Unified)](#deleting-logged-operands-rt-unified)
- [Modifying logged machine states (RT Unified)](#modifying-logged-machine-states-rt-unified)
- [Recalculating logged KPIs (RT Unified)](#recalculating-logged-kpis-rt-unified)

#### Operating the Performance Analyzer (RT Unified)

##### Use

The "Performance analyzer" control allows a comprehensive analysis according to different aspects.

You choose between two tabs in the Performance Analyzer:

- Trend graphic

  Graphic display of the indicators of equipment.
- Data table

  Data display of the indicators of equipment.

##### "Trend graphic" tab

Visualization is in the form of a function display. You can define the following elements for visualization using the "Settings" button:

- Equipment
- KPI
- Counter
- Numerical operand
- Calculation cycles

You can find additional information under [Configuring the Performance Analyzer](#configuring-the-performance-analyzer-rt-unified-1)

When displaying KPIs using calculation cycles, targets and thresholds can be displayed. These values can depend dynamically on the KPI or be constant.

!["Trend graphic" tab](images/144793853707_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> When you move the mouse pointer over the respective value, the following information is displayed as a tooltip:
>
> - Name of the indicator and associated plant object
> - Value of the indicator
> - Time stamp

##### "Data table" tab

You can evaluate data with the data table. You can find additional information under [Evaluating data](#evaluating-data-rt-unified)

!["Data table" tab](images/144794914187_DV_resource.Stream@PNG-en-US.png)

In addition, you have the following options using the "Settings" button in the "Entity editor" tab:

- [Modifying logged operands](#modifying-logged-operands-rt-unified)
- [Inserting logged operands](#inserting-logged-operands-rt-unified)
- [Deleting logged operands](#inserting-logged-operands-rt-unified)
- [Modifying logged machine states](#modifying-logged-machine-states-rt-unified)
- [Recalculating logged KPIs](#recalculating-logged-kpis-rt-unified)

> **Note**
>
> When processing is currently being performed by another Performance Analyzer control, for example, processing is currently not possible. As soon as processing is completed, you will be notified in the status bar. Once you have updated the view in the control, you can make your changes.

##### Operator controls

|  | Button | Function |
| --- | --- | --- |
| ![Operator controls](images/144780772747_DV_resource.Stream@PNG-de-DE.png) | "Settings" | Shows or hides the settings for the control. |
| ![Operator controls](images/110571319051_DV_resource.Stream@PNG-de-DE.png) | "Data request to the server" | Updates the data. |
| ![Operator controls](images/130288257547_DV_resource.Stream@PNG-de-DE.png) | "Automatic data refresh" | Refreshes the displayed data automatically in a configured cycle.  Default value: 10 seconds. |
| ![Operator controls](images/110572027403_DV_resource.Stream@PNG-de-DE.png) | "Show data only" | Hides the toolbar buttons.  To display the buttons again, double-click in the display area of the control. |
| ![Operator controls](images/110572035979_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the output. |
| ![Operator controls](images/110572364555_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports the output of the displayed data in a CSV file. |
| ![Operator controls](images/143647926923_DV_resource.Stream@PNG-de-DE.png)     ![Operator controls](images/144793845131_DV_resource.Stream@PNG-de-DE.png) | "Recalculation" /   "Stop recalculation" | Recalculate relevant KPIs.   Stops the recalculation.  The button is active only in the "Data table" tab. |

---

**See also**

[Deleting logged operands (RT Unified)](#deleting-logged-operands-rt-unified)

#### Configuring the Performance Analyzer (RT Unified)

##### Introduction

You configure the graphic output of the entities and the displayed data of the data table in Runtime in the control under "Settings" in the "Time" and "Indicators" tabs.

To show the configuration dialog, click the following button:

![Introduction](images/144780772747_DV_resource.Stream@PNG-de-DE.png)

A message is output if you have selected a combination of settings that cannot be displayed. For example, the end time of the visualization cannot be before the start time.

**General buttons**

| Symbol | Meaning |
| --- | --- |
| Cancel | Closes the configuration dialog without applying the changes. |
| Apply | Applies the changes. The configuration dialog remains open.   The changes are immediately visualized. |

##### Select time range

Select the time range that is to be displayed in the trend graphic or data table.

![Select time range](images/142672341515_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Select time range** |  | Displays the defined time range. |
| Mode | Selection | Defines the mode for calculating the time:  - Absolute time: You define a fixed start time and a fixed end time for a time range. - Relative time: You define a duration. The time range is displayed for the duration relative to the current time, e.g. last hour until now. |
| Start time | Number | Specifies the standard starting time for the calculation.  Only available in "Absolute time" mode. |
| End time | Number | Specifies the standard end time for the calculation.  Only available in "Absolute time" mode. |
| Relative time | Number | Specifies the period starting with the current time.  Only available in "Relative time" mode. |
| Unit | Selection | Specifies the duration of the calculation in hours, days or weeks. When you select "Fiscal week", the [period by calendar](#outputting-time-ranges-according-to-calendar-rt-unified) is output.  Only available in "Relative time" mode. |
| Refresh rate | Number | Specifies the refresh rate in minutes.   Default value: 1 minute  When you enter the value 0, the automatic update is disabled. |
| Maximize editing and recalculation view | Selection | Maximizes the editing and recalculation view. |

> **Note**
>
> If the user-defined time range is in the future, no results of the KPI calculation are displayed in the control.

##### Adding indicators

Select the indicators that are to be displayed in the trend graphic or data table and click on "Load".

![Adding indicators](images/142672345227_DV_resource.Stream@PNG-en-US.png)

| Property | Type | Description |
| --- | --- | --- |
| **Indicators** |  | List of all loaded indicators.  The indicator can be deleted with the "x" character at the end of the indicator name.  The indicator can be made visible or hidden with the "eye icon" in front of the indicator name. |
| **Adding indicators** |  |  |
| Select equipment | Selection | Specifies the equipment (plant object) for which indicators are visualized.  If you activate indicators of different plant objects, these are shown in the chart next to each other. |
| Select type | Selection | Determines the type of indicator:  - Operand - KPI |
| Select operand type | Selection | Determines the type of operand:  - Counter - Numerical operand   Only available when Operand is selected for "Select type". |
| Select data source | Selection | Determines the operand or KPI whose values are displayed. |
| Select calculation cycle | Selection | Determines the calculation cycle that is used to represent the values.  Only available when KPI is selected for "Select type". |

#### Evaluating data (RT Unified)

##### Introduction

Depending on your configuration, the data is displayed in the data table.

You can find additional information in the section [Configuring the Performance Analyzer](#configuring-the-performance-analyzer-rt-unified-1).

![Introduction](images/142666668939_DV_resource.Stream@PNG-en-US.png)

The data table has four levels. The levels can be expanded and collapsed with the following icons.

| Icon | Name | Description |
| --- | --- | --- |
| ![Introduction](images/142669521419_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands a level. |
| ![Introduction](images/142672294795_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses a level. |

> **Note**
>
> When you are in the data table, the "Automatic update" function is deactivated.

**Quality code**

In level 2 and level 4, the quality code is displayed next to the elements as follows:

| Icon | Quality code |
| --- | --- |
| ![Introduction](images/142667733387_DV_resource.Stream@PNG-de-DE.png) | 192, Good (Cascade) |
| ![Introduction](images/142667741963_DV_resource.Stream@PNG-de-DE.png) | 960, Good Cascade And Corrected Value  9152, Good Cascade And Corrected Value And Source Time Bit Flag Set |
| ![Introduction](images/142669158539_DV_resource.Stream@PNG-de-DE.png) | 8896, Good Cascade And Manuel Input And Source Time Bit Flag Set |
| ![Introduction](images/142669320715_DV_resource.Stream@PNG-de-DE.png) | Uncertain |
| ![Introduction](images/142669329291_DV_resource.Stream@PNG-de-DE.png) | Bad |
| ![Introduction](images/142669440267_DV_resource.Stream@PNG-de-DE.png) | 768, Bad And Unusable Value |

##### Level 1 - Equipment with/without calculation cycle

The equipment with or without calculation cycle is displayed on level 1 with the following properties:

**Equipment without calculation cycle**

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 1 - Equipment with/without calculation cycle](images/144154965515_DV_resource.Stream@PNG-de-DE.png) |
| Name | The name is made up of the configuration:"<name of the HMI device>/<name of the plant object> |
| Type | Plant object |

**Equipment with calculation cycle**

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 1 - Equipment with/without calculation cycle](images/142667648011_DV_resource.Stream@PNG-de-DE.png) |
| Name | The name is made up of the configuration:"<name of the HMI device>/<name of the plant object>.<name of the KPI>.<name of the calculation cycle> |
| Type | Trigger type of the calculation cycle:  - Tag - Context |

The associated KPI formula is displayed below the "Data table" tab.

##### Level 2 – KPI

On level 2, the KPIs are displayed with the following properties:

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 2 – KPI](images/142667613835_DV_resource.Stream@PNG-de-DE.png) |
| Name | Name of the logged KPI |
| Value | Calculated result of the KPI |
| Start time | Start time of the calculated KPI (default setting: hidden) |
| End time | End time of the calculated KPI |
| Quality code | Quality code of the calculated KPI |

##### Level 3 - Grouping

A grouping of the following elements is displayed on level 3:

- Incremental counters
- Incremental counters with limits
- Manual counters
- Numeric operands
- Machine states

##### Level 4 - Numerical operand, counters, machine state

**Numerical operand**

On level 4, the "Numerical operands" of the KPIs are displayed with the following properties:

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 4 - Numerical operand, counters, machine state](images/142667545483_DV_resource.Stream@PNG-de-DE.png) |
| Name | Name of the operand |
| Type | Type of the operand:  - Numerical operand |
| Value | Input value of the operand |
| Start time | The time stamp of the numerical operand that starts with the value.  (Raw data time stamp of the assigned tag) |
| End time | The time stamp of the operand that ends with the value.  (The assigned tag has a new value.) |
| Quality code | Quality code of the associated tag |

The operands are sorted alphabetically by their name. When several operands have the same name, the operands are sorted according to their start time.

**Counters**

The "Counter" operands of the KPIs with the following properties are displayed on the level:

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 4 - Numerical operand, counters, machine state](images/142667605259_DV_resource.Stream@PNG-de-DE.png) |
| Name | Name of the operand |
| Type | Type of the counter:  - Manually - Incremental - Incremental with limits |
| Value | Input value of the operand |
| Delta value | The calculated value of the calculation.  (Only available for incremental counters and incremental counters with limits.) |
| Start time | Relevant start time of the operand |
| End time | Relevant end time of the operand |
| Quality code | Quality code of the associated tag |

The operands are sorted alphabetically by their name. When several operands have the same name, the operands are sorted according to their start time.

**Machine state**

The machine states of the KPIs with the following properties are displayed on this level:

| Property | Description |
| --- | --- |
| No. | Row index |
| Icon | ![Level 4 - Numerical operand, counters, machine state](images/142666679307_DV_resource.Stream@PNG-de-DE.png) |
| Name | Name of the machine state |
| Type | Data type of the machine state:  - Bit-based - Value-based |
| Value | Duration of the machine state in seconds |
| Start time | Start time of the machine state |
| End time | End time of the machine state |
| Quality code | Quality code of the associated tag |

In the table, all machine states of a plant object that are within the selected time range of the logged KPI are displayed. When a machine state is busy the end time is displayed as empty.

The machine states are automatically sorted according to the start time.

#### Modifying logged operands (RT Unified)

This section contains information on the following topics:

- [Modifying "Numeric operands" (RT Unified)](#modifying-numeric-operands-rt-unified)
- [Modifying "manual counters" (RT Unified)](#modifying-manual-counters-rt-unified)
- [Modifying "Incremental counters" and "Incremental counters with limits" (RT Unified)](#modifying-incremental-counters-and-incremental-counters-with-limits-rt-unified)

##### Modifying "Numeric operands" (RT Unified)

###### Introduction

You can correct incorrect values of the operands of the "Numeric operand" type in the data table.

The "Entity editor" is available for this purpose.

The following properties are displayed in the Entity editor:

| Property | Description |
| --- | --- |
| Name | Name of the selected operand. |
| Start time | Start time of the selected operand. |
| End time | End time of the selected operand. |
| Value | Value of the selected operand. |

###### Procedure

1. Select a logged operand of the "Numerical operand" type in the data table.
2. Expand the "Entity editor".

   ![Procedure](images/144795143563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/144795143563_DV_resource.Stream@PNG-en-US.png)
3. Enter a new value under "Value."
4. Click the "Change" button.

###### Result

The value of the operand is changed. The quality code is automatically changed to "960, Good Cascade And Corrected Value".

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

##### Modifying "manual counters" (RT Unified)

###### Introduction

You can correct incorrect values of the operands of the "Manual counter" type in the data table by:

- Bulk change

  The value of several operands is changed.
- Simple change

  The value of a single operand is changed.

Depending on the selected element in the data table, you can make a mass change or a simple change:

| Level | Selected element | Possible change |
| --- | --- | --- |
| Level 1 | Calculation cycle | Mass change |
| Level 2 | Logged KPI | Mass change |
| Level 4 | Manual counters | Simple change |

The "Entity editor" is available for this purpose.

###### Performing a mass change

The following properties are displayed in the Entity editor:

| Property | Description |
| --- | --- |
| Operand type | - Manual counters - Incremental counters - Incremental counters with limits |
| Operand name | Name of the operand |
| From time stamp | The start time of the time range of the selected operand with the first invalid value. |
| To time stamp | The end time of the time range of the selected operand with the last invalid value. |
| Total offset of value | The value entered under "Total offset of value" is distributed over the number of operands that are in the specified period.  Example: There are 10 operands in the entered time range. You enter the value 10 under "Total offset of value". As a result, the "value" increases by one for each of these operands. |

**Procedure**

1. Select a calculation cycle or a logged KPI in the data table.
2. Expand the "Entity editor".

   ![Performing a mass change](images/143663853835_DV_resource.Stream@PNG-en-US.png)

   ![Performing a mass change](images/143663853835_DV_resource.Stream@PNG-en-US.png)
3. Under "Operand type", select the entry "Manual counters".
4. Select the operand name and the time.
5. Enter the desired value under "Total offset of Value".
6. Click "Perform mass change".

###### Performing a single change

The following properties are displayed in the Entity editor:

| Property | Description |
| --- | --- |
| Name | Name of the selected operand. |
| Start time | Start time of the selected operand. |
| End time | End time of the selected operand. |
| Value | Value of the selected operand. |

**Procedure**

1. Select a logged operand of the "Manual counter" type in the data table.
2. Expand the "Entity editor".

   ![Performing a single change](images/142673394059_DV_resource.Stream@PNG-en-US.png)

   ![Performing a single change](images/142673394059_DV_resource.Stream@PNG-en-US.png)
3. Enter a new value under "Value."
4. Click the "Change" button.

###### Result

The value of the single operand is changed. The quality code is automatically changed to "960, Good Cascade And Corrected Value".

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

##### Modifying "Incremental counters" and "Incremental counters with limits" (RT Unified)

###### Introduction

You can correct incorrect values of the operands of the type "Incremental counter" and "Incremental counter with limits" in the data table by:

- Bulk change

  The value of several operands is changed.
- Simple change

  The value of a single operand is changed.

Depending on the selected element in the data table, you can make a mass change or a simple change:

| Level | Selected element | Possible change |
| --- | --- | --- |
| Level 1 | Calculation cycle | Mass change |
| Level 2 | Logged KPI | Mass change |
| Level 4 | "Incremental counter" or "Incremental counter with limits" | Simple change |

The "Entity editor" is available for this purpose.

###### Performing a mass change

The following properties are displayed in the Entity editor:

| Property | Description |
| --- | --- |
| Operand type | - Manual counter - Incremental counter - Incremental counter with limits |
| Operand name | Name of the operand |
| From time stamp | The start time of the time range of the selected operand with the first invalid value. |
| To time stamp | The end time of the time range of the selected operand with the last invalid value. |
| Total offset of delta value | The value entered under "Total offset of delta value" is distributed over the number of operands that are in the specified period.  Example: There are 10 operands in the entered time range. You enter the value 10 under "Total offset of delta value". As a result, the "Delta value" increases by one for each of these operands. |

**Procedure**

1. Select a calculation cycle or a logged KPI in the data table.
2. Expand the "Entity editor".

   ![Performing a mass change](images/142673268235_DV_resource.Stream@PNG-en-US.png)

   ![Performing a mass change](images/142673268235_DV_resource.Stream@PNG-en-US.png)
3. Under "Operand type" select the entry "Incremental counter" or "Incremental counter with limits".
4. Select the operand name and the time.
5. Enter the desired value under "Total offset of delta value".
6. Click "Perform mass change".

###### Performing a single change

The following properties are displayed in the Entity editor:

| Property | Description |
| --- | --- |
| Name | Name of the selected operand |
| Start time | Start time of the selected operand |
| End time | End time of the selected operand |
| Delta value | Delta value of the selected operand |

**Procedure**

1. Select a logged operand of the "Incremental counter" or "Incremental counter with limits" type in the data table.
2. Expand the "Entity editor".

   ![Performing a single change](images/143678840203_DV_resource.Stream@PNG-en-US.png)

   ![Performing a single change](images/143678840203_DV_resource.Stream@PNG-en-US.png)
3. Enter a new value under "Delta value".
4. Click the "Change" button.

###### Result

The value of the single operand is changed. The quality code is automatically changed to "960, Good Cascade And Corrected Value". The value under "Value" remains unchanged.

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

#### Inserting logged operands (RT Unified)

This section contains information on the following topics:

- [Insert "Numeric operand" and "Manual counter" (RT Unified)](#insert-numeric-operand-and-manual-counter-rt-unified)
- [Insert "Incremental counter" and "Incremental counter with limits" (RT Unified)](#insert-incremental-counter-and-incremental-counter-with-limits-rt-unified)

##### Insert "Numeric operand" and "Manual counter" (RT Unified)

###### Introduction

To correct errors in the system, add a lost outgoing operand to the data table.

The following properties are displayed for operands of the type "Numeric operand" and "Manual counter" in the entity editor:

| Property | Description |
| --- | --- |
| Name | Name of the operand |
| Start time | Start time of the operand. |
| End time | End time of the operand. |
| Value | Value of the operand. |

###### Procedure

1. Select the desired operand.
2. Expand the Entity editor.
3. Click the "Insert" button.
4. If necessary, change the end time and the value.
5. Click the "Apply" button.

###### Result

The operand is inserted behind the previously selected operand in the data table. The quality code is automatically changed to "8896, Good Cascade And Manuel Input And Source Time Bit Flag Set".

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

> **Note**
>
> **Overlapping of the start time or the end time**
>
> If the start time or end time overlap with another operand, the time is automatically corrected by the system. The quality code is automatically changed to "9152, Good Cascade And Corrected Value And Source Time Bit Flag Set".
>
> In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". Then carry out a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

##### Insert "Incremental counter" and "Incremental counter with limits" (RT Unified)

###### Introduction

To correct errors in the system, add a lost outgoing operand to the data table.

The following properties are displayed for operands of the "Incremental counter" or "Incremental counter with limits" type in the Entity editor:

| Attribute | Description |
| --- | --- |
| Name | Name of the operand. |
| Start time | Start time of the operand. |
| End time | End time of the operand. |
| Insert mode | The following Insert mode is available:  - Insert delta value - Insert value |
| Delta value | Delta value of the operand. |
| Value | Value of the operand. |

###### Insert incremental counter with delta value

1. Select the desired operand.
2. Expand the Entity editor.
3. Click the "Insert" button.
4. If necessary, change the end time.
5. Under "Insert mode: Value", select the entry "Insert delta value".
6. Enter the value under "Delta value".
7. Click the "Apply" button.

###### Result

The operand is inserted behind the previously selected operand in the data table. The quality code is automatically changed to "8896, Good Cascade And Manuel Input And Source Time Bit Flag Set". The "Value" column is empty.

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

> **Note**
>
> **Overlapping of the start time or the end time**
>
> If the start time or end time overlap with another operand, the time is automatically corrected by the system. The quality code is automatically changed to "9152, Good Cascade And Corrected Value And Source Time Bit Flag Set".
>
> In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". Then carry out a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

###### Inserting an incremental counter with value

1. Select the desired operand.
2. Expand the Entity editor.
3. Click the "Insert" button.
4. If necessary, change the end time.
5. Under "Insert mode: Value" select the "Insert value".
6. Enter the value under "Value".
7. Click the "Apply" button.

###### Result

The operand is inserted behind the previously selected operand in the data table. The quality code is automatically changed to "8896, Good Cascade And Manuel Input And Source Time Bit Flag Set". The "Delta value" column is calculated automatically. The "Delta value" column of the operand below is automatically recalculated.

To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

> **Note**
>
> **Overlapping of the start time or the end time**
>
> If the start time or end time overlap with another operand, the time is automatically corrected by the system. The quality code is automatically changed to "9152, Good Cascade And Corrected Value And Source Time Bit Flag Set".
>
> In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". Then carry out a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

#### Deleting logged operands (RT Unified)

##### Introduction

To correct errors in the system, delete operands from the data table.

##### Procedure

1. Select the desired operand.
2. Expand the Entity editor.
3. Click "Delete".

##### Result

The operand has been deleted from the data table. The start time or end time of the following or preceding operand is adjusted by the system so that there is no gap. The quality code is automatically changed to "9152, Good Cascade And Corrected Value And Source Time Bit Flag Set".

In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

#### Modifying logged machine states (RT Unified)

##### Introduction

To correct errors in the system, you can change, split, or merge machine states.

##### Changing the machine state

| 1. Select the desired operand. 2. Expand the Entity editor.    The following properties are displayed:       | Property | Description | Editable/Non-editable |    | --- | --- | --- |    | Name | Name of the machine state | Non-editable |    | Editing mode | The following editing modes can be selected: - Change   Change start time and end time of the machine state - Merge before   The selected machine state is then merged with the machine state. - Merge after   The selected machine state is then merged with the machine state. - Split   Split machine state | Can be edited |    | Start time | Start time of the machine state | Can be edited |    | End time | End time of the machine state | Can be edited |    | Value | Duration of the machine state in seconds | Non-editable | 3. In "Editing mode", select the entry "Change". 4. Under "Start time", change the start time of the machine state. 5. Under "End time", change the end time of the machine state. 6. Click the "Apply" button. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Result**

The machine state has been changed and is visible in the data table. The quality code is automatically changed to "960, Good Cascade And Corrected Value".

In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

> **Note**
>
> **Undefined machine state**
>
> When changing a machine state creates a gap between two machine states, this is displayed as "undefined machine state" in the data table. This machine state can be merged with another machine state.

##### Splitting machine state

| 1. Select the desired machine state. 2. Expand the Entity editor.    The following properties are displayed:       | Property | Description | Editable/Non-editable |    | --- | --- | --- |    | Name | Name of the machine state | Non-editable |    | Editing mode | The following editing modes can be selected: - Change   Change start time and end time of the machine state - Merge before   The selected machine state is then merged with the machine state. - Merge after   The selected machine state is then merged with the machine state. - Split   Split machine state | Can be edited |    | Start time | Start time of the machine state | Non-editable |    | End time | End time of the machine state | Non-editable |    | Value | Duration of the machine state in seconds | Non-editable |    | Split at | The time at which the machine state is to be split. | Can be edited |    | First part of the split | The first part of the split of the machine state. | Can be edited |    | Second part of the split | The second part of the split of the machine state. | Can be edited | 3. In "Editing mode", select the entry "Split". 4. Under "Split at", enter the time at which the machine state is to be split. 5. Under "First part of the split", select the first part of the machine state. 6. Under "Second part of the split", select the second part of the machine state. 7. Click the "Apply" button. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Result**

The machine states are merged and visible in the data table. The quality code is automatically changed to "960, Good Cascade And Corrected Value".

In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

##### Merging machine states

| 1. Select the desired machine state. 2. Expand the Entity editor.    The following properties are displayed:       | Property | Description | Editable/Non-editable |    | --- | --- | --- |    | Name | Name of the machine state | Non-editable |    | Editing mode | The following editing modes can be selected: - Change   Change start time and end time of the machine state - Merge before   The selected machine state is then merged with the machine state. - Merge after   The selected machine state is then merged with the machine state. - Split   Split machine state | Can be edited |    | Start time | Start time of the machine state | Non-editable |    | End time | End time of the machine state | Non-editable |    | Value | Duration of the machine state in seconds | Non-editable |    | Target machine state | Machine state with which the selected machine state is merged. | Can be edited | 3. In "Editing mode", select the entry "Merge before" or "Merge after". 4. Under "Target machine state", select the machine state with which you want to merge the selected machine state. 5. Click the "Apply" button. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Result**

The machine states are merged and visible in the data table. The quality code is automatically changed to "960, Good Cascade And Corrected Value".

In the associated KPI, the quality code is automatically changed to "768, Bad And Unusable Value". To update the KPI, perform a [recalculation of the KPI](#recalculating-logged-kpis-rt-unified).

#### Recalculating logged KPIs (RT Unified)

##### Introduction

After you have modified, inserted or deleted logged operands and/or modified machine states, the quality code of the associated KPI is displayed with the value "768, Bad And Unusable Value". To correct this error in the system, recalculate the KPIs.

> **Note**
>
> **No KPI recalculation**
>
> When you change PFI-relevant data in engineering and load it into Runtime, you cannot recalculate the affected logged KPIs in the data table.

You have the following options to perform a KPI recalculation:

| Options | Description |
| --- | --- |
| Recalculating all KPIs | All KPIs from the equipment with the quality code "768, Bad And Unusable Value" are recalculated one after the other, depending on the setting in the "Time" window under "Maximize window of editing and recalculation". |
| Recalculating individual KPI | The selected KPI is recalculated. |

> **Note**
>
> **Counter calculation without the next logged value**
>
> If the next logged value of a counter begins within the selected time range and ends outside the selected time range, it will not be included in the KPI recalculation.

##### KPI recalculation

1. In the data table, select the desired KPI.
2. Click the "Recalculation" button.

   The "KPI recalculation" dialog box opens.
3. Select the option you want to use.
4. Click "Start recalculation".

   The "Recalculation" button changes to "Stop recalculation". You can stop the recalculation at any time by clicking the "Stop recalculation" button.

   The current newly calculated KPIs are shown in the status bar.

   When all KPIs have been recalculated, the "Stop recalculation" button changes to "Recalculation".

##### Result

In the recalculated KPIs, the quality code is automatically changed to "192, Good (Cascade)".

## Examples (RT Unified)

This section contains information on the following topics:

- [Frequently used KPIs, microstops and scripts (RT Unified)](#frequently-used-kpis-microstops-and-scripts-rt-unified)
- [How long has the machine been in a certain state? (RT Unified)](#how-long-has-the-machine-been-in-a-certain-state-rt-unified)
- [How is the quality of the production during a specific period? (RT Unified)](#how-is-the-quality-of-the-production-during-a-specific-period-rt-unified)
- [How was the availability of a machine? (RT Unified)](#how-was-the-availability-of-a-machine-rt-unified)
- [How often did unplanned standstills occur with my machine? (RT Unified)](#how-often-did-unplanned-standstills-occur-with-my-machine-rt-unified)
- [How can I calculate the overall equipment effectiveness (OEE) of my machine in a specific period? (RT Unified)](#how-can-i-calculate-the-overall-equipment-effectiveness-oee-of-my-machine-in-a-specific-period-rt-unified)
- [How can I use microstops? (RT Unified)](#how-can-i-use-microstops-rt-unified)
- [How can I use scripts in Performance Insight? (RT Unified)](#how-can-i-use-scripts-in-performance-insight-rt-unified)

### Frequently used KPIs, microstops and scripts (RT Unified)

Here you will find examples of calculating the KPIs that are used frequently in various plants.

Although KPIs are defined and calculated for a specific plant, there are standard KPIs that are frequently used in various plants.

An example also shows how to use microstops to calculate KPI. In the last example, scripts are used to design controls.

You can find the following examples:

- [How long has the machine been in a certain state?](#how-long-has-the-machine-been-in-a-certain-state-rt-unified)
- [How is the quality of the production during a specific period?](#how-is-the-quality-of-the-production-during-a-specific-period-rt-unified)
- [How was the availability of a machine?](#how-was-the-availability-of-a-machine-rt-unified)
- [How often did unplanned standstills occur with my machine?](#how-often-did-unplanned-standstills-occur-with-my-machine-rt-unified)
- [How can I calculate the overall equipment effectiveness (OEE) of my machine in a specific period?](#how-can-i-calculate-the-overall-equipment-effectiveness-oee-of-my-machine-in-a-specific-period-rt-unified)
- [How can I use microstops?](#how-can-i-use-microstops-rt-unified)
- [How can I use scripts in Performance Insight?](#how-can-i-use-scripts-in-performance-insight-rt-unified)

---

**See also**

[Configure global KPIs (RT Unified)](#configure-global-kpis-rt-unified)

### How long has the machine been in a certain state? (RT Unified)

#### Introduction

You have the option of using a KPI to calculate the time for which a machine was in a specific state, e.g. working.

#### Requirement

- The machine state "State_1" has been created.
- The "InWork" KPI has been created.

#### Procedure

Enter the following KPI formula in the KPI formula editor and, if necessary, adjust the name of the machine state:

SUM(MachineStates("MachineState_1").Duration)

### How is the quality of the production during a specific period? (RT Unified)

#### Introduction

You have the option to calculate how many good parts were produced during a specific period in your plant. For this purpose, you require an operand for the overall number of produced parts and an operand that transfers the number of defective parts.

#### Requirement

- The counter "TotalParts" for the total number of parts is created.
- The "RejectedParts" counter for the rejected parts has been created.
- The "Quality" KPI has been created.

#### Procedure

Enter the following KPI formula in the KPI formula editor and adapt the operand names if necessary:

(1 - SUM(Counters("RejectParts"))/SUM(Counters("TotalParts"))) * 100

---

**See also**

[How can I calculate the overall equipment effectiveness (OEE) of my machine in a specific period? (RT Unified)](#how-can-i-calculate-the-overall-equipment-effectiveness-oee-of-my-machine-in-a-specific-period-rt-unified)

### How was the availability of a machine? (RT Unified)

#### Introduction

In this example, you calculate the availability of a machine in a given period. The availability of a machine is calculated from the ratio between the actual manufacturing time and the planned busy time.

#### Requirement

- The time category "ActualProductionTime" for the production time is created.
- The time category "PlannedBusyTime" for the planned busy time has been created.
- The "Availability" KPI has been created.

#### Procedure

Enter the following KPI formula in the KPI formula editor and, if necessary, adjust the names of the time categories:

SUM(TimeCategories("ActualProductionTime").Duration) / SUM(TimeCategories("PlannedBusyTime").Duration.Planned)

---

**See also**

[How can I calculate the overall equipment effectiveness (OEE) of my machine in a specific period? (RT Unified)](#how-can-i-calculate-the-overall-equipment-effectiveness-oee-of-my-machine-in-a-specific-period-rt-unified)

### How often did unplanned standstills occur with my machine? (RT Unified)

#### Introduction

In this example, you calculate how often unplanned standstills occurred at the machine in a given period.

#### Requirement

- The time category "UnplannedDowntime" or the machine state "UnplannedDowntime" is created.
- The "UnplannedDowntimeAll" KPI is created.

#### Procedure

Enter the following KPI formula in the KPI formula editor and, if necessary, adjust the name of the time category:

SUM(TimeCategories("UnplannedDowntime").Occurrences)

Alternatively, create the "UnplannedDowntime" state for your machine in a time category and calculate its occurrences.

SUM(MachineStates("UnplannedDowntime").Occurrences)

### How can I calculate the overall equipment effectiveness (OEE) of my machine in a specific period? (RT Unified)

#### Introduction

In this example, you calculate the overall effectiveness of your machine or plant. The overall effectiveness is calculated from the [availability of the machine](#how-was-the-availability-of-a-machine-rt-unified), the average performance and the [number of good parts](#how-is-the-quality-of-the-production-during-a-specific-period-rt-unified) produced in the given period.

#### Requirement

- The "Availabilty" KPI has been configured.
- The "Effectiveness" KPI has been configured.
- The "Quality" KPI has been configured.
- The "OEE" KPI has been created.

#### Procedure

Enter the following KPI formula in the KPI formula editor and adapt the operand names if necessary:

`KPIs("Availability") * KPIs("Effectiveness") * KPIs("Quality")`

---

**See also**

[How is the quality of the production during a specific period? (RT Unified)](#how-is-the-quality-of-the-production-during-a-specific-period-rt-unified)
  
[How was the availability of a machine? (RT Unified)](#how-was-the-availability-of-a-machine-rt-unified)

### How can I use microstops? (RT Unified)

#### Introduction

In order to better understand the availability of the plant, you can include short downtimes of plant objects in the calculation of KPIs, and display them.

To do this, define a machine state as a stop state.

In the following example, calculate the plant availability with the machine states "Operating", "Tailback", and "Idle". The machine state "Tailback" is defined as a stop state. From the three machine states, calculate the "Availability" KPI in three variants:

- With microstops
- Without microstops
- Only microstops

An overview of when a plant object was in a specific state, and for how long, can be found in the "Performance Gantt chart" control.

In this control, you have the option of displaying either machine states with microstops, or only microstops.

#### Requirement

- A plant object type is defined.
- An interface tag "MachineState" is configured at the plant object type.
- A logging tag has been configured for the "MachineState" interface tag.
- The HMI device is assigned to the plant view.
- The plant object type is used in the plant view.
- A time category is configured in the time model.
- A screen is configured.

#### Procedure

**Creating machine states**

1. Open the "Time model" editor.
2. Create an "Operating" machine state.
3. Create a "Tailback" machine state.
4. Create an "Idle" machine state.
5. Select the "Tailback" machine state.
6. Open the Inspector window under "Properties > General > General".
7. Set the check mark in the "Stop state" area.

**Configuring KPIs**

1. Open the "Performance indicators" editor.
2. Create the "Availability_WithMicroStops" KPI.
3. Open the Inspector window under "Properties > General > KPI formula".
4. Configure the "SUM(MachineStates("Operating").Duration/(MachineStates("Operating").Duration+MachineStates("Tailback").Duration+MachineStates("Idle"). Duration))" formula.

   Use drag & drop to use the machine states in the "KPI formula" editor.
5. Create the "Availability_WithoutMicroStops" KPI.
6. Open the Inspector window under "Properties > General > KPI formula".
7. Configure the "SUM(MachineStates("Operating").Duration/(MachineStates("Operating").Duration+MachineStates("Tailback").Duration.WithoutMicroStops+MachineStates("Idle"). Duration))" formula.
8. Create the "Availability_OnlyMicroStops" KPI.
9. Open the Inspector window under "Properties > General > KPI formula".
10. Configure the "SUM(MachineStates("Operating").Duration/(MachineStates("Operating").Duration+MachineStates("Tailback").Duration.OnlyMicroStops+MachineStates("Idle"). Duration))" formula.
11. In the Inspector window, under "Properties > General > General", assign different colors for the display of the KPIs.

**Using KPIs and connecting machine states**

1. Open the plant object type.
2. Switch to the "Performance indicators > KPIs" tab.
3. Select the KPIs in the "Performance indicators" task card.
4. Drag the KPIs to the workspace area using drag & drop.
5. Switch to the "Performance indicators > Machine states" tab.
6. Select the "Operating" machine state.
7. Define the configured interface tag "MachineState" as source tag in the inspector window under "Properties > General > General".
8. Set the value "10" for both the low limit and the high limit.
9. Select the "Tailback" machine state.
10. Set the value "15" for both the low limit and the high limit in the Inspector window under "Properties > General > General".
11. Select the "Idle" machine state.
12. Set the value "0" for both the low limit and the high limit in the Inspector window under "Properties > General > General".
13. Switch to the "Performance indicators > Settings" tab.
14. Set the value "1" for the microstop time.
15. Set minutes as the microstop unit.

**Configuring the layout**

1. Open the configured screen.
2. Add an I/O field.
3. Use the interface tag "MachineState" of the plant object to make the I/O field dynamic in the Inspector window under "Properties > Properties > General > Process value".
4. Add the "Performance Gantt chart" control.
5. Create an element for the equipment in the Inspector window under "Properties > Properties > Miscellaneous > Interface > SelectedEquipment".
6. Expand the created element.
7. Select the plant object in the "Static value" column.

   The plant object is assigned to the "Performance Gantt chart" control.
8. Create a time range under "Properties > Properties > Miscellaneous > Interface > Selected time":

   - Time mode: Relative time
   - From: Current time
   - To > Offset: 2
9. Add the "Performance pie chart" control.
10. Create three elements in the Inspector window under "Properties > Properties > General > Interface > Selected KPIs".
11. In the "Static value" column, select a KPI for each item created.

    The KPIs are assigned to the "Performance pie chart" control.
12. Create a time range under "Properties > Properties > Miscellaneous > Interface > Selected time":

    - Time mode: Relative time
    - From: Current time
    - To > Offset: 2
13. Compile and download the project.
14. Enter a value for a machine state in the I/O field.
15. Update both controls in Runtime.

#### Result

The machine state is displayed in the "Performance Gantt chart" control. You have the option of filtering machine states:

- With microstops
- Only microstops

The configured KPIs are shown in a pie chart.

---

**See also**

[Microstops (RT Unified)](#microstops-rt-unified)
  
[Configuring machine states (RT Unified)](#configuring-machine-states-rt-unified)
  
[Configuring machine state at the plant object type (RT Unified)](#configuring-machine-state-at-the-plant-object-type-rt-unified)

### How can I use scripts in Performance Insight? (RT Unified)

#### Introduction

You can use scripts in Performance Insight to design the control. Scripts let you edit both the displayed data and the display of the control. You can define, for example, the following:

- KPIs and operands
- Time ranges
- Colors and lines
- Display order
- Size
- Display modes

In the example, the following actions are configured using scripts on buttons:

- Adding KPI
- Removing KPI
- Specifying time range in the "Start / end time" mode

#### Requirement

- An HMI device "HMI_RT_1" is configured and assigned to the plant view.
- One "KPI_1" KPI has been configured.
- An "Engine" plant object type has been configured.
- The KPI is used in the plant object type.
- The plant object type is used in a plant view.

  The resulting plant object is called "Engine_1".
- A screen is configured.
- A control of the "Performance display" type with the name "Performance Control_1" is configured on the screen.
- A "Show_KPI_1" button has been configured.
- A "Hide_KPI_1" button has been configured.
- A "Start_End_Time" button has been configured.
- A "From" I/O field has been created.
- A "To" I/O field has been created.
- An HMI tag "From" of the data type "DateTime" is defined.
- An HMI tag "To" of the data type "DateTime" is configured.

#### Procedure

1. Select the "Show_KPI_1" button in the configured screen.
2. Select the event "Click left mouse button" under "Properties > Events" in the Inspector window.
3. Convert the function list to a script.
4. Insert the "Show_KPI_1" sample code.
5. Repeat steps 1 to 4 for the "Hide_KPI_1" button and the "Hide_KPI_1" sample code.
6. Select the I/O field "From" in the configured screen.
7. Use the "From" HMI tag to make the "From" I/O field dynamic in the Inspector window under "Properties > Properties > Process value".
8. Select the I/O field "To" in the configured screen.
9. Use the "To" HMI tag to make the "From" I/O field dynamic in the Inspector window under "Properties > Properties > Process value".
10. Repeat steps 1 to 4 for the "Start-End_Time" button and the "Start-End_Time" sample code.
11. Compile and load it in runtime.
12. Trigger the event "Click left mouse button" on the buttons.

#### Result

**Show_KPI_1**

The "KPI_1" is displayed in the performance view.

**Hide_KPI_1**

The "KPI_1" is removed from the performance view.

**Start_End_Time**

- The mode for the time ranges is changed in "Start / end time".
- The time range adapts to the entries in the I/O fields.

#### Sample code

**Show_KPI_1**

`export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`

`var performanceControl = Screen.Items("Performance control_1");`

`performanceControl.AddKpi("HMI_RT_1::PO1.Kpi_1");`

`}`

**Hide_KPI_1**

`export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`

`var performanceControl = Screen.Items("Performance control_1");`

`performanceControl.RemoveKpi("HMI_RT_1::PO1.Kpi_1");`

`}`

**Start_End_Time**

`export function Start_End_Time_OnTapped(item, x, y, modifiers, trigger) {`
  
 `var From1 = Tags("From").Read();`

`var To1 = Tags("To").Read();`

`Screen.Items("Performance control_1").Properties.SelectedTime[0].From.Mode = "Start / End Time";`

`Screen.Items("Performance control_1").Properties.SelectedTime[0].To.Mode = "Start / End Time";`

`Screen.Items("Performance control_1").Properties.SelectedTime[0].From.Time = From1;`

`Screen.Items("Performance control_1").Properties.SelectedTime[0].To.Time = To1;`

`}`

## Local reporting for Performance Insight (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Procedure (RT Unified)](#procedure-rt-unified)
- [Defining report template (RT Unified)](#defining-report-template-rt-unified)
- [Create or edit configurations for KPIs, machine states, or operands (RT Unified)](#create-or-edit-configurations-for-kpis-machine-states-or-operands-rt-unified)
- [Creating a report job and downloading a report (RT Unified)](#creating-a-report-job-and-downloading-a-report-rt-unified)
- [Example: Evaluating machine state in Excel (RT Unified)](#example-evaluating-machine-state-in-excel-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-1)
- [Requirements (RT Unified)](#requirements-rt-unified-1)

#### Introduction (RT Unified)

When the Performance Insight option package is installed, you can generate production reports for KPIs, operands, logged KPIs and machine states in the form of Excel reports with WinCC Unified Reporting in Runtime. You can then continue to edit the data in Excel or save the report as PDF and distribute or log it.

![Figure](images/115612377099_DV_resource.Stream@PNG-de-DE.png)

#### Requirements (RT Unified)

To create production reports with Performance Insight, the Excel add-in must be installed. In addition, you must be familiar with the basic operation of WinCC Unified Reporting. The documentation for this can be found in the TIA Portal Help under "Creating production logs".

**Basic information on report templates**

Information on creating report templates is available in the TIA Portal help, in the "Creating templates for production reports" section.

This information is also available in the Excel add-in. For this purpose, click the "?" icon in the "WinCC Unified Reporting" tab.

**Basic information on production reports in Runtime**

Information on creating production logs in Runtime is available in the TIA Portal help in the section "Working with production logs in Runtime".

### Procedure (RT Unified)

#### Requirement

- The Performance Insight option package is installed.
- Position the "Reports" control in a screen of a WinCC Unified device.
- The same requirements apply to the use of Reporting with the WinCC Unified basic installation.

#### Run sequence

1. Define a report template for your jobs in the Excel add-in.
2. Define a trigger for the production reports in the "Reports" control.

### Defining report template (RT Unified)

#### Introduction

You define report templates in the Excel add-in.

#### Requirement

- Microsoft Excel is open and the "WinCC Unified" tab is visible.
- The server on which an active runtime project with PFI configuration is running is selected in the "WinCC Unified" tab under "Connections".
- The list of options retrieved from the server includes "Performance Insight".

#### Defining a time series segment

1. In the "WinCC Unified" tab, click on "Segments".

   The list of segments is loaded.
2. Select "New segment".

   The selection menu opens.
3. Select "New time series segment".

   A new time series segment is created.
4. Assign a name.
5. Specify the storage location, on which table and in which cell the time series segment should start.
6. Confirm with "OK".

#### Adding a data source element

1. Click on the created time series segment.
2. Click the "+" icon.

   The menu for selecting a data source item opens.

   ![Adding a data source element](images/130761492747_DV_resource.Stream@PNG-de-DE.png)

   ![Adding a data source element](images/130761492747_DV_resource.Stream@PNG-de-DE.png)
3. Select the "Performance Insight" option.
4. Select an equipment.
5. Select a type under "Select KPIs":

   - KPI
   - Operand

     Select between counter or numerical operand.
   - Logged KPI

     Logged KPIs are KPIs that have been logged by a calculation cycle.
   - Machine state

   You are offered all data source items of the equipment that have this type.
6. Select one or more KPIs, operands, archived KPIs or machine states.

   The elements are added to the "Selected data source items" list.
7. Select the desired data source items.

   The selected data source items receive a check mark.
8. To deselect a data source item, click the data source item again.
9. Click "Delete" to delete selected data source items.
10. Confirm your entries with "OK".

    The template is generated.
11. Save the report template.

**Note**

**Filtering the selection**

You can use filters to limit the selection on each level. Enter a string next to the filter symbol, for example, to filter for KPIs with the partial string "min".

While you are typing, Reporting filters the offered KPIs, machine states, and operands.

**Note**

**Changing the selection**

After you have added a KPI, operand, archived KPI or machine state, you can change the option, equipment, or type and add more data source items.

For example: To output KPIs of various items of equipment in a table, select a different item of equipment.

**Adjusting columns**

1. Select the "Edit" button of the data source item.
2. Select the desired columns.
3. Make your changes.
4. Confirm your entries with "OK".

   The template is updated.

**Testing the template**

Test your template by clicking on the ![Adding a data source element](images/143423888779_DV_resource.Stream@PNG-de-DE.png) button located next to the time series segments.

#### Result

The added KPIs, operands, archived KPIs and machine states are inserted under the segment for the defined period.

KPIs are recalculated for the respective period. Logged KPIs, in contrast, are KPIs that have been logged with defined calculation cycles. Archived values are also used for operands and machine states.

If you do not want the indicator to use the default configuration, create a configuration in the next step.

### Create or edit configurations for KPIs, machine states, or operands (RT Unified)

You can only create configurations for KPIs, machine states, and operands that are used in time series segments.

#### Requirement

- The "WinCC Unified" tab is visible in Excel.

#### Creating a configuration

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Click "Data source item segment configuration".
3. Click "Segment".
4. Select a template.
5. Set the configuration settings.
6. Confirm your entries with "OK".
7. Assign the newly created configuration to a data source item.

#### Editing a configuration

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Click "Data source item segment configuration".
3. Select a configuration.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the runtime data.

#### Settings for KPIs, archived KPIs, machine states and operands

| Setting | Description |
| --- | --- |
| "Name" | Enter the name of the configuration. |
| "Calculation mode" | Select which data is to be written if there is no current value. |
| "Interval" | For KPIs and machine states: Select how often the value is read.  For operands and archived KPIs: Read-only |
| "Show quality code" | Select whether the quality code is output with the value. |
| "Show target values and limits" | Select whether target values and limits are to be output with the value.  Only available for KPIs. |
| "Show microstop and limit" | Select whether microstops and limits are to be output with the value.  Only available for machine states. |
| "Group" | Select the context and associated context value according to which the KPIs are grouped.  Only available for KPIs. |

#### Calculation modes for machine states and operands

| Calculation mode | Description |
| --- | --- |
| Keep last value | If no data is available, the last value is used.  With this mode, you can also use values with an invalid quality code. |
| Interpolate | The values are interpolated linearly for the specified time period.  With this mode, you can only use values with a valid quality code. |
| Raw | The actual value available for the specified time period. If no data is available, no value is output.  Only available for counters. |

#### Calculation modes for KPIs

Only the calculation mode "KPI" is available.

### Creating a report job and downloading a report (RT Unified)

#### Introduction

Before you create a production report, create a report job in the "Reports" control and define a trigger. If necessary, download the production report as an XLSX file or PDF file.

#### Requirement

- A report template with a time series segment has been created in Excel.
- The "Reports" control is being used in Runtime.

#### Creating a report job and defining triggers

1. Select the "Job parameters" tab in the "Reports" control.
2. Under "Templates", select the "Add new" button.

   A selection dialog opens.
3. Select the report template previously created in the Excel add-in.
4. Select "Open".

   The report template is added.
5. Under "Trigger", select the "Add new" button.
6. Define a trigger.
7. Add a report job in the "Report jobs" area.
8. Define the template for the report job.
9. Define the trigger for the report job.

> **Note**
>
> **Generating reports**
>
> The execution of a report job generates a report. Report jobs are executed automatically when the trigger defined in their job parameters is initiated. You also have the option to execute report jobs manually.

#### Downloading a report

1. A new entry has been created in the "Reports" control under "Reports".
2. Select the file format.
3. Click "Export".

   The file is downloaded to the download directory of the browser.
4. To display the report, open the file.

### Example: Evaluating machine state in Excel (RT Unified)

#### Introduction

In this example, the machine state is queried while Runtime is active and output in an Excel sheet as a report.

#### Requirement

- Machine states are configured in the project that is running on the connected Runtime server.
- The "Performance Insight" option is activated in the connection settings in the Excel add-in.
- The "WinCC Unified" tab is visible in Excel.
- There is at least one segment.

#### Machine state in Runtime

A project with the "CuttingMachine" equipment is running in Runtime. Before, the equipment was in the "Shutdown" machine state. The "CuttingMachine" equipment is now started and is in the "Running" state.

![Machine state in Runtime](images/131765709451_DV_resource.Stream@PNG-de-DE.png)

#### Creating a report for machine state

In addition to the time segment, the following settings are necessary to evaluate the machine state in the Excel add-in:

![Creating a report for machine state](images/131764305163_DV_resource.Stream@PNG-de-DE.png)

#### Result

The "Running" machine state is output for the "CuttingMachine" equipment in the defined period as a report.

![Result](images/131765893003_DV_resource.Stream@PNG-de-DE.png)

A value of 1 means that the equipment is in the "Running" machine state.

If the value of 0 is output, the equipment is not in the "Running" machine state.

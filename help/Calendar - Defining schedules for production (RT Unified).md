---
title: "Calendar - Defining schedules for production  (RT Unified)"
package: WCCUCALESenUS
topics: 34
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Calendar - Defining schedules for production  (RT Unified)

This section contains information on the following topics:

- [Migrating V16 project (RT Unified)](#migrating-v16-project-rt-unified)
- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring the time model. (RT Unified)](#configuring-the-time-model-rt-unified)
- [Configuring a calendar (RT Unified)](#configuring-a-calendar-rt-unified)
- [Configuring a calendar control (RT Unified)](#configuring-a-calendar-control-rt-unified)
- [Compiling configuration data and loading it into Runtime (RT Unified)](#compiling-configuration-data-and-loading-it-into-runtime-rt-unified)
- [Validation of the configuration of plant objects (RT Unified)](#validation-of-the-configuration-of-plant-objects-rt-unified)
- Defining schedules during runtime (RT Unified)
- [Local reporting for calendar (RT Unified)](#local-reporting-for-calendar-rt-unified)

## Migrating V16 project (RT Unified)

### Introduction

When you open your V16 project with Calendar configuration in TIA Portal V17, you have the option of upgrading the project to V17.

The configured Runtime version of the HMI device must be separately changed to V17. The calendar control used in the screen must then be updated.

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

### Updating calendar control

1. Open a screen in your project.
2. Click the "Update" button in the task card "Toolbox &gt; My controls".

   ![Updating calendar control](images/141884950027_DV_resource.Stream@PNG-en-US.png)

## Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Requirements (RT Unified)](#requirements-rt-unified)
- [Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)
- [Changes in multi-user projects (RT Unified)](#changes-in-multi-user-projects-rt-unified)

### Introduction (RT Unified)

#### Introduction

SIMATIC WinCC Unified Calendar is an option package of the Plant Intelligence options of TIA Portal. With Calendar, you create schedules for the production lines and stations of your plant.

You make preparations for the scheduling during the engineering in TIA Portal. You perform the scheduling itself in runtime in the calendar control.

#### Functional scope

TIA Portal:

- You define a time model whose time categories are available in the option packages Calendar and Performance Insight.
- You configure the calendar and the calendar control with which you define templates and create schedules in runtime.

Runtime:

- You define and manage templates for typical shifts, days and actions that can be used as often as desired in the schedules. You create the templates from different time categories defined centrally in TIA Portal, e.g. break, work and maintenance.
- From the templates, you create production schedules for the future which implement the requirements for production and work planning.
- You can adapt the schedules to changed requirements at any time during production.

  Examples:

  - Move a planned maintenance activity to achieve a new setpoint number.
  - Respond to events in the production sequence, such as unplanned maintenance work or a staff meeting called at short notice.
- You define actions that access member tags of the plant model during a shift (internal tags or PLC tags). You define the starting point of the action relative to the starting point of your shift.

  In this way, you can control the production process already during scheduling. For example, you can switch on the lights in the production hall via Calendar half an hour before the first day shift begins.

#### Benefits

- You plan based on the created plant view and the time categories centrally managed in TIA Portal and thus guarantee data consistency.
- You speed up your scheduling by using centrally managed templates:

  - With a few clicks, you define templates that you can adapt flexibly to the specific production requirements.
  - You can forward changes to the templates automatically to the schedules.
- You react during production to changed boundary conditions and adapt your schedules on location.
- You collect basic data for additional evaluations and actions related to the shift, such as quantity statistics and production overviews.

### Requirements (RT Unified)

#### Introduction

You use SIMATIC WinCC Unified Calendar to configure schedules for the production lines. You require a license to use this option. You can find information on licenses in the Plant Intelligence Options Installation Guide, section "Licensing PI Options".

#### Software requirements

To use Calendar both in the engineering system and in runtime, you need the following products:

- TIA Portal V17 or higher with STEP 7 Professional
- WinCC Unified Runtime/PC V17
- WinCC Unified Calendar option package

#### Requirements in the TIA Portal

Your TIA Portal project must meet the following requirements so that you can prepare the scheduling for WinCC Unified Runtime in the engineering.

- The project is open.
- Devices and an HMI device are created in the "Devices" tab.
- The HMI device has a screen.
- A plant view is created in the "Plant objects" tab.
- The plant objects of the plant view have member tags (internal tags and tags for communication with a controller).
- An HMI device is assigned to the plant view.
- A time model with at least one user-defined time category has been created.

---

**See also**

[Configuring the time model. (RT Unified)](#configuring-the-time-model-rt-unified)

### Basics on scheduling in the WinCC Unified Calendar (RT Unified)

#### Plant-based planning

The plant is the basis of the scheduling. In the engineering system, the plant model is mapped in a tree in the plant view. The tree root represents the plant view, while the nodes represent the plant objects.

Plant objects have internal tags and tags for communication with a controller. Each plant object has access to its own tags as well as to the tags of its lower-level objects.

Plant objects also have different functional facets. These facets include the calendar object.

Plant Intelligence options for WinCC Unified work in a common plant view. It is defined with Common Plant Model.

> **Note**
>
> **Data losses in Runtime due to changes in engineering**
>
> - Deleting or moving a plant object with the calendar
>
>   Or
>
>   Deleting a calendar from the plant view:
>
>   The data that is created in runtime for the calendar is deleted. If the calendar was passed on to lower-level plant objects and overwritten there, this data is also deleted.
> - Inserting a new calendar at a plant object:
>
>   If the plant object has inherited and overwritten a calendar in runtime, this data is deleted. If the calendar was passed on to lower-level plant objects and overwritten there, this data is also deleted.
> - Changes to tag access of the calendar
>
>   When a member tag that is used by an action element in runtime is disabled, its status is set to "Undefined" in the calendar after the next compile and load. See also section [Defining tag access of the calendar](#defining-tag-access-of-the-calendar-rt-unified).

#### Calendar and inheritance of calendars

A calendar saves all data that is relevant for the schedules of a plant object and its lower-level objects. You define during engineering which objects from the plant view have their own calendar.

- When a plant object has a calendar, its lower-level objects inherit this calendar.

  In runtime, the calendar is valid for the plant object and its lower-level objects. The lower-level objects can amend and overwrite the schedules defined at the higher-level plant object.
- Lower-level nodes can also have their own calendar. This means that they lose access to the calendar of their higher-level node.

  They pass on their own calendar to their own lower-level objects.

For each calendar object you define which calendar settings apply to this calendar, for example, the pre-selected shift length and the beginning of the fiscal year.

#### Calendar control

The calendar control is the HMI control with which schedules are created in runtime.

The calendar control must be linked to a plant object. The link allows the calendar control to show the calendar of the linked plant object and to access the following tags in runtime:

- The member tags of the plant object
- The member tags of all plant objects subordinate to the plant object

You can limit the tag access in the engineering system via the calendar settings.

The link between the calendar control and plant object can be set as follows:

- Dynamic in runtime by selecting a plant object in the "Plant overview" control

  Requirement: The plant overview is configured as companion control in the properties of the calendar control.
- By a static entry in the properties of the calendar control
- By a script

See also section [Defining tag access of the calendar](#defining-tag-access-of-the-calendar-rt-unified).

#### Common Time Model and time categories

The Plant Intelligence options of WinCC Unified Performance Insight and WinCC Unified Calendar share a time model. The time model defines which time categories are available, the options for which they are relevant, how they are visualized and whether or not they belong to the working time.

In the calendar, time periods are combined into shifts from the time categories defined in the time model during runtime.

With installed Performance Insight option, you also define the machine states that you are using in KPIs in Performance Insight in the time model.

---

**See also**

[Configuring machine states (RT Unified)](Performance%20Insight%20-%20Optimizing%20processes%20with%20KPIs%20%28RT%20Unified%29.md#configuring-machine-states-rt-unified)
  
[Configuring a calendar control (RT Unified)](#configuring-a-calendar-control-rt-unified-1)

### Changes in multi-user projects (RT Unified)

Changes to the time model and calendars in multi-user projects always have to be executed in the server project view.

Changes made in the local session are overwritten as soon as the local session is being updated.

## Configuring the time model. (RT Unified)

This section contains information on the following topics:

- [Creating time categories (RT Unified)](#creating-time-categories-rt-unified)
- [Deleting time categories (RT Unified)](#deleting-time-categories-rt-unified)
- [Editing properties of a time category (RT Unified)](#editing-properties-of-a-time-category-rt-unified)
- [Editing the tree structure of the time model (RT Unified)](#editing-the-tree-structure-of-the-time-model-rt-unified)
- [Exporting time categories (RT Unified)](#exporting-time-categories-rt-unified)
- [Importing time categories (RT Unified)](#importing-time-categories-rt-unified)

### Creating time categories (RT Unified)

Time categories are structured in a tree. A root time category under which you create user-defined time categories serves as the tree root.

You can create any number of time categories. You can change the tree structure retrospectively.

#### Creating a root time category

**Requirement**

- No root time category is created in the time model editor.

**Procedure**

1. Select the "Plant objects" tab.
2. In the "Common data" folder, double-click the node "Time model".
3. In the time model editor, double click the "Add new" cell.

The root time category is created.

#### Creating a user-defined category

**Requirement**

- The root time category is created in the time model editor.

**Procedure**

1. In the "Common data" folder, double-click the node "Time model".
2. You have the following options:

   - Select the root time category.
   - In the time model editor, expand the time model and select a time category.

     The "Expand all" button extends the tree so that you can see all categories, "Collapse all" reduces it.
3. Click the "Add time category" button or select "Add time category" from the shortcut menu.
4. Enter the name of the category.
5. Configure additional properties of the new time category, either directly in the editor or in the Inspector window.

#### Copying time category

1. Select "Copy" in the shortcut menu of a time category.
2. Select the desired owner.
3. In the shortcut menu, select "Paste".

---

**See also**

[Editing properties of a time category (RT Unified)](#editing-properties-of-a-time-category-rt-unified)
  
[Editing the tree structure of the time model (RT Unified)](#editing-the-tree-structure-of-the-time-model-rt-unified)
  
[Importing time categories (RT Unified)](#importing-time-categories-rt-unified)

### Deleting time categories (RT Unified)

#### Requirement

- The time model editor is open.
- At least one time category has been created.

#### Procedure

1. Select the required time category.
2. Select "Delete" in the shortcut menu.

#### Result

After the next save, compile and load, the time category is no longer available to users in Runtime for planning.

> **Note**
>
> **Time categories used in Runtime**
>
> If the deleted time category is used in a calendar in Runtime, time intervals with this time category are marked with an "*". Users using this category must replace the time intervals that are in the future.

### Editing properties of a time category (RT Unified)

#### Requirement

- A time model is created on the "Plant objects" tab.
- The time model has user-defined time categories.

#### Procedure

1. In the "Common data" folder, double-click the node "Time model".
2. In the time model editor, expand the time model and select a time category.

   The "Expand all" button extends the tree so that you can see all categories, "Collapse all" reduces it.
3. Click on a time category.
4. Configure its properties, either directly in the editor or in the Inspector window.

#### Properties of the time category

| Property |  | Description |
| --- | --- | --- |
| Properties |  |  |
|  | Name | Assign a unique name.  Language-neutral  Unsupported special characters:  : :: . #\ / % [ ] $ " |
| Display name | Localizable |  |
| Description | Localizable |  |
| Color | Color for visualizing the category in the Plant Intelligence options. |  |
| Relevance |  |  |
|  | Calendar | In the time model, select the check box of a category so that it can be used in the calendar control.  When you activate a category, the hierarchically higher-level and lower-level categories are deactivated.  Default setting of new categories: Deactivated |

### Editing the tree structure of the time model (RT Unified)

> **Note**
>
> **Data losses in runtime through changes to the time model**
>
> If the time model is changed in TIA Portal after templates and schedules have been created in runtime, this can lead to data losses.

You can edit the tree structure of the time model as follows:

- Creating time categories
- Deleting time categories
- Moving time categories

  You can move a lower-level node or a higher-level node including all its children.
- Sorting time categories

#### Requirement

- A time model is created on the "Plant objects" tab.
- The time model has user-defined time categories.

#### Deleting time categories

Select one of the following procedures:

- Select "Delete" in the shortcut menu of the time category.
- Select the time category and press &lt;Del&gt;.
- Select the time category and click "Delete" in the toolbar.

The time category and its children are deleted.

#### Moving time categories

Select one of the following procedures:

- Select a time category and drag it to the new owner, keeping the left mouse button pressed.
- Select "Cut" in the shortcut menu of the time category and "Paste" in the shortcut menu of the new owner.

The time category and its children are moved.

#### Rearranging time categories

You rearrange the order of time categories on the same level:

1. Select a time category and drag it to the line header of a second category on the same level, keeping the left mouse button pressed:

   ![Rearranging time categories](images/144278097291_DV_resource.Stream@PNG-de-DE.png)

   ![Rearranging time categories](images/144278097291_DV_resource.Stream@PNG-de-DE.png)

The time category and its children are sorted above the second category.

### Exporting time categories (RT Unified)

You have the option to export the time categories to Excel.

#### Requirements

- A time model is created on the "Plant objects" tab.
- The time model has time categories.

#### Procedure

1. In the "Common data" folder, double-click the node "Time model".
2. Click the "Export" button.
3. Define the export path and the file name.
4. Click "Export".

#### Result

An Excel file is created. The time categories are exported into the "TimeCategories" worksheet.

> **Note**
>
> Do not rename the sheet if you are planning on a reimport.

### Importing time categories (RT Unified)

You have the option to import time categories from Excel.

#### Requirements

- The Excel file has a "TimeCategories" worksheet. The worksheet has the required format.

#### Importing time categories

1. In the "Common data" folder, double-click the node "Time model".
2. Click the "Import" button.
3. Select the import path and the Excel file.
4. Define what happens during the import if time categories in TIA Portal and in the import file have the same name. Select one of the following options:

   - The time category to be imported is renamed.
   - The time category to be imported overwrites the time category from TIA Portal.
5. Click "Import".

#### Result

If a time model already exists, the time categories are imported from the Excel file into the time model.

If no time model exists yet, a time model and the base time category are created. The time categories are imported from the Excel file into the time model.

## Configuring a calendar (RT Unified)

This section contains information on the following topics:

- [Creating a calendar (RT Unified)](#creating-a-calendar-rt-unified)
- [Opening a calendar (RT Unified)](#opening-a-calendar-rt-unified)
- [Configuring the basic settings of the calendar (RT Unified)](#configuring-the-basic-settings-of-the-calendar-rt-unified)
- [Defining tag access of the calendar (RT Unified)](#defining-tag-access-of-the-calendar-rt-unified)
- [Editing calendars (RT Unified)](#editing-calendars-rt-unified)
- [Deleting a calendar (RT Unified)](#deleting-a-calendar-rt-unified)

### Creating a calendar (RT Unified)

#### Requirements

- A plant object has been created in the plant view.
- A plant object has no calendar.

#### Creating a new calendar

1. Double-click the plant object or select "Open" in its shortcut menu.

   The editor for plant objects opens.
2. Select the "Calendar" tab.
3. Click the "Add calendar" button.

#### Copying an existing calendar

1. Copy a calendar in the detail view.
2. In the "Plant objects" tab, click a plant object without a calendar.
3. In the shortcut menu, select "Paste".

Alternative procedures:

- Keyboard commands &lt;Ctrl+C&gt; and &lt;Ctrl+V&gt;
- Using the shortcut menu of the calendar and the new owner or the menu bar
- Drag-and-drop in conjunction with keyboard command &lt;Ctrl&gt;

#### Result

A Calendar object is created and is loaded for editing into the "Calendar" tab in the work area.

If you select the plant object in the "Plant objects" tab, you see the calendar object in the detail view.

With a complete download, the changes become immediately visible in Runtime. In the case of a delta download, the changes become visible after a screen change or a browser refresh. Unsaved changes to the calendar are lost on screen change and browser refresh.

---

**See also**

[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)

### Opening a calendar (RT Unified)

#### Requirements

A plant object has a calendar.

#### Procedure

1. Select the plant object in the "Plant objects" tab.
2. Select "Open" in the detail view in the shortcut menu of the calendar

   or double-click the calendar in the detail view.

#### Result

The calendar editor opens.

---

**See also**

[Configuring the basic settings of the calendar (RT Unified)](#configuring-the-basic-settings-of-the-calendar-rt-unified)

### Configuring the basic settings of the calendar (RT Unified)

#### Requirement

A plant object in the "Plant objects" tab has a calendar.

#### Procedure

1. Open the calendar.
2. Select the "Calendar" tab.
3. Configure the general calendar properties under "Settings".
4. Under "Permitted interface tags", configure which of the member tags available in principle can be accessed via the calendar.
5. Save your project.

#### Overview of the general calendar settings

**Settings**

Under "Settings", you define the general calendar settings:

| Name | Description | Default setting |
| --- | --- | --- |
| "Time zone" | The time zone used by the calendar.  The property is write-protected. | The time zone set in the local system. |
| "Standard shift length." | Determines the length of created new shifts.  Minimum value: 2 hours  Maximum value: 24 hours | 8 hours |
| "First day of week" | Determines the day on which the working week starts. | Monday |
| "First week of year" | Determines the week in which the year starts.  Possible values:  - "1 January" - "First 4-day week" - "First full week" | First 4-day week |
| "Beginning of day offset" | Determines the number of hours after midnight until the working day starts. | 0 |
| "Fiscal year day" | Determines the first day of the fiscal year | 1 |
| "Fiscal year month" | Determines the first month of the fiscal year | January |
| "Weekdays" | Determines which days are part of the working week. | Monday to Friday |

**Permitted tags**

Under "Permitted interface tags", use the "Permitted" check box to configure the tags to which the calendar has access. See section [Defining tag access of the calendar](#defining-tag-access-of-the-calendar-rt-unified).

#### Result

With a complete download, the changes become visible immediately in runtime. In the case of a delta download, the changes become visible after a screen change or a browser refresh. Unsaved changes to the calendar are lost on browser refresh.

> **Note**
>
> **Deactivate weekdays of a calendar used in runtime**
>
> If you deactivate weekdays for a calendar used in runtime, shifts scheduled for those weekdays are not displayed in the working week view. The days are still executed in runtime.
>
> The planned shifts are not deleted.

---

**See also**

[Opening a calendar (RT Unified)](#opening-a-calendar-rt-unified)
  
[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)

### Defining tag access of the calendar (RT Unified)

#### Requirement

A plant object has a calendar.

#### Procedure

Proceed as follows to determine which tags the calendar can access in runtime:

1. Open the calendar.
2. Select the "Calendar" tab.

   Under "Permitted interface tags", you can see all member tags that were defined for the plant object and its lower-level objects in the "Interface" tab. The member tags have the "permissible" check box.
3. Select or clear the check boxes as required.
4. Save your project.

**Note**

**Deactivating tags used in runtime**

When you disable a tag that is used by an action element in runtime, its status is set to "Undefined" in the calendar after the next compile and load.

#### Result

Your settings for tag access are available in runtime as soon as you have compiled them and loaded them into the device. All tags with selected check box can be assigned to action elements in runtime.

With a complete download, the changes become visible immediately in runtime. In the case of a delta download, the changes become visible after a screen change or a browser refresh. Unsaved changes to the calendar are lost on browser refresh.

---

**See also**

[Opening a calendar (RT Unified)](#opening-a-calendar-rt-unified)
  
[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)

### Editing calendars (RT Unified)

#### Editing a calendar used in Runtime

1. Edit the desired calendar settings.
2. Compile the project and load it into the device.

With a complete download, the changes become immediately visible in Runtime. In the case of a delta download, the changes become visible after a screen change or a browser refresh. Unsaved changes to the calendar are lost on browser refresh.

---

**See also**

[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)

### Deleting a calendar (RT Unified)

#### Requirements

A plant object in the "Plant objects" tab has a calendar.

#### Procedure

1. Double-click the plant object or select "Open" in the shortcut menu.

   The editor for plant objects opens.
2. Select the "Calendar" tab.
3. Click "Remove calendar".

The calendar is deleted.

#### Deleting a calendar used in Runtime

1. Delete the calendar.
2. Compile the project and load it into the device.

With a complete download, the Calendar is no longer directly available in Runtime. In the case of a delta download, the calendar is no longer available after a screen change or a browser refresh.

---

**See also**

[Basics on scheduling in the WinCC Unified Calendar (RT Unified)](#basics-on-scheduling-in-the-wincc-unified-calendar-rt-unified)

## Configuring a calendar control (RT Unified)

This section contains information on the following topics:

- [Inserting a calendar control into a screen (RT Unified)](#inserting-a-calendar-control-into-a-screen-rt-unified)
- [Configuring a calendar control (RT Unified)](#configuring-a-calendar-control-rt-unified-1)
- [Set up access control for calendar control (RT Unified)](#set-up-access-control-for-calendar-control-rt-unified)

### Inserting a calendar control into a screen (RT Unified)

#### Procedure

1. Select the HMI device on the "Devices" tab.
2. Open the "Screens" folder.
3. Open the screen.
4. In the "My Controls" pane, select the calendar control and place it on the screen.

### Configuring a calendar control (RT Unified)

#### Requirement

- A plant object from the plant hierarchy has a calendar.
- The screen of an HMI device has a calendar control.
- Optional: A plant overview is inserted in the screen.

#### Procedure

| Symbol | Meaning |
| --- | --- |
| 1. Open the screen. 2. Select the calendar control in the screen. 3. In the Inspector window, click on the "Properties" tab. 4. Open the "Properties" node. 5. In "Active view", select the view with which the control starts in runtime. 6. Set a link to the plant object whose calendar the control should display in runtime.    Select one of the following options:       | Symbol | Meaning |    | --- | --- |    | Dynamically during runtime via the "Plant overview" control | | Symbol | Meaning | | --- | --- | | 1. Leave the "Plant object" field empty. 2. In the "Plant overview" control, configure the calendar control as a companion control. |  |  If a plant overview has been configured for the screen, the calendar control always displays the calendar of the plant object selected in the plant overview. |    | Link manually | | Symbol | Meaning | | --- | --- | | 1. Click the "Plant object" field and the "..." button. 2. In the left-hand area, select the owner of the plant object whose calendar the control should display. 3. In the right-hand area, select the tag of the plant object. |  |   The control always shows the calendar of this plant object. |    | Linking by script | | Symbol | Meaning | | --- | --- | | 1. Select "Script" as dynamization for the "Plant object" field. 2. Enter a script that sets the path to a plant object with calendar in runtime:     `Screen.Items('<`    `CalendarControl-Name`    `>').Properties.PlantObject = "<`    `The path to the plant object`    `>";`     Example: `Screen.Items('Calendar control_1').Properties.PlantObject = "HMI_RT_1.hierarchy::Plant1/Subplant_A";` 3. Select a tag or a timer as trigger. |  |  The script determines dynamically the plant object to which the control is linked, and which calendar it displays. |       | Symbol | Meaning |    | --- | --- |    | **Note**  **Alternative for a link by script** Instead of adding the script to the "Plant object" property, you can also configure a button and add the script to an event of the button. |  | |  |

> **Note**
>
> **Transferring changes to Runtime**
>
> The changes to the calendar are only available in runtime after you have compiled them and loaded them into the device.

---

**See also**

[Configuring "Plant overview" control and companion controls (RT Unified)](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#configuring-plant-overview-control-and-companion-controls-rt-unified)

### Set up access control for calendar control (RT Unified)

#### Introduction

You can set up access control for the calendar control. With this you determine which rights the runtime user gets for the control. To do this, you can assign predefined or user-specific runtime rights to the properties "Action edit", "Planning edit" or "Full access".

| Property | Description |
| --- | --- |
| Action edit | With this right, the Runtime user can edit actions in the "Planning" tab. Editing shifts and templates is not possible. |
| Planning edit | With this right, the Runtime user can edit actions and shifts in the "Planning" tab. Creating new plans and editing templates is not possible. |
| Full access | With this right, the runtime user can fully operate the Control (change and create actions, shifts, templates) and delete runtime data. |

If no function right is assigned to a property, all runtime users have the right.

#### Function rights of the runtime user

If more than one function right is configured for a runtime user, the right with the highest privilege is taken into account.

| Action edit | Planning edit | Full access | Function rights of the runtime user |
| --- | --- | --- | --- |
| X | X | X | User has only read rights. Operation is not possible. |
| ✓ | X | X | The user has the "Action edit" right. |
| X / ✓ | ✓ | X | The user has the "Planning edit" right. |
| X / ✓ | X / ✓ | ✓ | The user has the "Full access" right. |

**Legend:**

X = The runtime user does not have the function right that is set in the property.

✓ = The runtime user has the function right that is set in the property.

Or the property is empty.

#### Requirement

- In the security settings, you have configured "Users and roles" in accordance with your needs.

  You can find more information in the section "Configuring users and roles" in the WinCC Unified help.
- The "Allow operator control" option is activated in the control properties under "Security".
- The "Authorization" option is empty in the control properties under "Security".
- In the control properties under "Properties &gt; Miscellaneous &gt; Interface", the "Require explicit unlock" option is disabled under the property "Action edit", "Planning edit" and "Full access".

  This control property is for multipoint touch displays and is not supported in V17.

#### Procedure

1. Select the desired control in the screen.
2. Expand the property "Action edit", "Planning edit" or "Full access" under "Properties &gt; Miscellaneous &gt; Interface".
3. Expand the drop-down list in the "Static value" column under "Authorization".

   The function rights are displayed.
4. Select a function right.
5. If necessary, repeat steps 2-4 to configure the additional properties.

## Compiling configuration data and loading it into Runtime (RT Unified)

### Introduction

To receive configuration data in runtime, you have the option of performing a delta compile and delta download.

You can find more information in the WinCC Unified help under "Visualize processes &gt; Compile and load".

### Configuration changes to calendar data

Not all configuration changes can be compiled and downloaded in delta mode. The following table shows you the changes to the calendar data for which a delta compile and delta download are possible:

| Element | Delta download capability | No delta download capability |
| --- | --- | --- |
| Time model | Time category:  - Change the properties of a time category - Add or delete new child time category for an existing time category - Import or export of time categories | - |
| Time model in PFI controls | - | General, if time categories are used in the PFI controls:  - Create, rename or delete - Copy and paste - Move within the plant view |
| Calendar object | Calendar object:  - Change settings - Create or move under another plant object - Delete | - |
| Plant object | - | General:   - Create, rename or delete - Copy and paste - Move within the plant view |
| Plant object types | - | In general, if an instance of the plant object type exists:  - Rename or delete |
| Calendar control | All custom control screen properties are capable of a delta download. |  |

### Effects on the active RT project

Active Runtime is not terminated by delta download. The changes are immediately applied in the active RT project and are visible in Runtime after a screen change or browser refresh.

## Validation of the configuration of plant objects (RT Unified)

### Introduction

If validation errors in the plant view, missing or faulty properties of plant objects or plant object types have arisen, these errors are displayed during compilation. With the "Go to" function, you have the possibility to jump directly to the error location and eliminate the error immediately.

### Solve causes of errors during validation

1. Navigate in the Inspector window to "Info &gt; Compile".
2. ![Solve causes of errors during validation](images/122765203595_DV_resource.Stream@PNG-de-DE.png) Set the filter so that error messages are displayed.

   If a green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png) is displayed in the "Go to" column for a message, you can go directly to the appropriate tab for correcting the cause of the alarm.
3. Select the green arrow ![Solve causes of errors during validation](images/122844867979_DV_resource.Stream@PNG-de-DE.png).

   The tab in which corrections are expected is displayed. The corresponding property is selected.

## Local reporting for calendar (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Procedure (RT Unified)](#procedure-rt-unified)
- [Defining a report template with hierarchical segment (RT Unified)](#defining-a-report-template-with-hierarchical-segment-rt-unified)
- [Creating a report job and downloading a report (RT Unified)](#creating-a-report-job-and-downloading-a-report-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-1)
- [Requirements (RT Unified)](#requirements-rt-unified-1)

#### Introduction (RT Unified)

When the Calendar option package is installed, you can generate reports of shifts in Runtime with WinCC Unified Reporting. You can then continue to edit the data in Excel or save the report as PDF and distribute or archive it.

![Figure](images/115612377099_DV_resource.Stream@PNG-de-DE.png)

#### Requirements (RT Unified)

To create reports with Calendar, the Excel add-in must be installed. In addition, you must be familiar with the basic operation of WinCC Unified Reporting. The documentation for this can be found in the TIA Portal Help under "Creating production logs".

**Basic information on report templates**

Information on creating report templates is available in the TIA Portal help, in the "Creating templates for production reports" section.

This information is also available in the Excel add-in. For this purpose, click the "?" icon in the "WinCC Unified Reporting" tab.

**Basic information on production reports in Runtime**

Information on creating production logs in Runtime is available in the TIA Portal help in the section "Working with production logs in Runtime".

### Procedure (RT Unified)

#### Requirement

- The Calendar option package is installed.
- Position the "Reports" control in a screen of a WinCC Unified device.
- The same requirements apply to the use of Reporting with the WinCC Unified basic installation.

#### Run sequence

1. Define a report template for your jobs in the Excel add-in.
2. Define a trigger for the reports in the "Reports" control.

### Defining a report template with hierarchical segment (RT Unified)

#### Introduction

You can create a report template of the plant object on which a calendar is configured.

You define report templates with hierarchical view in the Excel add-in.

#### Requirement

- Microsoft Excel is open and the "WinCC Unified" tab is visible.
- The server on which an active runtime project with Calendar configuration is running is selected in the "WinCC Unified" tab under "Connections".
- The list of options that is called from the server includes "Calendar".

#### Defining a hierarchical segment

1. In the "WinCC Unified" tab, click on "Segments".

   The list of segments is loaded.
2. Select "New segment".

   The selection menu opens.
3. Select "New hierarchical segment".

   A new hierarchical segment is created.
4. Assign a name.
5. Specify the storage location, the table and the cell in which the hierarchical segment is to start.
6. Specify a start time and an end time.
7. Confirm with "OK".

#### Adding a data source item

1. Click the created hierarchical segment.
2. Click the "+" icon.

   The menu for selecting a data source item opens.
3. Select the "Calendar" option.
4. Select the "Plant view" context definition.
5. Under "Context definition", select the plant object for which the report is to be created.

   Multiple selection is possible if you want to create a report on several plant objects.

   ![Adding a data source item](images/142298126091_DV_resource.Stream@PNG-en-US.png)

   ![Adding a data source item](images/142298126091_DV_resource.Stream@PNG-en-US.png)
6. Confirm your entries with "OK".

   The template is generated.
7. Save the report template.

**Adjusting columns**

1. Select the "Edit" button of the data source item.
2. Select the desired columns.
3. Make your changes.
4. Confirm your entries with "OK".

   The template is updated.

#### Style of the report template

You can create the report template in different styles:

- Hierarchical display (default setting)

  ![Style of the report template](images/143474438283_DV_resource.Stream@PNG-de-DE.png)
- Display in a row

  ![Style of the report template](images/143474446859_DV_resource.Stream@PNG-de-DE.png)

**Procedure**

1. Click the "Edit" button next to the created hierarchical segment.
2. Under "Indent", select the "By level" option for hierarchical display or "By attribute" for display in a row.

**Testing the template**

Test your template by clicking the ![Style of the report template](images/143423888779_DV_resource.Stream@PNG-de-DE.png) button located next to the hierarchical segment.

### Creating a report job and downloading a report (RT Unified)

#### Introduction

Before you create a report, create a report job in the "Reports" control and define a trigger. If required, download the report as an XLSX file or PDF file.

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

---
title: "Portal view and project view"
package: StdrPortalviewenUS
topics: 7
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Portal view and project view

This section contains information on the following topics:

- [Portal view](#portal-view)
- [Project view](#project-view)

## Portal view

This section contains information on the following topics:

- [Portal view](#portal-view-1)
- [Drive parameterization](#drive-parameterization)
- [Adding a new device](#adding-a-new-device)

### Portal view

#### Function of the portal view

The portal view provides you with a task-oriented view of the tools. Here, you can quickly decide what you want to do and call up the tool for the task in hand. If necessary, the view changes automatically to the [project view](#project-view-1) for the selected task.

#### Layout of the portal view

The following figure shows an example of the components in the portal view:

![Portal view](images/95588325643_DV_resource.Stream@PNG-en-US.png)

Portal view

| Symbol | Meaning |
| --- | --- |
| ① | Portals for different tasks |
| ② | Actions for the selected portal |
| ③ | Selection window for the selected action |
| ④ | Switch to the project view |
| ⑤ | Display of the project that is currently open |

#### Portals

The portals provide the basic functions for the individual task areas. The portals provided in the portal view depend on the products that have been installed.

#### Actions for the selected portal

Here, you will find the actions available to you in the portal you have selected. You can call up the help function in every portal on a context-sensitive basis.

#### Selection window for the selected action

The selection window is available in all portals. The content of the window adapts to your current selection.

#### Switch to the project view

Use the "Project view" link to change to the project view.

#### Display of the project that is currently open

Here, you can obtain information about which project is currently open.

### Drive parameterization

#### Function of drive parameterization

In the drive parameterization, add new drives to the currently open project and configure it.

#### Layout of drive parameterization

The following figure shows an example of the drive parameterization:

![Layout of drive parameterization](images/133742155403_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The currently selected portal |
| ② | All of the available actions in the drive parameterization portal |
| ③ | Selection window for the selected action |
| ④ | Switch to the project view |
| ⑤ | Display of the project that is currently open |

#### Adding a drive unit

In the action overview, click on the button ① to add a new drive unit in your currently open project.

See also: [Adding a new device](#adding-a-new-device)

#### Portals

The portals provide the basic functions for the individual task areas. The portals provided in the portal view depend on the products that have been installed.

#### Actions for the selected portal

Here, you will find the actions available to you in the portal you have selected. You can call up the help function in every portal on a context-sensitive basis.

#### Selection window for the selected action

The selection window is available in all portals. The content of the window adapts to your current selection.

#### Switch to the project view

Use the "Project view" link to change to the project view.

#### Display of the project that is currently open

Here, you can obtain information about which project is currently open.

---

**See also**

[Adding a new device](#adding-a-new-device)

### Adding a new device

#### Adding a device in the portal view

To add a drive unit to the hardware configuration in the portal view, proceed as follows:

1. Open the "Devices & Networks" portal in the left overview.
2. Click the "Add new device" button in the "Add new device" action overview.

   The "Add new device" screen form is displayed.
3. Select the required drive unit from the tree structure.

   - Select the required device in the tree structure.
   - Enter an individual device name in the "Device name" entry field.

   More information about the drive unit presently selected is displayed on the right-hand side of the dialog.
4. Select the required firmware version of the drive unit in the "Version" drop-down list.
5. Click "Add" to add the selected drive unit.

## Project view

This section contains information on the following topics:

- [Project view](#project-view-1)

### Project view

#### Definition

The project view is a structured view of all components of the project.

#### Layout of the project view

The following figure shows an example of the components of the project view:

![Layout of the project view](images/131947585803_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Title bar |
| ② | Menu bar |
| ③ | Toolbar |
| ④ | Project tree |
| ⑤ | Reference projects |
| ⑥ | Detail view |
| ⑦ | Working area |
| ⑧ | Dividers |
| ⑨ | [Inspector window](Configuring%20SINAMICS%20S-G-MV%20drives.md#inspector-window) |
| ⑩ | Switch to [portal view](#portal-view-1) |
| ⑪ | Editor bar |
| ⑫ | Status bar with progress display |
| ⑬ | Task cards |

> **Note**
>
> Detailed information on the project view components can be found in the online help under "Layout of the user interface". There the components for the entire TIA Portal are explained using examples.

#### Title bar

The name of the project is displayed in the title bar.

#### Menu bar

The menu bar contains all the commands that you require for your work.

#### Toolbar

The tool bar provides you with buttons for commands you will use frequently. This allows you to access these commands faster.

#### Dividers

Dividers separate individual components of the program interface. The arrows on the dividers allow you to display and hide the adjacent sections of the user interface.

#### Switch to portal view

Use the "Portal view" link to change to the portal view.

#### Editor bar

The opened editors are displayed in the editor bar. This allows you to quickly switch between open elements. If you have opened numerous editors, you can display the editors of the same type as a group.

#### Status bar with progress display

The status bar contains the progress display for those background processes that are running currently. This also includes a progress bar that shows the progress graphically. Hover the mouse pointer over the progress bar to display a tooltip providing additional information on the active background process. You can cancel the background processes by clicking the button next to the progress bar.

If no background processes are currently running, the status bar displays the last generated alarm.

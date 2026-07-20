---
title: "Device and network diagnostics"
package: HWCDiagenUS
topics: 87
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Device and network diagnostics

This section contains information on the following topics:

- [Hardware diagnostics](#hardware-diagnostics)
- [Connection diagnostics](#connection-diagnostics)
- [Diagnosing the OPC UA server](#diagnosing-the-opc-ua-server)
- [System diagnostics with 'Report System Errors' (S7-300, S7-400)](System%20diagnostics%20with%20%27Report%20System%20Errors%27%20%28S7-300%2C%20S7-400%29.md#system-diagnostics-with-report-system-errors-s7-300-s7-400)
- [System diagnostics for S7-1500 PLCs (S7-1500)](System%20diagnostics%20for%20S7-1500%20PLCs%20%28S7-1500%29.md#system-diagnostics-for-s7-1500-plcs-s7-1500)
- [Using additional diagnostics options (S7-300, S7-400)](Using%20additional%20diagnostics%20options%20%28S7-300%2C%20S7-400%29.md#using-additional-diagnostics-options-s7-300-s7-400)

## Hardware diagnostics

This section contains information on the following topics:

- [Overview of hardware diagnostics](#overview-of-hardware-diagnostics)
- [Showing non-editable and current values of configurable module properties](#showing-non-editable-and-current-values-of-configurable-module-properties)
- [Showing the current values of dynamic modules properties](#showing-the-current-values-of-dynamic-modules-properties)
- [Checking a module for defects](#checking-a-module-for-defects)
- [Changing the properties of a module or the programming device/PC](#changing-the-properties-of-a-module-or-the-programming-devicepc)
- [Diagnostics in STOP mode](#diagnostics-in-stop-mode)
- [Online accesses in the Online and Diagnostics view](#online-accesses-in-the-online-and-diagnostics-view)
- [Checking PROFIBUS DP subnets for faults](#checking-profibus-dp-subnets-for-faults)

### Overview of hardware diagnostics

This section contains information on the following topics:

- [Principal methods of hardware diagnostics](#principal-methods-of-hardware-diagnostics)
- [Determination of which of the devices that are connected online are defective](#determination-of-which-of-the-devices-that-are-connected-online-are-defective)
- [Displaying diagnostics status and comparison status using icons](#displaying-diagnostics-status-and-comparison-status-using-icons)
- [Start online and diagnostics view](#start-online-and-diagnostics-view)
- [Activation of the "Online Tools" task card](#activation-of-the-online-tools-task-card)

#### Principal methods of hardware diagnostics

##### Principal methods of hardware diagnostics

Hardware diagnostics can be performed as follows:

- Using the Online and Diagnostics view
- Using the "Online Tools" task card
- Using the "Diagnostics > Device Info" area of the Inspector window
- Using diagnostics icons, for example, in the device view and the project tree

##### Structure of the Online and Diagnostics view

The Online and Diagnostics view consists of two windows alongside each other:

- The left window shows a tree structure with folders and - when you open the folder - groups.
- The right window contains detailed information on the selected folder or selected group.

The "Online access" group and the "Diagnostics" and "Functions" folders are located here:

- "Online access" group: Displays whether or not there is currently an online connection with the associated target. In addition, you can establish or disconnect the online connection.
- "Diagnostics": Contains several diagnostics groups for the selected module.
- "Functions": Contains several groups, in which you can make settings for the selected module or issue commands to the module.

##### Function and structure of the "Online Tools" task card

For modules with their own operating mode (such as CPUs), the "Online tools" task card allows you to read current diagnostics information and commands to the module.

If you selected a module without its own operating mode or if you selected several modules before activation of the "Online Tools" task card, the task card relates to the relevant CPU.

The "Online Tools" task card consists of the following panes:

- CPU control panel
- Cycle time
- Memory

  > **Note**
  >
  > A pane is filled with content only if the module controls the associated functions and an online connection exists.
  >
  > If there is no online connection to the respective module, the display "No online connection" appears in blue in each pane. If an existing online connection was disconnected, then "This target is not available" will be displayed.

##### Structure or the "Diagnostics" tab of the Inspector window

The "Diagnostics" tab of the Inspector window itself consists of several tabs. Of these tabs, the following is relevant for the hardware diagnostics.

- Device information

  This tab relates to all online devices (e.g. CPUs) to which an online connection has been established and to the devices that are assigned to these online devices (such as PROFINET devices and PROFIBUS slaves). Alarms related to the faulty online devices and the faulty devices are output here.

  > **Note**
  >
  > **What is displayed when a module is faulty?**
  >
  > If a module within a device is faulty, only the associated device or its proxy (e.g. head module) are shown, but not the module itself.
  >
  > The faulty devices are displayed "at the top level" and not in a hierarchical view below their online device (as is the case in the project tree).

---

**See also**

[Basics on task cards](Introduction%20to%20the%20TIA%20Portal.md#basics-on-task-cards)
  
[Inspector window](Introduction%20to%20the%20TIA%20Portal.md#inspector-window)

#### Determination of which of the devices that are connected online are defective

##### Overview of the defective devices

In the "Diagnostics > Device Info" area of the Inspector window you will obtain an overview of the defective devices that are or were connected online.

The "Diagnostics> Device Info" area of the Inspector window consists of the following elements:

- Header line with the number of defective devices
- Table with detailed information on each defective device

If you originate the establishment of an online connection to a device which is not reachable or reports one or more faults or is not in RUN mode, it will rank as defective.

##### Structure of the table with detailed information on the defective devices

The table consists of the following columns:

- Online status: Contains the online status as a diagnostic symbol and in words
- Operating mode: Contains the operating mode as a symbol and in words
- Device / module: Name of the affected device or the affected module
- Message: explains the entry of the previous column
- Details: The link opens the online and diagnostics view for the device, and places it in the foreground. If an online connection does not exist any longer, the link will open the connection establishment dialog.
- Help: The link supplies further information on the defect that has occurred.

---

**See also**

[Inspector window](Introduction%20to%20the%20TIA%20Portal.md#inspector-window)
  
[Displaying diagnostics status and comparison status using icons](#displaying-diagnostics-status-and-comparison-status-using-icons)

#### Displaying diagnostics status and comparison status using icons

##### Determining diagnostics status online and displaying using icons

When the online connection to a device is established, the diagnostics status of the device and, if applicable, its lower-level components is determined. The operating state of the device is also determined, where applicable.

The following is a description of which icons are displayed in specific views.

- Device view

  - The associated diagnostic icon is displayed for every hardware component (except the signal board on the CPU).

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - For hardware components with their own operating state, the operating state icon is also displayed to the left of or above the diagnostic icon.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: No diagnostic icons are displayed (due to the configuration as GSDML device).
  > **Note**
  >
  > **Diagnostics status of SCALANCE-XM-400 and SCALANCE-XR-500-managed modules**
  >
  > Incorrect or no diagnostic icons are displayed in case of an existing online connection to the SCALANCE-XM-400 and SCALANCE-XR-500-managed modules.
  >
  > The correct diagnostic icons will be displayed when you establish the online connection to an associated CPU.
- Device overview

  - The associated diagnostic icon is displayed for every hardware component.

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: For modules assigned to the CPU, the associated diagnostic icon is displayed (modules that are not assigned do not receive a diagnostic icon). The associated diagnostic icon is displayed for plug-in submodules of an assigned module (submodules that are not pluggable are not visible and therefore do not receive a diagnostic icon).
- Network view

  - The associated diagnostic icon is displayed for every device.

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: A diagnostic icon is displayed. It belongs to that part of the station that is assigned to the CPU.

- Network overview

  - The associated diagnostic icon is displayed for every hardware component.

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: A diagnostic icon is displayed. It belongs to that part of the station that is assigned to the CPU.
- Topology view

  - The associated diagnostic icon is displayed for every device.

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - The associated diagnostic icon is displayed for every port. The meaning of the individual colors is described further below.
  - Each cable between two online ports is assigned the color associated with its diagnostics status.

    The color of the cable between two ports depends on the status of the individual ports:

    | Color of the first port | Color of the second port | Color of the connecting cable |
    | --- | --- | --- |
    | light green | light green | light green |
    | light green | dark green | dark green |
    | green | gray | gray |
    | green | red | red |
    | gray | red | red |
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: A diagnostic icon is displayed. It belongs to that part of the station that is assigned to the CPU.
- Topology overview

  - The associated diagnostic icon is displayed for every hardware component.

    To start the Online and Diagnostics view (if available), double-click the diagnostic icon.
  - For a hardware component with lower-level components, if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: A diagnostic icon is displayed. It belongs to that part of the station that is assigned to the CPU.

- Project tree

  - The associated diagnostic icon is displayed behind every hardware component.
  - For a hardware component with lower-level components (e.g., distributed I/O, Slave_1), if there is a hardware error in at least one lower-level component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Hardware error in lower-level component" is also shown in the lower right corner.
  - For hardware components with their own operating state, the operating state icon is also displayed in the top right corner of the diagnostic icon.
  - If forcing is active on a CPU, a red F is displayed at the left margin of the diagnostic icon.
  - The diagnostic icon "Hardware error in lower-level component" is displayed behind the "Local modules" folder when there is a hardware error in at least one of the associated modules.
  - The diagnostic icon "Hardware error in lower-level component" is displayed behind the "Distributed I/O" folder when there is a hardware error in at least one of the associated modules.
  - The diagnostic icon "Hardware error in lower-level component" is displayed behind the project folder when the "Hardware error in lower-level component" diagnostic icon is displayed behind at least one of the "Local modules" or "Distributed I/O" folders.
  - The following applies to modules or submodules of a shared device with an S7-1500 CPU: The associated diagnostic icon is displayed for modules assigned to the CPU (modules that are not assigned are grayed out and do not receive a diagnostic icon). The associated diagnostic icon is displayed for plug-in submodules of an assigned module (submodules that are not pluggable are not visible and therefore do not receive a diagnostic icon).

> **Note**
>
> If the diagnostic for a hardware component is "not reachable from the CPU", the diagnostic icon "Hardware error in lower-level component" is not additionally shown.

##### Diagnostic icons for modules and devices

The following table shows the available icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Diagnostic icons for modules and devices](images/22259303691_DV_resource.Stream@PNG-de-DE.png) | The connection with a CPU is currently being established. |
| ![Diagnostic icons for modules and devices](images/22259312907_DV_resource.Stream@PNG-de-DE.png) | The CPU is not reachable at the set address. |
| ![Diagnostic icons for modules and devices](images/22259346699_DV_resource.Stream@PNG-de-DE.png) | The configured CPU and the CPU actually present are of incompatible types. |
| ![Diagnostic icons for modules and devices](images/22259367691_DV_resource.Stream@PNG-de-DE.png) | On establishment of the online connection to a protected CPU, the password dialog was terminated without specification of the correct password. |
| ![Diagnostic icons for modules and devices](images/22259622539_DV_resource.Stream@PNG-de-DE.png) | No fault |
| ![Diagnostic icons for modules and devices](images/22259631243_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Diagnostic icons for modules and devices](images/22259716747_DV_resource.Stream@PNG-de-DE.png) | Maintenance demanded |
| ![Diagnostic icons for modules and devices](images/22259776651_DV_resource.Stream@PNG-de-DE.png) | Error |
| ![Diagnostic icons for modules and devices](images/21385506827_DV_resource.Stream@PNG-de-DE.PNG) | The module or device is deactivated. |
| ![Diagnostic icons for modules and devices](images/7142639243_DV_resource.Stream@PNG-de-DE.png) | The module or the device cannot be reached from the CPU (valid for modules and devices below a CPU). |
| ![Diagnostic icons for modules and devices](images/67131309451_DV_resource.Stream@PNG-de-DE.png) | The functionality of the module or submodule is no longer available (for example. input and output data). Possible causes:  - Difference between expected and actual configuration. - Access error during updating the process images. |
| ![Diagnostic icons for modules and devices](images/7142571275_DV_resource.Stream@PNG-de-DE.png) | Diagnostics not or only partially possible. Possible causes:  - Difference between actual online and offline configuration data. - You have not executed the command "Compile" for the hardware. - You have not executed the command "Download to device" for the hardware or the hardware configuration. - The object does not support diagnostics.   For HMI devices: No diagnostics data is available. |
| ![Diagnostic icons for modules and devices](images/22260204427_DV_resource.Stream@PNG-de-DE.png) | The connection is established, but the module status has not yet been determined or is unknown. |
| ![Diagnostic icons for modules and devices](images/22260443531_DV_resource.Stream@PNG-de-DE.png) | The configured module does not support display of the diagnostics status. |
| ![Diagnostic icons for modules and devices](images/46305869963_DV_resource.Stream@PNG-de-DE.PNG) | Hardware error in lower-level component: A hardware fault has occurred in at least one lower-level hardware component (occurs as a separate icon only in the project tree) |
| ![Diagnostic icons for modules and devices](images/171213034763_DV_resource.Stream@PNG-de-DE.PNG) | Conflicting diagnostics information for same object. |

> **Note**
>
> Some modules, for example, the FM 450-1, are only indicated as having a problem in the case of an error if you have enabled the diagnostic interrupt when assigning the module property parameters.

##### Icons for the comparison status

The diagnostic icons can be combined at the bottom right with additional smaller icons that indicate the result of the online/offline comparison. The following table shows the available comparison icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Icons for the comparison status](images/46305869963_DV_resource.Stream@PNG-de-DE.PNG) | Hardware error in lower-level component: The online and offline versions differ (only in the project tree) in at least one lower-level hardware component. |
| ![Icons for the comparison status](images/7350347275_DV_resource.Stream@PNG-de-DE.png) | Software error in lower-level component: The online and offline versions differ (only in the project tree) in at least one lower-level software component. |
| ![Icons for the comparison status](images/7350724107_DV_resource.Stream@PNG-de-DE.png) | Online and offline versions of the object are different |
| ![Icons for the comparison status](images/7350435851_DV_resource.Stream@PNG-de-DE.png) | Object only exists online |
| ![Icons for the comparison status](images/7350401803_DV_resource.Stream@PNG-de-DE.png) | Object only exists offline |
| ![Icons for the comparison status](images/24640355723_DV_resource.Stream@PNG-de-DE.PNG) | Online and offline versions of the object are the same |

> **Note**
>
> If both a comparison icon and the "Error in lower-level component" diagnostic icon are to be displayed at the bottom right in the device view, the following rule applies: The diagnostic icon for the lower-level hardware component has a higher priority than the comparison icon. This means that a comparison icon is only displayed if the lower-level hardware components have no errors.

##### Display of software errors in the project tree

- The associated comparison icon is shown behind each block.
- Behind each folder, under which exclusively blocks are contained, the diagnostic icon "Software error in lower-level component" is displayed when there is a software error in at least one of the associated blocks.
- For a hardware component with lower-level software components, if there is no hardware error and there is an error in at least one lower-level software component, the diagnostic icon appears as follows: The hardware component's diagnostic icon has a pale appearance and the diagnostic icon "Software error in lower-level component" is also shown in the lower right corner.

##### Combined diagnostics and comparison icons

The following table shows examples of icons that are displayed in the diagnostics icon.

| Icon | Meaning |
| --- | --- |
| ![Combined diagnostics and comparison icons](images/23516936715_DV_resource.Stream@PNG-de-DE.png) | Folder contains objects whose online and offline versions differ (only in the project tree) |
| ![Combined diagnostics and comparison icons](images/22262216459_DV_resource.Stream@PNG-de-DE.png) | Object only exists online |

##### Operating state icons for CPUs and CPs

The following table shows the available icons and their respective operating states.

| Icon | Operating state |
| --- | --- |
| ![Operating state icons for CPUs and CPs](images/22262493963_DV_resource.Stream@PNG-de-DE.png) | RUN |
| ![Operating state icons for CPUs and CPs](images/22262502155_DV_resource.Stream@PNG-de-DE.png) | STOP |
| ![Operating state icons for CPUs and CPs](images/22263278347_DV_resource.Stream@PNG-de-DE.png) | STARTUP |
| ![Operating state icons for CPUs and CPs](images/22263312139_DV_resource.Stream@PNG-de-DE.png) | HOLD |
| ![Operating state icons for CPUs and CPs](images/22263320331_DV_resource.Stream@PNG-de-DE.png) | DEFECTIVE |
| ![Operating state icons for CPUs and CPs](images/22263366923_DV_resource.Stream@PNG-de-DE.png) | Unknown operating state |
| ![Operating state icons for CPUs and CPs](images/22263413515_DV_resource.Stream@PNG-de-DE.png) | The configured module does not support display of the operating state. |

> **Note**
>
> If forcing is active on a CPU, a red F is displayed on a pink background at the bottom right of the operating state icon.

##### Color marking of ports and Ethernet cables

The following table shows the available colors and their respective meaning.

| Color | Meaning |
| --- | --- |
| ![Color marking of ports and Ethernet cables](images/22281128587_DV_resource.Stream@PNG-de-DE.png) | No fault or maintenance required |
| ![Color marking of ports and Ethernet cables](images/69515021835_DV_resource.Stream@PNG-de-DE.png) | Offline |
| ![Color marking of ports and Ethernet cables](images/22281136779_DV_resource.Stream@PNG-de-DE.png) | Maintenance demanded |
| ![Color marking of ports and Ethernet cables](images/22294004363_DV_resource.Stream@PNG-de-DE.png) | Communication error or topological error |
| ![Color marking of ports and Ethernet cables](images/53537798923_DV_resource.Stream@PNG-de-DE.PNG) | no diagnostic capability |

#### Start online and diagnostics view

##### Overview of possible ways of starting the Online and Diagnostics view

You can start the Online and Diagnostics view of a module to be diagnosed at the following locations:

- Overview
- Project tree
- Device view
- Device overview
- Network view
- Network overview
- Topology view
- Topological overview

In the following, examples are used to show how to proceed.

##### Requirement

The project with the module to be diagnosed is open.

> **Note**
>
> This requirement does not apply if you call the online and diagnostics view from the project tree after you have identified the accessible devices.

##### Procedure

To start the online and diagnostics view of a module, follow these steps:

1. In the project tree, open the respective device folder.
2. Double click on "Online & Diagnostics".

Or:

1. In the project tree, select the respective device folder.
2. Select the "Online & Diagnostics" command in the shortcut menu or the "Online" main menu.

Or:

1. In the project tree, open the "Online access" folder.
2. Open the folder for the interface with which you want to establish the online connection.
3. Double click on "Show/Update accessible devices".
4. Select the module to be diagnosed.
5. Select the "Online & Diagnostics" command in the shortcut menu or the "Online" main menu.

Or:

1. In the project tree, open the "Local modules" folder.
2. Select the respective device or the module that is to be diagnosed.
3. Select the "Online & Diagnostics" command in the shortcut menu or the main menu.

Or:

1. Open the device view in the device configuration.
2. Select the module to be diagnosed.
3. Select the "Online & Diagnostics" command in the shortcut menu or the "Online" main menu.

Or:

1. Open the device view in the device configuration.
2. Establish an online connection to the module to be diagnosed.
3. Double-click on the diagnostics icon above the module.

Or:

1. Open the network view in the device configuration.
2. Select the station with the module to be diagnosed.
3. Select the "Online & Diagnostics" command in the shortcut menu or the "Online" main menu.

Or:

1. Open the topology view in the device configuration.
2. Establish an online connection to the module to be diagnosed.
3. In the topology view, double-click the diagnostic icon associated with the module.

##### Result

The online and diagnostics view of the module to be diagnosed will be started. If an online connection to the associated CPU had previously been created, the header bar of the Online and Diagnostics view will now have an orange background.

> **Note**
>
> If no online connection exists when the online and diagnostics view is started, no online information is displayed and the display fields remain empty.

---

**See also**

[View in online mode](Using%20online%20and%20diagnostics%20functions.md#view-in-online-mode)

#### Activation of the "Online Tools" task card

##### Activation of the "Online Tools" task card

You can activate this task card as follows:

1. Start the online and diagnostics view.
2. Click on the "Online Tools" task card.

Or:

1. Start the device view.
2. Click on the "Online Tools" task card.

Or:

1. Start the network view.
2. Click on the "Online Tools" task card.

### Showing non-editable and current values of configurable module properties

This section contains information on the following topics:

- [Showing general properties and system-relevant information for a module](#showing-general-properties-and-system-relevant-information-for-a-module)
- [Display configured cycle times](#display-configured-cycle-times)
- [Show interfaces and interface properties of a module](#show-interfaces-and-interface-properties-of-a-module)
- [Displaying IO controllers that access modules of a Shared Device (S7-1500)](#displaying-io-controllers-that-access-modules-of-a-shared-device-s7-1500)
- [Displaying sync domain properties of a PROFINET device](#displaying-sync-domain-properties-of-a-profinet-device)
- [Displaying MRP domain properties of a PROFINET device](#displaying-mrp-domain-properties-of-a-profinet-device)
- [Displaying current firmware of a module (S7-300, S7-400, S7-1500)](#displaying-current-firmware-of-a-module-s7-300-s7-400-s7-1500)

#### Showing general properties and system-relevant information for a module

##### Where do I find the information I need?

The general properties and system-relevant information for a module can be found in the "General" group in the "Diagnostics" folder in the online and diagnostics view of the module to be diagnosed.

##### Structure of the "General" group

The "General" group consists of the following areas:

- Module
- Module information
- Vendor information

##### "Module" area

This area shows the following data of the module:

- Short designation, for example, CPU 1214C DC/DC/DC
- Article no.
- Hardware
- Firmware

- TIA Portal version

  > **Note**
  >
  > **TIA Portal version**
  >
  > The displayed TIA Portal version is the minimum version that is required to open the blocks loaded to the device or to load the blocks to the ES. This means it does not necessarily have to be the version with which you have loaded the blocks to the device.
  >
  > Fictitious example: You have installed the TIA Portal in version V14.0 SP1 on your ES and are creating a new project. This project is assigned project version V14.0. You download this project (along with its project version) to the CPU. The project version, which means V14.0, is displayed.
- Racks
- Slot

##### "Module information" area

This area shows the following data of the module that you configured during hardware configuration:

- Module name
- Installation date (not displayed for all modules)
- Additional information (not displayed for all modules)

##### "Manufacturer information" area

This area shows the following data of the module:

- Manufacturer
- Serial number
- Profile: Profile ID as hexadecimal number

  > **Note**
  >
  > You will find the corresponding profile name in the profile ID table for PROFIBUS International (see "www.profibus.com").
- Profile details: Profile-specific type as hexadecimal number

  > **Note**
  >
  > You will find the corresponding profile-specific type name in the profile-specific type table for PROFIBUS International (see "www.profibus.com").

---

**See also**

[The basics of projects](Editing%20projects.md#the-basics-of-projects)

#### Display configured cycle times

##### Where do I find the information I need?

The required information can be found in the following places:

- In the "Cycle time" group of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.
- In the "Cycle time" pane of the "Online Tools" task card

##### Structure of the "Cycle time" group in the "Diagnostics" folder of the Online and Diagnostics view

The "Cycle time" group consists of the following areas:

- Cycle time diagram (graphical display of the assigned and measured cycle times)
- Cycle time configured (display of the assigned cycle times as absolute values)
- Cycle times measured (display of the measured cycle times as absolute values)

##### Structure of the "Cycle time" pane of the "Online Tools" task card

The "Cycle time" pane displays the cycle time diagram and below it the measured cycle times as absolute values.

##### Assigned cycle times

The following assigned cycle times are displayed in the cycle time diagram and in the "Cycle time configured" area.

- [Minimum cycle time](#)
   (The minimum cycle time is the time that is required for the runtime of the cyclic program, including the runtime of all nested program parts in higher-priority organization blocks.)
- [Maximum cycle time](#)
   (The maximum cycle time monitors the permitted execution time for the user program. If the execution time of the user program exceeds the specified maximum cycle time, the operating system generates an error alarm and the CPU changes to STOP.)

In the cycle time diagram, the minimum cycle time and the maximum cycle time correspond to the two markings on the time axis.

In the "Cycle time configured" area, the assigned cycle times are displayed as absolute values.

#### Show interfaces and interface properties of a module

##### Where do I find the information I need?

The interfaces and interface properties of a module can be found in the "Diagnostics" folder in the online and diagnostics view of the module to be diagnosed in the following group:

- PROFINET interface

##### "PROFINET interface" group

This group is divided into the following areas:

- "Ethernet address" with the "Network connection" and "IP Parameters" subareas
- "Ports"

##### "Network connection" subarea of the "Ethernet address" area

This subarea shows the following data for the module:

- MAC Address:

  MAC address of the interface.

  The MAC address consists of two parts. The first part ("Basic MAC address") identifies the manufacturer (Siemens, 3COM, ...). The second part of the MAC address differentiates between the various Ethernet devices. Each Ethernet module is assigned a unique MAC address.

##### "IP Parameters" subarea of the "Ethernet address" area

This subarea shows the following data for the module:

- IP address:

  Internet protocol address of the device on the bus (TCP/IP)
- Subnet mask:

  The subnet mask shows which part of the IP address determines the membership of a particular sub-network.
- Default router:

  If the subnet is connected via a router to other subnets, the IP address of the default router must be known. This is the only way a datagram can be forwarded with a non-matching subnet address.
- IP settings:

  Identifier for the path by which the device has obtained its IP settings (IP address, subnet mask, default router).

| Identifier | Meaning |
| --- | --- |
| 0 | IP address is not initialized |
| 1 | By configuration (i.e., by the configuration loaded to the device from the device or network view) |
| 2 | Via the "Assign IP address" group of the online and diagnostics view |
| 3 | Via the DHCP server (i.e., the IP parameters are obtained by a special service from a DHCP server (Dynamic Host Configuration Protocol) and assigned for a limited time) |
| 4 | IP address is set by a user program |
| 5 | Source of IP address unknown |

- IP setting time:

  Time stamp of the last change to the IP address directly through the Ethernet connection of the module

##### "Ports" area

This area shows the following data for the module:

- Ethernet ports

  Physical properties of the PROFINET interface

| Properties of the PROFINET interface | Meaning |
| --- | --- |
| Port no. | Port number The short description of interface (X + interface no.) and port (P + port no.) is specified in parentheses. An "R" in the short description of a port means that it is a ring port. |
| Status | Displays the status of the port LINK LED.  - Status "OK" means another device (such as a switch) is connected to the port and the physical connection is available. - Status "disconnected" means no other device is connected to the port. - Status "deactivated" means that access to the port is blocked. |
| Settings | - "Automatic" for automatic network settings of the device - Network settings for speed and transmission method for manual network settings of the device |
| Operating mode | Network settings for speed and transmission method |

If you select a line in the port table, additional help information will be provided for the corresponding port.

#### Displaying IO controllers that access modules of a Shared Device (S7-1500)

##### Where do I find the information I need?

The display of those IO controllers that access the modules of a Shared Device can be found in the Online and Diagnostics view of the interface module of the Shared Device in the "Diagnostics" folder in the following area of the "PROFINET interface" group:

- IO controller

---

**See also**

[Useful information on Shared Devices (S7-300, S7-400, S7-1500)](Special%20PROFINET%20configurations.md#useful-information-on-shared-devices-s7-300-s7-400-s7-1500)

#### Displaying sync domain properties of a PROFINET device

##### Where do I find the information I need?

The sync domain properties of a PROFINET device can be found in the following area of the "PROFINET interface" group in the "Diagnostics" folder of the Online and Diagnostics view of the device to be diagnosed:

- Domain

##### "Domain" area

This area is divided into the following subareas:

- Sync domain
- MRP domain

##### What is a sync domain?

A sync domain is a group of PROFINET devices that are synchronized to a common clock. Exactly one device has the role of the sync master (clock generator); all other devices assume the role of a sync slave. The sync master is usually an IO controller or a switch.

Non-synchronized PROFINET devices are not part of a sync domain.

##### "Sync domain" subarea of the "Domain" area

This subarea shows the following properties of the sync domain:

- Name:

  Name of sync domain
- Role:

  Role of the PROFINET device in the sync domain. The following roles are possible:

  - Sync master
  - Sync slave
- Synchronization interval:

  Interval at which the synchronization is performed
- Send clock

  Smallest possible send interval for the data exchange
- Jitter accuracy of the send clock
- Reserved bandwidth for cyclic communication

#### Displaying MRP domain properties of a PROFINET device

##### Where do I find the information I need?

The MRP domain properties of a PROFINET device can be found in the following area of the "PROFINET interface" group in the "Diagnostics" folder of the Online and Diagnostics view of the device to be diagnosed:

- Domain

##### "Domain" area

This area is divided into the following subareas:

- Sync domain
- MRP domain

##### What is an MRP domain?

The Media Redundancy Protocol (MRP) enables redundant networks to be structured. Redundant transmission paths (ring topology) ensure that, if one transmission path fails, an alternative communication path is available. The PROFINET devices that are part of this redundant network form an MRP domain.

##### "MRP domain" subarea of the "Domain" area

This subarea shows the following properties of the MRP domain:

- Name:

  Name of MRP domain
- Role:

  Role of the PROFINET device in the MRP domain. The following roles are possible:

  - Manager
  - Manager (Auto)
  - Client
  - Not a device of the ring
- Ring port 1:

  The port of the PROFINET device that has the "Ring port 1" property
- Ring port 2:

  The port of the PROFINET device that has the "Ring port 2" property
- Status of the MRP ring:

  Indicates whether the ring is interrupted ("open" status) or not ("closed" status).

#### Displaying current firmware of a module (S7-300, S7-400, S7-1500)

##### Displaying firmware

You can display the currently installed firmware of a module.

##### Requirements

- The module supports a firmware update.
- The module is connected online.

##### Procedure

To display the current firmware, follow these steps:

1. Open the module in the Online and Diagnostics view.
2. Select the "Firmware update" group in the "Functions" folder.
3. You read off the current firmware in the "Online data" area under "Firmware".

### Showing the current values of dynamic modules properties

This section contains information on the following topics:

- [Display measured cycle times](#display-measured-cycle-times)
- [Showing the current status of the LEDs of a CPU](#showing-the-current-status-of-the-leds-of-a-cpu)
- [Showing fill levels of all types of memory on a CPU](#showing-fill-levels-of-all-types-of-memory-on-a-cpu)
- [Displaying fill level of all types of memory of an S7-1500 CPU (S7-1500)](#displaying-fill-level-of-all-types-of-memory-of-an-s7-1500-cpu-s7-1500)

#### Display measured cycle times

##### Where do I find the information I need?

The measured cycle times can be found at each of the following places:

- In the "Cycle time" group of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.
- In the "Cycle time" pane of the "Online Tools" task card

##### Structure of the "Cycle time" group in the "Diagnostics" folder of the Online and Diagnostics view

The "Cycle time" group consists of the following areas:

- Cycle time diagram (graphical display of the assigned and measured cycle times)
- Cycle time configured (display of the assigned cycle times as absolute values)
- Cycle times measured (display of the measured cycle times as absolute values)

##### Structure of the "Cycle time" pane of the "Online Tools" task card

The "Cycle time" pane displays the cycle time diagram and below it the measured cycle times as absolute values.

##### Graphical display of the measured cycle times

The following measured cycle times are displayed in the cycle time diagram:

- Shortest cycle time: Duration of the shortest cycle since the last transition from STOP to RUN

  This corresponds to the dashed gray arrow on the left in the diagram.
- Current / last cycle time: Duration of the last cycle

  This corresponds to the green arrow in the diagram. If the current / last cycle time exceeds the maximum cycle time, the arrow will turn red.

  > **Note**
  >
  > If the duration of the last cycle comes close to the maximum cycle time, it may be possible that it will be exceeded. Depending on the CPU type, parameter assignment and your user program, the CPU can switch to STOP mode. If for instance you are monitoring the tags in your program, this will increase the cycle time.
  >
  > If the cycle lasts longer than double the maximum cycle time, and you do not restart the maximum cycle time in the user program (by calling the extended RE_TRIGR) instruction, the CPU will switch to STOP mode.
- Longest cycle time: Duration of the longest cycle since the last transition from STOP to RUN.

  This corresponds to the dashed blue arrow on the right in the diagram.

A blue band extends between the two dashed lines; this band corresponds to the entire range of the measured cycle times. If a measured cycle time is greater than the maximum cycle time, the portion of the band that lies outside the assigned limits will be colored red.

##### Display of the measured cycle times as absolute values

The following measured times are displayed in the "Cycle times measured" area and in the "Cycle time" pane.

- Shortest cycle time since the last transition from STOP to RUN.
- Current/last cycle time:
- Longest cycle time since the last transition from STOP to RUN.

#### Showing the current status of the LEDs of a CPU

##### Where do I find the information I need?

The current status of the LEDs of a CPU can be found in the display area of the "CPU control panel" pane of the "Online tools" task card.

##### Display area of the "CPU control panel" pane of the "Online Tools" task card

This area contains the following displays:

- Station name and CPU type (short designation)
- RUN / STOP (corresponds to the "RUN / STOP" LED of the CPU)
- ERROR (corresponds to the "ERROR" LED on the CPU)
- MAINT (corresponds to the "MAINT" LED on the CPU)

#### Showing fill levels of all types of memory on a CPU

##### Where do I find the information I need?

The fill levels of all types of memory on a CPU can be found on the following two pages:

- In the display area of the "Memory" group in the "Diagnostics" folder in the online and diagnostics view of the module to be diagnosed
- In the display area of the "Memory" pane on the "Online Tools" task card

##### Display area of the "Memory" group in the "Diagnostics" folder of the online and diagnostics view

This area contains the current memory utilization of the associated module and details of the individual memory areas.

The memory utilization is shown both as a bar diagram and as a numerical value (percentage).

The following memory utilizations are shown:

- Load memory

  If no memory card is inserted, the internal load memory is displayed.

  If a memory card is inserted, the operating system only uses the inserted load memory as the load memory. This is displayed here.
- Work memory
- Retentive memory

##### Display area of the "Memory" pane of the "Online Tools" task card

This area contains the current memory utilization of the associated module. The available memory is shown both as a bar diagram and as a numerical value (percentage). The numerical value is rounded to an integer value.

> **Note**
>
> If less than 1% of a memory area is utilized, the available portion of this memory area is shown as "99%".

The following memory utilizations are shown:

- Load memory

  If no memory card is inserted, the internal load memory is displayed.

  If a memory card is inserted, the operating system only uses the inserted load memory as the load memory. This is displayed here.
- Work memory
- Retentive memory

---

**See also**

[Load memory (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#load-memory-s7-1200)
  
[Work memory (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#work-memory-s7-1200)
  
[Retentive memory areas (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#retentive-memory-areas-s7-1200)

#### Displaying fill level of all types of memory of an S7-1500 CPU (S7-1500)

##### Where do I find the information I need?

The fill levels of all types of memory of an S7-1500 CPU can be found at the following two places:

- In the display area of the "Memory" group in the "Diagnostics" folder in the online and diagnostics view of the module to be diagnosed
- In the display area of the "Memory" pane on the "Online Tools" task card

##### Display area of the "Memory" group in the "Diagnostics" folder of the online and diagnostics view

This area contains the current memory utilization of the associated module and details of the individual memory areas.

The memory utilization is shown both as a bar diagram and as a numerical value (percentage).

The following memory utilizations are shown:

- Load memory

  > **Note**
  >
  > The load memory is located on the SIMATIC memory card.
- Code work memory: work memory for program code
- Data work memory: work memory for data blocks
- Retentive memory

##### Display area of the "Memory" pane of the "Online Tools" task card

This area contains the current memory utilization of the associated module. The available memory is shown both as a bar diagram and as a numerical value (percentage). The numerical value is rounded to an integer value.

> **Note**
>
> If less than 1% of a memory area is utilized, the available portion of this memory area is shown as "99%".

The following memory utilizations are shown:

- Load memory

  > **Note**
  >
  > The load memory is located on the SIMATIC memory card.
- Code work memory: work memory for program code
- Data work memory: work memory for data blocks
- Retentive memory

---

**See also**

[CPU memory areas (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#cpu-memory-areas-s7-1500)

### Checking a module for defects

This section contains information on the following topics:

- [Determining the diagnostic status of a module](#determining-the-diagnostic-status-of-a-module)
- [Performing communication diagnostics of PROFINET ports](#performing-communication-diagnostics-of-profinet-ports)
- [PROFINET IO component diagnostics](#profinet-io-component-diagnostics)
- [Reading out the diagnostics buffer of a CPU](#reading-out-the-diagnostics-buffer-of-a-cpu)
- [Saving service data (S7-1200, S7-1500)](#saving-service-data-s7-1200-s7-1500)

#### Determining the diagnostic status of a module

##### Where is the diagnostics status of a module displayed?

The diagnostic status of a module is displayed in the "Diagnostic status" group in the "Diagnostics" folder in the online and diagnostics view of the module to be diagnosed.

The "Diagnostics status" group consists of the following areas:

- Status
- Standard diagnostics (for S7-300 and S7-400 only for non-CPU modules)

##### "Status" area

The following status information is displayed in this area:

- Status of the module as viewed by the CPU, for example:

  - Module available and OK.
  - Module defective.

    If the module experiences a fault and you have enabled the diagnostic error interrupt during configuration, the "Module defective" status is displayed.
  - Module configured, but not available.

    Example: Diagnostics data is not available because the current online configuration differs from the offline configuration.
- Detected differences between the configured and the inserted module. Provided it can be ascertained, the article number will be displayed for the set and actual type.

The scope of the displayed information depends on the selected module.

##### "Standard diagnostics" area

The following diagnostics information for non-CPU modules is displayed in this area:

- Internal and external faults that relate to the overall module
- Associated diagnostics events

Examples of such diagnostics information are:

- Entire backup failed
- Module defective

  > **Note**
  >
  > **Diagnostic interrupts**
  >
  > A diagnostic interrupt can be reported to the CPU only if the module has diagnostic interrupt capability and the diagnostic interrupt has been enabled.
  >
  > The display of the diagnostic interrupt is a snapshot. Sporadic module defects can be identified in the diagnostics buffer of the respective CPU.

#### Performing communication diagnostics of PROFINET ports

##### Where are port-specific errors of PROFINET ports displayed?

The port-specific errors of PROFINET ports are displayed in the "Communication diagnostics" group of the "Diagnostics" folder in the Online and Diagnostics view of the module to be diagnosed.

##### Structure of the "Communication diagnostics" group

The "Communication diagnostics" group consists of the following areas:

- Table containing the port-specific errors
- "Details of the event" text field
- "Help on event" text field

##### Structure of the table containing the port-specific errors

Each line of the error table corresponds to one error.

The table consists of the following columns:

- Name: port no. and port designation, as well as diagnostics icon
- Error: description of the error that occurred on this port

##### "Details" text field

If you select a line in the error table, the "Detail" text field will contain detailed information (if available) on the corresponding error.

##### "Help on selected diagnostic line" text field

If you select a line in the error table, the "Help on selected diagnostic line" text field will contain help information (if available) on the corresponding error.

#### PROFINET IO component diagnostics

##### Where do I perform PROFINET IO component diagnostics?

You perform the PROFINET IO component diagnostics in the "PROFINET IO diagnostics" group under "PROFINET interface" in the "Diagnostics" folder of the Online and Diagnostics view.

##### "PROFINET IO diagnostics" group

Manufacturer-related diagnostics texts for the IO device or the selected module of the IO device are displayed in this area.

If the diagnostics can be read by the IO controller, then communication errors and configuration errors (online/offline discrepancies) are displayed here.

#### Reading out the diagnostics buffer of a CPU

##### Where do you read out the diagnostics buffer of a CPU?

You read out the diagnostics buffer of a CPU in the "Diagnostics buffer" group in the "Diagnostics" folder in the Online and Diagnostics view.

##### Structure of the "Diagnostics buffer" group

The "Diagnostics buffer" group consists of the following areas:

- "Events"
- "Settings"

##### Diagnostics buffer

The diagnostics buffer is used as a log file for the diagnostics events that occurred on the CPU and the modules assigned to it. These are entered in the order of their occurrence, with the latest event shown at the top.

##### "Events" area

The "Events" area consists of the following elements:

- Check box "CPU time stamp takes into account local PG/PC time"
- Event table
- "Freeze display" or "Cancel freeze" button
- Details of the event: Event no., event ID, module and possibly station or device name, rack/slot, description, help on the event, plant designation, location identifier, coming/going information, event type
- "Open in editor", "Save as" buttons

##### Check box "CPU time stamp takes into account local PG/PC time"

If you have not activated the check box, the diagnostics buffer entries are shown with the module time.

If you have activated the check box, the diagnostics buffer entries are shown with the time given by the following formula:

Displayed time = module time + time zone offset on your programming device / PC

This requires the module time to be identical to UTC.

You should use this setting if you wish to see the times of the diagnostics buffer entries for the module expressed in the local time of your programming device / PC.

Selecting or clearing the check box immediately changes the times displayed for the diagnostics buffer entries.

> **Note**
>
> If you use the "WR_SYS_T" instruction in your program or if you set the real-time clock of the CPU using an HMI device instead of using UTC, we recommend that you clear the "CPU time stamp takes into account local PG/PC time" check box. In this case, the module time is the sole time of concern.

##### Event table

The following information is displayed in the table for each diagnostics event:

- Sequential number of the entry

  The first entry contains the latest event.
- Date and time of the diagnostics event

  If no date and time are shown, the module has no integrated clock.
- Short name of the event and, if applicable, the reaction of the CPU

  > **Note**
  >
  > If an individual parameter of a text cannot be determined, the character string "###" is shown in its place.
  >
  > If no display text is yet available for new modules or new events, the numbers of the events and the individual parameters are stated as hexadecimal values.
- Only for S7-1200 and S7-1500 CPUs: Icon for the event type

  The following table shows the available icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Event table](images/21807039883_DV_resource.Stream@PNG-de-DE.PNG) | OK (no maintenance and/or no fault) |
| ![Event table](images/21807047435_DV_resource.Stream@PNG-de-DE.PNG) | Maintenance required |
| ![Event table](images/21807080587_DV_resource.Stream@PNG-de-DE.PNG) | Maintenance demanded |
| ![Event table](images/21807088139_DV_resource.Stream@PNG-de-DE.PNG) | Error |

- Icon for information related to incoming/outgoing status

  The following table shows the available icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Event table](images/21806912523_DV_resource.Stream@PNG-de-DE.PNG) | Incoming event |
| ![Event table](images/21806966027_DV_resource.Stream@PNG-de-DE.PNG) | Outgoing event |
| ![Event table](images/21806973579_DV_resource.Stream@PNG-de-DE.PNG) | Incoming event to which there is no independent outgoing event |
| ![Event table](images/21807019531_DV_resource.Stream@PNG-de-DE.PNG) | User-defined diagnostics event |

You can change the order of the columns, adjust the column widths and remove and add individual columns in the event table. In addition, you can sort as follows: by sequential number, by "Date and time" and by "Event".

##### "Freeze display" or "Cancel freeze" button

The "Freeze display" or "Cancel freeze" button is only enabled when there is an online connection to the CPU.

The default setting is "Freeze display".

The following happens when you click the "Freeze display" button:

- The current display of the diagnostics buffer entries is frozen.
- The labeling of the button changes to "Cancel freeze".

If an error has occurred in your system, diagnostics events can occur very quickly in succession. This produces a high update rate on the display. Freezing the display allows you to calmly examine the situation in more detail.

If the display is frozen and you click the "Cancel freeze" button, the following happens:

- The display of the diagnostics buffer entries is updated again.
- The labeling of the button changes to "Freeze display".

> **Note**
>
> If you freeze the diagnostics buffer display, the CPU continues to enter events in the diagnostics buffer.

##### Details of the event

If you select a line in the list of events, you obtain detailed information on the respective event:

- Sequential number of the event in the diagnostics buffer
- Event ID
- Module and, if applicable, station or device name
- Rack/slot
- Description of the event with event-specific additional information. Examples of this additional information:

  - Command that caused the event
  - Operating mode switch caused by the diagnostics event
- Help on the event: The selected event is explained in more detail and possible solutions may be specified. With outgoing events, the text "Outgoing event: "No user action required" is displayed.
- Only for S7-1200 and S7-1500 CPUs: Plant designation, location identifier
- Information on whether the event is an incoming or outgoing event
- Type of event. The following types of event are possible:

  - OK (no maintenance and/or no fault)
  - Maintenance required
  - Maintenance demanded
  - Error

##### "Open in editor" button

The following table shows if the "Open block" button is active and which function it conceals.

| When is the "Open in editor" button enabled? | What happens when you click this button? |
| --- | --- |
| If the diagnostics event references the relative address of a block.  This is the address of the command that caused the event. | The "Open in editor" function opens the referenced block in the offline view at the programming instruction that causes the error. This allows you to check and, if necessary, change the source code of the block at the specified place and then download it again to the CPU. |
| If the diagnostics event was triggered by a module. | The "Open in editor" function opens the Device view of the module involved. |

##### "Save as ..." button

If you click this button, the content of the diagnostics buffer is saved in a text file. "Diagnostics", depending on the language, with the extension ".txt" is suggested as the file name. You can however change this name.

##### "Settings" area

The "Settings" area consists of the following elements:

- "Display events" list
- "Apply settings as default" button
- "Output event information in hexadecimal format" check box

##### List "Display events:"

There is an check box in this list for every event class (default setting: all check boxes are selected). If you clear a check box, the events of that event class is no longer displayed in the "Events" area. Reselecting the check box displays the associated events once again.

##### "Apply settings as default" button

If you click this button, the settings are also applied to future occasions when the "Events" tab is opened.

##### "Output event information in hexadecimal format" check box

If you select the check box, the event IDs in the Events list of the "Events" area is displayed in hexadecimal format. If you clear the check box, the event information is given in text form.

---

**See also**

[Basic information on the diagnostics buffer](#basic-information-on-the-diagnostics-buffer)

#### Saving service data (S7-1200, S7-1500)

##### Validity

The following description applies to S7-1200 CPUs as of firmware version V4.5, to S7-1500 CPUs and various SIMATIC NET CPs.

##### Purpose

In the event of servicing it may be possible that the SIEMENS Customer Support requires very special information about the state of a module of your system for diagnostic purposes.

If such a case occurs in your system, you will be asked by Customer Support to save the service data of the module and send the resulting file to them.

##### Where do you carry out the saving of service data of a module?

You carry out the saving of service data of a module in its online and diagnostics view at the following points: In the "Functions" folder in the "Save service data" group

The "Save service data" group consists of the following areas:

- Online data
- Saving service data

##### "Online data" area

This area shows the following data of the module:

- Article number
- Firmware version
- Module name (you configured this while configuring the hardware.)
- Rack
- Slot

##### Area "Save service data"

Proceed as follows to create and save a file with special service data:

1. Select the point in the file system at which you want to save the file:

   - You use the path preset in the "Path" field.
   - Click the three-dot (browse) button. In the dialog that opens specify the desired path and enter the file name.
2. Click "Save service data".

##### Result

The data is stored in a .dmp file with the following naming convention: "<MLFB><Serial number><Time stamp>.dmp". You can change the file name later.

---

**See also**

[Reading out service data (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#reading-out-service-data-s7-300-s7-400-s7-1500)

### Changing the properties of a module or the programming device/PC

This section contains information on the following topics:

- [Changing the mode of a CPU](#changing-the-mode-of-a-cpu)
- [Performing a memory reset](#performing-a-memory-reset)
- [Determining and setting the time of day on a CPU](#determining-and-setting-the-time-of-day-on-a-cpu)
- [Managing password to protect confidential configuration data](#managing-password-to-protect-confidential-configuration-data)
- [Resetting an S7 CPU to the factory settings (S7-1200, S7-1500)](#resetting-an-s7-cpu-to-the-factory-settings-s7-1200-s7-1500)
- [Resetting a PROFINET IO device to factory settings (S7-1500)](#resetting-a-profinet-io-device-to-factory-settings-s7-1500)
- [Formatting an S7-1500 memory card (S7-1500)](#formatting-an-s7-1500-memory-card-s7-1500)
- [Updating the firmware of a module](#updating-the-firmware-of-a-module)
- [Assigning an IP address to a PROFINET IO device](#assigning-an-ip-address-to-a-profinet-io-device)
- [Assigning a PROFINET device name](#assigning-a-profinet-device-name)
- [Calibrating an S7-1500 analog module (S7-1500)](#calibrating-an-s7-1500-analog-module-s7-1500)
- [Loading I&M data to PROFINET IO devices and your modules](#loading-im-data-to-profinet-io-devices-and-your-modules)

#### Changing the mode of a CPU

##### Requirement

There is an online connection to the CPU whose mode you want to change.

##### Procedure

To change the mode of the CPU, follow these steps:

1. Enable the "Online tools" task card of the CPU.
2. Click the "RUN" button in the "CPU control panel" pane if you want to change the CPU to RUN mode or the "STOP" button if you want to change the CPU to STOP mode.
3. Acknowledge the confirmation prompt with "OK".

**Note**

The only button active is the one that can be selected in the current operating mode of the CPU.

Or:

1. Open the "Online" menu.
2. Choose the "Start CPU" menu command if you want to set the CPU to RUN mode and "Stop CPU" if you want to set the CPU to STOP mode.
3. Acknowledge the confirmation prompt with "OK".

**Note**

The only button that is active is the one that can be chosen in the current operating mode of the CPU.

Or:

1. Click the "Start CPU" button in the toolbar if you want to set the CPU to RUN mode and the "Stop CPU" button if you want to set the CPU to STOP mode.
2. Acknowledge the confirmation prompt with "OK".

**Note**

The only button that is active is the one that can be chosen in the current operating mode of the CPU.

##### Result

The CPU will be switched to the required operating mode.

#### Performing a memory reset

##### Requirement

- There is an online connection to the CPU on which the memory reset is to be performed.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the memory reset, you can place it in STOP mode after acknowledging a confirmation prompt.

##### Procedure

To perform a memory reset on a CPU, follow these steps:

1. Enable the "Online Tools" task card of the CPU.
2. Click the "MRES" button in the "CPU control panel" pane.
3. Acknowledge the confirmation prompt with "OK".

##### Result

The CPU is switched to STOP mode, if necessary, and the memory reset is performed on the CPU.

---

**See also**

[Basics of a memory reset (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#basics-of-a-memory-reset-s7-1200)
  
[Basics of a memory reset (S7-300, S7-400)](Functional%20description%20of%20S7-300-400%20CPUs%20%28S7-300%2C%20S7-400%29.md#basics-of-a-memory-reset-s7-300-s7-400)
  
[Basics of a memory reset (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#basics-of-a-memory-reset-s7-1500)

#### Determining and setting the time of day on a CPU

##### Where do I find the functions I need?

You determine and change the time of day on a CPU in the "Set time of day" group in the "Functions" folder of the Online and Diagnostics view. This requires an online connection.

##### Structure of the "Set time of day" group

The "Set time of day" group consists of the following areas:

- Area for reading out and setting the time of day
- Time system (This area does not exist for S7-1200 and will not be examined here.)

##### Structure of the area for reading out and setting the time of day

This area consists of the following parts:

- Programming device / PC time

  Here the time zone setting, the current date and the current time setting of your programming device / PC are displayed.
- Module time

  Here the date and time values currently read from the module (for example the CPU), are converted to local time and date and displayed.

  If the "Take from PG/PC" check box is selected, when you click the "Apply" button, the date and the PG/PC time converted to UTC are transferred to the module.

  If the "Take from PG/PC" check box is not selected, you can assign the date and time for the integrated clock of the module. After clicking the "Apply" button, the date and the time recalculated to UTC time are transferred to the module.

---

**See also**

[Overview of the CPU properties (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#overview-of-the-cpu-properties-s7-1500)

#### Managing password to protect confidential configuration data

This section contains information on the following topics:

- [Setting passwords for protecting confidential PLC configuration data](#setting-passwords-for-protecting-confidential-plc-configuration-data)
- [Deleting passwords for protecting confidential PLC configuration data](#deleting-passwords-for-protecting-confidential-plc-configuration-data)
- [Modifying passwords for protecting confidential PLC configuration data](#modifying-passwords-for-protecting-confidential-plc-configuration-data)

##### Setting passwords for protecting confidential PLC configuration data

###### Requirement

- There is an online connection to the CPU where you want to set the password to protect confidential PLC configuration data.
- The protection of confidential PLC configuration data is enabled (check box under Properties>General>Protection & Security>Protection of PLC configuration data).
- The password to protect confidential PLC configuration data was deleted or has not yet been set.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in the operating state RUN, you can set it to the operating state STOP when setting the password after a positive answer to a security question.

###### Procedure

Proceed as follows:

1. Open the Online and Diagnostics view of the CPU.
2. In the "Functions" folder, select the "Password to protect the PLC configuration data" group.

   The "Protection of confidential PLC configuration data" dialog box opens.
3. Click "Set".

   Another dialog window opens.
4. Enter the password in the upper text box and confirm by entering it again in the lower text box. Click "OK".

   The "Protection of confidential PLC configuration data" dialog box opens. "********" is shown in the "Password" box. The "Set" button is unavailable.

###### Result

The password to protect confidential PLC configuration data has been set.

##### Deleting passwords for protecting confidential PLC configuration data

###### Requirement

- There is an online connection to the CPU where you want to delete the password to protect confidential PLC configuration data.
- The protection of confidential PLC configuration data is enabled (check box under Properties>General>Protection & Security>Protection of PLC configuration data).
- The password for protecting confidential PLC configuration data was set earlier.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in the operating state RUN, you can set it to the operating state STOP when deleting the password after a positive answer to a security prompt.

###### Procedure

Proceed as follows:

1. Open the Online and Diagnostics view of the CPU.
2. In the "Functions" folder, select the "Password to protect the PLC configuration data" group.

   The "Protection of confidential PLC configuration data" dialog box opens. The "Set" button is unavailable.
3. Click "Delete".

   Another dialog opens, informing you that deleting the password to protect confidential PLC configuration data can place the PLC in a state where it no longer correctly functions.
4. Confirm the confirmation prompt with "Yes".

   The "Protection of confidential PLC configuration data" dialog box opens. The "Password" box is empty, the "Set" button is operable and the "Delete" button is unavailable.

###### Result

The password to protect confidential PLC configuration data has been deleted.

##### Modifying passwords for protecting confidential PLC configuration data

###### Requirement

- There is an online connection to the CPU where you want to change the password to protect confidential PLC configuration data.
- The protection of confidential PLC configuration data is enabled (check box under Properties>General>Protection & Security>Protection of PLC configuration data).
- The password for protecting confidential PLC configuration data was set earlier.
- The CPU is in STOP mode.

###### Procedure

Proceed as follows:

1. Delete the present password to protect confidential configuration data: [Deleting passwords for protecting confidential PLC configuration data](#deleting-passwords-for-protecting-confidential-plc-configuration-data)
2. Set a password to protect confidential configuration data: [Setting passwords for protecting confidential PLC configuration data](#setting-passwords-for-protecting-confidential-plc-configuration-data)

###### Result

The password to protect confidential PLC configuration data has been changed.

#### Resetting an S7 CPU to the factory settings (S7-1200, S7-1500)

This section contains information on the following topics:

- [Resetting an S7-1200 CPU to factory settings (S7-1200)](#resetting-an-s7-1200-cpu-to-factory-settings-s7-1200)
- [Restoring the factory settings of an S7-1200 CPU as of firmware version V4.5 without a memory card (S7-1200)](#restoring-the-factory-settings-of-an-s7-1200-cpu-as-of-firmware-version-v45-without-a-memory-card-s7-1200)
- [Resetting an S7-1500 CPU to factory settings (S7-1500)](#resetting-an-s7-1500-cpu-to-factory-settings-s7-1500)
- [Restoring the factory settings of an S7-1200 CPU as of firmware version V4.5 with a memory card or an S7-1500 CPU as of firmware version V2.9 (S7-1200, S7-1500)](#restoring-the-factory-settings-of-an-s7-1200-cpu-as-of-firmware-version-v45-with-a-memory-card-or-an-s7-1500-cpu-as-of-firmware-version-v29-s7-1200-s7-1500)

##### Resetting an S7-1200 CPU to factory settings (S7-1200)

###### Requirement

- There is no memory card inserted in the CPU.
- There is an online connection to the CPU that you want to reset to the factory settings.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the reset operation, you can place it in STOP mode by answering the security prompt with yes.

###### Procedure

To reset an S7-1200 CPU to factory settings, follow these steps:

1. Open the Online and Diagnostics view of the CPU.
2. Select the "Reset to factory settings" group in the "Functions" folder.
3. Select the "Keep IP address" check box if you want to keep the IP address or the "Delete IP address" check box if you want to delete the IP address.
4. Click the "Reset" button.
5. Acknowledge the confirmation prompt with "OK".

**Note**

The two check boxes mentioned are only available if the module to be reset is able to choose whether to retain or delete the IP address.

###### Result

The module is switched to STOP mode if necessary and the settings are then reset to factory settings. This means:

- The work memory and the internal load memory and all operand areas are cleared.
- All parameters are reset to their defaults.
- The diagnostic buffer is cleared.
- The time is reset.
- The IP address is kept or deleted depending on which setting you made.

##### Restoring the factory settings of an S7-1200 CPU as of firmware version V4.5 without a memory card (S7-1200)

###### Requirement

- There is no memory card inserted in the CPU.

  > **Note**
  >
  > **S7-1200-CPU with memory card**
  >
  > If your S7-1200 CPU as of firmware version V4.5 has a memory card inserted, it will behave like a S7-1500 CPU as of firmware version V2.9 when restoring the factory settings: See [Restoring the factory settings of an S7-1200 CPU as of firmware version V4.5 with a memory card or an S7-1500 CPU as of firmware version V2.9](#restoring-the-factory-settings-of-an-s7-1200-cpu-as-of-firmware-version-v45-with-a-memory-card-or-an-s7-1500-cpu-as-of-firmware-version-v29-s7-1200-s7-1500)
- There is an online connection to the CPU that you want to reset to the factory settings.
- The password for protecting confidential PLC configuration data was set earlier.
- The CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the reset operation, you can place it in STOP mode by answering the security prompt with yes.

###### Procedure

To restore the factory settings of an S7-1200 CPU as of firmware version V4.5 in which no memory card is inserted, follow these steps:

1. Open the Online and Diagnostics view of the CPU.
2. In the "Functions" folder, select the "Reset to factory settings" group.

   > **Note**
   >
   > **"Format memory card" check box**
   >
   > The "Format memory card" check box is unavailable.
3. Select the "Delete IP address" check box if you want to delete the IP address.
4. Select the "Delete password to protect confidential PLC configuration data" check box if you want to delete this password.
5. Click "Reset".
6. Click "OK" in response to the confirmation prompt.

###### Result

The module is switched to STOP mode if necessary and the settings are then reset to factory settings. This means:

- The work memory, the internal load memory and the remanent memory areas are deleted.
- All parameters are reset to their default values.
- The diagnostic buffer is cleared.
- The time is reset.
- The I&M data are deleted except for I&M0 data.
- The runtime meters are reset.
- The IP address is retained or deleted, depending on the setting you have made.
- The password for protecting confidential PLC configuration data is retained or deleted depending on the setting you have made.

##### Resetting an S7-1500 CPU to factory settings (S7-1500)

###### Requirement

- If you start a reset to factory settings from the project context, an online connection to the relevant CPU must exist.
- The relevant CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the reset operation, you can place it in STOP mode after acknowledging a confirmation prompt.

###### Procedure

To reset an S7-1500 CPU to factory settings, follow these steps:

1. Open the Online and Diagnostics view of the CPU (either from the project context or via "Accessible devices").
2. Select the "Reset to factory settings" group in the "Functions" folder.
3. Select the "Keep IP address" check box if you want to keep the IP address or the "Delete IP address" check box if you want to delete the IP address.
4. Click the "Reset" button.
5. Acknowledge the confirmation prompt with "OK".

**Note**

With "Delete IP address", all IP addresses are deleted. This applies regardless of how you created the online connection.

If a memory card is inserted, selecting the "Delete IP address" option causes the following: The IP addresses are deleted and the CPU is reset to factory settings. Then, the configuration (including IP addresses) that is stored on the memory card is transferred into the CPU (see below). If the memory card was formatted before resetting to factory settings or if it is empty, no IP address is transferred into the CPU.

###### Result

The module is switched to STOP mode if necessary and the settings are then reset to factory settings. This means:

- The work memory and the internal retentive system memory and all operand areas are cleared.
- All parameters are reset to their defaults.
- The diagnostic buffer is cleared.
- The time of day is reset.
- The I&M data are deleted except for I&M0 data.
- The runtime meters are reset.
- The IP address is kept or deleted depending on which setting you made.
- If a memory card was inserted prior to the reset to factory settings, the configuration contained on the memory card (hardware and software) is downloaded to the CPU.

##### Restoring the factory settings of an S7-1200 CPU as of firmware version V4.5 with a memory card or an S7-1500 CPU as of firmware version V2.9 (S7-1200, S7-1500)

###### Requirement

- There is an online connection to the CPU that you want to reset to the factory settings.
- The currently set protection level allows write access to the CPU.
- The password for protecting confidential PLC configuration data has already been set.
- The relevant CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start the reset operation, you can place it in STOP mode by responding to the security prompt with a positive answer.

###### Procedure

To restore the factory settings of an S7-1200 CPU as of firmware version V4.5 with an inserted Memory Card or an S7-1500 CPU as of firmware version V2.9, follow these steps:

1. Open the Online and Diagnostics view of the CPU.
2. In the "Functions" folder, select the "Reset to factory settings" group.
3. Select the "Delete IP address" check box if you want to delete the IP address.

   > **Note**
   >
   > With "Delete IP address", all IP addresses are deleted. This applies regardless of how you created the online connection.
   >
   > If a Memory Card is inserted, selecting the "Delete IP address" check box causes the following: The IP addresses are deleted, and the CPU is reset to factory settings. Then, the configuration (including IP addresses) that is stored on the Memory Card is transferred to the CPU (see below). If the Memory Card was formatted before resetting to factory settings, or if it is empty, or you have selected the "Format memory card" check box, no IP address is transferred to the CPU.
4. Select the "Delete password to protect confidential PLC configuration data" check box if you want to delete this password.

   > **Note**
   >
   > **Delete password to protect confidential configuration data**
   >
   > If you select the "Delete password to protect confidential PLC configuration data" check box, the Memory Card is deleted. If you want to delete the password to protect confidential PLC configuration data without deleting the Memory Card, you must proceed as follows:[Deleting passwords for protecting confidential PLC configuration data](#deleting-passwords-for-protecting-confidential-plc-configuration-data)
5. Select the "Format memory card" check box if you want to format the memory card.

   > **Note**
   >
   > **Delete password to protect confidential configuration data**
   >
   > If you delete a non-empty password to protect confidential configuration data, it is strongly recommended to format the memory card.
   >
   > If the memory card content requires a non-empty password to protect confidential PLC configuration data and you do not format the memory card, the operating system will not be able to transfer the memory card content to the CPU when the CPU starts up. The reason for this is that the correct password must first be set in the CPU that matches the project or program on the memory card.
6. Click "Reset".
7. Click "OK" in response to the confirmation prompt.

###### Result

The module is switched to STOP mode if necessary and the settings are then reset to factory settings. This means:

- The work memory and the internal remanent system memory are deleted.
- All operand areas are set to configured start values.
- All parameters are reset to their default values.
- The diagnostic buffer is cleared.
- The time is reset.
- The I&M data are deleted except for I&M0 data.
- The runtime meters are reset.
- The IP address is retained or deleted, depending on the setting you have made.
- The password for protecting confidential PLC configuration data is retained or deleted depending on the setting you have made. If it is deleted, the Memory Card is also deleted.
- The memory card is formatted or unformatted depending on the setting you have made.
- If a memory card was inserted prior to the reset to factory settings and you have not formatted the memory card, the configuration contained on the memory card (hardware and software) is downloaded to the CPU.

#### Resetting a PROFINET IO device to factory settings (S7-1500)

##### Requirements

- There must be an online connection to the PROFINET IO device that is to be reset.

##### Procedure

To reset a PROFINET IO device to factory settings, follow these steps:

1. Open the Online and Diagnostics view of the device (either from the project context or via "Accessible devices").
2. In the "Functions" folder, select the "Reset to factory settings" group.
3. Select the "Retain identification and maintenance data" option button or the "Delete identification and maintenance data" option button, depending on whether you want to retain or delete the identification and maintenance data IM0 to IM3 on the device.
4. Click the "Reset" button.
5. Click "OK" in response to the confirmation prompt.

   If the PROFINET IO device to be reset supports the Reset-to-Factory command according to PROFINET V2.3, its PROFINET device name, its IP address and the SNMP parameters (SNMP: Simple Network Management Protocol) are reset. Your selection in step 3 determines whether the identification and maintenance data is retained or deleted.

   The reset process is now complete.
6. If the PROFINET IO device to be reset does not support the Reset-to-Factory command according to PROFINET V2.3, however, you will see a message informing you that all data on the module will be lost during a reset to factory settings.

   Confirm the security prompt. The reset process will be conducted.

   If you have selected "Delete identification and maintenance data" in step 3, the identification and maintenance data IM0 to IM3 is deleted during the reset.

   However, if you have selected "Retain identification and maintenance data" in step 3, it can still happen that the identification and maintenance data IM0 to IM3 is deleted during the reset: The reset behavior depends on the module in this case.

##### Result

The PROFINET IO device is reset. The data deleted in the process depends on the factors described above.

#### Formatting an S7-1500 memory card (S7-1500)

##### Requirement

- If you start the formatting of the memory card from the project context, an online connection to the relevant CPU must exist.
- The relevant CPU is in STOP mode.

  > **Note**
  >
  > If the CPU is still in RUN mode and you start a formatting operation, you can place it in STOP mode after acknowledging a confirmation prompt.

##### Procedure

To format an S7-1500 memory card, follow these steps:

1. Open the Online and Diagnostics view of the CPU (either from the project context or via "Accessible devices").
2. Select the "Format memory card" group in the "Functions" folder.
3. Click the "Format" button.
4. Answer the safety prompt with "Yes".

##### Result

- The memory card is formatted.
- The CPU is temporarily unavailable.
- The project data on the CPU are deleted with the exception of the IP address.
- If you start the formatting of the memory card from the project context, the Online and Diagnostics view remains open. If formatting is started via "Accessible devices", the Online and Diagnostics view will close.

#### Updating the firmware of a module

This section contains information on the following topics:

- [Basic information on the firmware update of a module](#basic-information-on-the-firmware-update-of-a-module)
- [Calling the firmware update from the project tree](#calling-the-firmware-update-from-the-project-tree)
- [Starting the firmware update from the project context](#starting-the-firmware-update-from-the-project-context)

##### Basic information on the firmware update of a module

###### Performing a firmware update

Using firmware files, you can update the firmware of a module.

###### Requirements

- The module is connected online.
- The module supports a firmware update.
- For those modules that require supply voltage to perform the firmware update correctly: The supply voltage of the module is ensured. For details, see the documentation of the module.

###### Procedure

You can call up the firmware update of a module from the project tree or from the project context.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Impermissible system states possible**  An S7-1500 CPU immediately goes to STOP mode when you start the firmware update, which can have an effect on the operation of an online process or a machine. Unexpected operation of a process or a machine can result in severe or fatal injuries and/or damage to property. |  |

> **Note**
>
> After you have run a firmware update, you will need to replace the affected module with the same module with the current firmware version in the hardware configuration of your project. The engineering configuration then matches the actual physical configuration again.

###### "Run firmware after update" check box

If you have not selected the "Run firmware after update" check box, the previous firmware remains active until the module is reset (for example by power cycling). The new firmware only becomes active after the module has been reset.

If you have selected the check box, the module is automatically reset after the firmware has been downloaded and it then runs with the new firmware.

Activating the firmware following the update has the following consequences:

- A station executes a restart. All modules in the station become unavailable as a result.
- If the corresponding CPU is in RUN, activating the firmware can lead to access errors or other problems in the user program and might even mean that the CPU remains permanently in STOP.

  > **Note**
  >
  > For some CPUs, the "Run firmware after update" check box is grayed out and cleared. In this case, you must restart the CPU manually.
  >
  > For S7-1500 CPUs, the "Run firmware after update" check box is grayed out and selected. In this case, the new firmware is activated immediately after the download operation.

---

**See also**

[Replacing a hardware component](Configuring%20devices%20and%20networks.md#replacing-a-hardware-component)

##### Calling the firmware update from the project tree

###### Requirement

- The module is located in the first hierarchical level behind the head module (IM or CPU of the module family S7-1500 or ET200SP).
- The head module is connected to the engineering system via PROFINET.

###### Procedure

Follow these steps:

1. Select the relevant head module in the project tree.
2. Open the online and diagnostics view of the head module using the shortcut menu.
3. Select the "Firmware update" group in the "Functions" folder.
4. Select "Local modules".

   In the "Online data" area, a table lists modules of the first hierarchy level behind the head module. With Siemens modules, these are the modules that support a firmware update. With GSDML-based devices, this is all modules.
5. Select the module whose firmware you want to update.
6. Click the "Browse" button in the "Firmware loader" area in order to select the path to the firmware update files.
7. Select one of these files. The table then lists all modules for which an update is possible with the selected firmware file.
8. Optional: Select the "Run firmware after update" check box to reset the module after the load operation and to start the new firmware.
9. Click the "Start update" button. If the selected file can be interpreted by the module, it is downloaded to the module. If the operating mode of the CPU needs to be changed for this purpose, you will be prompted to do this by means of dialogs.

##### Starting the firmware update from the project context

###### Procedure

To perform a firmware update, follow these steps:

1. Open the module in the Online and Diagnostics view.
2. Select the "Firmware update" group in the "Functions" folder.
3. Click the "Browse" button in the "Firmware loader" area in order to select the path to the firmware update files.
4. Select one of these files. The table then lists all modules for which an update is possible with the selected firmware file.
5. Optional: Select the "Run firmware after update" check box to reset the module after the load operation and to start the new firmware.
6. Click the "Start update" button. If the selected file can be interpreted by the module, it is downloaded to the module. If the operating mode of the CPU needs to be changed for this purpose, you will be prompted to do this by means of dialogs.

**Note**

For S7-1500-CPUs, this group is subdivided into "PLC" and "Display".

#### Assigning an IP address to a PROFINET IO device

This section contains information on the following topics:

- [Basic information on assigning an IP address to a PROFINET IO device](#basic-information-on-assigning-an-ip-address-to-a-profinet-io-device)
- [Starting the address assignment via "Accessible devices"](#starting-the-address-assignment-via-accessible-devices)
- [Starting the address assignment from the project context](#starting-the-address-assignment-from-the-project-context)

##### Basic information on assigning an IP address to a PROFINET IO device

###### Overview

All PROFINET IO devices work with the TCP/IP protocol and therefore require an IP address for operation on Industrial Ethernet. Once an IP address has been assigned to an IO device, it can be accessed via this address. You can then download configuration data or perform diagnostics, for example.

###### Requirement

- The Ethernet LAN connection must already be established.
- The Ethernet interface of your programming device or PC must be accessible.
- The IO device that is to be assigned an IP address must be in the same IP band as the programming device or PC.

##### Starting the address assignment via "Accessible devices"

###### Requirement

- The devices accessible via the associated interface of the PG/PC are displayed in the project tree (to display these, either double-click "Update accessible devices" in the project tree or select the "Accessible devices..." command in the "Online" menu.).
- You have double-clicked "Online access" -> <Selected interface> -> <PROFINET IO device> -> "Online & Diagnostics" in the project tree to open the Online and Diagnostics view.

###### Procedure

1. Open the "Functions" folder and the "Assign IP address" group inside this folder. The "MAC address" field displays the MAC address of the PROFINET IO device. The "Accessible devices" button is grayed out.
2. Enter the desired IP address.
3. Enter the subnet mask.
4. If a router is to be used, select the "Use router" check box and enter its IP address.
5. Click the "Assign IP address" button.

###### Result

The IP address is permanently assigned to the IO device or to the relevant PROFINET interface of the IO device. It is retained even through a startup or a power failure.

> **Note**
>
> For an S7-1500 CPU, you can also use the above-described method to change the IP address of a PROFINET interface, if a project has already been downloaded to the CPU via this interface. This overwrites the IP address downloaded via the project.

---

**See also**

[Retentivity of IP address parameters and device names](Configuring%20devices%20and%20networks.md#retentivity-of-ip-address-parameters-and-device-names)
  
[Displaying accessible devices](Using%20online%20and%20diagnostics%20functions.md#displaying-accessible-devices)

##### Starting the address assignment from the project context

###### Requirement

- An online connection to the PROFINET IO device exists.
- You have opened the Online and Diagnostics view of the PROFINET IO device from the project context.
- The PROFINET IO device is not assigned to any IO controller.

###### Procedure

1. Open the "Functions" folder and the "Assign IP address" group inside this folder.
2. Click the "Accessible devices" button in order to identify the devices that can be accessed.  
   Note: For an S7-1500 CPU, there are two entries here because it has two PROFINET interfaces.
3. Select the IO device. The "IP address" field, "Subnet mask" field, "Use router" check box and "Router address" field are grayed out and contain the node properties you used to establish the current online access.
4. Click the "Assign IP address" button.

###### Result

The IP address is permanently assigned to the IO device or to the relevant PROFINET interface of the IO device. It is retained even through a startup or a power failure.

---

**See also**

[Retentivity of IP address parameters and device names](Configuring%20devices%20and%20networks.md#retentivity-of-ip-address-parameters-and-device-names)

#### Assigning a PROFINET device name

This section contains information on the following topics:

- [Basic information on assigning a name to a PROFINET IO device](#basic-information-on-assigning-a-name-to-a-profinet-io-device)
- [Assigning a name in the online and diagnostics view opened via "Accessible devices"](#assigning-a-name-in-the-online-and-diagnostics-view-opened-via-accessible-devices)
- [Assigning a name in the online and diagnostics view opened from the project context](#assigning-a-name-in-the-online-and-diagnostics-view-opened-from-the-project-context)
- [Assigning a name in the "Assign PROFINET device name" dialog](#assigning-a-name-in-the-assign-profinet-device-name-dialog)

##### Basic information on assigning a name to a PROFINET IO device

###### Device name

Before an IO device can be addressed by an IO controller, it must have a device name. This procedure was chosen for PROFINET because names are easier to handle than complex IP addresses.

Assigning a device name to a PROFINET IO device is comparable to setting the PROFIBUS address for a DP slave.

An IO device has no device name in its delivery state. For an IO controller to address an IO device, it must first be assigned a device name using the programming device or PC. It is now ready to transfer the configuration information including the IP address during startup or exchange user data in cyclic operation.

###### Rules for the device name

The device name is subject to the following limitations:

- Restricted to a total of 240 characters (lower case letters, numbers, dash, or dot)
- A name component within the device name, which is a character string between two dots, must not exceed 63 characters.
- No special characters such as umlauts, brackets, underscore, slash, blank space, etc. The only special character permitted is the dash.
- The device name must not begin or end with the "-" character.
- The device name must not begin with a number.
- The device name form n.n.n.n (n = 0, ... 999) is not permitted.
- The device name must not begin with the string "port-xyz" or "port-xyz-abcde" (a, b, c, d, e, x, y, z = 0, ... 9).

###### Where do I find the function I am seeking?

You can assign the name of a PROFINET IO device at the following places:

- In the online and diagnostics view of the device in the "Assign name" group of the "Functions" folder. The user interface for this group differs depending on how you open the online and diagnostics view:

  - Open via "Accessible devices"
  - Open from the project context
- In the "Assign PROFINET device name" dialog

---

**See also**

[Assigning a name in the online and diagnostics view opened via "Accessible devices"](#assigning-a-name-in-the-online-and-diagnostics-view-opened-via-accessible-devices)
  
[Assigning a name in the online and diagnostics view opened from the project context](#assigning-a-name-in-the-online-and-diagnostics-view-opened-from-the-project-context)
  
[Assigning a name in the "Assign PROFINET device name" dialog](#assigning-a-name-in-the-assign-profinet-device-name-dialog)

##### Assigning a name in the online and diagnostics view opened via "Accessible devices"

###### Requirement

- You have opened the online and diagnostics view of the PROFINET IO device using "Update accessible devices" (in the project tree) or "Accessible devices..." ("Online" menu).

###### Procedure

1. Open the "Functions" folder and the "Assign name" group inside this folder. The "Type" field displays the module type of the PROFINET IO device.
2. Enter the required device name in the "PROFINET device name" input box.
3. Optional: Select the "Flash LED" check box in order to run an LED flash test on the PROFINET IO device. In this way, you verify that you are naming the desired IO device.

   The LED flash test runs until you cancel it. This is done, for example, by clearing the "Flash LED" check box or by closing the online and diagnostics view.
4. Click "Assign name".

**Note**

The LED flash test is not supported by all PROFINET IO devices.

###### Result

The entered name is assigned to the PROFINET IO device.

##### Assigning a name in the online and diagnostics view opened from the project context

###### Requirement

- You have opened the online and diagnostics view of the PROFINET IO device from the project context.
- The PROFINET IO device can be accessed using at least one PG/PC interface.

###### Procedure

1. Open the "Functions" folder and the "Assign name" group inside this folder. The "PROFINET device name" drop-down list displays the current name in the offline project, and the "Type" box shows the module type of the PROFINET IO device.
2. Choose a different name from the drop-down list, if necessary.
3. In the "PG/PC interface for assignment" drop-down list, select the PG/PC interface you want to use to establish the online connection.
4. Optional: Use the three check boxes to make a selection from all IO devices available online.
5. Click the icon for determining the IO devices present in the PROFINET subnet. The table is then updated.
6. Select the desired IO device in the table.
7. Optional: Select the "Flash LED" check box in order to run an LED flash test on the PROFINET IO device. In this way, you verify that you are naming the desired IO device.

   The LED flash test runs until you cancel it. This is done, for example, by clearing the "Flash LED" check box, by selecting another IO device in the table, or by closing the online and diagnostics view.
8. Click "Assign name".

**Note**

For CPUs with several PROFINET interfaces, the names of all existing PROFINET interfaces are displayed in the offline project.

**Note**

In steps 3 to 5, you determine the IO devices that are present in the PROFINET subnet.

**Note**

The LED flash test is not supported by all PROFINET IO devices.

###### Result

The selected name is assigned to the PROFINET IO device or one of its PROFINET interfaces.

##### Assigning a name in the "Assign PROFINET device name" dialog

###### Requirement

- You have opened the "Assign PROFINET device name" dialog from the network view (from the shortcut menu of a PN/IE connection).
- The PROFINET IO device can be accessed using at least one PG/PC interface.

###### Procedure

1. The following is displayed in the "PROFINET device name" drop-down list:

   - the name of the interface that was used to open the project in the current offline project
   - the names of those IO devices that are connected by means of this interface

   The "Type" field displays the module type of the PROFINET IO device.

   Choose a different name from the drop-down list, if necessary.
2. In the "PG/PC interface for assignment" drop-down list, select the PG/PC interface you want to use to establish the online connection.
3. Optional: Use the three check boxes to make a selection from all IO devices available online.
4. Click the icon for determining the IO devices present in the PROFINET subnet. The table is then updated.
5. Select the desired IO device in the table.
6. Optional: Select the "Flash LED" check box in order to run an LED flash test on the PROFINET IO device. In this way, you verify that you are naming the desired IO device.

   The LED flash test runs until you cancel it. This is done, for example, by clearing the "Flash LED" check box or by selecting another IO device in the table.
7. Click "Assign name".

**Note**

In steps 2 to 4, you determine the IO devices that are present in the PROFINET subnet.

**Note**

The LED flash test is not supported by all PROFINET IO devices.

###### Result

The selected name is assigned to the PROFINET IO device or the interface that was used to open the dialog.

#### Calibrating an S7-1500 analog module (S7-1500)

This section contains information on the following topics:

- [Calibrating an S7-1500 analog module - Overview (S7-1500)](#calibrating-an-s7-1500-analog-module---overview-s7-1500)
- [Calibrating an S7-1500 analog module (S7-1500)](#calibrating-an-s7-1500-analog-module-s7-1500-1)
- [Canceling a running calibration of an S7-1500 analog module (S7-1500)](#canceling-a-running-calibration-of-an-s7-1500-analog-module-s7-1500)
- [Resetting an S7-1500 analog module to factory settings (S7-1500)](#resetting-an-s7-1500-analog-module-to-factory-settings-s7-1500)

##### Calibrating an S7-1500 analog module - Overview (S7-1500)

###### Where do you calibrate an S7-1500 analog module?

You calibrate an S7-1500 analog module in its Online and Diagnostics view in the "Calibrate" group of the "Functions" folder.

###### Overview of the function scope of the calibrating function

You can perform the following functions for an S7-1500 analog module in the "Calibrate" group:

- Specifying the current calibration of all channels
- Calibrating a channel
- Canceling a running calibration
- Resetting the calibration of a channel to the factory settings

###### Requirement for the calibrating function described below

The following is required for the calibrating function described below:

- You have opened the Online and Diagnostics view from the project context (thus not from the project tree or via the "Online" menu).
- There is an online connection to the analog module that is to be calibrated.
- Offline and online configuration are identical.

##### Calibrating an S7-1500 analog module (S7-1500)

###### Overview of the calibration of a channel of an S7-1500 analog module

The calibration of a channel of an S7-1500 analog module consists of the following steps:

1. Start calibration
2. Perform the second step up to the next to last step of the calibration
3. Complete calibration

These steps are described in more detail in the following section.

###### Requirement

- You have opened the Online and Diagnostic view of the S7-1500 analog module from the project context and are in the "Calibrate" group of the "Functions" folder.
- The associated CPU is online.
- No calibration is currently running on the analog module (if you want to start the calibration) or the last step initiated has been performed successfully (if you want to resume or complete the calibration).

###### Procedure for starting the calibration

To start the calibration, follow these steps:

1. In the overview table, select the line that belongs to the channel to be calibrated.
2. Click the "Start manual calibration" button.

The user interface then changes as follows:

- The overview table and the "Start manual calibration" button and "Set to factory settings" buttons become inactive.
- The step display is activated and displays the numbers of the current and last steps.
- The "Command" field becomes active and indicates what the user must do in the next calibration step.
- The "Status" field becomes active and shows the current status of the calibration, e.g., "Calibration successfully started".
- The "Measured value" field becomes active. For an input module a value is displayed here; you must enter a value here for an output module.
- The "Cancel" button becomes active.
- With certain analog modules (AI Energy Meter) the "Skip" button becomes active. This button can be used to skip to the next step of the calibration.
- The "Next" button becomes active. This button can be used to advance to the next step of the calibration.

###### Procedure for the second to the next to last step of the calibration

Follow these steps:

1. Click the "Next" button.

The fields of the user interface described above are then updated.

With certain analog modules (AI Energy Meter), you can skip the next calibration step as long as the next step is not the last step of the calibration procedure. To do this, follow these steps:

1. Click the "Skip" button.

The fields of the user interface described above are then updated.

###### Procedure for the last step of the calibration

Follow these steps:

1. Click the "Next" button.

The user interface then changes as follows:

- The overview table becomes active.
- The calibration display of the calibrated channel is updated.
- The "Start manual calibration" button and "Set to factory settings" buttons become active.
- The step display is deactivated and the numbers of the current step and last steps are empty.
- The "Command" field becomes inactive and is empty.
- The "Status" field becomes inactive and shows the last status of the calibration, e.g., "Calibration successfully finished".
- The "Measured value" field becomes inactive and is empty.
- The "Cancel" button becomes inactive.
- The "Skip" button becomes inactive.
- The "Next" button becomes inactive.

###### Error occurrence

If an error occurs during the calibration, the module cancels the calibration. Afterwards, the channel that was to be calibrated has the same settings as before the start of the calibration.

Except for the "Status" field, the user interface appears the same after the occurrence of an error as before the calibration. The "Status" field displays the error that the module detected during the calibration.

##### Canceling a running calibration of an S7-1500 analog module (S7-1500)

###### Requirement

- You have opened the Online and Diagnostic view of the S7-1500 analog module from the project context and are in the "Calibrate" group of the "Functions" folder.
- The associated CPU is online.
- A calibration is currently running on the analog module.

###### Procedure

To cancel a running calibration, follow these steps:

1. Click the "Cancel" button.

###### Result

The running calibration is canceled, and afterwards the channel to be calibrated has the same settings as before the calibration.

All operator controls in the user interface are deactivated until the cancelation is complete. Except for the "Status" field, the user interface appears the same afterwards as before the calibration. The "Status" field displays the result of the cancelation.

##### Resetting an S7-1500 analog module to factory settings (S7-1500)

###### Requirement

- You have opened the Online and Diagnostic view of the S7-1500 analog module from the project context and are in the "Calibrate" group of the "Functions" folder.
- The associated CPU is online.

###### Procedure

To reset a channel of an S7-1500 analog module to factory settings, follow these steps:

1. Select the line associated with the channel to be reset in the overview table.
2. Click the "Set to factory settings" button.

###### Result

All operator controls in the user interface are deactivated until the reset operation is complete. Except for the "Status" field, the user interface appears the same afterwards as before the reset operation. The "Status" field displays the result of the reset operation.

#### Loading I&M data to PROFINET IO devices and your modules

##### Which I&M data can be loaded to PROFINET IO devices and your modules?

You can load I&M 1 data (plant designation and location identifier) and/or I&M 2 data (installation date) and/or I&M 3 data (additional information) to the actual hardware.

##### Requirements

- In the project settings (Options > Settings, Hardware configuration > Compiling and downloading), the option "Download I&M data" must be enabled.
- There is an online connection to the PROFINET IO devices and the modules to which you want to load I&M data.
- You have entered the I&M data you want to download in the properties of the respective PROFINET IO devices and your modules (Inspector window: "Properties" tab > "General" tab, Settings > Identification & Maintenance).

##### Where do I specify which I&M data is downloaded to which PROFINET IO devices?

You specify which I&M data you want to download to which PROFINET IO devices in the "Load preview" dialog. You will find the following alternatives in the drop-down list of the "Identification and maintenance data (I&M)" row:

- Load nothing

  The check boxes for all PROFINET IO devices as well as the check boxes for the loadable I&M data are cleared.

  No I&M data is transferred to the actual hardware during loading with this setting.
- Load data

  The check boxes for all PROFINET IO devices as well as the check boxes for the loadable I&M data are selected.

  The respective I&M 1, I&M 2 and I&M 3 data is transferred to all PROFINET IO devices during loading with this setting.
- Load selected

  You select the check boxes of those PROFINET IO devices to which you want to load I&M data. You also select the check boxes of the identification data you want to load.

  With this setting, you transfer the selected I&M data to the selected PROFINET IO devices during loading.

> **Note**
>
> **Language dependency of the I&M data to be loaded**
>
> The I&M data are loaded to the real hardware in the form that you specified in the properties of the relevant PROFINET IO devices and your modules. There is no language dependency.

### Diagnostics in STOP mode

This section contains information on the following topics:

- [Basic information on the diagnostics buffer](#basic-information-on-the-diagnostics-buffer)
- [Determining the cause of a STOP of a CPU](#determining-the-cause-of-a-stop-of-a-cpu)

#### Basic information on the diagnostics buffer

##### Function

The operating system of the CPU enters the errors detected by the CPU and the diagnostics-capable modules into the diagnostics buffer in the order in which they occurred. This includes the following events:

- Every mode change of the CPU (POWER UP, change to STOP mode, change to RUN mode)
- Every hardware and diagnostic error interrupt

The top entry contains the most recent event. The entries in the diagnostics buffer are stored permanently. They are retained even if the power supply fails and can only be deleted by resetting the CPU to factory settings.

A diagnostics buffer entry contains the following elements:

- Time stamp
- Error ID
- Additional information specific to the error ID

##### Advantages of the diagnostics buffer

The diagnostics buffer offers the following advantages:

- After the CPU has changed to STOP mode, you can evaluate the last events prior to the STOP so that you can locate and identify the cause of the STOP.
- You can detect and eliminate the causes of errors more quickly and thus increase the availability of the system.
- You can evaluate and optimize the dynamic system response.

##### Organization of the diagnostics buffer

The diagnostics buffer is a ring buffer. With the S7-1200 CPUs, the maximum number of entries is 50. When the diagnostics buffer is full and a further entry needs to be made, all existing entries are shifted one position (which means that the oldest entry is deleted) and the new entry is made at the first position that is now free (FIFO principle: first in, first out).

##### Evaluation of the diagnostics buffer

The contents of the diagnostics buffer can be accessed as follows:

- Using the Online and Diagnostics view

The evaluation of events occurring prior to the error event (e.g., transition to STOP mode) allows you to obtain a picture of the possible causes or to zero in more closely or specify in more detail the possible causes (depending on the error type).

Read the detailed information about the events carefully and use the "Help on event" text box to obtain additional information and possible causes of individual entries.

> **Note**
>
> To make the best use of the time stamp information on the diagnostics buffer entries in time-critical systems, it is advisable to check and correct the date and time of day on the CPU occasionally.
>
> Alternatively, it is possible to perform a time-of-day synchronization using an NTP time server.

---

**See also**

[Resetting an S7-1200 CPU to factory settings (S7-1200)](#resetting-an-s7-1200-cpu-to-factory-settings-s7-1200)
  
[Determining the cause of a STOP of a CPU](#determining-the-cause-of-a-stop-of-a-cpu)
  
[Determining and setting the time of day on a CPU](#determining-and-setting-the-time-of-day-on-a-cpu)
  
[Assigning the clock parameters (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#assigning-the-clock-parameters-s7-1200)

#### Determining the cause of a STOP of a CPU

##### Requirement

The CPU you want to analyze is in STOP mode.

##### Procedure

To find out the reason why a CPU changed to STOP, follow these steps:

1. Open the online and diagnostics view of the CPU.
2. Select the "Diagnostics buffer" group from the "Diagnostics" folder.
3. Evaluate the events occurring prior to the transition to STOP mode. Use this to obtain a picture of the possible causes or to zero in on or specify in more detail the possible causes (depending on the error type).

   Read the detailed information about the events carefully and use the "Help on event" button to obtain additional information and possible causes of individual entries.

##### Result

You were able to zero in on or determine in more detail the cause of the CPU STOP.

> **Note**
>
> If the analysis does not enable you to overcome the problem, contact Customer Support. In this case, use the "Save as" button to back up the content of the diagnostics data to a text file and submit it to Customer Support.

---

**See also**

[Reading out the diagnostics buffer of a CPU](#reading-out-the-diagnostics-buffer-of-a-cpu)

### Online accesses in the Online and Diagnostics view

This section contains information on the following topics:

- [Displaying status of the online connection](#displaying-status-of-the-online-connection)
- [Specifying a PG/PC interface, going online](#specifying-a-pgpc-interface-going-online)
- [Going offline](#going-offline)
- [Performing the flash test for a device with an online connection](#performing-the-flash-test-for-a-device-with-an-online-connection)

#### Displaying status of the online connection

##### Requirement

- The associated device can be accessed using at least one PG/PC interface.

##### Procedure

1. Open the online and diagnostics view for the device whose online connection status you want to display.
2. Select the "Online access" group.

**Note**

The "Online access" group exists only for CPUs and some CPs. However, if you have opened the online and diagnostics view using the "Show/update accessible devices" function, it is not displayed.

##### Result

The status of the online connection is displayed in the "Status" area both graphically and in text form.

#### Specifying a PG/PC interface, going online

##### Requirement

- The associated device can be accessed using at least one PG/PC interface.
- There is currently no online connection to the relevant device.

##### Procedure

1. Open the Online and Diagnostics view of the device to which you want to establish an online connection.
2. Choose the "Online access" group and the "Online access" area within this group.
3. If an online connection was established previously for the device, the associated data for this online connection is preset in the drop-down lists. In this case, you can immediately continue with the last step of this operating instruction, provided you have not changed the IP address in the meantime using the Online and Diagnostics view.
4. Choose the interface type in the "Type of PG/PC interface" drop-down list.

   The "PG/PC interface for online access" drop-down list then shows only the interfaces of the programming device or PC that match the selected interface type.
5. In the "PG/PC interface for online access" drop-down list, select the programming device or PC interface via which you want to establish the online connection.
6. Optional: Click the "Properties" button to change the properties of the associated CP.
7. In the "Connection to subnet" drop-down list, select the subnet via which the device is connected to the PG/PC interface.
8. If the device is accessible via a gateway, select the gateway that connects the two subnets involved in the "1st gateway" drop-down list.
9. In the "Device address" entry field, enter the IP address of the device to which you want to establish an online connection, if necessary.
10. Alternatively: Click the "Show accessible devices" button and choose the device from the list of accessible devices to which you want to establish an online connection.
11. Click the "Go online" button.

**Note**

The "Online access" group exists only for CPUs and some CPs. If you have opened the Online and Diagnostics view using the "Show/update accessible devices" function, it is not displayed.

**Note**

The PG/PC interface is connected to an interface of a device.

If you only want to access this device, select the setting "Directly at slot <interface name>" in the drop-down list.

If, however, you want to access another device by means of routing, create a subnet at this interface in the device configuration and then select this subnet in the drop-down list.

**Note**

For CPUs with multiple IP addresses, select the IP address of the PROFINET interface you want to use to establish an online connection from the "Device address" drop-down list.

##### Result

The online connection to the desired device is established.

---

**See also**

[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
  
[Default setting online connection data](Using%20online%20and%20diagnostics%20functions.md#default-setting-online-connection-data)

#### Going offline

##### Requirement

- There is currently an online connection to the relevant device.

##### Procedure

1. Open the online and diagnostics view of the device for which you want to disconnect the online connection.
2. Choose the "Online access" group and the "Online access" area within this group.
3. Click the "Go offline" button.

**Note**

The "Online access" group exists only for CPUs and some CPs. However, if you have opened the online and diagnostics view using the "Show/update accessible devices" function, it is not displayed.

##### Result

The online connection to the desired device will be disconnected.

---

**See also**

[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)

#### Performing the flash test for a device with an online connection

##### Requirement

- There is currently an online connection to the relevant device.
- The FORCE function is not active.

##### Procedure

1. Open the online and diagnostics view of the device for which you want to perform a flash test.
2. Choose the "Online access" group and the "Status" area within this group.
3. Select the "LED flash test" check box.

**Note**

The "Online access" group exists only for CPUs and some CPs. However, if you have opened the online and diagnostics view using the "Show/update accessible devices" function, it is not displayed.

##### Result

- On an S7-1200 CPU, the RUN/STOP, ERROR and MAINT LEDs flash.
- On an S7-1500 CPU, the RUN/STOP, ERROR, and MAINT LEDs flash.
- On an S7-300 or S7-400 CPU, the FRCE LED flashes.

The LEDs flash until you cancel the flash test. This is done, for example, by clearing the "LED flash test" check box, by changing to another group of the online and diagnostics view, or by changing settings in the "Online access" area.

### Checking PROFIBUS DP subnets for faults

This section contains information on the following topics:

- [Basic information on the diagnostic repeater](#basic-information-on-the-diagnostic-repeater)
- [Displaying the status of the segment diagnostics using icons](#displaying-the-status-of-the-segment-diagnostics-using-icons)
- [Displaying the status of the segment diagnostics using graphics and text](#displaying-the-status-of-the-segment-diagnostics-using-graphics-and-text)

#### Basic information on the diagnostic repeater

##### What is the diagnostic repeater?

The diagnostic repeater is a repeater that can monitor a segment of an RS 485 PROFIBUS subnet (copper cable) during operation and signal line errors to the DP master via a diagnostics message frame.

The diagnostic repeater detects, localizes and visualizes line errors during operation at an early stage. As a result, problems in the system are identified early and production downtimes will be minimized.

##### Function of the diagnostic repeater

The diagnostic repeater can perform line diagnostics on the DP2 and DP3 segments because it has a measuring circuit for these segments.

The line diagnostics run in two steps:

- Step 1: Topology determination

  You start the topology determination by calling the "DP_TOPOL" instruction in your program.

  The diagnostic repeater then determines the PROFIBUS addresses and the distance of the devices and creates a topology table.
- Step 2: Error localization

  The diagnostic repeater checks the lines during operation. It determines the distance to the point of the error and the reason for the error; it then issues a diagnostics alarm with relative information on the error location.

##### Display of detailed information on the determined error location

You receive detailed information on the determined error location in the Online and Diagnostics view of the diagnostic repeater.

- By means of icons
- By means of a display with graphics and text

---

**See also**

[Displaying the status of the segment diagnostics using icons](#displaying-the-status-of-the-segment-diagnostics-using-icons)
  
[Displaying the status of the segment diagnostics using graphics and text](#displaying-the-status-of-the-segment-diagnostics-using-graphics-and-text)

#### Displaying the status of the segment diagnostics using icons

##### Where do I find the information I need?

The icons for the status of the segment diagnostics are available:

- In the expanded "Segment diagnostics" folder in the navigation pane of the Online and Diagnostics view of the relevant diagnostic repeater.

The diagnostics icon associated with the segment will be displayed behind the segment designation. It must be noted here that line errors will be displayed for the DP2 and DP3 segments only. The DP1 and programming device segments do not display errors in the form of a diagnostics icon; rather, they signal only a few bus errors.

##### Diagnostics icons

The following table shows the available icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Diagnostics icons](images/22259622539_DV_resource.Stream@PNG-de-DE.png) | Segment is error-free |
| ![Diagnostics icons](images/22259776651_DV_resource.Stream@PNG-de-DE.png) | Segment contains errors |
| ![Diagnostics icons](images/21909201803_DV_resource.Stream@PNG-de-DE.PNG) | Segment is deactivated |

#### Displaying the status of the segment diagnostics using graphics and text

##### Where is the status of the segment diagnostics displayed with graphics and text?

The status of the segment diagnostics will be displayed using graphics and text in the "DP1", "DP2", "DP3", and "PG" groups of the "Segment diagnostics" folder in the Online and Diagnostics view of the relevant diagnostic repeater.

##### Structure of the "DP1", "DP2" "DP3", and "PG" groups

The "DP1", "DP2", "DP3", and "PG" groups consist of the following elements:

- "Error location" field
- "Error" field
- "Resolution" field
- "Help on event" button
- "Freeze display" or "Cancel freeze" button

##### "Error location" field

This field displays the error location graphically, provided the diagnostic repeater can determine the location.

The following picture shows an example for a line error occurring in the DP2 segment.

!["Error location" field](images/20884965643_DV_resource.Stream@PNG-de-DE.png)

In this example, the diagnostic repeater has the PROFIBUS address 2, and a line error has occurred between the devices with PROFIBUS addresses 16 and 17. This line error is located 25 m from device 16, 4 m from device 17, and 72 m from the diagnostic repeater.

##### "Error" field

The error is explained in plain text in this field.

##### "Resolution" field

Here, you will find actions for resolving the error.

##### "Help on event" button

Click this button to obtain a more detailed explanation of the error and additional details on resolving the error, if applicable.

##### "Freeze display" or "Cancel freeze" button

The "Freeze display" or "Cancel freeze" button is only enabled when there is an online connection to the diagnostic repeater.

The default setting is "Freeze display".

The following happens when you click the "Freeze display" button:

- The current display of the segment diagnostics is frozen.
- The labeling of the button changes to "Cancel freeze".

If the display is frozen and you click the "Cancel freeze" button, the following happens:

- The display of the segment diagnostics is updated again.
- The labeling of the button changes to "Freeze display".

## Connection diagnostics

This section contains information on the following topics:

- [Overview of connection diagnostics](#overview-of-connection-diagnostics)
- [Displaying the connection status using icons](#displaying-the-connection-status-using-icons)
- [Detailed connection diagnostics](#detailed-connection-diagnostics)
- [Displaying the connection properties of the interface modules of an IO device in the S7-1500H system (S7-1500)](#displaying-the-connection-properties-of-the-interface-modules-of-an-io-device-in-the-s7-1500h-system-s7-1500)

### Overview of connection diagnostics

#### Basics

Connection diagnostics, as described below, refers to the diagnostics of communication connections.

The connection diagnostics is started each time an online connection is established to a module (CPU or CP) that participates in one or more communication services. The connection status is updated automatically in the background.

In the case of one-way connections, an online connection must exist to the communication partner that has established the communication connection.

On connections configured at both ends, a distinction between the following two situations must be made:

- If there is an online connection to only one connection endpoint, only the part of the connection belonging to this connection endpoint can be diagnosed.
- If there is an online connection to both connection endpoints, both parts of the connection (and therefore the entire connection) can be diagnosed.

#### Basic connections diagnostics options

Connection diagnostics can be performed as follows:

- Using icons on the connection status display

  This display is generated in the connection table.
- Through detailed connection diagnostics

  This step is available in the "Diagnostics > Connection information" area of the Inspector window.

#### Requirement for the connection diagnostics described below

The connection diagnostics is only possible if the devices participating in the connection make the corresponding diagnostics data available.

You can display the details of either all the communication connections created in the project (default) or selected communication connections in the connection table.

The connection diagnostics described in the following assume that you display the details of selected communication connections. To do this, clear the "Show all connections" option in the shortcut menu.

---

**See also**

[Working with the connection table](Configuring%20connections.md#working-with-the-connection-table)

### Displaying the connection status using icons

#### Content of connection table without an online connection

- For a CPU or CP, the connection table lists the communication connections (including properties) configured offline, if an online connection is not established.

#### Content of connection table with an online connection

After the online connection has been established, the properties of the communication connections listed offline will be expanded to include diagnostics icons for the connection status ("Online status" column).

In addition, entries for all communication connections that exist online only (e.g., connections for the instructions for Open User Communication, programming device and OP connections, connections for web server access) will now be added to the connection table.

For connections that exist online or offline only, the diagnostics icon at the bottom right is combined with a smaller additional comparison status icon.

#### Diagnostics icons for communication connections

The following table shows the diagnostics icons for communication connections.

| Icon | Meaning |
| --- | --- |
| ![Diagnostics icons for communication connections](images/41866212875_DV_resource.Stream@PNG-de-DE.png) | Connection setup |
| ![Diagnostics icons for communication connections](images/41866083339_DV_resource.Stream@PNG-de-DE.png) | Connection not setup / is being setup |
| ![Diagnostics icons for communication connections](images/41866341131_DV_resource.Stream@PNG-de-DE.png) | Connection not available |

#### Diagnostics icons for the comparison status

The diagnostic icons for communication connections can be combined at the bottom right with additional smaller icons that indicate the result of the online/offline comparison. The following table shows the available comparison icons and their meaning.

| Icon | Meaning |
| --- | --- |
| ![Diagnostics icons for the comparison status](images/20532787723_DV_resource.Stream@PNG-de-DE.png) | Connection exists online only |
| ![Diagnostics icons for the comparison status](images/20532780299_DV_resource.Stream@PNG-de-DE.png) | Connection exists offline only |

### Detailed connection diagnostics

This section contains information on the following topics:

- [Detailed connection diagnostics - overview](#detailed-connection-diagnostics---overview)
- [Determining online connection resources for S7-1200 (S7-1200)](#determining-online-connection-resources-for-s7-1200-s7-1200)
- [Determining online connection resources for S7-1500 (S7-1500)](#determining-online-connection-resources-for-s7-1500-s7-1500)
- [Determining connection details](#determining-connection-details)
- [Determining the address details of a connection (S7-1200, S7-1500)](#determining-the-address-details-of-a-connection-s7-1200-s7-1500)

#### Detailed connection diagnostics - overview

##### Where do I perform detailed connection diagnostics?

To perform detailed connection diagnostics, go to the "Diagnostics > Connection" information of the Inspector window.

##### How do I open the "Diagnostics > Connection information" area of the Inspector window?

The following options are available for opening the "Connection information" tab of the Inspector window.

- Select the line of the relevant connection in the connection table. Click the "Diagnostics" and "Connection information" tabs one after the other in the Inspector window.
- Double-click the diagnostics icon of the relevant connection in the connection table.
- This step takes you to the programming editor for a S7 communication instruction or open user communication instruction. Double-click the diagnostic icon of the instruction (stethoscope).

##### Structure or the "Diagnostics > Connection information" area of the Inspector window

Requirements: the content of the "Connection information" tab has been filled, and an online connection to at least one end point of the relevant connection has been established.

If a module has been selected (network view), the tab will contain the following group:

- Connection resources (for S7-1200 and S7-1500)

If a connection has been selected (connection table), it will contain the following groups:

- Connection details
- Address details of the connection (for S7-1200 and S7-1500)

#### Determining online connection resources for S7-1200 (S7-1200)

##### Where do you determine the online connection resources?

The online connection resources are obtained in the "Connection resources" group. This group is located in the "Diagnostics > Connection information" area of the Inspector window. It is displayed only if you have selected a module in the network view to which an online connection exists.

##### Number of connection resources

- Maximum number: Specifies the maximum number of available connection resources of the module.
- Not assigned: Indicates how many connection resources are not yet assigned. If connection resources are already reserved for certain types of communication, then the unreserved connection resources cannot always be used for the various connection types.

##### Reserved and currently assigned connection resources

For the communication types indicated below, the connection resources that are reserved and currently assigned by the module will be displayed.

| Communication type | Meaning |
| --- | --- |
| PG communication | Resources for connections between the module and programming devices (for example, for the establishment of a connection from the project tree, for online diagnostics, etc.) |
| HMI communication | Resources for connections between the module and HMI devices |
| Open User Communication | Resources for connection of open user communication instructions |
| S7 communication | Resources for configured S7 connections, through which data can be exchanged by calling instructions in the user program. |
| Other communication | Specifies other assigned connection resources for which connection resources are not reserved. |

#### Determining online connection resources for S7-1500 (S7-1500)

##### Where do you determine the online connection resources?

The online connection resources are obtained in the "Connection resources" group. This group is located in the "Diagnostics > Connection information" area of the Inspector window. It is displayed only if you have selected a module in the network view to which an online connection exists.

##### Description of the detailed display of the connection resources

The detailed display of the connection resources includes:

- Number of available connection resources
- Number of configured connection resources
- Number of connection resources still available

For a description of these, go to [here](Configuring%20devices%20and%20networks.md#display-of-the-connection-resources-s7-1500) .

#### Determining connection details

##### Where do I determine the connection details?

The connection details are obtained in the "Connection details" group. This group is located in the "Diagnostics > Connection information" area of the Inspector window.

##### When is the "Connection details" group filled in?

The following requirements must be met to fill in the "Connection details" group on the "Connection information" tab:

- An online connection to the end point of the relevant connection must exist.
- You have selected a line in the connection table.

##### Structure of the "Connection details" group

The "Connection details" group consists of the following elements:

- Local ID (hex)
- Connection type (for S7-1200 and S7-1500)
- Protocol
- Connection status: icon and description
- Details
- Last status change (for S7-300 and S7-400 only)

#### Determining the address details of a connection (S7-1200, S7-1500)

##### Where do I determine the address details of a connection?

The address details of a connection are obtained in the "Connection address details" group. This group is located in the "Diagnostics > Connection information" area of the Inspector window.

##### For which CPUs is the "Connection address details" group available?

The "Connection address details" group of the "Connection information" tab is available for S7-1200 and S7-1500 CPUs.

##### When is the "Connection address details" group filled in?

The following requirements must be met to fill in the "Connection address details" group on the "Connection information" tab:

- An online connection to the end points of the relevant connection must exist.
- You have selected a line in the connection table.

##### Structure of the "Connection address details" group

The address details relevant to the connection type are specified for the two communication partners.

### Displaying the connection properties of the interface modules of an IO device in the S7-1500H system (S7-1500)

#### Where can I find the information I need?

You can learn about the connection properties of the interface modules of an IO device in the S7-1500H system in the online and diagnostics view of the interface modules in the "Diagnostics" folder in the "Redundancy" group.

#### Requirements

- Firmware version of the S7-1500 H CPUs >= V3.0
- There is a switched S1 device or an S2 device or an R1 device (for definitions of terms, see: [Creating IO devices for R/H systems](Principle%20of%20operation%20for%20S7-1500R-H%20CPUs%20%28S7-1500%29.md#creating-io-devices-for-rh-systems-s7-1500))

#### "Redundant PLC connections" table

The names of the interface modules of the IO device are shown in the "Interface module" column.

- With a switched S1 device, both rows contain the name of the same interface module.

  This module has only one communication relationship to one of the two CPUs of the H system.
- For an S2 device, both rows contain the name of the same interface module.

  This module has one communication relationship to each of the two CPUs of the H system.
- For an R1 device, the first row contains the name of the interface module with the communication relationship to one CPU of the H system, the second row contains the name of the interface module with the communication relationship to the other CPU of the H system.

The "CPU" column contains the names of the assigned CPUs of the H system.

The "Connection status" column shows the current state of the connection between interface module and assigned CPU of the H system. If there is a connection, there is also an indication as to whether the connection is currently in use.

The following entries are possible in the "Connection status" column:

- Not connected
- Connected – stand by
- Connected – in use

The associated diagnostic symbols are displayed directly in front of the names of the interface modules.

## Diagnosing the OPC UA server

This section contains information on the following topics:

- [Requirements](#requirements)
- [Displaying general status information of the OPC UA server](#displaying-general-status-information-of-the-opc-ua-server)
- [Display status information for the OPC UA sessions](#display-status-information-for-the-opc-ua-sessions)

### Requirements

#### Requirements

The following conditions must be met for the status information described below to be displayed:

- The OPC UA server is located on a S7-1500 CPU with firmware version V2.8 or higher.
- You have activated and configured the OPC UA server on this CPU and there is an online connection to this CPU.

### Displaying general status information of the OPC UA server

#### Where is the general status information of the OPC UA server displayed?

The general status information of the OPC UA server is displayed in the Online and Diagnostics view of the corresponding CPU in the "OPC UA" folder in the "Server" group under "General".

#### Structure of the "Status" area

The "Status" area consists of the following items:

- Check box "Display CPU Time Stamps in PG/PC local time"
- Fields with the general status information of the OPC UA server

#### Check box "Display CPU Time Stamps in PG/PC local time"

The check box "Display CPU Time Stamps in PG/PC local time" affects the display of the following times:

- Current time (OPC UA > Server > General, "Status" area)
- Server start time (OPC UA > Server > General, "Status" area)
- Last contact of the client (OPC UA > Server > Sessions, "Session/subscription diagnostics" area, last table column)

The check box "Display CPU Time Stamps in PG/PC local time" has the following meaning:

- If you have not activated the check box, the named times are shown with the module time.
- If you have activated the check box, the above-mentioned times are shown with the time given by the following formula:

  Displayed time = module time + time zone offset on your programming device/PC

  This requires the module time to be identical to UTC.

#### General status information of the OPC UA server

The following general status information of the OPC UA server is displayed:

- Current time
- Starting the server
- Server status Overall status of the OPC UA server. Possible values: Running, unknown
- Seconds to shutdown: This field does not contain any relevant information. It is intended for a future delivery stage.
- Reason for shutdown: This field does not contain any relevant information. It is intended for a future delivery stage.

---

**See also**

[Using diagnostics options (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#using-diagnostics-options-s7-1200-s7-1500-s7-1500t)

### Display status information for the OPC UA sessions

#### Where is the status information of the OPC UA sessions displayed?

The status information for the OPC UA sessions is displayed in the Online and Diagnostics view of the corresponding CPU in the "OPC UA" folder in the "Server" group under "Sessions".

#### Structure of "Sessions"

"Sessions" consists of the following two sections:

- Statistics
- Session/subscription diagnostics

#### "Statistics" area

The "Statistics" area displays the following information about the total number of OPC UA sessions:

- Number of sessions: Number of currently active sessions
- Number of monitored items: Number of all monitored items (Monitored Items)
- Total number of requests: Sum of the requests of all currently active sessions
- Number of incorrect requests: Sum of the incorrect requests of all currently active sessions.
- Number of rejections: RejectedRequestCount + RejectedSessionCount + SecurityRejectedRequestCount + SecurityRejectedSessionCount
- Number of session timeouts: Number of session timeouts

#### "Session/subscription diagnostics"

The "Session/subscription diagnostics" area consists of the following items:

- Session/subscription table
- "Freeze display" or "Cancel freeze" button
- Details about the selected session/subscription

#### Session/subscription table

The following information is displayed in the table for each active session or subscription:

| Column | Significance for session | Meaning for subscription |
| --- | --- | --- |
| ID | Numeric session identifier: | Numeric subscription identifier |
| Name | Full name of the session | Formatted subscription_ID, where ID is the subscription Identifier |
| Endpoint URL | End point of the OPC UA server for the session | - |
| Subscriptions | Number of subscriptions for the current session | Always 1 |
| Monitored items | Number of items monitored in the current session (Monitored Items) | Number of items monitored in the current subscription (Monitored Items). |
| Timeout | Current CurrentTime minus the last contact time ClientLastContactTime in relation to the set ActualSessionTimeout | Current CurrentLifetimeCount in relation to the maximum MaxLifetimeCount of the current subscription |
| Last contact of the client | Time of the last client contact in the current session | - |

#### "Freeze display" or "Cancel freeze" button

The "Freeze display" or "Cancel freeze" button is only enabled when there is an online connection to the CPU.

The default setting is "Freeze display".

The following happens when you click the "Freeze display" button:

- The current display of the session/subscription entries is frozen.
- The labeling of the button changes to "Cancel freeze".

If the display is frozen and you click the "Cancel freeze" button, the following happens:

- The display of the session/subscription entries is updated again.
- The labeling of the button changes to "Freeze display".

#### Details about the selected session/subscription

If you select a row belonging to a session in the session/subscription table, the following detailed information about this session is displayed here:

- CurrentPublishRequestsInQueue
- ReadCount (TotalCount)
- ReadCount (ErrorCount)
- WriteCount (TotalCount)
- WriteCount (ErrorCount)
- PublishCount (TotalCount)
- PublishCount (ErrorCount)
- CreateSubscriptionCount (TotalCount)
- CreateSubscriptionCount (ErrorCount)
- CreateMonitoredItemsCount (TotalCount)
- CreateMonitoredItemsCount (ErrorCount)
- TotalRequestCount (TotalCount)
- TotalRequestCount (ErrorCount)

If you select a row that belongs to a subscription in the session/subscription table, the following detailed information about this subscription is displayed here:

- TransferredToSameClientCount
- PublishRequestCount
- DataChangedNotificationsCount
- EventNotificationsCount
- NotificationsCount
- LatePublishRequestCount
- CurrentKeepAliveCount
- TransferredToAltClientCount

> **Note**
>
> **Meaning of detailed information**
>
> The meaning of the detailed information on both the session and the subscription can be found in the OPC UA specification, Part 5, Information Model.

---

**See also**

[Using diagnostics options (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#using-diagnostics-options-s7-1200-s7-1500-s7-1500t)

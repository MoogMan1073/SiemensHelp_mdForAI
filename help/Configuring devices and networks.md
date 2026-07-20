---
title: "Configuring devices and networks"
package: HWC2MenUS
topics: 387
devices: [PC, S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring devices and networks

This section contains information on the following topics:

- [Hardware and network editor](#hardware-and-network-editor)
- [Configuring devices](#configuring-devices)
- [Configure networks](#configure-networks)
- [Creating configurations](#creating-configurations)
- [Displaying alarms](Displaying%20alarms.md#displaying-alarms)
- [Additional information on configurations](#additional-information-on-configurations)

## Hardware and network editor

This section contains information on the following topics:

- [Overview of hardware and network editor](#overview-of-hardware-and-network-editor)
- [Overview of settings for hardware configuration](#overview-of-settings-for-hardware-configuration)
- [Network view](#network-view)
- [Device view](#device-view)
- [Device view: Objects in the device view](#device-view-objects-in-the-device-view)
- [Device view: Area for unplugged modules](#device-view-area-for-unplugged-modules)
- [Topology view](#topology-view)
- [Inspector window](#inspector-window)
- [Inspector window: Displaying UDTs](#inspector-window-displaying-udts)
- [Hardware catalog](#hardware-catalog)
- [Browsing the hardware catalog](#browsing-the-hardware-catalog)
- [Enabling product support](#enabling-product-support)
- [Displaying product support for hardware components](#displaying-product-support-for-hardware-components)
- [Printing hardware and network configurations](#printing-hardware-and-network-configurations)
- [Printing: Changing settings](#printing-changing-settings)
- [Printing: Enabling page break preview](#printing-enabling-page-break-preview)
- [Keyboard operation: Navigation in the editor](#keyboard-operation-navigation-in-the-editor)
- [Keyboard operation: Editing objects](#keyboard-operation-editing-objects)

### Overview of hardware and network editor

#### Function of the hardware and network editor

The hardware and network editor opens when you double-click on the "Devices and Networks" entry in the project tree. The hardware and network editor is the integrated development environment for configuring, networking and assigning parameters to devices and modules. It provides maximum support for the realization of the automation project.

#### Structure of the hardware and network editor

The hardware and network editor consists of the following components:

![Structure of the hardware and network editor](images/61144128651_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | [Device view](#device-view), [Network view](#network-view), [Topology view](#topology-view): Graphic area |
| ② | [Device view](#device-view), [Network view](#network-view), [Topology view](#topology-view): Table area |
| ③ | [Hardware catalog](#hardware-catalog) |
| ④ | [Inspector window](#inspector-window) |

The hardware and network editor provides you with three views of your project. You can switch between these three views at any time depending on whether you want to produce and edit individual devices and modules, entire networks and device configurations or the topological structure of your project.

Drag the devices and modules you need for your automation system from the hardware catalog to the network, device ot topology view.

The inspector window contains information on the object currently marked. Here you can change the settings for the object marked.

### Overview of settings for hardware configuration

In "Options &gt; Settings &gt; Hardware configuration", you can make various settings relating to the hardware configuration.

#### Overview

The following table provides an overview of the settings for the hardware configuration:

| Group | Setting | Description |
| --- | --- | --- |
| Information on product support | Deactivated | Prevents access to the Siemens Industry Online Support |
| Via Internet | Enables access to product information about individual devices in the hardware catalog via the Internet. |  |
| Topology overview | Temporarily assigning an IP address | Assigns a temporary IP address for topology discovery if a device does not have a valid IP address. Topology information (LLDP) cannot be read from a device without valid IP address. |
| Show a warning if the option is activated | Shows a warning when a temporary IP address is assigned to a device during topology discovery. |  |
| Compiling and downloading | Download module comment | Transfers any existing comments in addition to the hardware configuration when loading the hardware configuration to the device. The comment is available after the device is loaded to a programming device. |
| Download I&amp;M data | This option must be enabled if you want to be able to also download I&amp;M data to the actual hardware when downloading the hardware configuration, the software or both to a device. |  |

---

**See also**

[Changing the settings](Introduction%20to%20the%20TIA%20Portal.md#changing-the-settings)
  
[Enabling product support](#enabling-product-support)
  
[Displaying product support for hardware components](#displaying-product-support-for-hardware-components)
  
[Topology view](#topology-view)

### Network view

#### Introduction

The network view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assign device parameters
- Networking devices with one another
- Editing the device names

#### Structure

The following diagram shows the components of the network view:

![Structure](images/68923669131_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Toolbar of network view |
| ③ | Graphic area of network view |
| ④ | Overview navigation |
| ⑤ | Table area of network view |

You can use your mouse to change the division between the graphic and table areas of the network view. The division can be changed between horizontal and vertical using a button in the toolbar. To change the position of the divider, click between the graphic and the table areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

#### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/21336125579_DV_resource.Stream@PNG-de-DE.png) | Mode to network devices. |
| ![Toolbar](images/21336128267_DV_resource.Stream@PNG-de-DE.png) | Mode to create connections. You can use the adjacent drop-down list to set the connection type. |
| ![Toolbar](images/21336122891_DV_resource.Stream@PNG-de-DE.png) | Mode to create relations. |
| ![Toolbar](images/125427930379_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment for PROFINET devices. For this purpose the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/21336119307_DV_resource.Stream@PNG-de-DE.png) | Show interface addresses. You can edit the addresses for the MPI, PROFIBUS and Ethernet interfaces in the network view itself: Select the required address and then click on the selected address field or press [F2]. |
| ![Toolbar](images/25209878539_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the pages break when printed. |
| ![Toolbar](images/78406352907_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/21357954699_DV_resource.Stream@PNG-de-DE.png) | You can zoom in (+) or zoom out (-) the view in steps using the zoom symbol or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/125427934347_DV_resource.Stream@PNG-de-DE.png) | Displays the name of the devices fully in the graphical view if these are cut off because of their length on the right or left and are therefore not displayed completely. |
| ![Toolbar](images/25385115915_DV_resource.Stream@PNG-de-DE.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

#### Graphic area

The graphic area of the network view displays any network-related devices, networks, connections and relations. In this area, you add devices from the hardware catalog, connect them with each other via their interfaces and configure the communication settings.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom leveling using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

#### Overview navigation

Click in the overview navigation to obtain an overview of the created objects in the graphic area. By holding down the mouse button, you can quickly navigate in the overview navigation to the desired objects and display them in the graphic area.

#### Table area

The table area of the network view includes various tables for the devices, connections and communication settings present:

- Network overview
- Connections
- Relations
- IO Communication
- VPN

You can use the shortcut menu of the title bar of the table to adjust the tabular display.

---

**See also**

[Adding a device to the hardware configuration](#adding-a-device-to-the-hardware-configuration)
  
[Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)
  
[Networking devices in the network view](#networking-devices-in-the-network-view)
  
[Tabular network overview](#tabular-network-overview)
  
[Configure networks](#configure-networks)
  
[Layout of the user interface](Introduction%20to%20the%20TIA%20Portal.md#layout-of-the-user-interface)
  
[Configuring S7 connections (S7-1200)](#configuring-s7-connections-s7-1200)
  
[Configuring HMI connections](#configuring-hmi-connections)

### Device view

#### Introduction

The device view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assign device parameters
- Configuring and assign module parameters
- Editing the names of devices and modules

#### Structure

The following diagram shows the components of the device view:

![Structure](images/68923673867_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Toolbar of device view |
| ③ | Graphic area of the device view |
| ④ | Overview navigation |
| ⑤ | Table area of device view |

You can use your mouse to change the spacing between the graphic and table areas of the device view. The division can be changed between horizontal and vertical using a button in the toolbar. To change the position of the divider, click between the graphic and the table areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

#### Toolbar

You can switch between the devices in your project in the device view using the drop-down list in the toolbar. The following functions are also available for device selection in addition to the drop-down list:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/21336113035_DV_resource.Stream@PNG-de-DE.png) | Switches to the network view. The device view can switch between the existing devices using the drop-down list. |
| ![Toolbar](images/21335642379_DV_resource.Stream@PNG-de-DE.png) | Show the area of unplugged modules. |
| ![Toolbar](images/125427930379_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment for PROFINET devices. For this purpose the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/21335645963_DV_resource.Stream@PNG-de-DE.png) | Show module labels. You can edit the labeling in the device view itself: Select the required labeling and then click on the selected text field or press [F2]. |
| ![Toolbar](images/25209878539_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the pages break when printed. |
| ![Toolbar](images/21357954699_DV_resource.Stream@PNG-de-DE.png) | You can use the Zoom icon to zoom in (+) or out (-) incrementally or to drag a frame around an area to be enlarged. With signal modules, you can recognize the address labels of the I/O channels from a zoom level of 200% or higher. |
| ![Toolbar](images/78406352907_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/25385115915_DV_resource.Stream@PNG-de-DE.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

#### Graphic area

The graphic area of the device view displays hardware components and if necessary the associated modules that are assigned to each other via one or more racks. In the case of devices with racks, you have the option of installing additional hardware objects from the hardware catalog into the slots on the racks.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom leveling using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

#### Overview navigation

Click in the overview navigation to obtain an overview of the created objects in the graphic area. By holding down the mouse button, you can quickly navigate in the overview navigation to the desired objects and display them in the graphic area.

#### Table area

The table area of the device view gives you an overview of the modules used and the most important technical and organizational data.

You can use the shortcut menu of the title bar of the table to adjust the tabular display.

---

**See also**

[Rack: Basics](#rack-basics)
  
[Network view](#network-view)
  
[Device view: Area for unplugged modules](#device-view-area-for-unplugged-modules)
  
[Rack: Inserting a module](#rack-inserting-a-module)
  
[Device view: Objects in the device view](#device-view-objects-in-the-device-view)
  
[Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)
  
[Layout of the user interface](Introduction%20to%20the%20TIA%20Portal.md#layout-of-the-user-interface)

### Device view: Objects in the device view

A graphic display of the rack and the devices plugged into it is shown in the left area of the device view. You can see the device overview in the right area of the device view. The device overview is a table showing you the most important information about the modules inserted in the rack. Both areas are displayed in a window. The size of both areas is adjusted using a divider. You can also use it to display one or the other area in full or to hide them.

#### Structure and content of device view

The offline configuration of the devices in the rack are displayed in the graphic device view. This is a symbolic representation of the configuration on the real rack.

The rack configuration is displayed as a table in the device view. Each line in the table contains the information for assigning a slot.

The following screenshot shows the device view with the configuration of a SIMATIC S7-1200 CPU.

![Structure and content of device view](images/78407125131_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Graphic view of the allocation of the rack by the CPU and various modules in slots 1 to 4, as well as 101 and 102. |
| ② | You can use the divider to adjust the proportion of the device view between the left area (graphic view) and the right area (device overview). If you click on the arrows, you can quickly switch the division of the separate areas. |
| ③ | Device view with the tabular representation of the rack's slots and the inserted components. You can show additional columns and hide displayed columns using the shortcut menu of the column title. |

Each line in the device overview represents one slot. The key information for each slot is displayed in the various columns:

| Column | Meaning |
| --- | --- |
| Online status | Symbolic representation of the online status |
| Fail-safe | Symbolic representation for fail-safe module |
| Module | Name of module, can be edited in any way |
| Rack | Number of the rack |
| Slot | Slot number |
| I address | Input address area, can be edited in any way |
| Q address | Output address area, can be edited in any way |
| F-source address | F-source address when using fail-safe I/O |
| F-destination address | F-destination address when using fail-safe I/O |
| Type | Catalog name of module |
| Article no. | Article number of the module |
| Firmware | Firmware version of the module |
| Comment | Optional comment |

#### Display in I/O channels

If you set the zoom level in the device view to at least 200%, you can see the individual I/O channels for I/O modules. If you have defined PLC tags for the channels, the names of the PLC tags are displayed.

The figure below shows the input channels of the digital input module with the two PLC tags "Test1" and "Test2" at a zoom level of 400 %.

![Display in I/O channels](images/69008782731_DV_resource.Stream@PNG-de-DE.png)

You can select the individual I/O channels and have the following options for channels with PLC tags:

- You see the general properties of the selected PLC tag in the inspector window under "Properties".
- In the inspector window under "Info &gt; Cross-references" you find the cross-reference information on the selected PLC tag. If you have selected the PLC tag, you can also open the cross-reference information using the shortcut menu.

---

**See also**

[Device view](#device-view)
  
[Overview of PLC tag tables](Declaring%20PLC%20tags.md#overview-of-plc-tag-tables)

### Device view: Area for unplugged modules

In some cases, the modules for a hardware configuration are not assigned a slot for short periods. Such unplugged modules are moved to the area of unplugged modules, a special area in the device view.

#### Adding modules to the storage area

The modules that, for example, should be assigned to a device using a copy action but for which the corresponding rack does not have a free compatible slot, are moved automatically into the area of unplugged modules.

Under the following conditions, modules are automatically added to the area of unplugged modules:

- In the network view, a module is moved to a device but the rack does not have a compatible free slot.
- In the device view, a module is moved or copied from the rack, the hardware catalog or the project tree straight into the storage area.

CPs and FMs that occupy a network resource can be moved into the area of unplugged modules but will lose the network resources they have been assigned.

You can add modules to the area of unplugged modules by means of drag-and-drop, for example. To do this, the area must be opened.

#### Using the area of unplugged modules

Use the corresponding button to open the area of unplugged modules.

You can find the area of unplugged modules in the device view.

![Using the area of unplugged modules](images/25455485835_DV_resource.Stream@PNG-en-US.png)

You open the area of unplugged modules with the respective icon in the [toolbar of the device view](#device-view).

| Icon | Meaning |
| --- | --- |
| ![Using the area of unplugged modules](images/6480223627_DV_resource.Stream@PNG-de-DE.png) | Open area of unplugged modules |

> **Note**
>
> To free up slots, move modules from your configuration into the storage area and plug the modules you want from the storage area into the freed up slots.
>
> You can use this approach to temporarily move modules whose parameters have already been assigned out of the configuration without deleting them.

#### Treatment of modules in the storage area

The following rules apply to modules in the storage area:

- The modules appear in the project tree under the corresponding device in the "Local modules" folder.
- The modules retain all settings and parameters previously assigned.
- The modules are not taken into account during loading to a target system. This means that a consistency check is not undertaken for modules in the area of unplugged modules.
- Using the context menu, the modules can be copied, cut, or deleted, for example.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Communication modules in the storage area**  When compiling the configuration, CPs or CMs in the storage area must not be connected to a subnet, otherwise this leads to an error when compiling the configuration. If a communication module in the storage area is connected to a subnet, pull the module out of the storage area and disconnect it from the subnet. You can then move the module back to the storage area. |  |

### Topology view

#### Introduction

The topology view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Displaying the Ethernet topology
- Configuring the Ethernet topology
- Identifying and minimizing differences between the desired and actual topology
- Editing the device names

#### Structure

The following figure provides an overview of the topology view.

![Structure](images/94962908299_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Topology view toolbar |
| ③ | Graphic area of the topology view |
| ④ | Overview navigation |
| ⑤ | Table area of the topology view (topology overview) |

You can use your mouse to change the spacing between the graphic and table areas of the topology view. The division can be changed between horizontal and vertical using a button in the toolbar. To change the position of the divider, click between the graphic and the table areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

#### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/125427930379_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment for PROFINET devices. For this purpose the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/83418604683_DV_resource.Stream@PNG-de-DE.png) | Changes the position of the devices in the topology view so that the new position is as close as possible to the position in the network view. |
| ![Toolbar](images/25209878539_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the pages break when printed. |
| ![Toolbar](images/21357954699_DV_resource.Stream@PNG-de-DE.png) | You can zoom in (+) or zoom out (-) the view in steps using the zoom symbol or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/78406352907_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/25385115915_DV_resource.Stream@PNG-de-DE.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

#### Graphic area

The graphic area of the topology view displays Ethernet modules with their appropriate ports and port interconnections. Here you can add additional hardware objects with Ethernet interfaces. See: [Adding a device to the hardware configuration](#adding-a-device-to-the-hardware-configuration)

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom leveling using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

#### Overview navigation

Click in the overview navigation to obtain an overview of the created objects in the graphic area. By holding down the mouse button, you can quickly navigate in the overview navigation to the desired objects and display them in the graphic area.

#### Table area

The table area consists of the following two tabs:

- "Topology overview" tab
- "Topology comparison" tab

The "Topology overview" tab displays the Ethernet or PROFINET modules, their ports and port interconnections in a table. This table corresponds to the network overview table in the network view.

In the "Topology comparison" tab, you identify and minimize differences between the desired and actual topology.

---

**See also**

[Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)
  
[Overview of settings for hardware configuration](#overview-of-settings-for-hardware-configuration)
  
[Layout of the user interface](Introduction%20to%20the%20TIA%20Portal.md#layout-of-the-user-interface)

### Inspector window

The properties and parameters shown for the object selected can be edited in the Inspector window.

#### Structure

The Inspector window consists of the following components:

![Structure](images/61413699851_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Switch between various information and work areas |
| ② | Switch between various tabs of the information and work areas |
| ③ | Navigation between various pieces of information and parameters |
| ④ | Display showing the selected information and parameters |

#### Description of functions

The information and parameters in the Inspector window are split into different types of information with different tabs:

- Properties

  This is where you can configure the device. You can make the settings for the hardware, edit tags and system constants and manage project texts. The following tabs are available here:

  - General (see [Properties and parameters](#editing-properties-and-parameters))
  - IO tags (see [Overview of PLC tag tables](Declaring%20PLC%20tags.md#overview-of-plc-tag-tables))
  - System constants (see [Rules for global system constants](Declaring%20PLC%20tags.md#rules-for-global-system-constants))
  - Texts (see [Project text basics](Editing%20project%20data.md#project-text-basics))
- Info

  In this area, you will find general information on the device in the project, a cross-reference list and messages and notes on compiling the device. The following tabs are available here:

  - General
  - Cross-reference list (see [Cross-references in the Inspector window](Displaying%20cross-references.md#editing-cross-references-in-the-inspector-window))
  - Compiling (see [Information on compiling](Editing%20project%20data.md#general-information-on-compiling-project-data))
- Diagnostics

  When you go online with the device, you will find the diagnostic information for the device and its connections here. The relevant diagnostic messages are also displayed. The following tabs are available here:

  - Device information (see [Hardware diagnostics](Device%20and%20network%20diagnostics.md#principal-methods-of-hardware-diagnostics))
  - Connection information (see [Connection diagnostics](Device%20and%20network%20diagnostics.md#overview-of-connection-diagnostics))
  - Message display (see [Message display](Displaying%20alarms.md#overview-of-the-alarm-display))

To display the corresponding information and parameters, click in the relevant area.

#### Display of device properties

The "Properties" area is the most important one for configuring an automation system. The editing options for this area are therefore described in detail below. For information on the other areas, please see the links above to other sections of the information system.

**"General" tab**

Display the properties and settings of the device or module. Here you can edit the settings and parameters. The left pane of the Inspector window is used for area navigation. Information and parameters are arranged there in groups. If you click on the arrow symbol to the left of the group name, you can expand the group if sub-groups are available. If you select a group or sub-group, the corresponding information and parameters are displayed in the right pane of the Inspector window and can be edited there too.

**"IO tags" tab**

Display the IO tags of the device, the PLC and the individual modules. You can assign names for the tags, assign the tags to the user-defined tag tables via a drop-down list, and enter comments for the tags. The IO tags are also shown in the PLC tag table.

![Display of device properties](images/85542136203_DV_resource.Stream@PNG-en-US.png)

You can click on the tag symbols in the table to drag and drop tags for use in other editors. For example, you can assign a tag to an instruction in the programming editor or copy a tag to the tag table of another device.

> **Note**
>
> **Using Autofill function**
>
> If you want to create multiple tags with similar names, you can also click on the name of a tag and drag the frame at the bottom right-hand corner over fields above or below. A new tag is created in all fields selected. To differentiate between the tags, a number is added to the name of the original tag in each case. If the tag name already ends in a number, the number is incremented:
>
> ![Display of device properties](images/85603315595_DV_resource.Stream@PNG-en-US.png)
>
> Using the same method, you can also use the column to create new tags for the tag table or assign existing tags a different tag table. Select a tag table from the drop-down list and drag the frame over additional fields as described above. This creates new tags in the corresponding tag table:
>
> ![Display of device properties](images/85604699787_DV_resource.Stream@PNG-en-US.png)
>
> If existing tags are affected by these actions, a dialog appears to ask whether the affected tags should be overwritten or whether new tags should only be inserted in empty fields. In the latter case, this means that only three tags are added to an area with nine fields and six existing tags; the existing tags are not changed.

**"System constants" tab**

Display of the global constants used by the device with HW identifiers, for example, of the modules, submodules and interfaces. Using the drop-down list, you can select whether to view all system constants of the device or only the system constants of the hardware or the software.

![Display of device properties](images/85542163595_DV_resource.Stream@PNG-en-US.png)

With I-slaves and I-devices, the system constants of the DP master or IO controller relating to the I-slave or I-device are also displayed.

If you click on the link in the column in which the use of the constant is displayed, the device view of the corresponding device opens. The system constants are also shown in the PLC tag table.

You can click on the constant symbols in the table to drag and drop system constants to use in other editors. For example, you can assign a system constant to an instruction in the programming editor or create a system constant as a user constant in another device.

**"Texts" tab**

Display the reference language and specify the text source for the project texts. Please see the rest of the information system.

---

**See also**

[Overview of hardware and network editor](#overview-of-hardware-and-network-editor)
  
[Translating project texts of individual objects](Editing%20project%20data.md#translating-project-texts-of-individual-objects)
  
[What you need to know about HW identifiers (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#what-you-need-to-know-about-hw-identifiers-s7-1200-s7-1500-s7-1500t)
  
[Addressing modules (S7-1200)](Configuring%20automation%20systems.md#addressing-modules-s7-1200)
  
[Addressing modules (S7-1500)](Configuring%20automation%20systems.md#addressing-modules-s7-1500)
  
[Inspector window: Displaying UDTs](#inspector-window-displaying-udts)

### Inspector window: Displaying UDTs

Under "Properties &gt; IO tags", the Inspector window displays self-defined data structures comprising multiple elements. These UDT (User Defined Data Types) PLC data types are displayed differently from simple IO tags.

#### Display of UDTs in the I/O tag table

Structured PLC tags that occupy the address space of a module are displayed along with the data items they contain in combined columns. Occupied address areas are indicated by vertical lines and individual addresses by small diamonds.

The following symbols are used for display in line with IO module channel address assignment by the address area of the UDTs:

| Symbol | Meaning |
| --- | --- |
| ![Display of UDTs in the I/O tag table](images/85532238219_DV_resource.Stream@PNG-de-DE.png) | Start of a data item address area covering several channels.  The address area of the entire channel is used. |
| ![Display of UDTs in the I/O tag table](images/85531993227_DV_resource.Stream@PNG-de-DE.png) | Part of a data item address area covering several channels.  The address area of the entire channel is used. |
| ![Display of UDTs in the I/O tag table](images/85531689995_DV_resource.Stream@PNG-de-DE.png) | End of a data item address area covering several channels.  The address area of the entire channel is used. |
| ![Display of UDTs in the I/O tag table](images/85532074891_DV_resource.Stream@PNG-de-DE.png) | Complete address area of a data item over the address area of a channel used in full.  Example: Only the input word of a channel is completely used for a data item. |
| ![Display of UDTs in the I/O tag table](images/85532259851_DV_resource.Stream@PNG-de-DE.png) | Start of a data item address area covering several channels.  Only part of the address area of the channel is used. |
| ![Display of UDTs in the I/O tag table](images/85532040459_DV_resource.Stream@PNG-de-DE.png) | End of a data item address area covering several channels.  Only part of the address area of the channel is used. |
| ![Display of UDTs in the I/O tag table](images/85532307083_DV_resource.Stream@PNG-de-DE.png) | Complete address area of a data item. Only the first part of the channel address is used.  Example: Only the first byte of a word is assigned. |
| ![Display of UDTs in the I/O tag table](images/85532315915_DV_resource.Stream@PNG-de-DE.png) | Complete address area of a data item. Only the second part of the channel address is used. Example: Only the second byte of a word is assigned. |
| ![Display of UDTs in the I/O tag table](images/85531680651_DV_resource.Stream@PNG-de-DE.png) | Single address of a data item for a channel that only has one address. Example: Individual bit access to the channel address of a digital input. |
| ![Display of UDTs in the I/O tag table](images/85527831819_DV_resource.Stream@PNG-de-DE.png) | Single address of a data item for a channel that has multiple addresses. Example: Individual bit access to the channel address of an analog input. |

#### Application example

The figure below shows a tag table with a UDT "Motor" PLC data type and its data items "Start", "Stop" and "Dummy":

![Application example](images/85502613131_DV_resource.Stream@PNG-en-US.png)

For a DI32 input module with input addresses I0.0 to I3.7, you see the combined column "Motor ("MotorUDT")" under the IO tags in the Inspector window. This combined column contains a column for the address area of the UDT "Motor" and a column for the data items contained in the UDT: "Motor.Dummy", "Motor.Start" and "Motor.Stop". The "Status" data item only starts at address I4.0 and is not displayed in the IO tags for this input module, because the address area of the 32 digital channels only runs from I0.0 to I3.7. The tag "ErrorCode (Byte)" is not part of the UDT. It is therefore not displayed in the combined column under UDT "Motor", but is instead shown in a separate column:

![Application example](images/85501462667_DV_resource.Stream@PNG-en-US.png)

The UDT "Motor" occupies an address area from I0.0 to I3.7 in this module. Within this address area, the "Dummy" tag occupies the address area from I0.0 to I1.7, and the two tags "Start" and "Stop" occupy the single addresses I2.0 and I2.1. The "ErrorCode (Byte)" tag that is not part of the UDT occupies the addresses I3.0 to I3.7 in its own column.

> **Note**
>
> The table of IO tags only shows the data in the address area of the selected device; in this case the address area of the input module DI32. When an additional input module with at least 16 channels is connected, the display of the address assignment is continued by the UDT with the extended address area: The address area of the UDT "Motor" runs to address I5.7, and the status data item it contains covers addresses I4.0 to I5.7. The "Status" data item occupies single addresses for individual status bits from I4.0 to I4.7. An additional column is added to the combined column of the UDT to display the status bits.

---

**See also**

[Other useful information regarding structured PLC tags](Declaring%20PLC%20tags.md#other-useful-information-regarding-structured-plc-tags)
  
[Creating structured PLC tags](Declaring%20PLC%20tags.md#creating-structured-plc-tags)
  
[Inspector window](#inspector-window)
  
[Details view](Introduction%20to%20the%20TIA%20Portal.md#details-view)
  
[Using PLC data types (UDT) (S7-1200, S7-1500)](Programming%20recommendations%20%28S7-1200%2C%20S7-1500%29.md#using-plc-data-types-udt-s7-1200-s7-1500)

### Hardware catalog

The "Hardware catalog" task card gives you easy access to a wide range of hardware components.

#### Structure

The "Hardware catalog" task card consists of the following panes:

![Structure](images/151209949451_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | "Catalog" pane, search and filter function |
| ② | "Catalog" pane, component selection |
| ③ | "Information" pane |

#### Search and filter function

The search and filter functions of the "Catalog" pane make it easy to search for particular hardware components. After entering the search text, you can start a search in the upwards or downwards direction from the current catalog position.

You can limit the display of the hardware components to certain criteria using the filter function. For example, you can limit the display to objects that you can also place within the current context or which contain certain functions. Objects that can be used in the current context include, for example, interconnectable objects in the network view or only modules compatible with the device in the device view.

You can create hardware profiles with which the objects displayed in the hardware catalog are limited. For example, you could create a hardware profile in which only certain controllers can be seen and another profile in which only certain devices of the distributed I/O are included. You can switch between the created hardware profiles.

#### Component selection

The component selection in the "Catalog" pane contains the installed hardware components in a tree structure. You can move the devices or modules you want from the catalog to the graphic work area of the device or network view.

Installed hardware components without a license are grayed out. You cannot use non-licensed hardware components.

Hardware components belonging to various components groups thematically are partially implemented as linked objects. When you click on such linked hardware components, a catalog tree opens in which you can find the appropriate hardware components.

#### Information

The "Information" pane contains detailed information on the object selected from the catalog:

- Schematic representation
- Name
- Article number
- Version number
- Description
- Type Identifier (only when activated)

> **Note**
>
> **Type Identifier**
>
> You can activate the display of the "Type Identifier" attribute in the "Options &gt; Settings &gt; Hardware configuration" menu. If the Type Identifier is activated, hardware objects for use in external development environments can be uniquely identified. The Type Identifier is displayed in the "Information" pane in the hardware catalog.

---

**See also**

[Browsing the hardware catalog](#browsing-the-hardware-catalog)
  
[Overview of hardware and network editor](#overview-of-hardware-and-network-editor)

### Browsing the hardware catalog

#### Introduction

Use the "Hardware catalog" task card to select the hardware components you want for a hardware configuration. Use the hardware catalog to select the interconnectable hardware components in the network and topology view and to select the modules you want in the device view.

#### Context filter

You can use the "Filter" option of the hardware catalog to restrict the number of displayed hardware components and the number of hardware components that can be found by searching.

When you enable the filter, components available in the hardware catalog are displayed depending on the selected view and the selected device. If you switch between the various views, the view of the filter objects is adapted to the current context. If the filter is not enabled, the entire hardware catalog is displayed in all views.

Example: With the filter enabled in the device view of an S7-1200 CPU, only S7-1200 CPUs and matching modules are displayed in the hardware catalog.

#### Search options

You can use the search function to search for specific entries in the hardware catalog. Note the following rules when entering search terms:

- No distinction is made between upper and lower case text.
- Dashes and blanks are ignored during the search.
- The search function considers parts of a search term.
- Multiple search terms must be separated by a space.
- The asterisk "*" is used as a wildcard.

> **Note**
>
> **Use of wildcards in the hardware catalog**
>
> In search queries, the asterisk "*" is used as a wildcard. A search for "1A**0", for example, also return hits with "1AD30" or "1AE40". The hardware catalog also contains modules with wildcards in their article numbers. The wildcards in the various article numbers can be either asterisks or the lowercase letters "x", "y" or "z". If you search for the specific article number "3RW4 422-1BC34", for example, your search will also return articles with the number "3RW4 422-*BC**" and "3RW4 4xx-1By3z".

You start the search from an object highlighted in the hardware catalog and either search upwards or downwards.

| Icon | Meaning |
| --- | --- |
| ![Search options](images/21350792331_DV_resource.Stream@PNG-de-DE.png) | Search down |
| ![Search options](images/21357951115_DV_resource.Stream@PNG-de-DE.png) | Search up |

#### Browsing the hardware catalog

If you want to browse the hardware catalog, proceed as follows:

1. Click in the entry field of the search function
2. Enter a search term. The search includes the following elements:

   - Name of device or module
   - Article number (MLFB)
   - Description in "Information" pane
3. Click on either the "Search down" or "Search up" button.

**Note**

To ensure the right search direction, note which point you have marked in the hardware catalog. To browse the entire catalog, click on the topmost object of the hardware catalog and start the search once you have entered the search term by clicking "Search down".

The first match with the search term found is displayed as the result. For more search results, again click on the "Search down" or "Search up" button.

Observe the context filter of the hardware catalog. If this is selected, the search in the hardware catalog is restricted to the displayed inserted hardware components.

---

**See also**

[Hardware catalog](#hardware-catalog)

### Enabling product support

For each device in the hardware catalog, you have the option of displaying additional information that is stored in the Siemens Industry Online Support. By default, the function is disabled. Instructions for enabling the function are given below.

#### Requirement

The TIA Portal has access to the Internet.

#### Procedure

To enable access to Siemens Industry Online Support, follow these steps:

1. In the "Options" menu, select the "Settings" command.
2. Open the "Hardware configuration" group in the area navigation.
3. Select the "Via Internet" check box.

#### Result

You can access product support, FAQs and manuals in the hardware catalog via the shortcut menu for the module.

---

**See also**

[Displaying product support for hardware components](#displaying-product-support-for-hardware-components)
  
[Overview of settings for hardware configuration](#overview-of-settings-for-hardware-configuration)

### Displaying product support for hardware components

In the hardware catalog, you have direct access to information that is stored for each module in Siemens Industry Online Support. You can jump directly to the following pages in Siemens Industry Online Support:

- Information on product support
- FAQs
- Manuals

#### Requirement

- You have access to the Internet.
- Access to Product Support is enabled in the settings of the TIA Portal.

  For information on how to enable the function, refer to section "[Enabling product support](#enabling-product-support)".

#### Procedure

To display the information for a particular module in Siemens Industry Online Support, follow these steps:

1. Navigate to the required module in the hardware catalog.
2. Right-click the module.
3. Select one of the following entries in the shortcut menu:

   - Information on product support
   - FAQs
   - Manuals

#### Result

The default browser set in the operating system is opened and the relevant page in the Siemens Industry Online Support is loaded.

---

**See also**

[Enabling product support](#enabling-product-support)
  
[Overview of settings for hardware configuration](#overview-of-settings-for-hardware-configuration)

### Printing hardware and network configurations

#### Printout of hardware and network configurations

You can print out the following elements of the hardware and network view as part of the project documentation:

- Graphic network view
- Network overview table
- Graphic device view
- The device overview table
- The parameters of the object currently selected in the editor

#### Printout of editor content

If you start a printout within an opened editor and no module is selected, the content of the editor is always printed. This includes a graphic representation of the editor as well as the table for the editor. You can adapt the scope of the printout. You can specify whether only the graphic view, the table or both together are to be printed. Read section "[Printing: Changing settings](#printing-changing-settings)" for more on this.

If the graphic is larger than the page layout you have selected, the printout is continued on the next page. No content is lost this way. Alternatively, you can change the zoom level of the graphic representation to fit the printout on one page. The printout is always made in the currently selected zoom setting.

To check that all content fits on one page, you can either use the print preview or activate the page break preview. When page break preview is activated, dashed lines are displayed within the graphic editor at the location where the page break is later made.

#### Printing very large tables

If a table is larger than the print area and therefore cannot be fully printed, the content of the table is not printed as a table, but instead as pairs between value and key.

Example:

| Object name | Property 1 | Property 2 |
| --- | --- | --- |
| Object A | Value A1 | Value A2 |
| Object B | Value B1 | Value B2 |

In this case, the printout has the following appearance:

**Object A**

Property 1: Value A1

Property 2: Value A2

**Object B**

Property 1: Value B1

Property 2: Value B2

You can also preset this as a template so that tables are always printed as pairs between the key and the value. Read section "[Changing the print settings](Editing%20project%20data.md#changing-the-print-settings)" for more on this.

#### Printing module parameters

Parameters of selected modules are printed out along with the current value settings in text form. All parameters from corresponding modules are also printed. For example, if you have selected a CPU, the parameters of an inserted signal board, if present, are printed as well.

You can determine the scope of the module parameters to be printed. In the "Print" dialog, select whether all properties and parameters of a module are to be printed or whether to use the compact printout. If you select the compact form, only the entries in the "General" area of the module properties are printed. Comments on modules, as well as the author and module description, are excluded. In compact mode, the following module parameters are therefore printed, for example:

- Module specifications

  Name, module slot, short description, article number, firmware version
- Name of the PROFINET interface
- Subnet specifications

  Name of the subnet, ID of the S7 subnet

---

**See also**

[Printing: Changing settings](#printing-changing-settings)
  
[Documentation settings](Editing%20project%20data.md#documentation-settings)
  
[Creating a print preview](Editing%20project%20data.md#creating-a-print-preview)
  
[Printing project data](Editing%20project%20data.md#printing-project-data)
  
[Printing: Enabling page break preview](#printing-enabling-page-break-preview)

### Printing: Changing settings

#### Changing the scope of the printout

When printing from an editor, you can specify whether both graphics and tables are to be printed or just one of the two. Both are printed by default.

#### Procedure

To change the scope of the printout, proceed as follows:

1. In the "Options" menu, select the "Settings" command.
2. In the area navigation, open the "Print settings" parameter group under "General".
3. Scroll to the "Hardware configuration" group.
4. Select or clear the "Active graphic view" check box, depending on whether you want to print the graphics of the network and device view as well.
5. Select or clear the "Active table" check box, depending on whether you want to print the table for the editor as well.

---

**See also**

[Printing hardware and network configurations](#printing-hardware-and-network-configurations)

### Printing: Enabling page break preview

You can activate the page break preview for the printout in the graphic editor. If this option is activated, dashed lines are shown within the graphic editor at the locations where page breaks are later made during printout.

#### Procedure

Proceed as follows to activate the page break preview:

1. Select the graphic area of the corresponding view.
2. Click on the "Show page break" symbol in the toolbar of the graphic editor.

   Dashed lines are displayed within the graphic editor at the location a page break is later made.
3. To modify the frame layout, select the "Print" command in the "Project" menu.
4. To disable page break preview, click again on the "Show page break" symbol in the toolbar of the graphic editor.

### Keyboard operation: Navigation in the editor

You can use shortcut keys in the network and device view to navigate between the components of the hardware and network editor and its objects.

#### Navigating between elements and functions

| Function | Shortcut keys |
| --- | --- |
| Switch to the next lower selection level  You can use &lt;Return&gt;, for example, to switch from a selected rack to the lower selection level of the devices and modules that are snapped onto it. If a device is selected, you can use &lt;Return&gt; to switch to the lower selection level of the interfaces that are displayed on the device. | &lt;Return&gt; |
| Switch to the next higher selection level  You can use &lt;Esc&gt;, for example, to switch from a selected interface to the higher selection level of the devices and modules. If a device is selected, you can use &lt;Esc&gt; to switch to the higher selection level of the rack. | &lt;Esc&gt; |
| Navigation between objects in the current selection level  You can use the arrow keys to switch between the objects within a current selection level. To change the selection level, use the &lt;Return&gt; or &lt;Esc&gt; keys. | &lt;Up arrow&gt;  &lt;Down arrow&gt;  &lt;Right arrow&gt;  &lt;Left arrow&gt; |
| Switches to the device view | &lt;Ctrl+Shift+D&gt; |
| Switches to the network view | &lt;Ctrl+Shift+N&gt; |
| Switches to the topology view | &lt;Ctrl+Shift+T&gt; |
| Switch between editor elements  Use the &lt;Tab&gt; key to switch from one editor element to the next element. Use &lt;Shift+Tab&gt; to switch to the previous element. You can switch, for example, between the graphical view, Speedy Splitter, table view or underlying tabs. | &lt;Tab&gt;  &lt;Shift+Tab&gt; |
| Switch between tabs  Use the &lt;Ctrl+Tab&gt; keys to switch from one tab to the next tab on the right. Use &lt;Ctrl+Shift+Tab&gt; to switch to the next tab to the left. You can use these keys, for example, to switch between the device view, the network view and the topology view. | &lt;Ctrl+Tab&gt;  &lt;Ctrl+Shift+Tab&gt; |

#### Opening elements and functions

| Function | Shortcut keys |
| --- | --- |
| Opening the online and diagnostics view  When a device is selected, &lt;Ctrl+D&gt; opens the online and diagnostics view for the selected device. | &lt;Ctrl+D&gt; |
| Opening the download to device dialog  When a device is selected, &lt;Ctrl+L&gt; opens the advanced download dialog. | &lt;Ctrl+L&gt; |
| Add new device  &lt;Ctrl+N&gt; opens the dialog for adding a new device. | &lt;Ctrl+N&gt; |
| Opens the "Hardware catalog" task card | &lt;Ctrl+Shift+C&gt; |
| Opens "Online Tools" task card | &lt;Ctrl+Shift+O&gt; |

---

**See also**

[Keyboard operation in the TIA Portal](Introduction%20to%20the%20TIA%20Portal.md#keyboard-operation-in-the-tia-portal)

### Keyboard operation: Editing objects

You can execute some of the functions of the network and device view directly with a combination of keyboard and mouse in the hardware and network editor. The [keyboard operation in tables](Introduction%20to%20the%20TIA%20Portal.md#keyboard-operation-in-the-tia-portal) corresponds to standard characteristics. Here you find the keyboard operation for the graphic work area of the network and device view.

#### General keyboard operation

| Function | Shortcut keys |
| --- | --- |
| Zoom in on view in frame  Drag a frame in the graphical view in order to correspondingly change the size of the view. | &lt;Ctrl+Space&gt; + pressed mouse button |
| Move view  Move the mouse pointer in order to move the view. | &lt;Space&gt; + pressed mouse button |
| Cancel current operation | &lt;Esc&gt; |
| Separate connection  Use &lt;Esc&gt; or a double-click to exit connection mode when dragging a connection. | &lt;Esc&gt; or double-click |
| Zoom in graphic view  The enlargement or reduction depends on the direction of rotation. | &lt;Ctrl&gt; + turn mouse wheel |

#### Selected objects

| Function | Shortcut keys |
| --- | --- |
| Select object | Mouse click |
| Cut an object  The selected object is copied to the clipboard and deleted from the graphical view. | &lt;Ctrl+X&gt; |
| Copy object  The selected object is copied to the clipboard. | &lt;Ctrl+C&gt; |
| Paste object  The object from the clipboard is inserted into the selection. | &lt;Ctrl+V&gt; |
| Delete selected object | &lt;Del&gt; |
| Select several objects 1  You can add several objects to the selected objects by clicking on them individually. Alternatively, you can use &lt;Shift&gt; + pressed mouse key to drag a frame around the objects that are to be selected. | &lt;Shift&gt; + click |
| Select several objects 2  You can add several objects to the selected objects by clicking on them individually. Alternatively, you can use &lt;Shift&gt; + pressed mouse key to drag a frame around the objects that are to be selected. When holding down the &lt;Ctrl&gt; key, you can use a mouse click to deselect selected objects. | &lt;Ctrl&gt; + click |
| Move selection  When the mouse button is pressed, you can drag devices or modules to allowed slots on a rack. | Mouse button pressed |
| Copy selection  Using &lt;Ctrl&gt; + pressed mouse button you can drag devices and modules to allowed slots on a rack. This copies the devices or modules. | &lt;Ctrl&gt; + pressed mouse button |

## Configuring devices

This section contains information on the following topics:

- [Introduction to configuring hardware](#introduction-to-configuring-hardware)
- [Adding a device to the hardware configuration](#adding-a-device-to-the-hardware-configuration)
- [Adding an unspecified CPU](#adding-an-unspecified-cpu)
- [Selecting a CPU](#selecting-a-cpu)
- [Inserting a signal board in a CPU (S7-1200)](#inserting-a-signal-board-in-a-cpu-s7-1200)
- [Selecting fail-safe modules](#selecting-fail-safe-modules)
- [Rack: Basics](#rack-basics)
- [Rack: General slot rules](#rack-general-slot-rules)
- [Rack: Inserting a module](#rack-inserting-a-module)
- [Select hardware component](#select-hardware-component)
- [Copying a hardware component](#copying-a-hardware-component)
- [Moving a hardware component](#moving-a-hardware-component)
- [Replacing a hardware component](#replacing-a-hardware-component)
- [Renaming hardware component](#renaming-hardware-component)
- [Deleting a hardware component](#deleting-a-hardware-component)
- [Changing or updating hardware components](#changing-or-updating-hardware-components)
- [Editing properties and parameters](#editing-properties-and-parameters)
- [Input and output addresses in the address overview](#input-and-output-addresses-in-the-address-overview)
- [Distributed I/O in the project tree](#distributed-io-in-the-project-tree)
- [Comparing devices](Comparing%20devices.md#comparing-devices)

### Introduction to configuring hardware

To set up an automation system, you will need to configure, assign parameters and interlink the individual hardware components. The work needed for this is undertaken in the device and network view.

#### Configuring

"Configuring" is understood to mean arranging, positioning, and networking devices and modules within the device or network view. Racks are represented symbolically. Just like "real" racks, they allow you to plug in a defined number of modules.

An address is automatically assigned to each module. The addresses can be subsequently modified.

When the automation system is started, the CPU compares the configuration that is preset by the software with the actual configuration of the system. Possible errors can be detected and reported straight away.

#### Assigning parameters

"Assigning parameters" is understood to mean the setting of properties of the components used. Parameter assignment is carried out for hardware components and for data exchange settings:

- Properties of modules with assignable parameters
- Settings for data exchange between components

The parameters are loaded to the CPU and transferred to the corresponding modules when the CPU starts up. Modules can be replaced with ease since the assigned parameters are automatically loaded into the new module during startup.

#### Adjusting the hardware to the project requirements

You need to configure hardware if you want to set up, expand or change an automation project. To do this, add hardware components to your configuration, connect them to existing components, and adapt the hardware properties to the tasks.

The properties of the automation systems and modules are preset in such a way that in many cases there is no need for additional parameter assignment. Parameter assignment is however needed in the following cases:

- You want to change the default parameter settings of a module.
- You want to use special functions.
- You want to configure communication connections.

---

**See also**

[Changing properties of the modules (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#changing-properties-of-the-modules-s7-1200)

### Adding a device to the hardware configuration

#### Introduction

There are various ways of adding a connectable device from the hardware configuration in the network view and the topology view:

- Command "Add new device" in the project tree
- Double-click device in hardware catalog
- Drag-and-drop from the hardware catalog in network view or in topology view:

  - Text entry from the "Catalog" pane
  - Preview graphic from the "Information" pane
- "Add &gt; Device" command from menu bar in network view or topology view
- Shortcut menu of a device in the hardware catalog for copying and pasting

A suitable rack is created along with the new device. The selected device is inserted at the first permitted slot of the rack.

Regardless of the method selected, the added device is visible in the project tree and the network view of the hardware and network editor.

#### Adding device using the project tree

To use the project tree to add a device to the hardware configuration, proceed as follows:

1. Click on the command "Add new device" in the project tree.

   The "Add new device" dialog box opens.
2. Display the required device in the tree structure:

   - Go to required device in the tree structure.
   - Enter a device name in the entry field.
3. Select the required device from the tree.

   More information about the device presently selected is displayed on the right-side of the dialog box.
4. If necessary, set the firmware version using the drop-down list in the dialog box.
5. Select the "Open device view" check box if you want to change to the device view immediately after adding the device.

   There you can immediately continue with device configuration and equipping the rack.
6. Click on "OK" to add the device selected.

   The dialog box closes.

#### Adding device from the hardware catalog

To add a device to the hardware configuration using the hardware catalog, proceed as follows:

1. Open the network view or the topology view.
2. Open the hardware catalog.
3. Go to the required device in the hardware catalog.
4. Click on the chosen device to select it.
5. If necessary, set the firmware version using the drop-down list in the hardware catalog.
6. Drag the device to the network view or the topology view.

   ![Adding device from the hardware catalog](images/14779289739_DV_resource.Stream@PNG-de-DE.png)

   ![Adding device from the hardware catalog](images/14779289739_DV_resource.Stream@PNG-de-DE.png)

You have now placed the device in the network view or in the topology view. The displayed rectangle (in other words "Station") symbolizes the plugged device together with its rack and any lower-level modules. Double-click on the device or station to open the device view and view the new rack and inserted device. In the next steps, you can configure the device in the device view and equip the rack with modules.

---

**See also**

[Network view](#network-view)
  
[Adding an unspecified CPU](#adding-an-unspecified-cpu)
  
[Topology view](#topology-view)

### Adding an unspecified CPU

#### Introduction

If you have not yet selected a CPU but have already started programming or want to use an existing program, you have the option of using an unspecified CPU. You can also adjust some settings with unspecified CPUs. The setting options are restricted to parameters that all CPUs of the same CPU family have in common.

#### Adding an unspecified CPU in the portal view

To add an unspecified CPU in the portal view, follow these steps:

1. Now, click one of the following options:

   - "Devices &amp; networks &gt; Add new device"
   - "PLC programming" &gt; "Device" button
2. For a device family, select an unspecified CPU from the tree structure of the "Add new device" dialog.
3. Click on "Add".

An unspecified CPU is added and the device view for this CPU is opened.

#### Further options for adding unspecified CPUs

In the project view, you can add unspecified CPUs like specified CPUs:

- Using the "Add new device" button in the project tree
- In the "Hardware catalog" task card

You can also use these methods to add multiple unspecified CPUs.

#### Specifying unspecified CPUs

You have two options for specifying unspecified CPUs:

- Use drag-and-drop to assign an existing CPU from the hardware catalog to an unspecified CPU by means of [module replacement](#replacing-a-hardware-component).
- Select a selected, unspecified CPU and then the menu command "Online &gt; Hardware detection" and assign a CPU identified online. For this purpose, you assign an IP address using the "Add address for PG/PC" button.

  > **Note**
  >
  > If you want to go online after the hardware detection, you have to first download the detected configuration to your project; otherwise, an error may occur due to inconsistent configurations. After hardware detection, the article numbers of the CPU in the project and the actually existing CPU are identical, but their parameters are not. The parameters of the CPU in the project have the default values; the parameters of the actually existing CPU have the values set by you.
  >
  > After module replacement, F-CPUs behave as a CPU without failsafe functionality. In contrast to F-CPUs from the hardware catalog, after module replacement with an unspecified CPU or a hardware recognition, the F capability is turned off and the protection level is set to "Full access (no protection)".

---

**See also**

[Selecting a CPU](#selecting-a-cpu)
  
[Adding a device to the hardware configuration](#adding-a-device-to-the-hardware-configuration)
  
[Configuring an IO device through hardware detection](#configuring-an-io-device-through-hardware-detection)

### Selecting a CPU

#### Introduction

Select a CPU from the hardware catalog and place it, together with a rack, in the network view. On this device drag the desired modules from the hardware catalog; they are arranged automatically on the rack.

#### Selecting the components in the hardware catalog

Each hardware component is displayed as a folder in the hardware catalog. When you open this folder, you see the different versions of the selected hardware component with its respective article numbers.

There will be an example of how to set up a CPU with a rack in network view.

#### Requirement

- The hardware catalog is open.
- You must be in the network view.

#### Procedure

To select a CPU from the hardware catalog, proceed as follows:

1. In the hardware catalog navigate to the folder with the desired CPUs.
2. Open the folder with the desired CPU type; you will see all article numbers for the selected CPU type.
3. Click on a CPU article number to get information about the selected CPU in the "Information" pane.

   ![Procedure](images/47002641163_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/47002641163_DV_resource.Stream@PNG-en-US.png)
4. Set up the CPU and a rack. You have the following options:

   - Use drag-and-drop to drag the CPU from the hardware catalog into network view.
   - Use Copy &amp; Paste to copy the CPU to the network view.
   - Double-click the CPU entry in the hardware catalog.

---

**See also**

[Browsing the hardware catalog](#browsing-the-hardware-catalog)
  
[Adding a device to the hardware configuration](#adding-a-device-to-the-hardware-configuration)
  
[Rack: Inserting a module](#rack-inserting-a-module)
  
[Rack: Basics](#rack-basics)
  
[Adding an unspecified CPU](#adding-an-unspecified-cpu)

### Inserting a signal board in a CPU (S7-1200)

#### Introduction

Signal boards allows you to increase the number of the S7-1200 CPU's own inputs and outputs. Just like all other hardware components, you will find signal boards in the hardware catalog. However, you do not insert signal boards in the rack like other modules but directly in a slot of the CPU itself.

Note the following points when using a signal board:

- Each CPU can have only one signal board inserted in it.
- A signal board can only be inserted when the slot in the CPU is free.

There are various ways of inserting a signal board in a CPU:

- Double click on a signal board in the hardware catalog when there is a free slot in the CPU
- Drag from the hardware catalog to a free slot in the CPU
- Shortcut menu of a signal board in the hardware catalog for copying and pasting

#### Requirement

- The hardware catalog is open.
- The S7-1200 CPU has a free slot for the signal board.

#### Inserting a signal board in a CPU

To insert a signal board in a CPU, proceed as follows:

1. Go to the required signal board in the hardware catalog.
2. Select the signal board you want to use.
3. Drag the signal board to the free slot in the CPU.

   ![Inserting a signal board in a CPU](images/14779340043_DV_resource.Stream@PNG-en-US.png)

   ![Inserting a signal board in a CPU](images/14779340043_DV_resource.Stream@PNG-en-US.png)

You have now inserted a signal board in the slot of the CPU.

If you are in the network view, you can also drag a signal board to a device. If the CPU has a an empty slot for a signal board, the signal board is inserted automatically into this slot.

### Selecting fail-safe modules

#### Introduction

Fail-safe automation systems (F systems) are used to control processes with a safe state that can be achieved immediately on shutdown. F systems control processes that can be shut down immediately without endangering human beings or the environment.

#### Selecting the F components in the hardware catalog

Each hardware component is displayed as a folder in the hardware catalog. Fail-safe hardware components are displayed with yellow symbols in the hardware catalog in contrast to the blue hardware components that are not fail-safe.

The following figure shows an excerpt from the hardware catalog with an F-CPU (yellow).

Based on this color coding, you can identify F components in the hardware catalog simply and quickly.

![Selecting the F components in the hardware catalog](images/76077547915_DV_resource.Stream@PNG-de-DE.png)

#### Display of the F components in the hardware and network editor

If you use fail-safe devices and "normal" devices in the graphic views of the hardware and network editor, you can recognize them simply by the yellow color-coding of the devices.

The following figure shows two CPUs. The F CPU is shown in yellow:

![Display of the F components in the hardware and network editor](images/76077804939_DV_resource.Stream@PNG-de-DE.png)

Fail-safe modules in racks or devices can also be recognized in the device view due to their yellow color coding. Since modules that are not capable of networking are not displayed in the network or topology view, devices with F components without networking capability are represented by a special symbol in the network and topology view.

The following figure shows a "normal" CPU and an F-CPU in the network view that both contain F components:

![Display of the F components in the hardware and network editor](images/25541555083_DV_resource.Stream@PNG-de-DE.png)

Based on the color coding of the fail-safe devices and modules, you can also identify the F components quickly in the graphic views of the hardware and network editor.

### Rack: Basics

#### Introduction

To assign modules to a device, you need a rack, for example a mounting rail. Secure the modules on the rack and connect these via the backplane bus with the CPU, a power supply or other modules.

#### Creating a rack

If you insert a device in the network view, a station and a rack suitable for the device selected are created automatically. The rack and slots available are displayed in the device view. The number of slots available again depends on the type of device used.

#### Rack structure

A rack always contains the device that has been inserted in the network view. The device is permanently assigned a slot which will depend on the type of device in question. There are additional slots on the right of the device and, if necessary, on left of the device; slot numbers are located above slots in which devices are plugged.

A corresponding short description is displayed above the plugged devices and modules. You show or hide this short description via the toolbar under "View" with the command "Display module titles" or the corresponding symbol in the [toolbar of the device view](#device-view).

| Symbol | Meaning |
| --- | --- |
| ![Rack structure](images/25455478283_DV_resource.Stream@PNG-de-DE.png) | Show module titles |

When modules are selected in the hardware catalog, all the slots permitted for this module are marked. This allows you to see immediately the slot into which the selected module can be inserted.

In the following screenshot, a signal module has been selected in the hardware catalog for a partially filled S7-1200 rack:

![Rack structure](images/14778998923_DV_resource.Stream@PNG-de-DE.png)

Since slots 101-103 are reserved for communications modules, only the other free slots are shown as available slots.

You can expand and collapse the front group of slots using an arrow symbol above the expandable slot. When the group of slots is collapsed, the first and last of the group's slot numbers are displayed.

The following figure shows the expanded slot group:

![Rack structure](images/14778991755_DV_resource.Stream@PNG-de-DE.png)

Groups of slots into which modules have already been plugged cannot be collapsed.

#### Exchanging a rack

You can also replace a created rack with another rack, for example with the ET 200MP I/O device, a U-connector mounting rail with a rack with an active backplane bus. You have the following options for this:

- Drag a suitable rack from the hardware catalog to the rack to be replaced. If the selected rack is compatible with the rack in use, the dialog for module exchange opens.
- Open the shortcut menu for the selected rack and select "Replace device". If compatible racks are available, the dialog for module exchange opens.

> **Note**
>
> **Replacement of a rack with a rack with an active backplane bus**
>
> When replacing a rack with an active backplane bus, for example with ET 200MP, a representative module is automatically created in slot 0. As no hardware has to be inserted in the real configuration, this representative module is shown as an empty slot. The module is intended for the diagnostics and/or parameters of the active backplane bus according to the characteristics of the selected rack. If you select slot 0 or the representative module, you will find the properties for the active backplane bus in the Inspector window.

Also note the information on [Replacing hardware components](#replacing-a-hardware-component).

#### Multiple selection of modules and slots

There are various ways of selecting several modules or slots:

- By pressing &lt;Shift&gt; or &lt;Ctrl&gt;, you can select several modules or slots at the same time.
- Click outside the rack and then hold the mouse button and drag a frame to include the modules or slots you want to select.

---

**See also**

[Inspector window](#inspector-window)
  
[Overview of hardware and network editor](#overview-of-hardware-and-network-editor)

### Rack: General slot rules

#### Introduction

Specific slot rules apply to each automation system and module.

If you select a module from the hardware catalog in the device view, all possible slots for the module selected are marked in the rack. You can only drag modules to marked slots.

If you insert, move or swap a module, the slot rules are also applied.

#### Consistency

Some slot rules depend on how the environment is configured. This means that you can sometimes plug modules into the rack although this would result in inconsistencies at the current time. If you change the configuration, for example by selecting different modules or module parameter settings, you can make the configuration consistent again.

In cases where inserting a module results in an inconsistency that can be corrected, this will be permitted. A consistency check is run when the configuration is compiled. Inconsistencies are displayed as alarms in the Inspector window under "Info". Based on the result of the consistency check, you can revise your configuration and make it consistent again.

#### Rules for arranging modules

The following rules apply generally to modules in racks:

- You can only plug modules into a rack.
- You can only plug interface modules into a module.
- You can only use modules of the same product or system family in one rack.

There are also other special rules for some modules:

- Can only be inserted in certain slots
- Insertion depends on other modules, CPUs or settings
- Limited number of uses in a rack

### Rack: Inserting a module

#### Introduction

Once you have added devices from the hardware catalog to your configuration in network view, you can add modules to the devices. There are various ways of adding a module to a rack in the device view:

- If there is an available valid slot, double-click a module in the hardware catalog.
- Use drag-and-drop to move the module from the hardware catalog to an available valid slot in the graphic or table area:

  - Text entry from the "Catalog" pane
  - Preview graphic from the "Information" pane
- Select "Copy" in the shortcut menu for a module in the hardware catalog and then select "Paste" in the shortcut menu on an available valid slot in the graphic or table area.

To access the device view from the network view, double-click a device or station in the network view or select the Device view tab. The device view contains an illustration of the device selected within a rack. The graphic illustration of the rack in the software corresponds to the real structure, i.e. you can see the same number of slots as exist in the real structure.

> **Note**
>
> You can also move a module to a rack in the network view. The filter function for the hardware catalog must be deactivated in this instance. The module is automatically plugged into a free and permitted slot. If there are no slots available, the module will be moved to the [area of unplugged modules](#device-view-area-for-unplugged-modules).

#### Equipping a rack

Arrange the modules on a rack according to the applicable slot rules.

After a module has been inserted in a rack with an already inserted CPU, the address areas are checked automatically so that addresses are not assigned twice. After it has been inserted, each module then has one valid address range. To do so, DP slaves and IO devices must be networked with a CPU via the corresponding DP master or IO system.

#### Requirements

- You are in the device view.
- The hardware catalog is open.

#### Adding module from the hardware catalog

How to insert a module from the hardware catalog into a rack is illustrated based on the example of a signal module. To do this, follow these steps:

1. Go to the required module board in the hardware catalog.
2. Select the chosen module.
3. If necessary, set the firmware version using the drop-down list in the hardware catalog.
4. Drag the signal module to a free slot in the rack.

   ![Adding module from the hardware catalog](images/14779309835_DV_resource.Stream@PNG-de-DE.png)

   ![Adding module from the hardware catalog](images/14779309835_DV_resource.Stream@PNG-de-DE.png)

**Note**

If you activate the filter function of the hardware catalog, only those modules which match the selected device type will be displayed.

You have now inserted the digital signal module in a slot in the rack. Repeat these steps with the other modules.

The name of the module is displayed above the inserted modules. You can activate or deactivate module labeling in the menu bar with "View &gt; Show module labels".

#### Inserting module

You can also drag modules and drop them between modules that have already been inserted. To do this, drag a module above and between the two existing modules while holding down the mouse button.

![Inserting module](images/13825754251_DV_resource.Stream@PNG-de-DE.png)

A mouse pointer appears. When you release the mouse button, all modules plugged to the right of the pointer are moved one slot to the right. Any redundant modules are moved to the area of unplugged modules. The new module is plugged at the point of the freed up slot.

---

**See also**

[Device view](#device-view)
  
[Device view: Area for unplugged modules](#device-view-area-for-unplugged-modules)
  
[Rack: General slot rules](#rack-general-slot-rules)
  
[Rules for modules (S7-300)](Configuring%20automation%20systems.md#rules-for-modules-s7-300)
  
[Rules for modules (S7-400)](Configuring%20automation%20systems.md#rules-for-modules-s7-400)

### Select hardware component

You can select hardware components and additional objects of the graphic views by clicking the left mouse button. You can also select multiple objects by dragging the mouse while keeping the left mouse button pressed or with the combination of left-click and the &lt;Shift&gt; or &lt;Ctrl&gt; keys.

You can select the following objects in the graphic views: Devices (with CPU, rack, modules), CPUs, CPs, modules, subnets, connections and nodes.

#### Rules

You can select objects in the graphic views as follows:

- Left-click on object: The object is selected.
- Left-click and &lt;Ctrl&gt; on an object: The object is added to the current selection.
- Left-click and &lt;Shift&gt; on an object: All objects between the currently selected object and the previously selected objects are added to the selection.
- Drag selection frame around multiple objects while pressing left mouse button: All objects completely enclosed by the frame are added to the selection.

Multiple selection is only possible for objects of the same category:

- Category 1: Devices, subnets, connections, port interconnections
- Category 2: CPUs, CPs, interface modules / module
- Category 3: Interfaces, ports, nodes

Behavior for multiple selection with objects from different category:

- Selection frame: Only objects of the respective highest category will become part of the multiple selection
- Left-click with &lt;Shift&gt; or &lt;Ctrl&gt;: The object of a new category that was selected last remains selected; the previously selected objects are dropped from the selection.

> **Note**
>
> **Multiple selection of different types of objects**
>
> Only the same object categories can be selected in case of multiple selection. For example, multiple CPUs or multiple networks can be selected. However, it is not possible to first select a device in a multiple selection and then only add the CPU of a second device or the interface of a third device to the multiple selection.

#### Multiple selection of devices with the help of the selection frame

To select multiple devices in the network view by dragging a selection frame, follow these steps:

1. Press the left mouse button and draw a frame around all devices that you want to include in your selection:

   ![Multiple selection of devices with the help of the selection frame](images/95037859595_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of devices with the help of the selection frame](images/95037859595_DV_resource.Stream@PNG-de-DE.png)
2. Release the mouse button. All devices within the drawn frame are now part of the multiple selection.

   ![Multiple selection of devices with the help of the selection frame](images/95043282827_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of devices with the help of the selection frame](images/95043282827_DV_resource.Stream@PNG-de-DE.png)

In the example above, the selection frame was drawn around entire devices. If you draw the frame so that it does not enclose entire devices but only the CPUs contained therein, only the CPUs and not the entire device is included in the multiple selection. If you draw the selection frame so that it partially encloses entire devices and partly only CPUs, the highest category of the selected objects is decisive and only the entire devices are added to the multiple selection.

#### Multiple selection of CPUs with the help of the &lt;Shift&gt; key

Instead of the multiple selection with a selection frame, you can also make the multiple selection with the &lt;Shift&gt; key. You select two objects with this key and all objects in between are included in the multiple selection.

To select multiple CPUs in the topology view with the &lt;Shift&gt; key, follow these steps:

1. Select the first CPU of your multiple selection with the left mouse button:

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95026701835_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95026701835_DV_resource.Stream@PNG-de-DE.png)
2. Select the last CPU of your multiple selection with the left mouse button while pressing the &lt;Shift&gt; key. The two selected CPUs behave like the margins of a selection frame indicated here by the orange line:

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95018737931_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95018737931_DV_resource.Stream@PNG-de-DE.png)
3. All CPUs between the first and the last CPU selected are included in the multiple selection:

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95026490763_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of CPUs with the help of the &lt;Shift> key](images/95026490763_DV_resource.Stream@PNG-de-DE.png)

In the example above, only CPUs were selected. If you select entire devices instead, the devices between the first and the second device selected are included in the multiple selection. If you select an entire device as well as a CPU, the category of the object selected last is decisive for the category of all selected objects.

#### Multiple selection of devices with the help of the &lt;Ctrl&gt; and &lt;Shift&gt; keys

You can also make a multiple selection with the two keys &lt;Ctrl&gt; and &lt;Shift&gt;. You select multiple objects with a left mouse click and the &lt;Ctrl&gt; key. If you then select an object with a left mouse click and the &lt;Shift&gt; key, all objects between the previously selected objects and the last selected object are included in the multiple selection.

To select multiple devices in the device view with the &lt;Shift&gt; and &lt;Ctrl&gt; keys, follow these steps:

1. Use the left mouse button and press the &lt;Ctrl&gt; key to select multiple individual devices:

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95026499595_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95026499595_DV_resource.Stream@PNG-de-DE.png)
2. Select the last device of your multiple selection with the left mouse button while pressing the &lt;Shift&gt; key. The already selected devices behave like the margins of a selection frame indicated here by the orange line:

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95183533323_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95183533323_DV_resource.Stream@PNG-de-DE.png)
3. All devices of the virtual selection frame and the subnets in the selection frame are now included in the multiple selection.

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95026546827_DV_resource.Stream@PNG-de-DE.png)

   ![Multiple selection of devices with the help of the &lt;Ctrl> and &lt;Shift> keys](images/95026546827_DV_resource.Stream@PNG-de-DE.png)

Only the same object categories are selected. In the example above this includes the subnets in addition to the corresponding devices because they were located within the virtual selection frame and belong to the same category as the devices. The subnets PN/IE_4 and PN/IE_5 were not located in the virtual selection frame and therefore are not part of the multiple selection.

### Copying a hardware component

You can copy hardware components in the device or network view. Copied hardware components are stored on a clipboard and can be pasted at another point from this clipboard. Copied stations are pasted as new stations in the network view. Copied devices and modules can be pasted into existing racks in the network and device view.

#### Rules

- Single objects as well as several objects can be copied at the same time.
- Modules inserted in the rack and in the area of unplugged modules can be copied.
- You can only copy devices and modules to free and valid slots in keeping with the slot rules.
- Racks with a CPU inserted cannot be copied individually, but only as complete units along with all inserted hardware components.

#### Procedure

Proceed as follows to copy a hardware component:

1. Select the hardware components you want to copy.

   - Device view: Select the module in a rack or put it in the area of unplugged modules.
   - Network or topology view: Select the station or the relevant hardware component from the network view.
   - Project tree: Select the station or module.
2. Select "Copy" from the shortcut menu or press &lt;Ctrl+C&gt;.

   If the "Copy" menu item is unavailable, your selection contains at least one component that cannot be copied.
3. Select the location at which the content of the clipboard is to be pasted.

   - In the device view select a free slot in the rack or area of unplugged modules.
   - In the network or topology view select a station where you want to insert devices or modules.
4. Select "Paste" from the shortcut menu or press &lt;Ctrl+V&gt;.

   - If you paste the copied object without selection in the network or topology view with &lt;Ctrl+V&gt;, the copied object is pasted to the right of the original object.
   - If you paste the copied object without selection in the network or topology view using the shortcut menu, it is placed at the location of the mouse pointer.

   If the "Paste" menu item is unavailable, the clipboard is empty or contains at least one component that cannot be pasted at this point.

The copied object is pasted at the chosen point.

If you have selected a station in the network or topology view to paste a module, the module is inserted into the first free and valid slot. If no free, valid slots are available, the object is inserted in the area of unplugged modules.

> **Note**
>
> You can also copy a module from one device to another:
>
> To do so, copy a module in the hardware and network editor, select a different device in the network or topology view or the drop down list of the device view and insert the module.
>
> You can insert the copied object directly in a slot or place it in the area of unplugged modules in the device view. If you add the copied object in the network view of a device or a station, it will be inserted in the first available slot.
>
> If there is no slot available for the object, it is automatically placed in the [area of unplugged modules](#device-view-area-for-unplugged-modules).

> **Note**
>
> You can use &lt;Ctrl&gt; and drag-and-drop to directly copy a selected hardware component.

---

**See also**

[Keyboard operation: Editing objects](#keyboard-operation-editing-objects)

### Moving a hardware component

You can move hardware components in the device or network view.

#### Rules

- You can move devices and modules from the rack and the area for unplugged modules taking the slot rules into consideration.
- CPs can be moved in the network view. The CP is plugged in a free and valid slot in the target device. If there are no free slots available, the CP to be inserted is moved to the area for unplugged modules.
- In the network view, CPU and slave head modules can be moved between the devices; depending on CPU type also within the rack.

> **Note**
>
> Moved CPs are disconnected from their network but keep their network parameters and address. If you reconnect the CP to the network and its address has been assigned, use a dialog to assign a new unique address to the CP.

#### Procedure

Proceed as follows to move a hardware component:

1. Select the hardware component you want to move.

   - Device view: Select the module in a rack or put it in the area of unplugged modules.
   - Network view: Select the hardware component of relevance to the network view.
2. Select "Cut" from the shortcut menu or press &lt;Ctrl+X&gt;.

   If the "Cut" menu item is unavailable, your selection contains at least one component that cannot be cut.
3. Select the location to which the cut object is to be moved.

   - Device view: Select a free slot in the rack or area of unplugged modules.
   - Network view: Select a station where you want to insert devices or modules.
4. Select "Paste" from the shortcut menu or press &lt;Ctrl+V&gt;.

   If the "Paste" menu item is unavailable, the clipboard is empty or contains at least one component that cannot be pasted at this point.

The selected hardware component is moved to the target. If the hardware component being moved is a networked object, it is disconnected from the network.

> **Note**
>
> You can use drag-and-drop to directly move a selected hardware component.

---

**See also**

[Keyboard operation: Editing objects](#keyboard-operation-editing-objects)

### Replacing a hardware component

You can replace hardware components such as racks, devices or different hardware modules with other components. This, for example, allows you to replace [unspecified CPUs](#adding-an-unspecified-cpu) with available CPUs from the hardware catalog.

#### Rules

You can only replace hardware components if they support module replacement and if the two components are compatible.

#### Procedure

To exchange hardware components with one another, proceed as follows:

1. Select the components you want to replace.
2. Open the shortcut menu:

   - If the "Replace device" entry is enabled, the module can be replaced.
   - If the "Replace device" entry is disabled, a module cannot be replaced.
3. Click on "Replace device" in the shortcut menu. The "Replace device" dialog box appears.
4. Under "New device" in the tree structure, select the module with which you want to replace your current module.
5. Click "OK".
6. Compile the hardware and software.

The existing hardware components are replaced by the new hardware components.

As an alternative, you can drag a hardware component from the hardware catalog directly to the component to be replaced. If the two components can be exchanged, this is indicated by the mouse pointer symbol.

---

**See also**

[Rack: Basics](#rack-basics)

### Renaming hardware component

You can conveniently edit the names of hardware components in all three views (network view, device view, topology view) directly in the graphic area as well as in the corresponding table areas or in the Inspector window.

#### Rules

You can rename the hardware components as follows:

- In the graphic view after selection of the displayed name.
- In the table view in the table cell with the name that is to be changed.
- In the Inspector window under "Properties &gt; General" for the selected hardware component.

#### Procedure

To rename a hardware component in the graphic area of a view, follow these steps:

For the device view:

1. Activate the display of the module names with the corresponding button in the toolbar.
2. Select the hardware component or its name.
3. You have two options:

   - Press &lt;F2&gt;.
   - Click on the previously selected name.
4. Edit the name.

![Procedure](images/96736362251_DV_resource.Stream@PNG-de-DE.png)

For the network and topology view:

1. Select the hardware component or its name.
2. You have three options:

   - Press &lt;F2&gt;.
   - Click on the previously selected name.
   - Select "Rename" from the shortcut menu.

   ![Procedure](images/96736371083_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/96736371083_DV_resource.Stream@PNG-de-DE.png)

For editing names in the table area, select the cell with the name you want to edit in the table. Then click on the name once again so that you can edit the names directly in the cell.

For editing names in the Inspector window, select the hardware component whose name you want to edit in the graphic area. The relevant parameters are then displayed in the Inspector window. Now you can edit the names under "Properties &gt; General".

---

**See also**

[Network view](#network-view)
  
[Device view](#device-view)
  
[Topology view](#topology-view)
  
[Inspector window](#inspector-window)

### Deleting a hardware component

There are various ways of deleting hardware components. Deleted hardware components are removed from the system and assigned addresses made available again.

#### Rules

- CPUs or modules from the rack and from the area of unplugged modules can be deleted.
- When a rack is deleted in the device view, the plugged hardware components are moved to the area of unplugged modules.

#### Procedure

Proceed as follows to delete a hardware component:

1. Select the hardware components you want to delete.

   - Network view: Select devices or network relevant hardware components in the graphic view or in the network view.
   - Device view: In the graphic view or device overview, select racks or modules in racks or in the area of unplugged components.
   - Topology view: Select devices or hardware components with Ethernet interfaces in the graphic view or in the topology view.
   - Project tree: Select devices or individual hardware components from the tree structure.
2. Select "Delete" from the shortcut menu or press &lt;Del&gt;.

   If the "Delete" menu item is unavailable, your selection contains at least one component that cannot be deleted.

The selected hardware components are deleted.

> **Note**
>
> Deleting hardware components may result in inconsistencies in the project, such as violation of slot rules. Inconsistencies are reported during the consistency check. Correct the inconsistencies by taking appropriate action, for example, ensuring compliance with the slot rules.

---

**See also**

[Keyboard operation: Editing objects](#keyboard-operation-editing-objects)

### Changing or updating hardware components

#### Explanation of terms

You can update the firmware version of a hardware component to a new version (in as far as available) or possibly use new functions of the hardware components by updating the module description.

The terms "Module description" and "Firmware version" are explained in more detail in the following section.

- Module description: The specific version of the configuration software from which the technical description of the module stems.

  Example: V11.0.0.0
- Firmware version: The version of the firmware of the module whose parameters are assigned offline

  Example: V2.0

#### Requirement

- You have created a device configuration.
- You have installed an update or an optional package at a later date. As a result of this installation, the module description of at least one module type was updated in the hardware catalog, whereby the new version of the module description is incompatible with the previous version.
- You have used such modules in your device configuration and want to use the modified or added properties.

#### Procedure

Perform the following step for each affected module type.

1. Select the affected module in the device view.
2. In the Inspector window, go to "Properties &gt; General &gt; Catalog Information". Click the "Update module description" button there.
3. In the query that then appears, specify whether you want to update the module description only for the selected module or for all modules of this type in the current project.

#### Result

The selected modules are replaced by the same modules with updated module description in the current project.

#### In which cases is it unnecessary to update the module description?

An updating of the module description is not necessary in the following cases:

- You do not want to use the modified or added properties of the modules.
- You open an existing project that was created in version V13 SPx with a more recent version of the configuration software. The system carries out an automatic project conversion. In this case, all older module descriptions are automatically adapted.

### Editing properties and parameters

Once you have inserted hardware components in your rack, you can edit their default properties, such as names, parameters or addresses, in the network view, device view or topology view.

#### Requirement

You are in the network view, device view or topology view.

> **Note**
>
> You can edit the relevant properties and parameters in the different views in the graphic view as well as in the table view. It depends on the view which parameters you can edit. In the graphic network view, you have access to the network-related hardware components and the station. You can access modules and hardware components not displayed in the graphic network view using the table network view. In the topology view and in the device view, you have access to additional parameters regarding the topology or device access.

#### Procedure

To change the properties and parameters of the hardware components in the device view, follow these steps:

1. In the graphic view, select the CPU, module, rack or interface you want to edit.
2. Edit the settings for the selected object:

   - In the graphic area you can, for example, change the object names with activated module labeling.
   - Use the table area to edit addresses and names, for example.
   - In the Inspector window additional setting possibilities are available in "Properties".

Note that modules can only be fully parameterized if they are assigned to a CPU. Therefore, PROFIBUS or PROFINET interfaces modules must first be networked with the CPU or a centrally inserted communication module so that they form a master system or IO system. Only then is it possible, for example, to edit the addresses of the distributed components that are inserted.

#### Example of changing settings

![Example of changing settings](images/61144539147_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Selection of a module |
| ② | Editing option for addresses in the device overview |
| ③ | Selection options in the inspector window |
| ④ | Editing option for addresses in the inspector window |

---

**See also**

[Inspector window](#inspector-window)

### Input and output addresses in the address overview

#### Introduction

The currently used input and output addresses can be displayed in the address overview in a table form. The address overview can be found in the Inspector window under "Properties" of the CPU.

#### Design of the address overview

With the different check boxes, you can set which objects should be displayed in the address overview:

- Inputs: Display of the input addresses
- Outputs: Display of the output addresses
- Address gaps: Display of open address spaces
- Slot: Display of the slot number

The following information is typically shown in the address overview:

| Table header | Meaning |
| --- | --- |
| Type | Type of the address range. Indicates whether the area is an input address area or an output address area.  - I = input address of module with input I/O address space (with length &gt; 0) - I* = input or diagnostics address of modules without input I/O address space (with length = 0) No data (signal statuses or measured values) is exchanged via these addresses in the user program. Used for reporting diagnostics events of the operating system (e.g. in the start information of error OBs). - Q = output address |
| Addr. from | Start address of the address range. Indicates the first assigned address of the input or output. |
| Addr. to | End address in the address range. Indicates the last assigned address of the input or output. |
| Size | Address length of the address range occupied by the module for the input or output.   Examples:  - With a start address of 0 and an end address of 1, the address length is 2 bytes. - With a start address of 0 and an end address of 3, the address length is 4 bytes. - With a start address of 0.1 and an end address of 0.2, the address length is 2 bits. - If the start address and end address are identical, 0 bytes is displayed. |
| Module | Module using the address area. |
| Rack | Number of the rack on which the hardware component is inserted. |
| Slot | Number of the slot in the rack in which the hardware component is inserted. |
| Device name | Name and type of device in which the module is inserted.   Examples:  - The module is inserted in a PLC with the name "PLC_1" of the type CPU 1516-3 PN/DP, "PLC_1 [CPU 1516-3]" is displayed. - The module is inserted in a head module with the name "IO Device_1" of the type IM 151-3 PN; "IO Device_1 [IM 151-3 PN]" is displayed |
| Device number | PROFINET device number or PROFIBUS address if the module is connected to a PLC via PROFINET or PROFIBUS. If the module is inserted directly in a PLC, "-" is displayed.  Examples:  - The module is inserted in a head module that is connected to a PLC via a PROFINET interface; the device number of the Ethernet address is displayed. - The module is inserted in a DP slave that is connected to a PLC via a PROFIBUS interface, the address parameter of the PROFIBUS address is displayed. |
| Master I/O system | Name of the DP master system or IO system via which the DP slave or IO device is connected to the PLC. The corresponding number of the DP master system or IO system is displayed in square brackets. If the module is inserted directly in a PLC, "-" is displayed.  Examples:  - The module is inserted in an IO device and is connected to a PLC via a PROFINET IO system with the name "PROFINET IO-System_1" and the number 100. "PROFINET IO-System_1 [100]" is displayed. - The module is inserted in a DP slave and is connected to a PLC via a PROFIBUS DP master system with the name "DP-Mastersystem" and the number 1. "DP-Mastersystem [1]" is displayed. |
| OB | Organization block that is assigned to the process image. The "Main" cycle OB always refers to the automatic update of the process image.   This column is not available for every CPU. |
| PIP | Process image partition. Indicates whether the address is updated automatically via the cyclic process image or is located in a process image partition that must be triggered explicitly for an update.   Refer to the further description of the "Process image partition PIP2" below. |

#### Process image partition PIP

The "PIP" table column shows the assignment of the address to the cyclic process image or to a process image partition (PIP).

For S7-300/400:

- "OB1-PA": The address is assigned to the cyclic process image. The operating system updates this address automatically in each program cycle.
- "PIP x": The address is assigned to the process image partition x (for example PIP 1, no cyclic process image). The operating system updates this PIP when the assigned OB is executed. If this PIP is not assigned to an OB, the operating system does not update this PIP. You have the option to update the PIP yourself with the instructions "UPDAT_PI" and "UPDAT_PO" (for S7-400 and some S7-300 CPUs).

For S7-1200:

- "Automatic update": The address is assigned to the cyclic process image (PIP 0). The operating system updates this address automatically in each program cycle.
- "None": The address not assigned to any process image partition. You access this address directly in the user program (direct I/O access, no process image).
- "PIP x": The operating system updates this PIP when the assigned OB is executed. If this PIP is not assigned to an OB, the operating system does not update this PIP. You have the option to read inputs or write outputs in the user program via direct I/O access. The instructions "UPDAT_PI", "UPDAT_PO", "SYNC_PI" and "SYNC_PO" are not supported for S7-1200.
- "PIP OB servo": The process image partition "PIP OB Servo" is not assigned to an organization block (fixed setting for organization block: "---(None)"). The operating system does not update this PIP or any of the addresses contained in it: You access the addresses directly in the user program (direct I/O access).

For S7-1500:

- "Automatic update": The address is assigned to the cyclic process image (PIP 0). The operating system updates this address automatically in each program cycle.
- "None": The address not assigned to any process image partition. You access this address directly in the user program (direct I/O access, no process image).
- "PIP x" (PIP 1 to PIP 31): The operating system updates PIP x when the assigned OB is executed. If this PIP is not assigned to an OB, the operating system does not update PIP x. You have the option to update the PIP x in the user program with the instructions "UPDAT_PI" and "UPDAT_PO". If PIP x is assigned to an isochronous mode interrupt OB (OB 61 to OB 64), the operating system does not update PIP x. You have the option to update PIP x in your user program with the instructions "SYNC_PI" and "SYNC_PO".
- "PIP OB servo": The process image partition "PIP OB servo" is permanently assigned to the OB "MC-Servo". STEP 7 generates this OB automatically when you create a technology object in the Motion Control area. When the OB is executed, the PIP OB Servo is updated isochronously. All drives and encoders used by Motion Control are assigned to this process image partition.

---

**See also**

[Specifying input and output addresses (S7-1200)](Configuring%20automation%20systems.md#specifying-input-and-output-addresses-s7-1200)

### Distributed I/O in the project tree

Distributed I/O devices in the project tree shown in separate folders. Depending on whether a device was assigned to a PROFINET IO system, a DP master system or no system, the device is displayed as a node or link to the device in one of the folders described below.

#### "Ungrouped devices" folder in the project

All distributed I/O devices in the project are collected in the "Ungrouped devices" folder.

The icons of the folders and links show the status "assigned" with colored identifiers: PROFINET IO devices are marked green, PROFIBUS DP slaves are marked magenta, other distributed I/O devices are not marked.

The icons of the folders and links show the status "not assigned" with question marks.

!["Ungrouped devices" folder in the project](images/82512081419_DV_resource.Stream@PNG-en-US.png)

If you have established a connection to an IO device or a DP slave with the "Go online" function, the same diagnostics information (e.g. green check mark) is displayed for the link of a device as for the device itself in the project navigation. For more information, refer to the section "View in the online mode".

It is possible to copy or move distributed I/O devices from the "Ungrouped devices" folder, but not the folder itself, to another position in the project tree. Possible destinations are the project folder or device folder. You can also copy or move distributed I/O devices back to the "Ungrouped devices" folder.

By double-clicking on the link, you go to the device view and can configure the distributed I/O device.

#### "Unassigned devices" folder in the project

Devices that are not assigned to a distributed I/O system appear as links in the "Unassigned devices" folder.

The icon for the folder and the link of the respective device in the project tree indicate with a question mark that they are not connected to a distributed I/O system. The link is marked by a small arrow.

!["Unassigned devices" folder in the project](images/82501563915_DV_resource.Stream@PNG-en-US.png)

The display of the project tree as a link allows IO devices or DP slaves to be selected individually, for example to select the destination of the link. It remains possible to select device groups.

By double-clicking on the link, you go to the device view and can configure the distributed I/O device.

#### "Distributed I/O" folder under a device

If you assign an IO device to a PROFINET IO system, this is displayed as a link below the node "Distributed I/O &gt; PROFINET IO system".

Accordingly, a DP slave that is assigned to a DP master system is shown as a link below the node "Distributed I/O &gt; DP master system".

The link references the corresponding IO device or the DP slave in the project tree.

The icon for the node and the link of the respective device in the project tree indicate whether the device is connected via PROFINET (green) or via PROFIBUS (magenta). The link is marked by a small arrow.

!["Distributed I/O" folder under a device](images/82501555211_DV_resource.Stream@PNG-en-US.png)

Gateways are shown as a link below the DP master/IO node to which they were assigned.

By double-clicking on the link, you go to the device view and can configure the distributed I/O device.

## Configure networks

This section contains information on the following topics:

- [Networking devices](#networking-devices)
- [Communication via connections](#communication-via-connections)
- [Displaying and configuring topology](#displaying-and-configuring-topology)
- [Secure Communication (S7-1200, S7-1500, S7-1500T)](#secure-communication-s7-1200-s7-1500-s7-1500t)
- [Industrial Ethernet Security](Industrial%20Ethernet%20Security.md#industrial-ethernet-security)

### Networking devices

This section contains information on the following topics:

- [Communication and networks](#communication-and-networks)
- [Networking devices in the network view](#networking-devices-in-the-network-view)
- [Tabular network overview](#tabular-network-overview)
- [Networking devices in the device view](#networking-devices-in-the-device-view)
- [Checking or changing network parameters and interface parameters](#checking-or-changing-network-parameters-and-interface-parameters)
- [Changing networkings](#changing-networkings)
- [Copying, cutting or deleting subnets](#copying-cutting-or-deleting-subnets)
- [Configuring PROFINET/Industrial Ethernet networks](#configuring-profinetindustrial-ethernet-networks)
- [PROFIBUS network configuration](#profibus-network-configuration)
- [MPI network configuration (S7-300, S7-400, PC)](#mpi-network-configuration-s7-300-s7-400-pc)
- [Assigning addresses via DHCP (S7-1500)](#assigning-addresses-via-dhcp-s7-1500)

#### Communication and networks

##### Communication between devices

The basis of all types of communication is always a previously configured network. You use the network configuration to organize the required accessibility of the various network nodes for communication. The following requirements apply for the message exchange in the S7 network:

- Assignment of unique S7 topological addresses to all nodes of the network
- Ensure the connection of the interfaces via physical line sections
- Communication of the devices with consistent transmission properties

##### Definition

Via the network, the various computers and end devices (PC, PG, PLC, AS) are connected together with interface modules, physical cables and suitable software. Networked devices can exchange data with each other. Networking can be implemented via wiring or a wireless network, e.g. via WLAN.

The different forms of the wiring result in different S7 subnets from the perspective of the network. An S7 subnet is part of the overall S7 network. The parameters of the nodes of an S7 subnet (e.g. for PROFIBUS) must be uniform with respect to the physical wiring. A physical S7 subnet includes the bus components and all connected devices. S7 subnets on different physical wiring can be coupled to gateways or routers in the S7 network.

##### Network configuration

The following steps are required to configure the S7 network:

- Connect devices to an S7 subnet
- Set properties/parameters for each S7 subnet
- Specify the node properties for each networked module (e.g. unique S7 topological address)
- Load the configuration data into the devices to provide interfaces with the settings resulting from the S7 network configuration
- Document S7 network configuration

Creation and configuration of an S7 subnet is supported by the connection configuration for Open User Communication, .

##### Relation between network configuration and project

S7 subnets are managed with their properties within a project. Properties essentially result from adjustable S7 network parameters and from the number and communication characteristics of the connected nodes.

The devices to be networked must be in the same project.

##### S7 subnet name and S7 subnet ID

S7 subnets are uniquely identified within the project by an S7 subnet name and an S7 subnet ID. The S7 subnet ID is stored in all components with networkable interfaces. Components can then be clearly assigned to an S7 subnet even after uploading into a project.

S7 subnets are available in two possible versions:

- Physical Ethernet Wiring ("Green Line")
- Physical PROFIBUS connection ("violet line")

##### Networking options

In the project, you can create and network devices with components capable of communication. The following basic options are available for networking the devices:

- You link the interfaces of the components capable of communication with one another. This creates a new S7 subnet that matches the interface type.
- You connect the interface of the communication-capable devices to a new or an existing S7 subnet.
- You create an Open User Communication connection. An S7 subnet is automatically created between the communication partners through the connection configuration of the Open User Communication.
- You use the graphic connection configuration to configure connections; missing networks are hereby recognized and are created either automatically or via dialog.

Due to different tasks of the devices or due to the expansion of the system, it may be necessary to operate several S7 subnets. These S7 subnets are managed in a project.

#### Networking devices in the network view

##### Options

In the graphic network view, you have an overview of the subnets of the entire system in the project. You can use the tabular network overview for additional support.

Depending on the starting situation, there are various ways of undertaking configuration to network the interface for a component capable of communication. The procedures are described in the following section:

- Creating an individual subnet
- Creating several subnets at one time
- Connecting two target devices via a new subnet
- Connecting devices to existing subnet
- Selecting an existing subnet from a list
- Automatic networking during the configuration of the connection;

  See also: [Creating a new connection - overview](Configuring%20connections.md#creating-a-new-connection---overview)

Possible starting situations are:

- A suitable subnet is not yet available.
- The subnet with which you want to connect the component already exists.

##### Procedure - creating a single subnet

To create a subnet and to connect it to an interface, proceed as follows:

1. Select the interface of a CPU / a CP.
2. Select the "Create subnet" command in the shortcut menu of the interface.

The selected interface is connected to a new subnet. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

The following schematic shows an interface with outgoing line connecting to a subnet:

![Procedure - creating a single subnet](images/12958023819_DV_resource.Stream@PNG-de-DE.png)

##### Procedure - creating several subnets at one time

To create several subnets at one time, proceed as follows:

1. Select several interfaces by clicking on them while pressing the &lt;Ctrl&gt; button.
2. Select the "Create subnet" command in the shortcut menu of the interface.

Each selected interface is connected to a new subnet. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

The following figure shows multiple subnets created by selecting multiple interfaces:

![Procedure - creating several subnets at one time](images/12958337163_DV_resource.Stream@PNG-de-DE.png)

##### Procedure – Connecting two target devices via a new subnet

To connect an interface with another device via a subnet that does not yet exist, proceed as follows:

1. Position the mouse pointer over the interface for a component capable of communication requiring networking.
2. Click with the left mouse button and hold the button down.
3. Move the mouse pointer.

   The pointer now uses the networking symbol to indicate "Networking" mode. At the same time, the mouse pointer shows the lock symbol that will only disappear when the pointer is on a valid target.

   ![Procedure – Connecting two target devices via a new subnet](images/12958282891_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure – Connecting two target devices via a new subnet](images/12958282891_DV_resource.Stream@PNG-de-DE.png)
4. Now move the pointer in networking mode onto the interface of the target device. You can either keep the mouse button pressed or release it.
5. Now release the left mouse button or press it again (depending on your previous action).

> **Note**
>
> If you want to exit networking mode beforehand, press &lt;Esc&gt;, right-click or double-click in the background of the network view.

A new subnet is created. The interfaces are now connected via the new subnet. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

The following schematic shows two networked devices:

![Procedure – Connecting two target devices via a new subnet](images/12958185355_DV_resource.Stream@PNG-de-DE.png)

##### Procedure - Connecting devices to existing subnet

To connect an interface to an existing subnet, proceed as follows:

1. Position the mouse pointer on the interface of a communications-compliant component you want to network or on the existing subnet.
2. Click with the left mouse button and hold the button down.
3. Move the mouse pointer.

   The pointer now uses the networking symbol to indicate "Networking" mode. At the same time, the mouse pointer shows the lock symbol that will only disappear once the pointer is moved to a valid target.
4. Now move the mouse pointer to the existing subnet or to the interface to be networked. You can either keep the mouse button pressed or release it.

   ![Procedure - Connecting devices to existing subnet](images/12958290827_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - Connecting devices to existing subnet](images/12958290827_DV_resource.Stream@PNG-de-DE.png)
5. Now release the left mouse button or press it again.  
   If you want to exit networking mode beforehand, press &lt;Esc&gt; or right-click.

Result:

The interface and selected subnet are now connected. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

##### Procedure - selecting an existing subnet from a list

To link an interface with a subnet that has already been created, proceed as follows:

1. Select the interface of a CPU.
2. Select the "Assign to new subnet" command in the shortcut menu of the interface.

   A list box containing the available subnets appears.
3. Select a subnet from the list.

The interface and selected subnet are now connected. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

#### Tabular network overview

##### Table area of network view

The table area of the network view consists of several tables:

- Network overview: The table for the network overview supplements the graphical network view with the following functions:

  - You obtain detailed information on the structure and parameter settings of the devices.
  - Using the "Subnet" column, you can connect components capable of communication with created subnets.
- Connections: Communication connections are displayed in this table. Some aspects of the connections displayed here can be edited directly in the table. Selected connections are displayed in the Inspector window and can be edited there.
- Relations: Logical connections of the HMI client-server relation are displayed here.
- I/O communication: Device communication via PROFIBUS DP and PROFINET IO is configured and displayed in this table. In the I/O communication table, only those interfaces of a device are displayed that can be used for communication via PROFIBUS DP or PROFINET IO.
- VPN: Properties of the VPN user groups and their assigned security modules are displayed here.

##### Basic functions for tables

The network overview supports the following basic functions for editing a table:

- Displaying and hiding table columns

  Note: The columns relevant for configuration cannot be hidden.
- Optimizing column width
- Sorting table
- Displaying the meaning of a column, a row or cell using tooltips.

#### Networking devices in the device view

##### Networking in the device view

In the device view, you can check and set all the parameters of the components belonging to a device and the interfaces in detail. Here you can also assign the interfaces to the subnets created in the project.

##### Requirements

- The subnet with which you want to connect an interface has already been created.
- If the subnet has not yet been created, change to the network view and perform the networking.

##### Procedure - connecting to an existing subnet

To connect an interface to an existing subnet, proceed in the device view as follows:

1. Select the entire communications-compliant component or the interface to be networked.  
   The properties of the selected interface or component are displayed in the Inspector window.
2. In the Inspector window, select the parameter group for the selected interface; for example, the "Ethernet addresses" parameter group for a PROFINET interface.
3. Select the subnet to be connected from the "Interface connected with" drop-down list.

The interface and selected subnet are now connected. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

##### Procedure - creating a new subnet

To create a subnet and to connect it to the interface, proceed as follows in the device view:

1. Select the entire communications-compliant component or the interface to be networked.  
   The properties of the selected interface or component are displayed in the Inspector window.
2. In the Inspector window, select the parameter group belonging to the selected interface, for example, the "Ethernet addresses" parameter group for a PROFINET interface.
3. In "Interface connected with", click the "Add new subnet" button.

The interface is connected to a new subnet of the appropriate subnet type. The inconsistencies possibly resulting from the modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

#### Checking or changing network parameters and interface parameters

##### Introduction

Communication between networked devices requires the following parameters to be configured:

- Network parameters

  Network parameters identify the network within the system configuration, for example, using a name.
- Interface parameters

  Interface parameters define specific properties of a component capable of communication. Addresses and transmission characteristics are set automatically and are consistent with the network parameters.

  > **Note**
  >
  > Network parameters and interface parameters are usually set during networking such that communication can take place for numerous applications without the parameters having to be changed. The inconsistencies possibly resulting from a modified configuration are clarified automatically or per query. In the case of consistency problems, the next free address is preferably used.

##### Procedure - checking or changing network parameters

Proceed as follows to check or change network parameters:

1. Enter the network view.
2. Select the subnet from the network view.

   You can see the network parameters in the "Properties" tab in the inspector window.
3. If necessary, check or modify the network parameters in the relevant group of parameters.

##### Procedure - checking or changing interface parameters

You can check and modify interface parameters in the network and device view.

Proceed as follows to check or change interface parameters:

1. Enter the network view or device view.
2. Select the interface.

   You can see the interface parameters in the "Properties" tab in the inspector window.
3. If necessary, check or modify the interface parameters in the relevant group of parameters.

##### Procedure - checking or changing interface addresses

You can edit the MPI, PROFIBUS and Ethernet addresses in the graphical network view itself.

Proceed as follows to edit MPI, PROFIBUS and Ethernet addresses in the network view:

1. Enable the display of interface addresses in the network view.
2. Select an MPI, PROFIBUS or Ethernet address to be edited.
3. Click on the selected address field or press [F2] to edit the address in the network view.

#### Changing networkings

##### Introduction

You can cancel an interface's network connection or assign it to another subnet of the same subnet type.

##### Consequences

Depending on the version, a distinction should be made between:

- Canceling a network connection for an interface

  The configured parameters for the interface remain unchanged.
- Assigning a network connection to another subnet

  If the addresses in the assigned subnet are not unique, in other words, they already exist, they will be changed automatically to make them unique.

##### Procedure - disconnecting from a network

Proceed as follows to cancel the network connection for an interface:

1. Select the networked interface.

   ![Procedure - disconnecting from a network](images/13006470155_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure - disconnecting from a network](images/13006470155_DV_resource.Stream@PNG-de-DE.png)
2. Select the "Disconnect from subnet" command in the shortcut menu of the interface.

The network connection is deleted, the interface addresses are, however, not changed.

Configured connections are retained; however these connections are marked red in the connection table because they are not networked. Specified connections remain specified.

---

**See also**

[Networking devices in the network view](#networking-devices-in-the-network-view)

#### Copying, cutting or deleting subnets

##### Introduction

You can copy subnets as individual objects or copy them along with networked devices or other networks.

For example, you can create complex configurations to be used more than once in different variants within the project with no additional effort.

##### Effects on the copied subnet

Properties that have to be assigned explicitly within a project are re-assigned appropriately when the copied objects are copied.

For subnets, this means: The subnet ID and name are re-assigned to the copied subnet.

The configured properties are adopted in the copied subnet.

##### Procedure - copying a subnet

Proceed as follows to copy one or more subnets:

1. Select one or more subnets.
2. In the shortcut menu, select the "Copy" command.
3. Select the "Paste" command in the shortcut menu.

The copied subnets are shown as "orphaned" subnets in the top part of the network view.

![Procedure - copying a subnet](images/12957973259_DV_resource.Stream@PNG-de-DE.png)

##### Procedure - copying a subnet with connected devices

To copy one or more subnets with networked devices, proceed as follows:

1. Select one or more subnets with the connected devices, for example by drawing a lasso around them.
2. In the shortcut menu, select the "Copy" command.
3. Select the "Paste" command in the shortcut menu.

Complete copies of the subnets and connected devices are created.

Configured connections are adopted and remain within the copied devices. Connections to devices that have not been copied are interrupted and become unspecified.

#### Configuring PROFINET/Industrial Ethernet networks

This section contains information on the following topics:

- [Useful information on configuring PROFINET/Industrial Ethernet](#useful-information-on-configuring-profinetindustrial-ethernet)
- [Settings for interconnecting Ethernet devices](#settings-for-interconnecting-ethernet-devices)
- [IP forwarding](#ip-forwarding)
- [Virtual interface for IP-based applications](#virtual-interface-for-ip-based-applications)

##### Useful information on configuring PROFINET/Industrial Ethernet

###### Rules for the network configuration

The Ethernet interfaces of the devices have a default IP address that you can change.

###### IP address

The IP parameters are visible if the module capable of communication supports the TCP/IP protocol. This is usually the case for all Ethernet modules.

The IP address consists of 4 decimal figures in the range of 0 to 255. The decimal figures are separated from one another by a dot.

Example: 140.80.0.2

The IP address consists of:

- Address of IP subnet
- Address of the device (generally also called host or network node)

###### Subnet mask

The subnet mask splits these two addresses. It determines which part of the IP address addresses the network and which part of the IP address addresses the device.

The set bits of the subnet mask determine the network part of the IP address.

Example:

Subnet mask: 255.255.0.0 = 11111111.11111111.00000000.00000000

In the example given for the above IP address, the subnet mask shown here has the following meaning:

The first 2 bytes of the IP address identify the subnet - i.e. 140.80. The last two bytes address the device, i.e. 0.2.

It is generally true that:

- The network address results from AND logic operation of the IP address and subnet mask.
- The device address results from the AND NOT logic operation of the IP address and subnet mask.

###### Relation between IP address and default subnet mask

An agreement exists relating to the assignment of IP address ranges and so-called "Default subnet masks". The first decimal number (from the left) in the IP address determines the structure of the default subnet mask. It determines the number of "1" values (binary) as follows:

| IP address (decimal) | IP address (binary) | Address class | Default subnet mask |
| --- | --- | --- | --- |
| 0 to 126 | 0xxxxxxx.xxxxxxxx.... | A | 255.0.0.0 |
| 128 to 191 | 10xxxxxx.xxxxxxxx... | B | 255.255.0.0 |
| 192 to 223 | 110xxxxx.xxxxxxxx... | C | 255.255.255.0 |

> **Note**
>
> **Range of values for the first decimal point**
>
> A value of between 224 and 255 is also possible for the first decimal number of the IP address (address class D, etc). This is not recommended, however, because there is no address check for these values.

###### Masking other subnets

You can use the subnet mask to add further structures and form "private" subnets for a subnet that is assigned one of the address classes A, B or C. This is done by setting other lower points of the subnet mask to "1". For each bit set to "1", the number of "private" networks doubles and the number of devices they contain is halved. Externally, the network functions like an individual network as it did previously.

Example:

You have a subnet of address class B (for example IP address 129.80.xxx.xxx) and change the default subnet mask as follows:

| Masks | Decimal | Binary |
| --- | --- | --- |
| Default subnet mask | 255.255.0.0 | 11111111.11111111.00000000.00000000 |
| Subnet mask | 255.255.128.0 | 11111111.11111111.10000000.00000000 |

Result:

All devices with addresses between 129.80.001.xxx and 129.80.127.xxx are on one IP subnet, all devices with addresses between 129.80.128.xxx and 129.80.255.xxx are on another IP subnet.

###### Router

The task of the routers is to connect the IP subnets. If an IP datagram is to be sent to another network, it first has to be conveyed to a router. To make this possible, you have to enter the address of the router for each device in the IP subnet.

The IP address of a device in the subnet and the IP address of the router can only differ at the points at which there is a "0" in the subnet mask.

---

**See also**

[Settings for interconnecting Ethernet devices](#settings-for-interconnecting-ethernet-devices)
  
[Virtual interface for IP-based applications](#virtual-interface-for-ip-based-applications)
  
[IP forwarding](#ip-forwarding)

##### Settings for interconnecting Ethernet devices

The following paragraph describes the behavior of STEP 7 during interconnection of PROFINET devices and the effects of the port interconnection on the network view.

###### Relation between port interconnection and network view

**Topology view**

In the topology view, you specify the physical interconnection of Ethernet ports. You specifically determine which Ethernet port of a device is to be connected with a specific Ethernet port of another device by means of an Ethernet cable (preset topology).

Example:

You specify that port 1 of the PROFINET interface of the CPU is to be connected to port 2 of the PROFINET interface of device A by means of an Ethernet cable. You also specify the interface for devices with several PROFINET interfaces.

Example:

You specify that port 1 of PROFINET interface X2 of the CPU is to be connected to port 2 of the PROFINET interface of device A by means of an Ethernet cable. The Ethernet ports can be interconnected in a table or graphically.

**Network view**

In the network view, you specify which devices are to be connected with each other via an Ethernet subnet. You do not specify the Ethernet ports by which the devices are interconnected with each other (that is the task of the port interconnection).

The port interconnection has effects on the network view: When you interconnect Ethernet ports of devices with each other in the topology view, STEP 7 connects the interconnected PROFINET interfaces of the devices in the network view with an Ethernet subnet (green line). However, the course of the green line does not reflect the actual cable routing. You specify the actual wiring in the topology view.

An Ethernet subnet always has a name and an S7 subnet ID. You can set these two values in the subnet properties.

###### Which Ethernet subnet is used to link interconnected devices?

STEP 7 distinguishes between the following cases:

- Ethernet subnet specified (default subnet).
- No Ethernet subnet specified (no default subnet).

###### Ethernet subnet specified (default subnet)

The option "Connect devices that are not linked with this subnet in case of port connection" is activated in the properties of an Ethernet subnet (default). This option can be activated for exactly one Ethernet subnet. Activate the option, if necessary, for the Ethernet subnet that is to be continued when interconnecting devices that are not linked. This subnet is referred to as "default subnet" below.

Response of STEP 7:

When you interconnect the ports of two devices that are not linked in the topology view, STEP 7 links these devices with the default subnet.

**Example**:

Step 1: Create a subnet in the network view at PLC_4, "Connect devices that are not linked with this subnet in case of port connection" option is **enabled**.

![Ethernet subnet specified (default subnet)](images/61272766859_DV_resource.Stream@PNG-de-DE.png)

Step 2: Interconnect PLC_1 with PLC_2 (topology view).

![Ethernet subnet specified (default subnet)](images/61272759435_DV_resource.Stream@PNG-de-DE.png)

**Result**: All PLCs are now connected to the same default subnet (network view).

![Ethernet subnet specified (default subnet)](images/61273101707_DV_resource.Stream@PNG-de-DE.png)

###### No Ethernet subnet specified (no default subnet).

This is the case when the following conditions are fulfilled:

- A subnet has been added to a PROFINET interface (this interface is referred to as "Interface A" below).
- The option "Connect devices that are not linked with this subnet in case of port connection" is deactivated in the properties of this subnet (no default subnet).
- There is no other Ethernet subnet for which this option is activated.

Response of STEP 7:

- The Ethernet subnet of interface A is only continued when you interconnect a port of interface A with a port of another device.
- When you interconnect ports of other devices that are not linked with each other, STEP 7 creates a new Ethernet subnet.

**Example**:

Step 1: Create a subnet in the network view at PLC_4, "Connect devices that are not linked with this subnet in case of port connection" option is **disabled**.

![No Ethernet subnet specified (no default subnet).](images/61273094283_DV_resource.Stream@PNG-de-DE.png)

Step 2: Interconnect PLC_1 with PLC_2 (topology view).

![No Ethernet subnet specified (no default subnet).](images/61273185931_DV_resource.Stream@PNG-de-DE.png)

**Result**: PLC_1 and PLC_2 are connected to a new subnet (network view).

![No Ethernet subnet specified (no default subnet).](images/61273193355_DV_resource.Stream@PNG-de-DE.png)

###### Manual adaptation of the IP addresses

It can occur that STEP 7 does not adapt the IP addresses of the interconnected devices in such a way that the resulting network can be correctly compiled, for example, for devices with multiple PROFINET interfaces. In these situations, you need to adapt the IP addresses of the devices manually.

The following rules apply:

- Devices that are to communicate with each other without a router cannot belong to different IP subnets.
- For devices with multiple PROFINET interfaces, the interfaces must be in different IP subnets.

To change the IP address of a PROFINET interface, perform the following steps:

1. Change to the network view (if not selected already).
2. Left-click on the icon of the PROFINET interface that is not to be part of the IP subnet.
3. Change the subnet part of the IP address in the properties of the PROFINET interface (in the "Ethernet addresses" area).

**Example: Manual conversion of the IP subnet part for devices with multiple PROFINET interfaces in a subnet**

The IP address is: "192.168.0.1".

The subnet mask is "255.255.255.0".

The first three numbers "192.168.0" form the IP subnet part of the IP address "192.168.0.1".

Change the IP subnet part, for example, to "192.168.1"

---

**See also**

[Interconnecting ports in the graphic view](#interconnecting-ports-in-the-graphic-view)
  
[Interconnecting ports in the table view](#interconnecting-ports-in-the-table-view)
  
[Useful information on configuring PROFINET/Industrial Ethernet](#useful-information-on-configuring-profinetindustrial-ethernet)
  
[Virtual interface for IP-based applications](#virtual-interface-for-ip-based-applications)
  
[IP forwarding](#ip-forwarding)

##### IP forwarding

###### Forwarding of IP packets with IP forwarding

IP forwarding is a function of devices to forward IP packets between two connected IP subnets.

Enable/disable the IP forwarding function in STEP 7. When IP forwarding is enabled, the S7‑1500 CPU forwards received IP packets not addressed to the CPU to locally connected IP subnets or to a configured router.

The following figure shows how a programming device accesses data of an HMI device. Programming device and HMI device are located in different IP subnets. The IP subnets are connected to the two interfaces X1 and X2 of the CPU.

![Access of a programming device to an HMI via IP forwarding](images/127426279307_DV_resource.Stream@PNG-en-US.png)

Access of a programming device to an HMI via IP forwarding

###### Areas of application

- Easy access from the control level to the field level for configuration and parameter assignment of field devices, e.g. via PDM or web browser
- Simplified integration of devices for remote access, e.g. for diagnostics during remote maintenance or firmware update

###### Requirements for using IP forwarding

- S7‑1500 CPU as of firmware version V2.8
- Number of Ethernet interfaces:

  - The CPU has at least two Ethernet interfaces.
  - Or the CPU has one Ethernet interface, and a CP 1543-1 as of firmware version V2.2 provides the other Ethernet interface. In this case, the "Access to PLC via communication module" function must be enabled for the CP in the CPU.
- IP forwarding is enabled.
- Suitable standard gateways/routes are configured in each participating device along the outgoing and return paths of the IP packets.

###### IP route table

When IP forwarding is enabled, the CPU forwards received IP packets that are not addressed to itself. How the CPU forwards the IP packets is defined in its internal IP route table.

The CPU automatically creates the IP route table from the following information of the loaded hardware configuration:

- IP configuration of the Ethernet interfaces
- Configured router

###### Example of a configuration with IP forwarding

The following figure shows a sample configuration along with the required IP address settings and router settings.

- A PC on the IP subnet 192.168.4.0 communicates with an HMI device on the IP subnet 192.168.2.0.
- The IP address of a router ("Standard Gateway") is configured at the CPU, Ethernet interface X3; in the figure below it is the device that is designated as "IP Router".  
  In STEP 7, you configure a router in the interface properties under "Ethernet Addresses" &gt; "IP Protocol".
- For the PC, the IP router, the IO device and the HMI device, the IP addresses of a standard gateway or the corresponding routes are also entered.

  ![Configuring the router](images/127431674763_DV_resource.Stream@PNG-en-US.png)

  Configuring the router

This example configuration results in the following IP routing table for the CPU.

![Sample configuration](images/127431309323_DV_resource.Stream@PNG-en-US.png)

Sample configuration

IP route table of the CPU

| Network destination | Interface | Gateway |
| --- | --- | --- |
| 0.0.0.0/0 | 10.10.0.10 | 10.10.0.1 |
| 192.168.1.0/24 | 192.168.1.1 | - |
| 192.168.2.0/24 | 192.168.2.1 | - |
| 10.10.0.0/24 | 10.10.0.10 | - |

For IP communication between the PG/PC and the HMI device, you need to set up additional IP routes to the IP subnet of the HMI device both in the PC and in the IP router. In the HMI device, you configure the IP address of the CPU interface X1 as the standard gateway.

In a Windows computer, for example, you set up an additional IP route from the command prompt using the command "route add &lt;destination IP subnet&gt; mask &lt;subnet mask&gt; &lt;gateway&gt;". However, you need certain access rights for this. For this example, enter the following prompt:

- "route add 192.168.2.0 mask 255.255.255.0 192.168.4.20"

In an IP router, you set up additional routes, e.g. via a web interface. Set up the following route for this example:

- Destination IP subnet: 192.168.2.0
- Subnet mask: 255.255.255.0
- Gateway: 10.10.0.10

###### Restrictions

You cannot configure any additional IP routes other than the router ("Standard Gateway") for an S7-1500 CPU. The network destination is either a connected IP subnet, or the network destination can be reached via exactly one configurable router. Because the S7‑1500 CPU does not support additional IP routes, you cannot build bi-directional IP router cascades.

In the following configuration, you can configure either "Router 1" or "Router 2" in the CPU. "Router 1" is configured as an example. In this case, you cannot configure "Router 2". IP communication between the PC and the HMI device is not possible because the route is not continuous in both directions.

![Unsupported IP router cascade](images/127431573131_DV_resource.Stream@PNG-en-US.png)

Unsupported IP router cascade

###### IP forwarding via the interface of a CP

IP forwarding also works via the interface of a CP. For this you have to activate the "Access to PLC via communication module" function for this CP in the CPU.

How you enable the "Access to PLC via communication module" function is described in the online help of STEP 7.

###### Linux of the CPU 1518 4 PN/DP MFP via interfaces X1 or X2

If you activate PN/DP MFP IP forwarding for the CPU 1518 4 PN/DP, you will not only reach devices in the IP subnet of interface X3 via interfaces X1 and X2, but also Linux. From the Linux of the CPU 1518 4 PN/DP MFP, you reach all devices in the IP subnets of the interfaces X1, X2 and X3.

Constraints:

- IP forwarding is activated for the CPU 1518 4 PN/DP MFP.
- The IP address of Linux and the IP address of interface X3 are located in the same IP subnet.
- The routes to the IP subnets at X1 and X2 are entered in Linux.  
  In Linux, enter a route with the following command: "Route add-net &lt;Destination IP subnet&gt; mask &lt;Subnet mask&gt; gw &lt;Gateway&gt;

The following figure shows a configuration in which a PC accesses Linux of the CPU 1518-4 PN/DP MFP via interface X2.

![Access to Linux via interface X2](images/127431746955_DV_resource.Stream@PNG-en-US.png)

Access to Linux via interface X2

###### Take network security into account for IP forwarding

If you activate IP forwarding for a CPU, you enable "external" access to devices that are actually only accessible and controlled by the CPU. These devices are therefore usually not protected against attacks.

The following figure shows how to protect your automation system against unauthorized access.

- The CPU accesses all devices within the dark green IP subnets B and C close to the CPU via the interfaces X1 and X2.

  ![Network security for IP forwarding](images/127431598347_DV_resource.Stream@PNG-en-US.png)

  Network security for IP forwarding
- A SCALANCE S router is configured in the CPU. The CPU accesses the devices in the remote, light green IP subnet A via the router.
- The "Access to PLC via communication module" function is enabled for the CP 1543 in the CPU. The CPU reaches all devices within the IP subnet D via interface W1.

If IP forwarding is activated in the CPU, a device from IP subnet A can access any device within IP subnets B, C and D close to the CPU.

Protect your automation system and connected devices against unauthorized access from outside.

Separate the CPU-related IP subnets from the remote IP subnets with a firewall. For example, use the SCALANCE S security modules with integrated firewall.  
This [application example](https://support.industry.siemens.com/cs/ww/en/view/22376747) describes how to protect an automation cell with a firewall using the SCALANCE S602 V3 and SCALANCE S623 security modules.

###### Enabling/disablng IP forwarding

To enable IP forwarding, proceed as follows:

1. Select the CPU in the network view of STEP 7 (TIA Portal).
2. In the properties of the CPU of the Inspector window, navigate to "General" &gt; "Advanced Configuration" &gt; "IP forwarding".
3. In the "Configuration IPv4 Forwarding" area, select the check box "Activate IPv4 for interfaces of this PLC".

   ![Enabling IP forwarding](images/127431449739_DV_resource.Stream@PNG-en-US.png)

   Enabling IP forwarding

Result: IP forwarding is enabled for all interfaces of the S7-1500 CPU.

You disable IP forwarding by clearing the check box "Enable IPv4 forwarding for interfaces of this PLC".

###### IP forwarding with redundant systems S7-1500R/H

For information on configuring IP forwarding of an S7-1500R/H system, refer to the section "Communication with the redundant system S7-1500R/H" in the Communication function manual.

---

**See also**

[Useful information on configuring PROFINET/Industrial Ethernet](#useful-information-on-configuring-profinetindustrial-ethernet)
  
[Settings for interconnecting Ethernet devices](#settings-for-interconnecting-ethernet-devices)
  
[Overview of the CPU properties (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#overview-of-the-cpu-properties-s7-1500)

##### Virtual interface for IP-based applications

As of firmware version 2.8, the S7-1500 CPU offers the option of reaching its IP-based applications, such as OPC UA, not only via its local (PN) interfaces, but also via the interfaces of communication processors in the same station. A communications partner reaches these IP-based applications via a virtual interface that can be configured in the TIA Portal as of version V16. The virtual interface is called W1 (according to IEC 81346-2).

###### Features of the virtual interface

The virtual interface is not a fully diagnostics-capable interface with the familiar properties of conventional interfaces. The virtual interface is not displayed in the graphical views, because the internal connection via the backplane bus does not represent an S7 subnet and does not have any ports. A physical connection by means of a network cable therefore cannot be established.

The IP address of the virtual interface is displayed (e.g. in the TIA Portal, in the display of the CPU) and can be configured.

The following IP-based services can be used e.g. via the virtual interface W1:

- OPC UA (client and server)
- Programmed OUC connections
- Programming device/HMI communication
- Partner access from S7 CPUs via PUT/GET instructions

The activated interface can be used in dialogs where IP-based connections are configured.

![Features of the virtual interface](images/127465985035_DV_resource.Stream@PNG-de-DE.png)

Compared to conventional interfaces, the virtual interface has the following restrictions:

- No access to the web server over the virtual interface.
- [Online backup](Creating%20a%20backup%20of%20an%20S7%20CPU.md#creating-a-backup-of-a-device-s7-1200-s7-1500) is not possible via a connected programming device with the TIA Portal.
- If the CPU and communication partners are connected via the virtual interface, they cannot exchange data via [LLDP](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#ieee-compliant-lldp-s7-1500) (Link Layer Discovery Protocol).
- The S7 routing service does not use the virtual interface W1.

###### Requirement

For a CPU service to be accessible via the Ethernet interface of a CP, the following requirements must be fulfilled:

- S7-1500 CPU firmware V2.8 or higher
- CP 1543-1 firmware V2.2 or higher

**Recommendation**: Use a CP 1543-1 with firmware V3.0 or higher. As of this version, the security functions (firewall) are also available for the virtual interface and no additional firewall needs to be installed between the station and a non-secure network.

###### Configuration of the virtual interface W1

In the properties of an S7-1500 CPU as of firmware V2.8, you can assign a plugged communications module to the virtual interface W1 under "Advanced Configuration &gt; Access to PLC via communications module". You can then use this for external access to the CPU. If no CPs are plugged in or the plugged CPs do not support access to the CPU, the selection is empty.

![Configuration of the virtual interface W1](images/126537120139_DV_resource.Stream@PNG-en-US.png)

After selecting the CP, the specifications and parameters for the virtual interface are displayed. Here, you can edit the settings for the IP protocol and the PROFINET parameters.

- The IP subnet is freely selectable, just like with the CP. The IP subnet is entered via the subnet mask and IP address of the virtual interface.
- When entering the IP subnet for the virtual interface, note that you are not using the same IP subnet as for the local interfaces of the CPU.

Once the IP address is entered, it is shown in the properties dialog of the OPC UA server in the list of server addresses. These settings provide the CPU with the new virtual interface W1 via which CPU services like the OPC UA server can be accessed via a communications module. The corresponding connections and S7 communication (e.g. HMI and BSEND, BRCV) are made via this interface. The OPC UA server does not allow selection of a specific interface (selection via an IP address), either all or none are possible.

> **Note**
>
> The IP address of the virtual interface is not listed as W1 in the device display under the currently displayed local interfaces (Xn) but is available under "Addresses" in the "Settings" section. The virtual interface is also visible when no CP is plugged or when the virtual interface is not activated. If no IP suite is available, the IP address and the subnet mask are 0.0.0.0.

If you have loaded the configured and loaded IP address parameters of the virtual interface and then change the IP address parameters via the display, T_CONFIG instruction or online, the loaded configuration is active again after the CPU restarts.

###### Configuration changes on the CP

A change of the assigned communications module may have an effect on the configuration of the virtual interface:

- In the properties of the CPU:

  - Assignment of a different CP: The configuration is used for the new CP.
  - Deselect the assigned CP: The virtual interface W1 is deactivated and the configuration is lost.   
    When a CP is assigned again, the configuration must be performed again.
- On the device:

  - Moving the CP: If the CP is only moved to another slot of the device, the configuration continues to be valid.
  - Removing the CP: If the CP is deleted or moved to another device, the configuration is retained. In the drop-down list of the CPU, the CP is displayed as missing and compiling the configuration indicates an error. The missing CP can be deselected or assigned to another CP.

###### Display in the diagnostics and the system constants

The virtual interface W1 is displayed in the diagnostics view under "Online &amp; Diagnostics". The hardware ID of the virtual interface is displayed in the system constants of the CPU properties.

###### Settings in the communications module (CP 1543-1 as of firmware V3.0)

As of firmware V3.0, you can use the CP's internal firewall to protect data traffic via the virtual interface. To activate the firewall in the communications module, proceed as follows in the protected project:

1. Select the communications module in the STEP 7 work area.
2. In the Inspector window, go to "Properties &gt; Security".
3. Activate the "Enable security functions" option.  
   The configurable security functions now appear in the Inspector window.
4. Enable the option "Activate firewall".   
   In the Inspector window, you can now permit the use of the virtual interface W1.

You can only secure data traffic via the virtual interface W1 of the CPU for the OPC UA service.

> **Note**
>
> **Checking the manual configuration**
>
> If the firewall is activated, you need to manually check whether the desired services are allowed by the firewall. Only enable those services for the IP and MAC filters that you also want to access via the CP interface. See the notes on security settings and firewall rules of the S7-1500 CPs in the info system of the TIA Portal.

###### Settings in the communications module (CP 1543-1, firmware V2.2, &lt; V3.0)

The security functions of the CP 1543-1 with a firmware version lower than V3.0 cannot secure data traffic via the virtual interface. Although you can activate the security functions in TIA Portal, such a configuration cannot be compiled.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Connecting to non-secure networks**  If you connect the CP to a non-secure network, it is absolutely necessary to connect an additional firewall between the CP and the non-secure network. For example, use the Security Modules SCALANCE S602 V3 and SCALANCE S623 with integrated firewall. |  |

---

**See also**

[Access to OPC UA applications (S7-1200, S7-1500, S7-1500T)](Configuring%20automation%20systems.md#access-to-opc-ua-applications-s7-1200-s7-1500-s7-1500t)
  
[Useful information on configuring PROFINET/Industrial Ethernet](#useful-information-on-configuring-profinetindustrial-ethernet)
  
[Settings for interconnecting Ethernet devices](#settings-for-interconnecting-ethernet-devices)
  
[IP forwarding](#ip-forwarding)

#### PROFIBUS network configuration

This section contains information on the following topics:

- [PROFIBUS addresses](#profibus-addresses)
- [What you need to know about PROFIBUS bus parameters](#what-you-need-to-know-about-profibus-bus-parameters)
- [Description of the bus parameters](#description-of-the-bus-parameters)
- [Bus profiles with PROFIBUS](#bus-profiles-with-profibus)
- [What you need to know about PROFIBUS line configuration](#what-you-need-to-know-about-profibus-line-configuration)
- [PROFIBUS communication load](#profibus-communication-load)

##### PROFIBUS addresses

###### Rules for the network configuration

All the devices in a subnet must have a different PROFIBUS address.

Only when all the modules in a subnet have different addresses and your actual structure matches that of the network configuration produced, should you load the settings across the network.

You can connect devices to the PROFIBUS subnet that communicate via configured connections or that belong to a PROFIBUS DP master system.

You can find more information on configuring a DP master system in the following sections.

###### Requirements

The 121xC CPU is PROFIBUS compatible as of firmware version 2.0.

###### Rules for assigning PROFIBUS addresses

- Allocate the PROFIBUS addresses in ascending order.
- Reserve the PROFIBUS address "0" for a programming device.
- Allocate a unique PROFIBUS address between 0 and 126 for each device on the PROFIBUS network and/or for each DP master and each DP slave in the PROFIBUS network.
- There are modules with which the smallest address that can be set has to be greater than 1.
- All PROFIBUS addresses of a PROFIBUS subnet must be different.

You will find additional rules relating to the structure of a network in the manuals for setting up automation systems, for example SIMATIC S7-1200.

> **Note**
>
> **PROFIBUS address "0"**
>
> Reserve PROFIBUS address "0" for a programming device that you will briefly connect up to the PROFIBUS network at a later date for servicing.

---

**See also**

[What you need to know about PROFIBUS bus parameters](#what-you-need-to-know-about-profibus-bus-parameters)

##### What you need to know about PROFIBUS bus parameters

###### Matching parameters to one another

The PROFIBUS subnet will only function without problem if the parameters for the bus profile are matched to one another. You should therefore only change the default values if you are familiar with how to configure the bus profile for PROFIBUS.

> **Note**
>
> It may be possible for the bus parameters to be adjusted depending on the bus profile. If the bus parameters cannot be adjusted, they are grayed out. The offline values of the bus parameters are always shown even if you are online and linked to the target system.

The parameters shown apply to the entire PROFIBUS subnet and are briefly explained below.

###### Activating cyclic distribution of the bus parameters

If the "Enable cyclic distribution of the bus parameters" check box is selected under "Bus parameters" while PROFIBUS subnet is selected in the Inspector window, the bus parameters are transferred cyclically during operation by the modules that support this function. This allows a programming device, for example, to be easily connected to the PROFIBUS in runtime.

You should deactivate this function:

- For a heterogeneous PROFIBUS subnet (or more accurately: when external devices are connected whose protocol uses the DSAP 63 for Multicast)
- When in constant bus cycle time mode (minimize bus cycle)

###### Bus parameters for the bus profile of PROFIBUS subnets

| Bus parameter | Adjustable? | Limit values |
| --- | --- | --- |
| Tslot_Init | Yes | Max. Tsdr + 15 &lt;= Tslot_init &lt;= 16.383 t_bit |
| Max. Tsdr | Yes | 35 + 2*Tset + Tqui &lt;= Max. Tsdr &lt;= 1.023 t_bit |
| Min. Tsdr | Yes | 11 t_bit &lt;= Min. Tsdr &lt;= MIN(255 t_bit, ...  ... Max. Tsdr - 1, 34 + 2*Tset + Tqui) |
| Tset | Yes | 1 t_bit &lt;= Tset &lt;= 494 t_bit |
| Tqui | Yes | 0 t_bit &lt;= Tqui &lt;= MIN(31 t_bit, Min. Tsdr - 1) |
| GAP factor | Yes | 1 &lt;= GAP factor &lt;= 100 |
| Retry limit | Yes | 1 &lt;= Retry limit &lt;= 15 |
| Tslot | No | --- |
| Tid2 | No | Tid2 = Max. Tsdr |
| Trdy | No | Trdy = Min. Tsdr |
| Tid1 | No | Tid1 = 35 + 2*Tset + Tqui |
| Ttr | Yes | 256 t_bit &lt;= Ttr &lt;= 16.777.960 t_bit |
| Ttr typical | No | This time is provided for information only and is not transferred to the nodes. |
| Response monitoring |  | 10 ms &lt;= response monitoring (watchdog) &lt;= 650 s |

If you want to create a customized bus profile, we recommend the following settings:

- Minimum target rotation time (Ttr) = 5000 x HSA (highest PROFIBUS address)
- Minimum response monitoring (watchdog) = 6250 x HSA

###### Recalculating

You can use the "Recalculate" button to recalculate the parameters.

---

**See also**

[PROFIBUS addresses](#profibus-addresses)
  
[Description of the bus parameters](#description-of-the-bus-parameters)

##### Description of the bus parameters

###### Detailed description of PROFIBUS bus parameters

| Bus parameter | Meaning |
| --- | --- |
| Tslot_Init | The wait-for-reception (slot time) defines the maximum time the sender will wait to receive a response from the addressed partner. If the influence of the line components on message frame run times is entered in the "Cable Configuration" parameter group, these components must also be taken into account. The component is added to the specified Tslot_Init and the total used as Tslot. |
| Max. Tsdr | The maximum protocol processing time defines the latest time by which the responding node should have replied. |
| Min. Tsdr | The minimum protocol processing time defines the earliest time by which the responding node may reply. |
| Tset | The trigger time is the time which may lapse between the reception of a data message frame and the response to it in the node. |
| Tqui | The modulator quiet time is the time which a sending node needs after the end of the message frame to switch from sending to receiving. |
| GAP factor | The GAP update factor defines the number of token rotations after which a newly added, active node can be added to the logical token ring. |
| Retry limit | This parameter defines the maximum number of attempts (message frame repeats) made to reach a node. |
| Tslot | The wait-for-reception time (slot time) defines the maximum time the sender will wait to receive a response from the addressed partner.  If the influence of the bus design components on message frame run times is entered in the "Cable Configuration" parameter group, these components must also be taken into account. The component is added to the specified Tslot_Init and the total used as Tslot. |
| Tid2 | Idle time 2 defines the earliest time by which a sending node may send the next message frame after sending a message frame that has not been acknowledged. |
| Trdy | The ready time specifies the earliest time by which a sending node may receive a response message frame. |
| Tid1 | Idle time 1 defines the earliest time by which a sending node may send the next message frame after receiving a response. |
| Ttr | The target rotation time is the maximum time made available for a token rotation. During this time, all active nodes (DP masters etc.) have the right to send (token) once. The difference between the target rotation time and the actual token holding time of a node determines how much time is left over for the other active nodes (programming device, other DP masters etc.) to send message frames. |
| Ttr typical | The typical data cycle time is the average response time on the bus if all configured slaves are exchanging data with the DP master. None of the slaves report diagnostics and there is no extra message frame traffic with programming devices or other active nodes etc. on the bus. |
| Response monitoring | The response monitoring time is only needed for PROFIBUS-DP bus systems. It defines the latest time by which a DP slave has to be addressed by its DP master with a new data message frame. If this does not happen, the DP slave assumes that the DP master has failed and resets its outputs to a secure mode. |

---

**See also**

[What you need to know about PROFIBUS bus parameters](#what-you-need-to-know-about-profibus-bus-parameters)

##### Bus profiles with PROFIBUS

###### Introduction

Depending on the device types connected and protocols used on the PROFIBUS, different profiles are available. The profiles differ in terms of the setting options and calculation of bus parameters. The profiles are explained below.

###### Devices with different profiles on the same PROFIBUS subnet

The PROFIBUS subnet only functions without problem if the bus parameters of all devices have the same values. For example, if both DP and FMS services are being used on a subnet, the "slower" sets of bus parameters must always be set for all devices, i.e. even the "Universal (DP/FMS)" profile for DP devices.

###### Profiles and transmission rates

| Profiles | Supported transmission speeds in kbps |
| --- | --- |
| DP | 9.6 19.2 45.45 93.75 187.5 500 1500 3000 6000 12000 |
| Standard | 9.6 19.2 45.45 93.75 187.5 500 1500 3000 6000 12000 |
| Universal (DP-FMS) | 9.6 19.2 93.75 187.5 500 1500 |
| Customized | 9.6 19.2 45.45 93.75 187.5 500 1500 3000 6000 12000 |

###### Meaning of profiles

| Profile | Meaning |
| --- | --- |
| DP | Select the "DP" bus profile when the only devices connected to the PROFIBUS subnet are those which satisfy the requirements of standard EN 50170 Volume 2/3, Part 8-2 PROFIBUS. The bus parameter setting is optimized on these devices.   This includes devices with DP master and DP slave interfaces of the SIMATIC S7 and distributed I/Os of other manufacturers. |
| Standard | Compared to the "DP" profile, the "Standard" profile also offers scope for devices of another project or devices which have not been configured here to be taken into account when calculating the bus parameters. The bus parameters are then calculated following a simple, non-optimized algorithm. |
| Universal (DP/FMS) | Select the "Universal (DP/FMS)" bus profile when individual devices on the PROFIBUS subnet use the PROFIBUS-FMS service.   This includes the following devices for example:   - CP 343-5 (SIMATIC S7) - PROFIBUS-FMS devices of other manufacturers   As with the "Standard" profile, this profile allows you to take other devices into account when calculating the bus parameters. |
| Customized | The PROFIBUS subnet will only function without problem if the parameters for the bus profile are matched to one another. Select the "Customized" profile when none of the usual profiles "match" a PROFIBUS device and you need to adapt the bus parameters to your special structure. Information on this can be found in the documentation for the PROFIBUS device.   You should only change the default values if you are familiar with how to configure the bus profile for PROFIBUS.   Not all combinations that can be theoretically set can be used even with this bus profile. The PROFIBUS standard specifies several parameter limits that depend on other parameters. For example, a responder must not respond (Min Tsdr) before the initiator can receive the message frame (Trdy). These standard specifications are also checked in the "Customized" profile.   Tip: The bus parameters last valid on the PROFIBUS subnet are always automatically set as customized. For example, if the "DP" bus profile was valid for the subnet, then the bus parameters for "DP" are set in the "Customized" bus profile. The parameters can be modified on this basis.   The monitoring times are not automatically recalculated so that you do not put at risk the consistency of set values, for example with configurations in other configuration tools without realizing that you have done so.  You can also have the Ttr monitoring times and target rotation time calculated on the basis of parameters you have set: Click here on the "Recalculate" button. |

> **Note**
>
> Both mono-master mode and multi-master mode are possible with all PROFIBUS profiles.

##### What you need to know about PROFIBUS line configuration

###### Cable configuration and bus parameters

Information regarding the cable configuration can be taken into consideration when calculating the bus parameters. For this purpose, you must select the "Consider cable configuration" check box in the properties for the PROFIBUS subnet.

The remaining information then depends on the type of cable used; the following settings are available:

- Copper cable
- Fiber-optic cable/optical ring

###### PROFIBUS line configuration, optical ring

The calculation depends on the OLM types used. The selection is made by activating the check box (multiple activation is possible, at least one OLM type must be selected):

- OLM/P12
- OLM/G12
- OLM/G12-EEC
- OLM/G12-1300

The following bus parameter adjustments are made:

- Configuration of a node not present

  > **Note**
  >
  > **The following restrictions apply to optical rings, even for passive nodes (DP slaves for example):**
  >
  > A maximum of HSA-1 nodes may be connected to the PROFIBUS network. With an HSA of 126, addresses 126 and 125 must not be used. A maximum of 125 nodes are possible on the bus (No. 0 to 124).
  >
  > If an HSA is less than or equal to 125, the addresses HSA and greater may not be used. The address HSA-1 may not be used.
- Increase the retry value to 3
- Setting of minimum slot time needed for ring mode

  > **Note**
  >
  > Short slot time values are needed for OLM/P12, average ones for OLM/G12 and OLM/G12-EEC and long ones for OLM/G12-1300. This results in high performance for small network lengths and average to low performance for average to large network lengths.

##### PROFIBUS communication load

###### Communication load - allowing for additional network stations

The bus parameters depend on the volume of communication between the active network nodes. There are differences between cyclic communication (DP) and connection-based, acyclic communication (S7 communication, Send/Receive (FDL), FMS). Unlike DP, the volume and size of communication tasks (communication load) depends on the user program. For this reason, the communication load cannot always be calculated automatically.

To calculate the bus times you can define a network configuration in the "Additional network stations" parameter group that differs from the network configuration.

###### Taking the profile into account

The network configuration can be defined for the "Standard", "Universal (DP/FMS)", and "User-defined" profiles. Parameters cannot be entered in the "Additional network stations" parameter group for the "DP" profile.

###### Quantification of the communication load

The following settings are available in order to make allowance for the communication load.

- Information regarding the number of unconfigured network stations;
- Information on the communication load resulting from the user programs for FDL or S7 communication. Here you can selected from the following settings:

  - Low

    Typically used for DP, no great data communication apart from DP.
  - Medium

    Typically used for mixed operations featuring DP and other communication services (such as for S7 communication), when DP has strict time requirements and for average acyclic volumes of communication.
  - High

    For mixed operations featuring DP and other communication services (such as for S7 communication), when DP has loose time requirements and for high acyclic volumes of communication.

#### MPI network configuration (S7-300, S7-400, PC)

##### Allocating MPI addresses

Note the following for devices with an MPI interface: All devices of a subnet must have a different device address.

CPUs with MPI address ship with the default MPI address 2. Since you can only use this address once in the MPI subnet, you will have to change the default address in all other CPUs.

The following applies to devices with the article no. 6ES7 3xx-xxxxx-0AB0:

When planning the MPI addresses for several CPUs, you have to fill "MPI address gaps" for FMs and CPs with separate MPI addresses to prevent addresses being assigned twice.

Only when all the modules in a subnet have different addresses and your actual structure matches that of the network configuration produced, should you load the settings across the network.

##### Rules for assigning the MPI address

- Allocate the MPI addresses in ascending order.
- Reserve MPI address 0 for a programming device.
- You can link up to 126 (addressable) devices with one another in an MPI subnet; up to 8 devices at a transfer speed of 19.2 KB/s.
- All MPI addresses in an MPI subnet must be different.

You will find other rules relating to the structure of a network in the manuals for setting up automation systems.

#### Assigning addresses via DHCP (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Principle of address assignment via DHCP (S7-1500)](#principle-of-address-assignment-via-dhcp-s7-1500)
- [DHCP with DNS (S7-1500)](#dhcp-with-dns-s7-1500)
- [Activate DHCP (S7-1500)](#activate-dhcp-s7-1500)
- [Configuring the client ID (S7-1500)](#configuring-the-client-id-s7-1500)
- [Get addresses of the DNS servers via DHCP (S7-1500)](#get-addresses-of-the-dns-servers-via-dhcp-s7-1500)
- [Get addresses of the NTP servers via DHCP (S7-1500)](#get-addresses-of-the-ntp-servers-via-dhcp-s7-1500)
- [Obtain host and domain name via DHCP (S7-1500)](#obtain-host-and-domain-name-via-dhcp-s7-1500)

##### Introduction (S7-1500)

In order to provide future-proof, efficient and flexible automation, more and more components from the production area support IT standards. Worldwide Ethernet standards, integrated communication and versatility make IT-supported automation an economical solution for your requirements. Functional expansions of the communication options of the S7-1500 CPUs in this direction give you more freedom for the possible uses of your system or machine. You use IT technology to automate efficiently. With the introduction of DHCP and the expansions of DNS for S7-1500 CPU as of firmware version V2.9, you gain more flexibility for the design of your automation solution.

For the interfaces of an S7-1500 CPU you can set that address parameters such as the IP address with subnet mask, can be got from a DHCPv4 server (hereinafter DHCP server).

![Figure](images/142287678987_DV_resource.Stream@PNG-en-US.png)

###### Areas of application

- Use of the S7-1500 CPU in a managed IT environment
- Adding new devices in a modular manufacturing structure

##### Principle of address assignment via DHCP (S7-1500)

###### Requirement configuration

The following requirements must be met so that a PROFINET interface of the S7-1500 CPU can obtain IP address parameters via a DHCP server:

- The address assignment via a DHCP server is configured.

  [Activate DHCP](#activate-dhcp-s7-1500)
- No PROFINET IO communication may be configured for the interface.

###### Principle of DHCP address assignment

The process begins as soon as the project is loaded into the CPU or the CPU is switched on with configured DHCP address assignment and started up, the process of DHCP assignment begins:

![Principle of DHCP address assignment](images/142287666315_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DHCP Discover | The DHCP client searches for a suitable DHCP server via broadcast. The DHCP client identifies itself to the DHCP-Server with the configured client ID or with its MAC address. |
| DHCP Offer | The DHCP server offers the DHCP-client IP address parameters (IPv4 address, subnet mask, optional default router) and if necessary further data (options). |
| DHCP Request | The DHCPclient requests the IP address parameters and options offered in the DHCP offer.   The DHCP client of the S7-1500 CPU always accepts the first DHCP offer of a DHCP server that meets the requirements (IP address with subnet mask). |
| DHCP Acknowledgment | The DHCP server confirms and transmits the IP address parameters and options offered in the DHCP offer.  The DHCP server also notifies the DHCP client how long the DHCP client can use the address parameters (lease time). |

The IP address parameters and options are stored in the load memory of the CPU. After a general reset or restart of the CPU, the IP address parameters and options are obtained again via DHCP.

###### DHCP address assignment options

For the S7-1500 CPU you can configure that the following options are obtained via a DHCP server:

- Addresses of up to four DNS servers

  [Get addresses of the DNS servers via DHCP](#get-addresses-of-the-dns-servers-via-dhcp-s7-1500)
- Addresses of up to four NTP servers

  [Get addresses of the NTP servers via DHCP](#get-addresses-of-the-ntp-servers-via-dhcp-s7-1500)
- Host and domain name

  [Obtain host and domain name via DHCP](#obtain-host-and-domain-name-via-dhcp-s7-1500)

If necessary, the DHCP server also supplies the address of a router (default gateway) as option.

###### How long can the S7-1500 CPU use the DHCP address parameters?

In addition to the address parameters, the DHCP server also notifies the S7-1500 CPU (DHCP client)of the lease time. The lease time defines how long the CPU can use the address parameters.

When the lease time has fully expired, the CPU returns the assigned address parameters. The CPU has an internal time monitoring for the lease time.

At certain times when the lease time expires, the CPU has the option of extending the lease time:

- Renewal: Half of the lease time has expired: The CPU contacts the original DHCP server and asks for an extension of the lease time. The original DHCP server can either confirm the existing lease time or assign a new lease time. With a new lease time, the time monitoring in the CPU is reset.
- Rebinding: 7/8 of the lease term has expired: The CPU contacts all available DHCP servers via broadcast and asks for an extension of the lease time. A DHCP server can either confirm the existing lease time or assign a new lease time. With a new lease time, the time monitoring in the CPU is reset.

  In the event of a negative response from the DHCP server during rebinding or if no DHCP server replies, the CPU returns the address parameters after the lease time has elapsed.

If the CPU has returned the address parameters after the lease time has expired, the CPU starts a new cycle for DHCP address assignment with a new DHCP discover.

##### DHCP with DNS (S7-1500)

As of STEP 7 V17 and firmware version V2.9, the S7‑1500 CPU supports the host name and domain address parameters used in name-based communication (DNS).

For specific communication services, name-based addressing via the complete name consisting of host name and domain, is useful:

- The CPU is addressable under the complete name, for example at OPC UA, Open User Communication. In the case of dynamic IP address assignment by the DHCP server, unique addressing is always possible through the DNS name.
- Certificates of the S7‑1500 CPU may contain the complete name, for example, for OPC UA communication, web server, secure communication.

  - Only when you configure host name and domain for the S7-1500 CPU in STEP 7 is the complete name entered in the device certificates in the project as subject alternate name (SAN).
  - As soon as you obtain the host name and/or domain via DHCP or assign it via the user program, the complete name is not stored in the device certificates in the project.

How you set the DNS configuration for your CPU depends on how you assign the host name and domain in your network .

- Central assignment of host name and domain

  You assign the host name and domain centrally in your network, for example via a configured DNS server. In STEP 7 you configure that the CPU obtains the host name and domain via DHCP.

  In the following configuration, only the client ID is configured in the S7-1500 CPU. At the DHCP address assignment the DHCP-server returns the host name and domain options to the CPU.

  ![Figure](images/142287742731_DV_resource.Stream@PNG-en-US.png)

  For this configuration, you must first activate the host name and domain configuration in STEP 7. You then configure that the host and domain name are obtained via DHCP.

  [Obtain host and domain name via DHCP](#obtain-host-and-domain-name-via-dhcp-s7-1500)
- Local assignment of host name and domain

  You can configure the host name and domain in STEP 7 or assign them in the user program.

  > **Note**
  >
  > **Validity of the data obtained from DHCP**
  >
  > If you change the host name and/or domain in the user program, then all data obtained via DHCP (IP suite, host name, domain, NTP server, DNS server) becomes invalid and is retrieved again from DHCP server. Therefore, you should only change the host name and/or domain in urgent cases and not during operation.
  >
  > All connections can be dropped if the IP address of the interface changes.

  In the following configuration, the S7‑1500 CPU has its host name and domain configured in addition to its client ID. When assigning DHCP addresses, the CPU supplies the client ID as well as the host name and the domain to the DHCP server.. The DHCP server receives the information to update, for example a DNS server with the address data of the CPU.

  ![Figure](images/142287691659_DV_resource.Stream@PNG-en-US.png)

  For this configuration, you must first activate the host name and domain configuration in STEP 7. You then configure the host name and domain in STEP 7.
- Central assignment of the domain and local assignment of host name.

  - In STEP 7 you configure that the CPU obtains the domain via DHCP.
  - You can configure the host name in STEP 7 or assign it via the user program.

  In the following configuration, the host name is also configured in the S7-1500 CPU in addition to the client ID. When assigning DHCP addresses, the CPU supplies the client ID as well as the host name to the DHCPv4 server. The DHCP server supplies the domain to the CPU.

  ![Figure](images/142287768203_DV_resource.Stream@PNG-en-US.png)

  For this configuration, you must first activate the host name and domain configuration in STEP 7. Then configure the host name in STEP 7 and configure that the domain is obtained via DHCP.

###### Requirements

- You have activated the address assignment via DHCP for at least one interface of the S7-1500 CPU.

###### Configuration of host and domain name

To activate the host name and domain configuration in STEP 7, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name" &gt; "Host and domain name configuration".
3. Select the "Enable host name and domain" check box.

###### Configuring the host name in STEP 7

To configure the host name in STEP 7, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name"&gt; "Host and domain name configuration"&gt; "Host name".
3. For "Host name configuration" select "Set host name in the project" from the drop-down list.
4. Enter the host name for "Host name:".

   - Enter your desired host name.
   - If you select the "Host name identical to device name" check box, STEP 7 automatically assigns the device name as the host name.

Only if you have configured the host and domain name in STEP 7, the full name is displayed for "Full name:".

###### Assign host name in the user program

To assign the host name in the user program, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name" &gt; "Host and domain name configuration" &gt; "Host name".
3. Under "Host name configuration” select "Set hostname directly on the device (e.g. PLC program, display)" in the drop-down list.
4. Call the instruction "CommConfig" in the user program. The DATA parameter must point to a UDT "Conf_Hostname" where the host name is defined.

**Additional information on the "CommConfig" instruction and on the UDT "Conf‑Hostname"**

[CommConfig: Reading and changing communication parameters](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#commconfig-reading-and-changing-communication-parameters-s7-1500)

###### Configuring a domain in STEP 7

To configure the domain in STEP 7, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name" &gt; "Host and domain name configuration" &gt; "Domain".
3. For "Domain configuration" select "Set domain in the project" from the drop-down list.
4. Enter your desired domain under "Domain:".

Only if you have configured the host name and domain in STEP 7 is the full name displayed for "Full name:".

###### Assigning a domain in the user program

To assign the domain in the user program, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name" &gt; "Host and domain name configuration" &gt; "Domain".
3. Under "Domain configuration" select "Set domain directly on the device (for example PLC program, display)" in the drop-down list.
4. Call the instruction "CommConfig" in the user program. The DATA parameter must point to a UDT "Conf_Domainname" where the domain name is specified.

You can find additional information on the "CommConfig" instruction and on the UDT "Conf-Domainname" in the STEP 7 online help.

###### Rules for maximum lengths of host name, domain and client ID

Note the following maximum lengths in bytes. One byte corresponds to one character:

- Host name: Maximum 63 bytes
- Domain: Maximum 252 bytes
- Client ID: Maximum 254 bytes
- Host + Domain name : Maximum 254 bytes
- Host + Domain name + Client ID: Maximum 260 bytes

  Applies only when host name and domain must be sent to the DHCP server.

##### Activate DHCP (S7-1500)

###### Requirements

- S7-1500 CPU as of firmware version V2.9

###### Procedure

To activate DHCP for the PROFINET interface of an S7‑1500 CPU, follow these steps:

1. Select the PROFINET interface of the S7‑1500 CPU in STEP 7.
2. In the properties of the interface, navigate to "Ethernet addresses" &gt; "Internet Protocol Version 4 (IPv4)".
3. Select the option "IP address of DHCP server".

###### Result

You have set the interface so that it obtains your IP address via a DHCP server.

"Use MAC address as client ID" is set as the operating mode for DHCP on the S7‑1500 CPU. How to adjust the client ID is described under [Configuring the client ID](#configuring-the-client-id-s7-1500).

##### Configuring the client ID (S7-1500)

###### The client ID

The S7-1500 CPU always identifies itself to a DHCP server with the client ID (DHCP option 61). The client ID is interface specific.

The S7-1500 CPU supports the following two operating modes with regard to the client ID:

- Use the MAC address as the client ID: The MAC address of the CPU is used as the client ID for the DHCP client. Note, if you execute a device exchange of the CPU in this operating mode, the MAC address and therefore also the client ID changes.
- User-defined client ID: With this option you specify the client ID in the configuration in STEP 7. You also have the option of adapting the client ID during runtime, for example, in the user program using the "CommConfig" instruction.  
  If you perform a device exchange of the CPU in this operating mode, the new CPU is assigned the configured client ID.

###### Requirement

- You have activated address assignment via DHCP for the interface.

###### Configuring the client ID

To configure the client ID in STEP 7, follow these steps:

1. Select the PROFINET interface of the S7‑1500 CPU in STEP 7.
2. In the properties of the interface, navigate to "Ethernet addresses" &gt; "Internet Protocol Version 4 (IPv4)"&gt; "IP address of DHCP server".
3. For "Operating mode" select the required operating mode from the drop-down list:

   - Use MAC address as client ID (default setting)
   - User-defined client ID

   If you have selected the option "Use MAC address as client ID", then you are already finished here. For "User-defined client ID", proceed to the next step.
4. Enter a valid client ID for "Client ID".

   - A character string with 7-bit ASCII characters is allowed in the area from 0x21 to 0x7e.
   - Some DHCP servers expect a leading "0" (e.g. some SCALANCE devices). In this case, enter "\ 0" followed by your client ID.
5. In order to make the user-defined client ID adaptable during runtime, select the "Client ID can be changed during runtime" check box.

   > **Note**
   >
   > **Forgo entry of a Client ID**
   >
   > If you have activated the "Client ID can be changed during runtime" check box, you can leave the field for the user-defined client ID empty in the configuration in STEP 7. In this case, the CPU uses the MAC address as client ID until the first adaptation of the client ID.

###### Adapting the client ID during runtime

You can use the "CommConfig" instruction to adapt the client ID via the user program. Call the instruction. The DATA parameter must point to a UDT "Conf_ClientId" or a UDT "Conf_ClientId_Opaque". The client ID must be specified in the UDT.

> **Note**
>
> **Validity of data obtained via DHCP**
>
> If you change the client ID with "CommConfig", all data obtained via DHCP will be invalid: IP Suite, domain name, NTP server, DNS server. Therefore, you should only change the client ID in urgent cases and not during operation.

If the client ID may be changed during runtime, the configured client ID or, if the field is left blank, the MAC address applies until the client ID is changed by the user program.

**More information on the instruction "CommConfig" and the UDTs "Conf_ClientId" and "Conf_ClientId_Opaque"**

[CommConfig: Reading and changing communication parameters](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#commconfig-reading-and-changing-communication-parameters-s7-1500)

###### Restore originally configured client ID

After the client ID has been changed by the user program, you can return to the originally configured client ID in the following way:

- Reset the CPU to factory settings and format the memory card. Then reload your configuration into the device.
- Load a new DHCP configuration in which the client ID adaptation is disabled during runtime.

To reset to factory settings, follow these steps:

1. Open the Online and Diagnostics view of the CPU.
2. In the "Functions" folder, select the "Reset to factory settings" group.
3. Select the "Format memory card" check box.
4. Click on "Reset PLC".

See also: [Resetting an S7 CPU to the factory settings](Device%20and%20network%20diagnostics.md#resetting-an-s7-cpu-to-the-factory-settings-s7-1200-s7-1500).

##### Get addresses of the DNS servers via DHCP (S7-1500)

###### Requirements

- You have activated the address assignment via DHCP for at least one interface of the S7-1500 CPU.

###### Get addresses from DNS servers via DHCP

To obtain the addresses of up to 4 DNS servers via DHCP, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "DNS configuration" &gt; "Server list".
3. For "Name resolution via DNS" select "Set DNS server remotely (e.g. DHCP)" in the drop-down list.

Result: If the DHCP server supplies addresses from DNS servers as option, the CPU uses up to 4 addresses.

##### Get addresses of the NTP servers via DHCP (S7-1500)

###### Requirements

- You have activated the address assignment via DHCP for at least one interface of the S7-1500 CPU.

###### Obtaining addresses from NTP servers via DHCP

To obtain the addresses of up to four NTP servers via DHCP, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Time of day" &gt; "Time synchronization"&gt; "NTP mode".
3. For "Time synchronization" select "Set NTP server remotely (e.g. DHCP)" in the drop-down list.

Result: If the DHCP server supplies addresses from NTP servers as option , the CPU uses up to 4 addresses.

##### Obtain host and domain name via DHCP (S7-1500)

###### Requirement

- You have activated the address assignment via DHCP for at least one interface of the S7-1500 CPU.
- You have activated the host name and domain configuration in STEP 7.

###### Obtain host name via DHCP

To obtain the host name via DHCP, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name"&gt; "Host and domain name configuration"&gt; "Host name".
3. For "Host name configuration" select "Set host name remotely (e.g. DHCP)" in the drop-down list.

Result: If the DHCP server supplies a host name as option, the CPU uses this host name.

###### Obtaining a domain via DHCP

To obtain the domain via DHCP, follow these steps:

1. Select the S7-1500 CPU in STEP 7.
2. In the properties of the CPU, navigate to "Advanced configuration" &gt; "Host and domain name" &gt; "Host and domain name configuration" &gt; "Domain".
3. For "Domain configuration:" select "Set domain remotely (e.g. DHCP)" in the drop-down list.

Result: If the DHCP server delivers a domain as option, the CPU uses this domain.

### Communication via connections

This section contains information on the following topics:

- [Working with connections](#working-with-connections)
- [Connections - Purpose and selection](Connections%20-%20Purpose%20and%20selection.md#connections---purpose-and-selection)
- [Configuring connections](Configuring%20connections.md#configuring-connections)
- [Connection types (S7-300, S7-400, S7-1500)](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#connection-types-s7-300-s7-400-s7-1500)

#### Working with connections

This section contains information on the following topics:

- [Libraries for communication for SIMATIC controllers](#libraries-for-communication-for-simatic-controllers)
- [Using Open User Communication (S7-1200, S7-1500, S7-1500T)](#using-open-user-communication-s7-1200-s7-1500-s7-1500t)
- [Configuring HMI connections](#configuring-hmi-connections)
- [Configuring S7 connections (S7-1200)](#configuring-s7-connections-s7-1200)
- [S7 connections using PUT and GET instructions](#s7-connections-using-put-and-get-instructions)
- [Connection resources](#connection-resources)

##### Libraries for communication for SIMATIC controllers

The libraries for communication are a collection of blocks for various communication tasks, functions and protocols for SIMATIC controllers. The libraries extend the range of functions or facilitate the application of the existing instructions for communication.

###### Link to the library

[Libraries for communication for SIMATIC controllers](https://support.industry.siemens.com/cs/ww/en/view/109780503)

###### Use cases for the communication libraries

Described below are use cases for which special libraries are available for you to download.

The names of the libraries and details that are important for the application can be found in lower-level application examples.

- Communication based on **TCP/IP**, additional communication functionalities by means of a separate protocol  
  (which means the establishment of a point-to-point full-duplex connection via Industrial Ethernet, based on the TCP standard)

  As the range of functions of the TCP transport protocol is not sufficient for many applications in the automation sector, a separate protocol (LCom protocol) is defined and implemented in the corresponding block library. The LCom protocol enables additional communication functionalities, such as automatic connection establishment after faults, consistent transmission of large data volumes, cyclical or one-time data transfer.
- Data exchange of an S7-1200/1500 controller with a **web server** in the local network or on the Internet via HTTP or HTTPS

  The HTTP request methods GET, POST and PUT can be implemented with a library in the user program. Due to the integrated certificate management in TIA Portal, it is also possible to transfer data securely via the library using HTTPS.

  See also:

  [Application example for using certificates in TIA Portal in Siemens Industry Online Support](https://support.industry.siemens.com/cs/ww/en/view/109769068)
- Communication of a SIMATIC S7-1200/1500 controller as **MQTT client**

  You can use the corresponding library to submit MQTT messages to a broker (Publisher role) and create subscriptions (Subscriber role). Communication can be secured via a TLS connection.
- Connection of a SIMATIC S7-1200/1500 controller to **MindSphere**

  MindSphere is the cloud-based, open IoT operating system from Siemens. With the "MindConnect IoT Extension" upgrade, it is possible to connect devices to MindSphere via MQTT. You can, for example, convert data points into a MindSphere-compliant message, request user data from MindConnect IoT Extension, transmit messages to MindConnect IoT Extension (Publisher role) and receive messages from MindConnect IoT Extension (Subscriber role) using the corresponding library.
- **OPC UA PubSub communication** for S7-1500 controllers

  Part 14 of the OPC UA specification introduced the "PubSub" communication mechanism. This mechanism uses a so-called "publish/subscribe" principle. In this principle, the publisher (sender) and subscriber (receiver) are decoupled from each other. The number of subscribers does not matter for the publisher; multicast or broadcasts are possible.

  The corresponding libraries implement PubSub via UDP and MQTT.
- Monitoring and control of **SNMP-capable network components** and sending of messages to a network management system

  The status of SNMP-capable network components can be monitored and, if necessary, controlled via SNMP (Simple Network Management Protocol) by network management systems, such as SINEC NMS. The corresponding library also allows a SIMATIC S7-1200/1500 controller with PROFINET interface to act as a simple SNMP manager. This means that the CPU can query and, if necessary, also control network components. Or that the CPU as SNMP agent can send SNMP traps (unacknowledged signals, messages) to an SNMP manager.
- Synchronization of the time in plant units by means of **SNMP server functions**

  Exact "atomic time" is often not necessary for plant components. It is usually sufficient to have a common time base for all automation components. The use of a SIMATIC S7 CPU as an SNTP server enables flexible and simple synchronization of plants and plant units, for example, to obtain descriptive time stamps for error messages and logging data plant-wide. The corresponding library provides the following functions:

  - Receiving and evaluating an NTP telegram from an (S)NTP client
  - Creating and sending an NTP telegram to the client for time synchronization
- Sending **syslog messages** from a controller via UDP or TCP with optional TLS encryption

  The simply designed syslog protocol is used to send messages, warnings or error conditions to a syslog server. syslog is typically used for computer system management and security monitoring and has now established itself as a standard (RFC 5424) in the field of logging.

  The corresponding library emulates the syslog protocol and provides the option of sending messages via UDP or TCP to a syslog server (e.g. SINEC INS). Optionally with TLS encryption.

##### Using Open User Communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
- [Connection configuration (S7-1200, S7-1500, S7-1500T)](#connection-configuration-s7-1200-s7-1500-s7-1500t)
- [Connection parameters (S7-1200, S7-1500, S7-1500T)](#connection-parameters-s7-1200-s7-1500-s7-1500t)

###### Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)

###### Introduction

Open User Communication (OUC) is the name given to a program-controlled communication process for communicating via the integrated PN/IE interface of S7-1200/1500 and S7-300/400 CPUs. Various connection types are available for this communications procedure.

The main feature of Open User Communication is its high degree of flexibility in terms of the data structures transferred. This allows open data exchange with any communicating devices providing they support the connection types available here. Since this communication is controlled solely by instructions in the user program, event-driven connection establishment and termination is possible. Connections can also be modified by the user program during runtime.

For CPUs with an integrated PN/IE interface, the TCP, UDP, and ISO-on-TCP connection types are available for Open User Communication. The communication partners can be two SIMATIC PLCs or a SIMATIC PLC and a suitable third-party device.

###### Instructions for Open User Communication

To create the connections, you have various instructions available after opening in the program editor in the "Instructions &gt; Communication &gt; Open User Communication" task card:

- Compact instructions for sending or receiving data via the integrated functions for establishing and terminating the connection (S7-1200/1500 only):

  - [TSEND_C](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200) (connection establishment/termination, sending)
  - [TRCV_C](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-receive-data-via-ethernet-s7-1200) (connection establishment/termination, receiving)
- Individual instructions for sending and receiving data or for establishing or terminating connections:

  - [TCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200) (connection establishment)
  - [TDISCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tdiscon-terminate-communication-connection-s7-1200-s7-1500) (connection termination)
  - [TSEND](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1) (TCP or ISO-on-TCP: Sending)
  - [TRCV](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv-receive-data-via-communication-connection-s7-1200) (TCP or ISO-on-TCP: Receiving)
  - [TUSEND](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tusend-sending-data-s7-1200-s7-1500) (UDP: Sending)
  - [TURCV](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#turcv-receiving-data-s7-1200-s7-1500) (UDP: Receiving)

###### Connection establishment

For Open User Communication, instructions for establishing and terminating the connection must exist for both communication partners. One communication partner sends its data using TSEND, TUSEND or TSEND_C while the other communication partner receives the data using TRCV, TURCV or TRCV_C.

One of the communication partners starts the connection establishment as the active partner. The other communication partner reacts by starting its connection establishment as the passive partner. If both communication partners have initiated their connection establishment, the communication connection is fully established.

###### Connection configuration

You can specify establishment of the connection via a connection description DB, for example, with the TCON_Param, TCON_IP_v4, or TCON_IP_RFC structure by means of parameter assignment as follows:

- Manually create, assign parameters and write directly to the instruction.
- Supported by connection configuration.

Connection configuration supports the establishment of the connection and should, therefore, be given preference over the other methods.

You specify the following in the connection configuration:

- Connection partner
- Connection type
- Connection ID
- Connection description DB
- Address details according to selected connection type

In addition, you specify here which communication partner activates the connection establishment and which partner establishes a connection passively in response to a request from its communication partner.

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Secure Communication (S7-1200, S7-1500, S7-1500T)](#secure-communication-s7-1200-s7-1500-s7-1500t)

###### Connection configuration (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
- [Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
- [Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
- [Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
- [Deleting connections (S7-1200, S7-1500, S7-1500T)](#deleting-connections-s7-1200-s7-1500-s7-1500t)

###### Overview of connection configuration (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can find the connection configuration in the inspector window of the program editor if you want to program Open User Communication with the communication instructions TSEND_C, TRCV_C or TCON.

Connection configuration supports the flexible functionality of communication programming: The parameters entered for the connection configuration are stored in an automatically generated global DB derived from the TCON_Param, TCON_IP_v4 or TCON_IP_RFC structure. You can modify the connection parameters in this connection description DB.

###### Structure of the connection configuration

The connection configuration is made up of the following components:

![Structure of the connection configuration](images/47089913355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Communication instruction for TCON, TSEND_C or TRCV_C |
| ② | "Configuration" tab in the "Properties" tab |
| ③ | Area navigation of the "Configuration" tab |
| ④ | General properties of the connection parameters |
| ⑤ | Address details of the connection parameters (for selected connection DBs) |

###### "Configuration" tab

Enter the desired connection parameters in the "Configuration" tab. The area navigation of the "Configuration" tab includes the "Connection parameters" group. This group contains the connection configuration. Here, you can enter the parameters for the connections and the address details with system support. Here, you also connect the CONNECT (TCON, TSEND_C, TRCV_C) or ID (TCON, TSEND, TRCV, TUSEND, TURCV) block parameters of the selected communication instructions.

When all the required parameters are assigned, a check mark is set in front of the "Connection parameters" group in the area navigation.

> **Note**
>
> The connection parameter assignment does not check whether the connection IDs and port numbers (TCP, UDP) or TSAPs (ISO-on-TCP, ISO) are unique. When you configure Open User Communication, you should, therefore, make sure that the parameter settings are unique within a device.

---

**See also**

[Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)](#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)
  
[Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)
  
[Connection parameters with structure according to TCON_IP_RFC (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500)
  
[TSEND_C: Send data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)
  
[TRCV_C: Receive data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-receive-data-via-ethernet-s7-1200)
  
[TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1)
  
[TCON: Establish communication connection (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)

###### Description of the connection parameters (S7-1200, S7-1500, S7-1500T)

###### Overview

The following table shows the general connection parameters:

| Parameter | Description |
| --- | --- |
| End point | The names of the local end point and the partner end point are shown.  The local end point is the CPU for which TCON, TSEND_C or TRCV_C is programmed. The local end point is, therefore, always known.  The partner end point is selected from the drop-down list. The drop-down list shows all available possible connection partners including unspecified connection partners for devices whose data is unknown in the project.  For S7-1500, broadcast can be selected as the partner end point (message to all subnet devices). For S7-1500 CPs/CMs, multicast can also be selected as the partner end point (message to a group within the subnet). The connection type is converted automatically to UDP in this case.  As long as no connection partner is selected, all other parameters in the mask are disabled except for the "Connection data" parameter. |
| Interface | The interface of the local end point is displayed. If multiple interfaces are available, e.g., by means of CPs or CMs, the interface can be selected from the drop-down list. To display or select the partner interface, a specified partner end point must first be selected. |
| Subnet | The subnet of the local end point is displayed, provided this exists. The partner subnet is displayed only after the partner end point has been selected.  If at least one of the two connection partners is not connected with a subnet, the two connection partners are connected with each other.  A connection between partners in different subnets is only possible with IP routing. The IP routing settings can be edited in the properties of the relevant Ethernet interfaces. |
| Address | The IP address or the PROFIBUS address of the local end point is displayed, depending on the subnet used. The corresponding address of the partner is displayed only after the partner end point has been selected.  If you have selected an unspecified connection partner, the input box is empty and has a red background. In this case, you must specify a valid IP address/PROFIBUS address. The address type (IP or PROFIBUS) depends on the type of subnet that is set for the local partner.  Broadcast (S7-1500 only): If "Broadcast" is set as the partner end point, a non-editable IP address with host address 255 is entered automatically for the connection partner. The network allocation corresponds to that of the sender. Example: Local IP address 192.168.0.1, partner IP address 192.168.0.255.  Multicast (S7-1500 CPs/CMs only): If "Multicast" is set as the partner end point, the editable IP address 224.0.1.0 is entered automatically for the connection partner. |
| Connection type | Select the connection type you want to use from the "Connection type" drop-down list:  - TCP - ISO-on-TCP - UDP   With the S7-1500, you can also select the ISO connection type at the configuration type of the configured connections for TSEND_C and TRCV_C or TCON.  The connection types can only be used for partners that support the corresponding protocol. |
| Configuration type (S7-1500 and S7-1200 as of FW V4.5) | With S7-1500 and S7-1200 CPUs, two different configuration types can be set for TSEND_C and TRCV_C:  - Programmed connections use program blocks for the connection description. - Configured connections are saved for the configuration and are only created after download to the device in runtime. You can also use the configured connection to select the connection type ISO.   The specified configuration method depends on the selected connection type. If both configuration methods are possible, the programmed connection is preset.  The same configuration method must be set for both connection partners. |
| Connection ID | Enter the connection ID in the input box. You can change the connection ID in the input boxes or enter it directly in TCON.  Ensure that the connection ID assigned is unique within the device. |
| Connection data | The names of the connection description DBs for the connection description structured according to, for example, TCON_IP_v4, TCON_IP_RFC or TCON_Param are displayed in the drop-down lists.  You can use the drop-down list to generate a new data block or to select an existing data block. This data block is filled automatically with the values from the connection configuration. The name of the selected data blocks is entered automatically in the CONNECT block parameter of the selected TSEND_C, TRCV_C or TCON instruction.  From the drop-down list, you can also reference another valid data block. If a DB is referenced using the CONNECT input parameter of the TSEND_C, TRCV_C or TCON extended instructions and this does not correspond to the structure of, for example, a TCON_IP_v4, TCON_IP_RFC or TCON_Param, the drop-down list is shown with no content on a red background. |
| Connection name (only with S7-1500 and S7-1200 as of FW V4.5) | If the configuration type of the configured connections is set for TSEND_C and TRCV_C with S7-1500 and S7-1200 CPUs, the "Connection data" parameter is replaced by the "Connection name" parameter. The name of the configured connection serves here as the connection data.  The drop-down list is still empty after selection of a connection partner. You can use the drop-down list to generate a new connection or to select an existing connection. If needed, a data block is created and automatically filled with the values from the connection configuration. The name of the data block is entered automatically in the CONNECT block parameter of the TSEND_C or TRCV_C instruction.  You can also reference an existing connection from the drop-down list. |
| Active connection establishment | Use the "Active connection establishment" check box to specify the active partner of the Open User Communication (only with TCP and ISO-on-TCP). |
| Port  (only with TCP and UDP) | Address component for a TCP or UDP connection. The default after creating a new TCP connection is 2000.  You can change the port numbers.   The port numbers must be unique on the device! |
| TSAP  (ISO-on-TCP only) | Address component for an ISO-on-TCP connection. The default value after creating a new ISO-on-TCP connection is E0.01.49.53.4F.6F.6E.54.43.50.2D.31 (S7-1200/1500) or E0.02.49.53.4F.6F.6E.54.43.50.2D.31 (S7-300/400).   You can enter the TSAP-ID with an extension or as an ASCII TSAP.   The TSAPs must be unique on the device! |

> **Note**
>
> **UDP connection for the "Broadcast" setting (S7-300/400/1200)**
>
> The parameters of the UDP connection for the "Broadcast" setting for the partner end point are stored in a connection description DB TCON_IP_v4 : With respect to UDP communication with TCON and TUSEND/TURCV , the TCON_IP_v4 is not filled with any partner parameters (value=0). However, the partner address and the partner port are necessary for sending the data and must be entered by the user in the TADDR_Param . The TADDR_Param for UDP communication is referenced by the TUSEND-/TURCV block parameter ADDR . The values for both parameters can be taken from the connection configuration.
>
> The configuration must also be adapted for the other recipients of UDP communication. In order to receive broadcast frames, the partner port must be configured at the receiver end. For this purpose, the RemotePort parameter of the TADDR_Param must be filled at the ADDR block.

> **Note**
>
> **Communication via TSEND_C and TRCV_C (S7-1500 and S7-1200 as of FW V4.5)**
>
> When TSEND_C and TRCV_C are used, a separate TSEND_C and TRCV_C block pair with a configured connection is required for each communication. Multiple TSEND_C and TRCV_C block pairs cannot simultaneously use the same configured connection for communication.
>
> Additional connections for a TSEND_C or TRCV_C instruction can be created in the inspector window for the connection parameters using the appropriate button next to the connection data.
>
> The connections configured using TSEND_C and TRCV_C are displayed in a connection table in the inspector window under "Properties &gt; Configuration &gt; Overview of configured connections" when the TSEND_C or TRCV_C block is selected.

---

**See also**

[Assignment of port numbers (S7-1200, S7-1500, S7-1500T)](#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)
  
[TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
  
[Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)](#ability-to-read-back-connection-description-parameters-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)](#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)
  
[Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)
  
[Connection parameters with structure according to TCON_IP_RFC (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500)
  
[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[Examples of TSAP assignment (S7-1200, S7-1500, S7-1500T)](#examples-of-tsap-assignment-s7-1200-s7-1500-s7-1500t)

###### Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)

The connection configuration for Open User Communication is enabled as soon as a TCON, TSEND_C or TRCV_C instruction for communication is selected in a program block.

###### Requirement

- Your project must contain at least one S7-CPU.
- The program editor is open.
- A network is available.

###### Procedure

To insert the extended instructions for Open User Communication, proceed as follows:

1. Open the task card, pane and folder "Instructions &gt; Communication &gt; Open User Communication".
2. Drag one of the following instructions to a network:

   - TSEND_C
   - TRCV_C
   - TCON

   The "Call options" dialog opens.
3. Edit the properties of the instance DB in the "Call properties" dialog. You have the following options:

   - Change the default name.
   - Select the "Manual" check box to assign your own number.
   - You can also execute the DB as a multi-instance for function blocks.
4. Click "OK" to complete your entry.

###### Result

A corresponding instance DB is created at a single instance for the inserted instruction TSEND_C, TRCV_C or TCON. In the case of a multi-instance, the instance DB of the function block is used.

With TSEND_C, TRCV_C or TCON selected, you will see the "Configuration" tab under "Properties" in the Inspector window. The "Connection parameters" group in area navigation contains the connection parameter assignment that you can now make.

---

**See also**

[Inserting FBD elements using the "Instructions" task card](Creating%20FBD%20programs.md#inserting-fbd-elements-using-the-instructions-task-card)
  
[Inserting LAD elements using the "Instructions" task card](Creating%20LAD%20programs.md#inserting-lad-elements-using-the-instructions-task-card)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Basics of instances](Programming%20basics.md#basics-of-instances)
  
[TSEND_C: Send data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)
  
[TRCV_C: Receive data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-receive-data-via-ethernet-s7-1200)
  
[TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1)
  
[TCON: Establish communication connection (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)

###### Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)

In the connection configuration for Open User Communication, you can create and configure connections of the TCP, UDP or ISO-on-TCP type.

###### Requirements

A CPU exists with a TCON, TSEND_C or TRCV_C communication instruction.

###### Procedure

To create a connection for Open User Communication, follow these steps:

1. Select a TCON, TSEND_C or TRCV_C block of Open User Communication in the program editor.
2. Open the "Properties &gt; Configuration" tab in the inspector window.
3. Select the "Connection parameters" group. Until you select a connection partner, only the drop-down lists for the partner end point and the local connection data are enabled. All other input options are disabled.

   The connection parameters already known are displayed:

   - Name of the local end point
   - Interface of the local end point
   - IP address (for Ethernet subnet) or PROFIBUS address (for PROFIBUS subnet) of the local end point.
4. If you want to use an existing connection description DB, go to step 6. If you want to configure the connection with a new remote connection partner, continue here:

   In the drop-down list box of the partner end point, select a connection partner. You can select an unspecified device or a CPU in the project as the communication partner. Certain connection parameters are then entered automatically.

   The following parameters are set:

   - Name of the partner end point
   - Interface of the partner end point
   - IP address (for Ethernet subnet) or PROFIBUS address (for PROFIBUS subnet) of the partner end point.

   If the connection partners are networked, the name of the subnet is displayed.
5. With S7-1500 or S7-1200 as of firmware version 4.5, you choose between using program blocks or configured connections in the "Configuration type" drop-down list.
6. Select an existing connection description DB in the "Connection data" drop-down list or for configured connections select an existing connection under "Connection name". You can also create a new connection description DB or a new configured connection. When you select an existing connection description DB, the available configuration data is applied and entered in the connection description. Any data of a remote partner that was entered previously is overwritten. Later, you can still select other configured connections or change the names of the connection description DBs in order to create new data blocks:

   - You can also see the selected data block at the interconnection of the CONNECT input parameter of the selected TCON, TSEND_C or TRCV_C instruction.
   - If you have already specified a connection description DB for the connection partner using the CONNECT parameter of the TCON, TSEND_C or TRCV_C instruction, you can either use this DB or create a new DB.
   - If you edit the name of the displayed data block in the drop-down list, a new data block with the changed name but with the same structure and content is generated and used for the connection.
   - Changed names of a data block must be unique in the context of the communication partner.
   - A connection description DB must have the structure TCON_Param, TCON_IP_v4 or TCON_IP_RFC, depending on CPU type and connection.
   - A data block cannot be selected for an unspecified partner.

   Additional values are determined and entered after the selection or creation of the connection description DB or configured connection.

   The following is valid for specified connection partners:

   - ISO-on-TCP connection type
   - Connection ID with default of 1
   - Active connection establishment by local partner
   - TSAP ID   
     for S7-1200/1500: E0.01.49.53.4F.6F.6E.54.43.50.2D.31  
     for S7-300/400: E0.02.49.53.4F.6F.6E.54.43.50.2D.31

   The following is valid for unspecified connection partners:

   - TCP connection type
   - Partner port 2000

   The following applies for a configured connection with a specified connection partner:

   - TCP connection type
   - Connection ID with default of 257
   - Active connection establishment by local partner
   - Partner port 2000

   The following applies for a configured connection with an unspecified connection partner:

   - TCP connection type
   - Local port 2000
7. Enter a connection ID as needed for the connection partner. No connection ID can be assigned to an unspecified partner.
8. Select the desired connection type in the relevant drop-down list. Default values are set for the address details depending on the connection type. You can choose between the following:

   - TCP
   - ISO-on-TCP
   - UDP

   For configured connections with S7-1500, ISO applies in addition.
9. You can edit the input boxes in the address details. Depending on the selected protocol, you can edit the ports (for TCP and UDP) or the TSAPs (for ISO-on-TCP and ISO).
10. Use the "Active connection establishment" check box to set the connection establishment characteristics for TCP, ISO and ISO-on-TCP. You can decide which communication partner establishes the connection actively.

**Note**

You must enter a unique value for the connection ID at a known connection partner. The uniqueness of the connection ID is not be checked by the connection parameter settings and there is no default value entered for the connection ID when you create a new connection.

Changed values are checked immediately for input errors by the connection configuration and entered in the data block for the connection description.

> **Note**
>
> Open User Communication between two communication partners can only work when the program section for the partner end point has been downloaded to the hardware. To achieve fully functional communication, make sure that you load not only the connection description of the local CPU on the device but also that of the partner CPU as well.

---

**See also**

[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
  
[Assignment of port numbers (S7-1200, S7-1500, S7-1500T)](#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)
  
[Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)](#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)
  
[Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)
  
[Connection parameters with structure according to TCON_IP_RFC (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500)
  
[TSEND_C: Send data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)
  
[TRCV_C: Receive data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-receive-data-via-ethernet-s7-1200)
  
[TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1)
  
[TCON: Establish communication connection (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)

###### Deleting connections (S7-1200, S7-1500, S7-1500T)

###### Introduction

The data of a created connection for Open User Communication is stored in a connection description DB. You can delete the connection by deleting the data block containing the connection description.

###### Requirement

You have created an Open User Communication connection.

###### Procedure

To delete a connection, follow these steps:

1. Select a communication partner for Open User Communication in the project tree.
2. Open the "Program blocks &gt; System blocks &gt; Program resources" folder below the selected communication partner.
3. Select the "Delete" command from the shortcut menu of the data block with the connection parameter assignment.

> **Note**
>
> If you are not certain which block to delete, open the extended instruction TCON, TSEND_C or TRCV_C. You will find the name of the data block as the CONNECT input parameter or in the connection parameter assignment as the "Connection data" parameter.
>
> If you only delete the instance DBs of the extended instructions TCON, TSEND_C or TRCV_C, the assigned connections are not deleted as well.

> **Note**
>
> If the connection DB is still being used by other blocks of the extended instructions, then the corresponding calls, their instance DBs, and, if present, the combination blocks TSEND_C and TRCV_C must also be deleted from the block folder, provided they are not used elsewhere.
>
> This action prevents the program from being inconsistent.

###### Result

You have deleted the connection.

> **Note**
>
> Insert an extended instruction TCON, TSEND_C, or TRCV_C again in order to reference an existing connection description with the TCON_Param, TCON_IP_v4, or TCON_IP_RFC structure again via the "Connection data" parameter.

###### Connection parameters (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
- [Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)](#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)
- [Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)
- [Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
- [Connection parameters in accordance with TCON_QDN (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
- [Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
- [Connection parameters with structure according to TCON_IP_RFC (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500)
- [Connection parameters to TCON_Phone (S7-1200, S7-1500, S7-1500T)](#connection-parameters-to-tcon_phone-s7-1200-s7-1500-s7-1500t)
- [Connection parameters to TCON_FDL (S7-1200, S7-1500)](#connection-parameters-to-tcon_fdl-s7-1200-s7-1500)
- [Assignment of port numbers (S7-1200, S7-1500, S7-1500T)](#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)
- [Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)](#ability-to-read-back-connection-description-parameters-s7-1200-s7-1500-s7-1500t)
- [TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
- [Examples of TSAP assignment (S7-1200, S7-1500, S7-1500T)](#examples-of-tsap-assignment-s7-1200-s7-1500-s7-1500t)

###### Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)

###### Introduction

Connection-oriented protocols establish a logical connection to the communication partner before data transmission is started. After the data transmission is complete, they then terminate the connection, if necessary. Connection-oriented protocols are used especially when reliable data transmission is important. Several logical connections can exist over one physical line.

Open User Communication supports the following connection types:

- TCP
- ISO-on-TCP
- ISO (S7-1500 only)
- UDP

Both communication partners must support the same connection type for a connection. If a communication partner does not support a connection of the type ISO-on-TCP, for example, use the connection type TCP instead, if it is supported.

For communication partners that cannot be configured in the TIA Portal, such as third-party devices or PCs, enter "unspecified" for the partner end point during connection parameter assignment. The required connection type for unspecified devices is listed in the respective documentation.

> **Note**
>
> **Connections with ISO**
>
> For S7-1500 CPUs, configured connections of the type ISO can be created using the TSEND_C and TRCV_C instructions. For additional information on these connection types, refer to the general connection descriptions.

###### Characteristics of TCP

TCP is a streaming protocol in which the length of the data stream is transmitted to the receiver so that it can receive the data stream as individual TCP segments. This means no information about the start and end of a message is transmitted during data transmission via a TCP connection. The receiver cannot determine by the received segments of the data stream where one message in the data stream ends and the next one begins. It is therefore recommended that the number bytes to be received (parameter LEN, instruction TRCV/TRCV_C) be assigned the same value as the number of bytes to be sent (parameter LEN, instruction TSEND/TSEND_C).

If the length of the sent data and the length of the expected data do not match, the following occurs:

- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) greater than length of data to be sent (parameter LEN, instruction TSEND/TSEND_C):

  TRCV/TRCV_C copies the received data to the specified receive area (parameter DATA) only after the assigned length is reached. When the assigned length is reached, data of the subsequent job are already being received. As a result, the receive area contains data from two different send jobs. If you do not know the exact length of the first message, you are unable to recognize the end of the first message and the start of the second message.
- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) less than length of data to be sent (parameter LEN, instruction TSEND/TSEND_C):

  TRCV/TRCV_C copies the number of bytes you specified in the LEN parameter to the receive data area (parameter DATA). Then, it sets the NDR status parameter to TRUE (job completed successfully) and assigns RCVD_LEN (amount of data actually received) the value of LEN. With each subsequent call, you receive a further block of the sent data.

A receive area with fixed data length can be specified in the TRCV/TRCV_C instructions with the protocol version of the Ad-hoc mode.

###### Characteristics of ISO-on-TCP

ISO-on-TCP is a message-oriented protocol which detects the end of the message at the receiver end and indicates the data that belongs to the message to the user. This does not depend on the specified reception length of the message. This means that information regarding the length and the end of a message is included during data transmission via an ISO-on-TCP connection.

If the length of the sent data and the length of the expected data do not match, the following occurs:

- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) greater than length of data to be sent (parameter LEN, instruction TSEND/TSEND_C):

  TRCV/TRCV_C copies all the sent data to the receive data area (parameter DATA). Then, it sets the NDR status parameter to TRUE (job completed successfully) and assigns RCVD_LEN (amount of data actually received) the length of the data sent.
- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) less than length of data to be sent (parameter LEN, instruction TSEND/TSEND_C):

  TRCV/TRCV_C does not copy any data to the receive data area (parameter DATA), but instead supplies the following error information: ERROR=1, STATUS=W#16#8088 (destination buffer too small).

###### Characteristics of UDP

UDP is a message-oriented protocol which detects the end of the message at the receiver end and indicates the data that belongs to the message to the user. This does not depend on the specified reception length of the message. This means that information on the length and the end of a message is included during data transmission via a UDP connection.

If the length of the sent data and the length of the expected data do not match, the following occurs:

- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) greater than length of data to be sent (parameter LEN, instruction TUSEND/TSEND_C):

  TURCV/TRCV_C copies all the sent data to the receive data area (DATA parameter). Then, it sets the NDR status parameter to TRUE (job completed successfully) and assigns RCVD_LEN (amount of data actually received) the length of the data sent.
- Length of data to be received (parameter LEN, instruction TRCV/TRCV_C) less than length of data to be sent (parameter LEN, instruction TUSEND/TSEND_C):

  TRCV/TRCV_C copies as much data to the receive data area (parameter DATA) as the LEN parameter requests. No further error message is generated. In this case, the user has to call a T_URCV again in order to receive the remaining bytes.

---

**See also**

[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[TSEND_C: Send data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200)
  
[TRCV_C: Receive data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv_c-receive-data-via-ethernet-s7-1200)
  
[TSEND: Send data via communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)
  
[TRCV: Receive data via communication connection (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv-receive-data-via-communication-connection-s7-1200)
  
[TUSEND: Sending data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tusend-sending-data-s7-1200-s7-1500)
  
[TURCV: Receiving data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#turcv-receiving-data-s7-1200-s7-1500)

###### Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)

###### Data block for connection description

A connection description DB with a structure according to TCON_Param is used for some S7-1200 CPUs when it comes to the assignment of parameters for TCP, UDP and ISO-on-TCP communication connections. The fixed data structure of the TCON_Param contains all the parameters that are needed to establish the connection. The connection description DB is automatically created for a new connection by the connection configuration for Open User Communication when the TSEND_C, TRCV_C or TCON instruction is used.

The CONNECT connection parameter of the instance DBs for TSEND_C, TRCV_C or TCON contains a reference to the data block used.

###### Structure of the connection description according to TCON_Param

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | block_length | UINT | 64 | Length: 64 bytes (fixed) |
| 2 … 3 | id | CONN_OUC | 1 | Reference to this connection (value range: 1 to 4095).  You must specify the value of this parameter for the TSEND_C, TRCV_C or TCON instruction under ID. |
| 4 | connection_type | USINT | 17 | Connection type:   - 17: TCP (17 dec = 0x11 hex) - 18: ISO-on-TCP (18 dec = 0x12 hex) - 19: UDP (19 dec = 0x13 hex) |
| 5 | active_est | BOOL | TRUE | Identifier for the type of connection establishment. FALSE always applies to UDP, since data can be sent and received via local ID.  The following is valid for TCP and ISO-on-TCP:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 6 | local_device_id | USINT | 1 | ID for the local PN/IE interface. |
| 7 | local_tsap_id_len | USINT | 0 | Length of parameter local_tsap_id used, in bytes; possible values:   - 0 or 2, if connection type = 17 (TCP)   Only the value 0 is permissible for the active side. - 2 to 16, if connection type = 18 (ISO-on-TCP) - 2, if connection type = 19 (UDP) |
| 8 | rem_subnet_id_len | USINT | 0 | This parameter is not used. |
| 9 | rem_staddr_len | USINT | 4 | Length of address of partner end point, in bytes:   - 0: unspecified, in other words, parameter rem_staddr is irrelevant. - 4: valid IP address in the parameter rem_staddr  (TCP and ISO-on-TCP only) |
| 10 | rem_tsap_id_len | USINT | 2 | Length of parameter rem_tsap_id used, in bytes; possible values:   - 0 or 2, if connection type = 17 (TCP)   Only the value 0 is permissible for the passive side. - 2 to 16, if connection type = 18 (ISO-on-TCP) - 0, if connection type = 19 (UDP) |
| 11 | next_staddr_len | USINT | 0 | This parameter is not used. |
| 12 … 27 | local_tsap_id | ARRAY [1..16] of BYTE | - | Local address component of connection:   - TCP and UDP: local port no. (possible values: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0);   local_tsap_id[1] = high byte of port no. in hexadecimal notation;   local_tsap_id[2] = low byte of port no. in hexadecimal notation;   local_tsap_id[3-16] = irrelevant - ISO-on-TCP: local TSAP-ID:   local_tsap_id[1] = B#16#E0;   local_tsap_id[2] = rack and slot of local end points (bits 0 to 4: Slot number, bits 5 to 7: rack number);    local_tsap_id[3-16] = TSAP extension, optional   Note: Make sure that every value of local_tsap_id is unique within the CPU. |
| 28 … 33 | rem_subnet_id | ARRAY [1..6] of USINT | - | This parameter is not used. |
| 34 … 39 | rem_staddr | ARRAY [1..6] of USINT | - | TCP and ISO-on-TCP only: IP address of the partner end point, for example, for 192.168.002.003:   - rem_staddr[1] = 192 - rem_staddr[2] = 168 - rem_staddr[3] = 002 - rem_staddr[4] = 003 - rem_staddr[5-6]= irrelevant |
| 40 … 55 | rem_tsap_id | ARRAY [1..16] of BYTE | - | Partner address component of connection  - TCP: partner port no. (possible values: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0);   rem_tsap_id[1] = high byte of port no. in hexadecimal notation;   rem_tsap_id[2] = low byte of port no. in hexadecimal notation;   rem_tsap_id[3-16] = irrelevant - ISO-on-TCP: partner TSAP-ID:   rem_tsap_id[1] = B#16#E0;    rem_tsap_id[2] = rack and slot of partner end point (bits 0 to 4: Slot number, bits 5 to 7: rack number);   rem_tsap_id[3-16] = TSAP extension, optional - UDP: This parameter is not used. |
| 56 … 61 | next_staddr | ARRAY [1..6] of BYTE | - | This parameter is not used. |
| 62 … 63 | spare | WORD | W#16#0000 | Reserved. |

> **Note**
>
> **TCON_Param for S7-1500 CPU**
>
> The connection description DB with the structure according to TCON_Param is also supported by S7-1500 CPUs for migration reasons. However, we recommend that you use the new structures TCON_IP_v4 and TCON_IP_RFC.

> **Note**
>
> **TCON_Param for S7-1500 R/H CPUs**
>
> The connection description DB with the structure according to TCON_Param is not supported by S7-1500 RH CPUs.

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)](#ability-to-read-back-connection-description-parameters-s7-1200-s7-1500-s7-1500t)
  
[Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
  
[Assignment of port numbers (S7-1200, S7-1500, S7-1500T)](#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

###### Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)

###### Data block for connection description

A connection description DB with a structure according to TCON_IP_v4 is used for CPUs of S7-1200 V4.0 and higher and S7-1500 to assign parameters for TCP and UDP communication connections. The fixed data structure of the TCON_IP_v4 contains all parameters that are required to establish the connection. The connection description DB is automatically created for a new connection by the connection configuration for Open User Communication when the TSEND_C, TRCV_C or TCON instruction is used.

The CONNECT connection parameter of the instance DBs for TSEND_C, TRCV_C or TCON contains a reference to the data block used.

###### Structure of the connection description according to TCON_IP_v4

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | 64 | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | 1 | Reference to this connection (value range: 1 to 4095).  You must specify the value of this parameter for the TSEND_C, TRCV_C or TCON instruction under ID. |
| 4 | ConnectionType | BYTE | 11 | Connection type:   - 11: TCP (11 dec = 0x0B hex) - 17: TCP (17 dec = 0x11 hex) - 19: UDP (19 dec = 0x13 hex)   In this case, only passive connection establishment is permitted on both sides. This means that the parameter "ActiveEstablished" must have the value FALSE on both sides. |
| 5 | ActiveEstablished | BOOL | TRUE | Identifier for the type of connection establishment:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 6 … 9 | RemoteAddress | ARRAY [1..4] of BYTE | - | - IP address of the partner end point, for example, for 192.168.0.1:    - addr[1] = 192   - addr[2] = 168   - addr[3] = 0   - addr[4] = 1 - Multicast address of an IPv4 multicast group (for S7-1500-CPUs as of firmware version V2.0 or V2.1 and higher when using TSEND_C/TRCV_C) |
| 10 … 11 | RemotePort | UINT | 2000 | Port number of the remote connection partner (range of values: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0. 0 is also permitted in the passive connection establishment). |
| 12 … 13 | LocalPort | UINT | 2000 | Port number of the local connection partner (value range: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0. 0 is also permitted in the active connection establishment). |

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)](#ability-to-read-back-connection-description-parameters-s7-1200-s7-1500-s7-1500t)
  
[Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Assignment of port numbers (S7-1200, S7-1500, S7-1500T)](#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

###### Connection parameters according to TCON_IP_V4_SEC (S7-1500)

###### Data block for connection description

To configure the communication connections for TCP over IPv4 with Secure Communication, use the following modules:

- CPUs with connection description DB with the structure of the SDT TCON_IP_V4_SEC:

  - S7-1200 as of firmware V4.4
  - S7-1500 as of firmware V2.0
- Also optional for the following CPs:

  - CP 1243-1 as of firmware V3.2
  - CP 1243-8 IRC as of firmware V3.2
  - CP 1543‑1 as of firmware V2.0
  - CP 1545‑1
  - CP 1543SP-1

> **Note**
>
> **Non-secure TCP or UDP connection over IPv4**
>
> You can also use SDT TCON_IP_V4_SEC for a non-secure TCP or UDP connection over IPv4.

The connection parameter CONNECT of the instance DBs for TCON contains a reference to the data block used.

###### Structure of the connection description according to TCON_IP_V4_SEC

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 15 | ConnPara | TCON_IP_v4 | - | SDT for the connection parameters  Information about the interface_id:  - If you leave the interface_id at the preset value of 0, the operating system of the CPU evaluates the remote IP address and the IP routes existing locally and then specifies an Industrial Ethernet interface of the CPU for establishing the secure OUC connection.  In this case, the diagnostics data is always assigned to the first Industrial Ethernet interface of the CPU. - If you specify the hardware identifier of an Industrial Ethernet interface of the CPU or of a CP as interface_id, the secure OUC connection is established via the associated Industrial Ethernet interface. |
| 16 | ActivateSecureConn | BOOL | FALSE | Activation of Secure Communication for this connection  If this parameter has the value FALSE, the subsequent security parameters are irrelevant, meaning that the connection is non-secure. You can set up a non-secure TCP or UDP connection in this case. |
| 17 | TLSServerReqClientCert | BOOL | FALSE | Only for the server side: Request for an X.509-V3 certificate from the TLS client |
| 18 ... 19 | ExtTLSCapabilities | WORD | 16#0 | - Bit 0: Only for the client side. A set bit means that the client validates the alternative name of the certificate subject (subjectAlternateName) in the X.509-V3 certificate of the server to check the identity of the server. The certificates are checked when the connection is established. - Bit 1 to 15: reserved for future upgrades |
| 20 ... 23 | TLSServerCertRef | UDINT | 0 | - Server side: ID of its own X.509-V3 certificate - Client side: ID of the X.509-V3 certificate (usually a CA certificate) that is used by the TLS client to validate the TLS server authentication. If this parameter is 0, the TLS client uses all the (CA) certificates currently loaded in the client certificate store to validate the server authentication. |
| 24 … 27 | TLSClientCertRef | UDINT | 0 | - Client side: ID of its own X.509-V3 certificate - Server side: ID of the X.509-V3 certificate (or a group of X.509-V3 certificates) that is used by the TLS server to validate the TLS client. If this parameter is 0, the TLS server uses all (CA) certificates currently loaded in the server certificate store to validate the client authentication. |

---

**See also**

[Connection parameters with structure according to TCON_IP_v4 (S7-1200, S7-1500)](#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)
  
[Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)](#secure-ouc-between-two-s7-1500-cpus-s7-1500-s7-1500t)

###### Connection parameters in accordance with TCON_QDN (S7-1500)

###### Data block for connection description

To configure the communication connections for TCP and UDP via the fully qualified domain name, use the following CPUs with connection description DB with the structure according to TCON_QDN:

- S7-1200-CPUs as of firmware V4.4
- S7-1500-CPUs as of firmware V2.0

The connection parameter CONNECT of the instance DBs for TCON contains a reference to the data block used.

> **Note**
>
> **TCON_DNS structure**
>
> TCON_QDN replaces TCON_DNS. Therefore use only connection description DBs with a structure according to TCON_QDN.

###### Structure of the connection description in accordance with TCON_QDN

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | interface_id | HW_ANY | 0 | S7-1200-CPUs as of firmware V4.4 / S7-1500-CPUs as of firmware V2.8:  - InterfaceId of a plugged CP:   - With CPs of S7-1500 as of firmware V2.2   - With CPs of S7-1200 as of firmware V3.2   - With CPs of ET 200SP as of firmware V2.1 - 0 (only S7-1500 CPUs as of firmware V2.8): As long as the connection is established, it is assigned to the first PROFINET interface. As soon as the connection is established successfully, it is assigned to the used PROFINET interface.   S7-1200-CPUs earlier than V4.4 / S7-1500-CPUs earlier than firmware V2.8:  - Parameter irrelevant for S7-1500 CPUs with the exception of S7-1500 F-CPUs 0 (only S7-1500 F-CPUs) - As of firmware version 2.0 of the S7-1500 CPU, the following applies: As long as the connection is established, it is assigned to the first PROFINET interface. As soon as the connection is established successfully, it is assigned to the used PROFINET interface. |
| 2 … 3 | id | CONN_OUC | 1 | Reference to this connection (value range: 1 to 4095).  You must specify the value of this parameter for the TCON instruction under ID. |
| 4 | connection_type | BYTE | 11 | Connection type:   - 11: TCP (11 dec = 0x0B hex) - 19: UDP (19 dec = 0x13 hex)   For compatibility and migration reasons, the CPU S7-1500 also allows the values of the connection description DB with a structure according to TCON_Param. For the connection type TCP, the entry 17 is therefore also valid (17 dec = 0x11 hex). |
| 5 | active_established | BOOL | TRUE | Identifier for the type of connection establishment:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 6 … 261 | remote_qdn | STRING | - | Fully qualified domain name of the partner end point, which must finish with "."  Please note that in a SIMATIC network, the name including the concluding dot must not exceed 254 characters. |
| 262 … 263 | remote_port | UINT | 2000 | Port number of the remote connection partner (range of values: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0. 0 is also permitted in the passive connection establishment). |
| 264 … 265 | local_port | UINT | 2000 | Port number of the local connection partner (value range: 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0, 1 to 65535 for S7-1500 as of firmware version V3.0. 0 is also permitted in the active connection establishment). |

###### Connection parameters in accordance with TCON_QDN_SEC (S7-1500)

###### Data block for connection description

To configure the communication connections for TCP via the fully qualified domain name with Secure Communication, use the following CPUs with a connection description DB with the structure of the SDT TCON_QDN_SEC:

- S7-1200-CPUs as of firmware V4.4
- S7-1500-CPUs as of firmware V2.0

> **Note**
>
> **Non-secure TCP or UDP connection over the fully qualified domain name**
>
> You can also use the TCON_QDN_SEC SDT for a non-secure TCP or UDP connection over the fully qualified domain name.

The connection parameter CONNECT of the instance DBs for TCON contains a reference to the data block used.

###### Structure of the connection description according to TCON_QDN_SEC

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 271 | ConnPara | TCON_QDN | - | Connection parameter |
| 272 | ActivateSecureConn | BOOL | FALSE | Activation of secure communication for this connection  If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case. |
| 273 | TLSServerReqClientCert | BOOL | FALSE | Only for the server side: Request for an X.509-V3 certificate from the TLS client |
| 274 ... 275 | ExtTLSCapabilities | WORD | 16#0 | - Bit 0: Only for the client side. A set bit means that the client validates the subjectAlternateName in the X.509-V3 certificate of the server to check the identity of the server. The certificates are checked when the connection is established. - Bit 1 to 15: reserved for future upgrades |
| 276 ... 279 | TLSServerCertRef | UDINT | 0 | - Server side: ID of its own X.509-V3 certificate - Client side: ID of the X.509-V3 certificate (usually a CA certificate) that is used by the TLS client to validate the TLS server authentication. If this parameter is 0, the TLS client uses all (CA) certificates currently loaded in the client certificate store to validate the server authentication. |
| 280 … 283 | TLSClientCertRef | UDINT | 0 | - Client side: ID of its own X.509-V3 certificate - Server side: ID of the X.509-V3 certificate (or a group of X.509-V3 certificates) that is used by the TLS server to validate TLS client authentication. If this parameter is 0, the TLS server uses all (CA) certificates currently loaded in the server certificate store to validate the client authentication. |

---

**See also**

[Connection parameters in accordance with TCON_QDN (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
  
[Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)](#secure-ouc-between-two-s7-1500-cpus-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as a TLS client to an external PLC (TLS server) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-a-tls-client-to-an-external-plc-tls-server-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as TLS server to an external PLC (TLS client) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-tls-server-to-an-external-plc-tls-client-s7-1500-s7-1500t)
  
[Secure OUC via e-mail (S7-1500, S7-1500T)](#secure-ouc-via-e-mail-s7-1500-s7-1500t)

###### Connection parameters with structure according to TCON_IP_RFC (S7-1200, S7-1500)

###### Data block for connection description

A connection description DB with a structure according to TCON_IP_RFC is used for CPUs of S7-1200 V4.0 and higher and S7-1500 to assign parameters to ISO-on-TCP communication connections. The fixed data structure of the TCON_IP_RFC contains all parameters that are required to establish the connection. The connection description DB is automatically created for a new connection by the connection configuration for Open User Communication when the TSEND_C, TRCV_C or TCON instruction is used.

The CONNECT connection parameter of the instance DBs for TSEND_C, TRCV_C or TCON contains a reference to the data block used.

###### Structure of the connection description according to TCON_IP_RFC

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | interface_id | HW_ANY | 64 | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | id | CONN_OUC | 1 | Reference to this connection (value range: 1 to 4095).  You must specify the value of this parameter for the TSEND_C, TRCV_C or TCON instruction under ID. |
| 4 | connection_type | BYTE | 12 | Connection type 12: ISO-on-TCP (12 dec = 0x0C hex)  For compatibility and migration reasons, the CPU S7-1500 also allows the values of the connection description DB with a structure according to TCON_Param. For the connection type ISO-on-TCP, the entry 18 is therefore also valid (18 dec = 0x12 hex). |
| 5 | active_established | BOOL | TRUE | Identifier for the type of connection establishment:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 8 … 11 | remote_address | ARRAY [1..4] of BYTE | - | IP address of the partner end point, for example, for 192.168.0.1:   - addr[1] = 192 - addr[2] = 168 - addr[3] = 0 - addr[4] = 1 |
| 12 … 45 | remote_tselector | TSelector | - | TSelector of the remote connection partner:  - TSelLength = Value range 0 to 32 as UINT - TSel[1-32] = Value range each 0 to 255 in bytes |
| 46 … 79 | local_tselector | TSelector | - | TSelector of the local connection partner:  - TSelLength = Value range 0 to 32 as UINT - TSel[1-32] = Value range each 0 to 255 in bytes |

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)](#ability-to-read-back-connection-description-parameters-s7-1200-s7-1500-s7-1500t)
  
[Basic principles for programming of data blocks](Programming%20data%20blocks.md#basic-principles-for-programming-of-data-blocks)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

###### Connection parameters to TCON_Phone (S7-1200, S7-1500, S7-1500T)

###### System data types TCON_... for telecontrol connections

TCON_PHONE is used as a connection description for the following types of connection:

- In mobile wireless CPs of the S7‑1200 for connections of Open User Communication to transfer SMS over TCON / TDISCON / TSEND or TSEND_C.
- With the CP 1242‑7 for telecontrol connections to SMS clients with TC_CON

To configure establishment of a connection using one of the previously mentioned instructions, the CONNECT parameter of the instruction is used for the connection description.

The connection description is defined by the structure of the system data type (SDT) TCON_Phone. The structure of the relevant SDT contains the parameters necessary to establish the connection with the remote communications partner.

###### Creating a DB of the type TCON_Phone

You need to type in the data type of the DB with the keyboard. It is not displayed in a selection list. Upper or lower case is unimportant when entering the data type.

Follow these steps to create the DB:

1. Create a data block of the type "Global DB" with block access "Standard".

   To do so, deactivate the property "Optimized access" in the block properties (shortcut menu) in the "Attributes" tab.
2. Create an SDT in the parameter configuration table of the DB.
3. Enter the following name in the declaration table of the DB in the cell of the data type: TCON_Phone

   The SDT and its parameters are created (see below).
4. Configure the parameters described below.

Reserved bits are not displayed.

###### System data type TCON_Phone for SMS connections

> **Note**
>
> **SMS text**
>
> - Programmed SMS texts for SMS messages to be sent are accessed using the DATA parameter of the TC_SEND instruction.
> - The text of a received SMS message is assigned to the address area of the CPU by the DATA parameter of the TC_RECV instruction.

Parameters of TCON_Phone

| Byte | Parameter | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | InterfaceId | HW_ANY |  | Reference to the local interface (telecontrol interface or Ethernet interface of the CP &gt; "Hardware identifier") |
| 2 ... 3 | ID | CONN_OUC | 1...07FF<sub>h</sub> | Reference to the local mobile wireless connection. The ID is assigned and must be unique within the CPU.  Note on telecontrol connections of the CP 1242-7: The same value as that of the parameter ID of the TC_CON instruction must be used here. |
| 4 | ConnectionType | Byte | W#16#0E | Protocol variant 14 (E<sub>h</sub>): SMS connection |
| 5 | ActiveEstablished | Bool |  | Identifier for the type of connection establishment (not relevant for the CP 1242-7):  - 0: Passive connection establishment (not relevant here) - 1: Active connection establishment |
| 6...7 | - | - | - | - reserviert - |
| 8 ... 31 | PhoneNumber | String[22] |  | Call number of the connection partner  Permitted values: Plus character (+) and numbers  Note the exact notation of the international dialing code of the relevant phone number assigned by the network provider ("+" character or zeros).  Note on the telecontrol connections of the CP 1242-7: if the parameter PhoneNumber is not entered, no connection partner is specified and SMS messages can be received by all authorized connection partners. Without an entry, TC_RECV initially delivers the oldest received SMS messages during startup. |

###### Connection parameters to TCON_FDL (S7-1200, S7-1500)

###### System data block (SDT) for FDL connection description

In order to parameterize an FDL connection for the CM 1542‑5, a connection description DB with an SDT to TCON_FDL is used. The fixed data structure of the STD contains all parameters that are required to establish the connection. The connection description SDT has to be created in a created DB.

The connection parameter CONNECT of the instance DBs for TSEND_C or TRCV_C contains a reference to the data block used.

The following types of FDL connections can be established:

- **Configured FDL connections**

  These connection types are configured in the STEP 7 program editor, see [Setting up communication over FDL](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#setting-up-communication-over-fdl-s7-300-s7-400). TSEND_C and TRCV_C are used as blocks.

  - Specified connection

    Fully configured connection between two masters
  - Unspecified connection

    Configured connection with an unspecified partner
- **Programmed FDL connections**

  These connection types cannot be configured in the STEP 7 program editor. Instead these connection types require the calling the TCON instruction together with TSEND/TRCV or TUSEND/TURCV, respectively.

  - Unspecified Layer 2 connection

    Programmed FDL connection with an unspecified partner with free Layer 2 access
  - Broadcast connection

    Connection with all connected partners
  - Multicast connection

    Connection with several defined partners

If specific settings for the individual connection types are required, this is mentioned at the subsequent parameters of the SDT.

###### Structure of the connection description "TCON_FDL" for configured connections

The table below describes the connection parameters for the following configured FDL connections:

- Specified connection
- Unspecified connection

| Byte | Parameter | Data type | Value range / Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceId | HW_ANY | 0 .. 65535 | Hardware identifier of the local interface |
| 2 … 3 | ID | CONN_OUC | 0 .. 4095 | Reference to this connection in accordance with connection configuration |
| 4 | ConnectionType | Byte | 15 | Connection type: 0x15 (dec. 21) for FDL |
| 5 | ActiveEstablished | Bool | FALSE | ID for the manner in which the connection is established  - FALSE: Passive connection establishment - TRUE: Active connection establishment   The parameter value is not processed further. |
| 5 | ServiceId | Byte | 0 .. 2 | Identifier of the data transfer service  - 0: Automatic default with selection of the service in accordance with the receiver configured in the connection description   Only SDA is used in this setting for configured connections. - 1: Send Data Acknowledged (SDA) - for active connections between two masters   Use this setting for unspecified connections. - 2: Send Data Non-Acknowledged (SDN) - for multicast / broadcast |
| 6 … 9 | RemotePBAddress | Byte | 0 .. 126 | PROFIBUS address of the connection partner  - Is used for specified connections by the connection configuration. - Has to be stated explicitly for unspecified connections. |
| 6 … 9 | LocalPBAddress | Byte | 0 .. 126 | Own (local) PROFIBUS address  Is assigned automatically by the interface configuration. |
| 10 … 11 | RemoteLSAP | Byte | 2 .. 32 | LSAP (link layer service access point) of the connection partner  Has to be stated explicitly for configured connections. |
| 12 … 13 | LocalLSAP | Byte | 2 .. 32 | Own (local) LSAP  Has to be stated explicitly for configured connections. |

###### Structure of the connection description "TCON_FDL" for programmed connections

The table below describes the connection parameters for the following programmed FDL connections:

- Unspecified Layer 2 connection
- Broadcast connection
- Multicast connection

| Byte | Parameter | Data type | Value range / Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceId | HW_ANY | 0 .. 65535 | Hardware identifier of the local interface |
| 2 … 3 | ID | CONN_OUC | 0 .. 4095 | Reference to this connection  Reference to the value of the ID generated by TCON.  Specify the value for TSEND / TRCV or TUSEND / TURCV at the parameter ID. |
| 4 | ConnectionType | Byte | 15 | Connection type: 0x15 (dec. 21) for FDL |
| 5 | ActiveEstablished | Bool | FALSE | ID for the manner in which the connection is established  - FALSE: Passive connection establishment - TRUE: Active connection establishment   The parameter value is not processed further. |
| 5 | ServiceId | Byte | 0 .. 2 | Identifier of the data transfer service  - 0: Automatic selection of the service. Not to be used for programmed connections. - 1: Send Data Acknowledged (SDA) - for active connections between two masters - 2: Send Data Non-Acknowledged (SDN) - for multicast / broadcast   "1" or "2" has to be programmed for programmed connections. |
| 6 … 9 | RemotePBAddress | Byte | 0 .. 127 | PROFIBUS address of the connection partner  Specify the address if TSEND or TUSEND is used.  The value is set by the user program for TRCV or TURCV.  - For broadcast / multicast: 127 |
| 6 … 9 | LocalPBAddress | Byte | 0 .. 126 | Own (local) PROFIBUS address  Is assigned automatically by the interface configuration. |
| 10 … 11 | RemoteLSAP | Byte | 2 .. 32, 63 | LSAP (link layer service access point) of the connection partner  Specify the address if TSEND or TUSEND is used:  - For unspecified Layer 2 connections: 2 .. 32 - For broadcast: 63 - For multicast: Use the same values as "LocalLSAP".   The value is set by the user program for TRCV or TURCV. |
| 12 … 13 | LocalLSAP | Byte | 2 .. 32 | Own (local) LSAP  Is to be assigned by the program. |

###### Assignment of port numbers (S7-1200, S7-1500, S7-1500T)

###### Introduction

TCP and UDP communication uses ports as part of the network address. Each connection has two ports, one on the client side and one on the server side. Possible port numbers are 0 to 65535.

For the port numbers of programmable connections, for S7-1200 and S7-1500 with firmware version &lt; V3.0, values from 1 to 49151 are allowed, for S7-1500, from firmware version V3.0, 65535. You can assign any port number within this range. When an Open User Communication is created, the value 2000 is automatically assigned as the port number. The value 0 continues to be permitted for the passive connection establishment in the remote port and in the active connection establishment in the local port.

> **Note**
>
> Port numbers must be unique. The connection configuration or a corresponding block call is rejected with an error if the port numbers are assigned twice.

###### Overview of port numbers

The following table shows a general summary of the port numbers.

| Port number | Description |
| --- | --- |
| 0 to 1023 | "Well-known Ports" or system ports |
| 1024 … 65535 | Registered ports or user ports |
| 49152 to 65535 | Dynamic ports or "private ports" |

> **Note**
>
> The user usually specifies the value 0 for the local port on the active connection end point for UDP/TCP. In this case, the CPU operating system selects the next available port above 49151. The partner port usually has the default 0 with the passive connection end point. The corresponding parameter is disabled in the connection configuration.

###### OUC server with passive connection establishment

In the case of an OUC server application, the CPU waits for the connection to be established by the remote partner (passive connection establishment).

Possible local port range of the CPU that can be addressed by the remote partner:

- Programmed connection using the TCON instruction:

  - 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0
  - 1...65535 for S7-1500 from firmware version V3.0 or higher
- Configured connections via TIA Portal: 1 to 65535

###### OUC client with active connection establishment

In the case of an OUC client application, the CPU establishes the connection to the remote partner (active connection establishment).

Possible local port range of the CPU:

- Programmed connection via TCON instruction defined by the user:

  - 1 to 49151 for S7-1200 and S7-1500 with firmware version &lt; V3.0
  - 1...65535 for S7-1500 from firmware version V3.0 or higher
- Programmed connection using the TCON instruction dynamically managed by the CPU: 49152 to 65535
- Configured connections via TIA Portal defined by the user: 1 to 65535:

---

**See also**

[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)

###### Ability to read back connection description parameters (S7-1200, S7-1500, S7-1500T)

###### Changing parameter values in the connection description

The connection description for exactly one connection of the Open User Communication is entered from the connection configuration in the connection description DB.

You can change the parameter values of the connection description DB outside of the connection configuration in the user program. Connection description DBs containing values you changed subsequently can be read back from the connection configuration. Under "Properties &gt; Configuration &gt; Connection parameters", the inspector window displays only the connection parameters stored in the connection description DB.

> **Note**
>
> You can only change the values in the running user program if the instructions TCON, TSEND_C or TRCV_C are not being processed and the referenced connection is not established.

The connection configuration does not support nested entries of connection descriptions in DB types that can only be found via offset referencing (for example, Global-DB).

The structure of the connection description cannot be changed.

###### Ability to read back individual connection parameters

For the "Address" parameter of the communication partner in a TCP or ISO-on-TCP connection, its IP address is displayed from the "rem_staddr" parameter of the connection description.

The following values can also be reloaded from the connection description:

- Connection type
- Local connection ID
- Active/passive connection establishment (only with UDP)
- Local TSAP (ISO-on-TCP only)
- Partner TSAP (ISO-on-TCP only)
- Local port (only with TCP and UDP)
- Partner port (only with TCP)

The values of the connection ID parameters of the communication partner, the connection data, as well as the connection establishment, are not included in the connection description in the local connection description DB. Consequently, these parameters cannot be displayed when the connection configuration is reopened. The connection establishment of the partner results from the local connection establishment and is therefore also displayed.

A new communication partner can be selected at any time in the "Partners" drop-down list box.

When a CPU recognized in the project is selected as a specified communication partner, the entry options for the connection ID and the connection data are shown again.

---

**See also**

[Connection parameters with structure according to TCON_Param (S7-1200, S7-1500, S7-1500T)](#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)
  
[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)

###### TSAP structure (S7-1200, S7-1500, S7-1500T)

###### Introduction

For an ISO-on-TCP connection, Transport Service Access Points (TSAPs) must be assigned for both communication partners. TSAP IDs are assigned automatically after an ISO-on-TCP connection is created. To ensure the uniqueness of TSAP IDs within a device, you can change the preassigned TSAPs in the connection parameter assignment.

###### Structure of TSAPs

You must comply with certain rules when assigning TSAPs. A TSAP must contain a certain number of bytes, which are able to be displayed and entered as hexadecimal values (TSAP-ID) or as ASCII characters (ASCII-TSAP):

![Structure of TSAPs](images/14916963851_DV_resource.Stream@PNG-en-US.png)

Entries or changes of the TSAP-ID or the ASCII-TSAP in the corresponding entry fields always take effect in the other display format as well.

If a TSAP contains no valid ASCII characters, the TSAP is displayed only as TSAP-ID and not as ASCII-TSAP. This is the case after a connection is created. The first two hex characters as TSAP-ID identify the communication type and the rack/slot. Because these characters are not valid ASCII characters for a CPU, the ASCII-TSAP is not displayed in this case.

![Structure of TSAPs](images/14916967307_DV_resource.Stream@PNG-en-US.png)

In addition to the rules for length and structure of TSAPs, you must also ensure the uniqueness of the TSAP-ID. The assigned TSAPs are not automatically unique.

###### Length and content of TSAPs

Structure of the TSAP ID with TSAP extension:

- Valid for CPU S7-1200 firmware V1

  Length = 2 to 16 bytes

  x_tsap_id[0] = 0xE0 (Open User Communication)

  x_tsap_id[1] (bits 0 to 4) = slot number of CPU

  x_tsap_id[1] (bits 5 to 7) = rack number of CPU

  x_tsap_id[2...15] = any characters (TSAP extension, optional)

  (x = loc (local) or x = rem (partner))
- Valid for CPU S7-1500 and S7-1200 firmware as of V2

  Length = 2 to 16 bytes

  x_tsap_id[0] = 0xE0 (Open User Communication)

  x_tsap_id[1] = 0x00 to 0xFF

  x_tsap_id[2...15] = any characters (TSAP extension, optional)

  (x = loc (local) or x = rem (partner))

Structure of the TSAP ID as ASCII TSAP:

- Valid for CPU S7-1200 firmware V1

  Length = 3 to 16 bytes

  x_tsap_id[0...2] = 3 ASCII characters (0x20 to 0x7E)

  x_tsap_id[3...15] = any characters (optional)

  (x = loc (local) or x = rem (partner))
- Valid for CPU S7-1200 firmware as of V2

  Length = 3 to 16 bytes

  x_tsap_id[0...2] for active connection = 3 ASCII characters (0x00 to 0xFF) or any bit string*

  x_tsap_id[0...2] for passive connection = 3 ASCII characters (0x20 to 0x7E) or any bit string*

  x_tsap_id[3...15] = any characters (optional)

  (x = loc (local) or x = rem (partner))
- Valid for S7-1500 CPU

  Length = 3 to 16 bytes

  x_tsap_id[0...2] = 3 ASCII characters (0x00 to 0xFF) or any bit string*

  x_tsap_id[3...15] = any characters (optional)

  (x = loc (local) or x = rem (partner))

* ASCII character strings must not start with "SIMATIC-"

The following table shows the schematic structure of various TSAP IDs:

| TSAP-ID | tsap_id_len | tsap_id[0] | tsap_id[1] | tsap_id[2] | tsap_id[3..15] |
| --- | --- | --- | --- | --- | --- |
| ...with extension  (CPU S7-1200 firmware V1) | 2...16 bytes | 0xE0 | 0x01 or 0x02 or 0x00* | Extension (optional) | Extension (optional) |
| ...with extension  (CPU S7-1500, S7-1200 firmware as of V2) | 2...16 bytes | 0xE0 | 0x00...0xFF | Extension (optional) | Extension (optional) |
| ...as ASCII-TSAP  (CPU S7-1200 firmware V1) | 3...16 bytes | 0x20...0x7E | 0x20...0x7E | 0x20...0x7 | Any (optional) |

* An S7-1200 CPU is normally inserted on rack 0 and slot 1, and an S7-300/400 CPU on rack 0 and slot 2. For this reason, hex value 01 or 02 is valid for the second position of the TSAP ID with extension. If the connection partner is an unspecified CPU, for example, a third-party device, the hex value 00 is also permissible for the slot address.

> **Note**
>
> For unspecified communication partners, the local TSAP-ID and the partner TSAP-ID can have a length of 0 to 16 bytes, in which all hex values from 00 to FF are permitted.

###### ASCII code table for entry of ASCII TSAP

When entering ASCII TSAPs with the hexadecimal values from 20 to 7E, only the following characters are permitted:

| Code | ..0 | ..1 | ..2 | ..3 | ..4 | ..5 | ..6 | ..7 | ..8 | ..9 | ..A | ..B | ..C | ..D | ..E | ..F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **2..** |  | ! | " | # | $ | % | &amp; | ’ | ( | ) | * | + | , | - | . | / |
| **3..** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | : | ; | &lt; | = | &gt; | ? |
| **4..** | @ | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| **5..** | P | Q | R | S | T | U | V | W | X | Y | Z | [ | \ | ] | ^ | _ |
| **6..** | ` | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o |
| **7..** | p | q | r | s | t | u | v | w | x | y | z | { | | | } | ~ |  |

---

**See also**

[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Examples of TSAP assignment (S7-1200, S7-1500, S7-1500T)](#examples-of-tsap-assignment-s7-1200-s7-1500-s7-1500t)

###### Examples of TSAP assignment (S7-1200, S7-1500, S7-1500T)

The following examples show the processing of the TSAPs for CPUs of the S7-1200/1500 (CPU on slot 1) under various points of view:

- Example 1: Creating a new connection for PLC-PLC communication
- Example 2: Entry of a local ASCII-TSAP
- Example 3: Entry of a TSAP extension in the TSAP-ID
- Example 4: Incorrect editing of the TSAP-ID
- Example 5: Entry of an ASCII-TSAP via the "TSAP-ID" entry field

###### Example 1: Creating a new connection for PLC-PLC communication

Once you have created a new connection with two PLCs for the Open User Communication, the TSAP extension "ISOonTCP-1" is assigned automatically.

This TSAP extension produces the TSAP-ID E0.01.49.53.4F.6F.6E.54.43.50.2D.31, which is entered automatically in the connection description DB and in the entry fields of the local and the partner TSAP. The entry fields of the ASCII-TSAPs remain empty:

|  | Local TSAP | Partner TSAP |
| --- | --- | --- |
| TSAP (ASCII) |  |  |
| TSAP-ID | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 |

You can change the values in the entry fields of the TSAP-ID and the ASCII-TSAP at any time.

The entry field of the TSAP-ID shows the complete TSAP stored in the data block of the connection description. The TSAP-ID with TSAP extension, which is limited to 16 characters, is not displayed in the "TSAP (ASCII)" entry field because the character E0 does not represent a valid character for the ASCII-TSAP.

If the displayed TSAP-ID is a valid ASCII-TSAP, it is displayed in the "TSAP (ASCII)" entry field.

Changes in the entry fields for TSAP-ID and ASCII-TSAP affect the other field.

###### Example 2: Entry of a local ASCII-TSAP

If you have created a new connection and assigned an ASCII value for the local TSAP in the "TSAP (ASCII)" entry field, for example, "ISOonTCP-1", the resulting TSAP-ID is created automatically.

When you exit the "TSAP (ASCII)" entry field, the number of ASCII characters is checked automatically for compliance with the limit (3 to 16 characters) and the resulting TSAP-ID is entered into the corresponding entry field:

|  | Local TSAP | Partner TSAP |
| --- | --- | --- |
| TSAP (ASCII) | ISOonTCP-1 |  |
| TSAP-ID | 49.53.4F.6F.6E.54.43.50.2D.31 | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 |

###### Example 3: Entry of a TSAP extension in the TSAP-ID

If, following creation of a connection and entry of an ASCII-TSAP (see examples 1 and 2) in the entry field of the local TSAP-ID, you add the prefix "E0.01" to the TSAP value, the ASCII-TSAP will no longer be displayed when the entry field is exited.

|  | Local TSAP | Partner TSAP |
| --- | --- | --- |
| TSAP (ASCII) |  |  |
| TSAP-ID | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 |

Once you have exited the entry field of the TSAP-ID, a check is performed automatically to determine whether the first character of the TSAP-ID is a valid ASCII character. Since the character "E0" now present in the TSAP-ID is not a valid character for the ASCII-TSAP, the "TSAP (ASCII)" entry field no longer displays an ASCII-TSAP.

If a valid ASCII character is used, the check for compliance with the length specification of 2 to 16 characters follows.

###### Example 4: Incorrect editing of the TSAP-ID

If you remove the hex value "E0" from a TSAP-ID beginning with "E0.01", the TSAP-ID now begins with "01" and therefore no longer complies with the rules and is invalid:

|  | Local TSAP | Partner TSAP |
| --- | --- | --- |
| TSAP (ASCII) |  |  |
| TSAP-ID | 01.49.53.4F.6F.6E.54.43.50.2D.31 | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 |

After the entry field is exited, a message is output because the TSAP-ID is neither a valid ASCII-TSAP (this would have to have a hex value in the range from 20 to 7E as the first value) or a valid TSAP-ID (this would have to have the identifier "E0" as the first value).

###### Example 5: Entry of an ASCII-TSAP via the "TSAP-ID" entry field

If you remove the value "01" in addition to the value "E0" from the incorrect TSAP-ID in example 4, the TSAP-ID begins with the hex value 49. This value is within the permissible range for ASCII-TSAPs:

|  | Local TSAP | Partner TSAP |
| --- | --- | --- |
| TSAP (ASCII) |  |  |
| TSAP-ID | 49.53.4F.6F.6E.54.43.50.2D.31 | E0.01.49.53.4F.6F.6E.54.43.50.2D.31 |

When you exit the entry field, the TSAP-ID is recognized as a valid ASCII-TSAP and the resulting ASCII-TSAP "ISOonTCP-1" is written to the "TSAP (ASCII)" entry field.

---

**See also**

[TSAP structure (S7-1200, S7-1500, S7-1500T)](#tsap-structure-s7-1200-s7-1500-s7-1500t)
  
[Description of the connection parameters (S7-1200, S7-1500, S7-1500T)](#description-of-the-connection-parameters-s7-1200-s7-1500-s7-1500t)

##### Configuring HMI connections

This section contains information on the following topics:

- [Introduction to configuring connections](#introduction-to-configuring-connections)
- [What you need to know about using connection resources](#what-you-need-to-know-about-using-connection-resources)
- [Views containing information about the configured connections](#views-containing-information-about-the-configured-connections)
- [Creating a new connection](#creating-a-new-connection)
- [Creating a new connection graphically](#creating-a-new-connection-graphically)
- [Interactively creating a new connection](#interactively-creating-a-new-connection)
- [Working in the network view](#working-in-the-network-view)
- [Working with the connection table](#working-with-the-connection-table)
- [Deleting connections](#deleting-connections)
- [Copying connections](#copying-connections)
- [Inconsistent connections - connections without assignment](#inconsistent-connections---connections-without-assignment)
- [HMI connection general settings](#hmi-connection-general-settings)

###### Introduction to configuring connections

###### Definition

A connection defines a logical assignment of two communication partners in order to undertake communication services. A connection defines the following:

- Communication partner involved
- Type of connection (e.g., HMI connection)
- Special properties (e.g., whether a connection is established permanently or whether it is established and terminated dynamically in the user program, and whether status messages are to be sent)
- Connection path

###### What you need to know about connection configuration

During connection configuration, a local connection name is assigned for an HMI connection as a unique local identification.

In the network view, a "Connections" tab is displayed in addition to the "Network overview" tab. This tab contains the connection table. A line in this connection table represents a configured connection, e.g., between an HMI device and PLC, along with its properties.

---

**See also**

Configuring a connection
  
Automatic creation of a connection

###### What you need to know about using connection resources

###### Introduction

Each connection requires connection resources for the end point and/or transition point on the devices involved. The number of connection resources is device-specific.

If all the connection resources of a communication partner are assigned, no new connections can be established. This situation is apparent when a newly created connection in the connection table has a red background. The configuration is then inconsistent and cannot be compiled.

###### HMI connections

For HMI connections via the **integrated** PN interface, one connection resource for the endpoint per HMI connection is occupied for the HMI device.

One connection resource is also required for the connection partner (PLC).

###### Views containing information about the configured connections

The views described below will provide you with comprehensive access to all the information and functions regarding configuring and checking communication connections.

- Connection display in the network view
- Connection table
- "Properties" tab for a connection in the inspector window

  ![Figure](images/47041814539_DV_resource.Stream@PNG-en-US.png)

###### Benefits

The information shown in these views are always up-to-date in terms of the current user actions. This means:

- The connection table displays all connections created.
- If you have selected a connection in the connection table:

  - You will graphically see the connection path in the network view.
  - The "Properties" tab in the Inspector window displays the parameters of this connection.

###### The connection table

The connection table offers the following functions:

- List of all connections in the project
- Selection of a connection and display of connections associated with it in the network view
- Changing of connection partners
- Display showing status information

###### "Properties" tab for a connection in the inspector window

The properties dialog has the following meaning:

- Display for connection parameters
- Display of connection path
- Subsequent specification of connections using the "Find connection path" button

###### Creating a new connection

###### Creating a connection - alternatives

You have the following options for creating a connection in the network view:

- Graphic connection configuration
- Interactive connection configuration

You'll find the individual steps for this in the following chapters.

###### Requirement and result

You have created the devices with CPUs and HMI devices between which you want to configure connections in the network view.

###### Specifying a connection

If both partners for the connection type selected are networked on the same network, use the graphic or interactive selection of both communication partners to create a fully specified connection.

This connection is entered automatically into the connection table of the HMI device. A local connection name is assigned for this connection.

The following schematic shows a configured connection with a networked device:

![Specifying a connection](images/14779528331_DV_resource.Stream@PNG-en-US.png)

###### Creating a new connection graphically

###### Graphically configuring connections

When using the graphic connection configuration, if necessary the system asks you to define the connection path. Select the devices to be connected in the current configuration.

###### Automatically determining connection path

To create a connection graphically, follow these steps:

1. Click the "Connections" button.

   ![Automatically determining connection path](images/14779496203_DV_resource.Stream@PNG-en-US.png)

   ![Automatically determining connection path](images/14779496203_DV_resource.Stream@PNG-en-US.png)

   The connection mode for the connection type you have selected is then activated.

   You will see this from the following:

   The devices that can be used for the connection type selected in your project are color-highlighted in the network view.
2. Hold down the mouse button and drag the mouse pointer from the device from which the connection will originate to the device at which the connection ends.

   ![Automatically determining connection path](images/14380104971_DV_resource.Stream@PNG-de-DE.png)

   ![Automatically determining connection path](images/14380104971_DV_resource.Stream@PNG-de-DE.png)
3. Release the mouse button over the destination device to create the connection between the two devices.

###### Result

- A specified connection is created.
- The connection path is highlighted.
- The connection is entered in the connection table.

###### Interactively creating a new connection

###### Interactively configuring connections

Define the local device and its connection partners.

###### Procedure

Proceed as follows to interactively create a connection:

1. Select the "Create new connection" command in the shortcut menu of a connection partner for which you want to create a connection.

   The "Create new connection" dialog is opened.
2. Select the partner endpoint.

   In the right pane of the dialog, a possible connection path fitting the selected endpoint is displayed, if available. Incomplete paths, for example, for a non-specified CPU, are marked by an exclamation mark on a red background.
3. To close the dialog, click "OK".   
   To accept the configured connection and to configure additional connections to other endpoints, click "Apply".

###### Working in the network view

###### Highlighting connection path and partner in the network view

To display the connection partners for all or certain connection types in the network view, proceed as follows:

1. Click the "Connections" button.

   ![Highlighting connection path and partner in the network view](images/14381194251_DV_resource.Stream@PNG-en-US.png)
2. Select the "Highlight connection partners" command in the shortcut menu for the HMI device whose connection partners you want to display in the network view.
3. Select "All connection partners" in the following menu.

   The local device and the CPUs of the target devices are selected. The local connection partner shows an arrow pointing right and the remote connection partners show an arrow pointing left.
4. To open a list with information on the target devices, click the arrow of the local device. This additional function is useful in complex network configurations in which some devices are not visible.

   ![Highlighting connection path and partner in the network view](images/25486714635_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> You can display one of the connection partners which cannot be seen in the current display range of the network view. Click on the communication partner in the list that appears. Result: The display is moved such that the connection partner becomes visible.

---

**See also**

[Creating a new connection graphically](#creating-a-new-connection-graphically)

###### Working with the connection table

###### Basic functions for tables

The connection table supports the following basic functions for editing a table:

- Changing column width
- Displaying the meaning of a column, a row or cell using tooltips.

###### Changing column width

To adjust the width of a column to the content so that all texts in the lines are legible, follow these steps:

1. Position the cursor in the header of the connection table to the right of the column that you want to optimize until the cursor changes its shape to two parallel lines (as if you wanted to change the width of the column by dragging it with the cursor).
2. Double click on this point.

or

1. Open the shortcut menu on the header of the table.
2. Click on

   - "Optimize column width" or
   - "Optimize width of all columns".

For columns that are too narrow, the complete content of specific fields is shown when you pause with the cursor on the respective field.

###### Show / hide columns

You can use the shortcut menu of the header of the connection table to control the display of the various table columns. The shortcut menu entry "Show/hide columns" provides you with an overview of the available columns. Use the check box to control whether columns are shown or hidden.

###### Using cursor keys to move within the connection table

You can use the UP and DOWN cursor keys to select a connection from the connection table; the selected connection is marked and is shown highlighted in the network view.

###### Changing properties of connection

You can directly edit the parameters displayed in the connection table in some cases. To change the name of a connection, you do not have to navigate to the Inspector window.

###### Changing connection partners

You can change the connection partner of a connection as follows:

1. Select the connection.
2. Select the new connection partner from the open drop-down list in the "Partner" column.

###### Deleting connections

You can delete configured connections using the network view or the connection table.

In the network view you can delete one highlighted connection per action. In the connection table you can delete one or several connections per action.

###### Procedure

To delete a connection, follow these steps:

1. Select the connection to be deleted:

   - In the network view: Select the connection to be deleted.
   - In the connection table: Select the rows of the connections to be deleted (multiple selection possible).
2. Open the shortcut menu with a right mouse click.
3. Select the "Delete" command.

###### Result

The selected connection is removed completely.

###### Copying connections

###### Introduction

Connections are not copied singly but always in context along with the project or the device.

You can copy:

- Entire projects
- One or more devices within a project or from one project to another

###### Copying a project

When you copy a project all configured connections will also be copied. No settings whatsoever are required for the copied connections because the connections remain consistent.

###### Copying devices

If you copy devices for which connections have been configured (HMI devices), the connections are copied as well. To complete the connection path, you must still finalize the networking.

An S7-1200 CPU with a V.10 firmware is only a server for connections and has no connection configuration itself. Consequently, no connections are copied along with it when an S7-1200 CPU with a V1.0 firmware is copied.

###### Inconsistent connections - connections without assignment

With an inconsistent connection the structure of the connection data is destroyed or the connection is not functional in the project context.

Inconsistent connections cannot be compiled and loaded - operation is not possible with such a connection.

In the connection table inconsistent connections are marked in red.

###### Possible causes for inconsistent connections

- Deletion or change of the hardware configuration.
- Missing interface network links in the project, which are necessary for a connection.
- Connection resources are exceeded
- Errors when backing up data due to insufficient memory
- Connections to an unspecified connection partner without partner address information.

Detailed information regarding the reasons for the inconsistency can be found in the "Compile" tab following compilation (Edit &gt; Compile).

###### Remedies

If the connection cannot be repaired by opening the connection properties, changing them or undoing them in the configuration, then it may be necessary to delete the connection and re-create it.

###### HMI connection general settings

###### General connection parameters

General connection parameters are displayed in the "General" parameter group under the properties of the connection; these connection parameters identify the local connection end point.

Here, you can also assign the connection path and specify all aspects of the connection partner.

###### Special connection properties

Display of the connection properties (cannot be changed):

- Active connection establishment

  The connection establishment always starts from the HMI device. This option is selected by default if the address of the partner is specified.
- One-way

  One-way means that the connection partner functions as a server on this connection and cannot send or receive actively.
- Sending operating mode messages

  Not relevant for HMI devices.

###### Address details

Displaying address details of the HMI connection. With an unspecified partner, the values for the rack and slot can be changed. All other values are obtained from the current configuration and cannot be changed.

###### Miscellaneous

Display of the access points for the online connection between HMI device and connection partner.

##### Configuring S7 connections (S7-1200)

This section contains information on the following topics:

- [Introduction to configuring connections (S7-1200)](#introduction-to-configuring-connections-s7-1200)
- [What you need to know about using connection resources (S7-1200)](#what-you-need-to-know-about-using-connection-resources-s7-1200)
- [Views containing information about the configured connections (S7-1200)](#views-containing-information-about-the-configured-connections-s7-1200)
- [Creating a new connection (S7-1200)](#creating-a-new-connection-s7-1200)
- [Creating a new connection graphically (S7-1200)](#creating-a-new-connection-graphically-s7-1200)
- [Interactively creating a new connection (S7-1200)](#interactively-creating-a-new-connection-s7-1200)
- [Working in the network view (S7-1200)](#working-in-the-network-view-s7-1200)
- [Working with the connection table (S7-1200)](#working-with-the-connection-table-s7-1200)
- [Deleting connections (S7-1200)](#deleting-connections-s7-1200)
- [Copying connections (S7-1200)](#copying-connections-s7-1200)
- [Inconsistent connections - connections without assignment (S7-1200)](#inconsistent-connections---connections-without-assignment-s7-1200)
- [S7 connection - general settings (S7-1200)](#s7-connection---general-settings-s7-1200)
- [S7 connection - address details (S7-1200)](#s7-connection---address-details-s7-1200)
- [S7 connections via CM/CP (S7-1200)](#s7-connections-via-cmcp-s7-1200)

###### Introduction to configuring connections (S7-1200)

###### Definition

A connection defines a logical assignment of two communication partners in order to undertake communication services. A connection defines the following:

- Communication partner involved
- Type of connection (for example, S7 connection)
- Special properties (e.g., whether a connection is established permanently or whether it is established and terminated dynamically in the user program, and whether status messages are to be sent)
- Connection path

###### What you need to know about connection configuration

During connection configuration, a local connection name is assigned for an S7 connection as a unique local identification.

In the network view, a "Connections" tab is displayed in addition to the "Network overview" tab. This tab contains the connection table. A row in this connection table represents a configured connection from the viewpoint of the local communication partner with its properties, for example, between two S7-1200 CPUs.

###### What you need to know about using connection resources (S7-1200)

###### Introduction

Each connection requires connection resources for the end point and/or transition point on the devices involved. The number of connection resources is device-specific.

If all the connection resources of a communication partner are assigned, no new connections can be established. This situation is apparent when a newly created connection in the connection table has a red background. The configuration is then inconsistent and cannot be compiled.

###### S7 connections

In the case of S7 connections via the PN interface, one connection resource per S7 connection is assigned for the endpoint for the S7-1200 CPU. One connection resource is also required for the connection partner.

You can find an overview of available and assigned connection resources for selected S7-1200 CPU in the Inspector window at "Properties &gt; Connection Resources"

###### Views containing information about the configured connections (S7-1200)

The views described below will provide you with comprehensive access to all the information and functions regarding configuring and checking communication connections.

- Connection display in the network view
- Connection table
- "Properties" tab for a connection in the inspector window

  ![Figure](images/47041393035_DV_resource.Stream@PNG-en-US.png)

###### Benefits

The information shown in these views are always up-to-date in terms of the current user actions. This means:

- The connection table displays all connections created.
- If you have selected a connection in the connection table:

  - When connection mode is enabled, the connection path is highlighted in the network view.
  - The "Properties" tab in the Inspector window displays the parameters of this connection.

###### The connection table

The connection table offers the following functions:

- List of all connections in the project
- Selection of a connection and display of connections associated with it in the network view (when connection mode is enabled)
- Changing of connection partners
- Display showing status information

###### "Properties" tab for a connection in the inspector window

The properties dialog has the following meaning:

- Display for connection parameters
- Display of connection path
- Subsequent specification of connections using the "Find connection path" button

###### Creating a new connection (S7-1200)

###### Creating a connection - alternatives

You have the following options for creating a connection in the network view:

- Graphic connection configuration
- Interactive connection configuration

You'll find the individual steps for this in the following chapters.

###### Requirement and result

In the network view, you have add devices between which the connections should be configured.

###### Specifying a connection

If both partners for the connection type selected are networked on the same network, use the graphic or interactive selection of both communication partners to create a fully specified connection.

This connection is entered automatically in the connection table of the S7-1200 CPU. A local connection name is assigned for this connection.

The following schematic shows a configured connection with a networked device:

![Specifying a connection](images/25485216651_DV_resource.Stream@PNG-en-US.png)

###### Creating a new connection graphically (S7-1200)

###### Graphically configuring connections

In the case of graphic connection configuration, the connection path is automatically specified provided interfaces and resources are available. Select the devices to be connected in the current configuration.

###### Automatically determining connection path

To create a connection graphically, follow these steps:

1. Click the "Connections" button.

   ![Automatically determining connection path](images/25485163147_DV_resource.Stream@PNG-en-US.png)

   ![Automatically determining connection path](images/25485163147_DV_resource.Stream@PNG-en-US.png)

   This step activates the connection mode: You can now select the connection type you want. You will see this from the following:  
   The devices that can be used for the connection type selected in your project are color-highlighted in the network view.
2. Hold down the mouse button and drag the mouse pointer from the device from which the connection will originate to the device at which the connection ends.

   ![Automatically determining connection path](images/25485237643_DV_resource.Stream@PNG-de-DE.png)

   ![Automatically determining connection path](images/25485237643_DV_resource.Stream@PNG-de-DE.png)
3. Release the mouse button over the destination device to create the connection between the two devices.

###### Result

- A specified connection is created.
- The connection path is highlighted.
- The connection is entered in the connection table.

###### Configuring a connection when there is no or no clear network assignment

Any networking not in place will if possible be created automatically when a connection is created. A query will be made upon completion of connection configuration if unique network assignment is not possible. You will be able to choose from the existing subnets.

Example below: A query is made upon creation of a connection between stations PLC_1 and PLC_2, which are not yet networked.

![Configuring a connection when there is no or no clear network assignment](images/26260176139_DV_resource.Stream@PNG-en-US.png)

###### Interactively creating a new connection (S7-1200)

###### Interactively configuring connections

Define the local device and its connection partners.

###### Procedure

Proceed as follows to interactively create a connection:

1. Select the "Add new connection" command in the shortcut menu of a connection partner for which you want to create a connection.  
   The "Create new connection" dialog appears.
2. Select the partner endpoint.  
   In the right pane of the dialog, a possible connection path fitting the selected endpoint is displayed, if available. Incomplete paths, for example, for a non-specified CPU, are marked by an exclamation mark on a red background.
3. To accept the configured connection and to configure additional connections to other endpoints, click "Add".  
   To close the dialog, click "OK".

###### Working in the network view (S7-1200)

###### Highlighting connection path and partner in the network view

To display the connection partners for all or certain connection types in the network view, proceed as follows:

1. Click the "Connections" button.

   ![Highlighting connection path and partner in the network view](images/25485285387_DV_resource.Stream@PNG-en-US.png)
2. Select the S7-CPU for which you want to display the connection partners in the network view and then select the "Highlight connection partners" command in the shortcut menu.
3. Select "All connection partners" in the following menu.

   The local device and the CPUs of the target devices are selected. The local connection partner shows an arrow pointing right and the remote connection partners show an arrow pointing left.
4. To open a list with information on the target devices, click the arrow of the local device. This additional function is useful in complex network configurations in which some devices are not visible.

   ![Highlighting connection path and partner in the network view](images/25485272203_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> You can display one of the connection partners which cannot be seen in the current display range of the network view. Click on the communication partner in the list that appears. Result: The display is moved such that the connection partner becomes visible.

###### Working with the connection table (S7-1200)

###### Basic functions for tables

The connection table supports the following basic functions for editing a table:

- Changing column width
- Displaying the meaning of a column, a row or cell using tooltips.

###### Changing column width

To adjust the width of a column to the content so that all texts in the lines are legible, follow these steps:

1. Position the cursor in the header of the connection table to the right of the column that you want to optimize until the cursor changes its shape to two parallel lines (as if you wanted to change the width of the column by dragging it with the cursor).
2. Double click on this point.

or

1. Open the shortcut menu on the header of the table.
2. Click on

   - "Optimize column width" or
   - "Optimize width of all columns".

For columns that are too narrow, the complete content of specific fields is shown when you pause with the cursor on the respective field.

###### Show / hide columns

You can use the shortcut menu of the header of the connection table to control the display of the various table columns. The shortcut menu entry "Show/hide columns" provides you with an overview of the available columns. Use the check box to control whether columns are shown or hidden.

If you want to store the layout, width and visibility of the table columns, click on the "Remember layout" function in the top right-hand of the network view.

| Symbol | Meaning |
| --- | --- |
| ![Show / hide columns](images/25385115915_DV_resource.Stream@PNG-de-DE.png) | Remember layout  Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

###### Using cursor keys to move within the connection table

You can use the UP and DOWN cursor keys to select a connection from the connection table; the selected connection is marked and is shown highlighted in the network view.

###### Changing properties of connection

You can directly edit some of the parameters displayed in the connection table. The name of the connection can, for example, only be changed in the connection table.

###### Changing connection partners

You can change the connection partner of a connection as follows:

1. Select the connection.
2. Select the new connection partner from the open drop-down list in the "Partner" column.

###### Deleting connections (S7-1200)

You can delete configured connections using the network view or the connection table.

In the network view you can delete one highlighted connection per action. In the connection table you can delete one or several connections per action.

###### Procedure

To delete a connection, follow these steps:

1. Select the connection to be deleted:

   - In the network view: Select the connection to be deleted.
   - In the connection table: Select the rows of the connections to be deleted (multiple selection possible).
2. Open the shortcut menu with a right mouse click.
3. Select the "Delete" command.

###### Result

The selected connection is removed completely.

###### Copying connections (S7-1200)

###### Introduction

Connections are not copied singly but always in context along with the project or the device.

You can copy:

- Entire projects
- One or more devices within a project or from one project to another

###### Copying a project

When you copy a project all configured connections will also be copied. No settings whatsoever are required for the copied connections because the connections remain consistent.

###### Copying devices

If you copy devices for which connections have been configured, the connections are copied as well. To complete the connection path, you must still finalize the networking.

An S7-1200 CPU with a V.10 firmware is merely a server for connections and has no connection configuration itself. Consequently, no connections are copied along with it when an S7-1200 CPU with a V1.0 firmware is copied.

###### Inconsistent connections - connections without assignment (S7-1200)

With an inconsistent connection the structure of the connection data is destroyed or the connection is not functional in the project context.

Inconsistent connections cannot be compiled and loaded - operation is not possible with such a connection.

In the connection table inconsistent connections are marked in red.

###### Possible causes for inconsistent connections

- Deletion or change of the hardware configuration.
- Missing interface network links in the project, which are necessary for a connection.
- Connection resources are exceeded
- Connections to an unspecified connection partner without partner address information.

Detailed information regarding the reasons for the inconsistency can be found in the "Compile" tab following compilation (Edit &gt; Compile).

###### Remedies

To assign a closed connection path to an existing open connection path, expand the device configuration in such a way that the interfaces required for the connection type are available for both partners. At "Properties &gt; General &gt; Interface" in the Inspector window, you can use the "Find connection path" button to create a connection to an existing partner.

###### S7 connection - general settings (S7-1200)

###### General connection parameters

General connection parameters are displayed in the "General" parameter group under the properties of the connection; these connection parameters identify the local connection end point.

Here, you can assign the connection path and specify all aspects of the connection partner.

###### Local ID

The local ID of the module from which the connection is viewed is displayed here (local partner). You can change the local ID. You may need to do this if you have already programmed communication function blocks, and you want to use the local ID specified in those function blocks for the connection.

###### Special connection properties

Display of connection properties (can be modified depending on the components used):

- One-way

  One-way means that the connection partner functions as a server on this connection and cannot send or receive actively.
- Active connection establishment

  In the case of one-way connection, for example with a S7-1200 CPU (firmware version V1.0), a connection partner can only be provided for the active connection establishment. In the case of a two-way connection you can set which connection partner will assume the active role.
- Sending operating mode messages

  Indicates whether or not the local partner sends operating mode messages to the connection partner.

###### Address details

Displaying address details of the S7 connection. With an unspecified partner, the values for the rack and slot can be changed. All other values are obtained from the current configuration and cannot be changed.

###### S7 connection - address details (S7-1200)

###### Meaning

The address details show the end points of the connection and can localize these via the specification of rack and slot.

When a connection is established, the connection-specific resources of a module are assigned permanently to this connection. This assignment requires that the connection resource can be addressed. The TSAP (Transport Service Access Point) is, as it were, the address of the resource that is formed with the help of the connection resource or, in the case of S7-1200 CPUs (firmware V2.0 or higher) with the SIMATIC-ACC (SIMATIC Application Controlled Communication).

###### Configuration of TSAP for S7-1200

- For S7-1200 CPU (firmare V2.0 or higher):

  "SIMATIC-ACC"&lt;nnn&gt;&lt;mm&gt;

  nnn = Local ID

  mm = any value
- For S7-1200 CPU (firmare V1.0):

  &lt;xx&gt;.&lt;yz&gt;

  xx = Number of the connection resource

  y = Rack number

  z = Slot number

###### TSAP structure, dependent on partner

The configuration of the TSAP for S7-1200 CPUs is dependent on the respective firmware and on the remote connection partner. When a S7-1200 CPU is connected with a S7-300/400 CPU, a S7-1200 CPU also uses a TSAP configuration that includes the connection resource.

See the following examples of TSAPs of various connection configurations

- Connection between two S7-1200 CPUs (both with firmware V2.0):

  - S7-1200 CPU "A" with firmware V2.0 and local ID 100:

    TSAP: SIMATIC-ACC10001
  - S7-1200 CPU "B" with firmware V2.0 and local ID 5AE:

    TSAP: SIMATIC-ACC5AE01
- Connection between two S7-1200 CPUs (firmware V2.0 and V1.0):

  - S7-1200 CPU with firmware V2.0 and local ID 1FF:

    TSAP: SIMATIC-ACC1FF01
  - S7-1200 CPU with firmware V1.0 (rack 0, slot 1, connection resource 03):

    TSAP: 03.01
- Connection between S7-1200 CPUs (firmware V2.0) and S7-300/400 CPU:

  - S7-1200 CPU with firmware V2.0 (rack 0, slot 1, connection resource 12):

    TSAP: 12.01
  - S7-300/400 CPU (rack 0, slot 2, connection resource 11):

    TSAP: 11.02

###### S7 connections via CM/CP (S7-1200)

###### Introduction

S7-1200 CPUs with a firmware version of V2.0 or higher support one-way and two-way S7 connections via CM/CP interfaces. This increases the number of Ethernet ports and networks that can be used for S7 connections. Even though the connection is then guided via the CM/CP, the associated S7-1200 CPU is an end point of the connection. The other end point can be any other device in the case of two-way connections. This other device must also support S7 connections.

###### Data volumes and configuration limit

The number of communication connections which are supported by CM/CP can be found in the manual accompanying every CM/CP. The number of connections per device can be further increased by adding other CM/CPs.

If several CM/CPs are fitted in a device, an automatic switch is made to the next CM/CP when this limit is exceeded. Specifically assign the connections using the path selection as required.

> **Note**
>
> Data transfer &gt; 240 byte transfer is supported by the current CPs.
>
> CPs with an older product version support the transfer of data with a data length of up to 240 bytes.
>
> For more information, refer to the details provided in the Ethernet CP equipment manual.

###### Tasks of the Ethernet CM/CP in online mode

During data transfer via a connection, the Ethernet CM/CP takes on the following tasks:

- Receiving

  Receiving data from the Ethernet and forwarding to the user data area in the CPU
- Sending

  Transferring data from the user data area of the CPU and sending data via the Ethernet

The connection is established automatically as soon as the partner can be reached.

##### S7 connections using PUT and GET instructions

This section contains information on the following topics:

- [Basic information on communication via the PUT/GET instruction](#basic-information-on-communication-via-the-putget-instruction)
- [Connection configuration](#connection-configuration)
- [Block parameter assignment](#block-parameter-assignment)

###### Basic information on communication via the PUT/GET instruction

###### Basic information on PUT/GET instructions

Use PUT and GET instructions to exchange data between two CPUs via an S7 connection.

The GET instruction is used to read data from a partner CPU. The PUT instruction is used to control the writing of tags by the communication partner via the user program. Apart from the PUT and GET instructions, no additional communication functions are provided for reading and writing tags.

To simplify the use of the two instructions, specify all required parameters for the connection and all block parameters in the Inspector window of the program editor.

###### Requirement

To be able to use the PUT and GET instructions, the following requirements must be satisfied:

- At least one S7-1200/1500 CPU or S7-300/400 CPU must be created in the project. Firmware 2.0 or higher must be installed on an S7-1200 CPU. If you have not yet created a second CPU in the project, you can initially establish the connection to an unspecified partner.
- An S7 connection must exist between the two CPUs. If you have not yet established a connection between two CPUs, a connection is automatically established during the configuration of the instructions.
- For both instructions, an instance data block is required in which all data used by the instruction is stored. The instance data block is created automatically as soon as you drag a PUT or GET instruction to a network in the program editor. For the correct execution of the program, it is essential that the instance data blocks are not changed; consequently, these data blocks are know-how protected. You only have read access to the instance data blocks.

---

**See also**

[Overview of connection configuration](#overview-of-connection-configuration)
  
[Assigning parameters to start request](#assigning-parameters-to-start-request)
  
[PUT: Set parameters for write and send area](#put-set-parameters-for-write-and-send-area)
  
[GET: Set parameters for read and memory area](#get-set-parameters-for-read-and-memory-area)

###### Connection configuration

This section contains information on the following topics:

- [Overview of connection configuration](#overview-of-connection-configuration)
- [Description of the connection parameters](#description-of-the-connection-parameters)
- [Starting connection parameter assignment](#starting-connection-parameter-assignment)
- [Creating and assigning parameters to connections](#creating-and-assigning-parameters-to-connections)
- [Deleting connections](#deleting-connections-1)

###### Overview of connection configuration

###### Introduction

The connection parameters for the PUT and GET instructions are assigned in the inspector window of the program editor. All parameters are saved in the corresponding instance data block.

###### Structure of the connection configuration

The connection configuration is made up of the following components:

![Structure of the connection configuration](images/47090019595_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Communication instruction for PUT or GET |
| ② | Call of online and diagnostic functions |
| ③ | "Configuration" tab in the "Properties" tab |
| ④ | Area navigation of the "Configuration" tab |
| ⑤ | General properties of the connection parameters |

###### Display of online and diagnostic functions

If you click the icon for starting the online and diagnostic functions, the associated CPU goes online automatically. The connection table in the network view is opened. In addition, the "Diagnostics" tab and the connection information are displayed in the inspector window.

###### Entering the connection parameters

Enter the desired connection parameters in the "Configuration" tab. The area navigation of the "Configuration" tab includes the "Connection parameters" group. This group contains the connection configuration. Here, you can enter the parameters for the connections using system functions. When all the required parameters are assigned, a check mark is set behind the "Connection parameters" group in the area navigation.

---

**See also**

[Assigning parameters to start request](#assigning-parameters-to-start-request)
  
[PUT: Set parameters for write and send area](#put-set-parameters-for-write-and-send-area)
  
[GET: Set parameters for read and memory area](#get-set-parameters-for-read-and-memory-area)

###### Description of the connection parameters

###### Overview

The following table shows the general connection parameters:

| Parameter | Description |
| --- | --- |
| End point | The names of the local end point and the partner end point are shown.  - Local end point   The local end point is the CPU in which the PUT or GET instruction is programmed. - Partner end point   The partner end point is selected from the drop-down list. The drop-down list shows all available possible connection partners including unspecified connection partners for devices whose data is unknown in the project.   As long as no connection partner is set, all other parameters in the mask are disabled. |
| Interface | The interface of the partner CPU is displayed. The partner interface is not displayed until a specified partner CPU has been selected. |
| Interface type | The type of interface via which communication is handled is displayed. |
| Subnet name | The subnet of the local end point is displayed, provided this exists. The partner subnet is displayed only after the partner end point has been selected.  If at least one of the two connection partners is not connected with a subnet, the two connection partners are automatically connected with each other. The partner which is not connected to a network is hereby connected to the same subnet via which the other partner is already connected to a network.  A connection of connection partners to different subnets is only possible with IP or S7 routing. The IP routing settings can be edited in the properties of the relevant Ethernet interfaces. |
| Address | The IP address of the local end point is displayed. The IP address of the partner is displayed only after the partner end point has been selected.  If you have selected an unspecified connection partner, the input box is empty and has a red background. In this case, you will need to specify a valid IP address for the connection partner. |
| Connection ID | The currently set connection ID is displayed. You can change the connection ID in the connection table in the network view. You can also directly access the connection table while you are setting the connection parameters. To do this, click the "Create new connection" icon. |
| Connection name | The name of the connection which was automatically created when the PUT/GET instruction was inserted is displayed. You can change the name of the connection by entered a different name in the field. You can also create a new connection or edit existing connections by clicking the "Create new connection" icon. |
| Active connection establishment | Use the "Active connection establishment" option button to specify which partner starts the communication. When the connection is created, the local partner is initially specified by default for the establishment of the connection. If a device does not support active connection establishment, you have to activate active connection establishment on the other partner. |
| Configured at one end | If this check box is selected, the connection partner is the server for this connection. It cannot actively send or receive. This corresponds to the behavior of the PUT/GET instructions. In this case, other instructions are not possible. If the check box is not selected, other instructions can also be used for the communication. |

###### Starting connection parameter assignment

You can assign the connection parameters for PUT and GET in the inspector window as soon as you have inserted and selected a PUT or GET instruction in a program block.

###### Procedure

To insert PUT/GET instructions, follow these steps:

1. Open the "Instructions" task card in the "Communication &gt; S7 Communication" folder.
2. Drag a PUT or GET instruction to a network.

   The "Call options" dialog opens.
3. Optional: Edit the properties of the instance DB in the "Call properties" dialog. You have the following options:

   - Change the default name.
   - Select the "Manual" check box to assign your own number.
4. Click "OK".

###### Result

A corresponding instance data block is created for the inserted PUT or GET instruction. For S7-300 CPUs, a function block is also created in the program resources.

When PUT or GET instruction is selected, you will see the "Configuration" tab under "Properties" in the inspector window. The "Connection parameters" group in area navigation contains the connection parameter assignment that you can now make.

---

**See also**

[Creating and assigning parameters to connections](#creating-and-assigning-parameters-to-connections)
  
[Deleting connections](#deleting-connections-1)

###### Creating and assigning parameters to connections

You can create S7 connections and assign the parameters for these in the connection parameter assignment of the PUT/GET instructions. Changed values are checked immediately by the connection parameter assignment for input errors.

###### Requirement

A CPU exists with a PUT or GET communication instruction.

###### Procedure

To configure an S7 connection using PUT/GET instructions, follow these steps:

1. In the program editor, select the call of the PUT or GET instruction.
2. Open the "Properties &gt; Configuration" tab in the inspector window.
3. Select the "Connection parameters" group. Until you select a connection partner, only the empty drop-down list for the partner end point is enabled. All other input options are disabled.

   The connection parameters already known are displayed:

   - Name of the local end point
   - Interface of the local end point
   - IP address of the local end point
4. In the drop-down list box of the partner end point, select a connection partner. You can select an unspecified device or a CPU in the project as the communications partner.

   The following parameters are automatically entered as soon as you have selected the connection partner:

   - Interface of the partner end point
   - Interface of the partner end point. If several interfaces are available, you can change the interface as required.
   - Interface type of the partner end point
   - Subnet name of both end points
   - IP address of the partner end point
   - Name of the connection which is used for the communication. If no connection exists yet, it is automatically established.
5. If required, change the connection name in the "Connection name" input box. If you want to create a new connection or edit an existing connection, click on the "Create new connection" icon.

**Note**

The PUT and GET instructions between two communication partners can only run if both the hardware configuration and the program part for the partner end point have been loaded into the hardware. To achieve fully functional communication, make sure that you load not only the connection description of the local CPU on the device but also that of the partner CPU as well.

###### Deleting connections

A connection which was automatically created during the insertion of a PUT or GET instruction appears in the connection table of the network view like every standard connection. As a result, it can be deleted in the connection table.

###### Procedure

To delete a connection, follow these steps:

1. Open the connection table in the network view.
2. In the connection table, select the connection that you want to delete.
3. To do this, right-click the connection and select the "Delete" command from the shortcut menu.

###### Result

The connection is deleted. The PUT or GET instruction and the associated instance data blocks are retained and must be manually deleted if necessary.

To continue using the PUT or GET instruction, you must configure the connection again in the inspector window of the program editor, since all connection parameters were also deleted when the connection was deleted. In this case, specify a new communication partner and a suitable connection.

###### Block parameter assignment

This section contains information on the following topics:

- [Assigning parameters to start request](#assigning-parameters-to-start-request)
- [PUT: Set parameters for write and send area](#put-set-parameters-for-write-and-send-area)
- [GET: Set parameters for read and memory area](#get-set-parameters-for-read-and-memory-area)

###### Assigning parameters to start request

To start communication via the PUT or GET instruction, you have to specify an event which activates the instruction. This event is referred to as control parameter (REQ). The communication job is activated as soon as there is a positive edge at the control parameter REQ.

Please note that the control parameter REQ is assigned the default FALSE at first call.

###### Requirement

- The program editor is open.
- You have already inserted a PUT or GET instruction.
- A connection has been established between two communication partners.

###### Procedure

To define the REQ control parameter, follow these steps:

1. Select the PUT or GET instruction in the program editor.
2. Open the "Configuration" tab in the inspector window.
3. Select the "Block parameter assignment" entry in the area navigation.
4. In the "REQ" field, select a tag of the "BOOL" data type to initialize the execution of the instruction. Alternatively, you can also interconnect a previous instruction in the program editor.

---

**See also**

[Data consistency (S7-1200, S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#data-consistency-s7-1200-s7-1500)
  
[PUT: Set parameters for write and send area](#put-set-parameters-for-write-and-send-area)
  
[GET: Set parameters for read and memory area](#get-set-parameters-for-read-and-memory-area)

###### PUT: Set parameters for write and send area

For communication via the PUT instruction, you must specify the memory area of the partner CPU to which the data should be written. In addition, you must specify the memory area of the local CPU from which the data is to be read.

###### Requirement

- The program editor is open.
- You have already inserted a PUT instruction.
- A connection has been established between two communication partners.

###### Procedure

To specify the read and the memory area for the instruction, follow these steps:

1. Select the PUT instruction in the program editor.
2. Open the "Configuration" tab in the inspector window.
3. Select the "Block parameter assignment" entry in the area navigation.
4. In the "In/Outputs &gt; Write area (ADDR_1) &gt; Start" field, select a "REMOTE" data type pointer to the area of the partner CPU which is to be written.

   Only absolute addressing is permitted.

   Example: P#DB10.DBX5.0 Byte 10
5. In the "Length" field, enter the length of the write area and select the data type of the memory area from the drop-down list.
6. In the "In/Outputs &gt; Send area (SD_1) &gt; Start" field, select a pointer to the area in the local CPU which contains the data to be sent.
7. In the Length field, enter the length of the memory area to be read and select the data type from the drop-down list.

   Only the data types BOOL (for a bit array, "0" must be used as address and an integer multiple of byte must be used as length), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER are permitted.

   If the VARIANT pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 Byte 10).

---

**See also**

[GET: Set parameters for read and memory area](#get-set-parameters-for-read-and-memory-area)

###### GET: Set parameters for read and memory area

For communication via the GET instruction, you must specify the memory area of the local CPU to which the data should be written. In addition, you must specify the memory area of the partner CPU from which the data is to be read.

###### Requirement

- The program editor is open.
- You have already inserted a GET instruction.
- A connection has been established between two communication partners.

###### Procedure

To specify the read and the memory area for the instruction, follow these steps:

1. Select the GET instruction in the program editor.
2. Open the "Configuration" tab in the inspector window.
3. Select the "Block parameter assignment" entry in the area navigation.
4. In the "In/Outputs &gt; Read area (ADDR_1) &gt; Start" field, select a "REMOTE" data type pointer to the area of the partner CPU which is to be read.

   Only absolute addressing is permitted.

   Example: P#DB10.DBX5.0 Byte 10
5. In the "Length" field, enter the length of the read area and select the data type of the memory area from the drop-down list.
6. In the "In/Outputs &gt; Memory area (RD_1) &gt; Start" field, select a pointer to the area in the local CPU in which the read data is to be stored.
7. In the Length field, enter the length of the memory area and select the data type from the drop-down list.

   Only the data types BOOL (for a bit array, "0" must be used as address and an integer multiple of byte must be used as length), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER are permitted.

---

**See also**

[PUT: Set parameters for write and send area](#put-set-parameters-for-write-and-send-area)

##### Connection resources

This section contains information on the following topics:

- [Configuration limits in the connection configuration](#configuration-limits-in-the-connection-configuration)
- [Connection resources and communication type](#connection-resources-and-communication-type)
- [Connection resources and connection type](#connection-resources-and-connection-type)
- [S7-1200 connection resources: (S7-1200)](#s7-1200-connection-resources-s7-1200)
- [Connection resources S7-1500 (S7-1500)](#connection-resources-s7-1500-s7-1500)

###### Configuration limits in the connection configuration

###### Connection resources

Some communications services require connections. During operation, communication connections utilize memory and program resources of the CPUs, CPs, and CMs involved in the communication path (e.g., memory areas in the CPU operating system). Within a controller (PLC), this applies, for example, to the CPU as connection end point and to the extensions with CPs as interfaces to the subnets. In most cases, one resource per CPU/CP/CM is assigned for a connection. In HMI communication, up to 3 connection resources are required for each HMI connection.

###### Available connection resources

The maximum configuration limit within the automation system is always defined by the CPU, either through the high system limit defined by the CPU (S7-1200/1500) or through the sum of usable resources of the CPU and CP (S7-300/400). In most cases, the available connection resources of a CPU/CP/CM are automatically distributed to their interfaces, as required.

Each CPU brings along reserved connection resources for programming device, HMI, and Web server communication in its configuration. In addition, there are available resources that can be used for any HMI, S7 and open communication (S7-1200/1500).

You can determine which resources are available to you based on the configuration of the devices as follows:

- Selection of the device type at connection end point (CPU)
- Number and type of additional communication modules (CP, CM)

The number of connection resources available differs for the various automation systems:

- S7-300: The used CPU defines the number of available resources for connections. The maximum number of resources for connections can be expanded by added CPs.
- S7-400: The used CPU defines the number of possible resources for S7 connections. The resources can also be used for other connection types, in which case the maximum number of resources for other connection types can be expanded by adding CPs.
- S7-1200: The used CPU defines the number of possible resources for S7 connections. This high limit can be extended by adding CPs or CMs.
- S7-1500: The CPU that is used defines the applicable high limit of the connection resources for the whole automation system. The CPU itself accounts for some of these connection resources, and additional resources are accrued via CPs and CMs. However, regardless of how many CPs and CMs are added, the total number of connection resources cannot exceed the high limit of connection resources defined by the CPU type.

###### Time of occupation of connection resources

Which resources are actually used in operation, depends on which communication functions are used at any specific time and which communication connections are enabled at any specific time. Therefore, only limited checks of compliance with specific configuration limits and available communication resources can be performed at the time of configuration. The connection configuration offers the greatest possible support for this.

###### Factors influencing the configuration limits

You determine the communication resources with the device configuration:

- Number of available S7 connection resources in the CPU (S7-300/400)
- Number of connection resources for S7 communication and open communication in the station (S7-1500)
- Number of protocol-specific connection resources in the CPs/CMs
- Number of available CPs/CMs
- Automatic, programmed, or configured connection setup

###### Behavior of the connection configuration

During input, the connection configuration checks the following circumstances and behaves as follows:

- During the creation of S7 connections

  Is the maximum number of available S7 connections assigned? If yes, it is not possible to configure another S7 connection via the selected interface.  
  For the S7-300, it is possible to increase the configuration limit by adding CPs.
- During the creation of any connection types

  Is the maximum number of protocol-specific connection resources in the interface (CP) assigned? If yes, it is not possible to configure another connection of the selected type via the selected interface.  
  For the S7-300/400, it is possible to increase the configuration limit by adding CPs.
- During the creation of any connection types with OPC (PC stations)

  In the case of connections with OPC as connection end point, more connections can generally be configured than can be operated at any one time in the CP used in the PC station. That is because the connection properties differentiate between "Maintain permanently" and "Set up on demand".

  The limit for Softnet IE CPs is 64 concurrent connections and 120 concurrent connections for Hardnet IE CPs.

  > **Note**
  >
  > **Number of locally configured connections greater than number of possible connections in runtime**
  >
  > The user can configure the maximum possible number of S7 and SEND/RECEIVE connections via OPC as "Maintain permanently" in runtime and then configure no additional connection as "Establish on demand". Alternatively, the user can configure less than the maximum possible number of S7 and SEND/RECEIVE connections via OPC as "Maintain permanently" in runtime, and accordingly configure additional S7 and SEND/RECEIVE connections as "Establish on demand".
  >
  > If the user configures more than 64 S7-connections and SEND/RECEIVE connections, a warning appears during the compiling of the configuration. The warning appears independent of whether the connections are permanently ("Maintain permanently") or temporarily ("Establish on demand") configured, as even with 65 temporary connections the maximum number of simultaneous connections can theoretically be exceeded in runtime.

When the connection configuration is compiled, a warning or, in the case of a non-assignable interface, an error is output, if appropriate.

> **Note**
>
> **S7 connection resources are exhausted**
>
> If the maximum number of S7 connection resources is reserved, no S7 connection resources additionally required for data transmission between CPU and CP are in operation or possibly available for connections. The corresponding communication jobs are then refused.
>
> You should therefore make sure that there is a sufficient number of non-assigned S7 connection resources, depending on the total assigned communication functions.
>
> You can find the number of reserved S7 connection resources for the selected S7-300 or S7-1200/1500 CPU in the area navigation under "Connection resources". For the S7-300, only the connection resources of the CPU are shown. For the S7-1200/1500, you also see the resources of the CPs and CMs.

###### Connection resources and communication type

Every connection needs connection resources for the endpoint and transition point (e.g., CP, CM) on the devices involved. The number of available connection resources is CPU/CP/CM-specific.

If all the connection resources of a communication partner are assigned, no new connections can be established. Each type of communication is considered in detail below. Any number of combinations are possible however as long as the available connection resources are taken into account.

###### S7 connections via integrated interface

With S7 connections via the integrated MPI/PROFIBUS DP/PN interface, one connection resource is assigned for the endpoint on the CPU per S7 connection. This applies to all S7-300/400/1200/1500 CPUs.

![S7 connections via integrated interface](images/42107444875_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Assigned S7 connection resource on the CPU |
| ② | Subnet (e.g., MPI, PROFIBUS-DP, or Industrial Ethernet/PROFINET) |

- S7-300/400 CPU: One S7 connection resource is assigned on the CPU.
- S7-1200/1500 CPU: One S7 connection resource is assigned on the CPU and thus also one S7 connection resource on the station.

###### S7 connections via external interfaces

With S7 connections via an external CP interface, a distinction should be made between the following scenarios:

- S7-300 CPU

  - S7 connection configured at one end: One S7 connection resource is assigned on the CPU (for the endpoint) and one S7 connection resource on the CP (transition point) for each S7 connection.

    ![S7 connections via external interfaces](images/42107431819_DV_resource.Stream@PNG-de-DE.png)

    | Symbol | Meaning |
    | --- | --- |
    | ① | One S7 connection resource in the CPU and one in the CP of the local end point |
    | ② | Connection partner |
    | ③ | Subnet, e.g., Industrial Ethernet |
  - S7 connection configured at both ends: One S7 connection resource is assigned on the CP for each S7 connection.

    ![S7 connections via external interfaces](images/42107483787_DV_resource.Stream@PNG-de-DE.png)

    | Symbol | Meaning |
    | --- | --- |
    | ① | One S7 connection resource in the CP of the local end point |
    | ② | Connection partner |
    | ③ | Subnet, e.g., Industrial Ethernet |
- S7-400 CPU

  One S7 connection resource is assigned on the CPU (for the endpoint) and one S7 connection resource on the CP (transition point) for each S7 connection.

  ![S7 connections via external interfaces](images/42107483787_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | One S7 connection resource in the CPU and one in the CP of the local end point |
  | ② | Connection partner |
  | ③ | Subnet, e.g., Industrial Ethernet |
- S7-1200/1500 CPU

  - S7 connection configured at one end: One S7 connection resource is assigned on the CPU and thus also one S7 connection resource on the station for each S7 connection.

    ![S7 connections via external interfaces](images/42107431819_DV_resource.Stream@PNG-de-DE.png)

    | Symbol | Meaning |
    | --- | --- |
    | ① | One S7 connection resource in the CPU and one in the CP of the local end point |
    | ② | Connection partner |
    | ③ | Subnet, e.g., Industrial Ethernet |
  - S7 connection configured at both ends: One S7 connection resource is assigned on the CPU and thus also one S7 connection resource on the station for each S7 connection.

    ![S7 connections via external interfaces](images/42107483787_DV_resource.Stream@PNG-de-DE.png)

    | Symbol | Meaning |
    | --- | --- |
    | ① | One S7 connection resource in the CP and, thus, also one in the station |
    | ② | Connection partner |
    | ③ | Subnet, e.g., Industrial Ethernet |

> **Note**
>
> The number of reserved S7 connection resources for the selected CPU for certain CPU types of the S7-300, and for the selected CPU and its connected communication modules for the S7-1200/1500, can be seen in the area navigation under "Connection resources". S7 connection resources for OP/PG and S7 basic communication can be reserved here.

###### Connections for open communication services (SEND/RECEIVE interface)

Communication via the SEND/RECEIVE interface is solely via CPs. For this, one protocol-specific connection resource is allocated for the endpoint per connection (i.e., FDL, ISO transport ISO on TCP, UDP and TCP connection).

Here, no connection resources are required for the connection on the CPU.

![Connections for open communication services (SEND/RECEIVE interface)](images/42107510283_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | 1 assigned connection resource in the CP |
| ② | Subnet, e.g., Industrial Ethernet |

Exception: on the S7-400 CPU, connections with the property "SPEED SEND/RECEIVE" require an additional S7 connection resource for each "SPEED SEND/RECEIVE" connection on the CPU.

###### Connection resources and connection type

###### Setting up the connection

Often, you can decide between a configured setup or a programmed setup. The programmed setup makes it easier to release connection resources following data transfer. With configured setup, you receive help in managing connection resources in STEP 7.

Setting up the communication service

| Communication service | Automatic setup | Programmed setup | Configured setup |
| --- | --- | --- | --- |
| PG communication | X | - | - |
| HMI communication | X | - | X |
| S7 communication | - | X | X |
| Open communication via TCP/IP | - | X | X |
| Open communication via ISO-on-TCP | - | X | X |
| Open communication via UDP | - | X | X |
| Open communication via ISO | - | X | X |
| Open communication via e-mail | - | X | - |
| Open communication via FTP | - | X | - |
| Open communication via FDL | - | X | X |
| S7 routing | - | - | X |
|  |  |  |  |

###### Assignment of connection resources according to the connection setup

Connection resources are assigned in different ways, depending on the type of connection setup:

- Configured setup

  In the case of configured connections, the connection resource is assigned as soon as the hardware configuration has been downloaded to the CPU. For OPC servers, the resources are assigned, as required.
- Programmed setup

  The call of the appropriate instructions for establishing the connection (using TSEND_C or T_CON) triggers assignment of a connection resource.
- Automatic setup

  As soon as you have connected the programming device or HMI device to a CPU physically and online, the connection resources will be assigned.

###### Connection resources for configured setup

You set up the connection in the network view of the hardware and network editor in the context of a CPU.

Following the data transfer, the connection is not terminated, i.e., the connection resources remain permanently assigned. To terminate the connection you must delete the connection configuration and download the modified configuration to the CPU.

OPC connections are automatically established and terminated as needed.

If you have **configured** the connections, compliance with the maximum possible number of connection resources in the automation system will be monitored.

###### Connection resources for programmed setup

You set up the connection in the program editor in the context of a CPU by parameter assignment of instructions for communication, e.g., TSEND_C.

Once the connection is established by the TCON or TSEND_C instruction, the connection will be terminated through appropriate parameter assignment of the TSEND_C instruction or by calling the TDISCON instruction after the data transfer. If the connection is terminated, the connection resources in the CPU/CP/CM are available again. If the connection is retained and another data transfer is performed, the processing time of the instructions will be shorter because the connection does not have to be reestablished.

If the establishment and termination of connections are **programmed** in the user program, you are responsible for ensuring compliance with the automation system limits. If necessary, you will receive a communication error at the "STATUS" output parameter of the TSEND_C or T_CON instruction and can obtain more detailed information from the connection diagnostics.

###### Connection resources for automatic setup

The connection will be set up automatically (e.g., programming device or HMI connection) as soon as the PG/PC interface has been physically connected to an interface of the CPU and the assignment to the interface has been made in the "Go online" dialog.

For **automatically** set up connections, compliance with the connection resources reserved in the automation system for these connections is monitored.

---

**See also**

[TCON: Establish communication connection (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)
  
[TDISCON: Terminate communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tdiscon-terminate-communication-connection-s7-1200-s7-1500)
  
[TCON: Establish communication connection (S7-300, S7-400)](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#tcon-establish-communication-connection-s7-300-s7-400)
  
[TDISCON: Terminate communication connection (S7-300, S7-400)](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#tdiscon-terminate-communication-connection-s7-300-s7-400)
  
[TSEND_C: Send data via Ethernet (S7-1200)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-send-data-via-ethernet-s7-1200)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)

###### S7-1200 connection resources: (S7-1200)

This section contains information on the following topics:

- [Display of connection resources (S7-1200)](#display-of-connection-resources-s7-1200)

###### Display of connection resources (S7-1200)

###### Connection resources in the Inspector window

You will find an overview of the reserved and available connection resources of an S7-1200 automation system in the inspector window of the hardware and network editor under the CPU properties.

###### Overview of connection resources

The CPU supports the following number of simultaneous, asynchronous communication connections for PROFINET and PROFIBUS. The maximum number of reserved connection resources assigned to each category is predefined. You cannot modify the values. The freely available connections can, however, be used to increase the number of connections in each category as required by your application.

Some connection types have a fixed number of reserved resources (guaranteed resources). Example: At least 12 HMI connections can be established to the CPU simultaneously. Additional connections can be established, but the connection resources must come from the pool of dynamic connection resources.

Dynamic or free connection resources can be used for any type of connection or communication. These resources are used by connections that have no reserved connection resources (e.g. OPC UA) or by connections that have used up all their reserved connections.

If you use OPC UA communication, you must ensure that sufficient dynamic connection resources are available for this purpose.

As of TIA Portal V17 (CPU firmware as of V4.5), S7-1200 CPUs have 34 dynamic resources.

![Overview of connection resources](images/143024209931_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If you add CM/CP modules, the total number of S7-1200 communication resources is not increased.

**Station resources**

The columns of the station-specific connection resources provide information about the reserved and dynamically available connection resources of the station. In the example, a maximum of 68 station-specific connection resources are available for the automation system.

- 34 connection resources are reserved for specific connection types
- 34 connection resources can be used freely for connection types

The warning triangle in the column of the dynamic station resources is displayed because the sum of the maximum available connection resources of the CPU has reached the station limit of 68.

> **Note**
>
> **Exceeding the available connection resources**
>
> STEP 7 signals the reaching of the station-specific connection resources with a warning. If you require more connection resources, you either have to use a CPU with a higher maximum number of available station-specific connection resources or reduce the number of communications connections.

**Module-specific connection resources**

The columns of the module-specific connection resources provide information about the allocation of resources on the CPUs, CPs and CMs of an automation system: The display is per module and not per interface. In the example, the CPU provides a maximum of 68 connection resources.

**Online view**

If you are connected to the CPU online, you can also see how many resources are currently being used in the "Connection information" tab of the "Diagnostics" section in the Inspector window.

The online view of the "Connection resources" table not only displays the reserved and dynamic connection resources of the configured connections, but also includes columns containing the connection resources of the programmed and automatically set-up connections that are currently allocated in the station. Thus, the online view displays **all** the assigned connection resources in the automation system, regardless of how the connection was set up. The "Other communication" row displays connection resources assigned for communication with external devices and communication via data record routing.

The table is updated automatically. If there are inconsistencies between the configured hardware configuration and the hardware configuration available online, a corresponding message will be output.

###### Resource requirements of the connections

The following number of connections per communication type is available: Note that not all specified maximum connection resources are available, because the dynamic connection resources are divided among the different communication types.

|  | Programming device communication | HMI communication | S7 communication | Open User Communication | Web communication | OPC UA client/server | Other communication |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maximum number of connection resources of a S7-1200 CPU | 4  (guaranteed support of 4 PG connections) | 18  (guaranteed support of 12 HMI connections) | 14  (guaranteed support of 8 S7 connections) | 14  (guaranteed support of 8 OUC connections) | 30  (guaranteed support of 2 HTTP connections) | 10 | - |

The communication connections of Open User Communication, S7 communication, HMI communication, PG communication and Web communication can utilize several connection resources depending on the functions used.

**Programming device communication**

For example, four connection resources are reserved for one PG communication. Depending on the currently used programming device functions, the programming device occupies up to three connection resources for a connection. With the S7-1200, at least one programming device connection is guaranteed at all times.

**HMI communication**

A further example is the number of HMI devices as shown in the following figure. 12 connection resources are reserved for HMI devices. Depending on the type or model of your HMI device and the HMI functions used, an HMI device can require up to three connection resources for a single HMI connection. For example, a Basic Panel requires one connection resource in the CPU for an HMI connection, while a Comfort Panel requires up to two connection resources in the CPU. Depending on the number of required connection resources, at least four HMI connections can be configured simultaneously.

An HMI device can use its available connection resources for the following functions:

- Reading
- Writing
- Interrupts and diagnostics

This is only an example. The actual number of connections can differ depending on the type and version of the HMI device.

| Example | HMI 1 | HMI 2 | HMI 3 | HMI 4 | HMI 5 | Total number of connection resources |
| --- | --- | --- | --- | --- | --- | --- |
| Used connection resources | 2 | 2 | 2 | 3 | 3 | 12 |

Information regarding the availability and assignment of connection resources for HMI connections is available in the offline view in the HMI device context (under "Properties &gt; General &gt; Connection resources" in the Inspector window):

![Resource requirements of the connections](images/128427731723_DV_resource.Stream@PNG-en-US.png)

The following is displayed in the connection resources area:

- Number of available connections on the HMI reserved for HMI communication and HTTP communication
- Number of connection resources for HMI communication and HTTP communications used offline in the HMI

  If the maximum number of available connection resources for an HMI device is exceeded, a corresponding alarm is output by STEP 7.
- Maximum number of used PLC resources per HMI connection. This parameter is a factor that is to be multiplied by the number of HMI connections used offline. The product is the number of HMI resources occupied on the CPU.

If the maximum number of available connection resources for an HMI device is exceeded, a corresponding alarm is output.

**Web communication**

The CPU provides web connections for multiple web browsers. The number of browsers that can be supported simultaneously by the CPU depends on the number of connections that a Web browser requests/utilizes.

###### Connection resources S7-1500 (S7-1500)

This section contains information on the following topics:

- [Connection resources in the automation system (S7-1500)](#connection-resources-in-the-automation-system-s7-1500)
- [Allocation of connection resources (S7-1500)](#allocation-of-connection-resources-s7-1500)
- [Details about OPC UA client/server connections (S7-1500)](#details-about-opc-ua-clientserver-connections-s7-1500)
- [Display of the connection resources (S7-1500)](#display-of-the-connection-resources-s7-1500)
- [Example for calculating the connection resources (S7-1500)](#example-for-calculating-the-connection-resources-s7-1500)
- [Data consistency (S7-1500)](#data-consistency-s7-1500)

###### Connection resources in the automation system (S7-1500)

###### Introduction

Some communications services require connections. Connections occupy resources in the automation system. The connection resources are made available by the CPUs, communications processors (CPs) and communications modules (CMs).

###### Connection resources of a station

The connection resources available depend on the CPUs, CPs and CMs and may not exceed a maximum number per station. The maximum number of resources of a station is determined by the CPU.

Each CPU has reserved connection resources for PG, HMI and Web server communication. This ensures, for example, that a PG can always establish at least one online connection with the CPU regardless of how many other communications services are already using connection resources. In addition, there are dynamic resources. The difference between the maximum number of connection resources and the number of reserved connection resources is the maximum number of dynamic connection resources. The communication services programming device communication, HMI communication, S7 communication, Open User Communication, Web communication and other communication (e.g. OPC UA) make use of the pool of dynamic connection resources.

The following figure shows an example of how individual components provide connection resources to an S7‑1500 station.

![Connection resources of a station](images/90812957707_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| ① | Available connection resources of the station, of which |  |
| A | Reserved connection resources of the station |  |
|  | A + B | Connection resources of CPU 1518 |
|  | C | Connection resources of communications module CM 1542‑1 |
|  | D | Connection resources of the communication processor CP 1543‑1 / CP 1545‑1 |
| ② | Maximum communication resources of the station using the example of a configuration from CPU 1518, CM 1542‑1 and CP 154x‑1 |  |

###### Number of connection resources of a station

The following table shows the maximum available connection resources for some CPU types:

| Connection resources of a station |  | 1511 1511C | 1512C  1513 | 1515 | 1516 | 1517 | 1518 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Maximum connection resources of the station |  | 96 | 128 | 192 | 256 | 320 | 384 |
|  | of which reserved | 10 |  |  |  |  |  |
|  | of which dynamic | 86 | 118 | 182 | 246 | 310 | 374 |
| Connection resources of the CPU |  | 64 | 88 | 108 | 128 | 160 | 192 |
| Max. additionally usable connection resources by plugging in CMs/CPs |  | 32 | 40 | 84 | 128 | 160 | 192 |
| Additional connection resources CM 1542‑1 |  | 64 |  |  |  |  |  |
| Additional connection resources CP 154x‑1 |  | 118 |  |  |  |  |  |
| Additional connection resources CM 1542‑5 |  | 40 |  |  |  |  |  |
| Additional connection resources CP 1542‑5 |  | 16 |  |  |  |  |  |

The number of connection resources supported by a CPU or a communication module is described in the technical specifications section of the manuals.

###### Example

You have configured a CPU 1518-4PN/DP with a communications module CM 1542-1 and a communications processor CP 1542-5.

- Maximum connection resources of the station: **384**
- Available connection resources:

  - CPU 1518-4 PN/DP: 192
  - CM 1542-1: 64
  - CP 1542-5: 16
  - Total: **272**

The setup provides 272 connection resources. By adding further communication modules the station can support a maximum of 112 additional connection resources.

###### Reserved connection resources

10 connection resources are reserved for stations with S7‑1500 CPU, ET 200SP CPU and ET 200pro CPU based on S7-1500:

- 4 for programming device communication required by STEP 7, for example, for testing and diagnostic functions or loading into the CPU.
- 4 for HMI communication occupied by the first HMI connections configured in STEP 7.
- 2 for communication with the Web server

###### Allocation of connection resources (S7-1500)

###### Overview - occupation of connection resources

The following figure shows how different connections occupy the resources of the S7-1500:

![Overview - occupation of connection resources](images/89094852235_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | HMI communication: See below. |
| ② | Open User Communication: Connections of Open User Communication occupy a connection resource in every end point. |
| ③ | S7 communication: Connections of S7 communication occupy a connection resource in every end point. |
| ④ | Web communication: The Web server connection occupies at least one connection resource in the station. The number of occupied connections depends on the browser. |
| ⑤ | PG communication: The PG connection occupies one connection resource in the station. |
| ⑥/⑦ | OPC UA client/server communication: Each session that the OPC UA server of the CPU establishes with an OPC UA client as a rule occupies one connection resource in the station.  Information about the connection resources of the OPC UA client: See below. |
| ![Overview - occupation of connection resources](images/89094373131_DV_resource.Stream@PNG-de-DE.png) | Connection resource for HMI communication |
| ![Overview - occupation of connection resources](images/89094731787_DV_resource.Stream@PNG-de-DE.png) | Connection resource for Open User Communication |
| ![Overview - occupation of connection resources](images/89094718859_DV_resource.Stream@PNG-de-DE.png) | Connection resource for S7 communication |
| ![Overview - occupation of connection resources](images/89094783371_DV_resource.Stream@PNG-de-DE.png) | Connection resource for Web communication |
| ![Overview - occupation of connection resources](images/89094744715_DV_resource.Stream@PNG-de-DE.png) | Connection resource for PG communication |
| ![Overview - occupation of connection resources](images/89094796299_DV_resource.Stream@PNG-de-DE.png) | Connection resource for OPC UA client/server communication see below |

###### Connection resources for HMI communication

With HMI communication, the occupation of connection resources in the station depends on the HMI device being used. The following table lists the maximum number of occupied connection resources for an HMI connection depending on the various HMI devices:

| HMI device | Maximum number of allocated connection resources of the station for each HMI connection |
| --- | --- |
| Basic Panel | 1 |
| Comfort Panel | 2<sup>1</sup> |
| RT Advanced | 2<sup>1</sup> |
| RT Professional | 3 |
| <sup>1</sup> If you do not use system diagnostics or alarm configuration, the station occupies only one connection resource per HMI connection. |  |

**Example:** You have configured the following HMI connections for a CPU 1516‑3 PN/DP:

- Two HMI connections to an HMI TP700 Comfort (2 connection resources each)
- One HMI connection to an HMI KTP1000 Basic (1 connection resource)

A total of 5 connection resources are allocated for HMI communication in the CPU.

###### Connection resources for routing

**S7 connections beyond network boundaries (S7 routing)**

To transfer data beyond S7 subnets ("S7 routing"), an S7 connection is established between two CPUs. The S7 subnets are connected via gateways known as S7 routers. The router is the transition point of an S7 connection and is capable of establishing S7 connections. CPUs, CMs and CPs in S7‑1500 are S7 routers.

The following applies for a routed S7 connection:

- A routed connection occupies one connection resource each in both end points. STEP 7 shows these connection resources in the "Connection resources" table.
- On the S7 router, two special connection resources are occupied for S7 routing. STEP 7 does not display the special connection resources for S7 routing in the "Connection resources" table. The number of resources for S7 routing depends on the CPU. You will find the resources for S7 routing in the technical specifications of the CPU in "Number of S7 routing connections".

The following figure shows the allocation of the connection resources at S7 routing:

![Connection resources for routing](images/89094865163_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ![Connection resources for routing](images/89094718859_DV_resource.Stream@PNG-de-DE.png) | Connection resource for S7 communication |
| ![Connection resources for routing](images/89094770443_DV_resource.Stream@PNG-de-DE.png) | Special connection resources for S7 routing |

**Data record routing**

Data record routing also enables transfer of data beyond S7 subnets from an engineering station connected to PROFINET to various field devices via PROFIBUS.

With data record routing, as with S7 routing, two of the special connection resources for S7 routing are also occupied at the network transitions in every record router. At the end point of communication (CPU), connection resources for data record routing are displayed in the online view of the "Connection resources" table in the "Other communication" row.

> **Note**
>
> **Connection resources with data record routing**
>
> With data record routing, on the data record router, two special connection resources for S7 routing are occupied. Neither the data record connection nor the allocated connection resources are displayed in the table of connection resources. You are responsible for observing the limits during configuration.

###### When are connection resources occupied?

The time for the occupation of connection resources depends on how the connection is set up.

- Programmed setup of a connection

  As soon as an instruction to establish a connection is called in the user program of the CPU (TSEND_C/TRCV_C or TCON), a connection resource is occupied. With suitable parameter assignment of the CONT parameter of the TSEND_C/TRCV_C instructions or by calling the TDISCON instruction, the connection can be terminated following data transfer and the connection resource is available again. If the connection is terminated, the connection resources on the CPU/CP/CM are available again.
- Configured connections (e.g. HMI connection)

  If you have configured a connection in STEP 7, the connection resource is occupied as soon as the hardware configuration is loaded to the CPU. After using a configured connection for data transfer, the connection is not terminated. The connection resource is permanently occupied. To release the connection resource again, you need to delete the configured connection in STEP 7 and download the modified configuration to the CPU.
- Programming device connection

  As soon as you have connected the programming device to a CPU online in STEP 7, connection resources are occupied.
- Web server

  As long as you have opened the Web server of the CPU in a browser, connection resources are occupied in the CPU.
- OPC UA server

  Each connection to the OPC UA server of the CPU occupies one connection resource in the station. This connection resource is released immediately when the connection is terminated.
- OPC UA client

  Each connection that the OPC UA client of the CPU has established to an OPC UA server occupies one connection resource in the station. When establishing an OPC UA connection, the OPC UA client temporarily occupies an additional connection resource. After terminating an OPC UA connection, the connection resource is not released again after a wait time of approx. 60 seconds in accordance with RFC 793 (see [Details about OPC UA client/server connections](#details-about-opc-ua-clientserver-connections-s7-1500)).
- "TCONSettings" instruction

  After the instruction "TCONSettings" with MODE=0 is called successfully, a new OUC connection is prepared, that is, a new connection ID is available and a connection resource has been allocated.

###### Monitoring the maximum possible number of connection resources

**Offline**

During configuration of connections, STEP 7 monitors the occupation of the connection resources. If the maximum possible number of connection resources is exceeded, STEP 7 signals this with a suitable warning.

**Online**

The CPU monitors the use of connection resources in the automation system. If you establish more connections in the user program than those provided by the automation system, the CPU acknowledges the instruction to establish the connection with an error.

###### Details about OPC UA client/server connections (S7-1500)

Connection resource bottlenecks can occur temporarily with OPC UA client/server communication, but only if the CPU is heavily loaded by communication requests.

The following are requirements for understanding temporary connection resource bottlenecks:

- The connection termination for TCP-based communication such as OPC UA temporarily occupies resources even after the connection has been closed (disconnected).
- The connection setup for OPC UA is basically 2-stage: First, the client establishes a connection for the discovery process, only then the productive connection.
- The number of possible OPC UA connections is determined by 2 limits. The behavior during a connection setup depends on which limit is reached first:

  - The maximum possible number of OPC UA client/server connections per se
  - The maximum possible number of resources of the "connection pool", which allows a variable use of resources

**Basic termination of TCP-based connections**

The following figure shows how a terminated connection continues to occupy resources for a period.

![Principle: Termination of an OPC UA connection](images/127358030987_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Disconnect: Client initiates connection termination |
| ② | "Orderly" shutdown of the connection according to RFC 793 (Transmission Control Protocol): The resource for the client (more precisely, for the partner that terminates the connection) remains occupied (approx. 60 seconds), the resource for the server (more precisely, the partner who is notified of the disconnection) is released immediately; the connection is displayed as "disconnected" at the client. Even if the "OPC_UA_Disconnect" instruction is terminated with "Done", the resource remains occupied for the duration of the waiting time. |
| ③ | Connection is terminated and the required waiting time for acknowledgment of the partner has elapsed; resource is also released at the client. |

Principle: Termination of an OPC UA connection

###### Basic establishment of an OPC UA client/server connection

An OPC UA connection is established in 2 stages depending on the system: First, a connection is established for the discovery process and then closed again after receiving the requested information. Only then is the productive connection established.

Together with the connection termination procedure described above, this results in a temporary allocation of 2 resources at the client.

![Principle: Establishment of an OPC UA connection](images/127358837003_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Connection for the discovery process: Occupies a resource at the client and the server |
| ② | Productive connection: Occupies a resource at the client and the server |
| ③ | Parallel discovery and productive connection: Only two resources are temporarily reserved for the client. |

Principle: Establishment of an OPC UA connection

###### Flexible model for managing connection resources

All connection types share a pool of connection resources in the CPU.

Boundary conditions:

- Reserved resources for certain connection types (programming device and HMI) reduce the number of freely available resources.
- For OPC UA client/server connections, there is a "separate" high limit for each CPU performance class similar to other connection types: Example: maximum 64 for the OPC UA server and maximum 40 for the OPC UA client with CPU 1518).

  You have the possibility to reduce the limit of possible connections to the server using the CPU parameter "Max. number of OPC UA sessions" in the "OPC UA &gt; Server &gt; Settings" area. For example, the CPU 1518 is preset to a value of 20.
- Example for custom high limits for specific other connection types, which prevent unrestricted use of the connection pool:

  Web communication with a maximum of 80 connections.

  Additional restrictions can result from the configuration limits of the individual interfaces.

The following figure shows in simplified form, for example, how additional demand for open-user communication connections is possible at the expense of other connections. In this case, the OPC UA client/server communication "suffers". It is also indicated that the two-stage connection establishment with OPC UA temporarily leads to higher resource requirement.

![Principle: Temporary resource consumption](images/127359067019_DV_resource.Stream@PNG-de-DE.png)

Principle: Temporary resource consumption

###### Tips and rules for working with OPC UA connections

You will find here once again the tips and rules from the explanations in summary.

- If you are at the limit with the number of required connections, OPC UA client/server connections should be established "stretched" over time one after the other on the client side. If OPC UA client/server connections are established at short intervals, there is a danger of a resource bottleneck (see description above for TIME_WAIT).
- Since OPC UA client/server connections are established in two stages and only use an additional connection temporarily, OPC UA client/server connections should be established first and only then the other connection types (HMI, OUC, etc.). The OPC UA client/server connections can then first be used from the resource pool to establish the connection unhindered.
- When planning resources for connections, at least one resource should remain unused. Background: If all connection resources are occupied and an OPC UA connection is interrupted, it cannot be re-established. Reason: Temporarily, two connection resources are required to re-establish this connection.

###### Display of the connection resources (S7-1500)

###### Connection resources in the Inspector window

You will find an overview of the reserved available connection resources of an S7-1500 automation system in the Inspector window of the hardware and network editor under the CPU properties.

###### Display of the connection resources in STEP 7 (offline view)

The display of connection resources distinguishes between the offline and online view. The following figure shows you the offline display of the reserved and available connection resources of an S7-1500 CPU with a CP and a CM:

![Display of the connection resources in STEP 7 (offline view)](images/128427710475_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Station-specific connection resources |
| ② | Module-specific connection resources |

**Station-specific connection resources**

The columns of the station-specific connection resources provide information about the reserved and dynamically available connection resources of the station. In the example, a maximum of 256 station-specific connection resources are available for the automation system.

- 10 reserved connection resources, of which 4 are already in use and a further 6 still available.  
  The occupied 4 resources are used for HMI communication.
- 246 dynamic connection resources, of which 26 are already in use and a further 220 still available.  
  The configured resources are divided up as follows:

  - 6 resources for HMI communication
  - 7 resources for S7 communication
  - 13 resources for Open User Communication

The warning triangle in the column of the dynamic station resources is therefore displayed because the sum of the maximum available connection resources of CPU, CP and CM (= 310 connection resources) exceeds the station limit of 256.

> **Note**
>
> **Exceeding the available connection resources**
>
> STEP 7 signals the exceeding of the station-specific connection resources with a warning. To make full use of the connection resources from the CPU, CP and CM, either use a CPU with a higher maximum number of available station-specific connection resources or reduce the number of communications connections.

**Module-specific connection resources**

The columns of the module-specific connection resources provide information about the allocation of resources on the CPUs, CPs and CMs of an automation system: The display is per module and not per interface. In the example, the CPU makes a maximum of 128 connection resources available, of which 18 are already in use and a further 110 still available.  
The configured resources are divided up as follows:

- 6 resources for HMI communication
- 4 resources for S7 communication
- 8 resources for Open User Communication

The CP makes 118 resources and the CM 64 resources available, of which 4 or 8 resources are used.

###### Display of the connection resources in STEP 7 (online view)

If you are connected to the CPU online, you can also see how many resources are currently being used in the "Connection information" tab of the "Diagnostics" section in the Inspector window. The following figure shows you the online display of the reserved, available and used connection resources of an S7-1500 CPU:

![Display of the connection resources in STEP 7 (online view)](images/128427714827_DV_resource.Stream@PNG-en-US.png)

The online view of the "Connection resources" table not only displays the reserved and dynamic connection resources of the configured connections, but also includes columns containing the connection resources of the programmed and automatically set-up connections that are currently allocated in the station. Thus, the online view displays **all** the assigned connection resources in the automation system, regardless of how the connection was set up. The "Other communication" row displays connection resources assigned for communication with external devices and communication via data record routing.

The table is updated automatically. If there are inconsistencies between the configured hardware configuration and the hardware configuration available online, a corresponding message will be output.

> **Note**
>
> If a routed S7 connection goes through a CPU, the required connection resources of the CPU do not appear in the table of connection resources!

###### Display of the connection resources for HMI

For HMI communication, connection resources in the CPU are assigned according to the HMI device used and the applications in which the HMI device is used. For example, a Basic Panel requires up to two connection resources in the CPU for an HMI connection, while a Comfort Panel requires up to three connection resources in the CPU.

Information regarding the availability and allocation of connection resources for HMI connections is available in the offline view in the HMI device context (under "Properties &gt; General &gt; Connection resources" in the Inspector window).

![Display of the connection resources for HMI](images/128427731723_DV_resource.Stream@PNG-en-US.png)

The following is displayed in the connection resources area:

- Number of available connections on the HMI reserved for HMI communication and HTTP communication
- Number of connection resources for HMI communication and HTTP communications used offline in the HMI

  If the maximum number of available connection resources for an HMI device is exceeded, a corresponding alarm is output by STEP 7.
- "Maximum number of used PLC resources per HMI connection". This parameter is a factor that is to be multiplied by the number of HMI connections used offline. The product is the number of HMI resources occupied on the CPU.

If the maximum number of available connection resources for an HMI device is exceeded, a corresponding alarm is output.

###### Displaying the connection resources in the Web server

You can display the connection resources not only in STEP 7, but also with a browser that displays the relevant page of the Web server. You will find information on displaying connection resources in the Web server in the function manual for the Web server.

###### Example for calculating the connection resources (S7-1500)

###### Introduction

This example for the table displaying connection resources shows you how the individual table entries are put together.

###### Requirement

- 2x CPU 1516-3 PN/DP each with one CP 1543-1 and one CM 1542-5as connection partners for the purpose of extending the configuration limit.
- 1 x PC system WinCC RT Professional with CP 1616 onboard as connection partner for HMI connections
- The devices are networked together.

###### Creating the connections

Once the connection partners (CPUs, CPs, CMs, WinCC RT Professional) have been created and networked in the network view of the hardware and network editor, follow these steps:

1. Switch to connection mode in the network view.
2. Create the following connections:

   - S7 connections: 2x via CPU, 21x via CM
   - TCP connections: 2x via CPU, 4x via CM
   - ISO connection: 6x via CP
   - ISO-on-TCP: 3x via CPU, 4x via CM
   - UDP connections: 4x via CPU, 106x via CP
   - HMI connections: 1x via CPU, 2x via CP

###### Result

The display of connection resources shows you not only the available resources but also the resources required for the created connections.

The available resources of devices and modules are highlighted in the following figure.

![Result](images/88494112139_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Depending on the CPU, at most 256 connections are available for this station. Ten (10) resources are reserved for particular connection types and 246 resources are dynamically available. |
| ② | The CPU provides 128 connection resources, and the CP and CM each provide another 118 resources. |
| ③ | CPU, CP, and CM altogether provide 128 + 118 + 118 = 364 resources. Because more connection resources are provided via the devices and modules than the station can operate with its maximum limit of 256 connection resources, a warning icon is displayed. |

The following figure highlights the resources utilized by the created connections:

![Result](images/88494116747_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | These are the resources assigned via the HMI connections. In this example, one HMI connection utilizes 3 connection resources. For the whole station, 3 + 6 = 9 connection resources are required for the HMI communication. |
| ② | Four (4) resources are reserved for the HMI communication. |
| ③ | The 9 resources required for HMI communication are broken down as follows: For the first 4 resources, the resources already reserved for HMI communication will be used. The other 5 required resources will be taken from the dynamic resources. |
| ④ | These are the resources assigned via the S7 connections. An S7 connection occupies 1 connection resource. For the whole station, 2 + 21 = 23 connection resources are required. |
| ⑤ | For the S7 communication, there are no reserved resources. All 23 required resources come from the dynamically available resources. |
| ⑥ | These are the resources of the Open User Communication (for TCP, FDL, ISO, ISO-on-TCP, and UDP). For the whole station, 9 + 112 + 8 = 129 connection resources are required. |
| ⑦ | For the Open User Communication, there are no reserved resources. All 129 required resources come from the dynamically available resources. |

###### Calculation of connection resources

Based on the available and utilized resources of individual devices and modules, the resources that are still free and the total resources used are calculated:

![Calculation of connection resources](images/88494172555_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | All required resources for the respective communication types of the CPU are displayed here. Three (3) resources are required for HMI communication, 2 for S7 communication, and 9 for the connection types of the Open User Communication. |
| ② | The total number of resources required is listed below the required resources for the communication types. For the CPU, therefore, 3 + 2 + 9 = 14 resources are required. |
| ③ | The CP 1543-1 has 118 available connection resources. If these are utilized, no more connections can be created for the CP. |
| ④ | For the CP 1543-1, 118 connection resources are already utilized by the 2 HMI connections (3 resources each = 6 resources) and 112 resources by connections of the open communication. |
| ⑤ | The CP 1543-1 has no more free resources. No more connections can be created for the CP 1543-1. |

The number of resources still available and the total number of resources used is also displayed for the whole station:

![Calculation of connection resources](images/88494177163_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | All connection resources used (configured), including both reserved and dynamic connection resources, for the individual communication types for the entire station. The values represent the sum of all resources utilized for devices and modules (CPU, CP, CM). |
| ② | All connection resources used (configured), including both reserved and dynamic connection resources, for all communication types for the entire station. |
| ③ | Total number of reserved and dynamic connection resources still available. The values are obtained by subtracting the number of resources used from the maximum number of resources that can be configured. |

###### Data consistency (S7-1500)

###### Definition

Data consistency is important for data transfer and you need to take this into account when configuring the communication task. Otherwise, malfunctions may occur.

A data area which cannot be modified by concurrent processes is called a consistent data area. This means that a data area which belongs together and which is larger than the maximum size of the consistent data area can consist in part of new and of old data at the same time.

An inconsistency can occur when an instruction for communication is interrupted, for example by a hardware interrupt OB with higher priority. This interrupts the transfer of the data area. If the user program in this OB now changes the data that has not yet been processed by the communication instruction, the transferred data originates from different times:

The following figure shows a data area that is smaller than the maximum size of the consistent data area. In this case, when transferring the data area, it is ensured that there is no interruption by the user program during data access so that the data is not changed.

![Consistent transfer of data](images/89095879947_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The source data area is smaller than the maximum size of the consistent data area (②). The instruction transfers the data together to the destination data area. |
| ② | Maximum size of the consistent data area |

Consistent transfer of data

The following figure shows a data area that is larger than the maximum size of the consistent data area. In this case, the data can be changed during an interruption of the data transfer. An interruption also occurs if, for example, the data area needs to be transferred in several parts. If the data is changed during the interruption, the transferred data originates from different times.

![Transfer of data larger than the maximum consistency area](images/89095892875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The source data area is larger than the maximum size of the consistent data area (③). At time T1, the instruction only transfers as much data from the source data area to the destination data area as fit in the consistent data area. |
| ② | At time T2, the instruction transfers the rest of the source data area to the destination data area. After the transfer, data from different points in time exist in the destination data area. If the data in the source data area has changed in the meantime, an inconsistency may result. |
| ③ | Maximum size of the consistent data area |

Transfer of data larger than the maximum consistency area

###### Example of an inconsistency

The figure below shows an example of changing data during the transfer. The destination data area contains data from different points in time.

![Example: Changing data during the transfer](images/89095982603_DV_resource.Stream@PNG-en-US.png)

Example: Changing data during the transfer

###### System-specific maximum data consistency for S7‑1500:

No inconsistency occurs if the system-specific maximum size of the consistent data is kept to. With an S7-1500, communication data is copied consistently into or out of the user memory in blocks of up to 512 bytes during the program cycle. Data consistency is not ensured for larger data areas. Where defined data consistency is required, the length of communication data in the user program of the CPU must not exceed 512 bytes. You can then access these data areas consistently, for example from an HMI device by reading/writing tags.

If more data than the system-specific maximum size needs to be transferred consistently, you yourself must ensure the data consistency with suitable measures in the user program.

###### Ensuring data consistency

**Use of instructions for access to common data:**

If the user program contains instructions for communication that access common data, for example TSEND/TRCV, you can coordinate access to this data area yourself, for example using the "DONE" parameter. The data consistency of the data areas that are transferred with an instruction for communication can therefore be ensured in the user program.

> **Note**
>
> **Measures in the user program**
>
> To achieve data consistency, you can copy transferred data to a separate data area (for example global data block). While the user program continues to work with the original data, you can transfer the data saved in the separate data area consistently with the communication instruction.
>
> For the copying, use uninterruptible instructions such as UMOVE_BLK or UFILL_BLK. These instructions ensure data consistency up to 16 KB.

**Use of** 
**PUT/GET**
 **instructions or Write/Read via HMI communication:**

In S7 communication with the PUT/GET instructions or Write/Read via HMI communication, you need to take into account the size of the consistent data areas during programming or configuration. In the user program of an S7-1500 as server, there is no instruction available that can coordinate the data transfer in the user program. The data exchanged using PUT/GET instructions updates the S7-1500 while the user program is running. There is no point in time within the processing of the cyclic user program at which the data is exchanged consistently. The length of the data area to be transferred should be smaller than 512 bytes.

###### Additional information

- You will also find the maximum amount of consistent data in the CPU, CM or CP manuals in the Technical Specifications.
- You will find further information on data consistency in the description of the instructions in the STEP 7 online help.

### Displaying and configuring topology

This section contains information on the following topics:

- [Overview of the topology view](#overview-of-the-topology-view)
- [Starting the topology view](#starting-the-topology-view)
- [Displaying topology](#displaying-topology)
- [Configuring topology](#configuring-topology)

#### Overview of the topology view

##### Functions of the topology view

The topology view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Displaying the Ethernet topology

  - Displaying all the PROFINET devices and passive Ethernet components of the project along with their ports
  - Displaying interconnections between the ports
  - Displaying corresponding logical networks
  - Display diagnostic information of all ports
- Configuring the Ethernet topology

  - Creating, modifying and deleting interconnections of the ports
  - Renaming stations, devices, interfaces or ports
  - Adding PROFINET devices and passive Ethernet components to the project from the hardware catalog
- Identifying and minimizing differences between the desired and actual topology

  - Running an offline/online comparison of Ethernet modules, ports and port interconnections
  - Adopting existing online topology information in the offline project

> **Note**
>
> **Devices without valid IP address**
>
> Topology information (LLDP) cannot be read from a device without valid IP address.
>
> To prevent devices from having an invalid IP address, specify in the settings of the TIA Portal for hardware configuration that devices without valid IP address are temporarily assigned an IP address.

> **Note**
>
> **Subnet membership**
>
> Before the topology determination, you have to set for the local interface of your PG/PC the network address that the Ethernet components that are to be determined also have in the real plant. If you do not meet this requirement, no further topology information (information about ports and neighborhood relationships) can be determined.

##### Differences between network view and topology view

- The network view shows all the logical subnets of the project.

  The topology view shows all Ethernet components of the project. These include passive components such as switches, media converters and cables.

  > **Note**
  >
  > Stations with non-Ethernet components are also displayed if the station has a least one Ethernet component.
- The position of a device in the network view and its position in the topology view are initially independent of one other; in other words, the same device generally appears at different locations in the two views.

  If you want to align the devices in the topology view as in the network view, click on the following icon in the toolbar of the topology view.

  | Icon | Meaning |
  | --- | --- |
  | ![Differences between network view and topology view](images/83418604683_DV_resource.Stream@PNG-de-DE.png) | Changes the position of the devices in the topology view so that the new position is as close as possible to the position in the network view. |
- If you open the hardware catalog in the topology view, you only see devices with an Ethernet interface.

##### Structure of the topology view

The [topology view](#topology-view) essentially consists of a graphic area (called the graphic view below) and a table area (called the table view below).

##### Which functions are there in the graphic view and which functions are there in the table view?

- Displaying the Ethernet topology

| Function | Graphic view | Table view |
| --- | --- | --- |
| Displaying all the PROFINET devices and passive Ethernet components of the project along with their ports | yes | yes |
| Display interconnections between the ports (including type of medium) | yes | yes |
| Displaying corresponding logical networks | no | yes |
| Displaying properties of the cables between the ports | no | yes |
| Display diagnostic information of all ports | yes | yes |

- Configuring the Ethernet topology

| Function | Graphic view | Table view |
| --- | --- | --- |
| Creating, modifying and deleting interconnections of the ports | - Create: yes - Modify: yes - Delete: yes | - Create: yes - Modify: yes - Delete: yes |
| Renaming stations, devices, interfaces or ports | no | yes |
| Adding PROFINET devices and passive Ethernet components to the project from the hardware catalog | yes | no |

- Identifying and minimizing differences between the desired and actual topology

| Function | Graphic view | Table view |
| --- | --- | --- |
| Running an offline/online comparison of Ethernet modules, ports and port interconnections | no | yes |
| Adopting existing online topology information in the offline project | no | yes |

##### Structure of the table view

The table view consists of the following two tabs:

- "Topology overview" tab
- "Topology comparison" tab

The "Topology overview" tab provides the following functions:

- Display of the configured topology with hierarchical structures (from the station to the port)
- Configuration of the Ethernet topology
- The display of the diagnostics status of hardware components

The "Topology comparison" tab provides the following functions:

- Identifying and minimizing differences between the desired and actual topology

#### Starting the topology view

##### Requirement

The device or network view is open in the hardware and network editor.

##### Procedure

To start the topology view of your project, follow these steps:

1. Click on the "Topology view" tab.

Or:

1. Open the network view of the hardware editor.
2. Select a PROFINET device or a PROFINET module.
3. Select the "Go to topology view" command in the shortcut menu.

##### Result

The topology view is started. If you opened the topology view using the shortcut menu, the selected component remains selected after the change of view.

#### Displaying topology

This section contains information on the following topics:

- [Displaying the graphic view of the configured topology](#displaying-the-graphic-view-of-the-configured-topology)
- [Displaying the table view of the configured topology](#displaying-the-table-view-of-the-configured-topology)
- [Displaying the diagnostics status of ports and cables in the graphic view](#displaying-the-diagnostics-status-of-ports-and-cables-in-the-graphic-view)
- [Showing the diagnostics status of hardware components in the table view](#showing-the-diagnostics-status-of-hardware-components-in-the-table-view)
- [Running an offline/online comparison and displaying the results](#running-an-offlineonline-comparison-and-displaying-the-results)
- [Running an advanced offline/online comparison and displaying the results](#running-an-advanced-offlineonline-comparison-and-displaying-the-results)

##### Displaying the graphic view of the configured topology

###### What is shown?

The graphic view of the configured topology shows the following:

- Configured PROFINET devices and passive Ethernet components along with their ports
- Configured stations with non-Ethernet components if there is at least one Ethernet component in the station
- Configured interconnections between the ports

###### Type of display

The way in which the graphic view of the topology view and the network view are displayed is very similar:

- Compared with the device view, components are shown in a simplified form.
- The interconnections between ports are shown as horizontal and vertical lines. These are dashed when an interconnection between a tool changer port and its possible partner ports is involved.

##### Displaying the table view of the configured topology

###### Requirement

- The table view of the topology is open.
- You are in the "Topology overview" tab

###### What is shown?

The table view of the configured topology shows exactly the same content as the graphic view except for the logical PROFINET subnets:

- All the configured PROFINET devices and passive Ethernet components along with their ports
- All the configured stations with non-Ethernet components if there is at least one Ethernet component in the station
- Configured interconnections between the ports

  For each port with the "Alternating partner port" property, there are as many completed rows as there are potential partner ports plus one empty row.

###### Type of display

As the name implies, the table view of the topology view consists of a table, the topology overview table. It displays the configured topology with hierarchical structures (from the station to the port) It is structured like the network overview table. It consists of the following columns:

- Device / port

  This is the most important column of the table. The entries in this column have a hierarchical structure with the PROFINET ports being the last element in the hierarchy. You can expand and collapse the hierarchical entries. For a CPU, for example, an entry consists of the following elements:

  - Station name
  - Device name
  - Name of the PROFINET interface
  - Names of the ports

  Note: All the other columns only have entries in the rows containing the port names.
- Slot

  Indicates the number of the slot in a rack in which the relevant module is installed. For interfaces, the designation of the interface is also displayed.
- Index (by default, this column is not displayed)

  This column is only relevant for PC stations. The index is the virtual slot address of the component.
- Device type (by default, this column is not displayed)

  Shows what type of station, device or interface the table row relates to or whether it belongs to a port.
- Article no. (by default, this column is not displayed)

  Article no. of the device
- Subnet (as default, this column is not displayed)

  Configured subnet to which the interface belongs
- Master/IO system (as default, this column is not displayed)

  Shows whether or not the interface belongs to a PROFIBUS DP master system or a PROFINET IO system.
- IP address (by default, this column is not displayed)

  Configured address of the interface in the subnet
- Partner station

  Name of the station that contains the partner port
- Partner device

  Name of the device that contains the partner port
- Partner interface

  Interface to which the partner port belongs
- Partner port
- Cable data

  Contains the cable length and the signal delay of the cable connecting the ports

###### Basic functions for tables

The topology overview table supports the following basic functions for editing a table:

- Displaying and hiding table columns

  Note: The columns relevant for configuration cannot be hidden.
- Optimizing column width
- Saving current representation
- Displaying the meaning of a column, a row or cell using tooltips.

##### Displaying the diagnostics status of ports and cables in the graphic view

###### Requirements

The graphic view of the topology view is open.

###### Procedure

To determine the diagnostics status of the port, follow these steps:

1. Go online with the required component or components.

###### Result

The following icons are displayed:

- The corresponding diagnostics icon is displayed for each device.
- If there is an error in at least one lower-level component, the diagnostics icon "Error in lower-level component" is also displayed in the left-hand lower corner of the diagnostics icon.
- The corresponding diagnostics icon is displayed for each port.
- Every cable between two ports that are online has the color that matches its diagnostics status.

You will find the possible diagnostics icons for ports and the color coding of Ethernet cables in the description of hardware diagnostics. See: [Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)

##### Showing the diagnostics status of hardware components in the table view

###### Requirement

- The table view of the topology view is open.
- You are in the "Topology overview" tab

###### Procedure

To obtain the diagnostics status of hardware components of the topology overview table, follow these steps:

1. Go online with the required components.

###### Result

The following icons are displayed at the left-hand edge of the topology overview table in each row that belongs to the component involved:

- The diagnostics icon belonging to the hardware component is displayed.
- If the hardware component has lower-level components and if there is an error in at least one of the lower-level components, the diagnostics icon "Error in lower-level component" is also displayed in the left-hand lower corner of the diagnostics icon of the hardware component.

For the possible diagnostics icons for hardware components, refer to the description of hardware diagnostics. See: [Displaying diagnostics status and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)

> **Note**
>
> The display of the diagnostics status of hardware components in the topology overview table and the network overview table is identical.

##### Running an offline/online comparison and displaying the results

###### Requirements

- The table view of the topology view is open.
- You are in the "Topology comparison" tab
- There may be an online connection to one or more devices, but this is not actually necessary.

###### Procedure

To find the differences between the configured and the actual topology, follow these steps:

1. Click the "Compare offline/online" button in the toolbar.

###### Result

The actual topology is identified and compared with the configured topology.

Devices identified online are automatically assigned to configured devices as far as this is possible. See [Automatic assignment of devices by offline/online comparison](#automatic-assignment-of-devices-by-offlineonline-comparison)

The columns on the right-hand side of the table are filled or updated:

- Columns for the result of the offline/online comparison: "Status" and "Action"
- Columns for the topology identified online

> **Note**
>
> **Stopping a running online/offline comparison**
>
> If you click the "Compare offline/online" button while topology discovery is active, the current topology discovery is stopped.

The following buttons are enabled in the toolbar of the table:

| Button | Name | Meaning |
| --- | --- | --- |
| ![Result](images/21293195147_DV_resource.Stream@PNG-de-DE.PNG) | Update | The detection of the existing online topology is started again. |
| ![Result](images/21293202699_DV_resource.Stream@PNG-de-DE.PNG) | Synchronize | - [Adopting the port interconnections identified online in the project](#apply-the-port-interconnections-identified-online-manually-to-the-project) - [Adopt the devices identified online in the project](#include-the-devices-identified-online-manually-in-the-project) |

> **Note**
>
> If you have not configured your own programming device or your own PC offline, the gray filled circle is displayed as a diagnostic symbol.
>
> You can also configure a second and third programming device or a second and third PC offline.

###### Columns for the result of the offline/online comparison

The following columns are displayed:

- "Status"

  The result of the offline/online comparison is shown here in the form of diagnostics icons. The following icons are possible:

| Diagnostics icon | Meaning |
| --- | --- |
| ![Columns for the result of the offline/online comparison](images/21291023499_DV_resource.Stream@PNG-de-DE.png) | Differing topology information in at least one lower-level component |
| ![Columns for the result of the offline/online comparison](images/21293117323_DV_resource.Stream@PNG-de-DE.PNG) | Identical topology information |
| ![Columns for the result of the offline/online comparison](images/21293125131_DV_resource.Stream@PNG-de-DE.png) | Topology information only available offline or device is disabled |
| ![Columns for the result of the offline/online comparison](images/21293170955_DV_resource.Stream@PNG-de-DE.png) | Topology information only exists online |
| ![Columns for the result of the offline/online comparison](images/21293178379_DV_resource.Stream@PNG-de-DE.png) | Differing topology information |
| ![Columns for the result of the offline/online comparison](images/83415165451_DV_resource.Stream@PNG-de-DE.png) | No port interconnection configured, no port interconnection discovered online |
|  | If a device does not support topology functions, the "Status" column remains empty. |

- "Action"

  The possible actions are shown here. The following actions are possible:

  - No action
  - Apply

> **Note**
>
> **Separating columns**
>
> To separate the offline and online columns of the topology comparison table optically, there is a separating column to the left of the "Status" column and to the right of the "Action" column. The separating columns cannot be hidden and their width cannot be changed.

###### Columns for the topology identified online

The following columns are displayed:

- "PROFINET device name"
- "Article no." (by default, this column is not displayed)
- "Device family" (by default, this column is not displayed)
- "IP address" (by default, this column is not displayed)
- "Port"
- "Interconnection"

  - Green line if the port is interconnected
  - Gray line if the port is not interconnected
- "Partner port"
- "Partner IP address"
- "Partner PROFINET device name"
- "Partner article number" (by default, this column is not displayed)
- "Partner device family" (by default, this column is not displayed)

###### Basic functions for tables

The topology comparison table supports the following basic functions for editing a table:

- Displaying and hiding table columns

  Note: The columns relevant for configuration cannot be hidden.
- Optimizing column width
- Saving current representation
- Displaying the meaning of a column, a row or cell using tooltips.

##### Running an advanced offline/online comparison and displaying the results

###### Overview

With the standard offline/online comparison, a search method based on the DCP protocol is used.

With the advanced offline/online comparison, ICMP is also used to be able to detect devices that do not support DCP. These include, for example, PG/PC stations.

###### Requirement

- The table view of the topology view is open.
- You are in the "Topology comparison" tab
- The devices to be detected with ICMP are located in the same subnet as the network adapter of your PG/PC you are currently using.

###### Procedure

Follow these steps:

1. In the toolbar, click on the arrow in the "Advanced comparison" button.
2. With the input boxes "Start address" and "End address", select an IP address range in which accessible Ethernet nodes will be searched for with ICMP. Confirm this, for example by clicking the button with the green check mark.
3. Click on the icon in the left-hand part of the "Advanced comparison" button.

###### Result

The Ethernet nodes detectable with DCP and ICMP are discovered.

The columns on the right-hand side of the table are filled or updated:

#### Configuring topology

This section contains information on the following topics:

- [Interconnecting ports](#interconnecting-ports)
- [Renaming stations, devices, interfaces or ports](#renaming-stations-devices-interfaces-or-ports)
- [Offline/online comparison](#offlineonline-comparison)

##### Interconnecting ports

This section contains information on the following topics:

- [Overview](#overview)
- [Interconnecting ports in the graphic view](#interconnecting-ports-in-the-graphic-view)
- [Interconnecting ports in the table view](#interconnecting-ports-in-the-table-view)
- [Interconnecting a port with more than one partner port in the graphic view](#interconnecting-a-port-with-more-than-one-partner-port-in-the-graphic-view)
- [Interconnecting a port with more than one partner port in the table view](#interconnecting-a-port-with-more-than-one-partner-port-in-the-table-view)

###### Overview

###### Interconnecting ports in the topology view

In the topology view, you have the following options for interconnecting ports:

- in the [graphic view](#interconnecting-ports-in-the-graphic-view)
- in the [graphic view of a tool changer](#interconnecting-a-port-with-more-than-one-partner-port-in-the-graphic-view)
- in the [table view](#interconnecting-ports-in-the-table-view)
- in the [table view of a tool changer](#interconnecting-a-port-with-more-than-one-partner-port-in-the-table-view)
- by [adopting port interconnections identified online](#apply-the-port-interconnections-identified-online-manually-to-the-project)

> **Note**
>
> **Interconnecting an electric with an optical port**
>
> If you want to interconnect an electric and an optical port, you have to decide between RT and IRT communication:
>
> - With RT communication, it is not necessary to configure a media converter.
> - With IRT communication, you have to make the interconnection via a media converter.

###### What effects does the interconnection of ports have on the network view?

> **Note**
>
> In the properties of a subnet in the network view, you can specify that this subnet is used when a port interconnection is created between two devices that are not networked.

When you create an interconnection between two ports, the following effects are possible in the network view:

- If the corresponding interfaces are disconnected: If you have specified a default subnet, this is used. Otherwise a new subnet is created to connect the two interfaces.
- If one (and only one) of the two interfaces involved is networked: The non-networked interface is connected to the same subnet as the already networked interface.
- In all other cases: The corresponding interfaces are not connected to a logical subnet.

---

**See also**

[Interconnecting ports](#interconnecting-ports-1)
  
[Settings for interconnecting Ethernet devices](#settings-for-interconnecting-ethernet-devices)

###### Interconnecting ports in the graphic view

###### Requirement

You are in the graphic view of the topology view.

###### Procedure – Creating a new interconnection between two ports

To interconnect a port of a device with a port of another device, follow these steps:

1. Place the mouse cursor on the port you want to interconnect.
2. Click with the left mouse button and hold it down.
3. Move the mouse pointer.

   The pointer now shows the networking symbol to indicate "Interconnect" mode. At the same time, the mouse pointer shows the lock symbol that will only disappear when the pointer is on a valid target.
4. Now drag the mouse cursor to the target port. You can do this while holding down or after releasing the mouse button.
5. Now release the left mouse button or press it again (depending on your previous action).

Result: A new port interconnection is created.

> **Note**
>
> **Creating a ring for S7-300, S7-400, and S7-1500 CPUs**
>
> If you create a ring using port interconnections for S7-300, S7-400, or S7-1500 CPUs, an MRP domain is created automatically.

###### Procedure – Changing an existing port interconnection without deleting it first

To do this, follow these steps:

1. Place the mouse cursor on the port of an existing interconnection that is to receive a new partner port.
2. Drag the port to the new partner port.

Result: The existing port interconnection is deleted. The new port interconnection is created.

Alternative procedure:

1. Place the mouse cursor on a port without an interconnection that is to be connected with an already interconnected port.
2. Drag the port to the already interconnected port.

Result: The existing port interconnection is deleted. The new port interconnection is created.

###### Procedure – Interconnecting two interconnected ports with each other without first deleting the two existing port interconnections

To do this, follow these steps:

1. Place the mouse cursor on the interconnected port that is to receive a new partner port.
2. Drag the port to the new partner port that has also already been interconnected.

Result: The two existing port interconnections are deleted. The new port interconnection is created.

###### Interconnecting ports in the table view

###### Which actions are possible with port interconnections in the table view?

The following actions are possible with port interconnections in the table view:

- Creating a new port interconnection
- Changing an existing port interconnection
- Deleting an existing port interconnection

###### Requirement

The row with the port whose interconnection you want to create, modify or delete is visible in the "Topology overview" tab.

###### Procedure

To create the interconnection of a port for the first time, to modify it or delete it, follow these steps:

1. Move the mouse pointer to the "Partner port" column in the row of the source port.
2. Click the drop-down list there.
3. Select the required partner port (when creating or changing a port interconnection) or the "Any partner" entry (when deleting a port interconnection).

###### Result

The required action is performed. The new partner port (after creating or modifying a port interconnection) or the "Select port" entry (after deleting a port interconnection) is displayed in the "Partner port" column.

###### Interconnecting a port with more than one partner port in the graphic view

###### Requirement

- You have configured a port of a PROFINET device with the "Alternative partners" property and have specified its possible partner ports.
- The graphic view of the topology view is open.

###### Procedure

1. Interconnect this port (referred to hereafter as source port) with one of the partner ports you have specified (referred to hereafter as target port).
2. Interconnect the source port with an additional target port.

   You can do this in several ways:

   - Drag the mouse pointer from a partner port that is already interconnected to a target port.
   - Drag the mouse pointer from an interconnection that has already been created to a target port.
   - Drag the mouse pointer from a target port to a partner port that is already interconnected.
   - Drag the mouse pointer from a target port to an already created interconnection.
3. If necessary, repeat the step above one or more times.

###### Result

An interconnection is created between the source port and the alternative partner ports. This is indicated by a dashed line.

###### Interconnecting a port with more than one partner port in the table view

###### Which actions are possible with port interconnections to several partner ports in the table view?

When working with a tool changer, the following actions can be performed with port interconnections to multiple partner ports in the table view:

- Creating a new port interconnection
- Changing an existing port interconnection
- Deleting an existing port interconnection

###### Requirement

- You have configured a port of a PROFINET device with the "Alternative partners" property and have specified its possible partner ports.
- The row with the port whose interconnection you want to create, modify or delete is visible in the "Topology overview" tab.

###### Procedure

To create the interconnection of a port to one or more partner ports for the first time, to modify it, or to delete it, follow these steps:

1. Move the mouse pointer to the "Partner port" column in the row of the source port.
2. Click the drop-down list there.
3. Select the required partner port (when creating or changing a port interconnection) or the "Any partner" entry (when deleting a port interconnection).

###### Result

The required action is performed:

- If you are creating an interconnection, a new row is inserted in the topology overview table. The new partner port is displayed there in the "Partner port" column.
- If you change an interconnection, the new partner port is displayed in the "Partner port" column.
- If you delete an interconnection, the row with the previous port interconnection is deleted.

  > **Note**
  >
  > With a tool changer, there are normally several rows for a port with port interconnections to more than one partner port. The last row is always an empty row. The first row can be edited, all other rows are read-only.

##### Renaming stations, devices, interfaces or ports

This section contains information on the following topics:

- [Rename a station, a device, an interface or a port](#rename-a-station-a-device-an-interface-or-a-port)

###### Rename a station, a device, an interface or a port

###### Requirement

- The table view of the topology view is open.
- You are in the "Topology overview" tab

###### Procedure

To rename a station, a device, an interface or a port, proceed as follows:

1. Click twice in the relevant field of the topology overview table (the second click starts the editing mode).
2. Enter the new name and then press the ENTER key (this closes editing mode).

###### Result

The object is renamed.

##### Offline/online comparison

This section contains information on the following topics:

- [Automatic assignment of devices by offline/online comparison](#automatic-assignment-of-devices-by-offlineonline-comparison)
- [Apply the port interconnections identified online manually to the project](#apply-the-port-interconnections-identified-online-manually-to-the-project)
- [Include the devices identified online manually in the project](#include-the-devices-identified-online-manually-in-the-project)
- [Automatic assignment of devices by advanced offline/online comparison](#automatic-assignment-of-devices-by-advanced-offlineonline-comparison)

###### Automatic assignment of devices by offline/online comparison

###### Overview

During the offline/online comparison, the configured topology is compared with the actual existing topology. Devices identified online are automatically assigned to configured devices as far as this is possible.

###### Start of availability detection

You start the availability detection the first time by clicking the "Compare offline/online" button in the toolbar of the "Topology comparison" tab.

You restart availability detection by clicking the "Update" button.

> **Note**
>
> The availability detection can take several seconds. During this time, no user input is possible.

###### Automatic assignment of a PNIO device

A PNIO device identified online is automatically assigned to a configured device if the following properties of the two devices match up:

- Article no.
- Device type or device family
- PROFINET device name

###### No automatic assignment

In the following situations, no automatic assignment is possible:

- No device can be identified online to match a configured device. (This means that the corresponding columns in the "Online topology" area of the topology comparison table are empty.)

  In this case, you should add the already configured device to your system or delete the configured device from the configuration.
- A device identified online can be assigned to a configured device, but there are differences in the port interconnections.

  In this case, you can apply the [port interconnections identified online manually to the project](#apply-the-port-interconnections-identified-online-manually-to-the-project).
- A device identified online cannot be assigned to a configured device. (In this case, the corresponding columns in the "Offline topology" area of the topology comparison table are empty.)

  In this case, you can include the [device identified online manually in the project](#include-the-devices-identified-online-manually-in-the-project).

###### Apply the port interconnections identified online manually to the project

###### Requirement

You have run an offline/online comparison in the topology view. The result of this is that at least one device identified online was automatically assigned to a configured device, but that there are differences relating to the interconnection.

###### Procedure

To adopt one more port interconnections identified online in the project manually, follow these steps:

1. Select the row belonging to the port interconnection.
2. If applicable, select further roles using multi-selection.
3. Select "Apply" &gt; "Use selected" in the shortcut menu.

   The content of the corresponding table cells in the "Action" column changes to "Apply".
4. If you have mistakenly prepared too many port interconnections to be included in the project:

   Select the rows that belong to the port interconnections you have mistakenly prepared for inclusion in the project using multi-selection.

   Select "Reset" &gt; "Reset selected" in the shortcut menu.

   The content of the corresponding table cells in the "Action" column change to "No action".
5. Click the "Synchronize" button.

###### Result

The port interconnections identified online for the corresponding devices are included in the project. Successful adoption is indicated by the diagnostics icon "Identical topology information" for each port.

> **Note**
>
> If other port interconnections are recognized for a device identified online and these differ from those that exist in the project, adopting these in the project means that the port interconnections that were previously in the project are replaced by those identified online. If no port interconnections are detected for a device identified online, adopting in the project means that all the port interconnections of this device are deleted in the project.

###### Include the devices identified online manually in the project

###### Requirements

You have run an offline/online comparison in the topology view. The result of this is that at least one device identified online could not be assigned to any configured device.

###### Procedure

To adopt one more devices identified online in the project manually, follow these steps:

1. For a configured device without an online partner, move the mouse pointer to the "Device/port" column of the online topology.
2. Select the device you want to assign to the configured device from the drop-down list of this box.
3. Repeat the previous steps if necessary for other configured devices without an online partner.

###### Result

The selected device that was identified online is moved up from the end of the table. Following this, it is in the row of the configured device to which you have just assigned it.

###### Automatic assignment of devices by advanced offline/online comparison

###### Overview

With the advanced offline/online comparison, ICMP is also used alongside DCP to be able to detect devices that do not support DCP.

###### Automatic assignment of devices detected by ICMP

With devices detected by ICMP, no type is available.

With passive devices, no article number is available. For this reason, passive devices can only be assigned automatically if you have not assigned an article number in the configured data and the offline and online IP addresses match.

With switches, automatic assignment is possible if the offline and online article number, IP address and PROFINET device name match.

### Secure Communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Basics of Secure Communication (S7-1200, S7-1500, S7-1500T)](#basics-of-secure-communication-s7-1200-s7-1500-s7-1500t)
- [Managing certificates (S7-1200, S7-1500, S7-1500T)](#managing-certificates-s7-1200-s7-1500-s7-1500t)
- [Requirements for secure communication (S7-1200, S7-1500, S7-1500T)](#requirements-for-secure-communication-s7-1200-s7-1500-s7-1500t)
- [Global security settings (S7-1200, S7-1500, S7-1500T)](#global-security-settings-s7-1200-s7-1500-s7-1500t)
- [Secure Open User Communication (S7-1500, S7-1500T)](#secure-open-user-communication-s7-1500-s7-1500t)
- [Secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)](#secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)

#### Basics of Secure Communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Useful information on Secure Communication (S7-1200, S7-1500, S7-1500T)](#useful-information-on-secure-communication-s7-1200-s7-1500-s7-1500t)
- [Device-dependent security features (S7-1200, S7-1500, S7-1500T)](#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)
- [Confidentiality through encryption (S7-1200, S7-1500, S7-1500T)](#confidentiality-through-encryption-s7-1200-s7-1500-s7-1500t)
- [Authenticity and integrity through signatures (S7-1200, S7-1500, S7-1500T)](#authenticity-and-integrity-through-signatures-s7-1200-s7-1500-s7-1500t)

##### Useful information on Secure Communication (S7-1200, S7-1500, S7-1500T)

For STEP 7 (TIA Portal) as of V14 and for S7-1500 CPUs as of firmware V2.0, the options for secure communication have been broadened considerably.

"S7-1500 CPUs" also refers to CPU versions S7-1500F, S7-1500T, S7-1500C as well as S7-1500pro CPUs and ET200SP CPUs.

In subsequent versions, additional components will support Secure Communication (secure OUC), see next section.

As of firmware version V4.4, S7-1200 CPUs also support Secure Communication (Secure OUC).

###### Requirement

- CPUs that support connection description DBs with the structure of the SDT TCON_IP_V4_SEC or SDT TCON_QDN_SEC. These are the following CPUs:

  - S7-1200 as of firmware V4.4
  - S7-1500 as of firmware V2.0
- Also optional via the following CPs:

  - CP 1243-1 as of firmware V3.2
  - CP 1243-8 IRC as of firmware V3.2
  - CP 1543‑1 as of firmware V2.0
  - CP 1545‑1
  - CP 1543SP-1

  Secure Communication via CP 1242-7 GPRS V2 is not possible.

###### Public Key Infrastructure (PKI)

The attribute "secure" is used for the identification of communication mechanisms that are based on a Public Key Infrastructure (PKI) (for example RFC 5280 for Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List Profile). A Public Key Infrastructure (PKI) is a system that can issue, distribute and check digital certificates. The digital certificates issued are used within the PKI to secure computer-based communication. If a PKI uses asymmetric key cryptography, the messages in a network can be digitally signed and encrypted.

Components that you have configured in STEP 7 (TIA Portal) for secure communication use an asymmetric key encryption scheme with a public key (Public Key) and a private key (Private Key). TLS (Transport Layer Security) is used as the encryption protocol. TLS is the successor for the SSL (Secure Sockets Layer) protocol.

###### Objectives of secure communication

Secure communication is used to achieve the following objectives:

- Confidentiality  
  i.e. the data is secret/cannot by read by eavesdroppers.
- Integrity  
  i.e. the message that reaches the recipient is the same message, unchanged, that the sender sent. The message has not been altered on the way.
- End point authentication  
  i.e. the end point communication partner is exactly who it claims to be and the party who is to be reached. The identity of the partner is verified.

In the past, these objectives were primarily relevant to IT and networked computers. Today, industrial machinery and control systems with sensitive data are at equally high risk, as they are also networked, and consequently pose high security requirements for data exchange.

Protection of the automation cell by means of the cell protection concept through firewall, or via connection through VPN, for example with the security module, was common in the past and remains so.

However, it is becoming increasingly necessary to also transfer data to external computers in encrypted form via Intranet or public networks.

###### Common principles of secure communication

Independent of the context, secure communication is based on the Public Key Infrastructure (PKI) concept and contains the following components:

- An asymmetric encryption scheme. This scheme allows the following:

  - Encryption or decryption of the messages using public or private keys.
  - The verification of signatures in messages and certificates.

    The messages / certificates are signed by the sender / certificate owner with their private key. The recipient / verifier checks the signature with the public key of the sender / certificate owner.
- Transport and storage of the public key using X.509 certificates.

  - X.509 certificates are digitally signed data that allow public key authentication in terms of the bound identity.
  - X.509 certificates can also contain information that describes in more detail or restricts use of the public key. For example the effective date of a public key in a certificate and when it expires.
  - X.509 certificates also contain information on the issuer of the certificate in secure form.

The following paragraphs give an overview of these basic concepts which are required for managing certificates in STEP 7 (TIA Portal), for example, and for programming the communication instructions for secure Open User Communication (sOUC).

###### Secure communication in STEP 7

STEP 7 as of V14 provides the required PKI for the configuration and operation of secure communication.

Examples:

- The Hypertext Transfer Protokoll (HTTP) becomes Hypertext Transfer Protokoll Secure (HTTPS) by means of the TLS (Transport Layer Security) protocol. Since HTTPS is a combination of HTTP and TLS, it is called "HTTP over TLS" in the corresponding RFC. You can see in the browser that HTTPS is being used. This is indicated by the URL scheme "https://" instead of "http://" in the address bar of the browser. Most browsers highlight such secure connections.
- Open User Communication becomes secure Open User Communication. The underlying protocol is also TLS.
- E-mail providers also offer access over the "Secure SMTP over TLS" protocol to increase the security of e-mail communication.

The figure below shows the TLS protocol in the context of communication layers.

![Secure communication in STEP 7](images/89530297867_DV_resource.Stream@PNG-en-US.png)

###### Secure communication with OPC UA

An OPC UA server is implemented in S7-1500 CPUs as of firmware V2.0. OPC UA Security also covers authentication, encryption and data integrity with digital X.509 certificates and also uses a Public Key Infrastructure (PKI). Depending on the requirements of the application you can select various security levels for the end point security. The following applies to the OPC UA: the security features are integral components of the specification and of the OPC UA stack and use the encryption algorithms that are used for TLS.

The description of the OPC UA server functionality is covered in a separate section.

###### Secure communication for PG/HMI communication

With the central components of the TIA Portal, STEP 7 and WinCC, an innovative and standardized Secure PG/PC and HMI Communication - PG/HMI communication for short - is implemented starting with version V17 together with the latest controllers and latest HMI devices. The underlying protocol is also TLS.

---

**See also**

[What you should know about the certificate manager (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#what-you-should-know-about-the-certificate-manager-s7-1500)
  
[Secure OUC via CP interface (S7-1500, S7-1500T)](#secure-ouc-via-cp-interface-s7-1500-s7-1500t)
  
[Secure OUC via e-mail (S7-1500, S7-1500T)](#secure-ouc-via-e-mail-s7-1500-s7-1500t)
  
[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)
  
[Secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)](#secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)

##### Device-dependent security features (S7-1200, S7-1500, S7-1500T)

Transport Layer Security (TLS) is a widespread security protocol that improves the data security for communications. For the automation systems S7-1200 and S7-1500, TLS is also used for secure communication for the following certificate-based applications:

- Web server (HTTPS protocol variant)
- Secure Open User Communication (OUC) including secure email (TMAIL application)
- Secure PG/HMI communication

Among other things, TLS takes care of the authentication and encryption of the communication between client and server for the listed applications, for example, between the web server of CPU and web browsers, which, for example, have to display a diagnostics web page of the CPU.

The OPC UA server and OPC UA client (S7-1500 only) applications do not actually directly use TLS, but the cryptographical processes used are comparable.

TLS is continuously being further developed, resulting in various TLS versions, which are distinct with regard to the cipher suites (standardized collection of cryptographic methods) supported and the performance.

The Internet Engineering Task Force (IETF) is responsible for the description of the TLS protocol. The following correlation applies:

- TLS 1.3 corresponds to RFC 8446
- TLS 1.2 corresponds to RFC 5246

In addition, not every device supports all the cryptographic methods defined in the RFCs. Therefore, after establishing the connection, the client and server negotiate a method that both support (Handshake) as well as the parameters to be used.

###### Supported TLS versions S7-1200

The following table shows the TLS versions that are basically supported in a given CPU firmware version.

| CPU firmware version | Supported TLS version |
| --- | --- |
| V4.6 | TLS 1.2, TLS 1.3 |
| V4.5 | TLS 1.2, TLS 1.3 |
| V4.4 | TLS 1.2 |

###### Supported TLS versions S7-1500

The following table shows the TLS versions that are basically supported in a given CPU firmware version.

| CPU firmware version | Supported TLS version |
| --- | --- |
| V3.0 | TLS 1.2, TLS 1.3 |
| V2.9 | TLS 1.2, TLS 1.3 |
| V2.8 ... V2.0 | TLS 1.2 |

###### Supported encryption methods and parameters for creating certificates

To generate the public key for a new certificate, in the TIA Portal, set the encryption method and encryption parameters. These certificate parameters are device-dependent and dependent on the application used

One possibility: In the CPU properties, go to "Protection &amp; Security &gt; Certificate manager" and generate a new device certificate. You can find settings for the encryption method and the encryption parameters under "Certificate Parameters" in the "Generate Certificates" dialog.

Example: RSA 2048 stands for asymmetric RSA encryption method with cryptographic key length 2048 bits.

The following table shows the supported encryption methods and encryption parameters depending on the CPU application.

| Encryption method/parameters   S7-1200 (firmware V4.6) | Web server (HTTPS)  Secure PG/HMI communication  Secure OUC | OPC UA |
| --- | --- | --- |
| EC prime256v1 | yes | no |
| EC secp384r1 | yes | no |
| EC secp256k1 | no | no |
| RSA 1024 | yes | yes |
| RSA 2048 | yes | yes |
| RSA 4096 | no | no |
| RSA 8192 | no | no |

| Encryption method/parameters   S7-1500 (firmware V3.0) | Web server (HTTPS)  Secure PG/HMI communication  Secure OUC | OPC UA |
| --- | --- | --- |
| EC prime256v1 | yes | no |
| EC secp384r1 | yes | no |
| EC secp256k1 | no | no |
| RSA 1024 | yes | yes |
| RSA 2048 | yes | yes |
| RSA 4096 | yes | yes |
| RSA 8192 | no | no |

---

**See also**

[Web server security (S7-1200)](Configuring%20automation%20systems.md#web-server-security-s7-1200)
  
[Useful information on Secure Communication (S7-1200, S7-1500, S7-1500T)](#useful-information-on-secure-communication-s7-1200-s7-1500-s7-1500t)

##### Confidentiality through encryption (S7-1200, S7-1500, S7-1500T)

Message encryption is an important element of data security. When encrypted messages are intercepted by third parties during communication, these potential eavesdroppers cannot access the information they contain.

There is a wide range of mathematical processes (algorithms) for encrypting messages.

All algorithms process a "key" parameter to encrypt and decrypt messages.

- Algorithm + key + message =&gt; encrypted message
- Encrypted message + key + algorithm =&gt; (decrypted) message

###### Symmetric encryption

The central aspect of symmetric encryption is that both communication partners use the same key for message encryption and decryption, as shown in the figure below. Bob uses the same key for encryption as Alice uses for decryption. In general, we also say that the two sides share a secret, the secret key, with which they encrypt or decrypt a message.

![Symmetric encryption](images/85933438347_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Bob encrypts his message with the symmetric key |
| ② | Alice decrypts the encrypted message with the symmetric key |

The process can be compared to a briefcase to which the sender and recipient have the same key, which both locks and opens the case.

- Advantage: Symmetric encryption algorithms (for example AES, Advanced Encryption Algorithm) are fast.
- Disadvantages: How can the key be sent to a recipient without getting into the wrong hands? This is a key distribution problem. If enough messages are received, the key can also be worked out and must therefore be changed regularly.

If there is a large number of communication partners, there is also a large number of keys to distribute.

###### Asymmetric encryption

Asymmetric encryption works with a pair of keys consisting of one public key and one private key. In connection with a PKI it is also called a Public Key process or only PKI process: A communication partner, Alice in the figure below, has a private key and a public key. The public key is provided to the public, in other words any potential communication partner. Anyone with the public key can encrypt messages for Alice. In the figure below, this is Bob.

Alice's private key, which she must not disclose, is used by Alice to decrypt an encrypted message addressed to her.

![Asymmetric encryption](images/85991394699_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Alice provides Bob with her public key. No precautionary measures are required to this purpose: Anyone can use the public key for messages to Alice if they are sure that it is actually Alice's public key. |
| ② | Bob encrypts his message with Alice's public key. |
| ③ | Alice decrypts the encrypted message from Bob with her private key. As only Alice has the private key and never discloses it, only she can decrypt the message. With her private key, she can decrypt any message encrypted with her public key - not only messages from Bob. |

The system can be compared to a mailbox into which anyone can put a message, but from which only the person with the key can remove messages.

- Advantages: A message encrypted with a public key can only be decrypted by the owner of the private key. As another (private) key is required for decryption, it is also much harder to work out the decryption key on the basis of large numbers of encrypted messages. This means that the public key does not have to be kept strictly confidential, unlike with symmetric keys.

  Another advantage is easier distribution of public keys. No specially secured channel is required in asymmetric cryptography to transfer the public key from the recipient to the sender encrypting the messages. Less effort is thus required in the management of the keys than with the symmetric encryption process.
- Disadvantages: Complex algorithm (e.g. RSA, named after the three mathematicians Rivest, Shamir and Adleman), and therefore poorer performance than with symmetric encryption.

###### Encryption processes in practice

In practice, for example with a CPU Web server and Secure Open User Communication, the TLS protocol is used below the relevant application layer. Application layers are HTTP or SMTP, for example, as detailed above.

TLS (Transport Layer Security) uses a combination of asymmetric encryption and symmetric encryption (hybrid encryption) for secure data transfer, for example, over the Internet, and uses the following subprotocols:

- TLS Handshake Protocol, responsible for authentication of communication partners and negotiation of the algorithms and keys to be used for subsequent data transfer on the basis of asymmetric encryption
- TLS Record Protocol, responsible for encryption of user data with symmetric encryption and data exchange.

Both asymmetric and symmetric encryption are considered secure encryption schemes - there is basically no difference in security between the two procedures. The degree of security depends on parameters such as the selected key length.

###### Improper use of encryption

You cannot tell what identity is assigned to a public key from the bit string. A fraud could provide their public key and claim to be someone else. If a third party then uses this key thinking that they are addressing their required communication partner, confidential information could end up with the fraud. The fraud then uses their private key to decrypt the message that was not intended for them, and sensitive information falls into the wrong hands.

To prevent this type of abuse, the communication partners must be confident that they are dealing with the right communication partner. This trust is established by using digital certificates in a PKI.

##### Authenticity and integrity through signatures (S7-1200, S7-1500, S7-1500T)

Attacks from programs that intercept communication between the server and client and act as if they themselves were client or server, are called man-in-the-middle attacks. If the false identity of these programs is not detected, they can, for example, obtain important information via the S7 program or set values in the CPU and attack a machine or plants. Digital certificates are used to avoid such attacks.

Secure communication uses digital certificates that meet the standard X.509 of the International Telecommunication Union (ITU). This allows the identity of a program, a computer or an organization to be checked (authenticated).

###### How certificates establish trust

The main role of X.509 certificates is to bind an identity with the data of a certificate subject (for example e-mail address or computer name) to the public key of the identity. Identities can be people, computers or machines.

Certificates are issued by certificate authorities (Certificate Authority, CA) or by the owner of a certificate itself. PKI systems specify how users can trust the certificate authorities and the certificates that they issue.

The certificate process:

1. Anyone wishing to own a certificate submits a certificate application to a registration authority linked to the certificate authority.
2. The certificate authority assesses the application and applicant on the basis of set criteria.
3. If the identity of the applicant can be clearly established, the certificate authority confirms that identity by issuing a signed certificate. The applicant has now become the certificate holder.

The figure below is a simplified overview of the process. It does not show how Alice can check the digital signature.

![How certificates establish trust](images/86064030731_DV_resource.Stream@PNG-en-US.png)

###### Self-signed certificates

Self-signed certificates are certificates whose signature comes from the certificate owner and not from an independent certificate authority.

Examples:

- You can create and sign a certificate yourself, for example, to encrypt messages to a communication partner. In the example above, Bob (instead of Twent) could himself sign his certificate with his private key. Alice can use Bob's public key to check that the signature and public key from Bob match. This procedure is sufficient for simple internal plant communication that is to be encrypted.
- A root certificate is, for example, a self-signed certificate, signed by the certificate authority (CA), that contains the public key of the issuer.

###### Features of self-signed certificates

The attributes "CN" (Common Name of Subject) for the certificate holder and "Issuer" (issuer) of the self-signed certificates are identical: You have signed your certificate yourself. The field "CA" (Certificate Autority) for the certificate authority must be set to "False"; the self-signed certificate should, after all, not be used to sign other certificates.

Self-signed certificates are not embedded in a PKI hierarchy.

###### Certificate content

A certificate to the X.509 V3 standard, the same standard that is used by STEP 7 and the S7-1500 CPUs, consists primarily of the following elements:

- Public key
- Details of the certificate holder (meaning the holder of the key). This is, for example, the Common Name (CN) of Subject
- Attributes such as serial number and validity period
- Digital signature from the certificate authority (CA) confirming that the information is correct.

There are also extensions, for example:

- Specification of what the public key may be used for (Key Usage), for example, signing or key encryption.   
  When you create a new certificate with STEP 7, for example in the context of Secure Open User Communication, select the correct entry from the list of possible usages, e.g. "TLS".
- Specification of a "Subject Alternative Name" ("SAN"), which is used in secure communication with Web servers (HTTP over TLS), for example, to ensure that the certificate in the address bar of the Web browser also belongs to the Web server specified in the URL.

###### How signatures are generated and verified

Asymmetric key usage ensures that certificates can be verified: The example of the certificate "MyCert" illustrates the "Sign" and "Verify signature" processes.

Generating a signature:

1. The issuer of the "MyCert" certificate generates a hash value from the certificate data using a specific hash function (for example SHA-1, Secure Hash Algorithm).

   The hash value is a bit string of a constant length. The advantage of the constant length of the hash value is that it always takes the same amount of time to sign.
2. Using the hash value generated in this way and the private key, the issuer of the certificate then generates a digital signature. The RSA signature scheme is often used.
3. The digital signature is saved in the certificate. The certificate is now signed.

Verifying a signature:

1. The authenticator of the "MyCert" certificate obtains the certificate of the certificate issuer and thus also the public key.
2. A new hash value is formed from the certificate data with the same hash algorithm that was used for signing (for example SHA-1).
3. This hash value is then compared with the hash value that was determined by means of the public key of the certificate issuer and the signature algorithm to verify the signature on the certificate.
4. If the signature verification supplies a positive result, both the identity of the certificate holder as well as the integrity, meaning the authenticity and genuineness of the certificate contents, is proven. Anyone who has the public key, meaning the certificate from the certificate authority, can check the signature and thus prove that the certificate was actually signed by the certificate authority.

The figure below shows how Alice uses the public key in the certificate from Twent (who represents the certificate authority, CA) to verify the signature on Bob's public key. All that is required for verification is therefore the availability of the certificate from the certificate authority at the time of verification. The validation itself is executed automatically in the TLS session.

![How signatures are generated and verified](images/86064261515_DV_resource.Stream@PNG-en-US.png)

###### Signing messages

The method described above for signing and verifying also uses the TLS session for signing and verifying messages:

If a hash value is generated by a message and this hash value is signed with the private key of the sender and attached to the original message, the recipient of the message is able to check the integrity of the message. The recipient decrypts the hash value with the public key of the sender, puts together the hash value from the message received and compares the two values. If the values are not the same, the message has been tampered with on the way.

###### Chain of certificates to root certificate

The certificates of a PKI are often organized hierarchically: The top of the hierarchy is formed by root certificates. These are certificates that are not signed by a higher-level certificate authority. The certificate holder and certificate issuer of root certificates are identical. Root certificates enjoy absolute trust. They are the "anchor" of the trust and must therefore be known at the receiver as absolute certificates. They are stored in an area provided for trusted certificates.

The function of root certificates is to sign certificates from lower-level certificate authorities, so-called intermediate certificates. This transfers the trust from the root certificate to the intermediate certificate. An intermediate certificate can sign a certificate just like a root certificate; both are therefore referred to as "CA certificates".

This hierarchy can be continued over multiple intermediate certificates until the end-entity certificate. The end-entity certificate is the certificate of the user who is to be identified.

The validation process runs through the hierarchy in the opposite direction: As described above, the certificate issuer is established and the signature checked with the issuer's public key, then the certificate of the higher-level certificate issuer is established along the entire chain of trust to the root certificate.

Conclusion: The chain of intermediate certificates to the root certificate, the certificate path, must be available in every device that is to validate an end-entity certificate of the communication partner, irrespective of the type of secure communication that you configure.

#### Managing certificates (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [What you should know about the certificate management (S7-1200, S7-1500, S7-1500T)](#what-you-should-know-about-the-certificate-management-s7-1200-s7-1500-s7-1500t)
- [Certificate management with TIA Portal (S7-1200, S7-1500, S7-1500T)](#certificate-management-with-tia-portal-s7-1200-s7-1500-s7-1500t)
- [Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)
- [How communication with certificates works: HTTP over TLS (S7-1200, S7-1500, S7-1500T)](#how-communication-with-certificates-works-http-over-tls-s7-1200-s7-1500-s7-1500t)

##### What you should know about the certificate management (S7-1200, S7-1500, S7-1500T)

This section shows the available certificate management options of an S7-1500 CPU depending on the service (CPU application) used and on the versions of the TIA Portal / the CPU firmware.

###### Overview of certificate management options

Since TIA Portal version V14 and CPU firmware version V2.0, it has been possible to manage certificates for secure communications for different services of S7-1500 CPU in the TIA Portal and load them in the CPU.

TIA Portal as of version V17, along with the S7-1500 CPUs as of version V2.9 support another option of certificate management: With GDS push methods, you can transfer or renew certificates in the CPU at runtime without having to reload the CPU.

Using the same route, as of TIA Portal version V18, you can also transfer web server certificates for a S7-1500 CPU (as of firmware V3.0).

The following table provides an overview of the certificate management options depending on the service used and the TIA Portal firmware version or CPU firmware version.

Click here for a description of the certificate management with GDS-push methods: [Automated certificate management with GDS](Configuring%20automation%20systems.md#automated-certificate-management-with-gds-s7-1500-s7-1500t)

| Service | Certificate management with TIA Portal   (TIA Portal version / S7-1500 CPU-FW version) | Certificate management with OPC UA GDS push methods  (TIA Portal version / S7-1500 CPU-FW version) |
| --- | --- | --- |
| Web server | as of V14 / as of V2.0 | as of V18 / as of V3.0 |
| Secure OUC communication | as of V14 / as of V2.0 | - |
| OPC UA server | as of V14 / as of V2.0 | as of V17 / as of V2.9 |
| OPC UA client | as of V15.1 / as of V2.6 | - |
| Secure PG/HMI Communication | as of V17 / as of V2.9 | - |

---

**See also**

[Certificate management with TIA Portal (S7-1200, S7-1500, S7-1500T)](#certificate-management-with-tia-portal-s7-1200-s7-1500-s7-1500t)

##### Certificate management with TIA Portal (S7-1200, S7-1500, S7-1500T)

The TIA Portal (STEP 7) from version V14 together with the S7-1500-CPUs from firmware version 2.0 support the Internet PKI (RFC 5280) in so far as an S7-1500-CPU is able to communicate with devices that also support the Internet PKI.

The use of X.509 certificates, for example to verify certificates as described in the preceding sections, is a result of this.

STEP 7 as of V14 uses a PKI similar to the Internet PKI. Certificate Revocation Lists (CRLs), for example, are not supported.

###### Creating or assigning certificates in the TIA Portal

For devices with security properties, such as an S7-1500 CPU as of firmware V2.0, you create certificates in STEP 7 for various applications.

The following areas in the Inspector window of the CPU allow the creation of new certificates or the selection of existing ones:

- "Web server &gt; Security" - for the generation and assignment of Web server certificates.
- "Protection &amp; Security &gt; Connection mechanisms" - for the generation or assignment of PLC communication certificates (Secure PG/HMI communication, as of TIA Portal V17).
- "Protection &amp; Security &gt; Certificate manager" - for the generation or assignment of all types of certificates. The default setting for the creation of certificates is TLS certificates for Secure Open User Communication.
- "OPC UA &gt; Server &gt; Security" - for the generation or assignment of OPC UA server certificates.

![Creating or assigning certificates in the TIA Portal](images/142880184971_DV_resource.Stream@PNG-en-US.png)

###### Special feature of the area "Protection &amp; security &gt; Certificate manager"

Only in this area of the Inspector window do you switch between the global, meaning the project-wide, certificate manager and the local, meaning the device-specific, certificate manager (option "Use global security settings for certificate manager"). The option decides whether you have access to all the certificates in the project or not.

- If you do **not** use the certificate manager in the global security settings, you only have access to the local certificate memory of the CPU. You do not have any access, for example, to imported certificates or root certificates. Without these certificates only limited functionality is available. You can, for example, only create self-signed certificates.
- If you use the certificate manager in the global security settings and you are logged on as an administrator, you have access to the global, project-wide certificate memory. You can, for example, assign imported certificates to the CPU or create certificates that are issued and signed by the project CA (certification authority of the project).

The figure below shows how the "Global security settings" are displayed in the project tree after activation of the option "Use global security settings for certificate manager" in the Inspector window of the CPU.

![Special feature of the area "Protection & security > Certificate manager"](images/113745265931_DV_resource.Stream@PNG-en-US.png)

When you double-click "User login" in the project tree below the global security settings and log in, a line "Certificate manager" is displayed there among other things.

With a double-click on the "Certificate manager" line you receive access to all the certificates in the project, divided into the tabs "CA" (certificate authorities), "Device certificates" and "Trusted certificates and root certification authorities".

![Special feature of the area "Protection & security > Certificate manager"](images/88061933195_DV_resource.Stream@PNG-en-US.png)

###### Private keys

The TIA Portal (STEP 7) generates private keys while generating device certificates or server certificates (end-entity certificates). It depends on the use of the global security settings for the certificate manager where the private key is stored encrypted:

- If you use global security settings, the private key is stored encrypted in the global (project-wide) certificate memory.
- If you do not use global security settings, the private key is stored encrypted in the local (CPU-specific) certificate memory.

The existence of the private key that is required, for example, to decrypt data, is displayed in the "Private key" column in the "Device certificates" tab of the certificate manager in the global security settings.

When the hardware configuration is downloaded, the device certificate, the public key as well as the private key are downloaded to the CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Enabling the "Use global security settings for the certificate manager" option - Consequences**  The option "Use global security settings for certificate manager" influences the previously used private keys: If you have already created certificates without using the certificate manager in the global security settings and then change the option to the use of the certificate manager, the private keys are lost and the certificate ID can change. A warning draws your attention to this fact. Therefore specify at the beginning of the configuration which option is required for the certificate management. |  |

##### Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)

As explained in the preceding sections, certificates are required for every type of secure communication. The following section shows as an example how you handle the certificates with STEP 7 so that the requirements for Secure Open User Communication are met.

In the following section a distinction is made as to which devices the participating communication partners are. The respective steps for supplying the communication participants with the required certificates are described for each. An S7-1500 CPU or an S7-1500 software controller as of firmware version 2.0 is required.

The following generally applies:

During the establishment of a secure connection ("handshake") the communication partners as a rule only transfer their end-entity certificates (device certificates).

Therefore the CA certificates required to verify the transferred device certificate must be located in the certificate memory of the respective communication partner.

> **Note**
>
> The current date/time must be set in the CPU.
>
> When using secure communication (for example, HTTPS, secure OUC, OPC UA), make sure that the corresponding modules have the current time of day and the current date. Otherwise, the modules evaluate the used certificates as invalid and the secure communication does not work.

###### Secure Open User Communication between two S7-1500 CPUs

Two S7-1500 CPUs PLC_1 and PLC_2 should interchange data over Secure Open User Communication.

You generate the required device certificates with STEP 7 and assign them to the CPUs as described below.

STEP 7 project certification authorities (CA of the project) are used to sign the device certificates.

The certificates are to be referenced by their certificate ID in the user program (TCON communication instruction in combination with the associated system data type, for example TCON_IPV4_SEC). STEP 7 assigns the certificate ID automatically when generating or creating certificates.

![Secure Open User Communication between two S7-1500 CPUs](images/88027114507_DV_resource.Stream@PNG-de-DE.png)

###### Procedure

STEP 7 automatically downloads the required CA certificates together with the hardware configuration to the participating CPUs so that the requirements for certificate verification exist for both CPUs. You therefore only have to generate the device certificates for the respective CPU - everything else is done by STEP 7 for you.

1. Select PLC_1 and activate the "Use global security settings for certificate manager" option in the "Protection &amp; Security" area.
2. Log in as a user in the project tree in the "Global security settings" area. The "Administrator" role is the default for the first login to a new project.
3. Return to the PLC 1 in the "Protection &amp; Security" section. Click in an empty line in the "Certificate holder" column in the "Device certificates" table to add a new certificate.
4. Click the "Add" button in the drop-down list to select a certificate.

   The "Generate new certificate" dialog opens.
5. Leave the default settings in this dialog. They are tailored to the usage of Secure Open User Communication (usage: TLS).

   Tip: Extend the preset name of the certificate holder - in this case the CPU name. In order to differentiate better, leave the default CPU name in case you have to manage a large number of device certificates.

   Example: PLC_1/TLS becomes PLC_1-SecOUC-Chassis17FactoryState.
6. Compile the configuration.

   The device certificate and the CA certificate are part of the configuration.
7. Repeat the steps described for PLC_2.

In the next step you have to create the user programs for the data exchange and download the configurations together with the program.

###### Use self-signed certificates instead of CA certificates

When creating device certificates you can select the "Self-signed" option. You can create self-signed certificates without having to be logged in for the global security settings. This procedure is not recommended because the certificates created by this method do not exist in the global certificate memory and can therefore not be assigned directly to a partner CPU.

As described above you should select the name of the certificate holder with care so that the right certificate can be assigned to a device without any doubt.

A verification with the CA certificates of the STEP 7 project is not possible with self-signed certificates. To ensure that self-signed certificates can be verified, you have to include the self-signed certificate of the communication partner in the list of trusted partner devices for each CPU. To do so, you must have activated the option "Use global security settings for certificate manager" and be logged in as a user in the global security settings.

Proceed as follows to add the self-signed certificate of the communication partner of the CPU:

1. Select PLC_1 and navigate to the table "Certificates of partner devices" in the "Protection &amp; Security" area.
2. Click in an empty line of the "Certificate holder" column to open the drop-down list for adding or selecting certificates.
3. From the drop-down list select the self-signed certificate of the communication partner and confirm the selection.

In the next step you have to create the user programs for the data exchange and download the configurations together with the program.

###### Secure Open User Communication between an S7-1500 CPU as a TLS client and an external device as a TLS server

Two devices are to interchange data via a TLS connection or TLS session, for example to exchange recipes, production data or quality data:

- An S7-1500 CPU (PLC_1) as the TLS client; the CPU uses Secure Open User Communication
- An external device (such as a Manufacturing Execution System (MES)) as the TLS server

As the TLS client the S7-1500 CPU establishes the TLS connection / session to the MES system.

![Secure Open User Communication between an S7-1500 CPU as a TLS client and an external device as a TLS server](images/90751714059_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | TLS client |
| ② | TLS server |

In order to authenticate the TLS server, the S7-1500 CPU requires the CA certificates of the MES system: The root certificate and if appropriate the intermediate certificates for verifying the certificate path.

You have to import these certificates into the global certificate memory of the S7-1500 CPU.

Proceed as follows to import certificates of the communication partner:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (trusted certificates of root certification authorities) for the certificate to be imported.
3. Right-click in the table to open the shortcut menu. Click "Import" and import the required certificate or the required CA certificates.

   Through the import the certificate receives a certificate ID and can be assigned to a module in the next step.
4. Select PLC_1 and navigate to the table "Certificates of partner devices" in the "Protection &amp; Security" area.
5. Click in an empty line of the "Certificate holder" column to add the imported certificates.
6. From the drop-down list select the required CA certificates of the communication partner and confirm the selection.

Optionally the MES system can also request a device certificate of the CPU to authenticate the CPU (meaning the TLS client). In this case the CA certificates of the CPU must be available to the MES system. Prerequisite for importing the certificates into the MES system is a preceding export of the CA certificates from the STEP 7 project of the CPU. Proceed as follows:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates) for the certificate to be exported.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Export".
5. Select the export format of the certificate.

In the next step you have to create the user programs for the data exchange and download the configurations together with the program.

###### Secure Open User Communication between an S7-1500 CPU as TLS server and an external device as TLS client

If the S7-1500 CPU acts as a TLS server and the external device, for example an ERP system (Enterprise Resource Planning System), establishes the TLS connection / session, you require the following certificates:

- For the S7-1500 CPU you generate a device certificate (server certificate) with a private key and download it with the hardware configuration. When generating the server certificate you use the option "Signed by certificate authority".

  The private key is required for the key exchange as explained in the figure for the example "HTTP over TLS".
- For the ERP system you have to export the CA certificate of the STEP 7 project and import / download it to the ERP system. With the CA certificate, the ERP system checks the server certificate of the S7-1500 that was transmitted from the CPU to the ERP system during the establishment of the TLS connection/session.

![Secure Open User Communication between an S7-1500 CPU as TLS server and an external device as TLS client](images/90751717899_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | TLS server |
| ② | TLS client |

The description of the required actions is provided in the preceding sections.

###### Secure Open User Communication via S7-1543-1 CP as an e-mail client (SMTP over TLS)

An S7-1500 CPU can establish a secure connection to an e-mail server via the CP 1543-1 with the communication instruction TMAIL-C.

The system data types TMail_V4_SEC, TMail_V6_SEC and TMail_QDN_SEC allow you to specify the partner port of the e-mail server and thus to reach the e-mail server via "SMTP over TLS".

![Secure Open User Communication via S7-1543-1 CP as an e-mail client (SMTP over TLS)](images/88192104203_DV_resource.Stream@PNG-de-DE.png)

Prerequisite for a secure e-mail connection is an import of the root certificate and of the intermediate certificates from the e-mail server (provider) into the global certificate memory of the STEP 7 project. When these certificates have been assigned to the CP, the CP can check the server certificate of the e-mail server that is sent by the e-mail server during the establishment of the TLS connection / session by means of this certificate.

Follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (trusted certificates of root certification authorities) for the certificate to be imported.
3. Right-click in the table to open the shortcut menu. Click "Import" and import the required certificate or the required CA certificates.

   Through the import the certificate receives a certificate ID and can be assigned to the CP in the next step.
4. Select the CP 1543-1 and navigate to the table "Certificates of partner devices" in the "Security" section.
5. Click in an empty line of the "Certificate holder" column to add the imported certificates.
6. From the drop-down list select the required CA certificates of the e-mail server and confirm the selection.

In the next step you have to create the user programs for the e-mail client function of the CPU and download the configurations together with the program.

---

**See also**

[Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)](#secure-ouc-between-two-s7-1500-cpus-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as a TLS client to an external PLC (TLS server) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-a-tls-client-to-an-external-plc-tls-server-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as TLS server to an external PLC (TLS client) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-tls-server-to-an-external-plc-tls-client-s7-1500-s7-1500t)
  
[Secure OUC via e-mail (S7-1500, S7-1500T)](#secure-ouc-via-e-mail-s7-1500-s7-1500t)
  
[Secure OUC via CP interface (S7-1500, S7-1500T)](#secure-ouc-via-cp-interface-s7-1500-s7-1500t)

##### How communication with certificates works: HTTP over TLS (S7-1200, S7-1500, S7-1500T)

The following paragraphs show examples of how the mechanisms described are used to create secure communication between a Web browser and the web server of an S7-1500 CPU.

First the changes for the option "Permit access only through HTTPS" in STEP 7 are described. As of STEP 7 V14 you have the option of influencing the server certificate of the Web server of an S7-1500 CPU as of firmware V2.0: The server certificate is generated with STEP 7 as of this version.

In addition the processes that are implemented when a website of the Web server of the CPU is called up with a Web browser of a PC via an encrypted HTTPS connection are displayed.

###### Using Web server certificates for S7-1500 CPUs as of FW V2.0

For S7-1500 CPUs with a firmware version before V2.0, you were able to set "Permit access only with HTTPS" when setting the Web server properties, without specific requirements applying.

You did not have anything to do with the handling of certificates for these CPUs; the CPU automatically generates the certificates required for the Web server.

For S7-1500 CPUs as of firmware V2.0, STEP 7 generates the server certificate (end-entity certificate) for the CPU. You assign a server certificate to the Web server in the properties of the CPU (Web server &gt; Server security).

Since a server certificate name is always preset, nothing changes in the simple configuration of the Web server: You activate the Web server and activate the option "Permit access only with HTTPS" - STEP 7 generates a server certificate with the preset name during compiling.

Irrespective of whether you use the certificate manager in the global security settings or not: STEP 7 has all the information needed to generate the server certificate.

In addition you have the option of determining the properties of the server certificate, for example, the name or the duration of validity.

> **Note**
>
> The current date/time must be set in the CPU.
>
> When using secure communication (for example, HTTPS, secure OUC, OPC UA), make sure that the corresponding modules have the current time of day and the current date. Otherwise, the modules evaluate the used certificates as invalid and the secure communication does not work.

###### Downloading the Web server certificate

The server certificate generated by the TIA Portal (STEP 7) is then automatically also loaded to the CPU when the hardware configuration is loaded.

- If you use the certificate manager in the global security settings, the certificate authority of the project (CA certificate) signs the server certificate of the Web server. When downloading the CA certificate of the project is automatically loaded as well.
- If you do not use the certificate manager in the global security settings, STEP 7 generates the server certificate as a self-signed certificate.

When you address the Web server of the CPU via the IP address of the CPU, a new server certificate (end-entity certificate) must be generated and loaded with each change of the IP address of an Ethernet interface of the CPU. This is necessary because the identity of the CPU changes with the IP address – and the identity requires a signature in accordance with the PKI rules.

You can avoid this problem by addressing the CPU with a domain name instead of its IP address, e.g. "myconveyer-cpu.room13.myfactory.com". To do so, you need to manage the domain names of your CPUs over a DNS server.

****Supplying a Web browser with a CA certificate of the Web server****

In the Web browser, the user who accesses the websites of the CPU through HTTPS should install the CA certificate of the CPU. If no certificate is installed, a warning is output recommending that you do not use the page. To view this page, you must explicitly "Add an exception".

The user receives the valid root certificate (Certification Authority) for download from the "Intro" web page of the CPU Web server under "Download certificate".

STEP 7 offers a different possibility: Export the CA certificate of the project with the certificate manager into the global security settings in STEP 7. Subsequently import the CA certificate into the browser.

###### Course of Secure Communication

The figure below shows, in simplified terms, how communication is established ("handshake"), focusing on the negotiation of keys used for data exchange (here via HTTP over TLS).

However, the course can theoretically be applied to all communication options that are based on the use of TLS, i.e. also for Secure Open User Communication (see Basics of secure communication).

![Course of Secure Communication](images/86063595147_DV_resource.Stream@PNG-en-US.png)

The figure does not show the measures taken at Alice's end (browser) to verify the certificate sent by the Web server. Whether Alice can trust the transferred Web server certificate and thus the identity of the Web server and allow the data exchange depends on a positive outcome of the verification.

The steps for verifying the authenticity of the Web server are:

1. Alice must know the public keys of all relevant certificate authorities, i.e. she requires the complete certificate chain to be able to verify the Web server certificate (i.e. the end-entity certificate of the Web server).

   Alice will generally have the required root certificate in her certificate memory. When a Web browser is installed, a whole range of trusted root certificates is also installed. If she does not have the root certificate, she has to download it from the certificate authority and install it in the certificate memory of the browser. The certificate authority can also be the device on which the Web server is located.

   You have the following options for obtaining the intermediate certificates:

   - The server itself sends the required intermediate certificates along with its end-entity certificate to Alice – in the form of a signed message so that Alice can check the integrity of the certificate chain.
   - The certificates often contain the URLs of the certificate issuer. Alice can load the required intermediate certificates from these URLs.

   When you handle certificates in STEP 7, it is always assumed that you have imported the required intermediate certificates and the root certificate into the project and have assigned them to the module.
2. Alice validates the signatures in the certificate chain with the public keys of the certificates.
3. The symmetric key has to have been generated and transferred to the Web server.
4. If the Web server is addressed by its domain name, Alice verifies the identity of the Web server in accordance with the PKI rules defined in RFC 2818. She is able to do this because the URL, in this case the "Fully Qualified Domain Name (FQDN) of the Web server, is saved in the end-entity certificate of the Web server. If the certificate entry in the "Subject Alternative Name" field corresponds to the entry in the address bar of the browser, everything is fine.

The process continues with the exchange of data with the symmetric key, as shown in the figure above.

---

**See also**

[Certificates for the Web server (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#certificates-for-the-web-server-s7-1500)
  
[Information about the web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#information-about-the-web-server-s7-300-s7-400-s7-1500)

#### Requirements for secure communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)](#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)
- [Useful information for the protection of confidential PLC configuration data (S7-1200, S7-1500, S7-1500T)](#useful-information-for-the-protection-of-confidential-plc-configuration-data-s7-1200-s7-1500-s7-1500t)
- [Changing your password (S7-1200, S7-1500, S7-1500T)](#changing-your-password-s7-1200-s7-1500-s7-1500t)
- [Resetting the password (S7-1200, S7-1500, S7-1500T)](#resetting-the-password-s7-1200-s7-1500-s7-1500t)
- [Assign password via SIMATIC Memory Card (S7-1200, S7-1500, S7-1500T)](#assign-password-via-simatic-memory-card-s7-1200-s7-1500-s7-1500t)
- [Special features when backing up and restoring a CPU (S7-1200, S7-1500, S7-1500T)](#special-features-when-backing-up-and-restoring-a-cpu-s7-1200-s7-1500-s7-1500t)
- [Tips for error avoidance and error handling (S7-1200, S7-1500, S7-1500T)](#tips-for-error-avoidance-and-error-handling-s7-1200-s7-1500-s7-1500t)
- [Rules for the replacement parts scenario (S7-1200, S7-1500, S7-1500T)](#rules-for-the-replacement-parts-scenario-s7-1200-s7-1500-s7-1500t)

##### Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)

As described in the basic information on secure communication, the proper functioning of certificate-based protocols requires private keys that must be protected as best as possible.

As of STEP 7 V17, you can use a password to protect these keys and other data worth protecting: The password to protect confidential PLC configuration data.

It is possible to do without the password if you have implemented measures to prevent unauthorized access to the TIA Portal project and the configuration of the CPU.

independently of whether you assign a password or not: The TIA Portal generates a key information that provides for the protection of the confidential PLC configuration data. This password has no influence on the secure communication process. However, the complexity of the password for the protection of confidential PLC configuration data determines how well the private keys, for example, are protected.

The presence of key information is a prerequisite for secure communication such as TLS-based secure PG/HMI communication: The CPU can handle certificates which are required for Secure Communication only if this key information is available.

The following figure shows the relationships described.

![Figure](images/141921453963_DV_resource.Stream@PNG-en-US.png)

###### Security settings wizard

When you add a CPU to the project that supports secure PG/HMI communication in the TIA Portal from the hardware catalog, a wizard starts for the security settings of the CPU.

The wizard guides you step-by-step through the following CPU settings:

- Password to protect confidential PLC configuration data
- PG/PC and HMI communication mode
- Access level

Each of these settings is explained in detail in the wizard. At the end, all settings are once again summarized in an overview.

The wizard also starts, for example, when you replace a module in the network view of the TIA Portal and the new CPU, unlike the replaced CPU, supports secure PG/HMI communication.

All settings in the wizard are applied in the Inspector window (CPU properties).

You can start the wizard at any time using a Start button in the "Protection &amp; Security" area of the CPU properties.

###### Requirement

- TIA Portal as of version V17
- CPU supports secure PG/HMI communication (for S7-1500 CPUs as of firmware version 2.9)
- The CPU is not yet loaded or the CPU is reset to factory settings with the option "Delete password for protection of confidential PLC configuration data"

###### Procedure

1. Open the CPU properties in the network view or in the device view.
2. Navigate to the area "Protection &amp; Security &gt; Protection of the PLC configuration data".

   **Result:** The "Protect confidential PLC configuration data" option is enabled first and the empty field for password entry is highlighted in red.
3. Configure the password (recommended) via the "Set" button or disable the "Protect confidential PLC configuration data" option.
4. Complete the configuration and create the user program.
5. Load the CPU.   
   When loading the hardware configuration, you will be asked once to re-enter the password.   
   **Background**: The configured password is used in the TIA Portal to generate the key information to protect confidential configuration data and thus to protect this data. For security reasons, however, neither the password nor the key information is saved in the project. In order for the key information to reach the CPU, it is re-generated when the hardware configuration is loaded, so that the password must be entered once at this point.

###### Certificate-based communication also between PG/HMI and CPU

Because, as of TIA Portal version V17 and CPU firmware version V2.9 (S7-1500) or V4.5 (S7-1200), the PG/HMI communication is also certificate-based, you will be prompted to accept the server certificate in the course of the commissioning.

###### Tips and rules for password management

- Manage your passwords in a password manager.
- Use TIA Portal's password policy verification settings to check newly entered passwords for compliance and prevent trivial passwords, for example:

  - In the project tree, navigate to the area "&lt;Project name&gt; &gt; Security settings &gt; Settings" area and select the "Password policies" area.
  - Specify, for example, the minimum number of characters the password must have or the minimum number of special characters.
- You do not have to assign different passwords for each CPU in a system or machine. If the requirements are met, you can also define the same password for a group of CPUs. This strategy also has advantages in the replacement parts scenario: If the group password is also assigned to the replacement CPU, the workload of replacing the CPU is reduced.

  Note here the risk that if the password of one of these CPUs is compromised, all CPUs with the same password are vulnerable.
- The definition of passwords also has an impact on the replacement part case, as the password for confidential PLC configuration data must be transferred to the new (replacement) CPU in addition to the configuration (see [Rules for the replacement parts scenario](#rules-for-the-replacement-parts-scenario-s7-1200-s7-1500-s7-1500t)).
- With **S7-1500R/H CPUs**, the password for confidential PLC configuration data is only loaded onto one of the two CPUs during loading. In order that the sync-up process works and that the partner CPU also works properly, the password must be transferred to the partner CPU before the sync-up, using the Online and Diagnostics editor:

  - In the Online and diagnostics view, you specify the area "Password to protect confidential PLC configuration data".
  - Enter the required password and click the "Set" button.

    If the correct password has been entered, the partner CPU can use the protected PLC configuration data and start the sync-up process.

---

**See also**

[Useful information for the protection of confidential PLC configuration data (S7-1200, S7-1500, S7-1500T)](#useful-information-for-the-protection-of-confidential-plc-configuration-data-s7-1200-s7-1500-s7-1500t)
  
[Using the Security settings wizard (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#using-the-security-settings-wizard-s7-1200)
  
[Using the Security settings wizard (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#using-the-security-settings-wizard-s7-1500)

##### Useful information for the protection of confidential PLC configuration data (S7-1200, S7-1500, S7-1500T)

The concept for Secure Communication protected by security standards comprises the following components:

- A password-based key information that is used for protecting confidential configuration data (e.g. private keys for certificates, passwords).
- A standardized log (TLS) that ensures communication between the participants (e.g. programming device and CPU).

###### "Protection of confidential configuration data" principle

The following figure shows in a simplified way how confidential configuration data, for example of a standard S7-1500 CPU, is protected: The two components project and key information are placed in different memory areas when loaded for the first time. The project in the load memory (memory card), the key information in a memory area in the CPU.

For other target systems (e.g. S7-1200 CPU, software controller) with different storage concepts, the implementation is adapted to the corresponding storage concepts, but the principle is the same.

!["Protection of confidential configuration data" principle](images/139652222731_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Project with password-protected confidential configuration data (here: in load memory = memory card) |
| ② | Key information (generated from password) to use the protected confidential configuration data (here: in the memory area in the CPU) |

###### Two memory areas for more security

The charged components are related to each other like two matching puzzle pieces: The project is bound to the loaded key information, the loaded key information is bound to the password that was assigned during configuration.

Project and key information must match, otherwise the CPU will not start.

The principle of two separate memory areas also applies to the S7-1200 CPUs and S7-1500 CPU versions without a memory card, e.g. for the SW controller or PLCSim/ PLCSim Advanced. In the versions without memory card, two separate partitions are used so that the two items of information can be managed independently of one another.

![Two memory areas for more security](images/139625288203_DV_resource.Stream@PNG-de-DE.png)

##### Changing your password (S7-1200, S7-1500, S7-1500T)

It makes a difference whether the CPU has already been loaded or not. If the CPU has already been loaded, it has the key information with which the password-protected PLC configuration data can be used.

###### Change password - configuration not yet loaded

As long as you have not yet loaded a configuration into the CPU, you can change an entered password or you can revoke the activation of the password protection.

**Requirement**

- The CPU is not yet loaded

**Procedure**

1. Open the CPU properties in the network view or in the device view.
2. Navigate to the area "Protection &amp; Security &gt; Protection of the PLC configuration data".
3. Click the "Change" button or deactivate the option "Protect confidential PLC configuration data".
4. Enter the previously valid password in the dialog. In case of a password change, also enter the new password and confirm the new password.

As long as you have not yet loaded a configuration into the CPU, the CPU is in a provisioning phase (see [CPU behavior from loading to operational readiness](#cpu-behavior-from-loading-to-operational-readiness-s7-1200-s7-1500-s7-1500t)) and you can load any valid configuration with your configured password.

###### Change password - configuration is already loaded

If the CPU has already been loaded with a configuration and the configuration is protected with a password for confidential PLC configuration data, you must first either reset the CPU to the factory settings and delete the password for confidential PLC configuration data in the CPU or delete it directly online and then set it.

**Requirements**

- You have write access to the CPU
- The CPU must be in STOP mode.

**Procedure**

1. Select the CPU in the network view.
2. Select the "Online &amp; Diagnostics" command from the shortcut menu.
3. If you also change the project on the memory card, i.e. then want to reload the configuration:

   - Select the "Reset to factory settings" area in the opened online and diagnostics view.
   - Activate the option "Delete password to protect confidential PLC configuration data". To avoid a repeated start-up of the CPU, also select the "Format memory card" option.
   - Then load the project with the changed configuration and the desired password.
4. If you do not have to change the project on the memory card, i.e. only the wrong password is set:

   - In the Online and diagnostics view, you specify the area "Password for the protection of confidential PLC configuration data".
   - Click the "Delete" button. If the "Delete" button is not available, no password has been set in the CPU yet.
   - Enter the required password and click the "Set" button.

   If the correct password has been entered, the CPU can use the protected PLC configuration data.

**No write access to the CPU**

If you do not have write access to the load memory (read access level), remove the memory card from the CPU or delete the memory card externally, e.g. in your computer, before you reset to factory settings with the option "Delete password to protect confidential PLC configuration data".

> **Note**
>
> **Reset to factory settings with mode selector of the CPU**
>
> Restoring the factory settings of the CPU via the mode selector also deletes the IP address of the CPU, but not the password for protecting confidential PLC configuration data.

---

**See also**

[Rules for the replacement parts scenario (S7-1200, S7-1500, S7-1500T)](#rules-for-the-replacement-parts-scenario-s7-1200-s7-1500-s7-1500t)

##### Resetting the password (S7-1200, S7-1500, S7-1500T)

The protection of the confidential PLC configuration data can be reset. This may be necessary, for example, if you want to change the password but no longer know the current password.

###### Password lost - configuration not yet loaded

Since you have to enter the password when loading the CPU via TIA Portal for the first time, the CPU configuration for this CPU can no longer be used. To change the password in the CPU properties, you must also enter the previously valid password. If you forget your password, do the following:

**Requirement**

- The CPU is not yet loaded

**Procedure**

1. Open the CPU properties in the network view or in the device view.
2. Navigate to the area "Protection &amp; Security &gt; Protection of the PLC configuration data".
3. Click "Reset".

   Please note that the certificates of the CPU (e.g. certificates for web server, for OPC UA server, for PG/PC communication and HMI communication) may no longer be used after the reset and may have to be created again and reassigned.

   - If you use the global security settings for the certificate manager, you must reassign the certificates from the certificate manager.
   - If you do not use the global security settings for the certificate manager, you must recreate and reassign the certificates.
4. Confirm the reset of the password.

The option for the protection of confidential PLC configuration data is still activated.

###### Delete password – Configuration is already loaded

If the CPU has already been loaded with a configuration and the configuration is protected with a password for confidential PLC configuration data, you can, for loading a new project, delete the password for confidential PLC configuration data online and then specify a new password.

**Requirements**

- You have write access to the CPU
- The CPU must be in STOP mode.

**Procedure**

1. Select the CPU in the network view.
2. Select the "Online &amp; Diagnostics" command from the shortcut menu.
3. In the area "Password to protect confidential PLC configuration data", click the "delete" button.   
   If the "Delete" button is not available, no password has been set in the CPU yet.

   | Symbol | Meaning |
   | --- | --- |
   |  | **Notice** |
   | **Deleting the password for confidential configuration data**  If the password is deleted and a loaded project requires a corresponding password, this project may no longer work without password. |  |
4. If required, now enter a new password via the "Set" button.
5. Perform a restart of the CPU.

---

**See also**

[Changing your password (S7-1200, S7-1500, S7-1500T)](#changing-your-password-s7-1200-s7-1500-s7-1500t)
  
[Resetting an S7 CPU to the factory settings (S7-1200, S7-1500)](Device%20and%20network%20diagnostics.md#resetting-an-s7-cpu-to-the-factory-settings-s7-1200-s7-1500)

##### Assign password via SIMATIC Memory Card (S7-1200, S7-1500, S7-1500T)

If you want to transfer the password to protect confidential PLC configuration data to a CPU without using TIA Portal, you can also use a SIMATIC memory card for this function.

The use of a SIMATIC memory card is suitable for the following purposes:

- Preparing a new CPU

  If a CPU is set up again, it should be configured with a password to protect the confidential PLC configuration data. After this configuration is completed, it is possible to use another SIMATIC memory card with the desired project.

  (S7-1200 CPU: A "transfer" card with transfer job can also be used to install the program on the CPU).
- CPU has a password to protect confidential PLC configuration data, but the password does not match the project

  If the passwords are not identical, you can set the correct password with the memory card in the CPU.

  (S7-1200 CPU: equipped either with SIMATIC "transfer" card or with SIMATIC "Program" card).
- reset the password for the protection of confidential PLC configuration data in the CPU

  As preparation for a disposal of the CPU or as preparation for a new project for the CPU.

###### Requirement

- TIA Portal as of version V17

###### Basic procedure

1. Creating a SIMATIC memory card with "SET PASSWORD" job

   This action creates a folder and file structure following a special pattern and writes a password for the protection of the confidential PLC configuration data as plain text to a special file on the SIMATIC memory card. See description below.
2. Insertion of a prepared SIMATIC memory card in the CPU and switch on the CPU.

   The PLC reads the password, processes it and stores the result in the internal memory. Any existing entry is overwritten.
3. Remove the SIMATIC memory card and restart the CPU.

   Results (S7-1500): While the CPU is reading the SIMATIC memory card, the LED shows the same behavior as with a firmware update. The RUN/STOP LED flashes while the CPU is setting the password. After the process has been completed successfully, the RUN/STOP LED lights up yellow and the MAINT LED flashes yellow.

The result of the operation is displayed in the diagnostics buffer as success or error message. If the password could not be set, the error LED flashes together with the other LEDs.

###### Creating a SIMATIC memory card with "SET PASSWORD" job

1. Create a folder in the root directory named "SET_PWD.S7S".
2. Create a text file named "PWD.TXT" with the password as text-only in the folder just created on the memory card.
3. Create a text file named "S7_JOB.S7S" in the root directory of the memory card with the content "SET_PWD".

   This file is the "Job file" for assigning a password for the protection of the confidential PLC configuration data of the PLC.
4. The file structure on the SIMATIC memory card then looks as follows:

   ![Creating a SIMATIC memory card with "SET PASSWORD" job](images/140775299595_DV_resource.Stream@PNG-de-DE.png)

   > **Note**
   >
   > **Safe storage of the SIMATIC memory card**
   >
   > Store the SIMATIC memory card in a safe location to which only authorized persons have access.

###### Rules and recommendations

- Setting the password must be done in a secure environment.
- The content of the text file "PWD.TXT" defines the password for the protection of confidential PLC configuration data. It must match the password that you have also assigned in the CPU configuration.
- To reset an existing password of a PLC, the text file "PWD.TXT" must be empty, i.e. the file size is 0 bytes.
- Use any text editor to create the text file. The recommended text format is "UTF-8".
- The folder and file names are not case-sensitive. However, the password itself is case-sensitive.
- Do not enter a CR/LF character at the end (PWD.TXT or S7_JOB.S7S).

##### Special features when backing up and restoring a CPU (S7-1200, S7-1500, S7-1500T)

You can back up a functional configuration of a CPU in the TIA Portal and access it at a later time; this means you can then restore the originally backed-up configuration. This allows you to load a modified configuration, for example, to test product enhancements, to change programs for troubleshooting in the system or you can replace components on a test basis. You can then restore the originally backed-up configuration of the CPU.

###### Backing up the configuration

In backing up a CPU ("Online" menu, "Load backup from online device” in TIA Portal), the password for the protection of confidential PLC configuration data is backed up as well.

###### Restoring the backup

When restore the backup of a CPU (menu "Online", command “Download to device” with marked backup in TIA Portal) the CPU can only communicate with a PG/PC or HMI if the following condition is fulfilled:

- After the restoration of a configuration protected with a password to protect confidential PLC configuration data, exactly this password must be present in the CPU.

  Otherwise the CPU cannot access the configuration data and therefore does not start.

**Remedy**

If the above error occurs, that is, the password for protecting confidential PLC configuration data does not match the backup, you must delete the password to protect confidential PLC configuration data in the CPU and then set the correct password. After a restart the CPU, the backup is functional.

---

**See also**

[Creating a backup of a device (S7-1200, S7-1500)](Creating%20a%20backup%20of%20an%20S7%20CPU.md#creating-a-backup-of-a-device-s7-1200-s7-1500)
  
[Changing your password (S7-1200, S7-1500, S7-1500T)](#changing-your-password-s7-1200-s7-1500-s7-1500t)

##### Tips for error avoidance and error handling (S7-1200, S7-1500, S7-1500T)

The following description lists some use cases that may result in CPU error messages.

###### Diagnostic buffer provides information

The CPU detects when the password protecting confidential configuration data and the loaded configuration do not match. A message in the diagnostic buffer indicates possible causes and remedies and usually leads to a solution of the problem.

###### Typical "pitfalls"

You should pay attention to the following circumstances in order to avoid or correct errors:

- Configuration loaded?  
  Regardless of whether you protect your confidential configuration data with a password or not: without a loaded configuration, the CPU does not leave the provisioning phase.
- You are trying to load the CPU with a configured password and the CPU has already received another password.  
  Example: CPU is exchanged for another CPU from the stock. The replacement CPU was not completely reset (reset to factory settings with option "Delete password for protection of confidential PLC configuration data").   
  Remedy:

  - Always prepare replacement CPUs with the appropriate option (password deleted).
  - For the configuration to be loaded, use the same password that was already used for the configuration already loaded.
  - It is also possible that the wrong project / CPU configuration was loaded. Check whether the correct CPU configuration is available.
  - Use the online function "Set password to protect confidential PLC configuration data" to delete the password or to set the same password as in the CPU configuration. Then, restart the device.

- The same error occurs if your CPU configuration does not use a password and the already loaded configuration requires a user-defined password.   
  Remedy:

  - Use the online function "Set password to protect confidential PLC configuration data" to delete the password or to set the same password as in the CPU configuration. Then, restart the device.

##### Rules for the replacement parts scenario (S7-1200, S7-1500, S7-1500T)

The assignment of passwords to protect confidential PLC configuration data also has an impact on the replacement parts scenario.

###### Rules for the replacement parts scenario

Observe the following rules for the replacement parts scenario:

**Configuration of the replacement CPU via TIA Portal**

- A CPU as replacement for an existing CPU should not have a configuration or a configured password to protect confidential PLC configuration data.  
  Advantage: You can load the project into the replacement CPU without any further preparation - regardless of whether a password is configured or not.
- If the replacement CPU has already been configured, you must reset the CPU to the factory settings with the following options set:

  - "Delete password for protection of confidential PLC configuration data"
  - "Format memory card"

**Replacement CPU is supplied with configuration data via memory card**

- If you have **not** assigned a password to a CPU in your project to protect confidential PLC configuration data, you can insert the memory card of the CPU to be replaced into a brand-new, unused CPU without any further action needed.   
  If the replacement CPU has already been configured with a password to protect confidential PLC configuration data, you must first reset this CPU to the factory settings using the option "Delete password for protection of confidential PLC configuration data".
- If you have assigned the same password to a group of CPUs, you can also assign the group password to the replacement CPU via the TIA Portal or via an appropriately prepared memory card (see [Protection of confidential configuration data](#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)).   
  In this case you can, for example, insert a memory card with the current project into the CPU and put it into operation without any further password handling.
- If you assign different passwords to each CPU in your project, you must first set the password valid for the respective CPU with the online and diagnostics editor when using the replacement CPU (area "Set password for protection of confidential PLC configuration data", see [Changing your password](#changing-your-password-s7-1200-s7-1500-s7-1500t)).

---

**See also**

[Assign password via SIMATIC Memory Card (S7-1200, S7-1500, S7-1500T)](#assign-password-via-simatic-memory-card-s7-1200-s7-1500-s7-1500t)
  
[Resetting an S7 CPU to the factory settings (S7-1200, S7-1500)](Device%20and%20network%20diagnostics.md#resetting-an-s7-cpu-to-the-factory-settings-s7-1200-s7-1500)

#### Global security settings (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Global security certificate manager (S7-1200, S7-1500, S7-1500T)](#global-security-certificate-manager-s7-1200-s7-1500-s7-1500t)
- [Managing users and roles (S7-1200, S7-1500, S7-1500T)](#managing-users-and-roles-s7-1200-s7-1500-s7-1500t)
- [Importing and exporting certificates (S7-1200, S7-1500, S7-1500T)](#importing-and-exporting-certificates-s7-1200-s7-1500-s7-1500t)
- [Renewing certificates (S7-1200, S7-1500, S7-1500T)](#renewing-certificates-s7-1200-s7-1500-s7-1500t)
- [Replacing certificates (S7-1200, S7-1500, S7-1500T)](#replacing-certificates-s7-1200-s7-1500-s7-1500t)
- [Show certificates (S7-1200, S7-1500, S7-1500T)](#show-certificates-s7-1200-s7-1500-s7-1500t)
- [Deleting certificates (S7-1200, S7-1500, S7-1500T)](#deleting-certificates-s7-1200-s7-1500-s7-1500t)

##### Global security certificate manager (S7-1200, S7-1500, S7-1500T)

###### Introduction

In the global certificate manager, you have an overview of all the certificates, for example, CA certificates, used in the project with information about the certificate holder, issuer, validity, use and the existence of a private key. With the corresponding authorization you can also manage certificates for the project there.

###### Activation of the global security settings

The global security settings are not visible until they have been activated in the project for at last one device. The "Use global security settings for certificate manager" check box is available to this end in the local CPU-specific certificate manager:

![Activation of the global security settings](images/113745265931_DV_resource.Stream@PNG-en-US.png)

The check box is located in the Inspector window in the general settings of a device with security functions under "Protection &amp; Security &gt; Certificate manager".

###### Principle

The CA certificate is issued by a certificate authority from which the device certificates are derived.

Certificate authorities can be:

- STEP 7: If the "certificate holder" and "issuer" are the same, this is a self-signed certificate; in other words a certificate issued by STEP 7.
- Higher-level certificate authority: These external certificates are external to the project and are imported and stored in the certificate memory of STEP 7.

Certificates created by one of the two certificate authorities always have a private key so that the device certificates can be derived from them.

###### Functions of the global security certificate manager

The following functions are available for selection in the global security certificate manager:

- Import of new certificates and certificate authorities.
- Import of SSL certificates (only CP x43-1 Adv.), for example, for FTP communication.
- Export of the certificates and certificate authorities used in the project.
- Renewal of expired certificates and certificate authorities.
- Replacement of existing certificate authorities.
- Adding trusted certificates and certification authorities.

Deleting manually imported certificates.

> **Note**
>
> **Downloading the configuration**
>
> After replacing or renewing certificates the configuration has to be downloaded to the corresponding devices. After replacing or renewing CA certificates the configuration has to be downloaded to the corresponding devices.

> **Note**
>
> **Current date and current time of day on the security modules**
>
> When using secure communication (for example, HTTPS), make sure that the corresponding devices have the current time of day and the current date. Otherwise the certificates used are not evaluated as valid and the secure communication does not work.

---

**See also**

[Local CPU-specific certificate manager (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#local-cpu-specific-certificate-manager-s7-1500)

##### Managing users and roles (S7-1200, S7-1500, S7-1500T)

###### Introduction

After you have activated the global security settings for the certificate manager, you have to log in to the global security settings or you require administrator rights. Otherwise you do not have sufficient user rights to edit the global certificates. You cannot access the global certificate manager without a login or if you do not have sufficient rights.

###### Roles and rights

You can configure the security settings if the predefined roles "Administrator" or "Standard" are assigned to you or if a different defined role with the associated authorization is assigned. You can view the roles in the project tree under "Global security settings &gt; User administration &gt; Roles" or, if you have corresponding rights, edit them.

| Assigned role | Diagnosing | Configuring | Managing users and roles |
| --- | --- | --- | --- |
| Administrator | Yes | Yes | Yes |
| Standard | Yes | Yes | No |
| Diagnostics | Yes | No | No |

You can create new roles and users as an administrator and assign users and roles to each other in the user administration.

###### Requirement

You have to be logged in as an administrator via the user login to the global security settings.

###### Procedure

Proceed as follows to edit users and roles:

1. In the project navigator go to user administration in the global security settings.
2. Select the role to be changed or create a new role.
3. Edit the rights of the selected role in the rights list.

##### Importing and exporting certificates (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can import and export certificates and the associated private keys. Certificates can only be imported with the global certificate manager. Certificates can also be exported via the local CPU-specific certificate manager.

You can import or export the certificates into the following file types:

- Certificates without private key to CER, DER, CRT or PEM
- Certificates with their private key to P12 (PKCS12).

###### Requirement

During import of certificates with private key you may require a password for access.

###### Importing certificates

To import a certificate follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates, device certificates, trusted certificates of root certification authorities) for the certificate to be imported.
3. Right-click in the table to open the shortcut menu.
4. Click "Import".
5. Select the import format of the certificate:

   - CER, DER, CRT or PEM for certificates without private keys.
   - P12 (PKCS12 archive) for certificates with private key.
6. Click "Open" to import the certificate.

The imported certificate has to be assigned manually to the desired device or module.

###### Exporting certificates

To export a certificate, follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates, device certificates, trusted certificates of root certification authorities) for the certificate to be exported.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Export".
5. Select the export format of the certificate:

   - CER, DER, CRT or PEM for certificates without private keys.
   - CRL for certificate block list encoded to DER
   - P12 (PKCS12 archive) for certificates with private key.
6. Click "Save" to export the certificate.

You can also export certificates directly from the local CPU-specific certificate manager.

###### Selectable file formats

X.509 certificates to the certificate standard X.509 V3 from the RFC 5280 can be imported or exported in various formats with different file name extensions:

| File name extension | PEM |
| --- | --- |
| File type | Privacy Enhanced Mail Security Certificate |
| Usage | Base64-encoded certificate |
| MIME type | application/x-pem-file |
| Meaning | Certificate in PEM/X509 format (PEM = Privacy-Enhanced Mail) with an encoding in ASCII (Base64). Format of the certificate authorities often used for the certificate transfer via e-mail to the applicant of the certificate. Instead of the file name extension PEM, a Base64-enoded certificate can also have the extensions CER or CRT. |
| Usage | In TIA Portal the import and export is supported with PEM encoding. An export with PEM encoding can be effected in the file format PEM or CRT. |

| File name extension | DER |
| --- | --- |
| File type | DER Encoded X509 Certificate |
| Usage | Binary encoded certificate |
| MIME type | application/x-x509-ca-cert, application/pkix-cert |
| Meaning | Certificate in DER/X.509 format (DER = Distinguished Encoding Rules) with binary encoding. The binary DER format is the basis for the ASCII-encoded PEM format. The DER format is used in particular in the Microsoft Windows environment and on Java platforms. Instead of the file name extension DER a binary-encoded certificate can also have the extensions CER or CRT. |
| Usage | In TIA Portal the import and export is supported with DER encoding. An export with DER encoding can be effected in the file format DER or CER. |

| File name extension | CER |
| --- | --- |
| File type | Internet Security Certificate File |
| Usage | After PEM or DER encoded certificate |
| MIME type | application/x-x509-ca-cert, application/pkix-cert, application/keychain_access |
| Meaning | Alternative file name extension CER (Canonical Encoding Rules) for a binary encoded certificate in the DER format or for a Base64/ASCII-encoded certificate in PEM format. |
| Usage | In TIA Portal the import and export is supported in the file format CER. When importing a certificate in the file format CER the encoding can be to PEM or DER. The DER encoding is used for export in the file format CER. |

| File name extension | CRT |
| --- | --- |
| File type | Internet Security Certificate File |
| Usage | After PEM or DER encoded certificate |
| MIME type | application/x-x509-ca-cert, application/pkix-cert, application/keychain_access |
| Meaning | Alternative file name extension CRT for a binary encoded certificate in the DER format or for a Base64/ASCII-encoded certificate in PEM format. |
| Usage | In TIA Portal the import and export is supported in the file format CRT. When importing a certificate in the file format CRT the encoding can be to PEM or DER. The PEM encoding is used for export in the file format CRT. |

| File name extension | CRL |
| --- | --- |
| File type | Certificate Revocation List |
| Usage | Certificate block list encoded to DER |
| MIME type | application/pkix-crl, application/x-pkcs7-crl |
| Meaning | The CRL (Certificate Revocation List) is an X.509 V3 extension and contains the list of blocked or revoked certificates for a specific root certificate. Certificate authorities use the option to revoke the authorization of certificates already issued. This is the case when certificates are compromised or if their content turns out to be faulty. Blocked certificates can be unblocked again with the CRL, for example, when the certificate turns out not to be compromised after all or if the content was correct after all. Revoked certificates remain invalid forever and cannot be authorized again. The certificate authority updates its CRLs as soon as their validity has expired or the content has changed. The source of supply of a CRL is entered in the respective certificate. |
| Usage | The TIA Portal does not support a certificate revocation via CRL. Since some external clients must have certificate block lists for the validation of the certificates, an export of the CRL is however supported. But the list is empty and solely serves the purpose of making the validation of an output certificate by certain external clients possible. |

| File name extension | P12 |
| --- | --- |
| File type | Personal Information Exchange File |
| Usage | As PKCS12-archive encoded certificates, optionally with private key |
| MIME type | application/keychain_access, application/x-pkcs12 |
| Meaning | File types in the format P12 can also contain the private key in addition to the server certificate and intermediate certificates. A password can be assigned when storing. |
| Usage | In TIA Portal the import and export is supported in the file format P12. The option for exporting into a PKCS12 archive only exists if the certificate disposes of a private key. During export a password can be assigned for the PKCS12 archive. Analog to the password assignment during exporting, the entry of a password may be required to access the certificate during importing. |

##### Renewing certificates (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can renew certificates, for example, to update a compromised certificate by an imported or new certificate.

###### Procedure

To renew a certificate, follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates, device certificates) for the certificate to be renewed.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Renew".
5. You can edit the data of the selected certificate in the dialog for new certificates.
6. When you click "OK", the certificate is renewed with the changed values.

When you renew a certificate, the old certificate is replaced by the certificate with the new values. Through the renewal of certificates no signature query to a certificate authority is generated.

##### Replacing certificates (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can replace an existing certificate by a different certificate.

###### Procedure

To replace a certificate, follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates, device certificates, trusted certificates of root certification authorities) for the certificate to be replaced.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Replace".
5. In the dialog for changing the certificate authority you replace the existing CA certificate of the project or the CA group certificate with a new one.

All certificates listed in the "Certificates involved" table are derived once again.

##### Show certificates (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can have an overview of all the certificate data displayed via the Windows certificate dialog

###### Procedure

Proceed as follows to display the certificate data:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (CA certificates, device certificates, trusted certificates of root certification authorities) for the certificate to be shown.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Show".

###### Result

Different information about the selected certificate is displayed in a window:

- General information about the certificate
- Detailed information about the certificate
- Information about the certification path

##### Deleting certificates (S7-1200, S7-1500, S7-1500T)

###### Introduction

You can delete certificates that are no longer required or are compromised.

###### Procedure

To delete a certificate, follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the matching table (device certificates, trusted certificates of root certification authorities) for the certificate to be deleted.
3. Right-click to open the shortcut menu for the selected certificate.
4. Click "Delete".

> **Note**
>
> CA certificates reserved for the project and certificates that are assigned automatically to a CP cannot be deleted.

You can also delete certificates directly in the local CPU-specific certificate manager. The certificate then remains in the global security manager for the project, but is no longer used for the device.

#### Secure Open User Communication (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)](#secure-ouc-between-two-s7-1500-cpus-s7-1500-s7-1500t)
- [Secure OUC from an S7-1500 CPU as a TLS client to an external PLC (TLS server) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-a-tls-client-to-an-external-plc-tls-server-s7-1500-s7-1500t)
- [Secure OUC from an S7-1500 CPU as TLS server to an external PLC (TLS client) (S7-1500, S7-1500T)](#secure-ouc-from-an-s7-1500-cpu-as-tls-server-to-an-external-plc-tls-client-s7-1500-s7-1500t)
- [Secure OUC via CP interface (S7-1500, S7-1500T)](#secure-ouc-via-cp-interface-s7-1500-s7-1500t)
- [Secure OUC via e-mail (S7-1500, S7-1500T)](#secure-ouc-via-e-mail-s7-1500-s7-1500t)

##### Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)

The following section describes how you can set up a Secure Open User Communication over TCP between two S7-1500 CPUs In the process one S7‑1500 CPU acts as a TLS client (active connection establishment) and the other S7‑1500 CPU as a TLS server (passive connection establishment).

###### Setting up a secure TCP connection between two S7-1500 CPUs

In order to establish secure TCP communication between two S7‑1500 CPUs you have to create a data block with the system data type TCON_IP_V4_SEC in each CPU, carry out the parameter assignment and call it directly at the instruction. The TCON instruction supports the system data types TCON_QDN_SEC and TCON_IP_V4_SEC. As of firmware version V2.5, the TSEND_C and TRCV_C instructions also support the TCON_QDN_SEC and TCON_IP_V4_SEC system data types.

Requirements:

- Current date and time are set in the CPU.
- Both S7-1500 CPUs have a minimum firmware version of V2.0
- TLS client and TLS server have all the required certificates.

![Setting up a secure TCP connection between two S7-1500 CPUs](images/90696787339_DV_resource.Stream@PNG-en-US.png)

###### Settings at the TLS client

To set up a secure TCP connection in the TLS client, follow these steps:

1. Create a global data block in the project tree.
2. Define a tag of the data type TCON_IP_4_SEC in the global data block. To do so, enter the string "TCON_IP_V4_SEC" in the "Data type" field.

   The example below shows the global data block "Data_block_1" in which the tag "SEC connection 1 TLS Client" of the data type TCON_IP_V4_SEC is defined.

   ![Settings at the TLS client](images/90872090251_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the IPv4 address of the TLS server for "RemoteAddress".

   > **Note**
   >
   > **Connection parameter InterfaceID**
   >
   > Note that you can enter the value "**0**" for the interface ID in the data type TCON_IP_V4_SEC. In this case the CPU itself searches for a matching local CPU interface.
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerCertRef": Enter the value 2 (reference to the CA certificate of the TIA Portal project (SHA256) or the value 1 (reference to the CA certificate of the TIA Portal project (SHA1)). If you use a different CA certificate, enter the corresponding ID from the certificate manager of the global security settings.
   - "TLSClientCertRef": ID of the own X.509-V3 certificate.
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_IP_V4_SEC.

###### Settings at the TLS server

To set up a secure TCP connection in the TLS server, follow these steps:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_IP_V4_SEC.

   The example below shows the global data block "Data_block_1" in which the tag "SEC connection 1 TLS Server" of the data type TCON_IP_V4_SEC is defined.

   ![Settings at the TLS server](images/90872398859_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the IPv4 address of the TLS client for "RemoteAddress".
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerReqClientCert ": Request for an X.509-V3 certificate from the TLS client Enter the value "true".
   - "TLSServerCertRef": ID of the own X.509-V3 certificate.
   - "TLSClientCertRef": Enter the value 2 (reference to the CA certificate of the TIA Portal project (SHA256) or the value 1 (reference to the CA certificate of the TIA Portal project (SHA1)). If you use a different CA certificate, enter the corresponding ID from the certificate manager of the global security settings.
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_IP_V4_SEC.

---

**See also**

[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)
  
[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

##### Secure OUC from an S7-1500 CPU as a TLS client to an external PLC (TLS server) (S7-1500, S7-1500T)

The following section describes how you can set up a Secure Open User Communication over TCP from an S7-1500 CPU as TLS client to a TLS server.

###### Setting up a secure TCP connection from an S7-1500 CPU as TLS client to a TLS server

S7-1500 CPUs as of firmware version V2 support Secure Communication with addressing via a Domain Name System (DNS).

In order to establish secure TCP communication via the domain name you have to create a data block yourself with the system data type TCON_QDN_SEC, carry out the parameter assignment and call it directly at the instruction. The TCON instruction supports the system data type TCON_QDN_SEC.

Requirements:

- At least one DNS server exists in your network.
- You have configured at least one DNS server for the S7‑1500 CPU.
- TLS client and TLS server have all the required certificates.

To set up a secure TCP connection to a TLS server, follow these steps:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_QDN_SEC.

   The example below shows the global data block "Data_block_1" in which the tag "DNS ConnectionSEC" of the data type TCON_QDN_SEC is defined.

   ![Setting up a secure TCP connection from an S7-1500 CPU as TLS client to a TLS server](images/90696774667_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the fully qualified domain name (FQDN) of the TLS server for "RemoteQDN".
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "ExtTLSCapabilities": When you enter the value 1, the client validates the subjectAlternateName in the X.509-V3 certificate of the server to check the identity of the server. The certificates are checked when the connection is established.
   - "TLSServerCertRef": ID of the X.509-V3 certificate (usually a CA certificate) that is used by the TLS client to validate the TLS server authentication. If this parameter is 0, the TLS client uses all (CA) certificates currently loaded in the client certificate store to validate the server authentication. The certificate ID of the CA certificate is entered in the TLS server.

     ![Setting up a secure TCP connection from an S7-1500 CPU as TLS client to a TLS server](images/90760369291_DV_resource.Stream@PNG-en-US.png)
   - "TLSClientCertRef": ID of the own X.509-V3 certificate.
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_QDN_SEC.

   In the example below, the CONNECT parameter of the TCON instruction is interconnected with the tag "DNS connectionSEC" (data type TCON_QDN_SEC).

   ![Setting up a secure TCP connection from an S7-1500 CPU as TLS client to a TLS server](images/88689694603_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

##### Secure OUC from an S7-1500 CPU as TLS server to an external PLC (TLS client) (S7-1500, S7-1500T)

The following section describes how you can set up a Secure Open User Communication over TCP from one S7-1500 CPU as TLS server to a TLS client.

###### Setting up a secure TCP connection via the domain name of the communication partner

S7-1500 CPUs as of firmware version V2 support Secure Communication with addressing via a Domain Name System (DNS).

In order to establish secure TCP communication via the domain name you have to create a data block yourself with the system data type TCON_QDN_SEC, carry out the parameter assignment and call it directly at the instruction. The TCON instruction supports the system data type TCON_QDN_SEC.

Requirements:

- At least one DNS server exists in your network.
- You have configured at least one DNS server for the S7‑1500 CPU.
- TLS client and TLS server have all the required certificates.

To set up a secure TCP connection to a TLS client, follow these steps:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_QDN_SEC.

   The example below shows the global data block "Data_block_1" in which the tag "DNS ConnectionSEC" of the data type TCON_QDN_SEC is defined.

   ![Setting up a secure TCP connection via the domain name of the communication partner](images/90696739467_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the local ID of the TCP connection in "ID".
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerReqClientCert": Request for an X.509-V3 certificate from the TLS client
   - "TLSServerCertRef": ID of the own X.509-V3 certificate.

     ![Setting up a secure TCP connection via the domain name of the communication partner](images/90696735115_DV_resource.Stream@PNG-en-US.png)
   - "TLSClientCertRef": ID of the X.509-V3 certificate (or a group of X.509-V3 certificates) that is used by the TLS server to validate TLS client authentication. If this parameter is 0, the TLS server uses all (CA) certificates currently loaded in the server certificate store to validate the client authentication.
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_QDN_SEC.

   In the example below, the CONNECT parameter of the TCON instruction is interconnected with the tag "DNS connectionSEC" (data type TCON_QDN_SEC).

   ![Setting up a secure TCP connection via the domain name of the communication partner](images/88689694603_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

##### Secure OUC via CP interface (S7-1500, S7-1500T)

The following sections describes the particular points to be taken into consideration in the case of Secure Open User Communication via a CP interface. At least one station is an S7-1500 station with the following modules:

- S7-1500 CPU as of firmware version V2.0 (except for S7-1500 software controller)
- CP

  - CP 1543-1 as of firmware version V2.0
  - CP 1545‑1 ab V1.0
  - CP 1543SP-1 as of firmware version V1.0

In an S7‑1500 station, the CP acts as TLS client (active connection setup) or as TLS server (passive connection setup).

The fundamental procedure and the concept for using secure communication via a CP interface is similar to that of secure communication via the interfaces of the S7-1500 CPUs. Essentially, you have to assign the certificates to the CPU in the role of a TLS server or TLS client and not to the CPU. Other rules and procedures therefore apply. These are described below.

###### Handling certificates for CPs

The following applies in general: You have to be logged on at the certificate manager in the global security settings. The generation of self-signed certificates also requires logon for the global security settings. You have to have sufficient rights as a user (administrator or user with the "Standard" role with the right to "Configure security").

The starting point for the generation or assignment of certificates at the CP is the section "Security &gt; Security properties". In this section, you log on for the global security settings.

Procedure:

1. In the network view of STEP 7, mark the CP and select the section "Security &gt; Security properties" in the Inspector window.
2. Click on the "User logon" button.
3. Log on using your user name and password.
4. Enable the "Activate security functions" option.

   The security properties are initialized.
5. Click in the first line of the "Device certificates" table to generate a new certificate or select an existing device certificate.
6. If the communication partner is also a S7-1500 station, you also need to assign a device certificate to the communication partner with STEP 7 as described here or as described for the S7-1500 CPU.

###### Example: Setting up a secure TCP connection between two S7 1500 CPUs via CP interfaces

For secure TCP communication between two S7‑1500 CPs, you need to create a data block with the TCON_IP_V4_SEC system data type in each CPU, configure it and call it directly at the instruction.

Requirements:

- Both S7 1500 CPUs have one of the firmware versions specified above.
- The CPs have one of the firmware versions specified above.
- TLS client and TLS server have all the required certificates.

  - A device certificate (end-entity certificate) for the CP must be generated and be located in the certificate memory of the CP. If a communication partner is an external device (for example an MES or ERP system), a device certificate also has to exist for this device.
  - The root certificate (CA certificate) with which the device certificate of the communication partner is signed must also be located in the certificate memory of the CP or in the certificate memory of the external device. If you use intermediate certificates, you have to ensure that the complete certificate path exists in the validating device. A device uses these certificates to validate the device certificate of the communication partner.
- The communication partner must always be addressed via its IPv4 address, not via its domain name.

The following figure shows the different certificates in the devices for a scenario in which both communication partners communicate via one CP. In addition, the figure shows the transfer of the device certificates during establishment of the connection ("Hello").

![Example: Setting up a secure TCP connection between two S7 1500 CPUs via CP interfaces](images/90696787339_DV_resource.Stream@PNG-en-US.png)

###### Settings at the TLS client

To set up a secure TCP connection in the TLS client, follow these steps:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_IP_V4_SEC. To do so, enter the string "TCON_IP_V4_SEC" in the "Data type" field.

   The example below shows the global data block "Data_block_1" in which the tag "SEC connection 1 TLS Client" of the data type TCON_IP_V4_SEC is defined.

   The Interface ID has the value of the HW identifier of the IE interface of the local CP (TLS client).

   ![Settings at the TLS client](images/113725651851_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the IPv4 address of the TLS server for "RemoteAddress".
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerCertRef": Enter the value 2 (reference to the CA certificate of the TIA Portal project (SHA256) or the value 1 (reference to the CA certificate of the TIA Portal project (SHA1)).
   - "TLSClientCertRef": ID of the own X.509-V3 certificate.
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_IP_V4_SEC.

###### Settings on the TLS server

To set up a secure TCP connection in the TLS server, proceed as follows:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_IP_V4_SEC.

   The example below shows the global data block "Data_block_1" in which the tag "SEC connection 1 TLS Server" of the data type TCON_IP_V4_SEC is defined.

   The interface ID has the value of the HW identifier of the IE interface of the local CP (TLS server).

   ![Settings on the TLS server](images/113725655563_DV_resource.Stream@PNG-en-US.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the IPv4 address of the TLS client for "RemoteAddress".
4. Set the parameters for Secure Communication in the "Start value" column.

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerReqClientCert ": Request for an X.509-V3 certificate from the TLS client Enter the value "true".
   - "TLSServerCertRef": ID of the own X.509-V3 certificate.
   - "TLSClientCertRef": Enter the value 2 (reference to the CA certificate of the TIA Portal project (SHA256) or the value 1 (reference to the CA certificate of the TIA Portal project (SHA1)).
5. Create a TCON instruction in the program editor.
6. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_IP_V4_SEC.

###### Upload device as new station

When you upload a configuration with certificates and configured secure Open User Communication as a new station into your STEP 7 project, the certificates of the CP are not uploaded, in contrast to the certificates of the CPU. After the device has been loaded as a new station, no more certificates are contained in the corresponding tables of the CPs for the device certificates.

You have to perform configuration of certificates again after the upload. Otherwise, renewed loading of the configuration results in the certificates that originally exist in the CP being deleted so that secure communication does not function.

###### Secure OUC connections via CPU and CP interfaces - similarities

- Connection resources:   
  No differences between OUC and secure OUC. A programmed secure OUC connection uses a connection resource just like an OUC connection, irrespective of which IE/PROFINET interface communicates with the station.
- Connection diagnostics:   
  No differences between OUC and secure OUC connection diagnostics.
- Loading of projects with secure OUC connections into the CPU:   
  Only possible in STOP of the CPU, if certificates are loaded as well.  
  Recommendation: Load to device &gt; Hardware and software. Reason: Ensuring the consistency between the program with secure OUC, hardware configuration and certificates.  
  Certificates are loaded with the hardware configuration - therefore loading requires a stop of the CPU. The reloading of blocks that utilize further secure OUC connections is only possible in RUN if the certificates required for this purpose are already located on the module.

---

**See also**

[TCON: Establish communication connection (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Creating certificates (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#creating-certificates-s7-1500)
  
[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

##### Secure OUC via e-mail (S7-1500, S7-1500T)

The following section describes how to set up a secure connection (SMTP over TLS) to a mail server with the TMAIL_C communication instruction.

###### Setting up a secure connection to a mail server

In order to establish a secure communication to a mail server you have to create a data block yourself with one of the system data types TMAIL_V4_SEC, TMAIL_V6_SEC or TMAIL_QDN_SEC, carry out the parameter assignment and call it directly at the TMAIL_C instruction.

Requirements:

- S7-1500 CPU as of firmware version V2.0 with communication module CP 1543‑1 as of firmware version V2.0
- ET 200SP CPU as of firmware version V2.0 with communication module CP 1542SP‑1 (IRC) as of firmware version V1.0
- You have assigned all CA certificates of the mail server (TLS server) to the CP (TLS client) and loaded the configuration into the CPU.

To set up a secure mail server connection using the IPv4 address of the mail server, proceed as follows:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TMAIL_V4_SEC.

   The example below shows the global data block "MailConnDB" in which the tag "MailConnectionSEC" of the data type TMAIL_V4_SEC is defined.

   ![Setting up a secure connection to a mail server](images/90872792075_DV_resource.Stream@PNG-de-DE.png)
3. Set the connection parameters of the TCP connection in the "Start value" column. For example, enter the IPv4 address of the mail server for "MailServerAdress".
4. Set the parameters for Secure Communication in the "Start value" column. For example, enter the certificate ID of the CA certificate of the communication partner for "TLSServerCertRef".

   - "ActivateSecureConn": Activation of secure communication for this connection. If this parameter has the value FALSE, the subsequent security parameters are irrelevant. You can set up a non-secure TCP or UDP connection in this case.
   - "TLSServerCertRef": Reference to the X.509 V3 (CA) certificate of the mail server which is used by the TLS client to validate the authentication of the mail server.

     ![Setting up a secure connection to a mail server](images/88689898635_DV_resource.Stream@PNG-en-US.png)
5. Create a TMAIL_C instruction in the program editor.
6. Interconnect the MAIL_ADDR_PARAM parameter of the TMAIL_C instruction with the tag of the data type TMAIL_V4_SEC.

   In the following example the MAIL_ADDR_PARAM parameter of the TMAIL_C instruction is interconnected with the "MAILConnectionSEC" tag (data type TMAIL_V4_SEC).

   ![Setting up a secure connection to a mail server](images/88689851915_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[Description TMAIL_C as of version V4.0 (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#description-tmail_c-as-of-version-v40-s7-1200-s7-1500)
  
[Parameter MAIL_ADDR_PARAM as of Version 4.0 of TMAIL_C (S7-1200, S7-1500)](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#parameter-mail_addr_param-as-of-version-40-of-tmail_c-s7-1200-s7-1500)
  
[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

#### Secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [PG/HMI communication based on standardized security mechanisms (S7-1200, S7-1500, S7-1500T)](#pghmi-communication-based-on-standardized-security-mechanisms-s7-1200-s7-1500-s7-1500t)
- [Additional settings for the secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)](#additional-settings-for-the-secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)
- [Tip for certificate-based communication between PG and CPU (S7-1200, S7-1500, S7-1500T)](#tip-for-certificate-based-communication-between-pg-and-cpu-s7-1200-s7-1500-s7-1500t)
- [CPU behavior from loading to operational readiness (S7-1200, S7-1500, S7-1500T)](#cpu-behavior-from-loading-to-operational-readiness-s7-1200-s7-1500-s7-1500t)
- [Using secure HMI communication (S7-1200, S7-1500, S7-1500T)](#using-secure-hmi-communication-s7-1200-s7-1500-s7-1500t)
- [Using Legacy PG/PC communication for TIA Portal (S7-1200, S7-1500, S7-1500T)](#using-legacy-pgpc-communication-for-tia-portal-s7-1200-s7-1500-s7-1500t)
- [Information about compatibility (S7-1200, S7-1500, S7-1500T)](#information-about-compatibility-s7-1200-s7-1500-s7-1500t)

##### PG/HMI communication based on standardized security mechanisms (S7-1200, S7-1500, S7-1500T)

With the central components of the TIA Portal, STEP 7 and WinCC, an innovative and standardized Secure PG/PC and HMI Communication - PG/HMI communication for short - is implemented starting with version V17 together with the latest controllers and latest HMI devices.

The following CPU families are referred to in detail:

- S7-1500 controller family as of firmware version V2.9
- S7-1200 controller family as of firmware version V4.5
- Software controllers as of firmware version V21.9
- SIMATIC Drive controllers as of firmware version V2.9
- PLCSim and PLCSim Advanced Version V4.0

HMI components have also been updated to support Secure PG/HMI Communication:

- Panels or PCs configured with WinCC Basic, Comfort and Advanced
- PCs with WinCC RT Professional
- WinCC Unified PCs and Comfort Panels

Also updated are SINAMICS RT SW as of version V6.1 and STARTDRIVE as of version V17.

###### Properties of PG/HMI communication

One characteristic of PG communication and HMI communication above all is their simplicity: Establishing an online connection from a programming device with installed TIA Portal to a CPU, for example, to load a program, requires little effort. This online connection also meets criteria such as confidentiality and integrity - based on a proven SIMATIC communication standard.

In the course of integrating machines and systems into an open IT environment, however, it must be ensured that the communication between the programming device / HMI device and the CPU is not only secure in the sense of maintaining integrity and confidentiality for sensitive data but also that this security meets generally accepted standards and is thus ready for the challenges of the future.

With TIA Portal version V14, the "Open User Communication" procedure for communication based on user programs has already been extended by the "**Secure** Open User Communication" variant. Other certificate-based communication mechanisms have become established (HTTPS, Secure SMTP over TLS or OPC UA). As of TIA Portal Version V17, PG/HMI communication has also been upgraded: Here, too, the TLS (Transport Layer Security) protocol is used to secure PG/HMI communication using standardized security mechanisms.

###### What has changed

**Additional optional password for more security**

The most noticeable change in the frame of the configuring of the above devices is the ability to assign a password to protect sensitive configuration data of the respective CPU. This refers to data such as private keys that are required for the proper functioning of certificate-based protocols (Secure Communication) - as of TIA Portal V17 also for the PG/HMI communication. You can use a policy setting to check the assigned passwords as they are entered into the TIA Portal. This will ensure that your company complies with prescribed password policies.

If your machine or system does not require this protection based on the Siemens Industrial Defense-in-Depth concept, you can dispense with password assignment, for example, because another equivalent protection is present. It is possible to do without the password if you have implemented measures to prevent unauthorized access to the TIA Portal project and the configuration of the CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Without password, weak protection of private keys**  Note that without a password to protect trusted configuration data, the private keys for certificates required for secure communication are only weakly protected. |  |

**Certificate-based communication between PG/HMI and CPU**

Because PG/HMI communication is certificate-based, you will be asked to accept the server certificate during commissioning.

Additional parameter assignment options allow you to determine the behavior of the CPU during operation: For example, you can specify that the CPU also allows connection to devices that do not support Secure PG/HMI communication.

**Maintenance / replacement parts scenario**

For the problem-free exchange of the CPU in replacement parts scenario, you must observe specific rules (see [Rules for the replacement parts scenario](#rules-for-the-replacement-parts-scenario-s7-1200-s7-1500-s7-1500t)).

---

**See also**

[Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)](#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)
  
[Using the Security settings wizard (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#using-the-security-settings-wizard-s7-1200)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

##### Additional settings for the secure PG/HMI communication (S7-1200, S7-1500, S7-1500T)

In addition to the assignment of a password to protect confidential PLC configuration data, you have further setting options for the behavior of the CPU during operation.

###### PG/PC and HMI communication mode

You can set how the CPU can communicate with programming devices and HMI devices:

- Only via secure PG/HMI communication
- Both via Secure PG/HMI communication and via the previously used PG/HMI communication, "Legacy PG/HMI communication" for short.

**Procedure**

1. In the CPU properties, navigate to the area "Protection &amp; Security &gt; Connection mechanisms".
2. Select the option you want to use.

###### Select certificate or generate a new certificate

If you select the connection mechanism for PG/HMI communication, you can select a PLC communication certificate for the protection of the connection in the same context or have it generated by the TIA Portal. If you have assigned a password or if you have deactivated the option to protect confidential PLC configuration data (i.e. no password has been set), then a certificate with suitable settings and a valid default name is already preset in the "Protection &amp; Security&gt; Connection mechanisms" area.

**Procedure**

If you want to have a new certificate generated by the TIA Portal or if you want to select another existing certificate:

1. In the "PLC communication certificate" field, click the three points to expand the field.
2. Select the certificate you want or click the "Add" button.
3. When adding a certificate, a dialog appears with setting options for the certificate.   
   The purpose is set to "TLS server", you can change other parameters (such as name, hash algorithm).

The general rules for certificate management apply. For example, if you want to generate a CA certificate, the option "Global settings for the certificate manager" must be selected. You also have the option of generating a self-signed PLC certificate.

---

**See also**

[Certificate management with TIA Portal (S7-1200, S7-1500, S7-1500T)](#certificate-management-with-tia-portal-s7-1200-s7-1500-s7-1500t)
  
[Global security settings (S7-1200, S7-1500, S7-1500T)](#global-security-settings-s7-1200-s7-1500-s7-1500t)

##### Tip for certificate-based communication between PG and CPU (S7-1200, S7-1500, S7-1500T)

The certificate-based PG/PC communication (Secure PG/PC communication) means that the communication partner of the CPU – the programming device with installed TIA Portal – must trust the device certificate of the CPU so that a connection can be loaded.

To put it simply, from the TIA Portal perspective you have the following options to trust the certificate of a CPU:

- The PG with TIA Portal is in possession of the device certificate of the CPU because it was, for example, created or imported in the project. In this case, the certificate check runs automatically and without prompting.
- The PG with TIA Portal is not in possession of the device certificate of the CPU, because the CPU was determined via "Accessible stations", for example, and is not available in the project. In this case, the TIA Portal asks the TIA Portal user whether the certificate can be trusted. This may be possible only with great effort because the CPU is not in sight, for example, and the authenticity can therefore not be checked immediately.
- The PG with TIA Portal is in possession of the CA certificate (certification authority) and all CPUs that can be reached in the network from the TIA Portal have device certificates issued by this CA certificate.

  Advantage of this solution: TIA Portal can check device certificates automatically, even if the device certificates of the communication partners are not available in TIA Portal.

The solution with a CA certificate (certification authority) is explained in more detail below.

###### Requirement

You can use the certification authority of the TIA Portal to create device certificates for a CPU and use the existing CA certificates to sign the device certificates. However, you can also import another certification authority into TIA Portal and use it.

Enabling the global security policies for the certificate manager is a requirement. Only with this setting you can generate CA-signed certificates.

See also here: [Certificate management with TIA Portal](#certificate-management-with-tia-portal-s7-1200-s7-1500-s7-1500t)

###### Exporting CA certificate for programming devices

To export the corresponding CA certificate after creating and assigning a certificate, follow these steps:

1. Open the certificate manager in the global security settings in the project tree.
2. Select the table "CA certificates" for the certificate to be exported.
3. Right-click to open the shortcut menu of the selected certificate.
4. Click "Export".
5. Select the export format of the certificate and the storage location.

###### Store CA certificate in the TIA Portal

To make the exported certificate known to a PG with TIA Portal and thus enable automatic certificate checking, follow these steps:

1. Copy the CA certificate exported in the previous step to the following directory:

   C:\ProgramData\Siemens\Automation\Certstore\Trusted
2. Start TIA Portal.

   In the "Info" tab of the Inspector window, a message appears for each CA certificate which provides information on whether the CA certificate could be successfully transferred to the CA store of TIA Portal.

   However, no detailed causes are output in case of failure.

###### Adding device certificates to the TIA Portal certificate revocation list (CRL)

You have the option to add individual device certificates to a certificate revocation list (CRL), for example, because the associated key is no longer considered secure.

When the TIA Portal establishes a connection to a CPU whose device certificate is in the certificate revocation list, a dialog appears in the TIA Portal asking whether you still want to trust the certificate. If you decline, the connection will not be established.

To add a device certificate to the certificate revocation list, follow these steps:

1. Copy the device certificate to the following directory:

   C:\ProgramData\Siemens\Automation\Certstore\CRL
2. Start TIA Portal.

   In the "Info" tab of the Inspector window, a message appears for each certificate which provides information about whether the certificate could be successfully transferred to the CRL store of TIA Portal.

   However, no detailed causes are output in case of failure.

---

**See also**

[Examples for the management of certificates (S7-1200, S7-1500, S7-1500T)](#examples-for-the-management-of-certificates-s7-1200-s7-1500-s7-1500t)

##### CPU behavior from loading to operational readiness (S7-1200, S7-1500, S7-1500T)

To ensure that communication between the CPU and a programming device or HMI device is secure, it must first have a certificate. However, the certificate for productive operation is only issued when the project is loaded into the CPU.

To ensure that the initial loading is also secured, the CPU first creates a self-signed certificate. The following description explains the different phases of establishing a connection.

###### Requirement for the initial establishment of connection to load the CPU

- No password for confidential PLC configuration data available in the CPU.

  If the CPU has already been loaded and therefore already has a password for confidential PLC configuration data, this password must then match the project that is to be loaded.
- Project with CPU configuration (including password for confidential PLC configuration data) and user program is available.
- The CPU is in STOP mode.
- Programming device and CPU are directly connected to each other and are located in a protected environment; i.e. you can identify the CPU to be loaded and control the connection between CPU and programming device.

###### Initial establishment of connetion to the CPU - provisioning phase

The first connection establishment for loading the CPU is secured by the TLS procedure in terms of Secure PG/HMI Communication.

However, the CPU uses its manufacturer device certificate (if available) or a self-signed certificate to establish this connection. The CPU can only be used to a limited extent in this phase. In this phase, the CPU waits for the provision of the password-based key information - or more simply stated, it is expecting the password for confidential PLC configuration data. In the following, this phase is also called the provisioning phase. A message in the diagnostic buffer indicates that the CPU is in the provisioning phase.

When a project is loaded into the CPU, the CPU receives the project data:

- Hardware configuration including configured certificates for secure communication (OPC UA, HTTPS, Secure OUC, Secure PG/HMI Communication)
- User program

![Initial establishment of connetion to the CPU - provisioning phase](images/140402154507_DV_resource.Stream@PNG-en-US.png)

###### Ending the provisioning phase

TIA Portal does not store the password for confidential PLC configuration data itself or the key information generated from the password in the project.

Therefore, the password is requested in a dialog when loading the project for the first time or when loading a new project and transferred to the CPU as key information. Only after this step the CPU is able to use the protected PLC configuration data - this completes the provisioning phase and the CPU can start operating.

If you do not protect the confidential PLC configuration data with a password, there is no need to enter the password when loading the CPU for the first time. This has no influence on the flow of the PG/HMI communication but you have to consider that the confidential PLC configuration data (e.g. private keys) offer almost no protection against unauthorized access in this case.

###### Startup of PG/HMI communication

When the CPU is loaded and has received the CPU certificate for Secure PG/HMI Communication, the programming device connects again - this time based on the loaded CA certificate.

![Startup of PG/HMI communication](images/142299179659_DV_resource.Stream@PNG-en-US.png)

##### Using secure HMI communication (S7-1200, S7-1500, S7-1500T)

As of TIA Portal version V17, the CPU and the HMI device communicate via secure HMI communication if both devices meet the requirements for this type of communication.

The basis of secure HMI communication is that the HMI device can verify the authenticity of the CPU, using the PLC communication certificate that the CPU sends when establishing communication, and considers the CPU to be "trustworthy". Secure HMI communication is only possible when this turns out to be the case.

This section describes the measures you must take for the various HMI devices to manually label the PLC communication certificate as "trustworthy".

###### Requirement

- CPU and HMI device support secure HMI communication.
- A current project is available on the CPU (TIA Portal V17 and higher).

###### Configuring secure HMI communication

1. Configure the HMI device with an alarm view.
2. Configure the CPU with the required security settings. Select a PLC communication certificate to protect the HMI connection or have the TIA Portal generate a PLC communication certificate.
3. Configure the HMI connection between the CPU and the HMI device.
4. Download the project to the CPU and the HMI device. During the project transfer, the PLC communication certificate and, if necessary, a CA (Certificate Authority) certificate is transferred to the CPU and the HMI device.

**Note**

Without an alarm view you cannot identify the errors during connection establishment.

###### Trusting the PLC communication certificate

During connection setup, the CPU transfers the PLC communication certificate to the HMI device.

- When the PLC communication certificate is already available on the HMI device with the "trustworthy" status, a secure HMI communication is automatically set up between the CPU and the HMI device.
- When the PLC communication certificate is not available in the "trustworthy" status on the HMI device, you will see a message in the alarm view of the HMI device informing you that the CPU is not trusted along with an error code.

  In this case, you must label the PLC communication certificate on the HMI device as "trustworthy".

Depending on the type of your HMI device, follow these steps.

**Basic Panels 2nd Generation**

1. In the Start Center, select "Settings &gt; Internet Settings &gt; Certificate store".
2. In the "Available certificates in Device" list, select the PLC communication certificate of the CPU.
3. Press "Trust".
4. Restart the HMI runtime software.

**Unified Comfort Panels**

1. Open the Control Panel.
2. Select "Security &gt; Certificates".
3. In the "Certifcate store" selection list, select the entry "Other Certificates".
4. In the "Other certificates" list, select the PLC communication certificate of the CPU.
5. Press "Trust".
6. Restart the HMI runtime software.

**Comfort Panels, Mobile Panels 2nd Generation**

1. Open the file manager via the Windows CE desktop icon "My Device".
2. Navigate to the directory​ "\flash\simatic\SystemRoot\OMS\Untrusted". There you will find the PLC communication certificate of the CPU.
3. Copy the PLC communication certificate of the CPU to the directory "\flash\simatic\SystemRoot\OMS\Trusted".
4. Restart the HMI runtime software.

When the PLC communication certificate is already available on the HMI device with the "trustworthy" status, secure HMI communication can be set up. You can find additional information in the operating instructions of the HMI device.

##### Using Legacy PG/PC communication for TIA Portal (S7-1200, S7-1500, S7-1500T)

As of TIA Portal version V17, the TIA Portal and the S7-1200/S7-1500 CPU as of firmware version V4.5/V2.9 automatically communicate "securely" - the connection partners set their connection mechanisms automatically to the highest possible security method.

Only special circumstances (see [Information about compatibility](#information-about-compatibility-s7-1200-s7-1500-s7-1500t)) cause a fallback to the old PG/PC communication, called "Legacy PG/PC communication".

There may be some cases in which the higher security is not desirable because it can impact the transmission rate of CPUs with weak communication performance.

###### Requirement

- There may be no online connections to the CPUs.
- For CPUs that are to be reached online, the option "Only permit secure PG/PC and HMI communication" must be disabled (CPU parameters in the area "Connection mechanisms").
- The communication partners are in a protected environment, for example, during the commissioning phase.

###### Setting the Legacy PG/PC communication

1. In the "Online" menu, select the command "Use only Legacy PG/PC communication".
2. Select the check box in front of the menu command.

**Result**: All online connections are set up as for TIA Portal versions &lt; V17.

The setting remains active for the duration of the session. When you open a project, the option "Use only·Legacy PG/PC communication" is not set.

###### Behavior with enabled option "Use only Legacy PG/PC communication"

- A password to protect confidential PLC configuration data cannot be specified, modified or deleted online for CPUs. These functions require disabling the "Use only Legacy PG/PC communication" option.
- A CPU that is set to only permit secure PG/PC and HMI communication can no longer be reached online.

##### Information about compatibility (S7-1200, S7-1500, S7-1500T)

The following description provides information about the interaction between different TIA Portal versions with different CPU firmware versions and the effects on the type of PG/HMI connection.

###### Projects created with TIA Portal &lt; V17

For example, if you have created a project with TIA Portal version V16 for an S7-1500 CPU (e.g. version V2.8), then the corresponding configuration with TIA Portal V17 can also be loaded into an S7-1500 CPU V2.9, e.g. in a spare part scenario - with the same behavior as a configuration on an S7-1500 CPU V2.8.

Even projects created with TIA Portal &lt; V17 and transferred to a memory card work without problems in an S7-1500 CPU V2.9.

However, the concept of protecting confidential PLC configuration data applies as soon as you open the project with TIA Portal ≥ V17, update the firmware version of the CPU via a device replacement and thus save it as a CPU with a firmware version ≥ V2.9 (see [Useful information for the protection of confidential PLC configuration data](#useful-information-for-the-protection-of-confidential-plc-configuration-data-s7-1200-s7-1500-s7-1500t)). The project can no longer be edited with previous versions of TIA Portal V17.

###### PG/HMI and CPU connected differently

As explained in the previous sections, the secure PG/HMI connection as of V17 between the PG/HMI device and CPU (current version) is characterized by the employed standardized communication procedure, TLS (Transport Layer Security).

You have the option of connecting a V2.9 CPU to a current programming device with TIA Portal V17 or higher and additionally, for example, to an HMI device with a runtime from the previous version: The devices automatically adjust their connection mechanisms accordingly. In order to be able to better differentiate between the two connection mechanisms, we call the previous procedure, which is based on a variant of S7 communication, "Legacy procedure" for short.

In summary ("PG" here stands for a programming device with TIA Portal):

- PG/HMI and CPU come with the V17 (or subsequent version): TLS procedure is used.
- PG/HMI comes from a predecessor version (&lt; V17): Legacy procedure is used - provided that you have deactivated the option "Only allow secure PG/PC and HMI communication" in the CPU properties.
- CPU comes with V17 (or higher), several PGs/HMIs are connected and come from both V17 (or higher) and previous versions: TLS + legacy procedures are used - provided that you have deactivated the option "Only allow secure PG/PC and HMI communication" in the CPU properties.

**When the CPU state changes**

The diagnostics buffer provides you with information if its status changes due to events in connection with the Secure PG/HMI Communication.

Examples:

- After successfully loading a configuration with a configured password, the diagnostics buffer reports that the CPU is changing from the provisioning phase to Secure Mode (TLS procedure).
- You have connected a PG with TIA Portal V17 to a CPU V2.9. Secure PG/HMI communication (TLS procedure) is established automatically.

## Creating configurations

This section contains information on the following topics:

- [Configuring automation systems](Configuring%20automation%20systems.md#configuring-automation-systems)
- Configuring PC systems (PC)
- [Configuring CPs and applications for PC stations](Configuring%20CPs%20and%20applications%20for%20PC%20stations.md#configuring-cps-and-applications-for-pc-stations)
- [Configuration for point-to-point links (S7-1500)](Configuration%20for%20point-to-point%20links%20%28S7-1500%29.md#configuration-for-point-to-point-links-s7-1500)
- [Configuration for point-to-point links (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#configuration-for-point-to-point-links-s7-300-s7-400)
- [TeleControl](TeleControl.md#telecontrol)
- [SCALANCE X, W and M](SCALANCE%20X%2C%20W%20and%20M.md#scalance-x-w-and-m)
- [Configuring AS-i devices](Configuring%20AS-i%20devices.md#configuring-as-i-devices)
- [Configuring PROFIBUS DP](Configuring%20PROFIBUS%20DP.md#configuring-profibus-dp)
- [Configuring PROFIBUS DP (S7-1200)](#configuring-profibus-dp-s7-1200)
- [Configuring PROFINET IO](#configuring-profinet-io)
- [Bus coupling with PN/PN coupler](#bus-coupling-with-pnpn-coupler)
- Configuring SIMOTION devices
- [Integrating external tools](#integrating-external-tools)
- [Loading a configuration](#loading-a-configuration)

### Configuring PROFIBUS DP (S7-1200)

This section contains information on the following topics:

- [The basics of configuring a DP master system (S7-1200)](#the-basics-of-configuring-a-dp-master-system-s7-1200)
- [DP slaves within the hardware catalog (S7-1200)](#dp-slaves-within-the-hardware-catalog-s7-1200)
- [DP/DP coupler in the hardware catalog  (S7-1200)](#dpdp-coupler-in-the-hardware-catalog-s7-1200)
- [Configurations involving PROFIBUS DP (S7-1200)](#configurations-involving-profibus-dp-s7-1200)
- [Configuring distributed I/O systems (S7-1200)](#configuring-distributed-io-systems-s7-1200)
- [Configuring intelligent DP slaves (S7-1200)](#configuring-intelligent-dp-slaves-s7-1200)
- [Configuring DP slaves as distributed I/O devices (S7-1200)](#configuring-dp-slaves-as-distributed-io-devices-s7-1200)
- [Using GSD files (S7-1200)](#using-gsd-files-s7-1200)

#### The basics of configuring a DP master system (S7-1200)

##### Distributed I/O

DP master systems that consist of a DP master and DP slaves which are connected via a bus and communicate with one another via the PROFIBUS DP protocol are referred to as distributed I/O.

##### Firmware version of the S7‑1200 CPU

Use of the PROFIBUS functions with the S7‑1200, requires CPUs with firmware version 2.0 or higher.

##### Configuring distributed I/O

Since DP masters and DP slaves are different devices, these instructions only provide a basic configuration procedure. However, the process for configuring distributed I/O is practically identical to that of non-distributed configuration.

##### Creating the DP master system in the network view

After you have used dragged a DP master and a DP slave (for example, a CM 1243‑5 and a CM 1243‑5) from the hardware catalog to the network view, connect them both to a PROFIBUS subnet.

##### Additional information

Observe additional information on the scope of functions in the manuals of the respective device.

#### DP slaves within the hardware catalog (S7-1200)

##### DP slaves within the hardware catalog

You will find the DP slaves in the "Distributed I/O" folder of the hardware catalog. Compact and modular DP slaves are located there:

- Compact DP slaves  
  Modules with integrated digital/analog inputs and outputs, for example, ET 200L
- Modular DP slaves  
  (Interface modules with S7 modules assigned, for example, ET 200M

The available DP master and the desired functionality will determine which DP slaves can be used.

##### I slaves within the hardware catalog

The CM 1242-5 is, for example, an DP slave that can be configured as intelligent DP slave. You can find it in the hardware catalog at:

- CM 1242‑5  
  "PLC &gt; SIMATIC S7 1200 &gt; Communication module &gt; PROFIBUS"

#### DP/DP coupler in the hardware catalog  (S7-1200)

##### Introduction

A DP/DP coupler connects two PROFIBUS DP networks as a gateway so that the DP master from one network can transfer data to the DP master of the other network.

The maximum amount of data that can be transferred is 244 bytes input data and 244 bytes output data.

##### DP/DP coupler in the hardware catalog

Details of a DP/DP coupler as gateway between two DM master systems are contained in the hardware catalog in the folder "Other field devices &gt; PROFIBUS-DP &gt; Gateways".

##### Configuring the DP/DP coupler

DP/DP couplers are configured in both PROFIBUS networks, each in their own master systems.

The input and output areas of both networks must thereby be matched to one another. The output data from one end of the DP/DP coupler are accepted as input data at the other respective end and vice versa.

#### Configurations involving PROFIBUS DP (S7-1200)

This section contains information on the following topics:

- [Configurations involving basic DP slaves (S7-1200)](#configurations-involving-basic-dp-slaves-s7-1200)
- [Configurations involving intelligent DP slaves (S7-1200)](#configurations-involving-intelligent-dp-slaves-s7-1200)

##### Configurations involving basic DP slaves (S7-1200)

###### Communication between DP master and DP slave

In the case of a configuration involving simple DP slaves, data is exchanged between the DP master and simple DP slaves, i.e. with I/O modules via the DP master. The DP master sequentially polls each DP slave configured within the DP master system and contained in its polling list. In doing so, it transfers the output data to the slaves and receives their input data in return.

###### Mono-master system

The configuration with only one DP master is also described as mono-master system. A single DP master with its associated DP slaves is connected to a physical PROFIBUS DP subnet.

![Mono-master system](images/26426690699_DV_resource.Stream@PNG-en-US.png)

##### Configurations involving intelligent DP slaves (S7-1200)

###### Definition

DP slaves that feature their own preprocessing program are referred to as intelligent DP slaves (I-slaves).

CM 1242-5 is an intelligent DP slave.

###### I-slave &lt;&gt; DP master data exchange

A higher-level automation system processes the automation task, which is broken down into sub-tasks. The sub-tasks are processed in the lower-level automation systems. The necessary control tasks are processed separately and efficiently in the CPUs as preprocessing programs.

In the case of configurations involving intelligent DP slaves, the DP master only accesses the operand area of the I-slave's CPU, and not the I/O modules of the intelligent DP slave. The operand area must not be assigned to any actual I/O modules in the I-slave. The assignment must be made during I-slave configuration.

The addresses of the data to be exchanged between the master and slave are configured in the transfer area of the I-slave.

![I-slave &lt;> DP master data exchange](images/41008052491_DV_resource.Stream@PNG-en-US.png)

#### Configuring distributed I/O systems (S7-1200)

This section contains information on the following topics:

- [Creating a DP master system (S7-1200)](#creating-a-dp-master-system-s7-1200)
- [Editing DP master systems and interfaces (S7-1200)](#editing-dp-master-systems-and-interfaces-s7-1200)
- [Adding DP slaves to the master system and configuring them (S7-1200)](#adding-dp-slaves-to-the-master-system-and-configuring-them-s7-1200)
- [Hint: Quick configuration of master systems (S7-1200)](#hint-quick-configuration-of-master-systems-s7-1200)

##### Creating a DP master system (S7-1200)

###### Introduction

To create a PROFIBUS DP master system, you need to have one DP master and at least one DP slave. As soon as you connect a DP master to a DP slave via their PROFIBUS DP interfaces, a master-slave link is established.

###### DP master and DP slave

The DP master must have a PROFIBUS DP interface. When using an S7-1200 CPU with PROFINET interface, you require the communications module CM 1243‑5 with PROFIBUS DP interface for use as the DP master.

As DP slave, you can use head modules of the distributed I/O with PROFIBUS DP interface or CPUs as intelligent DP slaves. When using an S7-1200 CPU with PROFINET interface, you require the communications module CM 1242‑5 with PROFIBUS DP interface to use the CPU as an intelligent DP slave.

###### Requirement

- You are in the network view.
- The hardware catalog is open.

###### Procedure

To create a DP master system, for example with a CPU 1217C , follow these steps:

1. Select a CPU 1217C from the hardware catalog as a potential DP master.
2. Drag the CPU onto the free area within the network view.
3. Select the communications module CM 1243‑5 from the hardware catalog.
4. Drag the communications module to the CPU in the network view.
5. Right-click on the DP interface of the communications module.
6. Select "Create master system" from the shortcut menu.

A DP master system with a CPU 1217C is created as the only node via the CM 1243‑5 as DP master.

If you connect the DP interface of a DP slave to the DP interface of the DP master, the DP slave will be added automatically to the DP master system. If there is not yet a subnet between the DP master and DP slave, a new subnet is created between the DP master and DP slave.

To include, for example, a CPU 1217C with communications module CM 1242‑5 as an intelligent DP slave in the DP master system, follow the steps below:

1. Click on the DP interface of the DP master (interface of the CM 1243‑5) or DP slave (interface of the CM 1242‑5).
2. Hold down the mouse button and draw a connecting line between this DP interface and that of the desired communication partner.

or

1. Click on the hyperlink of the DP slave CPU 1217C with CM 1242‑5.
2. Select the required DP master from the list of possible DP masters displayed.

The intelligent DP slave CPU 1217C with CM 1242‑5 is included in the DP master system as DP master with CPU 1217C and CM 1243‑5 .

![Procedure](images/78499389835_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drag between the DP interfaces of DP slave to DP master. |
| ② | Click on the link of an unassigned DP slave, and a selection of possible DP masters opens. |

If necessary, adapt the properties of the PROFIBUS subnet or of the DP master (e.g. PROFIBUS address) in the Inspector window under "Properties".

###### DP master display on the DP slave

When a DP slave is connected to a DP master, the name of the DP master is displayed on the DP slave as a hyperlink. Click the hyperlink to select the associated DP master.

![DP master display on the DP slave](images/78499394315_DV_resource.Stream@PNG-de-DE.png)

###### Highlighting applied to the DP master system

When you create a new DP master system, highlighting will be applied to it. This enables you to identify quickly which devices belong to the DP master system. You can also highlight a DP master system yourself by moving the mouse pointer over a subnet. This will result in the names of the available DP master systems being displayed. Click the required DP master system to highlight it.

![Highlighting applied to the DP master system](images/78499398667_DV_resource.Stream@PNG-en-US.png)

There are various ways of removing the highlighting from a DP master system:

- Highlight a different DP master system.
- Click on the pin with the name of the DP master system in the top right-hand corner of the network view.

##### Editing DP master systems and interfaces (S7-1200)

###### Introduction

Once you have created a DP master system, you also have the option of disconnecting the DP master system from its components. This can result in subnets with DP slaves but without DP master.

Generally, there is no need to edit the interfaces of a DP master.

You can change the name and number on the DP master system.

###### Disconnection of master or slaves from the DP master system

If you have configured a PROFIBUS CP as a DP master with master system, you can then disconnect the DP master system from the DP master. After this, the device will no longer be connected to the DP master system.

Disconnecting the subnet from a DP master effectively eliminates the master system in the sense that it is no longer assigned to a DP master. However, the individual DP slaves are still interconnected via the subnet.

If you delete the DP slaves or disconnect them from the master system, the master system is then retained on the DP master.

###### Requirement

- You must be in the network view.
- There has to be a DP master system with one DP master and at least one DP slave.

###### Disconnecting the DP master from the DP master system

To disconnect the DP master system, proceed as follows:

1. Right-click on the DP master's DP interface.
2. Select "Disconnect from master system" from the shortcut menu.

The selected DP master will be disconnected from the DP master system. A subnet with the DP slaves will be retained.

###### Adding a DP master to the DP master system

To reassign a DP master to a subnet, proceed as follows:

1. Right-click on the DP master's DP interface.
2. Select "Create master system" from the shortcut menu.
3. Draw connecting lines between the new DP master system and the DP interfaces of the DP slaves.

The DP master combines with the DP slaves to recreate a DP master system.

###### Editing the properties of a DP master system

To edit the properties of a DP master system, proceed as follows:

1. Move the mouse pointer over a subnet with a DP master system.
2. A message will appear displaying the available DP master systems. Click the one you want to edit. The DP master system will now be color-highlighted.
3. Click on the highlighted DP master system.
4. In the inspector window, edit the DP master system attributes under "Properties &gt; General".

**Note**

If you click a subnet when no DP master system is highlighted, you will be able to edit the properties of the entire subnet under "Properties" in the inspector window.

##### Adding DP slaves to the master system and configuring them (S7-1200)

In the network view, you can add various DP slaves from the hardware catalog directly by using the drag-and-drop function or by double-clicking.

###### Types of DP slaves

For configuration purposes, DP slaves are broken down into the following categories:

- Compact DP slaves  
  (Modules with integrated digital/analog inputs and outputs, for example, ET 200L)
- Modular DP slaves  
  (interface modules with S5 or S7 modules assigned, for example ET 200M)
- Intelligent DP slaves (I-slaves)  
  (SIMATIC S7-300 with, for example, CP 342-5, CPU 315-2 DP, or ET 200S with IM 151-7 CPU)

###### Slot rules

- Your DP master system should only contain one DP master, but it may contain one or or more DP slaves.
- You may only configure as many DP slaves in a DP master system as are permitted for the specific DP master.

  > **Note**
  >
  > When configuring the DP master system, remember to observe the DP master technical data (max. number of nodes, max. number of slots, max. quantity of user data). User data restrictions may possibly prevent you from being able to use the maximum number of nodes that is theoretically possible.

###### Requirements

- You are in the network view.
- A DP master system must have been created.

###### Adding a DP slave to the DP master system

To add a DP slave from the hardware catalog to the DP master system, follow these steps:

1. Select a DP slave from the hardware catalog.
2. Drag-and-drop the DP slave from the hardware catalog into the network view.
3. Draw a connecting line between the DP master's DP interface or a highlighted DP master system and the DP interface of the new DP slave.

A DP master system will be created and the DP slave will be connected to the DP master automatically.

> **Note**
>
> When a DP master system is highlighted, you can double-click the required DP slave in the hardware catalog. This will result in the DP slave being added to the highlighted DP master system automatically.

###### Disconnecting a DP slave from the DP master system

To disconnect a DP slave from the DP master system, follow these steps:

1. In the network view, right-click on the DP slave's DP interface.
2. From the shortcut menu, select the method for disconnecting from the DP master system:

   - "Disconnect from subnet": The PROFIBUS connection is broken and the device is no longer connected to the DP master system or a subnet.
   - "Disconnect from master system": The DP slave remains connected to the subnet, but is no longer assigned to the DP master system as a DP slave.

The selected DP slave will be disconnected from the DP master system.

You can also disconnect directly using the shortcut menu of the DP slave:

1. In the network view, right-click on the DP slave.
2. Select "Disconnect from DP master/IO system" from the shortcut menu.

The DP slave remains connected to the subnet, but is no longer assigned to the DP master system as a DP slave.

###### Assigning a DP slave to a new DP master system

To assign an existing DP slave to a new DP master system, follow these steps:

1. Right-click on the DP slave's DP interface.
2. From the shortcut menu, select "Assign to new master".

   It does not matter whether the DP slave concerned is already assigned to another DP master system.
3. From the selection list, select the DP master with the DP master system to which you want to connect the DP slave.

   The selected DP slave is now assigned to a new DP master system.

The "Assign to new subnet" function works in a similar way in that it allows you to connect a DP slave to a new subnet. However, in this case, the DP slave will not be connected to an existing DP master system.

You can also make the assignment directly using the shortcut menu of the DP slave:

1. Right-click the DP slave.
2. From the shortcut menu, select "Assign new DP master/IO system".
3. Select the DP master from the list of available DP masters.

The selected DP slave has now been assigned to a new DP master system.

> **Note**
>
> If there is only one DP master on a subnet, you only have to connect the interface of the DP slave to the subnet of this DP master with drag-and-drop. The DP slave is then connected to the subnet of the DP master immediately, and the DP slave is assigned to this DP master.

###### Configuring a DP slave

To configure a DP slave, follow these steps:

1. Switch to the DP slave's device view.
2. Select the module you want.
3. Configure the DP slave in the Inspector window.

##### Hint: Quick configuration of master systems (S7-1200)

If the DP master system has several DP slaves, use drag-and-drop operation to assign to the master in one step all DP slaves that were placed.

###### Requirements

DP master and DP slaves are placed in the network view.

###### Assigning DP slaves to a DP master system

To do this, follow these steps:

1. Select an appropriate zoom factor so that you can see as many DP slaves as possible in the network view.
2. Arrange the DP slaves in a maximum of two rows.
3. Select all DP interfaces with the mouse cursor (not all devices!). This only works if you begin to drag the mouse cursor outside of the first DP slave and release the mouse button at the last DP slave (selection with the lasso).

   ![Assigning DP slaves to a DP master system](images/26426488459_DV_resource.Stream@PNG-en-US.png)

   ![Assigning DP slaves to a DP master system](images/26426488459_DV_resource.Stream@PNG-en-US.png)
4. Select the shortcut menu "Assign to new master" and select the corresponding DP interface for the DP master in the subsequent dialog.

   ![Assigning DP slaves to a DP master system](images/26426675723_DV_resource.Stream@PNG-en-US.png)

   ![Assigning DP slaves to a DP master system](images/26426675723_DV_resource.Stream@PNG-en-US.png)
5. The DP slaves are automatically networked with the DP master and combine with it to form a DP master system.

**Note**

When a DP master system is highlighted, you can double-click on a DP slave in the hardware catalog and thereby quickly add additional DP slaves. This will result in the DP slave being added to the highlighted DP master system automatically.

#### Configuring intelligent DP slaves (S7-1200)

This section contains information on the following topics:

- [Adding an I-slave to a DP master system (S7-1200)](#adding-an-i-slave-to-a-dp-master-system-s7-1200)
- [Configuring access to I slave data (S7-1200)](#configuring-access-to-i-slave-data-s7-1200)

##### Adding an I-slave to a DP master system (S7-1200)

###### Introduction

One of the characteristics of an intelligent DP slave (I-slave) is that the DP master is not provided with I/O data directly by a real I/O, but by a preprocessing CPU. Together with the CP, this preprocessing CPU forms the I-slave.

![Introduction](images/41017960459_DV_resource.Stream@PNG-en-US.png)

###### Difference: DP slave v. intelligent DP slave

In the case of a DP slave, the DP master accesses the distributed I/O directly.

In the case of an intelligent DP slave, the DP master actually accesses a transfer area in the I/O address space of the preprocessing CPU instead of accessing the connected I/O of the intelligent DP slave. The user program running on the preprocessing CPU is responsible for ensuring data exchange between the address area and I/O.

> **Note**
>
> The I/O areas configured for data exchange between the DP master and DP slaves must not be used by I/O modules.

###### Applications

Configurations involving intelligent DP slaves: I-slave &lt;&gt; DP master data exchange

###### Procedure

To add an I-slave to a DP master system, follow these steps:

1. In the network view, drag from the hardware catalog to a station one CM 1242-5 as an I-slave and one CM 1243-5 as a DP master.
2. Draw a connecting line between the DP interfaces of both devices.

   This way you connect the I-slave with a DP master in a DP master system.

   Result: You have now set up a DP master system with one DP master and one I-slave.

##### Configuring access to I slave data (S7-1200)

###### Data access

The following applies to the CP 1242-5 in its function as I-slave: The addresses for the data transfer area and the address for the I/O modules in the I-slave differ. This means that the start address occupied by an I/O module can no longer be used for the transfer memory. If the higher-level DP master is to access the data of an I/O module in the I-slave, you must configure this data exchange between the I/O module and transfer area in the I-slave user program.

![Data access](images/41037650955_DV_resource.Stream@PNG-en-US.png)

###### Configuration of the transfer area for the CM 1242-5 (transfer area)

With CM 1242‑5, the transfer area for the cyclic PROFIBUS data exchange is configured as transfer area in the parameter group "PROFIBUS interface &gt; Mode &gt; I Slave Communication".

###### Direct data access from CPU to CPU

Direct data access from CPU to CPU via PROFIBUS is supported by the S7-1200 PROFIBUS CMs only via the PUT/GET services.

#### Configuring DP slaves as distributed I/O devices (S7-1200)

This section contains information on the following topics:

- [Configuring an ET 200S (S7-1200)](#configuring-an-et-200s-s7-1200)
- [Packing addresses (S7-1200)](#packing-addresses-s7-1200)
- [Configuring option handling with standby modules (S7-1200)](#configuring-option-handling-with-standby-modules-s7-1200)
- [Configuring option handling without standby modules (S7-1200)](#configuring-option-handling-without-standby-modules-s7-1200)
- [Configuring the ET 200S in DPV1 mode (S7-1200)](#configuring-the-et-200s-in-dpv1-mode-s7-1200)

##### Configuring an ET 200S (S7-1200)

###### Slot rules for configuring an ET 200S

The following rules apply when configuring an ET 200S:

- Do not leave any gaps when inserting the ET 200S modules.
- Slot 1: only for PM-E or PM-D Power Modules.
- To the left of an Electronics Module (EM): an EM or a Power Module (PM-E or PM-D) only.
- To the left of Motor Starter (MS): an MS, a PM-D, PM-D Fx (1..x..4) Power Module or a PM-X Power Module only.
- To the left of a PM-X: a motor starter or a PM-D only
- Up to 63 modules and one IM Interface Module are permitted

  > **Note**
  >
  > Remember to ensure that the correct PM-E and EM voltage ranges are assigned.

###### Configuring reference junctions

A reference junction is the connection of a thermocouple to a supply line (generally in the terminal box). The voltage that occurs due to the effects of temperature falsifies the temperature value measured by the module.

On the ET 200S, one channel of the AI RTD module can be programmed as a reference junction. Other AI TC modules can correct their measured values using the temperature at the reference junction as measured by this module.

![Configuring reference junctions](images/26467901067_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
|  |  |
| ① | Configuring the AI TC: → Selection of the reference junction used |
| ② | Configuring of the AI RTD:  → Activation of the reference junction → Specifying the slot and channel of the AI RTD |

###### Special characteristics to be noted when assigning parameters for reference junctions

The process of assigning parameters for reference junctions will be explained based on the example of a resistance thermometer with a Pt 100 climatic range that is used for measuring the reference junction temperature.

To assign parameters for the reference junction, follow these steps:

1. In the ET 200S device view, insert an analog electronics module, for example a 2AI RTD HF.
2. Select the module on the rack.
3. Under "Properties &gt; Inputs" in the inspector window, set a channel for the reference junctions function to the "RTD-4L Pt 100 climatic range" measuring range.
4. Select the ET 200S.
5. Under "Properties &gt; Module parameters &gt; Reference junctions" in the inspector window, select the "Reference junction" check box and specify the slot and channel number of the relevant RTD module.
6. Insert the analog electronics module for measuring the temperature using a thermocouple (TC module) and parameterize it with the reference junction number of the RTD module.

###### Additional information

For additional information on the various types and uses of ET 200S modules, please refer to the operating instructions and the manual titled "ET 200S Distributed I/O System".

For additional information on analog value processing, please see the documentation for the ET 200S distributed I/O system.

##### Packing addresses (S7-1200)

###### Introduction

DP slaves and I/O devices from the ET 200S family are configured in the same way as other modular DP slaves and I/O devices. As well as supporting all the standard modular DP slave and I/O device functions, the ET 200S also offers the "Pack addresses" function:

When digital electronics modules requiring an address space of 2 or 4 bits are inserted into the device view, they will initially be spread over a total area of 1 byte. However, the address area actually occupied can be compressed after configuration using the "Pack addresses" function.

|  | Initial state | After "Pack addresses" |
| --- | --- | --- |
| Module | I address | I address |
| 2DI (2-bit) | Byte 10 | 10.0...10.1 |
| 4DI (4-bit) | Byte 11 | 10.2...10.5 |

###### Requirements

- You are in the device view.
- An ET 200S, for example an IM 151-1, must be present.
- A pair of digital electronics modules, for example 2DI AC120V ST, must be inserted into the slots.

###### Packing addresses

To pack addressed, follow these steps:

1. Select the electronics modules whose addresses are to be packed. The following options are available for selecting multiple electronics modules:

   - Press and hold down &lt;Shift&gt; or &lt;Ctrl&gt; while clicking the relevant electronics modules.
   - Click off the rack and select the required electronics modules by drawing round them with the mouse.
2. Click "Pack addresses" in the shortcut menu for the selected electronics modules.

The address areas for inputs, outputs and motor starters are packed separately. The packed addresses will be displayed in the I address and Q address columns of the device overview.

###### How packed addresses are generated and structured

If you make use of the "Pack addresses" function, the addresses of the selected electronics modules will be packed in accordance with the following rules:

- The start of the address area is determined by the lowest address of the selected electronics modules: X.0
- If the bit address is not "0", then the next (free) byte address as of which the selected area can be compacted will be selected automatically: (X+n).0
- If no coherent area exists, the addresses will be automatically packed into any available address gaps.

Electronics modules with packed addresses and the same byte address form a packing group.

###### Unpacking addresses

To unpack addressed, follow these steps:

1. Select one or more electronics modules with packed addresses.
2. Click "Unpack addresses" in the shortcut menu for the selected electronics modules.

The packing groups of the selected electronics modules will be disbanded and the packed addresses for the relevant electronics modules unpacked.

The packing group will also be disbanded and the packed addresses unpacked in the following cases: if you delete electronics modules from a packing group, move electronics modules out of a packing group or insert electronics modules on a free slot within a packing group.

The start addresses of the unpacked electronics modules will be assigned to the next available byte addresses in each case.

###### Special characteristics of electronics modules with packed addresses

The following special characteristics apply to electronics modules with packed addresses:

- As far as the CPU is concerned, there is no way of assigning a slot for the electronics module. Consequently, the instruction GADR_LGC (SFC 5) outputs error information W#16#8099 "Slot not configured" for the actual slot of the electronic module.
- The instruction LGC_GADR (SFC 49) and SZL-ID W#16#xy91 "module status information" cannot be evaluated for an electronics module.
- The electronics module receives an additional diagnostics address via the DPV1 function, because otherwise the packed addresses would prevent interrupts from being assigned as far as the CPU is concerned.
- The "Insert/remove interrupt" is not possible. This is because the "Pack addresses" and "Insert/remove interrupt" functions are mutually exclusive.

##### Configuring option handling with standby modules (S7-1200)

You can use the option handling function to prepare the ET 200S with PROFIBUS interface for future expansions (options). This section describes option handling with standby modules.

You do this by assembling, wiring, configuring, and programming the maximum configuration envisaged for the ET 200S and by using cost-effective standby modules (138-4AA00 or 138-4AA10) during assembly until it becomes time to replace them with the necessary electronics modules.

> **Note**
>
> The ET 200S can be completely factory-wired with the master cabling, as no connection exists between a standby module and the terminals of the terminal module (and, in turn, to the process).

###### Requirement

- ET 200S interface module

  - IM 151-1 STANDARD (6ES7 151-1AA03-0AB0 or higher)
  - IM 151-1 FO STANDARD (6ES7 151-1AB02-0AB0 or higher)
- Power module with option handling

  - PM-E DC24..48V
  - PM-E DC24..48V/AC24..230V

###### Procedure

To activate option handling, follow these steps:

1. Select the IM 151-1 in the device view and enable it in "Option handling" check box under "Properties &gt; General &gt; Option handling" in the inspector window.
2. Select the numbered check boxes for the slots that are initially to accommodate the standby modules prior to the future electronics modules.
3. Select the power module in the device view and enable it in the "Option handling" check box under "Properties &gt; Addresses" in the inspector window. Reserve the necessary address space for the control and check-back interface in the process image output (PIQ) and process image input (PII).

The assembled standby modules can be replaced with the configured modules at a later date without having to modify the configuration.

> **Note**
>
> The addresses for these interfaces are reserved as soon as you activate option handling on the power module. The "Option handling" function must also be activated on the DP slave (IM 151-1 STANDARD Interface Module). If it is not activated, the addresses reserved for the control and check-back interface will be released again.
>
> Note that activating and deactivating the option handling function repeatedly can change the address of the control and check-back interface.
>
> Option handling may be activated for one PM-E DC24..48V or one PM-E DC24..48V/AC24..230V Power Module only.

###### Additional information

For additional information on the assignment and significance of bytes within the process image, option handling with PROFIBUS and the use of standby modules, please refer to the documentation for the ET 200S distributed I/O system.

###### How option handling works during startup

If "Startup when expected/actual config. differ" is not available, the ET 200S will still start up if a standby module is inserted instead of the configured electronics module and option handling has been activated for the slot concerned.

###### How option handling works during operation

During operation, the option handling mode varies in accordance with the following:

- Option handling enabled for a slot:   
  Either the standby module (option) or the configured electronics module can be plugged into this slot. If any other kind of module is present on this slot, diagnostics will be signaled (no module/incorrect module).
- Option handling disabled for a slot:   
  Only the configured electronics module can be plugged into this slot. If any other kind of module is present, diagnostics will be signaled (no module/incorrect module).

###### Standby module substitute values

- Substitute value for digital inputs: 0
- Substitute value for analog inputs: 0x7FFF

###### Control and evaluation in the user program

The ET 200S is equipped with a control and feedback interface for the "Option handling" function.

The control interface is located in the process image output (PIQ). Each bit in this address area controls one of the slots from 2 to 63:

- Bit value = 0: Option handling parameterized. Standby modules are permitted.
- Bit value = 1: Option handling canceled. Standby modules are not permitted on this slot.

The check-back interface is located in the process image input (PII). Each bit in this address area provides information about the modules that are actually plugged into slots 1 to 63:

- Bit value = 0: This slot has the standby module, an incorrect module or no module plugged into it.
- Bit value = 1: The configured module is plugged into this slot.

---

**See also**

[Which modules support option handling?](http://support.automation.siemens.com/WW/view/en/22564754)

##### Configuring option handling without standby modules (S7-1200)

You can use the option handling function to prepare the ET 200S for future expansions (options) without installing standby modules. This section describes option handling without standby modules.

> **Note**
>
> **ET 200S with PROFINET interface**
>
> This description refers to the ET 200S with PROFIBUS interface. In principle, option handling for ET 200S with PROFINET interface functions as described here without standby modules. PN interface modules are to be used instead of the DP interface modules listed here. You can find additional information about option handling for ET 200S with PROFINET interface in the corresponding manuals.

###### Requirement

- ET 200S interface module

  - IM 151-1 HIGH FEATURE (6ES7151-1BA02 or higher)
  - IM 151-1 STANDARD (6ES7 151-1AA05-0AB0 or higher)
- Power module with option handling

  - PM-E DC24..48V
  - PM-E DC24..48V/AC24..230V

###### Procedure

To activate option handling, follow these steps:

1. Select the IM 151-1 in the device view and enable it in "Option handling" check box under "Properties &gt; General &gt; Option handling" in the inspector window.
2. Select the power module in the device view and enable it in the "Option handling" check box under "Properties &gt; Addresses" in the inspector window. Reserve the necessary address space for the control and check-back interface in the process image output (PIQ) and process image input (PII).
3. Configure the slave's maximum configuration. The selection/clearing of options is controlled via the user program.

**Note**

The addresses for these interfaces are reserved as soon as you activate option handling on the power module. The "Option handling" function must also be activated on the DP slave (IM 151-1 interface module). If it is not activated, the addresses reserved for the control and check-back interface will be released again.

Note that activating and deactivating the option handling function repeatedly can change the address of the control and check-back interface.

Option handling may be activated for one PM-E DC24..48V or one PM-E DC24..48V/AC24..230V Power Module only.

###### Additional information

For additional information on the assignment and significance of bytes within the process image, option handling with PROFIBUS and the use of standby modules, please refer to the documentation for the ET 200S distributed I/O system.

###### Control and evaluation in the user program

The ET 200S is equipped with a control and feedback interface for the "Option handling" function.

The control interface is located in the process image output (PIQ). Each bit in this address area controls one of the slots from 1 to 63:

- Bit value = 0: Slot is not available in the actual configuration.
- Bit value = 1: Slot is available in the actual configuration.

The check-back interface is located in the process image input (PII). Each bit in this address area provides information about the modules that are actually plugged into slots 1 to 63:

- Bit value = 0: Slot belongs to an option that is not available or module status is faulty.
- Bit value = 1: The configured module is plugged into this slot.

---

**See also**

[Sample applications for ET 200S, option handling without standby module](http://support.automation.siemens.com/WW/view/en/29430270)

##### Configuring the ET 200S in DPV1 mode (S7-1200)

PROFIBUS DPV1 enables you to access extended PROFIBUS functions.

###### Requirement

- You must be in network view.
- A DP master with DPV1 functionality must be available.
- A master-slave connection must be established with PROFIBUS.

###### Procedure

To switch the DP slave over to DPV1, follow these steps:

1. Select the DP slave.
2. Under "Properties &gt; Module parameters" in the Inspector window, select "DPV1" mode from the "DP interrupt mode" drop-down list.

or

1. Select the DP master.
2. In the I/O communications table, select the row with the connection between the DP master and the desired DP slave.
3. Under "Properties &gt; Module parameters" in the Inspector window, select "DPV1" mode from the "DP interrupt mode" drop-down list.

###### Special characteristics

The parameters are subject to interdependencies, which are outlined below:

| Parameter | DPV0 mode | DPV1 mode |
| --- | --- | --- |
| Operation when target configuration does not match actual configuration | Fully available | Fully available |
| Diagnostics interrupt (OB 82) | Not available, not set | Fully available |
| Hardware interrupt (OB 40 to 47) | Not available, not set | Fully available |
| Insert/remove interrupt (OB 83) | Not available, not set | Only available when addresses are not packed.  "Startup when target configuration does not match actual configuration" is activated automatically along with an insert/remove interrupt. |

###### Interrupts in the case of modules with packed addresses

If the module is capable of triggering interrupts and the bit address is not equal to 0 because of packed addresses, you will need to assign a diagnostics address in the ET 200S address dialog.

The diagnostics address is required for the purpose of assigning a DPV1 interrupt to the module as an interrupt trigger. The CPU will only be able to assign an interrupt correctly and store information on the interrupt in the interrupt OB start information/in the diagnostics buffer if the module concerned has this "unpacked" address. In this context, the CPU cannot make use of "packed" addresses.

From the point of view of interrupt processing (interrupt OB), this means the module will have the assigned diagnostics address, but from the point of view of processing the input and output data in the user program, the module will have the packed addresses.

> **Note**
>
> When the module addresses are packed, the insert/remove interrupt for the ET 200S is unavailable.

#### Using GSD files (S7-1200)

This section contains information on the following topics:

- [GSD revisions (S7-1200)](#gsd-revisions-s7-1200)
- [Installing the GSD file (S7-1200)](#installing-the-gsd-file-s7-1200)
- [Deleting GSD file (S7-1200)](#deleting-gsd-file-s7-1200)
- [Finding unused GSD files (S7-1200)](#finding-unused-gsd-files-s7-1200)
- [Configuring GSD-based DP slave (S7-1200)](#configuring-gsd-based-dp-slave-s7-1200)

##### GSD revisions (S7-1200)

###### What you need to know about GSD revisions

The properties of DP slaves are made available to configuration tools by means of GSD files. Functional enhancements in the area of the distributed I/O will have an effect on the GSD specification, for example, they will require the definition of new keywords. This results in the versioning of the specification. In the case of GSD files, the version of the specification on which a GSD file is based is called a "GSD revision". From GSD revision 1, the GSD revision must be included as a keyword "GSD_revision" in GSD files. GSD files without this keyword will therefore be interpreted by configuration tools as GSD revision "0".

GSD files can be interpreted up to GSD revision 5. This means that DP slaves that support the following functions, for example, will be supported:

- Diagnostic alarms for interrupt blocks
- Isochronous mode and constant bus cycle time
- SYNC/FREEZE
- Clock synchronization for DP slaves

##### Installing the GSD file (S7-1200)

###### Introduction

A GSD file (generic station description file) contains all the DP slave properties. If you want to configure a DP slave that does not appear in the hardware catalog, you must install the GSD file provided by the manufacturer. DP slaves installed via GSD files are displayed in the hardware catalog and can then be selected and configured.

You can also install components for PROFIBUS PA using GSD files.

###### Requirement

- The hardware and network editor is closed.
- You have access to the required GSD files in a directory on the hard disk.

###### Procedure

To install a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD files are stored.
3. Choose one or more files from the list of displayed GSD files.
4. Click on the "Install" button. The selected GSD files are now being installed.
5. To create a log file for the installation, click on the "Save log file" button.

   Any problems during the installation can be tracked down using the log file.
6. Click "Close". You are notified that the DP slaves or potential equalization components from the installed GSD files are entered into the hardware catalog. This process can take a few seconds.

By installing a GSD file, you have added the DP slave or the potential equalization components described in the file to the hardware catalog.

###### Result

You will find the new DP slaves installed by means of GSD files in the hardware catalog under "Additional field devices &gt; PROFIBUS DP". New potential equalization components installed via GSD files can be found there under "Other field devices &gt; PROFIBUS PA".

GSD files are always saved together with the project, which means all information relevant for display of the device (including symbols) is also available in the saved project.

---

**See also**

[Overview of hardware and network editor](#overview-of-hardware-and-network-editor)

##### Deleting GSD file (S7-1200)

###### Introduction

You can delete installed DP slaves using GSD files. These DP slaves are then no longer displayed in the hardware catalog.

###### Requirement

- The hardware and network editor is closed.
- The hardware catalog contains DP slaves installed using GSD files.

###### Procedure

To delete a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD file is stored.
3. Select the file that is to be deleted from the list of displayed GSD files.
4. Click the "Delete" button.

The selected GSD file was deleted and the DP slave is no longer located in the hardware catalog.

##### Finding unused GSD files (S7-1200)

###### Introduction

When you add a GSD-based hardware component to your hardware configuration, different GSD files are added to the project data. If the GSD-based hardware component is once again deleted from the configuration, the GSD files remain in the data inventory of the project. The GSD files are no longer needed in the project if the corresponding GSD-based hardware component is not used in the hardware configuration again. You can find files that are no longer needed in the project with a search function and delete them.

###### Requirement

- A project must be open.
- The project must not be online.
- The project must not be write-protected.

###### Procedure

To find and delete unused GSD files, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. Click on the "Find unused GSDs" button in the "GSDs in the project" tab.
3. If GSD files that are no longer needed were found in the project data, you can now delete them. To do so, click the "Delete" button.

**Note**

Unused GSD files are only available if at least one GSD-based hardware component was added to the configuration and then removed from the configuration. Unused GSD files in the project libraries are included in the search. GSD-based hardware components that are still being used in the configuration are not considered to be unused.

Installed GSD-based hardware components that are included in the hardware catalog but have not been used in the hardware configuration of the project yet, could not have stored unused GSD data in the project.

GSD files that are no longer needed are deleted from the project data. The GSD-based hardware component is still available in the hardware catalog and, if necessary, can be added to the configuration once again. The necessary GSD data are once again copied to the project data in this case.

> **Note**
>
> If you delete a GSD-based hardware component with "Options &gt; Manage general station description files (GSD) &gt; Installed GSDs", it is deleted from the hardware catalog. However, unused GSD files of this hardware component can still be a part of the project data and can be deleted with the function for finding the unused GSD files.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Actions that cannot be undone**  When you delete GSD files that are not being used as an action, the action stack for actions that can be undone is deleted. This means the action of deleting unused GSD files as well as all previous actions can no longer be undone. |  |

---

**See also**

[Basics of undoing and redoing actions](Introduction%20to%20the%20TIA%20Portal.md#basics-of-undoing-and-redoing-actions)

##### Configuring GSD-based DP slave (S7-1200)

DP slaves that you have inserted through installation of a GSD file can be selected as usual via the hardware catalog and inserted in the network view. If you want to insert the modules of the GSD-based DP slaves, you must take into account some particular details.

###### Requirement

- You have installed a DP slave using a GSD file.
- You have inserted the head module in the network view in the usual manner.
- The device overview opens in the device view.
- The hardware catalog is open.

###### Procedure

To add the modules of a GSD-based DP slave, proceed as follows:

1. In the hardware catalog, navigate to the modules of the GSD-based DP slave.

   GSD-based DP slaves, also referred to as DP standard slaves, can be found in the "Other field devices" folder of the hardware catalog.
2. Select the desired module.
3. Use drag-and-drop to move the module to a free space in the device overview.
4. Select the module in the device overview to edit parameters.

You have now inserted the module in a free slot of the GSD-based DP slave and can edit its parameters.

> **Note**
>
> You can see only the GSD-based DP slave in the graphic area of the device view. The added modules of GSD-based DP slaves are only found in the device overview.

###### Preset configuration

For modules with an adjustable preset configuration, you can change this configuration in the inspector window under "Properties &gt; Preset configuration".

### Configuring PROFINET IO

This section contains information on the following topics:

- [What you need to know about PROFINET IO](#what-you-need-to-know-about-profinet-io)
- [Configure PROFINET IO](#configure-profinet-io)
- [Using GSD files](#using-gsd-files)
- [Special PROFINET configurations](Special%20PROFINET%20configurations.md#special-profinet-configurations)

#### What you need to know about PROFINET IO

This section contains information on the following topics:

- [What is PROFINET IO?](#what-is-profinet-io)
- [Overview of RT classes](#overview-of-rt-classes)
- [Which IO controllers and IO devices support which PROFINET functions?](#which-io-controllers-and-io-devices-support-which-profinet-functions)
- [Connecting existing bus systems](#connecting-existing-bus-systems)
- [Configuration with IE/PB LINK](#configuration-with-iepb-link)
- [Configuration using IWLAN/PN link](#configuration-using-iwlanpn-link)

##### What is PROFINET IO?

###### PROFINET IO

PROFINET is an Ethernet-based automation standard of PROFIBUS Nutzerorganisation e.V. (PNO) which defines a manufacturer-neutral communication, automation and engineering model.

###### Objective

The objective of PROFINET is:

- Integrated communication via field bus and Ethernet
- Open, distributed automation
- Use of open standards

###### Architecture

The PROFIBUS User Organisation e.V. (PNO) has designated the following aspects for PROFINET architecture:

- Communication between controllers as components within distributed systems.
- Communication between field devices, such as I/O devices and drives.

###### Implementation by Siemens

The demand for "Communication between controllers as components within distributed systems" is implemented by "Component Based Automation" (CBA). Component Based Automation is used to create a distributed automation solution based on prefabricated components and partial solutions.

The demand for "Communication between field devices" is implemented by Siemens with "PROFINET IO". Just as with PROFIBUS DP, the complete configuration and programming of the components involved is possible using the Totally Integrated Automation Portal.

The following sections deal with the configuration of communication between field devices using PROFINET IO.

##### Overview of RT classes

###### RT classes in PROFINET IO

PROFINET IO is a scalable, real-time communication system based on Ethernet technology. The scalable approach is reflected in several real-time classes:

- **RT:** Transmission of data in prioritized, non-isochronous Ethernet frames. The required bandwidth is within the free bandwidth area for TCP/IP communication.
- **IRT:** Isochronous transmission of data with high stability for time-critical applications (for example, motion control). The required bandwidth is from the area of bandwidth reserved for cyclic data.

Depending on the device, not all real-time classes are supported.

##### Which IO controllers and IO devices support which PROFINET functions?

###### Additional information and overviews

In the following Siemens Industry Online Support [article](http://support.automation.siemens.com/WW/view/en/44383954), you will find an overview of the PROFINET IO controllers and IO devices that support the following PROFINET functions:

- Isochronous real-time communication (IRT)
- Prioritized startup
- Media redundancy (MRP)
- PROFIenergy
- Shared device
- I-device
- Isochronous mode of process data

The functions are explained in the following sections, but without naming the respective hardware that supports these functions.

In the hardware catalog, you can also find an overview of the supported functions in the description below the selected components.

You can also find a description of PROFINET in the respective current STEP 7 version [here](http://support.automation.siemens.com/WW/view/en/49948856).

##### Connecting existing bus systems

###### Connection of PROFINET and PROFIBUS

PROFINET IO and PROFIBUS DP can be connected with each other as follows:

- via Industrial Ethernet:

  To connect the two network types, Industrial Ethernet (plant control level) and PROFIBUS (cell level/field level), use the IE/PB link, for example.
- via Industrial Wireless LAN:

  PROFIBUS devices, for example, can be connected to PROFINET IO via a wireless LAN/PB link. This allows existing PROFIBUS configurations to be integrated into PROFINET.

AS interface devices can be connected by an IE/AS-i link PN IO to the interface of a PROFINET device. This allows the existing AS-i network to be integrated into PROFINET.

The following figure shows the connection of a PROFIBUS subnet via a PROFINET device with proxy functions.

![Connection of PROFINET and PROFIBUS](images/24841072011_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | PROFINET devices |
| ② | PROFINET device with proxy functions (for example, IE/PB link) |
| ③ | PROFIBUS devices |

###### PROFINET device with proxy functions used as proxy for a PROFIBUS device

The PROFINET device with proxy functions is the proxy for a PROFIBUS device on the Ethernet. The proxy functionality enables a PROFIBUS device to communicate with all devices on the PROFINET and not just with its master.

Existing PROFIBUS systems can easily be integrated into PROFINET communication using the proxy functions.

If, for instance, you connect a PROFIBUS device via an IE/PB link to PROFINET, the IE/PB link acts as a proxy for the PROFIBUS components for communicating via PROFINET.

##### Configuration with IE/PB LINK

###### Configuration with IE/PB LINK PN IO / HA

You can use the IE/PB LINK to connect PROFIBUS DP configurations to PROFINET IO.

From the CPU perspective, the PROFIBUS DP slaves are connected to the same network as the IE/PB LINK. These slaves have the same device names and IP addresses as the IE/PB LINK, but different device numbers. Furthermore, each also has a specific PROFIBUS address.

In the properties of the IE/PB LINK, the PROFIBUS addresses of the connected DP slaves are displayed in addition to the PROFINET device numbers, as this device has two addressing schemes.

###### Handling device numbers and PROFIBUS addresses on the master system

During placement, the same number is assigned for the PROFINET device number and the PROFIBUS address.

In the Inspector window under "General Properties &gt; PROFINET device number", you can find an overview of the device numbers used and the PROFIBUS addresses of an IE/PB LINK. The device number can also be changed here. You can also set that the device number and the PROFIBUS address should or should not always be identical. If the "PROFINET device number=PROFIBUS address" option is activated, you do not have to update the device number when the PROFIBUS address changes.

The PROFIBUS address can be changed in the properties of the PROFIBUS device.

###### Restrictions

The following restrictions apply to DP slaves configured as described above on the PROFIBUS subnet of an IE/PB LINK:

- No pluggable IE/PB LINK
- No DP/PA link pluggable
- No pluggable Y link
- Not CiR-compliant
- No pluggable redundant slaves
- No isochronous transmission / constant bus cycle time can be configured
- SYNC/FREEZE instructions ("DPSYC_FR") of a CPU on the Ethernet subnet for DP slaves behind the IE/PB-Link are not supported.

---

**See also**

[Operating modes of the IE/PB LINK](Communications%20modules%20and%20network%20components.md#operating-modes-of-the-iepb-link)
  
[Connect the DP slave via the IE/PB Link to a PROFINET IO system](#connect-the-dp-slave-via-the-iepb-link-to-a-profinet-io-system)

##### Configuration using IWLAN/PN link

###### Maximum number of devices in a IWLAN segment

If an Ethernet subnet is set up as wireless network (IWLAN = Industrial Wireless LAN), cyclic data exchange between IO controllers and IO devices is possible via a wireless route.

On one side of the wireless route there are fixed installed access points (for example, SCALANCE W 788) and on the other side mobile stations (with, for example IWLAN/PB links with PROFIBUS devices).

If the action radius of the mobile stations is large, it may be necessary to install several access points (SCALANCE W 788). Since each access point forms a segment with its wireless range, the IWLAN is made up of a series of segments.

The mobile devices "on the one side" of the wireless link with their IWLAN/PB links can move along the segments.

###### Special feature

If several IWLAN/PB links are located within a segment, they have to share the bandwidth that is available for wireless transmission. This leads to a lengthening of the update time for these devices.

###### Example

In the following example there are two IO devices (IWLAN/PB link) with a segment.

If no more than a maximum of two IWLAN/PB links are present in a IWLAN segment at the same time, enter a "2".

![Example](images/25644520587_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Segment 1 |
| ② | Segment 2 |

#### Configure PROFINET IO

This section contains information on the following topics:

- [Addressing PROFINET devices](#addressing-profinet-devices)
- [Creating a PROFINET IO system](#creating-a-profinet-io-system)
- [Handling PROFINET IO systems](#handling-profinet-io-systems)
- [Configuring an IO device through hardware detection](#configuring-an-io-device-through-hardware-detection)
- [Tip: Quick configuration of IO systems](#tip-quick-configuration-of-io-systems)
- [Interconnecting ports](#interconnecting-ports-1)
- [Setting the send clock](#setting-the-send-clock)
- [Setting the update time](#setting-the-update-time)
- [Setting the watchdog time](#setting-the-watchdog-time)
- [Calculated bandwidth for cyclic IO data](#calculated-bandwidth-for-cyclic-io-data)
- [Setting port options](#setting-port-options)
- [Enabling device replacement without exchangeable medium](#enabling-device-replacement-without-exchangeable-medium)
- [Connect the DP slave via the IE/PB Link to a PROFINET IO system](#connect-the-dp-slave-via-the-iepb-link-to-a-profinet-io-system)
- [Setup recommendations for optimizing PROFINET](#setup-recommendations-for-optimizing-profinet)
- [Limitation of the data infeed into the network](#limitation-of-the-data-infeed-into-the-network)
- [Maintaining communication relations during faults](#maintaining-communication-relations-during-faults)
- [Activating maintenance of the communication relation in the CPU properties](#activating-maintenance-of-the-communication-relation-in-the-cpu-properties)

##### Addressing PROFINET devices

This section contains information on the following topics:

- [Assigning addresses and names to PROFINET devices](#assigning-addresses-and-names-to-profinet-devices)
- [Assigning the device name and IP address](#assigning-the-device-name-and-ip-address)
- [Example of the assignment of the device name](#example-of-the-assignment-of-the-device-name)
- [Assign device name via communication table](#assign-device-name-via-communication-table)
- [Assign device name via memory card](#assign-device-name-via-memory-card)
- [Retentivity of IP address parameters and device names](#retentivity-of-ip-address-parameters-and-device-names)
- [Specifying the router for a PROFINET IO device](#specifying-the-router-for-a-profinet-io-device)

###### Assigning addresses and names to PROFINET devices

In this chapter you will learn which address and naming conventions are valid for the PROFINET devices.

###### IP addresses

All PROFINET devices work with the TCP/IP protocol and therefore require an IP address for Ethernet operation.

You can set the IP addresses in the module properties. If the network is part of an existing company Ethernet network, ask your network administrator for this data.

The IP addresses of the IO devices are assigned automatically, usually at CPU startup. The IP addresses of the IO devices always have the same subnet mask as the IO controller and are assigned in ascending order, starting at the IP address of the IO controller.

###### Device names

Before an IO device can be addressed by an IO controller, it must have a device name. This procedure was chosen for PROFINET because names are easier to administer than complex IP addresses.

Both the IO controller as well as IO devices have a device name. When the "Generate PROFINET device name automatically" option is activated, the device name is automatically derived from the name configured for the device (CPU, CP or IM):

- The PROFINET device name is made up of the name of the device (for example, the CPU), the name of the interface (only with multiple PROFINET interfaces) and optionally the name of the IO system:

  &lt;CPU name&gt;.&lt;Name of the interface&gt;.&lt;IO system name&gt;

  You cannot change this name directly. You change the PROFINET device name indirectly, by changing the name of the affected CPU, CP or IM in the general properties of the module. This PROFINET device name is also displayed, for example, in the list of accessible devices. If you want to set the PROFINET device name independently of the module name, you have to deactivate the "Generate PROFINET device name automatically" option.
- A "converted name" is generated from the PROFINET device name. This is the device name that is actually loaded into the device.

  The PROFINET device name is converted if it does not comply to the rules of IEC 61158-6-10 or if the name begins with numbers (see next section). You cannot change this name directly either.

###### Rules for the converted name

The rules for the converted name are listed in the following section. If the converted name is **not** different from the name of the module, the name of the module must comply with this rule.

- The name consists of one or more labels , which are separated by a dot [.].
- Restricted to a total of 240 characters (lower case letters, numbers, dash, or dot)
- A name component within the device name, which means a character string between two dots, must not exceed 63 characters.
- A name component consists of the characters [a-z, 0-9].
- The device name must not begin or end with the "-" character.
- The device name must not begin with a number.
- The device name form n.n.n.n (n = 0, ... 999) is not permitted.
- The device name must not begin with the string "port-xyz" or "port-xyz-abcde" (a, b, c, d, e, x, y, z = 0, ... 9).

###### Example of device names

device-1.machine-1.plant-1.vendor

If you assign this name to a CPU, for example, STEP 7 will not convert it since it conforms to the rules described above.

###### Device number

In addition to the device name, a device number is also automatically assigned when an IO device is plugged in. You can change this number.

###### Devices in the PROFINET subnet

In a PROFINET subnet the maximum allowable number of devices is monitored during configuration.

---

**See also**

[Assigning the device name and IP address](#assigning-the-device-name-and-ip-address)
  
[Retentivity of IP address parameters and device names](#retentivity-of-ip-address-parameters-and-device-names)
  
[FAQ: What rules apply to PROFINET device names?](https://support.industry.siemens.com/cs/ww/en/view/109479552)

###### Assigning the device name and IP address

###### Assigning an IP address and subnet mask for an IO controller the first time

There are various options for this.

During parameter assignment of the PROFINET interface you must specify if the IP address is set in the project (which means in the hardware configuration) or if the IP address is to be set on the device.

| Assignment of an IP address | Comments |
| --- | --- |
| Option "IP address is set in the project":  The IO controller receives the IP address by loading the hardware configuration, for example, via one of the PROFINET interfaces, by means of the PROFIBUS interface or via the MPI interface. | When the hardware configuration is loaded to the IO controller (e.g. CPU), the IP address and the device name, if set, are also loaded.   Example PROFINET interface:   | Symbol | Meaning | | --- | --- | | 1. Connect your programming device/PC to the same network as the relevant PROFINET device. The interface of the PG/PC must be set to TCP/IP (Auto) mode. 2. Have a list of accessible devices displayed. 3. Select the target device by using its MAC address and load the hardware configuration including the configured IP address (IP address is then saved retentively). |  |   If your PROFINET device has an MPI or PROFIBUS DP interface, connect your programming device/PC directly to the PROFINET device via the MPI or PROFIBUS DP interface. The configured IP address is applied when the hardware configuration is loaded. |
| Option "IP address is set directly at the device":  - Assign online - Assignment by user program (instruction IP_CONFIG for S7-300/400, T_CONFIG for S7-1200/1500) - Assign via CPU display (S7-1500) - Higher-level IO controller makes assignment (only with I-devices) | If you have selected this option in the properties of the PROFINET interface, the IP address can be assigned by the online and diagnostics editor using the SINEC PNI Basic software (Primary Network Initialization) or the user program ("IP_CONFIG" instruction).   This option is set automatically if the option "Multiple use IO system" has been enabled in the properties of the PROFINET IO system (standard machine project).  In case of an S7-1200-CPU, make sure that access to the CPU is not protected by a password. If the CPU is write-protected, no IP address and no device name can be assigned directly on the device. |

###### Commissioning a PROFINET interface

Further details of how to commission a PROFINET interface can also be found in the operating instructions for the PROFINET devices of the SIMATIC family.

###### Assignment of device name for IO devices when the "Support device replacement without exchangeable medium" option is selected

For IO controllers with the "Support device replacement without exchangeable medium" option selected, you do not have to assign device names to the IO devices locally, for example in the event of device replacement. Another application is automatic commissioning, in which the CPU automatically assigns the device name and IP address parameters to the IO devices during startup.

Requirement: The ports of the devices are interconnected, and the devices involved support LLDP. The devices have been put into the delivery state or – for S7-1500 CPUs version V1.5 and higher – the "Permit overwriting of device names of all assigned IO devices" option is selected for the IO controller ("Advanced options &gt; Interface options" area of the properties of the PROFINET interface).

###### Assignment of device name and address for an IO device

The following graphic illustrates the process for assigning the device name and address. This process does not apply when the "Support device replacement without exchangeable medium" option is selected.

![Assignment of device name and address for an IO device](images/96428505483_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Each device receives a name; STEP 7 automatically assigns an IP address. |
| ② | From the name, STEP 7 generates a PROFINET device name that you assign to an IO device online (MAC address) and that is written to the device. |
| ③ | You load the configuration to the IO controller. |
| ④ | The IO controller assigns the appropriate IP address to the IO device with the assigned PROFINET device name during startup. |

###### Changing the device name and IP address

You can change the name and IP address manually. The device name must first be changed in the configuration in order to subsequently assign it to the IO device via the memory card or online with programming device/PC.

Offline with memory card:

1. Place the configured data (device name: for example, turbo-3) for the IO device on the MMC in the PG/PC. Use the command "SIMATIC Card Reader &gt; Save Device Name to Memory Card" in the "Project" menu for this.
2. Then insert the MMC into the IO device. The IO device automatically adopts the configured device name.

Online with programming device/PC:

1. Connect the programming device/PC directly to the Ethernet subnetwork via the PROFINET interface.
2. In the network view, select the subnet or I/O device, and click the "Assign device name" command:

   - Either in the shortcut menu of the selected subnet / I/O device or
   - in the menu bar of the graphic view on the corresponding button.
3. In the "Assign PROFINET device name" dialog box, select the suitable PG/PC interface to connect to the Ethernet subnet. All configured PROFINET device names are in the top drop-down list. Select a PROFINET device name from it and select the IO device to receive this device name from the table at the bottom. You can filter the display of devices in the table according to various criteria.
4. You can easily identify the device using the "Flash LED" button.
5. Click "Assign name".

The IO controller recognizes the IO device by its device name and automatically assigns the configured IP address to it.

###### IP address assignment for special IO devices

Special IO devices, for example, SCALANCE X, S7-300 CPs, support the option of assigning the IP addresses not from the IO controller during startup. In this case, the IP address is assigned in a different way. The option is called "IP address is set directly at the device". For additional information, refer to the manual of the respective PROFINET device of the SIMATIC device family.

Another special case is the option "IP address is set directly at the device" in the "IP protocol" area of the Ethernet address properties of an IO device. This option is set automatically when the option "Multiple use IO system" is selected for a standard machine project in the associated PROFINET IO system. In this case, an adapted IP address is not assigned by the IO controller until the IO controller itself has received a local IP address.

###### Requirement for additional procedures when assigning IP address and device name

If the IO device, as described above, should not obtain the IP address or device name from the IO controller, proceed as follows:

1. Select device or network view.
2. Open the properties of the respective PROFINET device and select the area "PROFINET interface [X1]" &gt; "Ethernet addresses".
3. Select the option "IP address is set directly at the device" under "IP protocol" or the option "PROFINET device name is set directly at the device" under "PROFINET".

###### Rules

If the "IP address/device name is set directly at the device" option is used for a PROFINET device, note the following:

- The subnet part of the IP address of the IO device must match the subnet part of the IP address of the IO controller.
- The corresponding PROFINET device cannot be used as a gateway.

---

**See also**

[Assigning a name in the online and diagnostics view opened via "Accessible devices"](Device%20and%20network%20diagnostics.md#assigning-a-name-in-the-online-and-diagnostics-view-opened-via-accessible-devices)
  
[Enabling device replacement without exchangeable medium](#enabling-device-replacement-without-exchangeable-medium)

###### Example of the assignment of the device name

In this example you assign device names to a PROFINET IO controller and a PROFINET IO device. To make assignment easier, the device names should also contain the names of the PROFINET IO system.

###### Requirement

- You must be in the network view.
- A CPU 1214C (V2.0 or higher) must be available in the network view.
- An interface module IM 151-3PN exists.
- The PROFINET interfaces of both modules are networked.

###### Procedure

To assign the names, follow these steps:

1. Select the CPU.

   Make sure that you have selected only the CPU and not the complete device!
2. Assign the name "myController" in the Inspector window, under "General".

   ![Procedure](images/25707542795_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25707542795_DV_resource.Stream@PNG-en-US.png)
3. Select the interface module.

   Ensure that you have selected only the interface module and not the complete ET 200S device.
4. Assign the name "Device_1" in the Inspector window, under "General".
5. Right-click on the PROFINET IO system and select the "Properties" command.
6. Assign the name "Plant_section1" to the IO system and select the check box "Use name as extension for PROFINET device names".

   ![Procedure](images/96430140683_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/96430140683_DV_resource.Stream@PNG-en-US.png)
7. You can find the automatically generated PROFINET device names at the selected device in the Inspector window, at "PROFINET interface".

   ![Procedure](images/44412809099_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/44412809099_DV_resource.Stream@PNG-en-US.png)

   The PROFINET device name corresponds to the name of the module (with the name of the IO system as extension) with the difference that only lower case text is used. Background: No distinction is made between upper and lower case ("case insensitive") for the storing of the name.

   If you want to specify the device name independently of the module name, you have to deactivate the "Generate PROFINET device name automatically" option. The PROFINET device name can be edited in this case.

   The converted name is displayed below. This is the name that is automatically generated from the PROFINET device name and satisfies the DNS conventions. If you work with STEP 7, you do not require this name. This name is displayed here as a check and corresponds to the name that is stored in the device. If you work with other tools that are able to record the data exchange and read the actual device names, then you find the converted names.

###### Other special features

For PROFINET devices with multiple PROFINET interfaces, the name of the interface is attached to the name of the module, separated by a dot.

Example:

- Name of the module: myController
- Name of the interface: Interface_1
- PROFINET device name: mycontroller.interface_1

###### Assign device name via communication table

###### Introduction

You can assign the device names of PROFINET IO devices configured offline to the devices online. You can do this in the table area of the network view in the table "I/O communication". You can also assign the device names to several devices at the same time.

###### "Online assignment" tab

In the I/O communication table, you will find the tabs "Offline configuration" and "Online assignment". In the "Online assignment" tab, you can assign the PROFINET device names that were assigned offline to the corresponding IO devices online. To do this, use the buttons "Check devices" and "Assign now".

The objects displayed in the table of the "Online assignment" tab depend on the setting of the filter function. If only selected objects should be displayed, only objects of the corresponding context are displayed depending on the selection in the network view.

- PROFINET subnet: All connected devices and their PROFINET interfaces
- IO system All devices involved and their PROFINET interfaces
- Sync domain: All devices involved and their PROFINET interfaces
- Devices: The device and any existing PROFINET interfaces
- Other subnets or interfaces such as MPI or PROFIBUS are not displayed

If the display is set for all devices using the filter function, all devices are displayed that have a PROFINET interface, regardless of whether they are connected via a PROFINET subnet or are part of an IO system. Devices without a PROFINET interface, for example only with a DP or MPI interface, are not displayed.

###### General procedure

To assign PROFINET device names, you must first detect the IO devices available online. With this procedure, it matters whether the MAC addresses are known or unknown. This results in a general procedure in two steps:

1. Detecting the IO devices available online
2. Assigning configured PROFINET device names to the IO devices available online

###### Requirements

- You are in the network view.
- There is an online connection to the devices.

###### Procedure (step 1)

To detect IO devices available online from the I/O communication table, follow these steps:

1. Optional: Entered known MAC addresses in the "MAC address" column. After every valid entry, the check box under "Assign device" is selected for the relevant row.
2. Click "Check devices" to start the check of the IO devices available online.
3. Set the PG/PC interface in the dialog window and click "Start".

**Note**

You can enter, insert or import the MAC address in different formats. The correct format is automatically entered in the cell. The following entries are supported and then converted to the required format:

- "08:00:06:BA:1F:20"
- "08 00 06 BA 1F 20"
- "080006BA1F20"

The formats used in the example are automatically converted to "08-00-06-BA-1F-20".

###### Intermediate result

After the check, the result is displayed for every device in the table. Online data found is automatically entered in the table and the check box "Assign device" is set to "checked" in the rows in which a MAC address was entered or found online. The result of the check is shown as an icon in the "Status" column.

| Status | Meaning |
| --- | --- |
| ![Intermediate result](images/83326495755_DV_resource.Stream@PNG-de-DE.png) | Agreement: Matching device and compatible type. The PROFINET device name and the device type of the device found online matches the device in the project. No action is required. |
| ![Intermediate result](images/83326535179_DV_resource.Stream@PNG-de-DE.png) | Ready for assignment: The device type of the device found online matches the device in the project. With a known MAC address the device is ready for the assignment of the PROFINET device name. |
| ![Intermediate result](images/83326481931_DV_resource.Stream@PNG-de-DE.png) | Different device type: A matching device was found online, but the device type does not match the device type in the project. Please select a device with a matching device type online. |
| ![Intermediate result](images/83326509067_DV_resource.Stream@PNG-de-DE.png) | Different device: No device could be found online that uniquely matches the device in the project. Please select a matching device manually. |
| ![Intermediate result](images/83326522123_DV_resource.Stream@PNG-de-DE.png) | Device cannot be accessed: With a known MAC address the device cannot be accessed online. Please check the connection to the device. |

> **Note**
>
> The icon "Ready for assignment" appears when a MAC address exists and matching device data was found, but no PROFINET device name was found online.

You can update the data of the detected devices again via their MAC addresses at any time. To do this, you specify the MAC address and the status of the device is displayed immediately without having to re-detect the device.

###### Procedure (step 2)

All PROFINET device names configured offline will be assigned to the devices available online in a bulk operation.

1. Click the "Assign now" button.
2. Click "Start" in the dialog window to start the assignment of the PROFINET device names.

**Note**

The bulk operation cannot be reversed. A message to this effect appears in a dialog window.

###### Result

The PROFINET device names configured offline will be assigned to the devices available online. This relates to devices in whose row the check box under "Assign device" is selected, that have a MAC address and have the status "Ready for assignment".

###### Importing and exporting data

Using the import and export button, you can import or export the data of the I/O communication table for the online assignment:

- When you export, the PROFINET device names and the MAC address of the table are exported to a CSV file. Using the filter function of the table, you can select which data will be exported.
- When you import, the data of the CSV file is written to the table. If there are conflicts with values already existing in the table, you can decide whether the data should be overwritten or whether the import needs to be stopped.

###### Assign device name via memory card

###### Introduction

You can configure the device names of PROFINET IO devices offline. To do this, store a configured device name on a memory card and then insert the card into the appropriate IO device.

If an IO device has to be completely replaced due to a device defect, the IO controller automatically reconfigures the new device. Using the memory card, a device can be replaced without a programming device.

###### Requirements

- The programming device has a card reader for memory cards.
- The IO device must support the assignment of the device name via memory card.
- The station and its PROFINET IO system is configured.

###### Procedure

To store a device name on a memory card, follow these steps:

1. Insert the memory card into the card reader.
2. Select the IO device whose device name is to be assigned by the memory card.
3. Select the "Card reader &gt; Save Device Name to Memory Card" command in the "Project" menu.

   If the memory card is not empty, a message will be issued informing you of this and you will have the option to delete the card.

###### Retentivity of IP address parameters and device names

The retentivity of IP address parameters (IP address, subnet mask, router setting) and device name depends on how the address is assigned.

The non-retentive, temporary assignment means:

- IP address parameters and device name remain valid for the following time period:

  - Until the next POWER OFF
  - Until the next memory reset
  - Until termination of the online connection (for example, after loading the program)

    After POWER OFF / POWER ON or a memory reset, the CPU can only be accessed via the MAC address.

If the IP address parameters are not retentive, communication based on the IP protocol can no longer take place after the above described events (for example, after POWER OFF/POWER ON).

The assignment of a temporary IP address also deletes retentively saved IP address parameters.

###### Assigning IP address parameters and device name non-retentively

IP address parameters and device name are not retentive in the following cases:

- A temporary IP address that is not retentive is implicitly assigned with the "Accessible devices" function, if the device (e.g. CPU) does not yet have an IP address.
- The device is a "normal" IO controller (i.e., not an I-device), and it is specified in the user program ("IP_Conf" instruction) that the IP address parameters/device name are not to be retentive.

###### Assigning IP address parameters and device name retentively

IP address parameters and device name are retentive in the following cases:

- In the properties of the PROFINET interface, it is specified that the IP address parameters are set in the project ("Set IP address in the project" option).
- In the properties of the PROFINET interface, it is specified that the IP address is to be set on the device.

  - Once the configuration is loaded, the IP address parameters and the device name are assigned via STEP 7 (STEP 7: online and diagnostic function "Assign IP address"). The assigned IP address parameters are retentive.
  - The device is a "normal" IO controller (i.e., not an I-device), and it is specified in the user program ("IP_Conf" instruction) that the IP address parameters/device name are to be retentive.

###### Special features of the I-device

In the properties of the PROFINET interface of the I-device, it is specified that the IP address parameters are to be set on the device. The IP address parameters for the I-device are assigned by the higher-level IO controller.

- If prioritized startup is set, the IP address parameters are retentive.
- If **no** prioritized startup is set, the IP address parameters are not retentive.

###### Recommendation

If possible, use the "Set IP address in project" option and specify an appropriate IP address. In this case, the IP address is assigned retentively.

###### Resetting of retentive IP address parameters and device names

Retentive IP address parameters and device names are reset via the online and diagnostic function "Reset to factory settings".

> **Note**
>
> **Consequences of reassignment of IP address parameters on top of existing IP parameters**
>
> - The temporary assignment of IP address parameters/device names results in a reset of any retentively saved IP address parameters/device names.
> - With a fixed assignment of IP address parameters/device names, previously retentively-saved parameters are replaced by the newly assigned parameters.

> **Note**
>
> **Reuse of devices**
>
> Execute the "Reset to factory settings" before you install a device with retentive IP address parameters and device name in another subnet or system or before you place it in storage.

###### Specifying the router for a PROFINET IO device

###### Introduction

You always require a router (also referred to as a "Standard Gateway") when the PROFINET device has to communicate with a node whose IP addresses lie outside the own IP subnet. If the PROFINET device sends an IP packet to an IP address outside its own IP subnet, the IP packet first goes to the configured router. The router in turn checks the IP address. If this lies outside its own subnet, the router passes the IP packet on to the next router. The IP packet is routed to the next router until it has reached the target address.

Like all S7-1500 CPUs, S7-1500 CPUs with several PROFINET interfaces provide the possibility to configure the IP address of a router. However, there is the restriction that you can only enter the IP address of a router at a PROFINET interface.

You cannot include an IP address of a router on the other PROFINET interfaces of the CPU. IO devices that are connected to this PROFINET interface adopt this setting. Up to and including STEP 7 V14 SP1, these IO devices did not have any possibility to reach devices in a different IP subnet.

As of STEP 7 V15, you have the possibility to assign the address of a router for an IO device independent of the setting of the IO controller. You can now, for example, set a router address at the IO device in the following cases as well:

- You have not set an IP address of a router for the interface of the associated IO controller.
- You have already set a router address for a different interface in the CPU.

  ![Specifying the router for an IO device](images/103644194571_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Router R1 configured at PROFINET X1 |
  | ② | If a router is configured at X1, you cannot configure a router at X2. |
  | ③ | Because a router is configured at X1, the IO device adopts the IP address of the router R1. The IO device can be reached from a different IP subnet. |
  | ④ | As of STEP 7 V15, you set the IP address of the router R2 at the IO device irrespective of the setting at the interface X2. The IO device can be reached from a different IP subnet. |

  Specifying the router for an IO device

###### Further information about the "User router" setting

You have the possibility to configure the use of a router including IP address of the router in the "IP protocol" section of the settings for the PROFINET interface (Ethernet addresses).

**Rules**

Observe the following rules if you want to configure a router for the PROFINET interface of an IO controller:

- A PROFINET IO device supports exactly one router, irrespective of the number of interfaces.
- You can configure a router for exactly one PROFINET interface. All IO devices that are assigned to the PROFINET interface adopt the configured router from the IO controller.
- You cannot configure a router for the further PROFINET interfaces of the CPU. The further PROFINET interfaces take on the IP address "0.0.0.0" as the router and pass it on to their IO devices.

As of STEP 7 V15, you can configure the use of a router for an IO device. This allows the IO device to communicate with a node outside its own IP subnet, irrespective of the setting of the PROFINET interface of the IO controller.

###### Configuration example: Configuring a router for an IO device

The following example shows a configuration in which you configure a router at the IO device so that the IO device reaches IP addresses in the higher-level network.

![Configuration example: Configuring a router for an IO device](images/103644143243_DV_resource.Stream@PNG-en-US.png)

Configuration example: Configuring a router for an IO device

You have a CPU 1516‑3PN/DP. The two PROFINET interfaces X1 and X2 of the CPU work in the "IO controller" operating mode. The PROFINET interface X1 is connected with the subnet "Production line 1". PROFINET interface X2 is connected with the subnet "Production line 2". The two subnets "Production line 1" and "Production line 2" are each connected via a router with the higher-level network "Superior line".

For PROFINET X1, you configure the router "Router 1" with the IP address 192.168.1.100.

The IO device (ET 200SP) in the "Production line 1" subnet adopts the router from the IO controller.

You cannot configure a router for the PROFINET interface X2 because you have already configured a router for the PROFINET interface X1 of the CPU.

No router is transferred by the PROFINET interface X2 to the IO device in the subnet "Production line 2".

In order for the IO device in the subnet "Production line 2" to reach nodes in the higher-level "Superior line", configure the router "Router 2" with the IP address 192.168.2.100 for the IO device.

###### Configuring the router for the IO controller

Requirements: You use the "Set IP address in the project" option for the PROFINET interface.

Follow these steps to configure a router for the IO controller in STEP 7:

1. In the network view of STEP 7, select the PROFINET interface of the IO controller.
2. In the Inspector window, navigate to "Properties" &gt; "General" &gt; "Ethernet addresses".
3. Select the "Use router" check box in the "IP protocol" field.
4. Enter the IP address of the router at "Router address".

###### Configuring a router for an IO device

Requirements:

- STEP 7 as of V15
- CPU 1500 as of firmware version V2.5
- IO device is assigned to the PROFINET interface of an IO controller. The PROFINET interface of the IO controller uses the "Set IP address in the project" option.

Follow these steps to configure a router for the IO device in STEP 7:

1. In the network view of STEP 7, select the PROFINET interface of the IO device.
2. In the Inspector window, navigate to "Properties" &gt; "General" &gt; "Ethernet addresses".
3. Clear the "Synchronize router settings with IO controller" check box.
4. Select the "Use router" check box.
5. Enter the IP address of the router at "Router address".

---

**See also**

[Creating IO devices for R/H systems (S7-1500)](Principle%20of%20operation%20for%20S7-1500R-H%20CPUs%20%28S7-1500%29.md#creating-io-devices-for-rh-systems-s7-1500)

##### Creating a PROFINET IO system

###### Introduction

To create a PROFINET IO system, you need to have a PROFINET IO controller and at least one PROFINET IO device. As soon as you connect an IO controller to an IO device via their PROFINET interfaces, a controller-device link is established.

###### IO controller and IO device

As IO controller, you can use the following devices with a PROFINET interface:

- CPU with a permanently integrated or plug-in PROFINET interface
- CP in conjunction with a CPU
- Interface module assigned to a CPU/FM
- Interface module with a PROFINET interface

As IO device, you can use head modules of the distributed I/O with PROFINET interface or CPUs as intelligent IO devices.

With some devices, you can switch between modes (such as "IO controller" and "IO device") under "Mode" in the Inspector window of the PROFINET interface. Select the option button with the required mode.

###### Requirements

- You are in the network view.
- The hardware catalog is open.

###### Procedure

To create a PROFINET IO system, for example with a CPU 1217C , follow these steps:

1. Select a CPU 1217C as a potential IO controller from the hardware catalog.
2. Drag the CPU onto the free area within the network view.
3. Right-click on the PROFINET interface of the CPU.
4. Select "Create IO system" from the shortcut menu.

A PROFINET IO system with a CPU 1217C as IO controller will be created as the only node.

If you connect the PROFINET interface of an IO device to the PROFINET interface of the IO controller, the IO slave will be added automatically to the IO system. If there is not yet a subnet between the IO controller and IO device, a new subnet is created between the IO controller and IO device.

To include a CPU 1217C as intelligent IO device in the IO system, for example, follow the steps below:

1. Click on the PROFINET interface of the IO controller or IO device.
2. Hold down the mouse button and drag a connection from the selected PROFINET interface to the PROFINET interface of the desired communications partner.

or

1. Click on the hyperlink of the IO device CPU 1217C.
2. Select the required IO controller from the displayed list of possible IO controllers.

The intelligent IO device CPU 1217C is included in the PROFINET IO system with the CPU 1217C as IO controller.

![Procedure](images/78502415755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drag between the PROFINET interfaces of IO device to IO controller. |
| ② | Click on the link of an unassigned IO device, and a selection of possible IO controller opens. |

If required, adapt the properties of the Ethernet subnet or the IO controller (for example, IP address) under "Properties" in the inspector window.

> **Note**
>
> If there is only one IO controller on a subnet, you only have to connect the interface of the IO device to the subnet of this IO controller with drag-and-drop. The IO device is then connected to the subnet of the IO controller immediately, and the IO device is assigned to this IO controller.

###### Display of the IO controller in the IO device

When an IO device is connected to an IO controller, the name of the IO controller is displayed on the IO device as a hyperlink. Click the hyperlink to select the assigned IO controller.

![Display of the IO controller in the IO device](images/78502481291_DV_resource.Stream@PNG-de-DE.png)

###### Highlighting the PROFINET IO system

When you have created a new PROFINET IO system, the PROFINET IO system will be highlighted. This enables you to identify quickly which devices belong to the PROFINET IO system. You can also highlight a PROFINET IO system yourself by moving the mouse pointer over a subnet. This will result in the names of the available PROFINET IO systems being displayed. If you click on one of the displayed PROFINET IO systems with the mouse, the corresponding PROFINET IO system is highlighted.

![Highlighting the PROFINET IO system](images/78502467723_DV_resource.Stream@PNG-en-US.png)

There are various ways of removing the highlighting from a PROFINET IO system:

- Highlight a different PROFINET IO system.
- Click on the pin with the name of the PROFINET IO system in the top right-hand corner of the network view.

##### Handling PROFINET IO systems

Using shortcut menu commands, you can delete PROFINET IO systems, create new ones or even connect the interface to another subnet from within the network view.

An existing PROFINET configuration can thereby be corrected in the network view.

###### Create new PROFINET IO system for IO controller

To create a new PROFINET IO for an IO controller, proceed as follows:

1. Make sure that no IO system is already assigned to the IO controller. If an IO system is already assigned to the IO controller, the "Assign IO system" shortcut menu command is disabled.
2. Select the PROFINET interface and then select the "Assign IO system" shortcut menu command.

A new PROFINET IO system is created at the IO controller and you can assign IO devices to this IO system.

###### Disconnecting PROFINET IO devices from PROFINET IO system

To disconnect an already networked PROFINET IO device from its PROFINET IO system, follow these steps:

1. Click on the PROFINET interface of an IO device.

   ![Disconnecting PROFINET IO devices from PROFINET IO system](images/26291800587_DV_resource.Stream@PNG-de-DE.png)

   ![Disconnecting PROFINET IO devices from PROFINET IO system](images/26291800587_DV_resource.Stream@PNG-de-DE.png)
2. Select the "Disconnect from IO system" shortcut menu command.

   The IO device that was assigned to this IO system is then no longer assigned to it.

   ![Disconnecting PROFINET IO devices from PROFINET IO system](images/26291808779_DV_resource.Stream@PNG-en-US.png)

   ![Disconnecting PROFINET IO devices from PROFINET IO system](images/26291808779_DV_resource.Stream@PNG-en-US.png)

You can create a new IO systems and can assign each of the non-assigned IO devices to an IO controller.

###### Assign PROFINET IO devices to other IO controllers

Existing PROFINET IO systems can be easily reconfigured in the network view by selecting the IO device or its interface and the required command from the shortcut menu:

When selecting the interface:

1. Select the interface of an IO device and then select the shortcut menu. You have the following options here:

   - Assign a new subnet to the IO device or disconnect it from the existing subnet
   - Assign the IO device to a new IO controller
   - Assign a new IO system to the IO device or disconnect it from the existing subnet
2. To assign another IO controller to the IO device, select the "Assign to new IO controller" shortcut menu command.

   If there is no connection, a subnet is automatically created and the IO device is assigned to the IO system of the new IO controller.

When selecting the entire device:

1. Select the IO device and select the shortcut menu. You have the following options here:

   - Assign the IO device to a new IO controller
   - Disconnect the IO device from the existing subnet
2. To assign the IO device to another IO controller, select the "Assign new DP master/IO controller" shortcut menu command.

   If there is no connection, a subnet is automatically created and the IO device is assigned to the IO system of the new IO controller.

##### Configuring an IO device through hardware detection

###### Introduction

As of STEP 7 V15, you have the possibility to detect a real existing IO device and to import it into your project.

You find the IO device in STEP 7 through the "Hardware detection" function. A detected device can be imported into your project. STEP 7 inserts the IO device with all the modules and submodules.

###### Hardware detection of the modules/submodules with ET 200S (GSDML)

Although the following IO devices of the ET 200S (GSDML) are taken into account during hardware detection, their plugged-in modules/submodules are not recognized. If such IO devices are added to the project, any modules/submodules that may be used must be subsequently taken from the HW catalog and configured.

Affected are:

- 6ES7 151-3AA00-0AB0 (with firmware V1.0)
- 6ES7 151-3AA10-0AB0 (with firmware V2.0)
- 6ES7 151-3BA00-0AB0 (with firmware V2.0)
- 6ES7 151-3AA20-0AB0 (with firmware V3.0)
- 6ES7 151-3BA20-0AB0 (with firmware V3.0)

###### Hardware detection of modules/submodules for ET 200SP

If you import an ET 200SP via the hardware detection in your project, you have to complete the determined station configuration manually yourself:

- Check and correct the configured potential group properties (light or dark BaseUnit) for each slot. STEP 7 cannot determine through the hardware detection which BaseUnit actually exists on which slot.
- Check at the interface module whether the appropriate BusAdapter was determined in the hardware configuration (e.g. BA 2xRJ45 instead of BA 2xFC actually present).

###### No hardware detection of IE/PB links

Hardware detection only detects devices that have a role as IO devices. Devices and other components without this role, such as IO controllers, I-devices or devices with assignments to multiple IO controllers (multiple assignment), are not taken into account in the hardware detection. IE/PB links are multi-assignment devices and are therefore not displayed during hardware detection.

###### Device names of PN/PN couplers

The names of the PN/PN couplers must be given special consideration for hardware detection of PN/PN couplers and their subsequent integration in the project configuration. Unlike other IO devices, these PROFINET devices have an additional attribute for automatic generation of device names. When adding a PN/PN coupler to a configuration from hardware detection, the device name reacts the same way, that is, as if the PN/PN coupler had been added to the configuration from the hardware catalog.

The device name of the PN/PN coupler is therefore automatically generated after the hardware detection has been added and may need to be adapted manually afterwards.

###### Hardware detection of SCALANCE XF204-2 BA

The IO device SCALANCE XF204-2 BA is taken into account in the hardware detection, but the modules / submodules (BusAdapter) plugged into it are not detected. When such an IO device is added to the project, any modules/submodules (BusAdapter) that may be used must subsequently be taken from the HW catalog and configured.

Affected are: 6GK5 204-2AA00-2BD2 (with firmware V5.3, V5.4, V5.5).

###### Requirements

- STEP 7 (TIA Portal) as of V15
- New or existing project must be open.
- It must be possible to technically access IO devices via IP

###### Procedure

To detect one or more existing IO devices in STEP 7 and add them to the project, follow these steps:

1. In STEP 7, navigate to "Online" &gt; "Hardware detection".
2. Click "PROFINET devices from network...".  
   STEP 7 opens the "Hardware detection of PROFINET devices" window.
3. Select the interface of your programming device at "PG/PC interface".
4. Click "Start search".  
   STEP 7 begins with the hardware detection. Detected IO devices are also displayed during the ongoing hardware detection. For detected devices, you can already proceed with the following step. When hardware detection is complete, a list of all detected IO devices is displayed.
5. Select the IO devices that you want to add to the project by clicking the corresponding check box in front of the IO device.
6. Click "Add devices".  
   After a brief moment, a window is opens to report about the success or failure of the hardware detection.

###### Result of the hardware detection

If the hardware detection is successful, STEP 7 inserts the IO device with all the modules and submodules into the project.

An IO device configured via hardware detection responds as follows:

- Modules configured through the "Hardware detection" are configured as if they have been inserted from the catalog.
- MAC address: STEP 7 imports the MAC address of the detected IO device into the project.
- IP settings:

  - If the detected IO device already has an IP address, STEP 7 imports the IP address into the project.
  - If the detected IO device does not have an IP address, STEP 7 automatically assigns an IP address in the project.

  PROFINET device name:

  - If the detected IO device already has a PROFINET device name, STEP 7 imports the PROFINET device name into the project.
  - If the detected IO device does not have a PROFINET device name, STEP 7 automatically assigns a PROFINET device name in the project.
- IO devices configured through "Hardware detection" have neither an IP subnet nor an IO controller assigned.

> **Note**
>
> **Hardware detection followed by online connection**
>
> When the "Online &gt; Hardware detection" command is performed for an unspecified CPU, the online configuration is not loaded from the CPU. If you do not load the configuration resulting from the hardware detection to the CPU, the device and network views will always show a difference between the offline and online configurations. It will appear that there are different configurations in the online and diagnostic views, although the article numbers are identical in the actual CPU and the offline CPU.

---

**See also**

[Adding an unspecified CPU](#adding-an-unspecified-cpu)

##### Tip: Quick configuration of IO systems

If the IO system has a lot of IO devices, assign all IO devices placed by drag-and-drop operation to an IO controller on one step.

###### Requirements

IO controller and IO devices are placed in the network view.

###### Assign IO devices to an IO system

To do this, follow these steps:

1. Select an appropriate zoom factor so that you can see as many IO devices as possible in the network view.
2. Arrange the IO devices in not more than of two rows.
3. Select all IO interfaces (not all devices) with the mouse cursor. This only works if you begin to drag the mouse cursor outside of the first IO device and release the mouse button at the last IO device (selection with the lasso).

   ![Assign IO devices to an IO system](images/26101430539_DV_resource.Stream@PNG-en-US.png)
4. Select the shortcut menu "Assign new IO controller" and select the corresponding IO interface of the IO controller in the subsequent dialog.

   ![Assign IO devices to an IO system](images/26101490443_DV_resource.Stream@PNG-en-US.png)
5. The IO devices are automatically networked with the IO controller and combine with it to form an IO system.

   > **Note**
   >
   > When an IO system is highlighted, you can double-click on an IO device in the hardware catalog and thereby quickly add additional IO devices. Result: The IO device is automatically added to the highlighted IO system.

##### Interconnecting ports

If an IO device is assigned to an IO controller, this does not yet specify how the ports are connected to each other.

Although a port interconnection is not required to make use of the Ethernet/PROFINET functions, it does offer the following advantages:

- A target topology is specified with the port interconnection. Based on an online-offline comparison, it is possible to conduct a target-actual comparison with all devices that support this function.
- Only with IRT communication: If a port interconnection is configured, STEP 7 can determine the required bandwidth more precisely. As a rule, this leads to a higher performance.

Make sure that no invalid ring structures occur through the interconnection of ports.

Port interconnection is only advisable for devices that support the topology configuration.

###### Interconnecting ports in the Inspector window

To interconnect ports, follow these steps:

1. Select the Ethernet/PROFINET device or the Ethernet/PROFINET interface.
2. Navigate to the port property "Port interconnection".

   When the Ethernet/PROFINET interface is selected, you can find this setting in the Inspector window as follows: Properties &gt; General &gt; Advanced Options &gt; Port [...] &gt; Port Interconnection.
3. In the "Local port" section, you can find the settings at the local port. In the case of fiber-optic cable you can, for example, set the cable names here.

   In the "Partner port" section, click on the black triangle in the "Partner port" box to display and select the available partner ports.
4. If the port interconnection is a port interconnection with copper as medium and the devices support IRT communication, you can also set cable length and signal transit time.

If the Ethernet/PROFINET interface was disconnected, it is automatically networked by this action. In the properties of the subnet you can set whether this subnet should or should not be used for the networking.

> **Note**
>
> **Interconnecting an electric with an optical port**
>
> If you want to interconnect an electrical and an optical port, you have to distinguish between RT and IRT communication:
>
> - With RT communication, it is not necessary to configure a media converter.
> - With IRT communication, you have to make the interconnection via a media converter.

###### Information on monitoring the partner port

After you have interconnected the two ports, you receive information on the monitoring of the partner port in a text field. The following displays are possible:

- Monitoring of the partner port is not possible.
- Partner port is being monitored.

It is not possible to monitor the partner port if you, for example, select a deactivated port as partner port. In this case it is not possible to monitor the target topology and the signal propagation time. A device replacement is then only possible with a Micro Memory Card.

---

**See also**

[Overview](#overview)
  
[Overview of the CPU properties (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#overview-of-the-cpu-properties-s7-1500)
  
[Interconnecting ports](#interconnecting-ports)

##### Setting the send clock

###### Requirements to change the send clock at the PROFINET device

The PROFINET device must be an IO controller as sync master or IRT (Isochronous Realtime) must not be configured in the IO system.

If the PROFINET device is not an IO controller as sync master, the following requirements must be met for the setting of the send clock:

- No device must be configured at the IO system as a sync slave or sync master.
- All devices at the IO system must be unsynchronized.

When IRT is configured with an IO controller as sync master, the send clock can be set at the device or in the sync domain.

###### Procedure

To set the send clock on the PROFINET device, follow these steps:

1. Select the PROFINET IO controller in the device or network view.
2. Change the value for the shortest possible update interval in the properties of the PROFINET interface under "PROFINET Interface &gt; Advanced options &gt; Real-time settings &gt; IO communication &gt; Send clock".

The send clock is valid for all PROFINET devices at the IO system. If the synchronization role is set to a value other than "Unsynchronized", you can also set the send clock in the sync domain, in other words, centrally at the PROFINET IO system.

1. Select the IO system using the PROFINET subnet.
2. Change the value for the send clock in the properties of the sync domain under "Domain management &gt; Sync domains &gt; Sync_domain_1 &gt; Send clock".

##### Setting the update time

###### Update time

An IO device / IO controller in the PROFINET IO system is supplied with new data from the IO controller / IO device within this time period. The update time can be separately configured for each IO device and determines the time interval in which data is transmitted from the IO controller to the IO device (outputs) as well as data from the IO device to the IO controller (inputs).

STEP 7 calculates the update time automatically in the default setting for each IO device of the PROFINET IO system, taking into account the volume of data to be exchanged as well as the set send clock.

###### Setting the update time

If you do not want to have the update time calculated automatically, you can change the setting.

To change the update time in the Inspector window, proceed as follows:

1. Select the PROFINET interface of the IO device in the network or device view.
2. Specify the update time in the interface properties under "Advanced options &gt; Real time settings &gt; IO cycle". You can specify the update time in two ways:

   - Automatic calculation of the optimal update time.
   - Update time you can set yourself by selecting different values from a drop-down list.
3. If you want to keep the relationship between the send clock and the update time constant, enable the "Adapt update time when send clock changes" option.

   This option ensures that the update time is not set to less than the send clock.

You can also carry out this setting directly in the I/O communication table via the drop-down list in the "Update time mode" column.

Manual setting of the send clock may result in errors if the available bandwidth is not adequate or when other limits/configuration limits are exceeded (for example, too many nodes are configured).

> **Note**
>
> When you change the update time mode from "Can be set" to "Automatic", a manually entered update time is overwritten by the automatically calculated value.

###### No update time can be calculated

STEP 7 determines the sequence of the cyclic data exchange based on the configuration information (IO controller properties, IO device properties, number and type of the IO devices, consistency of the cyclic user data...). The cyclic data is packed in frames and sent/received successively at calculated time intervals.

The maximum number/size of the frames and the maximum number of intervals available must be sufficient to "accommodate" all the data. The resulting send/receive interval must also be supported by every PROFINET device.

If the limits relating to the amount of cyclic user data/number of frames or relating to the intervals available are exceeded, STEP 7 cannot calculate an update time.

If there is no common basis for the send/receive interval, calculating the update time is also not possible.

If there is a reason preventing the calculation of the update time, STEP 7 reports the cause when compiling the hardware configuration.

How to eliminate the problem:

- Reduce the number of IO devices
- Reduce the number of modules within the IO devices
- If you are using an IE/PB link: Reduce the number of DP slaves downstream from the IE/PB link
- Use a more powerful IO controller or IE/PB link
- Increase the send clock

  - With RT: in the properties of the IO controller
  - With IRT: in the properties of the sync domain
- Check the device properties of the IO devices ('MinDeviceInterval' and the possible scan rates) due to the common basis for the send/receive interval. Replace unsuitable IO devices. This device properties are stored in the GSD file of the IO device.
- With IRT configuration:

  - Check whether the ports of the sync master and sync slaves are interconnected.
  - Check the order of the IO devices: There can be **no** unsynchronized device connected between the sync master and sync slave

    (Example of bad configuration: Sync master --- unsynchronized device --- sync slave).
  - Check whether you have configured more than one sync master.
  - Check the bandwidth remaining for RT data. The bandwidth for RT data available for the transfer can be restricted by IRT communication on the same Ethernet subnet.
- When using I-devices:

  It may not be possible to use the set send clock together with the existing I-device configuration.

  - Configure the I-device without lower-level IO devices and activate the setting "Parameter assignment of PN interface by higher-level IO controller".
  - Change the send clock of the IO controller to an even value (... 0.250, 0.500, 1.000, ...).

Identification of the IO devices involved:

You can identify the IO devices involved for which no update time can be calculated in the "I/O communication" table of the PROFINET IO system in the network view. No entry is made in the "Update time" column for the IO device involved (entry "-").

##### Setting the watchdog time

###### Watchdog time

You can configure the watchdog time for PROFINET IO devices.

If the IO device is not supplied with input or output data (IO data) by the IO controller within the watchdog time, it switches to the safe state.

Do not enter the watchdog time directly, but as "Accepted number of update cycles when IO data is missing". This makes setting easier because the update time can be shorter or longer, depending on the power of the IO device or the setting.

The resulting watchdog time is automatically calculated from the "Accepted number of update cycles when IO data is missing".

###### Configuring the watchdog time

To specify the watchdog time, follow these steps:

1. Select the PROFINET interface of the IO device in the network or device view.
2. In the properties of the interface, navigate to "Advanced options &gt; Realtime settings &gt; IO cycle".
3. Select the required number of cycles from the drop-down list "Trigger watchdog after # cycles with missing IO data".

The watchdog time is subsequently calculated automatically based on the preset factor. It must not be more than 1.92 seconds.

> **Note**
>
> You should only change the default setting in the following cases:
>
> - In the commissioning phase
> - When configuring S7-1500R/H systems
>
> **Configuring the watchdog time for S7-1500R/H systems**
>
> If you have configured modules for the IO devices and compile the project, you receive an error message for the watchdog timer in the Inspector window. Set the watchdog timer indicated in the error message.

##### Calculated bandwidth for cyclic IO data

###### Calculated bandwidth for cyclic IO data

Adherence to the maximum available bandwidth for cyclic IO data is monitored by the system. The maximum bandwidth depends on the send clock cycle. If the send clock cycle is greater than or equal to 1 ms, the maximum bandwidth is 0.5 ms. If the send clock cycle is shorter, the maximum available bandwidth is also reduced.

The bandwidth actually required for cyclic IO data is determined by the system based on the number of configured IO devices and IO modules. Furthermore, the required bandwidth depends on the update time that is used.

In general, the calculated bandwidth increases in the following cases:

- There is a greater number of IO devices
- There is a greater number of IO modules
- The update times are shorter.

###### Maximum bandwidth for cyclic IO data depending on the send clock

The following table shows how the maximum available bandwidth for cyclic IO data reacts based on the send clock:

| Send clock cycle | Maximum bandwidth for cyclic IO data |
| --- | --- |
| 250 µs – 468.75 µs | &lt;&lt; 125 µs |
| 500 µs – 968.75 µs | = send clock / 2 |
| 1 – 4 ms | = 500 µs* |

*: Lower maximum bandwidths apply for redundant systems:

- for S7-1500H = 250 µs applies
- for S7-1500R = 125 µs applies

##### Setting port options

This section contains information on the following topics:

- [Setting the port options](#setting-the-port-options)
- [Wiring rules for disabled autonegotiation](#wiring-rules-for-disabled-autonegotiation)
- [Boundaries at the port](#boundaries-at-the-port)

###### Setting the port options

###### Changing connection settings for the PROFINET IO port

By default, the settings for ports of a PROFINET interface are specified in such a way that problem-free data exchange is ensured in normal situations.

If necessary, you can change the settings. The setting options are described below.

###### Possible settings for transmission rate/duplex

Depending on the selected device, you can make the following settings for "Transmission rate/duplex":

- Automatic setting

  Recommended default setting of the port. The transmission settings are automatically "negotiated" with the partner port. The "Enable autonegotiation" option is automatically selected by default.
- TP/ITP at x Mbps full duplex (half duplex)

  Setting of the transmission rate and the full duplex/half duplex mode. The effectiveness depends on the "Enable autonegotiation" setting:

  - Autonegotiation enabled

    You can use both cross cable and patch cable. The port is monitored with this setting.
  - Autonegotiation disabled

    Make sure that you use the correct cables (patch or cross cables). The port is also monitored with this setting.
- Deactivated

  Depending on the device type, the drop-down list box can contain the "Deactivated" option. With this option, you can prevent access via an unused port for security reasons, for example. With this setting, diagnostic events are not generated.

###### "Monitor" option

With the "Monitor" option, you enable/disable port diagnostics. You can only enable monitoring if the device supports this function.

Below is a list of what is monitored during operation by the device when monitoring is enabled - regardless of whether you have interconnected the port or not:

- The link status is monitored; in other words, diagnostics is generated when the link is down (e.g. with a wire break or a removed connector). With fiber-optic ports (FO), the link power margin is monitored so that a staged maintenance diagnostics is obtained.
- The media settings are monitored; in other words, a diagnostics message is generated when the local port setting (transmission rate/duplex) during operation does not match the setting of the partner port.
- If the port is interconnected: The cable length/signal delay time is monitored; in other words, a diagnostics message is generated if the locally detected cable length/signal delay time does not match the cable length/signal delay time detected by the partner.

**Disabling monitoring**

Monitoring does **not** make sense in the following cases:

- The option "Alternative partners" is enabled at the local port, for example, for a docking port of a docking station (tool changer). In this case, a link status change is a normal operational situation.
- The partner port belongs to a non-PROFINET device. Only ports of PROFINET devices transfer their port settings such as the transmission rate, duplex setting etc.
- The local port is connected to a media converter (passive network component with different signal delay times for Ethernet frames).
- At the local port, the option "End of topology discovery" is enabled in the boundaries settings.

**Monitoring of the desired topology**

With the "Monitoring" option, no monitoring is linked to the adherence to the desired topology. This means that whether the configured interface and port properties such as device name, port name and cable length match the current settings is not influenced by the "Monitoring" option.

Adherence to the desired topology is checked automatically when you interconnect the local port with a partner port; the partner port must not then be disabled. The port properties indicate whether the monitoring of the desired topology is performed or is impossible (port interconnection, partner port refer, to the figure below ①).

!["Monitor" option](images/79783737099_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Display of whether the device can check the actual properties of the partner port against the configured properties of the partner port. This adherence to the desired topology is checked automatically when you interconnect the local port with a partner port. |
| ② | Setting the monitoring to link down, media settings and cable length/signal delay time. At runtime, the local port compares its own settings with the settings of the partner port. |

###### Option "Enable autonegotiation "

The autonegotiation setting can only be changed if a concrete medium (for example, TP 100 Mbps full duplex) is selected. Whether or not a concrete medium can be set depends on the properties of the module.

If autonegotiation is disabled, this causes the port to be permanently specified, as for example, is necessary for a prioritized startup of the IO device.

You must make sure the partner port has the same settings because, with this option, the operating parameters of the connected network are not detected and the data transmission rate and transmission mode can therefore not be optimally set.

> **Note**
>
> When a local port is interconnected, STEP 7 makes the setting for the partner port if the partner port supports the setting. If the partner port does not support the setting, an error message is generated.

###### Port options for using the GBIT PROFINET interface

The PROFINET interface (X3) of the CPU 1518-4 PN/DP supports a maximum transmission rate of 1000 Mbps (GBIT).

In order to achieve this transmission rate, the following requirements must be met:

- CPU Firmware Version V1.7 or higher.
- Devices on the same PROFINET subnet must also support the 1000 Mbps transmission rate.
- The network infrastructure (network cables and outlets) must be category CAT 5e or better.
- The port options of PROFINET interface X3 must be set as follows:

  - “Transmission rate/Duplex”: Automatic
  - “Autonegotiation”: Activated

---

**See also**

[Wiring rules for disabled autonegotiation](#wiring-rules-for-disabled-autonegotiation)
  
[Boundaries at the port](#boundaries-at-the-port)

###### Wiring rules for disabled autonegotiation

###### Requirement

You have made the following settings for the port in question, for example, to accelerate the startup time of the IO device:

- Fixed transmission speed
- Autonegotiation incl. autocrossing disabled

This saves you the time required to negotiate the transmission rate during startup.

If you have disabled autonegotiation, you must observe the wiring rules.

###### Wiring rules for disabled autonegotiation

PROFINET devices have the following two types of ports:

| Type of port | PROFINET devices | Note |
| --- | --- | --- |
| Switch port with crossed pin assignment | For IO devices: Port 2  For S7 CPUs with 2 ports: Ports 1 and 2 | Crossed pin assignment means that the pin assignment for the ports for sending and receiving between the respective PROFINET devices is exchanged internally. |
| End device port with uncrossed pin assignment | For IO devices: Port 1  For S7 CPUs with one port: Port 1 | - |

###### Validity of the wiring rules

The cabling rules described in the following paragraph apply exclusively to the situation in which you have specified a fixed port setting.

###### Rules for cabling

You can connect several IO devices in a line using a patch cable (one-to-one wiring of both connectors). To do this, you connect port 2 (P2) of the IO device to port 1 (P1) of the next IO device. The following graphic gives an example with two IO devices.

![Rules for cabling](images/23137225995_DV_resource.Stream@PNG-en-US.png)

###### Boundaries at the port

###### Requirement

The respective device must support boundaries settings in order to work with boundaries. If the device for PROFINET does not support boundary settings, the corresponding parameters are disabled, such as in the CPU 1215C V3, for example.

###### Enable boundaries

"Boundaries" are limits for transmission of certain Ethernet frames. The following boundaries can be set at a port:

- "End of detection of accessible devices"

  DCP frames for detection of accessible devices are not forwarded. Devices located behind this port are no longer displayed in the project tree under "Accessible devices". Devices located behind this port can no longer be reached by the CPU.

  The device must have more than one port for this function.
- "End of topology discovery"

  LLDP frames (Link Layer Discovery Protocol) for topology detection are not forwarded.
- "End of sync domain"

  Sync frames transmitted for synchronization of devices within a sync domain are not forwarded.

  For example, if you operate a PROFINET device with more than two ports in a ring, you should prevent the sync frames from being fed into the ring by setting a sync boundary (at the ports not inside the ring).

  The device must have more than one port for this function.

  Additional example: If you want to use several sync domains, configure a sync domain boundary for the port connected to a PROFINET device of the other sync domain.

###### Restrictions

The following restrictions must be observed:

- The individual check boxes can only be used if the port supports the function in question.
- If a partner port has been defined for the port, the following check boxes cannot be used:

  - "End of detection of accessible devices"
  - "End of topology discovery"

##### Enabling device replacement without exchangeable medium

###### Replacing an IO device without exchangeable medium

It is often necessary to replace IO devices in automation systems. The IO devices are generally assigned a device name by either inserting an exchangeable medium or via the programming device. The IO controller uses this device name to identify the IO device.

Subject to certain conditions, IO devices can also receive their device names without the insertion of an exchangeable medium (e.g., memory card) or without a programming device. For this purpose, the IO controller uses Ethernet mechanisms (LLDP protocol; Link Layer Discovery Protocol) to analyze the relationships between the individual IO devices and the IO controller. From these relationships, the IO controller detects which IO device was replaced and assigns the configured device name to it.

###### Requirements

- A port interconnection is already configured.
- The affected IO devices in the automation system must support device replacement without exchangeable medium (LLDP protocol).

> **Note**
>
> Use only new IO devices as replacement devices, or restore IO devices already configured to the delivery state prior to commissioning.
>
> For S7-1500 CPUs with firmware version V1.5 or higher, it is not necessary to reset IO devices with an existing parameter assignment to delivery state. Requirement: The "Permit overwriting of device names of all assigned IO devices" option is selected for the IO controller ("Advanced option &gt; Interface options" area of the properties of the PROFINET interface).

###### Procedure

In order to enable the replacement of an IO device without exchangeable medium, proceed as follows:

1. In the device or network view, select the PROFINET interface of the corresponding IO controller.
2. In the interface properties under "Advanced settings &gt; Interface options", select the "Support device replacement without exchangeable medium" check box.

The option "Support device replacement without exchangeable medium" also permits automatic commissioning, which means you can commission the IO system with the IO devices without assigning their device names in advance.

###### IO devices without corresponding functionality

When individual IO devices in the automation system do not support device replacement without exchangeable medium, a corresponding alarm is output for the IO device. It is possible to use the functionality nevertheless. However, all of the following conditions have to be fulfilled:

- The function "Device replacement without exchangeable medium" is activated in the higher-level IO controller.
- The IO device supports the LLDP protocol.
- At least one "neighbor" of the IO device supports

  - The function "Device replacement without exchangeable medium" as an IO controller or
  - The LLDP protocol as an IO device.

When you configure the environment of the IO device so that the conditions described above are met for the "Device replacement without exchangeable medium", the usage of the function is possible even if the IO device does not support the functionality directly.

---

**See also**

[Assigning the device name and IP address](#assigning-the-device-name-and-ip-address)
  
[Permit overwriting of PROFINET device name](Special%20PROFINET%20configurations.md#permit-overwriting-of-profinet-device-name)
  
[Components with the the device replacement without exchangeable medium function](http://support.automation.siemens.com/WW/view/en/36752540)

##### Connect the DP slave via the IE/PB Link to a PROFINET IO system

###### Requirements

- STEP 7 as of V12
- S7‑1500 CPU as of firmware version 1.7
- ET 200SP CPU as of firmware version 1.7
- S7-1500 software controller
- S7-300/400 CPU

###### Procedure for connecting a DP slave via an IE/PB Link

To connect a DP slave to a PROFINET IO system via an IE/PB Link in STEP 7, follow these steps:

1. Drag a PROFINET CPU, e.g. 1513-1 PN, from the hardware catalog to the network view of STEP 7.
2. Drag an IE/PB Link PN IO from the hardware catalog into the network view of STEP 7. The IE/PB Link PN IO is located under Network components &gt; Gateways &gt; IE/PB Link PN IO.
3. Assign the IE/PB Link PN IO to the CPU.
4. Drag a PROFIBUS interface module, e.g. IM155-6 DP HF, from the hardware catalog to the network view.
5. Assign the interface module to the IE/PB Link.

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031922827_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031922827_DV_resource.Stream@PNG-de-DE.png)
6. Select the IE/PB Link PN IO in the network view of STEP 7.
7. In the Inspector window, go to the "Gateway" area and select the "Network gateway as PROFINET IO proxy" option.

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031931531_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031931531_DV_resource.Stream@PNG-en-US.png)
8. In the PROFINET device number area, you can assign a PROFINET device number for the DP slave.  
   If you have selected the "Device number = PB address" check box (default), STEP 7 automatically assigns the device number according to the PROFIBUS address of the slave. In addition, you no longer need to update the device number if the PROFIBUS address changes.

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031940235_DV_resource.Stream@PNG-en-US.png)

   ![Procedure for connecting a DP slave via an IE/PB Link](images/72031940235_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuration with IE/PB LINK](#configuration-with-iepb-link)

##### Setup recommendations for optimizing PROFINET

###### Optimizing PROFINET with RT

PROFINET provides you with high-performance communication on all levels.

The figure below shows an example of an optimized PROFINET topology.

![Optimizing PROFINET with RT](images/88100062475_DV_resource.Stream@PNG-en-US.png)

When setting up your PN network topology, take care that the various automation applications are distributed among separate network branches so that a sufficient bandwidth reserve will be available for future expansions.

- When you integrate standard Ethernet devices into the network topology or use standard Ethernet communication, take into account the network load caused by standard Ethernet and adapt the network topology as appropriate (max. bandwidth 100 Mbps).
- For communication with higher-level networks with a high data volume, use the most direct paths possible to the higher-level network infrastructure.

Also observe the Installation Guideline of the PROFIBUS User Organization.

###### Setting up PROFINET with IRT

Keep in mind the following rules for setting up and operating a PROFINET IO system in IRT mode. These rules will ensure best possible operation of your PROFINET IO system.

- When using IRT, you must configure the topology. This will enable exact calculation of the update time, bandwidth, and other parameters.
- If you would like to use multiple sync domains, configure a sync boundary for the port which is currently connected to the PROFINET device of another sync domain.
- In a sync domain, you can only configure one sync master at a time.
- A PROFINET IO system may only be part of a single sync domain.
- When you configure PROFINET devices in a sync domain and want to synchronize with IRT, the PROFINET devices concerned must support IRT communication.
- If possible, use the same PROFINET device as the PROFINET IO controller and sync master.
- If only some of the PROFINET devices in a PROFINET IO system are synchronized, please keep in mind the following: Assign PROFINET devices that are not participating in the IRT communication to the RT class "RT" and the synchronization role "unsynchronized" in the sync domain.

###### Applications for CPU with multiple PROFINET IO interfaces

- Connecting machines: Your configuration contains machines located on separate IO lines. You can operate real-time communication between the CPUs over X2 PROFINET IO interfaces. Use the I‑device or shared I‑device function for this purpose.  
  The figure below shows an example configuration for 2 machines connected over the X2 interface with an I‑device relationship.

  ![Applications for CPU with multiple PROFINET IO interfaces](images/88100079371_DV_resource.Stream@PNG-en-US.png)
- Distribution by automation tasks:

  - For automation tasks with high performance and deterministic requirements, use PROFINET with IRT over the X1 interface.
  - For other tasks that you can implement with RT, use the X2 interface.

If you use interface X2 as the PROFINET IO interface for one of the following CPUs, this can affect performance:

- CPU 1515(F)‑2 PN
- CPU 1515T‑2 PN
- CPU 1516(F)‑3 PN/DP
- CPU 1516(F)pro-2 PN

You can find additional information in the Cycle and Response Times function manual.

###### Topological overlap of IO systems in multi‑controller applications

In a configuration with multiple IO controllers, shared paths are subject to the combined network loads of all connected PROFINET IO systems.

To avoid high communication loads in multi‑controller applications, observe the following recommendations:

- Avoid paths that are shared by multiple IO systems.  
  The figure below shows a configuration with two PROFINET IO systems that use the same paths.

  ![Topological overlap of IO systems in multi‑controller applications](images/88100028683_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Shared path |

  In the figure below, the two PROFINET IO systems do not use shared paths.

  ![Topological overlap of IO systems in multi‑controller applications](images/88100045579_DV_resource.Stream@PNG-en-US.png)
- If separation is not possible: Increase the update time for the affected IO devices.

###### Installation guidelines of the PROFIBUS user organization

The installation guidelines can be found on the Internet.

##### Limitation of the data infeed into the network

###### Limiting the data infeed into the network on PROFINET interfaces

The "Limit data infeed into the network" function limits the network load of standard Ethernet communication which is fed into the network by the interface to a maximum value. This does not apply to cyclic real-time communication (RT/IRT).

In a PROFINET IO system, critical network loads can occur quickly with standard Ethernet communication. All devices in a PROFINET IO system should support the "limitation of the data infeed into the network".

If you use devices that feed a lot of "standard Ethernet communication" into the PROFINET IO system, you should adapt the topology, if necessary.

Depending on the interface, you can activate or deactivate the "Limit data infeed into the network" function. If you use the X1 interface of an S7-1500 CPU as the IO controller or I-device, the "Limit data infeed into the network" function is always enabled. Example: If you are not using the X1 interface of an S7-1500 CPU as IO controller or I-device, you can enable or disable the function.

###### Uses of the limitation of the data infeed to the network

- Division of the bandwidth for standard Ethernet communication between devices:  
  In PROFINET networks cyclic real-time communication and standard Ethernet communication share the same network. This means that only a limited bandwidth remains for standard Ethernet communication. The limitation of the data infeed ensures that the remaining bandwidth for standard Ethernet communication is not used just by one device, but is divided between several devices.
- Smoothing peaks in the data infeed:  
  The limitation of the data infeed smooths peak loads of standard Ethernet communication (for example, from Open User Communication, access by the Web server).
- Limiting problems in the data infeed:   
  If applications in a device generate too much data, this data is not forwarded to the PROFINET network. Negative effects (for example data loss, communication breakdown) remain limited to the device and its communications partner. Other nodes are not disturbed.

###### Setting limitation of the data infeed into the network for a CPU

To set the limitation of the data infeed into the network ("infeed load limitation"), follow these steps:

1. In the network view of STEP 7, select the interface of the CPU.
2. In the Inspector window, go to "Properties" &gt; "General" &gt; "Advanced options" &gt; "Interface options".
3. Select or clear the "Limit data infeed into the network" check box.

   ![Setting limitation of the data infeed into the network for a CPU](images/90826252043_DV_resource.Stream@PNG-en-US.png)

##### Maintaining communication relations during faults

An existing communication relation (Application Relation, AR) is a precondition for data exchange between an IO controller and an IO device.

In a communication relation, data is transmitted cyclically and acyclically. If a protocol error or a timeout is detected during acyclic data record communication (for example, program instructions "RDREC", "WRREC", or reading a diagnostic data record) the IO controller cancels the communication relation. In this case, the IO controller assumes that communication is faulty. This also ends the cyclic IO data exchange. The error code is returned as a static error in the instruction to the data record transfer. In the diagnostic buffer of the IO controller, the error is displayed as the event "Failure of an IO device - Timeout in the acyclic PROFINET services".

Possible causes for a termination of the communication relation include:

- A high network load
- Too many ARP telegrams (Address Resolution Protocol).
- Too many UDP frames (User Datagram Protocol).
- Erroneous RPC calls (Remote Procedure Call).

###### Maintain communication relation

If you can tolerate timeouts during the data record communication from the point of view of your application and no negative repercussions are to be feared, you can change the described default behavior. If, for example, timeouts occur during the data record communication, the communication relation is still preserved. Cyclic IO data exchange continues.  
A data exchange error is then signaled as a temporary error (status code: 16#DE80_C300 or 16#DF80_C300) in the instruction for data record transfer.

As of STEP 7 V19, 2 options are available to activate maintaining of the communication relation. Depending on the FW version of the S7‑1500 CPU used, activate maintaining as follows:

- S7‑1500 CPU FW version V 3.1 onwards:

  - You can configure maintaining in the CPU properties.
  - You can transfer a data record 0xB072 to an integrated PROFINET interface of the S7‑1500 CPU.
- S7‑1500 CPU from FW version V3.0: You can transfer a data record 0xB072 to an integrated PROFINET interface of the S7‑1500 CPU.

You must activate maintaining of the communication relation separately for each required PROFINET interface as follows:

- When configuring in the CPU properties, you must activate maintaining for each required PROFINET interface separately.
- When transferring a data record 0xB072, you must transfer it separately to each required PROFINET interface.

You will find procedures for maintaining the communication relations in the sections below.

###### Maintaining the communication relations for S7-1500R/H systems

For S7‑1500R/H CPUs, activate maintenance of the communication relation as described above. However, the S7‑1500R/H system does not synchronize all changes automatically. Therefore you have to make the changes as follows:

- Activation in the CPU‑properties: Activate maintenance of the communication relation in the CPU‑properties of the CPU of the S7‑1500R/H system. STEP 7 synchronizes this setting automatically between the two CPUs.
- Transferring a data record: A PROFINET‑interface, for example X1, has different hardware identifiers for the two CPUs. Therefore, write the data record at runtime to the respective addressed PROFINET interface of both CPUs.

With S7-1500R/H systems, you can only maintain the communication relation at the PROFINET interface X1.

---

**See also**

[Activating maintenance of the communication relation in the CPU properties](#activating-maintenance-of-the-communication-relation-in-the-cpu-properties)

##### Activating maintenance of the communication relation in the CPU properties

###### Requirements

If you want to activate maintenance of the communication relationship in the CPU properties, the following requirements have to be met first:

- STEP 7 V19
- S7‑1500 CPU from FW version V3.1 onwards
- IO system, for example, "PLC_1.PROFINET IO System (100)", is configured at the respective PROFINET interface

###### Procedure

The following procedure shows an example of how to enable maintaining the communication relation at the integrated PROFINET interface X1. The procedure is identical for all integrated PROFINET interfaces of the S7‑1500 CPU. To enable or disable maintenance of the communication relation in the CPU properties, follow these steps:

1. Switch to the network view of STEP 7.
2. Configure a S7‑1500 CPU, for example, CPU 1516-3 PN/DP, with the required IO devices.
3. Select a PROFINET interface of the S7‑1500 CPU, for example X1.
4. In the Inspector window, go to "General &gt; Advanced options &gt; Interface options".
5. In the "Interface options" section activate the option" Maintain PROFINET IO communication on data record communication timeout".

   ![Procedure](images/168543871499_DV_resource.Stream@PNG-en-US.png)
6. If required, repeat steps 3 to 5 for another integrated PROFINET interface of the S7‑1500 CPU.
7. Load the changed settings to the S7‑1500 CPU.

   Result: The communication relation is maintained at the respective configured PROFINET interface of the S7‑1500 CPU.

The option "Maintain PROFINET IO communication on data record communication timeout" can only be activated if you have added an IO system to the affected PROFINET interface of the S7‑1500 CPU. If no IO system is available at this PROFINET interface, the option is displayed in gray. In this case, the option cannot be activated.

If you delete an existing IO system after activating the option "Maintain PROFINET IO communication on data record communication timeout" the check box still remains enabled. The option is displayed in gray in this case and cannot be changed.

###### Behavior of the option in the case of device exchange in STEP 7

The option "Maintain PROFINET IO communication on data record communication timeout" can be configured in STEP 7 V19 only for configured S7‑1500 CPUs from FW version V3.1 onwards. If you want to exchange or replace a S7‑1500 CPU, the option behaves as follows, depending on the configured FW version:

- S7‑1500 CPU with FW version V3.1 → S7‑1500 CPU with FW version V3.1:  
  STEP 7 applies the settings of the previous S7‑1500 CPU to the new S7‑1500 CPU.
- S7‑1500 CPU with FW version V3.1 → S7‑1500 CPU with FW version &lt; V3.1:  
  STEP 7 shows an alarm message. The option is deactivated and cannot be selected any more.
- S7‑1500 CPU with FW version V3.0 → S7‑1500 CPU with FW version V3.1:  
  STEP 7 shows an information message. The option can be selected and deactivated in the default settings.

At the new S7‑1500 CPU, the changes only become effective after the configuration has been loaded. Therefore, load the changed configuration into the new S7‑1500 CPU.

###### More information

A further possibility to set maintaining of the communication relations (from STEP 7 V18 and S7-1500 FW version 3.0 onwards):

Transfer a data record 0xB072 to the PROFINET interface of the S7‑1500 CPU. This data record encodes whether the communication relation should be terminated or remain active in the event of faults. The data record only has an effect on the addressed PROFINET interface.

You can find a description of the procedure and a programming example in the Function Manual PROFINET, PROFINET with STEP 7 V19.

---

**See also**

[Maintaining communication relations during faults](#maintaining-communication-relations-during-faults)

#### Using GSD files

This section contains information on the following topics:

- [GSD files for IO devices](#gsd-files-for-io-devices)
- [Installing the GSD file](#installing-the-gsd-file)
- [Deleting GSD file](#deleting-gsd-file)
- [Finding unused GSD files](#finding-unused-gsd-files)
- [Changing the revision of a GSD file](#changing-the-revision-of-a-gsd-file)

##### GSD files for IO devices

###### Basic information on GSD files of IO devices

The properties of PROFINET IO devices are not stored in a keyword-based text file (as for PROFIBUS DP slaves), but in an XML file whose structure and rules are determined by a GSDML schema.

The language used to describe the GSD files is GSDML (Generic Station Description Markup Language). It is defined by the GSDML schema. A GSDML schema contains validation rules that allow it, for example, to check the syntax of a GSD file. GSDML schemas (as schema files) are acquired by IO device manufacturers from PROFIBUS International.

Functional enhancements in the area of PROFINET IO will have an effect on the GSDML specification and the corresponding schema. A new version of the specification and of the schema is created by the functional enhancement.

###### Names of GSD files for IO devices

One possible example of a GSD file name for IO devices is:

"GSDML-V1.0-Siemens-ET200S-20030616.xml"

| Name component | Explanation |
| --- | --- |
| GSDML | String at the start of each GSD file for IO devices |
| V1.0 | Version of the GSDML schema |
| Siemens | Manufacturer |
| ET200S | Name of the device |
| 20030616 | Version code (date) |
| .xml | File extension |

###### Versioning of GSD files for IO devices

The version information for GSD files for PROFINET IO devices consists of two parts:

- Version of the GSDML schema: This determines the language scope used by a GSD file.
- Version number in form of a date: The version number of GSD files is incremented, for example, after elimination of an error or introduction of a functional enhancement.

Functional enhancements may result in a new version of the GSDML schema. A new version of a GSDML schema might only be supported with restrictions.

##### Installing the GSD file

###### Introduction

A GSD file (general station description file) contains all properties of an IO device. If you want to configure an IO device that is not available in the hardware catalog, you must install the GSD file provided by the manufacturer. IO devices installed via GSD files are displayed in the hardware catalog and can then be selected and configured.

###### Requirement

- The hardware and network editor is closed.
- You have access to the required GSD files in a directory on the hard disk.

###### Procedure

To install a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD files are stored.
3. Choose one or more files from the list of displayed GSD files.
4. Click on the "Install" button. The selected GSD files are now being installed.
5. To create a log file for the installation, click on the "Save log file" button.

   Any problems during the installation can be tracked down using the log file.
6. Click "Close". You will be notified that the IO devices from the installed GSD files are entered into the hardware catalog. This process can take a few seconds.

By installing a GSD file you have added the IO device described in the file to the hardware catalog.

###### Result

You will find the new IO devices installed by means of GSD files in the hardware catalog under "Additional field devices &gt; PROFINET IO".

GSD files are always saved together with the project, which means all information relevant for display of the device (including symbols) is also available in the saved project.

---

**See also**

[Overview of hardware and network editor](#overview-of-hardware-and-network-editor)
  
[Exporting an I-device as a GSD file](Special%20PROFINET%20configurations.md#exporting-an-i-device-as-a-gsd-file)

##### Deleting GSD file

###### Introduction

You can delete installed DP slaves using GSD files. These DP slaves are then no longer displayed in the hardware catalog.

###### Requirement

- The hardware and network editor is closed.
- You will find the new IO devices installed by means of GSD files in the hardware catalog under "Additional field devices &gt; PROFINET".

###### Procedure

To delete a GSD file, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. In the "Installed GSDs" tab, select the directory in which the GSD file is stored.
3. Select the file that is to be deleted from the list of displayed GSD files.
4. Click the "Delete" button.

The selected GSD file was deleted and the DP slave is no longer located in the hardware catalog.

##### Finding unused GSD files

###### Introduction

When you add a GSD-based hardware component to your hardware configuration, different GSD files are added to the project data. If the GSD-based hardware component is once again deleted from the configuration, the GSD files remain in the data inventory of the project. The GSD files are no longer needed in the project if the corresponding GSD-based hardware component is not used in the hardware configuration again. You can find files that are no longer needed in the project with a search function and delete them.

###### Requirement

- A project must be open.
- The project must not be online.
- The project must not be write-protected.

###### Procedure

To find and delete unused GSD files, follow these steps:

1. In the "Options" menu, select the "Manage general station description files (GSD)" command.
2. Click on the "Find unused GSDs" button in the "GSDs in the project" tab.
3. If GSD files that are no longer needed were found in the project data, you can now delete them. To do so, click the "Delete" button.

**Note**

Unused GSD files are only available if at least one GSD-based hardware component was added to the configuration and then removed from the configuration. Unused GSD files in the project libraries are included in the search. GSD-based hardware components that are still being used in the configuration are not considered to be unused.

Installed GSD-based hardware components that are included in the hardware catalog but have not been used in the hardware configuration of the project yet, could not have stored unused GSD data in the project.

GSD files that are no longer needed are deleted from the project data. The GSD-based hardware component is still available in the hardware catalog and, if necessary, can be added to the configuration once again. The necessary GSD data are once again copied to the project data in this case.

> **Note**
>
> If you delete a GSD-based hardware component with "Options &gt; Manage general station description files (GSD) &gt; Installed GSDs", it is deleted from the hardware catalog. However, unused GSD files of this hardware component can still be a part of the project data and can be deleted with the function for finding the unused GSD files.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Actions that cannot be undone**  When you delete GSD files that are not being used as an action, the action stack for actions that can be undone is deleted. This means the action of deleting unused GSD files as well as all previous actions can no longer be undone. |  |

---

**See also**

[Basics of undoing and redoing actions](Introduction%20to%20the%20TIA%20Portal.md#basics-of-undoing-and-redoing-actions)

##### Changing the revision of a GSD file

###### Changing the revision of a GSD file

You can change the revision of a GSD file for an IO device:

- Only for the current IO device
- All suitable IO devices within the IO system
- All suitable IO devices within the complete project

First, all existing GSD files for the current IO device are shown. The only difference between the GSD files shown is their revision status. The currently used GSD file is highlighted.

###### Requirement

- The I/O data is the same for all IO devices whose revision is to be changed.
- The article number has not changed.
- The number of submodules is identical.
- The configuration data has not changed.
- There must be no module or submodule in a slot that is invalid after the new GSD file has been created.

###### Procedure

To change the revision of one or more IO devices, proceed as follows:

1. Select the IO device whose GSD file revision is to be changed.
2. Click on the "Change revision" button under "General&gt; Catalog information" in the properties of the IO device.

   The "Change revision" dialog box opens.
3. Select the GSD revision you want to use in the "Available revisions" table.
4. Under "Use selected revision for", select the devices whose version are to be changed:

   - Only for the current IO device
   - For all suitable IO devices in the IO system
   - For all suitable IO devices in the project
5. Click the "Apply" button.

### Bus coupling with PN/PN coupler

This section contains information on the following topics:

- [Application and function](#application-and-function)
- [Linking Ethernet subnets](#linking-ethernet-subnets)

#### Application and function

##### Application

The PN/PN coupler is used to link two Ethernet subnets with one another and to exchange data. That way use data about input or output address areas or datasets can be used. The maximum size of the transferable input and output data is 1024 bytes. The division into input and output data is preferable, so that e.g. 800 byte input data and 200 byte output data can be configured.

As a device, the PN/PN coupler has two PROFINET interfaces, each of which is linked to one subnet.

In the configuration, two IO Devices are produced from this one PN/PN coupler which means that there is one IO Device for each station with its own subnet. The other part of PN/PN coupler in each case is known as the bus node. Once configuring is complete, the two parts are joined.

![Coupling two PROFINET IO subnets with one PN/PN coupler](images/24241308683_DV_resource.Stream@PNG-en-US.png)

Coupling two PROFINET IO subnets with one PN/PN coupler

##### Additional information

For additional information on "PN/PN couplers", refer to Service &amp; Support [on the Internet](http://support.automation.siemens.com/WW/view/en/44319532).

#### Linking Ethernet subnets

##### Linking Ethernet subnets with a PN/PN coupler

You can link Ethernet subnets with the standard device PN/PN coupler.

To link Ethernet subnets, follow these steps:

1. Create your Ethernet subnets.
2. Select the standard field devices in the hardware catalog. Find the PN/PN coupler as head module in the "PROFINET IO" folder.
3. In the network view, drag the two components X1 and X2 to the required version of the PN/PN coupler per drag-and-drop operation. The components form a device, but are shown separately to make handling easier.
4. Connect the Ethernet interface of the PN/PN coupler X1 to the first Ethernet subnet.
5. Connect the Ethernet interface of the PN/PN coupler X2 to the second Ethernet subnet.

   The Ethernet subnets are now linked through the two components of the PN/PN coupler.

   ![Linking Ethernet subnets with a PN/PN coupler](images/25025467787_DV_resource.Stream@PNG-de-DE.png)

   ![Linking Ethernet subnets with a PN/PN coupler](images/25025467787_DV_resource.Stream@PNG-de-DE.png)

### Integrating external tools

This section contains information on the following topics:

- [Integrating S7-external tools](#integrating-s7-external-tools)
- [Starting the SIMATIC S7-PCT](#starting-the-simatic-s7-pct)

#### Integrating S7-external tools

##### Introduction

Tools external to STEP 7 ("Device Tools") with a special call interface (Tool Calling Interface) can be used to configure distributed devices. Such devices are also referred to as "TCI capable".

The performance range of these tools exceeds the possibilities provided within GSD configuration, for example, they can provide expanded graphical input options.

Distributed devices can be as follows:

- PROFIBUS DP slaves
- Modules within a DP slave
- PROFINET IO devices
- Modules within an IO device

> **Note**
>
> **Warranty and liability**
>
> Siemens accepts no liability for third-party software (device tools) called with the TCI (Tool Calling Interface) or for proper interaction with the associated devices.

##### Requirement

The call interface of the tool complies with the TCI specification. Parameters and commands are forwarded to the distributed device via this call interface.

Such tools have to be installed using a setup provided by the manufacturer. The "S7-PCT" (Port Configuration Tool) device tool for IO-Link master modules and IO-Link devices is an exception; this is supplied with STEP 7. Special note: After the installation, the tool is not shown in the list of installed software or in the list of software products in the project.

The GSD file of the distributed device that is to be configured with the Device Tool must be installed.

##### Starting the device tool

The command for starting the device tool is available in the shortcut menu of the TCI-capable device in the shortcut menu of the graphical and tabular device view: "Start device tool".

---

**See also**

[Starting the SIMATIC S7-PCT](#starting-the-simatic-s7-pct)
  
[Using GSD files](Configuring%20PROFIBUS%20DP.md#using-gsd-files)

#### Starting the SIMATIC S7-PCT

##### Introduction

The "S7-PCT" (Port Configuration Tool) device tool is installed with STEP 7.

The tool is used to assign parameters to the ports of IO-Link modules such as 4SI IO-Link (S7-1200, ET 200S) or 4IOL+8DI+4DO (ET 200eco PN).

##### Requirement

You have configured the corresponding CPU, the DP slave or the IO device with an IO-Link module.

##### Procedure

To start via the graphical device view, follow these steps:

1. Select the IO-Link module in the device view.
2. Select "Start device tool" from the shortcut menu.

OR, to start with the tabular device view, follow these steps:

1. Select the IO-Link module in the device view.
2. Arrange the areas in the work area in such a way that the tabular device overview is visible (it is located between the device view and the inspector window).
3. Select the row with the IO-Link module in the device overview.
4. Select "Start device tool" from the shortcut menu.

##### Result

The tool starts and you can configure the ports.

---

**See also**

[Integrating S7-external tools](#integrating-s7-external-tools)

### Loading a configuration

This section contains information on the following topics:

- [Introduction to loading a configuration](#introduction-to-loading-a-configuration)
- [Downloading a configuration to a device](#downloading-a-configuration-to-a-device)
- [Loading a configuration to PG/PC](#loading-a-configuration-to-pgpc)

#### Introduction to loading a configuration

In order to commission a device, identical configurations must be stored on the programming device/PC and on the connected devices. To synchronize the configurations on the programming device/PC and the connected devices, you load a configuration. Configuration data can be loaded in two directions:

- From the programming device/PC to a device
- From the device to a PG/PC

---

**See also**

[Uploading project data from a device](Editing%20project%20data.md#uploading-project-data-from-a-device)
  
[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[Downloading a configuration to a device](#downloading-a-configuration-to-a-device)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[General information on loading to PG/PC](#general-information-on-loading-to-pgpc)
  
[Special features during startup (S7-1200)](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#special-features-during-startup-s7-1200)

#### Downloading a configuration to a device

##### Loading the hardware configuration

After you have inserted a new device in the project and configured it or if you have modified an existing hardware configuration, the next step is to load the current configuration to the device. This ensures that the same configuration is set on the programming device/PC and on the module that is physically present. Use the "Online &gt; [Download to device](Editing%20project%20data.md#downloading-project-data-to-a-device)" menu command for this.

In the first download, the complete hardware configuration is downloaded. In subsequent downloads, only changes to the hardware configuration are downloaded.

You have the following options for loading the hardware configuration:

- Loading in the device or network view
- Loading in the project tree
- Loading to an accessible device

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Perform load operation only in STOP mode**  Following loading, the machine or process may behave unexpectedly if the parameter assignment is incorrect. A CPU must be set to STOP mode for the load operation to rule out possible damage to equipment or personal injury. |  |

##### Special considerations for loading isochronous applications

Isochronous applications consist of a hardware configuration part and a software part.

Example: If you change the number of an IO system, the delay time, or the assignment of a process image partition of the isochronous I/O in the hardware configuration, this affects the parameters of the isochronous mode interrupt OB and thus also the software part.

With isochronous applications, you should always load the complete project (hardware and software). With partial loading (loading hardware and software separately at different times), inconsistencies can arise that, for example, can prevent CPU startup or isochronous operation of the application.

---

**See also**

[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[Downloading blocks in the "RUN" operating mode to the device (S7-1200, S7-1500)](Compiling%20and%20downloading%20PLC%20programs.md#downloading-blocks-in-the-run-operating-mode-to-the-device-s7-1200-s7-1500)

#### Loading a configuration to PG/PC

This section contains information on the following topics:

- [General information on loading to PG/PC](#general-information-on-loading-to-pgpc)
- [Loading specific device configurations](#loading-specific-device-configurations)
- [Loading configurations with web server](#loading-configurations-with-web-server)
- [Loading configurations with PROFIBUS](#loading-configurations-with-profibus)
- [Loading configurations with PROFINET](#loading-configurations-with-profinet)
- [Loading HMI devices](#loading-hmi-devices)
- [Going online with loaded configurations](#going-online-with-loaded-configurations)

##### General information on loading to PG/PC

###### Introduction

If you bring your PG/PC to a plant and the STEP 7 project used to create the configuration of this plant is not available, load the configuration to a new project on your PG/PC, for example. Use the "Online &gt; [Loading the device as new station (hardware and software)](Editing%20project%20data.md#uploading-project-data-from-a-device)" menu command for this.

The list of accessible devices in the project tree is always used when loading a device to your programming device.

###### Requirements

- The hardware configuration in the device must be created in TIA Portal, V12 or higher. A hardware configuration present in the device that was created with an older version cannot be loaded and must be [upgraded](Editing%20projects.md#upgrading-projects-1).
- Modules present in the device from GSD (ML), HSPs, or service packs must be installed in TIA Portal on the PG/PC.
- A project must be open. This project can be a new (empty) project or an existing project.
- The opened project is in offline mode.

###### Scope of load operation

The following list shows an overview of the loadable components of a configuration:

- The device (e.g., a CPU) with all I/O modules and all parameter settings
- PROFIBUS master systems and all PROFIBUS-relevant settings
- PROFINET IO systems and all PROFINET-relevant settings
- I devices and I slaves
- Settings for direct data exchange

After loading a CPU, all other modules within the address area of the CPU are also loaded.

The following connections are also loaded when the configuration is loaded:

- S7 connections (including routed connections) in combined PB/IE networks, including via IE-CP or PB-CM interfaces. S7 connections are automatically accepted as configured at one end when a device configuration is loaded, even if the S7 connection was configured at both ends in the original project. When both connection partners are loaded, the connection is joined together again during the next compilation.
- TCP connections via CPU-internal Ethernet interface, UDP/ISOonTCP connections, and TCP, UDP, ISO, and ISOonTCP connections via IE-CP interface
- Connections via the OUC connection parameter assignment for projects from STEP 7 V13 and higher

> **Note**
>
> The hardware configuration loaded to PG/PC is not completely identical to the configuration originally loaded to the device. Note the additional information on loading, in particular with regard to partially loaded configuration data in the case of cross-device communication.
>
> Loading PC systems, such as WinAC or PC-based automation, is not possible.

---

**See also**

[General information on loading](Editing%20project%20data.md#general-information-on-loading)

##### Loading specific device configurations

###### Information on loading

When device configurations are loaded to the PG/PC, all assigned parameters are transferred from the device to the project. If the CPU is connected to a subnet, all parameters of the device are loaded and the CPU is displayed in the network view as networked.

> **Note**
>
> CPUs reset to their factory settings do not have any hardware configuration. Therefore, nothing is loaded in this case after "Load to PG/PC" is selected in the "Online" menu.

###### **Loading S7-300/400 configurations**

To avoid conflicts when loading a device to an existing project, the following rules must be followed:

- Device names for CPUs, PROFIBUS slaves (DP slaves, I-slaves) and PROFINET devices (IO devices, I devices) must be unique
- The combination of network name, subnet ID, and IP/DP address for modules must be unique

If conflicts occur, the load operation is canceled and an alarm provides information about the problems that occurred. You can then adapt the project correspondingly or install missing components and then repeat the load operation.

Alarm configurations are not loaded to PG/PC.

###### **Loading S7-1200/1500 configurations**

Take the following into consideration when loading:

- CPUs of the S7-1200 series with firmware version V1.0 are not supported when loading.
- Device-specific diagnostic interrupts of the S7-1200 are not supported when loading. For device-specific diagnostic interrupts of the S7-1200 to be generated on the PG/PC once again, the hardware configuration must be compiled once again.
- Module comments of the S7-1200/1500 are loaded from the device to the PG/PC if the same project language is set that was used during loading to the device. You can deselect the loading of comments, if desired.

> **Note**
>
> All types of PC systems, such as WinAC, Embedded Controller, CP 1616 or PC CPs, do not support loading to PG/PC.

###### **Loading distributed I/O**

The following functionalities and settings of the distributed I/O are loaded:

- DP master systems/IO systems with associated DP masters/IO controllers (CPUs and CPs), DP slaves/IO devices, the utilized modules and their parameter assignment and properties, such as options handling, status bytes, or SYNC/FREEZE
- Connection of process image partitions (PIP) to organization blocks (OB). Applies to the module and OB properties
- Configured hardware interrupts with the associated properties
- DP master systems with I-slave
- CPs as PROFIBUS I-slave or PROFINET I-device
- Direct data exchange

Master-slave relationships between the I-slave/I-device and assigned DP master/IO controller are only established in the project if both the master as well as the I-slave are loaded to the PG. It does not matter whether you load the DP master/IO controller or the I-slave/I-device first. As soon as both devices are loaded, the master-slave/controller-device relationships will also be re-established.

###### **Loading subnets and devices with MPI, PROFIBUS, Ethernet, and PtP**

The following special considerations apply to loading subnets and end points of connections for MPI, PROFIBUS, Ethernet, and PtP with their respective connection properties:

- If a device with PROFIBUS interface is loaded, the bus parameters of the device will initially be different from the settings in the original project. The bus parameters will only match those of the original project after all devices involved are loaded and no additional devices are on the same bus.
- Passive communication devices that are not connected as DP slaves or IO devices to a corresponding master system or IO system do not participate in the data exchange. They are therefore not loaded.
- All devices involved should therefore be loaded for cross-device configurations. A warning is output during compiling of the project for missing network stations. Missing routing information due to communication stations that are not loaded is displayed as warning during compilation. If the configuration is loaded from the PG/PC back to the device, different routing information results.

When you compile the project after loading devices to the PG/PC, STEP 7 checks if all devices to which communication relationships have been configured are available. If devices are missing, you receive an alarm with the number of missing communication stations.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Cross-device communication**  When you load a configuration with cross-device communication to the PG/PC, you must also load all corresponding network stations to the PG/PC. If required network stations are missing and the configuration is loaded back to the device, there is no guarantee that cross-device communication is working again. |  |

---

**See also**

[Upgrading projects](Editing%20projects.md#upgrading-projects-1)
  
[Creating configurations](#creating-configurations)
  
[Configuring distributed I/O systems](Configuring%20PROFIBUS%20DP.md#configuring-distributed-io-systems)
  
[Configuring distributed I/O systems (S7-1200)](#configuring-distributed-io-systems-s7-1200)

##### Loading configurations with web server

###### Information on loading

The hardware configuration of a CPU also contains the Web server settings. A number of restrictions apply to loading a Web server configuration to the PG/PC:

- The assignment of the Web server language and project language is not loaded for S7-300/400. The project texts are not loaded and an alarm is output that no project languages are assigned. The languages assigned in STEP 7 are loaded without restriction for S7-1200/1500 CPU.
- User administration data of the S7-1200/1500 can be loaded but not edited. You can use a check box to select whether you want to use the existing data as read-only data or discard these data and enter new data.
- Watch tables of the Web server are not loaded.

The source files of the user-defined web pages (HTML pages, Java scripts, etc.) are not loaded. The program blocks generated during loading can only be edited if you enter the properties and the HTML page yourself.

---

**See also**

[Information about the web server (S7-1200)](Configuring%20automation%20systems.md#information-about-the-web-server-s7-1200)
  
[Information about the web server (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#information-about-the-web-server-s7-300-s7-400-s7-1500)

##### Loading configurations with PROFIBUS

###### Information on loading

A DP master is loaded to PG/PC. The DP master system and all connected DP slaves are inserted into the project. The respective settings remain unchanged. If a suitable PROFIBUS subnet has already been created, the loaded devices with PROFIBUS interface are connected to the existing subnet.

As a prerequisite for loading DP master systems with standard slaves, the corresponding GSD files must be installed in the TIA Portal and available in the hardware catalog. If a required GSD file is not available in the same version as in the device, differences are identified during the consistency check.

> **Note**
>
> Direct data exchange in a configuration is only loaded if all communication partners involved in the direct data exchange are loaded to the PG/PC.

###### Isochronous mode

Note the following when loading DP master systems with activated PROFIBUS functionality "Isochronous mode":

- Bus parameters and the settings for isochronous mode are only identical after the device is loaded to the PG/PC if all devices relevant for calculation of isochronous mode are loaded.
- Only mono-master systems with isochronous mode are supported. Therefore, only configurations with just one DP master on the PROFIBUS subnet are loaded.

###### I-slave

Master-slave relations between DP master and I slave are only established in the project if both the DP master and the I slave are downloaded to the PG. It does not matter whether you load the DP master or the I-slave first. If you load the DP master from a DP master system with connected I-slave, the DP master and its DP slaves are loaded. An I-slave proxy is loaded as dummy module for an involved I-slave.

For I-slave proxy devices:

- DP master can be complied and loaded
- Properties are displayed but cannot be changed
- Diagnostics in the project tree is not carried out

In the network view, proxy devices are represented with a question mark:

It is possible to load a DP master with connected I-slave proxy from the PG/PC to the device.

###### Replacing the I-slave proxy

In order to edit the I-slave in the project, you must load the I-device from the device to the PG/PC. The I-slave proxy is hereby replaced by the full I-slave with its subordinate DP slaves.

You have the following options for replacing the I-slave proxy with the corresponding I-slave:

- In the menu bar with the command "Online &gt;Upload device as new station (hardware and software)
- With selected I-slave proxy using the shortcut menu command "Upload from device &gt; Hardware and software".
- In the toolbar with the button "Upload from device".

> **Note**
>
> The replacement of I-slave proxy devices is only possible if the required I-device is available in the hardware catalog.
>
> I-slaves protected by a password are not loaded.

---

**See also**

[Configurations involving PROFIBUS DP](Configuring%20PROFIBUS%20DP.md#configurations-involving-profibus-dp)
  
[Using GSD files](Configuring%20PROFIBUS%20DP.md#using-gsd-files)
  
[Configurations involving PROFIBUS DP (S7-1200)](#configurations-involving-profibus-dp-s7-1200)
  
[Using GSD files (S7-1200)](#using-gsd-files-s7-1200)

##### Loading configurations with PROFINET

###### Information on loading

If you have selected a CPU in the list of accessible devices and perform an load operation to PG/PC, all IO controllers and IO devices associated with this device along with their IO systems will be loaded. Settings for the topology are also transferred. If there is already a suitable Ethernet network in the project, the loaded devices are integrated into the existing network.

Relationships between the IO controllers and IO devices are only established within the project if both the IO controller as well as the I-device are loaded to the PG. It does not matter whether you load the IO controller or the I-devices first.

###### **Supported functions**

The following functionalities and settings are loaded:

- PROFINET configurations (RT and IRT) in IO systems with the associated IO controllers (CPUs and CPs), IO devices, and the modules used
- Logical addresses and interface properties
- Port interconnections
- Isochronous mode
- Sync domains/MRP domains
- Redundancy role "Client" or "Manager" for MRP configurations

> **Note**
>
> Empty Sync domains and MRP domains are not included in the loading.

###### **GSD-based IO devices**

As a prerequisite for loading GSD-based IO devices, the corresponding GSD files must be installed in the TIA Portal and available in the hardware catalog. If a required GSD file is not available in the same version as in the device, differences are identified during the consistency check.

###### **I-device**

If you load the IO controller from an IO system with connected I-device, the IO controller and its IO devices will be loaded. An I-device proxy is loaded as dummy module for an involved I-device. The CPU parameter assignment, including the parameter assignment of the CPU's "own" (subordinate) IO system, is missing in the I-device proxy. Only the interface to the higher-level IO controller is loaded.

![I-device](images/61194545291_DV_resource.Stream@PNG-en-US.png)

For I-device proxy devices:

- IO controller can be compiled and loaded
- Properties are displayed but cannot be changed
- Diagnostics in the project tree is not carried out

In the network view, proxy devices are represented with a question mark:

![I-device](images/60522283019_DV_resource.Stream@PNG-de-DE.png)

It is possible to load an IO controller with connected I-device proxy from the PG/PC to the device.

###### Replacing the I-device proxy

In order to edit the I-device in the project, you must load the I-device from the device to the PG/PC. This replaces the I-device proxy with the complete I-device along with its subordinate IO devices.

You have the following options for replacing the I-device proxy with the corresponding I-device:

- In the menu bar with the command "Online &gt;Upload device as new station (hardware and software)
- With selected I-device proxy using the shortcut menu command "Upload from device &gt; Hardware and software".
- In the toolbar with the button "Upload from device".

> **Note**
>
> The replacement of I-device proxy devices is only possible if the required I-device is available in the hardware catalog.
>
> I-devices protected by a password are not loaded.
>
> An I-device proxy representing a SIMOTION I-device cannot be loaded and replaced.

###### **Configurations with IE/PB link**

If one of the following configurations with IE/PB Link PN IO as PROFINET IO device is present, the complete configuration with all subordinate PROFIBUS devices is loaded:

- CPU/CP of S7-300/400
- PC station and connected PROFIBUS master system

The complete configuration consists of the following:

- CPU
- CP configuration
- PROFINET IO system with connected IE/PB link
- PROFIBUS master system of the IE/PB link with connected DP slaves

An example configuration consists of an S7-300 CPU with a CP as PROFINET IO controller. An IE/PB link as IO device is connected to the IO controller. As the PROFIBUS DP master, the IE/PB link polls a PROFIBUS DP slave, e.g., ET 200L. If you load the CPU from the device to the PG/PC, the complete configuration is loaded.

> **Note**
>
> If the IE/PB link is not operated as a PROFINET IO proxy but rather as a gateway in standard mode, the IE/PB link functions as a CPU and can be loaded separately.

###### **Loading Shared Devices**

The following applies to loading comments: If an input/output module with the Module-internal Shared Input (MSI) or Module-internal Shared Output (MSO) function consists of only one submodule, the submodule does not have its own comment. Instead, it uses the comment of the input/output module. The module must be subdivided into several submodules for the input/output module and all submodules to have their own comment fields.

---

**See also**

[Configuring PROFINET IO](#configuring-profinet-io)

##### Loading HMI devices

###### Information on loading

We distinguish between the following cases when loading HMI devices to PG/PC:

- HMI devices connected to a DP master as DP slave or to an IO controller as IO device are loaded as DP slave or IO device respectively (for example, PP 17-I PROFIsafe).
- HMI devices in a master system as I-slave or in an IO system as I-device are loaded as I-slave proxies or [I-device proxies](#loading-configurations-with-profinet) (for example, SIMATIC Comfort Panels). The settings of the device proxy are read-only.
- HMI devices are not loaded if they are connected to a subnet (PROFIBUS or PROFINET) but not to a master system or IO system (for example, KP600 Basic color DP).

##### Going online with loaded configurations

You can go online with the loaded project or with loaded portions of the project.

###### Requirement

The hardware configuration loaded from the device to the PG/PC has been compiled. The statuses of the central and distributed modules are only correctly displayed after compilation.

> **Note**
>
> If you go online before compiling, the diagnostics icon “?” is displayed (diagnostics not possible). A corresponding alarm is displayed under "Info &gt; General" in the Inspector window.

###### Dependencies

Depending on how completely the hardware configuration was loaded to the PG, restrictions apply to going online and to diagnostics:

- Completely loaded device with all associated central and distributed modules, such as DP slaves or IO devices:   
  Going online and diagnostics are possible.
- Loaded device with connected I-devices/I-slaves:

  - I device/I slave is not loaded: Going online for the device and its modules is possible. For the dependent components of the configuration that are not loaded, device proxies are handled with only minimum diagnostics support. The online status is represented as an icon. The standard diagnostics is shown in the online and diagnostics view. I&amp;M data are not loaded.
  - I device/I slave is also loaded: Going online is possible for all devices; diagnostics is fully supported.

---

**See also**

[Connecting devices online](Using%20online%20and%20diagnostics%20functions.md#connecting-devices-online)

## Additional information on configurations

This section contains information on the following topics:

- [Communications modules and network components](Communications%20modules%20and%20network%20components.md#communications-modules-and-network-components)
- [Identification systems](Identification%20systems.md#identification-systems)
- [Distributed I/O](#distributed-io)
- [IPv4 routing for CM/CP 1500](#ipv4-routing-for-cmcp-1500)
- [IPv6 configuration](#ipv6-configuration)

### Distributed I/O

This section contains information on the following topics:

- [Distributed I/O systems](#distributed-io-systems)
- [Configuring HART variables](#configuring-hart-variables)
- [ET 200iSP](#et-200isp)
- [ET 200eco PN](#et-200eco-pn)
- [ET 200SP](#et-200sp)
- [ET 200AL](#et-200al)
- [ET 200MP](#et-200mp)
- [ET 200M](#et-200m)
- [ET 200S](#et-200s)
- [ET 200pro](#et-200pro)

#### Distributed I/O systems

##### SIMATIC ET 200 - The right solution for all applications

SIMATIC ET 200 provides the most varied range of distributed I/O systems.

- Solutions for use in the control cabinet
- Solutions without control cabinet directly at the machine

Additionally, there are also components that can be used in explosive areas. SIMATIC ET 200 systems for construction without a control cabinet are contained in robust, glass-fibre reinforced plastic casing and are therefore shock-resistant, resistant to dirt and watertight.

Their modular design allows the ET 200 systems to be easily scaled and expanded in small steps. Fully-integrated auxiliary modules lower costs and also provide a wide range of possible applications. There are several combination possibilities available:

- Digital and analog I/OS
- Intelligent modules with CPU functions,
- Safety technology,
- Pneumatics,
- Frequency converters
- Various technology modules.

Communication via PROFIBUS and PROFINET, uniform engineering, clear diagnostic possibilities as well as optimal connection to SIMATIC controller and HMI devices vouch for the unique consistency provided by Totally Integrated Automation.

The following table provides an overview of I/O devices for use in the control cabinet:

| I/O device | Properties |
| --- | --- |
| ET 200L | - Cost-effective digital block I/O - Digital electronic blocks up to 32 channels |
| ET 200M | - Modular design with standard modules from SIMATIC S7-300 - Failsafe I/O modules - Use in hazardous areas up to Zone 2, sensors and actuators up to Zone 1 - High level of plant availability, for example by plugging and unplugging during operation |
| ET 200MP | - Modular design with standard SIMATIC S7-1500 modules - Isochronous PROFINET IO with send clocks up to 250 µs - IO device with PROFINET IO interface - DP slave with PROFIBUS DP interface - Technology modules for counting, positioning, time-based IO |
| ET 200S | - Highly modular design with multiple conductor connections - Multifunctional due to a wide range of modules - I-device - Use in explosive areas (Zone 2) |
| ET 200S COMPACT | - Highly modular design with multiple conductor connections - Multifunctional due to a wide range of modules - Use in explosive areas (Zone 2) - Integrated DE/DA |
| ET 200SP | - Compact modules - Permanent wiring with one or more wire connection - PROFINET interface with 3 ports - Isochronous PROFINET IO with the profiles PROFIsafe and PROFIenergy - I-device - Modules for counting, positioning, weighing and measuring - Fail-safe CPUs and modules |
| ET 200iSP | - Modular design, also possible with redundancy - Robust and intrinsically safe design - Use in explosive areas up to Zone 1/21; sensors and actuators even up to Zone 0/20 - High level of plant availability, for example by plugging and unplugging during operation |
|  |  |

The following table provides an overview of I/O devices for use without a control cabinet:

| I/O device | Properties |
| --- | --- |
| ET 200AL | - Simple installation in all locations, in the smallest spaces - Connection to PROFINET IO, PROFIBUS DP or ET 200SP - High degree of protection IP65/IP67   For temperatures from -25 °C to   +55 °C, acceleration up to 5 g - Connection of sensors and actuators using M8 and M12 connector system |
| ET 200eco PN | - Cost-efficient, space-saving block I/OS - Digital modules up to 16 channels (also configurable) - Analog modules, IO-link master and load voltage distributor - PROFINET connection with 2-port switch in each module - Can be flexibly distributed via PROFINET in line or star shape directly within the plant |
| ET 200eco | - Cost-effective digital block I/O - Flexible connection possibilities - Failsafe modules - High level of plant availability |
| ET 200pro | - Modular design with compact housing - Easy assembly - Multifunctional due to a wide range of modules - I-device - High level of plant availability due to plugging and unplugging during operation and permanent wiring - Comprehensive diagnostics |
| ET 200R | - Specially for use on robots - Assembled directly on the chassis - Resistant to weld spatter due to robust metal housing |
|  |  |

---

**See also**

[Documentation on ET 200S](http://support.automation.siemens.com/WW/view/en/1144348/0/en)
  
[Documentation on ET 200M](http://support.automation.siemens.com/WW/view/en/1142798/0/en)
  
[Documentation on ET 200pro](http://support.automation.siemens.com/WW/view/en/21210852/0/en)
  
[Documentation on ET 200iSP](http://support.automation.siemens.com/WW/view/en/28930789/0/en)
  
[Documentation on ET 200L](http://support.automation.siemens.com/WW/view/en/1142908/0/en)
  
[Documentation on ET 200R](http://support.automation.siemens.com/WW/view/en/11966255/0/en)
  
[Documentation on ET 200eco PN](http://support.automation.siemens.com/WW/view/en/29999018/0/en)
  
[Documentation on ET 200eco](http://support.automation.siemens.com/WW/view/en/12403834/0/en) 
  
[Documentation on ET 200SP](http://support.automation.siemens.com/WW/view/en/84133942/0/en)
  
[Documentation on ET 200MP](http://support.automation.siemens.com/WW/view/en/86140384/en)
  
[Documentation on ET 200AL](http://support.automation.siemens.com/WW/view/en/95242965/0/en)

#### Configuring HART variables

##### Introduction

Numerous HART field devices make available additional measured quantities (e.g. sensor temperature). These can be read if they are set accordingly in the field device configuration. Using the HART variables. it is possible to apply the set measured values directly from the field device into the I/O area of your automation system.

Regardless of the number of configured channels, a maximum of 8 HART variables can be assigned for HART modules and no more than 4 HART variables per channel. You assign the HART variables to a channel in the properties for the module ("HART variable settings" area). To do this, check the manual of the corresponding module.

##### Address assignment

By default, the HART modules occupy 16 input/output bytes (user data). If you configure HART variables, the modules occupy an additional 5 bytes for each HART variable.

If you use all 8 HART variables, the HART input module occupies a total of 56 input/output bytes (16 bytes + 8 x 5 bytes = 56 bytes).

The "None" configuration occupies no additional input bytes.

##### Configuration of HART variables

You can configure up to 4 HART variables for a channel

- PV (Primary Variable)
- SV (Secondary Variable)
- TV (Tertiary Variable)
- QV (Quaternary Variable)

CiR is a placeholder that reserves the address space for a HART variable. You must configure the HART variables you are not using with the "None" parameter.

##### Configuration of HART variables

Each HART variable occupies 5 bytes of input data and is structured as follows:

![Configuration of HART variables](images/69198184971_DV_resource.Stream@PNG-en-US.png)

The quality code can accept different values depending on the module. To do this, check the manual of the corresponding module.

---

**See also**

[Documentation for HART analog modules](http://support.automation.siemens.com/WW/view/en/22063748)

#### ET 200iSP

This section contains information on the following topics:

- [ET 200iSP Distributed I/O Station](#et-200isp-distributed-io-station)
- [Assigning the channel and IEEE tag](#assigning-the-channel-and-ieee-tag)
- [Assigning parameters to reference junctions for thermocouples](#assigning-parameters-to-reference-junctions-for-thermocouples)
- [Fundamentals of Time Stamping](#fundamentals-of-time-stamping)
- [Counting](#counting)
- [Frequency measurement](#frequency-measurement)

##### ET 200iSP Distributed I/O Station

###### Definition

The ET 200iSP distributed I/O station is a highly modular and intrinsically safe DP slave with degree of protection IP 30.

###### Area of application

The ET 200iSP distributed I/O station can be operated in potentially explosive atmospheres characterized by gas and dust:

| Approval | ET 200iSP Station* | Inputs and outputs |
| --- | --- | --- |
| ATEX  IECEx | Zone 1, Zone 21 | up to Zone 0, Zone 20 ** |
| Zone 2, Zone 22 | up to Zone 0, Zone 20 ** |  |
| * In combination with an appropriate enclosure ** for electronic module 2 DO Relay UC60V/2A: up to Zone 1, Zone 21 |  |  |

The ET 200iSP distributed I/O station can, of course, also be used in the safety area.

You can insert almost any combination of ET 200iSP I/O modules directly next to the interface module that transfers the data to the DP master. This means you can adapt the configuration to suit your on-site requirements.

Every ET 200iSP consists of a power supply module, an interface module and a maximum of 32 electronic modules (for example digital electronics modules). Remember not to exceed the maximum current consumption.

###### Terminal modules and electronic modules

In principle, the ET 200iSP distributed I/O station consists of various passive terminal modules onto which you plug the power supply and the electronic modules.

The ET 200iSP is connected to PROFIBUS RS 485-IS by means of a connector on terminal module TM-IM/EM. Every ET 200iSP is a DP slave on the PROFIBUS RS 485‑IS.

###### DP master

All ET 200iSP modules support communication with DP masters that are compliant with IEC 61784-1:2002 Ed1 CP 3/1 and operate with "DP" transmission protocol (DP stands for distributed peripherals or distributed I/O).

---

**See also**

[Documentation on ET 200iSP](http://support.automation.siemens.com/WW/view/de/28930789/0/en)

##### Assigning the channel and IEEE tag

###### Properties

Analog electronic modules 4 AI I 2WIRE/HART, 4 AI I 4WIRE/ HART and 4 AO I HART support up to four IEEE tags.

The process input image (PII) provides up to 20 bytes per module for the IEEE tags. Thus, four blocks of 5 bytes each are available for the four IEEE tags within the PII.

###### Requirements

The HART field device must support the assigned number of IEEE tags.

###### Assigning IEEE tags

You assign the IEEE tags of the field devices to any one of the four blocks in the PII.

![Assigning IEEE tags](images/20280324491_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Documentation on ET 200iSP](http://support.automation.siemens.com/WW/view/de/28930789/0/en)

##### Assigning parameters to reference junctions for thermocouples

###### Compensation of the reference junction temperature

There are various ways of obtaining the reference junction temperature in order to get an absolute temperature value from the temperature difference between the reference junction and the measuring point.

Compensation of the reference junction temperature

| Option | Explanation | Reference junction parameters |
| --- | --- | --- |
| No compensation | You record not only the temperature of the measurement point. The temperature of the reference junction (transition from Cu line to thermocouple line) also affects the thermo-electromotive force. The measured value then includes an error. | None |
| Use of a Pt100 Climatic Range resistance thermometer to record the reference junction temperature (best method) | You can record the reference junction temperature using a resistance thermometer (Pt100 Climatic Range). If parameterized accordingly, this temperature value is distributed to the 4 AI TC modules in the ET 200iSP where it is offset against the temperature value obtained at the measuring location.  Number of reference junctions: 2 | The parameter assignment of the IM 152 and the 4 AI TC must be coordinated:  - 4 AI RTD assigned parameters for Pt100 climatic range in correct slot; - 4 AI TC: Reference junction : "yes"; select reference junction number "1" or "2" - IM 152-1:Assignment of the reference junction to a slot with 4 AI RTD; channel selection; |
| Internal compensation 4 AI TC | The TC sensor module (temperature sensor) is mounted onto the terminals of terminal module EM 4 AI TC. The temperature sensor reports the temperature of the terminals to the 4 AI TC. This value is then calculated together with the measured value from the channel of the electronic module. | - 4 AI TC: Reference junction number "internal" |

###### Compensation by means of a resistance thermometer at the 4 AI RTD

If thermocouples that are connected to the inputs of the 4 AI RTD have the same reference junction, compensate by means of a 4 AI RTD.

For both channels of the 4 AI TC module, you can select "1", "2" or "internal" as the reference junction number. If you select "1" or "2", the same reference junction (RTD channel) is always used for all four channels.

###### Setting parameters for the reference junction

You set the reference junctions for the 4 AI TC electronic modules by means of the following parameters:

Reference junction parameters

| Parameter | Module | Range of values | Explanation |  |
| --- | --- | --- | --- | --- |
| Slot reference junction 1 to slot 2 | IM 152 | none, 4 to 35 |  | With this parameter, you can assign up to 2 slots (none, 4 to 35), on which the channels for reference temperature measurement (calculating the compensation value) are located. |
| Input reference junction 1 to 4 input reference junction | IM 152 | RTD on channel 0  RTD on channel 1  RTD on channel 2  RTD on channel 3 |  | This parameter allows you to set the channel (0/1/2/3) for measuring the reference temperature (calculation of the compensation value) for the assigned slot. |
| Reference junction E0 to reference junction E3 | 4 AI TC | None  yes |  | This parameter allows you to enable the use of the reference junction. |
| Reference junction number | 4 AI TC | 1  2  Internal |  | This parameter allows you to assign the reference junction (1, 2) that contains the reference temperature (compensation value). |

---

**See also**

[Documentation on ET 200iSP](http://support.automation.siemens.com/WW/view/de/28930789/0/en)

##### Fundamentals of Time Stamping

###### Properties

Time stamping is possible with the IM 152 in customer applications using FB 62 (FB TIMESTMP).

###### Principle of operation

A modified input signal is assigned a time stamp and stored in a buffer (data record). If time stamped signals exists or a data record is full, a hardware interrupt is generated to the DP master. The buffer is evaluated with "Read data record". Special messages are generated for events that influence the time stamping (communication with the DP master interrupted, frame failure of time master, ...).

###### Parameter Assignment

With the parameter assignment you define which IM 152 user data will be monitored. For the time stamping these are digital inputs that are monitoring for signal changes.

| Parameter | Setting | Description |
| --- | --- | --- |
| Time stamping | - disabled - enabled | Activate the time staming for the channels of the electronics module 8 DI NAMUR. |
| Edge evaluation incoming event | - rising edge - falling edge | Determine the type of signal change that will be time-stamped. |

##### Counting

This section contains information on the following topics:

- [Count properties](#count-properties)
- [Principle of operation](#principle-of-operation)
- [Configuring counters](#configuring-counters)
- [Assigning parameters to counters](#assigning-parameters-to-counters)

###### Count properties

###### Counting functions

The 8 DI NAMUR electronics module has configurable counting functions:

- 2 x 16-bit up counters (standard counting function) or
- 2 x 16-bit down counters (standard counting function) or
- 1 x 32-bit down counter (cascading counter function)
- Setting a setpoint with the PIQ
- GATE function
- You can configure the control signals of the counters:

  - Configuration channel 0..1: "Counter", channel 2..7: "DI": Two counters are configured. The control signals of the counters are stored in the PIQ (process image output).
  - Configuration channel 0..1: "Counter", channel 2..7: "Control": Two counters are configured. The control signals of the counters are stored in the PIQ (process image output). They are also controlled by the digital inputs of the 8 DI NAMUR.

---

**See also**

[Principle of operation](#principle-of-operation)
  
[Configuring counters](#configuring-counters)
  
[Assigning parameters to counters](#assigning-parameters-to-counters)

###### Principle of operation

###### 16-bit up counters (standard counting function)

The counting range is 0 to 65,535.

With each count pulse at the digital input, the count is incremented by 1. Once the count limit is reached, the counter is reset to 0 and it counts up again from this value.

If there is counter overflow, the corresponding output is set in the PII.

A positive edge of the Reset output control signal resets the output in the PII. This does not affect the current count value.

In 16-bit up counting operations, the system does not set any outputs in the PIQ. These are always reset.

The positive edge of the Reset counter control signal sets the counter to 0 and resets the set counter output.

The GATE control signal pauses the counting on a positive edge. Count pulses are processed at the digital input again, but only at the negative edge. The Reset counter control signal is also effective when GATE is active.

![16-bit up counters (standard counting function)](images/20554891019_DV_resource.Stream@PNG-en-US.png)

###### 16-bit down counters (periodic counting function)

The maximum counting range is always 65,535 to 0.

When the counter is started, the actual value is set to the selected setpoint. Each counted pulse reduced the actual value by 1. Once the actual value reaches 0, the corresponding output in the PII is turned on and the actual value is set to the selected setpoint. The counter then counts down from this value.

The positive edge of the Reset counter control signal resets the selected setpoint and the corresponding output in the PII.

A positive edge of the Reset output control signal resets the output in the PII. This does not affect the current count value.

The GATE control signal pauses the counting on a positive edge. At the same time, the assigned output in the PII is reset. Count pulses are processed at the digital input again, but only at the negative edge. The Reset output and Reset counter control signals are also effective when GATE is active.

The setpoint of the counter is set and changed using the PIQ. The setpoint is adopted on a positive edge of the Reset counter control signal or when the counter has reached zero.

![16-bit down counters (periodic counting function)](images/20554909579_DV_resource.Stream@PNG-en-US.png)

###### 32-bit down counter (cascading counter function)

The maximum counting range is always 4294967295 to 0.

The principle of operation is identical to that of the 16-bit down counter. Channel 1 has no function.

---

**See also**

[Count properties](#count-properties)

###### Configuring counters

###### Procedure

1. Using the mouse, pull module 8 DI Namur from the hardware catalog into distributed I/O station ET 200iSP.
2. Select the required configuration (channel 0..1: "Counter", channel 2..7: "DI" or "Control"). In the module properties (inspector window), you can find this setting under "Parameters &gt; Inputs &gt; Configuration".

###### Configuration channel 0..1: "Counter", channel 2..7: "DI"

- Assignment of the digital inputs on the electronic module 8 DI NAMUR

Assignment of digital inputs for channel 0..1: "Counter", channel 2..7: "DI":

| Digital input | Terminal | Assignment |
| --- | --- | --- |
| Channel 0 | 1, 2 | Counter 1 |
| Channel 1 | 5, 6 | Counter 2 (does not apply to 32-bit down counters) |
| Channel 2 | 9, 10 | Digital input 2 |
| Channel 3 | 13, 14 | Digital input 3 |
| Channel 4 | 3, 4 | Digital input 4 |
| Channel 5 | 7, 8 | Digital input 5 |
| Channel 6 | 11, 12 | Digital input 6 |
| Channel 7 | 15, 16 | Digital input 7 |

- Assignment of the process image input (PII)

  ![Configuration channel 0..1: "Counter", channel 2..7: "DI"](images/20554521099_DV_resource.Stream@PNG-en-US.png)
- Assignment of the process image output (PIQ)

  ![Configuration channel 0..1: "Counter", channel 2..7: "DI"](images/20554872459_DV_resource.Stream@PNG-en-US.png)

###### Configuration channel 0..1: "Counter", channel 2..7: "CONTROL"

With this configuration, you can also control the counters over the digital inputs.

- Assignment of the digital inputs on electronic module 8 DI NAMUR

  For further information on input assignments, refer to the technical data for electronic module 8 DI NAMUR.

Assignment of the digital inputs for 2 Count/ 6 Control

| Digital input | Terminal | Assignment |
| --- | --- | --- |
| Channel 0 | 1, 2 | Counter 1 |
| Channel 1 | 5, 6 | Counter 2 (does not apply to 32-bit down counters) |
| Channel 2 | 9, 10 | control signal GATE 1 |
| Channel 3 | 13, 14 | control signal GATE 2 |
| Channel 4 | 3, 4 | control signal Reset counter 1 |
| Channel 5 | 7, 8 | control signal Reset counter 2 |
| Channel 6 | 11, 12 | control signal Reset counter output 1 |
| Channel 7 | 15, 16 | control signal Reset counter output 2 |

- Assignment of the process image input (PII)

  Assignment is identical to configuration 0..1: "Counter", channel 2..7: "DI".
- Assignment of the process image output (PIQ)

  Assignment is identical to configuration 0..1: "Counter", channel 2..7: "DI".

---

**See also**

[Count properties](#count-properties)

###### Assigning parameters to counters

###### Parameters for the counting function

Only those parameters that are relevant for the counters are explained below. These belong to the parameters of electronic module 8 DI NAMUR and depend on the selected configuration:

Parameters for the counters

| Parameter | Setting | Description |
| --- | --- | --- |
| Sensor type counter inputs | - Channel disabled - NAMUR sensor - Single contact, no load resistance | Select the sensor for the respective counter of channels 0 or 1. |
| Mode for counter 1 | - Standard counting function - Periodic counting function - Cascaded counting function | Select the mode for counter 1. |
| Mode for counter 2 | - Standard counting function - Periodic counting function - Cascaded counting function | Select the mode for counter 2. This parameter is not relevant if you have set the "Mode for counter 1" parameter to "Cascaded counter function". |

---

**See also**

[Count properties](#count-properties)

##### Frequency measurement

This section contains information on the following topics:

- [Frequency measurement properties](#frequency-measurement-properties)
- [Principle of operation](#principle-of-operation-1)
- [Configuring frequency meters](#configuring-frequency-meters)
- [Assigning parameters for the frequency meters](#assigning-parameters-for-the-frequency-meters)

###### Frequency measurement properties

###### Properties

The electronic module 8 DI NAMUR allows the frequencies to be measured on channel 0 and 1:

- 2 frequency meters from 1 Hz to 5 kHz
- Configurable metering window (GATE)
- The signals of the frequency meter are read in by means of the digital inputs of the electronic module.

---

**See also**

[Principle of operation](#principle-of-operation-1)
  
[Configuring frequency meters](#configuring-frequency-meters)
  
[Assigning parameters for the frequency meters](#assigning-parameters-for-the-frequency-meters)

###### Principle of operation

###### Frequency measurement

The signal frequencies are identified from the input signals of channel 0 or 1 of the electronic module. To calculate the frequency the signals are measured within a configurable gate.

The frequency is displayed as 16-bit value in fixed-point format and transferred to the PII.

The frequency meter calculates the frequency according to the follow formula:

![Frequency measurement](images/20563965707_DV_resource.Stream@PNG-en-US.png)

###### Exceeding the input frequency

If the input frequency exceeds 5kHz, 7FFF<sub>H</sub> is reported as actual value. If the input frequency is above approx. 8 kHz it is no longer possible to display correct actual values.

---

**See also**

[Frequency measurement properties](#frequency-measurement-properties)

###### Configuring frequency meters

###### Procedure

1. Using the mouse, pull module 8 DI Namur from the hardware catalog into distributed I/O station ET 200iSP.
2. Select the required configuration (channel 0..1: "Trace", channel 2..7: "DI"). In the module properties (inspector window), you can find this setting under "Parameters &gt; Inputs &gt; Configuration".

###### Configuration 0..1: "Trace", channel 2..7: "DI"

Assignment of the digital inputs on electronic module 8 DI NAMUR

| Digital input | Terminal | Assignment |
| --- | --- | --- |
| Channel 0 | 1, 2 | Frequency counter 1 |
| Channel 1 | 5, 6 | Frequency counter 2 |
| Channel 2 | 9, 10 | Digital input 2 |
| Channel 3 | 13, 14 | Digital input 3 |
| Channel 4 | 3, 4 | Digital input 4 |
| Channel 5 | 7, 8 | Digital input 5 |
| Channel 6 | 11, 12 | Digital input 6 |
| Channel 7 | 15, 16 | Digital input 7 |

Assignment of process image input (PII) for configuration of channel 0..1: "Trace", channel 2..7: "DI"

![Configuration 0..1: "Trace", channel 2..7: "DI"](images/20563870347_DV_resource.Stream@PNG-en-US.png)

Assignment of the process image output (PIQ): The PIQ is not assigned.

---

**See also**

[Frequency measurement properties](#frequency-measurement-properties)

###### Assigning parameters for the frequency meters

###### Parameters for frequency meter

Only those parameters that are relevant for the frequency meters are explained below. These are part of the parameters of electronic module 8 DI NAMUR.

Parameters for the frequency meters

| Parameter | Setting | Description |
| --- | --- | --- |
| Sensor type frequency inputs | - Channel disabled - NAMUR sensor - Single contact, no load resistance | Select the sensor for the relevant frequency meter for channel 0 or 1. |
| Measuring window (GATE) | - 50 ms - 200 ms - 1 s | Select the required measuring window for channel 0 or 1.   To achieve the highest possible accuracy when metering frequencies, remember the following rules:  - High frequencies (&gt; 4 kHz): Set a low measuring window (50 ms) - Variable/medium frequencies: set medium measuring window (200 ms) - Low frequencies (&lt; 1 kHz): Set a high measuring window (1 s) |

---

**See also**

[Frequency measurement properties](#frequency-measurement-properties)

#### ET 200eco PN

This section contains information on the following topics:

- [ET 200eco PN Distributed I/O Device](#et-200eco-pn-distributed-io-device)
- [Parameter description analog input](#parameter-description-analog-input)
- [Parameter description analog output](#parameter-description-analog-output)

##### ET 200eco PN Distributed I/O Device

###### Definition

The ET 200eco PN distributed I/O device is a compact PROFINET IO device in degree of protection IP 65/66 or IP 67 and UL Enclosure Type 4x, Indoor use only.

###### Field of application

The fields of application of the ET 200eco PN are derived from its special properties.

- A robust design and degree of protection IP 65/66 or IP 67 make the ET 200eco PN distributed I/O device suitable in particular for use in rugged industrial environments.
- The compact design of the ET 200eco PN is particularly favorable for applications in confined areas.
- The easy handling of ET 200eco PN facilitates efficient commissioning and maintenance.

###### Properties

The ET 200eco PN has the following properties:

- Integrated switch with 2 ports
- Supported Ethernet services:

  - ping
  - arp
  - Network diagnostics (SNMP)
  - LLDP
- Interrupts

  - Diagnostics interrupts
  - Maintenance interrupts
- Port diagnostics
- Isochronous real-time communication
- Prioritized startup
- Device replacement without programming device
- Media redundancy
- Connection to intelligent sensors/actuators via IO link master interface module.

###### IO Controller

The ET 200eco PN can communicate with all IO Controllers that conform to IEC 61158.

ET 200eco PN can be configured on a CPU with advanced diagnostics.

---

**See also**

[Documentation on ET 200eco PN](http://support.automation.siemens.com/WW/view/en/29999018)

##### Parameter description analog input

###### Group diagnostics

You can generally enable and disable the diagnostics function of the device with this parameter.

The "Fault" and "Parameter assignment error" diagnostics functions are always independent of the group diagnostics.

###### Diagnostics, missing 1L+

If you enable this parameter, the check for missing supply voltage is enabled.

###### Diagnostics, sensor supply short circuit

If you enable this parameter, a diagnostics event is generated if a short-circuit of the sensor supply to ground is detected and the channel is enabled. The sensor supply is monitored for connectors X1, X3, X5 and X7. It is not possible to differentiate which connector has experienced the sensor short circuit.

###### Interference frequency suppression

With this parameter, you set the integration time of the device, based on the selected interference frequency. Select the frequency of the supply voltage used. Interference frequency suppression **Off** means 500 Hz, which corresponds to an integration time of 2 ms for a measurement channel.

###### Temperature unit

Specify the unit of the temperature measurement here.

###### Measurement type (channel-wise)

With this parameter, you set the measurement type, for example, voltage. For any unused channels, you must select the **disabled** setting. For a disabled channel, the conversion time and integration time of the channel = 0 s and the cycle time is optimized.

###### Measuring range

With this parameter, you set the measuring range of the selected measurement type.

###### Temperature coefficient (for RTD, thermoresistor)

The correction factor for the temperature coefficients (α-value) indicates by what extent the resistance of specific material changes relatively if the temperature increases by 1 ℃.

The α-values conform to EN 60751, GOST 6651, JIS C 1604 and ASTM E-1137.

The temperature coefficient depends on the chemical composition of the material.

###### Smoothing

Smoothing of the analog values produces a stable analog signal for further processing. The smoothing of analog values is useful when handling wanted signals (measured values) with a slow rate of change, for example, temperature measurements.

The measured values are smoothed by digital filtering. To achieve smoothing, the device generates a mean value from a specified number of converted (digitized) analog values.

You assign a maximum of four levels for the smoothing (none, weak, medium, strong). The level determines the number of module cycles, from which the mean value is generated.

The stronger the smoothing, the more stable the smoothed analog value and the longer it takes until the smoothed analog value is applied following a signal change (see the example below).

The figure below shows the number of cycles a module requires to apply the smoothed analog value at almost 100% after a step response, based on the smoothing function settings. The figure applies to all signal changes at the analog input. The smoothing value defines the number of cycles a module requires to reach 63% of the end value of the changed signal.

![Smoothing](images/22524367499_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Smoothing, weak |
| ② | Smoothing, medium |
| ③ | Smoothing, strong |

###### Diagnostics, wire break

When this parameter is enabled, the **Wire break** diagnostics event is generated when a wire break is detected.

Observe the rules outlined below to handle a wire break in the 1 to 5 V and 4 to 20 mA measuring ranges:

| Parameter | Event | Measured value | Explanation |
| --- | --- | --- | --- |
| Enable wire break<sup>1</sup> | Wire break | 7FFF<sub>H</sub> | Diagnostics, **wire break** |
| Wire break disabled<sup>1</sup>  Underflow enabled | Wire break | 8000<sub>H</sub> | Measured value after leaving the underrange  Diagnostic message **Lower limit value undershot** |
| Wire break disabled<sup>1</sup>  Underflow disabled | Wire break | 8000<sub>H</sub> | Measured value after leaving the underrange |
| <sup>1</sup> Measuring range limits for wire break detection and measuring range undershoot detection:  - 1 to 5 V: At 0.296 V - 4 to 20 mA: At 1.185 mA |  |  |  |

###### Diagnostics, underflow

If you enable this parameter, the **Underflow** diagnostics event is generated when the measured value reaches the underflow range.

###### Diagnostics, overflow

If you enable this parameter, the **Overflow** diagnostics event is generated when the measured value reaches the overflow range.

###### Reference junction for thermoresistor (TC)

A difference in temperature between the measuring point and the free ends of the thermocouple (terminal point) generates a voltage between the free ends, namely the thermoelectric voltage. The value of this thermoelectric voltage is determined by the temperature difference between the measuring point and the free ends and by the type of material combination of the thermocouple. Since a thermocouple always measures a temperature difference, the free ends at the reference junction must be maintained at a known temperature in order to determine the temperature of the measuring point.

If you specify **Internal compensation**, the temperature of the measuring point in the housing of the I/O device is measured. With the **External compensation** setting, you can connect a compensation box in series in order to increase the accuracy of the temperature measurement.

##### Parameter description analog output

###### Group diagnostics

You can generally enable and disable the diagnostics function of the device with this parameter.

The "Fault" and "Parameter assignment error" diagnostics functions are always independent of the group diagnostics.

###### Diagnostics, missing 1L+

If you enable this parameter, the check for missing supply voltage is enabled.

###### Diagnostics, sensor supply short circuit

When this parameter is enabled, the system generates a diagnostics event if it detects a short-circuit of the sensor supply to ground. This diagnostics function is activated when the group diagnostics function is enabled.

###### Response to CPU/Master STOP

Select how the module's outputs will respond to a CPU STOP:

- Shut down

  The I/O device goes to the safe state. The process image output is deleted (=0).
- Keep last value

  The I/O device retains the last value to be output before STOP.
- Substitute value

  The I/O device outputs the value for the channel set beforehand.

  > **Note**
  >
  > Make sure that the plant is always in a safe state if "Keep last value" is selected.

###### Type of output

With this parameter, you set the output type, for example, voltage. For any unused channels, select the **disabled** setting. For a disabled channel, the conversion time and integration time of the channel = 0 s, and the cycle time is optimized.

###### Output range

With this parameter, you set the output range of the selected output type.

###### Diagnostics, wire break (in current mode)

When this parameter is enabled, the **Wire break** diagnostics event is generated when a wire break is detected. This diagnostics event cannot be detected in the zero range.

###### Diagnostics, short circuit (in voltage mode)

If you enable this parameter, a diagnostics event is generated in the event of a short circuit in the output line. This diagnostics event cannot be detected in the zero range.

###### Diagnostics, overload

If you enable this parameter, the diagnostics event is generated in the event of an overload.

###### Substitute values

With this parameter, you enter a substitute value that the module is to output in CPU-STOP mode. The substitute value must be in the nominal range, overrange, or underrange.

#### ET 200SP

This section contains information on the following topics:

- [ET 200SP distributed I/O system](#et-200sp-distributed-io-system)
- [ET 200SP with own CPU module](#et-200sp-with-own-cpu-module)
- [Interface module parameters](#interface-module-parameters)
- [Expanding ET 200SP with ET 200AL modules](#expanding-et-200sp-with-et-200al-modules)
- [Output module parameters](#output-module-parameters)
- [Input module parameters](#input-module-parameters)

##### ET 200SP distributed I/O system

###### Definition

The ET 200SP distributed I/O system is a scalable, highly flexible distributed I/O system for connection of process signals to a central controller via a field bus.

###### Application area

The ET 200SP is a multi-functional distributed I/O system for various fields of application. The scalable design allows you to configure the system exactly to the specific requirements on location.

The ET 200SP is approved for degree of protection IP 20 and for installation in a control cabinet.

###### Structure

The ET 200SP is mounted on a mounting rail and comprises:

- An interface module which can communicate with all IO controllers that conform to the PROFINET standard IEC 61158
- Up to 32 I/O modules which can be inserted on passive BaseUnits in any combination
- A server module that completes the design of the ET 200SP.

##### ET 200SP with own CPU module

###### ET 200SP with own CPU

The ET 200SP can be equipped with its own CPU, for example with the CPU 1510SP-1 PN or CPU 1512SP-1 PN.

You can connect up to 65 modules of the S7-1500 automation system to this CPU.

Note the configuration rules of the [ET 200SP](http://support.automation.siemens.com/WW/view/en/58649293).

##### Interface module parameters

This section contains information on the following topics:

- [Status bytes](#status-bytes)
- [Group diagnostics, missing supply voltage L+](#group-diagnostics-missing-supply-voltage-l)
- [Configuration control with ET 200SP](#configuration-control-with-et-200sp)
- [Configuration control for ET 200SP with integrated ET 200AL modules](#configuration-control-for-et-200sp-with-integrated-et-200al-modules)

###### Status bytes

###### Status bytes

If you enable the "Status bytes" option, 4 bytes of input data are reserved for the status of the supply voltage of each I/O module.

![Status bytes](images/41335971467_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> An inserted or missing server module always reports for the slot bit = 0.

###### Group diagnostics, missing supply voltage L+

###### Group diagnostics, missing supply voltage L+

This diagnostics is a group diagnostics that covers the supply voltage status of all I/O modules of a potential group which are defined by BaseUnits with incoming power supply (light-colored BaseUnit BU...D).

The group diagnostics is formed from the states of the supply voltage of the inserted I/O modules within the potential group.

The group diagnostics does not depend on the "Missing supply voltage L+" parameter of the I/O modules being enabled.

The server module does not influence the missing supply voltage L+ group diagnostics.

###### Requirements for the correct operation of the group diagnostics for missing supply voltage L+:

- I/O modules or BU covers must be inserted on the light-colored and dark-colored BaseUnits.

  If no I/O module is inserted on a light-colored BaseUnit, the start of this potential group will not be detected by the interface module; the I/O modules of this potential group will thus belong to the previous potential group. A supply voltage L+ group error will then be assigned to the wrong potential group.

  When an I/O module is inserted on the light-colored BaseUnit, the interface module detects the new potential group, re-evaluates the status, and reports a new group diagnostics in the case of an error.
- The server module must be inserted.

  The server module itself does not influence the missing supply voltage L+ group diagnostics.

###### Configuration control with ET 200SP

###### Operating principle

Configuration control allows you to operate various real configurations (options) with a single configuration of the distributed I/O device ET 200SP.

Configuration control provides you with the option of configuring the ET 200SP distributed I/O device with its maximum configuration and nevertheless operating it with missing modules. If missing modules are retrofitted later, no new configuration is required and the hardware configuration does not have to be reloaded either.

Using control data record 196, which is transferred to the interface module in the user program, you define a current preset configuration.

- The configured module is not present on a slot.

  - A BU cover can be inserted in this slot instead of the configured I/O module. As there is no configured module on the slot, the term "Configuration control with empty slots" is also used.
  - The module that is configured to the right of the missing module can be inserted on this slot instead of the configured module. The missing module makes the actual configuration appear pushed together. As the configured module is missing but no gap arises in the configuration, this is also referred to as a "Configuration without empty slots".
- The configuration is extended by an already configured module.

  - In the case of configuration control with empty spaces, you extend the configuration by inserting the configured module on the corresponding empty slot.
  - In the case of configuration control without empty spaces, insert the configured module on the right-hand side next to the last module of the ET 200SP.

###### Requirement

The CPU startup parameter "Compare preset to actual configuration" is set to Startup even if mismatch (default setting). This setting is also selected for the startup parameters of the individual modules of the ET 200SP.

###### Enabling configuration control

In the properties of the interface module under Module parameters &gt; General &gt; Configuration control, select "Enable reconfiguration of device via user program". This activates configuration control.

###### Control data record 196 for ET 200SP

The figure below shows the data block 196 for the configuration control of an ET 200SP with four modules.

The value "12" is in the "block_length" element.

If you configure an ET 200SP in STEP 7 with more modules, the data block will be longer. The data record for the maximum configuration with 65 modules is 134 bytes long (configuration with PN interface module).

There are two bytes in the data record for each module.

The positions of these two bytes in the data record each code a module in the original configuration with STEP 7:

- "slot_1" and "info_slot_1" (bytes 4 and 5 in the data record, see figure below) correspond to the module in slot 1 in configuration with STEP 7.
- "slot_2" and "info_slot_2" (bytes 6 and 7) correspond to the module in slot 2 in configuration with STEP 7.
- "slot_3" and "info_slot_3" (bytes 8 and 9) correspond to the module in slot 3 in configuration with STEP 7.
- etc.

**"slot_x" byte**

The current slot is coded by the figure that is assigned to "slot_x" (by its value). Examples:

- The value "1" in byte 4 means you are assigning the module originally inserted in slot 1 to slot 1 in the current configuration (slot_1 = 1).
- The value "2" in byte 4 means you are assigning the module originally inserted in slot 1 to slot 2 in the current configuration (slot_1 = 2).
- The value "3" in byte 4 means you are assigning the module originally inserted in slot 1 to slot 3 in the current configuration (slot_1 = 3).
- etc.
- The value "1" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 1 in the current configuration (slot_2 = 1).
- The value "2" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 2 in the current configuration (slot_2 = 2).
- The value "3" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 3 in the current configuration (slot_2 = 3).
- etc.

If a BU cover can be inserted instead of a module, code this by adding 128 to the slot (bit 7 of the "slot_x" byte is set). Examples:

- The value "129" in slot_1 means you are also assigning the module originally inserted in slot 1 to slot 1 in the current configuration. A BU cover can also be used instead of this module. In the real plant configuration, either the module or a BU cover is inserted.
- The value "130" in slot_1 means you are assigning the module originally inserted in slot 1 to slot 2 in the current configuration. A BU cover can also be used instead of this module. In the real plant configuration, either the module or a BU cover is inserted.
- The value "131" in slot_1 means you are assigning the module originally inserted in slot 1 to slot 3 in the current configuration. A BU cover can also be used instead of this module. In the real plant configuration, either the module or a BU cover is inserted.

**"info_slot_x" byte**

If a new potential group is opened with the module, assign the "info_slot_x" byte the value 1 (bit 0 of the byte is set). Examples:

- The value "1" in the "info_slot_2" byte means that a new potential group is opened with module 2.
- The value "1" in the "info_slot_3" byte means that a new potential group is opened with module 3.
- The value "1" in the "info_slot_4" byte means that a new potential group is opened with module 4.

Exception: A new potential group is automatically assigned to the first module in the original configuration in STEP 7. This is not coded in the data record. You can enter any value in "info_slot_1".

You can choose any name for the components of the control data record (for example "slot_1").

**Example of control data record 196 for ET 200SP**

The figure below shows control data record 196 for an ET 200SP with four modules.

The module inserted in slot 2 in the configuration in STEP 7 can also be inserted in slot 2 in this configuration. It can also be inserted in slot 2 of a BU cover. Otherwise, nothing has changed compared to the original configuration.

![Control data record 196 for ET 200SP](images/69882476811_DV_resource.Stream@PNG-de-DE.PNG)

###### Addressing the interface module using the HW identifier

To transfer data record 196 with the instruction WRREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Readback data record 197 for ET 200SP

Readback data record 197 is used to read the actual configuration of a station (in this case, of an ET 200SP).

This readback data record allows you to check the real configuration of the ET 200SP (actual configuration). The readback data record for each configured module specifies whether or not it is actually available.

- The value "1" means that the correct module is inserted in the correct slot.
- The value "0" codes all other possibilities (wrong module, empty slot, BU cover).

**Configuration details:**

The configuration of the data block corresponds to the original configuration of the ET 200SP with STEP 7.

There are two bytes in the data record for each module. The position of these two bytes in the data record corresponds to the position of a module in the original configuration with STEP 7.

Sequence of bytes:

- "status_slot_1" and "reserve_1" (bytes 4 and 5 in the data record) correspond to the module in slot 1 in the configuration,
- "status_slot_2" and "reserve_2" (bytes 6 and 7) correspond to the module in slot 2 in the configuration
- "status_slot_3" and "reserve_3" (bytes 8 and 9) correspond to the module in slot 3 in the configuration,
- etc.

**Example**

The original configuration in STEP 7 has been changed by a control data record 196 (see example above): In the modified configuration, module 2 can either be inserted in slot 2 or be replaced by a BU cover.

The figure below shows readback data record 197 which ET 200SP outputs to indicate that there is a module in slot 2: The "status_slot_2" byte has the value "1".

The other modules are also available and are inserted in the correct slots.

![Readback data record 197 for ET 200SP](images/69892918923_DV_resource.Stream@PNG-de-DE.PNG)

The figure below displays the readback data record 197 which ET 200SP outputs to indicate that a BU cover is being used in slot 2: The "status_slot_2" byte has the value "0".

The other modules are available and are inserted in the correct slots.

![Readback data record 197 for ET 200SP](images/71132937227_DV_resource.Stream@PNG-de-DE.PNG)

###### Reading readback data record 197

You can read readback data record 197 from the ET 200SP with the instruction RDREC. RDREC operates asynchronously. If you call RDREC in the startup OB, you must call the instruction multiple times using a loop until the "BUSY" or "DONE" output parameter indicates that the data record has been read.

To read data record 197 with the instruction RDREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Additional information and examples

Specific examples of configuration control can be found in this [application description](http://support.automation.siemens.com/WW/view/en/29430270).

Further information on ET 200SP can be found in the manuals [IM 155-6 PN](http://support.automation.siemens.com/WW/view/en/73184046) and [IM 155-6 DP](http://support.automation.siemens.com/WW/view/en/73098660)

You will find a library of the data records and other application examples here:

[Templates for the data records](http://support.automation.siemens.com/WW/view/en/29430270)

---

**See also**

[Configuration control with ET 200AL](#configuration-control-with-et-200al)
  
[Configuration control for ET 200SP with integrated ET 200AL modules](#configuration-control-for-et-200sp-with-integrated-et-200al-modules)

###### Configuration control for ET 200SP with integrated ET 200AL modules

###### ET 200SP with integrated ET 200AL modules

Configuration control for ET 200SP and ET 200AL is described in separate help topics. See the links under "See also".

The steps outlined also apply to configuration control of an ET 200SP with integrated AL modules. The procedure is different for control data record 196 and readback data record 197.

The following help text describes control data record 196 and the readback data record 197 for an ET 200SP expanded with ET 200AL modules.

###### Control data record 196

The two figures below show parts of control data record 196 for a configuration of an ET 200SP expanded with ET 200AL modules.

This configuration is given as an example:

- The module "BA Send 1xFC" is in slot 1 "slot_1". This module allows you to integrate ET 200AL modules into an ET 200SP. In our configuration example, 16 AL modules are connected to the BA-Send (maximum configuration). If a BA-Send is being used, this module must be inserted in slot 1.
- All slots from 2 to 64 are assigned ET 200SP modules.
- A server module is inserted in slot 65.
- There are 16 AL modules in slots 66 to 81.

The ET 200SP with integrated AL modules, originally configured with STEP 7, is now to be reconfigured from the user program.

The new configuration has the following properties:

- The "BA Send 1xFC" module is inserted in "slot_1_BA-Send" (fixed setting).
- Module 2 "slot_2" is not available in the modified configuration (value "0").
- Module 3 "slot_3" is in slot 2 in the modified configuration (value "2").
- Module 4 "slot_4" is in slot 3 in the modified configuration (value "3").
- All modules from slot 5 to slot 81 are operated in the original configuration with STEP 7.

![Control data record 196](images/69858185483_DV_resource.Stream@PNG-de-DE.PNG)

The components of control data record 196 (figure above):

- block_length: Note the length of the control data record here; in the example: 166 (bytes). The length of the control data block is calculated using the formula "2 x number of slots + 4".
- block_ID: Enter the figure 196 here.
- version: The ET 200SP uses version 2 of control data record 196.
- subversion: The ET 200SP uses subversion 0 of control data record 196.

![Control data record 196](images/69928874123_DV_resource.Stream@PNG-de-DE.PNG)

The components of control data record 196 (figure above):

- slot_65_SP: This byte relates to the server module in the ET 200SP rack. It ends the backplane bus of the ET 200SP.
- From "slot_66_AL" come the 16 configured ET 200AL modules: Our configuration example does not change the configuration with STEP 7. The byte "slot_66_AL" has the value "66", the byte "slot_67_AL" has the value "67", the byte "slot_68_AL" has the value "68", etc.

###### Definition of control data record 196

A control data record 196 containing a slot assignment is defined for configuration control.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Byte** | **Component** | **Value** | **Description** |  |
| 0 | block_length | e.g. 166 for maximum configuration with   65 ET-200SP modules and   16 ET 200AL modules  (with DP interface module, maximum of 33 ET 200SP modules and 16 ET 200AL modules) | The length of the data record is calculated using the formula: 4 + "number of modules" x 2 | Header |
| 1 | Block ID | 196 | ID for control data record 196 |  |
| 2 | version | 2 | Version 2 of control data record 196 |  |
| 3 | subversion | 0 | Subversion 0 of control data record 196 |  |
| 4 | slot_1_BA-Send | Real slot for SP module 1  Possible value:  1 | When AL modules are integrated in ET 200SP, the module "BA Send 1xFC" must always be inserted in slot 1. | 1st slot for SP modules  Assignment for the configured SP module 1 to a real slot |
| 5 | info_slot_1_BA-Send | 0 or 1 | The value "1" means that a new potential group is opened with this module. (Not evaluated in this byte) |  |
| 6 | slot_2 | Real slot for SP module 2  Possible values:  2 to 65  (not 66 to 81, reserved for AL modules)  0 (if the configured module 2 is not available) | The configured SP module 2 can be inserted in any real slot from 2 to slot 65 (2 to 33 for a DP interface module).     Slots 66 to 81 are for AL modules (34 to 49 with DP interface module). | 2nd slot for SP modules  Assignment for the configured SP module 2 to a real slot |
| 7 | info_slot_2 | 1 | The value "1" means that a new potential group is opened with this module.   A new potential group must always be opened in this byte as BA-Send cannot open a new potential group. |  |
| 8 | slot_3 | Real slot for SP module 3  Possible values:  2 to 65  (not 66 to 81, reserved for AL modules)  0 (if the configured module 3 is not available) | The configured SP module 3 can be inserted in any real slot from 2 to slot 65 (2 to 33 for a DP interface module).     Slots 66 to 81 are for AL modules (34 to 49 with DP interface module). | 3rd slot for SP modules  Assignment for the configured SP module 3 to a real slot |
| 9 | info_slot_3 | 1 | The value "1" means that a new potential group is opened with this module.   . |  |
| : | : | : | : | : |
| 132 | slot_65 | Real slot for SP module 65  Possible values:  2 to 65  (not 66 to 81, reserved for AL modules)  0 (if the configured module 65 is not available) | The configured SP module 65 can be inserted in any real slot from 2 to slot 65 (2 to 33 for a DP interface module).     Slots 66 to 81 are for AL modules (34 to 49 with DP interface module) | 65th Slot for SP modules  Assignment for the configured SP module 65 to a real slot |
| 133 | info_slot_65 | 0 or 1 | The value "1" means that a new potential group is opened with this module (the value is not evaluated in this slot). |  |
| 134 | slot_66 | Real slot for AL module 1  Possible values:  66 to 81  (not 1 to 65, reserved for SP modules)  0 (if the configured AL module 1 is not available) | The configured AL module 1 can be inserted in any slot from 66 to slot 81 (34 to 49 for PROFIBUS). | 1st Slot for AL modules  Assignment for the configured AL module 1 to a real slot |
| 135 | info_slot_66 | - | Reserve |  |
| : | : | : | : | : |
| 164 | slot_81 | Real slot for AL module 16  Possible values:  66 to 81  (not 1 to 65, reserved for SP modules)  0 (if the configured AL module 16 is not available) | The configured AL module 16 can be inserted in any slot from 66 to slot 81 (34 to 49 for DP interface module). | 16th Slot for AL modules  Assignment for the configured AL module 16 to a real slot |
| 165 | info_slot_81 | - | Reserve |  |

###### Rules

- If the "BA Send 1xFC" module is being used, it must be inserted in slot 1.
- ET 200SP modules are inserted in slots 2 to 65 (slots 2 to 33 for DP interface module).
- AL modules are inserted in slots 66 to 81 (slots 34 to 49 for DP interface module).
- If you expand an ET 200SP with ET 200 AL modules, the 1st AL module is always coded in bytes 134 and 135 of the control data record, the 2nd AL module in bytes 136 and 137, etc., even if not all SP slots are to be occupied by SP modules. Non-assigned SP slots are coded with the value "0".

###### Error messages

The following error messages are returned if an error occurs when writing control data record 196:

Error messages

| Error code | Meaning |
| --- | --- |
| 16#80A2 | DP protocol error on layer 2 Indicates that a data record has not been acknowledged due to the system. |
| 16#80B1 | Invalid length; the length information in data record 196 is not correct. |
| 16#80B5 | Configuration control parameters not assigned. |
| 16#80B2 | Invalid slot: The configured slot is  not assigned. |
| 16#80B8 | Parameter error; module signals invalid parameters. |
| 16#80C5 | DP slave or module not available. Indicates that a data record has not been acknowledged due to the system. |

###### Readback data record 197 for ET 200SP with AL modules

The actual configuration of an ET 200SP with AL modules can be checked with readback data record 197.

Data record 197 largely corresponds to readback data record 197 for ET 200SP without AL modules; however, it is longer as the additional AL modules also need to be coded.

There are two bytes in the data record for each module. The position of these two bytes in the data record codes a module in the original configuration with STEP 7.

In the figure below:

- The components "status_slot_1" and "reserve_1" (bytes 4 and 5 in the data record) correspond to the module in slot 1 in the configuration with STEP 7,
- "status_slot_2" and "reserve_slot_2" (bytes 6 and 7) correspond to the module in slot 2,
- "status_slot_3" and "reserve_slot_3" (bytes 8 and 9) correspond to the module in slot 3,
- etc.

The following data record is structured for configuration with 65 SP modules and 16 AL modules. The value "166" therefore appears in the "block_length" element of the data record.

If you configure an ET 200SP in STEP 7 with fewer AL modules, the data block will be shorter.

If you use fewer SP modules in a configuration, this has no effect on the length of data record 197 (with an expansion of ET 200SP with ET 200AL modules).

The "reserve_x" component of readback data record 197 is reserved for future applications.

You can choose any name for the components of the readback data record (for example "status_slot_1").

The figure below shows the start of readback data record 197 for reading the actual configuration of an ET 200SP with AL modules.

![Readback data record 197 for ET 200SP with AL modules](images/70593874955_DV_resource.Stream@PNG-de-DE.PNG)

It does not show the components "status_slot_7" to "reserve_81" (maximum configuration of an ET 200SP with PN interface module) or "status_slot_7" to "reserve_slot_49" (maximum configuration of an ET 200SP with DP interface module).

Meaning of "status_slot_x":

- The value "1" in status_slot_x means that module x is inserted in the correct slot
- The value "0" codes all other possibilities (wrong module, empty slot, BU cover).

The figure below shows part of feedback data record 197 for reading the actual configuration of an ET 200SP with AL modules (and PN interface module). ET 200SP modules are inserted up to slot 65, and then the AL modules. For example, a value of "1" in the byte "status_slot_66_AL" means that the 1st AL module actually exists in the plant and is inserted in the correct slot.

![Readback data record 197 for ET 200SP with AL modules](images/70593883147_DV_resource.Stream@PNG-de-DE.PNG)

###### Reading feedback data record 197

You can read the feedback data record 197 from the ET 200SP with the RDREC instruction. RDREC operates asynchronously. If you call RDREC in the startup OB, you must call the instruction multiple times using a loop until the "BUSY" or "DONE" output parameter indicates that the data record has been read.

###### Further information and examples

Specific examples of configuration control can be found in this [application description](http://support.automation.siemens.com/WW/view/en/29430270).

Further information on ET 200SP can be found in the manuals for [IM 155-6 PN](http://support.automation.siemens.com/WW/view/en/73184046) and [IM 155-6 DP](http://support.automation.siemens.com/WW/view/en/73098660)

Further information on ET 200AL is available [here](http://support.automation.siemens.com/WW/view/en/89254863).

---

**See also**

[Configuration control with ET 200SP](#configuration-control-with-et-200sp)
  
[Configuration control with ET 200AL](#configuration-control-with-et-200al)

##### Expanding ET 200SP with ET 200AL modules

###### Introduction

The ET 200SP is a distributed I/O system for installation in a control cabinet.

The system can be expanded with modules of the ET 200AL series with IP65/67 degree of protection. ET 200AL modules can be mounted on site, for example on a machine.

###### Slot rules

The following rules apply to the use of ET 200AL modules in an ET 200SP with interface module:

- The "BA-Send 1xFC" module must be inserted in slot 1 of the ET 200SP if the ET 200SP is to be expanded with ET 200AL modules.
- The ET 200AL modules must be configured with no gaps.

The procedure detailed further on covers the use of ET 200AL modules in an ET 200SP with interface module.

The following, different, rules apply to the use of ET 200AL modules in an ET 200SP with CPU:

- The "BA-Send 1xFC" module can be located in slots 2 to 4 of the ET 200SP CPU.
- A CM DP communication module can be inserted as CPU submodule, but then occupies slot 2.

###### Procedure

Follow the steps below to configure an ET 200SP with interface module with ET 200AL modules:

1. Drag an interface module (PROFINET or PROFIBUS) from the ET 200SP series to the network view.
2. Go to the device view. You do this by clicking twice on the icon of the module you have just inserted.
3. Insert the module "BA Send 1xFC" into slot 1 of the ET 200SP.

   STEP 7 now generates an ET-Connection rack with 16 slots for ET 200AL modules (figure below).

   An ET-Connection rack is a virtual rack that sets the order of the connected ET 200AL modules.

   Question marks are displayed above the slots as an ET 200AL module has yet to be connected to BA-Send.

   ![Procedure](images/71046478603_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/71046478603_DV_resource.Stream@PNG-de-DE.PNG)
4. From the hardware catalog (subfolder ET 200AL in the ET 200SP folder), select the first ET 200AL module to be connected to the ET 200SP: Drag and drop this module to the 1st slot in the ET connection rack.

   From this module, STEP 7 generates a line to the "BA-Send 1xFC" module and allocates the slot numbers 66 to 81 (figure below).

   If you configure the ET 200SP with a DP interface module, STEP 7 assigns the slot numbers 34 to 49 for the ET 200AL modules.

   ![Procedure](images/71285879819_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/71285879819_DV_resource.Stream@PNG-de-DE.PNG)
5. Now drag all other ET 200AL modules into the free slots in the ET-Connection rack.

   STEP 7 automatically inserts the ET-Connection between the individual ET 200AL modules (green loops).

   In the configuration below, five ET 200AL modules are connected in series.

   ![Procedure](images/71046518283_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/71046518283_DV_resource.Stream@PNG-de-DE.PNG)
6. Complete the configuration of the ET 200SP: Drag all ET 200SP modules from the hardware catalog to the slots in the ET 200SP.

   Five ET 200SP modules are plugged in the configuration example below: The PN interface module in slot 0, the module "BA-Send 1xFC" in slot 1, one input module each in slots 2 and 3, and a server module in slot 4:

   ![Procedure](images/71046532747_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/71046532747_DV_resource.Stream@PNG-de-DE.PNG)

---

**See also**

[Configuration control with ET 200AL](#configuration-control-with-et-200al)
  
[ET 200AL distributed I/O system](#et-200al-distributed-io-system)

##### Output module parameters

This section contains information on the following topics:

- [Substitute value reaction](#substitute-value-reaction)

###### Substitute value reaction

###### Substitute value reaction

In the ET 200SP, the substitute value reaction is executed by the IO controller per slot.

The respective output reacts according to its set substitute value reaction:

- "Turn off"
- "Output substitute value"
- "Keep last value"

This substitute value reaction is triggered in the following cases:

- IO controller in STOP
- Controller failure (connection interruption)
- Firmware update
- Reset to factory settings
- More than one I/O module withdrawn simultaneously
- Disable the IO device
- Station stop

  - Missing server module
  - More than one I/O module withdrawn simultaneously
  - At least one I/O module is inserted on the wrong BaseUnit

    > **Note**
    >
    > **Reducing a configuration**
    >
    > If you reduce the configuration of the ET 200SP and download the configuration to the CPU, the modules which are no longer configured but still present retain their original substitute value reaction. This applies until the supply voltage on the BaseUnit BU...D or on the interface module is turned off.

##### Input module parameters

This section contains information on the following topics:

- [Parameters of the digital input modules](#parameters-of-the-digital-input-modules)
- [Parameters of the analog input modules](#parameters-of-the-analog-input-modules)
- [Information about reference channel mode](#information-about-reference-channel-mode)
- [Information about the Oversampling function](#information-about-the-oversampling-function)
- [Special features of AI 4xRTD/TC 2-/3-/4-wire HF](#special-features-of-ai-4xrtdtc-2-3-4-wire-hf)
- [What you should know about the scalable measuring range](#what-you-should-know-about-the-scalable-measuring-range)

###### Parameters of the digital input modules

###### Diagnostics missing supply voltage L+

Enabling of the diagnostics for missing or insufficient supply voltage L+.

###### Diagnostics short-circuit to ground

Enabling of the diagnostics if a short-circuit of the actuator supply to ground occurs.

![Diagnostics short-circuit to ground](images/43299380363_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Encoder supply |
| ② | Short-circuit |

###### Diagnostics short-circuit to L+

Enabling of the diagnostics if a short-circuit of the encoder supply to L+ occurs.

![Diagnostics short-circuit to L+](images/43298713995_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Encoder supply |
| ② | Short-circuit |

###### Diagnostics wire break

Enabling diagnostics if the line to the encoder is interrupted.

###### Operating mode

Determines whether a channel is enabled or disabled.

###### Pulse extension (only High Feature modules)

Pulse extension is a function for changing a digital input signal. A pulse at a digital input is extended to at least the configured length. If the input pulse is already longer than the configured length, the pulse is not changed.

Pulse extension is started whenever the state of the input signal changes and no pulse extension is active for this channel.

###### Potential group of the left module / new potential group

Specifies whether the I/O module is located on a base unit with supply voltage feed (new potential group) or whether it is it located on a base unit without supply voltage feed (in which case it belongs to the potential group of the left module).

###### Parameters of the analog input modules

###### Missing supply voltage L+

Enabling of the diagnostics, with missing or too little supply voltage L+.

###### Reference junction (AI 4xRTD/TC 2-/3-/4-wire HF)

A BaseUnit with internal temperature sensor (BU..T) or the channel 0 of the I/O module can be used as reference junction, provided this has been configured as "Thermal resistor Pt100 climatic range Celsius".

A possible parameter assignment is shown below (see also [Information about reference channel mode](#information-about-reference-channel-mode)):

RTD channel

| Setting | Description |
| --- | --- |
| No reference channel operation | Temperature value at channel 0 can be used as module-wide reference value if the parameters of the other channels are assigned accordingly. |
| Reference channel of Group x | The channel acts as sender for the reference junction temperature of Group x. Distribution is performed via the interface module. |

TC channel

| Setting | Description |
| --- | --- |
| Reference channel of the module | The corresponding TC channel uses the channel 0 of the same module as reference junction temperature. This must be set as "Thermal resistor Pt 100 climatic range Celsius" and "No reference channel operation"; otherwise, reference junction diagnostics is triggered. |
| Internal reference junction | The reference junction temperature is read by an internal temperature sensor on the BaseUnit. Reference junction diagnostics is triggered if there is a wrong BaseUnit type. |
| Reference channel of Group x | With the setting "TC" (thermocouple...), the channel acts as receiver for the reference junction temperature of Group x. |
| Fixed reference temperature | No temperature compensation occurs. The linearization is executed with an assumed reference junction temperature of 0 °C. |

###### Overflow

Enabling of the diagnostics if the measured value exceeds the overflow range.

###### Underflow

Enabling of the diagnostics if the measured value falls below the underflow range.

###### Wire break

Enabling of the diagnostics if the module has no current flow or too low a current flow for the measurement on the corresponding configured input.

###### Smoothing

The individual measurements are smoothed using digital filtering. The smoothing can be set in 4 stages, whereby the smoothing factor k multiplied by the cycle time of the I/O module corresponds to the time constant of the smoothing filter. The larger the smoothing, the larger the time constant of the filter.

The following figure shows the step response for the various smoothing factors depending on the number of module cycles.

![Smoothing with AI 4×RTD/TC 2‑/3‑/4‑wire HF](images/41336483467_DV_resource.Stream@PNG-en-US.png)

Smoothing with AI 4×RTD/TC 2‑/3‑/4‑wire HF

###### Interference frequency suppression

With analog input modules, suppresses the disturbance caused by the frequency of the AC network used.

The frequency of the AC network may interfere with measured values, particularly for measurements within low voltage ranges and when thermocouples are being used. This parameter is used to define the predominant power frequency of the system.

###### Hardware interrupt limits

If the high limit 1/2 or the low limit 1/2 is violated, the module triggers a hardware interrupt.

Below are some examples for the selection of the limits 1 and 2.

![Hardware interrupt limits](images/41336509067_DV_resource.Stream@PNG-en-US.png)

###### Low limit 1/2

Specify a threshold whose undershoot triggers a hardware interrupt.

###### High limit 1/2

Specify a threshold whose overrange triggers a hardware interrupt.

###### Potential group of the left module/New potential group

Specifies whether the I/O module is located on a BaseUnit with supply voltage infeed (new potential group) or on a BaseUnit without supply voltage feed (in which case, it belongs to the potential group of the left module).

###### Temperature coefficient (measurement type thermoresistor)

The correction factor for the temperature coefficient (α value) defines the relative rate of change of the resistance of a specific material at a temperature rise of 1 ℃.

The temperature coefficient depends on the chemical composition of the material. In Europe, only one value is used per sensor type (default value).

The further values facilitate a sensor-specific setting of the temperature coefficient and enhance accuracy.

---

**See also**

[Special features of AI 4xRTD/TC 2-/3-/4-wire HF](#special-features-of-ai-4xrtdtc-2-3-4-wire-hf)

###### Information about reference channel mode

An RTD/TC module of the ET 200SP works in reference channel mode when a channel sends the reference temperature to other channels of the station. The receiving channels use the reference temperature for temperature compensation when measuring with thermocouples.

###### Structure and use of thermocouples

The thermocouple consists of two wires with different metals or alloys that are welded together at the end. The weld is called measuring point.

The other end of the two wires is open. This end is called reference junction.

A thermal voltage, which depends on the temperature at the measuring point, occurs between the two metals/alloys at the measuring point. Other thermal voltages also occur at the reference junction - with transition from thermocouple to copper lines, for example - that falsify the actual measured value and need to be compensated. No compensation is required for a reference junction temperature of 0 °C.

Different methods are used to compensate the reference junction temperature:

- Fixed reference temperature: The reference junction is permanently set to a specific temperature, for example, to 0 °C by an icewater bath (no compensation required).
- Internal reference junction: The reference junction is the terminal of the BaseUnit on which the analog module is plugged. If you select the "Internal reference junction" compensation type, you have to use BaseUnits with integrated temperature measurement to compensate the reference junction temperature. These BaseUnits have the designation "BU..T". The module records the temperature at the reference junction and uses this to determine the actual temperature at the measuring point.
- Reference channel of Group x: An external thermal resistor records the temperature at the reference junction for the Group x (group of channels within a station). The actual temperature at the respective measuring point can be determined as a result. One external thermal resistor is required for each group. The thermal resistors are each connected to one channel of an analog module. These channels are called senders (for the temperature at the reference junction).  
  The mode of operation and settings are described in the section "Station-wide distribution of reference temperature".
- Reference channel of the module: The mode of operation is comparable with "Reference channel of Group x". You connect an external thermal resistor to channel 0 of the module to measure the temperature at the reference junction. Other channels of the same module use this reference temperature for temperature compensation.

  The mode of operation and settings are described in the section "Module-wide distribution of reference temperature".

You can find information about the structure and mode of operation of a thermocouple in the [Analog value processing](http://support.automation.siemens.com/WW/view/en/67989094) manual.

###### Station-wide distribution of the reference temperature

You can record the temperature at the reference junction x using a thermal resistor on a channel (sender of the reference temperature) and send it to other channels within a station (receivers). All channels that receive the temperature at a reference junction x form the Group x.

For each group, you assign parameters to exactly one channel as sender of the reference temperature.

![Station-wide distribution of the reference temperature](images/65832831499_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Thermal resistor at the reference junction |
| ② | Channel records temperature at the reference junction and sends it to the other channels within a station (sender of Group x). The temperature value is used for the compensation of the reference junction temperature. |
| ③ | Channels of the Group x receive the temperature at the reference junction (receivers) |

###### Parameter assignment of a channel as reference channel (sender for Group 1)

Parameter assignment is described below using Group 1 as example:

1. Open the project in STEP 7
2. Select the required analog module (RTD/TC) in the device view**.**
3. Then select a channel that is to work as sender of the reference junction temperature.   
   The following settings are required:

   "Measurement type": "Thermal resistor", for example, "Thermal resistor (4-wire connection)"

   "Measuring range": "Pt 100 climatic range"

   "Temperature unit": "Degrees Celsius"

   "Reference junction": "Reference channel of Group 1"

The following figure shows the parameter assignment.

![Parameter assignment of a channel as reference channel (sender for Group 1)](images/65858591883_DV_resource.Stream@PNG-en-US.png)

The channel configured in this way (thermal resistor measurement type) works as reference channel of Group 1 and sends the measured temperature to all channels (thermocouple measurement type) that are configured as receivers of Group 1.

In the next section, you will learn how to assign parameters for channels that are receivers of Group 1.

###### Parameter assignment of a channel as receiver of Group 1

The figure below shows the parameter assignment of a channel that receives the temperature at the reference junction of Group 1.

![Parameter assignment of a channel as receiver of Group 1](images/65859860491_DV_resource.Stream@PNG-en-US.png)

The following settings are required:

- "Measurement type": "Thermocouple"
- "Reference junction": "Reference channel of Group 1"

###### Module-wide distribution of the reference temperature

You can record the temperature on a reference junction using the channel 0 of the module and use the temperature value for the channels 1, 2, 3... of this module. The recorded temperature value is not sent to the channels of the other modules within the station (no reference channel mode).

![Module-wide distribution of the reference temperature](images/65833202059_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Thermal resistor at the reference junction |
| ② | Channel records temperature at the reference junction, "Reference junction" parameter: "No reference channel mode" |
| ③ | Channels of the same module use the temperature value for the compensation of the reference junction temperature for the measurement with thermocouples, "Reference junction" parameter: "Reference channel of the module" |

###### Parameter assignment of channel 0 as reference channel of the module

The figure below shows the parameter assignment of channel 0 of a module that is to be used for recording the temperature at the reference junction:

![Parameter assignment of channel 0 as reference channel of the module](images/65860399499_DV_resource.Stream@PNG-en-US.png)

The following settings are required:

- "Measurement type": "Thermal resistor", for example, "Thermal resistor (4-wire connection)"
- "Measuring range": "Pt 100 climatic range"
- "Temperature unit": "Degrees Celsius"
- "Reference junction": "No reference channel mode"

###### Parameter assignment of a channel that uses channel 0 as reference channel

The figure below shows how parameters have to be assigned for a channel that uses the channel 0 of this module as reference channel for temperature compensation.

![Parameter assignment of a channel that uses channel 0 as reference channel](images/65863088395_DV_resource.Stream@PNG-en-US.png)

The settings below are required for the channels of the module that compensate the temperature of the reference junction using channel 0:

- "Measurement type": "Thermocouple"
- "Reference junction": "Reference channel of the module"

---

**See also**

[Parameters of the analog input modules](#parameters-of-the-analog-input-modules)

###### Information about the Oversampling function

High-speed analog modules (HS) are available to meet high performance and speed requirements. The main characteristics of these HS analog modules compared to Standard analog modules (ST) is their shorter cycle times. To achieve this goal, the input and output modules are equipped with components with extremely short throughput and conversion times. In addition, the entire architecture of the modules is designed for faster signal processing.

HS analog modules convert the output of measured values and output values at the same time. Each channel within the module has its own A/D or D/A converter. This means the cycle time is basically the conversion time and independent of the number of activated channels. This is true for analog input modules as well as analog output modules. This means HS modules can be used in fast isochronous mode.

Apart from isochronous mode, the HS analog modules also provide benefits in non-isochronous (free-running) mode. Due to the fast processing of the process signals, HS analog modules are able to detect changes in the process values more quickly and to respond to these events with the appropriate program blocks (for example, hardware interrupt or cyclic interrupt organization blocks).

###### Isochronous mode

Isochronous mode refers to synchronous coupling

- Of signal acquisition and output via the distributed I/O
- Of signal transmission via PROFIBUS or PROFINET
- Of program processing with the constant bus cycle time of the PROFIBUS or PROFINET.

The result is a system that acquires its input signals in constant time intervals, processes them and outputs the output signals. Isochronous mode guarantees reproducible and defined process reaction times as well as equidistant and synchronous signal processing with distributed I/O.

The bus system and the I/O modules work synchronously with configured isochronous mode. The transmitted input and output data are linked to an "isochronous task" in the CPU. As a result, the data of a cycle are always consistent. All data of a process image belong together logically and in time. Jitter in the user program caused by the acquisition of outdated values is therefore almost impossible.

Even fast processes can be perfectly controlled by the exact timely reproducibility of all processes. Isochronous mode thus contributes to high control quality and hence to greater manufacturing precision. While possible fluctuations of the process reaction times are drastically reduced. The time-assured processing can be utilized to improve machine cycle times. Shorter cycle times increase the processing speed and help to lower production costs.

###### Oversampling

The use of the oversampling function in analog input or analog output modules requires an isochronous configuration.

With analog input modules, the set send clock is divided into time-equidistant sub-cycles. The send clocks can be subdivided into 2 to 16 sub-cycles. Each sub-cycle reads in a measured value. The read-in measured values of a data cycle are copied to the interface module (IM) in the next send clock and are then available to the processing CPU one clock later.

With analog output modules, the set send clock is also divided into time-equidistant sub-cycles. The send clocks can be subdivided into 2 to 16 sub-cycles. Each sub-cycle returns an output value. The output values are copied to the interface module by the CPU within the same send clock and are written to the process one send clock later.

The read-in and output values are transmitted in the user data of the analog module. In this way, the address space of the module is extended from 2 bytes of user data per channel to 16 x 2 bytes of user data per channel (with 16 sub-cycles). If you subdivide the send clock into fewer than 16 sub-cycles, the unused addresses are assigned the error value 0x7FFF during input. For output, the values of the unused addresses are ignored.

Because the sub-cycles have to be within a send clock, oversampling needs an additional clock to copy the data to the interface module, unlike the 3-cycle model of isochronous mode. The result is a 5-cycle model.

![Oversampling](images/66016653067_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Send clock is divided into sub-cycles which record the measured value (in this case: 10 sub-cycles) |
| ② | Measured values are copied to the IM |
| ③ | Measured values are processed and output values determined |
| ④ | Output values are copied by the CPU to the IM |
| ⑤ | Output values are written to the process |

**Higher sampling rates through oversampling**

Due to the configured modules, the IO device has a minimum possible update time. Within this update period, the IO device/IO controller of the PROFINET IO system is supplied once with new data.

The following applies with respect to the channels of a single standard module in the I/O device: The shortest update time ("sampling rate") is exactly one send clock.

If you want to shorten the update time for the channels of a standard module, you have to shorten the send clock. Because of the properties of the involved components and the structure of the I/O system, this is only possible to a certain extent (e.g., down to 0.25 ms).

Modules with oversampling, however, offer the option of further reducing the update time ("sampling rate") for their channels without having to shorten the send clock for the entire IO device at the same time.

The subdivision of the send clock into time-equidistant sub-cycles enables the processing of faster processes through higher sampling rates.

**Example**

In practice, the use of oversampling makes sense when the isochronous system works with only one specific send clock (for example, 1 ms) due to the modules used and when faster sampling of the process values is required. By using oversampling and subdividing the send clock into 4 sub-cycles, for example, you can sample the process values in intervals of 250 µs.

**Configuring oversampling**

Enable the option "Isochronous mode" in the IO device used, and set the corresponding parameters ("Send clock", etc.).

With the distributed analog input modules (e.g. AI 2xU/I 2,4-wire HS), you specify the number of sub-cycles using the "Sampling rate" parameter.

With the distributed analog output modules (e.g. AQ 2xU/I HS), you specify the number of sub-cycles using the "Sampling rate" parameter.

If, for example, you configure a "Sampling rate" of 4 "Values/cycle" for a send clock of 1 ms, the send clock is subdivided into 4 sub-cycles and the process values are sampled at intervals of 250 µs.

###### Reference

You can find additional information in the manuals on the high-speed analog modules and in the [Analog value processing](http://support.automation.siemens.com/WW/view/en/67989094) function manual.

---

**See also**

[What is isochronous mode? (S7-1500, S7-1500T)](Special%20PROFINET%20configurations.md#what-is-isochronous-mode-s7-1500-s7-1500t)

###### Special features of AI 4xRTD/TC 2-/3-/4-wire HF

###### Use of Cu10 sensors

- Select "3-wire thermal resistor" and "Cu10" in the parameter assignment.
- Wire the Cu10 sensor using 3-wire connection technology.
- An automatic, internal compensation of the line resistance of the missing measuring line takes place during operation.

  > **Note**
  >
  > To ensure optimum line compensation for Cu10, please note the following:
  >
  > - The sum of cable resistance and measuring resistance must not exceed 31 Ω.
  > - Cable resistance should not exceed 8 Ω if you want to use the temperature range up to over 312 °C.   
  >   Example: A 200 m long copper cable with 0.5 mm<sup>2</sup> core cross-section has approx. 7 Ω. A lower cross-section reduces the permissible cable length accordingly.

###### Use of PTC resistors

PTCs are suitable for temperature monitoring of or as thermal protective equipment for complex drives or transformer windings.

- Select "2-wire resistor" and "PTC" in the parameter assignment.
- Connect the PTC using 2-wire technology.
- Use type A PTC resistors (PTC thermistors) in accordance with DIN/VDE 0660, Part 302.
- If the "Over-/underflow" diagnostics is enabled, a "low limit violation" diagnostics which shows a short circuit is generated for resistance values &lt; 18 Ω.
- Sensor data on PTC resistance:

Use of PTC resistors

| Property | Technical specifications | Note |
| --- | --- | --- |
| Switching points | **Reaction to rising temperature** |  |
| &lt; 550 Ω | **Normal range:**   - SIMATIC S7: bit 0 = "0", bit 2 = "0" (in the PII) |  |
| 550 Ω to 1650 Ω | **Prewarning range:**   - SIMATIC S7: bit 0 = "0", bit 2 = "1" (in the PII) |  |
| &lt; 1650 Ω | **Response range:**   - SIMATIC S7: bit 0 = "1", bit 2 = "0" (in the PII) |  |
| **Reaction to falling temperature** |  |  |
| &lt; 750 Ω | **Response range:**   - SIMATIC S7: bit 0 = "1", bit 2 = "0" (in the PII) |  |
| 750 Ω to 540 Ω | **Prewarning range:**   - SIMATIC S7: bit 0 = "0", bit 2 = "1" (in the PII) |  |
| &lt; 540 Ω | **Normal range:**   - SIMATIC S7: bit 0 = "0", bit 2 = "0" (in the PII) |  |
| (TNF-5) °C  (TNF+5) °C  (TNF+15) °C  Measuring voltage   Voltage on the PTC | max. 550 Ω  min. 1330 Ω  min. 4000 Ω  max. 7.5 V | RRT= rated response temperature |

- Assignment in the process image inputs (PII) with SIMATIC S7

  ![Assignment in the process image inputs (PII)](images/41336437259_DV_resource.Stream@PNG-en-US.png)

  Assignment in the process image inputs (PII)
- Notes on programming

  > **Note**
  >
  > Only the bits 0+2 are relevant for the evaluation in the process image inputs. You can use the bits 0+2 to monitor the temperature, for example, of a motor.
  >
  > The bits 0+2 in the process image inputs have no latching function. When you are assigning parameters, take into consideration that a motor, for example, starts up in a controlled manner (via an acknowledgment).
  >
  > Bits 0+2 can never be set simultaneously, but are instead set consecutively.
  >
  > For safety reasons, always evaluate the diagnostic entries of the AI 4×RTD/TC 2-/3-/4-wire HF, as no measurement is possible if I/O modules are unplugged, if the supply voltage of the I/O module has failed, or if there is a wire break or short circuit of the measuring lines.

###### Example

The following diagram shows the temperature variation and the associated switching points.

![Example](images/41336413835_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Parameters of the analog input modules](#parameters-of-the-analog-input-modules)
  
[What you should know about the scalable measuring range](#what-you-should-know-about-the-scalable-measuring-range)

###### What you should know about the scalable measuring range

###### The scalable measuring range

The scalable measuring range is a section from the temperature measuring range of an analog input module (for example, the ET 200SP module "AI 8xRTD/TC 2-wire HF").

In this section, a higher resolution of the measured values is possible, comparable with a magnifier that allows a subsection to be viewed in greater detail.

The scalable measuring range is supported for the following measurement types:

- Thermal resistor (RTD) standard
- Thermocouple

The scalable measuring range is not available with the following measurement types:

- Voltage
- Resistance
- Thermal resistor climatic

###### Position and resolution of the scalable measuring range

The position and resolution of the scalable measuring range can be set (scaled):

- **Position:** The scalable measuring range can be moved over the entire standard measuring range. This allows you to select the temperature range for which your application requires a higher resolution.

  Exception: The scalable measuring range cannot be moved to the extent that it enters the overflow or underflow of the standard measuring range (Clipping).

  You select the position of the scalable measuring range with the "Measuring range center" parameter (see figure below).
- **Resolution:** The following values can be set:

  - 2 decimal places (0.01 ℃)
  - 3 decimal places (0.001 ℃)

  You set the resolution with the "Measuring range resolution" parameter (figure below).

**Example of a parameter assignment**

The following figure shows a parameter assignment for the ET 200SP module "AI 8xRTD/TC 2-,3-,4-wire HF".

In STEP 7, you can find parameters in the properties box via General &gt; AI 4 &gt; Inputs &gt; Channel 0 to channel 3.

![Position and resolution of the scalable measuring range](images/71757406731_DV_resource.Stream@PNG-en-US.png)

**Conductor resistor:**

The "Conductor resistor" parameter in the parameter assignment above is enabled only if the "Thermal resistor (2-wire terminal)" measurement type was selected.

Here, enter the value for the resistance of the connecting cable of the thermal resistor: A 200 m long copper cable with 0.5 mm<sup>2</sup> wire cross-section, for example, has a resistance value of seven ohms.

**Measuring range resolution:**

In the parameter assignment above, a resolution of 0.01 °C was selected (measuring range resolution "2 decimal places").

**Measuring range center:**

The measuring range center is set to 500 °C.

With a resolution of 0.01 °C, this results in a scalable measuring range from 174.88 °C to 825.11 °C.

At a resolution of 0.01 °C, the scalable measuring range covers 650.23 °C.

**Maximum (scalable measuring range):**

This value represents the high limit of the scalable measuring range. In the example above, 825.11 ℃.

The value is calculated by STEP 7 (at a resolution of 0.001 °C, the high limit is at 532.511 °C, see figure below).

**Minimum (scalable measuring range):**

This value represents the low limit of the scalable measuring range. In the example above, 174.88 ℃.

The value is calculated by STEP 7 (at a resolution of 0.001 °C, the low limit is at 467.488 °C; see figure below).

**Higher resolution:**

The following figure shows a parameter assignment with a resolution of 0.001 °C (otherwise the same example as in the figure above):

![Position and resolution of the scalable measuring range](images/71757410443_DV_resource.Stream@PNG-en-US.png)

At a resolution of 0.001 °C, the scalable measuring range is between 467.488 and 532.511 °C and covers 65.023 °C (a tenth of the measuring range at a resolution of 0.01 °C).

###### Standard measuring range with 0.1 °C resolution

The following table shows the standard measuring range for thermal resistors of the type "Pt 100", values in degrees Celsius.

| Pt 100 standard in °C  (1 digit = 0.1 °C) | Decimal values | Hexadecimal values | Ranges |
| --- | --- | --- | --- |
| &gt; 1000.0 | 32767 | 7FFF | Overflow |
| 1000.0  :  850.1 | 10000  :  8501 | 2710  :  2135 | Over  range |
| 850.0  :  -200.0 | 8500  :  -2000 | 2134  :  F830 | Nominal range |
| -200.1  :  -243.0 | -2001  :  -2430 | F82F  :  F682 | Under range |
| &lt; -243.0 | -32768 | 8000 | Underflow |

The standard measuring range is the basis for the scalable measuring range.

You can set the measuring range center within the nominal range (-200 °C to 850 °C, see table above).

For temperatures below and above the set measuring range center, you then obtain measured values with a higher resolution.

The width of this range around the measured value center depends on the selected resolution.

###### Scalable measuring range 0.01 °C and 0.001 °C resolution

The scalable measuring range is identified by the following value ranges:

| Scalable measuring range | Measuring range resolution   **(values in °C)** |  | Hexadecimal values |
| --- | --- | --- | --- |
| **2 decimal places** | **3 decimal places** |  |  |
| Overflow | &gt; 325.11 | &gt; 32.511 | 7FFF |
| High limit | 325.11 | 32.511 | 7EFF |
| Measuring range center | 0 | 0 | 0 |
| Low limit | 325.11 | -32.511 | 8100 |
| Underflow | &lt; -325.11 | &lt; -32.511 | 8000 |

The maximum and minimum of the scalable measuring range depend on the selected resolution:

- 2 decimal places, resolution of 0.01 ℃:

  The high limit is 325.11 °C above the measuring range center you have set.

  The low limit is 325.11 °C below the measuring range center you have set.

  This means that the scalable measuring range is 650.22 °C around the measuring range center.
- 3 decimal places, resolution of 0.001 ℃:

  The high limit is 32.511 ℃ above the measuring range center you have set.

  The low limit is 32.511 ℃ below the measuring range center you have set.

  This means that the scalable measuring range is 65.022 ℃ around the measuring range center.

###### Calculation of the temperature

You calculate the temperature value by adding the value you receive from the module to the measuring range center.

Example:

- You have set the measuring range center 500 °C (see example in the section "Example of a parameter assignment"). For the resolution, you selected "2 decimal places".
- From the module, you receive the hexadecimal value "0100" in S7 format:

  | **Bit**    **15** | **Bit**    **14** | **Bit**    **13** | **Bit**    **12** | **Bit**    **11** | **Bit**    **10** | **Bit**    **9** | **Bit**    **8** | **Bit**    **7** | **Bit**    **6** | **Bit**    **5** | **Bit**    **4** | **Bit**    **3** | **Bit**    **2** | **Bit**    **1** | **Bit**    **0** |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
- The hexadecimal value "0100" corresponds to the decimal value 256.
- Since you have selected a resolution of 0.**01** °C, the number 256 corresponds to the temperature value "2.**56** °C".
- You now add 500 °C and 2.56 °C and obtain the measured value 502.56 °C.

###### Scalable measuring range in the standard measuring range

![Scalable measuring range in the standard measuring range](images/71757554955_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Scalable measuring range with 2 decimal places, temperature values in S7 format. |
| ② | Scalable measuring range with 3 decimal places, temperature values in S7 format. |
| ③ | Scalable measuring range cut off at the overflow of the standard measuring range ("Clipping").  The sum of the measuring range center (for example 750 °C) and the measured value returned by the module must not extend into the overflow of the standard measuring range. For this reason, in the example above, the maximum value that the module can return is limited to 250 °C |

###### Clipping

STEP 7 limits the maximum of the scalable measuring range so that the sum of the measured value center and the maximum measured value that the module can return is not located in the overflow of the standard measuring range. In the same way, STEP 7 restricts the minimum of the scalable measuring range.

---

**See also**

[Special features of AI 4xRTD/TC 2-/3-/4-wire HF](#special-features-of-ai-4xrtdtc-2-3-4-wire-hf)

#### ET 200AL

This section contains information on the following topics:

- [ET 200AL distributed I/O system](#et-200al-distributed-io-system)
- [Configuring ET 200AL](#configuring-et-200al)
- [Configuration control with ET 200AL](#configuration-control-with-et-200al)

##### ET 200AL distributed I/O system

###### SIMATIC ET 200AL

The SIMATIC ET 200AL distributed I/O system is a scalable and highly flexible, distributed I/O system for connecting process signals to a superordinate control with a field bus.

![SIMATIC ET 200AL](images/68619097483_DV_resource.Stream@PNG-de-DE.png)

###### Properties

- Connection to PROFINET or PROFIBUS or integration into ET 200SP / ET 200SP CPU
- Up to 32 modules on an ET 200AL
- Integration into ET 200SP / ET 200SP CPU: Up to 16 AT modules can be connected to an ET 200AL
- Connection of modules via ET-Connection
- Spatially separated mounting possible
- Module widths of 30 and 45 millimeters
- Degree of protection IP65/IP67
- Suitable for temperatures from -25 to +55 °C and accelerations up to 5 g.
- Installation in all positions
- Color coding of the cables and connections
- CA-compliant labeling of the interfaces
- PROFIenergy integrated
- Configuration control
- Connection of sensors and actuators using M8 and M12 connection system

###### Area of application

The SIMATIC ET 200AL distributed I/O system is especially well suited for use in tight spaces, moving applications and for assembly and handling technique. Thanks to its scalable construction, you have the option precisely customize its configuration to your on site needs.

The SIMATIC ET 200AL distributed I/O system features protection type IP65/IP67 and is suited for distributed use on a machine or assembly line.

###### Structure

The SIMATIC ET 200AL distributed I/O system is made up of the following components:

- Interface modules (PROFINET/PROFIBUS)
- Digital and analog I/O modules
- Communications module

After an interface module you can configure 2 lines (ET-Connection), each with 16 modules.

Alternatively, you can configure a line with 16 I/O modules on the SIMATIC ET 200SP distributed I/O system with BusAdapter BA-Send 1xFC.

The ET‑Connection backplane bus is designed as a cable. This allows you to create spatial distances of up to 10 m between the modules.

###### Configuration example

The figure below shows a configuration example of the SIMATIC ET 200AL distributed I/O system with a PROFINET interface module.

![Example configuration of the ET 200AL](images/70926123787_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Interface module (PROFINET) |
| ② | Digital input/Digital output module |
| ③ | Digital input module |
| ④ | Analog input module |
| ⑤ | Communications module |
| ⑥ | PROFINET cable |
| ⑦ | Power supply cable |
| ⑧ | ET-Connection line |
| ⑨ | Sealing caps |

Example configuration of the ET 200AL

---

**See also**

[Expanding ET 200SP with ET 200AL modules](#expanding-et-200sp-with-et-200al-modules)

##### Configuring ET 200AL

###### Introduction

ET 200AL is a distributed I/O system with an IP65/67 degree of protection. It is therefore designed for use on site, for example right beside a machine (no control cabinet required).

The system includes interface and communications modules as well as input and output modules.

There are two use cases for the ET 200AL:

1. As I/O device or DP slave: The system interface module is connected to a field bus (PROFINET or PROFIBUS) and connected to the PN or DP interface of a CPU.
2. As an ET 200SP expansion: The ET 200AL modules are connected to the ET 200SP over the "BA Send 1xFC" module ("mixed mode").

The following sections describe how to configure an ET 200AL as I/O device or DP slave (use case 1).

For use case 2, see the link under "See also".

###### Procedure

Follow the steps below to configure an ET 200AL in STEP 7:

1. Copy an interface module (PROFINET or PROFIBUS) from the ET 200SP series to the network view (drag-and-drop operation from the hardware catalog).
2. Go to the device view. Double-click on the interface module you have just inserted.

   The interface module and two ET-Connection racks are displayed in the device view (figure below).

   There are no slot numbers assigned yet, which is why question marks are displayed above the slots.

   ![Procedure](images/71007309195_DV_resource.Stream@PNG-de-DE.PNG)

   ![Procedure](images/71007309195_DV_resource.Stream@PNG-de-DE.PNG)
3. Now select the modules (input, output and communication modules) from the hardware catalog (ET 200AL folder) and drag them to the free slots (outlined in blue; not shown).

   You can place up to 16 ET 200AL modules in each ET-Connection rack (figure below).

   An ET-Connection rack is a virtual rack that sets the order of the connected ET 200AL modules.

   ![Procedure](images/71037500043_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/71037500043_DV_resource.Stream@PNG-de-DE.png)
4. Now connect the interface module to the two ET-Connection racks.

   First click on an ET-Connection interface of the interface module, then hold and drag a line to the left-hand ET connection of the first module in one of the two ET-Connection racks.

   Repeat this step for the second ET-Connection interface of the interface module and the second ET-Connection rack (if used).

   ![Procedure](images/71043414539_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/71043414539_DV_resource.Stream@PNG-de-DE.png)
5. Double-click on a module to access the module properties and set the module parameters.

###### Rules

- The ET 200AL modules must be configured with no gaps.
- The first module in an ET-Connection rack must be connected to the interface module.

---

**See also**

[ET 200AL distributed I/O system](#et-200al-distributed-io-system)

##### Configuration control with ET 200AL

###### Operating principle

With configuration control, you can change the original configuration of an ET 200AL (created by configuring with STEP 7) with a user program and operate the ET 200AL in this modified configuration. STEP 7 is no longer required for this configuration: You use your user program to signal to the ET 200AL the slot in which a configured module is actually inserted.

In this case, use control data record 196. In this data record, you code which modules are missing or located in different slots in the real configuration compared to the configuration with STEP 7. The configuration control has no effect on the parameter assignment of the modules (for example, the enabling of diagnostic alarms).

You then call the "WRREC" instruction and use it to write the data record to the interface module of the ET 200AL.

Configuration control gives you the flexibility to vary the configuration of an ET 200AL as long as the real configuration can be derived from a preset maximum configuration (originally created with STEP 7).

The following sections describe how to enable configuration control and how to structure the required data record 196 for the ET 200AL.

###### Requirement

The CPU startup parameter "Compare preset to actual configuration" is set to Startup even if mismatch (default setting). This setting is also selected for the startup parameters of the individual modules of the ET 200AL.

###### Enabling configuration control

In the properties of the interface module under Module parameters &gt; General &gt; Configuration control, select "Enable reconfiguration of device via user program". This activates configuration control.

![Enabling configuration control](images/105174298251_DV_resource.Stream@PNG-en-US.PNG)

###### Structure of control data record 196

The configuration of the data block corresponds to the original configuration of the ET 200AL with STEP 7.

There are two bytes in the data record for each module. The position of these two bytes in the data record codes a module in the original configuration with STEP 7.

- Bytes 4 and 5 in the data record correspond to the module in slot 1 in the original configuration.
- Bytes 6 and 7 in the data record correspond to the module in slot 2 in the original configuration.
- Bytes 8 and 9 in the data record correspond to the module in slot 3 in the original configuration.
- etc.

The current (real) slot is coded by the number that is assigned to the "Slot_x" byte (by its value): Examples:

- The value "2" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 2 in the current configuration.
- The value "3" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 3 in the current configuration.
- The value "4" in byte 6 means you are assigning the module originally inserted in slot 2 to slot 4 in the current configuration.
- etc.

###### Creating control data record 196

The figure below shows part of control data record 196 for configuration of an ET 200AL.

This configuration is given as an example:

- ET-Con1 is inserted in "slot_1" (fixed setting). The two ET-Connection submodules "ET-Con1" and "ET-Con2" are submodules of the interface module of the ET 200AL. They are integrated as fixed modules in the IM module. They cannot be inserted individually.
- ET-Con2 is inserted in "slot_18" (fixed setting).
- In this configuration, 16 AL modules are connected to ET-Con1 ("slot_2" to "slot_17" in the following data record). This is the maximum configuration.
- In this configuration, one AL module is connected to ET-Con2 ("slot_19"). However, a total of 16 AL electronic modules could be connected to ET-Con2 (as to ET-Con1).

The ET 200AL originally configured with STEP 7 is now to be reconfigured from the user program.

The new configuration has the following properties:

- ET-Con1 is inserted in "slot_1" (fixed setting).
- Module 2 is also operated in slot 2 in the modified configuration.
- Module 3 is not used.
- Module 4 is now inserted in slot 3.
- Module 5 is now inserted in slot 4.
- No other modules at ET-Con1 are used.
- ET-Con2 is inserted in "slot_18" (fixed setting)
- The module at ET-Con2 is used.

![Creating control data record 196](images/70925109387_DV_resource.Stream@PNG-de-DE.PNG)

The components of control data record 196 (definition in section "Control data record 196" below):

- block_length: Note the length of the control data record here; in the example: 42 (bytes). The length of the control data block is calculated using the following formula: 2 x "number of modules" + 4.
- block_ID: Enter the figure 196 here. This number identifies the data record as the data record for configuration control.
- version: The ET 200AL uses version 2 of control data record 196.
- subversion: The ET 200AL uses subversion 1 of control data record 196.
- slot_1: The ET-Connection 1 submodule is always inserted in slot 1 of the ET 200AL.
- reserve_1: This byte is not used (value "0").
- slot_2: The configured module 2 is inserted in slot 2 (value "2").
- reserve_2: This byte is not used (value "0").
- slot_3: The configured module 3 is not present in the current configuration (value "0").
- reserve_3: This byte is not used (value "0").
- slot_4: The configured module 4 is inserted in slot 3 in the current configuration (value "3").
- reserve_4: This byte is not used (value "0").
- slot_5: The configured module 5 is inserted in slot 4 in the current configuration (value "4").
- reserve_5: This byte is not used (value "0").
- slot_6: The configured module 6 is not present in the current configuration (value "0").
- reserve_6: This byte is not used (value "0").
- slot_7: The configured module 7 is not present in the current configuration (value "0").
- reserve_7: This byte is not used (value "0").
- etc.
- slot_18: The ET-Connection 2 submodule is always inserted in slot 18 of the ET 200AL (value "18").
- reserve_18: This byte is not used (value "0").
- slot_19: The configured module 19 is inserted in slot 19 in the current configuration (value "19").
- reserve_19: This byte is not used. (value "0")

###### Control data record 196 for ET 200AL

A control data record 196 containing a slot assignment is defined for configuration control.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Byte** | **Element** | **Value** | **Description** |  |
| 0 | Block length in bytes | e.g. 14 for ET 200AL with 5 modules | The length of the data record is calculated using the formula: 4 + (number of modules x 2) bytes | Header |
| 1 | Block ID | 196 | ID for control data record 196 |  |
| 2 | Version | 2 | Version 2 of control data record 196 |  |
| 3 | Subversion | 1 | Subversion 1 of control data record 196 |  |
| 4 | Configured module 1  (ET-Connection 1) | 1 | ET-Connection 1 is always assigned to slot 1 (fixed). The value "1" must therefore always be entered in byte 4. | Assignment for configured module 1 (ET-Connection 1) to real slot 1 |
| 5 | Reserve  for configured module 1 | 0 | Not used |  |
| 6 | Configured module 2 | Real slot of module 2  Possible values:  2 up to the number of modules (except 18) 0 (if the configured module 2 is not present) | The configured module 2 can be inserted in any slot from 2 to slot 34. Slot 18 is reserved for ET-Con 2.  If the configured module is not used, this byte contains the value "0". | Assignment for the configured module 2 to a real slot |
| 7 | Reserve  for configured module 2 | 0 | Not used |  |
| 8 | Configured module 3 | Real slot of module 3  Possible values:  2 up to the number of modules (except 18) 0 (if the configured module 2 is not present) | The configured module 3 can be inserted in any slot from 2 to slot 34. Slot 18 is reserved for ET-Connection 2. If the configured module is not used, this byte contains the value "0". | Assignment for the configured module 3 to a real slot |
| 9 | Reserve  for configured module 3 | 0 | Not used |  |
| : | : | : | : | : |
| 39 | Configured module 18  (ET-Connection 2) | 18 | ET-Connection 2 is always assigned to slot 18 if AT modules are connected at this submodule. | Assignment for configured module 18 (ET-Connection 2) to real slot 18 |
| 40 | Reserve  for configured module 18 | 0 | Not used |  |
| : | : | : | : | : |
| (Bytes 4 to 70,   not byte 39) | Configured module x | Real slot of module x  Possible values:  2 up to the number of modules (except 18) 0 (if there is no configured module x) | The configured module x can be inserted in any real slot from 2 to slot 34. Slot 18 is reserved for ET-Con 2 (bytes 39 and 40 in the control data record) | Assignment for configured module x to a real slot y |
| (Bytes 5 to 71,  not byte 40) | Reserve  for configured module x | 0 | Not used |  |

###### Rules

- The ET-Connection 1 and ET-Connection 2 submodules must be treated like real modules in configuration control. Restriction: ET-Connection 1 is always placed in slot 1 and ET‑Connection 2 is always placed in slot 18 (fixed assignment).
- There are no reserve modules for the ET 200AL (unlike for the ET 200S or with BU cover modules for the ET 200SP). For this reason, bit 7 of "slot_x" must not be set (i.e. only the values 0 to 127 may be used).
- The value "0" of "slot_x" indicates that this module is not inserted in the current configuration.
- Gaps must not be left between the AL modules when configuring with STEP 7.
- If no modules are connected to ET-Con2 when STEP 7 is configured, ET-Con2 is not configured: This shortens data record 196.
- If fewer than 16 modules are connected to ET-Con1 during configuration with STEP 7 and there are also modules connected to ET-Con2, control data record 196 must contain all unassigned slots for ET-Con 1. They are assigned zero as the value for the real slot.

###### Writing a data record

Transfer the control data record to the ET 200AL module.

To do so, call the extended WRREC (Write data record) instruction, and transfer the control data record created.

If you do not transfer a control data record, the interface module uses the original configuration with STEP 7. Here, the following applies: Configured module x is inserted in real slot x.

###### Addressing the interface module using the HW identifier

To transfer data record 196 with the instruction WRREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Error messages

The following error messages are returned if an error occurs when writing control data record 196:

Error messages

| Error code | Meaning |
| --- | --- |
| 16#80A2 | DP protocol error on layer 2 Indicates that a data record has not been acknowledged due to the system. |
| 16#80B1 | Invalid length; the length information in data record 196 is not correct. |
| 16#80B5 | Configuration control parameters not assigned. |
| 16#80B2 | Invalid slot: The configured slot is  not assigned. |
| 16#80B8 | Parameter error; module signals invalid parameters. |
| 16#80C5 | DP slave or module not available. Indicates that a data record has not been acknowledged due to the system. |

###### Feedback data record 197 for ET 200AL

The feedback data record 197 is used to read the actual configuration of a station (in this case of an ET 200AL).

This data record allows you to check the real configuration of the ET 200AL (actual configuration). The feedback data record for each configured module specifies whether or not it is actually present.

- The value "1" means that the correct module is inserted in the correct slot.
- The value "0" codes all other possibilities (wrong module, empty slot, BU cover).

Example:

A module has been configured with STEP 7 for slot 4.

This module has then been moved to slot 3 in the current configuration using data record 196.

If this module is also really in slot 3, this is coded by the value "1" (status_slot_4 = 1).

**Configuration details:**

The configuration of the data block corresponds to the original configuration of the ET 200AL with STEP 7.

There are two bytes in the data record for each module. The position of these two bytes in the data record corresponds to the position of a module in the original configuration with STEP 7.

**Sequence of bytes:**

- "status_slot_1_ET_Con1" and "reserve_slot_1_ET-Con1" (bytes 4 and 5 in the data record) correspond to the module in slot 1 in the configuration,
- "status_slot_2" and "reserve_slot_2" (bytes 6 and 7) correspond to the module in slot 2 in the configuration
- "status_slot_3" and "reserve_slot_3" (bytes 8 and 9) correspond to the module in slot 3 in the configuration,
- etc.

**Example**

The following feedback data record 197 is returned by the ET 200AL that was reconfigured with control data record 196 in the example above (section "Creating control data record 196").

![Feedback data record 197 for ET 200AL](images/70932000267_DV_resource.Stream@PNG-de-DE.PNG)

Modules 2, 4 and 5 are actually connected to ET-Con1.

None of the other modules that were connected to ET-Con1 in the configuration with STEP 7 are present in the current configuration (in line with the control data record 196 settings from the example above).

A module is really connected to ET-Con2 as in the original configuration with STEP 7.

###### Reading feedback data record 197

You can read the feedback data record 197 from the ET 200AL with the RDREC instruction. RDREC operates asynchronously. If you call RDREC in the startup OB, you must call the instruction multiple times using a loop until the "BUSY" or "DONE" output parameter indicates that the data record has been read.

To read data record 197 with the instruction RDREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Additional information and examples

Further information on ET 200AL is available [here](http://support.automation.siemens.com/WW/view/en/89254863).

Specific examples of configuration control can be found here in this [application description](http://support.automation.siemens.com/WW/view/en/29430270).

You will find a library of the data records and other application examples here: [Templates for the data records](http://support.automation.siemens.com/WW/view/en/29430270)

---

**See also**

[ET 200AL distributed I/O system](#et-200al-distributed-io-system)
  
[Expanding ET 200SP with ET 200AL modules](#expanding-et-200sp-with-et-200al-modules)
  
[Configuration control with ET 200SP](#configuration-control-with-et-200sp)

#### ET 200MP

This section contains information on the following topics:

- [ET 200MP distributed I/O system](#et-200mp-distributed-io-system)
- [Interface module parameters](#interface-module-parameters-1)
- [Input module parameters](#input-module-parameters-1)
- [Output module parameters](#output-module-parameters-1)

##### ET 200MP distributed I/O system

###### Definition

The ET 200MP distributed I/O system is a scalable and flexible distributed I/O system for connection of process signals to a central controller via a field bus.

###### Application area

The ET 200MP is a multi-functional distributed I/O system for various fields of application. The scalable design allows you to configure the system exactly to the specific requirements on location.

The ET 200MP complies with IP 20 degree of protection and is intended for installation in a control cabinet.

###### Structure

The ET 200MP is installed on a mounting rail and comprises:

- An interface module that communicates with all IO controllers conforming to the PROFINET standard IEC 61158
- Up to 30 modules (power supply modules and I/O modules from the S7-1500 I/O range) can be inserted to the right of the interface module.
- If you insert a power supply module to the left of the interface module, this yields a possible maximum configuration of 32 modules in total.
- The number of insertable I/O modules is limited by their power requirements.

###### Slot rules

- Slot 0: Power supply module (optional)
- Slot 1: Interface module
- Slot 2 to 31: I/O modules or power supply modules

##### Interface module parameters

This section contains information on the following topics:

- [Supply voltage L+ connected](#supply-voltage-l-connected)
- [Configuration control (handling options) with ET 200MP](#configuration-control-handling-options-with-et-200mp)

###### Supply voltage L+ connected

###### Parameter "Supply voltage L+ connected"

This parameter influences the diagnostics and the checking of the power budget.

- Diagnostics of the ET 200MP:

  If the actual configuration does not match the preset configuration with regard to the supply voltage of the interface module, the interface module generates a diagnostic alarm. Example: You have deactivated the "Supply voltage L+ connected" option, but you have connected the supply voltage in the actual configuration.
- Power budget check during configuration:

  The power budget changes in accordance with the parameter setting: Either the interface module feeds power into the backplane bus or it draws power from the backplane bus.

The default ("Supply voltage L+ connected" option is **activated**) means that the front of the interface module is supplied with 24 V DC and the power is stored in the backplane bus.

If the "Supply voltage L+ connected" option is **deactivated**, the interface module may not be supplied with 24 V DC on the front.

In this case, insert a power supply unit (PS) on the left next to the interface module that supplies the interface module and the modules to the right of the interface module.

> **Note**
>
> We recommend that you always supply the interface module on the front side with 24 V DC. If a system power supply unit (PS) is inserted and connected additionally **before** or on the left next to the interface module, both the power from the system power supply unit (PS) as well as the power from the integrated power supply of the interface module are then available to the configuration.
>
> In this case, you do not have to change the default setting of the parameter.

###### Configuration control (handling options) with ET 200MP

###### Operating principle

Configuration control allows you to operate various real configurations (options) with a single configuration of the distributed I/O device ET 200MP.

Configuration control provides you with the option of configuring the ET 200MP distributed I/O device with its maximum configuration and still operating it with modules missing. If missing modules are retrofitted later, no new configuration is required and the hardware configuration does not have to be reloaded either.

Using control data record 196, which is transferred to the interface module in the user program, you define a current configuration. You transfer the control data record with the instruction WRREC.

Readback data record 197 is used to read the actual configuration of an ET 200MP.

###### Requirements

The CPU startup parameter "Compare preset to actual configuration" is set to Startup even if mismatch (default setting). This setting is also selected for the startup parameters of the individual modules of the ET 200MP.

###### Enabling configuration control

In the properties of the interface module under Module parameters &gt; General &gt; Configuration control, select "Enable reconfiguration of device via user program". This activates configuration control.

###### Control data record 196 for ET 200MP

The figure below shows the start of control data record 196 for the configuration control of an ET 200MP.

The data block is 36 bytes long (maximum configuration with 32 modules). The value "36" therefore appears in the "block_length" element of the data record.

If you configure an ET 200MP in STEP 7 with fewer modules, the data block will be shorter: If there are only five modules, for example, the data record is reduced to 9 bytes (4 bytes for the header plus one byte for each module).

There is one byte in the data record for each module. The position of this byte in the data record codes a module in the original configuration with STEP 7:

- "slot_0 power supply" (byte 4 in the data record below) corresponds to the power supply module in slot 0 in the configuration with STEP 7.
- "slot_2" (byte 5 in the data record) corresponds to the module in slot 2 in the configuration.
- "slot_3" (byte 6 in the data record) corresponds to the module in slot 3 in the configuration.
- "slot_4" (byte 7) corresponds to the module in slot 4 in the configuration.
- etc.

> **Note**
>
> **Interface module in slot 1**
>
> Configuration control is controlled by the interface module (slot 1/submodule 1). The interface module in slot 1 is therefore not an element of the configuration control and is not included in the data record.

**Value in slot_x**

The current slot is coded by the figure that is assigned to "slot_x" (by its value). Examples:

- The value "2" in slot_2 means you are assigning the module originally inserted in slot 2 to slot 2 in the current configuration (slot_2 = 2).
- The value "3" in slot_2 means you are assigning the module originally inserted in slot 2 to slot 3 in the current configuration (slot_2 = 3).
- The value "4" in slot_2 means you are assigning the module originally inserted in slot 2 to slot 4 in the current configuration (slot_2 = 4).
- etc.

**Example for data record 196**

The following data record was created for a configuration that changes the original configuration with STEP 7.

The modified configuration has the following properties:

- The module inserted in slot 0 in the configuration (power supply module) is also inserted in slot 0 in the current configuration (specification).
- The module inserted in slot 2 in the configuration (module 2) is also inserted in slot 2 in the current configuration.
- The module inserted in slot 3 in the configuration (module 3) does not exist in the current configuration.
- The module inserted in slot 4 in the configuration (module 4) is inserted in slot 3 in the current configuration.
- The module inserted in slot 5 in the configuration (module 5) is inserted in slot 4 in the current configuration.
- etc.

The bytes "slot_6" to "slot_31" are not shown in the figure below.

![Control data record 196 for ET 200MP](images/80111352075_DV_resource.Stream@PNG-en-US.png)

###### Rules

- If a module dos not exist in the current configuration, this is indicated by the value 127: "slot_x" = 127.
- The power supply module is always in slot 0 ("slot_0 power supply" = 0).
- The interface module in slot 1 is not included in the control data record.

###### Addressing the interface module using the HW identifier

To transfer data record 196 with the instruction WRREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Readback data record 197 for ET 200MP

Readback data record 197 is used to read the actual configuration of a station (in this case, of an ET 200MP).

This data record allows you to check the real configuration of the ET 200MP (actual configuration). The readback data record for each configured module specifies whether or not it is actually available.

- The value "1" means that the correct module is inserted in the correct slot.
- The value "0" codes all other options (wrong module, empty slot, reserve module).

Example:

A module has been configured with STEP 7 for slot 4.

This module has then been moved to slot 3 in the current configuration using data record 196.

If this module is also really in slot 3, this is coded by the value "1" (status_slot_4 = 1).

**Configuration details:**

The configuration of the data block corresponds to the original configuration of the ET 200MP with STEP 7.

There is a byte in the data record for each module. The position of this bytes in the data record corresponds to the position of a module in the original configuration with STEP 7.

Sequence of bytes:

- "status_slot_0 power supply" (byte 4 in the data record below) corresponds to the power supply module in slot 0 in the configuration with STEP 7.
- "status_slot_2" (byte 5) corresponds to the module in slot 2 in the configuration.
- "status_slot_3" (byte 6) corresponds to the module in slot 3 in the configuration,
- etc.

You can choose any name for the components (for example "status_slot_2").

**Meaning of "status_slot_x":**

- The value "1" in status_slot_x means that module x is in the correct slot.
- The value "0" in status_slot_x codes all other possibilities (wrong module, module does not exist).

**Example:**

The figure below shows readback data record 197 for the configuration of an ET 200MP in which there is no module 3 (the module in slot 3 in the configuration).

All other modules are available and correctly plugged.

The bytes "status_slot_6" to "status_slot_31" are not shown in the figure below.

![Readback data record 197 for ET 200MP](images/75535233419_DV_resource.Stream@PNG-en-US.PNG)

###### Reading readback data record 197

You can read readback data record 197 from the ET 200MP with the instruction RDREC. RDREC operates asynchronously. If you call RDREC in the startup OB, you must call the instruction multiple times using a loop until the "BUSY" or "DONE" output parameter indicates that the data record has been read.

To read data record 197 with the instruction RDREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Additional information and examples

Further information on ET 200MP can be found in the manual for [IM 155-5 PN](http://support.automation.siemens.com/WW/view/en/89261636).

Specific examples of configuration control can be found in this [application description](http://support.automation.siemens.com/WW/view/en/29430270).

You will find a library of the data records and other application examples here: [Templates for the data records](http://support.automation.siemens.com/WW/view/en/29430270)

---

**See also**

[Documentation on configuration control](http://support.automation.siemens.com/WW/view/en/67295970)

##### Input module parameters

This section contains information on the following topics:

- [Parameters of the analog input modules](#parameters-of-the-analog-input-modules-1)
- [Temperature compensation for thermocouples](#temperature-compensation-for-thermocouples)

###### Parameters of the analog input modules

###### Missing supply voltage L+

Enabling of the diagnostics for missing or insufficient supply voltage L+.

###### Wire break

Enabling of the diagnostics if the module has no current flow or the current is too weak for the measurement at the corresponding configured input or the applied voltage is too low.

###### Current limit for wire break diagnostics

Threshold at which a wire break is reported. The value can be set to 1.185 mA or 3.6 mA, depending on the sensor used.

###### Overflow

Enabling of the diagnostics if the measured value exceeds the overrange.

###### Underflow

Enabling of the diagnostics if the measured value undershoots the underrange.

###### Common mode error

Enable diagnostics if the valid common mode voltage is exceeded.

###### Reference channel error (only for AI 8xU/I/RTD/TC ST)

- Enable diagnostics on error at the temperature compensation channel, e.g. wire break.
- Dynamic reference temperature compensation type is configured and no reference temperature has been transferred to the module yet.

###### Temperature coefficient

The temperature coefficient depends on the chemical composition of the material. In Europe, only one value is used per sensor type (default value).

The correction factor for the temperature coefficient (α value) specifies how much the resistance of a certain material changes when the temperature is raised by 1 °C.

The further values facilitate a sensor-specific setting of the temperature coefficient and enhance accuracy.

###### Interference frequency suppression

At analog input modules, this suppresses interference caused by the frequency of AC mains.

The frequency of the AC network may interfere with measured values, particularly for measurements within low voltage ranges and when thermocouples are being used. With this parameter, you define the mains frequency in your system.

###### Smoothing

The individual measured values are smoothed using filtering. Smoothing can be set in 4 stages for the analog input modules AI 8xU/I/RTD/TC ST and AI 8xU/I HS.

Smoothing time = number of module cycles (k) x cycle time of the module.

The figure below shows the number of module cycles after which the smoothed analog value is almost 100%, depending on the set smoothing. Is valid for each signal change at the analog input.

![Smoothing](images/44232344971_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | None (k = 1) |
| ② | Weak (k = 4) |
| ③ | Medium (k = 16) |
| ④ | Strong (k = 32) |

###### Reference junction (only for AI 8xU/I/RTD/TC ST)

The following settings can be configured for the reference junction parameter:

Possible parameter assignments for the reference junction parameter

| Setting | Description |
| --- | --- |
| Fixed reference temperature | The reference junction temperature is configured and stored in the module as a fixed value. |
| Dynamic reference temperature | The reference junction temperature is transferred in the user program from the CPU to the module by data records 192 to 199 using the WRREC (SFB 53) instruction. |
| Internal reference junction | The reference junction temperature is determined using an integrated sensor of the module. |
| Reference channel of the module | The reference junction temperature is determined using an external resistance thermometer (RTD) at the reference channel (COMP) of the module. |

> **Note**
>
> **Fixed reference temperature**
>
> During parameter assignment of a thermocouple Type B, only the setting "Fixed reference temperature" with a temperature of 0 °C is possible.

###### Enable hardware interrupt 1 or 2

Enable a hardware interrupt if high limit 1 or 2 is exceeded, or low limit 1 or 2 is violated.

###### Low limit 1 or 2

Specifies the low limit threshold that triggers hardware interrupt 1 or 2.

###### High limit 1 or 2

Specifies the high limit threshold that triggers hardware interrupt 1 or 2.

###### Temperature compensation for thermocouples

###### Introduction

You have several options of measuring the reference junction temperature in order to obtain an absolute temperature value as a function of the temperature difference between the reference junction and the measuring point.

You can use various compensation options depending on the required location of the reference junction.

> **Note**
>
> During parameter assignment of a thermocouple Type B, only the setting "Fixed reference temperature" with a temperature of 0 °C is possible.

###### Options of compensating for the reference junction temperature

| Compensation options | Explanation | Application case |
| --- | --- | --- |
| Internal reference junction | With this compensation, the reference junction temperature is determined using an integrated sensor of the module.   **Procedure**   Connect the thermocouple to the I/O module directly or with compensating lines. | - For the connection, you use compensating lines matching the thermocouple material. - If the reference junction temperature and the module temperature are identical in your system, you may also use lines made from a different material. |
| Reference channel of the module | The reference junction temperature is determined using an external resistance thermometer (RTD).   **Procedure**   Connect the thermocouple to the supply lines at the reference junction, either directly or with compensating lines. You connect the supply lines to the appropriate terminals of the module.  Connect the resistance thermometer (RTD) to the reference channel of the module. The resistance thermometer (RTD) must be placed in the area of the reference junction. | - You want to measure the temperature directly at the reference junction. - The measured temperatures of all channels that you have configured for this compensation type is corrected automatically by the temperature value of the reference junction. - You can use inexpensive lines, e.g., copper lines, from the reference junction to the module. |
| Dynamic reference temperature | The temperature of the reference junction is determined via a module. This temperature value is transferred to other modules via a data record in the user program.   **Procedure**   Connect the resistance thermometer (RTD) for the reference junction to any channel.  The reference junction temperature is communicated from the CPU to the module by data records 192 to 199 using the WRREC instruction. | - You use multiple modules at the reference junction and can therefore compensate all channels using a common temperature value. - You require only one resistance thermometer (RTD) to acquire the temperature value. - You can use inexpensive lines, e.g., copper lines, from the reference junction to the module. |
| Fixed reference temperature | The reference junction temperature is stored in the module as a fixed value.    **Procedure**   Connect the thermocouple to the supply lines at the reference junction, either directly or with compensating lines. You connect the supply lines to the appropriate terminals of the module.  When configuring the module, specify a fixed temperature value for the reference junction (e.g. 20 °C). | - You keep the reference junction temperature constant and know the temperature value. - You can use inexpensive lines, e.g., copper lines, from the reference junction to the module. |

##### Output module parameters

This section contains information on the following topics:

- [Parameters of the analog output modules](#parameters-of-the-analog-output-modules)
- [Pulse-width modulation (PWM)](#pulse-width-modulation-pwm)

###### Parameters of the analog output modules

###### Missing supply voltage L+

Enabling of the diagnostics, with missing or too little supply voltage L+.

###### Short-circuit to ground

Enabling of the diagnostics if a short-circuit of the actuator supply to ground occurs.

###### Wire break

Enabling diagnostics if the line to the encoder is interrupted.

###### Overflow

Enabling of the diagnostics if the measured value exceeds the overflow range.

###### Underflow

Enabling of the diagnostics if the measured value falls below the underflow range.

###### Reaction to CPU STOP

Determines the reaction of the output to the CPU going into STOP state.

###### Substitute value

The substitute values are values that the outputs (the output) issue in the event of a CPU STOP.

###### Pulse-width modulation (PWM)

The channels of some modules support the pulse width modulation (PWM) function. You can use the pulse width modulation function to easily generate periodic pulses with a constant rated voltage and a variable pulse duration for the above-mentioned channels.

###### Configuration

You configure the pulse width modulation with the following parameters:

- Enable PWM function on module
- Set PWM operating mode for the corresponding channel
- Set period

###### How it works

In the pulse width modulation mode, the correspondingly configured outputs provide a pulse width modulated output signal.

Pulse width modulation is characterized by its time period (frequency) and its duty factor. The duty factor describes the relation between pulse duration and time period.

The pulse duration is derived from the time period and the duty factor: Pulse duration = duty factor x time period.

Example for duty factor of 50% and time period of 10 ms:

Pulse duration 0.5 x 10 ms = 5 ms

You define the duty factor of the channels in the user program using the output value (0 ... 1000) in the process image output.

The output signal is a square wave signal (pulse sequence of on and off pulses).

![How pulse width modulation works](images/79193212683_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time period T (2 to 100 ms); Frequency of the pulse width modulation: f = 1/T (10 to 500 Hz) |
| ② | Pulse duration (duty factor x time period) |

How pulse width modulation works

###### Minimum pulse duration

The minimum pulse duration is 300 μs due to the hardware. The duty factor can be adjusted from 0.0 to 100.0%. The time period can be adjusted from 2 to 100 ms.

Example: If you configure a time period of 2 ms and set a duty factor of 0.1% for the output, this would result in a pulse duration of 200 μs. In fact, the output works with a minimum pulse duration of 300 μs.

###### Pulse waveform

The pulse duration of the actual signal profile is slightly longer than the specified, ideal pulse duration.

The figure below shows the reaction of the output to control by PWM. The blue line shows the specified, ideal signal profile (square wave signal), with which the output is controlled. The red dashed line show the actual signal profile on the output graph, caused by the externally connected load.

![Pulse waveform at output terminal](images/105729026443_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Time period |
| ② | Pulse duration (duty factor x time period) |

Pulse waveform at output terminal

#### ET 200M

This section contains information on the following topics:

- [Configuring an ET 200M](#configuring-an-et-200m)
- [ET 200M configuration](#et-200m-configuration)
- [Configuration of the 'Module replacement during operation' function](#configuration-of-the-module-replacement-during-operation-function)
- [Signal modules for process automation](#signal-modules-for-process-automation)
- [IQ Sense module](#iq-sense-module)

##### Configuring an ET 200M

###### Introduction

For the ET 200M series, you can find a wide range of modules in the hardware catalog under "Distributed I/O".

###### Configuration and parameter assignment

Information on configuration and parameter assignment can be found in the following sections.

##### ET 200M configuration

###### Definition

The distributed IO device, ET 200M, is a modular DP slave with an IP 20 degree of protection.

The ET 200M has the configuration technology of the S7‑300 automation system and consists of an IM 153‑x and I/O modules of the S7‑300.

ET 200M supports communication with:

- all DP masters compliant with IEC 61784-1:2002 Ed1 CP 3/1
- all IO controllers compliant with IEC 61158

###### Configuration of the ET 200M (example)

![Configuration of the ET 200M (example)](images/46300876683_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Power supply module PS 307 |
| ② | Interface module IM 153‑x |
| ③ | up to 12 I/O modules (SM / FM / CP) |

##### Configuration of the 'Module replacement during operation' function

###### Introduction

The ET 200M supports the "Replace modules during operation" function and the associated pull/plug interrupt.

The "Replace modules during operation" function makes it possible for you to pull modules from or plug modules into the ET 200M rack during operation.

###### Requirement

You have configured an interface module that supports replacing modules during operation. (as of IM 153-1, article no. 153-1AA02-0XB0).

In addition, the configured CPU must also support the function, e.g. for PROFIBUS an S7-400 with DP interface.

You must use the active backplane bus (bus rail with slots) for the hardware configuration. The conventional profile rail with bus connectors between the modules does not support this function.

###### Configuring

If the configuration requirements have been met, the "Replace modules during operation" parameter is available for selection in the inspector window's "Module parameters" area. Below this parameter, a table for the configured modules is displayed, which shows the required active bus modules for the hardware configuration.

For a PROFIBUS configuration, the "Startup if preset configuration does not match actual configuration" option is displayed. This option is automatically enabled if "Replace modules during operation" is enabled.

##### Signal modules for process automation

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Changeover contact](#changeover-contact)
- [Technological parameters](#technological-parameters)

###### Fundamentals

###### Introduction

Signal modules for the process automation are S7-300 models, such as SM 321; DI 16xNAMUR or SM 322; DO 16x24VDC/0.5A.

They are being operated in a DP slave (IM 153-2).

Unlike standard modules, they offer the following additional technical functions, such as pulse extension and chatter monitoring.

---

**See also**

[Changeover contact](#changeover-contact)
  
[Technological parameters](#technological-parameters)

###### Changeover contact

###### "Changeover contact" sensor type

If the digital inputs of a channel group are configured as "changeover contacts", the module runs diagnostics for the changeover contact sensor type for this channel group.

###### Changeover contact

A changeover contact is an auxiliary switch with only one moving switch element with one close setting each for closed and open switching device.

Remember the following rule:

- Always connect a normally open contact to the "even" channel
- Always connect a normally closed contact to the "odd" channel.

The tolerated switchover time between the two channels is fixed at 300 ms.

If the result of the check is negative, then

- the module identifies the value status of the normally open channel as "invalid"
- the module generates a diagnostic entry for the normally open channel
- triggers a diagnostic interrupt (if diagnostic interrupts have been enabled)

The digital input signal and the value status are updated only for the normally open channel. For the normally closed channel, the digital input signal is set permanently to "zero" and the value status to "invalid" since this channel is used only to check the sensor.

Diagnostics depends on the "Selection" parameter (of the sensor). You should also note the special features of diagnostics with the changeover contact sensor type in the "Signal Modules for Process Automation" manual.

---

**See also**

[Documentation on modules for process automation](http://support.automation.siemens.com/WW/view/de/7215812/0/en)

###### Technological parameters

###### Pulse extension and flutter monitoring

Pulse extension is a function for changing a digital input signal. A pulse at a digital input is extended to at least the length set in the parameters. If the input pulse is already longer than the specified length, it is not changed.

If you want the pulse to be extended, click in the box to select the time. If you do not want the pulses to be extended, select the "---" entry.

Flutter monitoring is a process control function for digital input signals. It detects and reports signal changes that are unexpected in process control, for example when an input signal fluctuates too often between "0" and "1".

Flutter monitoring is possible only when group diagnostics has also been enabled for this input.

###### Monitoring window and number of signal changes

Flutter monitoring works with aid of the two parameters Monitoring window and Number of signal changes.

The first time the signal changes, the time set as the monitoring window is started. If the signal changes more often during this time than allowed by the number of signal changes parameter, this is signaled as a flutter error. If no flutter error is detected during the monitoring window time, the monitoring window can be restarted at the next signal change.

> **Note**
>
> If you set pulse extension for an input channel, this also affects the flutter monitoring enabled for this channel. The "extended pulse" signal is the input signal for the flutter monitoring. You should therefore make sure that the values set for pulse extension and flutter monitoring are compatible with each other.

---

**See also**

[Documentation on modules for process automation](http://support.automation.siemens.com/WW/view/de/7215812/0/en)

##### IQ Sense module

This section contains information on the following topics:

- [Properties of 8 IQ-SENSE](#properties-of-8-iq-sense)
- [Anti-interference group](#anti-interference-group)
- [Encoder type](#encoder-type)
- [Switching hysteresis](#switching-hysteresis)
- [Time function,time value](#time-functiontime-value)
- [Multiplex/synchronous mode](#multiplexsynchronous-mode)
- [AFI value](#afi-value)
- [Transponder type](#transponder-type)

###### Properties of 8 IQ-SENSE

###### Properties

The 8 IQ-SENSE module has the following properties:

- Connection of sensors with IQ-SENSE®, photoelectric proximity switches: for example, reflex sensors, diffuse sensors, and laser sensors.
- It can be used centrally in an S7-300 or distributed in an ET 200M.
- You can connect up to 8 sensors to every module. Each sensor requires a two-wire cable.
- Function reserve that can be assigned parameters.
- Time functions, switching hysteresis, synchronous mode that can be assigned parameters
- Sensitivity and distance values can be specified (IntelliTeach using the "IQ-SENSE Opto" FB)
- Teach-in
- Sensors can be removed and inserted during operation (automatic reassignment of parameters)

###### Anti-interference group

Only for optical IQ Sense devices (IQ profile ID 1).

For IQ Sense devices with IQ profile ID 128 (ultrasound), see "Multiplex/synchronous mode" under the channel-specific parameters.

Prevention of interference (e.g., scattered light) by assigning an anti-interference group. This means:

- Anti-interference group: None (= default)  
  Optical sensors on one or more modules can mutually influence each other when unfavorably arranged.
- Anti-interference group: 3 or 4  
  Optical sensors on the same module with anti-interference group 3 or 4 cannot mutually influence each other. Similarly, optical sensors on different modules with anti-interference group 3 or 4 cannot mutually influence each other. You need not maintain minimum clearance between the IQ Sense devices and can, for example, align two retroreflective sensors on a single reflector.

###### Operating principle

The diagram below explains the functioning of the anti-interference group parameter:

![Operating principle](images/46358376587_DV_resource.Stream@PNG-en-US.png)

Mutual interference is only possible between the optical sensors of the modules in slot 5, 6, 7 and 9 because they are in the same anti-interference group 3 or "None" is set.

> **Note**
>
> Sensors in the same anti-interference group must be installed to maintain the minimum clearance (see sensor package insert) and to prevent mutual interference.

###### Encoder type

This parameter is used to set the sensor type per channel:

- Reflex sensor or
- Diffuse sensor or
- Disabled

###### Diffuse sensor

Diffuse sensor

| Diffuse sensor | Object |  |
| --- | --- | --- |
| Transmitter   Receiver | ![Diffuse sensor](images/46358408843_DV_resource.Stream@PNG-de-DE.png) | Circuit state 0: No object detected, which means the object is not in the beam. The receiver does not see any light. |
| Transmitter   Receiver | ![Diffuse sensor](images/46358433547_DV_resource.Stream@PNG-de-DE.png) | Circuit state 1: Object detected, which means the object is in the beam. The receiver does not see any light. |

###### Reflex sensor

Reflex sensor

| Reflex sensor | Object |  |
| --- | --- | --- |
| Transmitter   Receiver | ![Reflex sensor](images/46358445451_DV_resource.Stream@PNG-de-DE.png) | Circuit state 0: No object detected, which means the object is not in the beam. The receiver sees light. |
| Transmitter   Receiver | ![Reflex sensor](images/46358482955_DV_resource.Stream@PNG-de-DE.png) | Circuit state 1: Object detected, which means the object is in the beam. The receiver does not see any light. |

###### Switching hysteresis

Faults with the diffuse sensor or in the production process can result in signal wobbles. The measured value then changes the switching threshold by 100 % (object detected - object not detected). You can prevent this switching threshold wobble using the switching hysteresis parameter. This will ensure a stable output signal on the sensor.

You can assigned parameters to 5 %/10 %/20 %/50 % for switching hysteresis.

###### Requirements

You can only set the switching hysteresis parameter for diffuse sensors with background fadeout.

###### Operating principle

![Switching hysteresis parameter](images/46358501259_DV_resource.Stream@PNG-en-US.png)

Switching hysteresis parameter

###### Time function,time value

These parameters can be used to set the electronic module for its specific application.

###### Operating principle

![Time functions, time values parameters](images/46358519563_DV_resource.Stream@PNG-en-US.png)

Time functions, time values parameters

###### Multiplex/synchronous mode

For the prevention of mutual influence between IQ Sense ultrasound devices in spatial proximity (devices with IQ profile ID 128), use the "Multiplex/synchronous mode" parameter.

###### Settings for the multiplex/synchronous mode parameter

Disabled: Mutual influence between IQ Sense ultrasound sensors in spatial proximity is possible (default). The cycle time is determined by the IQ Sense ultrasound sensor.  
  
Multiplex: The IQ Sense ultrasound sensors determine the process value (distance) one after another, preventing them from affecting one another. The cycle time here is the sum of the configured synchronous cycle times of the IQ Sense ultrasound sensors that are to be multiplexed.  
  
Synchronization: The IQ Sense ultrasound sensors determine the process value (distance) at exactly the same time, preventing them from affecting one another. The cycle time here corresponds to the greatest configured synchronous cycle time from among the IQ Sense ultrasound sensors that are to be synchronized.  
  
You can, for example, use synchronous operation for a curtain function in which several IQ Sense ultrasound sensors aligned in parallel share a single extended detection area. The sensors simultaneously emit an ultrasound impulse. When an object enters the detection area, the sensor nearest to the object receives the echo most quickly. The object can therefore not only be detected, it can be located as well.

###### AFI value

Using the AFI value (application series identifier, as defined in the ISO 15693-3 international standard), transponders can be selected for different applications. Only transponders whose AFI value coincides with the value set on the sensor are processed. If a transponder has the AFI value "0", it can be identified and processed regardless of the AFI value of the sensor.

This parameter is only important if it is supported by the ident system, otherwise any value (normally "0") may be assigned.

###### Transponder type

Depending on the type of the transponder, you must configure whether it is an ISO transponder or a vendor-specific type.

For transponders in accordance with international standard ISO 15693, the value "1" should be selected; for all other types "0" is set. Based on this setting, one of the two possible air interface drivers is selected in the sensor.

This parameter is only important if it is supported by the ID system, otherwise any value (normally "0") may be assigned.

#### ET 200S

This section contains information on the following topics:

- [Configuring an ET 200S](#configuring-an-et-200s)
- [Frequency converters](#frequency-converters)

##### Configuring an ET 200S

###### Introduction

For the ET 200S series, you can find a wide range of modules in the hardware catalog under "Distributed I/O".

###### Assigning parameters

For information on configuration and parameter assignment, refer to "See also".

---

**See also**

[Configuring an ET 200S](Configuring%20PROFIBUS%20DP.md#configuring-an-et-200s)

##### Frequency converters

This section contains information on the following topics:

- [Use of the frequency converter](#use-of-the-frequency-converter)

###### Use of the frequency converter

###### Frequency converters

The frequency converters ICU24 and ICU24F (as fail-safe version) are modular frequency converters that are completely embedded in the distributed I/O system ET 200S. For parameterization of both modules, please see the following.

###### Message frame

The message frame number and the operating mode of the module are only displayed and cannot be modified.

###### Application ID

You indicate the saved parameters in the frequency converter as a whole with the application ID. Enter an application ID from the value range 0 to 65535. During startup (or pull/plug), this ID is compared with the application ID stored on the converter.

Converters that work with identical applications are usually also identically parameterized and should be identified with the same application ID. Converters with the same application ID may be exchanged between each other. Copying of the complete parameterization of a converter to another converter, for example, via an MMC, is only accepted, if both have the same application ID.

Converters that work with different applications and are parameterized differently must be identified by different application IDs. This prevents a converter with unsuitable parameterization from starting on an incorrect slot, i.e. on the wrong application. This also prevents the parameterization that is saved in the converter from being accidently overwritten with any parameteriation that is stored on an MMC.

###### Enable diagnostic interrupt

You can enable the diagnostic interrupt for the frequency converter. If diagnostic interrupt is enabled, an OB 82 must be available in a CPU to process the diagnostic events.

---

**See also**

[Documentation for the frequency converter](http://support.automation.siemens.com/WW/view/en/26291825/0/en)

#### ET 200pro

This section contains information on the following topics:

- [ET 200pro with own CPU module](#et-200pro-with-own-cpu-module)
- [Configuration control with ET 200pro](#configuration-control-with-et-200pro)
- [Use of the frequency converter](#use-of-the-frequency-converter-1)

##### ET 200pro with own CPU module

###### ET 200pro with own CPU

The ET 200pro can be equipped with its own CPU, for example with the CPU 1516pro.

In this regard, note the following rules.

**Expansion rules with the CPU 1516pro:**

- You can expand the CPU 1516pro with up to 16 modules.
- The total width can be a maximum of one meter.

**Expansion with wide modules**

If the maximum width of one meter is exceeded in a configuration with large modules (for example frequency converters or motor starters), the configuration cannot be compiled. In this case, reduce the configuration.

##### Configuration control with ET 200pro

###### Operating principle

Through the configuration control, it is possible to change the original configuration of an ET 200pro (created by configuring with STEP 7) and to operate the ET 200pro in this modified configuration. STEP 7 is no longer required for this configuration: You communicate to the ET 200pro the slot in which a configured module is actually inserted by means of your user program.

In this case, use control data record 196. In this data record, you code which modules are missing or located in different slots in the real configuration compared to the configuration. The configuration control has no effect on the parameter assignment of the modules (for example, the enabling of diagnostic alarms).

You then call the "WRREC" instruction and use it to write the data record to the interface module of the ET 200pro.

Configuration control gives you the flexibility to vary the configuration of an ET 200pro as long as the real configuration can be derived from a preset maximum configuration (originally created with STEP 7).

The following sections describe how to enable configuration control. They also outline how control data record 196 and readback data record 197 are structured.

###### Requirements

The CPU startup parameter "Compare preset to actual configuration" is set to Startup even if mismatch (default setting). This setting is also selected for the startup parameters of the individual modules of the ET 200pro.

###### Enabling configuration control

Enable the "Allow to reconfigure the device via the user program" parameter when configuring the ET 200pro in STEP 7 ("Configuration control" area).

![Enabling configuration control](images/105175050763_DV_resource.Stream@PNG-en-US.PNG)

###### Configuration of control data record 196 for the ET 200pro

There is a byte in control data record 196 for each module.

The position of this byte in the data record codes one module in the original configuration with STEP 7:

- "slot_IM" (byte 4 in the data record, figure below) corresponds to the module in slot 1 in the configuration
- "slot_2" (byte 5) corresponds to the module in slot 2 in the configuration.
- "slot_3" (byte 6) corresponds to the module in slot 3 in the configuration.
- etc.

**"slot_x" byte**

The current slot is coded by the figure that is assigned to "slot_x" (by its value). Examples:

- The value "2" in byte 5 means you are assigning the module originally inserted in slot 2 to slot 2 in the current configuration (slot_2 = 2).
- The value "3" in byte 5 means you are assigning the module originally inserted in slot 2 to slot 3 in the current configuration (slot_2 = 3).
- The value "4" in byte 5 means you are assigning the module originally inserted in slot 2 to slot 4 in the current configuration (slot_2 = 4).
- etc.

There are no reserve modules for the ET 200pro (unlike for the ET 200S or with BU cover modules for the ET 200SP). For this reason, bit 7 of "slot_x" must not be set.

The value "0" in "slot_x" indicates that this module is not inserted in the current configuration.

###### Example of control data record 196

The figure below shows control data record 196 for a configuration of an ET 200pro with four modules.

This configuration is given as an example:

- The module originally configured with STEP 7 in slot 1 is also inserted in slot 1 in the current configuration.
- The module in slot 2 is in slot 2 in the current configuration.
- The module in slot 3 does not exist in the current configuration.
- The module in slot 4 is actually inserted in slot 3 in the current configuration.

![Example of control data record 196](images/69824992011_DV_resource.Stream@PNG-de-DE.png)

The components of control data record 196 (figure above):

- block_length: Note here the length of the control data record; in the example: 8 (bytes). The length is calculated using the following formula: "Number of assigned slots" + 4.
- block_ID: Enter the figure 196 here.
- version: The ET 200pro uses Version 1 of control data record 196.
- subversion: The ET 200pro uses Subversion 0 of control data record 196.
- slot_IM: The IM module is always inserted in slot 0 of the ET 200pro. Slot 1 always contains the virtual power module that is integrated as a fixed module in the IM module. The "slot_IM" (name can be changed) can contain any values. This byte is not interpreted in the configuration control of the ET 200pro.
- slot_2: The configured module 2 is inserted in slot 2 (value "2").
- slot_3: The configured module 3 is not present in the current configuration (value "0").
- slot_4: The configured module 4 is inserted in slot 3 in the current configuration (value "3").

###### Definition of control data record 196

A control data record 196 containing a slot assignment is defined for configuration control.

|  |  |  |  |
| --- | --- | --- | --- |
| **Byte** | **Element** | **Value** | **Description** |
| 0 | Block length | e.g., 8 for ET 200pro with four modules | The length of the data record is calculated using the formula: 4 + Number of modules in bytes |
| 1 | Block ID | 196 | ID for control data record 196 |
| 2 | Version | 1 | Version 1 of control data record 196 |
| 3 | Subversion | 0 | Subversion 0 of control data record 196 |
| 4 | Slot_1 | Any values are possible: For example "1" | This byte is not interpreted for the ET 200pro because the power module that is integrated as a fixed module in the IM module of the ET 200pro is always inserted in slot 1. |
| 5 | Slot_2 | Coding of the actual slot:  2 = Slot 2  3 = Slot 3  4 = Slot 4  etc.  Coding for missing module:  0 = No slot, module not present | Byte 5 indicates where the module originally configured with STEP 7 in slot 2 is actually inserted in the current configuration.          Example: 2  The module originally configured with STEP 7 in slot 2 is also actually located in slot 2 in the current configuration (value "2"). |
| 6 | Slot_3 | Coding of the actual slot:  2 = Slot 2  3 = Slot 3  4 = Slot 4  etc.  Coding for missing module:  0 = No slot, module not present | Byte 6 indicates where the module originally configured with STEP 7 in slot 3 is actually inserted in the current configuration.    Example: 0  The module originally configured with STEP 7 in slot 3 is not present in the current configuration (value "0"). |
| 7 | Slot_4 | Coding of the actual slot:  2 = Slot 2  3 = Slot 3  4 = Slot 4  etc.  Coding for missing module:  0 = No slot, module not present | Byte 7 indicates where the module originally configured with STEP 7 in slot 4 is actually inserted in the current configuration.    Example: 3  The module originally configured with STEP 7 in slot 4 is actually located in slot 3 in the current configuration (value "3"). |
| : | : | : | : |

###### Writing a data record

Transfer the control data record to the ET 200pro module.

To do so, call the extended WRREC (Write data record) instruction, and transfer the control data record created.

If you do not transfer a control data record, the interface module uses the original configuration with STEP 7. Here, the following applies: Configured module x is inserted in real slot x.

###### Addressing the interface module using the HW identifier

To transfer data record 196 with the instruction WRREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Error messages

The following error messages are returned if an error occurs when writing control data record 196:

Error messages

| Error code | Meaning |
| --- | --- |
| 16#80A2 | DP protocol error on layer 2 Indicates that a data record has not been acknowledged due to the system. |
| 16#80B1 | Invalid length; the length information in data record 196 is not correct. |
| 16#80B5 | Configuration control parameters not assigned. |
| 16#80B2 | Invalid slot: The configured slot is  not assigned. |
| 16#80B8 | Parameter error; module signals invalid parameters. |
| 16#80C5 | DP slave or module not available. Indicates that a data record has not been acknowledged due to the system. |

###### Readback data record 197 for ET 200pro

Readback data record 197 is used to read the actual configuration of a station (in this case of an ET 200pro).

This data record allows you to check the real configuration of the ET 200pro (actual configuration). The feedback data record for each configured module specifies whether or not it is actually present.

- The value "1" means that the correct module is inserted in the correct slot.
- The value "0" codes all other options (wrong module, empty slot).

Example:

A module has been configured with STEP 7 for slot 4.

This module has then been moved to slot 3 in the current configuration using data record 196.

If this module is also really in slot 3, this is coded by the value "1" (status_slot_4 = 1).

**Configuration details:**

The configuration of the data block corresponds to the original configuration of the ET 200pro with STEP 7.

There is a byte in the data record for each module. The position of this bytes in the data record corresponds to the position of a module in the original configuration with STEP 7.

Sequence of bytes:

- "status_slot_IM" (byte 4 in the data record) corresponds to the module in slot 1 in the configuration,
- "status_slot_2" (byte 5) corresponds to the module in slot 2 in the configuration
- "status_slot_3" (byte 6) corresponds to the module in slot 3 in the configuration,
- etc.

The following example is for a configuration with 4 modules. The value "8" therefore appears in the "block_length" element of the data record.

If you configure an ET 200pro in STEP 7 with fewer modules, the data block will be shorter.

You can choose any name for the components of the control data record (for example "status_slot_2").

**Meaning of "status_slot_x":**

- The value "1" in status_slot_x means that module x is inserted in the correct slot
- The value "0" in status_slot_x codes all other options (wrong module, module does not exist).

**Example:**

The figure below shows readback data record 197 for an ET 200pro with four modules.

- There is no module 3 (this was assigned in control data record 196, see section "Example of control data record 196" above)
- The three other modules are actually inserted in the ET 200pro.

![Readback data record 197 for ET 200pro](images/70949475595_DV_resource.Stream@PNG-de-DE.PNG)

###### Reading readback data record 197

You can read readback data record 197 from the ET 200pro with the instruction RDREC. RDREC operates asynchronously. If you call RDREC in the startup OB, you must call the instruction multiple times using a loop until the "BUSY" or "DONE" output parameter indicates that the data record has been read.

To read data record 197 with the instruction RDREC, you must enter the HW identifier of the IM submodule with the extension "∼Head" as the input parameter for the instruction. The system constant of this HW identifier is, for example, "IO-Device_2∼Head". The system constants of a selected device are, for example, displayed in the network view in the "System constants" tab. Use the corresponding value for addressing.

###### Additional information and examples

Further information on the PN interface module of the ET 200pro is available [here](http://support.automation.siemens.com/WW/view/en/98099372).

Specific examples of configuration control can be found here in this [application description](http://support.automation.siemens.com/WW/view/en/29430270).

You will find a library of the data records and other application examples here:

[Templates for the data records](http://support.automation.siemens.com/WW/view/en/29430270)

---

**See also**

[Configuration control with ET 200SP](#configuration-control-with-et-200sp)

##### Use of the frequency converter

###### Frequency converters

The frequency converters ET 200pro FC and ET 200pro F-FC (as fail-safe version) are modularly design frequency converters that are completely embedded in the distributed I/O system ET 200pro. The following section describes how to configure the two modules.

###### Message frame

The message frame number and the operating mode of the module are only displayed and cannot be modified.

###### Application ID

You indicate the saved parameters in the frequency converter as a whole with the application ID. Enter an application ID from the value range 0 to 65535. During startup (or pull/plug), this ID is compared with the application ID stored on the converter.

Converters that work with identical applications are usually also identically configured and should be identified with the same application ID. Converters with the same application ID may be exchanged between each other. Copying of the complete configuration of a converter to another converter, for example, via an MMC, is only applied, if both have the same application ID.

Converters that work with different applications and are configured differently must be identified by different application IDs. This prevents a converter with unsuitable configuration from starting on an incorrect slot, in other words on the wrong application. This also prevents the configuration that is saved in the converter from being accidently overwritten with any configuration that is stored on an MMC.

###### Enable diagnostic interrupt

You can enable the diagnostic interrupt for the frequency converter. If diagnostic interrupt is enabled, an OB 82 must be available in a CPU to process the diagnostic events.

### IPv4 routing for CM/CP 1500

#### IPv4 routing between communication modules

The function enables static IPv4 routing between communication modules in a rack via the backplane bus. This means that routing between two subnets that are connected via two communication modules of the station is operated via the backplane bus of the station.

The function is supported by the following modules:

- CP 1545‑1
- CM 1542‑1

  As of firmware version V2.0
- CP 1543‑1

  - As of firmware version V2.0 with activated security functions
  - As of firmware version V2.1 with activated security functions

Restrictions: IPv4 routing via the communication module into the CPU of the station is not possible.

Please note:  
If you want to use IP routing you may only configure a router for one communication module in the station.

**IP configuration with CM 1542‑1 as PROFINET IO controller**

If the CM with enabled IPv4 routing over the backplane bus is used as PROFINET IO controller, please note the following points for IP configuration of the subordinate IO devices:

If IP address configuration for the subordinate IO devices is fixed ("Set IP address in the project" option), IPv4 routing over the CM to the IO devices is not possible.

The following settings are required in the IP configuration of the subordinate IO devices to allow IPv4 routing over the CM to those IO devices:

- First select the "Use router" option for the IO device.

  Copy the IP address of the IO controller (CM) to the router address field.
- Activate the "IP address is set directly at the device" option for the IO device.

### IPv6 configuration

This section contains information on the following topics:

- [IPv6 protocol](#ipv6-protocol)
- [IPv6 for CP 154x-1](#ipv6-for-cp-154x-1)

#### IPv6 protocol

The Internet protocol version 6 (IPv6) extends the address range of the Internet protocol version 4 (IPv4).

##### Address format IPv6: Notation

IPv6 addresses consist of 8 fields each with four-character hexadecimal numbers (128 bits in total). The fields are separated by a colon.

Example: fd00:0000:0000:0000:0db8:002f:0000:0000

Rules / simplifications:

- Leading zeros within a field can be omitted.

  Example: fd00:0000:0000:0000:0db8:002f:0000:0000, abbreviated fd00:0:0:0:db8:2f:0:0
- If one or more blocks have the value 0, a shortened notation is possible with two successive colons. To ensure uniqueness, this shortened form can only be used once within the entire address. With two or more such abbreviations, it may not be possible to determine how many blocks were shortened.

  Valid example: fd00::db8:2f:0:0 or fd00:0:0:0:db8:2f:: (both clearly recognizable as fd00:0:0:0:db8:2f:0:0)

  Invalid example: fd00::db8:2f:: (not clear, can be interpreted as fd00:0:0:0:db8:2f:0:0 or fd00:0:0:db8:2f:0:0:0 etc.)
- The last 2 fields or 4 bytes can be written in the normal decimal notation with periods.

  Example: The IPv6 address fd00::db8:fd01:2f is equivalent to fd00::db8.253.1.0.47

The entry of IPv6 addresses is possible in the notations described above. IPv6 addresses are always displayed in the notation of the entry.

##### Different IPv6 addresses of an interface

If you configure multiple IPv6 addresses for the interface of a communication module, please note that the two IPv6 addresses cover different subnet ranges.

---

**See also**

[IPv6 for CP 154x-1](#ipv6-for-cp-154x-1)

#### IPv6 for CP 154x-1

##### IPv6 use for CP 1543‑1 / CP 1545‑1

For all IP services, the CP supports the Internet protocol version 4 (IPv4)

The additional specification of addresses in IPv6 format can be used with the CP for the following services and applications:

- FETCH/WRITE: Direct write/read access by PC stations, SIMATIC S5 or third-party devices
- FTP client: FTP access from the S7-1500 CPU to an FTP server with FTP_CMD program block
- FTP server: FTP access from an FTP client to S7-1500 CPU data areas
- SNMP: Data query using MIB objects according to SNMP
- E-mail: Data transmission from the S7-1500 CPU with the T_Mail program block

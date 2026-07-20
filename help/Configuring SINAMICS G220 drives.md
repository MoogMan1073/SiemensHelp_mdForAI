---
title: "Configuring SINAMICS G220 drives"
package: StdrG220ConfenUS
topics: 150
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring SINAMICS G220 drives

This section contains information on the following topics:

- [SINAMICS G220 drive system](#sinamics-g220-drive-system)
- [Startdrive user interface](#startdrive-user-interface)
- [Fundamentals](#fundamentals)
- [Sequence of a device configuration and basic commissioning](#sequence-of-a-device-configuration-and-basic-commissioning)
- [Configuring devices in the project](#configuring-devices-in-the-project)
- [Establishing an online connection to the target device](#establishing-an-online-connection-to-the-target-device)
- [Diagnostics](#diagnostics)

## SINAMICS G220 drive system

This section contains information on the following topics:

- [Overview of SINAMICS G220](#overview-of-sinamics-g220)

### Overview of SINAMICS G220

#### Drive components in the drive line-up

The G220 drive system generally consists of the following components:

- Control Unit

  The Control Unit controls and monitors the Power Module and the connected motor using several different selectable control modes. The Control Unit is used to control the converter locally or centrally. There are various variants of the G220 Control Unit, depending on the application use.
- Power unit (Power Module)

  Power units supply the motor in a defined power range. In the G220, the power unit is fully integrated in the Control Unit.
- Motor

  A wide range of Siemens motor models are available. Third-party motors of the same motor type can also be used.
- Encoder and Sensor Modules

  Encoders determine the current position of the drive shaft.
- Option Modules

  With these modules, you can extend the Control Unit with additional functions.
- Reactors and filters

You can configure the various G220 drive components in Startdrive via the "device configuration" and "guided quick startup". In a later extension stage, the entire basic configuration and quick commissioning will be possible in the quick startup.

You can use the function view or the parameter view in the "Parameterization" area for any detailed settings.

---

**See also**

[Sequence of a device configuration and basic commissioning](#sequence-of-a-device-configuration-and-basic-commissioning)
  
[Startdrive user interface](#startdrive-user-interface)

## Startdrive user interface

This section contains information on the following topics:

- [G220 hardware catalog](#g220-hardware-catalog)
- [G220 device configuration](#g220-device-configuration)
- [Function view G220](#function-view-g220)
- [Parameter view G220](#parameter-view-g220)
- [Inspector window G220](#inspector-window-g220)
- [Rotating and optimizing G220](#rotating-and-optimizing-g220)
- [Guided quick startup G220](#guided-quick-startup-g220)
- [Icons for arithmetic and controller functions](#icons-for-arithmetic-and-controller-functions)

### G220 hardware catalog

This section contains information on the following topics:

- [Available modules](#available-modules)
- [Available components](#available-components)

#### Available modules

##### Components

The available components are arranged as follows in the hardware catalog:

![Hardware components: G220](images/167238365451_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Available Control Units |
| ② | Motors;   Available motor types for G220 |
| ③ | Measuring systems; all available encoder types |
| ④ | Supplementary system components; e.g. DRIVE-CLiQ option module |

Hardware components: G220

#### Available components

In Startdrive all available hardware components can be configured in the function view or in the parameter view. Below you will find a list of the components that are used in conventional SINAMICS G220 drives in a Startdrive project and can therefore be configured.

Which hardware components can be used?

| Component / drive system | G220 PN | G220 PN  Clean Power |
| --- | --- | --- |
| **Control Unit** |  |  |
| G220 PN <sup>1)</sup> | X | ‑ |
| G220 Clean Power PN <sup>1)</sup> | ‑ | X |
| **Power Modules** |  |  |
| Power Module <sup>1)</sup> | X | ‑ |
| Power Module <sup>1)</sup> | ‑ | X |
| **Motors** |  |  |
| DRIVE-CLiQ motors | X | X |
| Induction motors | X | X |
| Synchronous motors | X | X |
| Reluctance motors | X | X |
| Motor data input: for the following types of third-party motors:  - Induction motors - Rotating synchronous motors - Reluctance motors - Synchronous or reluctance motor with starting cage | X | X |
| **Measuring systems** |  |  |
| DRIVE-CLiQ encoder | X | X |
| SIN/COS encoder | X | X |
| SIN/COS+SSI encoder | X | X |
| SSI encoder | X | X |
| HTL/TTL encoder | X | X |
| HTL/TTL+SSI encoder | X | X |
| EnDat + SIN/COS encoder | X | X |
| **Supplementary system components** |  |  |
| DRIVE-CLiQ option module | X | X |
| SMT option module | X | X |
| IIoT option module | X | X |
| Communication Module PN <sup>1)</sup> | X | X |
| **Additional components** |  |  |
| External braking resistor  - External braking resistor <sup>2)</sup> - Siemens braking resistor <sup>2)</sup> - Third-party braking resistor <sup>2)</sup> | X  ‑  ‑ | ‑  X  X |
| <sup>1)</sup> Integrated in the drive. Not separately selectable in the device configuration and via the hardware selection. Is indirectly determined by the selection of the G220 type in the "Add new device" dialog.    <sup>2)</sup> An externally connected braking resistor can be configured using the detailed settings of the drive (see "Hardware settings"). Adding a braking resistor via the hardware selection is neither necessary nor possible. |  |  |

> **Note**
>
> **No Sensor Modules in the hardware catalog**
>
> Sensor Modules cannot be assigned using the hardware catalog. Sensor Modules are permanently assigned to the various encoders. Sensor Modules can be selected indirectly by selecting an encoder and by specifying the encoder evaluation at a later time (see "[Specifying the encoder evaluation](#specifying-the-encoder-evaluation)").

---

**See also**

[Perform detailed settings of the drive](#perform-detailed-settings-of-the-drive)

### G220 device configuration

This section contains information on the following topics:

- [Device view](#device-view)
- [Network view](#network-view)
- [Topology view](#topology-view)

#### Device view

##### Overview

The device view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assigning device parameters
- Configuring and assigning module parameters
- Editing the names of devices and modules

Configure the drive line-up in the "Device view". You can call the device view by double-clicking the "Device configuration" entry in the project tree.

The device overview provides a tabular overview of all configured components and their data.

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

##### Structure

The following figure shows an overview of the device view.

![G220 device view](images/153828848523_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control Unit (including CU and PM) |
| ② | Bus interface, Ethernet in this case |
| ③ | Supplementary system component: here the DRIVE-CLiQ Option Module |
| ④ | Bus interfaces, in this case PROFINET as integrated Communication Module |
| ⑤ | Motor |
| ⑥ | Encoder and Sensor Module |

G220 device view

##### Toolbar

You can switch between the devices in your project in the device view using the drop-down list in the toolbar. The following functions are also available in addition to the drop-down list for device selection:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145958600587_DV_resource.Stream@PNG-de-DE.png) | Switches to the network view. The device view can switch between the existing devices using the drop-down list. |
| ![Toolbar](images/145957702539_DV_resource.Stream@PNG-de-DE.png) | Show the area of unplugged modules. |
| ![Toolbar](images/145958637707_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/145958593163_DV_resource.Stream@PNG-de-DE.png) | Show module labels. You can edit the labeling directly in the device view: Select the required labeling and then click on the selected text field or press [F2]. |
| ![Toolbar](images/145958615435_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/145958608011_DV_resource.Stream@PNG-de-DE.png) | You can use the Zoom icon to zoom in (+) or out (-) incrementally or to drag a frame around an area to be enlarged. With signal modules, you can recognize the address labels of the I/O channels from a zoom level of 200% or higher. |
| ![Toolbar](images/145958622859_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/164973265931_DV_resource.Stream@PNG-de-DE.png) | Creates all DRIVE-CLiQ connections from new. |
| ![Toolbar](images/164975682955_DV_resource.Stream@PNG-de-DE.png) | Switches between a complete view and a compact view.   In the compact view, the DRIVE-CLiQ connections are hidden and the components are arranged closer to one another. |
| ![Toolbar](images/145958630283_DV_resource.Stream@PNG-de-DE.png) | Saves the current table view. The layout, width and visibility of columns in the table view are saved. |

##### Graphic area

The graphic area of the device view displays hardware components and, if applicable, the associated modules that are assigned to each other via one or more racks. In the case of devices with racks, you have the option of installing additional hardware objects from the hardware catalog into the slots on the racks.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom level using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

##### Table area

The table area of the device view gives you an overview of the modules used and the most important technical and organizational data.

You can use the shortcut menu of the title bar of the table to adjust the tabular display.

---

**See also**

[Creating a device configuration manually offline](#creating-a-device-configuration-manually-offline)

#### Network view

##### Overview

The network view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assigning device parameters
- Networking devices with one another
- Editing the device names

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

##### Structure

The network view is opened via the "Devices & networks" entry in the project tree.

![G220 network view](images/152044290443_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drive that is assigned as the IO device of a higher-level controller via fieldbus (in this case PROFINET IO). |
| ② | Fieldbus (in this case, PROFINET IO) |
| ③ | Higher-level controller, a SIMATIC S7-1500 in this case, that is configured as IO controller. |
| ④ | Data from drive and controller |

G220 network view

The specific parameters of the selected element are displayed in the inspector window.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145959026827_DV_resource.Stream@PNG-de-DE.png) | Mode to network devices. |
| ![Toolbar](images/145959034251_DV_resource.Stream@PNG-de-DE.png) | Mode to create connections. You can use the adjacent drop-down list to set the connection type. |
| ![Toolbar](images/145958637707_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/145958648203_DV_resource.Stream@PNG-de-DE.png) | Show interface addresses. You can edit the addresses for the MPI, PROFIBUS and Ethernet interfaces directly in the network view: Select the required address and then click on the selected address field or press [F2]. |
| ![Toolbar](images/145958615435_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/145958622859_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/145958608011_DV_resource.Stream@PNG-de-DE.png) | You can zoom in (+) or zoom out (-) the view in increments using the Zoom icon or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/145958630283_DV_resource.Stream@PNG-de-DE.png) | Saves the current table view. The layout, width and visibility of columns in the table view are saved. |

##### Graphic area

The graphic area of the network view displays any network-related devices, networks, connections and relations. In this area, you add devices from the hardware catalog, connect them with each other via their interfaces and configure the communication settings.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom level using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

##### Table area

The table area of the network view includes various tables for the devices, connections and communication settings present:

- Network overview
- Connections
- Relations
- I/O communication
- VPN

You can use the shortcut menu of the title bar of the table to adjust the tabular display.

#### Topology view

##### Overview

The topology view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Displaying the Ethernet topology
- Configuring the Ethernet topology
- Determining and minimizing differences between the desired and actual topology
- Editing the device names

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

##### Structure

The following figure provides an overview of the topology view.

![G220 topology view](images/152044294667_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Topology view toolbar |
| ③ | Graphic area of the topology view |
| ④ | Overview navigation |
| ⑤ | Table area of the topology view (topology overview) |

G220 topology view

You can use your mouse to change the split between the graphic and table areas of the topology view. The division can be changed between horizontal and vertical using a button in the toolbar. To change the position of the split, click between the graphic and the table areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145958637707_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/145959269643_DV_resource.Stream@PNG-de-DE.png) | Changes the position of the devices in the topology view so that the new position is as close as possible to the position in the network view. |
| ![Toolbar](images/145958615435_DV_resource.Stream@PNG-de-DE.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/145958608011_DV_resource.Stream@PNG-de-DE.png) | You can zoom in (+) or zoom out (-) the view in increments using the Zoom icon or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/145958622859_DV_resource.Stream@PNG-de-DE.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |

##### Graphic area

The graphic area of the topology view displays Ethernet modules with their associated ports and port interconnections. Here you can add additional hardware objects with Ethernet interfaces.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom level using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

##### Table area

The table area consists of the following two tabs:

- "Topology overview" tab

  Displays the Ethernet or PROFINET modules with their ports and port interconnections in a table. This table corresponds to the network overview table in the network view.
- "Topology comparison" tab

  Shows the differences between the desired and actual topology and details.

### Function view G220

#### Overview

You parameterize the drive using a graphical user interface in the "Function view". The individual function views are based on function diagrams and contain the required parameters.

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

> **Note**
>
> **All parameters**
>
> You can find all parameters of the drive in the "[Parameter view](#parameter-view-g220)". Experts can then comprehensively parameterize the drive. However, the parameter view can only be called for the parameter assignment. The parameter view is not available for commissioning.

#### Structure

The following figure shows an example of a function view structure:

![Function view G220](images/162585156875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Icon: Saves data protected against power failure (in online mode) |
| ③ | Icon: Restores the factory settings (in online mode) |
| ④ | Button: Toggles between the standard view and the extended view of the project tree |
| ⑤ | Fields: Used for manual input of values. |
| ⑥ | Selection of active data sets (DDS and/or CDS) |
| ⑦ | Button: Activates the online edit mode (for Safety Integrated, also offline) |
| ⑧ | Buttons: Start/end editing generally in online mode or for Safety Integrated. |
| ⑨ | Buttons: Jump to the next or previous step. |

Function view G220

> **Note**
>
> **Special case: Extended parameterization**
>
> The parameter assignment functions can be set in the standard scope or expanded scope. On the 1st call, only the functions of the standard parameter assignment are displayed in the secondary navigation.
>
> - Click ![Structure](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) to display the functions for extended parameterization.
> - Click ![Structure](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) to reduce the display to the functions of standard parameterization again.

### Parameter view G220

#### Overview

The "Parameter view" provides a clearly organized display of the parameters available for the device. For the "Parameterization", you can switch the working area between the "[Function view](#function-view-g220)" and the "Parameter view".

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

> **Note**
>
> No "Parameter view" is available for "Rotate and optimize" and "Guided quick startup".

SINAMICS uses three types of parameters:

- Adjustable parameters

  These are shown with the prefix "p". You can change the value of these parameters within a defined range.
- Display parameters

  These are shown with the prefix "r". You cannot change the value of these parameters.
- Interconnection parameters

  For interconnections between a signal source and a signal sink, possible signal sinks are marked with the prefix "c".

#### Parameter display

The fields of the individual parameters are displayed in the list in color as follows:

| Editing level | Offline color | Online color |
| --- | --- | --- |
| Read only | Gray | Pale orange |
| Read/write | White | Orange |

#### Structure

The following figure shows the structure of the parameter view:

![Parameter view G220](images/153498861195_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation: Restricts the parameter view to the required parameter group. |
| ② | Parameter number |
| ③ | Parameter name |
| ④ | Value of the parameter |
| ⑤ | Unit |
| ⑥ | Data set: Displays the data set to which the parameter belongs. |
| ⑦ | Minimum value |
| ⑧ | Maximum value |

Parameter view G220

#### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145959411211_DV_resource.Stream@PNG-de-DE.png) | Expands or reduces all secondary navigation nodes. |
| ![Toolbar](images/145959338763_DV_resource.Stream@PNG-de-DE.png) | Expands or reduces all nodes below the selected node. |
| ![Toolbar](images/145959440907_DV_resource.Stream@PNG-de-DE.png) | Saves the parameters protected against power failure (copy RAM to ROM). |
| ![Toolbar](images/145959449355_DV_resource.Stream@PNG-de-DE.png) | Restores the factory settings. |
| ![Toolbar](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) | Displays the functions of the extended parameterization in the secondary navigation. |
| ![Toolbar](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) | In the secondary navigation, reduces the functions back to the standard parameterization. |
| ![Toolbar](images/145959330315_DV_resource.Stream@PNG-de-DE.png) | Compares the parameters of the drive object with another parameter set.   - In offline mode, the parameters are compared to the factory settings by default. - In online mode, the parameters are compared to the offline settings by default. - The comparison can also be deactivated again. |
| ![Toolbar](images/145959432459_DV_resource.Stream@PNG-de-DE.png) | Starts a CSV export:   - Save displayed parameters in a CSV file. - Save all parameters of the drive object in a CSV file. |

### Inspector window G220

#### Overview

The properties and parameters of a selected object are displayed in the inspector window. The properties and parameters can be edited. For example, unspecified G220 drive objects newly inserted in the device view can in this way be specified.

> **Note**
>
> Offline settings are generally made in the inspector window. These basic settings are usually a prerequisite for subsequent commissioning settings.

#### Structure

The information parameters in the inspector window are split up into various information types, which are displayed as main and secondary tabs in the inspector window:

![Example: Inspector window G220](images/151946697355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary tab: In this example, the main "Properties" tab |
| ② | Main tab: Properties, information, diagnostics |

Example: Inspector window G220

#### Subdivision of the "Properties" area

There are further subareas for each type of information that can be displayed via secondary tabs.

The most important type of information for SINAMICS G220 drives is the "Properties" area. The following secondary tabs are displayed in this area:

- General

  Display of the properties and settings of the drive device, drive object, or the hardware component. You can edit the settings and parameters here. The left pane of the inspector window contains the secondary navigation. Information and parameters are arranged there in groups. If you click the arrow symbol to the left of the group name, you can expand the group if subgroups are available. If you select a group or subgroup, the corresponding information and parameters are displayed in the right pane of the inspector window and can also be edited there.

  For G220 drives, the drive objects used are mainly specified in this subarea.

  Mandatory entries are marked in the secondary navigation with the icon ![Subdivision of the "Properties" area](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG).
- IO tags

  Displays the IO tags of the PLC. You can assign names for the tags, assign the tags to the user-defined tag tables via a drop-down list, and enter comments for the tags. The IO tags are also shown in the PLC tag table.
- System constants

  Displays the constants required by the system with the HW identifiers of the modules. The system constants are also shown in the PLC tag table.
- Texts

  Displays the reference language and specifies the text source for the project texts.

#### Subdivision of the "Info" area

The following secondary tabs are displayed in this area:

- General
- Cross references
- Compilation

#### Subdivision of the "Diagnostics" area

The following secondary tabs are displayed in this area:

- Device information
- Connection information
- Alarm display

#### Showing or enlarging the inspector window

There are several options available for showing (hiding) the inspector window:

1. Use the regular window icons (top right-hand side in the header of the window).

   - Or -
2. Select a non-specified component in the device view and open the "Properties" shortcut menu.

The inspector window is displayed only partially in Startdrive when called, due to lack of space. Display of the inspector window can be maximized (minimized) for specification of the components:

1. To do so, double-click the header of the inspector window (gray bar).

### Rotating and optimizing G220

#### Overview

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

#### Structure: Control panel

The control panel is used for the control and monitoring of individual drives. You traverse drives with the control panel by specifying values. Depending on the operating mode, these are, for example, speed setpoints.

The following figure shows the various components of the control panel:

![Example G220: Control panel](images/168259391755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Control drive |
| ③ | Drive status (can be hidden online using an arrow) |
| ④ | Set/reset drive enable |
| ⑤ | Actual values (can be hidden online using an arrow) |

Example G220: Control panel

#### Structure: Stationary measurement/Rotating measurement

The stationary or rotating measurement is used for the motor data identification of the drive.

The following figure shows the various components of the "Stationary/rotating measurement" function view:

![Example G220: Rotating and optimizing](images/168259254539_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Specify measurement type |
| ③ | Activate/deactivate measurement |
| ④ | Determined status of the last measurement (can be hidden online using an arrow) |
| ⑤ | Switch on/off optimization |

Example G220: Rotating and optimizing

### Guided quick startup G220

#### Overview

The "guided quick startup" is a startup wizard with the help of which you can centrally set the most important basic settings of the G220 drive.

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

#### Structure

![Example: Guided quick startup in offline mode](images/162584913035_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icon: Saves data protected against power failure (in online mode) |
| ② | Icon: Restores the factory settings (in online mode) |
| ③ | Selection of active data sets (DDS and/or CDS) |
| ④ | Buttons: Start/stops editing in the quick startup in online mode. |
| ⑤ | Detailed setting of active quick startup area. |
| ⑥ | Inactive quick startup area: One of several possible areas |
| ⑦ | Buttons: Jump to the next or previous step. |
| ⑧ | Active quick startup area: Button is brightened |
| ⑨ | Quick startup buttons:   - Back/Next: are always displayed. - Cancel/finish: only displayed in online mode. |

Example: Guided quick startup in offline mode

#### Status display after changes

Changes to individual settings can also affect other settings in the guided quick startup. Status symbols indicate the change status of the particular step:

| Icon | Meaning |
| --- | --- |
| ![Status display after changes](images/155564453003_DV_resource.Stream@PNG-de-DE.png) | The system defaults in this step are valid. |
| ![Status display after changes](images/151783943947_DV_resource.Stream@PNG-de-DE.png) | The settings made in this step are valid.   The settings were made directly in this step, or are the consequences of settings in another step. |
| ![Status display after changes](images/152995660555_DV_resource.Stream@PNG-de-DE.png) | The program changed the settings in this step. Possible causes are:   - Subsequent changes were made in other steps, which are not automatically valid. - Subsequent changes have been made in the device configuration that affect the original settings.   Check the settings of this step. |

---

**See also**

[Guided quick startup](Commissioning%20SINAMICS%20G220%20drives.md#guided-quick-startup)

### Icons for arithmetic and controller functions

Symbols for arithmetic and controller functions, not used in a standard Windows operation, are used in the Startdrive function views. They will therefore be explained briefly at this point.

| Icon | Explanation | Icon | Explanation |
| --- | --- | --- | --- |
| ![Figure](images/149085360523_DV_resource.Stream@PNG-de-DE.png) | **NOT element**   Logical inversion (negation) | ![Figure](images/149086551179_DV_resource.Stream@PNG-de-DE.png) | **Threshold switch 1/0**   Outputs a logical "1" at output y if x < S. |
| ![Figure](images/149086231051_DV_resource.Stream@PNG-de-DE.png) | **AND element**   With logical subdivision of an input | ![Figure](images/149086461579_DV_resource.Stream@PNG-de-DE.png) | **Threshold switch 0/1**   Outputs a logical "1" at output y if x > S. |
| ![Figure](images/149086188299_DV_resource.Stream@PNG-de-DE.png) | **R/S flip-flop**   S/R = Set input/Reset input   Q = Non-inverted output   Q = Inverted output  In the case of a simultaneous 1 signal at the R input and S input, the S input is dominant. | ![Figure](images/149086615179_DV_resource.Stream@PNG-de-DE.png) | **Threshold switch 1/0 with hysteresis**   Outputs a logical "1" at output y if x < S. If x >= S + H, y returns to 0. |
| ![Figure](images/149086325003_DV_resource.Stream@PNG-de-DE.png) | **Exclusive OR/XOR**   y = 1 if x1 = x2. | ![Figure](images/149086474379_DV_resource.Stream@PNG-de-DE.png) | **Threshold switch 0/1 with hysteresis**   Outputs a logical "1" at output y if x > S. If x <= S - H, y returns to 0. |
| ![Figure](images/149086640779_DV_resource.Stream@PNG-de-DE.png) | **Comparator**   y = 1 if x1 = x2. | ![Figure](images/149086333579_DV_resource.Stream@PNG-de-DE.png) | **Limiter**   x is limited to the upper limit value LU and the lower limit value LL and is output at output y.   The binary signals MLU and MLL have the value "1" if upper or lower limiting is active. |
| ![Figure](images/149086316427_DV_resource.Stream@PNG-de-DE.png) | **Sign reversal**   y = -x | ![Figure](images/149086435979_DV_resource.Stream@PNG-de-DE.png) | **Sample & hold element**   Sample and hold element. y = x if SET = 1  (no retentive memory during POWER OFF) |
| ![Figure](images/149081763339_DV_resource.Stream@PNG-de-DE.png) | **Absolute-value generator**   y = |x| | ![Figure](images/149086627979_DV_resource.Stream@PNG-de-DE.png) | **Monitoring**   Positioning in sheet at bottom right. |
| ![Figure](images/149085240971_DV_resource.Stream@PNG-de-DE.png) | **Divider**   Y = X<sub>1</sub>/X<sub>2</sub> | ![Figure](images/149086222475_DV_resource.Stream@PNG-de-DE.png) | **Simple change-over switch**   The switch position as per the factory setting of --- is displayed (in this case, switch position 1). |
| ![Figure](images/149085351947_DV_resource.Stream@PNG-de-DE.png) | **Multiplier**   y = x1 · x2 |  |  |
| ![Figure](images/149086666379_DV_resource.Stream@PNG-de-DE.png) | **Comparator greater than 0**   y = 1 if analog signal x > 0, i.e. if it is positive. |  |  |
| ![Figure](images/149086384779_DV_resource.Stream@PNG-de-DE.png) | **Differentiator**   Y = dx/dt |  |  |

## Fundamentals

This section contains information on the following topics:

- [Permanently save the settings](#permanently-save-the-settings)
- [Restoring factory settings](#restoring-factory-settings)
- [Loading the configuration from the device to the project](#loading-the-configuration-from-the-device-to-the-project)
- [Loading the configuration from the project to the device](#loading-the-configuration-from-the-project-to-the-device)
- [Perform firmware update](#perform-firmware-update)
- [Managing supplementary functions that require a license](#managing-supplementary-functions-that-require-a-license)
- [Using a signal filter](#using-a-signal-filter)
- [Editing signal interconnections](#editing-signal-interconnections)
- [Using drive libraries](#using-drive-libraries)
- [Managing the parameter list](#managing-the-parameter-list)
- [Rules for the use of data sets](#rules-for-the-use-of-data-sets)

### Permanently save the settings

#### Overview

Parameterizations of your drive are generally volatile and are lost when the drive is switched off.

To permanently save settings, you have the following options:

- Saving settings in the project.
- Saving settings (offline/online) on the memory card of the converter.

#### Requirement

- With protection activated (UMAC):

  The function rights of your user account required for permanently saving (see [Access control](User%20administration%20and%20security.md#access-control))

  Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".

#### Saving settings only in the project

In Startdrive, settings are predominantly made via function views.

> **Note**
>
> **Immediate validity of inputs**
>
> Inputs in input fields as well as the selection of options in drop-down lists, option fields and check boxes are applied in Startdrive immediately after their input and without any further prompts.

The complete project must be saved in order that the settings made are permanently active.

1. Click "Save project" in the toolbar.

   - Or -
2. Select the "Project > Save" or "Project > Save as" menu.

#### Saving online data in non-volatile storage

If you are connected to the drive online, save your configuration as follows:

1. In the function view for the active Startdrive project, click on the ![Saving online data in non-volatile storage](images/145959908619_DV_resource.Stream@PNG-de-DE.png) icon (Retentively save data of the complete device).

   - Or -
2. In the project tree of your drive device, double-click on "Online & diagnostics".
3. In the secondary navigation, select the menu "Functions > Backup/Restore".
4. In the "Retentively save RAM data" area, click on "Save":

The program checks whether a memory card is available. If a matching memory card is detected, the parameter values are saved retentively to this card.

#### Saving offline data in non-volatile storage

For storing in a power-independent manner, it is important that the settings made are not only saved in the project on the PC, but are also stored permanently on the memory card of the drive (also known as "Save retentively" or "Copy RAM to ROM"). An online connection must be established to the drive for this purpose.

1. Establish an [online connection](#establishing-an-online-connection-to-the-target-device) to your drive.
2. Load the project data into your drives.
3. Click the ![Saving offline data in non-volatile storage](images/145959908619_DV_resource.Stream@PNG-de-DE.png) icon in the function view of the active Startdrive project.

   The current project settings are stored non-volatile on the memory card of the drive.

### Restoring factory settings

This section contains information on the following topics:

- [Restoring factory settings (standard scope)](#restoring-factory-settings-standard-scope)
- [Complete reset of device settings](#complete-reset-of-device-settings)

#### Restoring factory settings (standard scope)

##### Overview

In the following cases it may be necessary to reset the drive to the factory settings.

- Incomplete commissioning
- When changing the motor
- If there is any ambiguity regarding the previous parameter assignment or previous use of the drive

Restoring the factory settings using a Startdrive function only deletes the user-specific converter parameterization, i.e. the motor data for example.

> **Note**
>
> **Security settings are kept**
>
> Digital certificates and all Startdrive security settings are not affected when restoring the factory setting.

##### Requirement

- With protection activated (UMAC):

  The function rights of your user account required to reset factory settings (see [Access control](User%20administration%20and%20security.md#access-control))

  Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".

##### Procedure

In the online mode, you can restore the factory settings for the drive.

1. Establish an [online connection](#establishing-an-online-connection-to-the-target-device) to your drive.
2. Click on the ![Procedure](images/145959917067_DV_resource.Stream@PNG-de-DE.png) icon in the function view of the active Startdrive project.

   - Or -
3. In the drive project tree, call function view "Online & diagnostics".

   - In the secondary navigation, select the menu "Functions > Backup/Restore".
   - Click "Start" in the "Restoring factory settings" area.

##### Result

The factory settings are restored.

When performing the reset, the following settings are kept:

- Activation and settings of the User Management (User Management & Access Control)
- The communication settings "IP configuration" or "Device name" of service interface (X127) and the PROFINET interface (X150)
- Firmware installed on the converter

> **Note**
>
> If you wish to completely reset the drive, carry out a "[Complete reset of all device settings (via SD Card)](#complete-reset-of-device-settings)".
>
> The complete reset also deletes digital certificates.

#### Complete reset of device settings

##### Overview

In rare cases, device settings should be completely reset. Examples:

- You have forgotten your access password.
- You wish to deactivate User Management and all security settings (also certificates).
- You wish to delete all data as you want to sell the device or dispose of it.

You can only perform a full reset with a specially configured SD Card.

##### Requirements

- You can manually access the converter.
- The converter must be disconnected from the motor:

  - Disconnect all of the electrical connections to the motor (encoder, power and brake cables).
  - Disconnect PROFINET from the control system and other devices.
- You have an empty SD Card that can be written to (max. 32 GB, e.g., 6SL5970-0AA00-0AA0).

##### Procedure

1. Create an empty file named "RESET.TXT" in the source directory of the SD card.
2. Switch off the supply voltage of the converter.
3. Wait until all LEDs of the converter are off.
4. Insert the SD card with the "RESET.TXT" file into the card slot of the converter.
5. Switch on the supply voltage of the converter.

   The settings are reset to the factory settings. During this process, the RDY LED flashes quickly.

   ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png)
6. Wait until the factory settings have been restored.

   The RDY LED flashes quickly 3 times in succession and then pauses in an alternating sequence.

   ![Procedure](images/164842006539_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164842006539_DV_resource.Stream@PNG-de-DE.png)
7. Switch off the converter.
8. Remove the SD card with the "RESET.TXT" file.

   If the SD card remains inserted, each time the converter runs up it will manually restore the factory settings.

##### Result

When the SD Card is reset, the parameterization is deleted and the converter is reset to the factory setting or respectively the state when originally delivered. If you activated UMAC for the drive, then also this protection is deleted along with all of the associated security settings. However, the firmware that has been installed is completely kept and does not have to be reinstalled.

After manually restoring the factory settings, the web server can be accessed via the service interface (X127) and via the PROFINET interface (X150). Use the secure HTTPS transfer protocol when accessing via the service interface (X127).

Following the reset, complete recommissioning is necessary.

### Loading the configuration from the device to the project

#### Overview

If you changed the configuration in the drive online, then the data in the project no longer have the same state. As a consequence, to update the project data, load the drive data from the drive into the Startdrive project.

#### Requirements

- A project is open.
- The hardware configuration and software to be loaded must be compatible with the Startdrive. If the data on the device was created with a previous program version or with a different configuration software, please make sure they are compatible.

#### Procedure

Proceed as follows to load the project data from a drive into your Startdrive project:

1. Call the "Upload from device (software)" shortcut menu or click the ![Procedure](images/145960130315_DV_resource.Stream@PNG-de-DE.png) icon (upload from device) in the toolbar.

   If there is a user authentication for the opened Startdrive project, the "Upload preview" dialog is called automatically.

   If there is no user authentication yet, the "Log on to device" dialog appears.

   - Correct the default user name here if necessary.
   - Enter the password and confirm with "OK".

   The "Upload preview" dialog is then automatically called. Startdrive checks whether all requirements for loading have been met. In the event that not all of the requirements have been met, then these are displayed as messages in the dialog.

   ![Example: Upload from device](images/145960245387_DV_resource.Stream@PNG-en-US.png)

   ![Example: Upload from device](images/145960245387_DV_resource.Stream@PNG-en-US.png)

   Example: Upload from device
2. Check the messages in the "Upload preview" dialog. If necessary, activate the actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
3. Click the "Upload from device" button.

   The loading operation is performed.

#### Result

The project data have been loaded from the drive into your Startdrive project of your operating unit.

### Loading the configuration from the project to the device

#### Overview

To set up your project, you need to download the project data, which you generated offline, to the connected drives. This project data is generated, e.g. when hardware, networks, and connections are configured when the user program is programmed.

User authentication is mandatory for loading project data into a protected device. The program checks whether a successful login has already taken place when opening the Startdrive project (offline).

> **Note**
>
> **Downloading project data to PLCs**
>
> If you have connected the drive to a SIMATIC controller (for example, via a technology object), it is not sufficient to download the drive data to the connected drive. The offline parameterization of the PLCs also must be downloaded to the corresponding controller. The procedure is the same as for downloading to the drive.
>
> Prior to the download, the appropriate controller must be selected in the project tree. PLC project data are usually translated during the download to the controller.

> **Note**
>
> **Loading only UMAC settings into the device**
>
> If you only want to load the UMAC settings of your user administration into the drive, use the "[Load UMAC settings into the device" function](User%20administration%20and%20security.md#download-umac-to-device-from-sinamics-firmware-v61).

#### Trusted device

For secure communication between the operating unit and the drive, the drive must be classified as "trusted". Without this classification, online access is not possible. A device is considered trusted and therefore secure if it is assigned a digital certificate accepted by Startdrive.

See the page "[Secure communication with Trusted Devices](User%20administration%20and%20security.md#secure-communication-with-trusted-devices-from-sinamics-firmware-v61)" on how to assign a digital certificate to the drive.

#### Requirements

- The project data is consistent.
- Each drive to be loaded can be accessed online.

  If the project data are also to be downloaded to the control, the control must be accessible online.
- The drive must be classified as a "trusted" device by a digital certificate.
- With protection activated (UMAC):

  - The function rights of your user account required for the download (see [Access control](User%20administration%20and%20security.md#access-control))

    Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".
  - The protection (UMAC) is activated in the project settings for the current Startdrive project as well as for the drive.

#### Procedure

Proceed as follows to download the project data to the drive in the online mode:

1. In the project tree, select one or several drives.
2. Open the "Download to device" shortcut menu or click the ![Procedure](images/145960282379_DV_resource.Stream@PNG-de-DE.png) icon (download to device) in the toolbar.

   - If you have already established an online connection, the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
   - If you have not already established an online connection, the "Extended loading" dialog opens. First select the interfaces with which you want to establish the online connection to the device. You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command.

     However, the "Extended loading" dialog is only opened automatically if user authentication has already taken place for the active Startdrive project. If this login is missing, then the "Log in to device" dialog appears. Log in by entering the user name and a password. You can then check the download settings.

     Detailed information about going online can be found at "[Establishing an online connection to the target device](#establishing-an-online-connection-to-the-target-device)".
3. Check the messages in the "Load preview" dialog. Activate the required actions in the "Action" column to perform a secure download.

   ![Example: Load preview](images/145960316427_DV_resource.Stream@PNG-en-US.png)

   ![Example: Load preview](images/145960316427_DV_resource.Stream@PNG-en-US.png)

   Example: Load preview

   As soon as downloading becomes possible, the "Load" button is enabled.
4. Click "Load".

   Loading starts. If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. The "Load results" dialog then opens. In this dialog, you check whether the load task was successful, and you can select additional actions.
5. Click "Finish".

**Note**

**Downloading protection settings to the device**

The current security settings of the user management (UMAC) can also be automatically downloaded to the device together with the project data.

Ensure that option "Refresh UMAC" is activated in dialog "Load preview". The activated option is the requirement that the UMAC data are also transferred to the drive.

For details, see "[Transferring protection settings ...](User%20administration%20and%20security.md#activating-project-protection)".

#### Result

The selected project data have been downloaded to the drives.

> **Note**
>
> **Loading process with protection activated**
>
> If protection settings were made for the selected drive in the project, these protection settings must be complete. Otherwise, loading into the device is canceled. The UMAC settings in the Security Wizard must be completed via the "Finish" command.

> **Note**
>
> **Upload from device**
>
> Conversely, the project data of a selected drive can also be uploaded into your Startdrive project of your operating unit. Proceed as described in "[Loading the configuration from the device to the project](#loading-the-configuration-from-the-device-to-the-project)".

### Perform firmware update

This section contains information on the following topics:

- [Overview](#overview)
- [Performing a firmware update via memory card](#performing-a-firmware-update-via-memory-card)
- [Updating the firmware via an online connection](#updating-the-firmware-via-an-online-connection)

#### Overview

##### Fundamentals

A firmware update is required if you want to use a new firmware version with an extended range of functions. Generally, the following firmware update variants are available for G220:

- [Firmware update via memory card](#performing-a-firmware-update-via-memory-card)

  The firmware update is performed directly on the actuator using a memory card with new firmware.
- [Firmware update via online connection](#updating-the-firmware-via-an-online-connection)

  This firmware update is performed via the "Online & diagnostics" function view in Startdrive. The desired drive is accessed online.

> **Note**
>
> **Is the firmware version the same in the drive unit and Startdrive?**
>
> ONLINE connections between a Startdrive project and a drive unit are only possible when both communication partners have the same firmware version (see "[Checking the firmware version](#checking-the-firmware-consistency)").
>
> - If your current Startdrive project is working with an older firmware version than the drive unit, create a new project.
> - Set the firmware version of the Startdrive project to the latest updated version of the drive unit and accept all other settings from the old project.   
>   If you are still using an old Startdrive version, it may be necessary to install a new Startdrive version that supports the firmware version.

#### Performing a firmware update via memory card

##### Overview

A firmware update is required if you want to use a new firmware version with an extended range of functions.

You can find the available SINAMICS firmware versions on this [Internet website](https://support.industry.siemens.com/cs/ww/en/ps/13204):

Updating the firmware using a memory card is explained in detail in the following.

##### Requirements

- A backup is made before updating the firmware.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

| 1. Switch off the drive. 2. Remove the SD card with the old firmware version. 3. Insert the SD card with the new firmware into the drive. 4. Switch on your drive again.     The new firmware is being installed. The process takes about 2 minutes.       | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Procedure](images/164842006539_DV_resource.Stream@PNG-de-DE.png) | - | Firmware update complete | 5. Switch off the drive. 6. Remove the SD card. 7. Switch on your drive again.     The firmware of the connected DRIVE-CLiQ components is updated. A restart may be required to complete the update (see Startdrive alarm messages).       | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Procedure](images/146009085707_DV_resource.Stream@PNG-de-DE.png) | Firmware update of the connected DRIVE-CLiQ components in progress. - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Procedure](images/146009098379_DV_resource.Stream@PNG-de-DE.png) | Firmware update of the DRIVE-CLiQ components is complete. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The firmware has been updated.

Check in the Startdrive catalog information whether the required new firmware version is installed.

Call in secondary navigation in the "General > Catalog information" inspector window.

---

**See also**

[Going online - default settings](#going-online---default-settings)
  
[Overview](#overview-7)

#### Updating the firmware via an online connection

##### Overview

As an alternative to an update using a memory card, you can also update the firmware via the "Online & diagnostics" function view.

##### Requirements

- A backup is made before updating the firmware.
- The current firmware is saved in the file directory of your operating unit.
- There is a physical connection between the Ethernet interface of your operating unit and the Ethernet or PROFINET interface of your drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Procedure

| 1. Call the [Diagnostics view](#overview-7). 2. In the secondary navigation of the function view select the "Functions > Firmware update" menu.     The "Firmware update" function view opens in the diagnostics view. The drive article number and the currently used firmware version are displayed in area "Online data". 3. Click the "Browse" button in the "Firmware loader" area.     A selection dialog opens. 4. Select the firmware file with the required version in the file system of your operating unit.     The firmware file is now displayed in the line with the same name in the "Firmware loader" area.     In fields "Firmware version" and "Status", check again that you have selected the required firmware version, and whether the firmware can be read. 5. Optional: Activate the option "Automatically restart the drive...".     In this case, after updating the firmware, you do not have to restart the drive manually. In this case, step 8 is omitted. 6. To start the update, click on "Start firmware update"     Confirmation dialog "Firmware update" is displayed. 7. Click on "OK" to load the firmware into the drive.    The status of the firmware update is displayed in the "Status" field. The new firmware is being installed. The process takes about 2 minutes.       | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Procedure](images/164842006539_DV_resource.Stream@PNG-de-DE.png) | - | Firmware update complete | 8. Optional: If the option "Automatically restart the drive..." is not activated, then manually switch the drive off and on again.    The firmware of the connected DRIVE-CLiQ components is updated.        | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Procedure](images/146009085707_DV_resource.Stream@PNG-de-DE.png) | Firmware update of the connected DRIVE-CLiQ components in progress. - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Procedure](images/146009098379_DV_resource.Stream@PNG-de-DE.png) | Firmware update of the DRIVE-CLiQ components is complete. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The firmware has been updated.

Check in the Startdrive catalog information whether the required new firmware version is installed.

Call in secondary navigation in the "General > Catalog information" inspector window.

### Managing supplementary functions that require a license

This section contains information on the following topics:

- [Overview](#overview-1)
- [Overview of licenses](#overview-of-licenses)
- [Activate Trial License mode](#activate-trial-license-mode)
- [Creating a license key](#creating-a-license-key)
- [Extending/updating/restoring the license for the drive](#extendingupdatingrestoring-the-license-for-the-drive)
- [Important messages](#important-messages)

#### Overview

##### Overview

The drive system can generally be used without an additional license. Auxiliary functions or options, however, do require the availability of a purchased license. This license is electronically linked with the function/option of your hardware via a License Key.

The License Key is an electronic license stamp that indicates that one or more software licenses are owned.

Actual customer verification of the license for the software that is subject to license is called a "Certificate of License" (abbreviated to "CoL").

> **Note**
>
> Please refer to the ordering documentation (e.g. catalogs) for information on basic functions and functions subject to license.

**Properties of the license key**

- It is assigned to a specific memory card.
- It is stored retentively on the memory card.
- It cannot be transferred.
- During the ordering process, it can already be permanently assigned to an ordered memory card.
- It can also be subsequently generated with the "WEB License Manager" from a license database based on the previously ordered and received Certificates of License.
- It is stored in a text file, and can be saved in the zip format together with the associated signature file in a license file. The licensing of your drive can only be extended using this zip file.

##### Requirements

- A memory card is available for the drive and has been inserted.

  The licensed supplementary functions always require an existing memory card.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### System response if the license is not adequate

An insufficient license for an option or function is flagged with the following fault and LED on the Control Unit. The licensing is always checked when the converter is initially run up.

- F13000 Insufficient license
- LED READY flashes red at 2 Hz

> **Note**
>
> Operating the drive with an insufficient license for an option is only permitted during commissioning and when performing service work. For this purpose, the Trial License Mode must be activated explicitly.
>
> The drive requires a sufficient license in order for it to operate. Not all options support the Trial License Mode!

##### System response to insufficient licensing in normal operation

In normal converter operation, the following alarm indicates that the converter has insufficient licensing.

- A13002 licensing not sufficient in operation

**Possible cause:**

- Defective memory card or memory card has been removed
- License data does not match the memory card used

**Possible consequence:**

If the user does not respond to the alarm (e.g. reinsert the memory card), then fault F13000 is automatically output at the next restart. The licensed function can then no longer be used.

##### Additional parameters

- p9918
- p9919
- p9920
- p9921

---

#### Overview of licenses

##### Overview of licenses

You can obtain an overview of the licenses available for the drive and the status of these licenses on the license overview page.

| Element | Description |
| --- | --- |
| General license status | Displays the current license status, e.g. "underlicensed". |
| System response | Displays the system response to the current license status, e.g. "Blocks the drive from being switched on again." |
| Trial period | Displays the Trial License status; e.g. "Trial License mode not active". |
| Serial number of the memory card | Serial number of the memory card and button to copy the serial number. |
| Activate Trial License mode | Button to activate the Trial License mode. |
| Activate license key file | Button to load a license file. |
| Save eCoL archive | Button for saving the license certificates to the file system of the operating unit. |
| **Table columns** |  |
| Status | The following symbols display the status:     ![Overview of licenses](images/146631416203_DV_resource.Stream@PNG-de-DE.png): License is complete    ![Overview of licenses](images/146630234251_DV_resource.Stream@PNG-de-DE.png): Trial license mode is active    ![Overview of licenses](images/146631475979_DV_resource.Stream@PNG-de-DE.png): License is not available or the memory card with license is not inserted (underlicensed) |
| Function that requires a license | List of all used system options/functions subject to license. |
| Existing/required licenses | The required number of licenses compared with the number of licenses included with the License Key.  For operation, the number of available licenses ≥ the number of licenses required. |
| License status | Displays the current status of the function requiring a license. |
| Remaining operating time | Displays the remaining operating time of a trial period. |

This overview allows the following:

- Obtain a status overview of the individual licenses of your drive system
- Display and enter License Key

  See "[Extending/updating/restoring the license for the drive](#extendingupdatingrestoring-the-license-for-the-drive)"
- Display and copy the serial numbers of the memory cards being used
- Activate Trial License mode

  See "[Activate Trial License mode](#activate-trial-license-mode)"

##### Trial Licenses

Valid licenses can either be ordered together with a memory card, or when subsequently ordered, can be assigned to your memory card via the "Web License Manager". Most of the SINAMICS functions requiring a license can be operated for a limited period of time in a Trial License mode.

![Schematic: Trial License mode](images/146011105931_DV_resource.Stream@PNG-en-US.png)

Schematic: Trial License mode

**Features:**

- The Trial License mode can be used for a maximum of three periods. Whereby the first period is primarily envisaged as the initial trial period during commissioning and accompanying trials. The other two periods are intended for tests, presentations or service.
- The Trial License mode must be activated separately for each of the periods. Once activated, a trial period can no longer be interrupted or canceled. The active trial period also continues when you activate an additional option in the Trial License mode, deactivate an activated option again, or enter a valid License Key.
- The Trial License mode can be activated only as a block, i.e. for all options together. Option-granular activation is not possible.
- You receive messages in plenty of time before a period has expired. You can then activate the next trial period if it is still free or replace the Trial License with a full license.

  The next time the drive runs up, the Trial License mode will be deactivated. If you miss this opportunity, you can only continue to work with a full license or you must deactivate the option where a license is required - or remove it from your configuration.
- Not all SINAMICS licenses can be used in the Trial License mode.

#### Activate Trial License mode

##### Overview

The Trial License mode can be used for a maximum of three trial periods.

##### Requirements

- A project has been created.
- A drive has been created.
- An online connection has been established between the operating unit and the drive.

##### Procedure

1. Call the license overview page:

   - Double-click on "Online & diagnostics" in the project tree.
   - Click "License" in the secondary navigation.
2. Click on the "Activate Trial License mode" button.
3. To activate the Trial License mode, click the "Activate" button in the query dialog.

   Alarm A13030 indicates that the Trial License has been activated. The status overview then shows the remaining operating time of the licensed options in Trial License mode.

   After the trial period expires, alarm A13031 "Trial License period expired" is output.
4. Repeat steps 2 and 3 if you wish to activate the Trial License mode for another trial period.

   After the third trial period has expired, alarm A13033 "Last Trial License period expired" is output. Additional trial periods can now no longer be activated. After a trial period expires, a lock (inhibit) may become active next time the system starts up. You require a full license if you wish to use the associated subfunctions.
5. Proceed as follows if you wish to further use the associated subfunctions:

   - Purchase a full license for the associated subfunctions.
   - Generate a new License Key (see "[Creating a license key](#creating-a-license-key)").
   - Update the licensing for your drive (see "[Extending/updating/restoring the license for the drive](#extendingupdatingrestoring-the-license-for-the-drive)").

**Note**

You can only activate the next trial period after the previous period has expired.

##### Result

The Trial License mode is activated. You can use the program during the set trial period.

#### Creating a license key

##### Overview

The WEB License Manager informs you about how many and which licenses are assigned to your memory card. If you need additional licenses, you can assign these licenses to your memory card and create a new License Key using the WEB License Manager.

> **Note**
>
> A new license is not required for upgrading the firmware. Therefore, do not delete the License Key from the memory card (..\KEYS\SINAMICS\KEYS.txt) if you want to upgrade.

##### Requirements

The following information is required to work with the "WEB License Manager":

- Serial number of the memory card

  The serial number is on the memory card, or can be copied from the license overview.
- Enter the license number and delivery note number of the license (visible on the Certificate of License)
- Product name

##### Creating a license key

1. Call the following link:

   [WEB License Manager](https://mc-dwh.automation.siemens.com/ords/apex/f?p=20130:1)
2. Select the "Direct access" link.

   The progress indicator is at "Login" in the License Manager.
3. Enter the license number and delivery note number of your license. Then click "Next".

   The progress indicator is then at "Identify product".
4. Enter the serial number of the memory card.
5. Select the product you are using, e.g. "SINAMICS X2xx PN". Then click "Next".

   The progress indicator is at "Select licenses". In the "Already assigned licenses" column, you can see which licenses of the selected delivery note have already been assigned and how often.

   In the "Additional licenses to be assigned" column, you can activate required licenses or also specify how many additional licenses you require.
6. Activate the additionally required licenses. Then click "Next".

   The progress indicator is at "Assign licenses". A summary of the selected licenses is displayed here for checking.
7. To start the assignment, click "Assign".

   The licenses are permanently assigned to the specified hardware. The progress indicator is at "Generate license key". The License Key is displayed.
8. You require the license key as zip file be able to use the license key in Startdrive.

   Therefore, load the zipped license key file into a file directory of your operating unit.

##### Result

The zipped license key file is now in your operating unit. Using this zip file, you can then extend the licensing of your drive.

##### Displaying the license key

If the License Key on the memory card is accidentally deleted, you can display it again using the WEB license manager.

1. Call the following link:

   [WEB License Manager](https://mc-dwh.automation.siemens.com/ords/apex/f?p=20130:1)
2. In the navigation, click the "Display license key" option in the "User menu".

   Several input fields can be found to the right in the "Display license key" area.
3. Enter the serial number of your memory card either in the "Hardware serial number" or in the "License no." field. Enter your license number. Then click on "Display license key".

   The current License Key is then displayed.

#### Extending/updating/restoring the license for the drive

##### Overview

Check the drive license status using the license overview page. All of the additional license-controlled functions are listed in a table. You can identify which license is enabled for you and for which functions you do not have a license.

In the license overview you can enable additional functions based on additional licenses.

##### Requirements

- Data are consistent in the drive and in the Startdrive project.
- An online connection has been established between the operating unit and the drive.
- A SIEMENS memory card is inserted in the converter.
- A [License key file](#creating-a-license-key) was already generated for the required license using the Web License Manager.

##### Procedure

1. Call the license overview page:

   - Double-click on "Online & diagnostics" in the project tree.
   - Click "License" in the secondary navigation.
2. In the license overview page, click on "Activate License Key file".

   A load dialog with the same name opens.
3. Select the license key file in the file system of your operating unit. Close the load dialog.

   Startdrive unzips the license key file and checks the license.

   After a check has been successfully completed, dialog "Licensing" opens. A list in the dialog shows all licenses that are enabled for you after the licensing procedure has been completed.
4. Click on "Activate" to enable licenses.

##### Result

The dialog closes. The new licenses are active. The statuses of licenses listed in the license overview page are updated.

##### Other options: Saving eCol

The drive license certificates (eCol) are saved to the (optional) memory card of the drive.

When required, you can load these certificates directly from the memory card to the file system of your operating unit.

1. To do this, click on "Save eCol archive".
2. Select a file directory of your operating unit and confirm.

##### Other options: Restoring a license

The license key is always saved on the memory card. The licensed function is locked if the memory card was removed from the drive and warm start of the drive executed. Proceed as follows to reuse the license:

1. Reinsert the memory card into the card slot of the drive.
2. Execute a warm start of the drive.
3. Check the licensing on the license overview page.

#### Important messages

##### Overview of important alarms and faults

| Symbol | Meaning |
| --- | --- |
| - F13000 | Licensing is not sufficient |
| - A13002 | Licensing not sufficient in operation |
| - F13010 | Licensing function not licensed |
| - A13030 | Trial License activated |
| - A13031 | Trial License period expired |
| - A13032 | Trial License last period activated |
| - A13033 | Trial License last period expired |

### Using a signal filter

This section contains information on the following topics:

- [Overview](#overview-2)
- [Using the PT1 filter](#using-the-pt1-filter)
- [Using a PT2 filter](#using-a-pt2-filter)
- [Using a bandstop filter](#using-a-bandstop-filter)
- [Using a low-pass filter with reduction](#using-a-low-pass-filter-with-reduction)
- [Using a general 2nd order filter](#using-a-general-2nd-order-filter)

#### Overview

##### Filters available for processing signals

In Startdrive, various filters are available for SINAMICS drives for filtering signals:

- [PT1 filter](#using-the-pt1-filter); first-order low-pass filter
- [PT2 filter](#using-a-pt2-filter); second-order low-pass filter
- [General 2nd order filter](#using-a-general-2nd-order-filter)
- [Low-pass filter with defined reduction](#using-a-low-pass-filter-with-reduction)
- [Bandstop filter](#using-a-bandstop-filter) with different notch depth or reduction

The filters are used in different sections of the controlled system. Examples:

- Speed setpoint filter
- Current setpoint filter
- Speed actual value filter
- Precontrol balancing

#### Using the PT1 filter

##### Setting a time constant

The PT1 filter is a first-order low-pass filter. Use this filter to suppress disturbing signals, for example, to dampen resonance or noise.

Besides amplitude damping, the filter also produces a phase shift, which reduces the phase margin in the control loop. In this way, the maximum possible bandwidth of the speed controller is reduced.

The transfer function is expressed as follows:

![Setting a time constant](images/145966670731_DV_resource.Stream@PNG-de-DE.png)

where s = jω = j*2πf

The PT1 filter has the following features:

- Damping after the characteristic frequency is -20 dB/decade (factor 1/10) (see amplitude response).
- Phase shift at the characteristic frequency is -45° (see phase response).

![Bode diagram PT1](images/145966414987_DV_resource.Stream@PNG-en-US.png)

Bode diagram PT1

You set the time constant (smoothing time) in Startdrive. The following diagram shows the step response of a PT1 system with time constant T<sub>1</sub>.

![PT1 without dead time](images/145966658059_DV_resource.Stream@PNG-de-DE.png)

PT1 without dead time

The greater time constant T<sub>1</sub> that you select, the lower the characteristic frequency. This means that the amplitude damping and the phase shift engage at the lower frequencies and the delay time increases accordingly.

#### Using a PT2 filter

##### PT2 filter

The PT2 filter is a second-order filter, which is used here as a low-pass filter. The transfer function is expressed as follows:

![PT2 filter](images/145966406539_DV_resource.Stream@PNG-de-DE.png)

where s = jω = j*2πf

The PT2 filter has the following features:

- Phase shift at the characteristic frequency is -90°.
- Damping after the characteristic frequency is -20 dB/decade.

In Startdrive, the following parameters are required for the filter.

- Denominator damping D<sub>N</sub>; damping constant that can be used to influence the amplitude/phase response.
- Denominator natural frequency f<sub>N</sub> or characteristic frequency

Because Startdrive does not yet provide a calculation of the filters and representation of the amplitude and phase responses, the examples can offer a rough guide for the filter parameterization.

##### Amplitude and phase response with the standard settings

Example of a PT2 filter

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Characteristic frequency f<sub>N</sub> 2000 Hz Damping D<sub>N</sub> 0.7 | ![Amplitude and phase response with the standard settings](images/145966208395_DV_resource.Stream@PNG-en-US.png) | ![Amplitude and phase response with the standard settings](images/145966377867_DV_resource.Stream@PNG-de-DE.png) |

#### Using a bandstop filter

##### Bandstop

A bandstop filter is a filter that normally weakens a wide frequency band and does not allow passing in an error case. However, a notch filter always only blocks a single defined frequency.

Some characteristics of different bandstop filters in the following as examples:

##### Amplitude response and phase response for bandstop filter with infinite notch depth

Simplified conversion to parameters for general-order filters:

- Reduction or increase after the blocking frequency (Abs)
- Infinite notch depth at the blocking frequency
- Numerator natural frequency f<sub>Z</sub> = f<sub>Sp</sub>
- Numerator damping D<sub>Z</sub> = 0
- Denominator natural frequency f<sub>N</sub> = f<sub>Sp</sub>
- Denominator damping:

  ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/145965453067_DV_resource.Stream@PNG-en-US.png)

Example of bandstop filter with infinite notch depth

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>Sp</sub> = 500 Hz Bandwidth (-3 dB) f<sub>BB</sub> = 500 Hz Notch depth K = -∞ dB Reduction Abs = 0 dB | ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/145965293963_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/145965405451_DV_resource.Stream@PNG-de-DE.png) |

##### Amplitude response and phase response for bandstop filter with defined notch depth

Simplified conversion to parameters for general-order filters:

- No reduction or increase after the blocking frequency
- Defined notch at the blocking frequency K[dB] (e.g. -20 dB)
- Numerator natural frequency f<sub>Z</sub> = f<sub>Sp</sub>
- Numerator damping:

  ![Amplitude response and phase response for bandstop filter with defined notch depth](images/145965473163_DV_resource.Stream@PNG-de-DE.png)
- Denominator natural frequency f<sub>N</sub> = f<sub>Sp</sub>
- Denominator damping:

  ![Amplitude response and phase response for bandstop filter with defined notch depth](images/145965538955_DV_resource.Stream@PNG-en-US.png)

Example of bandstop filter with defined notch depth

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>Sp</sub> = 500 Hz Bandwidth f<sub>BB</sub> = 500 Hz Notch depth K = -20 dB Reduction Abs = 0 dB | ![Amplitude response and phase response for bandstop filter with defined notch depth](images/145965365259_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with defined notch depth](images/145965421323_DV_resource.Stream@PNG-de-DE.png) |

##### Amplitude response and phase response for bandstop filter with defined reduction

General conversion to parameters for general-order filters:

- Numerator natural frequency:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965518859_DV_resource.Stream@PNG-en-US.png)
- Numerator damping:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965559051_DV_resource.Stream@PNG-de-DE.png)
- Denominator natural frequency:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965579147_DV_resource.Stream@PNG-de-DE.png)
- Denominator damping:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965612043_DV_resource.Stream@PNG-de-DE.png)

Example of bandstop filter with defined reduction

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>SP</sub> = 500 Hz Bandwidth f<sub>BB</sub> = 500 Hz Notch depth K = -∞ dB Reduction ABS = -10 dB | ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965385355_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with defined reduction](images/145965437195_DV_resource.Stream@PNG-de-DE.png) |

#### Using a low-pass filter with reduction

##### General low-pass filter with reduction

Low-pass filters allow frequencies below a limit frequency to pass without weakening and only dampen the higher frequencies. With a low-pass filter with reduction, the amplitude response at high frequencies is reduced by a defined amount.

Conversion to parameters for general-order filters:

- Numerator natural frequency f<sub>Z</sub> = f<sub>Abs</sub> (start of reduction)
- Numerator damping:

  ![General low-pass filter with reduction](images/145966188299_DV_resource.Stream@PNG-de-DE.png)
- Denominator natural frequency f<sub>N</sub>
- Denominator damping D<sub>N</sub>

##### Amplitude response and phase response in the standard settings

Example of low-pass filter with reduction

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Characteristic frequency f<sub>Abs</sub> = 500 Hz Damping D = 0.7 Reduction Abs = -10 dB | ![Amplitude response and phase response in the standard settings](images/145966062731_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response in the standard settings](images/145966159627_DV_resource.Stream@PNG-de-DE.png) |

#### Using a general 2nd order filter

##### General 2nd order filter

The following formula shows the transfer function for a general second-order filter. You can also parameterize band-stop filters (notch filters) with this filter.

![Transfer function general second-order filter](images/145966054283_DV_resource.Stream@PNG-de-DE.png)

Transfer function general second-order filter

Numerator natural frequency f<sub>Z</sub>

Numerator damping D<sub>Z</sub>

Denominator natural frequency f<sub>N</sub>

Denominator damping D<sub>N</sub>

where s = jω = j*2πf

**Conversion of a band-stop filter to a second-degree transfer function:**

Example:

Blocking frequency = 800 Hz

Bandwidth (-3 dB) = 1000 Hz

Where f<sub>Sp</sub> = blocking frequency of the band-stop filter

| Symbol | Meaning |
| --- | --- |
| f<sub>z</sub> = f<sub>Sp</sub> | f<sub>z</sub> = 800 Hz |
| D<sub>z</sub> = 0 | D<sub>z</sub> = 0 |
| f<sub>N</sub> = f<sub>Sp</sub> | f<sub>N</sub> = 800 Hz |
| D<sub>N</sub> = f<sub>sp</sub> / 2 / f<sub>sp</sub> | D<sub>N</sub> = 1000 Hz / 2 / 800 Hz = 0.625 |

|  |  |  |
| --- | --- | --- |
| ![General 2nd order filter](images/145965632139_DV_resource.Stream@PNG-de-DE.png) | ![General 2nd order filter](images/145966037387_DV_resource.Stream@PNG-de-DE.png) | ![General 2nd order filter](images/145966045835_DV_resource.Stream@PNG-de-DE.png) |
| Low pass PT2 | Bandstop | General 2nd order filter |
| Characteristic frequency PT2: 1999.0 Hz | Blocking frequency: 800.0 Hz | Numerator frequency: 800.0 Hz |
| Damping: 0.700 | Bandwidth: 1000.0 | Numerator damping 0.0 |
|  | Notch depth: -∞ | Denominator frequency 800.0 Hz |
|  | Reduction: 0.00 | Denominator damping; 0.625 |

### Editing signal interconnections

This section contains information on the following topics:

- [Overview](#overview-3)
- [Interconnecting signal sources](#interconnecting-signal-sources)
- [Interconnecting signal sinks](#interconnecting-signal-sinks)

#### Overview

##### Description

Each drive contains a large number of connectable input and output variables and internal control variables.

The drive can be adapted to the widest range of requirements using binary or numerical signal interconnections.

Corresponding parameters are marked with interconnection symbols in the parameter list or in the function charts. Only r parameters or c parameters can be interconnected.

In Startdrive, signal interconnections are possible in the function view and in the parameter view.

##### Comparison

| Icon | Name | Parameter type | Properties | Interconnection possibilities |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Signal interconnection  with | Fixed value instead of  signal | Alternative  substitute value |  |  |  |  |
| ![Comparison](images/145966680203_DV_resource.Stream@PNG-de-DE.png) | Binary signal sink | c parameters | Binary signal without unit.  Can assume the value 0 or 1. | Binary signal source | X | X |
| ![Comparison](images/145966842251_DV_resource.Stream@PNG-de-DE.png) | Binary signal source | r parameters | Binary signal sink | ‑ | ‑ |  |
| ![Comparison](images/145966850699_DV_resource.Stream@PNG-de-DE.png) | Numerical signal sink | c parameters | Digital signal, e.g. in the 32-bit format.  To emulate words (16 bits), double words (32 bits) or analog signals. | Numerical signal source | X | X |
| ![Comparison](images/145966871947_DV_resource.Stream@PNG-de-DE.png) | Numerical signal source | r parameters | Numerical signal sink | ‑ | ‑ |  |

##### Further details:

[Interconnecting signal sources](#interconnecting-signal-sources)

[Interconnecting signal sinks](#interconnecting-signal-sinks)

#### Interconnecting signal sources

##### Overview

You use the interconnection dialog to interconnect binary or numerical signal sources.

##### Interconnecting a signal

To make a connection, proceed as follows:

1. Click the interconnection icon of the signal that you want to interconnect (![Interconnecting a signal](images/145966842251_DV_resource.Stream@PNG-de-DE.png) or ![Interconnecting a signal](images/145966871947_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Example dialog](images/164804195851_DV_resource.Stream@PNG-en-US.png)

   ![Example dialog](images/164804195851_DV_resource.Stream@PNG-en-US.png)

   Example dialog

   The last set signal sink is displayed in the "Selected sinks" field. If a connection was not available previously, the text "No sink selected" is displayed.
2. Activate the check boxes for the parameters that you want to interconnect.

   If connectable bits of the parameter are available, they are displayed in a drop-down list.

   ![Example dialog: Parameter bits opened](images/164804381707_DV_resource.Stream@PNG-en-US.png)

   ![Example dialog: Parameter bits opened](images/164804381707_DV_resource.Stream@PNG-en-US.png)

   Example dialog: Parameter bits opened
3. Activate the check boxes for the parameter bits that you want to interconnect.
4. Click "OK" to confirm.

   The connection dialog closes.

##### Result

The binary or numerical signal source is interconnected with the selected parameter (bit).

##### Deleting interconnections

By deactivating the respective check box, you can delete interconnections again. The program will support you in changing existing interconnections. Some predefined default interconnections cannot be changed. Messages indicate if an existing interconnection cannot be deleted.

##### Limit signal sinks

The list of signal sinks can be limited using the "Frequently used connections" option. If this option is activated, only the most frequently used signal sinks are offered for interconnection. You can activate/deactivate this option by clicking.

##### Multiple interconnections at outputs

Several interconnections can be set simultaneously for a parameter, which for reasons of space however, cannot be displayed in the interconnections field. Clicking the symbol ![Multiple interconnections at outputs](images/145967003659_DV_resource.Stream@PNG-de-DE.png) next to the interconnection field opens a list, which shows all of the active parameter interconnections.

#### Interconnecting signal sinks

This section contains information on the following topics:

- [Making a signal interconnection](#making-a-signal-interconnection)
- [Interconnecting fixed values instead of signals](#interconnecting-fixed-values-instead-of-signals)
- [Alternatively to signals, substitute values can also be interconnected](#alternatively-to-signals-substitute-values-can-also-be-interconnected)

##### Making a signal interconnection

###### Overview

You use the interconnection dialog to interconnect binary or numerical signal sinks.

###### Interconnecting a signal

To make a connection, proceed as follows:

1. Click the interconnection icon of the signal that you want to interconnect (![Interconnecting a signal](images/145966680203_DV_resource.Stream@PNG-de-DE.png) or ![Interconnecting a signal](images/145966850699_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Interconnection dialog](images/164810037259_DV_resource.Stream@PNG-en-US.png)

   ![Interconnection dialog](images/164810037259_DV_resource.Stream@PNG-en-US.png)

   Interconnection dialog

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. Select the parameter that you want to connect.

   If connectable bits of the parameter are available, they are displayed in a drop-down list.

   ![Parameter bits opened](images/164810041227_DV_resource.Stream@PNG-en-US.png)

   ![Parameter bits opened](images/164810041227_DV_resource.Stream@PNG-en-US.png)

   Parameter bits opened
3. Select the parameter bit that you want to connect.
4. Click "OK" to confirm.

   The connection dialog closes.

###### Result

The binary or numerical signal source is interconnected with the selected parameter (bit).

###### Changing interconnections

In contrast to signal sources, multiple interconnections are not possible for signal sinks. When setting a (new) interconnection, the existing interconnection is automatically deleted. A corresponding message appears if this is not possible.

###### Limit signal sources

The list of signal sources can be limited using the "Frequently used connections" option. If this option is activated, only the most frequently used signal sources are offered for interconnection. You can activate/deactivate this option by clicking.

###### Other options:

- [Interconnecting fixed values instead of signals](#interconnecting-fixed-values-instead-of-signals)
- [Alternatively to signals, substitute values can also be interconnected](#alternatively-to-signals-substitute-values-can-also-be-interconnected)

##### Interconnecting fixed values instead of signals

###### Overview

For signal sinks, fixed values can be interconnected instead of signals. However, the setting of these fixed values is different for binary and numerical signal sinks.

###### Requirement

- There is no signal interconnection with an alternative substitute value.

###### Interconnecting fixed values for numerical signal sinks

1. Click the interconnection icon of the signal that you want to interconnect (![Interconnecting fixed values for numerical signal sinks](images/145966850699_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Example: Fixed value 0 instead of signal interconnection](images/164805599243_DV_resource.Stream@PNG-en-US.png)

   ![Example: Fixed value 0 instead of signal interconnection](images/164805599243_DV_resource.Stream@PNG-en-US.png)

   Example: Fixed value 0 instead of signal interconnection

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. Select the fixed value type you want to use from the "Select signal source" list:

   - 0 = use 0 as fixed value
   - Fixed value = Use specific fixed value
3. If you selected the "Fixed value" entry, then manually assign the desired fixed value in the "Fixed value" field.

   If, on the other hand, you selected "0" as the fixed value, the value 0 is entered in the "Fixed value" field.
4. Click "OK" to confirm.

   The connection dialog closes.

###### Interconnecting fixed values for binary signal sinks

1. Click the interconnection icon of the signal that you want to interconnect (![Interconnecting fixed values for binary signal sinks](images/145966680203_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Examples: Fixed value 0 instead of signal interconnection](images/164805541387_DV_resource.Stream@PNG-en-US.png)

   ![Examples: Fixed value 0 instead of signal interconnection](images/164805541387_DV_resource.Stream@PNG-en-US.png)

   Examples: Fixed value 0 instead of signal interconnection

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. Select the fixed value type you want to use from the "Select signal source" list:

   - 0 = use 0 as fixed value
   - 1 = use 1 as fixed value

   - Or -

   Select the desired fixed value type in the "Fixed value" drop-down list:

   - [0] No
   - [1] Yes
3. Click "OK" to confirm.

   The connection dialog closes.

###### Result

- Display in an interconnection view:

  Instead of a signal, a fixed value was interconnected and this is displayed in the corresponding parameter field of the function view.
- Display in the parameter list:

  In the parameter list, for the interconnected r-parameter it is generally displayed in a second line whether a fixed value was interconnected or not. By clicking on the arrow in front of the r-parameter, you can show and hide the second line.

##### Alternatively to signals, substitute values can also be interconnected

###### Overview

For both binary and numeric signal sinks, fixed substitute values can be assigned in addition to signals. These are then automatically used when the signal interconnection has become invalid.

###### Requirements

- There is no interconnection of a fixed value.
- Ideally, there is a signal interconnection.

###### Additionally assigning substitute values for numerical signal sinks

1. Click the interconnection icon of the signal that you want to interconnect (![Additionally assigning substitute values for numerical signal sinks](images/145966850699_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Example: Signal interconnection without assigned substitute value](images/164807949323_DV_resource.Stream@PNG-en-US.png)

   ![Example: Signal interconnection without assigned substitute value](images/164807949323_DV_resource.Stream@PNG-en-US.png)

   Example: Signal interconnection without assigned substitute value

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. If there is no signal interconnection yet, select the parameter you want to interconnect.

   As soon as a signal interconnection is present, the "Substitute value" field is displayed below the "Selected source" field.
3. Enter the required substitute value in the "Substitute value" field.
4. Click "OK" to confirm.

   The connection dialog closes.

###### Additionally assigning substitute values for binary signal sinks

1. Click the interconnection icon of the signal that you want to interconnect (![Additionally assigning substitute values for binary signal sinks](images/145966680203_DV_resource.Stream@PNG-de-DE.png)).

   A connection dialog for the selection of the possible parameters opens.

   ![Example: Signal interconnection with substitute switched off](images/164808250379_DV_resource.Stream@PNG-en-US.png)

   ![Example: Signal interconnection with substitute switched off](images/164808250379_DV_resource.Stream@PNG-en-US.png)

   Example: Signal interconnection with substitute switched off

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. If there is no signal interconnection yet, select the parameter you want to interconnect.

   As soon as a signal interconnection is present, the "Substitute value" field is displayed below the "Selected source" field.
3. Select the substitute value type you want to use in the "Substitute value" drop-down list:

   - [0] No
   - [1] Yes
4. Click "OK" to confirm.

   The connection dialog closes.

###### Result

The selected source now has both a signal interconnection and an alternative substitute value. This substitute value is used in the case of an invalid interconnection.

The defined substitute value is even retained if you subsequently change the signal interconnection or in the event that the signal interconnection becomes invalid. A signal and substitute value can therefore be set independently of each other.

- Display in an interconnection view:

  A hint at the signal connection indicates the type of interconnection. In case of a signal interconnection with substitute value, the hint shows the interconnected parameter and additionally the specified substitute value.
- Display in the parameter list:

  In the parameter list, for the interconnected r-parameter it is generally displayed in a second line whether a substitute value has also been assigned or not. By clicking on the arrow in front of the r-parameter, you can show and hide the second line.

### Using drive libraries

This section contains information on the following topics:

- [Fundamentals](#fundamentals-1)
- [Creating copy templates](#creating-copy-templates)
- [Using copy templates](#using-copy-templates)

#### Fundamentals

##### Overview

In the TIA Portal, libraries are used to store objects that you want to use again.

It is possible to reuse the stored objects throughout a project or across projects.

The following library types are available:

- Project libraries

  You can use a project library when you only want to use the objects in the opened project.
- Global libraries

  You can use global libraries when you want to use the objects across projects.

These copy templates are then re-inserted in the respective context of the project.

A detailed description of libraries can be found in "[Using libraries](Using%20libraries.md#using-libraries)".

##### Possible copy templates

The following objects are possible as copy templates in the drive context:

- One or several drives from the project tree
- User-defined parameter lists of individual drives from the project tree
- Devices and networks from the network view or the device configuration

The copy templates contain the entire parameterization. You can therefore create copies of the initial drive using the copy template of a completely parameterized drive.

#### Creating copy templates

##### Overview

You can create one or more copies of a device with copy templates from a library, if required, with networks.

Therefore, first configure the device or devices that you want to use as copy templates.

##### Creating a copy template in a project library

To create a copy template in a project library, proceed as follows:

1. Open task card "Libraries".
2. Click "Project library" to open the palette.
3. Select the device in the project tree.

   - Or -

   Select a device or several devices with or without network in the network view (lasso is possible).
4. Drag the selection to the "Copy templates" folder or any of its subfolders.

##### Creating a copy template in a global library

To create a copy template in a global library, proceed as follows:

1. Open task card "Libraries".
2. Click "Global libraries" to open the palette.
3. Open the global library or create a new global library.
4. Select the device in the project tree.

   - Or -

   Select a device or several devices with or without network in the network view (lasso is possible).
5. Drag the selection to the "Copy templates" folder or any of its subfolders.

##### Result

The selected elements are inserted into the project library or global library as copy templates. Only one entry per object is created. A selection with several devices also only creates one entry. The symbol in front of the copy template indicates the source.

Each element is assigned a default name that you can change.

#### Using copy templates

##### Overview

The TIA Portal allows you to insert the copy templates at the appropriate positions in the drive project. Application areas:

- Using copy template, you can use individual objects a multiple number times in the same project.
- After the library has been exported, you can also use the objects in other projects and other operating units.
- You can also perform series commissioning for drives and/or networks parameterized using copy templates.

##### Using a copy template from a project library

To use a copy template from a project library, proceed as follows:

1. Open task card "Libraries".
2. Click "Project library" to open the palette.
3. Select the copy template.
4. Drag the selection to the project folder in the project tree.

   - Or -
5. Drag the selection to the network view if the copy template originates from there.

   If you have created a network with devices as copy template via the network view, it can only be inserted again in the network view.

##### Using a copy template from a global library

To use a copy template from a global library, proceed as follows:

1. Open task card "Libraries".
2. Click "Global libraries" to open the palette.
3. Open a global library.
4. Select the copy template.
5. Drag the selection to the project folder in the project tree.

   - Or -
6. Drag the selection to the network view if the copy template originates from there.

   If you have created a network with devices as copy template via the network view, it can only be inserted again in the network view.

##### Result

The objects included in the copy template - for example devices and networks - are created in the project.

### Managing the parameter list

This section contains information on the following topics:

- [Editing the parameter list](#editing-the-parameter-list)
- [Searching for parameters](#searching-for-parameters)
- [Comparing parameters](#comparing-parameters)
- [Managing user-defined lists](#managing-user-defined-lists)

#### Editing the parameter list

##### Overview

The parameter list provides the following functions:

- Monitoring and editing parameter values
- Exporting the parameters as CSV
- Comparing parameter settings

For information on the user interface, see also [Parameter view](#parameter-view-g220).

##### Monitoring and editing parameter values online

After you have established an online connection with Startdrive, all parameter input fields are displayed in orange that you can change online.

To change the parameters online, follow these steps:

1. Establish an [online connection](#establishing-an-online-connection-to-the-target-device).

   The display of the parameters changes to "orange".
2. Change the parameter values or settings, if required.
3. Press the enter key to accept the changes.

   The settings then take immediate effect in the drive.

##### Exporting the parameters to CSV file

CSV files can be opened in spreadsheet programs or editors.

To export the parameter list as a CSV file, proceed as follows:

1. Click on the arrow to the right of the ![Exporting the parameters to CSV file](images/149079199243_DV_resource.Stream@PNG-de-DE.png) icon (copy offline parameters to a CSV file).

   A menu selection opens. You can choose whether you only want to export the displayed parameters or the parameters of all drive objects to a CSV file.
2. Select the required export function.

   The Export window opens.
3. Select a storage location in your directory structure. Assign a name for the CSV file and click on "Save".

   The parameter list is saved as a CSV file.

#### Searching for parameters

##### Overview

Use the standard search function of the TIA Portal to specifically search for parameters for SINAMICS drives.

##### Using the standard search function of the TIA Portal

The standard search is displayed in the "Tasks" viewlet in the right-hand editor of the program user interface.

1. To skip the search dialog, enter <Ctrl+F> via the keyboard with activated parameter view.

   ![Searching for parameters](images/149081051019_DV_resource.Stream@PNG-en-US.PNG)

   ![Searching for parameters](images/149081051019_DV_resource.Stream@PNG-en-US.PNG)

   Searching for parameters
2. In the "Search" field, enter either the parameter number or a parameter text for which you wish to search.
3. To start the search, press the <Return> key or click on "Search".

   If the parameter or text is found, the cursor jumps automatically to the position in the parameter list.
4. Press <F3> to jump to the next search result.

#### Comparing parameters

##### Overview

The current parameters of a drive object can be compared with another parameter set via the comparison function in the parameter view.

You can compare the following values of a parameter:

- Deactivate comparison
- Offline - Factory setting
- Online - Offline
- Online - Factory setting

##### Comparing parameters

To compare the parameters of the drive object with another parameter set, proceed as follows:

1. Open the parameter view for the device whose parameters you want to compare.
2. Click the black arrow icon of the ![Comparing parameters](images/149081724299_DV_resource.Stream@PNG-de-DE.png) "Compare current parameters of this drive object with another data set" button.

   A drop-down list containing the comparison options opens:

   - Deactivate comparison
   - Offline - Factory setting (default setting in offline mode)
   - Online - Offline (default setting in online mode)
   - Online - Factory setting
3. Select the desired comparison option.

   The selected comparison option is executed as follows:

   - The "Comparison" column is displayed.
   - The comparison result of the selected comparison option is displayed in the "Comparison" column by icons.

**Optional:**

If you click the scales icon of the ![Comparing parameters](images/149081724299_DV_resource.Stream@PNG-de-DE.png) button, the selected parameter is compared depending on the active parameterization mode:

- Offline mode: The parameters are compared to the factory settings by default.
- Online mode: The parameters are compared to the offline settings by default.

**Icons in the "Comparison" column**

| Icon | Meaning |
| --- | --- |
| ![Comparing parameters](images/150767578123_DV_resource.Stream@PNG-de-DE.png) | The comparison values are equal and error-free. |
| ![Comparing parameters](images/149081596043_DV_resource.Stream@PNG-de-DE.png) | Offline - Factory setting: The comparison values are different as well as technologically and syntactically error-free. |
| ![Comparing parameters](images/149081587467_DV_resource.Stream@PNG-de-DE.png) | Online - Offline: The comparison values are different and error-free. |
| ![Comparing parameters](images/149081715723_DV_resource.Stream@PNG-de-DE.png) | Online - Factory setting: The comparison values are different and error-free. |
| ![Comparing parameters](images/149081604619_DV_resource.Stream@PNG-de-DE.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Comparing parameters](images/149081651595_DV_resource.Stream@PNG-de-DE.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Comparing parameters](images/149503415051_DV_resource.Stream@PNG-de-DE.png) | At least one of the two comparison values has a technological or syntax error. |
| ![Comparing parameters](images/149081681547_DV_resource.Stream@PNG-de-DE.png) | The comparison is not possible. At least one of the two comparison values is not available (e.g. snapshot). |

#### Managing user-defined lists

This section contains information on the following topics:

- [Fundamentals](#fundamentals-2)
- [Creating a user-defined parameter list](#creating-a-user-defined-parameter-list)
- [Editing the user-defined parameter list](#editing-the-user-defined-parameter-list)

##### Fundamentals

###### Overview

The user-defined list is used to compile a list of specifically selected parameters. This involves an excerpt from an underlying parameter list with specific parameters. The user-defined list can only be created and edited in the project tree.

You can edit the values of the parameters in this drop-down list. Example:

- You can create a user-defined list with values for a specific device and open the list in another device (preferably with the same hardware configuration).
- You can compare the device values with the saved values and can accept the saved value for the device if required.

**Benefits**

A user-defined list makes sense for the following application objectives:

- Compilation of the most important parameters
- Assignment of parameters to parameter groups with comments for users
- Carrying out series commissioning based on saved parameter values
- Documentation for the drive with listed parameters and setting values

The exported parameter list in json format can also be read in the web server.

###### Requirement

- If project protection is activated:   
  The [function rights](User%20administration%20and%20security.md#access-control) for editing the parameter values are enabled for your user account.   
  Observe the detailed information under point "[User administration and security](User%20administration%20and%20security.md#overview)".

###### Storage location

The user-defined list is saved together with the project or drive data. However, it can also be saved or archived as external file.

###### Call functions of the user-defined list

You can call a user-defined list either via the project tree or via menu functions.

The toolbar of the default parameter list provides the following functions:

Icons in the navigation

| Icon | Meaning |
| --- | --- |
| ![Call functions of the user-defined list](images/146041048075_DV_resource.Stream@PNG-de-DE.png) | Inserts a new parameter line above an active row. |
| ![Call functions of the user-defined list](images/146041056651_DV_resource.Stream@PNG-de-DE.png) | Inserts a new parameter row at the bottom of the list. |
| ![Call functions of the user-defined list](images/146041009547_DV_resource.Stream@PNG-de-DE.png) | Inserts a comment below the active row in the list. |
| ![Call functions of the user-defined list](images/149108825099_DV_resource.Stream@PNG-de-DE.png) | Imports a list from the file directory. |
| ![Call functions of the user-defined list](images/149495441675_DV_resource.Stream@PNG-de-DE.png) | Exports the active user-defined list to a file directory. |
| ![Call functions of the user-defined list](images/146039247371_DV_resource.Stream@PNG-de-DE.PNG) | Compares the current parameter settings with the factory settings or compares between online and offline values or compares with manually acquired new parameter settings. |
| ![Call functions of the user-defined list](images/149108979723_DV_resource.Stream@PNG-de-DE.png) | Displays a selection column. This column permits the selection of individual parameters for overwriting with user-defined parameter values. |
| ![Call functions of the user-defined list](images/171913450891_DV_resource.Stream@PNG-de-DE.png) | Displays the current overwrite direction of the parameter values. Allows you to set the desired overwrite direction. |
| ![Call functions of the user-defined list](images/149108958347_DV_resource.Stream@PNG-de-DE.png) | Executes an overwrite action. All selected parameters are overwritten. |
| ![Call functions of the user-defined list](images/149108833547_DV_resource.Stream@PNG-de-DE.png) | Toggles the extended display of the table on and off. |
| ![Call functions of the user-defined list](images/171913442059_DV_resource.Stream@PNG-de-DE.PNG) | Hides or shows invalid parameters. |
| ![Call functions of the user-defined list](images/171913317771_DV_resource.Stream@PNG-de-DE.png) | Turns a link column on or off. The link allows the user to jump to the original use of a parameter. |

In the project tree you can create a new list directly via navigation entries or load a saved list from your file location.

##### Creating a user-defined parameter list

###### Overview

You can create and save user-defined lists using icons or context menus. Here is a selection of the creation options:

###### Creating a parameter list and manually filling it with parameters

1. To create a new parameter list, proceed as follows:

   - In the project tree, select entry "User-defined lists" and call menu "Insert > Add new list".

     - Or -
   - In the project tree of the drive, call "User-defined lists > Add new list".

   The "User-defined list_#" tab opens (e.g. User-defined list_1, User-defined list_2).
2. Now compile the required parameters for the parameter list:

   - Enter the parameter number in the "Number" column in the <add new> text box and confirm with Return.

     - Or -
   - Enter a part of the parameter number in the "Number" column in the <add new> text box and open the drop-down list of the text box. Click on the required parameter in the list.

   Startdrive now automatically inserts the most important data of the parameter in the column fields of the current row.
3. Enter further parameters in the parameter list in the same way.

**Result**

A new parameter list is created in the project tree of the particular drive under "User-defined lists" and displays the manually inserted parameters. Within the project, this parameter list can also be dragged and dropped to another drive.

Other options:

- List names can be changed (in the project tree)
- The list can be shifted (dragging and dropping) within the drive or within the project
- List can be archived in the project library (see below)
- List can be deleted

###### Creating a parameter list with selected parameters

1. Select the required parameters from a general parameter list with <Shift key + mouse click> or <Ctrl + mouse click>.
2. Select shortcut menu "Attach to user-defined parameter list".

**Result**

The selected parameters are inserted in an existing parameter list.

###### Exporting the parameter list as file

The parameter list can be saved to a file with the set parameter values.

1. In a user-defined list that is open, click on icon ![Exporting the parameter list as file](images/149495441675_DV_resource.Stream@PNG-de-DE.png) (Export).

   - Or -

   In the drive project tree select the required list and call shortcut menu "Export user-defined list".

   Window "Export user-defined list to file" opens.
2. Select whether you want to export the parameter list with or without parameter values.
3. Click "OK" to confirm the selection.

   The "Save As..." dialog box opens.
4. Assign a file name and a file format (csv, json) for the file to be exported.

   For a json format, do not use any special characters in file name. This is necessary to ensure that the file can also be opened via the web server later on.
5. Assign a storage location in your file location and click "Save".

**Result**

The parameter list is saved as an export file. The assigned name of the export file is adopted as the new name of the parameter list and displayed in the parameter view in Startdrive. The export file also includes the drive type and firmware version. Later on, it will be possible to open the export file in, or import it to, drives only if these have the same drive type and firmware version.

###### Closing the parameter list

1. Click the X icon at the upper right-hand edge of the tab.
2. If you do not want to save the parameter list, click "No".

   The parameter list will then be closed without being saved. You can ignore the subsequent steps.
3. If you want to save the parameter list, click "Yes".

   The "Save As" window opens.
4. Assign a path and a file name to the json file in your file location and click "Save".

**Result**

The parameter list is saved as a json file. The assigned name of the json file is displayed as the name of the parameter list in Startdrive.

###### Creating a parameter list group

Using groups and subgroups, you can create and manage several parameter lists for a drive. You can create or import a parameter list in each group and subgroup. You can also archive groups in the project library.

1. Select a folder in project folder "User-defined list".
2. Open menu "Insert > Group".

   - Or -

   Open the shortcut menu "Add new group".
3. Save the project.

**Result**

A new group is created in the user-defined lists. The name of the group is preassigned.

Other options:

- Group names can be changed (in the project tree)
- Groups can be shifted (drag-and-drop)
- Groups can be archived in the project library (see below)
- Groups can be deleted

###### Storing a user-defined group or user-defined list as library

You can archive user-defined groups and lists in the project library.

1. Open task card "Libraries".
2. Click "Project library" to open the palette.
3. Select a group or list in the project tree
4. Drag-and-drop the group or list into the "Copy templates" folder or any subfolder of "Copy templates".
5. Save the project.

**Result**

A group or list is now available in the project library as copy template in the project.

##### Editing the user-defined parameter list

###### Overview

You have the following options in a user-defined list:

- Importing the parameter list

  > **Note**
  >
  > Parameter lists of different drive types are not compatible with each other. The parameter list to be opened must match the drive type of the displayed drive.
- Add parameters
- Add comments
- Add rows
- Copy parameters/comments
- Delete rows
- Filtering the parameter list
- Set user-defined parameter values
- Compare parameter values (with factory settings or online/offline)

###### Requirements

To open:

- A parameter list is saved in the file repository of your PC/PG and is usable at all times.

###### Importing the parameter list

You can import the parameter lists of the displayed drive saved in the file system into the project as follows.

1. In an open user-defined list, click the arrow to the right of the icon ![Importing the parameter list](images/149108825099_DV_resource.Stream@PNG-de-DE.png) (Import).

   - Or -

   In the project tree of the drive in the project, call menu "User-defined lists > Import list".

   Dialog "Import user-defined list from file" opens.
2. Select whether you want to import the user-defined parameter list with or without parameter values.

   The "Open" dialog opens.
3. Select the import file of the desired parameter list in the file location of your operating unit. Click "Open."

**Result**

If problems occurred during import, a warning message will be generated. A link in the message allows you to open a log file that explains the import problem in more detail and gives hints on how to fix it. The alarm is also listed in the Inspector window under "Info".

If the import was successful, the parameter list is opened and displayed in the project tree.

- If, when the list is opened, a parameter of the import file is not present in the parameter list of the drive, this parameter will then be removed from the opened list and a corresponding message will be displayed.
- If you imported a parameter list in json format during the import which contains several individual parameter lists, the individual imported parameter lists are inserted in a new collective folder in the project tree.

###### Inserting parameters in the displayed parameter list

Proceed as follows to append parameters:

1. Open the parameter list in the project tree.

   ![Entering parameters](images/173861188491_DV_resource.Stream@PNG-en-US.PNG)

   ![Entering parameters](images/173861188491_DV_resource.Stream@PNG-en-US.PNG)

   Entering parameters
2. Enter the parameter number in the "Add new" input field located in the "Number" column and confirm your entry with <Return>.
3. Repeat step 2 for all of the parameters you want to enter.

**Result**

The added parameters are inserted at the bottom of the user-defined parameter list or directly below the previously selected parameter line.

###### Add comments

Proceed as follows to add a comment to a parameter list:

1. Select a parameter line in the "User_list_#" for which a comment is to be inserted.
2. In the user list, select shortcut menu "Insert comment line".

   ‑ Or ‑

   In the toolbar, click on icon ![Add comments](images/146041009547_DV_resource.Stream@PNG-de-DE.png) (Insert comment line).
3. Repeat step 2 for all comments you want to enter.

**Result**

The new comment is inserted directly above the selected row in each case. The comment line is highlighted in white and marked with a "//".

The comment can also be deleted from the list in the same way as a parameter.

![Inserting a comment](images/173865355403_DV_resource.Stream@PNG-en-US.PNG)

Inserting a comment

###### Inserting a new row

1. Select the parameter line or comment line in the "User_list_#" after which a new row is to be inserted.

   ![Inserting a row](images/173866200715_DV_resource.Stream@PNG-en-US.PNG)

   ![Inserting a row](images/173866200715_DV_resource.Stream@PNG-en-US.PNG)

   Inserting a row
2. In the toolbar, click on icon ![Inserting a new row](images/146041048075_DV_resource.Stream@PNG-de-DE.png) (Insert row).

   - Or -

   In the toolbar, click on the ![Inserting a new row](images/146041056651_DV_resource.Stream@PNG-de-DE.png) (Insert row) icon.

**Result**

Depending on the call, the new row is inserted either before the selected row or as the last row of the parameter list.

###### Copying a parameter/comment

You can also copy the contents of a parameter list to another parameter list via Copy & Paste.

1. Select the parameter/comment or a row of a parameter list.

   ![Selected entries](images/173866142859_DV_resource.Stream@PNG-en-US.PNG)

   ![Selected entries](images/173866142859_DV_resource.Stream@PNG-en-US.PNG)

   Selected entries

   A multiple selection can be made by pressing the Shift or Ctrl key.
2. Select "Copy" in the shortcut menu.
3. As copy target, activate/open the required parameter list.
4. Select the parameter/comment or a row of the target parameter list.
5. In the shortcut menu, select "Paste".

**Result**

The copied parameters or comments are inserted in the next free rows of the list.

###### Deleting a row

To delete a parameter or comment, proceed as follows.

1. Select the parameter/comment or a row in the parameter list.

   A multiple selection can be made by pressing the Shift or Ctrl key.
2. Select "Delete" in the shortcut menu.

**Result**

The selected rows are deleted.

###### Filtering the parameter list

You can filter the parameters listed in the parameter list via the list columns. Below the header, each column has a filter field. By entering or selecting an entry, you can filter the entire list for the corresponding entries. Example: Show only r parameters:

1. Enter the letter "r" in the filter field of the "Number" column.

**Result**

The parameter list is restricted to r parameters.

###### Uncommenting parameters

You can convert parameters in the parameter list to a comment.

1. Select the parameter in the parameter list.
2. Insert "//" in front of the parameter name in the "Number" field.

**Result**

The parameter is now no longer listed as a parameter in the list, but rather, as a comment. The previously displayed parameter data of the parameter are hidden in this parameter list.

The comment can be changed back to a parameter by removing the "//". In this case, however, the program checks the parameter name for invalid characters and displays a message in case of an error.

###### Comparing parameters

You can compare changed parameter values of the parameter list displayed in the program with the factory settings.

1. Click the black arrow icon of the ![Comparing parameters](images/149081724299_DV_resource.Stream@PNG-de-DE.png) "Compare current parameters of this drive object with another data set" button.

   A drop-down list containing the comparison options opens:

   - Deactivate comparison
   - Offline - Factory setting (default setting in the offline mode) = only visible offline
   - Offline - user-defined value = only visible offline
   - Online - Offline (default setting in the online mode) = only visible online
   - Online - Factory setting = only visible online
   - Online - user-defined value = only visible online
2. Select the desired comparison option.

   The selected comparison option is executed as follows:

   - The "Comparison" column is displayed.
   - The comparison result of the selected comparison option is displayed in the "Comparison" column by icons.

**Optional:**

If you click the scales icon of the ![Comparing parameters](images/149081724299_DV_resource.Stream@PNG-de-DE.png) button, the selected parameter is compared depending on the active parameterization mode:

- Offline mode: The parameters are compared to the factory settings by default.
- Online mode: The parameters are compared to the offline settings by default.

**Icons in the "Comparison" column**

| Icon | Meaning |
| --- | --- |
| ![Comparing parameters](images/150767578123_DV_resource.Stream@PNG-de-DE.png) | The comparison values are equal and error-free. |
| ![Comparing parameters](images/149081596043_DV_resource.Stream@PNG-de-DE.png) | Offline - Factory setting: The comparison values are different as well as technologically and syntactically error-free. |
| ![Comparing parameters](images/150764441611_DV_resource.Stream@PNG-de-DE.PNG) | Offline - user-defined value: The user-defined values differ from the values displayed offline. |
| ![Comparing parameters](images/149081587467_DV_resource.Stream@PNG-de-DE.png) | Online - Offline: The comparison values are different and error-free. |
| ![Comparing parameters](images/149081715723_DV_resource.Stream@PNG-de-DE.png) | Online - Factory setting: The comparison values are different and error-free. |
| ![Comparing parameters](images/150768274315_DV_resource.Stream@PNG-de-DE.png) | Online - user-defined value: The user-defined values differ from the values displayed online. |
| ![Comparing parameters](images/149081604619_DV_resource.Stream@PNG-de-DE.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Comparing parameters](images/149081651595_DV_resource.Stream@PNG-de-DE.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Comparing parameters](images/149503415051_DV_resource.Stream@PNG-de-DE.png) | At least one of the two comparison values has a technological or syntax error. |
| ![Comparing parameters](images/149081681547_DV_resource.Stream@PNG-de-DE.png) | The comparison is not possible. At least one of the two comparison values is not available (e.g. snapshot). |

###### Acquiring and accepting user-defined parameter values

In the parameter list, you can make your own parameter settings, subsequently compare them with the factory settings and, in case of doubt, apply them.

1. Click the scales icon on the ![Acquiring and accepting user-defined parameter values](images/149081724299_DV_resource.Stream@PNG-de-DE.png) button.

   Several columns will then be shown. The comparison mode is automatically activated.
2. Select the parameter in the parameter list.
3. Set the parameter value required for this parameter in the "User-defined value" column.

   Following incorrect manual inputs, an error message indicating that the entered value lies outside of the permissible value range is displayed. In this case, correct the input.

   The comparison result of the selected comparison option is displayed in the "Comparison" column by icons.
4. If you want to accept the manual value input in the data set, activate the check box in front of the "Comparison" column.

   ![Changing values](images/173866424971_DV_resource.Stream@PNG-en-US.PNG)

   ![Changing values](images/173866424971_DV_resource.Stream@PNG-en-US.PNG)

   Changing values
5. Make any additional parameter settings for the other parameters in this list (steps 3 and 4).
6. Then click on the icon ![Acquiring and accepting user-defined parameter values](images/149108958347_DV_resource.Stream@PNG-de-DE.png) ("Execute overwrite action").

   A comparison value match is then displayed in the "Comparison" column ![Acquiring and accepting user-defined parameter values](images/150767578123_DV_resource.Stream@PNG-de-DE.png).

   ![Values changed](images/173866428939_DV_resource.Stream@PNG-en-US.PNG)

   ![Values changed](images/173866428939_DV_resource.Stream@PNG-en-US.PNG)

   Values changed

**Note**

**Overwrite direction**

The current parameter values are normally overwritten with the user-defined values. The corresponding overwrite direction is preset in the toolbar (![Acquiring and accepting user-defined parameter values](images/171913450891_DV_resource.Stream@PNG-de-DE.png)). However, you can change the overwrite direction if required.

- To do so, click on the vertical arrow in the icon and select the overwrite direction "Current parameter values to user-defined values".

**Result**

The parameter values or settings of the selected parameters are changed in the desired overwrite direction.

As a rule, the current parameter values are overwritten by the user-defined parameter values.

### Rules for the use of data sets

This section contains information on the following topics:

- [Overview](#overview-4)
- [Data set definitions](#data-set-definitions)

#### Overview

##### Maximum number of data sets which can be used

The maximum number of data sets possible is as follows:

- 4 [CDS](#cds-command-data-set-command-data-set) (command data sets) (default = 2)
- 16 [DDS](#dds-drive-data-set-drive-data-set) (drive data sets)
- 16 [EDS](#eds-encoder-data-set-encoder-data-set) (encoder data sets), with max. 3 EDS per DDS
- 16 [MDS](#mds-motor-data-set-motor-data-set) (motor data sets), with the number of MDS ≤ number of DDS

##### Schematic diagram

![Maximum permissible number of data sets](images/145688733579_DV_resource.Stream@PNG-en-US.png)

Maximum permissible number of data sets

#### Data set definitions

This section contains information on the following topics:

- [PDS: Parameter data set](#pds-parameter-data-set)
- [CDS: Command data set (Command Data Set)](#cds-command-data-set-command-data-set)
- [DDS: Drive data set (Drive Data Set)](#dds-drive-data-set-drive-data-set)
- [EDS: Encoder data set (Encoder Data Set)](#eds-encoder-data-set-encoder-data-set)
- [MDS: Motor data set (Motor Data Set)](#mds-motor-data-set-motor-data-set)

##### PDS: Parameter data set

A parameter data set (or power unit data set) consisting of multiple adjustable parameters which are responsible for the configuration of a power unit, e.g. of a Motor Module, Line Module, or Power Module.

###### Function diagrams (FD)

FD-8580

##### CDS: Command data set (Command Data Set)

###### Description

A number of signal interconnection parameters (signal sinks) that are responsible for the control are combined in a command data set (CDS).

By parameterizing several command data sets and switching between them, the drive can be operated with different pre-configured signal sources.

A command data set includes for example:

- Numerical signal sources for control commands (digital signals)

  - On/Off, Enables (c0844, etc.)
  - Jog (c1055, etc.)
- Binary signal sources for setpoints (analog signals)

  - Voltage setpoint for U/f control (c1330)
  - Torque limits and scaling factors (c1522, c1523, r1528, r1529)

A drive object can – depending on the type – manage up to 4 command data sets. The number of command data sets is configured with [p0170](SINAMICS%20Parameter%20G220.md#p0170-number-of-command-data-sets-cds).

Binector inputs c0810 to c0811 are used to select a command data set. They represent the number of the command data set (0 to 2) in binary format (where c0811 is the most significant bit).

- c0810: Command data set selection CDS bit 0
- c0811: Command data set selection CDS bit 1

If a command data set that does not exist is selected, the current data set remains active. The selected data set is displayed using parameter ([r0836](SINAMICS%20Parameter%20G220.md#r083603-command-data-set-cds-selected)).

> **Note**
>
> When using standard telegrams in command data sets, make sure that you do not change telegram interconnections as this may lead to inconsistent behavior otherwise. If you wish to change telegram interconnections, assign the telegram selection with 999 (free telegram).

###### Example: Switchover between command data set 0 and 1

![Switching the command data set (CDS)](images/164800756619_DV_resource.Stream@PNG-en-US.png)

Switching the command data set (CDS)

###### Function diagrams (FD)

Command data sets (CDS) - 8560 -

###### Additional parameters

---

##### DDS: Drive data set (Drive Data Set)

###### Description

A drive data set (DDS) contains various adjustable parameters that are relevant for open-loop and closed-loop drive control:

- Numbers of the assigned motor and encoder data sets:

  - [p0186](SINAMICS%20Parameter%20G220.md#p01860n-motor-data-sets-mds-number): Assigned motor data set (MDS)
  - [p0187](SINAMICS%20Parameter%20G220.md#p01870n-motor-encoder-encoder-data-set-number) to [p0188](SINAMICS%20Parameter%20G220.md#p01880n-encoder-2-encoder-data-set-number): up to 2 assigned encoder data sets (EDS)
- Various control parameters, e.g.:

  - Fixed speed setpoints ([p1001](SINAMICS%20Parameter%20G220.md#p10010n-fixed-speed-setpoint-1) to [p1015](SINAMICS%20Parameter%20G220.md#p10150n-fixed-speed-setpoint-15))
  - Speed limits min./max. ([p1080](SINAMICS%20Parameter%20G220.md#p10800n-minimum-speed), [p1082](SINAMICS%20Parameter%20G220.md#p10820n-maximum-speed))
  - Characteristic data of ramp-function generator ([p1120](SINAMICS%20Parameter%20G220.md#p11200n-ramp-function-generator-ramp-up-time) ff.)
  - Characteristic data of controller ([p1240](SINAMICS%20Parameter%20G220.md#p12400n-vdc-controller-or-vdc-monitoring-configuration) ff.)

The parameters that are grouped together in the drive data set are identified by "DDS" in the parameter help under "Dynamic Index" and are assigned an index [0...n].

It is possible to parameterize several drive data sets. You can switch easily between different drive configurations (control type, motor, encoder) by selecting the corresponding drive data set.

One drive object can manage up to 16 drive data sets. The number of drive data sets is configured with [p0180](SINAMICS%20Parameter%20G220.md#p0180-number-of-drive-data-sets-dds).

The binary signal sinks c0820 to c0824 are used to select a drive data set. They represent the number of the drive data set (0 to 31) in binary format (where c0824 is the most significant bit).

- c0820: Drive data set selection DDS, bit 0
- c0821: Drive data set selection DDS, bit 1
- c0822: Drive data set selection DDS, bit 2
- c0823: Drive data set selection DDS, bit 3
- c0824: Drive data set selection DDS, bit 4

**Recommendation for the number of DDSs for a drive:**

The number of drive data sets for a drive should correspond to the options for changeover. The following must therefore apply:

p0180 (DDS) ≥ max. ([p0120](SINAMICS%20Parameter%20G220.md#p0120-number-of-power-unit-data-sets-pds) (PDS), [p0130](SINAMICS%20Parameter%20G220.md#p0130-number-of-motor-data-sets-mds) (MDS))

###### Function diagrams (FD)

Drive data sets (DDS) - 8565 -

###### Additional parameters

---

##### EDS: Encoder data set (Encoder Data Set)

###### Description

An encoder data set (EDS) contains various adjustable parameters of the connected encoder, which are relevant for configuring the drive; e.g.:

- Encoder type selection ([p0400](SINAMICS%20Parameter%20G220.md#p04000n-encoder-type-selection))

The parameters that are grouped together in the encoder data set are identified by "EDS" in the parameter help under "Dynamic Index" and are assigned an index [0...n].

A separate encoder data set is required for each encoder controlled by the Control Unit. Up to 3 encoder data sets are assigned to a drive data set via parameters [p0187](SINAMICS%20Parameter%20G220.md#p01870n-motor-encoder-encoder-data-set-number) and [p0188](SINAMICS%20Parameter%20G220.md#p01880n-encoder-2-encoder-data-set-number).

An encoder data set can only be changed over using a DDS switchover.

An encoder data set switchover without pulse inhibit (motor is being fed with power) may only be performed on adjusted encoders (pole position identification has been carried out or the commutation angle determined for absolute encoders).

Each encoder must only be assigned to one drive.

Using a power unit for the alternating operation of several motors would be an EDS switchover application. Contactors are switched over so that the power unit can be connected to the different motors. Each of the motors can be equipped with an encoder or can also be operated without an encoder. Each encoder must be connected to its own SMx.

If encoder 1 (p0187) is switched over via DDS, then an MDS must also be switched over.

> **Note**
>
> **Switching over between several encoders**
>
> In order to be able to switch between two or more encoders using the EDS switched function, you must connect these encoders via various Sensor Modules or DRIVE-CLiQ ports.
>
> When using the same connection for several encoders, the same EDS and the same encoder type must be used. In this case a switchover on the analog side (e.g. of the SMC) is recommended. A switchover on the DRIVE-CLiQ side is, due to the permissible insertion cycles and the longer times to establish DRIVE-CLiQ communication, only possible with some restrictions.

One drive object can manage up to 16 encoder data sets. The number of encoder data sets configured is specified in [p0140](SINAMICS%20Parameter%20G220.md#p0140-number-of-encoder-data-sets-eds).

When a drive data set is selected, the assigned encoder data sets are also selected.

> **Note**
>
> **EDS switchover for safe motion monitoring**
>
> An encoder which is used for safety functions must not be switched over when a drive data set (DDS) is switched over.
>
> The safety functions check the safety-relevant encoder data for changes when data sets are switched over. If a change is detected, safety message C01670 is displayed with a fault value of 10, which results in a non-acknowledgeable STO. The safety-relevant encoder data in the various data sets must therefore be identical.

###### Function diagrams (FD)

Encoder data sets (EDS) - 8570 -

###### Additional parameters

---

##### MDS: Motor data set (Motor Data Set)

###### Description

A motor data set (MDS) contains various setting parameters of the connected motor, which are relevant when configuring the drive. It also contains certain display parameters with calculated data.

- Adjustable parameters, e.g.:

  - Motor type selection ([p0300](SINAMICS%20Parameter%20G220.md#p03000n-motor-type-selection))
  - Rated motor data ([p0304](SINAMICS%20Parameter%20G220.md#p03040n-rated-motor-voltage) ff.)
- Display parameters, e.g.:

  - Calculated rated data ([p0330](SINAMICS%20Parameter%20G220.md#r03300n-rated-motor-slip) ff.)

The parameters that are grouped together in the motor data set are identified by "MDS" in the parameter help under "Dynamic Index" and are assigned an index [0...n].

A separate motor data set is required for each motor that is controlled by the Control Unit via a Motor Module. The motor data set is assigned to a drive data set via parameter [p0186](SINAMICS%20Parameter%20G220.md#p01860n-motor-data-sets-mds-number).

A motor data set switchover can only be performed indirectly via a DDS switchover. The motor data set switchover is, for example, used for:

- Changing over between different motors
- Changing over different windings in a motor (e.g. star-delta changeover)
- Adapting the motor data

If several motors are operated alternately on a Motor Module, a matching number of drive data sets must be created.

One drive object can manage up to 16 motor data sets. The number of motor data sets in [p0130](SINAMICS%20Parameter%20G220.md#p0130-number-of-motor-data-sets-mds) must not exceed the number of drive data sets in [p0180](SINAMICS%20Parameter%20G220.md#p0180-number-of-drive-data-sets-dds).

If this rule is not observed, alarm A07514 is output.

###### Example of data set assignment

| DDS | Motor (p0186) | Encoder 1 ([p0187](SINAMICS%20Parameter%20G220.md#p01870n-motor-encoder-encoder-data-set-number)) | Encoder 2 ([p0188](SINAMICS%20Parameter%20G220.md#p01880n-encoder-2-encoder-data-set-number)) |
| --- | --- | --- | --- |
| DDS 0 | MDS 0 | EDS 0 | EDS 1 |
| DDS 1 | MDS 0 | EDS 0 | EDS 3 |
| DDS 2 | MDS 0 | EDS 0 | EDS 4 |
| DDS 3 | MDS 1 | EDS 6 | - |

###### Function diagrams (FD)

Motor data sets (MDS) - 8575 -

###### Additional parameters

---

## Sequence of a device configuration and basic commissioning

> **Note**
>
> **Only in the offline mode**
>
> The drive components can only be combined and specified in the offline mode. In online mode, all corresponding setting ranges are marked in the device view and in the inspector window.

> **Note**
>
> **User administration and security**
>
> SINAMICS drives of the latest generation generally have extended protection. This usually has the effect that, as a user, you have to log in to view or edit the drive data offline as well as online. The most important protective measures in brief:
>
> - Project protection can be activated for Startdrive projects in the TIA Portal (offline). If project protection is activated, corresponding rights are required for access. Once project protection has been activated, it cannot be deactivated.
> - A "Security Wizard" usually appears when creating new drives in the project. With the help of this wizard, you can already make the most important security settings for this drive within the project when creating the drive.
> - To access a protected drive online, you ALWAYS need the corresponding access rights.
>
> Detailed information on this topic can be found under "[User administration and security](User%20administration%20and%20security.md#overview)".

> **Note**
>
> **Editing mode required for online commissioning**
>
> If you want to make important settings online, activation of the editing mode is mandatory. Restore points that are required as a return point following a cancellation of the current online parameterization are automatically created by the editing mode in the "guided quick startup" (and in the "Parameterization" area) during configuration.
>
> A separate editing mode is not required in the "Rotating & optimizing" area.

> **Note**
>
> **Telegram configuration offline**
>
> In the guided quick startup, telegram settings can generally only be made offline.

### Basis: Simple basic parameterization

The following steps are required:

1. [Create or open the project with Startdrive](#managing-a-startdrive-project).
2. [Create the device configuration in Startdrive offline](#creating-a-device-configuration-manually-offline)

   Optional: Making security settings for project and drive
3. [Make basic settings offline via the guided quick startup](Commissioning%20SINAMICS%20G220%20drives.md#guided-quick-startup)
4. [Load the project to the target device](#loading-the-configuration-from-the-project-to-the-device).
5. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
6. [Perform optimization](Commissioning%20SINAMICS%20G220%20drives.md#rotate-optimize-1)

**Result:**

The motor rotates.

### Variant 1: Basic parameter assignment online

The basic parameterization can also be carried out in online mode as an alternative to offline mode. This results in a slightly modified procedure:

The following steps are required:

1. [Create or open the project with Startdrive](#managing-a-startdrive-project).
2. [Create the device configuration in Startdrive offline](#creating-a-device-configuration-manually-offline)

   Optional: Making security settings for project and drive
3. [Downloading project data to the target device](#loading-the-configuration-from-the-project-to-the-device)
4. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
5. Make basic settings online via the guided quick startup in editing mode

   - [Make basic settings in quick startup steps](Commissioning%20SINAMICS%20G220%20drives.md#guided-quick-startup)
   - [Perform optimization](Commissioning%20SINAMICS%20G220%20drives.md#rotate-optimize-1)

**Result:**

The motor rotates.

### Variant 2: Basic parameter assignment together with a SIMATIC controller

If you want to commission the SINAMICS drive together with a SIMATIC control system, the optimum sequence for basic parameterization is as follows:

1. [Create or open the project with Startdrive](#managing-a-startdrive-project)
2. Create the device configuration in Startdrive offline

   - [Insert the SINAMICS drive into the project](#adding-a-drive)
   - Optional: Making security settings for project, drive and controller
   - [Insert a motor, encoder and other system components](#motor)
   - [Insert the SIMATIC controller into the project](#adding-a-controller-plc)
   - [Network the SIMATIC controller and drive](#networking-the-controller-plc-and-drive)
   - [Insert a technology object into the SIMATIC controller](#inserting-a-technology-object-into-the-simatic-s7-controller)
   - [Interconnect the technology object with the drive](#interconnecting-the-technology-object-and-sinamics-drive)
3. [Downloading project data to the target device](#loading-the-configuration-from-the-project-to-the-device)
4. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
5. Make basic settings online via the guided quick startup in editing mode

   - [Make basic settings in quick startup steps](Commissioning%20SINAMICS%20G220%20drives.md#guided-quick-startup)
   - [Perform optimization](Commissioning%20SINAMICS%20G220%20drives.md#rotate-optimize-1)

**Result:**

The motor rotates.

## Configuring devices in the project

This section contains information on the following topics:

- [Managing a Startdrive project](#managing-a-startdrive-project)
- [Creating a device configuration manually offline](#creating-a-device-configuration-manually-offline)

### Managing a Startdrive project

This section contains information on the following topics:

- [Creating a new project](#creating-a-new-project)
- [Opening the project](#opening-the-project)
- [Closing a project](#closing-a-project)

#### Creating a new project

##### Requirements

- The TIA Portal is installed.
- A current Startdrive Advanced package is installed.

##### Procedure

You can create new projects once the Startdrive application has been opened in the TIA Portal.

1. Click on "Create new project" in the secondary navigation in the Startdrive portal view.

   The entry fields for the basic project data are displayed to the right in the detailed view.

   ![Example: Create new project](images/160241068683_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Create new project](images/160241068683_DV_resource.Stream@PNG-en-US.PNG)

   Example: Create new project
2. Acquire the project data:

   - Project name:

     Startdrive automatically counts each new project.
   - Path:

     The simpler the archive path for the project, the faster the project can be loaded.
   - Author:

     The short name of the person entering the data is preassigned.
   - Comment:

     You can store brief project information here.
3. Click "Create" to save basic project data.

##### Result

The new project is created and simultaneously opened. Possible next steps are displayed in the detailed view.

If necessary, you can assign a project protection for the newly created project (see [Managing project protection](User%20administration%20and%20security.md#activating-project-protection)).

#### Opening the project

##### Activated project protection

In the TIA Portal, you can apply project protection to Startdrive projects. This means that only a user with the appropriate access rights can access project data.

If a Startdrive project is protected, you are prompted to enter a password when you try to open it. You require the following information to open a project:

- User name with authorization for this project
- Password

This information is generated and managed in the user administration of the TIA Portal. Detailed information on project protection can be found in the online help under the heading of "[User administration and security](User%20administration%20and%20security.md#overview)".

> **Note**
>
> **Session timeout**
>
> When project protection is active, the session is timed out if there is no activity. The maximum time that can be set until a timeout is 60 minutes (this depends on the specific configuration). At the latest then, the project is automatically locked if there is no activity.

##### Requirements

- The TIA Portal is installed.
- A current Startdrive Advanced package is installed.

##### Opening an unprotected project

If you wish to change the data of an existing project, then you can load this project at any time.

1. Click on "Open existing project" in the secondary navigation in the Startdrive portal view.

   A selection of the projects last used is displayed to the right in the detailed view.

   ![Opening an existing project](images/160241072651_DV_resource.Stream@PNG-en-US.PNG)

   ![Opening an existing project](images/160241072651_DV_resource.Stream@PNG-en-US.PNG)

   Opening an existing project
2. Select the required project from the list. Then click the "Open" button.

   - Or -

   - Click "Browse", double-click the required project in your directory structure, select project file "*.ap1x.x".

     ![Opening an existing project from the directory](images/160241089419_DV_resource.Stream@PNG-en-US.PNG)

     ![Opening an existing project from the directory](images/160241089419_DV_resource.Stream@PNG-en-US.PNG)

     Opening an existing project from the directory
   - Then click the "Open" button.

##### Opening a protected/locked project

This is how you open a protected project:

1. Click on "Open existing project" in the secondary navigation in the Startdrive portal view.

   A selection of the projects last used is displayed to the right in the detailed view.
2. Select the required project from the list. Then click the "Open" button.

   - Or -

   - Click "Browse", double-click the required project in your directory structure, select project file "*.ap1x.x".
   - Then click the "Open" button.

   Since there is an active project protection, the "Login" dialog will open.
3. Select the user type.   
   If you selected "Anonymous user" or "Single Sign-on", continue with Step 6. Otherwise, continue with Step 4.
4. Enter your user name.
5. Enter your password.
6. Click "OK".

**Note**

As a rule, only limited access is possible without entering a password.

**Note**

If necessary, you can change your password at this point. A password change is mandatory in the following cases:

- If a global user logs on for the first time, if this has been specified in UMC.
- If a project user logs on after the password validity has expired.

Then perform the steps for changing the password; see [Changing the password](Managing%20users%20and%20roles.md#changing-your-own-password).

##### Result

The selected project opens. If another project was previously displayed, then it is now closed.

The interconnected modules of the newly opened project are displayed in the device view. You can specify existing modules differently, or remove existing modules and insert new modules instead.

#### Closing a project

##### Overview

The procedure for closing a project depends on whether the project contains unsaved data, whether there are active program tasks, and whether the project is protected and locked.

##### Requirement

- A Startdrive project is open.

##### Closing a project

To close a project, proceed as follows:

1. Call the "Project > Close" menu.

   - Or -

   Exit the program.

   If you have made changes to the project since it was last saved, a prompt is displayed.
2. Specify whether you want to save the project changes.

   The project is closed.

##### Closing a locked project

If a protected Startdrive project is locked, the "Project locked" dialog appears.

1. To close the project, click on "Close project" in the dialog.

   If you have made changes to the project since it was last saved, a prompt is displayed.
2. Specify whether you want to save the project changes.

   - If you want to save the unsaved data, the "Close project" dialog is displayed again. Unlock the project and save the project data.
   - If you do not want to save the unsaved data, the project will be closed immediately if there are no active program tasks.

   If there are still active program tasks, another message appears.
3. Specify whether you want to terminate these program tasks.

   - If you do not want to terminate the tasks, the "Close project" dialog is displayed again.
   - If you specified that the tasks should be closed, the project will be closed.

##### More information

For more information on project protection, see the "[User administration and security](User%20administration%20and%20security.md#overview)" page.

### Creating a device configuration manually offline

This section contains information on the following topics:

- [Drive](#drive)
- [Motor](#motor)
- [Measuring systems](#measuring-systems)
- [Supplementary system components](#supplementary-system-components)
- [Optional: Control](#optional-control)

#### Drive

This section contains information on the following topics:

- [Adding a drive](#adding-a-drive)
- [Perform detailed settings of the drive](#perform-detailed-settings-of-the-drive)

##### Adding a drive

###### Overview

You can add new drives either in the project view (see below) or in the portal view. For SINAMICS drives from firmware V6.1, you can already define the security settings to access the drive data when creating the drive.

###### Requirements

- A new project has been created.

  - Or -

  An existing project has been opened.
- If the project protection is activated:   
  The [function right](User%20administration%20and%20security.md#access-control) "Edit hardware configuration" is activated for your user account.

###### Procedure

To insert a drive in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click "Drives" to display the available drives.
3. Select the "SINAMICS G220" folder in the path "SINAMICS drives/SINAMICS G".

   Various G220 drives of the following types are available for selection here:

   - G220
   - G220 Clean Power
4. Select the required G220 drive.
5. Select the firmware version that is installed on your drive.
6. If necessary, correct by entering the recommended device name and click "OK".

   If you leave the "Device view" option activated, the device view will open automatically after the security settings (Step 7).
7. The "Security settings Drive unit_X" dialog is open.

   Make the required security settings here for the new drive to be created (see [Making security settings](User%20administration%20and%20security.md#making-security-settings)).

**Note**

If the version numbers (offline project in Startdrive compared with the drive unit) do not match, it will not be possible to go online later. When creating, the current firmware version is always suggested. If required, you can change the version number using the "Version" drop-down list.

**Variant: Inserting a device via the network view or topology view**

Alternatively, you can also insert a drive unit via the network view or topology view.

1. Open the network view.
2. Open the "Drives & starters" entry in the hardware catalog.
3. Open the "SINAMICS drives" entry in the hardware catalog and the corresponding subfolder of the required Control Unit (SINAMICSG/SINAMICS G220).
4. Drag the drive unit from the hardware catalog and drop it in the network view or the topology view.
5. The "Security settings Drive unit_X" dialog is open.

   Make the required security settings here for the new drive to be created (see [Making security settings](User%20administration%20and%20security.md#making-security-settings)).

###### Result

The device has been added. The motor and, if necessary, the motor holding brake must then be configured.

![G220 Control Unit inserted](images/153835023883_DV_resource.Stream@PNG-de-DE.PNG)

G220 Control Unit inserted

##### Perform detailed settings of the drive

###### Overview

You can configure the following details for the SINAMICS G220 drive:

| Group | Settings (detailed menu) |
| --- | --- |
| General | - Product information   Name data - Catalog information   Brief description, description of the components included, firmware version used |
| PROFINET interface [X150] | - General - Ethernet addresses   Subnet, IP address, subnet mask, PROFINET names - Telegram configuration   - Telegrams of the closed-loop drive control: Send, receive, Safety Integrated     For details, see [Telegram configuration](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive) - Advanced options   - Interface options   - Media redundancy   - Clock cycle synchronization for local modules (isochronous mode)   - Real time settings   - Port [X150 P1] and port [X150 P2] - Shared device   Enables the connection of multiple controllers at the same PROFINET interface of the drive. |
| Module parameters | - Activation of channel diagnostics |
| Protection & Security | - Wizard for security settings - User Management & Access Control - Ports and protocols - Encryption of the drive data  For details, see [Higher-level security settings](User%20administration%20and%20security.md#security-default-settings-for-projects-as-of-sinamics-fw-v61) |
| Ethernet commissioning interface [X127] | - General - Ethernet addresses   Subnet, IP address, subnet mask |
| Device selection G220 PN (**mandatory entry**) | - The selection of the desired performance class is mandatory at this point. The input area is marked with the following indication symbol until the performance class has been selected: ![Overview](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG). |
| Time synchronization/Time | - Synchronization with an NTP server   If the drive is connected with a control system in the device configuration, option "Use PLC as NTP server" is automatically activated. If the drive is connected to a PLC, the IP address of the PLC is displayed. The following settings can be made:    - IP address (only if option "Use PLC as NTP server" is deactivated)   - Time zone of the NTP server (always) - No synchronization   In this case, no NTP synchronization is managed in the project. You can separately configure this synchronization for the drive in online mode using the Online & Diagnostics function "[Set time](#setting-the-time-of-day)". |
| Hardware settings | - Power Module settings   - Output voltage - Power Module additional data   Output filter   - Motor reactor     Motor reactors reduce the voltage stress on the motor windings and the load placed on the drive as a result of capacitive recharging currents in the cables.   - dv/dt filter      A combination of dv/dt filter and a Voltage Peak Limiter (VPL) – dv/dt filter plus VPL – is available to suppress voltage peaks.   - Sine-wave filter, third-party manufacturer     The sine-wave filter at the drive output limits the voltage rate of rise and the peak voltages at the motor winding. - Braking resistor   A braking resistor must be set if an externally connected braking resistor is to be controlled:    - "External braking resistor" for standard G220 ![Overview](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG)     The maximum braking power is a mandatory entry. The braking resistor can be destroyed if the braking power is incorrectly entered.   - "Siemens braking resistor" or "Third-party braking resistor" ![Overview](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG) for Clean Power G220     It is crucial that detailed entries are made for third-party braking resistors. Incorrect entries can destroy the braking resistor. |
| Web server | - Permit access to service interface [X127] via the HTTP protocol - Permit access to service interface [X127] via the HTTPS protocol - Enable access to the PROFINET interface [X150]. This is only possible as secure HTTPS connection.  These settings are redundant to the web server settings under "Ports and protocols". |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Damage to a sine-wave filter due to incorrect parameterization**  If a sine-wave filter is installed in your hardware configuration, the sine-wave filter can be destroyed if it is not set in the additional data of the G220 drive.   - Set the installed sine-wave filter in the "Output filter" drop-down list and add the required parameter data of the filter. |  |

###### Requirements

- A new project has been created.

  - Or -

  An existing project has been opened.
- A SINAMICS G220 drive has been created in the project.

###### Performing the quick configuration

The following steps are required for a minimal configuration:

1. Select the G220 drive in the device view and open the Inspector window.
2. Select the required performance class in the "Device selection G220 PN" detail menu.

   ![Example: G220 power unit](images/152239920395_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: G220 power unit](images/152239920395_DV_resource.Stream@PNG-en-US.PNG)

   Example: G220 power unit

   The specification of the performance class is a mandatory entry. Without a performance class, the drive is not sufficiently specified in the project and further configuration of the drive is not possible.
3. If your drive has a filter, this must also be set in the project.

   In the secondary navigation select the entry "Hardware settings". Select the filter type used in the hardware from the "Output filter" (p0230) drop-down list.

###### Performing an extended configuration

1. Select the G220 drive in the device view and open the Inspector window.
2. In the secondary navigation of the Inspector window, select the desired detail menu (see list in the overview).
3. Make the required detail settings in the white fields. Default settings are usually available in most detail menus.

   The gray fields are corrected automatically in accordance with their setting. Fields with a gray background cannot be edited directly.

###### Result

You have made the detailed settings for the drive in your device configuration.

#### Motor

This section contains information on the following topics:

- [Configuring motors with manual motor data entry](#configuring-motors-with-manual-motor-data-entry)
- [Making the detailed settings for the motor holding brake](#making-the-detailed-settings-for-the-motor-holding-brake)
- [Configuring motors from the motor list](#configuring-motors-from-the-motor-list)
- [Inserting an additional motor from the motor list](#inserting-an-additional-motor-from-the-motor-list)

##### Configuring motors with manual motor data entry

###### Overview

Startdrive manages the motor data of numerous standard motors. Motors can therefore be quickly specified via the Inspector window. If you want to manage the motors in your device configuration that are not contained in the motor list, you can acquire the most important motor data, such as the rating plate values of the motor, manually in the Inspector window. Mandatory input fields are marked in pink.

###### Requirements

- A project has been created.
- A G220 Control Unit has been inserted in the device configuration.
- The motor data from the motor rating plate are known.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

An unspecified motor placeholder is automatically present in the created G220 Control Unit. This placeholder requires manual entry of the most important motor data.

1. Click on the unspecified motor in the drive in the device view.
2. Open the Inspector window if it is not already open or displayed.
3. Select the "Motor details" entry in the secondary navigation of the Inspector window.

   The "Motor details" function view has the subareas:

   - Rating plate values

     Mandatory entry marked with ![Procedure](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG).
   - Motor brake (see "[Detailed settings...](#making-the-detailed-settings-for-the-motor-holding-brake)")
4. Acquire the required motor data of the inserted motor. You can find this data on the rating plate of the motor used.

   ![Detailed settings of the motor](images/151990254731_DV_resource.Stream@PNG-en-US.PNG)

   ![Detailed settings of the motor](images/151990254731_DV_resource.Stream@PNG-en-US.PNG)

   Detailed settings of the motor

   The input fields marked in pink are mandatory input fields. Without the appropriate values in these fields, the device configuration cannot be completed.

###### Result

The motor is specified with the manually acquired motor data. The white area turns dark gray.

###### Information on the motor standard

The representation of the motor data depends on the motor standard. The converter represents the motor data corresponding to motor standard IEC or NEMA in the following systems of units:

- SI units
- US units

It is only possible to change the motor standard during commissioning. Some examples are listed below:

| Parameter | IEC/NEMA motor standard |  |  |
| --- | --- | --- | --- |
| IEC motor  50 Hz, SI units | NEMA motor  60 Hz, US units | NEMA motor  60 Hz, SI units |  |
| [r0206](SINAMICS%20Parameter%20G220.md#r020602-rated-power-unit-power) | kW | hp | kW |
| [p0219](SINAMICS%20Parameter%20G220.md#p021901-braking-resistor-braking-power) | kW | hp | kW |
| [p0307](SINAMICS%20Parameter%20G220.md#p03070n-rated-motor-power) | kW | hp | kW |
| [p0316](SINAMICS%20Parameter%20G220.md#p03160n-motor-torque-constant) | Nm/A | lbf ft/A | Nm/A |
| [r0333](SINAMICS%20Parameter%20G220.md#r03330n-rated-motor-torque) | Nm | lbf ft | Nm |
| [p0341](SINAMICS%20Parameter%20G220.md#p03410n-motor-moment-of-inertia) | kgm<sup>2</sup> | lb ft<sup>2</sup> | kgm<sup>2</sup> |
| <sup>1)</sup> Default value |  |  |  |

###### Additional parameters

---

##### Making the detailed settings for the motor holding brake

###### Requirements

- A project has been created.
- A G220 Control Unit has been inserted in the device configuration.
- The motor has been specified.

###### Procedure

1. Select the motor in the device view and open the inspector window.
2. Select the "Motor details > Motor brake" menu in the inspector window.

   The current configuration of the motor holding brake is displayed in the function view. You can only change this configuration in the basic parameterization.

   ![Motor brake](images/151990552331_DV_resource.Stream@PNG-en-US.PNG)

   ![Motor brake](images/151990552331_DV_resource.Stream@PNG-en-US.PNG)

   Motor brake
3. To change the configuration of the motor holding brake, click the ![Procedure](images/145963165963_DV_resource.Stream@PNG-de-DE.png) icon next to the "Brake control" entry.

   The "[Brake control](Commissioning%20SINAMICS%20G220%20drives.md#brake-control)" function view opens.
4. Here you specify whether the motor holding brake is to be positively opened.
5. Then save the project to accept the settings.

###### Result

You have made the detailed settings for the selected motors in your device configuration.

##### Configuring motors from the motor list

###### Overview

When creating a G220 drive in the device configuration, a motor placeholder is generally used for manual motor data input. This placeholder is intended for third-party motors whose data is not managed in the motor list. If you want to use a standard motor from the motor list, you can replace the motor placeholder before specifying. In the same way, you can generally replace motor placeholders of one motor type with a motor placeholder of another motor type.

###### Requirements

- The drive is offline.
- A project has been created.
- A G220 Control Unit with an unspecified motor placeholder is inserted into the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Select the desired motor type in the hardware catalog and drag the corresponding placeholder in the device view onto the placeholder for the currently used motor type.

   The "Replace motor" dialog opens:

   ![Replacing the motor](images/152004482443_DV_resource.Stream@PNG-en-US.PNG)

   ![Replacing the motor](images/152004482443_DV_resource.Stream@PNG-en-US.PNG)

   Replacing the motor

   The most important data of the used motor type and the new motor type are compared in the dialog.

   If the two types of motors are not fully compatible, the corresponding information is displayed in the "Compatibility information" field.
2. To accept the new motor type, click "OK".
3. Click on the unspecified motor in the device view.
4. If required, select the "Motor - Selection" entry in the secondary navigation in the Inspector window.
5. Select your motor in the list based on the article number.

   The motor placeholder is assigned the data of the selected motor. The white area turns gray. If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

**Note**

**DRIVE-CLiQ motors**

With DRIVE-CLiQ motors, the motor and encoder data is read into the drive automatically from the hardware used when the project data is downloaded. It is not possible or necessary to specify the motor data at this point. However, for reasons of consistency, make sure that the project data is once again transferred to the Startdrive project after downloading it to the drive and reading it from the hardware (see "Downloading the configuration from the device to the project").

###### Result

The motor has been added. If you had already inserted and specified an encoder before replacing the motor, you must do this again at this point. When replacing the motor, the encoder is deleted from the device configuration, since the encoder settings always refer to the motor used.

##### Inserting an additional motor from the motor list

###### Overview

When creating a G220 drive in the device configuration, a motor placeholder is generally used for manual motor data input. This placeholder is intended for third-party motors whose data is not managed in the motor list.

In addition or as an alternative to this motor placeholder, you also can insert and specify a motor placeholder from the motor data list. Several motors in the Control Unit are usually required for a data set switchover in which different drive data sets (DDSs) also use different motor data sets (MDSs).

###### Requirements

- The drive is offline.
- A project has been created.
- The G220 Control Unit already contains a completely specified motor.

  - Or -

  The standard motor placeholder was deleted from the device configuration of the G220.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Select the desired motor type in the hardware catalog and drag the corresponding placeholder into the lower area of the Control Unit (NOT onto a possibly already existing placeholder).

   The placeholder for the unspecified motor is added.

   ![Example: Additional motor](images/165030706315_DV_resource.Stream@PNG-en-US.png)

   ![Example: Additional motor](images/165030706315_DV_resource.Stream@PNG-en-US.png)

   Example: Additional motor
2. Click on the motor placeholder that has just been inserted in the device view.
3. If required, select the "Motor - Selection" entry in the secondary navigation in the Inspector window.
4. Select your motor in the list based on the article number.

   The motor placeholder is assigned the data of the selected motor. The white area turns gray. If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

**Note**

**DRIVE-CLiQ motors**

With DRIVE-CLiQ motors, the motor and encoder data is read into the drive automatically from the hardware used when the project data is downloaded. It is not possible or necessary to specify the motor data at this point. However, for reasons of consistency, make sure that the project data is once again transferred to the Startdrive project after downloading it to the drive and reading it from the hardware (see "Downloading the configuration from the device to the project").

###### Result

The motor has been added. If more than one motor has been created in the Control Unit, an additional [drive data set](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds) in which the respective motor is integrated as an independent motor data set (MDS) also will be created automatically for each additional motor.

If you had specified a motor without an assigned encoder, you can then add and specify an additional encoder if necessary.

#### Measuring systems

This section contains information on the following topics:

- [Basics](#basics)
- [Adding an encoder](#adding-an-encoder)
- [Specifying the encoder evaluation](#specifying-the-encoder-evaluation)
- [Making detailed settings](#making-detailed-settings)
- [Encoder and Sensor Modules](#encoder-and-sensor-modules)

##### Basics

###### Overview

A distinction is made between motor encoders and machine encoders.

- Motor encoders are attached to the motor shaft so that the movement of the motor (angle of rotation, rotor position, etc.) can be measured directly. Motor encoders provide the actual speed value for the closed-loop control (speed and current control) so that the actual speed value is supplied fast enough for fast controllers. Consequently, high-quality encoders should be deployed as motor encoders.

  - Preconfigured Siemens motors have already been created with the appropriate encoder and the encoder evaluation in the device view.

    DRIVE-CLiQ motors are added together with an encoder. When you download the configuration to the drive, the drive and encoder parameters are transferred. The correct motor and encoder configuration is available offline in the project after an upload.
  - If you use measuring systems that are not listed in the hardware catalog, you must enter the parameters manually.

  The encoders configured in this way are then intended as motor encoders (measuring system 1).

  ![Motor encoder](images/145963586315_DV_resource.Stream@PNG-de-DE.png)

  Motor encoder
- Machine encoders are installed in the machine. With machine encoders, for example, you synchronize the speed of one belt with another belt or determine the position of a workpiece. Because these values do not normally need to be present in the fast speed- or current-controller cycle, even basic mounted encoders can be used.

  ![Machine encoder](images/145963748363_DV_resource.Stream@PNG-de-DE.png)

  Machine encoder

##### Adding an encoder

###### Overview

If your hardware works with encoders, you can also assign encoders to the drive in the device configuration.

You insert an encoder first as placeholder in the device view via the hardware catalog.

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- A motor has been inserted (optional).
- An Option Module "DRIVE-CLiQ" is required to connect the encoder.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Open the "Measuring systems" entry in the hardware catalog. The following entries are displayed:

   - "DRIVE-CLiQ encoder"
   - "SIN/COS encoder"
   - "SSI encoder"
   - "SIN/COS + SSI encoder"
   - "HTL/TTL encoder"
   - "HTL/TTL + SSI encoder"
   - "EnDat + SIN/COS encoder"
2. Drag the unspecified encoder into the light gray frame area of the Control Unit in the device view. An encoder and a Sensor Module are created.

   ![Inserting an encoder](images/153841485963_DV_resource.Stream@PNG-en-US.png)

   ![Inserting an encoder](images/153841485963_DV_resource.Stream@PNG-en-US.png)

   Inserting an encoder

   The encoder requires a DRIVE-CLiQ option module for the connection. If a DRIVE-CLiQ option module was already available, a DRIVE-CLiQ connection from the encoder to a free interface on the DRIVE-CLiQ module is automatically established when the encoder placeholder is inserted. If there is still no corresponding option module, it is automatically created in the drive together with the encoder is and a connection established.
3. Click the unspecified encoder in the device view.

   ![Specifying the encoder](images/153845591947_DV_resource.Stream@PNG-en-US.PNG)

   ![Specifying the encoder](images/153845591947_DV_resource.Stream@PNG-en-US.PNG)

   Specifying the encoder
4. In the secondary navigation of the Inspector window, select the "Measuring system - Selection..." entry.

   As long as no encoder is selected, this mandatory entry is marked with the symbol ![Procedure](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG).
5. Select the desired encoder in the measuring system list based on the article number.

   The data of the selected encoder is assigned to the encoder placeholder. The white area turns gray.

   A Sensor Module (encoder evaluation) is also inserted. If only one Sensor Module is available for this encoder type, it is already inserted specified. Otherwise, you must also specify the Sensor Module (see "[Specifying the encoder evaluation](#specifying-the-encoder-evaluation)").

**Note**

The number of selectable entries depends on the drive unit type (see "[Available components](#available-components)").

**Note**

The number of option modules that can be used is limited. The Control Unit indicates in the device configuration whether further modules can be inserted.

###### Result

The encoder has been inserted and specified. You can also insert several encoders in parallel.

If you require further encoders for your task, configure them in the same manner. These encoders are then normally used as machine encoder. Since only 2 free interfaces are available in the Option Module "DRIVE-CLiQ", subsequently inserted additional encoders are not usually automatically wired.

An encoder data set (EDS) is automatically created for each of the first three encoders inserted; you can assign these to selected [drive data sets](#overview-4) as motor encoders or external encoders if required.

###### Handling DRIVE-CLiQ encoders

The process is slightly different from the standard procedure for DRIVE-CLiQ encoders. Two different versions are possible:

- If DRIVE-CLiQ motors are included in the device view, DRIVE-CLiQ encoders are added automatically. Motor and encoder **cannot** be specified in Startdrive in this case. The project data is downloaded to the drive instead, and the motor and encoder detail data is then read from the hardware.
- If non-DRIVE-CLiQ motors are used in the device view, you can still add DRIVE-CLiQ encoders later. The DRIVE-CLiQ encoders can be specified in Startdrive in this case.

##### Specifying the encoder evaluation

###### Requirements

- An encoder has been specified.
- The unspecified encoder evaluation is displayed.

  > **Note**
  >
  > Depending on the encoder it is possible that the encoder evaluation has already been preselected. In this case, using the appropriate selection option, you can also define other encoder evaluation types.

###### Procedure

Various Sensor Modules are available for the encoder evaluation. Different types are offered for selection depending on the encoder.

> **Note**
>
> Detailed information on the combination of encoders and Sensor Modules is available here: "[Encoder and Sensor Modules](#encoder-and-sensor-modules)".
>
> A description of all encoder types that can be used in Startdrive can be found here: "[Encoder descriptions](#encoder-descriptions)".

1. Click the unspecified encoder evaluation. The available Sensor Modules are displayed.

   ![Specifying the encoder evaluation](images/153846386443_DV_resource.Stream@PNG-en-US.PNG)

   ![Specifying the encoder evaluation](images/153846386443_DV_resource.Stream@PNG-en-US.PNG)

   Specifying the encoder evaluation

   As long as no Sensor Module is selected, this mandatory entry is marked with the symbol ![Procedure](images/146582751627_DV_resource.Stream@PNG-de-DE.PNG). The symbol only appears if no other Sensor Module has been assigned before.
2. Select your Sensor Module.

###### Result

The Sensor Module has been specified.

##### Making detailed settings

###### Overview

You can configure the following encoder details for measuring systems during commissioning:

- Actual value processing
- Encoder details such as encoder type, incremental track, gear ratio, etc.

###### Procedure

1. Select the encoder in the device view and open the inspector window.
2. Select the "Measuring system details" menu in the inspector window.
3. To configure the actual value processing, click the ![Procedure](images/145963165963_DV_resource.Stream@PNG-de-DE.png) icon next to the "Actual value processing" entry.

   The "Actual value processing" function view opens.

   Make the required settings here (see "[Basic parameterization](Commissioning%20SINAMICS%20G220%20drives.md#encoder-evaluation)").
4. If you have inserted several encoders, then you can change the default assignment of the motor encoder in the drive data set.

   Click on icon ![Procedure](images/145963165963_DV_resource.Stream@PNG-de-DE.png) next to entry "[Motor encoder assignment](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds)". Then set a different encoder as motor encoder in the drive data set.
5. Select the "Measuring system details" menu again in the inspector window.

   The setting options depend on the selected encoder type.
6. Make the required [Detailed settings of the encoder](#overview-5) in the white fields.

   The gray fields are corrected automatically in accordance with their setting.
7. You make additional detailed settings in the basic parameterization via the [Encoder evaluation](#specifying-the-encoder-evaluation).

   - In the work area, select menu "Basic parameterization > Encoder evaluation".
   - Select the encoder usage type, and then make the appropriate basic settings for this.

###### Result

You have made the detailed settings for the selected encoder in your device configuration.

##### Encoder and Sensor Modules

This section contains information on the following topics:

- [Encoder system connection](#encoder-system-connection)
- [Encoder descriptions](#encoder-descriptions)

###### Encoder system connection

###### Overview

The Sensor Modules evaluate the signals from the connected motor encoders or external encoders and convert the signals so that they can be evaluated by the Control Unit. The encoder system can only be connected to SINAMICS via DRIVE-CLiQ. The following rule applies: Motor encoders are connected to the associated Motor Module, external encoders are connected to the Control Unit. In conjunction with motor encoders, the motor temperature can also be evaluated using Sensor Modules.

Sensor Modules Cabinet (SMC) are intended for internal cabinet installation.

**Assignment of measuring system to Sensor Modules**

| Measuring systems | SMC20 | SMC30 |
| --- | --- | --- |
| Sin/Cos incremental encoder (1 Vpp)  with zero pulse | Yes | - |
| SSI absolute encoder  (with incremental tracks sin/cos 1 Vpp) | Yes | - |
| TTL/HTL incremental encoder | - | Yes |
| EnDat absolute encoder  (with incremental track 1 Vpp) | Yes | - |
| Temperature evaluation | Yes | Yes |

###### SMC20

The Sensor Module Cabinet-Mounted 20 (SMC20) evaluates encoder signals and transmits the speed, actual position value, rotor position and the home position via DRIVE-CLiQ to the Control Unit.

The encoders that can be connected are incremental encoders SIN/COS (1 Vpp) and absolute encoders EnDat/SSI with SIN/COS (1 Vpp).

![SMC20 interfaces](images/145964306955_DV_resource.Stream@PNG-en-US.png)

SMC20 interfaces

###### SMC30

The Sensor Module Cabinet-Mounted 30 (SMC30) evaluates encoder signals and transmits the speed, actual position value, rotor position and the home position via DRIVE-CLiQ to the Control Unit.

The encoders that can be connected are TTL/HTL square-wave encoders and SSI absolute encoders.

![SMC30 interfaces](images/145964395403_DV_resource.Stream@PNG-en-US.png)

SMC30 interfaces

###### Encoder descriptions

This section contains information on the following topics:

- [Overview](#overview-5)
- [SIN/COS incremental encoders](#sincos-incremental-encoders)
- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [SSI encoder](#ssi-encoder)
- [EnDat encoder](#endat-encoder)
- [Distance-coded zero marks](#distance-coded-zero-marks)

###### Overview

###### Available measuring systems (encoders)

The following encoder types are supported in Startdrive:

- DRIVE-CLiQ encoders

  These encoders are parameterized during a download and correctly displayed and after an upload.
- [SIN/COS encoders](#sincos-incremental-encoders)

  These incremental encoders supply a sine/cosine shaped signal.
- [SSI encoders](#ssi-encoder)

  These absolute encoders are controlled via the SSI protocol.
- [HTL/TTL encoders](#ttlhtl-incremental-encoder)

  These incremental encoders supply a square-wave signal and are also available with the SSI protocol.
- [EnDat](#endat-encoder)

  These absolute encoders are controlled via the EnDat 2.1 protocol.

###### Which changes are possible?

- All encoders that are listed in the hardware catalog, must no longer/can no longer be parameterized as the appropriate settings have already been preassigned and are write protected. The corresponding text boxes are visibly grayed out.
- For all user-defined encoders (third-party encoders), the parameters must be entered, as subsequently described. The text boxes are white, and can be edited.
- A few settings can also be corrected for listed encoders (e.g. gear ratio/measuring gearbox). These settings can be identified as they are shown in white.
- All settings in the "Parameterization" area that are linked to can be made in the same fashion for listed and user-defined encoders. This especially refers to the "Actual value processing" and the "Motor encoder assignment".

###### SIN/COS incremental encoders

###### Overview

Incremental encoders operate on the principle of optoelectronic scanning of dividing discs with the transmitted-light method. The light source is a light emitting diode (LED). The light-dark modulation generated as the encoder shaft rotates is picked up by photoelectronic elements. With an appropriate arrangement of the line pattern on the dividing disk connected to the shaft and the fixed aperture, the photoelectronic elements provide two trace signals A and B at 90° to one another, as well as a homing signal R. The encoder electronics amplify these signals and convert them to sin/cos 1 Vpp.

After a machine is switched on, a home position approach must be carried out to determine the absolute position.

**SIN/COS encoder operation**

![Sin/cos incremental encoders](images/145964876043_DV_resource.Stream@PNG-en-US.png)

Sin/cos incremental encoders

###### Settings

You can make the following settings for the encoder type:

| Settings | Explanation |
| --- | --- |
| Sin/Cos encoder type | The following general parameters can be selected for the "Sin/Cos" encoder type:  - Motor encoder assignment   Encoders are used in a drive according to the following rule: The first-entered encoder is used as the motor encoder. All additional encoders are used as external encoders (in the sequence that they are inserted). You can change this default assignment using the configuration of a drive data set. For example, this is how you define another motor encoder. By clicking on icon ![Settings](images/145963165963_DV_resource.Stream@PNG-de-DE.png), you go directly to the [configuration of the drive data sets](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds). - rotary   Select this option when a rotary encoder is available. - linear   Select this option when a linear scale is available. |
| Incremental tracks | This field is already preassigned for most encoders. The number of pulses per revolution can also be specified in bits in the encoder data sheets. Encoder pulse number = 2<sup>resolution</sup>. The resolution is contained in the bit.   Enter the number of pulses per revolution for your encoder. |
| Coarse synchronization | You use coarse synchronization to define how the pole position identification is to be carried out. The following options are available:   - Track C/D The flux position can be determined using the C/D track and the zero mark, which is adjusted to the magnetic position of the rotor. As the C/D track only has one encoder pulse per mechanical revolution, the accuracy of this determination method is only adequate for starting. Therefore, you must carry out another fine synchronization. - Hall sensor (only for linear motors) Hall sensors are used that measure the magnetic flux in the air gap. Two sensors are used, which supply information equivalent to a C/D track. - None |
| Zero marks | Zero marks serve as homing signal for incremental encoders. Select the appropriate zero signal for your encoder:  - No zero mark - Equidistant zero marks (evaluate several zero marks):   - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".   - At "Number of zero marks", enter how many zero marks you want to evaluate. - Irregular zero marks:  Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible. - [Distance-coded zero marks](#distance-coded-zero-marks) |
| Gear ratio/measuring gearbox | Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G220.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G220.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.  This information is contained in the motor data sheet. |

###### Additional parameters

---

###### TTL/HTL incremental encoder

###### Overview

These encoders operate analogously to the SIN/COS incremental encoders, although they supply a different output level. They are also referred to as pulse or square-wave encoders. The signals are quadrupled by an edge evaluation.

- HTL (High Threshold Logic); in unipolar design can be connected to the SMC30.
- RS 422 difference signals (TTL = Transistor Transistor Logic); in bipolar design can be connected to the SMC30.
- The resolution can be improved by a factor of four for TTL and HTL encoders through edge evaluation.
- TTL/HTL encoders are offered in the Startdrive with and without SSI protocol.

> **Note**
>
> **Using the SSI protocol**
>
> You can find information about the SSI protocol at [SSI encoder](#ssi-encoder).

**TTL/HTL encoder mode of operation**

![TTL pulse encoder](images/145964864395_DV_resource.Stream@PNG-en-US.png)

TTL pulse encoder

After the signal edges of tracks A and B have been evaluated, direction-dependent speed and position information is available.

###### Settings

You can make the following settings for the encoder type:

| Settings | Explanation |
| --- | --- |
| Absolute position | After switching on the machine, the absolute dimensional reference for the machine zero must be established with pulse encoders for positioning. Therefore, perform a home position approach. After homing, the absolute position is determined by adding up the individual incremental signals. |
| HTL/TTL encoder type | The following main settings can be made for the "HTL/TTL" encoder type:   - Motor encoder assignment   Encoders are used in a drive according to the following rule: The first-entered encoder is used as the motor encoder. All additional encoders are used as external encoders (in the sequence that they are inserted). You can change this default assignment using the configuration of a drive data set. For example, this is how you define another motor encoder. By clicking on icon ![Settings](images/145963165963_DV_resource.Stream@PNG-de-DE.png), you go directly to the [configuration of the drive data sets](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds). - rotary   Select this option when a rotary encoder is available. - linear   Select this option when a linear scale is available. |
| Power supply | The following settings are available for setting the power supply of your encoder:   - 5 V - 24 V - Remote sense;  Remote sensing ensures that a possible voltage drop along the cable is compensated. |
| Incremental tracks | The resolution of the encoder is determined by its "number of pulses". This value is located on the encoder rating plate and in the associated data sheet.  - Pulse number/rotation Enter the pulse number for the encoder. - Level Select whether you use an HTL (High Threshold Logic) or a TTL (Transistor-Transistor Logic) encoder. - Signal Select whether the encoder transfers a unipolar (ground-based) or a bipolar (differential) signal. Unipolar signals lie in the range of 0 ... 5 V. Bipolar signals lie in the range of -5 ... 5 V. - Track monitoring Activate this option if you want to monitor the incremental track. This can be used, for example, to monitor for wire break. If the track monitoring is selected, the signal must not be unipolar. |
| Zero marks ([p0404](SINAMICS%20Parameter%20G220.md#p04040n023-encoder-configuration-effective)) | Zero marks serve as homing signal for incremental encoders. Select the appropriate zero signal for your encoder:  - No zero mark - Equidistant zero marks (evaluate several zero marks)   - The number of pulses between the two equidistant zero marks are displayed at "Zero mark distance".   - At "Number of zero marks", enter how many zero marks you want to evaluate. - Irregular zero marks   Select this option if you do not want to evaluate the zero marks at each revolution, i.e. you want to evaluate them irregularly. - [Distance-coded zero marks](#distance-coded-zero-marks) |
| Gear ratio/measuring gearbox | Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G220.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G220.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.  This information is contained in the motor data sheet. |

###### Additional parameters

---

###### SSI encoder

###### Overview

SSI encoders use the SSI protocol for the data transfer. The SSI protocol is a serial data transfer between an encoder and an evaluation module.

> **Note**
>
> **Data sheet of the encoder being used**
>
> To parameterize the SSI protocol, it is absolutely necessary that you have the encoder data sheet at hand. Use the information in the data sheet to set the protocol parameters. Not all encoders support the parameterizable functions.

**Structure of an SSI protocol**

The SSI connection between the encoder and the encoder module is established using four wires. This is a serial transmission.

The data transmission with the SSI protocol is performed in just one direction, i.e. the data is transferred from the encoder to the evaluation module. The data is a position value for a rotary or linear measuring system and, possibly, further bits that describe the position value.

The structure of the telegram differs depending on the encoder manufacturer and the measuring system. Consequently, you must use the information provided by the manufacturer that describes the protocol structure in detail. Manufacturers frequently extend the position value and leading and trailing zero bits to produce a telegram length of 13, 21 or 25 bits. Whereby this information is extended to 9 bits for a telegram of 21 bits or to 12 bits for a telegram of 25 bits. In the meantime, however, any telegram length is common. In the following example, 29-bit position data is transferred and expanded with three bits before and after the position.

| Bits before position |  |  | Position bits |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Bits after position |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x | x | x | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | x | x | x |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| P indicates the position bits; x indicates the possible position of fault, alarm and parity bits. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

###### Settings

You can make the following settings for the encoder type:

| Settings | Explanation |
| --- | --- |
| Encoder type SSI | The following main settings can be made for the "SSI" encoder type:   - Motor encoder assignment   Encoders are used in a drive according to the following rule: The first-entered encoder is used as the motor encoder. All additional encoders are used as external encoders (in the sequence that they are inserted). You can change this default assignment using the configuration of a drive data set. For example, this is how you define another motor encoder. By clicking on icon ![Settings](images/145963165963_DV_resource.Stream@PNG-de-DE.png), you go directly to the [configuration of the drive data sets](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds). - Rotary   Select this option when a rotary encoder is available. - Linear   Select this option when a linear scale is available. |
| Power supply | The following settings are available for setting the power supply of your encoder:  - 5 V - 24 V - Remote sense;  Remote sensing ensures that a possible voltage drop along the cable is compensated. |
| Resolution | Enter the resolution. |
| Absolute protocol | You can select one of the following protocols:   - Multiturn   - Select in the drop-down list whether your encoder is multiturn-capable. - Singleturn resolution ([p0423](SINAMICS%20Parameter%20G220.md#p04230n-absolute-encoder-rotary-singleturn-resolution))   Singleturn encoders divide one rotation (360 degrees mechanical) into a specific number of encoder pulses, e.g. 8192. A unique code word is assigned to each position. After 360° the position values are repeated.   - Enter the singleturn resolution based on your encoder data sheet. - Multiturn resolution ([p0421](SINAMICS%20Parameter%20G220.md#p04210n-absolute-encoder-rotary-multiturn-resolution))   Multiturn encoders also record the number of revolutions, in addition to the absolute position within one revolution. To do this, further code disks which are coupled via gear steps with the encoder shaft are scanned. When evaluating 12 additional tracks, this means that an additional 4096 revolutions can be coded.   - Enter the multiturn resolution based on your encoder data sheet. |
| SSI protocol | **SSS protocol parameters**   - Code ([p0429](SINAMICS%20Parameter%20G220.md#p04290n06-encoder-ssi-configuration))   - Gray code; special coding of transfer signals; when transitioning from one position to another, only one bit is always changed.   - Binary code; binary-coded transfer signals - Baud rate ([p0427](SINAMICS%20Parameter%20G220.md#p04270n-encoder-ssi-baud-rate))   When setting the baud rate, also take into account the update rate of the speed or actual position value. All bits must be transferred within the cycle, as otherwise the data transfer is too slow and only performed every xth cycle. If you are using an SSI encoder with incremental track, the incremental track is used for the speed control.    **Example**: For a baud rate of 100 kHz and an SSI length of 35 bits, 10x35 µs = 350 µs + 30 µs monoflop time = 380 µs are required to transfer the SSI value. If the current controller cycle is faster, you must set a higher baud rate.   The possible baud rate depends on the cable length (see the diagram).        ![SSI baud rate](images/145964935435_DV_resource.Stream@PNG-en-US.png)    SSI baud rate   Here, enter the baud rate for the SSI encoder. - Parameterizing the protocol   - Position length in bits ([p0447](SINAMICS%20Parameter%20G220.md#p04470n-encoder-ssi-number-of-bits-absolute-value))   - Bits before position ([p0446](SINAMICS%20Parameter%20G220.md#p04460n-encoder-ssi-number-of-bits-before-the-absolute-value))   - Bits after position ([p0448](SINAMICS%20Parameter%20G220.md#p04480n-encoder-ssi-number-of-bits-after-the-absolute-value))Refer to the encoder data sheet to identify which value is suitable for your encoder. For a singleturn encoder, for example, 13 bits are used for the position information, and 25 bits for a multiturn encoder (this contains 13 bits of singleturn information).    **Bit functions in the SSI protocol**   If alarm bits, error bits or parity bits signal errors when transferring data, in Startdrive, alarms or faults are output in the inspector window.  - Alarm bit   If the encoder manufacturer has added alarm bits to the position value, you should certainly evaluate these because they provide the only possibility to output alarms regarding the position value. For example, the encoder may be soiled.    The alarm bit triggers an alarm on the SINAMICS device (A3x412, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).   - At "Bit activation", activate the alarm bit.   - At "Bit position", enter the position of the bit in the SSI protocol.   - At "Logical state", select at which level (high active or low active) the alarm bit should be output. High active means that the corresponding alarm is displayed on the SINAMICS when the bit is set. - Error bits   If the encoder manufacturer has added error bits to the position value, you must also evaluate them because they allow you to determine the validity of the position value.    Error bits trigger a fault on the SINAMICS device (F3x112, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).   - At "Bit activation", select the bit number for the error bit. You can parameterize several error bits (see online help online help for parameters).   - At "Bit position", enter the position of the bit in the SSI protocol.   - At "Logical state", select at which level (high active or low active) the error bit should be output. High active means that the corresponding fault is displayed on the SINAMICS when the bit is set. - Parity bit   Another possibility to validate the transmission is to transfer a parity bit in the telegram. This is a parity check for all of the bits of the telegram content. The following settings apply for the parity: even (= low level) and odd (= high level). Refer to the data sheet to see whether the encoder uses "even" or "odd" as checking criterion for the parity bit.    Example for "even" parity:   The number of bits filled with 1 in the telegram must always be even. An odd number of set bits is compensated by the parity bit. If an uneven number of set bits is nevertheless determined in the evaluation module, a fault is output on the SINAMICS side (F3x110 Bit 11, with x=1,2,3 for encoder 1, 2, 3).   For "uneven" parity, the inverse logic applies accordingly.   - At "Bit activation", select the bit number for the parity bit.   - At "Bit position", enter the position of the bit in the SSI protocol.   - Under "Logic state", select whether the parity bit has even or odd logic.Example telegram       ![SSI encoder example telegram](images/145964899339_DV_resource.Stream@PNG-en-US.png)    SSI encoder example telegram - Monoflop time   The monoflop time describes the minimum wait time between two transfers of the absolute value for the SSI encoder. The set value must be greater than or equal to the value specified in the data sheet for the encoder.    - Enter the monoflop time. - Transfer position value twice   Some manufacturers allow a position value to be transferred twice; this is called "ring shift" or "fetch doubled". It detects transmission errors, although it extends the time taken to transfer the position value. At least one fill bit is necessary between reading out the first time and second time. You can also refer to the encoder data sheet for the number of fill bits. The following example shows the use of fill bits:       ![SSI encoder position value](images/145964910987_DV_resource.Stream@PNG-en-US.png)    SSI encoder position value   - Select "Double transfer" and enter a value for the fill bits ([p0449](SINAMICS%20Parameter%20G220.md#p04490n-encoder-ssi-number-of-bits-filler-bits)). |
| Gear ratio/measuring gearbox | Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G220.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G220.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.  This information is contained in the motor data sheet. |

###### Additional parameters

---

###### EnDat encoder

###### Overview

Absolute encoders (absolute shaft encoders) are designed on the same scanning principle as incremental encoders, but have a greater number of tracks. For example, if there are 13 tracks, then 2<sup>13</sup> = 8192 steps are coded for singleturn encoders. The code used is a one-step code (Gray code) which prevents any scanning errors from occurring. After switching on the machine, the position value is transferred immediately to the evaluation module. Data is transferred between the encoder and the evaluation module via EnDat.

A home position approach is omitted; however, an absolute encoder adjustment must be performed during the first commissioning with a higher-level controller.

**EnDat encoder mode of operation**

![EnDat absolute encoder](images/145964430347_DV_resource.Stream@PNG-en-US.png)

EnDat absolute encoder

###### Settings

You can make the following settings for the encoder type:

| Settings | Explanation |
| --- | --- |
| Identify encoder | Select the option if you want to fetch the encoder configuration from the encoder (only online). |
| Incremental tracks | The parameters for the number of pulses/revolution are transferred over the course of the encoder identification. |
| Gear ratio/measuring gearbox | Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G220.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G220.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.  This information is contained in the motor data sheet. |

###### Additional parameters

---

---

**See also**

[Managing a drive data set (DDS)](Commissioning%20SINAMICS%20G220%20drives.md#managing-a-drive-data-set-dds)

###### Distance-coded zero marks

###### Description

Distance-coded measuring systems are the system of choice where travel to a (possibly distant) home position is not possible for mechanical reasons. The absolute position can be calculated as soon as two zero marks have been crossed.

The principle of distance coding is based on differing distances between zero marks, which change in a defined manner (see figure below).

- After measurement has been switched on, the axis is in a non-homed state. An absolute position is NOT available.
- The absolute position can be calculated by traveling over at least two adjacent zero marks.
- The distance traveled is relatively small in this method and is defined by the distance between the zero marks.

The distance-coded zero marks are evaluated:

- after measurement has been switched on and the travel movement described has been completed to determine the machine position
- cyclically to compare and monitor the incremental zero marks against the distance-coded zero marks.

The following figure illustrates the distance-coded zero marks for a linear traversing motion.

![Linear traversing motion with distance-coded zero mark](images/145964958091_DV_resource.Stream@PNG-de-DE.png)

Linear traversing motion with distance-coded zero mark

The following figure illustrates the distance-coded zero marks for a rotary motion.

![Rotary traversing motion with distance-coded zero mark](images/145965234315_DV_resource.Stream@PNG-de-DE.png)

Rotary traversing motion with distance-coded zero mark

###### Additional parameters

- [p0404](SINAMICS%20Parameter%20G220.md#p04040n023-encoder-configuration-effective).14
- p0424
- [p0425](SINAMICS%20Parameter%20G220.md#p04250n-encoder-rotary-zero-mark-distance)
- [p0426](SINAMICS%20Parameter%20G220.md#p04260n-encoder-zero-mark-differential-distance)

---

#### Supplementary system components

This section contains information on the following topics:

- [Overview](#overview-6)
- [Adding a DRIVE-CLiQ option module](#adding-a-drive-cliq-option-module)
- [Adding an SMT option module](#adding-an-smt-option-module)
- [Adding an IIoT option module](#adding-an-iiot-option-module)

##### Overview

You can supplement the G220 Control Unit with the following Option Modules:

- Option Modules (OM)

  - Option Module [DRIVE-CLiQ](#adding-a-drive-cliq-option-module)
  - Option Module [SMT](#adding-an-smt-option-module)
  - Option Module [IIoT](#adding-an-iiot-option-module)

However, the maximum number of modules usable in a G220 Control Unit is technically limited. Whether additional Option Modules can be added is optically indicated in the device configuration.

In general, a maximum of 5 slots are available for option modules. Each option module requires at least 2 slots (in exceptional cases 3 slots) for connection to the Control Unit.

With the aid of a DRIVE-CLiQ expansion adapter, 10 additional slots are available for further option modules.

###### Rules

The following rules apply to the insertion of modules:

- Only one module of one type can be inserted at a time; e.g. only one option module DRIVE-CLiQ or only one option module SMT.
- 2 or 3 option modules can be inserted via the standard slots.
- DRIVE-CLiQ expansion adapter: A maximum of 5 additional option modules can be inserted.

###### More information

More detailed information on installation, interfaces and technical data of the option modules is provided in the "[SINAMICS G220 converter](https://support.industry.siemens.com/cs/ww/en/ps/13204)" operating instructions.

##### Adding a DRIVE-CLiQ option module

###### Overview

A DRIVE-CLiQ option module extends the Control Unit of a G220 converter to include 2 additional DRIVE-CLiQ interfaces. For G220 converters, this DRIVE-CLiQ option module is plugged into the Control Unit. It does not have to be specified any further. Only one DRIVE-CLiQ option module can be used per converter.

DRIVE-CLiQ option modules are automatically created when encoders or Terminal Modules are inserted if they were not already present in the Control Unit. If any free DQ interfaces are available, the DQ interfaces will automatically be interconnected here.

###### Requirements

- A project has been created and opened.
- A G220 Control Unit has been inserted in the device configuration.
- There are free slots for option modules on the Control Unit (visible white bar).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Open the "Option Modules" entry in the hardware catalog.
2. Drag the DRIVE-CLiQ option module into the light gray framed area of the Control Unit in the device view.

   ![DRIVE-CLiQ option module](images/165030310667_DV_resource.Stream@PNG-en-US.png)

   ![DRIVE-CLiQ option module](images/165030310667_DV_resource.Stream@PNG-en-US.png)

   DRIVE-CLiQ option module

###### Result

The DRIVE-CLiQ option module is added to the Control Unit and internally connected.

You can connect the free DQ interfaces of the module to other modules; e.g. encoder:

![Inserting a DRIVE-CLiQ option module](images/165030314635_DV_resource.Stream@PNG-en-US.png)

Inserting a DRIVE-CLiQ option module

Now continue with the configuration or parameterization.

##### Adding an SMT option module

###### Overview

An SMT option module is required for the safe motor temperature monitoring of the converter. If you want to use the Safety Integrated Function SMT concerned, you first must extend the Control Unit of the converter with an SMT option module. This module does not have to be specified any further. Only one SMT option module can be used per converter.

###### Requirements

- A project has been created and opened.
- A G220 Control Unit has been inserted in the device configuration.
- There are free slots for option modules on the Control Unit (visible white bar).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Open the "Option Modules" entry in the hardware catalog.
2. Drag the SMT option module into the light gray framed area of the Control Unit in the device view.

###### Result

The SMT option module is added to the Control Unit. The module is internally connected to the Control Unit. A DRIVE-CLiQ connection is not planned.

![SMT option module](images/171771587595_DV_resource.Stream@PNG-de-DE.png)

SMT option module

The properties of this module are displayed in the Inspector window. Now continue with the configuration or parameterization.

---

**See also**

[Using SMT](Commissioning%20SINAMICS%20G220%20drives.md#using-smt)

##### Adding an IIoT option module

###### Overview

Using an IIoT option module (IIoT = Industrial Internet of Things), your drive data can be read out, analyzed and linked with other data sources (IoT-Gateway).

In the device configuration, you can extend your drive to include this IIoT option module. Only one IIoT option module can be used per drive.

###### Requirements

- A project has been created and opened.
- A G220 Control Unit has been inserted in the device configuration.
- There are free slots for option modules on the Control Unit (visible white bar).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Open the "Option Modules" entry in the hardware catalog.
2. Drag the IIoT option module into the light gray framed area of the Control Unit in the device view.

   ![Example: Option Module IIoT](images/153857538827_DV_resource.Stream@PNG-en-US.png)

   ![Example: Option Module IIoT](images/153857538827_DV_resource.Stream@PNG-en-US.png)

   Example: Option Module IIoT
3. Check the detailed settings of the IIoT option module in the inspector window and correct the Ethernet address and the data traffic if necessary.

   However, an IIoT option module does not need to be specified.

###### Result

The IIoT option module is added to the Control Unit. The module is internally connected to the Control Unit. A DRIVE-CLiQ connection is not planned.

The properties of this module are displayed in the Inspector window. Then perform detailed settings for the Option Module.

###### Performing detailed settings for the Option Module

In addition to general project information, in the option module properties you can configure the port addresses and the data transfer for IIoT.

1. Select the IIoT option module in the device view and open the inspector window.
2. In the Inspector window, select menu "Port addresses [X128] > Port addresses".
3. Here, you specify whether the IP address should be defined in the project or via a DHCP server.

   Only one of the two options is possible.
4. Then make the detailed settings for the IP address.

   The corresponding text boxes are active.
5. In the Inspector window, select menu "Port addresses [X128] > Configure data transfer".
6. Here, activate the required data transfer for the IIoT option module.

   The following are possible:

   - Data transfer to an Edge device can be activated
   - SFTP access for a firmware update can be activated

#### Optional: Control

This section contains information on the following topics:

- [Adding a controller (PLC)](#adding-a-controller-plc)
- [Networking the controller (PLC) and drive](#networking-the-controller-plc-and-drive)
- [Inserting a technology object into the SIMATIC S7 controller](#inserting-a-technology-object-into-the-simatic-s7-controller)
- [Interconnecting the technology object and SINAMICS drive](#interconnecting-the-technology-object-and-sinamics-drive)

##### Adding a controller (PLC)

###### Overview

If, in addition to the SINAMICS drive, you also want to use a controller in the device configuration, you must create a corresponding PLC in your project.

###### Requirements

- A new project has been created.

  - Or -

  An existing project has been opened.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To insert drive units in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click on "Controller" to display the list of available controllers.
3. Select the required PLC from the "SIMATIC S7-XXXX" list.
4. Select the firmware version of the PLC that you are using.

   If the version numbers (compare: hardware to software) do not match, then it will not be possible to subsequently go online. When creating, the current firmware version is always suggested. If required, you can change the version number using the "Version" drop-down list.
5. Enter a device name in the field at the top with the same name and then click on "OK".

   If the CPU of the PLC to be added supports secure PG/HMI communication, the wizard for security settings "PLC security settings" starts. The wizard guides you step by step through the following CPU settings:

   - Password to protect confidential PLC configuration data
   - PG/PC and HMI communication mode
   - Access level

   Make the necessary settings here (see [Protection & Security](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#using-the-security-settings-wizard-s7-1200)).

**Variant: Inserting a device via the network view or topology view**

1. Open the network view or the topology view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in the entry "SIMATIC S7-XXXX".
4. Drag-and-drop the PLC from the hardware catalog to the network view or topology view.

   If the CPU of the PLC to be added supports secure PG/HMI communication, the wizard for security settings "PLC security settings" starts.

   Make the necessary settings here (see [Protection & Security](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#using-the-security-settings-wizard-s7-1200)).

###### Result

The controller is inserted.

![Example: Inserting a PLC](images/144113011979_DV_resource.Stream@PNG-en-US.PNG)

Example: Inserting a PLC

In the network view and in the topology view, you must then [network](#networking-the-controller-plc-and-drive) the SINAMICS drive with the control system.

##### Networking the controller (PLC) and drive

###### Overview

If you have created a controller and a SINAMICS drive in your project, you have to connect these two components to each other. You need to network the components both in the network view and in the topology view.

###### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

Proceed as follows to establish the connection between the controller and the SINAMICS drive:

1. To open the network view, double-click the "Devices & Networks" entry in the project tree.

   The network view opens.
2. Draw a connection between the PROFINET interface of the controller and PROFINET interface X150 of the drive by pressing and holding the mouse button.

   ![PLC networked with the drive](images/144089379083_DV_resource.Stream@PNG-en-US.PNG)

   ![PLC networked with the drive](images/144089379083_DV_resource.Stream@PNG-en-US.PNG)

   PLC networked with the drive

   The PROFINET connection is established, and the converter is assigned to the controller.
3. Click on PROFINET interface_1 [X1] of the controller.
4. In the secondary navigation under "Advanced options" and then under "Real time settings", double-click the setting "Synchronization".

   The "Synchronization" display area appears.
5. Select the "Sync master" setting from the "Synchronization role" drop-down list.
6. Switch to the topology view.
7. Draw a connection between Port_1 [X1.P1] of the controller and Port_1 [X150.P1] of the drive.

###### Result

The controller and the SINAMICS drive are networked with one another in the network and topology views.

##### Inserting a technology object into the SIMATIC S7 controller

###### Overview

Through the technology object, Motion Control functions such as positioning and synchronous axes are available to you. For this reason, insert a new technology object (TO) in the SIMATIC S7 controller. In the "Configuration" function view, you can directly assign the inserted SINAMICS drive and go to the drive configuration.

The most common application for SINAMICS drives is positioning. To be able to perform positioning tasks in the SIMATIC S7 controller, you need to insert the Motion Control function "TO_PositioningAxis". Inserting a TO is described below based on the example of the Motion Control function "TO_PositioningAxis".

###### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created and is networked with the drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To insert a technology object into the SIMATIC S7 controller, proceed as follows:

1. Make sure that the list with available functions for the SIMATIC S7 controller in the project tree is expanded.

   ![Inserting a technology object](images/149078512907_DV_resource.Stream@PNG-en-US.png)

   ![Inserting a technology object](images/149078512907_DV_resource.Stream@PNG-en-US.png)

   Inserting a technology object
2. Expand the "Technology objects" entry.
3. Double-click the "Add new object" entry.

   The corresponding dialog opens.

   ![Dialog: Add new object](images/149074773771_DV_resource.Stream@PNG-en-US.PNG)

   ![Dialog: Add new object](images/149074773771_DV_resource.Stream@PNG-en-US.PNG)

   Dialog: Add new object
4. Click the "Motion Control" button to show the available technology objects.
5. Select the "TO_PositioningAxis" object from the "Motion Control" list.
6. If necessary, assign a different name for the TO in the input field "Name".
7. Click "OK".

###### Result

The "TO_PositioningAxis" technology object has been inserted and can be configured.

##### Interconnecting the technology object and SINAMICS drive

###### Overview

The inserted technology object "TO_PositioningAxis" must be interconnected with the SINAMICS drive.

###### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created and is networked with the drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. In the project tree, double-click the "Configuration" entry under the created technology object.

   The "Basic parameters" function view opens.
2. Select the entry "Hardware interface" in the secondary navigation.

   The corresponding function view opens.
3. Open the selection list in the "Drive" selection box.

   A selection list opens.

   ![Configuring the hardware interface](images/144081914507_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the hardware interface](images/144081914507_DV_resource.Stream@PNG-en-US.png)

   Configuring the hardware interface
4. Expand the "PROFINET IO system (100)" entry.
5. Click on the displayed converter (in this case: "Drive unit_1").
6. Click on the ![Procedure](images/149079116555_DV_resource.Stream@PNG-de-DE.png) icon to confirm your selection.

   The "Device configuration" setting option is enabled. In addition, the "Drive configuration" setting option is displayed and enabled.

###### Result

The "Basic parameterization" function view is called in the "Drive configuration" display area. The further configuration of the technology object depends on the SIMATIC controller used.

You can find additional details on the configuration of technology objects in the [SIMATIC help](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#introduction-s7-1500-s7-1500t).

## Establishing an online connection to the target device

This section contains information on the following topics:

- [Fundamentals](#fundamentals-3)
- [Checking the firmware consistency](#checking-the-firmware-consistency)
- [Going online - default settings](#going-online---default-settings)
- [Online connection via Ethernet IE](#online-connection-via-ethernet-ie)
- [Online connection via PROFINET IO](#online-connection-via-profinet-io)

### Fundamentals

#### Interfaces used

For most Control Units (CUs), there are two interfaces available with which the drive can go online.

> **Note**
>
> General information regarding the online mode in the TIA Portal is available under "[Connecting devices online](Using%20online%20and%20diagnostics%20functions.md#connecting-devices-online)" in the online help.

The procedure for "Going online" is subsequently explained based on the example of a G220 Control Unit. The procedure is identical for the other Control Unit.

> **Note**
>
> **Comply with the installation und industrial security guidelines - cell protection concept**
>
> - Ethernet commissioning interface X127:
>
>   Only local access (point-to-point connection) is permitted for this interface.
> - PROFINET interface X150:
>
>   PROFINET must be separated from the rest of the plant network in accordance with the Defense in Depth concept. Manual access to cables and any open connections must be protected as in a control cabinet.

> **Note**
>
> **Deactivated interfaces**
>
> Interfaces in the protected drive can only be used if they are activated at the drive. Interface activation can deviate from the factory setting as a result of individual settings or due to security settings.
>
> An overview of the interface factory settings is provided on Page "[Ports and protocols](User%20administration%20and%20security.md#activating-ports-and-protocols-features)".

The PROFINET addresses are in the range of the PROFINET subnet of a SIMATIC S7 controller so that you can network the drive unit with a controller without having to adapt the subnet mask and the IP address.

![Example: G220 PN interface](images/153859367307_DV_resource.Stream@PNG-en-US.png)

Example: G220 PN interface

#### Trusted device

For secure communication between the operating unit and the drive, the drive must be classified as "trusted". Without this classification, online access is not possible. A device is considered trusted and therefore secure if it is assigned a digital certificate accepted by Startdrive.

See the page "[Secure communication with Trusted Devices](User%20administration%20and%20security.md#secure-communication-with-trusted-devices-from-sinamics-firmware-v61)" on how to assign a digital certificate to the drive.

#### Requirements

- The drive must be classified as a "trusted" device by a digital certificate.
- The interfaces you want to use for a connection must be enabled for access in the project's general security settings.

  For details, see the "[General security settings - ports and protocols](User%20administration%20and%20security.md#security-default-settings-for-projects-as-of-sinamics-fw-v61)" page.

#### IP addresses

**Control Unit (hardware)**

- **Ethernet commissioning interface X127**: For X127, an IP address and a subnet mask have already been assigned on the Control Unit in the factory:

  - IP address: 169.254.11.22
  - Subnet mask: 255.255.0.0
- **PROFINET interface X150**: For X150, an IP address and a subnet mask have already been assigned on the Control Unit in the factory:

  - IP address: 0.0.0.0
  - Subnet mask: 0.0.0.0
- First wire your PC to the appropriate interface on the Control Unit.

**Project**

A G220 drive is created with the following IP addresses in a project in the TIA Portal:

- **Ethernet commissioning interface X127**: The addresses correspond to the addresses that have already been assigned in the drive unit.

  - IP address: 169.254.11.22
  - Subnet mask: 255.255.0.0
- **PROFINET interface X150**: The following addresses are assigned for X150:

  - IP address: 192.168.0.1
  - Subnet mask: 255.255.255.0

### Checking the firmware consistency

#### Overview

An online connection between your operating unit and the drive is only possible if you are using the same firmware version on both the operating unit and drive.

Different firmware versions often occur in the following situations:

- A firmware update was performed for the drive unit. But the firmware saved in the Startdrive project is older.
- A new Startdrive version was installed. The latest firmware version was automatically set when you created a new project. However, your drive still uses an older version.

#### Procedure

1. Check the firmware version on your memory card with the "General" diagnostics screen form.

   - Connect your operating unit to the drive using a LAN cable, and switch on the drive.
   - In your Startdrive project, open the "Online access" entry in the project tree.
   - Select the network interface of your operating unit.
   - Double-click "Update accessible devices".

     The accessible device is displayed with the IP address in the project tree.
   - In the project tree call the "Online & diagnostics" function for the displayed device.

     ![Firmware version of the hardware; example S120](images/145960351627_DV_resource.Stream@PNG-en-US.png)

     Firmware version of the hardware; example S120
2. Check the firmware version in the catalog information of the Control Unit in your current Startdrive project.

   - To do so, call the following menu: "Control Unit > Inspector window > General > Catalog information".

     ![Firmware version of the software; example S120](images/145960826635_DV_resource.Stream@PNG-en-US.png)

     Firmware version of the software; example S120

#### Result

An online connection is possible if the firmware versions are identical (see the example screens above).

If the firmware versions are not identical, then the versions must be aligned in order to establish an online connection. You usually upgrade the older version.

**Remedy:**

- Perform a firmware update on your drive unit (see "[Performing a firmware update via memory card](#performing-a-firmware-update-via-memory-card)").

  - OR -
- Perform a device replacement in the Startdrive project for the affected drive. Replace the drive with a drive with the same power but new firmware.

  - OR -
- If a device replacement is not possible in the project:   
  Create a new Startdrive project for your drive unit in Startdrive and set a newer firmware version for the Control Unit in the new project (see "[Adding a drive](#adding-a-drive)").

  If you are using an older Startdrive version, it may be necessary to install a more recent Startdrive version beforehand.

### Going online - default settings

#### Requirements

- The firmware in the drive and the project is identical (consistent).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

#### Selecting the preferred PG/PC interface

If you prefer to use a specific network interface of your operating unit to establish an online connection, then you can preset this interface:

1. Select the "Options > Settings" menu.

   The settings of the TIA Portal are displayed.
2. Select the "Online & diagnostics" entry in the secondary navigation.
3. In the "Preset connection path for online access" area, specify the type of the PG/PC interface as well as the interface.
4. Enable the option "Display dialog for setting the default connection path for online access".

#### Display: Inconsistent state, online/offline

If the online and offline configurations differ significantly, Startdrive will show you an inconsistent state when you "go online" via this icon ![Display: Inconsistent state, online/offline](images/145960343179_DV_resource.Stream@PNG-de-DE.png). Causes can include, for example, missing components in one of the two states.

**Remedial measures:**

- [Download to device](#loading-the-configuration-from-the-project-to-the-device)

  If the offline configuration in the Startdrive project is correct - but the online configuration in the drive is not.
- [Upload from device](#loading-the-configuration-from-the-device-to-the-project)

  If the online configuration in the drive is correct - but the offline configuration in the Startdrive project is not.

#### Drive protected, however no project protection activated

Access to SINAMICS drives can also be protected using a web server.

If you now want to access the drive via an unprotected Startdrive project, which was protected via the web server, then access is denied. In this case, an online connection to the protected drive cannot be established.

**Remedial measures:**

- Activate project protection and create the user account with the required access rights to the drive (see [User administration and security](User%20administration%20and%20security.md#overview)).

### Online connection via Ethernet IE

This section contains information on the following topics:

- [Going online via the Ethernet interface](#going-online-via-the-ethernet-interface)

#### Going online via the Ethernet interface

##### Overview

As the Ethernet commissioning interface has already been assigned an IP address, you can go online directly.

If you are not using a new project and devices have already been created, check the IP address of the interface in the project in the inspector window under "Properties > General > Ethernet addresses" and the IP address assigned to the device. The addresses and subnet masks must be identical.

##### Requirements

- A SINAMICS project with a corresponding Control Unit is created in Startdrive.
- There is a physical connection between the Ethernet interface of your operating unit and the Ethernet commissioning interface of your drive (X127).
- The Ethernet commissioning interface of your drive (X127) is activated.

  For details, see Page "[Ports and protocols](User%20administration%20and%20security.md#activating-ports-and-protocols-features)".
- The firmware version of the Control Unit is identical to the firmware version used in the Startdrive project.

##### Quick search via "Online access"

To obtain a fast overview, you can start a search in "Online access" at the required interface. If the wiring to your drive is error-free and you have wired the correct drive (LED flashing for checking), the drive is displayed with the appropriate IP address.

![Online access](images/172070576779_DV_resource.Stream@PNG-en-US.PNG)

Online access

##### Procedure: Going online

Once you have found the drive under "Online access", establish an online connection. The first time you establish a connection, you must set the "PG/PC interface" and "Connection to interface/subnet" parameters:

1. Click the "Go online" button.

   If there is a user authentication for the opened Startdrive project, the "Go online" dialog is called automatically.

   If there is no user authentication yet, the "Log on to device" dialog appears.

   - Correct the default user name here if necessary.
   - Enter the password and confirm with "OK".

   The "Go online" dialog is then opened automatically.

   ![Go online](images/145961114763_DV_resource.Stream@PNG-en-US.png)

   ![Go online](images/145961114763_DV_resource.Stream@PNG-en-US.png)

   Go online
2. If no correctly configured interface has been set yet, then select the type of the PG/PC interface (1).
3. If an interface has still not been preset, select the PG/PC interface of your operating unit (2).
4. Specify the Ethernet interface (X127) of the Control Unit (3) as the connection to the interface/subnet.
5. Click on "Start search" (4) to search for the drive with the set parameters.

   The devices found are displayed under "Select target device".
6. Select your drive from the table (5).
7. Click on "Connect" to establish an online connection to the drive (6).

##### Result

There is an online connection between your operating unit and the drive. The settings are used automatically the next time you go online and the "Go online" dialog is no longer displayed.

> **Note**
>
> You can also generally [preassign](#going-online---default-settings) interface settings.

---

**See also**

[Checking the firmware consistency](#checking-the-firmware-consistency)

### Online connection via PROFINET IO

This section contains information on the following topics:

- [Using the PROFINET IO interface](#using-the-profinet-io-interface)
- [Search for the target device (accessible devices)](#search-for-the-target-device-accessible-devices)
- [Assigning an IP address](#assigning-an-ip-address)
- [Going online via the PROFINET interface](#going-online-via-the-profinet-interface)
- [Assigning PROFINET device names](#assigning-profinet-device-names)
- [Comparing IP addresses](#comparing-ip-addresses)
- [Setting up the interface to the operating unit](#setting-up-the-interface-to-the-operating-unit)
- [Resetting PROFINET interface parameters](#resetting-profinet-interface-parameters)

#### Using the PROFINET IO interface

##### Requirement

The PROFINET interface of the Control Unit is X150. The drive and your operating unit must be located in the same subnet in order that an online connection is possible.

You must select the IP address and subnet mask accordingly.

##### Procedure

Proceed as follows to establish an online connection between an operating unit and a drive:

1. Search for a device using the online access
2. Assign the device an IP address and device name.
3. Adapt the IP address and subnet mask of the configured device in the project.
4. Compare the assigned interface data with the configured interface data.

---

**See also**

[Search for the target device (accessible devices)](#search-for-the-target-device-accessible-devices)

#### Search for the target device (accessible devices)

##### Overview

The TIA Portal can search for the drive based on the online accesses of your operating unit.

##### Requirements

- A SINAMICS project with a corresponding Control Unit is created in Startdrive.
- There is a physical connection between the EtherNet interface of your operating unit and the PROFINET interface of your drive (X150).
- The firmware version of the hardware is the same as the firmware version used in the Startdrive project.

##### Procedure

To search for a device, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your computer.
3. Double-click "Update accessible devices".

   The device is displayed in the project tree.

   ![PROFINET online access](images/145961566091_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET online access](images/145961566091_DV_resource.Stream@PNG-en-US.png)

   PROFINET online access

   If the communication parameters are at their factory settings (IP address 0.0.0.0 and no device name), then the default device names of the TIA Portal ("Device" in this case) and the MAC address are displayed.

   If you want to go online on the device (e.g. the drive), you must assign an IP address and a device name.
4. Select the device and, if required, assign an IP address and a device name, see also [Assigning an IP address](#assigning-an-ip-address) and [Assigning PROFINET device names](#assigning-profinet-device-names).

   ![PROFINET with IP address](images/145962911499_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET with IP address](images/145962911499_DV_resource.Stream@PNG-en-US.png)

   PROFINET with IP address

   The device is displayed with the device name (in this case, drive_1) and the IP address (in this case, 198.168.0.21).

   If you cannot assign an IP address and device name, you may have to check the IP address of your PG/PC. It must be in the same address range as the address of the device, see also [Setting up the interface to the operating unit](#setting-up-the-interface-to-the-operating-unit).

##### Result

You have found the device in the PROFINET subnet and assigned an IP address and a device name. You only have to establish an online connection.

#### Assigning an IP address

##### Overview

Before you can go online on a device via PROFINET, you must assign the PROFINET interface of the drive a matching IP address.

- The PROFINET interface of the drive does not have an IP address when delivered
- If the device already has an IP address, perform the "[Reset to factory settings](#resetting-profinet-interface-parameters)" function to reset it to 0.0.0.0.

The PROFINET interface has already been assigned an IP address and subnet mask in the project:

- IP address: 192.168.1.2
- Subnet mask: 255.255.255.0

The IP address and the subnet mask are located in the subnet of an S7-1500 control, which makes it simpler to network the control and drive.

> **Note**
>
> **Assigning the IP address without "Reset to factory settings"**
>
> If the device already has an IP address, you can overwrite it with a new address. However, you must perform a **Power ON** so that the setting becomes effective.

> **Note**
>
> **Trusted device**
>
> If the IP addresses of the Ethernet or PROFINET interface are changed in the drive, the drive is automatically considered [untrusted](User%20administration%20and%20security.md#secure-communication-with-trusted-devices-from-sinamics-firmware-v61) the next time it is accessed. An existing digital certificate still points to the old IP addresses.
>
> - Therefore, always create a new certificate after an IP change in the drive.

##### Requirement

- There is a physical connection between the Ethernet interface of your operating unit and the PROFINET interface of your device (X150).

##### Procedure

To assign an IP address, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your operating unit.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the entry "Assign IP address".

   ![Assigning an IP address](images/145961217419_DV_resource.Stream@PNG-en-US.png)

   ![Assigning an IP address](images/145961217419_DV_resource.Stream@PNG-en-US.png)

   Assigning an IP address
7. Enter a matching IP address for your project or correct an existing IP address.
8. Enter a suitable subnet mask.
9. Click the "Assign IP address" button.
10. Double-click "Update accessible devices".

    This display of the IP address is updated. The MAC address is read out automatically.

##### Result

The IP address has been assigned to the device.

#### Going online via the PROFINET interface

##### Overview

User authentication is mandatory for the online connection. The program checks whether a successful login has already taken place when opening the Startdrive project (offline). If the Startdrive project is not protected, a login is required at the latest when going online.

##### Procedure

If you have found the device at "Online access", establish an online connection. The first time you establish a connection, you must set the "PG/PC interface" and "Connection to interface/subnet" parameters:

1. Click the "Go online" button.

   If there is a user authentication for the opened Startdrive project, the "Go online" dialog is called automatically.

   If there is no user authentication yet, the "Log on to device" dialog appears.

   - Correct the default user name here if necessary.
   - Enter the password and confirm with "OK".

   The "Go online" dialog is then opened automatically.

   ![Connecting online via PROFINET interface](images/145961347083_DV_resource.Stream@PNG-en-US.png)

   ![Connecting online via PROFINET interface](images/145961347083_DV_resource.Stream@PNG-en-US.png)

   Connecting online via PROFINET interface
2. If no correctly configured interface has been set yet, select the type of the PG/PC interface.
3. If an interface has still not been preset, select the PG/PC interface of your operating unit.
4. Specify the PROFINET interface (X150) of the drive as the connection to the interface/subnet.
5. Click on "Start search" to search for the drive with the set parameters.

   The devices found are displayed in a table under "Select target device".
6. Select your device in the table.
7. Click "Connect" to establish an online connection to the device.

##### Result

There is an online connection between your operating unit and the drive. The settings are used automatically the next time you go online and the "Go online" dialog is no longer displayed.

#### Assigning PROFINET device names

##### Overview

For operation in a PROFINET subnet, the drive must also be assigned a device name.

The name must comply with the DNS name syntax; for detailed information, review the TIA Portal online help.

- The drive does not have a device name when delivered
- If the device already has a name, perform "Reset to factory settings". The name is deleted.

##### Requirement

- There is a physical connection between the Ethernet interface of your operating unit and the PROFINET interface of your drive (X150).

##### Procedure

To assign a name, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your operating unit.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the entry "Assign PROFINET device name".

   ![Assigning names](images/145961422475_DV_resource.Stream@PNG-en-US.png)

   ![Assigning names](images/145961422475_DV_resource.Stream@PNG-en-US.png)

   Assigning names
7. Enter a device name.
8. Click "Assign name" to assign a name to the drive.
9. Update the interface under "Online access".

##### Result

The name has been assigned to the drive.

#### Comparing IP addresses

##### Overview

After you have assigned the IP address to the device, check the IP address and subnet mask set in the project. An online connection can only be established when the settings in the project and in the device are identical.

##### Requirement

- There is a physical connection between the Ethernet interface of your operating unit and the PROFINET interface of your device (X150).

##### Procedure

To compare the address, proceed as follows:

1. Search for the device at "Online access" and "Update accessible devices".

   The device is displayed with IP address and subnet mask in the diagnostics view.
2. Switch to the device view and open the inspector window.
3. Select the "Properties" and "General" tabs in the inspector window.
4. In the secondary navigation of the inspector window, select the entries "PROFINET interface [X150]" and "Ethernet addresses".

   The properties of the interface are displayed.
5. Compare the IP address and subnet mask with the settings under "Online access".

   ![IP address in the project](images/145961513483_DV_resource.Stream@PNG-en-US.png)

   ![IP address in the project](images/145961513483_DV_resource.Stream@PNG-en-US.png)

   IP address in the project

##### Result

If both settings are the same, you can establish an online connection.

#### Setting up the interface to the operating unit

##### Overview

PROFINET communication between the device and the operating unit is established via an Ethernet interface. If you have not yet adapted the IP address and subnet mask of the PG/PC interface, you can apply the following procedure.

> **Note**
>
> **Assigning a temporary IP address**
>
> If you search for the device via "Accessible devices" or go online for the first time, the operating unit can automatically be assigned a temporary IP address in the subnet.

##### Requirement

- For PROFINET communication, the IP address and the subnet mask of the PG/PC interface (operating unit) must lie within the number range of the PROFINET subnet.

##### Displaying the properties of the PG/PC interface

The following procedure describes the process for the "Ethernet" interface type using the "Online access" function.

To assign the interfaces, proceed as follows:

1. Navigate to the appropriate interface in the project tree under "Online access".
2. In the shortcut menu, click "Properties".

   ![Properties: Online access](images/145962964107_DV_resource.Stream@PNG-en-US.png)

   Properties: Online access
3. In the next step, select the subnet and accept the setting with "OK" where applicable.

   ![Assigning a subnet](images/145963080715_DV_resource.Stream@PNG-en-US.png)

   Assigning a subnet

##### Adding an IP address in the subnet

1. Click ![Adding an IP address in the subnet](images/145963094923_DV_resource.Stream@PNG-en-US.png) on the toolbar.  
   The "Select devices for setting up the online connection" dialog box opens.

   ![Selecting a device for online connection](images/145963109131_DV_resource.Stream@PNG-en-US.png)

   Selecting a device for online connection
2. Select the device and confirm with "Connect".
3. Assign an IP address to the operating unit, which lies in the subnet of the device.  
   If you have not already done so, it is now possible to temporarily assign a suitable IP address from the subnet of the device via the Windows control panel.

   ![Assigning an IP address](images/145963137547_DV_resource.Stream@PNG-en-US.png)

   Assigning an IP address
4. Click "Yes" to assign the IP address.

   ![IP address added](images/145963151755_DV_resource.Stream@PNG-en-US.png)

   IP address added
5. Confirm with "Yes". The interface has been assigned the IP address within the PROFINET subnet.

##### Result

- You have assigned the PG/PC interface.
- The TIA Portal has assigned an IP address within a project.
- The online connection has been established.

##### Displaying and deleting temporary IP addresses

You can display and also delete all temporarily assigned addresses.

1. Navigate in the project tree under "Online access" to the appropriate interface.
2. In the shortcut menu, click "Properties".
3. Under Configuration, select the "IE-PG Access" item.

   ![Displaying and deleting temporary IP addresses](images/145963123339_DV_resource.Stream@PNG-en-US.png)

   Displaying and deleting temporary IP addresses

#### Resetting PROFINET interface parameters

##### Overview

If problems occur during the commissioning via PROFINET, it is recommended that the interface parameters of the drive be reset to the factory settings.

##### Requirement

- Physical connection between the Ethernet interface of your operating unit and the Ethernet and/or PROFINET interface of your drive.

##### Procedure

To restore the factory settings, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your operating unit.
3. Double-click "Update accessible devices" in the project tree.

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the "Resetting PROFINET interface parameters" entry in the secondary navigation.

   ![Resetting the PROFINET interface parameters](images/145961138955_DV_resource.Stream@PNG-en-US.png)

   ![Resetting the PROFINET interface parameters](images/145961138955_DV_resource.Stream@PNG-en-US.png)

   Resetting the PROFINET interface parameters

   The option "Retain I&M data" is selected by default. This means the IM0 to IM3 data are retained during resetting and are not deleted. If you want to reset this data too, select the "Delete I&M data" option.
7. Click the "Reset" button.

   The drive communication settings are reset to the factory settings.
8. Double-click "Update accessible devices" in the project tree.

**Note**

If the PROFINET IO device does not support a reset according to the PROFINET standard, the IM0 to IM3 data may be deleted even though they should be retained according to this configuration.

##### Result

The factory settings of the IP address and the device name are now displayed under "Online access".

> **Note**
>
> After a reset to factory settings, the most important drive data for communication are missing:
>
> - Assign a new IP address and a new device name to the drive after the reset, see also [Comparing IP addresses](#comparing-ip-addresses) and [Assigning PROFINET device names](#assigning-profinet-device-names).

## Diagnostics

This section contains information on the following topics:

- [Device diagnostics](#device-diagnostics)
- [Online & diagnostics](#online-diagnostics)

### Device diagnostics

#### Overview

Faults, warnings, or a requirement for maintenance pending on the device are displayed as icons on the Startdrive. The icons have different colors according to the seriousness of the situation. The icons are also displayed in the network and topology view so that consistent diagnostics is possible in these views.

Compilation of the most important diagnostic icons

| Icon | Meaning |
| --- | --- |
| ![Overview](images/165033745035_DV_resource.Stream@PNG-de-DE.png) | OK = No fault or maintenance required |
| ![Overview](images/145967912715_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Overview](images/145967933963_DV_resource.Stream@PNG-de-DE.png) | Maintenance requirement for a subordinate component |
| ![Overview](images/145967883019_DV_resource.Stream@PNG-de-DE.png) | Maintenance request |
| ![Overview](images/145967891467_DV_resource.Stream@PNG-de-DE.png) | Maintenance request for a subordinate component |
| ![Overview](images/165033966219_DV_resource.Stream@PNG-de-DE.png) | Fault/error |
| ![Overview](images/145967861771_DV_resource.Stream@PNG-de-DE.png) | Fault/error at a subordinate component |
| ![Overview](images/165034213003_DV_resource.Stream@PNG-de-DE.png) | Connection error to the device |
| ![Overview](images/165033974411_DV_resource.Stream@PNG-de-DE.png) | Establish a connection |
| ![Overview](images/145967942411_DV_resource.Stream@PNG-de-DE.png) | The configured device and the actual device have incompatible types. |
| ![Overview](images/165033842827_DV_resource.Stream@PNG-de-DE.png) | The diagnostics status is determined |
| ![Overview](images/165034550155_DV_resource.Stream@PNG-de-DE.png) | Online and offline versions of the object are different |
| ![Overview](images/165034968459_DV_resource.Stream@PNG-de-DE.png) | Object only exists online |
| ![Overview](images/165034541963_DV_resource.Stream@PNG-de-DE.png) | Object only exists offline |

The colored icons are displayed in the following areas of the TIA Portal:

- Project tree
- Device view
- Device overview

#### Requirement

- There is an online connection between the drive and the operating unit.

  Diagnostic information can only be displayed in online mode.

#### Display messages

Proceed as follows to display messages that have been assigned an icon:

1. Double click the icon.
2. The "Display message" tab is moved into the foreground of the inspector window.

   All pending messages are displayed there.

#### More information

More information on the display of the diagnostics and comparison status is provided in the information system on the following page:

- [Displaying the diagnostics and comparison status using icons](Device%20and%20network%20diagnostics.md#displaying-diagnostics-status-and-comparison-status-using-icons)

### Online & diagnostics

This section contains information on the following topics:

- [Overview](#overview-7)
- [Diagnostics](#diagnostics-1)
- [Functions](#functions)
- [Backup and restore](#backup-and-restore)

#### Overview

##### Description

In the diagnostics view, you are working in online mode and see the most important drive information or make important basic settings.

##### Requirements

- Physical connection between the Ethernet interface of your operating unit and the Ethernet or PROFINET interface of your drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Calling diagnostics

Proceed as follows to display diagnostics and functions for a drive connected online:

1. Double-click on the "Online & diagnostics" menu in the project tree.

   The diagnostics and diagnostic functions are displayed in the secondary navigation and can be called from here.
2. Select the "Online access" entry in the secondary navigation.
3. Select the network interface of your operating unit.
4. Click on "Go online".

##### Result

The online connection to the drive is established. The diagnostics view is displayed in the Startdrive working area. Use the secondary navigation of this diagnostics view to retrieve various diagnostic information for the drive and perform some important basic functions. The following illustration shows the structure of a diagnostics view:

![Example: Online & diagnostics made anonymous](images/171776671243_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Function view for online diagnostics and important basic functions |

Example: Online & diagnostics made anonymous

---

**See also**

[Overview](User%20administration%20and%20security.md#overview)
  
[Secure communication with Trusted Devices (from SINAMICS firmware V6.1)](User%20administration%20and%20security.md#secure-communication-with-trusted-devices-from-sinamics-firmware-v61)

#### Diagnostics

This section contains information on the following topics:

- [Diagnostics overview](#diagnostics-overview)
- [Communication](#communication)
- [Maintenance](#maintenance)
- [Security](#security)

##### Diagnostics overview

###### Overview

The diagnostics view provides the following diagnostic information from the connected drive:

- General

  Information about component, module and manufacturer

  You can therefore identify the drive and the most important drive data is displayed.
- Security

  Information on the security settings of the connected drive (see [Security](#security)).
- Active alarms

  Information on active warnings and alarms

  In the event of a fault, the parameterized fault response is initiated and the ZSW1.3 status signal is issued. The fault is also entered in the fault buffer. Faults must be acknowledged after the cause has been resolved. To do this, use the function icon at the top of the function view (![Overview](images/151892882187_DV_resource.Stream@PNG-de-DE.png)/![Overview](images/151892873611_DV_resource.Stream@PNG-de-DE.png)).

  In the event of an alarm, status signal ZSW1.7 is set. The alarm is also entered in the alarm buffer.
- Alarm history

  The individual drive components have an alarm history, in which all alarm messages and faults are recorded.

  Using the function icons on the function view, you can either clear the fault buffer (![Overview](images/151892839435_DV_resource.Stream@PNG-de-DE.png)) or export it to a CSV file (![Overview](images/151890267531_DV_resource.Stream@PNG-de-DE.png)).
- Actual values

  Information about the most important parameter actual values and status bits.
- Safety Integrated Function status

  Information on the current status of the Safety Integrated Functions.

  For detailed information on these functions, refer to the "[Function status](Commissioning%20SINAMICS%20G220%20drives.md#function-status)" section.
- PROFINET interface (X150)

  - Ethernet address

    Information about IP parameters (IP address and subnet mask) and the network connection (MAC address)
  - Communication

    Information on transmit and receive direction (PZDs of the telegrams).

    You can find detailed information on PZDs and telegrams in the "[Communication](#communication)" section.
- Maintenance

  Information on motor power consumption and fan wear.

  For detailed information on these functions, refer to the "[Maintenance](#maintenance)" section.

You call the individual diagnostic information in the secondary navigation of the diagnostics view.

###### Requirement

- There is an online connection between the drive and the operating unit.

  Diagnostics information can only be read out in online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Communication

This section contains information on the following topics:

- [G220 telegrams receive direction](#g220-telegrams-receive-direction)
- [G220 telegrams send direction](#g220-telegrams-send-direction)

###### G220 telegrams receive direction

###### Overview

In this diagnostics view, the components and interconnections of PROFIdrive telegrams are displayed for the converter in the receive direction (e.g. 20) by default.

You can use the telegram configuration (![Overview](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "PROFIsafe" or "Supplementary data" area.

###### Requirements

- There is an online connection between the drive and the PG/PC.

  The process data can only be configured in online mode.
- In the quick startup step "[Connection to PLC](Commissioning%20SINAMICS%20G220%20drives.md#connection-to-plc)", a connection to a PLC is configured and, optionally, a PROFIsafe connection can be activated to enable use of the Safety Integrated Functions.

###### Telegram structure

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

The following information of the displayed telegrams is displayed:

| Telegram type | PZD | Display of the value | Format switchover | Control words |
| --- | --- | --- | --- | --- |
|  | **The numbering and arrangement of the process data.** | **Value of the process data (PZD)** | **The value of the process data is switched to a different representation (hex, bin, dec).** | **List of the control words that are transmitted in the telegram.** |
| PROFIdrive  1, 2, 3, 4, 20, 102, 103, 352 | X | X | X | X |
| Torque supplementary telegram  750 | X | X | X | X |
| PROFIsafe  30, 902 | X | X | X | X |

###### Function diagrams (FD)

Standard telegrams and process data (PZD) - 2415 -

Manufacturer-specific telegrams and process data (PZD) - 2418 -

Supplementary telegram/free telegrams and process data (PZD) - 2423 -

Standard telegrams - 2915 -

Manufacturer-specific telegrams - 2917 -

###### G220 telegrams send direction

###### Overview

In this diagnostics view, the components and interconnections of PROFIdrive telegrams are displayed for the converter in the send direction (e.g. 20) by default.

You can use the telegram configuration (![Overview](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "PROFIsafe" or "Supplementary data" area.

###### Requirement

- There is an online connection between the drive and the PG/PC.

  The process data can only be configured in online mode.
- In the quick startup step "[Connection to PLC](Commissioning%20SINAMICS%20G220%20drives.md#connection-to-plc)", a connection to a PLC is configured and, optionally, a PROFIsafe connection can be activated to enable use of the Safety Integrated Functions.

###### Telegram structure

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

The following information of the displayed telegrams is displayed:

| Telegram type | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- |
|  | **List of the status words that are transferred in the telegram.** | **Value of the process data (PZD)** | **The value of the process data is switched to a different representation (hex, bin, dec).** | **Numbering and arrangement of the process data.** |
| PROFIdrive  1, 2, 3, 4, 20, 102, 103, 352 | X | X | X | X |
| Torque supplementary telegram  750 | X | X | X | X |
| PROFIsafe  30, 902 | X | X | X | X |

###### Function diagrams (FD)

Standard telegrams and process data (PZD) - 2415 -

Manufacturer-specific telegrams and process data (PZD) - 2418 -

Supplementary telegram/free telegrams and process data (PZD) - 2423 -

Standard telegrams - 2915 -

Manufacturer-specific telegrams - 2917 -

##### Maintenance

This section contains information on the following topics:

- [Displaying the motor energy consumption](#displaying-the-motor-energy-consumption)
- [Displaying the wear of the heat sink fans](#displaying-the-wear-of-the-heat-sink-fans)

###### Displaying the motor energy consumption

###### Overview

The energy values and the process energy values of the motor are displayed in the "Power consumption" function view. Information is provided regarding the energy balance and the energy that the motor draws and feeds back.

###### Requirements

- There is an active [online](#establishing-an-online-connection-to-the-target-device) connection between the drive and the operating panel.

  Diagnostics information can only be read out in online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Click on "Reset all displays" if you want to reset all energy displays.

###### Result

The energy values are newly acquired and displayed after the reset.

###### Displaying the wear of the heat sink fans

###### Overview

The wear of the heat sink fan is displayed in the "Power unit fan" function view. It is recommended that the fan is replaced if the wear counter is 100 %. After replacement, the wear meter can be reset to zero.

###### Requirements

- There is an active [online](#establishing-an-online-connection-to-the-target-device) connection between the drive and the operating panel.

  Diagnostics information can only be read out in online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Switch off the drive and replace the heat sink fan.
2. Switch the drive on again. Check that there is an active online connection.
3. Call up the "Power unit fan" function view again in the Startdrive project.

   The wear of the replaced fan is still displayed in the "Wear meter" field ([r0277](SINAMICS%20Parameter%20G220.md#r02770n-power-unit-heat-sink-fan-wear-counter)).
4. Click "Reset" next to the field.

###### Result

The wear counter is thus reset to zero and then records the wear of the current fan.

###### Additional parameters

---

##### Security

###### Overview

The "Security" diagnostics view displays a summary of the active security settings of the connected drive:

- Logged-in user

  - The user that is logged-in to the drive

    - or -
  - No logged-in user, as UMAC is not active

    In this case, UMAC activation is recommended.
- User Management & Access Control settings

  Shows the UMAC settings activated for the drive. Shows, for example, whether UMAC is active and what rights user account "Anonymous" has.
- Ports & protocols

  Displays the activation state (which interfaces are activated, which interfaces are deactivated) for the interfaces of the following areas:

  - Web server access
  - Fieldbus and associated protocols
  - S7 commissioning reports
  - DHCP configuration
- Encryption of the drive data

  Indicates whether the UMAC data in the drive is additionally encrypted.

###### Requirements

- There is an online connection between the drive and the operating unit.

  Diagnostic information can only be read out in online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### More information

You can only change these security settings offline in the Inspector window of the drive in the project.

Full details on configuring the runtime security settings are provided under Point "[Security settings for the drive](User%20administration%20and%20security.md#security-settings-for-the-drive-as-of-sinamics-fw-v61)".

#### Functions

This section contains information on the following topics:

- [Function overview](#function-overview)
- [Assigning an IP address](#assigning-an-ip-address-1)
- [Assigning PROFINET device names](#assigning-profinet-device-names-1)
- [Resetting PROFINET interface parameters](#resetting-profinet-interface-parameters-1)
- [Setting the time-of-day](#setting-the-time-of-day)

##### Function overview

###### Overview

The diagnostics view also provides important diagnostic information on the direct functions of the drive. You can change the settings of these direct functions ONLINE in the diagnostics view, the same as you do the settings for going online with the drive. You can also configure the following functions in the diagnostics view:

- [Assigning an IP address](#assigning-an-ip-address-1)
- [Updating the firmware online](#updating-the-firmware-via-an-online-connection)
- [Assigning a PROFINET device name](#assigning-profinet-device-names-1)
- [Entering the password for encrypting drive data](User%20administration%20and%20security.md#configuring-the-encryption-online-diagnostics)
- [Resetting PROFINET interface parameters](#resetting-profinet-interface-parameters-1)
- [Setting the time](#setting-the-time-of-day)
- [Using functions subject to license](#managing-supplementary-functions-that-require-a-license)

You call the individual functions in the secondary navigation of the diagnostics view.

###### Requirement

- There is an online connection between the drive and the operating unit.

  The direct functions can only be performed in online mode.
- With protection activated (UMAC):

  Corresponding function rights of your user account (see [Function rights and roles](User%20administration%20and%20security.md#access-control))

##### Assigning an IP address

###### Overview

Enter the IP address of the drive and the IP of the subnet mask in the diagnostics view "Online & diagnostics".

> **Note**
>
> **Changing an existing IP address**
>
> - If the device already has an IP address, run function "[Restore factory settings](#restoring-factory-settings-standard-scope)" to reset the IP address to 0.0.0.0.
> - If you wish to change the IP address without first restoring the factory settings, after making the change, restart the drive so that the settings become active.

###### Requirements

- There is an online connection between the drive and the operating unit.

  The direct functions can only be executed in the online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To assign an IP address, proceed as follows:

1. In the drive project tree, call function view "Online & diagnostics".
2. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
3. Select the entry "Assign IP address".

   ![Assigning an IP address](images/145961217419_DV_resource.Stream@PNG-en-US.png)

   ![Assigning an IP address](images/145961217419_DV_resource.Stream@PNG-en-US.png)

   Assigning an IP address
4. Enter a matching IP address for your project or correct an existing IP address.
5. Enter a suitable ID for the subnet mask.
6. Click the "Assign IP address" button.
7. Optional: If you are using a router, activate option "Use router" and enter the router address.
8. Save the settings in the drive.
9. Optional: Restart the drive.

###### Result

The IP address has been assigned to the device. The MAC address is read out automatically.

##### Assigning PROFINET device names

###### Overview

In addition to the IP address, the drive also requires a device name in the PROFINET subnet. The project factory setting defines that the device name is automatically generated. The automatically generated device name has the following structure:

<Drive name>.<Interface name>.<IO system name>

This name can only be indirectly changed by assigning another drive name.

If the automatically generated device name does not correspond to DNS naming conventions, then this name is automatically converted. This converted name is then subsequently shown in field "Converted name".

Once the PROFINET device name has been defined, you can assign this device name to a drive from the list of "Accessible devices in the network".

###### Requirements

- There is an online connection between the drive and the operating unit.

  The direct functions can only be executed in the online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To assign a name, proceed as follows:

1. In the drive project tree, call function view "Online & diagnostics".
2. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
3. Select the entry "Assign PROFINET device name".

   ![PN device name](images/164931064587_DV_resource.Stream@PNG-en-US.png)

   ![PN device name](images/164931064587_DV_resource.Stream@PNG-en-US.png)

   PN device name
4. Select a drive from the drop-down list "PROFINET device name".

   If the device name does not comply with DNS naming conventions, then an automatically generated device name is shown in field "Converted device name".
5. In area "Device filter", activate the filter options for the accessible devices in the network.
6. Click on "Update list" to update the list of "Accessible devices".

   All the devices accessible in the network are then shown in the list below.
7. From the list, select the drive to which the device name should be assigned.
8. Then click on "Assign name".
9. Save the settings in the drive.

###### Result

The name has been assigned to the drive.

##### Resetting PROFINET interface parameters

###### Overview

If problems occur when commissioning via PROFINET, it is recommended that the drive interface parameters are reset to the factory settings.

###### Requirements

- There is an online connection between the drive and the operating unit.

  The direct functions can only be executed in the online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To restore the factory settings, proceed as follows:

1. In the drive project tree, call function view "Online & diagnostics".
2. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
3. Select the "Resetting PROFINET interface parameters" entry in the secondary navigation.

   ![Resetting the PROFINET interface parameters](images/145961138955_DV_resource.Stream@PNG-en-US.png)

   ![Resetting the PROFINET interface parameters](images/145961138955_DV_resource.Stream@PNG-en-US.png)

   Resetting the PROFINET interface parameters

   The option "Retain I&M data" is selected by default. This means the IM0 to IM3 data are retained during resetting and are not deleted. If you want to reset this data too, select the "Delete I&M data" option.
4. Click the "Reset" button.

   The drive communication settings are reset to the factory settings.
5. Save the settings in the drive.

**Note**

In rare cases, the PROFINET IO device does not support a reset in compliance with the PROFINET standard. As a consequence, IM0 to IM3 data are deleted although this data should be retained according to this configuration.

###### Result

The factory settings of the IP address and the device name are now displayed under "Online access".

> **Note**
>
> After a reset to factory settings, the most important drive data for communication are missing:
>
> - After the reset, assign a new IP address and a new device name to the drive.
>
>   For details, see [Assigning an IP address](#assigning-an-ip-address-1) and [Assigning PROFINET device names](#assigning-profinet-device-names-1)

##### Setting the time-of-day

###### Overview

For the operation of a drive, the definition of a drive time is important. Two variants of the time definition are possible:

- Synchronize with the NTP server

  When the drive is connected to other devices and a central NTP server is to provide the time for the connected devices. Alternatively, a controller can also act as NTP server.
- No synchronization, time is manually set

  if the drive is initially operated without control.

You set the required drive time in the diagnostics view as a direct function. If a time has already been set, it is displayed in the "Current drive time" area. If it is a synchronized time, the NTP server used is also displayed in the "Time source" field.

> **Note**
>
> Alternatively, you can set the time settings offline in the inspector window of the drive. However, these settings are only transferred to the drive when the drive data is loaded.
>
> - If you differentiate the time settings between the drive and the project, this is indicated by the icon ![Overview](images/149081587467_DV_resource.Stream@PNG-de-DE.png). In this case, reload the drive data into the drive.
> - You receive an appropriate note if an already set NTP server cannot be accessed. Access attempts are repeated on a regular basis.

###### Requirements

- There is an online connection between the drive and the operating unit.

  The direct functions can only be executed in the online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Setting the time with synchronization (PLC becomes NTP server)

A synchronized time is always recommended when the drive is connected to a controller. This is the reason that factory setting "Synchronize with NTP server" is activated when the "Set time" diagnostics view is called for the first time.

1. If the "Synchronize with NTP server" option is not activated, then activate this option.

   By default, the "Use PLC as NTP server" option is now enabled. If the drive is connected to a PLC, the IP address of the PLC is displayed.
2. Select the time zone of your country in the "Time zone" area.

   Example: For Central Europe, use the time zone "GMT+01:00".
3. Then click on "Accept".

###### Setting the time with synchronization (any NTP server)

If you want to synchronize the time of the drive with any NTP server, proceed as follows.

1. If the "Synchronize with NTP server" option is not activated, then activate this option.

   By default, the "Use PLC as NTP server" option is now enabled. If the drive is connected to a PLC, the IP address of the PLC is displayed.
2. Disable the option "Use PLC as NTP server".

   The input field for the IP address is cleared.
3. Enter the IP address of the desired NTP server in the "IP address" field.
4. Select the time zone of your country in the "Time zone" area.

   Example: For Central Europe, use the time zone "GMT+01:00".
5. Then click on "Accept".

###### Setting the time without synchronization

A time of the drive without synchronization is used if the drive is operated for test purposes without a control unit connected. If you want to set the time without synchronization, proceed as follows:

1. Activate the option "No synchronization, set time manually".

   You can then select whether you accept the time of your operating unit or you wish to manually enter the time.
2. If you wish to use the operating unit time, activate option "Use time from PG/PC".

   - Or -

   Proceed as follows if you wish to manually set the time:

   - In the "Drive time" area, set the current calendar day, the current year, and the desired time.
   - Select the time zone of your country in the "Time zone" area.

     Example: For Central Europe, use the time zone "GMT+01:00".
3. Then click on "Accept".

###### Result

The set time is directly transferred to the drive. The current time settings are displayed in the "Current drive time" area. Save the drive data.

#### Backup and restore

This section contains information on the following topics:

- [Fundamentals](#fundamentals-4)
- [Restarting the drive](#restarting-the-drive)
- [Saving drive data retentively](#saving-drive-data-retentively)
- [Save drive data to backup file](#save-drive-data-to-backup-file)
- [Restore drive data from backup file](#restore-drive-data-from-backup-file)
- [Restoring factory settings](#restoring-factory-settings-1)
- [Restore Safety Integrated factory settings](#restore-safety-integrated-factory-settings)

##### Fundamentals

###### Overview

You have the following options with the "Backup/Restore" function view:

- Restart the drive (POWER ON)
- Retentively save RAM data
- Save drive data to backup file
- Restore drive data from backup file

  Alternatively, this can also be used for device replacement or series commissioning.
- Restore factory settings
- Restore Safety Integrated factory settings

  Only for SINAMICS drives which use Safety Integrated.

###### Requirements

- Physical connection between the Ethernet interface of your operating unit and the Ethernet or PROFINET interface of your drive.
- The drive has been switched on and is supplied with power.
- Optional memory card is inserted (for parameter backup).
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Call "Backup/Restore" via Online & diagnostics

1. In the project tree of your drive, double-click on "Online & diagnostics".

   The "Online access" display area is displayed.
2. In the secondary navigation, select menu "Functions > Backup/Restore".

   The "Backup/Restore" function view opens.
3. In the toolbar, click "Go online" and make all of the necessary connection settings.

   The "Backup/Restore" function view is now displayed in online mode and you can make the required settings.

###### Call "Backup/Restore" from the diagnostics view

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your operating unit.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. In the project tree call the "Online & diagnostics" function for the displayed device.

   The diagnostics view is displayed.
5. In the secondary navigation of the diagnostics view, select menu "Functions > Backup/Restore".

   In the diagnostics view, the "Backup/Restore" function view is opened and you can make the required settings.

###### Result

You have called the "Backup/Restore" function view and can now perform the existing backup and restore functions.

##### Restarting the drive

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- The "Online & diagnostics" view is displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

For a POWER ON of your drive, proceed as follows:

1. In the area "Restart the drive", click on "Restart".

###### Result

The drive is restarted. The LEDs indicate the current drive status.

##### Saving drive data retentively

###### Overview

The parameter values are normally saved as volatile data in the RAM of the drive. To keep the data safe, you can retentively store the parameter values in the ROM and, if available, simultaneously on a memory card.

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- Optional memory card is inserted (for parameter backup).
- The "Online & diagnostics" view is displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. In the "Retentively save RAM data" area, click on "Save":

###### Result

The program saves the parameter values in the ROM and checks whether a memory card is inserted. If a matching memory card is detected, then the parameter values are also saved retentively to this card.

##### Save drive data to backup file

###### Overview

With the function "Save drive data to backup file" you save all settings of the drive in a file.

The following data is contained in the backup file:

- Security settings and UMAC (users, their passwords and rights)
- Password to protect confidential drive data
- Drive settings
- Support settings
- Parameter values

Execute the "Save drive data to backup file" function in the following cases:

- after commissioning
- before "Restore factory settings"
- before a firmware upgrade/downgrade

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- The "Online & diagnostics" view is displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. In the "Save drive data to backup file", click on the "Create backup" button.
2. Enter a name for the new backup file.
3. Select a file directory of your operating unit as storage location and then confirm the backup.

###### Result

The drive data is then saved in a zip file in the selected file directory. Based on this backup, you can restore the drive data of your drive at a later time.

You can load the backed-up drive data and settings into other drives. The target drives must meet the following requirements:

- The rated power of the target drive matches the backed-up rated power.
- Firmware version of the target drive is ≥ the firmware version of the drive from which the backup data originates.

##### Restore drive data from backup file

###### Overview

If a backup file is available, you have the option of loading backed-up drive data into a drive.

This is particularly useful and time-saving in the event of a device replacement or series commissioning.

The following data is contained in the backup file:

- Security settings and UMAC (users, their passwords and rights)
- Password to protect confidential drive data
- Drive settings
- Support settings
- Parameter values

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- The "Online & diagnostics" view is displayed.
- A backup file of the drive is available on your operating unit.
- The rated power of the target drive matches the backed-up rated power.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Click the "Restore" button in the "Restore drive data from backup file" area.

   A selection dialog opens.
2. Select the file directory of your operating unit where the backup file is stored.
3. There, select the desired backup file whose drive data you want to restore and confirm the selection.

###### Result

The backup zip file is loaded into the drive and stored there. It is not imported during ongoing operation of the drive.

The backup is automatically imported when the drive is restarted (warm start).

##### Restoring factory settings

###### Overview

We recommend restoring the factory setting in the following cases:

- Interruption of the line voltage during commissioning
- Incomplete commissioning
- Ambiguity regarding the previous parameterization or previous use of the drive

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- The "Online & diagnostics" view is displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Click "Start" in the "Restoring factory settings" area.

###### Result

The factory settings of all parameters (including Safety Integrated) are now imported back into the drive.

The I&M data, communication settings and security settings (also certificates with TSL encryption) are retained.

For all other data, the factory settings are restored. Specifically the following data are no longer available:

- Specific motor configuration
- Closed-loop control settings that were made
- All settings made during commissioning

The drive must be recommissioned.

> **Note**
>
> If you wish to completely reset the drive, carry out a "[Complete reset of all device settings (via SD Card)](#complete-reset-of-device-settings)".
>
> To do this, you require a special memory card, which completely resets the converter when it starts up.
>
> The complete reset also deletes digital certificates.

##### Restore Safety Integrated factory settings

###### Overview

It is not always necessary to reset all of the drive settings. A separate reset function exists for Safety Integrated settings, which only explicitly reset Safety Integrated settings to the factory settings.

###### Requirements

- There is an online connection between the drive and the operating unit.
- The drive has been switched on and is supplied with power.
- The "Online & diagnostics" view is displayed.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. In field "Restore Safety Integrated factory setting", click on "Start".

###### Result

The factory settings are restored only for the Safety Integrated settings. All other settings are not reset.

---
title: "Configuring SINAMICS S200 drives"
package: StdrS200ConfenUS
topics: 110
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring SINAMICS S200 drives

This section contains information on the following topics:

- [Drive system](#drive-system)
- [Startdrive user interface](#startdrive-user-interface)
- [Fundamentals](#fundamentals)
- [Sequence of a device configuration and basic commissioning](#sequence-of-a-device-configuration-and-basic-commissioning)
- [Configuring devices in the project](#configuring-devices-in-the-project)
- [Establishing an online connection to the target device](#establishing-an-online-connection-to-the-target-device)
- [Diagnostics](#diagnostics)

## Drive system

This section contains information on the following topics:

- [Overview of SINAMICS S200](#overview-of-sinamics-s200)

### Overview of SINAMICS S200

The SINAMICS S200 drive system is a single-axis servo drive system. It comprises the following harmonized components:

- SINAMICS S200 drive series, which is available in the two following basic versions:

  - SINAMICS S200 Basic (200 V supply voltage)
  - SINAMICS S200 (200 V and 400 V supply voltages)

  All S200 variants are based on these two basic versions.
- SIMOTICS S-1FL2 motor
- MOTION-CONNECT 350 standard cables or MOTION-CONNECT 380 flexible cables
- BiSS interface to connect absolute encoders

The drive and the motor are intended for use with a higher-level control (PLC).  
Prefabricated MOTION-CONNECT 350 and MOTION-CONNECT 380 cables in various lengths are used to simply  
and reliably connect the motor to the drive.

SINAMICS S200 supports three encoder types:

- Absolute encoders, 17-bit singleturn
- Absolute encoders, 21-bit singleturn
- Absolute encoders, 21-bit singleturn + 12-bit multiturn

The drive is connected to the motor encoder at BiSS interface X100.

An example of an S200 drive system with PROFINET interface and the connected components is shown below:

![Example: SINAMICS S200 drive system with 3 AC cable connections](images/165161275275_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| ① | Fuse or type E combination motor controller (optional) | ⑧ | Shield plate |
| ② | Line filter (optional) | ⑨ | 24 V DC power supply (optional) |
| ③ | External braking resistor (optional) | ⑩ | STO connector |
| ④ | SIMOTICS S-1FL2 motor | ⑪ | Memory card |
| ⑤ | Motor connection cable | ⑫ | Commissioning tool  Web server or Startdrive |
| ⑥ | Encoder cable | ⑬ | Control (e.g. SIMATIC S7-1500) |
| ⑦ | Shield connection clamp | ⑭ | PROFINET cable to the next device |

Example: SINAMICS S200 drive system with 3 AC cable connections

---

**See also**

[Available components](#available-components)

## Startdrive user interface

This section contains information on the following topics:

- [Hardware catalog](#hardware-catalog)
- [Device configuration](#device-configuration)
- [Function view S200](#function-view-s200)
- [S200 parameter view](#s200-parameter-view)
- [S200 inspector window](#s200-inspector-window)
- [Rotate & optimize S200](#rotate-optimize-s200)
- [S200 guided quick startup](#s200-guided-quick-startup)

### Hardware catalog

This section contains information on the following topics:

- [Power variants S200](#power-variants-s200)
- [Available components](#available-components)

#### Power variants S200

##### Modules and components

The various SINAMICS S200 modules are stored as follows in the hardware catalog:

![SINAMICS S200 PN hardware catalog](images/164881765387_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | SINAMICS S200 converter;   SINAMICS S200 PN power variants that are available  SINAMICS S200 Basic PN power variants are listed in a similar fashion. |
| ② | 1FL2 motors;   Based on the motor article number, these synchronous motors can be assigned various absolute encoders. |

SINAMICS S200 PN hardware catalog

#### Available components

In Startdrive all available hardware components can be configured in the function view or in the parameter view. A list of the components that can be used for SINAMICS S200 in a Startdrive project is provided below.

Which hardware components can be used?

| Component / drive system | S200 | S200 Basic<sup>3)</sup> |
| --- | --- | --- |
| **Control Unit**  <sup>1)</sup> |  |  |
| S200 PN | X | X |
| **Motors** |  |  |
| 1FL2 synchronous motor | X | X |
| **Measuring systems** |  |  |
| Absolute encoder with BiSS interface<sup>2)4)</sup> | X | X |
| <sup>1)</sup> Integrated in the drive. Not separately selectable in the device configuration and via the hardware selection. Is indirectly determined by selecting the S200 type in the "Add new device" dialog.    <sup>2)</sup> BiSS interface: Open Source interface according to the SSI standard   <sup>3)</sup> Basis drive with fewer functions   <sup>4)</sup> Absolute encoders can be used as singleturn and multiturn encoders. The appropriate encoder is selected based on the Article No. of the motor. An encoder cannot be selected from the hardware list. |  |  |

> **Note**
>
> **Special case, S200 PTI**
>
> SINAMICS S200 PTI drives can only be configured using the "Web server" engineering tool. Startdrive currently does not have the appropriate functionality.

### Device configuration

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

![S200 device view](images/170762377611_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control Unit (including CU and PM) |
| ② | Bus interface, Ethernet in this case |
| ③ | Bus interface, PROFINET in this case |
| ④ | Motor |
| ⑤ | Encoder |
| ⑥ | Sensor Module |

S200 device view

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

![S200 network view](images/165122286475_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drive that is assigned as the IO device of a higher-level controller via fieldbus (in this case PROFINET IO). |
| ② | Fieldbus (in this case, PROFINET IO) |
| ③ | Higher-level controller, a SIMATIC S7-1500 in this case, that is configured as IO controller. |
| ④ | Data from drive and controller |

S200 network view

The specific parameters of the selected element are displayed in the inspector window.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145959026827_DV_resource.Stream@PNG-de-DE.png) | Mode to network devices. |
| ![Toolbar](images/145959034251_DV_resource.Stream@PNG-de-DE.png) | Mode to create connections. You can use the adjacent drop-down list to set the connection type. |
| ![Toolbar](images/145958637707_DV_resource.Stream@PNG-de-DE.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/145958648203_DV_resource.Stream@PNG-de-DE.png) | Show interface addresses. You can edit the addresses for the MPI, PROFIBUS and EtherNet interfaces directly in the network view: Select the required address and then click on the selected address field or press [F2]. |
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

- Displaying the EtherNet topology
- Configuring the EtherNet topology
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

![S200 topology view](images/165123063947_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Topology view toolbar |
| ③ | Graphic area of the topology view |
| ④ | Overview navigation |
| ⑤ | Table area of the topology view (topology overview) |

S200 topology view

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

The graphic area of the topology view displays EtherNet modules with their associated ports and port interconnections. Here you can add additional hardware objects with EtherNet interfaces.

The operator controls for view control are located at the bottom edge of the graphic area:

- Select the zoom level using the drop-down list. You can also enter a value directly into the field of the drop-down list.
- You can also set the zoom level using the slider.
- You can re-focus the window of the graphic area using the icon in the bottom right corner.

##### Table area

The table area consists of the following two tabs:

- "Topology overview" tab

  Displays the EtherNet or PROFINET modules with their ports and port interconnections in a table. This table corresponds to the network overview table in the network view.
- "Topology comparison" tab

  Shows the differences between the desired and actual topology and details.

### Function view S200

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
> You can find all drive parameters in the "[Parameter view](#s200-parameter-view)". Experts can then comprehensively parameterize the drive. However, the parameter view can only be called for the parameter assignment. The parameter view is not available for commissioning optimization.

#### Structure

The following figure shows an example of a function view structure:

![Function view S200](images/171657942411_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Icon: Saves data protected against power failure (in online mode) |
| ③ | Icon: Restores the factory settings (in online mode) |
| ④ | Button: Activates the online editing mode |
| ⑤ | Fields: Used for the manual input of values. |
| ⑥ | Button: Navigates to the previous or the following function view |
| ⑦ | Display field: Shows the drive data. This data cannot be changed when shown with a grey background. |

Function view S200

> **Note**
>
> **Special case: Extended parameterization**
>
> The parameter assignment functions can be set in the standard scope or expanded scope. On the 1st call, only the functions of the standard parameter assignment are displayed in the secondary navigation.
>
> - Click ![Structure](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) to display the functions for extended parameterization.
> - Click ![Structure](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) to reduce the display to the functions of standard parameterization again.

### S200 parameter view

#### Overview

The "Parameter view" provides a clearly organized display of the parameters available for the device. For the "Parameterization", you can switch the working area between the "[Function view](#function-view-s200)" and the "Parameter view".

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> User without these function rights either have read-only access or no access at all.

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

![S200 parameter view](images/162107676811_DV_resource.Stream@PNG-en-US.png)

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

S200 parameter view

#### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/145959411211_DV_resource.Stream@PNG-de-DE.png) | Expands or reduces all secondary navigation nodes. |
| ![Toolbar](images/145959338763_DV_resource.Stream@PNG-de-DE.png) | Expands or reduces all nodes below the selected node. |
| ![Toolbar](images/145959440907_DV_resource.Stream@PNG-de-DE.png) | Saves the parameters retentively (copy RAM to ROM). |
| ![Toolbar](images/145959449355_DV_resource.Stream@PNG-de-DE.png) | Restores the factory settings. |
| ![Toolbar](images/153507418891_DV_resource.Stream@PNG-en-US.PNG) | Displays the functions of the extended parameterization in the secondary navigation. |
| ![Toolbar](images/153509539339_DV_resource.Stream@PNG-en-US.PNG) | In the secondary navigation, reduces the functions back to the default parameterization. |
| ![Toolbar](images/145959330315_DV_resource.Stream@PNG-de-DE.png) | Compares the parameters of the drive object with another parameter set.   - In offline mode, the parameters are compared to the factory settings by default. - In online mode, the parameters are compared to the offline settings by default. - The comparison can also be deactivated again. |
| ![Toolbar](images/145959432459_DV_resource.Stream@PNG-de-DE.png) | Starts a CSV export:   - Save displayed parameters in a CSV file. - Save all parameters of the drive object in a CSV file. |

### S200 inspector window

#### Overview

The properties and parameters of a selected object are displayed in the inspector window. The properties and parameters can be edited. For example, new unspecified S200 drive objects inserted in the device view can be specified.

> **Note**
>
> Offline settings are generally made in the inspector window. These basic settings are usually a requirement for subsequent commissioning settings.

#### Structure

The information parameters in the inspector window are split up into various information types, which are displayed as main and secondary tabs in the inspector window:

![S200 inspector window](images/165110004875_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary tab: In this example, the main "Properties" tab |
| ② | Main tab: Properties, information, diagnostics |

S200 inspector window

#### Subdivision of the "Properties" area

For each information type, there are additional subareas that can be displayed using secondary tabs.

The most important type of information for SINAMICS S200 drives is the "Properties" area. The following secondary tabs are displayed in this area:

- General

  Displays the properties and settings of the drive, drive object or the hardware component. You can edit the settings and parameters here. The left pane of the inspector window contains the secondary navigation. Information and parameters are arranged there in groups. If you click the arrow symbol to the left of the group name, you can expand the group if subgroups are available. If you select a group or subgroup, the corresponding information and parameters are displayed in the right pane of the inspector window and can also be edited there.

  For S200 drives, mainly the drive objects used are specified in this subarea.

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

### Rotate & optimize S200

#### Overview

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> Users without these function rights either have read-only access or no access at all.

#### Structure: Control panel

The control panel is used for the control and monitoring of individual drives in online mode. You traverse drives with the control panel by specifying values. Depending on the operating mode, these are, for example, speed setpoints.

The following figure shows the various components of the control panel:

![S2x0 control panel](images/168263074827_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Control (drive can be controlled online using buttons) |
| ③ | Drive status (can be hidden online using an arrow) |
| ④ | Set/reset drive enable |
| ⑤ | Actual values (can be hidden online using an arrow) |

S2x0 control panel

> **Note**
>
> **Checking EPOS settings**
>
> As soon as the "Positioning" control mode is activated, the "Operating mode" drop-down list is added to the control panel.
>
> If the "Positioning" operating mode is set, selected EPOS functions can be tested via the control panel (see [Testing EPOS settings with the control panel](Commissioning%20SINAMICS%20S200%20drives.md#testing-epos-settings-with-the-control-panel)).

#### One Button Tuning

One Button Tuning is used to determine the optimum control parameters of the drive in online mode.

The following figure shows the various components of the "One Button Tuning" function view:

![S2x0 One Button Tuning](images/168261337355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Dynamic response settings via defined stages |
| ③ | Optimization result. Comparison of values before and after optimization (can be hidden online using an arrow). |
| ④ | Start measurement for optimization |
| ⑤ | Configuration/distance limit |
| ⑥ | Show whether optimization status successful/not successful |
| ⑦ | Stop/switch off measurement |
| ⑧ | Extended settings for selected parameters |

S2x0 One Button Tuning

### S200 guided quick startup

#### Overview

The "guided quick startup" is a commissioning wizard. You can use this to make the most important basic settings of an S200 drive.

> **Note**
>
> **Access rights**
>
> If protection (UMAC) is activated, you need corresponding function rights of your user account for access (see [Access control](User%20administration%20and%20security.md#access-control)).
>
> User without these function rights either have read-only access or no access at all.

#### Structure

![Example: Guided quick startup in offline mode](images/167536091403_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icon: Saves data powerfail-proof (in online mode) |
| ② | Icon: Restores the factory settings (in online mode) |
| ③ | Buttons: Start or exit editing mode (in online mode) |
| ④ | Buttons: Jump to the next or previous step. |
| ⑤ | Active quick startup step: Button is brightened |
| ⑥ | Inactive quick startup step: One of several possible steps |
| ⑦ | Detailed setting of active quick startup step. |
| ⑧ | Quick startup buttons:   - Back/Next: are always displayed. - Cancel/finish: only displayed in online mode. |

Example: Guided quick startup in offline mode

#### Status display after changes

Changes to individual settings affect other settings in the "guided quick startup". Status symbols indicate the change status of the particular step:

| Icon | Meaning |
| --- | --- |
| ![Status display after changes](images/155564453003_DV_resource.Stream@PNG-de-DE.png) | The system defaults in this step are valid. |
| ![Status display after changes](images/151783943947_DV_resource.Stream@PNG-de-DE.png) | The settings made in this step are valid.   The settings were made directly in this step, or are the consequences of settings in another step. |
| ![Status display after changes](images/152995660555_DV_resource.Stream@PNG-de-DE.png) | The program changed the settings in this step. Possible causes are:   - Subsequent changes were made in other steps, which are not automatically valid. - Subsequent changes have been made in the device configuration that affect the original settings.   Check the settings of this step. |

## Fundamentals

This section contains information on the following topics:

- [Permanently save the settings](#permanently-save-the-settings)
- [Restoring factory settings](#restoring-factory-settings)
- [Loading the configuration from the device to the project](#loading-the-configuration-from-the-device-to-the-project)
- [Loading the configuration from the project to the device](#loading-the-configuration-from-the-project-to-the-device)
- [Perform firmware update](#perform-firmware-update)
- [Setting signal interconnections](#setting-signal-interconnections)
- [Managing supplementary functions that require a license](#managing-supplementary-functions-that-require-a-license)
- [Using drive libraries](#using-drive-libraries)
- [Managing the parameter list](#managing-the-parameter-list)

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
- [Update the firmware from a memory card](#update-the-firmware-from-a-memory-card)
- [Updating the firmware via an online connection](#updating-the-firmware-via-an-online-connection)

#### Overview

##### Fundamentals

A firmware update is required if you want to use a new firmware version with an extended range of functions. Generally, several variants of a firmware update are available to you:

- [Firmware update via memory card](#update-the-firmware-from-a-memory-card)

  The firmware update is performed directly on the actuator using a memory card with new firmware.
- [Firmware update via online connection](#updating-the-firmware-via-an-online-connection)

  This firmware update is performed via the "Online & diagnostics" function view in Startdrive. The desired drive is accessed online.
- [Firmware update in the device configuration in the project](#optional-replace-drive)

  When creating the drive in the device configuration, a firmware is always assigned to the drive. If required, the firmware of the drive can be updated in the project via the "Replace device" function. Creating a new project is no longer necessary for updating the firmware.

  > **Note**
  >
  > **Is the firmware version the same in the drive and Startdrive?**
  >
  > Online connections between a Startdrive project and a drive are only possible when both communication partners have the same firmware version (see "[Checking the firmware version](#checking-the-firmware-consistency)").
  >
  > If your current Startdrive project uses an older firmware version than the drive, proceed as follows:
  >
  > - Call up the device configuration of the drive in the project.
  > - Call up the "Replace device" function in the device configuration. Replace the device with a device with identical power, but new/current firmware.

#### Update the firmware from a memory card

##### Overview

A firmware update is required if you want to use a new firmware version with an extended range of functions.

The available SINAMICS firmware versions are listed on this [Internet page](https://support.industry.siemens.com/cs/ww/en/view/109812409):

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

#### Updating the firmware via an online connection

##### Overview

As an alternative to an update using a memory card, you can also update the firmware using "Online & Diagnostics".

##### Requirements

- A backup is made before updating the firmware.
- The current firmware is saved in the file directory of your operating unit.
- There is a physical connection between the Ethernet interface of your operating unit and the Ethernet or PROFINET interface of your drive.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Required function rights](User%20administration%20and%20security.md#access-control))

##### Procedure

| 1. Call the [Diagnostics view](#overview-2). 2. In the secondary navigation of the function view select the "Functions > Firmware update" menu.     The "Firmware update" function view opens in the diagnostics view. The drive article number and the currently used firmware version are displayed in area "Online data". 3. Click the "Browse" button in the "Firmware loader" area.     A selection dialog opens. 4. Select the firmware file with the required version in the file system of your operating unit.     The firmware file is now displayed in the line with the same name in the "Firmware loader" area.     In fields "Firmware version" and "Status", check again that you have selected the required firmware version, and whether the firmware can be read. 5. Optional: Activate the option "Automatically restart the drive...".     In this case, after updating the firmware, you do not have to restart the drive manually. In this case, step 8 is omitted. 6. To start the update, click on "Start firmware update"     Confirmation dialog "Firmware update" is displayed. 7. Click on "OK" to load the firmware into the drive.    The status of the firmware update is displayed in the "Status" field. The new firmware is being installed. The process takes about 2 minutes.       | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | ![Procedure](images/164840824843_DV_resource.Stream@PNG-de-DE.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Procedure](images/164842006539_DV_resource.Stream@PNG-de-DE.png) | - | Firmware update complete | 8. Optional: If the option "Automatically restart the drive..." is not activated, then manually switch the drive off and on again.    The firmware of the connected DRIVE-CLiQ components is updated.        | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Procedure](images/146009085707_DV_resource.Stream@PNG-de-DE.png)  (0.5 Hz) | Firmware update of the connected components is in progress - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Procedure](images/146009098379_DV_resource.Stream@PNG-de-DE.png)  (2 Hz) | Component firmware update has been completed. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

The firmware has been updated.

Check in the Startdrive catalog information whether the required new firmware version is installed.

Call in secondary navigation in the "General > Catalog information" inspector window.

### Setting signal interconnections

#### Overview

SINAMICS drives use signal interconnections differently.

- High-end devices require extensive configuration options so that many functions can be interconnected with one another via signals. Interconnection parameters are marked using different icons. These icons are used to call the required interconnection dialogs.  
  For example for S120 or G220:

  | Icon | Name |
  | --- | --- |
  | ![Overview](images/145966680203_DV_resource.Stream@PNG-de-DE.png) | Binary signal sink |
  | ![Overview](images/145966842251_DV_resource.Stream@PNG-de-DE.png) | Binary signal source |
  | ![Overview](images/145966850699_DV_resource.Stream@PNG-de-DE.png) | Numerical signal sink |
  | ![Overview](images/145966871947_DV_resource.Stream@PNG-de-DE.png) | Numerical signal source |
- Simpler devices, where fast and simple commissioning is desirable, only use a restricted number of signal interconnections. This especially applies to SINAMICS S200 or S210.

  Generally, fixed values are specified instead, which in tests have proven themselves to be optimal values. Infrequently, however, signal interconnections are still required. For example, digital inputs or digital outputs generally require a signal interconnection.

  For SINAMICS S200 or S210 devices, signal interconnections are established in the function views using drop-down lists. Only the preferred interconnection options are listed in these drop-down lists. Example:

  ![Example: Simple signal interconnection for a digital output](images/172208763787_DV_resource.Stream@PNG-en-US.png)

  Example: Simple signal interconnection for a digital output

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

For information on the user interface, see also [Parameter view](#s200-parameter-view).

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
> - A "Security Wizard" usually appears when creating new drives in the project. Using this wizard, you can already make the most important security settings for this drive in the project when creating the drive.
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
2. [Create the device configuration in Startdrive offline](#manually-creating-a-device-configuration-offline)

   Optional: Making security settings for project and drive
3. [Make basic settings offline via the guided quick startup](Commissioning%20SINAMICS%20S200%20drives.md#guided-quick-startup)
4. [Load the project to the target device](#loading-the-configuration-from-the-project-to-the-device).
5. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
6. [Perform optimization](Commissioning%20SINAMICS%20S200%20drives.md#rotate-optimize-1)

**Result:**

The motor rotates.

### Variant 1: Basic parameter assignment online

The basic parameterization can also be carried out in online mode as an alternative to offline mode. This results in a slightly modified procedure:

The following steps are required:

1. [Create or open the project with Startdrive](#managing-a-startdrive-project).
2. [Create the device configuration in Startdrive offline](#manually-creating-a-device-configuration-offline)

   Optional: Making security settings for project and drive
3. [Downloading project data to the target device](#loading-the-configuration-from-the-project-to-the-device)
4. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
5. Make basic settings online via the guided quick startup in editing mode

   - [Make basic settings in quick startup screen forms](Commissioning%20SINAMICS%20S200%20drives.md#guided-quick-startup)
   - [Perform optimization](Commissioning%20SINAMICS%20S200%20drives.md#rotate-optimize-1)

**Result:**

The motor rotates.

### Variant 2: Basic parameter assignment together with a SIMATIC controller

If you want to commission the SINAMICS drive together with a SIMATIC control system, the optimum sequence for basic parameterization is as follows:

1. [Create or open the project with Startdrive](#managing-a-startdrive-project)
2. Create the device configuration in Startdrive offline

   - [Insert the SINAMICS drive into the project](#adding-a-drive)
   - Optional: Making security settings for project, drive and controller
   - [Completing motor data](#specifying-motor-and-encoder)
   - [Insert the SIMATIC controller into the project](#adding-a-controller-plc)
   - [Network the SIMATIC controller and drive](#networking-the-controller-plc-and-drive)
   - [Insert a technology object into the SIMATIC controller](#inserting-a-technology-object-into-the-simatic-s7-controller)
   - [Interconnect the technology object with the drive](#interconnecting-the-technology-object-and-sinamics-drive)
3. [Downloading project data to the target device](#loading-the-configuration-from-the-project-to-the-device)
4. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-target-device)
5. Make basic settings online via the guided quick startup in editing mode

   - [Make basic settings in quick startup screen forms](Commissioning%20SINAMICS%20S200%20drives.md#guided-quick-startup)
   - [Perform optimization](Commissioning%20SINAMICS%20S200%20drives.md#rotate-optimize)

**Result:**

The motor rotates.

## Configuring devices in the project

This section contains information on the following topics:

- [Managing a Startdrive project](#managing-a-startdrive-project)
- [Manually creating a device configuration offline](#manually-creating-a-device-configuration-offline)

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

### Manually creating a device configuration offline

This section contains information on the following topics:

- [Drive](#drive)
- [Motor and measuring system](#motor-and-measuring-system)
- [Optional: Control](#optional-control)

#### Drive

This section contains information on the following topics:

- [Adding a drive](#adding-a-drive)
- [Optional: Replace drive](#optional-replace-drive)
- [Perform detailed settings of the drive](#perform-detailed-settings-of-the-drive)

##### Adding a drive

###### Overview

You can add new drives either in the project view (see below) or in the portal view. For the latest generation of SINAMICS drives, you can already define the security settings to access the drive data when creating the drive.

###### Requirements

- A new project has been created.

  - Or -

  An existing project has been opened.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

To insert drives in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click "Drives" to display the available drives.

   ![Select a drive](images/160253908491_DV_resource.Stream@PNG-en-US.PNG)

   ![Select a drive](images/160253908491_DV_resource.Stream@PNG-en-US.PNG)

   Select a drive
3. Select the "SINAMICS S200" folder in path "SINAMICS drives/SINAMICS S".

   The following SINAMICS S200 drive types can be selected here:

   - S200 PN
   - S200 Basic PN

   One matching device is displayed for each performance class of an S200 type.
4. Select the required SINAMICS S200 drive.
5. Select the firmware version that is installed on your drive.
6. Enter a name and click "OK".

**Note**

If the version numbers (offline project in Startdrive compared with drive) do not match, it will not be possible to go online later. When creating, the current firmware version is always suggested. If required, you can change the version number using the "Version" drop-down list.

If you leave the "Device view" option activated, the device view opens automatically.

**Alternatively: Inserting a device via the network view or topology view**

Alternatively, you can also insert a drive via the network view or the topology view.

1. Open the network view.
2. Open the "Drives & starters" entry in the hardware catalog.
3. Open the "SINAMICS drives" entry in the hardware catalog and the corresponding subfolder of the required Control Unit.
4. Drag the drive from the hardware catalog and drop it into the network view or the topology view.

###### Result

The drive has been inserted. Then check the drive default settings in the inspector window and correct these [Detailed settings](#perform-detailed-settings-of-the-drive).

The motor and measuring system must then be defined.

##### Optional: Replace drive

###### Overview

In the device configuration and project tree of an S200 drive, you can replace the current device with a device at any time:

- with different power
- with identical power, but new/current firmware

When replacing the drive, previous configurations of the motor and/or the encoder are kept if both devices are compatible with one another.

###### Requirements

- A project has been created.
- An S200 Control Unit is inserted in the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Replacing a device via the project tree

1. In the project tree, select the drive to be replaced. Open shortcut menu "Change device".

   Dialog "Change device - S200 PN" opens:

   ![Changing the device using the project tree](images/171967864075_DV_resource.Stream@PNG-en-US.png)

   ![Changing the device using the project tree](images/171967864075_DV_resource.Stream@PNG-en-US.png)

   Changing the device using the project tree

   The data of the current drive are displayed on the top left. At the top right, the replacement devices that are applicable are displayed in a hardware catalog.
2. In the hardware catalog of dialog "Change device", select the replacement device required.

   Now, only the most important data of the new device are displayed at the center of the dialog in field "New device". You can compare this data with the data of the current device (left-hand side).

   If both drives are not fully compatible, then the corresponding information is displayed in the "Compatibility information" field. This can mean that you must possibly assign another motor if you still go ahead and accept the required replacement device.
3. Optional: If you want to use the same device but a different firmware, select the desired firmware version in the "New device" area in the "Version" drop-down list.
4. Click on "OK" to accept the new drive.

###### Replacing a device using the hardware catalog

1. Select the new S200 drive in the hardware catalog. In the device view, drag the drive to the placeholder for the current drive.

   Dialog "Change device - S200 PN" opens:

   ![Changing the device using the hardware catalog](images/171968636683_DV_resource.Stream@PNG-en-US.png)

   ![Changing the device using the hardware catalog](images/171968636683_DV_resource.Stream@PNG-en-US.png)

   Changing the device using the hardware catalog

   In the dialog, the most important data of the existing drive and the new drive are compared.

   If both drives are not fully compatible, then the corresponding information is displayed in the "Compatibility information" field. This can mean that you must possibly assign another motor if you still go ahead and accept the required replacement device.
2. Optional: If you want to use the same device but a different firmware, select the desired firmware version in the "New device" area in the "Version" drop-down list.
3. Click on "OK" to accept the new drive.

###### Result

The current drive is replaced by the required replacement device.

If the two drives are not completely compatible with one another, then in the device navigation, the placeholder for the motor is displayed unspecified. You must reassign an appropriate motor power.

##### Perform detailed settings of the drive

###### Overview

You can configure the following details for the SINAMICS S200 drive:

| Group | Settings (detailed menu) |
| --- | --- |
| General | - Product information   Name data - Catalog information   Brief description, description of the components included, firmware version used - Identification & Maintenance   Information and data to identify and localize a drive within a plant or system. |
| PROFINET interface [X150] | - General - Ethernet addresses   Subnet, IP address, subnet mask, PROFINET names - Telegram configuration   - Telegrams of the closed-loop drive control: Sending, receiving     For details, see [Telegram configuration](Communication%20and%20telegrams.md#telegram-configuration-via-profidrive) - Advanced options   - Interface options   - Media redundancy   - Clock cycle synchronization for local modules (isochronous mode)   - Real time settings   - Port [X150 P1] and port [X150 P2] - Shared device   Enables the connection of multiple controllers at the same PROFINET interface of the drive. |
| Module parameters | - Activation of channel diagnostics |
| Protection & Security | - Wizard for security settings - User Management & Access Control - Ports and protocols - Encryption of the drive data  For details, see [Higher-level security settings](User%20administration%20and%20security.md#security-default-settings-for-projects-as-of-sinamics-fw-v61) |
| Ethernet commissioning interface [X127] | - General - Ethernet addresses   Subnet, IP address, subnet mask |
| Time synchronization/Time | - Synchronization with an NTP server   If the drive is connected with a control system in the device configuration, option "Use PLC as NTP server" is automatically activated. If the drive is connected to a PLC, the IP address of the PLC is displayed. The following settings can be made:    - IP address (only if option "Use PLC as NTP server" is deactivated)   - Time zone of the NTP server (always) - No synchronization   In this case, no NTP synchronization is managed in the project. You can separately configure this synchronization for the drive in online mode using the Online & Diagnostics function "[Set time](#setting-the-time-of-day)". |
| Hardware settings  Power Module settings | - Output voltage |
| Web server | - Permit access to service interface [X127] via the HTTP protocol - Permit access to service interface [X127] via the HTTPS protocol - Enable access to the PROFINET interface [X150]. This is only possible as secure HTTPS connection.  These settings are redundant to the web server settings under "Ports and protocols". |

###### Requirements

- A new project has been created.

  - Or -

  An existing project has been opened.
- A SINAMICS S200 drive has been created in the project.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Select the SINAMICS S200 drive in the device view and open the inspector window.
2. In the secondary navigation of the inspector window, select the desired detail menu (see list in the summary).
3. Make the required detail settings in the white fields.   
   The detailed settings are preassigned with the factory setting.

   The gray fields are corrected automatically in accordance with their setting. Fields with a gray background cannot be edited directly.

###### Result

You have made the detailed settings for the drive in your device configuration. Save the settings in the project.

#### Motor and measuring system

This section contains information on the following topics:

- [Specifying motor and encoder](#specifying-motor-and-encoder)
- [Optional: Replacing the motor](#optional-replacing-the-motor)
- [Encoder details](#encoder-details)

##### Specifying motor and encoder

###### Overview

The drive that has just been inserted in the project has a placeholder for the required "1FL2" motor type. You must specify this placeholder in the configuration. An absolute encoder (singleturn or multiturn) is connected to the motor via a BiSS interface.

###### Requirements

- A project has been created.
- An S200 Control Unit is inserted in the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Procedure

1. Double-click on the white motor placeholder (MOT) in the drive. The inspector window is displayed.
2. Select "Motor - selection - 1FL2" entry in the secondary navigation in the Inspector window.
3. In the list, select the motor power rating based on the article number.

   With this selection, specify whether the motor should be equipped with a holding brake.

   By selecting the article number also define which absolute encoder type (singleturn or multiturn) you are using.

   ![Specifying the motor](images/164877750539_DV_resource.Stream@PNG-en-US.png)

   ![Specifying the motor](images/164877750539_DV_resource.Stream@PNG-en-US.png)

   Specifying the motor

   If the motor is equipped with a motor holding brake, then you can configure this later as part of the basic parameterization.

###### Result

The motor placeholder is assigned the data of the selected motor. The white area turns gray. Save the settings in the project.

![Specifying the motor and associated encoder](images/170758799883_DV_resource.Stream@PNG-en-US.png)

Specifying the motor and associated encoder

The motor has been added. The absolute encoder defined using the motor article number together with the encoder evaluation is automatically added.

##### Optional: Replacing the motor

###### Overview

For the S200 drive, the motor placeholder can be exchanged.

###### Requirements

- The drive is offline.
- A project has been created.
- An S200 Control Unit with an unspecified motor placeholder is inserted into the device configuration.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

###### Replacing a motor using the hardware catalog

1. Select the required motor type in the hardware catalog. Drag the corresponding placeholder in the device view onto the placeholder for the currently used motor type.

   Dialog "Replace device - 1Fxx synchronous motor" opens:

   ![Replacing the motor placeholder using hardware selection](images/165126629515_DV_resource.Stream@PNG-en-US.png)

   ![Replacing the motor placeholder using hardware selection](images/165126629515_DV_resource.Stream@PNG-en-US.png)

   Replacing the motor placeholder using hardware selection

   In the dialog, the most important data of the used motor type and the new motor type are compared.

   If the two types of motors are not fully compatible, the corresponding information is displayed in the "Compatibility information" field.
2. To accept the new motor type, click "OK".
3. Click on the unspecified motor in the device view.
4. If required, select the "Motor - Selection" entry in the secondary navigation in the Inspector window.
5. In the list, select your motor based on the article number.

   The motor placeholder is assigned the data of the selected motor. The white area turns gray. If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

###### Replacing a motor using the shortcut menu

1. Select the motor placeholder of the drive in the device configuration. Open shortcut menu "Change device".

   Dialog "Replace device - 1Fxx synchronous motor" opens:

   ![Manually changing the motor placeholder](images/165126500107_DV_resource.Stream@PNG-en-US.png)

   ![Manually changing the motor placeholder](images/165126500107_DV_resource.Stream@PNG-en-US.png)

   Manually changing the motor placeholder

   The data of the current motor type are displayed at the top left. The motor types that are applicable are displayed in a hardware catalog at the top right.
2. In the hardware catalog of dialog "Change device - 1Fxx synchronous motor", select the motor placeholder of the required motor type.

   Now, only the most important data of the new motor type are displayed at the center of the dialog in field "New device". You can compare this data with the data of the current motor type (left-hand side).

   If both motor types are not fully compatible, then the corresponding information is displayed in the "Compatibility information" field.
3. Click on "OK" to accept the motor type.
4. Click on the unspecified motor in the device view.
5. If required, select the "Motor - Selection" entry in the secondary navigation in the Inspector window.
6. In the list, select your motor based on the article number.

   The motor placeholder is assigned the data of the selected motor. The white area turns gray. If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

###### Result

The motor has been added. If you had already inserted and specified an encoder before replacing the motor, you must do this again at this point. When replacing the motor, the encoder is deleted from the device configuration, since the encoder settings always refer to the motor used.

##### Encoder details

This section contains information on the following topics:

- [Basics](#basics)
- [Encoder types](#encoder-types)

###### Basics

###### Overview

A distinction is made between motor encoders and machine encoders.

| Applications | Description |
| --- | --- |
| Motor encoder | Motor encoders are attached to the motor shaft so that the movement of the motor (angle of rotation, rotor position, etc.) can be measured directly. Motor encoders provide the speed actual value, which is fed into the closed-loop control (closed-loop speed and current control). For controllers with a high dynamic response, the speed actual value signal must also manifest an adequately high dynamic response. This is why it is important to use a high-quality motor encoder.   Preconfigured Siemens motors are already created with an encoder placeholder in the device view. You still have to define whether the encoder used is a singleturn encoder or a multiturn absolute encoder. SINAMICS S200 only uses motor encoders.   The encoders configured in this way are then intended as motor encoders (measuring system 1).      ![Motor encoder](images/145963586315_DV_resource.Stream@PNG-de-DE.png)   Motor encoder |
| Machine encoder (not for S200) | Machine encoders are installed in the machine. With machine encoders, you synchronize the speed of one belt with another belt or determine the position of a workpiece. As these values infrequently need to be available in the fast speed controller or current controller clock cycle, even basic mounted encoders can be used.      ![Machine encoder](images/145963748363_DV_resource.Stream@PNG-de-DE.png)   Machine encoder |

###### Encoder types

###### Overview

In its first expansion stage, SINAMICS S200 uses the following encoder types:

- Singleturn absolute encoder with 17 or 21-bit resolution and BiSS interface
- Multiturn absolute encoder with 21-bit resolution, 12-bit rotational resolution and BiSS interface

###### Absolute encoders

Absolute encoders provide the position value as an absolute numerical value. Initial homing as is the case for incremental encoders is not necessary as the numerical value is unique over the range of resolution of the absolute encoder.

The absolute numerical value is transferred from the absolute encoder to the drive via the BiSS (Bidirectional Serial Synchronous) interface. For rotary encoders, a distinction is made between the following variants:

- Encoders, which can only resolve one revolution and then start again at 0 (**singleturn**).
- Encoders, which can resolve several revolutions (**multiturn**).

**Absolute encoder adjustment**

The absolute position value supplied by an absolute encoder must be assigned to the associated mechanical position via an absolute encoder adjustment. The absolute encoder adjustment only has to be performed once. The absolute encoder adjustment results in an absolute value offset saved permanently even when the controller is switched off and on again. The absolute encoder adjustment is performed on the positioning axis / synchronous axis.

**Singleturn absolute encoders**

For a singleturn absolute encoder, absolute position values are assigned only to the angular positions within one revolution. This means that the angular position is known only within one revolution. However, in order to determine the position values also over multiple revolutions, the revolutions of the encoder for the positioning axis or synchronous axis are accumulated.

When the drive is switched off, the revolutions counted for a positioning axis or synchronous axis are saved permanently. When the drive is switched on again, the permanently stored number of revolutions is included in the calculation of the actual position. To ensure that an axis continues travel from the correct position after switching on, it must be guaranteed that the singleturn absolute encoder does not turn more than half a revolution when switched off.

The singleturn absolute encoder used in the drive has a 21-bit resolution and therefore provides 2 (= 2097152) absolute position values for one revolution. Singleturn rotary transducers have a measuring range of 360 degrees.

**Multiturn rotary transducers**

For a multiturn rotary transducer, an absolute position value is formed from each angle position within a revolution together with the number of complete revolutions. Unlike its singleturn equivalent, the multiturn rotary transducer may turn more than half a revolution when switched off.

The singleturn absolute encoder used in the drive has a 21-bit resolution and a 12-bit rotational resolution. It therefore resolves a revolution with 2 (2097152) angle positions and 2 (4096) revolutions. Multiturn rotary transducers have a measuring range of n x 360 degrees. Where n represents the number of revolutions that the encoder can resolve.

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

The procedure for "Going online" is subsequently explained based on the example of a standard S200 Control Unit.

> **Note**
>
> **Comply with the installation and industrial security guidelines - cell protection concept**
>
> - EtherNet commissioning interface X127:
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

![S200 PN interfaces](images/166050543115_DV_resource.Stream@PNG-en-US.png)

S200 PN interfaces

#### Trusted device

For secure communication between the operating unit and the drive, the drive must be classified as "trusted". Without this classification, online access is not possible. A device is considered trusted and therefore secure if it is assigned a digital certificate accepted by Startdrive.

See the page "[Secure communication with Trusted Devices](User%20administration%20and%20security.md#secure-communication-with-trusted-devices-from-sinamics-firmware-v61)" on how to assign a digital certificate to the drive.

#### Requirements

- The drive must be classified as a "trusted" device by a digital certificate.
- The interfaces you want to use for a connection must be enabled for access in the project's general security settings.

  For details, see page "[General security settings - ports and protocols](User%20administration%20and%20security.md#activating-ports-and-protocols-features)".

#### IP addresses

**Control Unit (hardware)**

- **EtherNet commissioning interface X127**: For X127, an IP address and a subnet mask have already been assigned on the Control Unit in the factory:

  - IP address: 169.254.11.22
  - Subnet mask: 255.255.0.0
- **PROFINET interface X150**: For X150, an IP address and a subnet mask have already been assigned on the Control Unit in the factory:

  - IP address: 0.0.0.0
  - Subnet mask: 0.0.0.0
- First wire your PC to the appropriate interface on the Control Unit.

**Project**

An S210 drive is created with the following IP addresses in a project in the TIA Portal:

- **EtherNet commissioning interface X127**: The addresses correspond to the addresses that have already been assigned in the drive unit.

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

- Perform a firmware update on your drive unit (see "[Update the firmware from a memory card](#update-the-firmware-from-a-memory-card)").

  - OR -
- Perform a device replacement in the Startdrive project for the affected drive. Replace the drive with a drive with the same power but new firmware.

  - OR -
- If a device replacement is not possible in the project:   
  Create a new Startdrive project for your drive unit in Startdrive and set a newer firmware version for the Control Unit in the new project (see "[Optional: Replace drive](#optional-replace-drive)").

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

- [Overview](#overview-2)
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

  For detailed information on these functions, refer to the "[Function status](Commissioning%20SINAMICS%20S200%20drives.md#function-status)" section.
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

- [Receive direction S200 telegrams](#receive-direction-s200-telegrams)
- [Send direction S200 telegrams](#send-direction-s200-telegrams)

###### Receive direction S200 telegrams

###### Description

As standard, the components and interconnections of PROFIdrive telegrams in the receive direction for the converter are displayed in this diagnostics view (e.g. 105 or 750).

You can use the telegram configuration (![Description](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "Supplementary data" area.

###### Telegram structure (S200)

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

The following information of the displayed telegrams is displayed:

| Telegram type | PZD | Display of the value | Format switchover | Control words |
| --- | --- | --- | --- | --- |
|  | **The numbering and arrangement of the process data.** | **Value of the process data (PZD)** | **The value of the process data is switched to a different representation (hex, bin, dec).** | **List of the control words that are transmitted in the telegram.** |
| PROFIdrive  1, 2, 3, 5, 7, 9, 102, 105, 111, 112 | X | X | X | X |
| Torque supplementary telegram  750 | X | X | X | X |

###### Send direction S200 telegrams

###### Description

As standard, the components and interconnections of PROFIdrive telegrams in the send direction for the converter are displayed in this diagnostics view (e.g. 105 or 750).

You can use the telegram configuration (![Description](images/148900571915_DV_resource.Stream@PNG-de-DE.PNG)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "Supplementary data" area.

###### Telegram structure (S200)

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

The following information of the displayed telegrams is displayed:

| Telegram type | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- |
|  | **List of the status words that are transferred in the telegram.** | **Value of the process data (PZD)** | **The value of the process data is switched to a different representation (hex, bin, dec).** | **Numbering and arrangement of the process data.** |
| PROFIdrive  1, 2, 3, 5, 7, 9, 102, 105, 111, 112 | X | X | X | X |
| Torque supplementary telegram  750 | X | X | X | X |

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

   The wear of the replaced fan is still displayed in the "Wear meter" field ([r0277](SINAMICS%20Parameter%20S200%20Basic%20PN.md#r02770-power-unit-heat-sink-fan-wear-counter)).
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
- [Performing a firmware update](#update-the-firmware-from-a-memory-card)
- [Assigning a PROFINET device name](#assigning-profinet-device-names-1)
- [Entering the password for encrypting drive data](User%20administration%20and%20security.md#configuring-the-encryption-online-diagnostics)
- [Resetting PROFINET interface parameters](#resetting-profinet-interface-parameters-1)
- [Setting the time](#setting-the-time-of-day)
- [Using functions subject to license](#managing-supplementary-functions-that-require-a-license)

You call the individual functions in the secondary navigation of the diagnostics view.

###### Requirements

- There is an online connection between the drive and the operating unit.

  The direct functions can only be performed in online mode.
- With protection activated (UMAC):

  Your user account has the corresponding function rights (see [Access control](User%20administration%20and%20security.md#access-control))

##### Assigning an IP address

###### Overview

Enter the IP address of the drive and the IP of the subnet mask in the diagnostics view "Online & diagnostics".

> **Note**
>
> **Changing an existing IP address**
>
> - If the device already has an IP address, run function "[Restore factory settings](#restoring-factory-settings-1)" to reset the IP address to 0.0.0.0.
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

---

**See also**

[Engineering rights](User%20administration%20and%20security.md#engineering-rights)

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

---
title: "Configuring SINAMICS S210 drives"
package: StdrS210ConfenUS
topics: 90
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring SINAMICS S210 drives

This section contains information on the following topics:

- [SINAMICS S210 drive system](#sinamics-s210-drive-system)
- [Startdrive user interface](#startdrive-user-interface)
- [Basics](#basics)
- [Sequence of a device configuration in S210](#sequence-of-a-device-configuration-in-s210)
- [Adding and assigning parameters](#adding-and-assigning-parameters)
- [Establishing an online connection to the drive](#establishing-an-online-connection-to-the-drive)
- [Diagnostics](#diagnostics)

## SINAMICS S210 drive system

This section contains information on the following topics:

- [System overview](#system-overview)
- [The scope of supply for the system components](#the-scope-of-supply-for-the-system-components)

### System overview

The drive system comprises the following system components tailored to one another:

- SINAMICS S210 converter
- SIMOTICS S-1FK2 motor
- OCC MOTION-CONNECT cable

The converter and the motor are optimally tailored to one another and are intended for use with a higher-level controller (PLC). Connection to the controller is via PROFINET:

Prefabricated MOTION-CONNECT cables in various lengths are available to simply connect the motor to the converter and to ensure safe and reliable operation.

#### System overview

![System overview](images/148017496715_DV_resource.Stream@PNG-en-US.png)

#### Interface overview

![Interface overview](images/148017501579_DV_resource.Stream@PNG-en-US.png)

#### More information

You can now find exhaustive information on the topic of "S210 converters" for downloading from the Siemens "Industry Online Support" website on the internet.

You will find the most important information bundled in the "SINAMICS/SIMOTICS SINAMICS S210 servo drive system" operating instructions.

[Download](https://support.industry.siemens.com/cs/ww/en/view/109771824):

There you can find detailed information about combinations of motors, converters and the associated connecting cables.

### The scope of supply for the system components

You must order the components individually.

#### Motor

The motor scope of delivery includes:

- A "Safety instructions" sheet
- A sheet referencing links to product information

#### Converter

The converter scope of delivery includes:

- The Quick Installation Guide (English)
- Shield plate
- A warning label for affixing in the control cabinet
- The following connectors:

  - X1: Line connection and external braking resistor (jumper for internal braking resistor is enclosed.)
  - X2: Motor connection
  - X107: Motor holding brake
  - X124: 24 V DC supply voltage
  - X130: Connector for digital inputs

#### MOTION-CONNECT cable (OCC cable)

The scope of supply for the prefabricated MOTION-CONNECT cables includes:

- The MOTION-CONNECT cable with assembled connectors for connecting to motors and encoders
- A shield clamp for the connection of the shield to the shield plate of the converter
- A safety data sheet

#### Optional components

- Memory card

  A memory card is required for data backups, for series commissioning, for firmware updates and, in general, for functions requiring a license. It is not included in the scope of delivery and must be ordered separately.

## Startdrive user interface

This section contains information on the following topics:

- [S210 hardware catalog](#s210-hardware-catalog)
- [Device configuration S210](#device-configuration-s210)
- [S210 function view](#s210-function-view)
- [S210 parameter view](#s210-parameter-view)
- [S210 inspector window](#s210-inspector-window)
- [Rotate & optimize screen forms S210](#rotate-optimize-screen-forms-s210)

### S210 hardware catalog

#### Performance groups and components

The available SINAMICS S210 performance groups are available in the hardware catalog as follows:

![SINAMICS S210 hardware catalog](images/148017567627_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | SINAMICS S210 converter;   Available performance groups of the type SINAMICS S210 |
| ② | Motors;   Measuring systems are already assigned automatically to these motors. |

SINAMICS S210 hardware catalog

### Device configuration S210

This section contains information on the following topics:

- [Device view](#device-view)
- [Network view](#network-view)
- [Topology view](#topology-view)

#### Device view

The device view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assigning device parameters
- Configuring and assigning module parameters
- Editing the names of devices and modules

Configure the drive line-up in the "Device view". You can call the device view by double-clicking the "Device configuration" entry in the project tree.

The device overview provides a tabular overview of all configured components and their data.

##### Structure

The following figure shows an overview of the device view (the DRIVE-CLiQ editor).

![Device view](images/148017571723_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control Unit |
| ② | Bus interface, Ethernet in this case |
| ③ | DRIVE-CLiQ interface |
| ④ | DRIVE-CLiQ connection |
| ⑤ | Motor |
| ⑥ | Encoder |
| ⑦ | Encoder evaluation |

Device view

##### Toolbar

You can switch between the devices in your project in the device view using the drop-down list in the toolbar. The following functions are also available in addition to the drop-down list for device selection:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147991859723_DV_resource.Stream@PNG-en-US.png) | Switches to the network view. The device view can switch between the existing devices using the drop-down list. |
| ![Toolbar](images/147991883403_DV_resource.Stream@PNG-en-US.png) | Show the area of unplugged modules. |
| ![Toolbar](images/147991722635_DV_resource.Stream@PNG-en-US.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/147991932683_DV_resource.Stream@PNG-en-US.png) | Show module labels. You can edit the labeling directly in the device view: Select the required labeling and then click on the selected text field or press [F2]. |
| ![Toolbar](images/147991777803_DV_resource.Stream@PNG-en-US.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/147991788683_DV_resource.Stream@PNG-en-US.png) | You can use the Zoom icon to zoom in (+) or out (-) incrementally or to drag a frame around an area to be enlarged. With signal modules, you can recognize the address labels of the I/O channels from a zoom level of 200% or higher. |
| ![Toolbar](images/147991799563_DV_resource.Stream@PNG-en-US.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/147991823243_DV_resource.Stream@PNG-en-US.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

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

The network view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assigning device parameters
- Networking devices with one another
- Editing the device names

##### Structure

The network view is opened via the "Devices & networks" entry in the project navigation.

![Network view](images/148017575819_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Drive that is assigned as the IO device of a higher-level controller via fieldbus (in this case PROFINET IO). |
| ② | Fieldbus (in this case, PROFINET IO) |
| ③ | Higher-level controller, a SIMATIC S7-1500 in this case, that is configured as IO controller. |
| ④ | Data from drive and controller |

Network view

The specific parameters of the selected element are displayed in the inspector window.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147992020107_DV_resource.Stream@PNG-en-US.png) | Mode to network devices. |
| ![Toolbar](images/147992030987_DV_resource.Stream@PNG-en-US.png) | Mode to create connections. You can use the adjacent drop-down list to set the connection type. |
| ![Toolbar](images/147991722635_DV_resource.Stream@PNG-en-US.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/147992052747_DV_resource.Stream@PNG-en-US.png) | Show interface addresses. You can edit the addresses for the MPI, PROFIBUS and Ethernet interfaces directly in the network view: Select the required address and then click on the selected address field or press [F2]. |
| ![Toolbar](images/147991777803_DV_resource.Stream@PNG-en-US.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/147991799563_DV_resource.Stream@PNG-en-US.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/147991788683_DV_resource.Stream@PNG-en-US.png) | You can zoom in (+) or zoom out (-) the view in increments using the Zoom icon or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/147991823243_DV_resource.Stream@PNG-en-US.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

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

The topology view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Displaying the Ethernet topology
- Configuring the Ethernet topology
- Identifying and minimizing differences between the desired and actual topology
- Editing the device names

##### Structure

The following figure provides an overview of the topology view.

![Topology view](images/148017579915_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Changeover switch: device view / network view / topology view |
| ② | Topology view toolbar |
| ③ | Graphic area of the topology view |
| ④ | Overview navigation |
| ⑤ | Table area of the topology view (topology overview) |

Topology view

You can use your mouse to change the split between the graphic and table areas of the topology view. The division can be changed between horizontal and vertical using a button in the toolbar. To change the position of the split, click between the graphic and the table areas and change the spacing by moving the divider to the left or right while keeping the mouse button pressed. The Speedy Splitter (the two small arrow keys) allows you to use a single click to minimize the table view, maximize the table view or restore the last selected split.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147991722635_DV_resource.Stream@PNG-en-US.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/147992103307_DV_resource.Stream@PNG-en-US.png) | Changes the position of the devices in the topology view so that the new position is as close as possible to the position in the network view. |
| ![Toolbar](images/147991777803_DV_resource.Stream@PNG-en-US.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/147991788683_DV_resource.Stream@PNG-en-US.png) | You can zoom in (+) or zoom out (-) the view in increments using the Zoom icon or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/147991799563_DV_resource.Stream@PNG-en-US.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |

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

### S210 function view

You parameterize the drive using a graphical user interface in the "Function view". The individual masks (screen forms) are based on function diagrams and contain the required parameters.

> **Note**
>
> **All parameters**
>
> You can find all parameters of the drive in the "[Parameter view](#s210-parameter-view)". Experts can then comprehensively parameterize the drive. However, the parameter view can only be called for the parameter assignment. The parameter view is not offered for commissioning.

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

#### Structure of the masks (screen forms)

The following figure shows an example of a mask (screen form) structure:

![S210 function view; example](images/155230562187_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icon: Saves data retentively (in online mode) |
| ② | Icon: Restores the factory settings (in online mode) |
| ③ | Secondary navigation |
| ④ | Icon: Activates editing of the screen form in online mode |
| ⑤ | Icon: Saves the editing of the screen form in online mode |
| ⑥ | Boxes: Input of parameters |
| ⑦ | Boxes: Display parameters |
| ⑧ | Button: Shows dialogs or subordinate screen forms for parameter assignment. |

S210 function view; example

### S210 parameter view

The "Parameter view" (expert list) provides a clearly organized display of the parameters available for the device. For the "Parameter assignment", you can switch the working area between the "[Function view](#s210-function-view)" and the "Parameter view".

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

> **Note**
>
> The "Parameter view" is not available for "Rotate & optimize".

SINAMICS uses two types of parameters:

- Display parameters

  They are preceded by the letter "r". You cannot change the value of these parameters. S210 has many r parameters.
- Adjustable parameters

  They are preceded by the letter "p". You can change the value of these parameters within a defined range.

> **Note**
>
> **Locked parameters**
>
> Parameters can be locked in the parameter view to prevent changes from being made. In this case, they are identified by the![Figure](images/147992365067_DV_resource.Stream@PNG-en-US.PNG) icon. Parameters are always locked in the following cases:
>
> - When the parameters can only be changed online but not offline. In this case, the![Figure](images/147992365067_DV_resource.Stream@PNG-en-US.PNG) icon disappears as soon as you go online.
>
>   If the lock icon is also visible online, however, the following causes may be more likely:
> - When the parameter was set in a previous basic parameterization (such as in the device configuration) and any change to the parameter would subsequently have an effect on the structure.
> - When they are not intended to be changed manually by the user, for example, because they are configured by other programs (such as a controller).
> - When they are generally only going to be configured via screen forms in Startdrive. The display of these parameters in the parameter view is merely for the sake of clarity in this case.

#### Parameter display

The fields of the individual parameters are displayed in the list in color as follows:

| Editing level | Offline color | Online color |
| --- | --- | --- |
| Read only | Gray | Pale orange |
| Read/write | White | Orange |

#### Structure of the parameter view

The following figure shows the structure of the parameter view:

![S210 parameter view](images/148017639691_DV_resource.Stream@PNG-en-US.png)

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

S210 parameter view

#### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147992381835_DV_resource.Stream@PNG-en-US.png) | Expands or reduces all secondary navigation nodes. |
| ![Toolbar](images/147992385803_DV_resource.Stream@PNG-en-US.png) | Expands or reduces all nodes below the selected node. |
| ![Toolbar](images/147992389771_DV_resource.Stream@PNG-en-US.png) | Icon: Compares the parameters of the drive object with another parameter set.   - In offline mode, the parameters are compared to the factory settings by default. - In online mode, the parameters are compared to the offline settings by default. - The comparison can also be deactivated again. |
| ![Toolbar](images/147992406539_DV_resource.Stream@PNG-en-US.png) | Starts a CSV export: Save all displayed parameters in a CSV file. Save all parameters of the drive object in a CSV file. |
| ![Toolbar](images/147992410507_DV_resource.Stream@PNG-en-US.png) | Saves the parameters retentively (copy RAM to ROM). |
| ![Toolbar](images/147992414475_DV_resource.Stream@PNG-en-US.png) | Restores the factory settings. |

### S210 inspector window

The properties and parameters of a selected object are displayed in the Inspector window. The properties and parameters can be edited. For example, new unspecified S210 drive objects inserted in the device view can be specified.

#### Structure

The information parameters in the Inspector window are split up into various information types, which are displayed as main and secondary tabs in the Inspector window:

![Example: S210 Inspector window](images/148017700107_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary tab: In this example, the main "Properties" tab |
| ② | Main tab: Properties, information, diagnostics |

Example: S210 Inspector window

#### Subdivision of the "Properties" area

There are further subareas for each type of information that can be displayed via secondary tabs.

The most important type of information for SINAMICS S210 drives is the "Properties" area. The following secondary tabs are displayed in this area:

- General

  Display of the properties and settings of the drive device, drive object, or the hardware component. You can edit the settings and parameters here. The left pane of the Inspector window contains the secondary navigation. Information and parameters are arranged there in groups. If you click the arrow symbol to the left of the group name, you can expand the group if subgroups are available. If you select a group or subgroup, the corresponding information and parameters are displayed in the right pane of the Inspector window and can also be edited there.

  For S210 drives, mainly the drive objects used are specified in this subarea.
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

#### Showing or enlarging the Inspector window

There are several options available for showing (hiding) the Inspector window:

1. Use the regular window icons (top right-hand side in the header of the window).

   - Or -
2. Select a non-specified component in the device view and open the "Properties" shortcut menu.

The Inspector window is displayed only partially in Startdrive when called, due to lack of space. Display of the Inspector window can be maximized (minimized) for specification of the components:

1. To do so, double-click the header of the Inspector window (gray bar).

### Rotate & optimize screen forms S210

#### Requirement

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

#### Control panel

The control panel is used for the control and monitoring of individual drives. You traverse drives with the control panel by specifying values. Depending on the operating mode, these are, for example, speed setpoints.

The following figure shows the various components of the control panel:

![Startdrive S210: Control panel](images/168727593227_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Control drive |
| ③ | Drive status |
| ④ | Drive OFF |
| ⑤ | Set/reset drive enable |
| ⑥ | Actual values |

Startdrive S210: Control panel

#### One Button Tuning

One Button Tuning serves to establish the optimum control parameters of the drive.

The following figure shows the various components of the "One Button Tuning" screen form:

![Startdrive S210: One Button Tuning](images/168727597579_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Dynamic response settings via defined stages |
| ③ | Result of tuning. Comparison of values before and after tuning. |
| ④ | Start/stop optimization for One Button Tuning |
| ⑤ | Configuration/distance limit |
| ⑥ | Status of One Button Tuning |
| ⑦ | Advanced settings for selected parameters |

Startdrive S210: One Button Tuning

## Basics

This section contains information on the following topics:

- [Permanently save the settings](#permanently-save-the-settings)
- [Restoring factory settings](#restoring-factory-settings)
- [Loading project data from a drive](#loading-project-data-from-a-drive)
- [Loading the project data to the drive unit](#loading-the-project-data-to-the-drive-unit)
- [Updating the firmware](#updating-the-firmware)
- [Using parameter lists](#using-parameter-lists)
- [Licensing](#licensing)
- [Using drive libraries](#using-drive-libraries)

### Permanently save the settings

#### Overview

Parameterizations of your drive are generally volatile and are lost when the drive is switched off.

To permanently save settings, you have the following options:

- Saving settings in the project.
- Saving settings (offline/online) on the memory card of the converter.

#### Requirement

- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Saving settings only in the project

In Startdrive, settings are predominantly made via screen forms.

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

In the function view for the active Startdrive project, click on the ![Saving online data in non-volatile storage](images/147992784395_DV_resource.Stream@PNG-en-US.png) icon (Retentively save data of the complete device).

The current project settings are stored non-volatile on the memory card of the drive.

#### Saving offline data in non-volatile storage

For storing in a power-independent manner, it is important that the settings made are not only saved in the project on the PC, but are also stored permanently on the memory card of the drive (also known as "Save retentively" or "Copy RAM to ROM"). An online connection must be established to the drive for this purpose.

1. Establish an [online connection](#establishing-an-online-connection-to-the-drive) to your drive.
2. Load the project data into your drives.
3. Click the ![Saving offline data in non-volatile storage](images/147992784395_DV_resource.Stream@PNG-en-US.png) icon in the function view of the active Startdrive project.

   The current project settings are stored non-volatile on the memory card of the drive.

### Restoring factory settings

#### Requirement

- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Procedure

In the online mode, you can restore the factory settings for the drive control.

1. Establish an [online connection](#establishing-an-online-connection-to-the-drive) to your drive unit.
2. Click the ![Procedure](images/147992822667_DV_resource.Stream@PNG-en-US.png) icon in the function view of the active Startdrive project.

   The factory settings are restored.

### Loading project data from a drive

#### Requirements

- A project is open.
- The hardware configuration and software to be loaded must be compatible with the Startdrive. If the data on the device was created with a previous program version or with a different configuration software, please make sure they are compatible.

#### Uploading project data of a device

To load the project data from a drive into your Startdrive project, proceed as follows:

1. Call the "Upload from device (software)" shortcut menu or click the ![Uploading project data of a device](images/147992848907_DV_resource.Stream@PNG-en-US.png) icon (Upload from device) in the toolbar.

   The "Upload preview" dialog opens. Startdrive checks whether all requirements for loading have been met. In the event that not all of the requirements have been met, then these are displayed as messages in the dialog.

   ![Example: Upload from device](images/147992865803_DV_resource.Stream@PNG-en-US.png)

   ![Example: Upload from device](images/147992865803_DV_resource.Stream@PNG-en-US.png)

   Example: Upload from device
2. Check the alarms in the "Upload preview" dialog, and select the necessary actions in the "Action" column.

   As soon as uploading becomes possible, the "Upload from device" button is enabled.
3. Click the "Upload from device" button.

   The loading operation is performed.

**Result**

The project data has been loaded from the drive into your Startdrive project on the PC.

---

**See also**

[Establishing an online connection to the drive](#establishing-an-online-connection-to-the-drive)

### Loading the project data to the drive unit

#### Overview

In order to set up your project, you need to load the project data you generated offline on the connected drive units. This project data is generated, for example when configuring hardware, networks, and connections or when programming the user program or when creating recipes.

#### Requirements

- The project data is consistent.
- Each drive unit to be loaded can be accessed online.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Procedure

To download the project data to the drive unit in online mode, proceed as follows:

1. Select one or more drive units in the project navigation.
2. Open the "Download to device" shortcut menu or click the ![Procedure](images/147992929931_DV_resource.Stream@PNG-en-US.png) icon (Download to device) in the toolbar.

   - If you have already established an online connection, the "Load preview" dialog opens. This dialog displays alarms and proposes actions necessary for loading.
   - If you have not yet established any online connection, the "Extended loading" dialog opens and you must first select the interfaces with which the online connection to the device should be established. You have the option of showing all compatible devices by selecting the corresponding option and clicking the "Start search" command.

     Detailed information about going online can be found at "[Establishing an online connection to the drive](#establishing-an-online-connection-to-the-drive)".
3. Check the messages in the "Load preview" dialog. Activate the required actions in the "Action" column to perform a secure download.

   ![Example: Load preview](images/147992933899_DV_resource.Stream@PNG-en-US.png)

   ![Example: Load preview](images/147992933899_DV_resource.Stream@PNG-en-US.png)

   Example: Load preview

   As soon as downloading becomes possible, the "Load" button is enabled.
4. Click "Load".

   The loading operation is performed. If there is a need for synchronization, the system automatically displays the "Synchronization" dialog. This dialog displays messages and suggests actions that are needed for the synchronization. You have the option of performing these actions or forcing the download without synchronization by clicking "Force download to device". If you have performed the suggested actions, you will be asked whether you want to continue with the download. The "Load results" dialog then opens. In this dialog, you can check whether the load task was successful and select any further actions.
5. Click "Finish".

**Result**

The selected project data has been downloaded to the drive units.

> **Note**
>
> **Upload from device**
>
> Conversely, the project data of a selected drive unit can also be uploaded into your Startdrive project on your PC. Proceed as described in "[Loading project data from a drive](#loading-project-data-from-a-drive)".

### Updating the firmware

#### Description

The firmware of the SINAMICS S210 drive system is distributed throughout the system. It is located on the Control Unit and in each individual DRIVE-CLiQ component.

A firmware update is required if you want to use a new firmware version with an extended range of functions.

You can find the available SINAMICS S210 firmware versions on this [website](https://support.industry.siemens.com/cs/ww/en/view/109744577):

> **Note**
>
> **Is the firmware version the same in the drive unit and Startdrive?**
>
> ONLINE connections between a Startdrive project and a drive unit are only possible when both communication partners have the same firmware version (see "[Checking the firmware version](#going-online)").
>
> - If your current Startdrive project is working with an older firmware version than the drive unit, create a new project.
> - Set the firmware version of the Startdrive project to the latest updated version of the drive unit and apply all other settings from the old project.   
>   If you are still using an old Startdrive version, it may be necessary to install a new Startdrive version that supports the firmware version.

#### Requirement

- For an update via an online connection:   
  Physical connection between the Ethernet interface of your PG/PC and the Ethernet or PROFINET interface of your drive.

#### Updating the memory card

| 1. Disconnect your drive unit. 2. Remove the memory card with the old firmware version. 3. Overwrite the memory card with the new firmware version. 4. Insert the memory card with the new firmware version. 5. Switch on your drive unit again.     The new firmware is being installed. This may take up to 5 minutes and longer. The update is complete when both LEDs flash red synchronously at 1 Hz.       | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Updating the memory card](images/147993054859_DV_resource.Stream@PNG-en-US.png) | ![Updating the memory card](images/147993058955_DV_resource.Stream@PNG-en-US.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Updating the memory card](images/147993063051_DV_resource.Stream@PNG-en-US.png) | ![Updating the memory card](images/147993063051_DV_resource.Stream@PNG-en-US.png) | Synchronous flashing of LEDs (1 Hz): Converter is waiting for the power supply to be disconnected and reconnected after the firmware update. | 6. Turn the drive unit off and on again.     The firmware of the connected DRIVE-CLiQ components is updated. A restart may be required to complete the update (see Startdrive alarm messages).       | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Updating the memory card](images/147993058955_DV_resource.Stream@PNG-en-US.png)  (0.5 Hz) | Firmware update of the connected DRIVE-CLiQ components in progress. - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Updating the memory card](images/147993067147_DV_resource.Stream@PNG-en-US.png)  (2 Hz) | Firmware update of the DRIVE-CLiQ components is complete. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | 7. Check in the Startdrive catalog information whether the required new firmware version is installed.     Call in secondary navigation in the "General > Catalog information" Inspector window. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Performing an update via online connection

| 1. Call the [Diagnostics view](#overview-4) . 2. In the secondary navigation of the function view select the "Functions > Firmware update" menu.     The "Firmware update" screen form opens in the diagnostics view. 3. Click the "Browse" button in the "Firmware loader" area.     A selection dialog opens. 4. Select the firmware file in the required version in the file system of your PC/PG.     The firmware file is now displayed in the line with the same name in the "Firmware loader" area.     Check once again in the "Firmware version" field whether you have selected the required firmware version. 5. To start the update, click the "Perform update" button.     The status of the firmware update is displayed in the "Status" field. The new firmware is being installed. This may take up to 5 minutes and longer. The update is complete when both LEDs flash red synchronously at 1 Hz.       | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Performing an update via online connection](images/147993054859_DV_resource.Stream@PNG-en-US.png) | ![Performing an update via online connection](images/147993058955_DV_resource.Stream@PNG-en-US.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Performing an update via online connection](images/147993063051_DV_resource.Stream@PNG-en-US.png) | ![Performing an update via online connection](images/147993063051_DV_resource.Stream@PNG-en-US.png) | Synchronous flashing of LEDs (1 Hz): Converter is waiting for the power supply to be disconnected and reconnected after the firmware update. | 6. Turn the drive unit off and on again.    The firmware of the connected DRIVE-CLiQ components is updated. A restart may be required to complete the update (see Startdrive alarm messages).       | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Performing an update via online connection](images/147993058955_DV_resource.Stream@PNG-en-US.png)  (0.5 Hz) | Firmware update of the connected DRIVE-CLiQ components in progress. - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Performing an update via online connection](images/147993067147_DV_resource.Stream@PNG-en-US.png)  (2 Hz) | Firmware update of the DRIVE-CLiQ components is complete. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | 7. Check in the Startdrive catalog information whether the required new firmware version is installed.    Call in secondary navigation in the "General > Catalog information" Inspector window. |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Using parameter lists

This section contains information on the following topics:

- [Editing the parameter list](#editing-the-parameter-list)
- [Comparing parameters](#comparing-parameters)
- [Using user-defined parameter lists](#using-user-defined-parameter-lists)

#### Editing the parameter list

##### Overview

The parameter list provides the following functions:

- Monitoring and editing parameter values
- Exporting the parameters as CSV

For information on the user interface, see also [Parameter view](#s210-parameter-view).

##### Monitoring and editing parameter values online

The input fields of the parameters that you can change online are displayed in orange after you have established an online connection with Startdrive.

To change the parameters online, follow these steps:

1. Establish an [online connection](#establishing-an-online-connection-to-the-drive).

   The display of the parameters changes to "orange".
2. Change the parameter values or settings, if required.
3. Press the enter key to apply the changes.

   The settings then take immediate effect in the drive.

##### Exporting the parameters to CSV file

CSV files can be opened in spreadsheet programs or editors.

To export the parameter list as a CSV file, proceed as follows:

1. Click on the arrow to the right of the ![Exporting the parameters to CSV file](images/147992406539_DV_resource.Stream@PNG-en-US.png) icon (copy offline parameters to a CSV file).

   A menu selection opens. You can choose whether you only want to export the displayed parameters or the parameters of all drive objects to a CSV file.
2. Select the required export function.

   The Export window opens.
3. Select a storage location in your directory tree, assign a name for the CSV file and click "Save".

   The parameter list is saved as a CSV file.

#### Comparing parameters

The current parameters of a drive object can be compared with another parameter set via the comparison function in the parameter view.

You can compare the following values of a parameter:

- Deactivate comparison
- Offline - Factory setting
- Online - Offline
- Online - Factory setting

##### Comparing parameters

To compare the parameters of the drive object with another parameter set, proceed as follows:

1. Open the parameter view for the device whose parameters you want to compare.
2. Click the black arrow icon of the ![Comparing parameters](images/166014146443_DV_resource.Stream@PNG-en-US.png) "Compare current parameters of this drive object with another data set" button.

   A selection list containing the comparison options opens:

   - Deactivate comparison
   - Offline - Factory setting (default setting in offline mode)
   - Online - Offline (default setting in online mode)
   - Online - Factory setting
3. Select the desired comparison option.

   The selected comparison option is executed as follows:

   - The "Comparison" column is displayed.
   - The comparison result of the selected comparison option is displayed in the "Comparison" column by icons.

Optional:

If you click the scales icon of the ![Comparing parameters](images/166014146443_DV_resource.Stream@PNG-en-US.png) button, the selected parameter is compared depending on the active parameterization mode:

- Offline mode: The parameters are compared to the factory settings by default.
- Online mode: The parameters are compared to the offline settings by default.

##### Icons in the "Comparison" column

| Icon | Meaning |
| --- | --- |
| ![Icons in the "Comparison" column](images/147993244427_DV_resource.Stream@PNG-en-US.png) | The comparison values are equal and error-free. |
| ![Icons in the "Comparison" column](images/147993248395_DV_resource.Stream@PNG-en-US.png) | Offline - Factory setting: The comparison values are different as well as technologically and syntactically error-free. |
| ![Icons in the "Comparison" column](images/147993252363_DV_resource.Stream@PNG-en-US.png) | Online - Offline: The comparison values are different and error-free. |
| ![Icons in the "Comparison" column](images/147993260299_DV_resource.Stream@PNG-en-US.png) | Online - Factory setting: The comparison values are different and error-free. |
| ![Icons in the "Comparison" column](images/147993256331_DV_resource.Stream@PNG-en-US.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Icons in the "Comparison" column](images/147993289867_DV_resource.Stream@PNG-en-US.png) | The value of at least one subordinate parameter index is different to the comparison value. |
| ![Icons in the "Comparison" column](images/166014077963_DV_resource.Stream@PNG-en-US.png) | At least one of the two comparison values has a technological or syntax error. |
| ![Icons in the "Comparison" column](images/166014072203_DV_resource.Stream@PNG-en-US.png) | The comparison is not possible. At least one of the two comparison values is not available (e.g. snapshot). |

#### Using user-defined parameter lists

This section contains information on the following topics:

- [Overview](#overview)
- [Creating a user-defined parameter list](#creating-a-user-defined-parameter-list)
- [Editing the user-defined parameter list](#editing-the-user-defined-parameter-list)

##### Overview

The user-defined parameter list is used to compile a list of specially selected parameters. This involves an excerpt from an underlying parameter list with specific parameters.

> **Note**
>
> Do not use the user-defined parameter list for the series commissioning.

You can execute the following actions in the user-defined parameter list:

- Add the required parameters
- Add a comment or a heading to the grouping of the parameters

Parameters also may occur multiple times in a list with a sorted or an unsorted sequence. The user-defined parameter list is saved in CSV format (*.csv).

The created list is designated as a user-defined list only after it has been saved.

**Saving a parameter list without values**

User-defined parameter lists can be saved as a CSV file only without parameter values.

**Storage location of the user-defined parameter list**

The user-defined parameter list is not saved together with the project or drive data. After the user-defined parameter list has been created, it must be saved as an external CSV file. The user-defined parameter list is displayed as a sub-tab in the parameter view only as long as the project is opened in Startdrive. If the project is reopened later on, the respective user-defined parameter list must be loaded/opened manually.

###### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147992353419_DV_resource.Stream@PNG-en-US.png) | Creates a new user-defined parameter list.   This function can be called up via the standard parameter list or a user-defined parameter list. |
| ![Toolbar](images/147993338635_DV_resource.Stream@PNG-en-US.png) | Saves the user-defined parameter list to any directory of the PG/PC. |
| ![Toolbar](images/147992357387_DV_resource.Stream@PNG-en-US.png) | Opens a user-defined parameter list from any directory of the PG/PC. |
| ![Toolbar](images/147993346571_DV_resource.Stream@PNG-en-US.png) | Inserts a comment below the active row in the user-defined parameter list. |
| ![Toolbar](images/147993342603_DV_resource.Stream@PNG-en-US.png) | Inserts a new parameter line above an active row in the user-defined parameter list. |

##### Creating a user-defined parameter list

###### Overview

You can create and save user-defined parameter lists by means of icons or shortcut menus. Here is a selection of the creation options:

###### Creating a user-defined parameter list and manually filling it with parameters

1. Click on ![Creating a user-defined parameter list and manually filling it with parameters](images/147992353419_DV_resource.Stream@PNG-en-US.png) in the toolbar located in the parameter view (Create new user-defined parameter list).

   - Or -

   Click in a parameter list and open the "Create new user-defined parameter list" shortcut menu.

   The "User_list_#" tab card opens (e.g. User_list_1, User_list_2).
2. In "User_list_#", enter the parameter number in the "Number" column in the <add new> input field and confirm with Return.

   Startdrive then automatically inserts the most important parameter data of this parameter in the other column fields of the current row.
3. Enter additional parameters in the user-defined parameter list in the same way.

**Result**

A new user-defined parameter list is created and displays the manually inserted parameters.

###### Creating a user-defined parameter list with selected parameters

1. Select the required parameters from a general parameter list with <Shift key + mouse click> or <Ctrl + mouse click>.
2. Select the "Create new user-defined parameter list" shortcut menu.

   - Or -

   If you want to add the selected parameters of an existing user-defined parameter list, select the "Append to user-defined parameter list" shortcut menu.

**Result**

The selected parameters are inserted in a new or in an existing user-defined parameter list.

###### Saving a user-defined parameter list as a file

The user-defined parameter list can be saved to a file only without parameter values.

1. Open the "Save the user-defined parameter list" shortcut menu in the user-defined parameter list.

   - Or -

   Click the ![Saving a user-defined parameter list as a file](images/147993338635_DV_resource.Stream@PNG-en-US.png) icon (Save the user-defined parameter list).

   The "Save As" window opens.
2. Assign a path and a file name to the CSV file in your file repository and click "Save".

   Do not use any special characters in the name of the CSV file. This is necessary to ensure that the file can also be opened via the web server later on.

**Result**

The user-defined parameter list is saved as a CSV file without parameter values. The assigned name of the CSV file is adopted as the new name of the user-defined parameter list and displayed in the parameter view in Startdrive. The drive type and firmware version also are stored in the CSV file. This parameter list can be loaded only in the parameter view of a drive which has both the same drive type and the same firmware version.

###### Closing the user-defined parameter list

1. Click in the list and open the "Close tab" shortcut menu.

   - Or -

   Click the X icon at the upper right-hand edge of the tab.

   A confirmation prompt is displayed. You can specify here whether you want to save or discard the user-defined parameter list.
2. If you do not want to save the parameter list, click "No".

   The parameter list will then be closed without being saved. You can ignore the subsequent steps.
3. If you want to save the parameter list, click "Yes".

   The "Save As" window opens.
4. Assign a path and a file name to the CSV file in your file repository and click "Save".

**Result**

The user-defined parameter list is saved as a CSV file. The assigned name of the CSV file is displayed as the name of the user-defined parameter list in Startdrive.

##### Editing the user-defined parameter list

###### Overview

You have the following options in a user-defined parameter list:

- Open the user-defined parameter list

  > **Note**
  >
  > User-defined parameter lists of different drive types are not compatible with each other. The parameter list to be opened must match the drive type of the displayed drive.
- Add parameters
- Add comments
- Add rows
- Delete rows

###### Requirements

To open:

- A user-defined parameter list is saved as a CSV file in the file repository of your PC/PG and is usable at all times.

- The saved parameter list must come from an identical drive type and have the same firmware version as the drive currently displayed. You can read the corresponding information from the CSV file using an editor.

###### Open the user-defined parameter list

The user-defined parameter list can be displayed only without parameter values. You can open the stored user-defined parameter lists of the displayed drive in the file system as follows:

1. Open the "Open the user-defined parameter list" shortcut menu in a parameter list of the parameter view.

   - Or -

   Click the ![Open the user-defined parameter list](images/147992357387_DV_resource.Stream@PNG-en-US.png) icon (Open the user-defined parameter list).

   The "Open" dialog opens.
2. Select the CSV file of the desired parameter list in the file repository of your PC/PG and click "Open".

**Result**

The user-defined parameter list is displayed as a separate tab without values in the parameter view.

If, when the list is opened, a parameter of the CSV file is not present in the parameter list of the drive, this parameter will then be removed from the opened list and a corresponding message will be displayed.

###### Inserting parameters in the displayed parameter list

Proceed as follows to append parameters:

1. Open the user-defined parameter list in the parameter view.

   ![Inserting parameters in the displayed parameter list](images/147993433355_DV_resource.Stream@PNG-en-US.png)

   ![Inserting parameters in the displayed parameter list](images/147993433355_DV_resource.Stream@PNG-en-US.png)
2. Enter the parameter number in the "Add new" input field located in the "Number" column and confirm your entry with <Return>.
3. Repeat step 2 for all of the parameters you want to enter.

**Result**

The added parameters are inserted at the bottom of the user-defined parameter list or directly below the previously selected parameter line.

###### Add comments

Proceed as follows to add a comment to a user-defined parameter list:

1. Select a parameter line in the "User_list_#" for which a comment is to be inserted.
2. Select the "Add comment" shortcut menu in the user list.

   ‑ Or ‑

   Click on the ![Add comments](images/147993346571_DV_resource.Stream@PNG-en-US.png) icon in the toolbar (Add comment).
3. Repeat step 2 for all comments you want to enter.

**Result**

The new comment is inserted directly above the selected row in each case. The comment line is highlighted in white and marked with a "//".

The comment can also be deleted from the list in the same way as a parameter.

![Add comments](images/147993429387_DV_resource.Stream@PNG-en-US.png)

###### Inserting a new row

1. Select the parameter line or comment line in the "User_list_#" after which a new row is to be inserted.

   ![Inserting a new row](images/147993437323_DV_resource.Stream@PNG-en-US.PNG)

   ![Inserting a new row](images/147993437323_DV_resource.Stream@PNG-en-US.PNG)
2. Open the "Insert row" shortcut menu.

   - Or -

   In the toolbar, click on the ![Inserting a new row](images/147993342603_DV_resource.Stream@PNG-en-US.png) (Insert row) icon.

**Result**

A new empty row will be inserted directly below the selected row.

###### Copying a parameter/comment

You can also copy the contents of a parameter list to another parameter list via Copy & Paste.

1. Select the parameter/comment or a row of a parameter list.

   ![Copying a parameter/comment](images/147993437323_DV_resource.Stream@PNG-en-US.PNG)

   ![Copying a parameter/comment](images/147993437323_DV_resource.Stream@PNG-en-US.PNG)

   A multiple selection can be made by pressing the Shift or Ctrl key.
2. Select "Copy" in the shortcut menu.
3. Activate/open the required user-defined parameter list as the copy target.
4. Select the parameter/comment or a row of the target parameter list.
5. In the shortcut menu, select "Paste".

**Result**

The copied parameters or comments are inserted in the next free rows of the list.

###### Deleting a row

To delete a parameter or comment, proceed as follows.

1. Select the parameter/comment or a row in the user-defined parameter list.

   A multiple selection can be made by pressing the Shift or Ctrl key.
2. Select "Delete" in the shortcut menu.

**Result**

The selected rows are deleted.

###### Uncommenting parameters

You can change parameters in the user-defined parameter list to a comment if necessary.

1. Select the parameter in the user-defined parameter list.
2. Insert "//" in front of the parameter name in the "Number" field.

**Result**

The parameter is now no longer listed as a parameter in the list, but rather, as a comment. The previously displayed parameter data of the parameter are hidden in this parameter list.

The comment can be changed back to a parameter by removing the "//". In this case, however, the program checks the parameter name for invalid characters and displays a message in case of an error.

### Licensing

This section contains information on the following topics:

- [Overview](#overview-1)
- [Overview of licenses](#overview-of-licenses)
- [Activate Trial License mode](#activate-trial-license-mode)
- [Creating a license key](#creating-a-license-key)
- [Displaying/entering a license key](#displayingentering-a-license-key)
- [Important messages](#important-messages)

#### Overview

The drive system can generally be used without an additional license. Auxiliary functions or options, however, do require the availability of a purchased license. This license is electronically linked with the function/option of your hardware via a License Key.

The License Key is an electronic license stamp that indicates that one or more software licenses are owned.

Actual customer verification of the license for the software that is subject to license is called a "Certificate of License" (abbreviated to "CoL").

> **Note**
>
> Please refer to the ordering documentation (e.g. catalogs) for information on basic functions and functions subject to license.

**Properties of the license key**

- Is assigned to a specific memory card.
- Is stored retentively on the memory card.
- Is not transferable.
- Can be permanently assigned to an ordered memory card already during the ordering process.
- Can also be generated subsequently with the "WEB License Manager" from a license database based on the previously ordered and received Certificates of License.

##### Requirement

- An optional memory card is available for the drive.

  The licensing function requires a memory card to be available.

##### System responses

**System response if there is a not a sufficient license for an option**

An insufficient license for an option is indicated with the following fault and LED on the control unit:

- F13000 Insufficient license
- LED READY flashes red at 2 Hz

  ![System responses](images/147994370827_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The drive system can only be operated with an insufficient license for an option during commissioning and servicing. For this purpose, the Trial License Mode must be activated explicitly.
>
> The drive requires a sufficient license in order for it to operate. Not all options support the Trial License Mode!

**System response for an insufficient license for a function module**

An insufficient license for a function module is indicated with the following faults and LEDs on the control unit:

- F13000 Insufficient license
- F13010 Licensing, function module not licensed.
- The drive is stopped with an OFF1 response.
- LED READY flashes red at 2 Hz

  ![System responses](images/147994370827_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> It is not possible to operate a drive system with an insufficient license for a function module.
>
> The drive requires a sufficient license in order for it to operate.

##### Additional parameters

- p9918
- p9919
- p9920
- p9921

Pxxxx

#### Overview of licenses

##### Overview of licenses

The Startdrive commissioning tool includes a license overview page.

![Overview of licenses](images/147994428299_DV_resource.Stream@PNG-en-US.PNG)

Overview of licenses

| Element | Description |
| --- | --- |
| General license status | Indicates the current license status (e.g. you do not have all of the licenses you need). |
| System response | Displays the system response to the current license status, e.g. "Blocks the drive from being switched on again." |
| Trial period | Displays of the status Trial License; e.g. Trial License mode is not active. |
| Serial number of the memory card | Serial number of the memory card and button to copy the serial number. |
| Activate Trial License mode | Button to activate the Trial License mode. |
| Display/enter License Key | Button for displaying and entering the License Key |
| Function that requires a license | List of all used system options/functions subject to license. |
| Existing/required licenses | The required number of licenses compared with the number of licenses included with the License Key.  For operation, the number of available licenses ≥ the number of licenses required. |
| License status | Displays the current status of the function requiring a license. |
| Remaining operating time | Displays the remaining operating time of the trial period. |

This overview allows the following:

- Obtain a status overview of the individual licenses of your drive system
- Display and enter License Key

  See "[Displaying/entering a license key](#displayingentering-a-license-key)"
- Display and copy the serial numbers of the memory cards being used
- Activate Trial License mode

  See "[Activate Trial License mode](#activate-trial-license-mode)"

##### Trial Licenses

Valid licenses can either be ordered together with a memory card, or when subsequently ordered, can be assigned to your memory card via the "Web License Manager". Most of the SINAMICS functions requiring a license can be operated for a limited period of time in a Trial License mode.

![Trial License mode schema](images/147994397835_DV_resource.Stream@PNG-en-US.png)

Trial License mode schema

**Features:**

- The Trial License mode can be used for a maximum of three periods. Whereby the first period is primarily envisaged as the initial trial period during commissioning and accompanying trials. The other two periods are intended for tests, presentations or service.
- The Trial License mode must be activated separately for each of the periods. Once activated, a trial period can no longer be interrupted or canceled. The active trial period also continues when you activate an additional option in the Trial License mode, deactivate an activated option again, or enter a valid License Key.
- The Trial License mode can be activated only as a block, i.e. for all options together. An option-granular activation is not possible.
- You receive messages in plenty of time before a period has expired. You can then activate the next trial period if it is still free or replace the Trial License with a full license.

  The next time the drive runs up, the Trial License mode will be deactivated. If you miss this opportunity, you can only continue to work with a full license or you must deactivate the option where a license is required - or remove it from your configuration.
- Not all SINAMICS licenses can be used in the Trial License mode.

#### Activate Trial License mode

##### Requirements

- A project has been created.
- A drive has been created.
- An online connection has been established between the PG/PC and the drive.

##### Procedure

The Trial License mode can be used for a maximum of three trial periods.

1. Call the license overview page:

   - Double-click the drive control in the project tree.
   - Double-click the "Parameter" entry.
   - Click "License" in the secondary navigation.
2. Click on the "Activate Trial License mode" button.
3. To activate the Trial License mode, click the "Activate" button in the query dialog.

   Alarm A13030 indicates that the Trial License has been activated. The status overview then shows the remaining operating time of the licensed options in Trial License mode.

   After the trial period expires, alarm A13031 "Trial License period expired" is output.
4. Repeat steps 2 and 3 if you wish to activate the Trial License mode for another trial period.

   After the third trial period has expired, alarm A13033 "Last Trial License period expired" is output. Additional trial periods can now no longer be activated. After a trial period expires, a lock (inhibit) may become active next time the system runs up. You require a full license if you wish to use the associated subfunctions.
5. Proceed as follows if you wish to further use the associated subfunctions:

   - Purchase a full license for the associated subfunctions.
   - Generate a new License Key (see "[Creating a license key](#creating-a-license-key)").
   - Enter the new License Key (see "[Displaying/entering a license key](#displayingentering-a-license-key)").

**Note**

For S210 the Trial License can also be configured via "Online & diagnostics". The subsequent steps are the same.

**Note**

You can only activate the next trial period after the previous period has expired.

#### Creating a license key

The WEB License Manager informs you about how many and which licenses are assigned to your memory card. If you need additional licenses, you can assign them to your memory card and create a new License Key using the WEB License Manager.

> **Note**
>
> A new license is not required for upgrading the firmware. Therefore, do not delete the License Key from the memory card (..\KEYS\SINAMICS\KEYS.txt) if you want to upgrade.

The following information is required to work with the "WEB License Manager":

- Serial number of the memory card

  The serial number is on the memory card, or can be copied from the license overview
- Enter the license number and delivery note number of the license (visible on the Certificate of License)
- Product name

##### Creating a license key

1. Call the following link:

   [WEB License Manager](https://workplace.automation.siemens.com/pls/swl-pub/SWL_MAIN_MENU.NAVIGATION_HEAD?a_lang_id=E&a_action=)
2. Select the "Direct access" link.

   The progress indicator is at "Login" in the License Manager.
3. Enter the license number and delivery note number of your license and then click "Next".

   The progress indicator is then at "Identify product".
4. Enter the serial number of the memory card.
5. Select the product that you are using, e.g. "SINAMICS S CU320-2 PN". Then click "Next".

   The progress indicator is at "Select licenses". In the "Already assigned licenses" column, you can see which licenses of the selected delivery note have already been assigned and how often.

   In the "Additional licenses to be assigned" column, you can activate the required licenses or also specify how many additional licenses you require.
6. Activate the additional required licenses and then click "Next".

   The progress indicator is at "Assign licenses". A summary of the selected licenses is displayed here for checking.
7. To start the assignment, click "Assign".

   A prompt appears.
8. When you are sure that the license has been correctly assigned, click "OK".

   The licenses are permanently assigned to the specified hardware. The progress indicator is at "Generate license key". The License Key is displayed and can be saved as a text file or as a PDF.

##### Displaying the license key

If the License Key on the memory card is accidentally deleted, you can display it again via the WEB License Manager.

1. Call the following link:

   [WEB License Manager](https://workplace.automation.siemens.com/pls/swl-pub/SWL_MAIN_MENU.NAVIGATION_HEAD?a_lang_id=E&a_action=)
2. In the navigation, click the "Display license key" option in the "User menu".

   Several input fields can be found on the right of the "Display license key" view.
3. Enter the serial number of your memory card either in the "Hardware serial number" or in the "License no." field. enter your license number and then click the "Display license key" button.

   The current Lizense Key is then displayed.

   You can request this License Key by e-mail in the form of a report. This report contains all previously ordered licenses for this memory card. Missing licenses can be detected and re-ordered on the basis of this report.
4. Enter your address in the "E-mail address" field and then click the "Request license report" button.

#### Displaying/entering a license key

##### Requirements

- A project has been created.
- A drive has been created.
- An online connection has been established between the PG/PC and the drive.

##### Procedure

A license overview page is included in the Startdrive commissioning tool; you can use this to view the actual License Key, and when required, enter a new key.

1. Call the license overview page:

   - Double-click the drive control in the project tree.
   - Double-click the "Parameter" entry.
   - Click "License" in the secondary navigation.
2. Click the "Display/enter license key" button in the license overview page.

   A dialog opens having the same name. The current license key of your drive is visible in the upper field (provided already available).
3. If you wish to use a new License Key, enter it in the "New license key" field (example: E1MQ-4BEA).

   For example, you can replace a previous Trial License with a full license.
4. Click the "Activate" button to activate the License Key that has just been entered.

   The dialog closes. The new License Key is active immediately and can be saved to ROM via RAM.

#### Important messages

##### Overview of important alarms and faults

| Symbol | Meaning |
| --- | --- |
| - F13000 | Licensing is not sufficient |
| - F13010 | Licensing, function module not licensed |
| - A13030 | Trial License activated |
| - A13031 | Trial License period expired |
| - A13032 | Trial License last period activated |
| - A13033 | Trial License last period expired |

### Using drive libraries

This section contains information on the following topics:

- [Overview](#overview-2)
- [Creating copy templates](#creating-copy-templates)
- [Using copy templates](#using-copy-templates)

#### Overview

##### Using drives in libraries

In the TIA Portal, libraries are used to archive objects that you wish to reuse. The archived objects can be reused within a project or across projects.

In the drive context, working with libraries allows you to create drive copies/device copies in libraries using networks. You then reinsert these copy templates into the particular project context.

A detailed description of libraries is provided in the online help under "[Using libraries](Using%20libraries.md#using-libraries)".

##### Library types

The following library types are available:

- Project libraries

  You use a project library if you only wish to use the objects in the opened project.
- Global libraries

  You use global libraries if you wish to use the objects across projects.

##### Devices and drives

The following objects are possible as copy templates within the drive context:

- One or several devices from the project navigation
- Devices and networks from the network view, respectively the device configuration

Copy templates include the complete parameterization. This means that with a copy template you can create complete parameterized drive copies from the initial source drive.

#### Creating copy templates

##### Precondition

With copy templates, from the library you create one or several copies of the device, possibly with networks. As a consequence, first configure and parameterize the device or the devices that you wish to use as a copy template.

##### Creating a copy template in a project library

Proceed as follows to create a copy template in a project library:

1. Open the "Libraries" task card.
2. Click on "Project library" to open the palette.
3. Select the device in the project navigator.

   - Or -

   Select a device or several devices with or without network in the network view (possible to lasso)
4. Drag your selection and drop it into the "Copy templates" folder - or into any subfolder of "Copy templates".

##### Creating a copy template in a global library

Proceed as follows to create a copy template in a global library:

1. Open the "Libraries" task card.
2. Click on "Global libraries" to open the palette.
3. Open a global library, or create a new global library.
4. Select the device in the project navigator.

   - Or -

   Select a device or several devices with or without network in the network view (possible to lasso)
5. Drag your selection and drop it into the "Copy templates" folder - or into any subfolder of "Copy templates".

##### Result

The selected elements are inserted as copy template in the project library or the global library. Only one entry per object is generated. Only one entry is created even when selecting several devices. The preceding symbol signifies the source of the copy template.

Every element is assigned a default name, that you can change.

#### Using copy templates

##### Using copy templates from project libraries and global libraries

Use copy templates to use objects a multiple number times in the same project. After exporting the library, you can also use the objects in other projects and PGs/PCs. Using copy templates of parameterized drives or networks, you can carry out series commissioning. If you have created a network with devices as copy template via the network view, you can only reinsert in the network view.

The TIA Portal allows you to insert the copy templates at the appropriate locations.

##### Using a copy template from a project library

Proceed as follows to use a copy template from a project library:

1. Open the "Libraries" task card.
2. Click on "Project library" to open the palette.
3. Select the copy template.
4. Drag the selection from the project folder and drop into the project navigation.

   - Or -
5. Drag the selection and drop into the network view if the copy template is from the network view.

##### Using a copy template from a global library

Proceed as follows to use a copy template from a global library:

1. Open the "Libraries" task card.
2. Click on "Global libraries" to open the palette.
3. Open a global library.
4. Select the copy template.
5. Drag the selection from the project folder and drop into the project navigation.

   - Or -
6. Drag the selection and drop into the network view if the copy template is from the network view.

##### Result

The objects included in the copy template - for example devices and networks - are created in the project.

## Sequence of a device configuration in S210

> **Note**
>
> **Only in the offline mode**
>
> The drive components can only be combined and specified in the offline mode. In the online mode, all corresponding setting ranges are marked in the device view and in the Inspector window.

### Usual procedure:

The following steps are required:

1. [Create or open the project with Startdrive](#creating-a-new-or-loading-an-existing-startdrive-project).
2. [Create the device configuration in Startdrive offline](#creating-a-device-configuration-manually)

   - Or -

   [Read out the device configuration and load into the project](#uploading-a-device-configuration-as-new-station)
3. [Perform the basic parameterization of the drive units](Commissioning%20SINAMICS%20S210%20drives.md#basic-parameter-assignment-1)
4. [Load the project to the target device](#loading-the-project-data-to-the-drive-unit).
5. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-drive).
6. [Perform commissioning steps](Commissioning%20SINAMICS%20S210%20drives.md#rotate-optimize)

**Result:**

The motor turns.

### Variant 1: Basic parameterization online

For S210 Control Units, as an alternative to the offline mode, the basic parameterization can also be carried out in the online mode. This results in a slightly modified procedure:

The following steps are required:

1. [Create or open the project with Startdrive](#loading-the-project-data-to-the-drive-unit).
2. [Create the device configuration in Startdrive offline](#creating-a-device-configuration-manually)

   - Or -

   [Read out the device configuration and load into the project](#uploading-a-device-configuration-as-new-station)
3. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-drive).
4. [Perform the basic parameterization of the drive units](Commissioning%20SINAMICS%20S210%20drives.md#basic-parameter-assignment-1)
5. [Perform commissioning steps](Commissioning%20SINAMICS%20S210%20drives.md#rotate-optimize)

**Result:**

The motor turns.

### Variant 2: Basic parameterization together with a SIMATIC S7-1500

If you wish to commission an S210 Control Unit together with a SIMATIC S7-1500 controller, the optimum parameterization procedure differs significantly from the two previous configuration variants.

> **Note**
>
> Similarly, the S210 drive also can be configured together with the "SINUMERIK MC" controller.

The following steps are required:

1. [Create or open the project with Startdrive](#loading-the-project-data-to-the-drive-unit).
2. Create the device configuration in Startdrive offline

   - [Insert the SINAMICS drive into the project](#adding-devices-offline)
   - [Insert the SIMATIC controller into the project](#adding-a-controller-plc)
   - [Network the SIMATIC controller and drive](#networking-the-controller-plc-and-drive)
   - [Insert a technology object into the SIMATIC controller](#inserting-a-technology-object-into-the-simatic-s7-controller)
   - [Interconnect the technology object with the drive](#interconnecting-the-technology-object-and-sinamics-drive)
3. [Load the project data to the target device](#loading-the-project-data-to-the-drive-unit).
4. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-drive)
5. Making the basic settings in the commissioning mode

   - [Make the basic settings for the S210 drive](Commissioning%20SINAMICS%20S210%20drives.md#basic-parameter-assignment-1)
   - [Perform commissioning optimization](Commissioning%20SINAMICS%20S210%20drives.md#rotate-optimize)

**Result:**

The motor turns.

---

**See also**

[SINAMICS S210 servo drive system](https://support.industry.siemens.com/cs/ww/en/view/109771824)

## Adding and assigning parameters

This section contains information on the following topics:

- [Creating a new or loading an existing Startdrive project](#creating-a-new-or-loading-an-existing-startdrive-project)
- [Creating a device configuration manually](#creating-a-device-configuration-manually)
- [Uploading a device configuration as new station](#uploading-a-device-configuration-as-new-station)
- [Optional: Configuring a controller with drive](#optional-configuring-a-controller-with-drive)

### Creating a new or loading an existing Startdrive project

This section contains information on the following topics:

- [Overview](#overview-3)
- [Creating a new project](#creating-a-new-project)
- [Opening the project](#opening-the-project)
- [Opening an older project version](#opening-an-older-project-version)

#### Overview

For projects, the choice is yours:

- You create a completely new project (see "[Creating a new project](#creating-a-new-project)").
- You open an existing project, and subsequently change the project configuration (see "[Opening the project](#opening-the-project)").

##### Requirement

- You have opened the "Startdrive" application in the TIA Portal.

#### Creating a new project

##### Procedure

You can create new projects once the Startdrive application has been opened in the TIA Portal.

1. Click "Create new project" in the secondary navigation in the portal view of Startdrive.

   The entry fields for the basic project data are displayed to the right in the detailed view.

   ![Entering project data](images/147996059531_DV_resource.Stream@PNG-en-US.PNG)

   ![Entering project data](images/147996059531_DV_resource.Stream@PNG-en-US.PNG)

   Entering project data
2. Enter the project data here:

   - Project name:

     Startdrive automatically counts each new project.
   - Path:

     The simpler the archive path for the project, the faster the project can be loaded.
   - Author:

     The login code for the person entering the data is preassigned.
   - Comment:

     You can store brief project information here.
3. Click "Create" to save basic project data.

##### Result

The new project is created and simultaneously opened. Possible next steps are displayed in the detailed view.

![Getting Started](images/147996063499_DV_resource.Stream@PNG-en-US.png)

Getting Started

#### Opening the project

##### Opening an existing project

If you wish to change the data of an existing project, then you can load this project at any time.

1. Click "Open existing project" in the secondary navigation in the portal view of Startdrive.

   A selection of the projects last used is displayed to the right in the detailed view.

   ![Opening an existing project](images/147996099083_DV_resource.Stream@PNG-en-US.PNG)

   ![Opening an existing project](images/147996099083_DV_resource.Stream@PNG-en-US.PNG)

   Opening an existing project
2. Select the required project from the list, and then click "Open".

   - Or -

   Click "Browse", double-click the required project in your directory structure, select project file "*.ap15.x".

   ![Opening an existing project from the directory](images/147996103051_DV_resource.Stream@PNG-en-US.PNG)

   ![Opening an existing project from the directory](images/147996103051_DV_resource.Stream@PNG-en-US.PNG)

   Opening an existing project from the directory

   Then click "Open".

**Note**

**Older project versions**

You can also open older project versions. Generally, however, these project versions must be upgraded. Startdrive has a check and upgrade mechanism to do this, see "[Opening an older project version](#opening-an-older-project-version)".

##### Result

The selected project opens. If another project was previously displayed, then it is now closed.

- If you have created a new project, the next possible steps for the project that has been opened are now displayed in the detailed view (see the description in the following sections).
- If you have opened an existing project, the interconnected modules of this project are displayed in the device view. You can specify existing modules differently, or remove existing modules and insert new modules instead.

##### Project protection

In the TIA Portal, you can apply project protection to Startdrive projects. All parameters and passwords contained in the project are encrypted and protected from being overwritten. If a Startdrive project is protected, you have to enter a password when you try to open it. You require the following information to open a project:

- User name with authorization for this project
- Password

This information is generated and administered in the user administration of the TIA Portal. Detailed information on project protection can be found in the online help under "[Using user administration](Managing%20users%20and%20roles.md#managing-users-and-roles)".

#### Opening an older project version

In Startdrive, it is possible to determine the last Startdrive version used to process a project based on its extension. Extension "*.ap15", for example, indicates the older version V15.

To open older project versions, it is necessary to upgrade the project to the current program version.

##### Upgrading Startdrive versions V14 or V14 SP1

In contrast to G120 projects, S120 projects with version V14 or V14 SP1 cannot be opened with a newer version of Startdrive (V15 or higher). If you wish to upgrade S120 projects with version V14 SP1 to version V15, then carefully observe the procedure described in this document:

"[Migrating SINAMICS S120 projects in Startdrive from V14 to V15](https://support.industry.siemens.com/cs/ww/en/view/109755173)

##### Upgrading Startdrive versions from V15 to higher versions

1. Select the Startdrive project and then click on "Open".

   When opening, Startdrive identifies an older TIA Portal project version and checks whether all preconditions are satisfied so that this project can be upgraded to the current project version. The following dialog is displayed:

   ![Example: Migrate project and open](images/147996126603_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Migrate project and open](images/147996126603_DV_resource.Stream@PNG-en-US.PNG)

   Example: Migrate project and open

   The "Upgrade possible" column displays as to whether your project can be upgraded. If the upgrade is possible then the "Upgrade" button is activated.
2. Click on "Upgrade" to upgrade your project to the current version.

**Note**

If, for a program package, "Installation required" is displayed in column "Upgrade possible", then it is not possible to upgrade the project in the standard way.

In this case, before upgrading, reinstall the appropriate program package. Then attempt to open the old project version again. This dialog is reopened. Generally, upgrade is then possible.

**Result**

Startdrive duplicates the old project version in a current version, and opens this new project version.

The original project remains unchanged and can therefore be simply opened using the old program versions.

### Creating a device configuration manually

This section contains information on the following topics:

- [SINAMICS S210](#sinamics-s210)
- [Motors and measuring systems](#motors-and-measuring-systems)
- [Optional settings](#optional-settings)

#### SINAMICS S210

This section contains information on the following topics:

- [Adding devices offline](#adding-devices-offline)
- [Optional: Replace device](#optional-replace-device)
- [Detailed drive settings](#detailed-drive-settings)

##### Adding devices offline

You can insert new drive units in the portal view or in the project view.

###### Requirements

- A new project has been created.

  - Or -
- An existing project has been opened.

###### Inserting a new drive unit

To insert drive units in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click "Drives" to display the available drives.
3. Select the "SINAMICS S210" folder from the list.

   One matching device is displayed for each performance class of the S210.
4. Select the required S210 drive.
5. Select the firmware version that is installed on your drive.
6. Enter a name and click "OK".

**Note**

If the version numbers (offline project in Startdrive compared with the drive unit) do not match, it will not be possible to go online later. On creation, the current firmware version is always suggested. If required, you can change the version number via the "Version" drop-down list.

If you leave the "Device view" option activated, the device view opens automatically.

**Inserting a device via the network view or topology view**

Alternatively, you can also insert a drive unit via the network view or topology view.

1. Open the network view.
2. Open the "Drives & starters" entry in the hardware catalog.
3. Open the "SINAMICS drives" entry in the hardware catalog and the corresponding subfolder of the desired Control Unit.
4. Drag the drive unit from the hardware catalog and drop it in the network view or the topology view.

###### Result

The device has been added. The motor and measuring system must then be determined.

![S210 Control Unit inserted](images/148017896971_DV_resource.Stream@PNG-en-US.PNG)

S210 Control Unit inserted

##### Optional: Replace device

###### Description

In the device configuration and the project navigation of an S210 drive unit, you can replace the current S210 drive unit with an S210 drive unit with a different performance range at any time. When replacing the drive device, previous configurations of the motor and/or the encoder remain if both devices are compatible with one another (see "[Additional information](#system-overview)").

###### Requirements

- A project has been created.
- An S210 Control Unit has been inserted in the device configuration.

###### Replacing a device via the project navigation

1. In the project tree, select the drive unit to be replaced and call the shortcut menu "Change device".

   Dialog "Change device - S210" is opened:

   ![Device replacement via project navigation](images/148017920907_DV_resource.Stream@PNG-en-US.png)

   ![Device replacement via project navigation](images/148017920907_DV_resource.Stream@PNG-en-US.png)

   Device replacement via project navigation

   The data of the current drive unit is displayed on the top left. The replacement devices in question are displayed in a hardware catalog on the top right.
2. Select the desired replacement device in the hardware catalog of the "Replace device" dialog.

   The most important data of the new device is displayed in the center of the dialog in the "New device" field. You can compare this data with the data of the current device (on the left).

   If both drive units are not fully compatible, then corresponding information is displayed in the "Compatibility information" field. This can mean that you must assign a different motor, if applicable, if you nevertheless import the desired replacement device.
3. To import the new drive unit, click on OK.

###### Replacing a device via the hardware catalog

1. In the hardware catalog, select the new S210 drive unit and move it to the placeholder for the current drive unit in the device view.

   The "Replace device" dialog opens:

   ![Device replacement via hardware catalog](images/148017925003_DV_resource.Stream@PNG-en-US.png)

   ![Device replacement via hardware catalog](images/148017925003_DV_resource.Stream@PNG-en-US.png)

   Device replacement via hardware catalog

   The most important data of the old drive unit and the new drive unit are compared to each other in the dialog.

   If both drive units are not fully compatible, then corresponding information is displayed in the "Compatibility information" field. This can mean that you must assign a different motor, if applicable, if you nevertheless import the desired replacement device.
2. To import the new drive unit, click on OK.

###### Result

The current drive unit has been replaced by the desired replacement device.

If both drive units are not fully compatible, the placeholder for the motor is displayed unspecified in the device navigation and you must reassign a suitable motor output.

##### Detailed drive settings

You can configure the following details for the S210 Control Unit

- General

  - Product information

    Name data
  - Catalog information

    Brief description, description of the components included, firmware version used
  - Identification & maintenance

    Information and data to identify and localize a drive within a plant or system.
- PROFINET interface [X150]

  - General
  - Ethernet addresses

    Subnet, IP address, subnet mask, PROFINET names
  - Telegram configuration

    Telegrams of the closed-loop drive control Send, receive, Safety Integrated
  - Advanced options

    Interface options

    Media redundancy

    Clock cycle synchronization for local modules (isochronous mode)

    Real time settings

    Port [X150 P1] and port [X150 P2]
  - Module parameters

    Activation of channel diagnostics
- Ethernet commissioning interface [X127]

  - General
  - Ethernet addresses

    Subnet, IP address, subnet mask
- Power Module settings

  Supply voltage
- [Web server](#configuring-web-server-access)

  Access settings for the S210 web server.

###### Procedure

1. Select the S210 Control Unit in the device view and open the Inspector window.
2. In the secondary navigation of the Inspector window, select the required detail menu.
3. Make the required detail settings in the white fields.

   The gray fields are corrected automatically in accordance with their setting.

###### Result

You have made the detailed settings for the drive unit in your device configuration.

#### Motors and measuring systems

This section contains information on the following topics:

- [Inserting and specifying motors](#inserting-and-specifying-motors)
- [Implement detailed settings of the motor](#implement-detailed-settings-of-the-motor)
- [Making detailed settings of the measuring system](#making-detailed-settings-of-the-measuring-system)

##### Inserting and specifying motors

###### Requirements

- A project has been created.
- An S210 Control Unit has been inserted in the device configuration.
- The intended motor is compatible with the S210 control module, see [Additional information in the operating instructions](#system-overview).

###### Procedure

The drive that has just been inserted in the project has a placeholder for the required motor. You must specify this placeholder in the configuration.

> **Note**
>
> If the motor placeholder has been accidentally deleted from the drive, follow these steps:
>
> - Open the "Motors" entry in the hardware catalog.
> - Drag the unspecified "1FK2 synchronous motor" to the lower area of the S210 drive unit.  
>   A motor placeholder appears.

1. Double-click on the white motor placeholder (MOT) in the drive. The inspector window is displayed.
2. If required, select the "Motor – Selection 1FK2" entry in the secondary navigation in the inspector window.
3. On the basis of the article number, select the power rating of the motor and an associated encoder. Also define whether or not the motor has a holding brake.

   ![Specifying the motor](images/148017967755_DV_resource.Stream@PNG-en-US.png)

   ![Specifying the motor](images/148017967755_DV_resource.Stream@PNG-en-US.png)

   Specifying the motor

   A DRIVE-CLiQ encoder is automatically assigned to all motors in the list.

###### Result

The motor placeholder is assigned the data of the selected motor. The white area turns gray.

![Motor and associated encoder specified](images/148017971851_DV_resource.Stream@PNG-en-US.PNG)

Motor and associated encoder specified

The motor has been added. The assigned encoder and the encoder evaluation are automatically also added and specified.

##### Implement detailed settings of the motor

You can configure the following motor details for motors during commissioning:

- Basic parameterization
- Rating plate values
- Motor brake

###### Procedure

1. Select the motor in the device view and open the inspector window.
2. Select the "Motor details > Rating plate values" menu in the inspector window.

   The "Rating plate values" screen form is displayed in the inspector window.
3. To perform the basic parameterization for the motor, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Basic parameterization" entry.

   The function view of the drive axis opens:

   Make the required settings here (see "[Basic parameterization](Commissioning%20SINAMICS%20S210%20drives.md#basic-parameter-assignment-1)").
4. Select the "Motor details > Rating plate values" menu again in the inspector window.
5. Make the required settings in the white fields.

   The gray fields are refreshed automatically in accordance with their setting.
6. Select the "Motor details > Motor brake" menu in the inspector window.

   The current configuration of the motor holding brake is displayed in the screen form. You can only change this configuration in the basic parameterization.
7. To change the configuration of the motor holding brake, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Brake control" entry.

   The "Basic parameterization" screen form opens.
8. Here you specify whether the motor holding brake is to be positively opened.
9. Then save the project to accept the settings.

###### Result

You have made the detailed settings for the selected motor in your device configuration.

##### Making detailed settings of the measuring system

You can configure the following encoder details for measuring systems during commissioning:

- Actual value processing
- Encoder details such as encoder type, incremental tracks, absolute SSI protocol, etc.

###### Procedure

1. Select the encoder in the device view and open the inspector window.
2. Select the "Measuring system details" menu in the inspector window.
3. To configure the detail configuration, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Actual value processing" entry.

   The "Basic parameterization" screen form opens in the function view.

   Make the required settings here (see "[Basic parameterization](Commissioning%20SINAMICS%20S210%20drives.md#basic-parameter-assignment-1)").
4. Select the "Measuring system details" menu again in the inspector window.

   The setting options depend on the selected encoder type.
5. Make the required detailed settings of the encoder in the white fields.

   The gray fields are corrected automatically in accordance with their setting.

###### Result

You have made the detailed settings for the selected encoder in your device configuration.

#### Optional settings

This section contains information on the following topics:

- [Copying drives to the project](#copying-drives-to-the-project)
- [Configuring web server access](#configuring-web-server-access)
- [Configuring NTP time synchronization](#configuring-ntp-time-synchronization)

##### Copying drives to the project

###### Copying drives from other projects

You can also copy drives from other projects. You have different options to do so.

**Copy drive using the project tree**

1. Open a second Startdrive instance.
2. Open the project from which you want to copy a drive.
3. Click the drive you wish to copy in the project tree.
4. Select "Copy" from the shortcut menu.
5. Switch to the Startdrive instance to which you want to copy the drive.
6. Open the project to which you want to copy the drive.
7. In the project tree open the shortcut menu and select "Paste".  
   The drive is copied to the target project.

**Copy drive using drag-and-drop**

1. Open a second Startdrive instance.
2. Open the project from which you want to copy a drive.
3. Click the drive you wish to copy in the project tree.
4. Drag the drive to the program window of the Startdrive instance to which you want to copy the drive.
5. Drag the drive to the project tree.  
   The drive is copied to the target project.

> **Note**
>
> **Copying between protected and unprotected projects**
>
> If you have activated project protection via the user administration in the TIA Portal, the drive parameters and passwords in the Startdrive project are encrypted.
>
> Encryption of the data cannot be canceled. It is not possible to copy drives from protected to unprotected projects.

###### Copying drives from a reference project

You can also copy drives from a reference project. Detailed information on the use of reference projects can be found in the online help under "Editing projects".

> **Note**
>
> **Copying between protected and unprotected projects**
>
> If you have activated project protection via the user administration in the TIA Portal, the drive parameters and passwords in the Startdrive project are encrypted.
>
> Encryption of the data cannot be canceled. It is not possible to copy drives from protected to unprotected projects.
>
> Copying between protected and unprotected projects across instances is not possible. Copying is only possible if you open one of the projects as a reference project.

###### Downloading objects from libraries

You can also download drive objects from a library. Detailed information on the use of libraries can be found in the online help under "Using libraries".

> **Note**
>
> **Copying between protected and unprotected projects**
>
> If you have activated project protection via the user administration in the TIA Portal, the drive parameters and passwords in the Startdrive project are encrypted.
>
> Drive objects can only be downloaded from unprotected projects to a global library. It is possible, however, to download drive objects from a library to a protected project.

##### Configuring web server access

###### Configuring the web server

The web server provides information about a SINAMICS device on its web pages. Access is made with an Internet browser.

For an S210 converter, you configure the web server in the Inspector window.

###### Requirements

- The S210 converter is in the offline mode.
- The "Web server" setting area is active in the Inspector window of the drive.

###### Disabling the web server

The web server is activated as standard in the "Web server" setting area of the Inspector window. If necessary, the web server can be disabled as follows:

1. Deactivate the option "Activate the web server on this device" in the configuration dialog.
2. Save the project to apply the changes.

###### Restricting web server access to a secure connection

The standard configuration of the web server allows you to access the SINAMICS converter via an HTTP connection and via an encrypted HTTPS connection. The configuration can be changed to allow access only via a secure HTTPS connection.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Use of non-encrypted connections (HTTP)**  HTTP also supports the transfer of unencrypted login data. This simplifies, for example, damage by third-parties for password stealing attacks with data manipulation.   - To transfer all data encrypted, restrict access to secure connections. |  |

**Procedure:**

1. In the configuration dialog, activate the option "Only permit secure access to the service interface [X127] via HTTPS protocol".
2. If you wish to work with a PROFINET interface, also activate the option "Activate access via the PROFINET interface [X150]. This is only possible as secure HTTPS connection".

###### Setting or changing user accounts

For SINAMICS S210, the rights of both user accounts "SINAMICS" and "Administrator" are permanently defined and cannot be changed by users.

The "Administrator" user has full access rights by default. However, only restricted access rights apply for the standard "SINAMICS" user.

For the web server user accounts, you can make the following settings in Startdrive:

- Enable or disable the "SINAMICS" or "Administrator" user
- Create the password of the "SINAMICS" or "Administrator" user
- Change the password of a "SINAMICS" or "Administrator" user (only online).
- Delete the password of a "SINAMICS" user (only online).

**Password default settings after first commissioning**

- SINAMICS: No password is preset.

  You are recommended to assign a password. It must comprise at least eight characters.
- Administrator: No password is preset.

  For this user, a password must be assigned. It must comprise at least eight characters.

> **Note**
>
> **Secure passwords**
>
> The password must include the following elements to provide protection against unauthorized access, e.g. unauthorized persons.
>
> - At least 8 characters
> - Uppercase as well as also lowercase letters
> - Numbers and special characters (e.g.: ?!%+ ...)
>
> The password must not be used anywhere else.

> **Note**
>
> **Project protection for encryption of passwords**
>
> If you activate project protection for user administration in the TIA Portal, then all parameters and passwords within the project are encrypted. This also involves passwords for the web server users "SINAMICS" and "Administrator".
>
> Detailed information on project protection can be found in the online help under the heading of "User management (UMAC)".

###### Creating a password for the "SINAMICS" user

To enable the "SINAMICS" user and assign a password to it, proceed as follows:

1. Activate the "Enable SINAMICS user" option if it has not yet been activated.
2. Click on "Specify password".

   The "Specify password" dialog box opens.
3. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
4. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.
5. Click "OK" to confirm the input in the password dialog.

   If the two password inputs were identical, the input dialog closes. If the two inputs do not match, the input dialog remains open and an error message appears. The two inputs in the input dialog are also cleared. In this case, you must reenter the password in the two input fields.

   A prompt is made once for the password when the web site is called later.

###### Creating a password for the "Administrator" user

A password is also required to enable the "Administrator" user. For this reason, the procedure for enabling is slightly different than for the "SINAMICS" user:

1. Click on "Specify password".

   The "Specify password" dialog box opens.
2. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
3. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.
4. Click "OK" to confirm the input in the password dialog.

   If the two password inputs were identical, the input dialog closes. If the two inputs do not match, the input dialog remains open and an error message appears. The two inputs in the input dialog are also cleared. In this case, you must reenter the password in the two input fields. Once the password for the administrator has been assigned, this user also will be enabled automatically. The "Enable Administrator user" option is activated.

   A prompt is made once for the password when the web site is called later.

###### Deleting the password of the "SINAMICS" user

For the "SINAMICS" user, you can delete a password that has been created as follows:

1. Click the "Delete password" button.

   The password is deleted, and the message "The password has been deleted" is displayed.

> **Note**
>
> The "Administrator" user must have a password. If this user is enabled, then you can only change the administrator password but however you cannot delete it.

###### Changing an existing password

Existing passwords for "SINAMICS" and "Administrator" users can be changed as long as the user in question is enabled.

1. Click the "Change password" button.

   The "Change password" dialog box opens.
2. Enter the new password in the "New password" input field. Note that these entries are case-sensitive.
3. Enter the same password in the "Confirm password" field.

   For security reasons, the password inputs in the input fields are shown encrypted.

   The entry is checked. If all entries were correct, the message "Password has been changed" will appear.

###### Saving/transferring settings

Proceed as follows, after you have configured the web server for your S210 converter:

1. Save the project to apply the changes.
2. Subsequently transfer the settings to your S210 converter using the "Load to device" function.

##### Configuring NTP time synchronization

In the factory setting, SINAMICS S210 drives use an operating hours counter. Based on the operating hours, the SINAMICS S210 drive saves alarms and warnings that occur. However, with this method, the time stamps of different drives cannot be compared.

To obtain a comparable time stamp between several devices, you must change over the operating hours counting to time in the UTC format and synchronize with a time master (a control system).

This means that the events of all bus nodes, which are synchronized with the control system time, can be set in reference to one another.

###### Definitions

**System time (UTC) and local time**

With the Coordinated Universal Time (UTC) as basis, starting from the zero meridian, the local time is determined corresponding to the time offset and possible summer (daylight saving) and winter (standard) times. The Central European Time (CET) is calculated from the Coordinated Universal Time plus one hour. In the summer, the Central European Summer Time (CEST) applies which is calculated from the Coordinated Universal Time plus two hours. The NTP and SNTP protocols always send the UTC time according to the specification. If the current local time is to be received, then the appropriate settings or calculations must be performed.

**Network Time Protocol (NTP)**

NTP is used to synchronize clocks in a network. PCs, panels, CPUs etc. can synchronize the time via one or several servers.

An NTP client sends a telegram - with time stamps - to the NTP server. The server responds to this telegram (using an algorithm for example to take into account packet propagation times), and sets its clock based on the information of the telegram received.

An NTP client can have several entered time servers. Based on the stratum entered in the telegram (distance of a time server from a time source) and other factors, the client selects the best possible server and sends the request telegram to this server.

###### Requirements

- A project has been created.
- A SINAMICS S210 drive has been inserted in the device configuration.
- The drive is assigned to a PLC in the project.
- There is an online connection to the drive unit.

  Without an online connection, you must save the settings in the project and then load to the device.

###### Activating time synchronization using the Network Time Protocol (NTP)

A drive configured as NTP client synchronizes the time via a PROFINET connection with a SIMATIC PLC configured as NTP server (a time source).

Proceed as follows if you wish to activate time synchronization:

1. In the drive project configuration, select "Device configuration".
2. Select the drive in the device view and open the Inspector window.
3. In the Inspector Window under tab "General", select menu "Drive unit_X > Clock synchronization / Time".
4. Select the "Activate time synchronization via NTP server" option (p3103).

**Result:**

The IP address of the PLC used as time source is displayed in the "Server" field.

###### Setting local time

Proceed as follows to set the local time zone for NTP synchronization:

1. Select the required local time in area "Local time" in the drop-down list "Time zone" (p3106).

###### Additional information

Additional information regarding the NTP server functionality of SIMATIC S7-CPUs is provided in the [Siemens Industry Online Support-Portal](https://support.industry.siemens.com/cs/ww/en/view/82203451).

### Uploading a device configuration as new station

#### Overview

For all control modules, using the "Upload device as new station" function, you have the option of reading out the device configuration of a converter and to create as station (drive device) in your current Startdrive project.

#### Requirements

- A project has been created, or an existing project is open.
- There is a physical LAN connection between the drive and the PG/PC. The drive is switched on.
- An IP address has been assigned to the drive.

#### Procedure

To upload a device as a new station, proceed as follows:

1. In the project tree of the interface you are using click on "Update accessible devices".

   The drive is determined as accessible device. The appropriate IP address is displayed in square brackets.
2. Select the device and call the shortcut menu "Upload device as new station".

   Startdrive checks whether all prerequisites for uploading have been met.

   Uploading starts automatically if all of the prerequisites for uploading exist.

   If all of the prerequisites for uploading do not exist (e.g. components that have not been identified), then the "Upload preview" dialog box opens.

   - Check the messages in the dialog, and if necessary, activate the necessary actions in the "Action" column.

     As soon as uploading becomes possible, the "Upload from device" button is enabled.
   - Click the "Upload from device" button to start the upload.

#### Result

The project data has been uploaded as new drive device in your Startdrive project on the PC and created in the project tree.

### Optional: Configuring a controller with drive

This section contains information on the following topics:

- [Adding a controller (PLC)](#adding-a-controller-plc)
- [Networking the controller (PLC) and drive](#networking-the-controller-plc-and-drive)
- [Inserting a technology object into the SIMATIC S7 controller](#inserting-a-technology-object-into-the-simatic-s7-controller)
- [Interconnecting the technology object and SINAMICS drive](#interconnecting-the-technology-object-and-sinamics-drive)

#### Adding a controller (PLC)

##### Overview

If, in addition to the SINAMICS drive, you also want to use a controller in the device configuration, you must create a corresponding PLC in your project.

##### Requirements

- A new project has been created.

  - Or -
- An existing project has been opened.

##### Procedure

You can insert new drive units in the portal view or in the project view.

To insert drive units in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click on "Controller" to display the list of available controllers.
3. Select the required PLC from the "SIMATIC S7-XXXX" list.
4. Select the firmware version of the PLC that you are using.

   If the version numbers (compare: hardware to software) do not match, then it will not be possible to subsequently go online. On creation, the current firmware version is always suggested. If required, you can change the version number via the "Version" drop-down list.
5. Enter a device name in the field at the top with the same name and then click on "OK".

   If you leave the "Open device view" option activated, then the device view opens automatically.

**Variant 1: Inserting a device in the network view**

Alternatively, you can also insert the controller via the network view.

1. Open the network view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in the entry "SIMATIC S7-XXXX".
4. Drag & drop the PLC from the hardware catalog to the network view.

**Variant 2: Inserting a device in the topology view**

Alternatively, you can also insert the controller via the topology view.

1. Open the topology view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in the entry "SIMATIC S7-XXXX".
4. Drag & drop the PLC from the hardware catalog to the network view.

##### Result

The controller is inserted.

![Example: Inserting a PLC](images/148018056331_DV_resource.Stream@PNG-en-US.PNG)

Example: Inserting a PLC

Then you have to [network](#networking-the-controller-plc-and-drive) the SINAMICS drive with the controller in the network view and in the topology view.

#### Networking the controller (PLC) and drive

##### Overview

If you have created a controller and a SINAMICS drive in your project, you have to connect these two components to each other. You need to network the components both in the network view and in the topology view.

##### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created.

##### Procedure

Proceed as follows to establish the connection between the controller and the SINAMICS drive:

1. To open the network view, double-click the "Devices & Networks" entry in the project navigation.

   The network view opens.
2. Draw a connection between the PROFINET interface of the controller and PROFINET interface X150 of the drive by pressing and holding the mouse button.

   ![Example: PLC networked with the drive](images/148018078603_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: PLC networked with the drive](images/148018078603_DV_resource.Stream@PNG-en-US.PNG)

   Example: PLC networked with the drive

   The PROFINET connection is established, and the converter is assigned to the controller.
3. Click on PROFINET interface_1 [X1] of the controller.
4. In the secondary navigation under "Advanced options" and then under "Real time settings", double-click the setting "Synchronization".

   The "Synchronization" display area appears.
5. Select the "Sync master" setting from the "Synchronization role" drop-down list.
6. Switch to the topology view.
7. Draw a connection between Port_1 [X1.P1] of the controller and Port_1 [X150.P1] of the drive.

##### Result

The controller and the SINAMICS drive are networked with one another in the network and topology views.

#### Inserting a technology object into the SIMATIC S7 controller

##### Overview

Through the technology object, Motion Control functions such as positioning and synchronous axes are available to you. For this reason, insert a new technology object (TO) in the SIMATIC S7 controller. In the "Configuration" mask, you can assign the inserted SINAMICS drive directly and access the drive configuration.

The most common application for SINAMICS drives is positioning. To be able to perform positioning tasks in the SIMATIC S7 controller, you need to insert the Motion Control function "TO_PositioningAxis". Inserting a TO is described below based on the example of the Motion Control function "TO_PositioningAxis".

##### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created and is networked with the drive.

##### Procedure

To insert a technology object into the SIMATIC S7 controller, proceed as follows:

1. Make sure that the list with available functions for the SIMATIC S7 controller in the project tree is expanded.

   ![Inserting a technology object](images/148018114315_DV_resource.Stream@PNG-en-US.png)

   ![Inserting a technology object](images/148018114315_DV_resource.Stream@PNG-en-US.png)

   Inserting a technology object
2. Expand the "Technology objects" entry.
3. Double-click the "Add new object" entry.

   The corresponding dialog opens.

   ![Dialog: Add new object](images/148018118283_DV_resource.Stream@PNG-en-US.PNG)

   ![Dialog: Add new object](images/148018118283_DV_resource.Stream@PNG-en-US.PNG)

   Dialog: Add new object
4. Click the "Motion Control" button to show the available technology objects.
5. Select the "TO_PositioningAxis" object from the "Motion Control" list.
6. If necessary, assign a different name for the TO in the input field "Name".
7. Click "OK".

##### Result

The "TO_PositioningAxis" technology object has been inserted and can be configured.

#### Interconnecting the technology object and SINAMICS drive

##### Overview

The inserted technology object "TO_PositioningAxis" must be interconnected with the SINAMICS drive.

##### Requirements

- A project is open.
- A SINAMICS drive has been created and specified.
- A controller (e.g. SIMATIC S7-1500) has been created and is networked with the drive.

##### Procedure

1. In the project tree, double-click the "Configuration" entry under the created technology object.

   The "Basic parameters" screen form opens.
2. Select the entry "Hardware interface" in the secondary navigation.

   The corresponding screen form opens.
3. Open the selection list in the "Drive" selection box.

   A selection list opens.

   ![Configure the HW interface](images/148018163467_DV_resource.Stream@PNG-en-US.png)

   ![Configure the HW interface](images/148018163467_DV_resource.Stream@PNG-en-US.png)

   Configure the HW interface
4. Expand the "PROFINET IO system (100)" entry.
5. Click on the displayed converter (in this case: "Drive unit_2").

   Telegram 105 is automatically preset.
6. Click on the icon ![Procedure](images/148018155531_DV_resource.Stream@PNG-en-US.png) to confirm the selection.

   The "Device configuration" setting option is enabled. In addition, the "Drive configuration" setting option is displayed and enabled.
7. Click the green icon ![Procedure](images/148018159499_DV_resource.Stream@PNG-en-US.png) to get to the basic parameterization of the converter.

##### Result

The "Basic parameter assignment" screen form in the "Drive configuration" display area opens. You can find additional details on the configuration of technology objects in the [SIMATIC help](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#introduction-s7-1500-s7-1500t).

## Establishing an online connection to the drive

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Going online](#going-online)
- [Checking the firmware consistency](#checking-the-firmware-consistency)
- [Online connection via Ethernet IE](#online-connection-via-ethernet-ie)
- [Online connection via PROFINET IO](#online-connection-via-profinet-io)

### Fundamentals

#### Interfaces used

SINAMICS S210 converters have two interfaces which enable online communication between the PG/PC and the drive.

> **Note**
>
> General information regarding the online mode in the TIA Portal is available under "[Connecting devices online](Using%20online%20and%20diagnostics%20functions.md#connecting-devices-online)" in the online help.

> **Note**
>
> **Comply with the installation und industrial security guidelines - cell protection concept**
>
> - Ethernet commissioning interface X127
>
>   The Ethernet interface X127 is intended for commissioning and diagnostics and therefore needs to be accessible at all times (e.g. for servicing).
>
>   In addition, the following restrictions apply to X127:
>
>   - Only local access is permitted.
>   - No networking or only local networking in a closed control cabinet is permitted.
> - PROFINET interface X150
>
>   The network with which interface X150 is connected must be separated from the rest of the plant network in accordance with the Defense in Depth concept. Manual access to cables and possibly open connections must take place in a protected fashion, for example, in a control cabinet.

The PROFINET addresses are in the range of the PROFINET subnet of a SIMATIC S7 controller so that you can network the drive unit with a controller without having to adapt the subnet mask and the IP address.

![Interfaces S210](images/148018211211_DV_resource.Stream@PNG-en-US.png)

Interfaces S210

#### IP addresses

**Control Unit (hardware):**

| Interface | IP address | Subnet mask |
| --- | --- | --- |
| Ethernet interface X127 | 169.254.11.22 | 255.255.0.0 |
| PROFINET interface X150 | determined from CPU | determined from CPU |

**Project:**

| Interface | IP address | Subnet mask |
| --- | --- | --- |
| Ethernet interface X127 | 169.254.11.22 | 255.255.0.0 |
| PROFINET interface X150 | 0.0.0.0 | 0.0.0.0 |

### Going online

#### Requirement

The firmware in the drive and the project is identical ([consistent](#checking-the-firmware-consistency)).

#### Selecting the preferred PG/PC interface

If you prefer to use a specific network interface of your PG/PC to establish an online connection, you can preset this interface.

1. Select the "Options > Settings" menu.

   The settings of the TIA Portal are displayed.
2. Select the "Online & diagnostics" entry in the secondary navigation.
3. In the "Preset connection path for online access" area, specify the type of the PG/PC interface as well as the interface.
4. Enable the option "Display dialog for setting the default connection path for online access".

#### Inconsistent state, online/offline

If the online and offline configurations deviate significantly from one another, then when "Going online", Startdrive flags this inconsistent state using this symbol ![Inconsistent state, online/offline](images/147998264587_DV_resource.Stream@PNG-en-US.png). Causes can include missing components in one of the two states or for example, a completely different closed-loop control mode (servo control instead of vector control).

**Remedial measures:**

- [Download to device](#loading-the-project-data-to-the-drive-unit)

  If the offline configuration is correct - however, the online configuration is not.
- [Upload from device](#loading-project-data-from-a-drive)

  If the online configuration is correct - however, the offline configuration is not correct.

### Checking the firmware consistency

#### Overview

An online connection between the PG/PC and drive unit is only possible when the PG/PC and drive unit are using the same firmware version.

Different firmware versions often occur in the following situations:

- A firmware update was performed for the drive unit. But the firmware saved in the Startdrive project is older.
- A new Startdrive version was installed. The latest firmware version was automatically set when you created a new project. However, your drive unit still uses an older version.

#### Procedure

1. Check the firmware version on your memory card with the "General" diagnostics screen form.

   - Connect your PG/PC to the drive unit using a LAN cable and switch on the drive unit.
   - In your Startdrive project, open the "Online access" entry in the project tree.
   - Select the network interface of your PG/PC.
   - Double-click "Update accessible devices".

     The accessible device is displayed with the IP address in the project tree.
   - In the project tree call the "Online & diagnostics" function for the displayed device.

     ![Firmware version of the hardware; example S120](images/147998327947_DV_resource.Stream@PNG-en-US.PNG)

     Firmware version of the hardware; example S120
2. Check the firmware version in the catalog information of the Control Unit in your current Startdrive project.

   - To do so, call the following menu: "Control Unit > Inspector window > General > Catalog information".

     ![Firmware version of the software; example S120](images/147998344715_DV_resource.Stream@PNG-en-US.PNG)

     Firmware version of the software; example S120

#### Result

An online connection is possible if the firmware versions are identical (see the example screens above).

If the firmware versions are not identical, then the versions must be aligned in order to establish an online connection. You usually upgrade the older version.

**Remedy:**

- Perform a firmware update on your drive unit (see "[Updating the firmware](Configuring%20SINAMICS%20S-G-MV%20drives.md#updating-the-firmware)").

  - OR -
- Create a new Startdrive project for your drive unit in Startdrive and set a newer firmware version for the Control Unit in the new project (see "[Adding drives offline](Configuring%20SINAMICS%20S-G-MV%20drives.md#adding-drives-offline)").

  If you are using an older Startdrive version, it may be necessary to install a more recent Startdrive version beforehand.

### Online connection via Ethernet IE

This section contains information on the following topics:

- [Going online via the Ethernet interface](#going-online-via-the-ethernet-interface)

#### Going online via the Ethernet interface

##### Overview

As the Ethernet commissioning interface has already been assigned an IP address, you can go online directly.

If you are not using a new project and devices have already been created, check the IP address of the interface in the project in the Inspector window under "Properties > General > Ethernet addresses" and the IP address assigned to the device. The addresses and subnet masks must be identical.

##### Requirements

- A SINAMICS project with a corresponding Control Unit (e.g. CU320-2 PN) has been created in Startdrive.
- There is a physical connection between the Ethernet interface of your PG/PC and the Ethernet commissioning interface of your drive unit (X127).
- The firmware version of the Control Unit is [identical](#checking-the-firmware-consistency) to the firmware version used in the Startdrive project.

##### Quick search via "Online access"

For a quick overview, you can start a search at the desired interface in "Online access". If the wiring to your drive is error-free and you have wired the correct drive (LED flashing for checking), the drive is displayed with the appropriate IP address.

![Online access](images/147998391819_DV_resource.Stream@PNG-en-US.PNG)

Online access

##### Procedure: Going online

Once you have found the drive under "Online access", establish an online connection. The first time you establish a connection, you must set the "PG/PC interface" and "Connection to interface/subnet" parameters:

1. Click the "Go online" button.

   The "Go online" dialog is called.

   ![Go online](images/147998395787_DV_resource.Stream@PNG-en-US.png)

   ![Go online](images/147998395787_DV_resource.Stream@PNG-en-US.png)

   Go online
2. If no correctly configured interface has been set yet, then select the type of the PG/PC interface (1).
3. If no interface has been preset yet, select the PG/PC interface of your PC (2).
4. Specify the Ethernet interface (X127) of the Control Unit (3) as the connection to the interface/subnet.
5. Click "Start search" (4) to search for the drive unit with the set parameters.

   The devices found are displayed under "Select target device".
6. Select your drive in the table (5).
7. Click "Connect" to establish an online connection to the drive unit (6).

##### Result

An online connection has been established between the PG/PC and the drive unit. The settings are used automatically the next time you go online and the "Go online" dialog is no longer displayed.

### Online connection via PROFINET IO

This section contains information on the following topics:

- [Using the PROFINET IO interface](#using-the-profinet-io-interface)
- [Search for the target device (accessible devices)](#search-for-the-target-device-accessible-devices)
- [Assigning an IP address](#assigning-an-ip-address)
- [Going online via the PROFINET interface](#going-online-via-the-profinet-interface)
- [Assigning PROFINET device names](#assigning-profinet-device-names)
- [Comparing IP addresses](#comparing-ip-addresses)
- [Setting the PG/ PC interface](#setting-the-pg-pc-interface)
- [Resetting PROFINET interface parameters](#resetting-profinet-interface-parameters)

#### Using the PROFINET IO interface

##### Requirement

The PROFINET interface of the Control Unit (e.g. CU320-2 PN) is the X150. The device and the PG/PC must be in the same subnet for an online connection to be possible.

You must select the IP address and subnet mask accordingly.

##### Procedure

To establish an online connection between a PG/PC and a device, proceed as follows:

1. Search for a device using the online access
2. Assign the device an IP address and device name.
3. Adapt the IP address and subnet mask of the configured device in the project.
4. Compare the assigned interface data with the configured interface data.

---

**See also**

[Search for the target device (accessible devices)](#search-for-the-target-device-accessible-devices)

#### Search for the target device (accessible devices)

##### Overview

The TIA Portal can search for the device via the online access of your PG/PC.

##### Requirements

- A SINAMICS project with a corresponding Control Unit (e.g. CU320-2 PN) has been created in Startdrive.
- There is a physical connection between the Ethernet interface of your PG/PC and the PROFINET interface of your device (X150).
- The firmware version of the hardware is the same as the firmware version used in the Startdrive project.

##### Procedure

To search for a device, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your computer.
3. Double-click "Update accessible devices".

   The device is displayed in the project tree.

   ![PROFINET online access](images/147998504203_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET online access](images/147998504203_DV_resource.Stream@PNG-en-US.png)

   PROFINET online access

   If the communication parameters are at their factory settings (IP address 0.0.0.0 and no device name), then the default device names of the TIA Portal ("Device" in this case) and the MAC address are displayed.

   If you want to go online on the device (e.g. the drive), you must assign an IP address and a device name.
4. Select the device and, if required, assign an IP address and a device name, see also [Assigning an IP address](#assigning-an-ip-address) and [Assigning PROFINET device names](#assigning-profinet-device-names).

   ![PROFINET with IP address](images/156161975435_DV_resource.Stream@PNG-en-US.png)

   ![PROFINET with IP address](images/156161975435_DV_resource.Stream@PNG-en-US.png)

   PROFINET with IP address

   The device is displayed with the device name (in this case, drive_1) and the IP address (in this case, 198.168.0.21).

   If you cannot assign an IP address and device name, you may have to check the IP address of your PG/PC. It must be in the same address range as the address of the device, see also [Setting the PG/ PC interface](#setting-the-pg-pc-interface).

##### Result

You have found the device in the PROFINET subnet and assigned an IP address and a device name. You only have to establish an online connection.

#### Assigning an IP address

##### Overview

Before you can go online on a device via PROFINET, you must assign the PROFINET interface of the device a suitable IP address.

- The PROFINET interface of the device does not have an IP address in the delivered state.
- If the device already has an IP address, perform the "[Reset to factory settings](#resetting-profinet-interface-parameters)" function to reset it to 0.0.0.0.

The PROFINET interface has already been assigned an IP address and subnet mask in the project:

- IP address: 192.168.1.2
- Subnet mask: 255.255.255.0

The IP address and the subnet mask are in the subnet of an S7-1500 controller, which simplifies networking the controller and drive.

> **Note**
>
> **Assigning the IP address without "Reset to factory settings"**
>
> If the device already has an IP address, you can overwrite it with a new address. However, you must perform a **Power off/on** for the setting to take effect.

##### Requirement

- There is a physical connection between the Ethernet interface of your PG/PC and the PROFINET interface of your device (X150).

##### Procedure

To assign an IP address, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the entry "Assign IP address".

   ![Assigning an IP address](images/147998544651_DV_resource.Stream@PNG-en-US.PNG)

   ![Assigning an IP address](images/147998544651_DV_resource.Stream@PNG-en-US.PNG)

   Assigning an IP address
7. Enter a matching IP address for your project or correct an existing IP address.
8. Enter a suitable subnet mask.
9. Click the "Assign IP address" button.
10. Double-click "Update accessible devices".

    This display of the IP address is updated. The MAC address is read out automatically.

##### Result

The IP address has been assigned to the device.

---

**See also**

[Assigning PROFINET device names](#assigning-profinet-device-names)

#### Going online via the PROFINET interface

##### Procedure

If you have found the device at "Online access", establish an online connection. The first time you establish a connection, you must set the "PG/PC interface" and "Connection to interface/subnet" parameters:

1. Click the "Go online" button.

   The "Go online" dialog is called.

   ![Connecting online via PROFINET interface](images/147998593163_DV_resource.Stream@PNG-en-US.png)

   ![Connecting online via PROFINET interface](images/147998593163_DV_resource.Stream@PNG-en-US.png)

   Connecting online via PROFINET interface
2. If no correctly configured interface has been set yet, select the type of the PG/PC interface.
3. If no interface has been preset yet, select the PG/PC interface of your PC.
4. Specify the PROFINET interface (X150) of the Control Unit as the connection to the interface/subnet.
5. Click "Start search" to search for the device with the set parameters.

   The devices found are displayed in a table under "Select target device".
6. Select your device in the table.
7. Click "Connect" to establish an online connection to the device.

##### Result

An online connection has been established between the PG/PC and the device. The settings are used automatically the next time you go online and the "Go online" dialog is no longer displayed.

#### Assigning PROFINET device names

##### Overview

In addition to the IP address, the device must also be assigned a device name for operation in a PROFINET subnet.

The name must comply with the DNS name syntax; for detailed information, review the TIA Portal online help.

- The device does not have a device name when it is delivered
- If the device already has a name, perform "Reset to factory settings". The name is deleted.

##### Requirement

- There is a physical connection between the Ethernet interface of your PG/PC and the PROFINET interface of your device (X150).

##### Procedure

To assign a name, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the entry "Assign PROFINET device name".

   ![Assigning names](images/147998628363_DV_resource.Stream@PNG-en-US.png)

   ![Assigning names](images/147998628363_DV_resource.Stream@PNG-en-US.png)

   Assigning names
7. Enter a device name.
8. Click "Assign name" to assign a name to the device.
9. Update the interface under "Online access".

##### Result

The name has been assigned to the device.

#### Comparing IP addresses

##### Overview

After you have assigned the IP address to the device, check the IP address and subnet mask set in the project. An online connection can only be established when the settings in the project and in the device are identical.

##### Requirement

- There is a physical connection between the Ethernet interface of your PG/PC and the PROFINET interface of your device (X150).

##### Procedure

To compare the address, proceed as follows:

1. Search for the device at "Online access" and "Update accessible devices".

   The device is displayed with IP address and subnet mask in the diagnostics view.
2. Switch to the device view and open the Inspector window.
3. Select the "Properties" and "General" tabs in the Inspector window.
4. In the secondary navigation of the Inspector window, select the entries "PROFINET interface [X150]" and "Ethernet addresses".

   The properties of the interface are displayed.
5. Compare the IP address and subnet mask with the settings under "Online access".

   ![IP address in the project](images/147998663435_DV_resource.Stream@PNG-en-US.png)

   ![IP address in the project](images/147998663435_DV_resource.Stream@PNG-en-US.png)

   IP address in the project

##### Result

If both settings are the same, you can establish an online connection.

#### Setting the PG/ PC interface

##### Overview

The PROFINET communication between the device and the PG/PC is established via an Ethernet interface. If you have not yet adapted the IP address and subnet mask of the PG/PC interface, you can use the following procedure.

> **Note**
>
> **Assigning a temporary IP address**
>
> If you search for the device via "Accessible devices" or go online for the first time, the PG/PC can automatically be assigned a temporary IP address in the subnet.

##### Requirement

For PROFINET communication, the IP address and the subnet mask of the PG/PC interface must lie within the number range of the PROFINET subnet.

##### Displaying the properties of the PG/PC interface

The following procedure describes the process for the "Ethernet" interface type using the "Online access" function.

To assign the interfaces, proceed as follows:

1. Navigate to the appropriate interface in the project tree under "Online access".
2. In the shortcut menu, click "Properties".

   ![Online access properties](images/147998729099_DV_resource.Stream@PNG-en-US.png)

   Online access properties
3. In the next step, select the subnet and apply the setting with "OK" where applicable.

   ![Assigning a subnet](images/147998733067_DV_resource.Stream@PNG-en-US.png)

   Assigning a subnet

##### Adding an IP address in the subnet

1. Click ![Adding an IP address in the subnet](images/147998737035_DV_resource.Stream@PNG-en-US.png) on the toolbar.  
   The "Select devices for setting up the online connection" dialog box opens.

   ![Selecting a device for online connection](images/147998753803_DV_resource.Stream@PNG-en-US.png)

   Selecting a device for online connection
2. Select the device and confirm with "Connect".
3. Assign an IP address to the PG/PC within the subnet of the device.  
   If you have not already done so, it is now possible to temporarily assign a suitable IP address from the subnet of the device via the Windows Control Panel.

   ![Assigning an IP address](images/147998761739_DV_resource.Stream@PNG-en-US.png)

   Assigning an IP address
4. Click "Yes" to assign the IP address.

   ![IP address added](images/147998778507_DV_resource.Stream@PNG-en-US.png)

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

   ![Displaying and deleting temporary IP addresses](images/147998757771_DV_resource.Stream@PNG-en-US.png)

   Displaying and deleting temporary IP addresses

#### Resetting PROFINET interface parameters

##### Overview

If problems occur during the commissioning via PROFINET, it is recommended that the interface parameters of the drive be reset to the factory settings.

##### Requirement

- Physical connection between the Ethernet interface of your PG/PC and the Ethernet or PROFINET interface of your drive unit.

##### Procedure

To restore the factory settings, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices" in the project tree.

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the "Resetting PROFINET interface parameters" entry in the secondary navigation.

   ![Resetting the PROFINET interface parameters](images/148018312459_DV_resource.Stream@PNG-en-US.PNG)

   ![Resetting the PROFINET interface parameters](images/148018312459_DV_resource.Stream@PNG-en-US.PNG)

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
- [DRIVE-CLiQ wiring diagnostics](#drive-cliq-wiring-diagnostics)
- [Online & diagnostics](#online-diagnostics)

### Device diagnostics

#### Display device faults

Faults, warnings, or a requirement for maintenance pending on the device are displayed as icons on the Startdrive. The icons have different colors according to the seriousness of the situation. The icons are also displayed in the network and topology view so that consistent diagnostics is possible in these views.

The table lists the possible icons.

| Icon | Meaning |
| --- | --- |
| ![Display device faults](images/147999101579_DV_resource.Stream@PNG-en-US.png) | OK = No fault or maintenance required |
| ![Display device faults](images/147999105547_DV_resource.Stream@PNG-en-US.png) | Maintenance required |
| ![Display device faults](images/147999109515_DV_resource.Stream@PNG-en-US.png) | Maintenance requirement for a subordinate component |
| ![Display device faults](images/147999113483_DV_resource.Stream@PNG-en-US.png) | Maintenance request |
| ![Display device faults](images/147999117451_DV_resource.Stream@PNG-en-US.png) | Maintenance request for a subordinate component |
| ![Display device faults](images/147999121419_DV_resource.Stream@PNG-en-US.png) | Fault/error |
| ![Display device faults](images/147999125387_DV_resource.Stream@PNG-en-US.png) | Fault/error at a subordinate component |
| ![Display device faults](images/147999129355_DV_resource.Stream@PNG-en-US.png) | Connection error to the device |
| ![Display device faults](images/147999133323_DV_resource.Stream@PNG-en-US.png) | Establish a connection |
| ![Display device faults](images/147999137291_DV_resource.Stream@PNG-en-US.png) | The diagnostic status is determined |
| ![Display device faults](images/147999141259_DV_resource.Stream@PNG-en-US.png) | The configured device and the actual device have incompatible types. |
| ![Display device faults](images/147999145227_DV_resource.Stream@PNG-en-US.png) | The device is only available in the offline configured device configuration and has been deactivated. |

The colored icons are displayed in the following areas of the TIA Portal:

- Project tree
- Device view
- Device overview

![Diagnostics icons in the Startdrive/TIA Portal](images/148018316683_DV_resource.Stream@PNG-en-US.PNG)

Diagnostics icons in the Startdrive/TIA Portal

#### Display messages

Proceed as follows to display any messages that have been assigned to an icon:

1. Double click the icon.
2. The "Display message" tab is moved into the foreground of the inspector window.

   All pending messages are displayed there.

#### Diagnostics and comparison icons

The diagnostics status and comparison status of drives and higher-level controllers are displayed via icons on the user interface.

A description of the icons can be found under "Displaying diagnostics status and comparison status using icons."

### DRIVE-CLiQ wiring diagnostics

#### Errors in the DRIVE-CLiQ wiring of the drive line-up

All DRIVE-CLiQ components of the drive line-up are displayed in the device view. If the DRIVE-CLiQ wiring of the offline configuration is different to the actual wiring, these errors are displayed in the device view. A reference-target adjustment of the DRIVE-CLiQ wiring is performed online.

If you call the tooltip of an incorrectly connected port, the cause of the error (reference-actual adjustment) is described. You must then either change the wiring on the device or adapt it in the device view.

| Symbol | Meaning |
| --- | --- |
| ![DRIVE-CLiQ without error](images/148018340235_DV_resource.Stream@PNG-en-US.PNG)   DRIVE-CLiQ without error | ![DRIVE-CLiQ with error](images/148018344203_DV_resource.Stream@PNG-en-US.PNG)   DRIVE-CLiQ with error |

### Online & diagnostics

This section contains information on the following topics:

- [Overview](#overview-4)
- [Diagnostics](#diagnostics-1)
- [Functions](#functions)
- [Backup and restore](#backup-and-restore)
- [Communication](#communication)

#### Overview

In the diagnostics view, you are working in online mode and see the most important drive information or make important basic settings.

> **Note**
>
> Comprehensive further information on online and diagnostic functions in the TIA Portal is available in the Startdrive online help under "Using online and diagnostic functions".

##### Requirement

- Physical connection between the Ethernet interface of your PG/PC and the Ethernet or PROFINET interface of your drive.

##### Calling diagnostics

To display diagnostics and diagnostic functions for a drive unit connected online, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Establish an online connection to the device.

   You can also establish the online connection beforehand.
5. In the project tree call the "Online & diagnostics" function for the displayed device.

##### Result

The diagnostics view is displayed in the Startdrive working area. Use the secondary navigation of this diagnostics view to retrieve various diagnostic information for the drive unit and perform some important basic functions. The following illustration shows the structure of a diagnostics view:

![Diagnostics view](images/148018378635_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Screen form for online diagnostics and important basic functions |

Diagnostics view

#### Diagnostics

In the diagnostics view you obtain the following diagnostic information from the connected converter:

- General

  Information about component, module and manufacturer
- Active warnings

  Information on active warnings and alarms
- Actual values

  Information about the most important parameter actual values and status bits.
- Safety Integrated Functions status

  Information on the current status of the Safety Integrated Functions.

  For detailed information on these functions, refer to the "[Function status](Commissioning%20SINAMICS%20S210%20drives.md#function-status)" section.
- PROFINET interface (X150)

  - Ethernet address

    Information about IP parameters (IP address and subnet mask) and network connection (MAC address)
  - Communication

    Information on transmit and receive direction (PZDs of the telegrams, e.g. 105).

    You can find detailed information on PZDs and telegrams in the "[Communication](#communication)" section.

You call the individual diagnostic information in the secondary navigation of the diagnostics view.

##### Requirement

- There is an online connection between the drive and the PC/PG.

  Diagnostic information can only be read out in online mode.

#### Functions

The diagnostics view also provides important diagnostic information on the basic functions of the drive unit. You can configure the settings of these basic functions in the diagnostics view:

- [Assigning an IP address](#assigning-an-ip-address)
- [Assigning a PROFINET device name](#assigning-profinet-device-names)
- [Reset of PROFINET interface parameters](#resetting-profinet-interface-parameters)
- [Firmware update](#updating-the-firmware)
- [Using functions subject to license](#activate-trial-license-mode)

You call the individual functions in the secondary navigation of the diagnostics view.

##### Requirement

- There is an online connection between the drive and the PC/PG.

  The direct functions can only be performed in online mode.

#### Backup and restore

##### Description

The "Backup/Restore" screen form offers the following options:

- Retentively save RAM data
- Restart drive (POWER ON)
- Restoring factory settings

##### Requirements

- Physical connection between the Ethernet interface of your PG/PC and the Ethernet or PROFINET interface of your drive.
- The drive has been switched on and is supplied with power.
- Optional memory card is inserted (for parameter backup).
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

##### Call "Backup/Restore" from the diagnostics view

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices".

   The accessible participant is displayed with IP address in the project navigation.
4. In the project tree call the "Online & diagnostics" function for the displayed device.

   The diagnostics view is displayed.
5. In the secondary navigation of the diagnostics view, select menu "Functions > Backup/Restore".

   In the diagnostics view, the "Backup/Restore" screen form is opened and you can make the required settings.

##### Call "Backup/Restore" via Online & diagnostics

1. In the project tree of your drive device, double-click on "Online & diagnostics".

   The "Online access" display area is displayed.
2. In the secondary navigation, select menu "Functions > Backup/Restore".

   The "Backup/Restore" screen form opens.
3. In the toolbar, click "Go online" and make all of the necessary connection settings.

   The "Backup/Restore" screen form is now displayed in the online mode and you can make the required settings.

##### Backing up parameterization

The parameter values are normally saved as volatile data in the RAM of the drive. To save the data retentively, proceed as follows:

1. In the "Retentively save RAM data" area, click on "Save":

   The program checks whether a memory card is available. If a matching memory card is detected, the parameter values are saved retentively to this card.

##### Restarting drives

For a POWER ON of your drive, proceed as follows:

1. In the area "Restart the drive", click on "Restart".

   The drive is restarted. The LEDs indicate the current drive status.

##### Restoring factory settings

We recommend restoring the factory setting in the following cases:

- Interruption of the line voltage during commissioning
- Incomplete commissioning
- Ambiguity regarding the previous parameterization or previous use of the drive

To restore the factory settings, proceed as follows:

1. Click "Start" in the "Restoring factory settings" area.

   The factory settings of all parameters (including Safety Integrated) are now imported back into the drive unit.

#### Communication

This section contains information on the following topics:

- [S210 telegrams receive direction](#s210-telegrams-receive-direction)
- [S210 telegrams send direction](#s210-telegrams-send-direction)

##### S210 telegrams receive direction

###### Description

By default, the components and interconnections of the PROFIdrive telegrams in the receive direction are displayed for the converter in this screen form (e.g. 105, 700 or 750).

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "PROFIsafe" or "Supplementary data" area.

**Telegram structure**

The interconnections for the process data in the receive direction are created automatically for the standard and manufacturer-specific telegrams.

Only those telegrams available for the drive object are offered. The interconnections of the control words or receive words have already been created.

The following information of the displayed telegrams is displayed:

| Telegram type | PZD | Display of the value | Format switchover | Control words |
| --- | --- | --- | --- | --- |
|  | The numbering and arrangement of the process data. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | List of the control words that are transmitted in the telegram. |
| PROFIdrive  3, 5, 102, 105 | X | X | X | X |
| PROFIsafe  30, 901 | X | X | X | X |
| Supplementary data 700, 701 | X | X | X | X |
| Torque  750 | X | X | X | X |

##### S210 telegrams send direction

###### Description

By default, the components and interconnections of the PROFIdrive telegrams are displayed in this screen form for the converter in the sending direction (e.g. 105, 700 or 750).

Use the telegram configuration (![Description](images/147853831051_DV_resource.Stream@PNG-en-US.png)) to add additional telegrams (see table). The content of this selected telegram is then displayed in the "PROFIsafe" or "Supplementary data" area.

**Telegram structure**

The interconnections for the process data in the send direction are created automatically for the standard and manufacturer-specific telegrams.

The following information of the displayed telegrams is displayed:

| Telegram type | Status words | Value | Format switchover | PZD |
| --- | --- | --- | --- | --- |
|  | List of the status words that are transmitted in the telegram. | Value of the process data (PZD) | Switching the value of the process data to a different display (hex, bin, dec). | Numbering and arrangement of the process data. |
| PROFIdrive  3, 5, 102, 105 | X | X | X | X |
| PROFIsafe  30, 901 | X | X | X | X |
| Supplementary data 700, 701 | X | X | X | X |
| Torque  750 | X | X | X | X |

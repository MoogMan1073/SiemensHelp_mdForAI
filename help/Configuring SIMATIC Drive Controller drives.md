---
title: "Configuring SIMATIC Drive Controller drives"
package: StdrSIMATICDriveControllerConfenUS
topics: 168
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring SIMATIC Drive Controller drives

This section contains information on the following topics:

- [System overview](#system-overview)
- [Startdrive user interface](#startdrive-user-interface)
- [Fundamentals](#fundamentals-1)
- [Sequence of a device configuration](#sequence-of-a-device-configuration)
- [Adding and assigning parameters](#adding-and-assigning-parameters)
- [Establishing an online connection to the PLC](#establishing-an-online-connection-to-the-plc)
- [Diagnostics](#diagnostics)
- [Testing the drive settings using the control panel](#testing-the-drive-settings-using-the-control-panel)

## System overview

This section contains information on the following topics:

- [Fundamentals](#fundamentals)
- [Structure of the Drive Controller](#structure-of-the-drive-controller)
- [DRIVE-CLiQ interfaces](#drive-cliq-interfaces)
- [Scalability](#scalability)
- [System components and automation levels](#system-components-and-automation-levels)
- [Additional information](#additional-information)

### Fundamentals

The SIMATIC Drive Controller is a drive-based control system in the SIMATIC S7-1500 range.

![SIMATIC DC](images/148039640459_DV_resource.Stream@PNG-en-US.png)

SIMATIC DC

A SIMATIC Drive Controller integrates the following functions in a SINAMICS S120 Booksize Compact housing:

- Fail-safe SIMATIC S7-1500 technology CPU with integrated technology I/O
- SINAMICS S120 drive control

Both components are called "CPU" and "SINAMICS Integrated" in this documentation.

The integrated SINAMICS S120 CPU 150xD is based on a CU320-2 Control Unit and can control:

- a maximum of 6 drives with servo control; or
- a maximum of 6 drives with vector control; or
- a maximum of 12 drives with U/f control

Two fail-safe technology CPUs with scaled performance are available. Safety Integrated on the CPU and drive sides means that you can use the system in fail-safe applications.

The SIMATIC Drive Controller supports communications via PROFINET IO and PROFIBUS DP.

**Functions and components that are not supported:**

SINAMICS Integrated offers you a functional subset of the SINAMICS S120 CPU 150xD drive functions relevant in the control context. The SIMATIC Drive Controller does not support the following functions/components:

- Logic processing integrated in the drive using Drive Control Chart (DCC)
- Drive Control Block (DCB)
- SINAMICS web server
- CBE20 Communication Board

> **Note**
>
> **Use of SINAMICS S120 CPU 150xD**
>
> Additional Control Units connected to the SIMATIC Drive Controller have the complete functional scope that S7-1500 CPUs provide.

**TIA Portal applications that are required**

Both of the following applications are required to be able to practically configure a SIMATIC Drive Controller:

- Step 7 Professional V16 or higher
- Startdrive V16 or higher

### Structure of the Drive Controller

#### Structure

The system based on a SIMATIC Drive Controller can comprise the following components as maximum configuration:

- Power supply for the SIMATIC Drive Controller and DRIVE-CLiQ components
- SIMATIC Drive Controller (with integrated CU 320-2)
- SINAMICS S120 power units:

  - SINAMICS Line Modules
  - SINAMICS Motor Modules
  - SINAMICS Power Modules
- Motors with/without DRIVE-CLiQ
- DRIVE CLiQ Hub Modules
- Terminal Boards (TB)
- Terminal Modules (TM)
- Sensor Modules (SMx)
- Voltage Sensing Modules (VSM)

#### Sample configuration

![Example: Structure of a SIMATIC Drive Controller in a system](images/148039662859_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | HMI device |
| ② | SIMATIC Drive Controller |
| ③ | Line Module |
| ④ | SINAMICS S120 Double Motor Module |
| ⑤ | SINAMICS S120 Single Motor Module |
| ⑥ | SIMOTICS S servomotor |
| ⑦ | SINAMICS Terminal Module |
| ⑧ | SINAMICS Sensor Module Cabinet-Mounted |

Example: Structure of a SIMATIC Drive Controller in a system

### DRIVE-CLiQ interfaces

SINAMICS Integrated has 4 DRIVE-CLiQ interfaces. 24 V/450 mA are available for each DRIVE-CLiQ to connect encoders and measuring systems.

You can connect all SINAMICS Integrated components - including the motors and encoders - via the common DRIVE-CLiQ serial interface.

DRIVE-CLiQ implements a high-performance point-to-point coupling for drive-internal communications between the various drive components (Line Module, Motor Module, Sensor Module, Terminal Module and motors).

You use the DRIVE-CLiQ interfaces of the SIMATIC Drive Controller for the following purposes:

- To connect the power units (Line Module, Motor Modules) to the closed-loop drive control of SINAMICS Integrated
- To connect motors equipped with DRIVE-CLiQ interface to the Motor Modules
- To connect encoder systems via Sensor Modules Cabinet-Mounted (SMC)
- To expand drive-related I/O using Terminal Modules (TM)

After it has been switched on, SINAMICS Integrated identifies all of the connected drive components via the DRIVE-CLiQ interface. During operation, cyclic drive-related data is exchanged isochronously with the drive components, e.g. parameters and diagnostic data.

#### Advantages and customer benefits

DRIVE-CLiQ provides the following benefits:

- The connected components are automatically identified, therefore reducing commissioning costs.
- Standardized cables and connectors reduce the variety of different parts and cut stock inventory costs.
- Seamless diagnostics down to the various drive components.
- Encoder evaluation functions for converting standard encoder signals to DRIVE-CLiQ are available for third-party motors and retrofit applications.

### Scalability

The SIMATIC Drive Controller provides you with the required flexibility and performance to address a wide range of open-loop control applications in machine and plant engineering.

The SIMATIC Drive Controller is scalable in the CPU and motion control computing power - as well as in the quantity structure - to address your requirements when it comes to plant and machine planning. It also allows you to configure your network via PROFINET IO and PROFIBUS DP.

#### Scalable performance class

SIMATIC Drive Controllers are scalable regarding their CPU and motion control computing power. The available integrated communication interfaces as well as SINAMICS Integrated are the same for all SIMATIC Drive Controllers. This allows you to simply scale your system according to the CPU performance class without having any impact on the plant or machine topology.

#### Scalable quantity structure

The integrated SINAMICS S120 closed-loop drive control of the SINAMICS Drive Controller controls either:

- max. 6 drives with servo control
- max. 6 drives with vector control
- max. 12 drives with U/f control

You can expand the drive quantity structure of a SIMATIC Drive Controller, for example using SINAMICS S120 (CU320-2) or SINAMICS S210 (e.g. for individual drives). In this case, the axis technology objects of the CPU execute the motion control functions for the SINAMICS Integrated drives and the externally connected drives. The maximum axis quantity structures on the CPU side are restricted by the available motion control resources.

![Configuration with SINAMICS S120 and SINAMICS S210](images/148039760267_DV_resource.Stream@PNG-en-US.png)

Configuration with SINAMICS S120 and SINAMICS S210

In principle, you can connect all drives that support the following:

- Standard PROFIdrive profile for drive technology
- PROFIdrive telegrams that can be used with SIMATIC S7-1500

> **Note**
>
> It is not possible to increase the drive-side computing power using a SIMOTION CX32‑2 Controller Extension for SIMOTION D4x5‑2 Control Units.

#### Scalable through modularization

In modular machine concepts, several control systems and drives are used that are controlled and traversed depending on one another.

SIMATIC Drive Controllers have the functionality of cross-PLC synchronous operation. With synchronous operation extending over PLCs, you can implement synchronous operation beyond device boundaries. This allows you to distribute high axis quantity structures over several CPUs and/or implement modular machine concepts.

For modular machine concepts, the functionality is distributed over several machine modules, each equipped with its own control. You can distribute leading value source and synchronous axes over various controls. The coupling between the leading axis/external encoder and the following axis is established isochronously via PROFINET IO with IRT. The axis clock cycles are synchronized.

![Example: System configuration with SIMATIC Drive Controller, SINAMICS S120 and SINAMICS S210](images/148039755403_DV_resource.Stream@PNG-en-US.png)

Example: System configuration with SIMATIC Drive Controller, SINAMICS S120 and SINAMICS S210

#### Scaling via technology I/O and technology modules

The SIMATIC Drive Controller CPU has motion control technology objects such as a modular S7-1500T-CPU.

The integrated 8 digital inputs/outputs (interface X142) provide the technology I/Os that can be parameterized.

Of the integrated 8 digital inputs/outputs of the SINAMICS Integrated (interface X122/132), you can also use the 8 digital inputs as probe inputs.

High-performance technology modules in the ET 200MP and ET 200SP distributed I/O system are available to expand the integrated technology I/O - for example, for additional probe inputs and cam outputs.

### System components and automation levels

SIMATIC Drive Controllers are especially used for production automation and motion control applications, for smaller up to high-end machines. The combination of SIMATIC S7-1500 CPU and integrated SINAMICS S120 drive control offers you powerful and flexible automation solutions that address a wide range of motion control applications:

- The process signals are connected to the central master computer via fieldbus
- The SIMATIC Drive Controller is seamlessly integrated in the individual automation levels across all communication standards.
- SIMATIC Drive Controllers control an axis group via the integrated SINAMICS Integrated drive and the extensive range of SINAMICS S120 power units (Line and Motor Modules).
- Motors are equipped with DRIVE-CLiQ interface simplify commissioning and diagnostics.
- You integrate motors without DRIVE-CLiQ interface, e.g. third-party motors or for retrofit projects, using Sensor Modules Cabinet-Mounted (SMC) or Sensor Modules External (SME). Terminal Modules (TM) are terminal expansion modules via DRIVE-CLiQ - e.g. for drive-related digital or analog inputs and outputs.
- The F-CPU integrated in the SIMATIC Drive Controller guarantees fail-safe operations and sequences.
- Technology I/Os are already integrated in the SIMATIC Drive Controller. When required, you can expand the SIMATIC Drive Controller to include technology modules in the ET 200MP and ET 200SP distributed I/O system.
- SIMATIC Drive Controllers are intended for installation in control cabinets with IP20 degree of protection.

The schematic diagram below shows the key components of a SIMATIC Drive Controller system that extends from the management level to the control level and down to the field level.

![Example: SIMATIC Drive Controller at the management, control and field levels](images/148039924619_DV_resource.Stream@PNG-en-US.png)

Example: SIMATIC Drive Controller at the management, control and field levels

---

**See also**

[Available components](#available-components)

### Additional information

Detailed information about "SIMATIC Drive Controllers" is provided in the System Manual having the same name. You can download this system manual in the SIOS portal from the following address.

[SIMATIC Drive Controller](https://support.industry.siemens.com/cs/ww/en/view/109766665)

## Startdrive user interface

This section contains information on the following topics:

- [Hardware catalog](#hardware-catalog)
- [Device configuration](#device-configuration)
- [Function view](#function-view)
- [Parameter view](#parameter-view)
- [Inspector window](#inspector-window)
- [Rotate & optimize screen forms](#rotate-optimize-screen-forms)
- [Icons for arithmetic and controller functions](#icons-for-arithmetic-and-controller-functions)

### Hardware catalog

This section contains information on the following topics:

- [Modules in the hardware catalog](#modules-in-the-hardware-catalog)
- [Available components](#available-components)

#### Modules in the hardware catalog

##### Control Unit and components of the integrated drive

In the following example, the modules of the integrated SINAMICS drive are saved in the hardware catalog as follows:

![Example: Drive Controller hardware](images/148040135563_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control Units; type S120 control modules available for the CPU 150xD |
| ② | Unspecified Line Modules |
| ③ | Unspecified Power Modules |
| ④ | Unspecified Motor Modules |
| ⑤ | Motors; the motors are sorted according to motor type |
| ⑥ | Measuring systems (encoder) |
| ⑦ | Supplementary system components (DQ hubs, TMs, VSMs) |

Example: Drive Controller hardware

> **Note**
>
> **Reference of the hardware catalog to the desired drive system**
>
> You can find an assignment of the available components of the internal drive in comparison with an S120 on page "[Available components](#available-components)".

##### PLC modules of the Drive Controller

As alternative, the Drive Controller uses one of the subsequently listed CPUs as PLC. Generally, the CPUs are selected when inserting the Drive Controller; however, they can also be subsequently changed with a [device replacement](#device-replacement-replacing-the-plc-in-the-drive-controller).

![PLC components](images/148040105995_DV_resource.Stream@PNG-en-US.PNG)

PLC components

#### Available components

In Startdrive all available hardware components can be configured in the function view or in the parameter view. A comparison between the typical components of an S120 and the components of a Drive Controller with integrated drive is shown below.

Which hardware components can be used in which drive system?

| Component / drive system | S120  CU320-2 | S120  CU310-2 | SIMATIC Drive Controller |
| --- | --- | --- | --- |
| **Control Unit** |  |  |  |
| 320-2 Control Unit | X | ‑ | ‑ |
| 310-2 Control Unit | ‑ | X | ‑ |
| S120 for the CPU 150xD   (as integrated SINAMICS drive) | ‑ | ‑ | X |
| **Line Modules** |  |  |  |
| Active Line Modules | X | ‑ | X |
| Basic Line Modules | X | ‑ | X |
| Smart Line Modules | X | ‑ | X |
| **Power Modules** |  |  |  |
| AC Power Module | X | X | X |
| Power Module PM 240-2  - CUA31/CUA32 Control Unit Adapter <sup>1)</sup> | X | ‑ | X |
| **Motor Modules** |  |  |  |
| Single Motor Modules | X | ‑ | X |
| Double Motor Modules | X | ‑ | X |
| **Motors** |  |  |  |
| DRIVE-CLiQ motors | X | X | X |
| Induction motors | X | X | X |
| Synchronous motors | X | X | X |
| Reluctance motors | X | X | X |
| Motor data input | X | X | X |
| **Measuring systems** |  |  |  |
| DRIVE-CLiQ encoder | X | X | X |
| SIN/COS encoder | X | X | X |
| SSI encoder | X | X | X |
| SIN/COS + SSI encoder | X | X | X |
| HTL/TTL encoder | X | X | X |
| HTL/TTL + SSI encoder | X | X | X |
| EnDat encoder | X | X | X |
| EnDat + SIN/COS encoder | X | X | X |
| Resolver encoder | X | X | X |
| **Supplementary system components** |  |  |  |
| CBE20 Communication Board | X | ‑ | - |
| DRIVE-CLiQ Hub Module DMx20 | X | X | X |
| TB30 Terminal Board | X | - | - |
| TM15 Terminal Module | X | X | X |
| TM31 Terminal Module | X | X | X |
| TM41 Terminal Module | X | X | X |
| TM120 Terminal Module | X | X | X |
| TM150 Terminal Module | X | X | X |
| VSM10 Voltage Sensing Module | X | X | X |
| <sup>1)</sup> Coupled to the "Blocksize" Power Module. Is inserted into the view with it. Cannot be selected separately in the hardware catalog. |  |  |  |
| List of all available components for each drive system |  |  |  |

> **Note**
>
> **No Sensor Modules in the hardware catalog**
>
> Sensor Modules cannot be assigned using the hardware catalog. Sensor Modules are permanently assigned to the various encoders. Sensor Modules can be selected indirectly by selecting an encoder and by specifying the encoder evaluation at a later time (see "[Encoder system connection](#encoder-system-connection)").

### Device configuration

This section contains information on the following topics:

- [Device view](#device-view)
- [Network view](#network-view)
- [Topology view](#topology-view)
- [Device configuration detection](#device-configuration-detection)

#### Device view

The device view is one of three working areas of the hardware and network editor. You undertake the following tasks here:

- Configuring and assigning device parameters
- Configuring and assigning module parameters
- Editing the names of devices and modules

Configure the drive line-up in the "Device view". You can insert components and edit the DRIVE-CLiQ connections via the DRIVE-CLiQ editor. You can call the device view by double-clicking the "Device configuration" entry in the project tree.

The device overview provides a tabular overview of all configured components and their data.

##### Structure

The following figure shows an overview of the device view (the DRIVE-CLiQ editor).

![Structure](images/147991718539_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Control Unit |
| ② | DRIVE-CLiQ interface |
| ③ | DRIVE-CLiQ connection |
| ④ | Infeed |
| ⑤ | Motor |
| ⑥ | Slot for option modules |
| ⑦ | Motor Module |
| ⑧ | Encoder |
| ⑨ | Bus interface, PROFINET in this case |

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

![Network view](images/148040158347_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Higher-level controller, in this case a SIMATIC DC |
| ② | Fieldbus (in this case, PROFINET IO) |
| ③ | Drive that is assigned as the IO device of a higher-level controller via fieldbus (in this case PROFINET IO). |
| ④ | Data from drive and controller |

Network view

The specific parameters of the selected element are displayed in the inspector window.

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147992020107_DV_resource.Stream@PNG-en-US.png) | Mode to network devices. |
| ![Toolbar](images/147992030987_DV_resource.Stream@PNG-en-US.png) | Mode to create connections. You can use the adjacent drop-down list to set the connection type. |
| ![Toolbar](images/147992041867_DV_resource.Stream@PNG-en-US.png) | Mode to create relations. |
| ![Toolbar](images/147991722635_DV_resource.Stream@PNG-en-US.png) | Opens the dialog for manual name assignment of PROFINET devices. For this purpose, the IO device must be inserted and connected online with the IO system. |
| ![Toolbar](images/147992052747_DV_resource.Stream@PNG-en-US.png) | Show interface addresses. You can edit the addresses for the MPI, PROFIBUS and Ethernet interfaces directly in the network view: Select the required address and then click on the selected address field or press [F2]. |
| ![Toolbar](images/147991777803_DV_resource.Stream@PNG-en-US.png) | Enables page break preview. Dotted lines are displayed at the positions where the page will break when printed. |
| ![Toolbar](images/147991799563_DV_resource.Stream@PNG-en-US.png) | Changes the division of the graphical area and table area of the editor view between horizontal and vertical. |
| ![Toolbar](images/147991788683_DV_resource.Stream@PNG-en-US.png) | You can zoom in (+) or zoom out (-) the view in increments using the Zoom icon or draw a frame around an area to be zoomed in. |
| ![Toolbar](images/147991932683_DV_resource.Stream@PNG-en-US.png) | Displays the name of the devices fully in the graphical view, if these are truncated to the right or left because of their length and therefore not displayed completely. |
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

![Topology view](images/148040200843_DV_resource.Stream@PNG-en-US.png)

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
| ![Toolbar](images/147991823243_DV_resource.Stream@PNG-en-US.png) | Saves the current table view. The layout, width and visibility of columns in the table view is stored. |

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

#### Device configuration detection

All components that could not automatically be assigned during the device configuration detection are listed in the "Non-assignable components" folder ([Detecting device configuration automatically](Configuring%20SINAMICS%20S-G-MV%20drives.md#advanced-detecting-processing-and-inserting-a-device-configuration)). These components can be manually assigned via drag-and-drop or via the shortcut menu of a main component.

The dialog has the following structure:

![Figure](images/147992240523_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Options** | **Explanation** |
| Universal (vector) | All axes are operated universally. |
| High dynamic (servo) | All axes are operated high dynamic. |
| Can be selected | The drive object type can be individually adapted for each motor control. |
| Parallel connection view | Enables/disables parallel connection view.   In the parallel connection view, only the parallel connection-capable components are displayed. These can be connected in parallel with components of the same type using drag & drop or using the shortcut menu. |
| **Columns** | **Explanation** |
| Module | Drive object (DO) with automatically assigned components. |
| Drive object type | Control type of the DO |
| Component type | Type of the individual component |
| Identification | Option to identify the component via flashing LED.   It is controlled on the Control Unit via parameters p9210 and p9211. |
| DRIVE-CLiQ connection | DRIVE-CLiQ connection of the component |
| Article No. | Article number of the component |

---

**See also**

[Advanced: Detecting, processing and inserting a device configuration](Configuring%20SINAMICS%20S-G-MV%20drives.md#advanced-detecting-processing-and-inserting-a-device-configuration)
  
[Rules for wiring with DRIVE-CLiQ](Configuring%20SINAMICS%20S-G-MV%20drives.md#rules-for-wiring-with-drive-cliq)

### Function view

This section contains information on the following topics:

- [Function view](#function-view-1)

#### Function view

##### Overview

You parameterize the drive using a graphical user interface in the "Function view". The individual masks (screen forms) are based on function diagrams and contain the required parameters.

> **Note**
>
> **All parameters**
>
> You can find all parameters of the drive in the "[Parameter view](#parameter-view-1)". Experts can then comprehensively parameterize the drive. However, the parameter view can only be called for the parameter assignment. The parameter view is not offered for commissioning and diagnostics.

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

##### Structure of the masks (screen forms)

The following figure shows an example of a mask (screen form) structure:

![Function view (example)](images/147992299787_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Icon: Saves data retentively. |
| ② | Icon: Restores the factory settings. |
| ③ | Icon: Shows invalid BICO interconnections. |
| ④ | Secondary navigation |
| ⑤ | Icon: Activates editing in online mode (e.g. for Safety and EPOS functions). |
| ⑥ | Icon: Saves editing in online mode (e.g. for Safety and EPOS functions). |
| ⑦ | Boxes: Enables the input of parameters/interconnection of BICO signals. |
| ⑧ | Boxes: Shows display parameters. |
| ⑨ | Button: Opens dialogs or lower-level screen forms for parameter assignment. |

Function view (example)

### Parameter view

This section contains information on the following topics:

- [Parameter view](#parameter-view-1)

#### Parameter view

##### Overview

The "Parameter view" (expert list) provides a clearly organized display of the parameters available for the device. For the "Parameter assignment", you can switch the working area between the "[Function view](#function-view-1)" and the "Parameter view".

> **Note**
>
> The "Parameter view" is not available for "Rotate & optimize" and "Diagnostics".

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

Parameters are the access points for the adaptation of the converters/drives and function blocks to the application, for interconnecting function blocks via connectors and binectors and for monitoring internal signals.

SINAMICS uses two types of parameters:

- Display parameters

  They are preceded by the letter "r". You cannot change the value of these parameters.
- Adjustable parameters

  They are preceded by the letter "p". You can change the value of these parameters within a defined range.

> **Note**
>
> **Locked parameters**
>
> Parameters can be locked in the parameter view to prevent changes from being made. In this case, they are identified by the![Overview](images/147992365067_DV_resource.Stream@PNG-en-US.PNG) icon. Parameters are always locked in the following cases:
>
> - When the parameters can only be changed online but not offline. In this case, the![Overview](images/147992365067_DV_resource.Stream@PNG-en-US.PNG) icon disappears as soon as you go online.
>
>   If the lock icon is also visible online, however, the following causes may be more likely:
> - When the parameter was set in a previous basic parameterization (such as in the device configuration) and any change to the parameter would subsequently have an effect on the structure.
> - When they are not intended to be changed manually by the user, for example, because they are configured by other programs (such as a controller).
> - When they are generally only going to be configured via screen forms in Startdrive. The display of these parameters in the parameter view is merely for the sake of clarity in this case.

##### Parameter display

The fields of the individual parameters are displayed in the list in color as follows:

| Editing level | Offline color | Online color |
| --- | --- | --- |
| Read only | Gray | Pale orange |
| Read/write | White | Orange |

##### Structure of the parameter view

The following figure shows the structure of the parameter view:

![Parameter view](images/147992361355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation: Restricts the parameter view to the required parameter group. Exception: MV drive units do not use secondary navigation in the parameter view. |
| ② | Drop-down list: Restricts the parameter views:   - Display standard parameters - Display extended parameters - Display service parameters |
| ③ | Parameter number |
| ④ | Parameter name |
| ⑤ | Value of the parameter |
| ⑥ | Unit |
| ⑦ | Data set: Displays the data set (MDS, DDS, etc.) to which the parameter belongs. |
| ⑧ | Minimum value |
| ⑨ | Maximum value |

Parameter view

##### Toolbar

The toolbar provides the following functions:

| Icon | Meaning |
| --- | --- |
| ![Toolbar](images/147992381835_DV_resource.Stream@PNG-en-US.png) | Expands or reduces all secondary navigation nodes. |
| ![Toolbar](images/147992385803_DV_resource.Stream@PNG-en-US.png) | Expands or reduces all nodes below the selected node. |
| ![Toolbar](images/147992389771_DV_resource.Stream@PNG-en-US.png) | Compares the parameters of the drive object with another parameter set.   - In offline mode, the parameters are compared to the factory settings by default. - In online mode, the parameters are compared to the offline settings by default. - The comparison can also be deactivated again. |
| ![Toolbar](images/147992406539_DV_resource.Stream@PNG-en-US.png) | Starts a CSV export:   - Save all displayed parameters in a CSV file. - Save all parameters of the drive object in a CSV file. |
| ![Toolbar](images/147992353419_DV_resource.Stream@PNG-en-US.png) | Creates a new user-defined parameter list.   Can be invoked via the standard parameter list or a user-defined parameter list. |
| ![Toolbar](images/147992357387_DV_resource.Stream@PNG-en-US.png) | Opens a user-defined parameter list from any directory of the PG/PC. |
| ![Toolbar](images/147992410507_DV_resource.Stream@PNG-en-US.png) | Saves the parameters retentively (copy RAM to ROM). |
| ![Toolbar](images/147992414475_DV_resource.Stream@PNG-en-US.png) | Restores the factory settings. |
| ![Toolbar](images/147992456843_DV_resource.Stream@PNG-en-US.png) | Shows open BICO interconnections on all drive objects in the offline project. |
| ![Toolbar](images/147992460811_DV_resource.Stream@PNG-en-US.png) | Opens an exception list for the know-how protection of S120. |

### Inspector window

This section contains information on the following topics:

- [Settings, information and diagnostics](#settings-information-and-diagnostics)

#### Settings, information and diagnostics

The properties and parameters of a selected object are displayed in the inspector window. The properties and parameters can be edited. For example, new unspecified S120 drive objects inserted in the device view can be specified.

##### Structure

The information and parameters in the Inspector window are subdivided into various information types, which are displayed as main and secondary tabs in the Inspector window:

![Example: Inspector window for the infeed](images/147992519051_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary tab: In the example of the main tab "Properties" |
| ② | Main tab: Properties, Info, Diagnostics |

Example: Inspector window for the infeed

##### Subdivision of the "Properties" area

There are further subareas for each type of information that can be displayed via secondary tabs.

The most important type of information for SINAMICS S120 drives is the "Properties" area. The following secondary tabs are displayed in this area:

- General

  Display of the properties and settings of the drive device, drive object, or the hardware component. You can edit the settings and parameters here. The left pane of the inspector window contains the secondary navigation. Information and parameters are arranged there in groups. If you click the arrow symbol to the left of the group name, you can expand the group if subgroups are available. If you select a group or subgroup, the corresponding information and parameters are displayed in the right pane of the inspector window and can also be edited there.

  For S120 drives, the drive objects (e.g. an infeed) are mainly specified in this subarea.
- IO tags

  Displays the IO tags of the PLC. You can assign names for the tags, assign the tags to the user-defined tag tables via a drop-down list, and enter comments for the tags. The IO tags are also shown in the PLC tag table.
- System constants

  Displays the constants required by the system with the HW identifiers of the modules. The system constants are also shown in the PLC tag table.
- Texts

  Displays the reference language and specifies the text source for the project texts.

##### Subdivision of the "Info" area

The following secondary tabs are displayed in this area:

- General
- Cross references
- Compilation

##### Subdivision of the "Diagnostics" area

The following secondary tabs are displayed in this area:

- Device information
- Connection information
- Alarm display

##### Showing or enlarging the inspector window

There are several options available for showing (hiding) the inspector window:

1. Use the regular window icons (top right-hand side in the header of the window).

   - Or -
2. Select a non-specified component in the device view and open the "Properties" shortcut menu.

The inspector window is displayed only partially in Startdrive when called, due to lack of space. Display of the inspector window can be maximized (minimized) for specification of the components:

1. To do so, double-click the header of the inspector window (gray bar).

### Rotate & optimize screen forms

This section contains information on the following topics:

- [Control panel](#control-panel)
- [One Button Tuning (SERVO drive)](#one-button-tuning-servo-drive)

#### Control panel

> **Note**
>
> **Only reading rights?**
>
> If the project protection is activated, the function rights "Edit hardware configuration" and "Edit software configuration" are required for active access.
>
> Users without these function rights only have reading access.

The control panel is used for the control and monitoring of individual drives. You traverse drives with the control panel by specifying values. Depending on the operating mode, these are, for example, speed setpoints.

The following figure shows the various components of the control panel. The appearance of the control panel can vary depending on the set operating mode.

![Example: S120 control panel with speed setpoint specification as operating mode](images/168661173387_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Control drive (depending on the selected operating mode) |
| ③ | Drive status |
| ④ | Drive OFF |
| ⑤ | Set/reset drive enable |
| ⑥ | Actual values |

Example: S120 control panel with speed setpoint specification as operating mode

---

**See also**

[Using the control panel](Configuring%20SINAMICS%20S-G-MV%20drives.md#using-the-control-panel)

#### One Button Tuning (SERVO drive)

One Button Tuning serves to establish the optimum control parameters of a SERVO drive.

The following figure shows the various components of the "One Button Tuning" screen form:

![Startdrive S120: One Button Tuning](images/168673532171_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate/deactivate master control |
| ② | Dynamic response settings via defined stages or via a dynamic response factor (only for CU320-2) |
| ③ | Result of tuning. Comparison of values before and after tuning. |
| ④ | Start/stop optimization for One Button Tuning |
| ⑤ | Configuration/distance limit |
| ⑥ | Status of One Button Tuning |
| ⑦ | Advanced settings for selected parameters |

Startdrive S120: One Button Tuning

### Icons for arithmetic and controller functions

Icons for arithmetic and controller functions, not used in a standard Windows operation, are used in the Startdrive screen forms. They will therefore be explained briefly at this point.

| Icon | Explanation | Icon | Explanation |
| --- | --- | --- | --- |
| ![Figure](images/147853723915_DV_resource.Stream@PNG-en-US.png) | **NOT element**   Logical inversion (negation) | ![Figure](images/147992604683_DV_resource.Stream@PNG-en-US.png) | **Threshold switch 1/0**   Outputs a logical "1" at output y if x < S. |
| ![Figure](images/147992608779_DV_resource.Stream@PNG-en-US.png) | **AND element**   With logical subdivision of an input | ![Figure](images/147992612747_DV_resource.Stream@PNG-en-US.png) | **Threshold switch 0/1**   Outputs a logical "1" at output y if x > S. |
| ![Figure](images/147992616843_DV_resource.Stream@PNG-en-US.png) | **R/S flip-flop**   S/R = Set input/Reset input   Q = Non-inverted output   Q = Inverted output  In the case of a simultaneous 1 signal at the R input and S input, the S input is dominant. | ![Figure](images/147992620811_DV_resource.Stream@PNG-en-US.png) | **Threshold switch 1/0 with hysteresis**   Outputs a logical "1" at output y if x < S. If x >= S + H, y returns to 0. |
| ![Figure](images/147992637707_DV_resource.Stream@PNG-en-US.png) | **Exclusive OR/XOR**   y = 1 if x1 = x2. | ![Figure](images/147992641675_DV_resource.Stream@PNG-en-US.png) | **Threshold switch 0/1 with hysteresis**   Outputs a logical "1" at output y if x > S. If x <= S - H, y returns to 0. |
| ![Figure](images/147992645771_DV_resource.Stream@PNG-en-US.png) | **Comparator**   y = 1 if x1 = x2. | ![Figure](images/147992662667_DV_resource.Stream@PNG-en-US.png) | **Limiter**   x is limited to the upper limit value LU and the lower limit value LL and is output at output y.   The binary signals MLU and MLL have the value "1" if upper or lower limiting is active. |
| ![Figure](images/147992666763_DV_resource.Stream@PNG-en-US.png) | **Sign reversal**   y = -x | ![Figure](images/147992670731_DV_resource.Stream@PNG-en-US.png) | **Sample & hold element**   Sample and hold element. y = x if SET = 1  (no retentive memory during POWER OFF) |
| ![Figure](images/147853746827_DV_resource.Stream@PNG-en-US.png) | **Absolute-value generator**   y = |x| | ![Figure](images/147992687627_DV_resource.Stream@PNG-en-US.png) | **Monitoring**   Positioning in sheet at bottom right. |
| ![Figure](images/147992691723_DV_resource.Stream@PNG-en-US.png) | **Divider**   Y = X<sub>1</sub>/X<sub>2</sub> | ![Figure](images/147992695691_DV_resource.Stream@PNG-en-US.png) | **Simple change-over switch**   The switch position as per the factory setting of --- is displayed (in this case, switch position 1). |
| ![Figure](images/147992712459_DV_resource.Stream@PNG-en-US.png) | **Multiplier**   y = x1 · x2 |  |  |
| ![Figure](images/147992716427_DV_resource.Stream@PNG-en-US.png) | **Comparator greater than 0**   y = 1 if analog signal x > 0, i.e. if it is positive. |  |  |
| ![Figure](images/147992720523_DV_resource.Stream@PNG-en-US.png) | **Differentiator**   Y = dx/dt |  |  |

## Fundamentals

This section contains information on the following topics:

- [Permanently save the settings](#permanently-save-the-settings)
- [Restoring factory settings](#restoring-factory-settings)
- [Loading project data from a drive](#loading-project-data-from-a-drive)
- [Loading the project data to the drive unit](#loading-the-project-data-to-the-drive-unit)
- [Activating/deactivating drive components](#activatingdeactivating-drive-components)
- [Uniquely identify drive components](#uniquely-identify-drive-components)
- [Updating the firmware](#updating-the-firmware)
- [Checking the firmware](#checking-the-firmware)
- [Using parameter lists](#using-parameter-lists)
- [Editing BICO interconnections](#editing-bico-interconnections)
- [Filters](#filters)
- [Licensing](#licensing)
- [SINAMICS rules in Startdrive](#sinamics-rules-in-startdrive)

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

1. Establish an [online connection](#establishing-an-online-connection-to-the-plc) to your drive.
2. Load the project data into your drives.
3. Click the ![Saving offline data in non-volatile storage](images/147992784395_DV_resource.Stream@PNG-en-US.png) icon in the function view of the active Startdrive project.

   The current project settings are stored non-volatile on the memory card of the drive.

### Restoring factory settings

#### Requirement

- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Procedure

In the online mode, you can restore the factory settings for the drive control.

1. Establish an [online connection](#establishing-an-online-connection-to-the-plc) to your drive unit.
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

     Detailed information about going online can be found at "[Establishing an online connection to the PLC](#establishing-an-online-connection-to-the-plc)".
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

### Activating/deactivating drive components

#### Description

Configure the drive line-up that consists of a Control Unit and various drive objects/components in the device view (DRIVE-CLiQ editor). All components are usually activated in this drive line-up. However, you can also deactivate individual components of the drive line-up or reactivate them later using the following statuses:

- Deactivate drive object/component

  Deactivates a selected component in the device view temporarily, for example, when replacing a component.
- Activate drive object/component

  Activates a briefly deactivated component in the device view.
- Deactivate drive object/component and not available

  Deactivates individual components that are actually missing in the hardware in the device view of a very large drive line-up. This allows for maximum configuration of a drive project. Deactivated components in the drive project can also be missing in the hardware without any errors being generated because of it. Possible applications are, for example, the test of parts of a large plant or the commissioning of components when replacement parts are used.

**Drive objects/components that can be deactivated:**

The table below shows which drive objects/components can be deactivated:

| Drive object/status | ... deactivate | ... deactivate and not available |
| --- | --- | --- |
| Control Unit | X | ‑ |
| Line Module | X | X |
| Power module | X | X |
| Motor Module | X | X |
| Motor | ‑ | ‑ |
| Measuring systems/encoders | ‑ | ‑ |
| Encoder evaluation | X | X |
| CUA Control Unit Adapter | X | X |
| DRIVE CLiQ Hub Module DMC20/DME20 | X | X |
| CBE 20 Communication Board | ‑ | ‑ |
| TB30 Terminal Board | ‑ | ‑ |
| Terminal Modules | ‑ | ‑ |
| Voltage Sensing Modules | X | X |

#### Deactivate

1. Select the drive object (component) that you want to deactivate in the device view.
2. Open the Inspector window of the selected drive object, and the "General" menu in the secondary navigation.
3. Select one of the two options in the "Component activation" or "Drive object activation" drop-down list:

   - ... deactivated
   - ... deactivated and not available
4. Then save the project.

#### Activate

1. In the device view, select the drive object (component) that you want to activate.
2. Open the Inspector window of the selected drive object, and the "General" menu in the secondary navigation.
3. Select the "Activate ..." option in the "Component activation" or "Drive object activation" drop-down list.
4. Then save the project.

### Uniquely identify drive components

#### Description

Each version of any Startdrive component has a unique number, which is known as the TypeIdentifier . In Startdrive, the TypeIdentifier can be optionally displayed and in the default setting, is deactivated.

Benefits of a TypeIdentifier:

- The Control Unit or other components of a drive unit can be uniquely identified.
- The TypeIdentifier can be used in custom programs that are to execute Startdrive functions (e.g. with Startdrive Openness) in which program codes are used.

#### Activating the display of the TypeIdentifier in Startdrive

1. In the Startdrive project view, select menu "Options > Settings".

   The "Settings" configuration area opens.
2. In the secondary navigation, select entry "Hardware configuration".
3. Activate option "Activate display of the TypeIdentifier for devices and modules".

   The TypeIdentifier display is now active. When creating a new device, the TypeIdentifier of the Control Unit is also displayed to provide additional information. For all of the components used in the Startdrive project, an additional table column can be inserted in the Inspector window. For each specified component, this then shows the corresponding TypeIdentifier.

#### Reading out the TypeIdentifier of the Control Unit

To read out the TypeIdentifier of a Control Unit, proceed as follows:

1. Double-click in the Startdrive project tree on "Add new device".

   The dialog with the same name opens.
2. Select the required Control Unit from the selection list.

   The TypeIdentifier for the corresponding Control Unit is displayed to the right in the detailed view (below the Article number and firmware number).   
   Example: `OrderNumber:6SL3040-1MA01-0Axx/V5.2/S120`

#### Reading out the TypeIdentifier via the Inspector window

Proceed as follows to read out the TypeIdentifier for a component (not a Control Unit) in the Inspector window:

1. In the device view of the Startdrive project, double-click on the required component.

   The Inspector window opens. The active version of the component is displayed in the list.
2. The associated TypeIdentifier is listed in the outer right-hand column.   
   Example: `OrderNumber:6SL3131-7TE23-6Axx`

### Updating the firmware

#### Description

The firmware for the drive system is distributed in the system. It is located on the Control Unit and in each individual DRIVE-CLiQ component.

A firmware update is required if you want to use a new firmware version with an extended range of functions.

You can find the firmware versions available for SIMATIC Drive Controllers on this [website](https://support.industry.siemens.com/cs/ww/en/view/109773914):

> **Note**
>
> **Is the firmware version the same in the drive and Startdrive?**
>
> ONLINE connections between a Startdrive project and a drive are only possible when both communication partners have the same firmware version (see "[Checking the firmware](#checking-the-firmware)").
>
> - If your current Startdrive project is working with an older firmware version than the drive, create a new project.
> - Set the firmware version of the Startdrive project to the latest updated version of the drive and apply all other settings from the old project.   
>   If you are still using an old Startdrive version, it may be necessary to install a new Startdrive version that supports the firmware version.

> **Note**
>
> **Saving web server data**
>
> The web server settings saved on the memory card are overwritten and therefore lost when the memory card is overwritten with the new firmware. To prevent this from happening, back up the data and upload it to the memory card again after upgrading the firmware.

#### Requirement

- PG/PC is connected to the drive unit via LAN (physically ONLINE).

#### Updating the memory card

| 1. Back up the configuration data from the "\OEM\SINAMICS\HMI\" directory of the memory card prior to the firmware update. 2. Disconnect your Control Unit. 3. Remove the memory card with the old firmware version. 4. Overwrite the memory card with the new firmware version. 5. Use the backed-up data from the memory card with the old firmware to overwrite the following directory on the current memory card: \OEM\SINAMICS\HMI\. 6. Insert the memory card with the new firmware version. 7. Turn your Control Unit on again.     The drive now starts with a self-configuration and downloads the firmware data from the memory card to the Control Unit.        | RDY | COM | Explanation of LED displays |    | --- | --- | --- |    | ![Updating the memory card](images/147993054859_DV_resource.Stream@PNG-en-US.png) | ![Updating the memory card](images/147993058955_DV_resource.Stream@PNG-en-US.png) | Firmware update is active - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |    | ![Updating the memory card](images/147993063051_DV_resource.Stream@PNG-en-US.png) | ![Updating the memory card](images/147993063051_DV_resource.Stream@PNG-en-US.png) | Synchronous flashing of LEDs (1 Hz): Converter is waiting for the power supply to be disconnected and reconnected after the firmware update. |     Wait until the Control Unit has completed the transfer of the new firmware. 8. Next, download the current Startdrive project data to the drive unit (see "[Loading the project data to the drive unit](#loading-the-project-data-to-the-drive-unit)"). 9. Turn the drive off and on again.     The firmware of the connected DRIVE-CLiQ components is updated. A restart may be required to complete the update (see Startdrive alarm messages).       | RDY | Explanation of LED displays |  |    | --- | --- | --- |    | ![Updating the memory card](images/147993058955_DV_resource.Stream@PNG-en-US.png)  (0.5 Hz) | Firmware update of the connected DRIVE-CLiQ components in progress. - Do not disconnect the power supply. - Do not separate the motor from the frequency converter. |  |    | ![Updating the memory card](images/147993067147_DV_resource.Stream@PNG-en-US.png)  (2 Hz) | Firmware update of the DRIVE-CLiQ components is complete. Waiting for POWER ON of the respective component.  **Remedy**: Turn the component off and on again. |  | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Checking the firmware

An online connection between the PG/PC and drive unit is only possible when the PG/PC and drive unit are using the same firmware version.

Different firmware versions frequently occur in the following cases:

- A firmware update was performed for the drive unit. However, the firmware saved in the Startdrive project is older.
- A new Startdrive version was installed. The latest firmware version was automatically set when you created a new project. However, your drive unit still uses an older version.

#### Checking firmware consistency:

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

#### Result:

An online connection is possible if the firmware versions are identical (see the example screens above).

If the firmware versions are not identical, then the versions must be aligned in order to establish an online connection. You usually upgrade the older version.

#### Workaround:

- Update the firmware of your drive unit.

  - OR -
- Create a new Startdrive project for your drive unit in Startdrive and set a newer firmware version for the Control Unit in the new project.

  If you are using an older Startdrive version, it may be necessary to install a more recent Startdrive version beforehand.

### Using parameter lists

This section contains information on the following topics:

- [Editing the parameter list](#editing-the-parameter-list)
- [Searching for parameters](#searching-for-parameters)
- [Comparing parameters](#comparing-parameters)
- [Using user-defined parameter lists](#using-user-defined-parameter-lists)

#### Editing the parameter list

##### Working with the parameter list

The parameter list provides the following functions:

- Monitoring and editing parameter values
- Restricting the parameter view
- Exporting the parameters as CSV

For information on the user interface, see also [Parameter view](Configuring%20SINAMICS%20S-G-MV%20drives.md#parameter-view-1).

##### Monitoring and editing parameter values online

The input fields of the parameters that you can change online are displayed in orange after you have established an online connection with Startdrive.

To change the parameters online, follow these steps:

1. Establish an [online connection](Configuring%20SINAMICS%20S-G-MV%20drives.md#establishing-an-online-connection-to-the-drive).

   The display of the parameters changes to "orange".
2. Change the parameter values or settings, if required.
3. Press the enter key to apply the changes.

   The settings then take immediate effect in the drive.

##### Switching the parameter view

The parameter list provides the following views in Startdrive:

- "Display standard parameters":

  Default: This view displays the most important and typical parameters of the drive.
- "Display extended parameters":

  This view contains parameters that are required by experts for extended settings.
- "Display service parameters":

  This view contains parameters that are required by service employees.

##### Exporting the parameters to CSV file

CSV files can be opened in spreadsheet programs or editors.

To export the parameter list as a CSV file, proceed as follows:

1. Click on the arrow to the right of the ![Exporting the parameters to CSV file](images/147992406539_DV_resource.Stream@PNG-en-US.png) icon (copy offline parameters to a CSV file).

   A menu selection opens. You can choose whether you only want to export the displayed parameters or the parameters of all drive objects to a CSV file.
2. Select the required export function.

   The Export window opens.
3. Select a storage location in your directory tree, assign a name for the CSV file and click "Save".

   The parameter list is saved as a CSV file.

#### Searching for parameters

Use the standard search function of the TIA Portal for the specific search of parameters for SINAMICS S drives.

##### Using the standard search of the TIA Portal

The standard search is displayed in the "Tasks" viewlet in the right-hand editor of the program user interface.

1. To skip the search dialog, enter <Ctrl+F> via the keyboard with activated parameter view.

   ![Searching for parameters](images/147993145611_DV_resource.Stream@PNG-en-US.PNG)

   ![Searching for parameters](images/147993145611_DV_resource.Stream@PNG-en-US.PNG)

   Searching for parameters
2. In the "Search" field, enter either the parameter number or a parameter text for which you wish to search.
3. To start the search, press the <Return> key or click on "Search".

   If the parameter or text is found, the cursor jumps automatically to the position in the parameter list.
4. Press <F3> to jump to the next search result.

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

### Editing BICO interconnections

This section contains information on the following topics:

- [Binectors, Connectors](#binectors-connectors)
- [Interconnecting BICO outputs](#interconnecting-bico-outputs)
- [Interconnect BICO inputs](#interconnect-bico-inputs)

#### Binectors, Connectors

##### Description

Each drive unit contains a large number of interconnectable input and output variables and internal control variables.

BICO technology (Binector Connector technology) allows the drive unit to be adapted to a wide variety of requirements.

These parameters are identified accordingly in the parameter list or in the function diagrams.

In Startdrive, the parameterization is possible via:

- Function view
- Parameter view

##### Binectors, BI: Binector input, BO: Binector output

A binector is a unitless digital (binary) signal that can assume a value of 0 or 1.

Binectors are subdivided into binector inputs (BI) and binector outputs (BO).

**Binectors**

|  |  |  |  |
| --- | --- | --- | --- |
| **Abbreviation** | **Icon** | **Name** | **Description** |
| BI | ![Binectors, BI: Binector input, BO: Binector output](images/147993575307_DV_resource.Stream@PNG-en-US.png) | Binector Input (signal sink) | Can be interconnected with a binector output as source. |
| BO | ![Binectors, BI: Binector input, BO: Binector output](images/147993541771_DV_resource.Stream@PNG-en-US.png) | Binector Output (signal source) | Can be used as a source for a binector input. |

##### Connectors, CI: Connector input, CO: Connector output

A connector is a digital signal, e.g. in the 32-bit format. It can be used to emulate words (16 bits), double words (32 bits), or analog signals.

Connectors are subdivided into connector inputs (CI) and connector outputs (CO).

**Connectors**

|  |  |  |  |
| --- | --- | --- | --- |
| **Abbreviation** | **Icon** | **Name** | **Description** |
| CI | ![Connectors, CI: Connector input, CO: Connector output](images/147993571339_DV_resource.Stream@PNG-en-US.png) | Connector Input (signal sink) | Can be interconnected with a connector output as source. |
| CO | ![Connectors, CI: Connector input, CO: Connector output](images/147993579275_DV_resource.Stream@PNG-en-US.png) | Connector Output (signal source) | Can be used as a source for a connector input. |

##### Multiple BICO interconnections

The ![Multiple BICO interconnections](images/147993596043_DV_resource.Stream@PNG-en-US.png) icon has several meanings:

- Icon in the toolbar:

  Determines all open BICO interconnections in the drive objects of the project.
- Icon next to the interconnection:

  Opens an interconnection dialog in which you can create a bit by bit interconnection (multiple interconnections).

##### Propagation of faults

In the event of faults which are triggered by the Control Unit or a Terminal Module, for example, central functions of the drive are often also affected. Propagation is therefore used to forward faults triggered by one drive object to other drive objects. This behavior also applies to the faults that are set in a DCC chart on the Control Unit using a DCC block.

The following types of propagation are available:

- BICO

  The fault is forwarded to all active drive objects with control functions (infeed, drive) for which a BICO interconnection exists.
- DRIVE

  The fault is forwarded to all active drive objects with closed-loop control functions.
- GLOBAL

  The fault is forwarded to all active drive objects.
- LOCAL

  The behavior of this propagation type depends on parameter p3116:

  - With binector input p3116 = 0 signal (factory setting):

    The fault is forwarded to the first active drive object with closed-loop control functions.
  - With binector input p3116 = 1 signal:

    The fault is not forwarded.

##### Notes on BICO technology

**BICO interconnections to other drives**

The following parameters are available for BICO interconnections to other drives:

- r9490 Number of BICO interconnections to other drives
- r9491[0...9] BI/CI of BICO interconnections to other drives
- r9492 [0...9] BO/CO of BICO interconnections to other drives
- p9493[0...9] Reset BICO interconnections to other drives

**Copying drives**

When a drive is copied, the interconnection is copied with it.

**Binector-connector-converter**

- Several digital signals are converted into a 32-bit integer double word or into a 16-bit integer word.
- p2080[0...15] BI: PROFIdrive PZD send bit-by-bit

**Connector-binector converter**

- A 32-bit integer double word or a 16-bit integer word is converted to individual digital signals.
- p2099[0...1] CI: PROFIdrive PZD selection receive bit-by-bit

**Fixed values for interconnection via BICO technology**

The following connector outputs are available for interconnecting any fixed value settings:

- p2900[0...n] CO: Fixed value_%_1
- p2901[0...n] CO: Fixed value_%_2
- p2930[0...n] CO: Fixed value_M_1

#### Interconnecting BICO outputs

Use the connection dialog to connect binector or connector outputs.

##### Connecting a signal

To make a connection, proceed as follows:

1. Click the binector or connector icon of the signal that you want to connect (![Connecting a signal](images/147993541771_DV_resource.Stream@PNG-en-US.png) or ![Connecting a signal](images/147993579275_DV_resource.Stream@PNG-en-US.png)).

   A connection dialog for the selection of the possible parameters opens. The drive object for which you want to make an interconnection is displayed automatically in the "Drive object" drop-down list on the right.

   ![Example dialog](images/147993639563_DV_resource.Stream@PNG-en-US.png)

   ![Example dialog](images/147993639563_DV_resource.Stream@PNG-en-US.png)

   Example dialog

   The last set signal sink is displayed in the "Selected sinks" field. If a connection was not available previously, the text "No sink selected" is displayed.
2. Activate the check boxes for the parameters that you want to connect.

   If connectable bits of the parameter are available, they are displayed in a drop-down list.

   ![Example dialog: Parameter bits opened](images/147993643531_DV_resource.Stream@PNG-en-US.png)

   ![Example dialog: Parameter bits opened](images/147993643531_DV_resource.Stream@PNG-en-US.png)

   Example dialog: Parameter bits opened
3. Activate the check boxes for the parameter bits that you want to connect.
4. Confirm with OK.

   The connection dialog closes.

**Result**

The binector or connector output is connected to the selected parameter (bit).

##### Multiple connections at outputs

Several interconnections can be set simultaneously for a parameter, which for reasons of space however, cannot be displayed in the interconnections field. Clicking the symbol ![Multiple connections at outputs](images/147993635595_DV_resource.Stream@PNG-en-US.PNG) next to the interconnection field opens a list, which shows all of the active parameter interconnections.

#### Interconnect BICO inputs

Use a connection dialog to connect binector or connector inputs.

##### Connecting a signal

To make a connection, proceed as follows:

1. Click the binector or connector icon of the signal that you want to connect (![Connecting a signal](images/147993575307_DV_resource.Stream@PNG-en-US.png) or ![Connecting a signal](images/147993571339_DV_resource.Stream@PNG-en-US.png)).

   A connection dialog for the selection of the possible parameters opens. The drive object for which you want to make a connection is displayed automatically in the "Drive object" drop-down list on the right.

   ![BICO interconnection dialog](images/147993707659_DV_resource.Stream@PNG-en-US.png)

   ![BICO interconnection dialog](images/147993707659_DV_resource.Stream@PNG-en-US.png)

   BICO interconnection dialog

   The last set signal source is displayed in the "Selected source" field. If a connection was not available previously, the value 0 is displayed.
2. Select the parameter that you want to connect.

   If connectable bits of the parameter are available, they are displayed in a drop-down list.

   ![BICO dialog: Parameter bits opened](images/147993712011_DV_resource.Stream@PNG-en-US.png)

   ![BICO dialog: Parameter bits opened](images/147993712011_DV_resource.Stream@PNG-en-US.png)

   BICO dialog: Parameter bits opened
3. Select the parameter bit that you want to connect.
4. Confirm with OK.

   The connection dialog closes.

**Result**

The binector or connector input is connected to the selected parameter (bit).

### Filters

This section contains information on the following topics:

- [Overview](#overview-1)
- [Using the PT1 filter](#using-the-pt1-filter)
- [Using a PT2 filter](#using-a-pt2-filter)
- [Using a bandstop filter](#using-a-bandstop-filter)
- [Using a low-pass filter with reduction](#using-a-low-pass-filter-with-reduction)
- [Using a general 2nd order filter](#using-a-general-2nd-order-filter)

#### Overview

##### Filters available for processing signals

In Startdrive, various filters are available for SINAMICS drives for filtering signals.

- [PT1 filter](#using-the-pt1-filter); first-order low-pass filter
- [PT2 filter](#using-a-pt2-filter); second-order low-pass filter
- [General 2nd order filter](#using-a-general-2nd-order-filter)
- [Low-pass filter with defined reduction](#using-a-low-pass-filter-with-reduction)
- [Bandstop filter](#using-a-bandstop-filter) with different notch depth or reduction

The filters are used in different sections of the controlled system.

- Speed setpoint filter
- Current setpoint filter
- Speed actual value filter
- Precontrol balancing

#### Using the PT1 filter

##### Setting a time constant

The PT1 filter is a first-order low-pass filter. Use this filter to suppress disturbing signals, for example, to dampen resonance or noise.

Besides amplitude damping, the filter also produces a phase shift, which reduces the phase margin in the control loop. In this way, the maximum possible bandwidth of the speed controller is reduced.

The transfer function is expressed as follows:

![Transfer function PT1](images/147993818379_DV_resource.Stream@PNG-en-US.png)

Transfer function PT1

where s = jω = j*2πf

The PT1 filter has the following features:

- Damping after the characteristic frequency is -20 dB/decade (factor 1/10) (see amplitude response).
- Phase shift at the characteristic frequency is -45° (see phase response).

![Bode diagram PT1](images/147993809419_DV_resource.Stream@PNG-en-US.png)

Bode diagram PT1

You set the time constant (smoothing time) in Startdrive. The following diagram shows the step response of a PT1 system with time constant T<sub>1</sub>.

![PT1 without dead time](images/147993814283_DV_resource.Stream@PNG-en-US.png)

PT1 without dead time

The greater time constant T<sub>1</sub> that you select, the lower the characteristic frequency. This means that the amplitude damping and the phase shift engage at the lower frequencies and the delay time increases accordingly.

#### Using a PT2 filter

##### PT2 filter

The PT2 filter is a second-order filter, which is used here as a low-pass filter. The transfer function is expressed as follows:

![Transfer function PT2](images/147993887499_DV_resource.Stream@PNG-en-US.png)

Transfer function PT2

where s = jω = j*2πf

The PT2 filter has the following features:

- Phase shift at the characteristic frequency is -90°.
- Damping after the characteristic frequency is -20 dB/decade.

In Startdrive, the following parameters are required for the filter.

- Denominator damping D<sub>N</sub>; damping constant that can be used to influence the amplitude/phase response.
- Denominator natural frequency f<sub>N</sub> or characteristic frequency

Because Startdrive V14 does not yet provide a calculation of the filters and representation of the amplitude and phase responses, the examples can offer a rough guide for the filter parameterization.

##### Amplitude and phase response with the standard settings

Example of a PT2 filter

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Characteristic frequency f<sub>N</sub> 2000 Hz Damping D<sub>N</sub> 0.7 | ![Amplitude and phase response with the standard settings](images/147993867531_DV_resource.Stream@PNG-en-US.png) | ![Amplitude and phase response with the standard settings](images/147993877515_DV_resource.Stream@PNG-en-US.png) |

#### Using a bandstop filter

##### Bandstop filter

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

  ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/147993967371_DV_resource.Stream@PNG-en-US.png)

Example of bandstop filter with infinite notch depth

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>Sp</sub> = 500 Hz Bandwidth (-3 dB) f<sub>BB</sub> = 500 Hz Notch depth K = -∞ dB Reduction Abs = 0 dB | ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/147993934475_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with infinite notch depth](images/147993944587_DV_resource.Stream@PNG-en-US.png) |

##### Amplitude response and phase response for bandstop filter with defined notch depth

Simplified conversion to parameters for general-order filters:

- No reduction or increase after the blocking frequency
- Defined notch at the blocking frequency K[dB] (e.g. -20 dB)
- Numerator natural frequency f<sub>Z</sub> = f<sub>Sp</sub>
- Numerator damping:

  ![Amplitude response and phase response for bandstop filter with defined notch depth](images/147994160523_DV_resource.Stream@PNG-en-US.png)
- Denominator natural frequency f<sub>N</sub> = f<sub>Sp</sub>
- Denominator damping:

  ![Amplitude response and phase response for bandstop filter with defined notch depth](images/147994170635_DV_resource.Stream@PNG-en-US.png)

Example of bandstop filter with defined notch depth

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>Sp</sub> = 500 Hz Bandwidth f<sub>BB</sub> = 500 Hz Notch depth K = -20 dB Reduction Abs = 0 dB | ![Amplitude response and phase response for bandstop filter with defined notch depth](images/147993977483_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with defined notch depth](images/147993987595_DV_resource.Stream@PNG-en-US.png) |

##### Amplitude response and phase response for bandstop filter with defined reduction

General conversion to parameters for general-order filters:

- Numerator natural frequency:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994107275_DV_resource.Stream@PNG-en-US.png)
- Numerator damping:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994117387_DV_resource.Stream@PNG-en-US.png)
- Denominator natural frequency:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994140299_DV_resource.Stream@PNG-en-US.png)
- Denominator damping:

  ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994150411_DV_resource.Stream@PNG-en-US.png)

Example of bandstop filter with defined reduction

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Blocking frequency f<sub>SP</sub> = 500 Hz Bandwidth f<sub>BB</sub> = 500 Hz Notch depth K = -∞ dB Reduction ABS = -10 dB | ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994035979_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response for bandstop filter with defined reduction](images/147994084491_DV_resource.Stream@PNG-en-US.png) |

#### Using a low-pass filter with reduction

##### General low-pass filter with reduction

Low-pass filters allow frequencies below a limit frequency to pass without weakening and only dampen the higher frequencies. With a low-pass filter with reduction, the amplitude response at high frequencies is reduced by a defined amount.

Conversion to parameters for general-order filters:

- Numerator natural frequency f<sub>Z</sub> = f<sub>Abs</sub> (start of reduction)
- Numerator damping:

  ![General low-pass filter with reduction](images/147994262155_DV_resource.Stream@PNG-en-US.png)
- Denominator natural frequency f<sub>N</sub>
- Denominator damping D<sub>N</sub>

##### Amplitude response and phase response in the standard settings

Example of low-pass filter with reduction

| Filter parameter | Amplitude response | Phase response |
| --- | --- | --- |
| Characteristic frequency f<sub>Abs</sub> = 500 Hz Damping D = 0.7 Reduction Abs = -10 dB | ![Amplitude response and phase response in the standard settings](images/147994229259_DV_resource.Stream@PNG-en-US.png) | ![Amplitude response and phase response in the standard settings](images/147994252171_DV_resource.Stream@PNG-en-US.png) |

#### Using a general 2nd order filter

##### General second-order filter

The following formula shows the transfer function for a general second-order filter. You can also parameterize band-stop filters (notch filters) with this filter.

![Transfer function general second-order filter](images/147994308619_DV_resource.Stream@PNG-en-US.png)

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
| ![General second-order filter](images/147994312587_DV_resource.Stream@PNG-en-US.png) | ![General second-order filter](images/147994316555_DV_resource.Stream@PNG-en-US.png) | ![General second-order filter](images/147994320523_DV_resource.Stream@PNG-en-US.png) |
| Low pass PT2 | Bandstop | General second-order filter |
| Characteristic frequency PT2: 1999.0 Hz | Blocking frequency: 800.0 Hz | Numerator frequency: 800.0 Hz |
| Damping: 0.700 | Bandwidth: 1000.0 | Numerator damping 0.0 |
|  | Notch depth: -∞ | Denominator frequency 800.0 Hz |
|  | Reduction: 0.00 | Denominator damping; 0.625 |

### Licensing

This section contains information on the following topics:

- [Overview](#overview-2)
- [Licensing SINAMICS Integrated](#licensing-sinamics-integrated)

#### Overview

##### Licenses for the SINAMICS Integrated and S120 Control Units

Certain functionalities require licensing in the SINAMICS S120 drive system. The licensing procedure for SINAMICS Integrated differs from the licensing procedure for SINAMICS S120 Control Units.

In a process similar to that for runtime licenses for the CPU, SINAMICS Integrated is licensed via Engineering by confirming the purchase of the licenses. SINAMICS S120 Control Units, on the other hand, are licensed using the memory card. The memory card is generally ordered pre-licensed for this purpose.

In the order, specify the type and number of licenses you require in additional information (Z options). Alternatively, you can also license the memory card with single licenses.

The single licenses are available in two variants:

- CoL as hard copy
- CoL as a file

| Licenses for functions/Technology Extensions (TEC) | Licensing | Article number of the single license to be purchased for the SINAMICS Integrated or for SINAMICS S120 Control Units | Z option for pre-licensing CF cards with SINAMICS S120 control units |
| --- | --- | --- | --- |
| Safety Integrated Extended   Functions | Per axis  max. 12 | CoL as hard copy 6SL3074-0AA10-0AA0  CoL as a file 6SL3074-0AA10-0AH0 | Fxx (xx = number of licenses) |
| Safety Integrated Advanced   Functions | Per axis  max. 12 | CoL as hard copy 6SL3074-0AA20-0AA0  CoL as a file 6SL3074-0AA20-0AH0 | Axx (xx = number of licenses) |
| Detent torque compensation | Per axis | CoL as hard copy 6SL3074-0AA15-0AA0   CoL as a file 6SL3074-0AA15-0AH0 | Z option: - |
| Advanced Position Control (APC) | Per axis | CoL as hard copy 6SL3074-0AA05-0AA0   CoL as a file 6SL3074-0AA05-0AH0 | Z option: - |
| Dynamic network support | Per SINAMICS /CU  Integrated/CU | CoL as hard copy 6SL3074-0AA07-0AA0  CoL as a file 6SL3074-0AA07-1AH0  (Booksize)  6SL3074-0AA07-0AH0   (Chassis) | S01 |
| Line droop control | Per SINAMICS /CU  Integrated/CU | CoL as hard copy 6SL3074-0AA08-0AA0  CoL as a file   6SL3074-0AA08-0AH0   (up to 2000 kW)   6SL3074-0AA08-1AH0   (up to 1600 kW)   6SL3074-0AA08-2AH0   (up to 1250 kW)   6SL3074-0AA08-3AH0   (up to 950 kW)   6SL3074-0AA08-4AH0   (up to 650 kW)   6SL3074-0AA08-5AH0   (up to 350 kW)   6SL3074-0AA08-6AH0   (up to 200 kW)   6SL3074-0AA08-7AH0   (up to 100 kW)   6SL3074-0AA08-8AH0   (up to 50 kW) | S02 |
| Advanced Synchronous   Reluctance Control | Per axis | CoL as hard copy 6SL3074-0AA06-0AA0  CoL as a file 6SL3074-0AA06-0AH0 | Z option: - |
| Controller Parameter Adaption | Per axis | CoL as hard copy  CoL as a file 6SL3074-0AA17-0AH0 | Z option: - |
| Technology Extension VIBX   (Vibration Extinction) | Per SINAMICS /CU  Integrated/CU | CoL as hard copy 6SL3077-0AA00-5AB0  CoL as a file 6SL3077-0AA00-5AH0 | U03 |
| Technology Extension SERVCOUP   (Servo Coupling) | Per SINAMICS /CU  Integrated/CU | CoL as hard copy 6SL3077-0AA00-8AB0  CoL as a file 6SL3077-0AA00-8AH0 | Z option: - |
| DCB Extension Library | Per SINAMICS /CU  Integrated/CU | CoL as hard copy 6SL3077-0AA00-0AB0  CoL as a file 6SL3077-0AA00-0AH0 | U01 |
| SINAMICS Integrated only supports the licensed functions and Technology Extensions (TEC) listed.   Additional licensed functions and Technology Extensions (TEC) are available for SINAMICS S120 Control Units. |  |  |  |

> **Note**
>
> The SINAMICS Technology Extension licenses are only displayed when the corresponding Technology Extension was installed in Startdrive.

> **Note**
>
> Licenses must be purchased to use the functions in question. For details, see the licensing terms for the given product.
>
> If the SINAMICS Integrated is sub-licensed, this is indicated in the project tree and in the Startdrive working area.
>
> The number of licenses purchased is saved in the project. There is no sub-licensing response at the drive end.

> **Note**
>
> SINAMICS S120 CU320-2 connected to the SIMATIC Drive Controller are licensed with the CF card of CU320-2. With sub-licensing, there is a sub-licensing response on the CU320-2.

##### Additional parameters

- [p9918](SINAMICS%20Parameter%20CU.md#p9918-licensing-active-trial-license)
- [p9919](SINAMICS%20Parameter%20CU.md#r991903-licensing-trial-license-status)
- [p9920](SINAMICS%20Parameter%20CU.md#p9920099-licensing-enter-license-key)
- [p9921](SINAMICS%20Parameter%20CU.md#p9921-licensing-activate-license-key)

---

#### Licensing SINAMICS Integrated

Licenses must be purchased to use the respective functions. For details, refer to the license conditions for the product in question.

If the SINAMICS Integrated is under-licensed, this is indicated in the project tree and in the Startdrive work area.

| Icon | Where? | Explanation |
| --- | --- | --- |
| ![Figure](images/148040455563_DV_resource.Stream@PNG-en-US.PNG) | Project tree | Shows need for corrections in the license settings.   This symbol is also displayed in the "Info" tab of the Inspector window. |
| ![Figure](images/148040444427_DV_resource.Stream@PNG-en-US.png) | Function view | Function does not require a license. |
| ![Figure](images/148040448395_DV_resource.Stream@PNG-en-US.png) | Function view | Function is under-licensed. Needs at least one more license. |
| ![Figure](images/148040451979_DV_resource.Stream@PNG-en-US.png) | Function view | Function is sufficiently licensed. |

The number of licenses purchased is saved with the project. There is no under-licensing reaction from the integrated drive.

> **Note**
>
> **Licenses for additionally connected S120 drives**
>
> SINAMICS S120 CU320-2 connected to the SIMATIC Drive Controller are licensed with the memory card of the CU320-2. In the event of under-licensing, there is an under-licensing response on the CU320-2 (see [Overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-2)).

##### Procedure

To license SINAMICS Integrated , follow these steps:

1. In the SINAMICS Integrated project tree, double-click on "Parameter assignment" under "Automatic speed control".

   - Or -

   Double-click directly on the license icon ![Procedure](images/148040455563_DV_resource.Stream@PNG-en-US.PNG) in the project tree.

   The runtime functions available for licensing and their license requirements are displayed in the function view under "License".
2. In the right-hand column for each function available for licensing, select the number of licenses you have purchased.

   This number is then entered in the column to the left. If the number of purchased licenses is at least as high as the number of required licenses, the status of the respective function requiring a license is shown in green. This allows you to work with this function.
3. Save these license settings with the project (see [Permanently save the settings](#permanently-save-the-settings)).

### SINAMICS rules in Startdrive

This section contains information on the following topics:

- [Overview of system limits](#overview-of-system-limits)
- [System rules](#system-rules)
- [Rules for sampling times](#rules-for-sampling-times)
- [Sampling times and number of controllable drives](#sampling-times-and-number-of-controllable-drives)
- [Rules for connecting power units in parallel](#rules-for-connecting-power-units-in-parallel)

#### Overview of system limits

The number and type of controlled axes, infeeds and Terminal Modules as well as the additionally activated functions can be scaled by configuring the firmware.

The software and control functions available in the system are executed cyclically with different sampling times ([p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions), [p0799](SINAMICS%20Parameter%20CU.md#p079902-cu-inputsoutputs-sampling-time-2), [p4099](SINAMICS%20Parameter%20SERVO.md#p4099-inputsoutputs-sampling-time)). The sampling times are automatically preassigned during configuration of the drive (see "[Default setting](#default-settings-for-the-sampling-times)"). They can be subsequently adapted by the user.

The number of controllable drives, infeeds and Terminal Modules that can be operated with the selected Control Unit depends on some system rules, the set sampling times, the control mode and the activated additional functions.

There are also still dependencies and rules for the components used and the selected DRIVE-CLiQ wiring.

The existing rules are described in greater detail in the following sub-sections. After this there are notes on the number of controllable drives and some example topologies.

The following standard quantity structures are operable with standard clock cycles:

- 12 V/f control axes with 500 µs
- 6 vector axes with 500 µs
- 6 servo axes with 125 μs
- 3 vector axes with 250 μs
- 3 servo axes with 62.5 μs
- 1 servo axis with 31.25 μs (single-axis module)

Consequently, the conversion of an axis from 125 µs to 62.5 µs normally leads to the loss of an axis. This rule can also be used for the clock-cycle mixing to achieve a general estimate of the quantity structure.

Especially for demanding configurations, drives with high dynamic response or a large number of axes with additional utilization of special functions for example, a check using the SIZER engineering tool is recommended. The SIZER engineering tool calculates the feasibility of the project.

Finally, the utilization flag in [r9976](SINAMICS%20Parameter%20CU.md#r997607-system-utilization) indicates whether a topology is operable. If the utilization exceeds 100%, this is indicated with fault F01054. In this case, one or more axes must be dispensed with or the function scope reduced.

##### Additional parameters

---

#### System rules

This section contains information on the following topics:

- [System rules](#system-rules-1)

##### System rules

A maximum of 24 drive objects (DOs) can be connected to one Control Unit.

**Control Units**

- The CU310-2 Control Unit is a single-axis control module for operating the AC/AC Power Modules in the blocksize (PM240-2) and chassis formats. In addition to these, Terminal Modules, Sensor Modules and HUB modules can also be connected.
- The CU320-2 Control Unit is a multi-axis Control Unit for operating Infeed Modules and Motor Modules in the booksize format. In addition to these, Terminal Modules, Sensor Modules and HUB modules can also be connected.

**Motor Modules / control modes**

For the CU310-2 Control Unit the following applies:

- The CU310-2 Control Unit is a 1-axis control module (servo control, vector control or vector control V/f control) that is plugged onto a Power Module or is operated with a maximum of one AC/AC Power Module in the chassis format (via the X100 DRIVE-CLiQ connection).

For the CU320-2 Control Unit the following applies:

- The CU320-2 Control Unit is a multi-axis control module for operating Motor Modules in the booksize, chassis and blocksize formats (PM240-2 via a Control Unit Adapter).
- For multi-axis modules, each axis counts individually (one Double Motor Module = two Motor Modules).
- There can be a maximum of 12 drive objects of the VECTOR type present concurrently.

  - A maximum of 6 drive objects can be operated concurrently in vector control.
  - A maximum of 12 drive objects can be operated concurrently with V/f control.
- Mixed operation of control types:

  The following are permissible:

  - Mixed operation of servo control and V/f control.
  - Mixed operation of vector control and V/f control.

  The following are not permissible:

  - Mixed operation of servo control and vector control.

The following applies when connecting Motor Modules in parallel:

- Parallel connection is only permitted in the chassis or chassis-2 formats.
- When commissioning Motor Modules in the Chassis-2 format, a firmware version of ≥ V5.2 must be available.
- A parallel connection is only permitted in the VECTOR or V/f control modes.
- Within a parallel connection, a maximum of 4 identical Motor Modules in the chassis format or a maximum of 6 identical Motor Modules in the chassis-2 format are permitted. All modules connected in parallel must have the same power rating.
- Only one drive object may be created for a parallel connection.
- Only one parallel connection is permitted for each Control Unit.

**Line Modules**

For the CU310-2 Control Unit the following applies:

- Operating Line Modules is not permitted.

For the CU320-2 Control Unit the following applies:

- Only one drive object of the Smart Line Module (SLM), Basic Line Module (BLM) and Active Line Module (ALM) types is permissible in each case.
- Mixed operation of an Active Line Module with a Smart Line Module (SLM) or with a Basic Line Module (BLM) is not permissible.
- Mixed operation of a drive object of the Smart Line Module (SLM) type with a drive object of the Basic Line Module (BLM) type is permissible.
- Each active Active Line Module (ALM) or Smart Line Module (SLM) in chassis format must be assigned an active Voltage Sensing Module (VSM). A violation of this rule causes fault F05061 to be issued.
- Two further Voltage Sensing Modules can be operated with the "Network transformer" function module for Active Line Modules (ALM).

The following rules apply when connecting Line Modules in the chassis or chassis-2 format in parallel:

- A parallel connection is permissible for a maximum of 4 infeed modules in the chassis format, or a maximum of 6 infeed modules in the chassis-2 format.
- It is not permissible to operate Infeed Modules with different power ratings.
- When commissioning ALMs in the chassis-2 format connected in parallel, a firmware version of ≥ V5.2 must be available.
- An active Voltage Sensing Module (VSM) must be assigned to each Active Line Module (ALM). A violation of this rule causes alarm F05061 to be issued.
- When using Smart Line Modules (SLM) an active Voltage Sensing Module (VSM) must be assigned to at least one Smart Line Module (SLM) in the parallel connection. A violation of this rule causes fault F05061 to be issued.

The following rules apply when connecting Line Modules in the booksize format in parallel:

- In the booksize format, a maximum of 2 Active Line Modules (ALM) from the 55 kW, 80 kW or 120 kW power class are permissible for each parallel connection.
- It is not permissible to operate Infeed Modules with different power ratings.
- When commissioning ALMs in the booksize format connected in parallel, a firmware version of ≥ V5.2 must be available.
- The use of Voltage Sensing Modules (VSM) is optional.

**Terminal Modules**

Control Unit CU310-2:

- In total, a maximum of 8 drive objects, types TM31, TM15, TM41, TM120 or TM150 can be operated simultaneously.
- A maximum of 3 drive objects, types TM15, TM17 and TM41 may be operated simultaneously.

Control Unit CU320-2:

- In total a maximum of 16 drive objects of the types TM15, TM31, TM41, TM120 or TM150 can be operated concurrently.

**DRIVE-CLiQ Hub Module**

- A maximum of 8 drive objects can be operated at the same time for DRIVE-CLiQ Hub Modules (DMC20 or DME20). DMC20/DME20 are not counted twice here.

#### Rules for sampling times

This section contains information on the following topics:

- [Rules when setting the sampling times](#rules-when-setting-the-sampling-times)
- [Rules for isochronous mode](#rules-for-isochronous-mode)
- [Default settings for the sampling times](#default-settings-for-the-sampling-times)
- [Setting the pulse frequency](#setting-the-pulse-frequency)
- [Setting sampling times](#setting-sampling-times)

##### Rules when setting the sampling times

The following rules apply when setting the sampling times:

**General rules**

- A maximum of two possible cycle levels on the Control Unit, where the shortest sampling times are not integer multiples with respect to one another. All sampling times set must be an integer multiple of the shortest sampling time from one of these two cycle levels.

  This setting is permissible.  
  Additional sampling times must be integer multiples of 250 µs or 455 µs.

**Terminal Modules, Terminal Board, Control Unit**

- For the digital and analog inputs/outputs of these components the minimum sampling time ([p0799](SINAMICS%20Parameter%20CU.md#p079902-cu-inputsoutputs-sampling-time-2), [p4099](SINAMICS%20Parameter%20SERVO.md#p4099-inputsoutputs-sampling-time), [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)) set must be 125 µs.

**Pulse frequencies and current controller sampling times:**

- The current controller sampling times of the drives and infeeds must be synchronous to the set pulse frequency of the power unit (see also [p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency)). Any increase in the pulse frequency requires a reduction in the sampling times and increases the derating in the power unit.

**Line Modules**

- For Active Line Modules (ALM) and Smart Line Modules (SLM) in booksize format, the only current controller sampling time which can be set is 125 µs or 250 µs.
- The permissible current controller sampling time depends on the respective module for Active Line Modules (ALM) and Smart Line Modules (SLM) in chassis format. Either only one current controller sampling time of 250 µs can be set or a current controller sampling time of 400 µs or 375 µs (375 µs for [p0092](SINAMICS%20Parameter%20CU.md#p0092-clock-synchronous-operation-pre-assignmentcheck) = 1) can be selected.
- For Basic Line Modules (BLM), the only current controller sampling time which can be set is 2000 µs (chassis format) or 250 µs (booksize format).

**Motor Modules**

- For Single Motor Modules in booksize format, a current controller sampling time of minimum 31.25 µs can be set (31.25 µs ≤ p0115[0] ≤ 500 µs).
- For Double Motor Modules in booksize format, a current controller sampling time of minimum 62.5 µs can be set (62.5 µs ≤ p0115[0] ≤ 500 µs).
- For Motor Modules in chassis format, a minimum current controller sampling time of 125 µs can be set (125 µs ≤ p0115[0] ≤ 500 µs).
- For Motor Modules in blocksize format, a current controller sampling time of 62.5 µs, 125 µs, 250 µs or 500 µs can be set (only pulse frequencies in multiples of 2 kHz are permissible).

  For PM240-2 FS D-F the minimum current controller sampling time is 125 µs.

**Servo control**

- For servo control, a current controller sampling time between 31.25 µs and 250 µs can be set (31.25 µs ≤ p0115[0] ≤ 250 µs).
- The fastest sampling time of a drive object in the servo control mode is obtained as follows:

  - T<sub>i</sub> = 31.25 µs: Exactly one drive object in servo control
  - T<sub>i</sub> = 62.5 µs: Max. 3 drive objects in servo control
  - T<sub>i</sub> = 125 µs: Max. 6 drive objects in servo control

**Vector control / V/f control**

- A current controller sampling time between 125 µs and 500 µs can be set for vector control (125 µs ≤ p0115[0] ≤ 500 µs). This also applies for operation with V/f control.
- For vector control and vector control V/f control, and when using a sine-wave filter ([p0230](SINAMICS%20Parameter%20VECTOR.md#p0230-drive-filter-type-motor-side) > 0), it is only permissible to change the current controller sampling time of the drive object involved in multiple integer steps of the default value on account of the design of the sine-wave filter.
- The fastest sampling time of a drive object in vector control is obtained as follows:

  - T<sub>i</sub> = 250 µs: Max. 3 drive objects in vector control
  - T<sub>i</sub> = 375 µs: Max. 4 drive objects in vector control
  - T<sub>i</sub> = 400 µs: Max. 5 drive objects in vector control
  - T<sub>i</sub> = 500 µs: Max. 6 drive objects in vector control
  > **Note**
  >
  > **Restriction of the number of axes for chassis in vector control**
  >
  > With active edge modulation / optimized pulse patterns and active sweep, only half the number of axes are permitted.

  > **Note**
  >
  > **Restriction when using Active Line Modules in the chassis-2 format**
  >
  > If an Active Line Module (ALM) in the chassis-2 format is operated in parallel with VECTOR drives, the sampling times in the Motor Modules must be set to 400 μs. To ensure the ability to set faster sampling times, the ALM must be operated on a separate Control Unit.
- The fastest sampling time of a drive object in V/f control mode is obtained as follows:

  - T<sub>i</sub> = 500 µs: Max. 12 drive objects in V/f control mode
- When vector control is operated together with vector control V/f control, a maximum of 11 axes is possible (ALM, TB and TM also possible).

**Safety Integrated Functions**

- Only Single Motor Modules are permissible for servo control with a current controller sampling time T<sub>IReg</sub> ≤ 62.5 μs with the "Safety sensorless" functionality.

###### Additional parameters

---

##### Rules for isochronous mode

> **Note**
>
> **PROFIBUS legend**
>
> T<sub>dp</sub> = PROFIBUS cycle (also DP cycle)
>
> T<sub>mapc</sub> = master application cycle time
>
> T<sub>i</sub> = Input Time (German time of incorporation of actual value)
>
> T<sub>o</sub> = Output Time (German time for setpoint value specification)

The following supplementary conditions must be observed for isochronous operation:

- The PROFIBUS cycle T<sub>dp</sub> must be an integer multiple of 250 μs.
- The PROFIBUS cycle T<sub>dp</sub> must be an integer multiple of the current controller sampling time.
- The times T<sub>i</sub> (time of incorporation of actual value) and T<sub>o</sub> (time for setpoint value specification) must be integer multiples of 125 μs.
- The times T<sub>i</sub> and T<sub>o</sub> must be an integer multiple of the current controller sampling time.
- T<sub>mapc</sub> is an integer multiple of the speed controller sampling time.
- Because T<sub>i</sub> and T<sub>o</sub> are always predefined for a PROFIBUS line, all drives of a Control Unit are affected and run with the same setting.
- p0092 = 1 (isochronous operation preassignment/validation) sets default values for the controller cycles for isochronous PROFIdrive operation during the initial commissioning.

  - The current controller sampling times from "[Pulse frequencies and current controller sampling times for servo control](#cycle-times-for-servo-control)" can be set for servo control.
  - The current controller sampling times from "[Pulse frequencies and current controller sampling times for vector control](#cycle-times-for-vector-control)" can be set for vector control.
- The setting rules for the safety actual value acquisition cycle and the safety monitoring cycle must be observed (for details, see SINAMICS S120 Safety Integrated Function Manual):

  - The monitoring cycle (p9500) must be an integer multiple of the actual value acquisition cycle (p9511). For p9511 = 0, the isochronous PROFIBUS cycle T<sub>dp</sub> is used as the actual value acquisition cycle.
  - Actual value acquisition cycle ≥ 4 × current controller sampling time.
  - The DP cycle should be at least one current controller sampling time longer than the sum of T<sub>i</sub> and T<sub>o</sub>.

The above conditions mean that the smallest common multiple of the current controller sampling time of all axes operated on the isochronous PROFIBUS and 125 µs is used to set T<sub>i</sub>, T<sub>o</sub> and T<sub>dp</sub>.

If isochronous operation is not possible due to incorrect sampling time settings, an appropriate message will be output (A01223, A01224).

###### Cycle settings for SINAMICS Link

SINAMICS Link permits only three cycle settings:

Settings for activated isochronous operation

| T<sub>i</sub> [µs] | T<sub>o</sub> [µs] | T<sub>dp</sub> [µs] |
| --- | --- | --- |
| 500 | 500 | 500 |
| 500 | 1000 | 1000 |
| 1500 | 1500 | 1500 |

##### Default settings for the sampling times

The sampling times of the functions are pre-assigned automatically when the drive is configured.

These default settings are based on the selected mode (vector/servo control) and the activated functions.

If isochronous mode is to be possible with a controller, before the automatic configuration, parameter [p0092](SINAMICS%20Parameter%20CU.md#p0092-clock-synchronous-operation-pre-assignmentcheck) must be set to "1" in order that the sampling times are appropriately preset. If isochronous operation is not possible due to incorrect sampling time settings, an appropriate message will be output (A01223, A01224).

If the application requires a change of the preset sampling times, they can be set using parameters [p0112](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0112-sampling-times-pre-setting-p0115) and [p0113](SINAMICS%20Parameter%20SERVO.md#p0113-minimum-pulse-frequency-selection-1) or directly using [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions), [p0799](SINAMICS%20Parameter%20CU.md#p079902-cu-inputsoutputs-sampling-time-2) and [p4099](SINAMICS%20Parameter%20SERVO.md#p4099-inputsoutputs-sampling-time).

> **Note**
>
> **Recommendation**
>
> Only appropriately qualified experts should change the sampling times set as default values.

When commissioning for the first time, the current controller sampling times (p0115[0]) are automatically preset with factory setting values:

Factory settings

| Format | Number | p0112 | p0115[0] | [p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency) |
| --- | --- | --- | --- | --- |
| **Active Infeed** |  |  |  |  |
| Booksize | 1 | 2 (Low) | 250 µs | - |
| Chassis 400 V / ≤ 300 kW 690 V / ≤ 330 kW | 1 1 | 2 (Low) 2 (Low) | 250 µs 250 µs | - - |
| Chassis 400 V / > 300 kW 690 V / > 330 kW | 1 1 | 0 (Expert) 1 (xLow) | 375 µs (p0092 = 1) 400 µs (p0092 = 0) | - - |
| Chassis-2 | 1 | 2 (Low) | 250 µs | 4 kHz |
| **Smart Infeed** |  |  |  |  |
| Booksize | 1 | 2 (Low) | 250 µs | - |
| Chassis 400 V / ≤ 355 kW 690 V / ≤ 450 kW | 1 1 | 2 (Low) 2 (Low) | 250 µs 250 µs | - - |
| Chassis 400 V / > 355 kW 690 V / > 450 kW | 1 1 | 0 (Expert) 1 (xLow) | 375 µs (p0092 = 1) 400 µs (p0092 = 0) | - - |
| **Basic Infeed** |  |  |  |  |
| Booksize | 1 | 4 (High) | 250 µs | - |
| Chassis | 1 | 2 (Low) | 2000 µs | - |
| **SERVO** |  |  |  |  |
| Booksize | 1 ... 6 | 3 (Standard) | 125 µs | 4 kHz |
| Chassis | 1 ... 6 | 1 (xLow) | 250 µs | 2 kHz |
| Chassis-2 | 1 ... 6 | 1 (xLow) | 250 µs | 2 kHz |
| Blocksize | 1 ... 5 | 3 (Standard) | 125 µs | 4 kHz |
| **VECTOR** |  |  |  |  |
| Booksize | 1 ... 3 only n_ctrl 1 ... 6 only V/f | 3 (Standard) | 250 µs | 4 kHz |
| Chassis 400 V / ≤ 250 kW |  |  |  |  |
| Booksize | 4 ... 6 only n_ctrl   7 ... 12 only f_ctrl | 0 (Expert) | 500 µs | 4 kHz |
| Chassis 400 V / ≤ 250 kW |  |  |  |  |
| Chassis 400 V / > 250 kW 690 V | 1 ... 4 only n_ctrl 1 ... 5 only V/f 5 ... 6 only n_ctrl | 0 (Expert) 1 (xLow) 0 (Expert) | 375 µs (p0092 = 1) 400 µs (p0092 = 0) 500 µs (p0092 = 1) | 1.333 kHz 1.25 kHz 1.0 kHz |
| Chassis-2 | 1 ... 4 only n_ctrl 1 ... 5 only V/f 5 ... 6 only n_ctrl | 0 (Expert) 1 (xLow) 0 (Expert) | 375 µs (p0092 = 1) 400 µs (p0092 = 0) 500 µs (p0092 = 0) | 1.333 kHz 2.5 kHz 1.0 kHz |

> **Note**
>
> If a Power Module blocksize is connected to a Control Unit, the sampling times of all vector drives are set according to the rules for Power Modules blocksize (only 250 µs or 500 µs is possible).

###### Additional parameters

---

##### Setting the pulse frequency

The sampling times for the following functions are set by selecting the appropriate values in [p0112](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0112-sampling-times-pre-setting-p0115) for the closed-loop control configuration in µs and are copied to [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions)[0...6] depending on the performance levels required:

- Current controller (p0115[0])
- Speed controller (p0115[1])
- Flux controller (p0115[2])
- Setpoint channel (p0115[3])
- Position controller (p0115[4])
- Positioner (p0115[5])
- Technology controller (p0115[6])

The performance levels range from xLow to xHigh. Details of how to set the sampling times are given in the SINAMICS S120/S150 List Manual.

###### Setting the pulse frequency using the commissioning tool in online operation

Enter the minimum pulse frequency in [p0113](SINAMICS%20Parameter%20SERVO.md#p0113-minimum-pulse-frequency-selection-1). For isochronous operation ([p0092](SINAMICS%20Parameter%20CU.md#p0092-clock-synchronous-operation-pre-assignmentcheck) = 1), you can only set the parameter so that a resulting current controller sampling time with an integer multiple of 125 μs is obtained. The required pulse frequency can be set after commissioning ([p0009](SINAMICS%20Parameter%20CU.md#p0009-device-commissioning-parameter-filter) = [p0010](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0010-infeed-commissioning-parameter-filter) = 0) in [p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency).

Pulse frequency for isochronous operation

| Control type | p0115[0]  Current controller sampling time / µs | p0113  Pulse frequency / kHz |
| --- | --- | --- |
| Servo control | 250 | 2 |
| 125 | 4 |  |
| Vector control | 500 | 1 |
| 250 | 2 |  |

When commissioning is exited (p0009 = p0010 = 0), the effective pulse frequency (p1800) is appropriately pre-assigned, depending on p0113, and can be subsequently modified.

###### Additional parameters

---

##### Setting sampling times

If sampling times are required which cannot be set using [p0112](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0112-sampling-times-pre-setting-p0115) > 1, you can directly set the sampling times in expert mode using [p0115](SINAMICS%20Parameter%20CU.md#p01150-sampling-time-for-supplementary-functions).

If p0115 is changed online, then the values of higher indices are automatically adapted.

> **Note**
>
> Do not change the sampling times when the commissioning tool is in the offline mode, because in this case if there is an incorrect parameterization, the project download is canceled.

###### Making and checking settings

1. Activate the drive basic configuration with [p0009](SINAMICS%20Parameter%20CU.md#p0009-device-commissioning-parameter-filter) = 3 in the parameter view of the Control Unit.
2. Activate the expert mode with p0112 = 0 in the parameter view of the drive object.
3. Specify the current controller sampling time for the drive object as follows: p0115[0] = current controller sampling time.   
   For the current controller sampling time, only use the values from "[Pulse frequencies and current controller sampling times for servo control](#cycle-times-for-servo-control)" and "[Pulse frequencies and current controller sampling times for vector control](#cycle-times-for-vector-control)".
4. Complete the cycle setting with p0009 = 0 in the parameter view of the Control Unit.

   A startup is then performed. The speed controller sampling time and flux controller cycle are adapted automatically. They therefore remain an integer multiple of the current controller sampling time.
5. Then check the maximum speed [p1082](SINAMICS%20Parameter%20SERVO.md#p10820n-maximum-speed-1), the set pulse frequency [p1800](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1800-pulse-frequency) and start an automatic calculation of the controller data ([p0340](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p0340-automatic-calculation-control-parameters) = 4).

###### Additional parameters

---

#### Sampling times and number of controllable drives

This section contains information on the following topics:

- [Cycle times for servo control](#cycle-times-for-servo-control)
- [Cycle times for vector control](#cycle-times-for-vector-control)
- [System sampling times and number of controllable drives](#system-sampling-times-and-number-of-controllable-drives)
- [Cycle mix for servo control and vector control](#cycle-mix-for-servo-control-and-vector-control)

##### Cycle times for servo control

The number of axes that can be operated with a Control Unit depends on the cycle times and the control mode. The number of usable axes and the associated cycle times for each control type are listed below. The other available remaining computation times are available for options (e.g. DCC).

###### Cycle times for servo control

This following table lists the number of axes that can be operated with a Control Unit in the servo control mode. The number of axes is also dependent on the cycle times of the controller:

Sampling time setting for servo control

| Cycle times [µs] |  | Number |  | Motor/dir. measuring systems | TM<sup>1)</sup>/TB |
| --- | --- | --- | --- | --- | --- |
| Current controller | Speed controller | Axes | Infeed |  |  |
| 125 | 125 | 6 | 1 [250 μs] | 6 / 6 | 3 [2000 μs] |
| 62.5 | 62.5 | 3 | 1 [250 μs] | 3 / 3 | 3 [2000 μs] |
| 31.25<sup>2)</sup> | 31.25<sup>2)</sup> | 1 | 1 [250 μs] | 1 / 1 | 3 [2000 μs] |
| <sup>1)</sup> Valid for TM31 or TM15; for TM41, TM15, TM120, TM150 - restrictions are possible depending on the set sampling time.   <sup>2)</sup> In the cycle level 31.25 µs, you can also create the following objects: Sensor Module External (SME) and SMC20 that support the current firmware and hardware. These can be recognized from the Article end number ... 3. No additional axis can be operated in this cycle level. |  |  |  |  |  |

###### Adjustable pulse frequencies and current controller sampling times for servo control

The pulse frequencies that can be set depending on the selected current controller sampling time are shown in [r0114](SINAMICS%20Parameter%20SERVO.md#r011409-minimum-pulse-frequency-recommended). Because of the integrating current measurement, pulse frequencies that are a multiple of half the current controller sampling frequency should be preferred. Otherwise, the current is not measured synchronous to the pulse frequency and a fluctuating actual current value results. This causes disturbance in the control circuits and higher losses in the motor (such as pulse frequency 5.333 kHz and current controller sampling time 62.5 μs).

The recommended settings are marked with **XX** in the Table; all other possible settings are marked with X.

Pulse frequencies and current controller sampling times for servo control

| Pulse frequency [kHz] | Current controller sampling time [µs] |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 250.0 | 187.5 | 150.0 | 125.0 | 100.0 | 93.75 | 75.0 | 62.5 | 50.0 | 37.5 | 31.25 |  |
| 16.0 | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | X | ‑ | ‑ | **XX** |
| 13.333 | ‑ | ‑ | X | ‑ | ‑ | ‑ | X | ‑ | ‑ | **XX** | ‑ |
| 12.0 | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 10.666 | ‑ | X | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | X |
| 10.0 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | **XX** | ‑ | ‑ |
| 8.888 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ |
| 8.0 | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | **XX** | ‑ | ‑ | X |
| 6.666 | ‑ | ‑ | X | ‑ | ‑ | ‑ | **XX** | ‑ | X | X | ‑ |
| 6.4 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X |
| 5.333 | ‑ | X | ‑ | ‑ | ‑ | **XX** | ‑ | X | ‑ | X | ‑ |
| 5.0 | ‑ | ‑ | ‑ | ‑ | **XX** | ‑ | ‑ | ‑ | X | ‑ | ‑ |
| 4.444 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| 4.0 | X | ‑ | ‑ | **XX** | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ |
| 3.555 | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| 3.333 | ‑ | ‑ | **XX** | ‑ | X | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| 3.2 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ |
| 2.666 | ‑ | **XX** | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.5 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.222 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.133 | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.0 | **XX** | ‑ | ‑ | X | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.777 | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.666 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.6 | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.333 | ‑ | X | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |

###### Cycle mix

Detailed information about the cycle mix for servo control is provided in the Section "[Cycle mix for servo control and vector control](#cycle-mix-for-servo-control-and-vector-control)".

###### Additional parameters

---

##### Cycle times for vector control

###### Cycle times for vector control

This following table lists the number of axes that can be operated with a Control Unit in the vector control mode. The number of axes is also dependent on the cycle times of the controller:

Sampling time setting for vector control

| Cycle times [µs] |  | Number |  | Motor/dir. measuring systems | TM<sup>1)</sup>/TB |
| --- | --- | --- | --- | --- | --- |
| Current controller | Speed controller | Axes | Infeed<sup>2)</sup> |  |  |
| 500 µs | 2000 µs | 6 | 1 [250 μs] | 6 / 6 | 3 [2000 μs] |
| 400<sup>3)</sup> µs | 1600 µs | 5 | 1 [250 μs] | 5/5 | 3 [2000 μs] |
| 250 µs | 1000 µs | 3 | 1 [250 μs] | 3 / 3 | 3 [2000 μs] |
| <sup>1)</sup> Valid for TM31 or TM15; for TM41, TM15, TM120, TM150 - restrictions are possible depending on the set sampling time.   <sup>2)</sup> For power units in the chassis format, the infeed cycle depends on the power rating of the module and can be 400 μs, 375 μs or 250 μs.   <sup>3)</sup> This setting results in lower remaining computation times. |  |  |  |  |  |

> **Note**
>
> **Restriction when connecting Active Line Modules of the chassis-2 format in parallel**
>
> If an Active Line Module (ALM) in the chassis-2 format is operated in parallel with VECTOR drives, the sampling times in the Motor Modules must be set to 400 μs. To ensure the ability to set faster sampling times, the ALM must be operated on a separate Control Unit.

###### Adjustable pulse frequencies and current controller sampling times for vector control

The pulse frequencies that can be set depending on the selected current controller sampling time are shown in [r0114](SINAMICS%20Parameter%20SERVO.md#r011409-minimum-pulse-frequency-recommended).

This means that maximum 2 cycle levels can be mixed.

Pulse frequencies and current controller sampling times for vector control

| Pulse frequency [kHz] | Current controller sampling time [µs] |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 500.0 | 375.0 | 312.5 | 250.0 | 218.75 | 200.0 | 187.5 | 175.0 | 156.25 | 150.0 | 137.5 | 125.0 |  |
| 16.0 | X | X | X | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | X |
| 15.0 | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 14.545 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ |
| 14.0 | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 13.714 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 13.333 | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ |
| 12.8 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ |
| 12.0 | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 11.428 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| 10.666 | ‑ | X | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| 10.0 | X | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 9.6 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 9.142 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 8.0 | X | X | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X |
| 7.272 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ |
| 6.666 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ |
| 6.4 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ |
| 6.0 | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 5.714 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| 5.333 | ‑ | X | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| 5.0 | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 4.571 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 4.0 | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X |
| 3.636 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ |
| 3.333 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ |
| 3.2 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ |
| 2.857 | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ |
| 2.666 | ‑ | X | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.5 | ‑ | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.285 | ‑ | ‑ | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 2.0 | X | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.6 | ‑ | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.333 | ‑ | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |
| 1.0 | X | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ | ‑ |

> **Note**
>
> **Restriction for chassis format**
>
> If edge modulation with [p1802](SINAMICS%20Parameter%20VECTOR.md#p18020n-modulator-mode-1) ≥ 7 and sweep with [p1810](SINAMICS%20Parameter%20ACTIVE%20INFEED%20CONTROL.md#p1810-modulator-configuration).2 = 1 are activated simultaneously, the quantity structure for the vector control is halved. Then maximum 3 axes at 500 µs, 2 axes at 400 µs or 1 axis at 250 µs current controller sampling time is permitted.

###### Additional parameters

---

##### System sampling times and number of controllable drives

###### Cycle times for V/f control

The following table lists the number of axes that can be operated with a Control Unit in the V/f control mode. The number of axes depends on the current controller sampling time:

Sampling time setting for V/f control

| Cycle times [µs] |  | Number |  | Motor/dir. measuring systems | TM/TB |
| --- | --- | --- | --- | --- | --- |
| Current controller | Speed controller | Drives | Infeed |  |  |
| 500 | 2000 | 12 | 1 [250 μs] | - / - | 3 [2000 μs] |

###### Mixed operation of servo control and V/f control

In mixed operation with servo control and V/f control, one axis in servo control at 125 µs uses exactly as much computing power as two axes in V/f control at 500 µs. In conjunction with servo control, a maximum of 11 axes are permitted (1 servo control plus 10 vector control V/f).

Number of axes for mixed servo control operation

| Number of axes in servo control |  |  |  | Number of axes in V/f control |  |
| --- | --- | --- | --- | --- | --- |
| 6 | 125 µs | 3 | 62.5 µs | 0 | ‑ |
| 5 | 125 µs | ‑ | ‑ | 2 | 500 µs |
| 4 | 125 µs | 2 | 62.5 µs | 4 | 500 µs |
| 3 | 125 µs | ‑ | ‑ | 6 | 500 µs |
| 2 | 125 µs | 1 | 62.5 µs | 8 | 500 µs |
| 1 | 125 µs | ‑ | ‑ | 10 | 500 µs |
| 0 | ‑ | 0 | ‑ | 12 | 500 µs |

###### Mixed operation of vector control and V/f control

In mixed operation with vector control and V/f control, one axis in vector control at 250 µs uses exactly as much computing power as two axes in V/f control at 500 µs. In conjunction with vector control, a maximum of 11 axes are permitted (1 vector control plus 10 V/f control).

Number of axes for mixed vector control operation

| Number of axes in vector control |  |  |  | Number of axes in V/f control |  |
| --- | --- | --- | --- | --- | --- |
| 6 | 500 µs | 3 | 250 µs | 0 | ‑ |
| 5 | 500 µs | ‑ | ‑ | 2 | 500 µs |
| 4 | 500 µs | 2 | 250 µs | 4 | 500 µs |
| 3 | 500 µs | ‑ | ‑ | 6 | 500 µs |
| 2 | 500 µs | 1 | 250 µs | 8 | 500 µs |
| 1 | 500 µs | ‑ | ‑ | 10 | 500 µs |
| 0 | ‑ | 0 | ‑ | 12 | 500 µs |

###### Cycle times of the CU310-2 in the servo control mode

Setting the sampling times for servo control

| Cycle times [µs] |  | Number |  | Via DQ<sup>2)</sup> | Snapped-on | TM<sup>1)</sup> / TB |
| --- | --- | --- | --- | --- | --- | --- |
| Current controller | Speed controller | Axes | Infeed | Motor Module | Power Module |  |
| 125 | 125 | 1 | ‑ | ‑ | 1 | 3 [2000 μs] |
| 62.5 | 62.5 | 1 | ‑ | ‑ | 1 | 3 [2000 μs] |
| <sup>1)</sup> Valid for TM15 or TM41; for TM31, TM120, TM150, restrictions may apply depending on the sampling time that is set.   <sup>2)</sup> DQ = DRIVE-CLiQ |  |  |  |  |  |  |

If the CU 310-2 is snapped onto a PM240-2 FS A-C, a minimum current controller sampling time of 62.5 µs is possible. For PM240-2 FS D-F the minimum current controller sampling time is 125 µs.

###### Using DCC

The available remaining computation time can be used for DCC. The following supplementary conditions apply:

- For each servo control axis with 125 μs saved (≙ 2 V/f axes with 500 μs), max. 75 DCC blocks with 2 ms time slice can be configured.
- 50 DCC blocks with 2 ms time slice correspond to 1.5 V/f axes with 500 μs.

Detailed information on how to use DCC standard blocks is provided in the "SINAMICS/SIMOTION DCC Editor Description" Manual.

###### Using EPOS

The following table lists the number of axes that can be operated with a SINAMICS S120 when using a "basic positioner" (EPOS) function module. The number of axes depends on the current controller sampling time.

Sampling times when using EPOS

| Cycle times [µs] |  | Cycle times [ms] |  | Number |  |
| --- | --- | --- | --- | --- | --- |
| Current controller | Speed controller | Position controller | Positioner | Axes | Infeed |
| 250 | 250 | 2 | 8 | 6 | 1 [250 μs] |
| 250 | 250 | 1 | 4 | 5 | 1 [250 μs] |
| 125 | 125 | 1 | 4 | 4 | 1 [250 μs] |

The CPU processing time required for the EPOS function module (with 1 ms position controller/4 ms positioner) corresponds to the same CPU processing time of 0.5 V/f axes with 500 μs.

###### Using the SINAMICS Web server

The available computation time can be used for the SINAMICS Web server. The following supplementary condition applies:

- The utilization of the system ([r9976](SINAMICS%20Parameter%20CU.md#r997607-system-utilization)) must be less than 90%!
- A maximum of five users can access data on the same drive via the SINAMICS Web server.

###### Using the CUA31/CUA32

The following table shows the number of axes that can be operated when using the CUA31 or CUA32 Control Unit Adapter. The number of axes is dependent on the following conditions:

Number of axes when using the CUA31/CUA32

| Condition | Number of axes |
| --- | --- |
| The CUA31 or CUA32 is the first component in the topology. | 5 |
| The CUA31 or CUA32 is **not** the first component in the topology. | 6 |
| Current controller sampling time = 62.5 µs | 1 |

###### Additional parameters

---

##### Cycle mix for servo control and vector control

###### Supplementary conditions

The rules for setting the sampling time (see "[Rules when setting the sampling times](#rules-when-setting-the-sampling-times)") and the rules on isochronous mode (see "[Rules for isochronous mode](#rules-for-isochronous-mode)") apply.

These rules mean that the smallest common multiple of the current controller sampling times of all axes operated on the isochronous PROFIBUS and 125 µs is used to set T<sub>i</sub>, T<sub>o</sub> and T<sub>dp</sub>.

###### Current controller sampling times for cycle mix

Consequently the smallest common multiple of the current and speed controller sampling times of all axes operated on the isochronous PROFIBUS is used to set the base cycle for T<sub>i</sub>, T<sub>o</sub> and T<sub>dp</sub>. For a cycle mix, a compromise must be sought between the base cycle to set T<sub>i</sub>, T<sub>o</sub> and T<sub>dp</sub>, and the required pulse frequency.

Examples of cycle mixes for servo control

| Cycle mix: Current controller sampling times [µs] |  | Base cycle for T<sub>i</sub>, T<sub>o </sub>[µs] | Base cycle for T<sub>dp</sub>, T<sub>mapc</sub>[µs] |
| --- | --- | --- | --- |
| 250.00 | +125.00 | 250 | 250 |
| 187.50 | +125.00 | 375 | 750 |
| 150.00 | +125.00 | 750 | 750 |
| 125.00 | +125.00 | 125 | 250 |
| 100.00 | +125.00 | 500 | 500 |
| 93.75 | +125.00 | 375 | 750 |
| 75.00 | +125.00 | 375 | 750 |
| 62.50 | +125.00 | 125 | 250 |
| 50.00 | +125.00 | 250 | 250 |
| 37.50 | +125.00 | 750 | 750 |
| 31.25 | +125.00 | 125 | 250 |
| Base cycles for the isochronous PROFIBUS for a cycle mix with 125 μs |  |  |  |

Examples for cycle mixes for vector control

| Cycle mix: Current controller sampling times [µs] |  | Base cycle for T<sub>i</sub>, T<sub>o </sub>[µs] | Base cycle for T<sub>dp</sub> [µs] | Base cycle for T<sub>mapc</sub> [µs] |
| --- | --- | --- | --- | --- |
| 500.00 | +250.00 | 500 | 500 | 2000 |
| 375.00 | +250.00 | 750 | 750 | 3000 |
| 312.50 | +250.00 | 1250 | 1250 | 5000 |
| 250.00 | +250.00 | 250 | 250 | 1000 |
| 218.75 | +250.00 | 1750 | 1750 | 7000 |
| 200.00 | +250.00 | 1000 | 1000 | 4000 |
| 187.50 | +250.00 | 750 | 750 | 3000 |
| 175.00 | +250.00 | 1750 | 1750 | 7000 |
| 156.25 | +250.00 | 1250 | 1250 | 5000 |
| 150.00 | +250.00 | 750 | 750 | 3000 |
| 137.50 | +250.00 | 2750 | 2750 | 11000 |
| 125.00 | +250.00 | 250 | 250 | 1000 |
| Base cycles for the isochronous PROFIBUS for a cycle mix with 250 μs |  |  |  |  |

> **Note**
>
> When the current controller sampling time is set, the speed controller sampling time is automatically preset:
>
> - Servo control: Speed controller sampling time = current controller sampling time
> - Vector control: Speed controller sampling time = current controller sampling time x 4
>
> The preassignment of the speed controller sampling time can be changed to influence T<sub>mapc</sub>. For example, the current controller sampling time can be increased from 800 µs to 1000 µs so that T<sub>mapc</sub> can be set to be a multiple of 1000 µs.

###### Asynchronous node on the isochronous PROFIBUS

For cycle mix, lengthened base cycles with the following effects often result on the isochronous PROFIBUS:

- Because the isochronous PROFIBUS can no longer be operated with the default setting, adaptations must be made to the hardware configuration.
- The increased setting values for T<sub>i</sub>, T<sub>o</sub> and T<sub>dp</sub> have disadvantageous effects on the dynamics of the position control loop.

Despite a cycle mix, the parameter p2049 can be used to operate the axis with the different current controller sampling time asynchronously on the isochronous PROFIBUS. This allows the default setting of the hardware configuration to be retained.

This, however, causes the advantages of the isochronous operation for the asynchronous axis to be lost:

- The setpoints act at times that differ from T<sub>o</sub>, i.e. an interpolating position-controlled operation with other axes is not possible.
- The actual values are read at times that differ from T<sub>i</sub>, i.e. the actual values must not be used to control other axes.

  A critical application would be, for example, a spindle that cuts a thread with the programmed thread pitch together with a position-controlled Z-axis by the controller adjusting the plunging depth of the Z-axis depending on the spindle position.

#### Rules for connecting power units in parallel

This section contains information on the following topics:

- [Fundamentals](#fundamentals-2)
- [Possible applications](#possible-applications)
- [Connecting Line Modules in parallel](#connecting-line-modules-in-parallel)
- [Parallel connection of Motor Modules](#parallel-connection-of-motor-modules)

##### Fundamentals

In order to extend the power range, SINAMICS S120 supports the parallel connection of identical power units such as Line Modules and/or Motor Modules.

**Advantages of a parallel connection:**

- Higher converter power if it is not technically or economically feasible to achieve the required power in another way.
- Higher availability, for example, to maintain emergency operation (possibly also at a lower power level), if a power unit fails.

**Derating of the rated current**

When SINAMICS S120 power units are connected in parallel you must slightly reduce the rated current.

| Reduction (derating) of the rated current | Parallel connection of | Comment |
| --- | --- | --- |
| 7.5 % | Basic Line Modules with Smart Line Modules | Modules do not have current equalization control functionality |
| 5.0 % | Active Line Modules with Motor Modules | Modules operate with current equalization control |

**Permissible mixed configurations when connecting Line Modules in parallel**

Smart Line Modules may be operated together with Basic Line Modules that have Article numbers ending with a "3" (Chassis) or a "2" (Cabinet) with one or several CUs if precisely defined preconditions and the information in the Configuration Manual are strictly maintained. You can find this information in the "[SINAMICS - Low Voltage Engineering Manual](http://www.automation.siemens.com/mcms/infocenter/dokumentencenter/ld/Documentsu20Catalogs/lv-umrichter/sinamics-engineering-manual-lv-en.pdf)".

**Variants of the parallel connection that have not been released**

- Combining different types of Line Modules within the same parallel connection (e.g. Basic Line Modules with Smart Line Modules or Basic Line Modules with Active Line Modules).
- Motor Modules in servo control
- Motor Modules in the Blocksize and Booksize formats

###### Requirements

- Same type
- Same type rating
- Same rated voltage
- Same firmware version

  > **Note**
  >
  > For the following power units, when commissioning, a firmware version ≥ V5.2 must be available.
  >
  > - Active Line Module in the Booksize format
  > - Active Line Modules in the Chassis-2 format
  > - Motor Modules in the Chassis-2 format
- Chassis format

  > **Note**
  >
  > **Exception:**
  >
  > A few ALMs in the Booksize format can also be connected in parallel.
- Vector drive when connecting Motor Modules in parallel

> **Note**
>
> **Check made in Startdrive**
>
> As soon as power units connected in parallel are specified in the device view, Startdrive checks whether it is possible to connect the selected power units in parallel. If a parallel connection is not permitted, a message is output and Startdrive allows you to remove all of the components involved in the parallel connection that are not required. The program effectively prevents parallel connections that are not permitted from being configured.

###### Features

The main features of parallel connection are:

- Parallel connection of up to four Motor Modules on one motor

  - Parallel connection of multiple Motor Modules on one motor with separate winding systems (p7003 = 1).

    > **Note**
    >
    > The preferred solution is that you use motors with separate winding systems
  - Parallel connection of multiple Motor Modules on one motor with a single winding system (p7003 = 0) is possible.
  - Parallel connection of up to 6 Chassis-2 Motor Modules on one motor is possible.
  > **Note**
  >
  > Carefully take into account the additional notes and instructions provided in the SINAMICS S120 Equipment Manual Chassis Power Units.
- Parallel connection of up to 4 power units of the Chassis format on the infeed side (controlled/uncontrolled).
- Parallel connection of up to 6 power units of the Chassis-2 format on the infeed side (controlled).
- A Control Unit, which controls and monitors power units on the line supply and motor sides connected in parallel, can control an additional drive, e.g. an auxiliary drive.
- Parallel-connected power units must be connected to the same Control Unit.
- For Line Modules of the Chassis-2 format, no additional drives/infeed units can be connected to a CU if the number of modules connected in parallel is > 4.
- A Control Unit CU320-2 can simultaneously actuate a maximum of one parallel connection on the grid side and one parallel connection on the motor side if the number of modules connected in parallel is > 4 in each case.
- Components at the line and motor sides for decoupling the parallel-connected power units and for ensuring symmetrical current distribution are recommended.
- Simple commissioning, because no special parameterization is necessary.
- Individual power units can be parameterized and diagnosed (troubleshooting) with p7000 ff.

##### Possible applications

Power units can be connected in parallel (infeeds) in the following cases:

- 6-pulse circuit

  The modules connected in parallel are supplied from a two-winding transformer.
- 12-pulse circuit

  The modules connected in parallel are supplied via a three-winding transformer, whose secondary windings supply voltages with a phase shift of 30°.

**Overview:**

![Figure](images/147995147275_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Additional information on parallel power unit connections, particularly with regard to their configuration, can be found in the "[SINAMICS Low Voltage Configuration Manual](http://www.automation.siemens.com/mcms/infocenter/dokumentencenter/ld/Documentsu20Catalogs/lv-umrichter/sinamics-engineering-manual-lv-en.pdf)".

###### Infeed concepts - parallel (one Control Unit) and parallel redundant (2Control Units)

Some applications require redundant infeeds for a DC line-up. This requirement can be fulfilled through the implementation of multiple, independent infeeds which are connected in parallel to the DC line-up. Depending on how the drive is dimensioned, the DC line-up can continue operating at between 50% to 100% output when one infeed fails.

In the cases of the non-redundant variant, a single Control Unit generally controls all parallel-connected power units which then function like a single, high-output infeed. For the redundant parallel connection, each infeed is controlled by a separate Control Unit and is thus completely independent.

The type of circuit required depends on whether the redundancy requirement applies only to the infeed itself or also includes the supply-side transformers or the line supply systems.

###### 6-pulse infeed

With a 6-pulse infeed, the two redundant infeeds with the same power rating are supplied from a line supply via a two-winding transformer. As both infeeds are supplied with exactly the same line voltage, the current distribution is largely symmetrical in normal operation, even with uncontrolled infeeds. The infeeds can thus be dimensioned such that, taking into account a minor current derating factor, each can carry 50% of the total current. However, if one infeed fails, only half the output remains available. If the full output needs to be available when one infeed fails, then each infeed must be dimensioned to carry the full current.

###### 12-pulse infeed

For a 12-pulse infeed, the two redundant infeeds with the same power rating are supplied from a line supply via a three-winding transformer. Depending on the transformer design, the line-side voltages of the two infeeds will include minor tolerances of between about 0.5% to 1%. These can cause slightly asymmetrical current distribution in normal operation when uncontrolled infeeds are used and current derating factors must be applied accordingly. If the full output needs to be available when one infeed fails, then each infeed must be dimensioned to carry the full current.

In addition to the requirements of the three-winding transformer and the infeed, the line supply system must also meet certain standards with respect to the voltage harmonics present at the point of common coupling of the three-winding transformer.

###### 6-pulse, 12-pulse infeed

When separate Control Units are used, pre-charging may not be synchronized accurately enough, i.e. a converter system must be able to pre-charge the total capacity of the drive line-up. Pre-charging power for the DC link in parallel operation must be dimensioned so that the capacitance of the DC link can be fully charged by a single converter system. Otherwise a separate pre-charging device must be provided.

###### Configuring a parallel connection

Additional information on connecting power units in parallel can be found in the "SINAMICS Low Voltage Engineering Manual" (see above).

##### Connecting Line Modules in parallel

This section contains information on the following topics:

- [Active Line Modules](#active-line-modules)
- [Basic Line Modules](#basic-line-modules)
- [Smart Line Modules](#smart-line-modules)

###### Active Line Modules

Active Line Modules (ALMs) can supply motoring energy and return regenerative energy to the supply system.

The parallel connection of a maximum of 4 identical ALMs in the Chassis format or a maximum of 6 identical ALMs in the Chassis-2 format is supplied via a common two-winding transformer and controlled in synchronism from a common Control Unit. In the case of a parallel connection of more than 4 power units, a stand-alone Control Unit must be provided that is not used to operate any additional drive objects (DOs). The modules must not be connected to the supply using a three-winding transformer with phase-displaced secondary voltages.

Active Line Modules generate a controlled DC voltage, which remains constant despite fluctuations in the line voltage. In this case, the line voltage must remain within the permissible tolerance range.

Active Line Modules draw an almost sinusoidal current from the supply system and therefore cause virtually no line harmonic distortions.

When connecting Active Line Modules in parallel you must carefully take into account the following module-specific information.

Active Line Modules are available for the following voltages and power ratings:

| Line supply voltage | Rated power |
| --- | --- |
| 380 to 480 V 3 AC | 132 to 900 kW |
| 500 to 690 V 3 AC | 560 to 1400 kW |

###### Active Line Modules (Chassis and Chassis-2 formats)

The following preconditions apply when connecting Active Line Modules in the Chassis and Chassis-2 formats in parallel:

**Requirements:**

- Chassis format
- 2 Voltage Sensing Modules (VSM10)
- The DC link voltage is greater than the rms value of the rated line voltage by a factor of 1.5.

**Rules:**

- Up to 4 identical ALMs of the Chassis format or 6 identical ALMs of the Chassis-2 format can be switched in parallel.
- A common Control Unit is always required whenever the modules are connected in parallel.
- For the parallel connection of ALMs of the Chassis-2 format with more than 4 modules, the DRIVE-CLiQ line must be separated. The modules 1 to 3 connected in parallel must be operated at the 1st DRIVE-CLiQ socket. The remaining modules must be operated at the 2nd DRIVE-CLiQ socket.
- Special Line Connection Modules are available for the parallel connection.
- In the case of multiple infeeds, the systems must be supplied by a common infeed point. Different networks are, as a result, not permissible.
- A derating factor of 5% must be taken into consideration, regardless of the number of ALMs connected in parallel.

###### Active Line Modules (Booksize format)

Active Line Modules (ALMs) in the Booksize format are available in the 55 kW, 80 kW and 120 kW power variants.

**Requirements:**

- Booksize format
- Firmware version ≥ V5.2
- 2 Voltage Sensing Modules (VSM10)

**Rules:**

- Up to 2 identical ALMs can be connected in parallel.
- The parallel connection is possible in a DRIVE-CLiQ topology with one CU320-2 without Motor Modules.
- A common Control Unit (CU) must always be used to implement the parallel connection.
- Special Line Connection Modules are available for the parallel connection.
- In the case of multiple infeeds, the systems must be supplied by a common infeed point. Different networks are, as a result, not permissible.
- A derating factor of 5% must be taken into consideration, regardless of the number of ALMs connected in parallel.

###### Balancing the currents

The following measures help to ensure balanced currents in parallel connections of Active Line Modules:

- Reactors in the Clean Power Filters of the Active Interface Modules.
- Use of symmetrical power cabling between the transformer and the Active Interface Modules / Active Line Modules connected in parallel (identical cables with the same cross-section and length)
- Referred to the rated current of the individual Active Interface Modules/Active Line Modules, the derating factor is 5 %.

###### Additional information

You can find additional information on the following topics in the SINAMICS S120 Drive Functions Function Manual in Chapter "Master/slave function for Active Infeed":

- 6-pulse, redundant parallel connection of Active Line Modules with several Control Units
- 12-pulse parallel connection of Active Line Modules

###### Basic Line Modules

Basic Line Modules supply energy to the connected Motor Modules. They are used where regenerative feedback capability is not required. The DC link voltage is greater than the rms value of the line rated voltage by a factor of 1.35.

If regenerative operating states occur in the drive line-up, Braking Modules that convert the excess energy to heat in braking resistors must be used.

Basic Line Modules in Chassis format are available for the following voltages and power ratings:

| Line supply voltage | Rated power |
| --- | --- |
| 380 to 480 V 3 phase AC | 200 ... 710 kW |
| 500 to 690 V 3-phase AC | 250 ... 1100 kW |

**Requirements:**

As Basic Line Modules have no current compensation control, the three-winding transformer, power cabling and line reactors must meet the following requirements in order to provide a balanced current:

- Three-winding transformer must be symmetrical, recommended vector groups Dy5d0 or Dy11d0.
- Relative short-circuit voltage of three-winding transformer u<sub>k</sub> ≥ 4%.
- Difference between relative short-circuit voltages of secondary windings Δu<sub>k</sub> ≤ 5%.
- Difference between no-load voltages of secondary windings ΔU ≤ 0.5%.
- Use of symmetrical power cabling between the transformer and the Basic Line Modules (cables of identical type with the same cross-section and length)
- Using line reactors that match the Basic Line Modules

  Line reactors can be omitted if a double-tier transformer is used and only one Basic Line Module is connected to each secondary winding of the transformer.

A double-tier transformer is generally the only means of meeting the requirements of a three-winding transformer for this application. Line reactors must always be installed if other types of three-winding transformer are used. Alternative solutions for obtaining a phase offset of 30°, such as 2 separate transformers with different vector groups, cannot be used due to the inadmissibly high tolerances involved.

**Rules:**

- Up to 4 identical Basic Line Modules can be connected in parallel.
- A common Control Unit is always required whenever the modules are connected in parallel.
- Special Line Connection Modules are available for the parallel connection.
- For several infeeds, power must be supplied to the systems from a common infeed point (i.e. the modules cannot be operated on different line supplies).
- A current reduction (derating) of 7.5% must be taken into consideration, regardless of the number of modules connected in parallel.

###### 6-pulse parallel connection of Basic Line Modules

With the 6-pulse parallel connection, up to four Basic Line Modules are supplied by a common two-winding transformer on the line side and controlled by a common Control Unit.

###### 12-pulse parallel connection of Basic Line Modules

For 12-pulse parallel connections, up to four Basic Line Modules are supplied by a three-winding transformer on the line side. In this case, an even number of modules (e.g. two or four) must be divided between the two secondary windings. The Basic Line Modules of both subsystems are controlled by a common Control Unit - even though the input voltages are 30° out of phase.

There is also the redundant version with which two BLMs in each case are controlled by one Control Unit.

If several Motor Modules are supplied from a non-regenerative infeed unit (e.g. a BLM) - or for power failure or overload (for SLM/ALM), the V<sub>dc_max</sub> control may only be activated for a Motor Module whose drive should have a high moment of inertia.

For the other Motor Modules, this function must be disabled or monitoring must be set.

**Unstable drives:**

If the V<sub>dc_max</sub>control is active for multiple Motor Modules, then the controllers may have negative effects on each other in the case of unfavorable parameter assignment. The drives may become unstable and individual drives may unintentionally accelerate.

Remedial measures:

- activate the V<sub>dc_max</sub> control:

  - Vector control: p1240 = 1 (factory setting)
  - Servo control: p1240 = 1
  - U/f control: p1280 = 1 (factory setting)
- Inhibit V<sub>dc_max</sub> control:

  - Vector control: p1240 = 0
  - Servo control: p1240 = 0 (factory setting)
  - U/f control: p1280 = 0
- Activate the V<sub>dc_max</sub> monitoring

  - Vector control: p1240 = 4 or 6
  - Servo control: p1240 = 4 or 6
  - U/f control: p1280 = 4 or 6

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected motion of individual drives**   If several Motor Modules are supplied from one infeed unit, then if the V<sub>dc_max</sub>control is incorrectly parameterized, individual drives can accelerate in an uncontrolled fashion - which can lead to death or severe injury.   - Only activate the V<sub>dc_max</sub> control for the Motor Module whose drive has the highest moment of inertia. - Inhibit this function for all other Motor Modules, or set this function to monitoring only. |  |

###### Smart Line Modules

Smart Line Modules are infeed/regenerative feedback units. Just like Basic Line Modules, they supply energy to the connected Motor Modules. However, they are capable of feeding regenerative energy back into the line supply.   
The DC-link voltage is greater than the rms value of the line rated voltage by a factor of 1.3.

Smart Line Modules in the Chassis format can be connected to grounded (TN, TT) and ungrounded (IT) line supplies. They are available for the following voltages and power ratings:

| Line supply voltage | Rated power |
| --- | --- |
| 380 to 480 V 3 phase AC | 250 ... 800 kW |
| 500 to 690 V 3-phase AC | 450 ... 1400 kW |

**Rules:**

- Up to four identical Smart Line Modules can be connected in parallel.
- A common Control Unit must always be used to implement the parallel connection.
- A 4% reactor is always required upstream of each Smart Line Module for the purpose of current balancing.
- Special Line Connection Modules are available for the parallel connection.
- With multiple infeeds, power must be supplied to the systems from a common infeed point (i.e. the modules cannot be operated on different line supplies).
- A derating factor of 7.5% must be taken into consideration, regardless of the number of modules connected in parallel.

###### 6-pulse parallel connection of Smart Line Modules

With the 6-pulse parallel connection, up to four Smart Line Modules are supplied by a common two-winding transformer on the line side and synchronously controlled by a common Control Unit.

As Smart Line Modules have no current compensation control, the current must be balanced by the following measures:

- Use of suitable line reactors for the Smart Line Modules.
- Use of symmetrical power cabling between the transformer and the parallel-connected Smart Line Modules (cables of identical type with the same cross-section and length).
- The current reduction (derating) from the rated value for individual Smart Line Modules in a parallel connection is 7.5%.

###### 12-pulse parallel connection of Smart Line Modules

For 12-pulse parallel connections, up to 4 Smart Line Modules are supplied through a three-winding transformer on the line side. In this case, an even number of Smart Line Modules (i.e. 2 or 4), must be divided between the two secondary windings. The Smart Line Modules of both subsystems must be controlled by 2 Control Units due to the 30° phase offset of the input voltages.

##### Parallel connection of Motor Modules

###### Rules

The following rules and notes must be observed when connecting Motor Modules in parallel:

- In the VECTOR control mode, up to 4 Motor Modules in the Chassis format or 6 Motor Modules in the Chassis-2 format can feed a motor in parallel operation. The motor can have electrically isolated winding systems or a common winding system. The type of winding system is set in p7003 (winding in a parallel connection), and influences the following setting options:

  - The required decoupling measures at the outputs of the Motor Modules connected in parallel.
  - The possible modulation systems to generate pulse patterns.

    > **Note**
    >
    > **Operation of Motor Modules for separate winding systems**
    >
    > For separate winding systems, only one Motor Module may be operated per winding.
- In conjunction with the type of infeed, the modulation systems define the maximum attainable output voltage or the motor voltage.

###### Requirements

The following power unit-specific preconditions apply when connecting Motor Modules in parallel:

- Chassis or Chassis-2 format
- When commissioning Motor Modules in the Chassis-2 format, a firmware version of ≥ V5.2 must be available.

###### Permissible motors for parallel connections

The following motors are permissible:

- Motors with electrically isolated winding systems (multi-winding system) in which the individual systems are not electrically coupled.
- Motors with a common winding system (single winding system) in which all parallel windings in the motor are interconnected in such a way that from the outside they look like a single winding system.

The following are inadmissible:

- Motors with separate winding systems on the line side which have a common, internal neutral.

###### Parallel connection of two Motor Modules to one motor with double winding system

Motors in the power range from about 1 MW to 4 MW, for which power units connected in parallel are generally used, frequently have several parallel windings. If these parallel windings are separately routed to the terminal box of the motor, a motor is obtained with winding systems that can be separately accessed. In this case, you can dimension a parallel Motor Module connection so that each motor winding system is precisely supplied from one of the Motor Modules connected in parallel. The diagram below shows this type of arrangement.

![Parallel connection of two Motor Modules to one motor with double winding system](images/147995292939_DV_resource.Stream@PNG-en-US.png)

Parallel connection of two Motor Modules to one motor with double winding system

Owing to the electrical isolation of the winding systems, this arrangement offers the following advantages:

- No decoupling measures (minimum cable lengths and no motor reactors) are required at the infeed output in order to limit any potential circulating currents between the parallel-connected Motor Modules.
- Both types of modulation system, i.e. space vector modulation and pulse-edge modulation can be used, i.e. when the parallel connection is supplied by Basic Line Modules or Smart Line Modules, the maximum obtainable output voltage is almost equal to the three-phase AC line voltage connected to the infeeds (97%). When the parallel connection is supplied by Active Line Modules, a higher output voltage than the input voltage at the three-phase end can be obtained due to the increased DC-link voltage.

In reference to the rated values for individual Motor Modules, the derating factor is 5%.

###### Parallel connection of two Active Line Modules and two Motor Modules on a motor with a single winding system

In many cases, it is not possible to use motors with separate winding systems, for example, in the following cases:

- The required number of separate winding systems cannot be realized due to the pole number.
- The motor is delivered by a third party.
- A motor with a common winding system is already present.

In such cases, the outputs of the Motor Modules connected in parallel are interconnected via the motor cables in the motor terminal box.

Active Interface Modules isolate switching-frequency harmonics from the supply connection and thus effect basic interference suppression of the supply system. These modules are essential to the operation of Active Line Modules. VSM10 Voltage Sensing Modules support Active Line Modules (Chassis format) to operate without any disturbances when line supply conditions are not favorable (e.g. significant voltage fluctuations, brief interruptions in the line voltage).

**Features:**

When 2 ALMs are operated in parallel, the following applies:

- Chassis format

  For ALMs in the Chassis and Chassis-2 format, the VSMs are already integrated in the Active Interface Modules.
- Booksize format

  The use of Voltage Sensing Modules (VSM) is optional (see "[Adding a Voltage Sensing Module](#adding-a-voltage-sensing-module)").

## Sequence of a device configuration

> **Note**
>
> **Offline only**
>
> The drive components can only be combined, specified and configured in the offline mode. In the online mode, all of the corresponding setting ranges in the device view and in the Inspector window are locked.

### Procedure 1: Create a project offline

With this procedure, the Drive Controller and the components of the integrated Drive are configured offline in a project.

1. [Create the project in the TIA Portal](#creating-a-new-project-or-loading-a-project)
2. [Create the device configuration in the TIA Portal offline](#manually-creating-a-device-configuration)
3. Perform the basic parameterization of the drive units

   - [High dynamic SERVO drives](Servo%20drives%20%28highly%20dynamic%29.md#basic-parameter-assignment)

     - OR -
   - [Universal VECTOR drives](VECTOR%20drives%20%28universal%29.md#basic-parameterization)
4. [Perform a basic parameterization of the Drive Controller](#configuring-the-drive-controller-plc)
5. [Load the project to the target device](#loading-the-project-data-to-the-drive-unit).
6. [Establish an online connection between the PG/PC and the target device](#establishing-an-online-connection-to-the-plc).
7. Perform commissioning steps

   - [High dynamic SERVO drives](Servo%20drives%20%28highly%20dynamic%29.md#rotate-optimize)

     - OR -
   - [Universal VECTOR drives](VECTOR%20drives%20%28universal%29.md#rotate-optimize)

**Result:**

The motor turns.

### Procedure 2: Create a project by reading out a device configuration

In this procedure the drive components are read out online and completed offline when required:

1. [Create or open the project in the TIA-Portal](#creating-a-new-project-or-loading-a-project).
2. [Read out the drive configuration and load into the project](#basic-uploading-a-drive-configuration-as-new-station)

   - Or -

   [Determine the drive configuration from the connected target device, edit and insert.](#advanced-automatically-detecting-the-drive-configuration)
3. Correct the basic parameterization of the drive units

   - [High dynamic SERVO drives](Servo%20drives%20%28highly%20dynamic%29.md#basic-parameter-assignment)

     - OR -
   - [Universal VECTOR drives](VECTOR%20drives%20%28universal%29.md#basic-parameterization)
4. [Perform a basic parameterization of the Drive Controller](#configuring-the-drive-controller-plc)
5. [Load the project to the target device](#loading-the-project-data-to-the-drive-unit).
6. [Establish an online connection between Startdrive and the target device](#establishing-an-online-connection-to-the-plc).
7. Perform commissioning steps

   - [High dynamic SERVO drives](Servo%20drives%20%28highly%20dynamic%29.md#rotate-optimize)

     - OR -
   - [Universal VECTOR drives](VECTOR%20drives%20%28universal%29.md#rotate-optimize)

**Result:**

The motor turns.

### Deactivated drive objects in a drive line-up

Individual drive objects in a drive line-up can be temporarily deactivated in the Startdrive project, for example, because the respective component is being replaced or is currently still missing in the hardware. More detailed information on this topic is available here: "[Activating/deactivating drive components](#activatingdeactivating-drive-components)".

## Adding and assigning parameters

This section contains information on the following topics:

- [Creating a new project or loading a project](#creating-a-new-project-or-loading-a-project)
- [Manually creating a device configuration](#manually-creating-a-device-configuration)
- [Reading out the device configuration from the drive](#reading-out-the-device-configuration-from-the-drive)
- [Configuring the Drive Controller (PLC)](#configuring-the-drive-controller-plc)

### Creating a new project or loading a project

This section contains information on the following topics:

- [Overview](#overview-3)
- [Creating a new project](#creating-a-new-project)
- [Opening the project](#opening-the-project)

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

**Result**

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

   Click "Browse", double-click the required project in your directory structure, select project file "*.ap1x_x".

   ![Example: Opening an existing project from the directory](images/147996103051_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Opening an existing project from the directory](images/147996103051_DV_resource.Stream@PNG-en-US.PNG)

   Example: Opening an existing project from the directory

   Then click "Open".

**Note**

**Older project versions**

You can also open older project versions. Generally, however, these project versions must be upgraded. Startdrive has a check and upgrade mechanism to do this.

**Result**

The selected project opens. If another project was previously displayed, then it is now closed.

- If you have created a new project, the next possible steps for the project that has been opened are now displayed in the detailed view (see the description in the following sections).
- If you have opened an existing project, the interconnected modules of this project are displayed in the device view. You can specify existing modules differently, or remove existing modules and insert new modules instead.

**Project protection**

In the TIA Portal, you can apply project protection to Startdrive projects. All parameters and passwords contained in the project are encrypted and protected from being overwritten. If a Startdrive project is protected, you have to enter a password when you try to open it. You require the following information to open a project:

- User name with authorization for this project
- Password

This information is generated and administered in the user administration of the TIA Portal. Detailed information on project protection can be found in the online help under the heading of "[User management (UMAC)](Managing%20users%20and%20roles.md#managing-users-and-roles)".

### Manually creating a device configuration

This section contains information on the following topics:

- [PLC and Control Unit](#plc-and-control-unit)
- [Line Modules](#line-modules)
- [Motor Modules](#motor-modules)
- [Power Modules](#power-modules)
- [Motors](#motors)
- [Measuring systems](#measuring-systems)
- [Supplementary system components](#supplementary-system-components)

#### PLC and Control Unit

This section contains information on the following topics:

- [Adding the Drive Controller offline](#adding-the-drive-controller-offline)
- [Device replacement: Replacing the PLC in the Drive Controller](#device-replacement-replacing-the-plc-in-the-drive-controller)

##### Adding the Drive Controller offline

The SIMATIC DC drive controller comprises a PLC and an integrated SINAMICS drive (S120 for the CPU 150xD). Several options are shown below to create the Control Unit of the Drive Controller in your device configuration.

> **Note**
>
> You can formally create the Drive Controller via the list of drives, in a similar way as for an S120 drive. However, in this case, only the integrated drive (SINAMICS I) of the Drive Controller is created in the device configuration. You would have to manually add and link the associated PLC in this way. This is the reason that we recommend as exception that you transfer the Control Unit of the Drive Controller into the project via the list of controllers. The following description is based on this recommendation.

###### Requirements

- The online connection to the drive is deactivated.
- A new project has been created.

  - Or -
- An existing project has been opened.

###### Inserting a new Drive Controller with integrated drive

You can insert new drives or controls either in the portal view or in the project view.

To insert drive units in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click on "Controller" to display the list of available controllers.
3. Select the required Drive Controller from list "SIMATIC Drive Controller".
4. Select the firmware version installed on your drive unit.

   If the version numbers (compare: hardware to software) do not match, then it will not be possible to subsequently go online. On creation, the current firmware version is always suggested. If required, you can change the version number via the "Version" drop-down list.
5. Enter a device name in the field at the top with the same name and then click on "OK".

   If you leave the "Open device view" option activated, then the device view opens automatically.

**Inserting a device in the network view**

Alternatively, you can also insert the Drive Controller via the network view.

1. Open the network view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in entry "SIMATIC Drive Controller".
4. Drag the Drive Controller from the hardware catalog and drop it in the network view.

**Inserting a device in the topology view**

Alternatively, you can also insert the Drive Controller via the topology view.

1. Open the topology view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in entry "SIMATIC Drive Controller".
4. Drag the Drive Controller from the hardware catalog and drop it in the network view.

###### Result

The Drive Controller has been inserted. In the network view, the Drive Controller is shown as PLC, which is networked with an internal drive via PROFIdrive.

![Drive Controller networked](images/148040712331_DV_resource.Stream@PNG-en-US.PNG)

Drive Controller networked

Now continue with the configuration or parameter assignment.

> **Note**
>
> When required, you can subsequently assign another PLC to the integrated SINAMICS drive (SINAMICS I) (see "[Device replacement](#device-replacement-replacing-the-plc-in-the-drive-controller)").

##### Device replacement: Replacing the PLC in the Drive Controller

###### Description

You can replace the PLC component of the SIMATIC Drive Controller at any time by a PLC with a different performance level. The linked internal S120 drive is not influenced. When replacing the PLC, the settings of the internal drive are kept. However, the internal drive itself cannot be replaced.

###### Requirements

- A project has been created.
- The Drive Controller (comprising the PLC and internal drive) is created in the network view.

###### Replacing a device via the project tree

1. In the project tree, select the PLC of the Drive Control to be replaced and call the shortcut menu "Change device".

   The "Change device - Drive Controller" dialog box opens.

   ![Replacing the PLC via the project tree](images/148040761483_DV_resource.Stream@PNG-en-US.png)

   ![Replacing the PLC via the project tree](images/148040761483_DV_resource.Stream@PNG-en-US.png)

   Replacing the PLC via the project tree

   The data of the current drive unit is displayed on the top left. The replacement devices in question are displayed in a hardware catalog on the top right.
2. In the hardware catalog of dialog "Change device", select the required replacement device in subfolder "SIMATIC Drive Controller".

   The most important data of the new device is displayed in the center of the dialog in the "New device" field. You can compare this data with the data of the current device (on the left).

   If both drive units are not fully compatible, then corresponding information is displayed in the "Compatibility information" field. This can mean that you may have to accept functional restrictions if you still wish to take the replacement device.
3. Click OK to accept the new PLC.

**Note**

You can also select a PLC in the "SIMATIC S7-1500" subfolder. However, frequently these PLCs are not compatible with the existing device.

###### Replacing a device via the hardware catalog

1. In the hardware catalog, select the required replacement PLC (CPU 150xD), and in the device view, drag this to the placeholder for the current PLC.

   The "Change device" dialog opens:

   ![Replacing the PLC via the hardware catalog](images/148040765579_DV_resource.Stream@PNG-en-US.png)

   ![Replacing the PLC via the hardware catalog](images/148040765579_DV_resource.Stream@PNG-en-US.png)

   Replacing the PLC via the hardware catalog

   The old and new PLCs are compared with the most important data in the dialog.

   If both drive units are not fully compatible, then corresponding information is displayed in the "Compatibility information" field. This can mean that you must assign a different motor, if applicable, if you nevertheless import the desired replacement device.
2. To import the new drive unit, click on OK.

###### Result

The actual PLC of the Drive Controller was replaced by the selected replacement device.

#### Line Modules

This section contains information on the following topics:

- [Adding an infeed](#adding-an-infeed)
- [Making detailed settings](#making-detailed-settings)

##### Adding an infeed

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- A PM 240-2 Power Module is not inserted in the device configuration.   
  PM240-2 and Line Modules are mutually exclusive in the device configuration.

###### Inserting an infeed

You can add an infeed via the hardware catalog.

1. Open the "Line Modules" entry in the hardware catalog.

   The following entries are displayed:

   - "Active Line Modules"
   - "Basic Line Modules"
   - "Smart Line Modules"
2. Drag the unspecified infeed to the DRIVE-CLiQ editor.

   The DRIVE-CLiQ connections are drawn automatically.
3. Click the infeed in the DRIVE-CLiQ editor. Make sure that you click in the white area of the infeed.
4. Select the "Infeed - selection" entry in the secondary navigation.
5. Select your infeed in the list based on the article number.

   The infeed placeholder is assigned the data of the selected infeed.

   The white area turns gray.

   The DRIVE-CLiQ-connection between the interfaces X100 and X200 is drawn as default setting.

###### Connecting infeeds in parallel

> **Note**
>
> **Rules for connecting power units in parallel**
>
> In Startdrive S, power units within certain limits can be connected in parallel. When specifying modules connected in parallel, Startdrive checks whether the rules for connecting in parallel are complied with, and only allows the parallel connection to be established if all rules are complied with. If the rules do not permit a parallel connection, then the program suggests that the last module connected in parallel is removed – or in some instances, prevents the parallel connection from being configured in the first place.
>
> Detailed information about these rules is available under [Rules for parallel connection](#rules-for-connecting-power-units-in-parallel).

To connect Line Modules in parallel with already added modules, proceed as follows:

1. Open the "Line Modules" entry in the hardware catalog. The following entries are displayed:

   - "Active Line Modules"
   - "Basic Line Modules"
   - "Smart Line Modules"
2. Drag a non-specified infeed to the DRIVE-CLiQ editor in the light gray area of the existing infeed.

   Click the infeed in the DRIVE-CLiQ editor. Make sure that you click in the white area of the infeed.
3. Select the "Infeed - selection" entry in the secondary navigation.
4. Select your infeed in the list.

   The infeed placeholder is assigned the data of the selected infeed.

   The white area turns gray.

###### Result

The infeed has been added. Now continue with the configuration or parameter assignment.

> **Note**
>
> If an Active Line Module with the Chassis format is inserted, a Voltage Sensing Module is automatically added and wired.

##### Making detailed settings

During commissioning, generally the device supply voltage and, when ALMs are used, also the used line filters can be parameterized.

Following automatic commissioning, the appropriate filter for the matching Active Interface Module is preset as the line filter. If the drive line-up is set up differently, then the line filter type must be adjusted.

When it is first switched on with a new/modified network, an automatic controller setting must be implemented using the line and DC link identification routine (p3410). While the identification routine is running, it is not permissible that other loads are switched-in/switched-out.

###### Procedure

1. Select the infeed in the device view and open the inspector window.
2. Select the "Line Module details > Line Module settings" menu in the inspector window.

   The "Line Module settings" screen form is displayed in the inspector window.
3. To parameterize the device supply voltage, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Line data/operating mode" entry.

   The "Line data/operating mode" screen form opens.

   - Set the desired device supply voltage here (see "[Line data/operating mode](SINAMICS%20S-G%20infeed%20units.md#line-data-operating-mode)").
   - Make the other entries depending on the infeed type.

   If you have used a BLM or SLM as infeed, the detailed setting is completed here. However, if you are using an ALM, proceed as described here:
4. If you are using a different line filter than the preset line filter, select the desired line filter in the drop-down list (p0220[0]) with the same name.
5. If you are using an AIM line filter for booksize format, you can also activated a specified Basic Line Filter.

   In this case, activate the "Basic Line Filter booksize ..." (p0220[1]) option.

###### Result

You have made the detailed settings for the infeed of your device configuration.

#### Motor Modules

This section contains information on the following topics:

- [Adding a Motor Module](#adding-a-motor-module)
- [Changing the drive object type](#changing-the-drive-object-type)
- [Making detailed settings](#making-detailed-settings-1)

##### Adding a Motor Module

When creating a Motor Module, a certain drive object type is active by default depending on the drive unit type, either "High dynamic (servo)" or "Universal (vector)". You can change the drive object type of the module in the hardware device configuration of Startdrive. Many of the following settings depend on the set drive object type. The setting of the correct type is therefore prerequisite for all other settings during the commissioning and further parameterization of the Motor Module.

> **Note**
>
> **Modifying the device configuration for a subsequent change of the drive object type**
>
> Make sure that you set the drive object type in the device configuration first and only then add and specify the motor, measuring systems and supplementary system components.
>
> If you change the drive object type subsequently, the configuration of some components may be lost and have to be repeated.

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- An infeed has been inserted.

  In case of doubt, you can insert the infeed at a later time. However, in this case you must wire the "infeed" component manually to the other components.

###### Adding and specifying a Motor Module

You can insert a Motor Module in unspecified form via the hardware catalog.   
After adding, you can select the control type via the Motor Module. You can find additional information on selecting the control type at [Changing the drive object type](#changing-the-drive-object-type).

1. Open the "Motor Modules" entry in the hardware catalog.   
   The following Motor Modules are available for selection:

   - Single Motor Modules
   - Double Motor Modules
2. Select the required, unspecified Motor Module in the device overview.  
   Drag the unspecified Motor Module to the device view.

   The DRIVE-CLiQ connections are drawn automatically.
3. Click the Motor Module in the DRIVE-CLiQ editor. Make sure that you click in the white area of the Motor Module.
4. Open the inspector window if it is not already open or displayed.
5. Select the "Motor Module - Selection" entry in the secondary navigation of the inspector window.
6. All Motor Modules with the default drive object type are displayed in the list.   
   If you change the drive object type, you must change the display of the list.
7. To change the drive object type, select the desired control type in the "Selected drive object type" drop-down list:

   A confirmation prompt appears as to whether you really want to change the drive object type.
8. Click "Yes" to confirm the prompt.

   The Motor Module list is now refreshed. Only Motor Modules of the selected drive object type are now available for selection. In the same way, the list can be changed again.
9. Select your Motor Module in the list based on the article number.

   The data of the selected Motor Module is assigned to the unspecified Motor Module. The white area turns gray.

###### Connecting Motor Modules in parallel

> **Note**
>
> **Rules for connecting power units in parallel**
>
> In Startdrive S, power units within certain limits can be connected in parallel. When specifying modules connected in parallel, Startdrive checks whether the rules for connecting in parallel are complied with, and only allows the parallel connection to be established if all rules are complied with. If the rules do not permit a parallel connection, then the program suggests that the last module connected in parallel is removed – or in some instances, prevents the parallel connection from being configured in the first place.
>
> Detailed information about these rules is available under [Rules for parallel connection](#rules-for-connecting-power-units-in-parallel).

To connect Motor Modules in parallel with already added modules, proceed as follows:

1. Open the "Motor Modules" entry in the hardware catalog.  
   The following Motor Modules are available for selection:

   - Single Motor Modules
   - Double Motor Modules
2. Select the required, unspecified Motor Module in the device overview.
3. Drag the unspecified Motor Module to the device view in the light gray area of the existing Motor Module.
4. Click the Motor Module in the DRIVE-CLiQ editor. Make sure that you click in the white area of the Motor Module.
5. Open the inspector window if it is not already open or displayed.
6. Select your Motor Module in the list based on the article number.

   The data of the selected Motor Module is assigned to the unspecified Motor Module. The white area turns gray.

###### Adding a Double Motor Module with different control types for each drive axis

You can also configure a Double Motor Module with different control types on each axis.

> **Note**
>
> An axis can handle only one type of motor, either linear motor or rotatory motor.
>
> For example, if an axis has linear motor already added, then only linear motors can be added to the axis and vice versa.
>
> To change the type of the motor, open the Motor Module via right click and select "Change device" from the menu.

After adding the Double Motor Module, select the control type via the individual drive axis. You can find additional information on selecting the control type at [Changing the drive object type](#changing-the-drive-object-type).

To add a Double Motor Module with different control types on both drive axis, proceed as follows:

1. Open the "Motor Modules" entry in the hardware catalog.
2. Drag the unspecified Double Motor Module to the device view.

   The DRIVE-CLiQ connections are drawn automatically.
3. Click one of the drive axis of the Double Motor Module in the DRIVE-CLiQ editor. Make sure that you click on the white area of the Double Motor Module.
4. Open the inspector window if it is not already open or displayed.
5. Select the "Motor Module - Selection - DMM" entry in the secondary navigation of the inspector window.
6. All Motor Modules for the "SERVO" drive object type (default setting for first call) are displayed in the list. If you are using the "VECTOR" drive object type, you must change the display of the list.
7. If you are using drive objects of the "VECTOR" type, select the "VECTOR" option in the "Selected drive object type" drop-down list.

   A confirmation prompt appears as to whether you really want to change the drive object type.
8. Click "Yes" to confirm the prompt.

   The Motor Module list is now refreshed. Only Motor Modules of the "VECTOR" type are now available for selection. In the same way, the list can be changed back to modules of the "SERVO" type.
9. Select your Motor Module in the list based on the article number.

   The data of the selected Motor Module is assigned to the unspecified Double Motor Module. The white area turns gray.
10. Click the other drive axis of the Double Motor Module in the DRIVE-CLiQ editor.
11. Depending on in which area of the drive axis you have clicked, you can change the drive object type in different ways, see [Change drive object type](#changing-the-drive-object-type).

**Note**

**Order when creating**

You can set the drive object type of the drive axes of a Double Motor Module in any order.

###### Result

The Motor Module has been added. Now continue with the configuration or parameter assignment.

##### Changing the drive object type

The drive object type can be changed in the Power Modules drop-down list or Motor Modules drop-down list as well as in the project information of the drive axis.

###### Requirement

- A Power Module or a Motor Module is created and, if required, specified in Startdrive in the device configuration.

###### Setting the drive object type in the Motor Modules list or Power Modules list

1. If the device configuration is not active in your Startdrive project, call it via the project navigation.
2. Select the required drive axis in the device configuration.
3. Open the inspector window if it is not already open or displayed.
4. Select the "Power Module - Selection - xx" entry or "Motor Module - Selection - xxx" entry in the secondary navigation of the inspector window.

   The list of the corresponding modules opens:

   ![Setting the drive object type in the Motor Modules list or Power Modules list](images/147996555019_DV_resource.Stream@PNG-en-US.png)

   ![Setting the drive object type in the Motor Modules list or Power Modules list](images/147996555019_DV_resource.Stream@PNG-en-US.png)
5. Select the required type ("High dynamic (servo)" or "Universal (vector)") in the "Selected drive object type" drop-down list.

   A confirmation prompt appears as to whether you really want to change the drive object type.
6. Click "Yes" to confirm the prompt.

   The Motor Module drop-down list is now refreshed. Only Motor Modules of the selected type are now available for selection.
7. Save the changes in the project.

###### Setting the drive object type in the project information

1. If the device configuration is not active in your Startdrive project, call it via the project navigation.
2. Select the required drive axis in the device configuration.
3. Open the inspector window if it is not already open or displayed.
4. In the secondary navigation of the inspector window, select "General".

   ![Setting the drive object type in the project information](images/147996559115_DV_resource.Stream@PNG-en-US.png)

   ![Setting the drive object type in the project information](images/147996559115_DV_resource.Stream@PNG-en-US.png)
5. Select the required type from the "Drive object type" drop-down list (generally "Universal (vector)", because "High dynamic (servo)" is set by default via the Motor Module).

   A confirmation prompt appears as to whether you really want to change the drive object type.
6. Click "Yes" to confirm the prompt.

   The desired drive object type is set.
7. Save the changes in the project.

##### Making detailed settings

Further detail settings can be carried out in the inspector window for Motor Modules and Power Modules:

- Motor Module settings/Power Module settings

  Allows the modification of the default supply voltage.

  Displays the standard for power settings of the converter and motor.
- Motor Module additional data/Power Module additional data

  Allows filter settings for modules of the "Universal (vector)" drive object type.

The procedure for detail settings is identical for Motor Modules and Power Modules.

###### Procedure

The detailed settings are explained using a Power Module as an example.

| Symbol | Meaning |
| --- | --- |
| 1. Select the desired Power Module in the device view and open the inspector window. 2. Select the menu "Power Module Details > Power Module Settings" in the inspector window.    The default supply voltage is displayed in the screen form: 3. Enter a new supply voltage as required. 4. If you use the "Universal (vector)" drive object type, you can set further additional data.     Select the menu "Power Module Details > Power Module Additional Data" in the inspector window. 5. Select a desired filter in the "Output filter" drop-down list.       | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Damage to a sine-wave filter through incorrect parameter assignment** If a sine-wave filter is installed in your hardware configuration, the sine-wave filter can be destroyed if it is not set in the additional data of the Motor Module or Power Module.  - Set the installed sine-wave filter in the "Output filter" drop-down list and add the required parameter data of the filter. |  |     Additional display or entry fields are now shown depending on the selected filter. 6. Now parameterize the associated detailed settings for the selected filter. |  |

###### Result

You have performed the detail settings for a selected Power Module or Motor Module.

#### Power Modules

This section contains information on the following topics:

- [Adding Power Modules (Booksize, Chassis)](#adding-power-modules-booksize-chassis)
- [Adding Power Modules (Blocksize)](#adding-power-modules-blocksize)
- [Changing the drive object type](#changing-the-drive-object-type-1)
- [Making detailed settings](#making-detailed-settings-2)

##### Adding Power Modules (Booksize, Chassis)

When creating a Power Module, a certain drive object type is active by default depending on the drive unit type, either "High dynamic (servo)" or "Universal (vector)". You can change the drive object type of the module in the hardware device configuration of Startdrive. Many of the following settings depend on the set drive object type. The setting of the correct type is therefore prerequisite for all other settings during the commissioning and further parameterization of the Power Module.

> **Note**
>
> **Modifying the device configuration for a subsequent change of the drive object type**
>
> Make sure that you set the drive object type in the device configuration first and only then add and specify the motor, measuring systems and supplementary system components.
>
> If you change the drive object type subsequently, the configuration of some components may be lost and have to be repeated.

###### Requirements

- A project has been created.
- A Drive Controller Control Unit has been inserted in the device configuration.
- An infeed is optionally available.

  When you use Power Modules, it is usually possible to omit an infeed.

  In case of doubt, you can insert the infeed at a later time. However, in this case you must wire the "infeed" component manually to the other components.

###### Adding and specifying a Power Module

You can add a Power Module in unspecified form via the hardware catalog.

After adding, you can select the control type via the Power Module. You can find additional information on selecting the control type at [Changing the drive object type](#changing-the-drive-object-type-1).

1. Open the "Power Modules" entry in the hardware catalog.

   The following Power Modules are available for selection:

   - AC Power Module
   - PM 240-2
2. Select the required, unspecified Power Module in the device overview.
3. Drag the unspecified Power Module to the device view.

   The DRIVE-CLiQ connection is automatically established.
4. Click on the Power Module in the device view. Make sure that you click in the white area of the Power Module.
5. Open the inspector window if it is not already open or displayed.
6. Select the "Power Module - Selection - PM" entry in the secondary navigation of the Inspector window.

   All Power Modules with the default drive object type are displayed in the list.   
   If you change the drive object type, you must change the display of the list.
7. To change the drive object type, select the desired control type in the "Selected drive object type" drop-down list:

   A confirmation prompt appears as to whether you really want to change the drive object type.
8. Click "Yes" to confirm the prompt.

   The Power Modules list is now refreshed. Only Power Modules of the selected drive object type are now available for selection. In the same way, the list can be changed again.
9. Select your Power Module in the list based on the article number.

   The data of the selected Power Module is assigned to the unspecified Power Module. The white area turns dark gray.

###### Connecting Power Modules in parallel

> **Note**
>
> **Rules for connecting power units in parallel**
>
> In Startdrive S, power units within certain limits can be connected in parallel. When specifying modules connected in parallel, Startdrive checks whether the rules for connecting in parallel are complied with, and only allows the parallel connection to be established if all rules are complied with. If the rules do not permit a parallel connection, then the program suggests that the last module connected in parallel is removed – or in some instances, prevents the parallel connection from being configured in the first place.
>
> Detailed information about these rules is available under [Rules for parallel connection](#rules-for-connecting-power-units-in-parallel).

To connect Power Module units in parallel with modules that have already been added, proceed as follows:

1. Open the "Power Modules" entry in the hardware catalog.  
   The following Power Modules are available for selection:

   - AC Power Module
   - PM 240-2
2. Select the required, unspecified Power Module in the device overview.
3. Drag the unspecified Power Module to the device view in the light gray area of the existing module.
4. Click the Power Module in the DRIVE-CLiQ editor. Make sure that you click in the white area of the Power Module.
5. Open the inspector window if it is not already open or displayed.
6. Select your Power Module in the list based on the article number.

   The data of the selected Power Module is assigned to the unspecified Power Module. The white area turns gray.

###### Result

The Power Module has been inserted and specified.

##### Adding Power Modules (Blocksize)

###### Description

To be connected to a Control Unit, Power Modules (PM240-2) in the "Blocksize" format require a Control Unit Adapter (CUA). The CUA31 or the CUA32 can be used as adapter. Contrary to the CUA31, the CUA32 has an integrated encoder evaluation function that can be configured for HTL/TTL or SSI encoders.

> **Note**
>
> **Modifying the device configuration for a subsequent change of the drive object type**
>
> Make sure that you set the drive object type in the device configuration first and only then add and specify the motor, measuring systems and supplementary system components.
>
> If you change the drive object type subsequently, the configuration of some components may be lost and have to be repeated.

###### Requirements

- A project has been created.
- A Drive Controller Control Unit has been inserted in the device configuration.
- **No** infeed (Line Module) has been inserted in the device configuration.

###### Adding a Power Module and specifying together with Control Unit Adapters

You can add a Power Module in unspecified form via the hardware catalog.

After adding, you can select the control type via the Power Module. You can find additional information on selecting the control type at [Changing the drive object type](#changing-the-drive-object-type-1).

1. Open the "Power Modules" entry in the hardware catalog.

   The following Power Modules are available for selection:

   - AC Power Module
   - PM 240-2
2. Select the required, unspecified PM 240-2 Power Module in the device overview.
3. Drag the unspecified PM 240-2 Power Module to the device view.

   For this Power Module, the DRIVE-CLiQ connection is not automatically established with every control unit. A Control Unit Adapter is required to establish a connection to the Control Unit. There is a corresponding placeholder on the Power Module. It is linked automatically with the Control Unit after insertion via a DRIVE-CLiQ connection.
4. Click on the Power Module in the device view. Make sure that you click in the white area of the Power Module.
5. Open the inspector window if it is not already open or displayed.
6. Select the "Power Module - Selection - PM" entry in the secondary navigation of the Inspector window.

   All Power Modules in the Blocksize format with the default drive object type are displayed in the list.   
   If you change the drive object type, you must change the display of the list.
7. To change the drive object type, select the desired control type in the "Selected drive object type" drop-down list:

   A confirmation prompt appears as to whether you really want to change the drive object type.
8. Click "Yes" to confirm the prompt.

   The Power Modules list is now refreshed. Only Power Modules of the selected drive object type are now available for selection. In the same way, the list can be changed again.
9. Select your Power Module in the list based on the article number.

   The data of the selected Power Module is assigned to the unspecified Power Module. The white area turns dark gray.
10. You need the CUA to establish a connection between this Power Module and the Control Unit. A placeholder is automatically present in the Power Module.

    In the Power Module, click on the empty border of the CUA.
11. Select the "Power Module - Selection - CUA" entry in the secondary navigation of the Inspector window.   
    In the Inspector window screen form of the same name, select the desired adapter type, so either CUA31 or CUA32.

    The adapter is automatically displayed and specified.

**Note**

A Power Module cannot be used for MV drive units.

###### Result

The "Blocksize" Power Module is inserted, specified and then automatically linked with the CU using the Control Unit Adapter.

##### Changing the drive object type

The drive object type can be changed in the Power Modules drop-down list or Motor Modules drop-down list as well as in the project information of the drive axis.

###### Requirement

- A Power Module or a Motor Module is created and, if required, specified in Startdrive in the device configuration.

###### Setting the drive object type in the Motor Modules list or Power Modules list

1. If the device configuration is not active in your Startdrive project, call it via the project navigation.
2. Select the required drive axis in the device configuration.
3. Open the inspector window if it is not already open or displayed.
4. Select the "Power Module - Selection - xx" entry or "Motor Module - Selection - xxx" entry in the secondary navigation of the inspector window.

   The list of the corresponding modules opens:

   ![Setting the drive object type in the Motor Modules list or Power Modules list](images/147996555019_DV_resource.Stream@PNG-en-US.png)

   ![Setting the drive object type in the Motor Modules list or Power Modules list](images/147996555019_DV_resource.Stream@PNG-en-US.png)
5. Select the required type ("High dynamic (servo)" or "Universal (vector)") in the "Selected drive object type" drop-down list.

   A confirmation prompt appears as to whether you really want to change the drive object type.
6. Click "Yes" to confirm the prompt.

   The Motor Module drop-down list is now refreshed. Only Motor Modules of the selected type are now available for selection.
7. Save the changes in the project.

###### Setting the drive object type in the project information

1. If the device configuration is not active in your Startdrive project, call it via the project navigation.
2. Select the required drive axis in the device configuration.
3. Open the inspector window if it is not already open or displayed.
4. In the secondary navigation of the inspector window, select "General".

   ![Setting the drive object type in the project information](images/147996559115_DV_resource.Stream@PNG-en-US.png)

   ![Setting the drive object type in the project information](images/147996559115_DV_resource.Stream@PNG-en-US.png)
5. Select the required type from the "Drive object type" drop-down list (generally "Universal (vector)", because "High dynamic (servo)" is set by default via the Motor Module).

   A confirmation prompt appears as to whether you really want to change the drive object type.
6. Click "Yes" to confirm the prompt.

   The desired drive object type is set.
7. Save the changes in the project.

##### Making detailed settings

Further detail settings can be carried out in the inspector window for Motor Modules and Power Modules:

- Motor Module settings/Power Module settings

  Allows the modification of the default supply voltage.

  Displays the standard for power settings of the converter and motor.
- Motor Module additional data/Power Module additional data

  Allows filter settings for modules of the "Universal (vector)" drive object type.

The procedure for detail settings is identical for Motor Modules and Power Modules.

###### Procedure

The detailed settings are explained using a Power Module as an example.

| Symbol | Meaning |
| --- | --- |
| 1. Select the desired Power Module in the device view and open the inspector window. 2. Select the menu "Power Module Details > Power Module Settings" in the inspector window.    The default supply voltage is displayed in the screen form: 3. Enter a new supply voltage as required. 4. If you use the "Universal (vector)" drive object type, you can set further additional data.     Select the menu "Power Module Details > Power Module Additional Data" in the inspector window. 5. Select a desired filter in the "Output filter" drop-down list.       | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Damage to a sine-wave filter through incorrect parameter assignment** If a sine-wave filter is installed in your hardware configuration, the sine-wave filter can be destroyed if it is not set in the additional data of the Motor Module or Power Module.  - Set the installed sine-wave filter in the "Output filter" drop-down list and add the required parameter data of the filter. |  |     Additional display or entry fields are now shown depending on the selected filter. 6. Now parameterize the associated detailed settings for the selected filter. |  |

###### Result

You have performed the detail settings for a selected Power Module or Motor Module.

#### Motors

This section contains information on the following topics:

- [Inserting and specifying motors from the motor list](#inserting-and-specifying-motors-from-the-motor-list)
- [Inserting and specifying motors that are missing from the motor list](#inserting-and-specifying-motors-that-are-missing-from-the-motor-list)
- [Making detailed settings](#making-detailed-settings-3)

##### Inserting and specifying motors from the motor list

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- A Motor Module or a Power Module has been inserted.
- An infeed has been inserted.

  In case of doubt, you can insert the infeed at a later time. However, in this case you must wire the "infeed" component manually to the other components.
- An encoder has been inserted (optional).

###### Adding a motor and selecting the motor data

You can insert motors in unspecified form via the hardware catalog.

The motors can be inserted by using the following ways:

- Drag and drop
- Double click
- Copy and paste

**Adding the motor by drag and drop**

1. Open the "Motors" entry in the hardware catalog. The following entries are displayed:

   - DRIVE-CLiQ motors
   - Induction motors
   - Synchronous motors
   - Reluctance motors
2. Drag the unspecified motor to the lower area of the Motor Module.

   The placeholder for the unspecified motor is added.
3. Click the unspecified motor in the DRIVE-CLiQ editor.
4. If required, select the "Motor - Selection" entry in the secondary navigation in the inspector window.
5. Select your motor in the list based on the article number.

   The motor placeholder is assigned the data of the selected motor. The white area turns gray. If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

**Adding the motor by double clicking**

1. Open the "Motors" entry in the hardware catalog.
2. Select the unspecified motor that you want to add and double click on it.

   The new motor will be added in the device view.

**Adding the motor by performing copy and paste**

1. Open the "Motors" entry in the hardware catalogue.
2. Select and right click on the unspecified motor that you want to add and click on "Copy".
3. In the "Device view", select and right click on the drive and click on "Paste".

###### Result

The motor has been added. If you have selected a motor without encoder, add an encoder and an encoder evaluation in the next step.

##### Inserting and specifying motors that are missing from the motor list

Startdrive manages the motor data of numerous standard motors. Motors can therefore be quickly specified via the inspector window. If you want to manage the motors in your device configuration that are not contained in the motor list, you can acquire the most important motor data, such as the rating plate values of the motor, manually in the inspector window. Mandatory input fields are marked in pink.

###### Inserting and specifying a motor

You can insert motors in unspecified form via the hardware catalog.

1. Open the "Motors" entry in the hardware catalog and then the "Motor data input" subentry.

   The motors are presorted according to motor type. A range of induction motors, synchronous motors and reluctance motors are available for a general selection.
2. Select the unspecified motor in the device overview.
3. Drag the unspecified motor to the lower area of the Motor Module.
4. Click the unspecified motor in the device view.
5. Open the inspector window if it is not already open or displayed.
6. Select the "Motor details" entry in the secondary navigation of the inspector window.

   The "Motor details" input screen form has the subareas:

   - Rating plate values
   - Optional motor data (can also be activated)
   - Equivalent circuit diagram data (can also be activated)

     If this screen form is not activated, then the corresponding equivalent circuit diagram data are automatically calculated. If the screen form is activated, then all of the fields shown in pink must be populated.
   - Motor brake (see "[Detailed settings...](#making-detailed-settings-3)")
7. If you also want to acquire the optional motor data and circuit diagram data, activate the "Activate the display of the ..." options in the "Rating plate values" screen form.

   The additionally activated subareas are displayed in the secondary navigation under "Motor details".

   ![Inserting and specifying a motor](images/147996811403_DV_resource.Stream@PNG-en-US.png)

   ![Inserting and specifying a motor](images/147996811403_DV_resource.Stream@PNG-en-US.png)
8. Acquire the required motor data of the inserted motor.

   The input fields marked in pink are mandatory input fields. Without the appropriate values in these fields, the device configuration cannot be completed.

###### Result

The motor is specified with the manually acquired motor data. The white area turns dark gray.

If you have selected a motor with encoder, the encoder and the encoder evaluation are also added automatically.

##### Making detailed settings

You can configure the following motor details for motors during commissioning:

- Basic parameterization
- Rating plate values
- Motor brake
- Optional motor data (can also be activated)
- Equivalent circuit diagram data (can also be activated)

###### Procedure

1. Select the motor in the device view and open the inspector window.
2. Select the "Motor details > Rating plate values" menu in the inspector window.

   The "Rating plate values" screen form is displayed in the inspector window.
3. To perform the basic parameterization for the motor, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Basic parameterization" entry.

   The function view of the drive axis opens:

   Make the required settings here (see "[Basic parameterization](Servo%20drives%20%28highly%20dynamic%29.md#basic-parameter-assignment)").
4. Select the "Motor details > Rating plate values" menu again in the inspector window.
5. If you also want to acquire the optional motor data and circuit diagram data, activate the "Activate the display of the ..." options in the "Rating plate values" screen form.

   The additionally activated subareas are displayed in the secondary navigation under "Motor details".
6. Make the required settings in the white fields of the screen forms "Rating plate values", "Optional motor data" and "Equivalent circuit diagram data".

   The gray fields are refreshed automatically in accordance with their setting.
7. Select the "Motor brake" menu in the Inspector window.

   The current configuration of the motor holding brake is displayed in the screen form. You can only change this configuration in the brake control.
8. To change the configuration of the motor holding brake, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Brake control" entry.

   The "Brake control" screen form opens.
9. Here, you can select the required brake control in the "Configuration" drop-down list and make the detailed settings (see "[Brake control](Servo%20drives%20%28highly%20dynamic%29.md#brake-control)").

   The selected brake control is displayed in the motor details.

**Note**

**For 1FN1 linear motors**

You can select “Enable extended motor brake” check box to activate extended motor brake in the drive object function module.

###### Result

You have made the detailed settings for the selected motor in your device configuration.

#### Measuring systems

This section contains information on the following topics:

- [Adding an encoder](#adding-an-encoder)
- [Making detailed settings](#making-detailed-settings-4)
- [Specifying the encoder evaluation](#specifying-the-encoder-evaluation)
- [Encoder and Sensor Modules](#encoder-and-sensor-modules)

##### Adding an encoder

###### Fundamentals

A distinction is made between motor encoders and machine encoders.

- Motor encoders are attached to the motor shaft so that the movement of the motor (angle of rotation, rotor position, etc.) can be measured directly. Motor encoders provide the actual speed value for the closed-loop control (speed and current control) so that the actual speed value is supplied fast enough for fast controllers. Consequently, high-quality encoders should be deployed as motor encoders.

  - Preconfigured Siemens motors have already been created with the appropriate encoder and the encoder evaluation in the device view.
  - DRIVE-CLiQ motors are added together with an encoder. When you download the configuration to the drive, the drive and encoder parameters are transferred. The correct motor and encoder configuration is available offline in the project after an upload.
  - If you use measuring systems that are not listed in the hardware catalog, you must enter the parameters manually.

  The encoders configured in this way are then intended as motor encoders (measuring system 1).

  ![Motor encoder](images/147996858635_DV_resource.Stream@PNG-en-US.png)

  Motor encoder
- Machine encoders are installed in the machine. With machine encoders, for example, you synchronize the speed of one belt with another belt or determine the position of a workpiece. Because these values do not normally need to be present in the fast speed- or current-controller cycle, even basic mounted encoders can be used.

  ![Machine encoder](images/147996862603_DV_resource.Stream@PNG-en-US.png)

  Machine encoder

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- An infeed has been inserted.

  In case of doubt, you can insert the infeed at a later time. However, in this case you must wire the "infeed" component manually to the other components.
- A Motor Module has been inserted.
- A motor has been inserted (optional).

###### Inserting an encoder manually and assigning encoder data

You insert an encoder first as placeholder in the device view via the hardware catalog.

1. Open the "Measuring systems" entry in the hardware catalog. The following entries are displayed:

   - "DRIVE-CLiQ encoder"
   - "SIN/COS encoder"
   - "SSI encoder"
   - "SIN/COS+SSI encoder"
   - "HTL/TTL encoder"
   - "HTL/TTL+SSI encoder"
   - "EnDat + SIN/COS encoder"
   - "Resolver encoder"
2. Drag the unspecified encoder to the lower area of the Motor Module. An encoder and a Sensor Module are created.
3. Click the unspecified encoder in the DRIVE-CLiQ editor.
4. In the secondary navigation of the inspector window, select the "Measuring system - Selection..." entry.
5. Select the desired encoder in the measuring system list based on the article number.

   The data of the selected encoder is assigned to the encoder placeholder. The white area turns gray.

   A Sensor Module (encoder evaluation) is also inserted. If only one Sensor Module is available for this encoder type, it is already inserted specified. Otherwise you must also specify the Sensor Module.

###### Result

The encoder has been inserted and specified.

###### Handling DRIVE-CLiQ encoders

The process is slightly different from the standard procedure for DRIVE-CLiQ encoders. Two different versions are possible:

- If DRIVE-CLiQ motors are included in the device view, DRIVE-CLiQ encoders are added automatically. Motor and encoder **cannot** be specified in Startdrive in this case. The project data is downloaded to the drive instead, and the motor and encoder detail data is then read from the hardware.
- If non-DRIVE-CLiQ motors are used in the device view, you can still add DRIVE-CLiQ encoders later. The DRIVE-CLiQ encoders can be specified in Startdrive in this case.

###### Adding further encoders

If you require further encoders for your task, configure them in the same manner. These encoders are then normally used as machine encoder.

##### Making detailed settings

You can configure the following encoder details for measuring systems during commissioning:

- Actual value processing
- Encoder details such as encoder type, incremental track, gear ratio, etc.

###### Procedure

1. Select the encoder in the device view and open the inspector window.
2. Select the "Measuring system details" menu in the inspector window.
3. To configure the actual value processing, click the ![Procedure](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon next to the "Actual value processing" entry.

   The "Actual value processing" screen form opens in the function view.

   Make the required settings here (see "[Basic parameterization](Servo%20drives%20%28highly%20dynamic%29.md#actual-value-processing-servo)").
4. Select the "Measuring system details" menu again in the inspector window.

   The setting options depend on the selected encoder type.
5. Make the required detailed settings of the encoder in the white fields.

   The gray fields are corrected automatically in accordance with their setting.

###### Result

You have made the detailed settings for the selected encoder in your device configuration.

##### Specifying the encoder evaluation

###### Requirements

- An encoder has been specified.
- The unspecified encoder evaluation is displayed.

###### Specifying the encoder evaluation

Various Sensor Modules are available for the encoder evaluation. Different types are offered for selection depending on the encoder.

1. Click the unspecified encoder evaluation. The available Sensor Modules are displayed.
2. Select your Sensor Module.

###### Result

The Sensor Module has been specified.

##### Encoder and Sensor Modules

This section contains information on the following topics:

- [Encoder system connection](#encoder-system-connection)
- [Encoder descriptions](#encoder-descriptions)

###### Encoder system connection

###### Description

The Sensor Modules evaluate the signals from the connected motor encoders or external encoders and convert the signals so that they can be evaluated by the Control Unit. The encoder system can only be connected to SINAMICS via DRIVE-CLiQ. The following rule applies: Motor encoders are connected to the associated Motor Module, external encoders are connected to the Control Unit. In conjunction with motor encoders, the motor temperature can also be evaluated using Sensor Modules.

Sensor Modules Cabinet (SMC) are intended for internal cabinet installation.

**Assignment of measuring system to Sensor Modules**

|  | SMC |  |  |  | SME |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Measuring systems | SMC10 | SMC20 | SMC30 | SMC40<sup>2)</sup> | SME20 | SME25 | SME120 | SME125 |
| Resolver | Yes | - | - | - | - | - | - | - |
| Sin/Cos incremental encoder (1 Vpp)  with zero pulse | - | Yes | - | - | Yes | - | Yes | - |
| TTL/HTL incremental encoder | - | - | Yes | - | - | - | - | - |
| EnDat + SIN/COS encoder  (with incremental track 1 Vpp) | - | Yes | - | - | - | Yes | - | Yes |
| SSI absolute encoder <sup>1)</sup> (with incremental tracks sin/cos 1 Vpp) | - | Yes | - | - | - | Yes | - | Yes |
| Temperature evaluation | Yes | Yes | Yes | - | - | - | Yes<sup>3)</sup> | Yes<sup>3)</sup> |
| <sup>1)</sup> Only as of article number 6SL3055-0AA00-5CA1   <sup>2)</sup> For direct measuring systems only   <sup>3)</sup> Reliable electrical separation |  |  |  |  |  |  |  |  |

###### SMC10 and SMC20

**SMC10**

The Sensor Module Cabinet-Mounted 10 (SMC10) evaluates encoder signals and transmits the speed, actual position value, rotor position and the home position via DRIVE-CLiQ to the Control Unit.

The SMC10 evaluates the following encoder signals:

- 2-pole resolver
- Multi-pole resolver (with same number of pole pairs as motor)

**SMC20**

The Sensor Module Cabinet-Mounted 20 (SMC20) evaluates encoder signals and transmits the speed, actual position value, rotor position and the home position via DRIVE-CLiQ to the Control Unit.

The encoders that can be connected are incremental encoders SIN/COS (1 Vpp) and absolute encoders EnDat/SSI with SIN/COS (1 Vpp).

Interface description:

![SMC10 and SMC20 representation](images/147996939531_DV_resource.Stream@PNG-en-US.png)

SMC10 and SMC20 representation

###### SMC30

The Sensor Module Cabinet-Mounted 30 (SMC30) evaluates encoder signals and transmits the speed, actual position value, rotor position and the home position via DRIVE-CLiQ to the Control Unit.

The connectable encoders are TTL/HTL rectangular encoders and SSI absolute encoders.

Interface description:

![SMC30 representation](images/147996962571_DV_resource.Stream@PNG-en-US.png)

SMC30 representation

###### SMC40

The Sensor Module Cabinet-Mounted SMC40 is used to convert encoder signals from EnDat absolute encoders without incremental tracks (order designation EnDat encoder) to DRIVE-CLiQ and send these to the Control Unit. Two encoder systems with EnDat encoder can be connected to the SMC40. Their signals are converted independently of each other to two DRIVE-CLiQ encoder signals.

![SMC40](images/147997006091_DV_resource.Stream@PNG-en-US.png)

SMC40

****Temperature sensor information****

The SMC 40 has no separate input for a temperature sensor. The temperature information of an external temperature sensor connected to the EnDat measuring system, however, is transmitted by SMC 40 via the DRIVE-CLiQ interface and interpreted as a motor temperature. The internal temperature information of an EnDat measuring system is not transmitted.

![SMC40 - Temperature sensor](images/160568238475_DV_resource.Stream@PNG-en-US.png)

SMC40 - Temperature sensor

The wiring diagram shows two different applications of the SMC40. For each conversion of an EnDat encoder signal into a DRIVE-CLiQ signal, a dedicated DRIVE-CLiQ cable must be used, as the electronics in the SMC40 is designed so that each channel is independent. The DRIVE-CLiQ cables cannot be interchanged.

The SMC40 supports the connection of different series of measuring systems (with or without functional safety) to the DRIVE-CLiQ interface. Only measuring systems with order designation EnDat encoder are supported.

###### SME20 and SME25

**SME20**

Measuring systems outside the cabinet can be connected directly to the Sensor Module External 20 (SME20). The SME20 evaluates these measuring systems and converts the signals to DRIVE-CLiQ. Incremental SIN/COS (1 Vpp) measuring systems can be connected.

**SME25**

Measuring systems outside the cabinet can be connected directly to the Sensor Module External 25 (SME25). The SME20 evaluates these measuring systems and converts the signals to DRIVE-CLiQ. Absolute measuring systems with incremental tracks (1 Vpp) and EnDat/SSI can be connected.

![SME20 and SME25 representation](images/147996972043_DV_resource.Stream@PNG-en-US.png)

SME20 and SME25 representation

###### SME120 and SME125

**SME120**

Measuring systems outside the cabinet can be connected directly to the Sensor Module External 120 (SME120). The SME120 evaluates these measuring systems and converts the signals to DRIVE-CLiQ. The component is always used when the temperature signals of the motors are not reliably electrically separated. To determine the commutator position of the linear motor, a Hall-effect sensor box can be connected. The SME120 is used, in particular, in linear motor applications. Incremental SIN/COS (1 Vpp) measuring systems can be connected.

**SME125**

Measuring systems outside the cabinet can be connected directly to the Sensor Module External 125 (SME125). The SME125 evaluates these measuring systems and converts the calculated values to DRIVE-CLiQ. The component is always used when the temperature signals of the motors are not reliably electrically separated. The SME125 is used, in particular, in linear motor applications. Absolute measuring systems with incremental tracks (1 Vpp) and EnDat/SSI can be connected.

![SME120 and SME125 representation](images/147996983051_DV_resource.Stream@PNG-en-US.png)

SME120 and SME125 representation

###### Encoder descriptions

This section contains information on the following topics:

- [Encoder – overview](#encoder-overview)
- [SIN/COS incremental encoders](#sincos-incremental-encoders)
- [SSI encoder](#ssi-encoder)
- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [EnDat + SIN/COS encoder](#endat-sincos-encoder)
- [Resolver](#resolver)
- [Distance-coded Zero Marks](#distance-coded-zero-marks)

###### Encoder – overview

###### Available measuring systems (encoders)

The following encoder types are supported in Startdrive:

- DRIVE-CLiQ encoders; these encoders are parameterized when downloading – and are correctly displayed after an upload.
- [SIN/COS encoders](#sincos-incremental-encoders); incremental encoders that supply a sine/cosine-type signal.
- [HTL/TTL encoders](#ttlhtl-incremental-encoder); incremental encoders that supply a sine/cosine-type signal; are also available with the SSI protocol.
- [EnDat + SIN/COS encoder](#endat-sincos-encoder); absolute encoder, which is controlled using the EnDat + SIN/COS encoder protocol.
- [SSI encoders](#ssi-encoder); absolute encoder, which is controlled using the SSI protocol.
- [Resolvers](#resolver); rotary encoders.

> **Note**
>
> **Encoders from the hardware catalog**
>
> All encoders, which are listed in the hardware catalog, no longer have to be parameterized as they are already preassigned the appropriate settings.
>
> Parameters must be entered for user-defined encoders (third-party encoders) as described below.

###### SIN/COS incremental encoders

###### Description

Incremental encoders operate on the principle of optoelectronic scanning of dividing discs with the transmitted-light method. The light source is a light emitting diode (LED). The light-dark modulation generated as the encoder shaft rotates is picked up by photoelectronic elements. With an appropriate arrangement of the line pattern on the dividing disk connected to the shaft and the fixed aperture, the photoelectronic elements provide two trace signals A and B at 90° to one another, as well as a reference signal R. The encoder electronics amplify these signals and convert them to sin/cos 1 Vpp.

**Absolute position**

After a machine is switched on, a reference point approach must be carried out to determine the absolute position.

**Sine/cosine encoder mode of operation**

![Sin/cos incremental encoders](images/147997103755_DV_resource.Stream@PNG-en-US.png)

Sin/cos incremental encoders

**Sin/Cos encoder type**

The following general parameters can be selected for the "Sin/Cos" encoder type:

- Motor encoder  
  This option is selected for each encoder inserted first (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- Rotary  
  Required for rotary encoder.
- Linear  
  Is required for a linear scale.

**Incremental tracks**

This field is already preassigned for most encoders. The number of pulses per revolution can also be specified in bits in the encoder data sheets. Encoder pulse number = 2<sup>resolution</sup>. The resolution is contained in the bit.

Enter the number of pulses per revolution for your encoder.

**Coarse synchronization**

You use coarse synchronization to define how the pole position identification is to be carried out. The following options are available:

- Track C/D  
  The flux position can be determined using the C/D track and the zero mark, which is adjusted to the magnetic position of the rotor. As the C/D track only has one encoder pulse per mechanical revolution, the accuracy of this determination method is only adequate for starting. Therefore, you must carry out another fine synchronization.
- Hall sensor (only for linear motors)  
  Hall sensors are used that measure the magnetic flux in the air gap. Two sensors are used, which supply information equivalent to a C/D track.
- None

**Zero marks**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- Equidistant zero marks (evaluate several zero marks):

  - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".
  - At "Number of zero marks", enter how many zero marks you want to evaluate.
- Irregular zero marks:   
  Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible.
- [Distance-coded zero marks](#distance-coded-zero-marks)

**Gear ratio/measuring gearbox**

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20SERVO.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20SERVO.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

###### Additional parameters

---

---

**See also**

[Rotor position synchronization (servo)](Servo%20drives%20%28highly%20dynamic%29.md#rotor-position-synchronization-servo-1)

###### SSI encoder

###### SSI encoder

SSI encoders use the SSI protocol for the data transfer. The SSI protocol is a serial data transfer between an encoder and an evaluation module.

> **Note**
>
> **Data sheet of the encoder being used**
>
> To parameterize the SSI protocol, it is absolutely necessary that you have the encoder data sheet at hand. Use the information in the data sheet to set the protocol parameters. Not all encoders support the parameterizable functions.

**Encoder type SSI**

The following main settings can be made for the "SSI" encoder type:

- Motor encoder  
  This option is selected for each encoder inserted first (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- Rotary  
  Select this option when a rotary encoder is available.
- Linear  
  Select this option when a linear scale is available.

**Power supply**

The following settings are available for setting the power supply of your encoder:

- 5 V
- 24 V
- Remote sense;   
  Remote sensing ensures that a possible voltage drop along the cable is compensated.

###### Absolute SSI protocol

**Multiturn**

Select in the drop-down list whether your encoder is multiturn-conform:

**Singleturn resolution ([p0423](SINAMICS%20Parameter%20SERVO.md#p04230n-absolute-encoder-rotary-singleturn-resolution))**

Singleturn encoders divide one rotation (360 degrees mechanical) into a specific number of encoder pulses, e.g. 8192. A unique code word is assigned to each position. After 360° the position values are repeated.

Enter the singleturn resolution based on your encoder data sheet.

**Multiturn resolution ([p0421](SINAMICS%20Parameter%20SERVO.md#p04210n-absolute-encoder-rotary-multiturn-resolution))**

Multiturn encoders also record the number of revolutions, in addition to the absolute position within one revolution. To do this, further code disks which are coupled via gear steps with the encoder shaft are scanned. When evaluating 12 additional tracks, this means that an additional 4096 revolutions can be coded.

Enter the multiturn resolution based on your encoder data sheet.

###### SSI protocol structure

The SSI connection between the encoder and the encoder module is established using four wires. This is a serial transmission.

The data transmission with the SSI protocol is performed in just one direction, i.e. the data is transferred from the encoder to the evaluation module. The data is a position value for a rotary or linear measuring system and, possibly, further bits that describe the position value.

The structure of the telegram differs depending on the encoder manufacturer and the measuring system. Consequently, you must use the information provided by the manufacturer that describes the protocol structure in detail. Manufacturers frequently extend the position value and leading and trailing zero bits to produce a telegram length of 13, 21 or 25 bits. Whereby this information is extended to 9 bits for a telegram of 21 bits or to 12 bits for a telegram of 25 bits. In the meantime, however, any telegram length is common. In the following example, 29-bit position data is transferred and expanded with three bits before and after the position.

| Bits before the position |  |  | Position bits |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Bits after the position |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x | x | x | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | x | x | x |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| P indicates the position bits; x indicates the possible position of fault, alarm and parity bits. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

###### Parameters that can be set for the SSI protocol

**Code ([p0429](SINAMICS%20Parameter%20SERVO.md#p04290n-encoder-ssi-configuration))**

1. Here, select which code versions your encoder supports:

   - Gray code; special coding of transfer signals; when transitioning from one position to another, only one bit is always changed.
   - Binary code; binary-coded transfer signals

**Baud rate ([p0427](SINAMICS%20Parameter%20SERVO.md#p04270n-encoder-ssi-baud-rate))**

1. Here, enter the baud rate for the SSI encoder.

   When setting the baud rate, also take into account the update rate of the speed or actual position value. All bits must be transferred within the cycle, as otherwise the data transfer is too slow and only performed every xth cycle. If you are using an SSI encoder with incremental track, the incremental track is used for the speed control.

   **Example**: For a baud rate of 100 kHz and an SSI length of 35 bits, 10x35 µs = 350 µs + 30 µs monoflop time = 380 µs are required to transfer the SSI value. If the current controller cycle is faster, you must set a higher baud rate.

   The possible baud rate depends on the cable length (see the diagram).

   ![Parameters that can be set for the SSI protocol](images/147997211659_DV_resource.Stream@PNG-en-US.png)

**Parameterizing the protocol**

For the protocol, define the "Position length", "Bit before position" and "Bit after position" parameters:

1. Enter a value for the "Position length in bits" ([p0447](SINAMICS%20Parameter%20SERVO.md#p04470n-encoder-ssi-number-of-bits-absolute-value)). Refer to the encoder data sheet to identify which value is suitable for your encoder. For a singleturn encoder, for example, 13 bits are used for the position information, and 25 bits for a multiturn encoder (this contains 13 bits of singleturn information).

   Also observe the count direction for the position bit. For the examples shown here, the protocols start with "0" (ascending from left to right). However, there are also manufacturers who have defined a different way of counting, starting from the MSB, counting downward from left to right. Therefore, compare the setting with the data in the encoder data sheet.
2. Enter a value for the "Bits before the position" ([p0446](SINAMICS%20Parameter%20SERVO.md#p04460n-encoder-ssi-number-of-bits-before-the-absolute-value)); see the diagram above.
3. Enter a value for the "Bits after the position" ([p0448](SINAMICS%20Parameter%20SERVO.md#p04480n-encoder-ssi-number-of-bits-after-the-absolute-value)); see the diagram above.

###### Bit functions in the SSI protocol

If alarm bits, error bits or parity bits signal errors when transferring data, in Startdrive, alarms or faults are output in the Inspector window.

**Alarm bit – only if the encoder supports it**

If the encoder manufacturer has added alarm bits to the position value, you should certainly evaluate these because they provide the only possibility to output alarms regarding the position value. For example, the encoder may be soiled.

The alarm bit triggers an alarm on the SINAMICS device (A3x412, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", activate the alarm bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the alarm bit should be output. High active means that the corresponding alarm is displayed on the SINAMICS when the bit is set.

**Error bits – only if the encoder supports it**

If the encoder manufacturer has added error bits to the position value, you must also evaluate them because they allow you to determine the validity of the position value.

Error bits trigger a fault on the SINAMICS device (F3x112, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", select the bit number for the error bit. You can parameterize several error bits (see online help for parameters)
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the error bit should be output. High active means that the corresponding fault is displayed on the SINAMICS when the bit is set.

**Parity bit – only if the encoder supports it**

Another possibility to validate the transmission is to transfer a parity bit in the telegram. This is a parity check for all of the bits of the telegram content. The following settings apply for the parity: even (= low level) and odd (= high level). Refer to the data sheet to see whether the encoder uses "even" or "odd" as checking criterion for the parity bit.

Example for "even" parity:

The number of bits filled with 1 in the telegram must always be even. An odd number of set bits is compensated by the parity bit. If an uneven number of set bits is nevertheless determined in the evaluation module, a fault is output on the SINAMICS side (F3x110 Bit 11, with x=1,2,3 for encoder 1, 2, 3).

For "uneven" parity, the inverse logic applies accordingly.

1. At "Bit activation", select the bit number for the parity bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. Under "Logic state", select whether the parity bit has even or odd logic.

**Example telegram**

![SSI encoder example telegram](images/147997164043_DV_resource.Stream@PNG-en-US.png)

SSI encoder example telegram

**Monoflop time**

The monoflop time describes the minimum wait time between two transfers of the absolute value for the SSI encoder. The set value must be greater than or equal to the value specified in the data sheet for the encoder.

1. Enter the monoflop time.

**Transfer the position value twice – only if the encoder supports it**

Some manufacturers allow a position value to be transferred twice; this is called "ring shift" or "fetch doubled". It detects transmission errors, although it extends the time taken to transfer the position value. At least one fill bit is necessary between reading out the first time and second time. You can also refer to the encoder data sheet for the number of fill bits. The following example shows the use of fill bits:

1. Select "Double transfer" and enter a value for the fill bits ([p0449](SINAMICS%20Parameter%20SERVO.md#p04490n-encoder-ssi-number-of-bits-filler-bits)).

   ![SSI encoder position value](images/147997175051_DV_resource.Stream@PNG-en-US.png)

   SSI encoder position value

###### Gear ratio/measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20SERVO.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20SERVO.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

###### Additional parameters

---

###### TTL/HTL incremental encoder

###### Description

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

**TTL/HTL encoder mode of operation.**

![TTL pulse encoder](images/147997394315_DV_resource.Stream@PNG-en-US.png)

TTL pulse encoder

After the signal edges of tracks A and B have been evaluated, direction-dependent speed and position information is available.

**Absolute position**

After switching on the machine, the absolute dimensional reference for the machine zero must be established with pulse encoders for positioning. Therefore, perform a homing procedure. After homing, the absolute position is determined by adding up the individual incremental signals.

**HTL/TTL encoder type**

The following main settings can be made for the "HTL/TTL" encoder type:

- Motor encoder  
  This option is selected for each encoder inserted first (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- Rotary  
  Required for rotary encoder.
- Linear  
  Is required for a linear scale.

**Power supply**

The following settings are available for setting the power supply of your encoder:

- 5 V
- 24 V
- Remote sense;   
  Remote sensing ensures that a possible voltage drop along the cable is compensated.

**Incremental tracks**

The resolution of the encoder is determined by its "number of pulses". This value is located on the encoder rating plate and in the associated data sheet.

- Pulse number/rotation  
  Enter the pulse number for the encoder.
- Level  
  Select whether you use an HTL (High Threshold Logic) or a TTL (Transistor-Transistor Logic) encoder.
- Signal  
  Select whether the encoder transfers a unipolar (ground-based) or a bipolar (differential) signal. Unipolar signals lie in the range of 0 ... 5 V. Bipolar signals lie in the range of -5 ... 5 V.
- Track monitoring  
  Activate this option if you want to monitor the incremental track. This can be used, for example, to monitor for wire break. If the track monitoring is selected, the signal must not be unipolar.

**Zero marks ([p0404](SINAMICS%20Parameter%20SERVO.md#p04040n-encoder-configuration-effective))**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- Equidistant zero marks (evaluate several zero marks)

  - The number of pulses between the two equidistant zero marks are displayed at "Zero mark distance".
  - At "Number of zero marks", enter how many zero marks you want to evaluate.
- Irregular zero marks

  Select this option if you do not want to evaluate the zero marks at each revolution, i.e. you want to evaluate them irregularly.
- [Distance-coded zero marks](#distance-coded-zero-marks)

**Gear ratio/measuring gearbox**

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20SERVO.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20SERVO.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

###### Additional parameters

---

---

**See also**

[SSI encoder](#ssi-encoder)
  
[Distance-coded Zero Marks](#distance-coded-zero-marks)

###### EnDat + SIN/COS encoder

###### Description

Absolute encoders (absolute shaft encoders) are designed on the same scanning principle as incremental encoders, but have a greater number of tracks. For example, if there are 13 tracks, then 2<sup>13</sup> = 8192 steps are coded for singleturn encoders. The code used is a one-step code (Gray code) which prevents any scanning errors from occurring. After switching on the machine, the position value is transferred immediately to the evaluation module. Data is transferred between the encoder and the evaluation module via EnDat.

A reference point approach is omitted, but an absolute encoder adjustment must be performed during the first commissioning with a higher-level controller or EPOS.

![EnDat absolute encoder](images/147997479691_DV_resource.Stream@PNG-en-US.png)

EnDat absolute encoder

**Identify encoder**

Select the option if you want to fetch the encoder configuration from the encoder (only online).

**Incremental tracks**

The parameters for the number of pulses/revolution are transferred over the course of the encoder identification.

**Gear ratio/measuring gearbox**

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20SERVO.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20SERVO.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

###### Additional parameters

---

###### Resolver

###### Description

Resolvers are rotary encoders that supply an absolute signal within a pole pitch. Therefore, resolvers do not have to be homed.

In principle, a resolver is made up of two components:

- Two stator windings offset by 90°
- One rotor

With the aid of an excitation voltage (typically 8 kHz), two tracks offset by 90° are generated according to the transformer principle, with an amplitude that depends upon the rotor position. The evaluation of the signals that are still modulated with the excitation frequency is done in the SMx10, which means that the speed, actual position value, rotor position and reference point are available.

![Resolver](images/147997564683_DV_resource.Stream@PNG-en-US.png)

Resolver

> **Note**
>
> When a multi-pole resolver is used, the number of resolver poles matches the number of motor poles.

**Encoder type Resolver**

The following general parameters can be selected for the resolver encoder type:

- Motor encoder  
  This option is selected for each encoder inserted first (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- Rotary  
  This option is preselected for resolvers.

**Enter the number of pole pairs ([p0408](SINAMICS%20Parameter%20SERVO.md#p04080n-rotary-encoder-pulse-number))**

Enter the number of pole pairs that the associated encoder provides.

**Gear ratio/measuring gearbox**

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20SERVO.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20SERVO.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

###### Additional parameters

---

###### Distance-coded Zero Marks

###### Description

Distance-coded measuring systems are the system of choice where travel to a (possibly distant) reference point is not possible for mechanical reasons. The absolute position can be calculated as soon as two zero marks have been crossed.

The principle of distance coding is based on differing distances between zero marks, which change in a defined manner (see figure below).

- After measurement has been switched on, the axis is in a non-homed state. An absolute position is NOT available.
- The absolute position can be calculated by traveling over at least two adjacent zero marks.
- The distance traveled is relatively small in this method and is defined by the distance between the zero marks.

The distance-coded zero marks are evaluated:

- after measurement has been switched on and the travel movement described has been completed to determine the machine position
- cyclically to compare and monitor the incremental zero marks against the distance-coded zero marks.

The following figure illustrates the distance-coded zero marks for a linear traversing motion.

![Linear traversing motion with distance-coded zero mark](images/147997624715_DV_resource.Stream@PNG-en-US.png)

Linear traversing motion with distance-coded zero mark

The following figure illustrates the distance-coded zero marks for a rotary motion.

![Rotary traversing motion with distance-coded zero mark](images/147997635595_DV_resource.Stream@PNG-en-US.png)

Rotary traversing motion with distance-coded zero mark

###### Additional parameters

- [p0404](SINAMICS%20Parameter%20SERVO.md#p04040n-encoder-configuration-effective).14
- [p0424](SINAMICS%20Parameter%20SERVO.md#p04240n-encoder-linear-zero-mark-distance)
- [p0425](SINAMICS%20Parameter%20SERVO.md#p04250n-encoder-rotary-zero-mark-distance)
- [p0426](SINAMICS%20Parameter%20SERVO.md#p04260n-encoder-zero-mark-differential-distance)

---

#### Supplementary system components

This section contains information on the following topics:

- [DRIVE-CLiQ Hub Modules](#drive-cliq-hub-modules)
- [Terminal Boards](#terminal-boards)
- [Terminal Modules](#terminal-modules)
- [Voltage Sensing Modules](#voltage-sensing-modules)

##### DRIVE-CLiQ Hub Modules

This section contains information on the following topics:

- [Adding DRIVE-CLiQ Hub Modules](#adding-drive-cliq-hub-modules)

###### Adding DRIVE-CLiQ Hub Modules

###### Description

SINAMICS uses so-called DRIVE-CLiQ Hub Modules to expand/duplicate DRIVE-CLiQ sockets. The following Hub Modules (star couplers) are available to you in SINAMICS:

- DMC20 (DRIVE-CLiQ Hub Module Cabinet)

  Expansion module for snapping on to a standard mounting rail according to EN 60715. It is used for star-shaped distribution of a DRIVE-CLiQ line. With DMC20, an axis group can be expanded by 5 DRIVE-CLiQ sockets for additional partial groups.
- DME20 (DRIVE-CLiQ Hub Module External)

  Expansion module for star-shaped distribution of a DRIVE-CLiQ line. With DME20, an axis group can be expanded by 5 DRIVE-CLiQ sockets for additional partial groups. The DME20 has IP67 degree of protection and is particularly suitable for applications that require it to be possible for DRIVE-CLiQ devices to be removed in groups without interrupting the DRIVE-CLiQ line and thus interrupting data exchange.

The common name "DRIVE-CLiQ-Hub Module DMx20" is used for these two Hub Modules in Startdrive.

> **Note**
>
> **Detailed information in manual**
>
> You can find detailed information on the Hub Modules mentioned in the "Control Units and additional system components" manual.
>
> - During commissioning, observe also the safety instructions given in the "Hub Modules" section in this manual.

###### Requirements

- A project has been created.
- An S120 Control Unit (or a SIMATIC Drive Controller) has been inserted in the device configuration.

###### Procedure

You add a DRIVE-CLiQ Hub Module via the hardware catalog.

1. Open the "DRIVE-CLiQ Hub Modules" entry in the hardware catalog.
2. Drag the Hub Module "DRIVE-CLiQ-Hub Module DMx20" into the device configuration.

   Generally, the DRIVE-CLiQ connections are automatically established to the next free DQ interface of the Control Unit.

   ![Example: DRIVE-CLiQ Hub Module with CU320-2 PN](images/147997710731_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: DRIVE-CLiQ Hub Module with CU320-2 PN](images/147997710731_DV_resource.Stream@PNG-en-US.PNG)

   Example: DRIVE-CLiQ Hub Module with CU320-2 PN

**Note**

**No automatic wiring**

The wiring is not performed automatically for an MV drive or an S120 drive with a CU310-2. You must create the DQ connection manually for both variants.

- Click on a DQ interface of the Hub Module and establish a DRIVE-CLiQ connection to the target port of the required component (e.g. the Control Unit).

###### Result

The DRIVE-CLiQ Hub Module has been inserted. You will find more information on the Hub Module in the Inspector window. If necessary, you can change the name of the Hub Module there.

You can then manually connect components to this Hub Module (and hereby change automatically drawn connections, if necessary).

If all DRIVE-CLiQ interfaces of the Control Unit are occupied, all additional components added are automatically wired to the first inserted Hub Module (not with CU310-2 and MV).

##### Terminal Boards

This section contains information on the following topics:

- [Adding a Terminal Board](#adding-a-terminal-board)

###### Adding a Terminal Board

###### Requirements

- A project has been created.
- A Control Unit is contained in the device configuration.

###### Adding a Terminal Board

The TB30 Terminal Board allows you to expand the interfaces of the Control Unit (CU). The Terminal Board is inserted into the option slot of the Control Unit. The Terminal Board does not have to be specified any further.

1. Open the "Supplementary system components > Terminal Boards" entry in the hardware catalog. The following entry is displayed:

   - "TB30 Terminal Board"
2. Drag the Terminal Board to the DRIVE-CLiQ editor.

###### Result

The Terminal Board is added to the device configuration. The DRIVE-CLiQ connections are drawn automatically.

##### Terminal Modules

This section contains information on the following topics:

- [Adding a Terminal Module](#adding-a-terminal-module)

###### Adding a Terminal Module

###### Requirements

- A project has been created.
- A Control Unit is contained in the device configuration.

###### Adding Terminal Modules

With Terminal Modules, you can expand the interfaces of the Control Unit. They are connected to the Control Unit via DRIVE-CLiQ. Terminal Modules do not have to be specified any further.

1. Open the "Supplementary system components > Terminal Modules" entry in the hardware catalog. The following entries are displayed:

   - "TM15 Terminal Module"
   - "TM31 Terminal Module"
   - "TM41 Terminal Module"
   - "TM120 Terminal Module"
   - "TM150 Terminal Module"
2. Drag the Terminal Module to the DRIVE-CLiQ editor.

###### Result

The Terminal Module is added to the device configuration. The DRIVE-CLiQ connections are drawn automatically.

##### Voltage Sensing Modules

This section contains information on the following topics:

- [Adding a Voltage Sensing Module](#adding-a-voltage-sensing-module)

###### Adding a Voltage Sensing Module

Voltage Sensing Modules (VSM) can be used for two different drive objects:

- Infeed

  Is used for voltage measurement, e.g. for the "line transformer" function.

  A VSM10 allows an exact recording of the line voltage curve and supports the fault-free operation of the Line Modules in unfavorable network conditions.
- Motor Module of the "Universal (vector)" type

  Required for the functions "synchronize" and "flying restart."

> **Note**
>
> Voltage Sensing Modules are inserted automatically when adding Active Line Modules or Smart Line Modules in chassis format.

###### Requirements

- A project has been created.
- A Control Unit has been inserted in the device configuration.
- An infeed is available.

  Alternatively: A Motor Module of the "Universal (vector)" drive object type is available.

###### Adding a Voltage Sensing Module

You add a VSM via the hardware catalog. The VSM does not have to be specified any further.

1. Open the "Supplementary system components > Voltage Sensing Modules" entry in the hardware catalog. The following entries are displayed:

   - VSM10 Voltage Sensing Module
2. Move the VSM into the bottom light-gray area of the Line Module.

   - Or -

   Alternatively, drag the VSM onto a Motor Module of the "Universal (vector)" type.

   Depending on the type and format of the Line Module, you can add up to 3 VSMs by dragging & dropping.

**Note**

**Activating the "Line transformer" function module**

If you operate several VSMs on one Line Module, you must activate the "Line transformer" function module in the basic parameterization of the Line Module.

**Note**

**Deleting additional Voltage Sensing Modules**

When you delete additional VSMs, you must deactivate the "Line transformer" function module in the basic parameterization. Otherwise the computing power of the Control Unit may be adversely affected.

###### Result

The Voltage Sensing Module is added in the selected drive object.

### Reading out the device configuration from the drive

This section contains information on the following topics:

- [Basic: Uploading a drive configuration as new station](#basic-uploading-a-drive-configuration-as-new-station)
- [Advanced: Automatically detecting the drive configuration](#advanced-automatically-detecting-the-drive-configuration)

#### Basic: Uploading a drive configuration as new station

For all Control Units, using the "Upload device as new station" function, you have the option of reading out the device configuration of a drive and to create as station (drive unit) in your current Startdrive project. You would have to manually add and link the associated PLC in this way.

##### Requirement

- A project has been created, or an existing project is open.
- There is a physical LAN connection between the drive and the PG/PC. The drive is switched on.
- An IP address has been assigned to the drive.

##### Procedure

To upload a device as a new station, proceed as follows:

1. In the project tree of the interface you are using click on "Update accessible devices".

   The drive is determined as accessible device. The appropriate IP address is displayed in square brackets.
2. Select the device and call the shortcut menu "Upload device as new station".

   Startdrive checks whether all requirements for loading have been met.

   Uploading starts automatically if all of the prerequisites for uploading exist.

   If all of the prerequisites to upload are not available (e.g. components that have not been identified), then the "Upload preview" dialog box opens.

   - Check the messages in the dialog, and if necessary, activate the necessary actions in the "Action" column.

     As soon as uploading becomes possible, the "Upload from device" button is enabled.
   - Click the "Upload from device" button to start the upload.

##### Result

The project data has been uploaded as new drive unit in your Startdrive project on the PC and created in the project tree.

#### Advanced: Automatically detecting the drive configuration

This section contains information on the following topics:

- [Creating PLC and Control Unit in the project](#creating-plc-and-control-unit-in-the-project)
- [Reading out and editing the drive configuration](#reading-out-and-editing-the-drive-configuration)

##### Creating PLC and Control Unit in the project

The SIMATIC DC drive controller comprises a PLC and an integrated SINAMICS drive (S120 for the CPU 150xD). Several options are shown below to create the Control Unit of the Drive Controller in your device configuration.

> **Note**
>
> You can formally create the Drive Controller via the list of drives, in a similar way as for an S120 drive. However, in this case, only the integrated drive (SINAMICS I) of the Drive Controller is created in the device configuration. You would have to manually add and link the associated PLC in this way. This is the reason that we recommend as exception that you transfer the Control Unit of the Drive Controller into the project via the list of controllers. The following description is based on this recommendation.

###### Requirements

- The online connection to the drive is deactivated.
- A new project has been created.

  - Or -
- An existing project has been opened.

###### Inserting a new Drive Controller with integrated drive

You can insert new drives or controls either in the portal view or in the project view.

To insert drive units in the project view via the project tree, proceed as follows:

1. Double-click "Add new device" in the project tree.

   The dialog box with the same name opens.
2. Click on "Controller" to display the list of available controllers.
3. Select the required Drive Controller from list "SIMATIC Drive Controller".
4. Select the firmware version installed on your drive unit.

   If the version numbers (compare: hardware to software) do not match, then it will not be possible to subsequently go online. On creation, the current firmware version is always suggested. If required, you can change the version number via the "Version" drop-down list.
5. Enter a device name in the field at the top with the same name and then click on "OK".

   If you leave the "Open device view" option activated, then the device view opens automatically.

**Inserting a device in the network view**

Alternatively, you can also insert the Drive Controller via the network view.

1. Open the network view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in entry "SIMATIC Drive Controller".
4. Drag the Drive Controller from the hardware catalog and drop it in the network view.

**Inserting a device in the topology view**

Alternatively, you can also insert the Drive Controller via the topology view.

1. Open the topology view.
2. Open the "Controllers" entry in the hardware catalog.
3. Here, open a subentry in entry "SIMATIC Drive Controller".
4. Drag the Drive Controller from the hardware catalog and drop it in the network view.

###### Result

The Drive Controller has been inserted. In the network view, the Drive Controller is shown as PLC, which is networked with an internal drive via PROFIdrive.

![Drive Controller networked](images/148040712331_DV_resource.Stream@PNG-en-US.PNG)

Drive Controller networked

Now continue with the configuration or parameter assignment.

> **Note**
>
> When required, you can subsequently assign another PLC to the integrated SINAMICS drive (SINAMICS I) (see "[Device replacement](#device-replacement-replacing-the-plc-in-the-drive-controller)").

##### Reading out and editing the drive configuration

The "Device configuration detection" function reads the actual topology of your internal drive and places it in your Startdrive project as the initial basis for offline configuration.

The wizard automatically identifies existing components and DRIVE-CLiQ interconnections, and creates the appropriate drive objects (DOs) and connections in the project.

The results of a detection run (of the device configuration) are listed in the dialog "[Detection of the device configuration](#device-configuration-detection)".

All assignable components are listed in the table and are assigned as follows:

- Components are assigned to drive objects.
- Drive objects are assigned to drive units.

> **Note**
>
> **Overwriting existing data in the device configuration**
>
> Existing components and their configuration are overwritten by the automatically detected device configuration.

###### Requirements

- A project has been created, or an existing project is open.
- The device configuration includes a SINAMICS Integrated (see "[Creating PLC and Control Unit in the project](#creating-plc-and-control-unit-in-the-project)").
- Physical connection between the Ethernet interface of your PG/PC and the Ethernet or PROFINET interface of your integrated drive. The integrated drive is switched on.

###### Starting the device configuration detection

1. You can start detection of the device configuration in one of the following ways:

   - Project tree: In the shortcut menu of an internal drive unit or of a CU in the project tree, select the "Detection of the device configuration" entry.
   - Device view: In the device view in the shortcut menu of a CU, select the "Detection of the device configuration" entry.
   - Network view: In the network view in the shortcut menu of a CU, select the "Detection of the device configuration" entry.
   - Main menu: Run "Detection of the device configuration" in the "Online" menu.
2. Before the actual topology can be read, an online connection must exist between the PG/PC and the internal drive unit. If no connection yet exists, the [Connecting devices online](#establishing-an-online-connection-to-the-plc) dialog opens. In this dialog, establish a connection with the drive unit.
3. The topology of the drive unit is read out: Existing DRIVE-CLiQ interconnections are transferred directly from the actual topology of the drive unit.
4. The "Detection of the device configuration" dialog is displayed.   
   All located components are displayed in a tabular overview.   
   Components that cannot be assigned to any main component are displayed in the drop-down entry "Non-assignable components."
5. To cause an LED of a particular module in your actual topology to flash, select the "LED Flashing" option in the "Identification" column. This is how you can identify the module.
6. Assign non-assignable components to the main components. You have the following options for assigning the components:

   - Drag-and-drop: Drag the non-assignable components onto the main components. The system automatically takes account of the DRIVE-CLiQ interconnection rules. If the plug-in rules do not allow insertion into the component in question, a 'forbidden' cursor appears.
   - Shortcut menu: Right-click the component to be connected. All of the possible main components that are assignable as per the plug-in rules are listed in the shortcut menu of the components below the "Move" entry. Delete a component via the "Delete" menu entry. Change the name of a component via the "Rename" menu entry.

###### Selecting the drive object type of motor controllers

After the device configuration has been read out, the drive object type in the header of the dialog is automatically set to "High dynamic (servo)".

If you want to set another motor control, proceed as follows:

1. Presetting the drive object type:   
   Select the option "Universal (vector)" or "High dynamic (servo)" to define the respective drive object type for all motor controllers. In this case, the drive object type can then no longer be changed in the tabular device overview.
2. Individually selecting the drive object type:   
   Select the option "Can be selected" to individually define the drive object type for each motor control. Select the desired drive object type in the tabular device overview in the column "Drive object type" for each drive object in the drop-down list.

**Note**

If one of the motor controllers does not support a control type as drive object type, this option can no longer be selected as a default setting. You must select the drive object type of each motor controller individually in this case.

###### Assigning components

If all components found in the actual topology have been assigned, no further adaptations must be made in the   
"Detection of the device configuration" dialog. The "Create" button can then be selected.   
If the "Create" button cannot be selected (i.e. is grayed out), the topology of the components still has to be adapted:

All of the components that are found are displayed in a tabular overview in the lower area of the dialog.  
Components that are not assignable to a main component are displayed in the drop-down "Non-assignable components" entry.

1. To cause an LED of a particular module in your actual topology to flash, activate the "LED Flashing" checkbox in the "Identification" column. This is how you can identify the module.
2. Assign non-assignable components to the main components. You have the following options for assigning the components:

   - Drag-and-drop: Drag the non-assignable components onto the main components. The system automatically takes account of the DRIVE-CLiQ interconnection rules. If the plug-in rules do not allow insertion into the component in question, a 'forbidden' cursor appears. If components logically belong together, they are moved together and assigned.
   - Shortcut menu: Select the main component to be assigned in the shortcut menu of the component below the "Move" entry. Delete a component via the "Delete" menu entry. Change the name of a component with the "Rename" menu entry.

###### Using the parallel connection view

The parallel connection view supports you with parallel connection of components.

1. Activate the "Parallel connection view" checkbox.

   The "Connect in parallel at" shortcut menu is now available (see Step 2).
2. You have the following options for connecting components in parallel:

   - Drag-and-drop: Move the parallel interconnection-capable components together by dragging them to interconnect them in parallel.
   - Shortcut menu: In the shortcut menu, under menu item "Connect in parallel at" select the drive objects to which you want to connect the component in parallel.
   - The "All" entry connects the selected power unit to all of the interconnectable components in parallel.

   Any components which are hidden but associated with a component are automatically also interconnected in parallel.
3. Move the components via drag-and-drop to the higher-level drive unit to cancel a parallel connection. Alternatively, you can cancel the parallel connection via the "Undo parallel connection" menu entry in the shortcut menu. A new drive object appears as a result.

**Cancelling a parallel connection**

You can cancel an existing parallel connection as follows:

1. Drag components to the higher-level drive unit using drag-and-drop.  
   - Or -
2. Select a component connected in parallel and select the "Disconnect parallel connection" shortcut menu.

###### Creating the configuration

After you have checked and, if required, corrected the topology determined in the configuration, you can transfer this topology to a Startdrive project.

1. Make sure that there are no non-assignable components in the "Device configuration detection" dialog.

   Only when there are no non-assignable components is the "Create" button active.
2. Click the "Create" button.

The components are created in the offline condition. While the topology is being created, an interruptible progress dialog is displayed. If you interrupt the operation, the online connection is maintained. After creation, the topology is displayed in the device view.

###### Result

The topology is created in the device configuration of the selected internal drive unit. The view changes into the device view.

The online connection with the target device is automatically disconnected. As a consequence, you can immediately make changes to the specification or configuration of the components. This would not be possible in the online mode.

### Configuring the Drive Controller (PLC)

This section contains information on the following topics:

- [Parameterizing the PLC of the Drive Controller](#parameterizing-the-plc-of-the-drive-controller)

#### Parameterizing the PLC of the Drive Controller

Detailed information on parameterizing the PLC of the Drive Controller is provided in the TIA Portal online help. [The procedure when parameterizing](Principle%20of%20operation%20of%20SIMATIC%20Drive%20Controllers.md#principle-of-operation-of-simatic-drive-controllers) is described in detail here. Alternatively, you can refer to a Step 7 Manual (S7-1500).

A detailed list of the possibly applicable Manuals is provided in the System Manual "SIMATIC Drive Controller" under "Documentation Guide". You can download this system manual via the SIOS portal starting in 12/2019.

## Establishing an online connection to the PLC

This section contains information on the following topics:

- [Fundamentals](#fundamentals-3)
- [Online connection via PROFINET IO](#online-connection-via-profinet-io)
- [Online connection via PROFIBUS DP](#online-connection-via-profibus-dp)

### Fundamentals

#### Interfaces used

The interfaces for communication via PROFINET IO and PROFIBUS DP are integrated in the SIMATIC Drive Controller (PLC). The online connections to the device can be established via the PLC. The integrated SINAMICS drive has only DRIVE CliQ interfaces for connecting drive components and connection of the drive to the PLC.

![SIMATIC DC interfaces](images/148041253899_DV_resource.Stream@PNG-en-US.PNG)

SIMATIC DC interfaces

Detailed information on the interfaces used by the SIMATIC Drive Controller (PLC) can be found on the following page: [PROFINET, PROFIBUS, PROFIdrive Integrated](Principle%20of%20operation%20of%20SIMATIC%20Drive%20Controllers.md#profinet-profibus-profidrive-integrated)

### Online connection via PROFINET IO

This section contains information on the following topics:

- [Using the PROFINET IO interface](#using-the-profinet-io-interface)
- [Search for the target device (accessible devices)](#search-for-the-target-device-accessible-devices)
- [Assigning an IP address](#assigning-an-ip-address)
- [Going online via the PROFINET interface](#going-online-via-the-profinet-interface)
- [Assigning PROFINET device names](#assigning-profinet-device-names)
- [Comparing IP addresses](#comparing-ip-addresses)
- [Setting the PG/ PC interface](#setting-the-pg-pc-interface)
- [Resetting the communication settings to the factory settings](#resetting-the-communication-settings-to-the-factory-settings)

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
- If the device already has an IP address, perform the "[Reset to factory settings](#resetting-the-communication-settings-to-the-factory-settings)" function to reset it to 0.0.0.0.

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

#### Resetting the communication settings to the factory settings

##### Overview

If problems occur during the commissioning via PROFINET, it is recommended that the IP settings of the device are reset to the factory settings. This provides a defined basis for an error-free commissioning.

##### Requirement

- There is a physical connection between the Ethernet interface of your PG/PC and the PROFINET interface of your device (X150).

##### Procedure

To restore the factory settings, proceed as follows:

1. Open the "Online access" entry in the project tree.
2. Select the network interface of your PG/PC.
3. Double-click "Update accessible devices".

   The accessible device is displayed with the IP address in the project tree.
4. Double-click "Online & diagnostics" in the project tree of the device found.
5. Select the "Functions" entry in the secondary navigation of the "Online & diagnostics" working area.
6. Select the "Reset to factory settings" entry in the secondary navigation.

   ![Resetting factory settings](images/147998802827_DV_resource.Stream@PNG-en-US.PNG)

   ![Resetting factory settings](images/147998802827_DV_resource.Stream@PNG-en-US.PNG)

   Resetting factory settings

   The option "Retain I&M data" is selected by default. This means the IM0 to IM3 data are retained during resetting and are not deleted. If you want to reset this data too, select the "Delete I&M data" option.
7. Click the "Reset" button.

   The device communication settings are reset to the factory settings.
8. Double-click "Update accessible devices".

**Note**

If the PROFINET IO device does not support a reset according to the PROFINET standard, the IM0 to IM3 data may be deleted even though they should be retained according to this configuration.

##### Result

The factory settings of the IP address and the device name are now displayed under "Online access".

> **Note**
>
> After a reset to factory settings, the most important device data for communication is missing:
>
> - Assign a new IP address and a new device name to the device after the reset, see also [Assigning an IP address](#assigning-an-ip-address) and [Assigning PROFINET device names](#assigning-profinet-device-names).

### Online connection via PROFIBUS DP

This section contains information on the following topics:

- [Overview](#overview-4)
- [Setting up the PG/PC interface](#setting-up-the-pgpc-interface)
- [Going online via the PROFIBUS interface](#going-online-via-the-profibus-interface)
- [Parameterizing the automatic detection of the PROFIBUS interface](#parameterizing-the-automatic-detection-of-the-profibus-interface)
- [Resetting communication to the factory settings](#resetting-communication-to-the-factory-settings)

#### Overview

For the SIMATIC Drive Controller, you can also establish an online connection with the PG/PC via a PROFIBUS interface.

Further, you can integrate the internal drive in a PROFIBUS DB subnet of a higher-level control system.

##### Requirements

- There is a physical online connection (using a PROFIBUS cable) between the drive and PG/PC.
- A SIMATIC Drive Controller with an internal S120 drive, which has a PROFIBUS interface, has been created in Startdrive.
- The firmware version of the hardware is identical with the firmware version to be used in the Startdrive project.

##### Online project access

In the "Online access" folder of the project tree, you can find all active interfaces of your PG/PC. Each interface icon provides you with information on the status. You can also display the properties of an interface and change these.

You can find detailed information about this on the following help page "[Online access](Using%20online%20and%20diagnostics%20functions.md#online-access)".

##### Displaying accessible devices

Accessible devices are all devices connected to an interface of the PG/PC that are switched on. Devices that allow only restricted configuration using the currently installed products or that cannot be configured at all can also be displayed.

You can determine accessible devices as follows:

- Via the "Online access" folder in the project tree.
- Via menu item "Accessible devices" in the "Online" program menu.

Additional information on determining accessible devices is provided on the help page "[Display accessible devices](Using%20online%20and%20diagnostics%20functions.md#displaying-accessible-devices)".

#### Setting up the PG/PC interface

Before you can go online using the PROFIBUS interface, check the settings of this interface in the drive and if necessary, correct.

##### Procedure

1. Open the "Online access" entry in the project tree.
2. Double-click "Update accessible devices".

   The drive is displayed in the project tree.
3. Here, select the PROFIBUS interface of your PG/PC.
4. Open the shortcut menu "Properties".

   The "Properties" dialog opens.
5. In the secondary navigation of the dialog, select "General".

   The active configuration of the interface is displayed in the "Configuration" setting area.
6. In the drop-down list "Active configuration", select the PROFIBUS version of the interface.
7. In the secondary navigation of the dialog then select the "PROFIBUS" entry.

   The active PROFIBUS configuration is now displayed to the right in the dialog.
8. If your PG/PC should be the only master in the subnet, then activate option "Is only master".
9. When required, correct other PROFIBUS configuration settings.

   For details, see the help page "[Parameterizing the PROFIBUS interface](Using%20online%20and%20diagnostics%20functions.md#setting-parameters-for-the-profibus-interface)".
10. Click "OK" to confirm the settings that have been made.

##### Result

The PROFIBUS setting of the drive has been made. You must [permanently save](#permanently-save-the-settings) the configuration so that it is not just temporary until the drive restarts.

#### Going online via the PROFIBUS interface

##### Procedure

If you have found the drive at "Online access", establish an online connection. The first time you establish a connection, you must set the "PG/PC interface" and "Connection to interface/subnet" parameters:

1. Click the "Go online" button.

   The "Go online" dialog is called.
2. If no correctly configured interface has been set yet, select the type of the PG/PC interface.
3. If no interface has been preset yet, select the PG/PC interface of your PC.
4. Specify the PROFIBUS interface of the Control Unit as the connection to the interface/subnet.
5. Click "Start search" to search for the drive unit with the set parameters.

   The devices found are displayed in a table under "Select target device".
6. Select your drive unit in the table.
7. Click "Connect" to establish an online connection to the drive unit.

##### Result

An online connection has been established between the PG/PC and the drive unit. The settings are used automatically the next time you go online and the "Go online" dialog is no longer displayed.

#### Parameterizing the automatic detection of the PROFIBUS interface

If you select an interface with automatic detection of the bus parameters, you can connect the PG/PC to PROFIBUS without having to set bus parameters. However, at data transfer rates less than 187.5 Kbps, you may have wait times of up to one minute.

##### Requirements

- There is a physical online connection (using a PROFIBUS cable) between the drive and PG/PC.
- Masters that cyclically distribute bus parameters are connected to the bus.
- In PROFIBUS networks, the cyclic distribution of bus parameters is activated.
- The interface is not assigned to a subnet. If you assign a subnet in the properties of the interface, the settings for the subnet in the project take precedence. In this case, the settings for the automatic interface configuration cannot be changed.

##### Procedure

1. Open the "Online access" entry in the project tree.
2. Here, select the PROFIBUS interface of your PG/PC.
3. Open the shortcut menu "Properties".

   The "Properties" dialog opens.
4. In the secondary navigation of the dialog, select "General".

   The active configuration of the interface is displayed in the "Configuration" setting area.
5. In the drop-down list "Active configuration", select the setting "Automatic protocol detection".
6. In the secondary navigation of the dialog then select the "Automatic configuration" entry.

   The dialog shows the local settings of the automatic configuration on the right-hand side.
7. In the local settings, from the drop-down list "Own address", select the address of the PG/PC interface.
8. Click "OK" to confirm the settings that have been made.

##### Result

The PROFIBUS setting of the drive has been made. You must [permanently save](#permanently-save-the-settings) the configuration so that it is not just temporary until the drive restarts.

#### Resetting communication to the factory settings

If problems occur during commissioning via PROFIBUS, we recommend that you reset the PROFIBUS interface to the factory settings. This provides a basis for fault-free commissioning.

##### Procedure

1. Open the "Online access" entry in the project tree.
2. Here, select the PROFIBUS interface of your PG/PC.
3. Open the shortcut menu "Properties".

   The "Properties" dialog opens.
4. In the secondary navigation of the dialog, select entry "PROFIBUS".

   The active PROFIBUS configuration is now displayed to the right in the dialog.
5. If you wish to set the PROFIBUS configuration back to the factory settings, then in the setting area with the same name, click on "Standard".
6. Click "OK" to confirm the settings that have been made.

##### Result

The PROFIBUS configuration of the drive is set back to the factory setting. You must [permanently save](#permanently-save-the-settings) the configuration so that it is not just temporary until the drive restarts.

## Diagnostics

This section contains information on the following topics:

- [Device diagnostics](#device-diagnostics)
- [DRIVE-CLiQ wiring diagnostics](#drive-cliq-wiring-diagnostics)

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

![Diagnostics icons in the Startdrive/TIA Portal](images/147999097355_DV_resource.Stream@PNG-en-US.png)

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

In the example below, the connection to Servo_03 was changed from X201 to X200 on the device.

| Symbol | Meaning |
| --- | --- |
| ![DRIVE-CLiQ without error](images/147999168779_DV_resource.Stream@PNG-en-US.png)   DRIVE-CLiQ without error | ![DRIVE-CLiQ with error](images/147999172747_DV_resource.Stream@PNG-en-US.png)   DRIVE-CLiQ with error |

## Testing the drive settings using the control panel

This section contains information on the following topics:

- [Using the control panel](#using-the-control-panel)
- [Speed setpoint specification](#speed-setpoint-specification)
- [Basic positioner](#basic-positioner)

### Using the control panel

You can use the control panel to traverse the drive and therefore test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life in the event of non-observance of the safety instructions for the drive control panel**  The safety shutdowns from the higher-level controller have no effect with this function. The **Stop with spacebar** function is not guaranteed in all operating modes. Incorrect operation by untrained personnel and non-observance of the appropriate safety instructions can result in death or serious injury.   - Make sure that this function is only used for commissioning, diagnostic and service purposes. - Make sure that this function is only used by trained and authorized skilled personnel. - Make sure that a hardware device is always available for the EMERGENCY OFF circuit. |  |

> **Note**
>
> **Drive reacts immediately**
>
> Although all enables are removed before returning the master control, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

#### Requirements

- An online connection to the drive has been established.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Activating the control panel

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active after you have activated the control panel and set the enables.

> **Note**
>
> **Control panel locked in torque control mode**
>
> The control panel cannot be activated for drives with torque control mode (p1300 = 23).

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> In addition, as a result of inactivity, the automatic project lock is not activated as long as the control panel is active.

When you activate the control panel, you assume master control of the drive. The control panel can always only be activated for one drive.

To activate the control panel, proceed as follows:

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 2. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

#### Activating the infeed

If an infeed is available in your drive, then the infeed must also be activated. If it is not activated, no further drive enable can be set.

1. Click the "1" icon at "Infeed" to activate the infeed.

#### Setting the enable

To set the required enable for the control panel, proceed as follows.

1. Click the "Set" button under "Drive enables".

   Further areas of the control panel are activated.
2. Click the "Acknowledge faults" button to acknowledge the currently pending faults.
3. If you no longer require the enables, click the "Reset" button under "Drive enables".

#### Deactivating the control panel

When you deactivate the control panel, you return the master control.

To deactivate the control panel, proceed as follows:

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the control panel.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface of the control panel indicates that the master control is deactivated.

#### Result

You can now traverse the drive with the control panel. Enables and faults are displayed at "Drive status". In the "Active fault" display field, the currently pending fault is shown.

### Speed setpoint specification

This section contains information on the following topics:

- [Traversing the drive with speed specification](#traversing-the-drive-with-speed-specification)

#### Traversing the drive with speed specification

After you have set the drive enables, in the "Control Panel" screen form specify the operating mode and switch on the motor.

##### Specifying the setpoint

To specify the setpoint, proceed as follows:

1. In the "Operating Mode" drop-down list, select menu item "Speed setpoint specification".
2. Enter a speed setpoint in the "Speed" field with which the motor is to turn.

   Once you have specified the speed setpoint, the drive is switched on as soon as you click one of the buttons "Start backward", "Start forward", "Jog forward" or "Jog backward" for the first time.

   The motor does not accelerate until you click the "Backward" or "Forward" buttons.

   - To rotate the motor backwards, click the "Backward" button.
   - To rotate the motor forward, click the "Forward" button.
   - Click the "Jog forward" button to inch the motor forward.
   - Click the "Jog backward" button to inch the motor backward.

**Note**

**Rotation through clicking**

The motor continues to rotate while you keep the mouse clicked on the button. Traversing stops when you release the mouse button.

##### Stopping the drive

1. Click "Stop" to stop the drive.
2. Click the "Stop" button to switch off the drive.

##### Viewing actual values of the drive

The current values of various parameters are displayed at "Actual values".

### Basic positioner

This section contains information on the following topics:

- [Manual positioning](#manual-positioning)
- [Relative positioning](#relative-positioning)
- [Absolute positioning](#absolute-positioning)
- [Modify traversing block](#modify-traversing-block)
- [Active homing](#active-homing)
- [Direct homing](#direct-homing)

#### Manual positioning

With manual positioning, you traverse the drive endlessly or with jog position-controlled with a defined velocity and acceleration.

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.

##### Procedure

To traverse the drive via manual positioning, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Manual positioning" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Velocity" and "Acceleration" entries are displayed.
4. At "Velocity", enter a value in LU/min and press the ENTER key. The length unit is an internal length unit of the drive.
5. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key.
6. Use the buttons to traverse the motor forward or backward (see "[Using the control panel](#using-the-control-panel)").

##### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

#### Relative positioning

Use the "Relative positioning" function to traverse an axis a defined distance with the aid of the control panel.

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.

##### Procedure

To traverse the drive via relative positioning, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Relative positioning" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Distance", "Velocity" and "Acceleration" entries are displayed.
4. At "Distance", enter a value in LU and press the ENTER key.
5. At "Velocity", enter a value in LU/s and press the ENTER key.
6. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key. The value is used for acceleration and deceleration.
7. Use the buttons to start the positioning job forward or backward (see "[Using the control panel](#using-the-control-panel)").

##### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

#### Absolute positioning

With "Absolute positioning" you traverse the axis to an absolute position. The function is oriented towards "Direct setpoint specification/MDI".

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.
- The configured encoder system is homed.

##### Procedure

To traverse the drive via absolute positioning, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Absolute positioning" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Target position:", "Velocity", and "Acceleration" entries are displayed.
4. At "Target position", enter a value in LU and press the ENTER key.
5. At "Velocity", enter a value in LU/s and press the ENTER key.
6. At "Acceleration", enter a value in LU/s<sup>2</sup> and press the ENTER key. The value is used for acceleration and deceleration.
7. Click "Start" to start the positioning job.

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, parameters are also available for free selection in two drop-down lists. If the required parameters are not displayed in the list, call a dialog box for extended parameter selection via the "Additional values..." list item.

#### Modify traversing block

You traverse the programmed traversing blocks with "Modify traversing blocks". You can test individual traversing blocks or all programmed traversing blocks in an automatic run.

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.
- The configured encoder system is homed.

##### Procedure

To modify the traversing blocks, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Modify traversing blocks" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Traversing block no." entry is displayed.
4. Select the desired traversing block in the "Traversing block no." drop-down list.
5. Click "Start" to start the traversing block.

##### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

#### Active homing

With active homing you traverse the drive to a home position by means of a homing procedure without a higher-level controller. The drive itself controls and monitors the homing cycle.

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.

##### Procedure

To traverse the drive via active homing, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Active homing" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Home position coordinates" entry is displayed.
4. Under "Home position coordinate", enter a value in LU/min and press the ENTER key. The length unit is an internal length unit of the drive.
5. Use the "Start" and "Stop" buttons to start or stop active homing (e.g. SERVO drives, see "[Active homing](Servo%20drives%20%28highly%20dynamic%29.md#active-homing)").

**Note**

You can also configure the home position coordinate directly in the homing settings of the basic positioner (e.g. SERVO drives, see "[Absolute encoder adjustment](Servo%20drives%20%28highly%20dynamic%29.md#absolute-encoder-adjustment)")

##### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

#### Direct homing

With direct homing, you traverse the drive to a defined home position without using a higher-level control system. The drive itself controls and monitors the homing cycle.

##### Requirements

- Startdrive is in online mode.
- The "Basic positioner" function module is activated.
- The drive control panel is called and the master control is activated.

##### Procedure

To traverse the drive via direct homing, proceed as follows:

1. Select the "Basic positioner" entry in the "Operating mode" drop-down list.
2. Select the "Direct homing" entry in the "Mode" drop-down list.
3. Click "1" in the "Switch on" field to switch on the motor.

   The "Home position coordinates" entry is displayed.
4. Under "Home position coordinate", enter a value in LU/min and press the ENTER key. The length unit is an internal length unit of the drive.
5. Click the "Set" button to activate the home position coordinate directly.

**Note**

You can also configure the home position coordinate directly in the homing settings of the basic positioner (e.g. SERVO drives, see "[Absolute encoder adjustment](Servo%20drives%20%28highly%20dynamic%29.md#absolute-encoder-adjustment)")

##### Drive status

The status of the various parameters are displayed as LEDs at "Drive status".

##### Actual values

The values currently active in the drive are displayed at "Actual values" (actual values and current values in the drive). In addition to the default parameter values, additional r-parameters are available for free selection in two drop-down lists.

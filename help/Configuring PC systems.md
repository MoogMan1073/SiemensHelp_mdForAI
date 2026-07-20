---
title: "Configuring PC systems"
package: HWCWinACPCenUS
topics: 53
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring PC systems

This section contains information on the following topics:

- [Overview](#overview)
- [Integrating IPCs into the TIA Portal](#integrating-ipcs-into-the-tia-portal)
- [Basic configuration of the Open Controller](#basic-configuration-of-the-open-controller)
- [Parameter assignment](#parameter-assignment)
- [Special features of the S7 Modular Embedded Controller](#special-features-of-the-s7-modular-embedded-controller)

## Overview

This section contains information on the following topics:

- [Important information about PC systems and PC stations](#important-information-about-pc-systems-and-pc-stations)
- [Software components of a PC station](#software-components-of-a-pc-station)
- [Improvements of PC Station V2.x compared to PC Station V1.0](#improvements-of-pc-station-v2x-compared-to-pc-station-v10)
- [Rules for the configuration](#rules-for-the-configuration)
- [Procedure for configuring a PC system](#procedure-for-configuring-a-pc-system)
- [Special features of the diagnostics in the PC System V2.x](#special-features-of-the-diagnostics-in-the-pc-system-v2x)
- [Loading with STEP 7](#loading-with-step-7)
- [Load via file](#load-via-file)
- [Web server](#web-server)

### Important information about PC systems and PC stations

#### Definition of PC systems

PC systems are available in a wide range of designs, which can flexibly be expanded with software and hardware components. In this case, we are describing PC systems with a software controller that makes a PC (e.g. IPC) into a controller - similar to a modular controller such as a CPU S7-300/400 or a CPU S7-1500.

PC Station and possibly other components are installed in a PC system.

#### Definition of PC Station

PC Station is a software component that manages SIMATIC software products and the use of interfaces on a PC. In addition, it controls communication among the SIMATIC products on a PC.

PC Station is required by the SIMATIC software products SIMATIC NET PC software, WinAC RT or the SIMATIC S7-1500 software controllers and installed on the target PC.

SIMATIC HMI products such as WinCC Advanced RTX can work with different versions of PC Station.

As of version V2.x, PC Station can also be installed without the software controller.

#### Selecting the version of PC Station

During configuration, the version of your PC Station is automatically adapted by the software components configured in the PC system.

The following scenario is an example of a version change for PC Station:

- You have selected an IPC from the hardware catalog that conforms to PC Station V2.x:

  - In the initial state of the IPC, PC Station V1.0 is the default.
  - PC Station V1.0 remains installed as long as components that are compatible with PC Station V1.0 are inserted in the PC system.
  - The version of the PC Station only adjusts automatically to V2.x when the S7-1500 version of the software controller is inserted in an IPC.
  - If you **only** insert WinCC Runtime, the display changes from "PC Station" to "not installed". No installation of PC Station is required on the PC.
  - If you insert WinCC Runtime and a software controller is already inserted, the version of PC Station remains unchanged.
  > **Note**
  >
  > When you include incompatible software products in the PC system, you receive an error message when trying to compile the station.

The properties of PC Station indicate which version of PC Station is installed: For the selected PC Station, you can find the settings in the Inspector window in the "PC Station" area.

#### Reference

You can find more information on operating a software controller with a PC Station in the [SIMATIC ET 200SP Open Controller CPU 1515SP PC](https://support.industry.siemens.com/cs/de/en/view/109248384) manual, in the [SIMATIC S7-1500 CPU 150xS](https://support.industry.siemens.com/cs/de/en/view/109249299) operating manual and in the [SIMATIC NET PC software Commissioning PC Stations](https://support.industry.siemens.com/cs/de/en/view/109488960) configuration manual.

### Software components of a PC station

A PC station contains a range of configurable software components, which are applied during loading to the PC station. There are different applications which have different effects on the generation and handling of the configuration data.

- PC station V2.x:

  - WinCC RT Advanced, as of V13 SP1
  - S7-1500 Software Controller
- PC station V1.0:

  - Standard application
  - OPC server as a central communication service provider
  - WinCC RT Advanced
  - WinCC RT Professional
  - WinCC V7
  - WinAC RTX
  - Communications processors
- Not installed:

  - WinCC RT Advanced
  - WinCC RT Professional
  - WinCC Client

You configure the specific properties of these components according to the utilized services.

#### WinCC RT Advanced

WinCC RT Advanced is a PC-based HMI solution for single-user systems directly at the machine level. The WinCC RT software is integrated in the SIMATIC HMI devices (e.g. Basic/Comfort/Mobile Panel) and permits data exchange over HMI connections.

If you want to set up several HMI connections to a CPU, use for example:

- The PROFINET and PROFIBUS DP interfaces of the PC station
- CPs and CMs with the relevant interfaces

Other communication options:

- OPC UA client or as server (all HMI versions)
- Communication between HMI systems over the Intranet/Internet

  - Read and write access to tags

#### S7-1500 Software Controller

The SIMATIC S7-1500 Software Controller is a PC-based controller.

- It offers the same functionality as CPUs of the SIMATIC S7‑1500 automation system.
- Software Controllers offer the functionality of a programmable logic controller (PLC) in a PC-based real-time environment.
- In order to develop your user program, use the same programming languages, program structure, and programming interface (STEP 7) with the PC-based controller as those used for hardware controllers.
- For the SIMATIC S7-1500 Software Controller, you can use the same user program as for a hardware controller. The Software Controller CPU has a display application that runs on the PC. The CPU's operating mode can be shown with the display application. With the display application - similar to the display of a hardware CPU - you can execute diagnostics and commissioning tasks.
- The Software Controller makes use of the interfaces of the PC for PROFINET and PROFIBUS.

  Windows-independent use of PROFINET or PROFIBUS for operating distributed I/O. Depending on the interface hardware used, the following functions are possible:

  - PROFINET IO RT or PROFINET IO IRT
  - PROFIenergy
  - I-device
  - PROFIBUS DP master
- Communication (SIMATIC communication, Open User Communication, OPC UA) with Windows applications or external devices via the Windows interfaces of the PC.  
  The communications services are based on the module in use.

The Software Controller based on S7-1500 is available in the following versions:

- As SIMATIC ET 200SP Open Controller CPU 1515SP PC and as CPU 1515SP PC including HMI in ET 200SP design, with pre-installed and pre-configured SIMATIC S7-1500 Software Controller. Can be centrally expanded using ET 200SP I/O modules.
- As CPU 1507S and CPU 1508S Software Controller for PC-based automation. The SIMATIC S7-1500 Software Controller provides the benefits of the standard SIMATIC S7-1500 controller on high-performance industrial PCs.

#### Standard application

With standard applications, you communicate with other applications and devices via your PC module.

You can configure the following communication services depending on the PC module in use:

- S7 connections
- DP services

#### OPC server as central communication service provider

OPC clients use the interface to an OPC server to communicate with an automation device (such as a SIMATIC S7‑1500).

Configure its properties to adapt the OPC server. The set or changed parameters take effect after the configuration data is downloaded to the PC station and the OPC server is started.

You can use the following communication services depending on the PC module in use:

- All connection types
- DP services (DPV0)

#### WinAC RTX

The SIMATIC WinAC (Windows Automation Center) is a PC-based controller and provides the same functionality as SIMATIC S7-300/400 CPUs (hardware controllers). WinAC RTX is used as a solution for typical PC applications (for example, MS Office and user programs) and automation tasks in a system.

Distributed I/O is controlled via:

- PROFIBUS

  - The connection of I/Os via PROFIBUS DP takes place over the integrated DP interface of the SIMATIC PCs or over a communications processor.
- PROFINET

  - The connection of I/O devices via PROFINET takes place over an integrated Ethernet interface of the SIMATIC IPC or over a communications processor.

Optimum access to the data, e.g. for image processing, measured value acquisition, etc., takes place via the WinAC option Open Development Kit (ODK).

You can use the following communication services depending on the PC module in use:

- PG/OP communication
- S7 communication
- Open User Communication (OUC)
- Process data access via OPC

#### Communications processors

Connecting the SIMATIC controllers via communications processors enables direct integration of controllers in industrial networks.

You can use the following communication services depending on the PC module in use:

- OPC UA client or as server
- Open communication (TCP/IP and UDP): Multicast with UDP
- PG/OP communication: cross-network via S7 routing
- S7 communication (client, server)
- IT communication (HTTP(S), e-mail)
- PROFINET IO controller with real-time properties (RT and IRT)
- IP address assignment via DCP
- Shared device
- PROFIBUS DP
- PG/OP communication

#### WinCC RT Professional

WinCC RT Professional is a PC-based control and monitoring system for visualizing and operating processes, production flows, machines and plants – from simple single-user systems to multi-user systems and multi-site solutions with Web clients.

The WinCC RT software is integrated in the SIMATIC HMI devices (e.g. Basic/Comfort/Mobile Panel) and permits data exchange over HMI connections.

If you want to set up several HMI connections to a CPU, use for example:

- The PROFINET and PROFIBUS DP interfaces of the PC station
- CPs and CMs with the relevant interfaces

Other communication options:

- OPC server
- OLE DB server
- WinCC WebNavigator
- WinCC DataMonitor

#### WinCC Client

Depending on requirements, a WinCC single-user system can be expanded into a high-performance client/server system. In this way, several coordinated HMI stations can be operated in a single group with networked automation systems.

#### Reference

You can find more information on WinCC RT in the WinCC online help.

You can find additional information on the S7-1500 Software Controller and WinAC RTX in the section [What you need to know about PC systems](#important-information-about-pc-systems-and-pc-stations).

You can find additional information about the meaning and handling of PC applications and the OPC server in the [SIMATIC NET ‑ Industrial Communication](https://support.industry.siemens.com/cs/de/en/view/https://support.industry.siemens.com/cs/de/de/view/61630799) configuration manual and the [SIMATIC NET ‑ Commissioning PC Stations](https://support.industry.siemens.com/cs/de/en/view/109488960) configuration manual.

You can find more information on communication processors on the[Service&Support](http://w3.siemens.com/mcms/industrial-communication/en/ie/system-interfacing/advanced-controller/Pages/CPs-fuer-advanced-controller.aspx) Web pages.

You can find application examples for changing to the new Software Controller generation in the [Guide for Migrating PC-based Controllers: from SIMATIC WinAC RTX to the SIMATIC S7-1500 Software Controller and TIA Portal](https://support.industry.siemens.com/cs/document/109478804/guide-for-migrating-pc-based-controllers%3A-from-simatic-winac-rtx-to-the-simatic-s7-1500-software-controller-and-tia-portal?dti=0&lc=en-WW).

### Improvements of PC Station V2.x compared to PC Station V1.0

The common features and improvements of the two PC Stations are listed briefly below.

#### Common features of PC Station V2.x and V1.0

PC Station V2.x and PC Station V1.0 have the following common features:

- Simple installation of all required software components via a setup (for example, S7-1500 Software Controller, WinCC Advanced RT, etc.)
- PC systems with pre-installed software controller or pre-installed Runtime Advanced can also be ordered.

#### Improvements of PC Station V2.2 compared to PC Station V2.1

PC Station V2.2 offers the following improvements compared to PC Station V2.1:

- Loading project data in a configuration file

#### Improvements of PC Station V2.1 compared to PC Station V2.0

PC Station V2.1 offers the following improvements compared to PC Station V2.0:

- [Access possible via a Web server](#web-server)

#### Improvements of PC Station V2.0 compared to PC Station V1.0

Compared to PC Station V1.0, PC Station V2.x provides the following improvements:

- Loading the PC Station configuration is easy, similar to a modular S7-1500 controller; no prior configuration of the PC system setup is needed on the IPC.
- Integrated PC hardware diagnostics is integrated into the system diagnostics, for example, to diagnose the state of PC components such as fan or hard disk.

### Rules for the configuration

#### Rules and special features for configuring a PC system

Due to the numerous possible combinations of software and interface cards with various IPC versions, there are complex dependencies.

We recommend simply configuring PC Station according to your requirements and then compiling. STEP 7 performs most of the required adjustments, such as setting the station type. If a combination cannot be compiled, an error message indicates that a rule has been violated and you receive information about how to rectify the error.

The following sections provide information on the basic rules:

- If an IPC is suitable for an S7-1500 Software Controller, it can also be inserted in a WinAC RTX. Applies to most IPCs.
- The following components are suitable or not suitable for the S7-1500 controller software:

  - The open controller (CPU 1515SP PC) is not suitable for the S7-1500 Software Controller.
  - The IPC2x7D and Embedded Controller (S7-mEC 31) are not suitable for the S7-1500 controller software.
- Device replacement between S7-1500 Software Controller and WinAC RTX is not possible.
- You can only insert one software controller in a PC system in each case.
- Neither an OPC server nor an application (user application) can be used in combination with an S7-1500 Software Controller. An installed PC Station V2.x prevents installation of the OPC server or the application on an IPC.   
  Both components are used for a PC Station V1.0.
- Assigning interfaces: Assigning "None, or a different Windows setting" to an interface is only practical for onboard interfaces. The interfaces of the configured CPs/CMs are initially assigned to the PC station, because they are normally used by the configured components of the PC station.
- The graphic view of a PC Station in STEP 7 is identical in the network view and the device view.   
  The "slots" on which the components of a PC system are located are not numbered. When you insert components by dragging them from the hardware catalog, STEP 7 places them automatically: The hardware components (e.g. CPs) are on the left side, the software components (e.g. a software controller) are on the right.   
  Detailed information, for example, about the order number (i.e. the localization information similar to a slot in the PC system) is available only in the device overview table of the device view.

  - In the device overview table, index 125 is permanently assigned for the PC station (it is also referred as the "Station Manager" for PC Station V1.0). This index is displayed in the first row of the device overview table.
  - For the open controller CPU 1515SP PC, there are the columns "Rack", "Slot" and "I address" and "Q address" in addition to the "Index" column. These columns contain the corresponding information for inserted ET 200SP modules.
  - Inserted software components and CPs obtain their index in the order in which they are inserted in the device view. You can force a specific index only by dragging it from the hardware catalog to the corresponding row in the device overview table. This has no impact on the representation in the graphic device view.
  - You can find onboard interfaces to which no software components have been assigned starting at index 100. As soon as you have assigned an onboard interface, it is assigned the next free index, for example 4. In this way, assigned interfaces always appear at the start of the device overview table.

#### IPCs, CPs and software components for PC Station V2.x

The following IPCs are suitable for PC Station V2.x:

- IPC227E, IPC277E
- IPC427D, IPC477D
- IPC427E, IPC477E
- As of IPC547G (without Software Controller CPU 1505SP, CPU 1507S or CPU 1508S)
- IPC627D, IPC647D, IPC677D
- IPC827D, IPC847D (not with fail-safe versions of the Software Controller)

The following CPs are suitable for PC Station V2.x (can only be used as an interface of the S7-1500 Software Controller, CPU 1507S):

- IE generally for PROFINET IO with RT
- CP 1625 for PROFINET IO RT
- CP 1625 for PROFINET IO IRT
- CP5622 for PROFIBUS DP
- CP5623 for PROFIBUS DP

The following software components are suitable for PC Station V2.x:

- CPU 1507S Software Controller
- CPU 1505SP Software Controller
- CPU 1507S Software Controller
- CPU 1508S Software Controller
- WinCC RT Advanced as of V13 SP1

### Procedure for configuring a PC system

#### Introduction

The following section describes how to select a PC system from the hardware catalog in the network view. Drag the required modules from the hardware catalog to this PC system; they will be arranged automatically.

#### Selecting the components in the hardware catalog

Each component is displayed as a folder in the hardware catalog. When you open this folder, you see the different versions of the selected component with their respective article numbers.

The following provides an example of how to create a PC system in the network view.

#### Requirement

- The hardware catalog is open.
- You are in the network view.

#### Procedure

To configure a PC system with a required software controller, follow these steps:

1. Navigate to the "PC Systems" folder in the hardware catalog.
2. Open the folder with the required industrial PC type. You will see all types of the selected IPC type.
3. Click the chosen IPC type to select it.
4. Drag the IPC from the hardware catalog and drop it into the network view.
5. Navigate to the "SIMATIC Controller Application" folder in the hardware catalog.
6. Select the desired software controller:

   - CPU 1507S or CPU 1508S
   - SIMATIC WinAC RTX
7. Drag the desired software controller and drop it onto this PC system.
8. Configure the properties of the PC system and the Software Controller.

> **Note**
>
> **Requirements for loading**
>
> In order to load the hardware configuration, the software controller or PC station must be assigned to an interface.

Refer the following sections to learn how to assign interfaces: [Important information about assigning interfaces](#important-information-about-assigning-interfaces) and [Assigning interfaces for the communication](#assigning-interfaces-for-communication-of-the-pc-station-v2x).

#### Installation requirements depending on configured components

The configured components of a PC system in STEP 7 determine which installation requirements apply to the target system, for example, to an IPC. These installation requirements must be met in order to successfully load the configuration and enable you to access the PC system with STEP 7 online. STEP 7 shows the applicable (minimum) installation requirements for a selected PC system in the "PC System" area of the Inspector window.

**Example: Only WinCC RT configured**

If only WinCC RT is configured, "not installed" must be shown in the PC system in the sense of "no PC Station installed".

Therefore, STEP 7 displays "not installed".

**Example: WinAC RTX configured**

If the WinAC RTX Software Controller is configured, SIMATIC WinAC RTX 2010 must be installed (referred to as "PC Station V1.0" below) on the PC system. SIMATIC WinAC RTX 2010 includes PC Station or S7-RTM, referred to as "PC Station V1.0" in the following, as an installation component.

STEP 7 automatically sets this version of PC Station once a WinAC RTX has been configured.

**Example: CPU 1507S Software Controller configured**

If the CPU 1507S Software Controller is configured, the SIMATIC S7-1500 Software Controller must be installed on the PC system. This includes PC Station installation component, referred to as "PC Station V2.x" below.

STEP 7 automatically sets this version of PC Station once a SIMATIC S7-1500 software controller has been configured.

- PC Station V2.4 (for Software Controller V2.6 as of TIA Portal V15 SP1)
- PC Station V2.3 (for Software Controller V2.5 as of TIA Portal V15)
- PC Station V2.2 (for Software Controller V2.1 as of TIA Portal V14 SP1)
- PC Station V2.1 (for Software Controller V2.0 as of TIA Portal V14)
- PC Station V2.0 (for Software Controller V1.x as of TIA Portal V13 SP1)

#### Reference

You can find additional information about the installation requirements of the relevant PC Station version in the section [Loading with STEP 7](#loading-with-step-7).

### Special features of the diagnostics in the PC System V2.x

#### Special features of the diagnostics in the PC System V2.x

The diagnostics concept for a PC System V2.x has the same hierarchical structure as that of a modular CPU. You can see at a glance whether the station is free from faults or if, for example, an underlying component has a fault.

There is only one difference: They have one hierarchical level more than modular CPUs; the PC system is on a level higher than the Software Controller. The PC system has its own hardware status (separate diagnostics).

The following figure shows the diagnostics of the complete PC system in the project tree. The PC station itself is OK (green check mark), but has an underlying component with a fault (exclamation mark in a green check mark). The symbol provides preliminary information about disrupted or missing modules in the underlying structure.

To obtain a more detailed description of the error, double-click on the "Online & Diagnostics" entry in the project tree.

![Displaying faults in the project tree](images/78354201483_DV_resource.Stream@PNG-en-US.png)

Displaying faults in the project tree

The following figure shows the two entries in the project tree for starting the online and diagnostics view of the PC system. For details, refer to the figure's legend.

!["Online & Diagnostics" project navigation](images/77227421451_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Hardware diagnostics of the PC system (for example, fans, temperatures, voltages for IPCs) |
| ② | Standard diagnostics (as for S7-1500 CPU) |
| ② | Visual brackets for the components of the PC station |

"Online & Diagnostics" project navigation

#### Additional information

You can find additional information on "Diagnostics" and the legend with the meaning of each symbol in the [Diagnostics](http://support.automation.siemens.com/WW/view/en/59192926) function manual.

### Loading with STEP 7

This section contains information on the following topics:

- [Loading PC station V2.x with STEP 7](#loading-pc-station-v2x-with-step-7)
- [Loading PC station V1.0 with STEP 7](#loading-pc-station-v10-with-step-7)

#### Loading PC station V2.x with STEP 7

The special features for loading a PC System V2.x with STEP 7 are listed below.

##### Requirement

- The corresponding software components are installed on the PC system (e.g. SIMATIC S7-1500 CPU 1507S).
- If needed, also install the corresponding version of the Setup DVD for SIMATIC WinCC Runtime Advanced on the PC system.
- The SIMATIC IPC hardware component is physically connected via Ethernet to the PC on which STEP 7 is installed.
- The Software Controller is started.

Other settings on the PC station are not required, because PC System V2.x is fully configured by loading the project.

> **Note**
>
> **Recommended interfaces for download**
>
> - Use a "PN/IE" interface to load a SIMATIC IPC, which is not to be assigned to the Software Controller as a PROFINET interface.   
>   The "X1" interface is recommended.
> - Use the "X2" interface to load a CPU 1515SP PC.

##### Procedure

To download the STEP 7 project, follow these steps:

1. Select the PC system in the device view.
2. Select the "Download to device" shortcut menu command.

   The "Extended download to device" dialog opens.
3. Configure the settings for the interface.
4. Click the "Download" button to start the download.

   If the PC system is not executed in the "Extended download to device" dialog, this may be due to the lack of an interface assignment.

##### Result

The project is downloaded step-by-step. A dialog shows the download progress.

- If you have made changes to the PC system configuration (for example, interface assignment, LED, NVRAM or index), then the PC system configuration is downloaded first. If a restart is required after this, STEP 7 displays a corresponding message. You can stop the download at this point, for example, to first configure the Software Controller and then perform the download later. Configurations already loaded are only reloaded if they have changed.
- If you wait instead of stopping the download after the download of the PC system configuration, the PC system reboots and automatically loads the remaining components, such as the configuration of the Software Controller and WinCC Advanced.

##### Checking the result of the download

After successful completion of the download, the CPU link appears in the Windows Start menu with the name you have assigned in the CPU settings in STEP 7.

The name assigned in STEP 7 is also visible in the CPU display.

#### Loading PC station V1.0 with STEP 7

The special features for loading a PC System V1.0 with STEP 7 are listed below.

##### Requirement

- The SIMATIC WinAC RTX DVD is installed on the PC system.
- Each device to which you want to load is accessible via online access.
- The PC station (runtime PC) is linked to the configuration station over a network. The PC station can be reached as communication station, for example, by setting the parameters in the initial configuration.
- An existing connection is checked, for example, with the "Accessible devices" function.
- The target PC station must be configured with the Station Configuration Editor.

##### Transfer of the configuration

You have the following options for transferring a created configuration to the PC station:

- Online operation

  - Networked (engineering station networked with Runtime PC); access point: "S7ONLINE (STEP 7)"
  - Local (configuration station same as PC station); access point: "PC internal (local)"
- Offline operation (separate engineering station and runtime PC) - Create and import XDB file and WinAC program file (*.wld)

##### Online operation

Online operation enables direct loading of the configuration data:

- Loading over a PC station connected to a network (MPI, PROFIBUS or Ethernet)
- Loading to the local PC station that is also used as configuration station

**Procedure: Online operation - networked**

1. Select the station to be loaded in STEP 7.
2. Load the configuration data with "Online" > "Download to device".

**Note**

**For programming device operation**

Make sure that you set the correct interface with "Set PG/PC Interface" (access point "S7ONLINE (STEP 7)").

**Procedure: Online operation - local**

The configuration data is transferred over an internal PC connection in this case.

1. Select the station to be loaded in STEP 7.
2. Load the configuration data with "Online" > "Download to device".

##### Offline mode

A file of the type XDB is required for data transfer in this operating mode. The configuration system generates an XDB file for each configured PC station.

The storage location of the configuration file is available in the properties of the "PC Station" object in the configuration system. This file can be imported with the "Station Configuration Editor" on the PC station.

You can find more information on offline information in section "[Loading PC station V1.0 via storage medium](#load-pc-station-v10-via-file-1)".

##### Reference

Additional information can be found in the "[NET PC software Commissioning PC Stations - Manual and Quick Start](https://support.industry.siemens.com/cs/de/en/view/109488960)".

### Load via file

This section contains information on the following topics:

- [Load PC Station V1.0 via file](#load-pc-station-v10-via-file)
- [Loading PC Station V2.x with file](#loading-pc-station-v2x-with-file)

#### Load PC Station V1.0 via file

This section contains information on the following topics:

- [Load PC Station V1.0 via file](#load-pc-station-v10-via-file-1)
- [Create and import a configuration using an XDB file](#create-and-import-a-configuration-using-an-xdb-file)
- [Create the program with the help of the memory card and load it to the Software Controller](#create-the-program-with-the-help-of-the-memory-card-and-load-it-to-the-software-controller)

##### Load PC Station V1.0 via file

The particularities of loading a PC Station V1.0 via storage medium are listed below.

To load the complete configuration, you have two options:

- Option 1: [Create and import a configuration using an XDB file](#create-and-import-a-configuration-using-an-xdb-file)
- Option 2: [Create the program with the help of the memory card and load it to the Software Controller](#create-the-program-with-the-help-of-the-memory-card-and-load-it-to-the-software-controller)

##### Create and import a configuration using an XDB file

> **Note**
>
> WinAC RTX cannot be installed.

###### Procedure

Follow these steps to configure a PC station offline using an XDB file and then importing it:

1. Drag a device for a PC station into the network view from the hardware catalog under "PC systems".
2. Select the PC station.
3. Change the name of the PC station to suit your needs under "Properties > General" in the Inspector window.
4. Drag-and-drop the additional components required into the PC station from the hardware catalog. An added component is inserted on a new index.

   > **Note**
   >
   > You can change the index of a selected component in the Inspector window under "Properties > General > Position number". There may be gaps in index numbering for this reason. These gaps are not displayed in the graphic representation of the device view. However, gaps are displayed in the tabular area of the device view.
5. Select the PC station.
6. Under "Properties > XDB configuration" in the Inspector window, select the "Generate XDB file" check box.

   The connection data and addresses for CPs and applications are saved in the XDB file.
7. Specify the storage path under "XDB file path".
8. Select the PC station.
9. Select the shortcut menu command "Compile > ...".

   When the configuration of a PC station is saved and compiled, system data and the XDB configuration file are generated. This can then be loaded into the target system or be installed.

   > **Note**
   >
   > The location of the configuration file is set on the target PC station via the program "Set PG-PC interface" (in the "STEP 7 Configuration" tab).
10. Copy the XDB file to a storage medium that can be accessed by the target station.
11. Import the XDB file to your target PC station with the Station Configuration Editor.

##### Create the program with the help of the memory card and load it to the Software Controller

###### Procedure

The configuration data, the current values of the DBs and the STEP 7 user program can be archived, reused and passed on in wld files. The log file (*.wld) does not save the configuration of the PC station in the Station Configuration Editor.

The controller must be in STOP mode for this to take place.

To create a log file, follow these steps:

1. Select the "New..." command in the "Project > Memory card file" menu.

   A dialog opens.
2. Select the directory in which you want to create the file.
3. Enter the file name and the path.
4. Confirm with "Create".

   > **Note**
   >
   > You can also create a log file in WinAC with the menu command "File > Archive from CPU".
5. Select the "Open..." command in the "Project > Memory card file" menu to display the created log file in the project tree.
6. Select the directory in which the log file with the file extension (*.wld) is located.
7. The log file is displayed in the project tree under "Card Reader/USB memory".
8. Copy the wld file to a storage medium that can be accessed by the target station.
9. To restore the log file, select the menu command "File > Download to CPU**".**
10. Select the log file with the extension *.wld that you want to restore.
11. Click "OK" to confirm. The STEP 7 user program and the configuration for the Software Controller are loaded again.

#### Loading PC Station V2.x with file

This section contains information on the following topics:

- [Load PC Station V2.x via file](#load-pc-station-v2x-via-file)
- [Create configuration file](#create-configuration-file)
- [Loading project data to configuration file](#loading-project-data-to-configuration-file)
- [Open existing configuration files](#open-existing-configuration-files)
- [Import configuration file on the target system](#import-configuration-file-on-the-target-system)

##### Load PC Station V2.x via file

The possibility to save and transport the system configuration of the PC system in a configuration file, offers the following advantages:

- Update of large plants without the TIA Portal
- Simple provision of program and configuration updates
- Plant-level update no longer necessary
- No special software required

##### Create configuration file

###### Create configuration file

The entire configuration of your PC station is saved in a configuration file from the TIA Portal. The data may be re-used and distributed. The configuration file has the extension *.psc.

To create a configuration file, follow these steps:

1. Select the menu command "Project > PC Station configuration file > New > PC Station configuration file".
2. Enter the file name in the "Create memory card file" dialog that opens. To avoid error messages, make sure that the entries are correct:

   - Use short, unique name
   - Name may not contain more than 255 characters
   - Name may not contain spaces
   - Only use permitted characters; these are letters and digits, and the special characters '-' and '_'.
3. Select the desired directory in which you want to create the file. To avoid error messages, also make sure that the entries are correct, as in 2.
4. Confirm with "Create".

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Secure data against access by third parties**  The customer is fully responsible for the secure transport of data. |  |

###### Result

The "Memory card file" folder is created in the project tree under "Card Reader/USB memory" with the following structure:

- PC system configuration file   
  This file contains the PC system configuration file. The information indicates the file name and path information, for example: Drive:\PC-SystemConfiguration01.psc

  - "Display PC system info" icon  
    Double-click on the icon to display all project, device and module information about the configuration loaded. If more data is loaded, you can use the "Update" button to display the latest metadata.
  - Folder with station name already assigned in the project navigation, for example, PC-System_1.   
    This folder contains the configuration of the PC system.

##### Loading project data to configuration file

To load data into the PC system configuration file, you have the following options:

- Load project data to a memory card using Drag&Drop or Copy&Paste
- Write project data to a memory card

###### Requirement

- A PC system with a PC station V2.2 or higher is configured in the STEP 7 project.

  For Failsafe, a PC system with a PC station V2.3 or higher is configured.
- A *.psc file is created and opened in the project tree.
- If you use a CPU1515SP PC2, Microbox, Nanobox "E", IPC547G or an IPC xxxD in your configuration, this is only possible with a PC station version ≥ V2.2.

  > **Note**
  >
  > **Special feature**
  >
  > An individual software CPU cannot be copied to the *psc file.

Please also note the information on configuration file import in the Failsafe manual "[Configuring and programming Safety"](https://support.industry.siemens.com/cs/ww/en/view/54110126).

You will find an application example for "Loading project data to configuration file" on the [Internet](https://support.industry.siemens.com/cs/ww/en/view/109759142).

###### Loading project data to a memory card file

To load project data to a memory card file, follow these steps:

1. Drag the project data that you want to load from the project tree to the memory card.  
   If necessary, the project data is compiled.
2. Then, the "Load preview" dialog opens. This dialog displays messages and recommends actions necessary for loading.
3. Check the messages and enable the actions in the "Action" column if necessary. As soon as loading is possible, the "Load" button is enabled.
4. Click the "Load" button.   
   The loading is performed.

or:

1. Select the "PC system" folder in the project tree.
2. Right-click on the selection and select the "Copy" command from the shortcut menu. Alternatively, you can also use the shortcut <Ctrl+V>.
3. Right-click on the "*.psc" file level or "PC system" folder in the memory card file and select the "Paste" shortcut menu command. Alternatively, you can also use the shortcut <Ctrl+V>.  
   All other levels are locked. If necessary, the project data is compiled.
4. Then, the "Load preview" dialog opens. This dialog displays messages and recommends actions necessary for loading.
5. Check the messages and enable the actions in the "Action" column if necessary. As soon as loading is possible, the "Load" button is enabled.
6. Click the "Load" button.   
   The loading is performed.

or:

1. Select the "PC system" folder in the project tree.
2. In the "Project" menu, select the command "Card Reader / USB memory > Write to memory card".  
   The "Select memory card Select" dialog opens.
3. Select a memory card.  
   A button with a green check mark is enabled in the lower part of the dialog.
4. Click on the button with the green check mark.  
   If necessary, the project data is compiled.
5. Then, the "Load preview" dialog opens. This dialog displays messages and recommends actions necessary for loading.
6. Check the messages and enable the actions in the "Action" column if necessary. As soon as loading is possible, the "Load" button is enabled.
7. Click the "Load" button.   
   The loading is performed.

###### Result

The psc file contains the configuration for all components in corresponding subfolders. The name of the folder is changed to the current PC system name.

> **Note**
>
> **Check that file is complete**
>
> Check the psc file in your TIA Portal to make sure it is complete, for the file can only be edited in the TIA Portal.

##### Open existing configuration files

###### Open configuration file

To view a configuration file in the project tree, follow these steps:

1. Select the menu command "Project > PC Station configuration file > Open > PC Station configuration file".
2. Select the directory containing the psc file.

The memory card file appears with the mentioned content under "Card Reader / USB memory" in the project tree.

##### Import configuration file on the target system

The following lists the tools with which you can commission the target system without TIA Portal:

- Command line tool
- PC Station display in the information area

###### Requirements

- You have administrator rights.
- A Software Controller, version 2.5 or higher, is installed.
- Access to the Open Controller CPU 1515 SP PC2 and/or an IPC is possible.
- The psc file is located in a local directory or is available on a medium such as a USB flash drive.
- For Failsafe: You are a member of the Windows "Failsafe Operators" user group.

###### Overview of the supported command line commands

The following table provides an overview of the supported command line commands:

| Command | Explanation |
| --- | --- |
| PCSystem_Control.exe /Help | Displays the help text in the command line editor. |
| PCSystem_Control.exe /HelpExitCode | Displays the help text for the error codes in the command line editor. |
| PCSystem_Control.exe /PrintConfig <file.psc*> | Displays the information about the components; output format: Standard |
| PCSystem_Control.exe /PrintConfig <file.psc*> /xml | Displays the information about the components; output format: XML format |
| PCSystem_Control.exe /ImportConfig <file.psc*> | The call starts the full import of the psc file. |
| PCSystem_Control.exe /GetStatus /ImportConfig | Displays the current status of all the components, the import process; output format: XML format |
| PCSystem_Control.exe /GetStatus /SimaticComponents | Displays information on all installed Simatic components; output format: XML format |
| * The <file.psc > parameter stands for the full path and file name, for example, C:\Data\Test.psc |  |

###### Result

The data is imported in the background.

If a restart is configured, this is performed automatically once the import is completed. If software CPU is contained in the imported configuration, it remains in STOP after the restart.

###### Procedure for error messages

If an error occurs with a command, you can determine the bit number of the error and to obtain an accurate description of it.

Proceed as follows:

1. To obtain the error code, enter the command "echo% errorlevel%" in the command line tool.
2. This command gives you the following result:

   - If error code = 0, there is no error.
   - If error code > 0, there is an error and it is output as a decimal number.
   - For Failsafe: Error code 20899 or 0x51A3, import successful.
3. The decimal number must be converted into a binary number.
4. To get an overview of the bit number describing the error, enter the command line command "HelpExitCode".

###### Example

Example of conversion of number systems:

- Decimal number: 288
- Binary number: 100100000

Bit number with the corresponding error description:

Result: You can read the error at bit number 5 "Err_Net_45_Full=1" and bit number 8 "Err_IIS_Running=1".

### Web server

This section contains information on the following topics:

- [Settings of the Web server on the target system](#settings-of-the-web-server-on-the-target-system)
- [Enabling of Internet Information Services for Windows 7 and Windows 10](#enabling-of-internet-information-services-for-windows-7-and-windows-10)
- [Configuration of the Web server in the TIA Portal](#configuration-of-the-web-server-in-the-tia-portal)
- [Setting up the Web server using command line commands](#setting-up-the-web-server-using-command-line-commands)
- [Access via HTTPS](#access-via-https)
- [Creating your own certificate](#creating-your-own-certificate)

#### Settings of the Web server on the target system

The Web server functionality is available as of PC Station V2.1. Below you will find the settings and special features for using the Web server.

##### Requirement

The following software requirements are necessary to use the full range of functions offered by the Web server:

- PC Station ≥ V2.3:

  - Windows 10 IoT Enterprise (64-bit) is installed
- PC Station ≤ V2.2:

  - Windows 7 Embedded is installed
  - Windows Ultimate 7 including the Internet Information Services (IIS) ≥ V7.0 is installed (see section [Installing the Internet Information Service](#enabling-of-internet-information-services-iis-for-windows-7))
- .NET version ≥ 4.5 is installed

> **Note**
>
> The software must be installed BEFORE installing the PC station.

##### Principle

The Web server is a Web application and part of the Microsoft Internet Information Server installation. During installation, the Web server integrates itself into the standard website under the pre-installed IIS with access via port 80.   
The Web server is used when the URL address contains /simatic or /simatic/.

##### Example

Examples of how to reach the Web server:

- http://IP address/simatic/ or http://IP address/simatic
- http://computer name/simatic/ or http://computer name/simatic

##### Reference

You can find additional information on the Web server in the [Web server function manual](https://support.industry.siemens.com/cs/de/en/view/59193560).

#### Enabling of Internet Information Services for Windows 7 and Windows 10

This section contains information on the following topics:

- [Enabling of Internet Information Services (IIS) for Windows 7](#enabling-of-internet-information-services-iis-for-windows-7)
- [Enabling of Internet Information Services (IIS) for Windows 10](#enabling-of-internet-information-services-iis-for-windows-10)

##### Enabling of Internet Information Services (IIS) for Windows 7

Below we will show you how to enable the Internet Information Services (IIS) and the required settings.

> **Note**
>
> The additional installation of the IIS is only necessary when Windows 7 Ultimate is installed on your computer.

###### Requirement

Windows 7 Ultimate is installed.

###### Procedure

Follow these steps to enable the Internet Information Services (IIS):

1. Click on the "Start" menu icon.
2. Select "System Control > Programs and Features > Turn Windows features on or off".
3. Confirm the message for user account control with "Yes".
4. Navigate to the menu command: "Internet Information Services" and make the following settings:

![Settings for Internet Information Services](images/89558203275_DV_resource.Stream@PNG-en-US.png)

Settings for Internet Information Services

###### Problems when accessing the Web server

You can find possible causes and their remedies here:

- Internet Information Services were enabled after installation of .NET
- A 64-bit version of Windows is run on the computer

To remedy the problem, you must register a .NET version afterwards in the Internet Information Services (IIS). To do so, execute the following command in the Windows CMD window: C:\Windows\Microsoft.NET\Framework64\v4.0.30319>aspnet_regiis.exe –ir

##### Enabling of Internet Information Services (IIS) for Windows 10

Below we will show you how to enable the Internet Information Services (IIS) and the required settings.

> **Note**
>
> The additional installation of the IIS is only necessary when Windows 10 IoT Enterprise (64-bit) is installed on your computer.

###### Requirement

Windows 10 IoT Enterprise (64-bit) is installed.

###### Procedure

Follow these steps to enable the Internet Information Services (IIS):

1. Right-click on the "Start" menu icon.
2. Select "Programs and Features > Turn Windows features on or off".
3. Confirm the message for user account control with "Yes".
4. Navigate to the menu command: "Internet Information Services" and make the following settings:

   ![Procedure](images/115112793611_DV_resource.Stream@PNG-en-US.png)

###### Problems when accessing the Web server

You can find possible causes and their remedies here:

- Internet Information Services were enabled after installation of .NET
- A 64-bit version of Windows is run on the computer

To remedy the problem, you must register a .NET version afterwards in the Internet Information Services (IIS). To do so, execute the following command in the Windows CMD window: C:\Windows\Microsoft.NET\Framework64\v4.0.30319>aspnet_regiis.exe –ir

#### Configuration of the Web server in the TIA Portal

The procedure for configuring the Web server in the TIA Portal is described below.

##### Procedure

To use the Web server, follow these steps:

1. Select the desired PC system.
2. Select the following settings in the Inspector window under "Properties > General > Web server":

   - Activate web server on this module
   - Enable automatic update
   - Create and manage users

##### Reference

You can find additional information on the Web server in the [Web server function manual](https://support.industry.siemens.com/cs/de/en/view/59193560).

#### Setting up the Web server using command line commands

The following command line tool is installed when installing the PC system: PCSystem_Control.exe.

The tool enables you to query information over the Web server and perform the following tasks:

- Query and check the Web server registration
- Register a Web server
- Revoke Web server registration
- Subsequently change the Web server settings

##### Requirement

The user has administrator rights.

##### Overview of the supported command line commands

The following table provides an overview of the supported command line commands:

| Command | Explanation |
| --- | --- |
| PCSystem_Control.exe/Help | Displays the help text in the command line editor. |
| PCSystem_Control.exe /HelpExitCode | Displays the help text for the error codes in the command line editor. |
| PCSystem_Control.exe/Help/RegWebserver | Displays the help text for this call. |
| PCSystem_Control.exe/Help/UnregWebserver |  |
| PCSystem_Control.exe/Help/VerifyWebserver |  |
| PCSystem_Control.exe/RegWebserver/ | The Dispatcher Web server registers itself in the Internet Information Services (IIS). |
| PCSystem_Control.exe/RegWebserver/HTTP | The call expects an existing connection for the HTTP protocol to the standard port "80". |
| PCSystem_Control.exe/RegWebserver/HTTPS | The call expects an existing connection for the HTTPS protocol to the standard port "443". |
| PCSystem_Control.exe/RegWebserver/HTTP/HTTPS | The call expects an existing connection for the HTTP protocol to the standard port "80" and for the HTTPS protocol to the standard port "443". |
| PCSystem_Control.exe/RegWebserver/Sitename"..." | The call expects an existing website in the IIS with the transferred name. |
| PCSystem_Control.exe/UnregWebserver | The registration of the Web server in the IIS is undone. |
| PCSystem_Control.exe/VerifyWebserver | Displays whether the user can register the Web server in the IIS or if prerequisites have to be met. |

##### Procedure for error messages

If an error occurs with a command, you can determine the bit number of the error and obtain an accurate description of it.

Proceed as follows:

1. To obtain the error code, enter the command "echo% errorlevel%" in the command line tool.
2. This command gives you the following result:

   - If the error code = 0, there is no error
   - If the error code > 0, there is an error and it is output as a decimal number
3. The decimal number must be converted into a binary number.
4. To get an overview of the bit number describing the error, enter the command line command "HelpExitCode".

##### Example

Here is an example for a conversion and a bit number associated with the corresponding error description:

- Decimal number: 288
- Binary number:100100000

Result: You can read the error at bit number 5 "Err_Net_45_Full=1" and bit number 8 "Err_IIS_Running=1".

#### Access via HTTPS

##### Requirements

The requirements for error-free HTTPS access are as follows:

- The current time-of-day is set.
- The firewall is configured appropriately.
- A valid certificate is installed.

  - If no certificate is installed, a recommendation is displayed that you should not use the page. You also have the option of creating your own certificate.

##### Input and example

To access the Web pages with the HTTPS protocol, enter the URL in the following format:

- https://ww.xx.yy.zz, where ww.xx.yy.zz   
  Example input: https://192.168.3.141

You can recognize an encrypted connection by a lock symbol in the status bar of the Web page.

##### Reference

You can find additional information on how to create your own certificate in the section [Creating your own certificate](#creating-your-own-certificate).

#### Creating your own certificate

If your company does not have a Certification Authority (CA), you can use the procedure described in this section. The key files are created with the "OpenSSL" program. If you have not yet installed OpenSSL on your PC, you can download and install the program for free from the following website: <http://openssl.org/>

##### Procedure

To create your own certificate, follow these steps:

1. Open the "Internet Information Services manager" application.
2. Click on the computer name.
3. Double-click "Server Certificates" in the "Features" view.  
   The "Server Certificates" directory opens.
4. Click "Create Self-Signed Certificate" in the "Actions" area.
5. On the "Create Self-Signed Certificate" page, enter a display name for the certificate in the "Specify a friendly name for the certificate" field.
6. Click "OK".   
   The new certificate is displayed in the "Certificate Server" overview.
7. Switch back to the "Internet Information Services Manager".
8. In the "Pages" directory, select the website in which the new HTTPS connection shall be created.
9. On the right side, click on "Edit Page > Binding".  
   The dialog box with the available Web pages opens.
10. Select the connection type "https" and click "Add new".  
    The dialog with the connection properties opens.
11. Select the protocol type "HTTPS" and the port number 443; insert the certificate you created in the "SSL Certificates" selection box.
12. Click "OK" to create a new connection.

## Integrating IPCs into the TIA Portal

This section contains information on the following topics:

- [Advantages](#advantages)
- [System requirements](#system-requirements)
- [Installation](#installation)
- [PC station display in the notification area](#pc-station-display-in-the-notification-area)
- [Repairing/uninstalling](#repairinguninstalling)

### Advantages

In addition to control and visualization tasks, PC systems can also be used for the following applications:

- Data gateway to higher-level MES
- Plant-level data server
- Hardware platform for SCADA systems
- Industrial workstations (for example, at test stations)
- Process & data analysis on site

#### Integrating SIMATIC IPCs in TIA Portal

Integrating the SIMATIC PC station (IPC in TIA Portal) integrates a PC system in a plant configuration (TIA project), with the following advantages:

- Fast configuration

  - Configuration via drag-and-drop from the hardware catalog
  - Detailed display of all interfaces – suitable for configuration of SIMATIC IPC
  - Network-spanning view including display of IP addresses
  - Fine-grained status diagnostic network topology
- Simplified commissioning

  - Central overview of all IP addresses

    Excludes conflicts due to duplicate assignments

    Easy to find SIMATIC IPC (including host name and IP address) via "Accessible devices"
  - Status diagnostics within the TIA Portal

    Diagnostics of the Ethernet/PROFINET connection to the SIMATIC IPC from the configuration

    Simple and fast error localization, for example, topology errors in the network, inaccessible devices

    Port-granular diagnostics (including the ports assigned in the topology on the SCALANCE switch)
  - Overview of the entire network

    Comprehensive information on topology, structures and hierarchies
- Integration of hardware diagnostics for IPCs in the TIA Portal

  - Fine-grained status diagnostics of the network topology, for example, topology errors in the network, inaccessible devices
  - Preventive maintenance, for example, of hard disks or fans
  - Early reaction to violation of high/low limit of the permitted operating temperature
  - Central overview of all SIMATIC IPCs in a plant
  - Display of hardware diagnostics in the WinCC Diagnostic Viewer

    Display of PC diagnostics in the running plant

    Preventive maintenance

### System requirements

To install a PC station in an IPC, the following requirements must be met:

#### Requirements

- You have administrator rights on your computer.
- A minimum of 400 MB space is available.

#### Hardware requirements

The following IPCs are supported:

- SIMATIC IPC2x7E
- SIMATIC IPC4x7D
- SIMATIC IPC4x7E
- SIMATIC IPC547G
- SIMATIC IPC6x7D
- SIMATIC IPC8x7D

> **Note**
>
> **Make sure that the IPCs you use in your configuration are compatible.**
>
> If you ignore the error message about your configuration, diagnostics errors in TIA Portal can result.
>
> Always select the appropriate IPC for your configuration.

#### Software requirements

- The SIMATIC IPC software can be used with the following operating systems:

  - Windows 10 Enterprise IoT (for CPU 1515SP PC2, all IPCs; exception: IPC4x7D)
  - Windows Embedded Standard 7 E/P SP1 32-bit
  - Windows Embedded Standard 7 E/P SP1 64-bit
  - Windows 7 SP1 32-bit
  - Windows 7 SP1 64-bit
- The following diagnostic software is installed:

  - DiagBase >= V1.5.0 or
  - DiagMonitor >= V4.5.0

#### Restrictions

- The following filters are disabled:

  - UWF (for CPU 1515SP PC2, all IPCs; exception: IPC4x7D)
  - EWF
  - FBWF
- The following components may not be installed:

  - PC Station classic (S7-RTM)
  - CPU 150xS
  - SIMATIC NET
  - WinAC RTX

### Installation

#### Storage media for the installation

Setup can be installed from the following media:

- USB stick
- DVD
- Hard disk
- Network drive

#### Installation

Setup is started by running "start.exe" in the Setup folder.

Proceed as follows for this:

1. Double-click on "start.exe".
2. Select the desired product properties for the installation.
3. Follow the instructions on the screen during the installation.

#### Result

After a successful installation, the following components have been installed:

- PC Station V2.x
- S7 device drivers
- SIMATIC NET CP Manager Plus
- PC Station Web server

In addition, an icon for the PC Station service ![Result](images/72509366283_DV_resource.Stream@PNG-de-DE.png) is also displayed in the notification area of the Windows task bar during operation of the CPU.

#### Reference

Additional information on the installation requirements of configured components is available in the section [Procedure for configuring a PC system](#procedure-for-configuring-a-pc-system).

### PC station display in the notification area

An icon for the PC Station service ![Figure](images/72509366283_DV_resource.Stream@PNG-de-DE.png) is also displayed in the notification area of the Windows task bar during operation of the CPU. Among other things the icon indicates the current state of the PC Station service, and provides you with the opportunity to do configurations.  
Right clicking the icon ![Figure](images/72509366283_DV_resource.Stream@PNG-de-DE.png) in the notification area opens the PC Station shortcut menu.

#### States of the notification area icon

The state of the icon for the PC Station service in the notification area of the task bar changes as soon as the mode of the PC station changes.  
The notification area icon can display the following states:

| RUN | STOP |
| --- | --- |
| ![States of the notification area icon](images/72509366283_DV_resource.Stream@PNG-de-DE.png) | ![States of the notification area icon](images/72509490315_DV_resource.Stream@PNG-de-DE.png) |

#### Configuration options using the "Station Manager" service's icon

The icon for the PC Station service in the task bar's notification area gives you the following configuration options via the shortcut menu:

- Import > Import Configuration

  This shortcut menu command opens and displays the metadata of a selected PC system configuration file. The user also starts the import of the psc file with this. The feature is not supported for F-CPUs.
- Configuration

  - Delete existing configuration  
    Administrative rights are required for this configuration option.

    This shortcut menu command causes the configuration to be deleted.

    This function is disabled by default in an F-CPU. The "Failsafe Operators" user group must be added explicitly authorized in order to provide them with permission on an individual basis. Furthermore, the configured passwords for an F-CPU are retained after the configuration is deleted. These passwords are required later again for downloading. To reset the password, load a project without passwords.
  - Change the storage path of configuration data  
    Administrative rights are required for this configuration option.

    If you are protecting a partition with an enhanced write filter (EWF), for example, the configuration and diagnostic data is also thereby write-protected.

    Save the diagnostic data in an area of the hard disk that is not write-protected. You can also save the configuration data containing the configuration in a section of the hard disk that is not write-protected.
- Restart all of the PC Station services

  Administrative rights are required for this configuration option.

  This shortcut menu command causes all of the PC Station services to be restarted.
- Exit

  This shortcut menu command causes the PC Station panel to be closed. The icon for the PC Station service in the notification area of the task bar is hidden. Restart the PC Station panel using the following entry in the Windows Start menu: **Siemens Automation > SIMATIC > PC Station > "PC Station"**

### Repairing/uninstalling

You have the option to repair or uninstall the installed program.

#### Repairing

To repair the program, proceed as follows:

1. Navigate to the path where your Setup is installed.
2. Double-click on "start.exe".
3. Select "TIA integration for SIMATIC IPC" by placing a check mark and click "Next".
4. Select the "Repair" button.
5. Click "Next" and follow the instructions on the screen.

#### Uninstalling

To uninstall the program, you have two options.

**Via the Control Panel**

1. In the Windows taskbar, select **Start > Control Panel > Run Advertised Programs**
2. Select the program "TIA integration for SIMATIC IPC".
3. Click "Uninstall".
4. Follow the on-screen instructions during the uninstall process.

**Via "start.exe":**

1. Navigate to the path where your Setup is installed.
2. Double-click on "start.exe".
3. Select "TIA integration for SIMATIC IPC" by placing a check mark and click "Next".
4. Select the "Uninstall" button.
5. Click "Next" and follow the instructions on the screen.

#### Restrictions for cancellation

When the setup is aborted, all installation steps must be carried out again.

## Basic configuration of the Open Controller

This section contains information on the following topics:

- [Initial configuration of an Open Controller](#initial-configuration-of-an-open-controller)

### Initial configuration of an Open Controller

#### Creating the configuration

You have created a new project in the TIA Portal.

To create the configuration in the TIA Portal, follow these steps:

1. Double-click "Add new device" in the project tree.
2. Select "CPU 1515SP PC (+HMI)" under "PC Systems > Open Controller".
3. Select the appropriate version.

   The configured Open Controller is displayed in the device view.
4. The following components can be seen in the Open Controller:

   - Onboard interface X2 (GB Ethernet Windows interface) that is assigned directly to the PC station (1 port)
   - Exchangeable BusAdapter X1 that is assigned directly to the Software Controller (2 ports)
   - On the right side (behind the plugged modules in the rack): the configured CPU 1505S Software Controller and WinCC Runtime Advanced.
5. Insert the server module.   
   The server module at the right end of the configuration forms the termination of the CPU with the I/O modules.

**Setting the IP addresses:**

In the Inspector window under "Properties":

- Onboard interface X2: The configured, preset IP address is identical to the Windows IP address that is set on the Open Controller during initial commissioning.
- BusAdapter X1: The configured, preset IP address is identical to the IP address that was set in the panel of the Software Controller (display application) during initial commissioning.

**Important properties of the Software Controller**

If necessary, you can change the properties in the Inspector window under "Properties".

- Selecting startup type
- System diagnostics
- Setting the storage location for retentive data
- Setting up copy protection
- Using the LEDs of the hardware
- Configuring the Web server
- Assigning interfaces for the communication

**Establish HMI connection**

1. Right-click the WinCC RT Advanced in the device view.
2. Start the HMI device wizard.
3. Apply all default settings.  
   The wizard creates system images for you with the corresponding navigation.
4. Switch to the connection view in the network view.
5. Click on WinCC RT Advanced.
6. Draw a line from the WinCC RT Advanced software to the S7-1500 Software Controller (e.g. CPU 1505SP) while keeping the mouse button pressed.  
   A network connection is established between the two devices.

#### Downloading the project to the target system

The complete PC station is downloaded the first time you download the configuration.

1. Select the complete PC system in the device view.
2. Click the "Download" button.
3. Make the following settings:

   - Type of connection
   - Specify the interface of the programming device
   - Specify the X2 interface on the Open Controller

> **Note**
>
> The first TIA Portal download **must** take place over the "X2" interface.
>
> Only ASCII characters are permitted in the name of the interface X2 PN/IE (LAN) in the TIA Portal, e.g. PROFINET_2.

Download and compile the project. The hardware configuration and the first download are now completed.

#### WinCC RT Advanced

WinCC Runtime Advanced contains all the essential functions for operator control and monitoring of machinery or plants.

#### Reference

You can find additional information on configuration and downloading in the [ET 200SP Open Controller CPU 1515SP PC](https://support.industry.siemens.com/cs/de/en/view/109248384) manual.

You can find more information on WinCC RT Advanced in the [WinCC Advanced V13.0 SP1](https://support.industry.siemens.com/cs/de/en/view/109091876) system manual.

## Parameter assignment

This section contains information on the following topics:

- [Startup of the Software Controller (startup parameter)](#startup-of-the-software-controller-startup-parameter)
- [Special features in the parameter assignment of the access protection](#special-features-in-the-parameter-assignment-of-the-access-protection)
- [Advanced configuration for Software Controllers](#advanced-configuration-for-software-controllers)
- [Setting the storage location for retentive data](#setting-the-storage-location-for-retentive-data)
- [Using the LEDs of the hardware](#using-the-leds-of-the-hardware)
- [Important information about assigning interfaces](#important-information-about-assigning-interfaces)
- [Assigning interfaces for communication of the PC Station V2.x](#assigning-interfaces-for-communication-of-the-pc-station-v2x)
- [SIMATIC NET version](#simatic-net-version)

### Startup of the Software Controller (startup parameter)

#### Configuration of the startup type of the CPU

With a CPU 150xS, you have the option of assigning parameters for the startup characteristics in addition to the standard startup parameters, for example "Startup after POWER ON". The CPU can be started (POWER ON) in two different ways:

- Manual start via the "Power" button on the CPU display
- Automatic start during PC start (recommended)

Using the "Automatic start after booting the PC" option in the properties of the software controller, you determine how the CPU starts.

We recommend you enable the option "Automatic start after booting the PC", otherwise the software controller does not automatically boot after the PC system starts. A software controller can be only loaded after it has started.

If this option is disabled, you must start the CPU manually before a download procedure via the CPU display.

> **Note**
>
> **BIOS memory test on SIMATIC IPCs**
>
> PCs provide the option of a memory test. Some hardware tests, such as the memory test, are disabled by default in the BIOS setup program and are skipped during startup of the PC. Booting is accelerated as a result.
>
> If you are using the CPU on a SIMATIC IPC or CPU 1515SP PC, the BIOS memory test must not be enabled.

The default startup parameters are no different from the startup parameters of S7-1500 CPUs.

#### Setting the startup type

To set the startup type, follow these steps:

1. Start STEP 7.
2. Open your project.
3. Change to the project view.
4. Open the device view.
5. Select the CPU.
6. On the "Properties" > "General" tab of the Inspector window, select the "Startup" area.
7. Configure the startup characteristics of your CPU.

   ![Setting the startup type](images/91750113163_DV_resource.Stream@PNG-en-US.png)

   ![Setting the startup type](images/91750113163_DV_resource.Stream@PNG-en-US.png)
8. Download the project to the CPU, by selecting the PC system before you start the download.

#### Result

If, in addition to the settings for the startup type, you also change the "Automatic start after booting the PC" option, the CPU is stopped automatically before the download. At the beginning of the download, the CPU starts again in STOP mode.

The project is downloaded. The new settings for the startup type are active.

### Special features in the parameter assignment of the access protection

#### Assigning access protection parameters in STEP 7

The access protection parameters are assigned using the properties of the PC system in which the software controller is inserted.

The access levels are read-only in the properties of the CPU. To access the properties of the PC system, click the arrow![Assigning access protection parameters in STEP 7](images/77540203531_DV_resource.Stream@PNG-de-DE.png). Here you can define the access levels of the PC system and overwrite them for the entire application.

> **Note**
>
> **Assigning access protection parameters for the entire PC system**
>
> Unlike for a hardware CPU, parameter assignment for access protection is not done directly in the CPU's properties. This ensures that consistent protection level passwords are configured for all of a PC system's components.
>
> Unlike a hardware CPU of the S7-1500 automation system, a separate display password cannot protect the CPU against unauthorized access . Because the CPU can also be controlled by remote access, it uses the access protection passwords from STEP 7 to ensure access protection for the display.

#### Reference

For additional information on the protection concept in conjunction with display access, refer to the[SIMATIC S7-1500 CPU 150xS](https://support.industry.siemens.com/cs/de/en/view/109249299) operating manual.

### Advanced configuration for Software Controllers

If you select an S7-150xS software controller in the device view or network view, click on the "Advanced configuration" area in the Inspector window. The parameters under "Advanced configuration" are explained below or you can find references to explanations for these parameters.

#### PC communication interface

The PC communication interface offers access, for example, to an office network via a Windows-controlled interface independent of a PROFIBUS or PROFINET subnet. Your user program uses this interface to communicate with other devices or fetch information via the web server of the software controller:

**Accessing the web server**

Similar to the hardware interface, you also need to enable access via the PC communication interface to be able to access the web server of the controller software through this interface.

The following figure shows the web server access from the web browser of the PC system via the PC communication interface.

![PC communication interface](images/115224525707_DV_resource.Stream@PNG-en-US.png)

**Communication via Open User Communication (OUC)**

You can also use Ethernet interfaces on the PC via the PC communication interface.  
Basically, only the name of the host interface and the hardware ID is displayed for the configuration.  
In the properties of a communication instruction (e.g. TSEND_C), you can access the properties of the PC communication interface and use the "Connection data" area to access the address parameters for the programmed OUC communication. The hardware ID of the PC communication interface is entered in the connection data.

#### Index

The index of a component in the PC system corresponds to the position of the component (for example, a hardware resource as an interface). It is a sort of "slot address on the PC-internal subnet" (Softbus).

The index of a software or hardware component is not displayed in the graphical view.

When a software controller is selected in the network view or device view, you can read or change the index in the properties of the software controller under "Advanced configuration". You can also change the index in the device overview table in the device view.

#### Reference

You can find information on using the hardware LEDs [here](#using-the-leds-of-the-hardware).

You can find information about setting the storage location for retentive data [here](#setting-the-storage-location-for-retentive-data).

### Setting the storage location for retentive data

The S7-1500 Software Controller (CPU) provides the option of storing data retentively in the PC mass storage or in the integrated NVRAM when the CPU is stopped or a power failure occurs. You set the type of data storage in the CPU properties.

> **Note**
>
> **Data loss when changing the storage type**
>
> When you change the storage type, the current retentive data and the contents of the diagnostic buffer are deleted when the changed configuration is loaded.

#### Requirement

The project view is open.

The device view is open.

#### Procedure

To configure the type of storage, follow these steps:

1. Select the CPU.
2. Select the "Advanced configuration" area on the "Properties" tab of the Inspector window.

   - Select the "PC mass storage" option button to store the retentive data in the mass storage of your PC.
   - Select the "NVRAM of PC platform" option button to save the retentive data in the integrated NVRAM of your PC.

   ![Procedure](images/72343610763_DV_resource.Stream@PNG-en-US.png)
3. To change the type of data storage in STEP 7 at a later time, download the project to the PC system again.

> **Note**
>
> **Downloading the change of configuration**
>
> When you change the storage type for storage of retentive data in STEP 7, you must download the entire PC system for this configuration change. When you change the storage type, the CPU reboots during the download process. Without a reboot the storage type is not changed despite the download process.
>
> To ensure the required restart of the CPU, you have to load the PC and then restart it.

---

**See also**

[Advanced configuration for Software Controllers](#advanced-configuration-for-software-controllers)

### Using the LEDs of the hardware

The S7-1500 Software Controller (CPU) can display its status on the LEDs of the hardware platform on which it is installed. You set this functionality in the CPU properties in STEP 7.

> **Note**
>
> **Simultaneous access by multiple components**
>
> Take care that multiple competing components (for example DiagBase and CPU) do not make simultaneous access to the hardware LED.

#### Requirement

Your project is open.

You are in the project view.

#### Procedure

To use the LEDs of the hardware platform for the CPU, follow these steps:

1. Open the network view or device view.
2. Select the CPU.
3. Select the "Advanced configuration > Hardware LED" area on the "Properties" tab of the Inspector window.

   ![Procedure](images/72344085003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72344085003_DV_resource.Stream@PNG-en-US.png)
4. Select the "Use hardware LEDs with CPU 150xS" option.

As described in the note below the option, you then have to fully download the PC system and reboot it.

#### Result

The PC is shut down and the CPU is stopped. The project is downloaded.

The PC is restarted automatically. The CPU starts in STOP mode. The download is continued. After completion of the download, the CPU is put into RUN mode.

#### Special feature

If there is an online/offline difference with regard to the "Use hardware LEDs" property, this difference is not shown in the online/offline comparison.

---

**See also**

[Advanced configuration for Software Controllers](#advanced-configuration-for-software-controllers)

### Important information about assigning interfaces

As of STEP 7 V13 SP1, relationships between a software component, such as a Software Controller, and its interfaces to the outside world, e.g. a PROFINET interface, are represented by reference lines.

#### Representation of relationships

If nothing was selected, all interfaces and the software components are connected by a gray line. The lines have a square connector at the end. These lines show the relationship between software components (e.g. S7-1500 Software Controller, WinCC RTX or OPC server) and interfaces (PROFINET, PROFIBUS, ...).

When you select an interface, the assigned software components can be recognized by the blue line that is clearly distinguishable from the gray lines.

Interfaces without relation lines or with gray reference lines are not assigned.

#### Example 1: Assigning an interface to the Software Controller (CPU)

A blue reference line between a selected interface and an S7-1500 Software Controller means that the interface is assigned to the S7-1500 Software Controller and can only be used by it. In this case, the Software Controller, as IO controller, can operate a PROFINET IO system on this interface.

Only with this type of interface assignment is it possible to configure the IP address and the device name of the PROFINET interface and load it in the PC system.

![Example 1: Assigning an interface to the Software Controller (CPU)](images/78357970571_DV_resource.Stream@PNG-en-US.png)

#### Example 2: Assigning the interface to the SIMATIC PC station

A blue reference line from a selected onboard interface to several software components means that this interface is assigned to the PC station and can therefore be used by all software components. Programming device communication, for example, can be performed through this interface.

Although you can edit the IP address of the interface with this type of interface assignment, this setting is not loaded in the PC system. The IP address must be set in Windows on the PC system. It still makes sense to synchronize IP addresses, for example, to be offered exactly this PC station in the "Extended download" dialog (filter function).

![Example 2: Assigning the interface to the SIMATIC PC station](images/78357974283_DV_resource.Stream@PNG-en-US.png)

#### Example 3: None, or a different Windows setting

If you assign the "None, or a different Windows setting" option to an onboard interface, no relation to the inserted software components is possible and therefore also not visible. Only Windows applications can use this interface; however, they are not visible in the configuration. The IP address of the interface is not visible in the configuration as well.

![Example 3: None, or a different Windows setting](images/78358579595_DV_resource.Stream@PNG-en-US.png)

#### Displaying the position of the interface

The position of the interface is displayed below the "Interface assignment" area in the Inspector window. Depending on the assignment to the PC station or to the Software Controller, the index or the hardware resource/interface type is displayed.

### Assigning interfaces for communication of the PC Station V2.x

#### Interface types

The PC station uses the Ethernet interfaces on the PC for communication. The following communication services are available through these Ethernet interfaces:

- Engineering access to the PC station and the installed components, for example, the S7-1500 Software Controller or WinCC RT Advanced
- HMI connections to the PC station or to the Software Controller
- Data communication (S7 communication of the Software Controller)
- HMI connections, for example, between WinCC RT Advanced and external controllers
- S7 connections routed through the PC

#### Communication between devices

To enable configured communication between components on the PC and other SIMATIC devices, you need to assign the interface to the PC station. The following Ethernet interfaces can be assigned to PC Station V2.x:

- On-board Ethernet interfaces, for example, X1 and X2, of the SIMATIC IPC (not: on-board CP 1616)
- On-board X2 interface of CPU 1515SP PC

A maximum of 2 on-board interfaces can be assigned.

Engineering functions are possible with all Ethernet interfaces of the PC as long as they are operated under Windows, even if they are not assigned to the PC station.  
However, for simplified commissioning, at least one interface must be assigned:

- SIMATIC PC: X1 interface
- CPU 1515SP PC: X2 interface
- No use of external CPs

> **Note**
>
> Interfaces for exclusive use can also be assigned to the S7-1500 Software Controller. These are then not available for the PC station.

#### Procedure

To assign the interfaces for the communication to the PC station, follow these steps:

1. Select the PC system.
2. Select the desired integrated interface in the device view.
3. In the Inspector window, select the area "General > Interface assignment".
4. Assign the interface to the "SIMATIC PC station".
5. Compile the project with "Edit > Compile".
6. Download the hardware configuration of the PC system to the target device.

#### Result

After downloading, the interfaces can be used for configured communication services.

#### Reference

You can find more information on the special aspects of configuring interfaces with the S7-1500 Software Controller in the [SIMATIC S7-1500 CPU 150xS operating manual](https://support.industry.siemens.com/cs/de/en/view/109249299).

### SIMATIC NET version

Information on the SIMATIC Net version is available at Service&Support under the [Entry ID:63098071](https://support.industry.siemens.com/cs/document/63098071?lc=en-WW).

#### SIMATIC NET version for onboard interfaces

The SIMATIC NET version of the onboard interfaces can be found as follows:

1. Select the onboard interface.
2. In the Inspector window, select the area "General > Catalog information".

   - For a **V2.x PC system,** STEP 7 automatically sets the version of the PC station once a SIMATIC S7-1500 Software Controller has been configured. This setting should not be changed. SIMATIC NET cannot be used or configured.
   - For a **V1.0 PC system**, the latest version of the SIMATIC NET CD from the hardware catalog is displayed, for example V8.2, see the description text. STEP 7 does not know the SIMATIC NET version actually used because you are installing and configuring PC System V1.0 with S7-RTM (Station Manager) from the SIMATIC NET CD.

#### SIMATIC NET version for PC Station

If you select a PC system in the network view and select the "PC Station" area in the Inspector window, the various PC system versions can be selected in the drop-down list.

- Select "PC System V1.0" option: **No** SIMATIC NET version displayed because STEP 7 does not know the SIMATIC NET version actually used, see above.
- Select the "PC-System V2.x" option: SIMATIC NET cannot be used or configured.

## Special features of the S7 Modular Embedded Controller

This section contains information on the following topics:

- [Special features of the S7 Modular Embedded Controller](#special-features-of-the-s7-modular-embedded-controller-1)
- [Introduction and basic procedure](#introduction-and-basic-procedure)
- [EC31-HMI/RTX: Configuring visualization](#ec31-hmirtx-configuring-visualization)
- [Downloading the configuration data to the target system](#downloading-the-configuration-data-to-the-target-system)

### Special features of the S7 Modular Embedded Controller

#### Recommendation

For new projects we recommend switching to the new product generation with S7-1500 Software Controllers.

#### Reference

You can find additional information on the S7-modular Embedded Controller in the [SIMATIC Embedded Automation S7 Modular Embedded Controller](https://support.industry.siemens.com/cs/de/en/view/37971572) operating instructions.

### Introduction and basic procedure

#### Introduction

S7-modular Embedded Controllers (S7-mEC) are PCs in S7-300 design with preinstalled and preconfigured software:

- Windows Embedded Standard operating system
- WinAC RTX (F)
- SIMATIC NET
- WinCC Runtime (only with EC31-HMI/RTX)

#### Ethernet interfaces of the S7-modular Embedded Controller

An S7-modular Embedded Controller has two integrated Industrial Ethernet interfaces:

- The X1 PN LAN P1 / X1 PN LAN P2 interface can be configured as a PROFINET interface.
- The X2 P1 PN/IE LAN  interface is assigned to the PC station in index 3 at IE General and is preconfigured for Industrial Ethernet communication.

  > **Note**
  >
  > If accessing S7-mEC via Remote Desktop Protocol, ensure that S7-mEC and the Engineering PC/programming device are connected to the same Ethernet subnet.
  >
  > To access S7-mEC via Remote Desktop protocol, you have to use the IE General network connection (usually X2 P1 PN/IE LAN interface).

#### Basic configuration and programming of the S7-mEC

Since an S7-mEC is a preconfigured system, follow these steps:

1. Create a project.
2. Insert a PC station.
3. Configure the hardware.
4. Create an S7 program.
5. Configure visualization in WinCC for the EC31-HMI/RTX.
6. Download the configuration data to the WinLC RTX EC.

### EC31-HMI/RTX: Configuring visualization

#### For EC31-HMI/RTX only

Create the visualization project for the EC31-HMI/RTX on the engineering PC, using SIMATIC WinCC.

#### Requirement

- WinCC is installed on the engineering PC.
- A WinCC RT object had been inserted in the PC station.

#### Procedure

In order to create a visualization project for EC31-HMI/RTX, follow these steps:

1. Open the device view of the PC station of the EC31‑HMI/RTX.
2. Select WinCC RT object.
3. Select the "Open object" command.

   WinCC is started.
4. Create and configure the necessary elements: Pictures, alarms, tags, etc., using the WinCC editors.
5. Save and test the visualization.
6. Transfer the project to the EC31-HMI/RTX target system.

### Downloading the configuration data to the target system

#### Download options

You can download the following configuration data from STEP 7 to the embedded controller:

- The entire PC station (including, for example, IE General)
- Only the configuration data of the WinLC RTX / WinLC RTX F
- Only the S7 program of the WinLC RTX / WinLC RTX F

For an EC31-HMI/RTX, you will need to transfer the configuration data from WinCC.

#### Requirement

- The enhanced write filter (EWF) must be deactivated on the Embedded Controller if the entire PC station is to be downloaded.
- The embedded controller is connected to the programming device / PC via Industrial Ethernet. The PG/PC interface must be set to TCP/IP.
- **EC31-HMI/RTX only:** The visualization project has been created in WinCC.
- Before the following functions become available, the embedded controller must be connected to the engineering system via a port of the X1 PN LAN interface:

  - Assign PROFINET IO device names
  - PROFINET CBA: Interconnection download and online functions

#### Procedure

1. Deactivate EWF on the EC31-RTX / EC31-RTX F / EC31-HMI/RTX (if not already deactivated). After EWF has been deactivated, turn off and restart the embedded controller.
2. Start WinLC.
3. Activate the PC station in the Station Configuration Editor ("Enable station" button).
4. Change the embedded controller to STOP mode.
5. Download the hardware configuration, the S7 program and the configuration data to the target system.

#### Making ready for operation

To make the EC31-RTX / EC31-HMI/RTX ready for operation, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Set the enhanced write filter for drive C:\ to the "activated" state.      | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Flash memory failure** If you leave the enhanced write filter in "deactivated" state, you risk an early failure of your flash memory due to the persistent write access of the operating system. When the enhanced write filter is activated, the number of write accesses to the operating system partition is minimized, thereby increasing the life of the flash memory. |  | 2. Record all special settings (such as changes to the IP addresses) made in the course of application development. Store them along with your project. 3. Create a backup copy of your settings. |  |

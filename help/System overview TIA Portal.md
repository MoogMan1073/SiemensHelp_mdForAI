---
title: "System overview TIA Portal"
package: PEProdOverviewenUS
topics: 8
source: Siemens TIA Portal Information System (offline help, en-US)
---


# System overview TIA Portal

This section contains information on the following topics:

- [Scaling of products in TIA Portal](#scaling-of-products-in-tia-portal)
- [Cross-product engineering options](#cross-product-engineering-options)
- [Options for S7-1500 Runtime](#options-for-s7-1500-runtime)
- [Options for STEP 7 Engineering System](#options-for-step-7-engineering-system)
- [Options for WinCC Engineering and Runtime systems](#options-for-wincc-engineering-and-runtime-systems)
- [Options for WinCC Unified](#options-for-wincc-unified)
- [Options for Startdrive](#options-for-startdrive)

## Scaling of products in TIA Portal

### Scope of performance of the products

The following graphic shows the scope of services offered by the individual products in TIA Portal:

![Scope of performance of the products](images/157555226507_DV_resource.Stream@PNG-en-US.png)

### SIMATIC STEP 7

SIMATIC STEP 7 (TIA Portal) is the engineering software for configuring the SIMATIC controller families S7-1200, S7-1500, S7-300/400 and software controllers (WinAC). STEP 7 (TIA Portal) is available in two editions, depending on the configurable controller families:

- STEP 7 Basic for configuring the S7-1200
- STEP 7 Professional for configuring S7-1200, S7-1500, S7-300/400 and Software-Controller (WinAC)

### SIMATIC WinCC

SIMATIC WinCC (TIA Portal) is engineering software for configuring SIMATIC Panels, SIMATIC Industrial PCs, and Standard PCs with the WinCC Runtime Advanced or the SCADA System WinCC Runtime Professional visualization software.

WinCC (TIA Portal) is available in the following editions, depending on the configurable operator control systems:

- WinCC Basic for configuring Basic Panels

  WinCC Basic is included with every STEP 7 Basic and STEP 7 Professional product.
- WinCC Comfort for configuring all panels (including Comfort Panels, Mobile Panels)
- WinCC Advanced for configuring all panels and PCs with the WinCC Runtime Advanced visualization software

  WinCC Runtime Advanced is a visualization software for PC-based single-station systems. WinCC Runtime Advanced can be purchased with licenses for 128, 512, 2k, 4k, 8k and 16k PowerTags (tags with a process interface).
- WinCC Professional for configuring panels and PCs with WinCC Runtime Advanced or SCADA System WinCC Runtime Professional. WinCC Professional is available in the following editions: WinCC Professional for 512 and 4096 PowerTags as well as "WinCC Professional max. PowerTags".

  WinCC Runtime Professional is a SCADA system for structuring a configuration ranging from single-station systems to multi-station systems including standard clients or web clients. WinCC Runtime Professional can be purchased with licenses for 128, 512, 2k, 4k, 8k, 64k, 100k, 150k and 256k PowerTags (tags with a process interface).

### SIMATIC WinCC Unified

SIMATIC WinCC Unified is the modern visualization system that brings visualization functions to a variety of platforms. WinCC Unified projects are configured uniformly in the TIA Portal. The support of web technologies such as HTML5, SVG and JavaScript enables easy access to visualization functions via a web browser. Installation of additional applications or plug-ins is not necessary. WinCC Unified is flexibly scalable, from operator panels directly at the machine to complex PC-based solutions.

WinCC Unified is available in the following versions:

- WinCC Unified Comfort for visualization on Unified Comfort Panels
- WinCC Unified PC for visualization on Unified PCs

### SINAMICS Startdrive

SINAMICS Startdrive is the commissioning software for integrating SINAMICS drives into automation.

SINAMICS Startdrive is available in two versions:

- Startdrive Basic for commissioning, optimization and diagnostics of the SINAMICS S120, S150, S210 drive systems as well as G115D, G120, G120C, G120D, G130, G150
- Startdrive Advanced with all functions of SINAMICS Startdrive Basic and additionally integrated safety acceptance tests for SINAMICS S120, S210, G125D and G120

### SIMOTION SCOUT TIA

SIMOTION SCOUT TIA is the engineering software for programming, parameter assignment, configuration, testing and commissioning of the motion control systems SIMOTION D (drive-based), SIMOTION C (PLC-based), SIMOTION P (PC-based).

### SIRIUS SIMOCODE ES

SIRIUS SIMOCODE ES is the central software for configuration, commissioning, operation and diagnostics of SIMOCODE pro motor management and controlgear.

SIRIUS SIMOCODE ES is available in two versions:

- SIMOCODE ES Basic for commissioning and maintenance of devices
- SIMOCODE ES Professional with extended range of functions and integrated graphics editor for engineering and configuration tasks such as parameter assignment and diagnostics via PROFIBUS / PROFINET

## Cross-product engineering options

The following cross-product engineering options are available for products in TIA Portal:

- TIA Portal Multiuser (multiple users work jointly on a TIA Portal project)
- TIA Portal Test Suite Advanced (style guide checker and application test)
- TIA Portal Cloud Connector (access to local interface using RDP)
- TIA Portal Teamcenter Gateway (connection to Teamcenter)
- TIA User Management Component (UMAC) (User management)
- SIMATIC Visualization Architect (SiVArc) (Creation of HMI content based on STEP 7 projects)
- SIMATIC Energy Suite (Energy management) / S7 EE Monitor (energy efficiency monitor)
- SIMATIC Safe Kinematics (Safe zones and velocity monitoring of kinematics motions)

## Options for S7-1500 Runtime

The engineering of the following functions is integrated in the Engineering packages of SIMATIC STEP 7 Professional or SIMATIC Energy Suite. The activation takes place in the CPU context:

- SIMATIC OPC UA S7-1500 (connection of any third-party devices to the S7-1500)
- SIMATIC ProDiag (machinery and plant diagnostics for S7-1500 and SIMATIC HMI)
- SIMATIC Energy Suite S7-1500 (energy management)
- SIMATIC Modular Application Creator (generation of executable software modules for the TIA Portal)

## Options for STEP 7 Engineering System

The following options are available for STEP 7 Engineering:

- SIMATIC STEP 7 Safety Basic/Advanced (safety programs for F-CPUs)
- SIMATIC S7 PLCSIM Advanced (Virtual Controller S7-1500)
- SIMATIC Target™ for Simulink® (add-on for Simulink®)
- SIMATIC ODK 1500S (C/C++ programming for S7-1500 Software Controller and CPU 1518(F) ODK/MFP)
- SIMATIC STEP 7 Continuous Function Chart (CFC) (Configuration of CFCs)
- SIMATIC Robot Library (Robot library)

## Options for WinCC Engineering and Runtime systems

SIMATIC Panels as well as WinCC Runtime Advanced and WinCC Runtime Professional contain all essential functions for operator control and monitoring of machines or plants. Additional options allow you to extend the functionality in some cases to increase the range of available tasks.

### Options for Comfort Panels, Mobile Panels

The following extension options are available for Comfort Panels and Mobile Panels:

- WinCC Audit (audit trail and electronic signature for regulated applications)
- SIMATIC ProDiag (machinery and plant diagnostics for S7-1500 and SIMATIC HMI)

### Options for WinCC Runtime Advanced

The following possible extensions are available for WinCC Runtime Advanced:

- WinCC SmartServer (remote operation)
- WinCC Recipes (recipe system)
- WinCC Logging (logging of process values and alarms)
- WinCC Audit (audit trail for regulated applications)
- SIMATIC ProDiag (machinery and plant diagnostics for S7-1500 and SIMATIC HMI)

> **Note**
>
> In contrast to WinCC flexible 2008, functions from the WinCC flexible /Sm@rtService, WinCC flexible /Sm@rtAccess options as well as the WinCC flexible /OPC Server option are incorporated into the basic functionality.

### Options for WinCC Runtime Professional

The following possible extensions are available for WinCC Runtime Professional:

- WinCC Client (standard client for structuring multi-station systems)
- WinCC Server (supplements WinCC Runtime to include server functionality)
- WinCC Recipes (recipe system, formerly WinCC / UserArchives)
- WinCC WebNavigator (Web-based operator control and monitoring)
- WinCC DataMonitor (display and evaluation of process states and historical data)
- WebUX (platform and browser-independent operation and monitoring via the Web)
- SIMATIC Information Server 2014 (Web-based and browser-independent analysis and reports of historic process data)
- SIMATIC Process Historian 2014 (plant-wide archive server for messages and process data)
- Industrial Data Bridge (configurable connections to databases and IT systems)
- Redundancy (increased availability due to redundant server)
- SIMATIC ProDiag (machinery and plant diagnostics for S7-1500 and SIMATIC HMI)

> **Note**
>
> In contrast to WinCC V7, functions from the WinCC /OPC-Server and WinCC /ConnectivityPack options are incorporated into the basic functionality. Likewise, the basic functionality includes the Runtime API from WinCC /ODK.

## Options for WinCC Unified

SIMATIC WinCC Panel and PC systems include all essential functions for operator control and monitoring of machines or plants.

Additional options allow you to extend the functionality in some cases to increase the range of available tasks.

### Options for WinCC Unified Comfort and PC

The following extension options are available for WinCC Unified Comfort and PC:

- WinCC Unified Collaboration (Setup of distributed configurations)
- WinCC Unified Clients "Operate" (Additional operating clients for flexible web-based remote control)
- WinCC Unified Clients "Monitor" (Additional viewer clients for flexible web-based remote monitoring)
- WinCC Unified Audit Basis (Documentation and validation according to legal requirements)
- WinCC Unified ProDiag (machinery and plant diagnostics for S7-1500 and SIMATIC HMI)

### Options for WinCC Unified PC

The following extension options are available for WinCC Unified PC:

- WinCC Unified Logging (Local data collection for small to medium applications; already included for Unified Comfort Panel)
- WinCC Unified Parameter Control (Unified management and control of machine or production parameters; already included for Unified Comfort Panel)
- WinCC Unified Database Storage (Extensive, high-performance, long-term archiving)

## Options for Startdrive

The following option is available for SINAMICS Startdrive:

- SINAMICS Drive Control Chart (DCC) (Configuration of control functions)
